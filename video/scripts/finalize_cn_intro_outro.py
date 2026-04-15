#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
import subprocess
import tempfile
from dataclasses import dataclass
from pathlib import Path

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from _shared_paths import BRANDING_OUT_DIR, PIPELINE_OUT_DIR, default_font_path
from timing_profiles import TIMING_HOLD_PROFILES, get_timing_holds


TIME_RE = re.compile(
    r"(?P<sh>\d\d):(?P<sm>\d\d):(?P<ss>\d\d),(?P<sms>\d\d\d)\s+-->\s+"
    r"(?P<eh>\d\d):(?P<em>\d\d):(?P<es>\d\d),(?P<ems>\d\d\d)"
)


@dataclass(frozen=True)
class Cue:
    start_ms: int
    end_ms: int
    text: str


def ffmpeg_path(name: str) -> Path:
    brew = Path("/opt/homebrew/bin") / name
    return brew if brew.exists() else Path(name)


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
        start_ms = (
            int(match.group("sh")) * 3_600_000
            + int(match.group("sm")) * 60_000
            + int(match.group("ss")) * 1_000
            + int(match.group("sms"))
        )
        end_ms = (
            int(match.group("eh")) * 3_600_000
            + int(match.group("em")) * 60_000
            + int(match.group("es")) * 1_000
            + int(match.group("ems"))
        )
        cues.append(
            Cue(
                start_ms=start_ms,
                end_ms=end_ms,
                text=re.sub(r"\s+", " ", " ".join(lines[2:])).strip(),
            )
        )
    return cues


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\n", " ")).strip()


def stretch_cues(
    cues: list[Cue],
    timing_holds_ms: dict[int, int],
) -> tuple[list[Cue], list[tuple[int, int]]]:
    adjusted: list[Cue] = []
    freeze_windows: list[tuple[int, int]] = []
    shift_ms = 0

    for index, cue in enumerate(cues, start=1):
        hold_ms = timing_holds_ms.get(index, 0)
        start_ms = cue.start_ms + shift_ms
        end_ms = cue.end_ms + shift_ms + hold_ms
        adjusted.append(Cue(start_ms=start_ms, end_ms=end_ms, text=cue.text))
        if hold_ms:
            freeze_windows.append((end_ms - hold_ms, end_ms))
            shift_ms += hold_ms

    return adjusted, freeze_windows


def source_time_for_output_ms(output_ms: float, freeze_windows: list[tuple[int, int]]) -> float:
    completed_freeze_ms = 0
    for start_ms, end_ms in freeze_windows:
        if output_ms < start_ms:
            return output_ms - completed_freeze_ms
        if start_ms <= output_ms < end_ms:
            return start_ms - completed_freeze_ms
        completed_freeze_ms += end_ms - start_ms
    return output_ms - completed_freeze_ms


def text_bbox(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.FreeTypeFont, stroke_width: int) -> tuple[int, int]:
    bbox = draw.textbbox((0, 0), text, font=font, stroke_width=stroke_width)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def split_overwide_word(
    word: str,
    draw: ImageDraw.ImageDraw,
    font: ImageFont.FreeTypeFont,
    max_width: int,
    stroke_width: int,
) -> list[str]:
    parts: list[str] = []
    current = ""
    for ch in word:
        candidate = current + ch
        if current and text_bbox(draw, candidate, font, stroke_width)[0] > max_width:
            parts.append(current)
            current = ch
        else:
            current = candidate
    if current:
        parts.append(current)
    return parts


def wrap_text(
    text: str,
    draw: ImageDraw.ImageDraw,
    font: ImageFont.FreeTypeFont,
    max_width: int,
    stroke_width: int,
) -> list[str]:
    normalized = normalize_text(text)
    if not normalized:
        return []

    segments: list[tuple[str, bool]] = []
    words = normalized.split(" ")
    for word_index, word in enumerate(words):
        if not word:
            continue
        pieces = [word]
        if text_bbox(draw, word, font, stroke_width)[0] > max_width:
            pieces = split_overwide_word(word, draw, font, max_width, stroke_width)
        for piece_index, piece in enumerate(pieces):
            segments.append((piece, word_index > 0 and piece_index == 0))

    lines: list[str] = []
    current = ""
    for piece, add_space in segments:
        candidate = piece if not current else current + (" " if add_space else "") + piece
        if not current:
            current = piece
        elif text_bbox(draw, candidate, font, stroke_width)[0] <= max_width:
            current = candidate
        else:
            lines.append(current)
            current = piece
    if current:
        lines.append(current)
    return lines


def render_caption_overlay(
    text: str,
    frame_width: int,
    font_path: str,
    font_size: int = 36,
    max_text_width: int | None = None,
    supersample: int = 2,
) -> np.ndarray:
    max_text_width = max_text_width or frame_width - 320
    scale = max(1, supersample)
    font = ImageFont.truetype(font_path, font_size * scale)
    stroke_width = 4 * scale
    line_gap = 12 * scale
    shadow_offset = 3 * scale
    padding_x = 0
    padding_y = 0

    probe = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
    draw = ImageDraw.Draw(probe)
    lines = wrap_text(text, draw, font, max_text_width * scale, stroke_width)
    if not lines:
        return np.zeros((1, 1, 4), dtype=np.uint8)

    metrics: list[tuple[str, int, int]] = []
    for line in lines:
        w, h = text_bbox(draw, line, font, stroke_width)
        metrics.append((line, w, h))

    text_width = max(width for _, width, _ in metrics)
    text_height = sum(height for _, _, height in metrics) + line_gap * max(0, len(metrics) - 1)

    overlay = Image.new(
        "RGBA",
        (text_width + padding_x * 2 + shadow_offset * 2 + 8, text_height + padding_y * 2 + shadow_offset * 2 + 8),
        (0, 0, 0, 0),
    )
    draw_overlay = ImageDraw.Draw(overlay)
    y = padding_y + 2
    for line, width, height in metrics:
        x = padding_x + 4 + (text_width - width) // 2
        draw_overlay.text(
            (x + shadow_offset, y + shadow_offset),
            line,
            font=font,
            fill=(0, 0, 0, 170),
            stroke_width=0,
        )
        draw_overlay.text(
            (x, y),
            line,
            font=font,
            fill=(255, 255, 255, 255),
            stroke_width=stroke_width,
            stroke_fill=(0, 0, 0, 255),
        )
        y += height + line_gap

    if scale > 1:
        overlay = overlay.resize(
            (max(1, overlay.width // scale), max(1, overlay.height // scale)),
            Image.Resampling.LANCZOS,
        )
    return np.array(overlay)


def overlay_rgba(frame_bgr: np.ndarray, overlay_rgba: np.ndarray, x: int, y: int) -> np.ndarray:
    if overlay_rgba.size == 0:
        return frame_bgr

    h, w = overlay_rgba.shape[:2]
    frame_h, frame_w = frame_bgr.shape[:2]
    if x >= frame_w or y >= frame_h or x + w <= 0 or y + h <= 0:
        return frame_bgr

    x1 = max(0, x)
    y1 = max(0, y)
    x2 = min(frame_w, x + w)
    y2 = min(frame_h, y + h)

    overlay_x1 = x1 - x
    overlay_y1 = y1 - y
    overlay_x2 = overlay_x1 + (x2 - x1)
    overlay_y2 = overlay_y1 + (y2 - y1)

    roi = frame_bgr[y1:y2, x1:x2].astype(np.float32)
    overlay_crop = overlay_rgba[overlay_y1:overlay_y2, overlay_x1:overlay_x2]
    alpha = overlay_crop[:, :, 3:4].astype(np.float32) / 255.0
    overlay_bgr = overlay_crop[:, :, :3][:, :, ::-1].astype(np.float32)
    blended = roi * (1.0 - alpha) + overlay_bgr * alpha
    frame_bgr[y1:y2, x1:x2] = blended.astype(np.uint8)
    return frame_bgr


def load_first_frame(source_video: Path) -> np.ndarray:
    cap = cv2.VideoCapture(str(source_video))
    if not cap.isOpened():
        raise RuntimeError(f"Unable to open video: {source_video}")
    try:
        ok, frame = cap.read()
        if not ok:
            raise RuntimeError(f"Unable to read first frame from: {source_video}")
        return frame
    finally:
        cap.release()


def watermark_box(width: int, height: int) -> tuple[int, int, int, int]:
    # Keep the mask tight so we only touch the NotebookLM badge in the corner.
    watermark_w = max(1, int(round(width * 0.115)))
    watermark_h = max(1, int(round(height * 0.052)))
    watermark_x = max(0, width - watermark_w)
    watermark_y = max(0, height - watermark_h)
    return watermark_x, watermark_y, watermark_w, watermark_h


def inpaint_watermark(frame: np.ndarray, target_width: int, target_height: int) -> np.ndarray:
    watermark_x, watermark_y, watermark_w, watermark_h = watermark_box(target_width, target_height)
    mask = np.zeros((target_height, target_width), dtype=np.uint8)
    mask[
        watermark_y : watermark_y + watermark_h,
        watermark_x : watermark_x + watermark_w,
    ] = 255
    return cv2.inpaint(frame, mask, 2, cv2.INPAINT_TELEA)


def fit_title_block(
    title: str,
    font_path: str,
    draw: ImageDraw.ImageDraw,
    max_text_width: int,
    max_text_height: int,
    scale: int = 2,
) -> tuple[ImageFont.FreeTypeFont, int, list[str], list[tuple[str, int, int]], int]:
    probe = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
    probe_draw = ImageDraw.Draw(probe)
    line_gap = 16 * scale
    for font_size in range(90, 54, -2):
        font = ImageFont.truetype(font_path, font_size * scale)
        stroke_width = max(4, font_size // 14) * scale
        lines = wrap_text(title, probe_draw, font, max_text_width, stroke_width)
        metrics: list[tuple[str, int, int]] = []
        for line in lines:
            w, h = text_bbox(probe_draw, line, font, stroke_width)
            metrics.append((line, w, h))
        if not metrics:
            continue
        text_width = max(width for _, width, _ in metrics)
        text_height = sum(height for _, _, height in metrics) + line_gap * max(0, len(metrics) - 1)
        if text_width <= max_text_width and text_height <= max_text_height:
            return font, stroke_width, lines, metrics, line_gap

    font = ImageFont.truetype(font_path, 54 * scale)
    stroke_width = 4 * scale
    lines = wrap_text(title, probe_draw, font, max_text_width, stroke_width)
    metrics = []
    for line in lines:
        w, h = text_bbox(probe_draw, line, font, stroke_width)
        metrics.append((line, w, h))
    return font, stroke_width, lines, metrics, line_gap


def render_cover_image(
    source_video: Path,
    title: str,
    output_image: Path,
    font_path: str,
    target_width: int = 1920,
    target_height: int = 1080,
    remove_watermark: bool = True,
) -> None:
    frame = load_first_frame(source_video)
    if (frame.shape[1], frame.shape[0]) != (target_width, target_height):
        frame = cv2.resize(frame, (target_width, target_height), interpolation=cv2.INTER_LANCZOS4)
    if remove_watermark:
        frame = inpaint_watermark(frame, target_width, target_height)

    scale = 2
    working_width = target_width * scale
    working_height = target_height * scale
    frame = cv2.resize(frame, (working_width, working_height), interpolation=cv2.INTER_LANCZOS4)
    base = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)).convert("RGBA")
    overlay = Image.new("RGBA", (working_width, working_height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # A gentle darkening so the title stays readable on complex background art.
    draw.rectangle((0, 0, working_width, working_height), fill=(0, 0, 0, 48))

    max_text_width = int(working_width * 0.74)
    max_text_height = int(working_height * 0.34)
    font, stroke_width, lines, metrics, line_gap = fit_title_block(
        title=title,
        font_path=font_path,
        draw=draw,
        max_text_width=max_text_width,
        max_text_height=max_text_height,
        scale=scale,
    )

    text_width = max(width for _, width, _ in metrics)
    text_height = sum(height for _, _, height in metrics) + line_gap * max(0, len(metrics) - 1)
    panel_padding_x = 88 * scale
    panel_padding_y = 62 * scale
    panel_width = text_width + panel_padding_x * 2
    panel_height = text_height + panel_padding_y * 2
    panel_x1 = (working_width - panel_width) // 2
    panel_y1 = (working_height - panel_height) // 2
    panel_x2 = panel_x1 + panel_width
    panel_y2 = panel_y1 + panel_height

    draw.rounded_rectangle(
        (panel_x1, panel_y1, panel_x2, panel_y2),
        radius=42 * scale,
        fill=(8, 10, 12, 156),
        outline=(255, 255, 255, 72),
        width=2 * scale,
    )

    y = panel_y1 + panel_padding_y
    for line, width, height in metrics:
        x = panel_x1 + (panel_width - width) // 2
        draw.text(
            (x + 3 * scale, y + 4 * scale),
            line,
            font=font,
            fill=(0, 0, 0, 150),
            stroke_width=0,
        )
        draw.text(
            (x, y),
            line,
            font=font,
            fill=(255, 255, 255, 255),
            stroke_width=stroke_width,
            stroke_fill=(0, 0, 0, 255),
        )
        y += height + line_gap

    cover = Image.alpha_composite(base, overlay).convert("RGB")
    cover = cover.resize((target_width, target_height), Image.Resampling.LANCZOS)
    cover.save(output_image)


def make_title_card_clip(cover_image: Path, output_clip: Path, duration_seconds: float = 3.0) -> None:
    ffmpeg = ffmpeg_path("ffmpeg")
    subprocess.run(
        [
            str(ffmpeg),
            "-y",
            "-framerate",
            "30",
            "-loop",
            "1",
            "-i",
            str(cover_image),
            "-f",
            "lavfi",
            "-i",
            "anullsrc=channel_layout=stereo:sample_rate=48000",
            "-t",
            f"{duration_seconds:.3f}",
            "-filter_complex",
            "[0:v]scale=1920:1080:flags=lanczos,setsar=1[v]",
            "-map",
            "[v]",
            "-map",
            "1:a:0",
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
            "-ar",
            "48000",
            "-ac",
            "2",
            "-movflags",
            "+faststart",
            str(output_clip),
        ],
        check=True,
        capture_output=True,
        text=True,
    )


def render_main_video(
    source_video: Path,
    cues: list[Cue],
    freeze_windows: list[tuple[int, int]],
    output_video_only: Path,
    font_path: str,
    target_width: int = 1920,
    target_height: int = 1080,
    subtitle_size: int = 36,
    remove_watermark: bool = True,
) -> None:
    cap = cv2.VideoCapture(str(source_video))
    if not cap.isOpened():
        raise RuntimeError(f"Unable to open video: {source_video}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)
    source_duration_ms = int(round(frame_count * 1000.0 / fps))
    total_freeze_ms = sum(end_ms - start_ms for start_ms, end_ms in freeze_windows)
    target_output_ms = source_duration_ms + total_freeze_ms

    overlays = [
        render_caption_overlay(
            cue.text,
            frame_width=target_width,
            font_path=font_path,
            font_size=subtitle_size,
            max_text_width=target_width - 360,
            supersample=2,
        )
        for cue in cues
        ]

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

    cue_index = 0
    output_frame_idx = 0
    current_source_idx = -1
    current_source_frame: np.ndarray | None = None
    watermark_x, watermark_y, watermark_w, watermark_h = watermark_box(target_width, target_height)
    target_frame_count = int(round(target_output_ms * fps / 1000.0))

    try:
        while output_frame_idx < target_frame_count:
            output_ms = output_frame_idx * 1000.0 / fps
            source_ms = source_time_for_output_ms(output_ms, freeze_windows)
            target_source_idx = min(int(source_ms * fps / 1000.0 + 1e-6), max(0, frame_count - 1))

            while current_source_idx < target_source_idx:
                ok, frame = cap.read()
                if not ok:
                    current_source_idx = max(0, frame_count - 1)
                    break
                current_source_frame = frame
                current_source_idx += 1

            if current_source_frame is None:
                raise RuntimeError("Unable to read source frame")

            frame = current_source_frame.copy()
            if (frame.shape[1], frame.shape[0]) != (target_width, target_height):
                frame = cv2.resize(frame, (target_width, target_height), interpolation=cv2.INTER_LANCZOS4)

            if remove_watermark:
                mask = np.zeros((target_height, target_width), dtype=np.uint8)
                mask[
                    watermark_y : watermark_y + watermark_h,
                    watermark_x : watermark_x + watermark_w,
                ] = 255
                frame = cv2.inpaint(frame, mask, 2, cv2.INPAINT_TELEA)

            t_ms = int(round(output_ms))
            while cue_index < len(cues) and t_ms >= cues[cue_index].end_ms:
                cue_index += 1
            if cue_index < len(cues) and cues[cue_index].start_ms <= t_ms < cues[cue_index].end_ms:
                overlay = overlays[cue_index]
                oh, ow = overlay.shape[:2]
                x = max(0, (target_width - ow) // 2)
                y = max(0, target_height - oh - 82)
                frame = overlay_rgba(frame, overlay, x, y)

            if writer.stdin is None:
                raise RuntimeError("ffmpeg stdin closed unexpectedly")
            writer.stdin.write(frame.tobytes())
            output_frame_idx += 1
            if output_frame_idx % 1500 == 0:
                print(f"rendered {output_frame_idx}/{target_frame_count or '?'} frames")
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
    filter_parts = []
    concat_inputs = []
    for index in range(len(clips)):
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
    parser = argparse.ArgumentParser(description="Render a cleaner Chinese final video with optional title card.")
    parser.add_argument(
        "--timing-profile",
        default="agi",
        choices=("none", *TIMING_HOLD_PROFILES.keys()),
        help="Named timing-hold profile used for subtitle stretching and freeze frames.",
    )
    parser.add_argument(
        "--main-video",
        type=Path,
        default=PIPELINE_OUT_DIR / "main.zh.source.mp4",
        help="Raw main source video for optional regeneration.",
    )
    parser.add_argument(
        "--main-clip",
        type=Path,
        default=PIPELINE_OUT_DIR / "main.zh.cnonly.mp4",
        help="Prebuilt main clip with subtitles and corrected audio.",
    )
    parser.add_argument(
        "--build-main-from-source",
        action="store_true",
        help="Regenerate the main clip from --main-video and --subtitle instead of reusing --main-clip.",
    )
    parser.add_argument(
        "--audio-source",
        type=Path,
        default=None,
        help="Optional audio source for the regenerated main clip. Defaults to --main-video.",
    )
    parser.add_argument(
        "--subtitle",
        type=Path,
        default=PIPELINE_OUT_DIR / "main.zh.srt",
        help="Chinese subtitle file.",
    )
    parser.add_argument(
        "--intro",
        type=Path,
        default=BRANDING_OUT_DIR / "intro_cn.mp4",
        help="Intro clip.",
    )
    parser.add_argument(
        "--outro",
        type=Path,
        default=BRANDING_OUT_DIR / "outro.mp4",
        help="Outro clip.",
    )
    parser.add_argument(
        "--font-path",
        type=Path,
        default=default_font_path(),
        help="Font file for subtitles.",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=PIPELINE_OUT_DIR / "chinese.final.intro_title_outro.clean.mp4",
        help="Final output video path.",
    )
    parser.add_argument(
        "--cover-output",
        type=Path,
        default=PIPELINE_OUT_DIR / "chinese.final.cover.png",
        help="Cover image path.",
    )
    parser.add_argument(
        "--cover-title",
        type=str,
        default="大模型的死局：为什么“大力出奇迹”永远造不出真正的 AGI？",
        help="Title text shown on the 3-second cover card.",
    )
    parser.add_argument(
        "--cover-duration",
        type=float,
        default=3.0,
        help="Duration of the title card in seconds.",
    )
    parser.add_argument(
        "--skip-cover",
        action="store_true",
        help="Skip the cover/title card and concatenate intro, main clip, and outro directly.",
    )
    args = parser.parse_args()
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.cover_output.parent.mkdir(parents=True, exist_ok=True)

    cues = parse_srt(args.subtitle)
    if not cues:
        raise SystemExit(f"No cues found in {args.subtitle}")
    timing_holds_ms = get_timing_holds(args.timing_profile)
    cues, freeze_windows = stretch_cues(cues, timing_holds_ms)

    with tempfile.TemporaryDirectory(prefix="cn_final_", dir=str(args.output.parent)) as tmp_dir_name:
        tmp_dir = Path(tmp_dir_name)
        if args.build_main_from_source:
            main_video_only = tmp_dir / "main_render.mp4"
            main_with_audio = tmp_dir / "main_render_with_audio.mp4"

            render_main_video(
                source_video=args.main_video,
                cues=cues,
                freeze_windows=freeze_windows,
                output_video_only=main_video_only,
                font_path=str(args.font_path),
                target_width=1920,
                target_height=1080,
                subtitle_size=36,
                remove_watermark=True,
            )
            mux_audio(
                video_only=main_video_only,
                audio_source=args.audio_source or args.main_video,
                output=main_with_audio,
            )
            main_clip = main_with_audio
        else:
            main_clip = args.main_clip

        if args.skip_cover:
            concat_clips(
                clips=[args.intro, main_clip, args.outro],
                output=args.output,
            )
        else:
            render_cover_image(
                source_video=main_clip,
                title=args.cover_title,
                output_image=args.cover_output,
                font_path=str(args.font_path),
                target_width=1920,
                target_height=1080,
                remove_watermark=True,
            )
            title_clip = tmp_dir / "title_card.mp4"
            make_title_card_clip(
                cover_image=args.cover_output,
                output_clip=title_clip,
                duration_seconds=args.cover_duration,
            )
            concat_clips(
                clips=[args.intro, title_clip, main_clip, args.outro],
                output=args.output,
            )

    print(f"wrote {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
