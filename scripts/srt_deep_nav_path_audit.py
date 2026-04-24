#!/usr/bin/env python3
"""
SRT Deep Navigation Path Audit

Purpose
-------
Validate that path-like references in SRT navigation files point to existing
files or directories in the repository.

This script is intentionally conservative: it audits navigation references,
not theoretical correctness.

Usage
-----
Run from repository root:

    python scripts/srt_deep_nav_path_audit.py

Optional:

    python scripts/srt_deep_nav_path_audit.py --report Operations/_SRT_DEEP_NAV_PATH_AUDIT_REPORT.md
    python scripts/srt_deep_nav_path_audit.py --json Operations/_SRT_DEEP_NAV_PATH_AUDIT_REPORT.json

Exit codes
----------
0 = no missing required paths
1 = missing required paths found

Notes
-----
- Graphify outputs are allowed, but reported separately as generated-support paths.
- Directory references are allowed when the directory exists.
- Non-path code spans such as `Ψ_f`, `d-value`, `L0 -> L1`, LaTeX, and symbolic
  expressions are ignored.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

DEFAULT_NAV_FILES = [
    "_SRT_INDEX.md",
    "_SRT_CONTEXT_ROUTER.md",
    "_SRT_DEEP_THEORY_MAP.md",
    "Bridge/SRT_Adjacent_Theory_Interface_Index.md",
    "Operations/_SRT_DEEP_NAV_TODO.md",
]

PATH_EXTENSIONS = (
    ".md",
    ".yaml",
    ".yml",
    ".json",
    ".html",
    ".htm",
    ".py",
    ".sh",
    ".csv",
    ".txt",
)

IGNORE_PREFIXES = (
    "http://",
    "https://",
    "source:",
    "user-material:",
)

SYMBOLIC_TOKENS = {
    "Ψ_f",
    "Psi_f",
    "d-value",
    "d",
    "T_dir",
    "L0",
    "L1",
    "L2",
    "L_0",
    "L_1",
    "L_2",
    "Ĝ",
    "Ĝθ",
    "g_F",
    "D_eff",
    "FEP",
    "IIT",
    "GNW",
}

@dataclass
class PathRef:
    source_file: str
    line: int
    raw: str
    normalized: str
    status: str
    note: str = ""


def repo_root() -> Path:
    try:
        out = subprocess.check_output(["git", "rev-parse", "--show-toplevel"], text=True).strip()
        return Path(out)
    except Exception:
        return Path.cwd()


def git_files(root: Path) -> set[str]:
    try:
        out = subprocess.check_output(["git", "ls-files"], cwd=root, text=True)
        return {line.strip() for line in out.splitlines() if line.strip()}
    except Exception:
        files: set[str] = set()
        for p in root.rglob("*"):
            if p.is_file() and ".git" not in p.parts:
                files.add(p.relative_to(root).as_posix())
        return files


def git_dirs(files: Iterable[str]) -> set[str]:
    dirs: set[str] = set()
    for f in files:
        parts = Path(f).parts
        for i in range(1, len(parts)):
            dirs.add(Path(*parts[:i]).as_posix())
    return dirs


def extract_code_spans(line: str) -> list[str]:
    return re.findall(r"`([^`]+)`", line)


def looks_like_path(token: str) -> bool:
    t = token.strip()
    if not t or t in SYMBOLIC_TOKENS:
        return False
    if t.startswith(IGNORE_PREFIXES):
        return False
    if any(ch in t for ch in ["\\", "$", "{", "}", "=", "→"]):
        return False
    if " " in t and not any(ext in t for ext in PATH_EXTENSIONS):
        return False
    if t.endswith(PATH_EXTENSIONS):
        return True
    if "/" in t and not re.search(r"\s", t):
        return True
    return False


def normalize_path(token: str) -> str:
    t = token.strip()
    t = t.strip("'\"")
    t = t.lstrip("./")
    # Drop anchors in markdown-like references if users put them inside code spans.
    t = t.split("#", 1)[0]
    return t


def audit_file(root: Path, source: str, files: set[str], dirs: set[str]) -> list[PathRef]:
    path = root / source
    refs: list[PathRef] = []
    if not path.exists():
        refs.append(PathRef(source, 0, source, source, "nav_file_missing"))
        return refs

    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), start=1):
        for raw in extract_code_spans(line):
            if not looks_like_path(raw):
                continue
            norm = normalize_path(raw)
            if not norm:
                continue
            if norm in files:
                status = "ok_file"
            elif norm in dirs or norm.rstrip("/") in dirs:
                status = "ok_dir"
            else:
                status = "missing"
            note = "generated_support" if norm.startswith("graphify-out/") else ""
            refs.append(PathRef(source, i, raw, norm, status, note))
    return refs


def build_markdown_report(refs: list[PathRef], repo_file_count: int) -> str:
    missing = [r for r in refs if r.status == "missing"]
    graphify = [r for r in refs if r.note == "generated_support"]
    ok = [r for r in refs if r.status.startswith("ok_")]

    lines: list[str] = []
    lines.append("---")
    lines.append("id: SRT-DEEP-NAV-PATH-AUDIT-REPORT")
    lines.append("type: audit_report")
    lines.append("tags: [Navigation, Path Audit, Retrieval]")
    lines.append("status: generated")
    lines.append("layer: operations")
    lines.append("epistemic_layer: meta")
    lines.append("claim_mode: navigation")
    lines.append("---")
    lines.append("")
    lines.append("# SRT Deep Navigation Path Audit Report")
    lines.append("")
    lines.append("> Generated by `scripts/srt_deep_nav_path_audit.py`.")
    lines.append("")
    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Repository tracked files: `{repo_file_count}`")
    lines.append(f"- Path-like references checked: `{len(refs)}`")
    lines.append(f"- Existing references: `{len(ok)}`")
    lines.append(f"- Missing references: `{len(missing)}`")
    lines.append(f"- Graphify support references: `{len(graphify)}`")
    lines.append("")

    if missing:
        lines.append("## Missing References")
        lines.append("")
        lines.append("| Source | Line | Referenced path |")
        lines.append("|---|---:|---|")
        for r in missing:
            lines.append(f"| `{r.source_file}` | {r.line} | `{r.normalized}` |")
        lines.append("")
    else:
        lines.append("## Missing References")
        lines.append("")
        lines.append("No missing required path-like references found.")
        lines.append("")

    lines.append("## Graphify Support References")
    lines.append("")
    if graphify:
        lines.append("These exist but should remain support-only unless promoted elsewhere.")
        lines.append("")
        lines.append("| Source | Line | Referenced path |")
        lines.append("|---|---:|---|")
        for r in graphify:
            lines.append(f"| `{r.source_file}` | {r.line} | `{r.normalized}` |")
    else:
        lines.append("No graphify support references detected.")
    lines.append("")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--nav-file", action="append", default=[], help="Navigation file to audit. Can repeat.")
    parser.add_argument("--report", default="", help="Write markdown report to this path.")
    parser.add_argument("--json", default="", help="Write JSON report to this path.")
    args = parser.parse_args()

    root = repo_root()
    files = git_files(root)
    dirs = git_dirs(files)
    nav_files = args.nav_file or DEFAULT_NAV_FILES

    refs: list[PathRef] = []
    for source in nav_files:
        refs.extend(audit_file(root, source, files, dirs))

    missing = [r for r in refs if r.status == "missing"]
    report_md = build_markdown_report(refs, len(files))

    if args.report:
        out = root / args.report
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(report_md, encoding="utf-8")
    else:
        print(report_md)

    if args.json:
        out_json = root / args.json
        out_json.parent.mkdir(parents=True, exist_ok=True)
        out_json.write_text(json.dumps([asdict(r) for r in refs], ensure_ascii=False, indent=2), encoding="utf-8")

    return 1 if missing else 0


if __name__ == "__main__":
    raise SystemExit(main())
