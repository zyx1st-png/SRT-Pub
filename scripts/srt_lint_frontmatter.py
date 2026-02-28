#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1] / "SRT"
REQUIRED = ["id", "type", "tags", "status", "dependency"]
ID_RE = re.compile(r"^[A-Z0-9]+(?:-[A-Z0-9_]+)*$")


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


def main() -> int:
    files = sorted(ROOT.rglob("*.md"))
    issues = []
    for p in files:
        txt = p.read_text(errors="ignore").lstrip("\ufeff")
        fm = parse_frontmatter(txt)
        rel = p.relative_to(ROOT)
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

    print(f"Frontmatter lint passed ({len(files)} files checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
