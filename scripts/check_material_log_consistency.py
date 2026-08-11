#!/usr/bin/env python3
"""Verify the active Pipeline 1 material log and authoritative aggregates stay synchronized.

Historical dated parts contain a small amount of acknowledged duplicated routing debt, so this
check deliberately does not reinterpret every historical physical row. It enforces the live
invariants that new writes must preserve: README/root declared part counts agree, the current
latest part's declared count matches its physical rows, declared counts sum to the root total,
and the root A/B/C summary and integration rate are arithmetically coherent.
"""

from __future__ import annotations

from pathlib import Path
import re

from governance_common import ROOT


LOG_DIR = ROOT / "Operations" / "Material_Log"
README = LOG_DIR / "README.md"
ROOT_LOG = ROOT / "Operations" / "_SRT_MATERIAL_LOG.md"
README_ROW_RE = re.compile(
    r"^\| \[(?P<part>\d{4}-\d{2}_Part\d{2})\.md\]\([^)]*\) \| (?P<count>\d+) \|"
)
ROOT_ROW_RE = re.compile(
    r"^\| (?P<part>\d{4}-\d{2}_Part\d{2}) \| .* \| (?P<count>\d+) \|\s*$"
)


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def parse_counts(text: str, regex: re.Pattern[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for line in text.splitlines():
        match = regex.match(line)
        if match:
            result[match.group("part")] = int(match.group("count"))
    return result


def physical_row_count(path: Path) -> int:
    count = 0
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.split("|")]
        if len(cells) < 6:
            continue
        if cells[1] in {"日期", "Date", "date"} or set(cells[1]) <= {"-", ":"}:
            continue
        count += 1
    return count


def summary_number(text: str, pattern: str, label: str, errors: list[str]) -> int | None:
    match = re.search(pattern, text)
    if not match:
        fail(errors, f"root material log: missing summary field {label}")
        return None
    return int(match.group(1))


def main() -> None:
    errors: list[str] = []
    readme_text = README.read_text(encoding="utf-8")
    root_text = ROOT_LOG.read_text(encoding="utf-8")
    readme_counts = parse_counts(readme_text, README_ROW_RE)
    root_counts = parse_counts(root_text, ROOT_ROW_RE)

    if not readme_counts:
        raise SystemExit("FAIL: no dated material-log routes found in README")

    if set(readme_counts) != set(root_counts):
        missing_root = sorted(set(readme_counts) - set(root_counts))
        missing_readme = sorted(set(root_counts) - set(readme_counts))
        if missing_root:
            fail(errors, f"root log missing parts declared by README: {', '.join(missing_root)}")
        if missing_readme:
            fail(errors, f"README missing parts declared by root log: {', '.join(missing_readme)}")

    for part in sorted(set(readme_counts) & set(root_counts)):
        if readme_counts[part] != root_counts[part]:
            fail(
                errors,
                f"{part}: README rows={readme_counts[part]}, root rows={root_counts[part]}",
            )

    # New Pipeline 1 writes append to the lexicographically latest dated part. Enforce that
    # active surface against the file itself without turning known historical duplicate rows
    # into unrelated PR blockers.
    latest_part = max(readme_counts)
    latest_path = LOG_DIR / f"{latest_part}.md"
    if not latest_path.is_file():
        fail(errors, f"latest declared part does not exist: {latest_path.relative_to(ROOT)}")
    else:
        physical = physical_row_count(latest_path)
        declared = readme_counts[latest_part]
        if physical != declared:
            fail(errors, f"{latest_part}: physical rows={physical}, declared rows={declared}")

    declared_total = sum(readme_counts.values())
    summary_total = summary_number(root_text, r"- 总提交：(\d+) 条", "总提交", errors)
    summary_a = summary_number(root_text, r"- A（融入）：(\d+) 条", "A（融入）", errors)
    summary_b = summary_number(root_text, r"- B（观察）：(\d+) 条", "B（观察）", errors)
    summary_c = summary_number(root_text, r"- C（拒绝）：(\d+) 条", "C（拒绝）", errors)

    if summary_total is not None and summary_total != declared_total:
        fail(errors, f"root summary total={summary_total}, declared part total={declared_total}")

    if None not in {summary_a, summary_b, summary_c, summary_total}:
        class_total = int(summary_a) + int(summary_b) + int(summary_c)
        if class_total != summary_total:
            fail(errors, f"root A+B+C={class_total}, total={summary_total}")

    rate_match = re.search(r"- 融入率：([0-9]+(?:\.[0-9]+)?)%", root_text)
    if not rate_match:
        fail(errors, "root material log: missing 融入率")
    elif summary_total and summary_a is not None:
        reported_rate = float(rate_match.group(1))
        expected_rate = round(100.0 * summary_a / summary_total, 1)
        if abs(reported_rate - expected_rate) > 1e-9:
            fail(errors, f"root 融入率={reported_rate:.1f}%, expected={expected_rate:.1f}%")

    if errors:
        for error in errors:
            print(f"FAIL: {error}")
        print(f"material-log consistency: failures={len(errors)}")
        raise SystemExit(1)

    print(
        "PASS: material-log consistency "
        f"parts={len(readme_counts)} latest={latest_part}:{readme_counts[latest_part]} "
        f"total={summary_total} A={summary_a} B={summary_b} C={summary_c}"
    )


if __name__ == "__main__":
    main()
