#!/usr/bin/env python3
"""
SRT Deep Navigation Coverage Audit

Purpose
-------
Find tracked repository files that are not referenced by the SRT navigation
layer, then classify which unreferenced files are likely deep-content candidates
for future routing.

Complements `scripts/srt_deep_nav_path_audit.py`:
- path audit: referenced path -> does it exist?
- coverage audit: repository file -> is it referenced by the navigation layer?
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
from collections import defaultdict
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable

DEFAULT_NAV_FILES = [
    "README.md",
    "AGENTS.md",
    "SRT_AI_START.md",
    "SRT_Navigation_Map.md",
    "_SRT_INDEX.md",
    "_SRT_CONTEXT_ROUTER.md",
    "_SRT_DEEP_THEORY_MAP.md",
    "_SRT_HIGH_PRIORITY_CORE_COVERAGE_INDEX.md",
    "_SRT_MEDIUM_AI_NEURO_COVERAGE_INDEX.md",
    "_SRT_MEDIUM_PHILOSOPHY_COVERAGE_INDEX.md",
    "_SRT_MEDIUM_PHYSICS_COVERAGE_INDEX.md",
    "_SRT_MEDIUM_SPIRITUALITY_COVERAGE_INDEX.md",
    "_SRT_MEDIUM_PAPERS_PUBLICATION_COVERAGE_INDEX.md",
    "_SRT_MEDIUM_ROOT_TOPIC_FAQ_COVERAGE_INDEX.md",
    "Bridge/SRT_Adjacent_Theory_Interface_Index.md",
    "Governance/README.md",
    "Operations/README.md",
    "Operations/_SRT_DEEP_NAV_TODO.md",
    "Operations/_SRT_DEEP_NAV_AUDIT_2026-04-24.md",
]

THEORY_EXTENSIONS = (".md", ".markdown", ".html", ".htm")
PATH_EXTENSIONS = (".md", ".markdown", ".yaml", ".yml", ".json", ".html", ".htm", ".py", ".sh", ".csv", ".txt")

IGNORE_FILE_PATTERNS = (
    r"^\.git/",
    r"^\.DS_Store$",
    r"^node_modules/",
    r"^\.venv/",
    r"^venv/",
    r"^__pycache__/",
    r"\.pyc$",
    r"^data/",
    r"^assets/",
    r"^images/",
    r"^figures/",
    r"^graphify-out/root_snapshots/",
    r"^graphify-out/.*\.json$",
    r"^Operations/_SRT_DEEP_NAV_.*REPORT\.(md|json)$",
)

SUPPORT_ONLY_PATTERNS = (
    r"(^|/)Archive/",
    r"(^|/)memory/",
    r"(^|/)Operations/",
    r"(^|/)graphify-out/wiki/",
    r"(^|/)README\.md$",
    r"(^|/)[^/]*(Split|Annex)/",
    r"(_SPLIT_PLAN|_Merge_Targets_|_AUDIT|_CHANGELOG|_LOG|_PLAN|_TEMPLATE)",
    r"(_GUIDE|_PIPELINE|_SCORECARD|_METRICS|_RELEASE|_HISTORY|_REVIEW)",
)

LOW_PRIORITY_PREFIXES = ("Archive/", "memory/", "graphify-out/wiki/")
HIGH_PRIORITY_PREFIXES = ("Core/", "Core_Law/", "Governance/")
MEDIUM_PRIORITY_PREFIXES = ("AI/", "Neuroscience/", "Physics/", "Philosophy/", "Spirituality/", "Bridge/", "papers/")
ROOT_DEEP_PREFIXES = ("SRT_", "_SRT_", "CANONICAL_", "ANNEX_", "LONGFORM_")
SYMBOLIC_TOKENS = {"Ψ_f", "Psi_f", "d-value", "d", "T_dir", "L0", "L1", "L2", "L_0", "L_1", "L_2", "Ĝ", "Ĝθ", "g_F", "D_eff", "FEP", "IIT", "GNW"}


@dataclass
class FileCoverage:
    path: str
    top_dir: str
    referenced: bool
    priority: str
    reason: str
    covered_by: str = ""


def repo_root() -> Path:
    try:
        return Path(subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip())
    except Exception:
        return Path.cwd()


def git_files(root: Path) -> set[str]:
    try:
        out = subprocess.check_output(["git", "ls-files", "-z"], cwd=root)
        return {x for x in out.decode("utf-8", errors="surrogateescape").split("\0") if x}
    except Exception:
        return {p.relative_to(root).as_posix() for p in root.rglob("*") if p.is_file() and ".git" not in p.parts}


def git_dirs(files: Iterable[str]) -> set[str]:
    dirs: set[str] = set()
    for f in files:
        parts = Path(f).parts
        for i in range(1, len(parts)):
            dirs.add(Path(*parts[:i]).as_posix())
    return dirs


def should_ignore_file(path: str) -> bool:
    return any(re.search(pattern, path) for pattern in IGNORE_FILE_PATTERNS)


def is_support_only_file(path: str) -> bool:
    return any(re.search(pattern, path) for pattern in SUPPORT_ONLY_PATTERNS)


def is_theory_like(path: str) -> bool:
    return path.endswith(THEORY_EXTENSIONS)


def extract_code_spans(text: str) -> list[str]:
    return re.findall(r"`([^`]+)`", text)


def extract_markdown_links(text: str) -> list[str]:
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", text)


def extract_bare_path_candidates(text: str) -> list[str]:
    return re.findall(r"(?<![\w./-])(?:[A-Za-z0-9_.-]+/)+[A-Za-z0-9_.+@%=-]+(?:\.[A-Za-z0-9]+)?", text)


def looks_like_path(token: str) -> bool:
    t = token.strip().strip("'\"")
    if not t or t in SYMBOLIC_TOKENS or t.startswith(("http://", "https://", "mailto:", "#")):
        return False
    if any(ch in t for ch in ["\\", "$", "{", "}", "=", "→"]):
        return False
    if " " in t and not any(ext in t for ext in PATH_EXTENSIONS):
        return False
    return t.endswith(PATH_EXTENSIONS) or ("/" in t and not re.search(r"\s", t))


def normalize_path(token: str) -> str:
    t = token.strip().strip("'\"<>")
    t = t.split("#", 1)[0].split("?", 1)[0]
    return t.rstrip(".,;:，。；：、").lstrip("./")


def collect_referenced_paths(root: Path, nav_files: list[str], files: set[str]) -> tuple[set[str], set[str]]:
    refs: set[str] = set()
    dir_refs: set[str] = set()
    dirs = git_dirs(files)
    nav_texts: list[str] = []

    for nav in nav_files:
        p = root / nav
        if not p.exists():
            continue
        text = p.read_text(encoding="utf-8")
        nav_texts.append(text)
        if nav in files:
            refs.add(nav)
        candidates = extract_code_spans(text) + extract_markdown_links(text) + extract_bare_path_candidates(text)
        for c in candidates:
            if not looks_like_path(c):
                continue
            norm = normalize_path(c)
            if norm in dirs:
                dir_refs.add(norm)
            elif norm.rstrip("/") in dirs:
                dir_refs.add(norm.rstrip("/"))
            else:
                refs.add(norm)

    combined_text = "\n".join(nav_texts)
    for f in files:
        if f in combined_text:
            refs.add(f)
    for d in dirs:
        explicit_dir_pattern = rf"(?<![\w./-]){re.escape(d)}/(?=$|[\s`),.;:，。；：、\]])"
        if re.search(explicit_dir_pattern, combined_text):
            dir_refs.add(d)

    return refs, dir_refs


def top_dir(path: str) -> str:
    parts = path.split("/")
    return parts[0] if len(parts) > 1 else "."


def find_covering_dir(path: str, dir_refs: set[str]) -> str:
    candidates = [d for d in dir_refs if path.startswith(f"{d.rstrip('/')}/")]
    return max(candidates, key=len) if candidates else ""


def classify_priority(path: str, referenced: bool, covered_by: str = "") -> tuple[str, str]:
    if referenced:
        return ("referenced", f"covered by navigation directory reference `{covered_by}`") if covered_by else ("referenced", "exact path referenced by navigation layer")
    if should_ignore_file(path):
        return "ignored", "ignored generated/data/cache/report pattern"
    if not is_theory_like(path):
        return "ignored", "non-theory extension"
    if is_support_only_file(path):
        return "low", "support/split/annex/operations artifact; review only if repeatedly useful"
    if path.startswith(LOW_PRIORITY_PREFIXES):
        return "low", "generated/archive/memory support; review only if reusable"
    if path.startswith(HIGH_PRIORITY_PREFIXES):
        return "high", "core/governance file not referenced by navigation"
    if path.startswith(MEDIUM_PRIORITY_PREFIXES):
        return "medium", "domain or paper theory file not referenced by navigation"
    if any(path.startswith(prefix) for prefix in ROOT_DEEP_PREFIXES):
        return "medium", "root-level SRT/theory file not referenced by navigation"
    if path.endswith("README.md"):
        return "low", "readme-like file not referenced"
    return "low", "unreferenced theory-like file"


def build_coverage(files: set[str], refs: set[str], dir_refs: set[str]) -> list[FileCoverage]:
    coverage: list[FileCoverage] = []
    for f in sorted(files):
        covered_by = "" if f in refs else find_covering_dir(f, dir_refs)
        referenced = f in refs or bool(covered_by)
        priority, reason = classify_priority(f, referenced, covered_by)
        coverage.append(FileCoverage(f, top_dir(f), referenced, priority, reason, covered_by))
    return coverage


def group_by_priority(coverage: Iterable[FileCoverage]) -> dict[str, list[FileCoverage]]:
    groups: dict[str, list[FileCoverage]] = defaultdict(list)
    for item in coverage:
        groups[item.priority].append(item)
    return groups


def group_unreferenced_by_dir(coverage: Iterable[FileCoverage]) -> dict[str, list[FileCoverage]]:
    groups: dict[str, list[FileCoverage]] = defaultdict(list)
    for item in coverage:
        if not item.referenced and item.priority != "ignored":
            groups[item.top_dir].append(item)
    return groups


def build_markdown_report(coverage: list[FileCoverage], refs: set[str], dir_refs: set[str], nav_files: list[str]) -> str:
    groups = group_by_priority(coverage)
    unref_groups = group_unreferenced_by_dir(coverage)
    total = len(coverage)
    referenced = len(groups.get("referenced", []))
    ignored = len(groups.get("ignored", []))
    high = len(groups.get("high", []))
    medium = len(groups.get("medium", []))
    low = len(groups.get("low", []))

    lines: list[str] = [
        "---",
        "id: SRT-DEEP-NAV-COVERAGE-AUDIT-REPORT",
        "type: audit_report",
        "tags: [Navigation, Coverage Audit, Retrieval]",
        "status: generated",
        "layer: operations",
        "epistemic_layer: meta",
        "claim_mode: navigation",
        "---",
        "",
        "# SRT Deep Navigation Coverage Audit Report",
        "",
        "> Generated by `scripts/srt_deep_nav_coverage_audit.py`.",
        "",
        "## Summary",
        "",
        f"- Tracked files checked: `{total}`",
        f"- Navigation files scanned: `{len(nav_files)}`",
        f"- Unique navigation references detected: `{len(refs)}`",
        f"- Directory references detected: `{len(dir_refs)}`",
        f"- Referenced tracked files: `{referenced}`",
        f"- Ignored files: `{ignored}`",
        f"- Unreferenced high-priority candidates: `{high}`",
        f"- Unreferenced medium-priority candidates: `{medium}`",
        f"- Unreferenced low-priority candidates: `{low}`",
        "",
        "Interpretation: high/medium/low are review priorities, not proof that a file must be added to navigation.",
        "",
        "## Navigation Sources",
        "",
    ]
    lines.extend(f"- `{nav}`" for nav in nav_files)
    lines.append("")

    for priority, title in [("high", "High-Priority Unreferenced Candidates"), ("medium", "Medium-Priority Unreferenced Candidates"), ("low", "Low-Priority Unreferenced Candidates")]:
        items = groups.get(priority, [])
        lines.extend([f"## {title}", ""])
        if not items:
            lines.extend(["None.", ""])
            continue
        lines.extend(["| Path | Reason |", "|---|---|"])
        for item in items[:300]:
            lines.append(f"| `{item.path}` | {item.reason} |")
        if len(items) > 300:
            lines.append(f"| ... | truncated; {len(items) - 300} more |")
        lines.append("")

    lines.extend(["## Unreferenced Candidates by Top-Level Directory", "", "| Directory | Count |", "|---|---:|"])
    for d, items in sorted(unref_groups.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        lines.append(f"| `{d}` | {len(items)} |")
    lines.extend([
        "",
        "## Suggested Review Workflow",
        "",
        "1. Review high-priority candidates first.",
        "2. Decide whether each candidate should be added to `_SRT_CONTEXT_ROUTER.md`, `_SRT_DEEP_THEORY_MAP.md`, `_SRT_INDEX.md`, or none.",
        "3. Review medium-priority domain and paper files next.",
        "4. Treat graphify, memory, and archive files as support-only unless a page is repeatedly useful.",
        "5. Do not add every unreferenced file to navigation; the goal is retrieval quality, not exhaustive listing.",
        "",
    ])
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--nav-file", action="append", default=[], help="Navigation file to use for reference extraction. Can repeat.")
    parser.add_argument("--report", default="", help="Write markdown report to this path.")
    parser.add_argument("--json", default="", help="Write JSON report to this path.")
    args = parser.parse_args()

    root = repo_root()
    files = git_files(root)
    nav_files = args.nav_file or DEFAULT_NAV_FILES
    refs, dir_refs = collect_referenced_paths(root, nav_files, files)
    coverage = build_coverage(files, refs, dir_refs)
    report = build_markdown_report(coverage, refs, dir_refs, nav_files)

    if args.report:
        out = root / args.report
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(report, encoding="utf-8")
    else:
        print(report)

    if args.json:
        out_json = root / args.json
        out_json.parent.mkdir(parents=True, exist_ok=True)
        out_json.write_text(json.dumps([asdict(x) for x in coverage], ensure_ascii=False, indent=2), encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
