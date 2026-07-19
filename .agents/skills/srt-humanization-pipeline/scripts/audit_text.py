#!/usr/bin/env python3
"""Compare a source draft with a humanized draft using conservative checks."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Iterable


NUMBER_RE = re.compile(r"(?<![\w.])\d+(?:\.\d+)?%?(?![\w.])")
URL_RE = re.compile(r"https?://[^\s)>\]}]+")
LINK_TARGET_RE = re.compile(r"\]\(([^)]+)\)")
CODE_SPAN_RE = re.compile(r"(?<!`)`([^`\n]+)`(?!`)")
HEADING_RE = re.compile(r"^#{1,6}\s+.+$", re.MULTILINE)
DOUBLE_QUOTE_RE = re.compile(r"[\"“]([^\"”\n]{2,})[\"”]")

PATTERNS = {
    "em_dash": "——",
    "bold_marker": "**",
    "narrator_本文": "本文",
    "narrator_这里": "这里",
    "binary_不是": "不是",
    "binary_而是": "而是",
    "emphasis_真正": "真正",
    "emphasis_必须": "必须",
}


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise RuntimeError(f"cannot read {path}: {exc}") from exc


def paragraphs(text: str) -> int:
    return sum(1 for part in re.split(r"\n\s*\n", text.strip()) if part.strip())


def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def counter_diff(before: Iterable[str], after: Iterable[str]) -> dict[str, list[str]]:
    left = Counter(before)
    right = Counter(after)
    missing = list((left - right).elements())
    added = list((right - left).elements())
    return {"missing": sorted(missing), "added": sorted(added)}


def metrics(text: str) -> dict[str, object]:
    return {
        "sha256": sha256(text),
        "bytes": len(text.encode("utf-8")),
        "characters": len(text),
        "lines": len(text.splitlines()),
        "paragraphs": paragraphs(text),
        "pattern_counts": {name: text.count(pattern) for name, pattern in PATTERNS.items()},
    }


def compare(before: str, after: str, strict: bool) -> dict[str, object]:
    hard = {
        "numbers": counter_diff(NUMBER_RE.findall(before), NUMBER_RE.findall(after)),
        "urls": counter_diff(URL_RE.findall(before), URL_RE.findall(after)),
        "markdown_link_targets": counter_diff(
            LINK_TARGET_RE.findall(before), LINK_TARGET_RE.findall(after)
        ),
    }
    review = {
        "headings": counter_diff(HEADING_RE.findall(before), HEADING_RE.findall(after)),
        "inline_code": counter_diff(CODE_SPAN_RE.findall(before), CODE_SPAN_RE.findall(after)),
        "quoted_spans": counter_diff(DOUBLE_QUOTE_RE.findall(before), DOUBLE_QUOTE_RE.findall(after)),
    }
    hard_failures = [name for name, diff in hard.items() if diff["missing"] or diff["added"]]
    review_changes = [name for name, diff in review.items() if diff["missing"] or diff["added"]]
    passed = not hard_failures and (not strict or not review_changes)
    return {
        "passed": passed,
        "strict": strict,
        "hard_failures": hard_failures,
        "review_changes": review_changes,
        "before": metrics(before),
        "after": metrics(after),
        "hard_checks": hard,
        "manual_review": review,
    }


def compact(items: list[str], limit: int = 8) -> str:
    if not items:
        return "none"
    shown = items[:limit]
    suffix = f" … (+{len(items) - limit})" if len(items) > limit else ""
    return ", ".join(json.dumps(item, ensure_ascii=False) for item in shown) + suffix


def render_markdown(result: dict[str, object], before_path: Path, after_path: Path) -> str:
    lines = [
        "# Humanization audit",
        "",
        f"- Before: `{before_path}`",
        f"- After: `{after_path}`",
        f"- Result: **{'PASS' if result['passed'] else 'FAIL'}**",
        f"- Strict review mode: `{str(result['strict']).lower()}`",
        "",
        "## Metrics",
        "",
        "| Metric | Before | After |",
        "|---|---:|---:|",
    ]
    before = result["before"]
    after = result["after"]
    for key in ("bytes", "characters", "lines", "paragraphs"):
        lines.append(f"| {key} | {before[key]} | {after[key]} |")
    lines.extend(["", "## Pattern counts", "", "| Pattern | Before | After |", "|---|---:|---:|"])
    for key, value in before["pattern_counts"].items():
        lines.append(f"| {key} | {value} | {after['pattern_counts'][key]} |")
    lines.extend(["", "## Hard checks", ""])
    for name, diff in result["hard_checks"].items():
        state = "PASS" if not diff["missing"] and not diff["added"] else "FAIL"
        lines.append(f"- **{name}: {state}**")
        if state == "FAIL":
            lines.append(f"  - missing: {compact(diff['missing'])}")
            lines.append(f"  - added: {compact(diff['added'])}")
    lines.extend(["", "## Manual review", ""])
    for name, diff in result["manual_review"].items():
        state = "unchanged" if not diff["missing"] and not diff["added"] else "changed"
        lines.append(f"- **{name}: {state}**")
        if state == "changed":
            lines.append(f"  - missing: {compact(diff['missing'])}")
            lines.append(f"  - added: {compact(diff['added'])}")
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compare protected tokens and style metrics before and after humanization."
    )
    parser.add_argument("before", type=Path)
    parser.add_argument("after", type=Path)
    parser.add_argument("--strict", action="store_true", help="Treat heading, code, and quote changes as failures.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of Markdown.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        before = read_text(args.before)
        after = read_text(args.after)
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    result = compare(before, after, args.strict)
    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(render_markdown(result, args.before, args.after))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
