#!/usr/bin/env python3
"""
generate_srt_videos.py
Generates intro (3s) and outro (5s) MP4 videos for the SRT Project YouTube channel.
Usage: uv run python scripts/generate_srt_videos.py
"""

import io
import math
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path
from typing import Generator

from PIL import Image, ImageDraw, ImageFont


# ─────────────────────────────────────────────
# LAYER 1: Configuration
# ─────────────────────────────────────────────

@dataclass
class VideoConfig:
    width: int = 1920
    height: int = 1080
    fps: int = 30

    ffmpeg_path: str = "/opt/homebrew/Cellar/ffmpeg/8.1/bin/ffmpeg"
    output_dir: Path = Path("/Users/zhangyuxin/.openclaw/workspace/videos")

    font_path: str = "/System/Library/Fonts/Helvetica.ttc"
    font_fallbacks: list = field(default_factory=lambda: [
        "/System/Library/Fonts/HelveticaNeue.ttc",
        "/System/Library/Fonts/Avenir Next.ttc",
        "/System/Library/Fonts/Geneva.ttf",
    ])

    # Colors
    bg_color: tuple = (0, 0, 0)
    text_white: tuple = (255, 255, 255)
    text_gray: tuple = (180, 180, 180)
    subscribe_red: tuple = (255, 0, 0)

    # Content
    channel_name: str = "SRT Project"
    tagline: str = "Existence is Selection"
    subscribe_label: str = "SUBSCRIBE"
    subscribe_subtext: str = "for more on Selection-Reality Theory"

    # Font sizes
    size_title: int = 80
    size_tagline: int = 36
    size_subscribe_btn: int = 30
    size_subscribe_sub: int = 24

    # Intro timing (frames)
    intro_total_frames: int = 90       # 3.0 s
    intro_title_fade_in_end: int = 45  # 0–45: title fades in (1.5 s)
    intro_tagline_fade_in_start: int = 15
    intro_tagline_fade_in_end: int = 60
    intro_fade_out_start: int = 75     # 75–90: fade to black

    # Outro timing (frames)
    outro_total_frames: int = 150       # 5.0 s
    outro_title_fade_in_end: int = 30   # 0–30: title fades in
    outro_content_fade_in_end: int = 60 # 30–60: button + subtext fade in
    outro_fade_out_start: int = 120     # 120–150: fade to black

    # Subscribe button
    btn_width: int = 300
    btn_height: int = 70
    btn_radius: int = 35
    btn_pulse_freq: float = 1.5
    btn_pulse_min: float = 0.88
    btn_pulse_max: float = 1.06

    # FFmpeg settings
    crf: int = 18
    preset: str = "slow"
    pix_fmt: str = "yuv420p"


# ─────────────────────────────────────────────
# LAYER 2: Font Loading
# ─────────────────────────────────────────────

@dataclass
class FontSet:
    title: ImageFont.FreeTypeFont
    tagline: ImageFont.FreeTypeFont
    btn_label: ImageFont.FreeTypeFont
    btn_sub: ImageFont.FreeTypeFont

    @staticmethod
    def _load_font(path: str, size: int, index: int = 0,
                   fallbacks: list = None) -> ImageFont.FreeTypeFont:
        candidates = [(path, index)] + [(f, 0) for f in (fallbacks or [])]
        for fpath, fidx in candidates:
            try:
                return ImageFont.truetype(fpath, size, index=fidx)
            except (IOError, OSError):
                continue
        print(f"WARNING: Could not load any TrueType font. Using PIL default.", file=sys.stderr)
        return ImageFont.load_default()

    @classmethod
    def load(cls, cfg: VideoConfig) -> "FontSet":
        fb = cfg.font_fallbacks
        return cls(
            title=cls._load_font(cfg.font_path, cfg.size_title, index=1, fallbacks=fb),
            tagline=cls._load_font(cfg.font_path, cfg.size_tagline, index=0, fallbacks=fb),
            btn_label=cls._load_font(cfg.font_path, cfg.size_subscribe_btn, index=1, fallbacks=fb),
            btn_sub=cls._load_font(cfg.font_path, cfg.size_subscribe_sub, index=0, fallbacks=fb),
        )


# ─────────────────────────────────────────────
# LAYER 3: Drawing Primitives
# ─────────────────────────────────────────────

def ease_in_out_cubic(t: float) -> float:
    t = max(0.0, min(1.0, t))
    return t * t * (3.0 - 2.0 * t)


def fade_alpha(frame: int, start: int, end: int) -> int:
    if frame <= start:
        return 0
    if frame >= end:
        return 255
    t = (frame - start) / (end - start)
    return int(ease_in_out_cubic(t) * 255)


def draw_text_centered(
    draw: ImageDraw.ImageDraw,
    canvas_w: int,
    y_center: int,
    text: str,
    font: ImageFont.FreeTypeFont,
    color_rgb: tuple,
    alpha: int,
) -> None:
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    x = (canvas_w - tw) // 2 - bbox[0]
    y = y_center - th // 2 - bbox[1]
    draw.text((x, y), text, font=font, fill=(*color_rgb, alpha))


def draw_subscribe_button(
    draw: ImageDraw.ImageDraw,
    cfg: VideoConfig,
    fonts: FontSet,
    center_x: int,
    center_y: int,
    btn_alpha: int,
    pulse_scale: float,
) -> None:
    bw = int(cfg.btn_width * pulse_scale)
    bh = int(cfg.btn_height * pulse_scale)
    radius = int(cfg.btn_radius * pulse_scale)

    x0 = center_x - bw // 2
    y0 = center_y - bh // 2
    x1 = x0 + bw
    y1 = y0 + bh

    draw.rounded_rectangle(
        [x0, y0, x1, y1],
        radius=radius,
        fill=(*cfg.subscribe_red, btn_alpha),
    )

    lbl = cfg.subscribe_label
    bbox = draw.textbbox((0, 0), lbl, font=fonts.btn_label)
    lw = bbox[2] - bbox[0]
    lh = bbox[3] - bbox[1]
    lx = center_x - lw // 2 - bbox[0]
    ly = center_y - lh // 2 - bbox[1]
    draw.text((lx, ly), lbl, font=fonts.btn_label, fill=(255, 255, 255, btn_alpha))


def composite_frame(overlay: Image.Image, bg_color: tuple) -> Image.Image:
    w, h = overlay.size
    bg = Image.new("RGB", (w, h), bg_color)
    bg.paste(overlay, mask=overlay.split()[3])
    return bg


# ─────────────────────────────────────────────
# LAYER 4: Frame Generators
# ─────────────────────────────────────────────

def gen_intro_frames(cfg: VideoConfig, fonts: FontSet) -> Generator[Image.Image, None, None]:
    W, H = cfg.width, cfg.height

    for f in range(cfg.intro_total_frames):
        overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)

        # Global fade-out
        if f < cfg.intro_fade_out_start:
            global_factor = 1.0
        else:
            t = (f - cfg.intro_fade_out_start) / (cfg.intro_total_frames - cfg.intro_fade_out_start)
            global_factor = 1.0 - ease_in_out_cubic(t)

        # "SRT Project"
        title_a = int(fade_alpha(f, 0, cfg.intro_title_fade_in_end) * global_factor)
        draw_text_centered(draw, W, H // 2 - 50, cfg.channel_name,
                           fonts.title, cfg.text_white, title_a)

        # "Existence is Selection"
        tagline_a = int(
            fade_alpha(f, cfg.intro_tagline_fade_in_start, cfg.intro_tagline_fade_in_end)
            * global_factor
        )
        draw_text_centered(draw, W, H // 2 + 50, cfg.tagline,
                           fonts.tagline, cfg.text_gray, tagline_a)

        yield composite_frame(overlay, cfg.bg_color)


def gen_outro_frames(cfg: VideoConfig, fonts: FontSet) -> Generator[Image.Image, None, None]:
    W, H = cfg.width, cfg.height
    btn_center_x = W // 2
    btn_center_y = H // 2 + 30
    subtext_y = btn_center_y + cfg.btn_height // 2 + 50

    for f in range(cfg.outro_total_frames):
        overlay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)

        # Global fade-out
        if f < cfg.outro_fade_out_start:
            global_factor = 1.0
        else:
            t = (f - cfg.outro_fade_out_start) / (cfg.outro_total_frames - cfg.outro_fade_out_start)
            global_factor = 1.0 - ease_in_out_cubic(t)

        # "SRT Project" title
        title_a = int(fade_alpha(f, 0, cfg.outro_title_fade_in_end) * global_factor)
        draw_text_centered(draw, W, H // 2 - 130, cfg.channel_name,
                           fonts.title, cfg.text_white, title_a)

        # Pulse scale (only active during hold phase)
        if f < cfg.outro_content_fade_in_end:
            pulse_scale = 1.0
        else:
            t_pulse = f / cfg.fps
            raw = math.sin(2 * math.pi * cfg.btn_pulse_freq * t_pulse)
            mid = (cfg.btn_pulse_min + cfg.btn_pulse_max) / 2
            half = (cfg.btn_pulse_max - cfg.btn_pulse_min) / 2
            pulse_scale = mid + half * raw

        # Subscribe button + subtext
        btn_a = int(
            fade_alpha(f, cfg.outro_title_fade_in_end, cfg.outro_content_fade_in_end)
            * global_factor
        )
        if btn_a > 0:
            draw_subscribe_button(draw, cfg, fonts,
                                  btn_center_x, btn_center_y, btn_a, pulse_scale)
            draw_text_centered(draw, W, subtext_y, cfg.subscribe_subtext,
                               fonts.btn_sub, cfg.text_gray, btn_a)

        yield composite_frame(overlay, cfg.bg_color)


# ─────────────────────────────────────────────
# LAYER 5: FFmpeg Encoding
# ─────────────────────────────────────────────

def encode_to_mp4(
    frames: Generator[Image.Image, None, None],
    output_path: Path,
    cfg: VideoConfig,
    label: str = "video",
) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        cfg.ffmpeg_path,
        "-y",
        "-f", "image2pipe",
        "-vcodec", "png",
        "-r", str(cfg.fps),
        "-i", "pipe:0",
        "-vcodec", "libx264",
        "-pix_fmt", cfg.pix_fmt,
        "-crf", str(cfg.crf),
        "-preset", cfg.preset,
        "-movflags", "+faststart",
        str(output_path),
    ]

    print(f"Encoding {label}: {output_path}")

    proc = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
    )

    frame_count = 0
    try:
        for frame_img in frames:
            buf = io.BytesIO()
            frame_img.save(buf, format="PNG")
            proc.stdin.write(buf.getvalue())
            frame_count += 1

        proc.stdin.close()
        proc.wait()

    except BrokenPipeError:
        proc.wait()
        stderr_out = proc.stderr.read().decode(errors="replace")
        raise RuntimeError(
            f"FFmpeg pipe broke after {frame_count} frames.\nFFmpeg stderr:\n{stderr_out}"
        )

    if proc.returncode != 0:
        stderr_out = proc.stderr.read().decode(errors="replace")
        raise RuntimeError(
            f"FFmpeg exited with code {proc.returncode}.\nFFmpeg stderr:\n{stderr_out}"
        )

    size_kb = output_path.stat().st_size // 1024
    print(f"  Done: {frame_count} frames -> {output_path} ({size_kb} KB)")


# ─────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────

def main() -> None:
    cfg = VideoConfig()
    fonts = FontSet.load(cfg)

    print(f"Output directory: {cfg.output_dir}")
    print()

    encode_to_mp4(
        frames=gen_intro_frames(cfg, fonts),
        output_path=cfg.output_dir / "srt_intro.mp4",
        cfg=cfg,
        label="SRT Intro (3s, 90 frames)",
    )

    encode_to_mp4(
        frames=gen_outro_frames(cfg, fonts),
        output_path=cfg.output_dir / "srt_outro.mp4",
        cfg=cfg,
        label="SRT Outro (5s, 150 frames)",
    )

    print()
    print("All done.")
    print(f"  Intro: {cfg.output_dir / 'srt_intro.mp4'}")
    print(f"  Outro: {cfg.output_dir / 'srt_outro.mp4'}")


if __name__ == "__main__":
    main()
