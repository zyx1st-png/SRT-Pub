#!/usr/bin/env python3
from __future__ import annotations

import argparse
import math
import os
import re
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path

from pydub import AudioSegment

from timing_profiles import TIMING_HOLD_PROFILES, get_timing_holds


TIME_RE = re.compile(
    r"(?P<sh>\d\d):(?P<sm>\d\d):(?P<ss>\d\d),(?P<sms>\d\d\d)\s+-->\s+"
    r"(?P<eh>\d\d):(?P<em>\d\d):(?P<es>\d\d),(?P<ems>\d\d\d)"
)

PROXY_VARS = (
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "http_proxy",
    "https_proxy",
    "ALL_PROXY",
    "all_proxy",
    "NO_PROXY",
    "no_proxy",
)

@dataclass(frozen=True)
class Block:
    index: int
    start_ms: int
    end_ms: int
    text: str


def parse_timecode(value: str) -> int:
    match = TIME_RE.match(value)
    if not match:
        raise ValueError(f"Invalid timecode line: {value!r}")
    start = (
        int(match.group("sh")) * 3600
        + int(match.group("sm")) * 60
        + int(match.group("ss"))
    )
    start_ms = start * 1000 + int(match.group("sms"))
    end = (
        int(match.group("eh")) * 3600
        + int(match.group("em")) * 60
        + int(match.group("es"))
    )
    end_ms = end * 1000 + int(match.group("ems"))
    return start_ms, end_ms


def parse_srt(path: Path) -> list[Block]:
    raw = path.read_text(encoding="utf-8").strip()
    blocks: list[Block] = []
    for chunk in re.split(r"\n\s*\n", raw):
        lines = [line.rstrip("\r") for line in chunk.splitlines() if line.strip()]
        if len(lines) < 3:
            continue
        index = int(lines[0].strip())
        start_ms, end_ms = parse_timecode(lines[1].strip())
        text = re.sub(r"\s+", " ", " ".join(lines[2:])).strip()
        blocks.append(Block(index=index, start_ms=start_ms, end_ms=end_ms, text=text))
    blocks.sort(key=lambda item: item.index)
    return blocks


def clean_env() -> dict[str, str]:
    return os.environ.copy()


def ffmpeg_path(name: str) -> Path:
    path = Path("/opt/homebrew/bin") / name
    if path.exists():
        return path
    return Path(name)


def probe_duration_ms(video_path: Path) -> int:
    ffprobe = ffmpeg_path("ffprobe")
    cmd = [
        str(ffprobe),
        "-v",
        "error",
        "-show_entries",
        "format=duration",
        "-of",
        "default=nw=1:nk=1",
        str(video_path),
    ]
    result = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return int(round(float(result.stdout.strip()) * 1000))


def edge_tts_bin() -> Path:
    return Path(sys.executable).with_name("edge-tts")


def say_bin() -> Path:
    system_say = Path("/usr/bin/say")
    if system_say.exists():
        return system_say
    return Path("say")


def synthesize_tts(
    text: str,
    backend: str,
    voice: str,
    rate: str,
    out_path: Path,
    retries: int = 5,
) -> None:
    if backend == "edge":
        cmd = [
            str(edge_tts_bin()),
            "--text",
            text,
            "--voice",
            voice,
            "--rate",
            rate,
            "--write-media",
            str(out_path),
        ]
        proxy = (
            os.environ.get("EDGE_TTS_PROXY")
            or os.environ.get("WSS_PROXY")
            or os.environ.get("WS_PROXY")
            or os.environ.get("HTTPS_PROXY")
            or os.environ.get("HTTP_PROXY")
        )
        if proxy:
            cmd.extend(["--proxy", proxy])
        env = clean_env()
        last_error = None
        for attempt in range(1, retries + 1):
            try:
                subprocess.run(
                    cmd,
                    check=True,
                    env=env,
                    capture_output=True,
                    text=True,
                )
                return
            except subprocess.CalledProcessError as exc:
                last_error = exc
                if attempt < retries:
                    time.sleep(0.8 * attempt)
                    continue
                stderr = exc.stderr.strip() if exc.stderr else ""
                raise RuntimeError(
                    f"edge-tts failed for rate {rate} after {retries} tries: {stderr}"
                ) from exc
        if last_error is not None:
            raise last_error

    if backend == "say":
        cmd = [
            str(say_bin()),
            "-v",
            voice,
            "-r",
            rate,
            "-o",
            str(out_path),
            text,
        ]
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        return

    raise ValueError(f"Unknown TTS backend: {backend}")


def build_atempo_chain(factor: float) -> list[str]:
    filters: list[str] = []
    remaining = factor
    while remaining > 2.0:
        filters.append("atempo=2.0")
        remaining /= 2.0
    while remaining < 0.5:
        filters.append("atempo=0.5")
        remaining /= 0.5
    filters.append(f"atempo={remaining:.6f}")
    return filters


def speedup_audio(input_path: Path, output_path: Path, factor: float) -> None:
    ffmpeg = ffmpeg_path("ffmpeg")
    filters = build_atempo_chain(factor)
    cmd = [
        str(ffmpeg),
        "-y",
        "-i",
        str(input_path),
        "-filter:a",
        ",".join(filters),
        str(output_path),
    ]
    subprocess.run(cmd, check=True, capture_output=True, text=True)


def load_audio(path: Path) -> AudioSegment:
    segment = AudioSegment.from_file(path)
    return segment.set_channels(1)


def choose_clip_for_block(
    block: Block,
    next_start_ms: int,
    tmp_dir: Path,
    backend: str,
    voice: str,
    rate_candidates: list[str],
    safety_ms: int,
) -> tuple[AudioSegment, str, int, int]:
    allowed_ms = max(100, next_start_ms - block.start_ms - safety_ms)
    chosen_rate = rate_candidates[-1]
    chosen_clip: AudioSegment | None = None
    chosen_len = 0

    for rate in rate_candidates:
        suffix = "aiff" if backend == "say" else "mp3"
        media_path = tmp_dir / f"{block.index:04d}_{rate.replace('%', 'pct').replace('+', 'p').replace('-', 'm')}.{suffix}"
        synthesize_tts(block.text, backend=backend, voice=voice, rate=rate, out_path=media_path)
        clip = load_audio(media_path)
        clip_len = len(clip)
        if clip_len <= allowed_ms:
            chosen_rate = rate
            chosen_clip = clip
            chosen_len = clip_len
            break
        if chosen_clip is None or clip_len < chosen_len:
            chosen_rate = rate
            chosen_clip = clip
            chosen_len = clip_len

    assert chosen_clip is not None

    if chosen_len > allowed_ms:
        stretched = tmp_dir / f"{block.index:04d}_stretched.wav"
        factor = chosen_len / allowed_ms
        speedup_audio(
            input_path=tmp_dir / f"{block.index:04d}_{chosen_rate.replace('%', 'pct').replace('+', 'p').replace('-', 'm')}.{ 'aiff' if backend == 'say' else 'mp3'}",
            output_path=stretched,
            factor=factor,
        )
        chosen_clip = load_audio(stretched)
        chosen_len = len(chosen_clip)
        if chosen_len > allowed_ms:
            chosen_clip = chosen_clip[:allowed_ms]
            chosen_len = len(chosen_clip)

    return chosen_clip, chosen_rate, chosen_len, allowed_ms


def mux_video(video_path: Path, audio_path: Path, output_path: Path) -> None:
    ffmpeg = ffmpeg_path("ffmpeg")
    cmd = [
        str(ffmpeg),
        "-y",
        "-i",
        str(video_path),
        "-i",
        str(audio_path),
        "-map",
        "0:v:0",
        "-map",
        "1:a:0",
        "-c:v",
        "copy",
        "-c:a",
        "aac",
        "-b:a",
        "192k",
        "-movflags",
        "+faststart",
        str(output_path),
    ]
    subprocess.run(cmd, check=True, capture_output=True, text=True)


def main() -> int:
    parser = argparse.ArgumentParser(description="Timestamp-aligned dubbing for a video.")
    parser.add_argument(
        "--video",
        type=Path,
        required=True,
        help="Source video path.",
    )
    parser.add_argument(
        "--srt",
        type=Path,
        required=True,
        help="Subtitle file to dub.",
    )
    parser.add_argument(
        "--voice",
        default="Reed",
        help="TTS voice name.",
    )
    parser.add_argument(
        "--tts-backend",
        choices=("say", "edge"),
        default="say",
        help="TTS backend to use.",
    )
    parser.add_argument(
        "--output-prefix",
        default=None,
        help="Output file prefix inside the subtitle directory.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Optional output directory. Defaults to the subtitle directory.",
    )
    parser.add_argument(
        "--timing-profile",
        default="none",
        choices=("none", *tuple(TIMING_HOLD_PROFILES.keys())),
        help="Named timing-hold profile to make room for slower speech.",
    )
    args = parser.parse_args()

    blocks = parse_srt(args.srt)
    if not blocks:
        raise SystemExit(f"No subtitle blocks found in {args.srt}")

    homebrew_bin = "/opt/homebrew/bin"
    os.environ["PATH"] = f"{homebrew_bin}:{os.environ.get('PATH', '')}"
    AudioSegment.converter = str(ffmpeg_path("ffmpeg"))
    AudioSegment.ffprobe = str(ffmpeg_path("ffprobe"))

    video_ms = probe_duration_ms(args.video)
    out_dir = args.output_dir or args.srt.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    output_prefix = args.output_prefix or f"{args.video.stem}.dubbed"
    out_wav = out_dir / f"{output_prefix}.wav"
    out_mp4 = out_dir / f"{output_prefix}.mp4"
    log_path = out_dir / f"{output_prefix}.log"
    timing_holds_ms = get_timing_holds(args.timing_profile)
    total_hold_ms = sum(timing_holds_ms.values())
    timeline_ms = video_ms + total_hold_ms

    if args.tts_backend == "say":
        rate_candidates = ["200", "210", "220", "230", "240"]
    else:
        rate_candidates = ["+0%", "+5%", "+10%", "+15%", "+20%"]
    safety_ms = 80
    frame_rate = 24000

    log_lines: list[str] = []
    log_lines.append(f"video_ms={video_ms}")
    log_lines.append(f"timeline_ms={timeline_ms}")
    log_lines.append(f"subtitle_blocks={len(blocks)}")
    log_lines.append(f"voice={args.voice}")
    log_lines.append(f"timing_profile={args.timing_profile}")
    log_lines.append(f"rates={','.join(rate_candidates)}")
    log_lines.append(f"holds_ms={timing_holds_ms}")

    mix = AudioSegment.silent(duration=timeline_ms, frame_rate=frame_rate)

    with tempfile.TemporaryDirectory(prefix="aligned_dub_", dir=str(out_dir)) as tmp_name:
        tmp_dir = Path(tmp_name)
        shift_ms = 0
        for i, block in enumerate(blocks):
            hold_ms = timing_holds_ms.get(block.index, 0)
            block_start_ms = block.start_ms + shift_ms
            block_end_ms = block.end_ms + shift_ms
            next_start_ms = (
                blocks[i + 1].start_ms + shift_ms + hold_ms
                if i + 1 < len(blocks)
                else timeline_ms
            )
            clip, rate, clip_len, allowed_ms = choose_clip_for_block(
                block=Block(
                    index=block.index,
                    start_ms=block_start_ms,
                    end_ms=block_end_ms,
                    text=block.text,
                ),
                next_start_ms=next_start_ms,
                tmp_dir=tmp_dir,
                backend=args.tts_backend,
                voice=args.voice,
                rate_candidates=rate_candidates,
                safety_ms=safety_ms,
            )
            clip = clip.set_frame_rate(frame_rate).set_channels(1)
            mix = mix.overlay(clip, position=block_start_ms)
            log_lines.append(
                f"#{block.index:03d} start={block_start_ms} end={block_end_ms} next={next_start_ms} "
                f"hold={hold_ms} allowed={allowed_ms} clip={clip_len} rate={rate} text={block.text}"
            )
            print(
                f"[{block.index:03d}/{len(blocks)}] "
                f"rate={rate} clip={clip_len}ms allowed={allowed_ms}ms"
            )
            if hold_ms:
                shift_ms += hold_ms

    if len(mix) < timeline_ms:
        mix += AudioSegment.silent(duration=timeline_ms - len(mix), frame_rate=frame_rate)
    elif len(mix) > timeline_ms:
        mix = mix[:timeline_ms]

    mix = mix.set_frame_rate(48000).set_channels(1)
    mix.export(out_wav, format="wav")
    mux_video(args.video, out_wav, out_mp4)

    log_path.write_text("\n".join(log_lines) + "\n", encoding="utf-8")
    print(f"wrote {out_wav}")
    print(f"wrote {out_mp4}")
    print(f"wrote {log_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
