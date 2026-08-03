#!/usr/bin/env python3
"""Regression tests for frontmatter anti-blocking helpers."""

from __future__ import annotations

from check_frontmatter import status_fix_suggestions
from check_frontmatter_baseline_monotonic import parse_baseline


def main() -> None:
    assert status_fix_suggestions("active_v1", {}) == [
        "status: active",
        "version: v1",
    ]
    assert status_fix_suggestions("draft_v2", {}) == [
        "status: draft",
        "version: v2",
    ]
    assert status_fix_suggestions("patch_v0_1", {}) == [
        "status: active",
        "version: v0_1",
        "type: material_patch",
    ]
    assert status_fix_suggestions("source_card", {}) == [
        "status: active",
        "type: material_source_card",
    ]
    assert status_fix_suggestions("preprint_v2", {}) == [
        "status: active",
        "source_stage: preprint_v2",
    ]
    assert status_fix_suggestions("author_confirmed_live_correction_v0", {}) == [
        "status: active",
        "record_stage: author_confirmed_live_correction_v0",
    ]
    assert status_fix_suggestions("active", {}) == []

    baseline = parse_baseline(
        """# comment\n\nfile-a: warning\n  file-b: warning  \n# ignored\n"""
    )
    assert baseline == {"file-a: warning", "file-b: warning"}

    print("frontmatter anti-blocking tests: PASS")


if __name__ == "__main__":
    main()
