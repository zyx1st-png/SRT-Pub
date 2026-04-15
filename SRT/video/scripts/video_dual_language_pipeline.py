#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

from _shared_paths import BRANDING_OUT_DIR, PIPELINE_OUT_DIR


SCRIPT_DIR = Path(__file__).resolve().parent
TRANSCRIBE_SCRIPT = SCRIPT_DIR / "transcribe_video_fw.py"
TRANSLATE_SCRIPT = SCRIPT_DIR / "translate_subtitles.py"
CLEAN_SCRIPT = SCRIPT_DIR / "finalize_en_intro_outro_clean.py"
ALIGN_SCRIPT = SCRIPT_DIR / "align_dub.py"
BURN_SCRIPT = SCRIPT_DIR / "burn_bilingual_subs.py"

TIME_RE = re.compile(
    r"(?P<sh>\d\d):(?P<sm>\d\d):(?P<ss>\d\d),(?P<sms>\d\d\d)\s+-->\s+"
    r"(?P<eh>\d\d):(?P<em>\d\d):(?P<es>\d\d),(?P<ems>\d\d\d)"
)


@dataclass(frozen=True)
class SrtCue:
    index: int
    start_ms: int
    end_ms: int
    header: str
    body: list[str]


def ffmpeg_path(name: str) -> Path:
    brew = Path("/opt/homebrew/bin") / name
    return brew if brew.exists() else Path(name)


def run_step(label: str, cmd: list[str]) -> None:
    print(f"\n==> {label}")
    subprocess.run(cmd, check=True)


def probe_duration_seconds(path: Path) -> float:
    ffprobe = ffmpeg_path("ffprobe")
    result = subprocess.run(
        [
            str(ffprobe),
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "default=nw=1:nk=1",
            str(path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    return float(result.stdout.strip())


def parse_timestamp(token: str) -> int:
    match = TIME_RE.match(token)
    if not match:
        raise ValueError(f"Invalid SRT timecode: {token!r}")
    start = (
        int(match.group("sh")) * 3_600_000
        + int(match.group("sm")) * 60_000
        + int(match.group("ss")) * 1_000
        + int(match.group("sms"))
    )
    return start


def format_timestamp(ms: int) -> str:
    ms = max(0, ms)
    hours, rem = divmod(ms, 3_600_000)
    minutes, rem = divmod(rem, 60_000)
    seconds, millis = divmod(rem, 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{millis:03d}"


def parse_srt(path: Path) -> list[SrtCue]:
    raw = path.read_text(encoding="utf-8").strip()
    cues: list[SrtCue] = []
    for chunk in re.split(r"\n\s*\n", raw):
        lines = [line.rstrip("\r") for line in chunk.splitlines() if line.strip()]
        if len(lines) < 3:
            continue
        times = lines[1].strip()
        start_text, end_text = [part.strip() for part in times.split("-->")]
        cues.append(
            SrtCue(
                index=int(lines[0].strip()),
                start_ms=parse_timestamp(start_text),
                end_ms=parse_timestamp(end_text),
                header=times,
                body=lines[2:],
            )
        )
    cues.sort(key=lambda cue: cue.index)
    return cues


def write_shifted_srt(source: Path, output: Path, shift_ms: int) -> None:
    cues = parse_srt(source)
    lines: list[str] = []
    for cue in cues:
        lines.append(str(cue.index))
        lines.append(
            f"{format_timestamp(cue.start_ms + shift_ms)} --> "
            f"{format_timestamp(cue.end_ms + shift_ms)}"
        )
        lines.extend(cue.body)
        lines.append("")
    output.write_text("\n".join(lines), encoding="utf-8")


def concat_clips(clips: list[Path], output: Path, target_width: int = 1920, target_height: int = 1080) -> None:
    ffmpeg = ffmpeg_path("ffmpeg")
    filter_parts: list[str] = []
    concat_inputs: list[str] = []
    for index, _clip in enumerate(clips):
        filter_parts.append(
            f"[{index}:v]scale={target_width}:{target_height}:flags=lanczos,setsar=1[v{index}]"
        )
        filter_parts.append(f"[{index}:a]aformat=sample_rates=48000:channel_layouts=stereo[a{index}]")
        concat_inputs.append(f"[v{index}][a{index}]")
    filter_parts.append("".join(concat_inputs) + f"concat=n={len(clips)}:v=1:a=1[v][a]")
    filter_complex = ";".join(filter_parts)

    subprocess.run(
        [
            str(ffmpeg),
            "-y",
            *sum((["-i", str(clip)] for clip in clips), []),
            "-filter_complex",
            filter_complex,
            "-map",
            "[v]",
            "-map",
            "[a]",
            "-c:v",
            "libx264",
            "-preset",
            "medium",
            "-crf",
            "16",
            "-pix_fmt",
            "yuv420p",
            "-c:a",
            "aac",
            "-b:a",
            "192k",
            "-movflags",
            "+faststart",
            str(output),
        ],
        check=True,
    )


def extract_mp3(source: Path, output: Path) -> None:
    ffmpeg = ffmpeg_path("ffmpeg")
    subprocess.run(
        [
            str(ffmpeg),
            "-y",
            "-i",
            str(source),
            "-vn",
            "-c:a",
            "libmp3lame",
            "-b:a",
            "192k",
            str(output),
        ],
        check=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser(
        description="One-click pipeline for a dual-language video package."
    )
    parser.add_argument("--video", type=Path, required=True, help="Source video.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=PIPELINE_OUT_DIR,
        help="Directory for all outputs.",
    )
    parser.add_argument(
        "--chinese-srt",
        type=Path,
        default=None,
        help="Manual Chinese subtitle file aligned to the source video. If omitted, Chinese subtitles are generated automatically.",
    )
    parser.add_argument(
        "--intro-cn",
        type=Path,
        default=BRANDING_OUT_DIR / "intro_cn.mp4",
        help="Chinese intro clip.",
    )
    parser.add_argument(
        "--outro-cn",
        type=Path,
        default=BRANDING_OUT_DIR / "outro.mp4",
        help="Chinese outro clip.",
    )
    parser.add_argument(
        "--intro-en",
        type=Path,
        default=BRANDING_OUT_DIR / "intro.mp4",
        help="English intro clip.",
    )
    parser.add_argument(
        "--outro-en",
        type=Path,
        default=BRANDING_OUT_DIR / "outro_en.mp4",
        help="English outro clip.",
    )
    parser.add_argument("--voice", default="Grandpa (中文（中国大陆）)", help="Chinese TTS voice.")
    parser.add_argument(
        "--tts-backend",
        choices=("say", "edge"),
        default="say",
        help="TTS backend for Chinese dubbing.",
    )
    parser.add_argument("--font-size", type=int, default=28, help="Subtitle font size.")
    parser.add_argument(
        "--translate-model",
        default=None,
        help="Optional translation model override for automatic subtitle translation.",
    )
    parser.add_argument(
        "--translate-base-url",
        default=None,
        help="Optional OpenAI-compatible base URL override for automatic subtitle translation.",
    )
    parser.add_argument(
        "--translate-api-key-env",
        default=None,
        help="Optional environment variable name containing the translation API key.",
    )
    parser.add_argument("--english-model", default="small", help="Whisper model for English transcription.")
    parser.add_argument("--english-device", default="cpu", help="Device for Whisper transcription.")
    parser.add_argument(
        "--english-compute-type",
        default="int8",
        help="Compute type for Whisper transcription.",
    )
    parser.add_argument("--force", action="store_true", help="Rebuild existing outputs.")
    args = parser.parse_args()

    if not TRANSCRIBE_SCRIPT.exists():
        raise SystemExit(f"Missing script: {TRANSCRIBE_SCRIPT}")
    if not TRANSLATE_SCRIPT.exists():
        raise SystemExit(f"Missing script: {TRANSLATE_SCRIPT}")
    if not CLEAN_SCRIPT.exists():
        raise SystemExit(f"Missing script: {CLEAN_SCRIPT}")
    if not ALIGN_SCRIPT.exists():
        raise SystemExit(f"Missing script: {ALIGN_SCRIPT}")
    if not BURN_SCRIPT.exists():
        raise SystemExit(f"Missing script: {BURN_SCRIPT}")

    if not args.video.exists():
        raise SystemExit(f"Source video not found: {args.video}")
    if args.chinese_srt is not None and not args.chinese_srt.exists():
        raise SystemExit(f"Chinese SRT not found: {args.chinese_srt}")
    for clip in (args.intro_cn, args.outro_cn, args.intro_en, args.outro_en):
        if not clip.exists():
            raise SystemExit(f"Missing intro/outro clip: {clip}")

    args.output_dir.mkdir(parents=True, exist_ok=True)
    stem = args.video.stem
    work_dir = args.output_dir / f"{stem}.work"
    work_dir.mkdir(parents=True, exist_ok=True)

    english_srt = work_dir / f"{stem}.en.srt"
    english_json = work_dir / f"{stem}.en.json"
    chinese_contextual = work_dir / f"{stem}.en.zh.contextual.srt"
    chinese_polished = work_dir / f"{stem}.en.zh.polished.srt"
    chinese_spoken = work_dir / f"{stem}.en.zh.spoken.srt"
    clean_main = work_dir / f"{stem}.clean_main.mp4"
    english_final = args.output_dir / f"{stem}.en.final.mp4"
    english_final_srt = args.output_dir / f"{stem}.en.final.srt"
    english_final_mp3 = args.output_dir / f"{stem}.en.final.mp3"
    chinese_dubbed = work_dir / f"{stem}.zh.dubbed.mp4"
    chinese_subbed = work_dir / f"{stem}.zh.dubbed.cnonly.mp4"
    chinese_final = args.output_dir / f"{stem}.zh.final.mp4"
    chinese_final_srt = args.output_dir / f"{stem}.zh.final.srt"
    chinese_final_mp3 = args.output_dir / f"{stem}.zh.final.mp3"

    print(f"Output directory: {args.output_dir}")
    print(f"Work directory: {work_dir}")

    if args.force or not english_srt.exists():
        run_step(
            "Transcribe English",
            [
                sys.executable,
                str(TRANSCRIBE_SCRIPT),
                "--input",
                str(args.video),
                "--output-dir",
                str(work_dir),
                "--output-prefix",
                f"{stem}.en",
                "--model",
                args.english_model,
                "--device",
                args.english_device,
                "--compute-type",
                args.english_compute_type,
                "--language",
                "en",
                "--beam-size",
                "5",
                "--word-timestamps",
            ],
        )
    elif english_json.exists():
        print(f"Reusing existing English transcript: {english_srt}")

    auto_generated_chinese = args.chinese_srt is None
    chosen_chinese_srt = args.chinese_srt
    if auto_generated_chinese:
        if args.force or not chinese_spoken.exists():
            translate_cmd = [
                sys.executable,
                str(TRANSLATE_SCRIPT),
                "--input-srt",
                str(english_srt),
                "--output-dir",
                str(work_dir),
                "--output-prefix",
                f"{stem}.en",
            ]
            if args.translate_model:
                translate_cmd.extend(["--model", args.translate_model])
            if args.translate_base_url:
                translate_cmd.extend(["--base-url", args.translate_base_url])
            if args.translate_api_key_env:
                translate_cmd.extend(["--api-key-env", args.translate_api_key_env])
            run_step("Translate Chinese subtitles", translate_cmd)
        else:
            print(f"Reusing generated Chinese subtitles: {chinese_spoken}")
        chosen_chinese_srt = chinese_spoken

    assert chosen_chinese_srt is not None

    if args.force or not clean_main.exists():
        run_step(
            "Clean main video",
            [
                sys.executable,
                str(CLEAN_SCRIPT),
                "--main-video",
                str(args.video),
                "--output",
                str(clean_main),
                "--no-concat",
            ],
        )
    else:
        print(f"Reusing cleaned main video: {clean_main}")

    intro_en_seconds = probe_duration_seconds(args.intro_en)
    intro_cn_seconds = probe_duration_seconds(args.intro_cn)

    if args.force or not english_final.exists():
        print("Building English final video...")
        concat_clips([args.intro_en, clean_main, args.outro_en], english_final)
    else:
        print(f"Reusing English final video: {english_final}")

    write_shifted_srt(english_srt, english_final_srt, int(round(intro_en_seconds * 1000)))
    extract_mp3(english_final, english_final_mp3)

    if args.force or not chinese_dubbed.exists():
        run_step(
            "Generate Chinese dubbing",
            [
                sys.executable,
                str(ALIGN_SCRIPT),
                "--video",
                str(clean_main),
                "--srt",
                str(chosen_chinese_srt),
                "--voice",
                args.voice,
                "--tts-backend",
                args.tts_backend,
                "--output-prefix",
                f"{stem}.zh.dubbed",
            ],
        )
    else:
        print(f"Reusing Chinese dubbed video: {chinese_dubbed}")

    if args.force or not chinese_subbed.exists():
        run_step(
            "Burn Chinese subtitles",
            [
                sys.executable,
                str(BURN_SCRIPT),
                "--video",
                str(chinese_dubbed),
                "--chinese",
                str(chosen_chinese_srt),
                "--chinese-only",
                "--output-prefix",
                f"{stem}.zh.dubbed.cnonly",
                "--font-size",
                str(args.font_size),
            ],
        )
    else:
        print(f"Reusing Chinese subtitle video: {chinese_subbed}")

    if args.force or not chinese_final.exists():
        print("Building Chinese final video...")
        concat_clips([args.intro_cn, chinese_subbed, args.outro_cn], chinese_final)
    else:
        print(f"Reusing Chinese final video: {chinese_final}")

    write_shifted_srt(chosen_chinese_srt, chinese_final_srt, int(round(intro_cn_seconds * 1000)))
    extract_mp3(chinese_final, chinese_final_mp3)

    print("\nDone.")
    print(f"English video: {english_final}")
    print(f"English SRT:   {english_final_srt}")
    print(f"English MP3:   {english_final_mp3}")
    print(f"Chinese video: {chinese_final}")
    print(f"Chinese SRT:   {chinese_final_srt}")
    print(f"Chinese MP3:   {chinese_final_mp3}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
