#!/usr/bin/env python3
"""Shared helpers for SRT repository governance scripts."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import hashlib
import os
import re


ROOT = Path(__file__).resolve().parents[1]

SKIP_DIRS = {
    ".git",
    ".claude",
    "__pycache__",
}

ARTIFACT_PREFIXES = (
    "Papers/",
    "papers/",
    "graphify-out/",
    "Archive/",
    "video/",
)

MARKDOWN_SUFFIXES = {".md", ".markdown", ".txt"}


@dataclass(frozen=True)
class Frontmatter:
    data: dict[str, str]
    raw: str
    malformed: bool = False


def repo_path(path: str | Path) -> Path:
    item = Path(path)
    if item.is_absolute():
        return item
    return ROOT / item


def relpath(path: str | Path, start: str | Path | None = None) -> str:
    base = ROOT if start is None else Path(start)
    return os.path.relpath(Path(path), base).replace(os.sep, "/")


def should_skip(path: Path) -> bool:
    try:
        parts = path.relative_to(ROOT).parts
    except ValueError:
        parts = path.parts
    return any(part in SKIP_DIRS for part in parts)


def is_artifact(rel: str) -> bool:
    return rel.startswith(ARTIFACT_PREFIXES)


def iter_markdown(include_artifacts: bool = False) -> list[Path]:
    paths: list[Path] = []
    for path in ROOT.rglob("*"):
        if should_skip(path):
            continue
        if not path.is_file():
            continue
        if path.suffix.lower() not in MARKDOWN_SUFFIXES:
            continue
        rel = path.relative_to(ROOT).as_posix()
        if not include_artifacts and is_artifact(rel):
            continue
        paths.append(path)
    return sorted(paths)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def parse_frontmatter(text: str) -> Frontmatter | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return Frontmatter(data={}, raw="", malformed=True)
    raw = text[4:end]
    data: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        data[key.strip()] = value.strip().strip('"').strip("'")
    return Frontmatter(data=data, raw=raw)


def frontmatter_for(path: Path) -> Frontmatter | None:
    return parse_frontmatter(read_text(path))


def markdown_links(text: str) -> list[str]:
    links: list[str] = []
    for match in re.finditer(r"\[[^\]]+\]\(([^)]+)\)", text):
        target = match.group(1).strip()
        if "://" in target or target.startswith("#"):
            continue
        links.append(target.replace("%20", " "))
    return links


def parse_longform_registry() -> list[str]:
    registry = ROOT / "LONGFORM_SPLITS.md"
    if not registry.is_file():
        return []
    text = read_text(registry)
    return re.findall(r"^-\s+`([^`]+)`", text, flags=re.MULTILINE)


def find_split_readmes() -> list[str]:
    readmes: set[str] = set()
    for path in ROOT.rglob("README.md"):
        if should_skip(path):
            continue
        rel = path.relative_to(ROOT).as_posix()
        if "/_Split/" in rel or rel.endswith("_Split/README.md"):
            readmes.add(rel)
    for special in [
        "Glossary/README.md",
        "Operations/Material_Log/README.md",
        "Operations/Status_History/README.md",
        "STATUS_Split/README.md",
    ]:
        if (ROOT / special).is_file():
            readmes.add(special)
    return sorted(readmes)


def resolve_markdown_link(readme: Path, target: str) -> Path:
    if "#" in target:
        target = target.split("#", 1)[0]
    return (readme.parent / target).resolve()


def print_summary(
    name: str,
    errors: list[str],
    warnings: list[str],
    max_items: int = 80,
) -> None:
    print(f"{name}: errors={len(errors)} warnings={len(warnings)}")
    shown_errors = errors[:max_items]
    shown_warnings = warnings[:max_items]
    for item in shown_errors:
        print(f"ERROR: {item}")
    if len(errors) > len(shown_errors):
        print(f"ERROR: ... {len(errors) - len(shown_errors)} more")
    for item in shown_warnings:
        print(f"WARN: {item}")
    if len(warnings) > len(shown_warnings):
        print(f"WARN: ... {len(warnings) - len(shown_warnings)} more")
