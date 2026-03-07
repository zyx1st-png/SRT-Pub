#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1] / "SRT"
REQUIRED = ["id", "type", "tags", "status", "dependency"]
ID_RE = re.compile(r"^[A-Z0-9]+(?:-[A-Z0-9_]+)*$")

# Non-governed content that should not block core SRT frontmatter lint.
IGNORE_DIRS = {".venv", ".obsidian", "node_modules", "papers"}
IGNORE_FILE_PATTERNS = [
    re.compile(r"^未命名(?:\s\d+)?\.md$"),
    re.compile(r"^LICENSE\.md$"),
]
IGNORE_REL_PATHS = {
    Path("_SRT_DAILY_REVIEW_LOG.md"),
}


def parse_frontmatter(text: str):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end == -1:
        return None
    block = text[4:end].splitlines()
    data = {}
    for line in block:
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip()
    return data


def should_ignore(rel: Path) -> bool:
    if rel in IGNORE_REL_PATHS:
        return True
    if any(part in IGNORE_DIRS for part in rel.parts):
        return True
    name = rel.name
    return any(pat.match(name) for pat in IGNORE_FILE_PATTERNS)


def main() -> int:
    files = sorted(ROOT.rglob("*.md"))
    checked = 0
    issues = []
    for p in files:
        rel = p.relative_to(ROOT)
        if should_ignore(rel):
            continue
        checked += 1
        txt = p.read_text(errors="ignore").lstrip("\ufeff")
        fm = parse_frontmatter(txt)
        if fm is None:
            issues.append(f"[NO_FRONTMATTER] {rel}")
            continue
        for key in REQUIRED:
            if key not in fm:
                issues.append(f"[MISSING_FIELD:{key}] {rel}")
        if "id" in fm and not ID_RE.match(fm["id"]):
            issues.append(f"[BAD_ID_FORMAT] {rel}: {fm['id']}")

    if issues:
        print("Frontmatter lint failed:\n")
        print("\n".join(issues))
        return 1

    print(f"Frontmatter lint passed ({checked} files checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
