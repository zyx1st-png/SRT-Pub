#!/usr/bin/env python3
"""Refresh source-owner size/hash metadata in registered split README files."""

from __future__ import annotations

import argparse
import re

from governance_common import (
    ROOT,
    parse_longform_registry,
    read_text,
    resolve_markdown_link,
    sha256_file,
)


OWNER_PATTERNS = [
    r"(.*原始总文[^`]*：\[`[^`]+`\]\(([^)]+)\).*)",
    r"(.*总表[^`]*：\[`[^`]+`\]\(([^)]+)\).*)",
]


def find_owner_line(lines: list[str]) -> tuple[int, str] | None:
    for index, line in enumerate(lines):
        for pattern in OWNER_PATTERNS:
            match = re.match(pattern, line)
            if match:
                return index, match.group(2).replace("%20", " ")
    return None


def remove_old_metadata(lines: list[str]) -> list[str]:
    return [
        line
        for line in lines
        if not line.startswith("- Source owner bytes:")
        and not line.startswith("- Source owner SHA-256:")
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()

    changed: list[str] = []
    skipped: list[str] = []

    for rel in parse_longform_registry():
        readme = ROOT / rel
        if not readme.is_file():
            skipped.append(f"{rel}: missing")
            continue
        original = read_text(readme)
        lines = remove_old_metadata(original.splitlines())
        owner = find_owner_line(lines)
        if owner is None:
            skipped.append(f"{rel}: no owner link")
            continue
        owner_index, owner_link = owner
        owner_path = resolve_markdown_link(readme, owner_link)
        if not owner_path.is_file():
            skipped.append(f"{rel}: owner missing")
            continue
        metadata = [
            f"- Source owner bytes: `{owner_path.stat().st_size}`",
            f"- Source owner SHA-256: `{sha256_file(owner_path)}`",
        ]
        new_lines = lines[: owner_index + 1] + metadata + lines[owner_index + 1 :]
        new_text = "\n".join(new_lines).rstrip() + "\n"
        if new_text != original:
            changed.append(rel)
            if not args.check:
                readme.write_text(new_text, encoding="utf-8")

    mode = "would_change" if args.check else "changed"
    print(f"refresh_split_metadata: {mode}={len(changed)} skipped={len(skipped)}")
    for item in changed[:80]:
        print(f"{mode}: {item}")
    if len(changed) > 80:
        print(f"{mode}: ... {len(changed) - 80} more")
    for item in skipped[:40]:
        print(f"skip: {item}")
    if len(skipped) > 40:
        print(f"skip: ... {len(skipped) - 40} more")
    raise SystemExit(1 if args.check and changed else 0)


if __name__ == "__main__":
    main()
