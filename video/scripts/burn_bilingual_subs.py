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

from _shared_paths import default_font_name, default_font_path


TIME_RE = re.compile(
    r"(?P<sh>\d\d):(?P<sm>\d\d):(?P<ss>\d\d),(?P<sms>\d\d\d)\s+-->\s+"
    r"(?P<eh>\d\d):(?P<em>\d\d):(?P<es>\d\d),(?P<ems>\d\d\d)"
)


@dataclass(frozen=True)
class Cue:
    index: int
    start: str
    end: str
    start_ms: int
    end_ms: int
    text: str


@dataclass(frozen=True)
class BilingualCue:
    index: int
    start: str
    end: str
    start_ms: int
    end_ms: int
    top_text: str
    bottom_text: str


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
                index=int(lines[0].strip()),
                start=lines[1].split(" --> ")[0],
                end=lines[1].split(" --> ")[1],
                start_ms=start_ms,
                end_ms=end_ms,
                text="\n".join(lines[2:]).strip(),
            )
        )
    cues.sort(key=lambda item: item.index)
    return cues


def format_ms(ms: int) -> str:
    hours, rem = divmod(ms, 3_600_000)
    minutes, rem = divmod(rem, 60_000)
    seconds, millis = divmod(rem, 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d},{millis:03d}"


def normalize_subtitle_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.replace("\n", " ")).strip()


def ensure_same_length(*cue_lists: list[Cue]) -> None:
    lengths = {len(items) for items in cue_lists}
    if len(lengths) != 1:
        raise ValueError(f"Subtitle lengths do not match: {sorted(lengths)}")


def pair_cues(english: list[Cue], chinese: list[Cue], chinese_first: bool) -> list[BilingualCue]:
    ensure_same_length(english, chinese)
    paired: list[BilingualCue] = []
    for en, zh in zip(english, chinese, strict=True):
        if en.start != zh.start or en.end != zh.end:
            raise ValueError(
                f"Timestamp mismatch at cue {en.index}: "
                f"{en.start} --> {en.end} vs {zh.start} --> {zh.end}"
            )
        top_raw, bottom_raw = (zh.text, en.text) if chinese_first else (en.text, zh.text)
        paired.append(
            BilingualCue(
                index=en.index,
                start=en.start,
                end=en.end,
                start_ms=en.start_ms,
                end_ms=en.end_ms,
                top_text=normalize_subtitle_text(top_raw),
                bottom_text=normalize_subtitle_text(bottom_raw),
            )
        )
    return paired


def build_bilingual_srt(
    english: list[Cue],
    chinese: list[Cue],
    chinese_first: bool,
) -> str:
    paired = pair_cues(english, chinese, chinese_first)
    lines: list[str] = []
    for cue in paired:
        lines.append(str(cue.index))
        lines.append(f"{cue.start} --> {cue.end}")
        lines.append(f"{cue.top_text}\n{cue.bottom_text}")
        lines.append("")
    return "\n".join(lines)


def ass_escape(text: str) -> str:
    return (
        text.replace("\\", r"\\")
        .replace("{", r"\{")
        .replace("}", r"\}")
        .replace("\n", r"\N")
    )


def build_bilingual_ass(
    english: list[Cue],
    chinese: list[Cue],
    chinese_first: bool,
    font_name: str,
    font_size: int,
) -> str:
    paired = pair_cues(english, chinese, chinese_first)
    header = """[Script Info]
ScriptType: v4.00+
PlayResX: 1280
PlayResY: 720
WrapStyle: 0
ScaledBorderAndShadow: yes
YCbCr Matrix: TV.709

[V4+ Styles]
Format: Name,Fontname,Fontsize,PrimaryColour,SecondaryColour,OutlineColour,BackColour,Bold,Italic,Underline,StrikeOut,ScaleX,ScaleY,Spacing,Angle,BorderStyle,Outline,Shadow,Alignment,MarginL,MarginR,MarginV,Encoding
"""
    style = (
        f"Style: Default,{font_name},{font_size},"
        "&H00FFFFFF&,&H00FFFFFF&,&H00000000&,&H80000000&,"
        "0,0,0,0,100,100,0,0,1,2,0,2,48,48,28,1\n"
    )
    events = """[Events]
Format: Layer,Start,End,Style,Name,MarginL,MarginR,MarginV,Effect,Text
"""
    body: list[str] = [header, style, events]
    for cue in paired:
        text = ass_escape(f"{cue.top_text}\n{cue.bottom_text}")
        body.append(f"Dialogue: 0,{cue.start},{cue.end},Default,,0,0,0,,{text}\n")
    return "".join(body)


def build_single_srt(cues: list[Cue]) -> str:
    lines: list[str] = []
    for cue in cues:
        lines.append(str(cue.index))
        lines.append(f"{cue.start} --> {cue.end}")
        lines.append(normalize_subtitle_text(cue.text))
        lines.append("")
    return "\n".join(lines)


def cues_as_single_language(cues: list[Cue]) -> list[BilingualCue]:
    return [
        BilingualCue(
            index=cue.index,
            start=cue.start,
            end=cue.end,
            start_ms=cue.start_ms,
            end_ms=cue.end_ms,
            top_text=normalize_subtitle_text(cue.text),
            bottom_text="",
        )
        for cue in cues
    ]


def ffmpeg_path(name: str) -> Path:
    brew = Path("/opt/homebrew/bin") / name
    return brew if brew.exists() else Path(name)


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
    normalized = re.sub(r"\s+", " ", text.strip())
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
    top_text: str,
    bottom_text: str,
    frame_width: int,
    font_cn: ImageFont.FreeTypeFont,
    font_en: ImageFont.FreeTypeFont,
    max_text_width: int,
    stroke_width: int = 2,
) -> np.ndarray:
    probe = Image.new("RGBA", (1, 1), (0, 0, 0, 0))
    draw = ImageDraw.Draw(probe)
    top_lines = wrap_text(top_text, draw, font_cn, max_text_width, stroke_width)
    bottom_lines = wrap_text(bottom_text, draw, font_en, max_text_width, stroke_width)

    # Keep the subtitle block compact and centered.
    padding_x = 34
    padding_y = 18
    line_gap = 6
    section_gap = 10

    line_entries: list[tuple[str, ImageFont.FreeTypeFont, int, int]] = []
    for idx, line in enumerate(top_lines):
        w, h = text_bbox(draw, line, font_cn, stroke_width)
        line_entries.append((line, font_cn, w, h))
    if top_lines and bottom_lines:
        line_entries.append(("\n", font_cn, 0, section_gap))
    for idx, line in enumerate(bottom_lines):
        w, h = text_bbox(draw, line, font_en, stroke_width)
        line_entries.append((line, font_en, w, h))

    if not line_entries:
        return np.zeros((1, 1, 4), dtype=np.uint8)

    text_width = max(entry[2] for entry in line_entries)
    text_height = sum(entry[3] for entry in line_entries)
    text_height += line_gap * max(0, len(line_entries) - 1)

    overlay_width = min(frame_width - 80, text_width + padding_x * 2)
    overlay_height = text_height + padding_y * 2

    overlay = Image.new("RGBA", (overlay_width, overlay_height), (0, 0, 0, 0))
    draw_overlay = ImageDraw.Draw(overlay)
    draw_overlay.rounded_rectangle(
        [(0, 0), (overlay_width - 1, overlay_height - 1)],
        radius=20,
        fill=(0, 0, 0, 170),
    )

    y = padding_y
    for entry_index, (line, font, width, height) in enumerate(line_entries):
        if line == "\n":
            y += section_gap
            continue
        x = max(0, (overlay_width - width) // 2)
        draw_overlay.text(
            (x, y),
            line,
            font=font,
            fill=(255, 255, 255, 255),
            stroke_width=stroke_width,
            stroke_fill=(0, 0, 0, 255),
        )
        y += height + line_gap

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


def watermark_box(width: int, height: int) -> tuple[int, int, int, int]:
    # Keep the removal box tight around the NotebookLM badge in the corner.
    watermark_w = max(1, int(round(width * 0.115)))
    watermark_h = max(1, int(round(height * 0.052)))
    watermark_x = max(0, width - watermark_w)
    watermark_y = max(0, height - watermark_h)
    return watermark_x, watermark_y, watermark_w, watermark_h


def render_burned_video(
    source_video: Path,
    cues: list[BilingualCue],
    output_video_only: Path,
    font_cn_path: str,
    font_en_path: str,
    font_cn_size: int = 20,
    font_en_size: int = 18,
    remove_watermark: bool = False,
) -> None:
    cap = cv2.VideoCapture(str(source_video))
    if not cap.isOpened():
        raise RuntimeError(f"Unable to open video: {source_video}")

    fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT) or 0)

    font_cn = ImageFont.truetype(font_cn_path, font_cn_size)
    font_en = ImageFont.truetype(font_en_path, font_en_size)

    max_text_width = max(240, width - 220)
    overlays = []
    for cue in cues:
        overlays.append(
            render_caption_overlay(
                top_text=cue.top_text,
                bottom_text=cue.bottom_text,
                frame_width=width,
                font_cn=font_cn,
                font_en=font_en,
                max_text_width=max_text_width,
            )
        )

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
            f"{width}x{height}",
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
            "18",
            "-pix_fmt",
            "yuv420p",
            str(output_video_only),
        ],
        stdin=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    cue_index = 0
    watermark_x, watermark_y, watermark_w, watermark_h = watermark_box(width, height)

    frame_idx = 0
    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            if remove_watermark:
                mask = np.zeros((height, width), dtype=np.uint8)
                mask[
                    watermark_y : watermark_y + watermark_h,
                    watermark_x : watermark_x + watermark_w,
                ] = 255
                frame = cv2.inpaint(frame, mask, 2, cv2.INPAINT_TELEA)

            t_ms = int(round(frame_idx * 1000.0 / fps))
            while cue_index < len(cues) and t_ms >= cues[cue_index].end_ms:
                cue_index += 1
            if cue_index < len(cues) and cues[cue_index].start_ms <= t_ms < cues[cue_index].end_ms:
                current_overlay = overlays[cue_index]
                overlay_h, overlay_w = current_overlay.shape[:2]
                x = max(0, (width - overlay_w) // 2)
                y = max(0, height - overlay_h - 28)
                frame = overlay_rgba(frame, current_overlay, x, y)

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


def main() -> int:
    parser = argparse.ArgumentParser(description="Create bilingual subtitles and burn them into a video.")
    parser.add_argument(
        "--video",
        type=Path,
        required=True,
        help="Source video to subtitle.",
    )
    parser.add_argument(
        "--english",
        type=Path,
        default=None,
        help="English subtitle file. Required unless --chinese-only is set.",
    )
    parser.add_argument(
        "--chinese",
        type=Path,
        required=True,
        help="Chinese subtitle file.",
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
        help="Optional output directory. Defaults to the video directory.",
    )
    parser.add_argument(
        "--english-first",
        action="store_true",
        help="Put English on the first line and Chinese on the second line.",
    )
    parser.add_argument(
        "--chinese-only",
        action="store_true",
        help="Render only the Chinese subtitles.",
    )
    parser.add_argument(
        "--font-path",
        type=Path,
        default=default_font_path(),
        help="Font file used when burning subtitles.",
    )
    parser.add_argument(
        "--font-name",
        default=default_font_name(),
        help="Font name used in the reference ASS file.",
    )
    parser.add_argument(
        "--font-size",
        type=int,
        default=20,
        help="Subtitle font size when burning subtitles.",
    )
    parser.add_argument(
        "--remove-watermark",
        action="store_true",
        help="Mask the NotebookLM watermark in the bottom-right corner.",
    )
    args = parser.parse_args()

    if not args.chinese_only and args.english is None:
        raise SystemExit("--english is required unless --chinese-only is set.")

    english = parse_srt(args.english) if args.english else []
    chinese = parse_srt(args.chinese)
    if args.chinese_only:
        subtitle_text = build_single_srt(chinese)
        ass_text = ""
        cue_list = cues_as_single_language(chinese)
    else:
        subtitle_text = build_bilingual_srt(
            english=english,
            chinese=chinese,
            chinese_first=not args.english_first,
        )
        ass_text = build_bilingual_ass(
            english=english,
            chinese=chinese,
            chinese_first=not args.english_first,
            font_name=args.font_name,
            font_size=args.font_size,
        )
        cue_list = pair_cues(english, chinese, chinese_first=not args.english_first)

    out_dir = args.output_dir or args.video.parent
    out_dir.mkdir(parents=True, exist_ok=True)
    output_prefix = args.output_prefix or (
        f"{args.video.stem}.cnonly" if args.chinese_only else f"{args.video.stem}.bilingual"
    )
    srt_path = out_dir / f"{output_prefix}.srt"
    ass_path = out_dir / f"{output_prefix}.ass"
    out_video = out_dir / f"{output_prefix}.mp4"

    srt_path.write_text(subtitle_text, encoding="utf-8")
    if ass_text:
        ass_path.write_text(ass_text, encoding="utf-8")
    with tempfile.TemporaryDirectory(prefix="bilingual_render_", dir=str(out_dir)) as tmp_name:
        tmp_dir = Path(tmp_name)
        video_only = tmp_dir / f"{args.output_prefix}.video_only.mp4"
        render_burned_video(
            source_video=args.video,
            cues=cue_list,
            output_video_only=video_only,
            font_cn_path=str(args.font_path),
            font_en_path=str(args.font_path),
            font_cn_size=args.font_size,
            font_en_size=max(args.font_size - 2, 16),
            remove_watermark=args.remove_watermark,
        )
        mux_audio(
            video_only=video_only,
            audio_source=args.video,
            output=out_video,
        )

    print(f"wrote {srt_path}")
    if ass_text:
        print(f"wrote {ass_path}")
    print(f"wrote {out_video}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
