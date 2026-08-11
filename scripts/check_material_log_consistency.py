#!/usr/bin/env python3
"""Verify Pipeline 1 material-log row counts and root aggregates stay synchronized."""

from __future__ import annotations

from pathlib import Path
import re
import sys

from governance_common import ROOT


LOG_DIR = ROOT / "Operations" / "Material_Log"
README = LOG_DIR / "README.md"
ROOT_LOG = ROOT / "Operations" / "_SRT_MATERIAL_LOG.md"
PART_RE = re.compile(r"^\d{4}-\d{2}_Part\d{2}\.md$")
README_ROW_RE = re.compile(
    r"^\| \[(?P<part>\d{4}-\d{2}_Part\d{2})\.md\]\([^)]*\) \| (?P<count>\d+) \|"
)
ROOT_ROW_RE = re.compile(
    r"^\| (?P<part>\d{4}-\d{2}_Part\d{2}) \| .* \| (?P<count>\d+) \|\s*$"
)
CLASS_RE = re.compile(r"^\s*\*{0,2}(?P<class>[ABC])(?:\*|\s|（|\(|$)")


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def material_rows(path: Path) -> tuple[int, dict[str, int], list[str]]:
    count = 0
    classes = {"A": 0, "B": 0, "C": 0}
    errors: list[str] = []

    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.split("|")]
        if len(cells) < 6:
            continue
        if cells[1] in {"日期", "Date", "date"} or set(cells[1]) <= {"-", ":"}:
            continue

        # Pipeline 1 dated parts use: date | source | type | audit conclusion | ...
        conclusion = cells[4]
        match = CLASS_RE.match(conclusion)
        if not match:
            errors.append(f"{path.relative_to(ROOT)}:{lineno}: cannot classify audit conclusion {conclusion!r}")
            continue
        count += 1
        classes[match.group("class")] += 1

    return count, classes, errors


def parse_counts(text: str, regex: re.Pattern[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for line in text.splitlines():
        match = regex.match(line)
        if match:
            result[match.group("part")] = int(match.group("count"))
    return result


def summary_number(text: str, pattern: str, label: str, errors: list[str]) -> int | None:
    match = re.search(pattern, text)
    if not match:
        fail(errors, f"root material log: missing summary field {label}")
        return None
    return int(match.group(1))


def main() -> None:
    errors: list[str] = []
    part_paths = sorted(path for path in LOG_DIR.iterdir() if path.is_file() and PART_RE.match(path.name))
    if not part_paths:
        raise SystemExit("FAIL: no dated material-log parts found")

    actual_counts: dict[str, int] = {}
    actual_classes = {"A": 0, "B": 0, "C": 0}
    for path in part_paths:
        count, classes, row_errors = material_rows(path)
        errors.extend(row_errors)
        key = path.stem
        actual_counts[key] = count
        for cls in actual_classes:
            actual_classes[cls] += classes[cls]

    readme_text = README.read_text(encoding="utf-8")
    root_text = ROOT_LOG.read_text(encoding="utf-8")
    readme_counts = parse_counts(readme_text, README_ROW_RE)
    root_counts = parse_counts(root_text, ROOT_ROW_RE)

    for part, actual in actual_counts.items():
        if readme_counts.get(part) != actual:
            fail(errors, f"{part}: actual rows={actual}, README rows={readme_counts.get(part)!r}")
        if root_counts.get(part) != actual:
            fail(errors, f"{part}: actual rows={actual}, root rows={root_counts.get(part)!r}")

    extra_readme = sorted(set(readme_counts) - set(actual_counts))
    extra_root = sorted(set(root_counts) - set(actual_counts))
    if extra_readme:
        fail(errors, f"README references missing dated parts: {', '.join(extra_readme)}")
    if extra_root:
        fail(errors, f"root log references missing dated parts: {', '.join(extra_root)}")

    total = sum(actual_counts.values())
    summary_total = summary_number(root_text, r"- 总提交：(\d+) 条", "总提交", errors)
    summary_a = summary_number(root_text, r"- A（融入）：(\d+) 条", "A（融入）", errors)
    summary_b = summary_number(root_text, r"- B（观察）：(\d+) 条", "B（观察）", errors)
    summary_c = summary_number(root_text, r"- C（拒绝）：(\d+) 条", "C（拒绝）", errors)

    expected = {"A": actual_classes["A"], "B": actual_classes["B"], "C": actual_classes["C"]}
    reported = {"A": summary_a, "B": summary_b, "C": summary_c}
    if summary_total is not None and summary_total != total:
        fail(errors, f"root summary total={summary_total}, actual dated rows={total}")
    for cls in expected:
        if reported[cls] is not None and reported[cls] != expected[cls]:
            fail(errors, f"root summary {cls}={reported[cls]}, actual {cls} rows={expected[cls]}")

    if sum(actual_classes.values()) != total:
        fail(errors, f"A+B+C={sum(actual_classes.values())}, actual dated rows={total}")

    rate_match = re.search(r"- 融入率：([0-9]+(?:\.[0-9]+)?)%", root_text)
    if not rate_match:
        fail(errors, "root material log: missing 融入率")
    elif total:
        reported_rate = float(rate_match.group(1))
        expected_rate = round(100.0 * actual_classes["A"] / total, 1)
        if abs(reported_rate - expected_rate) > 1e-9:
            fail(errors, f"root 融入率={reported_rate:.1f}%, expected={expected_rate:.1f}%")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        print(f"material-log consistency: failures={len(errors)}")
        raise SystemExit(1)

    print(
        "PASS: material-log consistency "
        f"parts={len(actual_counts)} total={total} "
        f"A={actual_classes['A']} B={actual_classes['B']} C={actual_classes['C']}"
    )


if __name__ == "__main__":
    main()
