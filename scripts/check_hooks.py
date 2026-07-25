#!/usr/bin/env python3
"""Check IntegrationHook closure ledgers.

Pipeline 1 (`Operations/_SRT_MATERIAL_PIPELINE.md` §5.6) ends at the
IntegrationHook: the record of how a material patch is meant to reach body
text. Before the 2026-07-25 closure audit there was no machine check that a
hook's declared target existed, or that a hook claiming to be integrated had
actually landed. Three Physics hooks pointed at a file that never existed and
four Philosophy hooks silently carried unlanded canonical targets.

This checker enforces the closure ledger:

    integration_status: landed | partial | pending | withdrawn
    landing_ledger:
      - target: <repo-relative .md path>
        state: landed | pending | withdrawn
        anchor: "<literal substring that must occur in target>"   # landed only
        blocked_by: "<reason>"                                    # pending only
        target_status: planned      # target document does not exist yet

Rules:
1. Every hook under `*/hooks/*_Integration_Hook.md` must declare
   `integration_status` and a non-empty `landing_ledger`.
2. Every ledger target must exist, whatever its state. Two escapes, both of
   which force the absence to be stated rather than hidden: a `withdrawn` entry
   carrying `withdrawn_reason`, and a `pending` entry carrying
   `target_status: planned` (a synthesis document that is planned but has never
   been created — a real category here, e.g. the Physics bridge v0.2 doc that
   three 2026-04 hooks were written against).
3. Every `landed` entry must carry an `anchor` that literally occurs in the
   target file. This is what makes "已融入" checkable rather than self-reported.
4. `integration_status` must agree with the ledger: all landed -> `landed`;
   none landed -> `pending`; mixed -> `partial`; all withdrawn -> `withdrawn`.

The frontmatter parser in `governance_common` is line-oriented and does not
handle nested lists, so the ledger is parsed here directly from the raw block.
"""

from __future__ import annotations

from pathlib import Path
import argparse
import re
import sys

from governance_common import ROOT, read_text, relpath, should_skip

HOOK_GLOB = "*_Integration_Hook.md"
LEDGER_STATES = {"landed", "pending", "withdrawn"}
HOOK_STATUSES = {"landed", "partial", "pending", "withdrawn"}


def iter_hooks() -> list[Path]:
    hooks: list[Path] = []
    for path in ROOT.rglob(HOOK_GLOB):
        if should_skip(path) or not path.is_file():
            continue
        if path.parent.name != "hooks":
            # Legacy domain-root hook bundles predate the `hooks/` convention
            # and are tracked in the audit record, not by this checker.
            continue
        hooks.append(path)
    return sorted(hooks)


def frontmatter_block(text: str) -> str | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    return text[4:end]


def parse_ledger(block: str) -> tuple[str, list[dict[str, str]]]:
    """Return (integration_status, ledger entries) from a frontmatter block."""
    status = ""
    entries: list[dict[str, str]] = []
    in_ledger = False
    current: dict[str, str] | None = None

    for line in block.splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        stripped = line.strip()

        if not line.startswith((" ", "\t", "-")):
            in_ledger = False
            if current is not None:
                entries.append(current)
                current = None
            key, _, value = stripped.partition(":")
            key = key.strip()
            if key == "integration_status":
                status = value.strip().strip("\"'")
            elif key == "landing_ledger":
                in_ledger = True
            continue

        if not in_ledger:
            continue

        if stripped.startswith("- "):
            if current is not None:
                entries.append(current)
            current = {}
            stripped = stripped[2:].strip()
        if current is None or ":" not in stripped:
            continue
        key, _, value = stripped.partition(":")
        current[key.strip()] = value.strip().strip("\"'")

    if current is not None:
        entries.append(current)
    return status, entries


def expected_status(entries: list[dict[str, str]]) -> str:
    states = [entry.get("state", "") for entry in entries]
    active = [state for state in states if state != "withdrawn"]
    if not active:
        return "withdrawn"
    if all(state == "landed" for state in active):
        return "landed"
    if not any(state == "landed" for state in active):
        return "pending"
    return "partial"


def check_hook(path: Path) -> list[str]:
    rel = relpath(path)
    problems: list[str] = []
    block = frontmatter_block(read_text(path))
    if block is None:
        return [f"{rel}: missing or malformed frontmatter"]

    status, entries = parse_ledger(block)
    if status not in HOOK_STATUSES:
        problems.append(
            f"{rel}: integration_status `{status or '<absent>'}` not in "
            f"({'|'.join(sorted(HOOK_STATUSES))})"
        )
    if not entries:
        problems.append(f"{rel}: landing_ledger is empty or absent")
        return problems

    for index, entry in enumerate(entries, start=1):
        label = f"{rel}: landing_ledger[{index}]"
        target = entry.get("target", "")
        state = entry.get("state", "")
        if state not in LEDGER_STATES:
            problems.append(
                f"{label}: state `{state or '<absent>'}` not in "
                f"({'|'.join(sorted(LEDGER_STATES))})"
            )
        if not target:
            problems.append(f"{label}: missing target")
            continue

        planned = entry.get("target_status", "") == "planned"
        target_path = ROOT / target
        if not target_path.is_file():
            if state == "withdrawn" and entry.get("withdrawn_reason"):
                continue
            if state == "pending" and planned and entry.get("blocked_by"):
                continue
            problems.append(f"{label}: target does not exist: {target}")
            continue
        if planned:
            problems.append(
                f"{label}: target_status `planned` but {target} exists — "
                "resolve the entry instead of leaving it planned"
            )

        if state == "landed":
            anchor = entry.get("anchor", "")
            if not anchor:
                problems.append(f"{label}: landed entry has no anchor")
            elif anchor not in read_text(target_path):
                problems.append(
                    f"{label}: anchor not found in {target}: {anchor!r}"
                )
        elif state == "pending" and not entry.get("blocked_by"):
            problems.append(f"{label}: pending entry has no blocked_by reason")

    wanted = expected_status(entries)
    if status in HOOK_STATUSES and status != wanted:
        problems.append(
            f"{rel}: integration_status `{status}` disagrees with ledger "
            f"(expected `{wanted}`)"
        )
    return problems


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Reserved for future warning escalation; currently a no-op.",
    )
    parser.parse_args()

    hooks = iter_hooks()
    problems: list[str] = []
    for hook in hooks:
        problems.extend(check_hook(hook))

    for problem in problems:
        print(f"ERROR: {problem}")
    print(f"hooks: checked={len(hooks)} errors={len(problems)}")
    raise SystemExit(1 if problems else 0)


if __name__ == "__main__":
    main()
