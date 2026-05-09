#!/usr/bin/env python3
"""Run the SRT repository governance preflight checks."""

from __future__ import annotations

from pathlib import Path
import argparse
import subprocess
import sys

from governance_common import ROOT


def run_step(label: str, command: list[str]) -> int:
    print(f"\n== {label} ==")
    result = subprocess.run(command, cwd=ROOT, text=True)
    if result.returncode == 0:
        print(f"PASS: {label}")
    else:
        print(f"FAIL: {label} (exit {result.returncode})")
    return result.returncode


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true", help="Escalate warning-prone checks.")
    parser.add_argument(
        "--strict-split-metadata",
        action="store_true",
        help="Require source-owner SHA metadata without enabling all strict checks.",
    )
    parser.add_argument("--skip-write-report", action="store_true")
    args = parser.parse_args()

    python = sys.executable
    steps: list[tuple[str, list[str]]] = []

    audit_cmd = [python, "scripts/audit_large_files.py"]
    if not args.skip_write_report:
        audit_cmd.append("--write-report")
    steps.append(("large-file audit", audit_cmd))

    if (ROOT / "scripts" / "check_book_outline_split.py").is_file():
        steps.append(("book outline split", [python, "scripts/check_book_outline_split.py"]))

    split_cmd = [python, "scripts/check_split_freshness.py"]
    if args.strict or args.strict_split_metadata:
        split_cmd.append("--strict-metadata")
    steps.append(("split freshness", split_cmd))

    registry_cmd = [python, "scripts/check_registry_consistency.py"]
    if args.strict:
        registry_cmd.append("--strict")
    steps.append(("registry consistency", registry_cmd))

    frontmatter_cmd = [python, "scripts/check_frontmatter.py"]
    if args.strict:
        frontmatter_cmd.append("--strict")
    steps.append(("frontmatter", frontmatter_cmd))

    noise_cmd = [python, "scripts/check_forbidden_noise.py"]
    if args.strict:
        noise_cmd.append("--strict-worktree")
    steps.append(("forbidden local noise", noise_cmd))

    failures = 0
    for label, command in steps:
        failures += 1 if run_step(label, command) else 0

    print(f"\npreflight: failures={failures}")
    raise SystemExit(1 if failures else 0)


if __name__ == "__main__":
    main()
