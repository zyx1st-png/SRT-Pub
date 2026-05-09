#!/usr/bin/env python3
"""Audit Markdown frontmatter and authority-layer leakage."""

from __future__ import annotations

import argparse

from governance_common import frontmatter_for, iter_markdown, print_summary, relpath


RECOMMENDED_KEYS = {
    "id",
    "type",
    "status",
    "layer",
    "epistemic_layer",
    "claim_mode",
}

AUTHORITY_HELPER_MARKERS = (
    "_Split/",
    "_Annex/",
    "/hooks/",
    "/patches/",
    "Operations/",
    "Materials/",
)


def is_helper_path(rel: str) -> bool:
    return any(marker in rel for marker in AUTHORITY_HELPER_MARKERS)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    parser.add_argument("--include-artifacts", action="store_true")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    ids: dict[str, str] = {}

    for path in iter_markdown(include_artifacts=args.include_artifacts):
        rel = relpath(path)
        fm = frontmatter_for(path)
        if fm is None:
            message = f"{rel}: missing frontmatter"
            if args.strict:
                errors.append(message)
            else:
                warnings.append(message)
            continue
        if fm.malformed:
            errors.append(f"{rel}: malformed frontmatter fence")
            continue

        missing = sorted(RECOMMENDED_KEYS - set(fm.data))
        if missing:
            message = f"{rel}: missing recommended frontmatter keys: {', '.join(missing)}"
            if args.strict:
                errors.append(message)
            else:
                warnings.append(message)

        file_id = fm.data.get("id")
        if file_id:
            previous = ids.get(file_id)
            if previous and previous != rel:
                warnings.append(f"duplicate frontmatter id `{file_id}`: {previous} / {rel}")
            ids[file_id] = rel

        if is_helper_path(rel):
            claim_mode = fm.data.get("claim_mode", "")
            canonical = fm.data.get("canonical", "")
            if canonical.lower() == "true":
                errors.append(f"{rel}: helper-layer file declares canonical: true")
            if claim_mode == "canonical":
                warnings.append(f"{rel}: helper-layer file uses claim_mode: canonical")

    print_summary("frontmatter", errors, warnings)
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
