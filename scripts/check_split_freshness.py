#!/usr/bin/env python3
"""Check split indexes, shard sizes, links, and optional owner freshness metadata."""

from __future__ import annotations

import argparse
import re

from governance_common import (
    ROOT,
    markdown_links,
    parse_longform_registry,
    print_summary,
    read_text,
    resolve_markdown_link,
    sha256_file,
)


OWNER_PATTERNS = [
    r"原始总文[^`]*：\[`[^`]+`\]\(([^)]+)\)",
    r"总表[^`]*：\[`[^`]+`\]\(([^)]+)\)",
]


def extract_owner_link(text: str) -> str | None:
    for pattern in OWNER_PATTERNS:
        match = re.search(pattern, text)
        if match:
            return match.group(1).replace("%20", " ")
    return None


def extract_declared_owner_sha(text: str) -> str | None:
    match = re.search(r"Source owner SHA-256:\s*`([0-9a-f]{64})`", text)
    if match:
        return match.group(1)
    match = re.search(r"source_owner_sha256:\s*([0-9a-f]{64})", text)
    if match:
        return match.group(1)
    return None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--max-shard-bytes", type=int, default=50_000)
    parser.add_argument("--strict-metadata", action="store_true")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    for rel in parse_longform_registry():
        readme = ROOT / rel
        if not readme.is_file():
            errors.append(f"registered split index missing: {rel}")
            continue
        text = read_text(readme)
        owner_link = extract_owner_link(text)
        owner_path = None
        if owner_link:
            owner_path = resolve_markdown_link(readme, owner_link)
            if not owner_path.is_file():
                errors.append(f"{rel}: source owner link is broken: {owner_link}")
        else:
            warnings.append(f"{rel}: no source owner link found")

        declared_sha = extract_declared_owner_sha(text)
        if owner_path and declared_sha:
            actual_sha = sha256_file(owner_path)
            if actual_sha != declared_sha:
                errors.append(f"{rel}: source owner hash is stale")
        elif owner_path:
            message = f"{rel}: no source owner SHA metadata; freshness is link/size-only"
            if args.strict_metadata:
                errors.append(message)
            else:
                warnings.append(message)

        for target in markdown_links(text):
            if "://" in target or target.startswith("#"):
                continue
            target_path = resolve_markdown_link(readme, target)
            if not target_path.exists():
                errors.append(f"{rel}: broken link: {target}")
                continue
            if target_path == owner_path or target_path.name == "README.md":
                continue
            if target_path.suffix.lower() in {".md", ".markdown", ".txt"}:
                size = target_path.stat().st_size
                if size > args.max_shard_bytes:
                    errors.append(
                        f"{rel}: shard exceeds {args.max_shard_bytes} bytes: "
                        f"{target} ({size})"
                    )

    print_summary("split_freshness", errors, warnings)
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
