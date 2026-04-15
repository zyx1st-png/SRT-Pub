#!/usr/bin/env python3
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1] / "SRT"
IGNORE_DIRS = {".venv", ".obsidian", "papers", "node_modules"}
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def is_external(target: str) -> bool:
    t = target.strip().lower()
    return t.startswith("http://") or t.startswith("https://") or t.startswith("mailto:") or t.startswith("#")


def main() -> int:
    issues = []
    files = sorted(
        p for p in ROOT.rglob("*.md")
        if not any(part in IGNORE_DIRS for part in p.relative_to(ROOT).parts)
    )
    for p in files:
        txt = p.read_text(errors="ignore")
        rel = p.relative_to(ROOT)
        for raw in LINK_RE.findall(txt):
            target = raw.split(" ")[0].split("#")[0].strip()
            if not target or is_external(target):
                continue
            # 避免把 LaTeX/数学文本误识别为链接目标
            if "/" not in target and "." not in target:
                continue
            if not target.endswith((".md", ".yaml", ".yml", ".png", ".jpg", ".jpeg", ".pdf")):
                continue
            tgt = (p.parent / target).resolve()
            if not tgt.exists():
                issues.append(f"[BROKEN_LINK] {rel} -> {raw}")

    if issues:
        print("Link check failed:\n")
        print("\n".join(issues))
        return 1

    print(f"Link check passed ({len(files)} files checked).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
