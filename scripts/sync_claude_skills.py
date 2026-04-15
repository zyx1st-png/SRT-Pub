#!/usr/bin/env python3
"""Sync Claude skills into Codex/OpenClaw skill directories.

This script keeps the source of truth in ~/.claude/skills and copies a
compatible subset into runtime skill directories used by other assistants.
"""

from __future__ import annotations

import argparse
import shutil
from datetime import datetime
from pathlib import Path
from typing import Iterable


HOME = Path.home()
SOURCE_ROOT = HOME / ".claude" / "skills"
TARGET_ROOTS = {
    "codex": HOME / ".codex" / "skills",
    "openclaw": HOME / ".openclaw" / "skills",
}
ACADEMIC_REPO = SOURCE_ROOT / "academic-research-skills"
ACADEMIC_SHARED = ACADEMIC_REPO / "shared"
ACADEMIC_SUBSKILLS = (
    "academic-paper",
    "academic-paper-reviewer",
    "academic-pipeline",
    "deep-research",
)
IGNORE_NAMES = shutil.ignore_patterns(
    ".DS_Store",
    ".git",
    ".gitignore",
    "__pycache__",
    "cache",
    "downloads",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync ~/.claude/skills into Codex/OpenClaw skill folders."
    )
    parser.add_argument(
        "--targets",
        nargs="+",
        choices=sorted(TARGET_ROOTS),
        default=sorted(TARGET_ROOTS),
        help="Target runtimes to sync into.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show planned operations without writing anything.",
    )
    return parser.parse_args()


def ensure_source_exists(path: Path, label: str) -> None:
    if not path.exists():
        raise SystemExit(f"Missing {label}: {path}")


def iter_direct_skills() -> Iterable[Path]:
    ensure_source_exists(SOURCE_ROOT, "Claude skill root")
    for child in sorted(SOURCE_ROOT.iterdir()):
        if not child.is_dir():
            continue
        if child.name == "academic-research-skills":
            continue
        if (child / "SKILL.md").exists():
            yield child


def copy_tree(src: Path, dst: Path, dry_run: bool) -> None:
    action = "Would copy" if dry_run else "Copying"
    print(f"{action}: {src} -> {dst}")
    if dry_run:
        return

    dst.parent.mkdir(parents=True, exist_ok=True)
    staging = dst.parent / f".{dst.name}.sync-staging"
    if staging.exists():
        shutil.rmtree(staging)
    shutil.copytree(src, staging, ignore=IGNORE_NAMES)

    if dst.exists():
        backup = dst.parent / f".{dst.name}.bak-{timestamp()}"
        print(f"Backing up existing skill: {dst} -> {backup}")
        dst.rename(backup)

    staging.rename(dst)


def timestamp() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def sync_standard_skills(target_root: Path, dry_run: bool) -> None:
    for skill_dir in iter_direct_skills():
        copy_tree(skill_dir, target_root / skill_dir.name, dry_run=dry_run)


def sync_academic_skills(target_root: Path, dry_run: bool) -> None:
    ensure_source_exists(ACADEMIC_REPO, "academic-research-skills repo")
    ensure_source_exists(ACADEMIC_SHARED, "academic-research shared folder")

    for skill_name in ACADEMIC_SUBSKILLS:
        src = ACADEMIC_REPO / skill_name
        ensure_source_exists(src / "SKILL.md", f"{skill_name} skill file")
        dst = target_root / skill_name
        copy_tree(src, dst, dry_run=dry_run)

        shared_dst = dst / "shared"
        action = "Would copy shared schema into" if dry_run else "Copying shared schema into"
        print(f"{action}: {shared_dst}")
        if dry_run:
            continue

        shared_dst.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ACADEMIC_SHARED / "handoff_schemas.md", shared_dst / "handoff_schemas.md")


def sync_target(target_name: str, dry_run: bool) -> None:
    target_root = TARGET_ROOTS[target_name]
    ensure_source_exists(target_root, f"{target_name} skill root")
    print(f"\n== Sync target: {target_name} ({target_root}) ==")
    sync_standard_skills(target_root, dry_run=dry_run)
    sync_academic_skills(target_root, dry_run=dry_run)


def main() -> None:
    args = parse_args()
    print(f"Source root: {SOURCE_ROOT}")
    for target in args.targets:
        sync_target(target, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
