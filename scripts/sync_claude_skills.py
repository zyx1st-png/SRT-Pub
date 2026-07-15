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
DEFAULT_SOURCE_ROOT = HOME / ".claude" / "skills"
TARGET_ROOTS = {
    "codex": HOME / ".codex" / "skills",
    "openclaw": HOME / ".openclaw" / "skills",
}
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
        "--source-root",
        type=Path,
        default=DEFAULT_SOURCE_ROOT,
        help=(
            "Skill source directory (default: ~/.claude/skills). "
            "Use --source-root .claude/skills from the repo root to sync "
            "repo-tracked skills."
        ),
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


def iter_direct_skills(source_root: Path) -> Iterable[Path]:
    ensure_source_exists(source_root, "Claude skill root")
    for child in sorted(source_root.iterdir()):
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


def sync_standard_skills(source_root: Path, target_root: Path, dry_run: bool) -> None:
    for skill_dir in iter_direct_skills(source_root):
        copy_tree(skill_dir, target_root / skill_dir.name, dry_run=dry_run)


def sync_academic_skills(source_root: Path, target_root: Path, dry_run: bool) -> None:
    academic_repo = source_root / "academic-research-skills"
    academic_shared = academic_repo / "shared"
    if not academic_repo.exists():
        print(f"Skipping academic skills: not present under {source_root}")
        return
    ensure_source_exists(academic_shared, "academic-research shared folder")

    for skill_name in ACADEMIC_SUBSKILLS:
        src = academic_repo / skill_name
        ensure_source_exists(src / "SKILL.md", f"{skill_name} skill file")
        dst = target_root / skill_name
        copy_tree(src, dst, dry_run=dry_run)

        shared_dst = dst / "shared"
        action = "Would copy shared schema into" if dry_run else "Copying shared schema into"
        print(f"{action}: {shared_dst}")
        if dry_run:
            continue

        shared_dst.mkdir(parents=True, exist_ok=True)
        shutil.copy2(academic_shared / "handoff_schemas.md", shared_dst / "handoff_schemas.md")


def sync_target(source_root: Path, target_name: str, dry_run: bool) -> None:
    target_root = TARGET_ROOTS[target_name]
    ensure_source_exists(target_root, f"{target_name} skill root")
    print(f"\n== Sync target: {target_name} ({target_root}) ==")
    sync_standard_skills(source_root, target_root, dry_run=dry_run)
    sync_academic_skills(source_root, target_root, dry_run=dry_run)


def main() -> None:
    args = parse_args()
    source_root = args.source_root.expanduser().resolve()
    print(f"Source root: {source_root}")
    for target in args.targets:
        sync_target(source_root, target, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
