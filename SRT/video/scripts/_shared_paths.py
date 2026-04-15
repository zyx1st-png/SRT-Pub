from __future__ import annotations

from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
VIDEO_DIR = SCRIPT_DIR.parent
BRANDING_OUT_DIR = VIDEO_DIR / "out"
PIPELINE_OUT_DIR = VIDEO_DIR / "pipeline_out"

_FONT_CANDIDATES: list[tuple[Path, str]] = [
    (Path("/System/Library/Fonts/STHeiti Medium.ttc"), "STHeiti Medium"),
    (Path("/System/Library/Fonts/PingFang.ttc"), "PingFang SC"),
    (Path("/System/Library/Fonts/Supplemental/Arial Unicode.ttf"), "Arial Unicode MS"),
]


def default_font_path() -> Path:
    for path, _name in _FONT_CANDIDATES:
        if path.exists():
            return path
    return _FONT_CANDIDATES[0][0]


def default_font_name() -> str:
    resolved = default_font_path()
    for path, name in _FONT_CANDIDATES:
        if path == resolved:
            return name
    return resolved.stem
