#!/usr/bin/env python3
"""Detect forbidden local noise and unresolved merge markers."""

from __future__ import annotations

from pathlib import Path
import argparse
import subprocess

from governance_common import ROOT, print_summary


FORBIDDEN_NAMES = {
    ".DS_Store",
}

FORBIDDEN_PARTS = {
    "__pycache__",
}

CONFLICT_MARKER_PREFIXES = (
    "<<<<<<< ",
    "||||||| ",
    ">>>>>>> ",
)


def is_forbidden(rel: str) -> bool:
    path = Path(rel)
    if path.name in FORBIDDEN_NAMES:
        return True
    if any(part in FORBIDDEN_PARTS for part in path.parts):
        return True
    if rel.startswith(".claude/"):
        return True
    if rel.endswith(".pyc"):
        return True
    return False


def git_lines(*args: str) -> list[str]:
    result = subprocess.run(
        ["git", *args],
        cwd=ROOT,
        check=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    return [line for line in result.stdout.splitlines() if line.strip()]


def tracked_conflict_markers() -> list[str]:
    """Return tracked text lines that still contain Git conflict markers.

    Do not key on a bare ``=======`` line because Markdown/prose may use it
    legitimately. The three marker prefixes below are specific enough to catch
    unresolved Git conflicts while keeping false positives low.
    """
    result = subprocess.run(
        [
            "git",
            "grep",
            "-n",
            "-I",
            "-E",
            r"^(<<<<<<< |\|\|\|\|\|\|\| |>>>>>>> )",
            "--",
            ".",
        ],
        cwd=ROOT,
        check=False,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode not in (0, 1):
        raise RuntimeError(result.stderr.strip() or "git grep failed")
    return [line for line in result.stdout.splitlines() if line.strip()]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict-worktree", action="store_true")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    staged = git_lines("diff", "--cached", "--name-only")
    for rel in staged:
        if is_forbidden(rel):
            errors.append(f"forbidden staged path: {rel}")

    porcelain = git_lines("status", "--short")
    for line in porcelain:
        rel = line[3:] if len(line) > 3 else line
        rel = rel.strip().strip('"')
        if not rel:
            continue
        if is_forbidden(rel):
            message = f"forbidden local noise in worktree: {rel}"
            if args.strict_worktree:
                errors.append(message)
            else:
                warnings.append(message)

    for match in tracked_conflict_markers():
        errors.append(f"unresolved merge marker in tracked text: {match}")

    print_summary("forbidden_noise", errors, warnings)
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
