#!/usr/bin/env python3
"""Prevent ordinary PRs from silently expanding frontmatter warning debt."""

from __future__ import annotations

import argparse
import subprocess

from governance_common import ROOT, read_text, repo_path


def parse_baseline(text: str) -> set[str]:
    return {
        line.strip()
        for line in text.splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }


def resolve_base_ref(base_ref: str) -> str:
    candidates = [base_ref]
    if not base_ref.startswith("origin/"):
        candidates.append(f"origin/{base_ref}")
    for candidate in candidates:
        result = subprocess.run(
            ["git", "rev-parse", "--verify", "--quiet", candidate],
            cwd=ROOT,
            text=True,
            capture_output=True,
        )
        if result.returncode == 0:
            return candidate
    raise ValueError(
        f"cannot resolve base ref `{base_ref}`; fetch the base branch or pass --base-ref explicitly"
    )


def baseline_at_ref(base_ref: str, path: str) -> set[str]:
    result = subprocess.run(
        ["git", "show", f"{base_ref}:{path}"],
        cwd=ROOT,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        detail = result.stderr.strip() or result.stdout.strip()
        raise RuntimeError(f"cannot read `{path}` at `{base_ref}`: {detail}")
    return parse_baseline(result.stdout)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--base-ref",
        default="main",
        help="Git ref whose baseline is the debt ceiling (default: main).",
    )
    parser.add_argument(
        "--baseline",
        default="Governance/Frontmatter_Warning_Baseline.txt",
        help="Baseline file to compare.",
    )
    parser.add_argument(
        "--allow-added",
        action="store_true",
        help="Allow additions after an explicit governance approval decision.",
    )
    args = parser.parse_args()

    try:
        resolved = resolve_base_ref(args.base_ref)
        before = baseline_at_ref(resolved, args.baseline)
        current_path = repo_path(args.baseline)
        if not current_path.is_file():
            raise FileNotFoundError(current_path)
        after = parse_baseline(read_text(current_path))
    except (ValueError, RuntimeError, FileNotFoundError) as exc:
        print("frontmatter_baseline_monotonic: errors=1 warnings=0")
        print(f"ERROR: {exc}")
        raise SystemExit(1)

    added = sorted(after - before)
    retired = sorted(before - after)
    print(
        "frontmatter_baseline_monotonic: "
        f"base={resolved} before={len(before)} after={len(after)} "
        f"added={len(added)} retired={len(retired)}"
    )

    if added and not args.allow_added:
        for item in added:
            print(f"ERROR: unauthorized baseline addition: {item}")
        print(
            "ERROR: baseline debt may grow only in a dedicated PR carrying the "
            "`governance-baseline-expansion-approved` label"
        )
        raise SystemExit(1)

    for item in added:
        print(f"APPROVED_ADDITION: {item}")
    for item in retired:
        print(f"RETIRED: {item}")
    raise SystemExit(0)


if __name__ == "__main__":
    main()
