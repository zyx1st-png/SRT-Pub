#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import math
from dataclasses import asdict, dataclass
from pathlib import Path

from faster_whisper import WhisperModel


@dataclass(frozen=True)
class Segment:
    index: int
    start: float
    end: float
    text: str
    words: list[dict[str, float | str]] | None = None


def format_timestamp(seconds: float) -> str:
    milliseconds = max(0, int(round(seconds * 1000)))
    hours, rem = divmod(milliseconds, 3_600_000)
    minutes, rem = divmod(rem, 60_000)
    secs, millis = divmod(rem, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{millis:03d}"


def build_srt(segments: list[Segment]) -> str:
    lines: list[str] = []
    for segment in segments:
        text = " ".join(segment.text.split())
        lines.append(str(segment.index))
        lines.append(f"{format_timestamp(segment.start)} --> {format_timestamp(segment.end)}")
        lines.append(text)
        lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Transcribe a video/audio file with faster-whisper.")
    parser.add_argument("--input", type=Path, required=True, help="Input media file.")
    parser.add_argument("--output-dir", type=Path, required=True, help="Directory for outputs.")
    parser.add_argument("--output-prefix", default=None, help="Output filename prefix.")
    parser.add_argument("--model", default="small", help="Whisper model name.")
    parser.add_argument("--device", default="cpu", help="Inference device.")
    parser.add_argument("--compute-type", default="int8", help="Compute type.")
    parser.add_argument("--language", default="en", help="Language code.")
    parser.add_argument("--beam-size", type=int, default=5, help="Beam size.")
    parser.add_argument("--vad-filter", action="store_true", help="Enable VAD filtering.")
    parser.add_argument("--word-timestamps", action="store_true", help="Include word timestamps in JSON.")
    args = parser.parse_args()

    args.output_dir.mkdir(parents=True, exist_ok=True)
    prefix = args.output_prefix or args.input.stem

    model = WhisperModel(args.model, device=args.device, compute_type=args.compute_type)
    segments_iter, info = model.transcribe(
        str(args.input),
        language=args.language,
        beam_size=args.beam_size,
        vad_filter=args.vad_filter,
        word_timestamps=args.word_timestamps,
    )

    segments: list[Segment] = []
    for idx, segment in enumerate(segments_iter, start=1):
        words = None
        if args.word_timestamps and segment.words:
            words = [
                {
                    "word": word.word,
                    "start": word.start,
                    "end": word.end,
                    "probability": word.probability,
                }
                for word in segment.words
            ]
        segments.append(
            Segment(
                index=idx,
                start=float(segment.start),
                end=float(segment.end),
                text=segment.text.strip(),
                words=words,
            )
        )
        print(f"[{idx:03d}] {segment.start:7.2f}-{segment.end:7.2f} {segment.text.strip()}")

    srt_path = args.output_dir / f"{prefix}.srt"
    txt_path = args.output_dir / f"{prefix}.txt"
    json_path = args.output_dir / f"{prefix}.json"

    srt_path.write_text(build_srt(segments), encoding="utf-8")
    txt_path.write_text("\n".join(seg.text for seg in segments).strip() + "\n", encoding="utf-8")
    json_path.write_text(
        json.dumps(
            {
                "input": str(args.input),
                "language": info.language,
                "language_probability": info.language_probability,
                "duration": info.duration,
                "segments": [asdict(seg) for seg in segments],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )

    print(f"wrote {srt_path}")
    print(f"wrote {txt_path}")
    print(f"wrote {json_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
