#!/usr/bin/env python3
"""Export the current book manuscript as a reader-facing publication draft."""

from __future__ import annotations

from argparse import ArgumentParser
from dataclasses import dataclass
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BOOK_DIR = ROOT / "01_Source_Intuition" / "BOOK"
DRAFTS_DIR = BOOK_DIR / "Drafts_26Q"
EXPORT_DIR = BOOK_DIR / "Exports"


@dataclass(frozen=True)
class ManuscriptItem:
    filename: str
    kind: str


MANUSCRIPT_ORDER = [
    ManuscriptItem("致读者.md", "front"),
    ManuscriptItem("Q00_序章.md", "chapter"),
    ManuscriptItem("Q01_给定性.md", "chapter"),
    ManuscriptItem("Q02_对象化.md", "chapter"),
    ManuscriptItem("Q03_前对象场.md", "chapter"),
    ManuscriptItem("Q04_最低非中立性.md", "chapter"),
    ManuscriptItem("幕间桥_一二幕.md", "interlude"),
    ManuscriptItem("幕前_二幕.md", "interlude"),
    ManuscriptItem("Q04b_选材.md", "chapter"),
    ManuscriptItem("Q05_选择不是挑选.md", "chapter"),
    ManuscriptItem("Q06_排除与阴影.md", "chapter"),
    ManuscriptItem("Q07_锚定.md", "chapter"),
    ManuscriptItem("Q08_不可逆性.md", "chapter"),
    ManuscriptItem("Q09_现实厚度.md", "chapter"),
    ManuscriptItem("Q10_秩序背景化.md", "chapter"),
    ManuscriptItem("幕间桥_二三幕.md", "interlude"),
    ManuscriptItem("幕前_三幕.md", "interlude"),
    ManuscriptItem("Q11_被选择.md", "chapter"),
    ManuscriptItem("Q12_攸关.md", "chapter"),
    ManuscriptItem("Q13_在乎.md", "chapter"),
    ManuscriptItem("Q14_价值不是偏好.md", "chapter"),
    ManuscriptItem("Q15_关切维度.md", "chapter"),
    ManuscriptItem("Q15b_能动性.md", "chapter"),
    ManuscriptItem("Q16_主体沉积.md", "chapter"),
    ManuscriptItem("Q17_意识.md", "chapter"),
    ManuscriptItem("幕间桥_三四幕.md", "interlude"),
    ManuscriptItem("幕前_四幕.md", "interlude"),
    ManuscriptItem("Q18_秩序与自由.md", "chapter"),
    ManuscriptItem("Q19_脚手架与牢笼.md", "chapter"),
    ManuscriptItem("Q20_遮蔽.md", "chapter"),
    ManuscriptItem("Q21_苦难.md", "chapter"),
    ManuscriptItem("Q22_方向.md", "chapter"),
    ManuscriptItem("幕间桥_四五幕.md", "interlude"),
    ManuscriptItem("幕前_五幕.md", "interlude"),
    ManuscriptItem("Q23_共同体.md", "chapter"),
    ManuscriptItem("幕间桥_Q23_Q24.md", "interlude"),
    ManuscriptItem("Q24_AI.md", "chapter"),
    ManuscriptItem("幕间桥_Q24_Q25.md", "interlude"),
    ManuscriptItem("Q25_选择广于意识.md", "chapter"),
    ManuscriptItem("Q26_可证伪性.md", "chapter"),
    ManuscriptItem("Q27_理论自反.md", "chapter"),
    ManuscriptItem("Q28_回到生成.md", "chapter"),
    ManuscriptItem("附录_三问使用指南.md", "appendix"),
    ManuscriptItem("附录_跨域难题_重述而非解决.md", "appendix"),
    ManuscriptItem("附录_术语表.md", "appendix"),
]


def strip_leading_frontmatter(text: str) -> str:
    """Remove only the YAML block at the start of a source file."""
    if not text.startswith("---\n"):
        return text.lstrip("\n")
    closing = text.find("\n---\n", 4)
    if closing == -1:
        raise ValueError("unterminated frontmatter")
    return text[closing + len("\n---\n") :].lstrip("\n")


def first_heading(markdown: str) -> str:
    for line in markdown.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "未命名章节"


def page_break() -> str:
    return "\n\n\\newpage\n\n"


def build_publication(export_date: str) -> tuple[str, str]:
    chapters: list[tuple[ManuscriptItem, Path, str, str]] = []
    for item in MANUSCRIPT_ORDER:
        path = DRAFTS_DIR / item.filename
        if not path.exists():
            raise FileNotFoundError(path.relative_to(ROOT))
        raw = path.read_text(encoding="utf-8")
        body = strip_leading_frontmatter(raw).strip() + "\n"
        chapters.append((item, path, first_heading(body), body))

    toc_lines = ["# 目录", ""]
    for item, _path, title, _body in chapters:
        toc_lines.append(f"- {title}")

    header = [
        "# 从存在到秩序",
        "",
        "作者：张宇鑫",
        "",
        "RC1 出版合并稿",
        "",
        export_date,
        "",
    ]

    parts = ["\n".join(header), "\n".join(toc_lines)]
    for _item, _path, _title, body in chapters:
        parts.append(body)

    manuscript = page_break().join(part.rstrip() for part in parts).rstrip() + "\n"

    manifest_lines = [
        "# 《从存在到秩序》出版合并稿来源清单",
        "",
        f"- 导出日期：{export_date}",
        f"- 导出脚本：`{Path(__file__).relative_to(ROOT)}`",
        f"- 源目录：`{DRAFTS_DIR.relative_to(ROOT)}`",
        f"- 合并文件数：{len(chapters)}",
        "- 导出规则：剥离每个源文件开头的 YAML 元数据，保留正文 Markdown 与正文分隔线。",
        "",
        "## 合并顺序",
        "",
    ]
    for index, (item, path, title, _body) in enumerate(chapters, start=1):
        rel = path.relative_to(ROOT)
        manifest_lines.append(f"{index}. `{item.kind}` · {title} · `{rel}`")
    manifest = "\n".join(manifest_lines).rstrip() + "\n"

    return manuscript, manifest


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--date", default=date.today().isoformat())
    args = parser.parse_args()

    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    manuscript, manifest = build_publication(args.date)

    stem = f"从存在到秩序_RC1_出版合并稿_{args.date}"
    manuscript_path = EXPORT_DIR / f"{stem}.md"
    manifest_path = EXPORT_DIR / f"{stem}_来源清单.md"
    manuscript_path.write_text(manuscript, encoding="utf-8")
    manifest_path.write_text(manifest, encoding="utf-8")

    print(manuscript_path.relative_to(ROOT))
    print(manifest_path.relative_to(ROOT))
    print(f"bytes={len(manuscript.encode('utf-8'))}")
    print(f"items={len(MANUSCRIPT_ORDER)}")


if __name__ == "__main__":
    main()
