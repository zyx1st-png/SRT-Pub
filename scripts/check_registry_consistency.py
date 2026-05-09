#!/usr/bin/env python3
"""Check that split indexes are registered and registry entries exist."""

from __future__ import annotations

import argparse

from governance_common import ROOT, find_split_readmes, parse_longform_registry, print_summary


ALLOW_UNREGISTERED = {
    "Operations/Material_Log/README.md",
    "Operations/Status_History/README.md",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []

    entries = set(parse_longform_registry())
    actual = set(find_split_readmes())

    for entry in sorted(entries):
        if not (ROOT / entry).is_file():
            errors.append(f"registered split index missing: {entry}")

    for readme in sorted(actual - entries):
        if readme in ALLOW_UNREGISTERED:
            continue
        message = f"split index exists but is not listed in LONGFORM_SPLITS.md: {readme}"
        if args.strict:
            errors.append(message)
        else:
            warnings.append(message)

    print_summary("registry_consistency", errors, warnings)
    raise SystemExit(1 if errors else 0)


if __name__ == "__main__":
    main()
