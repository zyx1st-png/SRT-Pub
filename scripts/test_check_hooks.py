#!/usr/bin/env python3
"""Fixture tests for `check_hooks.py`.

Covers the four ledger states plus the error paths that would otherwise let a
hook pass syntactically while staying unclosed in substance: path escapes,
non-Markdown targets, missing reasons, absent targets, weak (non-unique)
anchors, and status/ledger disagreement.

Run: `uv run python scripts/test_check_hooks.py`
"""

from __future__ import annotations

from pathlib import Path
import sys
import tempfile

sys.path.insert(0, str(Path(__file__).resolve().parent))

from check_hooks import check_hook, expected_status  # noqa: E402

FAILURES: list[str] = []


def build(root: Path, name: str, frontmatter: str) -> Path:
    hook_dir = root / "Domain" / "hooks"
    hook_dir.mkdir(parents=True, exist_ok=True)
    path = hook_dir / f"{name}_Integration_Hook.md"
    path.write_text(f"---\n{frontmatter}\n---\n\n# {name}\n", encoding="utf-8")
    return path


def target(root: Path, rel: str, body: str) -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body, encoding="utf-8")


def expect(label: str, problems: list[str], substring: str | None) -> None:
    """substring=None means: expect no problems at all."""
    if substring is None:
        if problems:
            FAILURES.append(f"{label}: expected clean, got {problems}")
        return
    if not any(substring in problem for problem in problems):
        FAILURES.append(f"{label}: expected {substring!r}, got {problems}")


def run() -> None:
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        target(root, "Domain/Body.md", "## Unique Heading\n\nrepeated repeated\n")

        # --- the four states, all valid -------------------------------------
        hook = build(root, "Landed", (
            'integration_status: landed\n'
            'landing_ledger:\n'
            '  - target: "Domain/Body.md"\n'
            '    state: landed\n'
            '    anchor: "## Unique Heading"'
        ))
        expect("landed/valid", check_hook(hook, root), None)

        hook = build(root, "Pending", (
            'integration_status: pending\n'
            'landing_ledger:\n'
            '  - target: "Domain/Body.md"\n'
            '    state: pending\n'
            '    blocked_by: "canonical freeze"'
        ))
        expect("pending/valid", check_hook(hook, root), None)

        hook = build(root, "Withdrawn", (
            'integration_status: withdrawn\n'
            'landing_ledger:\n'
            '  - target: "future bridge document"\n'
            '    state: withdrawn\n'
            '    withdrawn_reason: "never created"'
        ))
        expect("withdrawn/valid", check_hook(hook, root), None)

        hook = build(root, "Partial", (
            'integration_status: partial\n'
            'landing_ledger:\n'
            '  - target: "Domain/Body.md"\n'
            '    state: landed\n'
            '    anchor: "## Unique Heading"\n'
            '  - target: "Domain/Planned.md"\n'
            '    state: pending\n'
            '    target_status: planned\n'
            '    blocked_by: "synthesis doc not written yet"'
        ))
        expect("partial/valid", check_hook(hook, root), None)

        # --- error paths ----------------------------------------------------
        hook = build(root, "Escape", (
            'integration_status: pending\n'
            'landing_ledger:\n'
            '  - target: "../outside/Secret.md"\n'
            '    state: pending\n'
            '    blocked_by: "x"'
        ))
        expect("path/dotdot", check_hook(hook, root), "must not escape")

        hook = build(root, "Absolute", (
            'integration_status: pending\n'
            'landing_ledger:\n'
            '  - target: "/etc/passwd.md"\n'
            '    state: pending\n'
            '    blocked_by: "x"'
        ))
        expect("path/absolute", check_hook(hook, root), "must be repo-relative")

        hook = build(root, "NotMarkdown", (
            'integration_status: pending\n'
            'landing_ledger:\n'
            '  - target: "Domain/Body.txt"\n'
            '    state: pending\n'
            '    blocked_by: "x"'
        ))
        expect("path/suffix", check_hook(hook, root), "must be a Markdown file")

        hook = build(root, "WithdrawnNoReason", (
            'integration_status: withdrawn\n'
            'landing_ledger:\n'
            '  - target: "Domain/Body.md"\n'
            '    state: withdrawn'
        ))
        expect(
            "withdrawn/no-reason",
            check_hook(hook, root),
            "no withdrawn_reason",
        )

        hook = build(root, "Missing", (
            'integration_status: landed\n'
            'landing_ledger:\n'
            '  - target: "Domain/Nope.md"\n'
            '    state: landed\n'
            '    anchor: "x"'
        ))
        expect("target/missing", check_hook(hook, root), "does not exist")

        hook = build(root, "WeakAnchor", (
            'integration_status: landed\n'
            'landing_ledger:\n'
            '  - target: "Domain/Body.md"\n'
            '    state: landed\n'
            '    anchor: "repeated"'
        ))
        expect("anchor/not-unique", check_hook(hook, root), "occurs 2x")

        hook = build(root, "AbsentAnchor", (
            'integration_status: landed\n'
            'landing_ledger:\n'
            '  - target: "Domain/Body.md"\n'
            '    state: landed\n'
            '    anchor: "nowhere to be found"'
        ))
        expect("anchor/absent", check_hook(hook, root), "anchor not found")

        hook = build(root, "PlannedButExists", (
            'integration_status: pending\n'
            'landing_ledger:\n'
            '  - target: "Domain/Body.md"\n'
            '    state: pending\n'
            '    target_status: planned\n'
            '    blocked_by: "x"'
        ))
        expect(
            "planned/target-exists",
            check_hook(hook, root),
            "but Domain/Body.md exists",
        )

        hook = build(root, "StatusMismatch", (
            'integration_status: landed\n'
            'landing_ledger:\n'
            '  - target: "Domain/Body.md"\n'
            '    state: pending\n'
            '    blocked_by: "x"'
        ))
        expect("status/mismatch", check_hook(hook, root), "disagrees with ledger")

        hook = build(root, "NoLedger", "integration_status: landed")
        expect("ledger/empty", check_hook(hook, root), "landing_ledger is empty")

        hook = build(root, "BadStatus", (
            'integration_status: integrated\n'
            'landing_ledger:\n'
            '  - target: "Domain/Body.md"\n'
            '    state: landed\n'
            '    anchor: "## Unique Heading"'
        ))
        expect("status/enum", check_hook(hook, root), "not in (landed|partial")

    # --- aggregation semantics ---------------------------------------------
    cases = [
        ([{"state": "landed"}, {"state": "landed"}], "landed"),
        ([{"state": "landed"}, {"state": "pending"}], "partial"),
        ([{"state": "pending"}, {"state": "pending"}], "pending"),
        ([{"state": "withdrawn"}], "withdrawn"),
        # withdrawn entries do not drag an otherwise-landed hook off `landed`
        ([{"state": "landed"}, {"state": "withdrawn"}], "landed"),
    ]
    for entries, wanted in cases:
        got = expected_status(entries)
        if got != wanted:
            FAILURES.append(f"expected_status({entries}) = {got!r}, want {wanted!r}")

    if FAILURES:
        for failure in FAILURES:
            print(f"FAIL: {failure}")
        raise SystemExit(1)
    print("test_check_hooks: all cases pass")


if __name__ == "__main__":
    run()
