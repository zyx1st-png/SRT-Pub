#!/usr/bin/env python3
"""Validate the split book-outline layout.

The master outline intentionally stays small so GitHub-style connectors can
read it without truncation. Chapter briefs live in volume-level part files.
"""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
BOOK_DIR = ROOT / "01_Source_Intuition" / "BOOK"
MASTER = BOOK_DIR / "00_全书章节写作概要.md"
PARTS_DIR = BOOK_DIR / "Outline_Parts"
README = PARTS_DIR / "README.md"

EXPECTED_PARTS = [
    "00_总览与序章.md",
    "01_卷一_从存在到成为.md",
    "02_卷二_选择的本性.md",
    "03_卷三_从选择到主体与价值.md",
    "04_卷四_秩序的双面性.md",
    "05_卷五_从个体秩序到共同秩序.md",
    "06_卷六_意识_AI_修行.md",
    "07_卷七_边界与张力.md",
    "08_收尾与维护规则.md",
]

MAX_MASTER_BYTES = 12_000
MAX_PART_BYTES = 25_000


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"missing file: {path.relative_to(ROOT)}")
    return path.read_text(encoding="utf-8")


def require_frontmatter(path: Path, text: str) -> None:
    if not text.startswith("---\n"):
        fail(f"missing frontmatter: {path.relative_to(ROOT)}")
    if "\n---\n" not in text[4:]:
        fail(f"unterminated frontmatter: {path.relative_to(ROOT)}")


def main() -> None:
    master_text = read(MASTER)
    readme_text = read(README)
    require_frontmatter(MASTER, master_text)
    require_frontmatter(README, readme_text)

    if len(master_text.encode("utf-8")) > MAX_MASTER_BYTES:
        fail(
            "master outline is too large; keep chapter briefs in Outline_Parts/"
        )

    if "role: split_master_index" not in master_text:
        fail("master outline must keep role: split_master_index")

    forbidden_master_markers = ["## 第 1 章", "## 第 52 章", "# 卷二：选择的本性"]
    for marker in forbidden_master_markers:
        if marker in master_text:
            fail(f"master outline appears to contain split body marker: {marker}")

    missing_links = []
    oversized_parts = []
    for filename in EXPECTED_PARTS:
        part = PARTS_DIR / filename
        part_text = read(part)
        require_frontmatter(part, part_text)
        if "type: book_project_outline_part" not in part_text:
            fail(f"wrong type for part: {part.relative_to(ROOT)}")
        if "canonical: false" not in part_text:
            fail(f"part must remain non-canonical: {part.relative_to(ROOT)}")
        if len(part_text.encode("utf-8")) > MAX_PART_BYTES:
            oversized_parts.append(filename)

        master_link = f"Outline_Parts/{filename}"
        if master_link not in master_text:
            missing_links.append(f"master:{filename}")
        if filename not in readme_text:
            missing_links.append(f"readme:{filename}")

    if missing_links:
        fail("missing part links: " + ", ".join(missing_links))
    if oversized_parts:
        fail("part file(s) exceed connector-safe size: " + ", ".join(oversized_parts))

    print("OK: book outline split layout is connector-safe")
    print(f"master_bytes={len(master_text.encode('utf-8'))}")
    print(f"parts={len(EXPECTED_PARTS)}")


if __name__ == "__main__":
    main()
