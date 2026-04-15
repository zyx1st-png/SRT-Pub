#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request
from dataclasses import dataclass
from pathlib import Path


TIME_RE = re.compile(
    r"(?P<sh>\d\d):(?P<sm>\d\d):(?P<ss>\d\d),(?P<sms>\d\d\d)\s+-->\s+"
    r"(?P<eh>\d\d):(?P<em>\d\d):(?P<es>\d\d),(?P<ems>\d\d\d)"
)


@dataclass(frozen=True)
class Cue:
    index: int
    start: str
    end: str
    text: str


STAGE_PROMPTS: dict[str, str] = {
    "contextual": (
        "You are translating English video subtitles into simplified Chinese. "
        "Preserve meaning faithfully, preserve technical terms like L0/L1/L2 exactly, "
        "keep tone serious and precise, and do not add or remove claims. "
        "Return only JSON with a top-level key 'translations' whose value is a list of "
        "objects containing 'index' and 'text'."
    ),
    "polished": (
        "You are polishing simplified Chinese subtitles for clarity and rhetorical force. "
        "Do not change the argument, terminology, or factual content. "
        "Make the Chinese read naturally for an educated audience while staying precise. "
        "Return only JSON with a top-level key 'translations' whose value is a list of "
        "objects containing 'index' and 'text'."
    ),
    "spoken": (
        "You are rewriting simplified Chinese subtitles into a spoken voiceover style. "
        "Keep the meaning intact, but make the language more oral, direct, and easy to speak aloud. "
        "Use shorter clauses where helpful, avoid hype, preserve technical terms like L0/L1/L2, "
        "and do not add explanations that were not present. "
        "Return only JSON with a top-level key 'translations' whose value is a list of "
        "objects containing 'index' and 'text'."
    ),
}


def parse_srt(path: Path) -> list[Cue]:
    raw = path.read_text(encoding="utf-8").strip()
    cues: list[Cue] = []
    for chunk in re.split(r"\n\s*\n", raw):
        lines = [line.rstrip("\r") for line in chunk.splitlines() if line.strip()]
        if len(lines) < 3:
            continue
        match = TIME_RE.match(lines[1].strip())
        if not match:
            raise ValueError(f"Invalid timecode line in {path}: {lines[1]!r}")
        start, end = [part.strip() for part in lines[1].split(" --> ")]
        cues.append(
            Cue(
                index=int(lines[0].strip()),
                start=start,
                end=end,
                text="\n".join(lines[2:]).strip(),
            )
        )
    cues.sort(key=lambda cue: cue.index)
    return cues


def build_srt_like(reference: list[Cue], translated: list[str]) -> str:
    if len(reference) != len(translated):
        raise ValueError("Reference cues and translated text length do not match.")
    lines: list[str] = []
    for cue, text in zip(reference, translated, strict=True):
        lines.append(str(cue.index))
        lines.append(f"{cue.start} --> {cue.end}")
        lines.append(text.strip())
        lines.append("")
    return "\n".join(lines)


def normalize_base_url(value: str) -> str:
    value = value.rstrip("/")
    if value.endswith("/chat/completions"):
        return value[: -len("/chat/completions")]
    return value


def extract_json_blob(text: str) -> dict:
    stripped = text.strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```(?:json)?\s*", "", stripped)
        stripped = re.sub(r"\s*```$", "", stripped)
    try:
        return json.loads(stripped)
    except json.JSONDecodeError:
        pass

    start = stripped.find("{")
    end = stripped.rfind("}")
    if start == -1 or end == -1 or end <= start:
        raise ValueError("Model response did not contain a JSON object.")
    return json.loads(stripped[start : end + 1])


def chunk_cues(cues: list[Cue], max_items: int, max_chars: int) -> list[list[Cue]]:
    chunks: list[list[Cue]] = []
    current: list[Cue] = []
    current_chars = 0
    for cue in cues:
        cue_chars = len(cue.text)
        if current and (len(current) >= max_items or current_chars + cue_chars > max_chars):
            chunks.append(current)
            current = []
            current_chars = 0
        current.append(cue)
        current_chars += cue_chars
    if current:
        chunks.append(current)
    return chunks


def call_openai_compatible_chat(
    *,
    base_url: str,
    api_key: str,
    model: str,
    system_prompt: str,
    user_prompt: str,
    temperature: float,
    timeout: float,
) -> str:
    endpoint = normalize_base_url(base_url) + "/chat/completions"
    payload = {
        "model": model,
        "temperature": temperature,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    }
    request = urllib.request.Request(
        endpoint,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        data = json.loads(response.read().decode("utf-8"))
    return data["choices"][0]["message"]["content"]


def translate_chunk(
    *,
    cues: list[Cue],
    stage: str,
    model: str,
    base_url: str,
    api_key: str,
    temperature: float,
    timeout: float,
    max_retries: int,
) -> list[str]:
    if stage not in STAGE_PROMPTS:
        raise ValueError(f"Unsupported stage: {stage}")

    compact_payload = [{"index": cue.index, "text": cue.text} for cue in cues]
    user_prompt = (
        "Translate or rewrite the following subtitle cues.\n"
        "Keep every index exactly once and in the same order.\n"
        "Return JSON only.\n\n"
        f"{json.dumps({'translations': compact_payload}, ensure_ascii=False, indent=2)}"
    )

    last_error: Exception | None = None
    for attempt in range(1, max_retries + 1):
        try:
            raw = call_openai_compatible_chat(
                base_url=base_url,
                api_key=api_key,
                model=model,
                system_prompt=STAGE_PROMPTS[stage],
                user_prompt=user_prompt,
                temperature=temperature,
                timeout=timeout,
            )
            data = extract_json_blob(raw)
            translations = data["translations"]
            if len(translations) != len(cues):
                raise ValueError(
                    f"Expected {len(cues)} translations, got {len(translations)}."
                )
            texts: list[str] = []
            for expected_cue, item in zip(cues, translations, strict=True):
                if int(item["index"]) != expected_cue.index:
                    raise ValueError(
                        f"Index mismatch: expected {expected_cue.index}, got {item['index']}."
                    )
                text = str(item["text"]).strip()
                if not text:
                    raise ValueError(f"Empty translation returned for cue {expected_cue.index}.")
                texts.append(text)
            return texts
        except Exception as exc:  # noqa: BLE001
            last_error = exc
            if attempt == max_retries:
                break
            time.sleep(1.2 * attempt)
    assert last_error is not None
    raise last_error


def write_stage_output(
    *,
    stage: str,
    cues: list[Cue],
    translated_texts: list[str],
    output_prefix: str,
    output_dir: Path,
) -> Path:
    output_path = output_dir / f"{output_prefix}.zh.{stage}.srt"
    output_path.write_text(
        build_srt_like(cues, translated_texts) + "\n",
        encoding="utf-8",
    )
    return output_path


def lookup_api_key(explicit_env_name: str | None) -> str:
    env_names = [name for name in [explicit_env_name, "SRT_VIDEO_TRANSLATE_API_KEY", "OPENAI_API_KEY"] if name]
    for name in env_names:
        value = os.environ.get(name)
        if value:
            return value
    tried = ", ".join(env_names)
    raise SystemExit(f"No API key found. Set one of: {tried}")


def stage_transform(
    *,
    source_path: Path,
    source_cues: list[Cue],
    stage: str,
    model: str,
    base_url: str,
    api_key: str,
    max_items: int,
    max_chars: int,
    temperature: float,
    timeout: float,
    max_retries: int,
    output_prefix: str,
    output_dir: Path,
) -> tuple[Path, list[Cue]]:
    chunks = chunk_cues(source_cues, max_items=max_items, max_chars=max_chars)
    translated_texts: list[str] = []
    for chunk_index, chunk in enumerate(chunks, start=1):
        print(f"[{stage}] chunk {chunk_index}/{len(chunks)} ({len(chunk)} cues)")
        translated_texts.extend(
            translate_chunk(
                cues=chunk,
                stage=stage,
                model=model,
                base_url=base_url,
                api_key=api_key,
                temperature=temperature,
                timeout=timeout,
                max_retries=max_retries,
            )
        )
    output_path = write_stage_output(
        stage=stage,
        cues=source_cues,
        translated_texts=translated_texts,
        output_prefix=output_prefix,
        output_dir=output_dir,
    )
    return output_path, parse_srt(output_path)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Translate English subtitles into staged Chinese outputs (contextual, polished, spoken)."
    )
    parser.add_argument("--input-srt", type=Path, required=True, help="Source English SRT.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Output directory. Defaults to the input SRT directory.",
    )
    parser.add_argument(
        "--output-prefix",
        default=None,
        help="Output prefix. Defaults to the source SRT stem.",
    )
    parser.add_argument(
        "--stages",
        nargs="+",
        default=["contextual", "polished", "spoken"],
        choices=["contextual", "polished", "spoken"],
        help="Stages to run in order.",
    )
    parser.add_argument(
        "--model",
        default=os.environ.get("SRT_VIDEO_TRANSLATE_MODEL", "gpt-4.1-mini"),
        help="OpenAI-compatible model name.",
    )
    parser.add_argument(
        "--base-url",
        default=os.environ.get("SRT_VIDEO_TRANSLATE_BASE_URL", "https://api.openai.com/v1"),
        help="OpenAI-compatible API base URL.",
    )
    parser.add_argument(
        "--api-key-env",
        default=os.environ.get("SRT_VIDEO_TRANSLATE_API_KEY_ENV"),
        help="Optional environment variable name that stores the API key.",
    )
    parser.add_argument("--max-items", type=int, default=24, help="Max subtitle cues per chunk.")
    parser.add_argument("--max-chars", type=int, default=3600, help="Approx max source characters per chunk.")
    parser.add_argument("--temperature", type=float, default=0.2, help="Model temperature.")
    parser.add_argument("--timeout", type=float, default=180.0, help="Per-request timeout in seconds.")
    parser.add_argument("--max-retries", type=int, default=3, help="Max retries per chunk.")
    args = parser.parse_args()

    if not args.input_srt.exists():
        raise SystemExit(f"Input SRT not found: {args.input_srt}")

    output_dir = args.output_dir or args.input_srt.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    output_prefix = args.output_prefix or args.input_srt.stem
    api_key = lookup_api_key(args.api_key_env)

    current_path = args.input_srt
    current_cues = parse_srt(current_path)
    generated_paths: list[Path] = []

    for stage in args.stages:
        current_path, current_cues = stage_transform(
            source_path=current_path,
            source_cues=current_cues,
            stage=stage,
            model=args.model,
            base_url=args.base_url,
            api_key=api_key,
            max_items=args.max_items,
            max_chars=args.max_chars,
            temperature=args.temperature,
            timeout=args.timeout,
            max_retries=args.max_retries,
            output_prefix=output_prefix,
            output_dir=output_dir,
        )
        generated_paths.append(current_path)

    manifest = {
        "input_srt": str(args.input_srt),
        "model": args.model,
        "base_url": normalize_base_url(args.base_url),
        "stages": args.stages,
        "outputs": {path.name.split(".zh.", 1)[1].rsplit(".", 1)[0]: str(path) for path in generated_paths},
    }
    manifest_path = output_dir / f"{output_prefix}.zh.translation_manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    for path in generated_paths:
        print(f"wrote {path}")
    print(f"wrote {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
