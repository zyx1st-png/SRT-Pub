#!/usr/bin/env python3
"""Build the current complete manuscript as Markdown and a polished A5 PDF."""

from __future__ import annotations

from argparse import ArgumentParser
from datetime import date
from hashlib import sha256
from pathlib import Path
import sys

from export_book_philosophy_reader import (
    OUTPUT_DIR,
    heading,
    keep_inline_notes_in_place,
    render_pdf,
    strip_frontmatter,
)
from export_book_publication import MANUSCRIPT_ORDER


ROOT = Path(__file__).resolve().parents[1]
BOOK_DIR = ROOT / "01_Source_Intuition" / "BOOK"
DRAFTS_DIR = BOOK_DIR / "Drafts_26Q"


def cover(export_date: str) -> str:
    return f"""
<section class="cover">
  <p class="kicker">生成哲学 · 当前完整书稿</p>
  <h1>从存在到秩序</h1>
  <p class="subtitle">完整稿</p>
  <p class="author">张宇鑫</p>
  <p class="edition">更新至 {export_date} · 可复制文本 PDF</p>
</section>
"""


def edition_note() -> str:
    return """
# 版本说明

《从存在到秩序》是一部关于现实如何生成、秩序如何形成，以及秩序如何不封闭生成的哲学书。SRT 是它背后的理论发动机、问题链来源和概念脚手架，但本书不是 SRT 的教材、说明书或 canonical 注释。

本文件依照当前五幕顺序整理，包含：

- 致读者与序章；
- 第一幕至第五幕全部正文；
- 四座幕终桥、两座第五幕内部幕间桥及第二至第五幕幕前页；
- 选材章与能动性章两座不编号主题章；
- 三份附录：三问使用指南、跨域难题、术语表。

<div class="status-box">
<p><strong>书稿地位：</strong>本稿属于读者向完整书稿，正文首先承担哲学表达与问题推进，不自动构成 SRT canonical 定义。书中的候选安置、跨域显影、开放问题与失败条件，应按各章自己的边界说明阅读。</p>
</div>

本版从当前工作区的 `Drafts_26Q/` 逐文件生成，不改写源章。章末专业注释予以保留；行内注释保持在原段落附近，便于连续阅读与批注。
"""


def load_sources() -> list[tuple[object, Path, str, str]]:
    sources: list[tuple[object, Path, str, str]] = []
    for item in MANUSCRIPT_ORDER:
        path = DRAFTS_DIR / item.filename
        if not path.exists():
            raise FileNotFoundError(path.relative_to(ROOT))
        raw = path.read_text(encoding="utf-8")
        body = keep_inline_notes_in_place(strip_frontmatter(raw).strip()) + "\n"
        sources.append((item, path, heading(body), body))
    return sources


def contents(sources: list[tuple[object, Path, str, str]]) -> str:
    lines = ["# 目录", ""]
    for item, _path, title, _body in sources:
        prefix = {
            "front": "前置",
            "chapter": "正文",
            "interlude": "幕前／幕间",
            "appendix": "附录",
        }.get(item.kind, item.kind)
        lines.append(f"- {prefix} · {title}")
    return "\n".join(lines) + "\n"


def build(export_date: str) -> tuple[str, str]:
    sources = load_sources()
    chunks = [cover(export_date).strip(), edition_note().strip(), contents(sources).strip()]
    chunks.extend(body.strip() for _item, _path, _title, body in sources)
    manuscript = "\n\n".join(chunks).rstrip() + "\n"

    manifest_lines = [
        "# 《从存在到秩序：完整稿》来源清单",
        "",
        f"- 导出日期：{export_date}",
        f"- 导出脚本：`{Path(__file__).relative_to(ROOT)}`",
        f"- 源目录：`{DRAFTS_DIR.relative_to(ROOT)}`",
        f"- 合并文件数：{len(sources)}",
        "- 导出规则：剥离 YAML 元数据；保留正文、幕前、幕间、附录和章末专业注释；行内注释保持在原段附近。",
        "- 源文件状态：使用导出时当前工作区内容；不修改源章。",
        "",
        "## 合并顺序",
        "",
    ]
    for index, (item, path, title, body) in enumerate(sources, start=1):
        digest = sha256(body.encode("utf-8")).hexdigest()[:12]
        manifest_lines.append(
            f"{index}. `{item.kind}` · {title} · `{path.relative_to(ROOT)}` · "
            f"sha256 `{digest}`"
        )
    manifest = "\n".join(manifest_lines).rstrip() + "\n"
    return manuscript, manifest


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--no-pdf", action="store_true")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    stem = f"从存在到秩序_完整稿_{args.date}"
    markdown_path = OUTPUT_DIR / f"{stem}.md"
    manifest_path = OUTPUT_DIR / f"{stem}_来源清单.md"
    pdf_path = OUTPUT_DIR / f"{stem}.pdf"

    manuscript, manifest = build(args.date)
    markdown_path.write_text(manuscript, encoding="utf-8")
    manifest_path.write_text(manifest, encoding="utf-8")
    if not args.no_pdf:
        render_pdf(
            markdown_path,
            pdf_path,
            title="从存在到秩序：完整稿",
            subject="生成哲学当前完整书稿",
        )

    print(markdown_path.relative_to(ROOT))
    print(manifest_path.relative_to(ROOT))
    if not args.no_pdf:
        print(pdf_path.relative_to(ROOT))
    print(f"bytes={len(manuscript.encode('utf-8'))}")
    print(f"items={len(MANUSCRIPT_ORDER)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
