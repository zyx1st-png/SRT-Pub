#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
import tempfile
from pathlib import Path

import cv2
import numpy as np

from _shared_paths import BRANDING_OUT_DIR, PIPELINE_OUT_DIR


def ffmpeg_path(name: str) -> Path:
    brew = Path("/opt/homebrew/bin") / name
    return brew if brew.exists() else Path(name)


def watermark_box(width: int, height: int) -> tuple[int, int, int, int]:
    # Keep the mask tight around the NotebookLM badge in the bottom-right corner.
    watermark_w = max(1, int(round(width * 0.115)))
    watermark_h = max(1, int(round(height * 0.052)))
    watermark_x = max(0, width - watermark_w)
    watermark_y = max(0, height - watermark_h)
    return watermark_x, watermark_y, watermark_w, watermark_h


def inpaint_watermark(frame: np.ndarray, width: int, height: int) -> np.ndarray:
    watermark_x, watermark_y, watermark_w, watermark_h = watermark_box(width, height)
    mask = np.zeros((height, width), dtype=np.uint8)
    mask[
        watermark_y : watermark_y + watermark_h,
        watermark_x : watermark_x + watermark_w,
    ] = 255
    return cv2.inpaint(frame, mask, 2, cv2.INPAINT_TELEA)


def render_clean_main_video(
    source_video: Path,
    output_video_only: Path,
    target_width: int = 1920,
    target_height: int = 1080,
    remove_watermark: bool = True,
) -> None:
    cap = cv2.VideoCapture(str(source_video))
    if not cap.isOpened():
        raise RuntimeError(f"Unable to open video: {source_video}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)

    ffmpeg = ffmpeg_path("ffmpeg")
    writer = subprocess.Popen(
        [
            str(ffmpeg),
            "-y",
            "-f",
            "rawvideo",
            "-pix_fmt",
            "bgr24",
            "-s",
            f"{target_width}x{target_height}",
            "-r",
            f"{fps:.6f}",
            "-i",
            "pipe:0",
            "-an",
            "-c:v",
            "libx264",
            "-preset",
            "medium",
            "-crf",
            "16",
            "-pix_fmt",
            "yuv420p",
            str(output_video_only),
        ],
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    frame_idx = 0
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            if (frame.shape[1], frame.shape[0]) != (target_width, target_height):
                frame = cv2.resize(frame, (target_width, target_height), interpolation=cv2.INTER_LANCZOS4)

            if remove_watermark:
                frame = inpaint_watermark(frame, target_width, target_height)

            if writer.stdin is None:
                raise RuntimeError("ffmpeg stdin closed unexpectedly")
            writer.stdin.write(frame.tobytes())
            frame_idx += 1
            if frame_idx % 1500 == 0:
                print(f"rendered {frame_idx}/{frame_count or '?'} frames")
    finally:
        cap.release()
        if writer.stdin is not None:
            writer.stdin.close()

    stderr = writer.stderr.read().decode("utf-8", errors="replace") if writer.stderr else ""
    ret = writer.wait()
    if ret != 0:
        raise RuntimeError(f"ffmpeg video render failed:\n{stderr}")


def mux_audio(video_only: Path, audio_source: Path, output: Path) -> None:
    ffmpeg = ffmpeg_path("ffmpeg")
    subprocess.run(
        [
            str(ffmpeg),
            "-y",
            "-i",
            str(video_only),
            "-i",
            str(audio_source),
            "-map",
            "0:v:0",
            "-map",
            "1:a:0",
            "-c:v",
            "copy",
            "-c:a",
            "copy",
            "-movflags",
            "+faststart",
            str(output),
        ],
        check=True,
        capture_output=True,
        text=True,
    )


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
        capture_output=True,
        text=True,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Clean a video and optionally add intro/outro clips.")
    parser.add_argument(
        "--main-video",
        type=Path,
        required=True,
        help="Source English main video.",
    )
    parser.add_argument(
        "--intro",
        type=Path,
        default=BRANDING_OUT_DIR / "intro.mp4",
        help="English intro clip.",
    )
    parser.add_argument(
        "--outro",
        type=Path,
        default=BRANDING_OUT_DIR / "outro_en.mp4",
        help="English outro clip.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=PIPELINE_OUT_DIR / "english.clean.final.mp4",
        help="Final cleaned English output.",
    )
    parser.add_argument(
        "--no-concat",
        action="store_true",
        help="Only render the cleaned main video, without intro/outro clips.",
    )
    args = parser.parse_args()

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="en_final_", dir=str(args.output.parent)) as tmp_dir_name:
        tmp_dir = Path(tmp_dir_name)
        main_video_only = tmp_dir / "main_clean.mp4"
        main_with_audio = tmp_dir / "main_clean_with_audio.mp4"

        render_clean_main_video(
            source_video=args.main_video,
            output_video_only=main_video_only,
            target_width=1920,
            target_height=1080,
            remove_watermark=True,
        )
        mux_audio(
            video_only=main_video_only,
            audio_source=args.main_video,
            output=main_with_audio,
        )
        if args.no_concat:
            main_with_audio.replace(args.output)
            print(f"wrote {args.output}")
            return 0
        concat_clips(
            clips=[args.intro, main_with_audio, args.outro],
            output=args.output,
        )

    print(f"wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
