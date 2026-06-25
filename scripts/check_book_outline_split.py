#!/usr/bin/env python3
"""Validate the current book manuscript layout.

The old 52-chapter outline split was archived. The current mainline lives in
01_Source_Intuition/BOOK/Drafts_26Q/ as Q00 through Q28 plus the appendix.
"""

from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
BOOK_DIR = ROOT / "01_Source_Intuition" / "BOOK"
STATUS = BOOK_DIR / "BOOK_CURRENT_STATUS.md"
DRAFTS_DIR = BOOK_DIR / "Drafts_26Q"

EXPECTED_DRAFTS = [
    "致读者.md",
    "Q00_序章.md",
    "Q01_给定性.md",
    "Q02_对象化.md",
    "Q03_前对象场.md",
    "Q04_最低非中立性.md",
    "幕间桥_一二幕.md",
    "幕前_二幕.md",
    "Q04b_选材.md",
    "Q05_选择不是挑选.md",
    "Q06_排除与阴影.md",
    "Q07_锚定.md",
    "Q08_不可逆性.md",
    "Q09_现实厚度.md",
    "Q10_秩序背景化.md",
    "幕间桥_二三幕.md",
    "幕前_三幕.md",
    "Q11_被选择.md",
    "Q12_攸关.md",
    "Q13_在乎.md",
    "Q14_价值不是偏好.md",
    "Q15_关切维度.md",
    "Q15b_能动性.md",
    "Q16_主体沉积.md",
    "Q17_意识.md",
    "幕间桥_三四幕.md",
    "幕前_四幕.md",
    "Q18_秩序与自由.md",
    "Q19_脚手架与牢笼.md",
    "Q20_遮蔽.md",
    "Q21_苦难.md",
    "Q22_方向.md",
    "幕间桥_四五幕.md",
    "幕前_五幕.md",
    "Q23_共同体.md",
    "幕间桥_Q23_Q24.md",
    "Q24_AI.md",
    "幕间桥_Q24_Q25.md",
    "Q25_选择广于意识.md",
    "Q26_可证伪性.md",
    "Q27_理论自反.md",
    "Q28_回到生成.md",
    "附录_三问使用指南.md",
    "附录_跨域难题_重述而非解决.md",
    "附录_术语表.md",
]

MAX_DRAFT_BYTES = 45_000


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
    status_text = read(STATUS)
    require_frontmatter(STATUS, status_text)
    if "Drafts_26Q/" not in status_text:
        fail("BOOK_CURRENT_STATUS must point to Drafts_26Q/")

    missing = []
    oversized = []
    for filename in EXPECTED_DRAFTS:
        path = DRAFTS_DIR / filename
        text = read(path)
        require_frontmatter(path, text)
        # Book drafts must remain non-canonical source text. The real convention
        # is claim_mode: companion_exposition (致读者 uses navigation; the glossary
        # appendix omits the field), and no draft carries canonical: false. So we
        # enforce the rule negatively: a draft must not promote itself to canonical.
        if "canonical: true" in text:
            fail(f"book draft must remain non-canonical: {path.relative_to(ROOT)}")
        if len(text.encode("utf-8")) > MAX_DRAFT_BYTES:
            oversized.append(filename)
        if filename.startswith("Q") and filename not in status_text:
            missing.append(filename)

    if missing:
        fail("BOOK_CURRENT_STATUS missing draft reference(s): " + ", ".join(missing))
    if oversized:
        fail("book draft(s) exceed connector-safe size: " + ", ".join(oversized))

    print("OK: current book manuscript layout is connector-safe")
    print(f"drafts={len(EXPECTED_DRAFTS)}")


if __name__ == "__main__":
    main()
