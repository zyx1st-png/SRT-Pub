#!/usr/bin/env python3
"""Export the eight-chapter spine reading edition."""

from __future__ import annotations

from argparse import ArgumentParser
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from export_book_publication import first_heading, page_break, strip_leading_frontmatter


ROOT = Path(__file__).resolve().parents[1]
BOOK_DIR = ROOT / "01_Source_Intuition" / "BOOK"
DRAFTS_DIR = BOOK_DIR / "Drafts_26Q"
EXPORT_DIR = BOOK_DIR / "Exports"
READER_AID = BOOK_DIR / "READER_AID_速查与采样路径_2026-06-12.md"


@dataclass(frozen=True)
class SpineItem:
    path: Path
    kind: str


SPINE_ORDER = [
    SpineItem(DRAFTS_DIR / "致读者.md", "front"),
    SpineItem(DRAFTS_DIR / "Q00_序章.md", "spine_chapter"),
    SpineItem(DRAFTS_DIR / "Q05_选择不是挑选.md", "spine_chapter"),
    SpineItem(DRAFTS_DIR / "Q09_现实厚度.md", "spine_chapter"),
    SpineItem(DRAFTS_DIR / "Q10_秩序背景化.md", "spine_chapter"),
    SpineItem(DRAFTS_DIR / "Q11_被选择.md", "spine_chapter"),
    SpineItem(DRAFTS_DIR / "Q13_在乎.md", "spine_chapter"),
    SpineItem(DRAFTS_DIR / "Q22_方向.md", "spine_chapter"),
    SpineItem(DRAFTS_DIR / "Q28_回到生成.md", "spine_chapter"),
    SpineItem(READER_AID, "reader_aid"),
]


def reader_aid_core_only(markdown: str) -> str:
    body = strip_leading_frontmatter(markdown)
    marker = "\n## 第二部分：采样阅读路径"
    if marker in body:
        body = body.split(marker, 1)[0].rstrip()
    body = body.replace("# 读者辅助件：核心词速查 ＋ 采样阅读路径", "# 核心词速查")
    body = body.replace("## 第一部分：核心词速查页\n\n", "")
    return body.strip() + "\n"


def keep_inline_notes_in_place(markdown: str) -> str:
    """Avoid Pandoc moving inline footnotes to the end of the whole excerpt."""
    output: list[str] = []
    index = 0
    while index < len(markdown):
        start = markdown.find("^[", index)
        if start == -1:
            output.append(markdown[index:])
            break
        end = markdown.find("]", start + 2)
        if end == -1:
            output.append(markdown[index:])
            break
        output.append(markdown[index:start])
        output.append("（注：" + markdown[start + 2 : end] + "）")
        index = end + 1
    return "".join(output)


def body_for(item: SpineItem) -> str:
    raw = item.path.read_text(encoding="utf-8")
    if item.path == READER_AID:
        return reader_aid_core_only(raw)
    return keep_inline_notes_in_place(strip_leading_frontmatter(raw).strip()) + "\n"


def build_spine(export_date: str) -> tuple[str, str]:
    sections: list[tuple[SpineItem, str, str]] = []
    for item in SPINE_ORDER:
        if not item.path.exists():
            raise FileNotFoundError(item.path.relative_to(ROOT))
        body = body_for(item)
        sections.append((item, first_heading(body), body))

    toc_lines = ["# 目录", ""]
    for _item, title, _body in sections:
        toc_lines.append(f"- {title}")

    header = [
        "# 从存在到秩序",
        "",
        "作者：张宇鑫",
        "",
        "八章主干试读版",
        "",
        "可复制文本 PDF 源稿",
        "",
        export_date,
        "",
        "> 本版是从全书中裁出的主干阅读版，不替代完整书稿。它保留“稳定不是起点 → 留下 → 回来 → 方向 → 回到生成”的最短骨架。",
        "",
    ]

    parts = ["\n".join(header), "\n".join(toc_lines)]
    parts.extend(body for _item, _title, body in sections)
    manuscript = page_break().join(part.rstrip() for part in parts).rstrip() + "\n"

    manifest_lines = [
        "# 《从存在到秩序》八章主干试读版来源清单",
        "",
        f"- 导出日期：{export_date}",
        f"- 导出脚本：`{Path(__file__).relative_to(ROOT)}`",
        f"- 合并文件数：{len(sections)}",
        "- 导出规则：剥离源文件开头的 YAML 元数据；读者辅助件只保留核心词速查部分。",
        "- PDF 规则：保留文本层，可选中、搜索、复制。",
        "",
        "## 合并顺序",
        "",
    ]
    for index, (item, title, _body) in enumerate(sections, start=1):
        manifest_lines.append(f"{index}. `{item.kind}` · {title} · `{item.path.relative_to(ROOT)}`")
    manifest = "\n".join(manifest_lines).rstrip() + "\n"

    return manuscript, manifest


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--date", default=date.today().isoformat())
    args = parser.parse_args()

    EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    manuscript, manifest = build_spine(args.date)

    stem = f"从存在到秩序_RC1_八章主干试读版_可复制_{args.date}"
    manuscript_path = EXPORT_DIR / f"{stem}.md"
    manifest_path = EXPORT_DIR / f"{stem}_来源清单.md"
    manuscript_path.write_text(manuscript, encoding="utf-8")
    manifest_path.write_text(manifest, encoding="utf-8")

    print(manuscript_path.relative_to(ROOT))
    print(manifest_path.relative_to(ROOT))
    print(f"bytes={len(manuscript.encode('utf-8'))}")
    print(f"items={len(SPINE_ORDER)}")


if __name__ == "__main__":
    main()
