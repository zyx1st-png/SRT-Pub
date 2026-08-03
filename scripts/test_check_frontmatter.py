#!/usr/bin/env python3
"""Regression tests for the frontmatter anti-blocking helpers."""

from __future__ import annotations

from check_frontmatter import (
    baseline_additions,
    parse_baseline_text,
    status_repair_suggestion,
)


def test_parse_baseline_text() -> None:
    text = """
# comment

alpha warning
 beta warning 
# another comment
"""
    assert parse_baseline_text(text) == {"alpha warning", "beta warning"}


def test_baseline_nonexpansion() -> None:
    base = {"a", "b"}
    assert baseline_additions(base, {"a"}) == []
    assert baseline_additions(base, {"a", "b", "c"}) == ["c"]


def test_status_repair_suggestions() -> None:
    assert status_repair_suggestion("active_v1") == "status: active; version: v1"
    assert status_repair_suggestion("draft_v2") == "status: draft; version: v2"
    assert status_repair_suggestion("patch_v0_1") == (
        "status: active; type: material_patch; version: v0_1"
    )
    assert status_repair_suggestion("source_card") == (
        "status: active; type: material_source_card"
    )
    assert status_repair_suggestion("author_confirmed_live_correction_v0") == (
        "status: active; record_stage: author_confirmed_live_correction_v0"
    )


def main() -> None:
    test_parse_baseline_text()
    test_baseline_nonexpansion()
    test_status_repair_suggestions()
    print("test_check_frontmatter: all cases pass")


if __name__ == "__main__":
    main()
