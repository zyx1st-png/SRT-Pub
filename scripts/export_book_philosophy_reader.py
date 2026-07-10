#!/usr/bin/env python3
"""Build the current philosophy-reader sample as Markdown and a polished A5 PDF."""

from __future__ import annotations

from argparse import ArgumentParser
from dataclasses import dataclass
from datetime import date
from hashlib import sha256
from pathlib import Path
import subprocess
import sys
import tempfile

from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
BOOK_DIR = ROOT / "01_Source_Intuition" / "BOOK"
DRAFTS_DIR = BOOK_DIR / "Drafts_26Q"
OUTPUT_DIR = ROOT / "Output" / "pdf"
TMP_DIR = ROOT / "tmp" / "pdfs"
CHROME = Path("/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")


@dataclass(frozen=True)
class SourceItem:
    filename: str
    role: str


ITEMS: list[SourceItem | str] = [
    "part_1",
    SourceItem("Q00_序章.md", "opening"),
    SourceItem("Q01_给定性.md", "act_1"),
    SourceItem("Q02_对象化.md", "act_1"),
    SourceItem("Q03_前对象场.md", "act_1"),
    SourceItem("Q04_最低非中立性.md", "act_1"),
    SourceItem("幕间桥_一二幕.md", "act_1_closing"),
    "part_2",
    SourceItem("Q04b_选材.md", "selection_entry"),
    SourceItem("Q05_选择不是挑选.md", "selection_core"),
    "bridge_to_value",
    "part_3",
    SourceItem("Q14_价值不是偏好.md", "value"),
    "bridge_to_subject",
    SourceItem("Q16_主体沉积.md", "subject"),
    SourceItem("Q17_意识.md", "consciousness"),
    "bridge_to_direction",
    "part_4",
    SourceItem("Q22_方向.md", "direction"),
    "bridge_to_ai",
    "part_5",
    SourceItem("Q24_AI.md", "ai"),
    SourceItem("幕间桥_Q24_Q25.md", "ai_boundary_interlude"),
    SourceItem("Q25_选择广于意识.md", "selection_boundary"),
    SourceItem("Q26_可证伪性.md", "failure_conditions"),
    SourceItem("Q27_理论自反.md", "reflexivity"),
    SourceItem("Q28_回到生成.md", "closing"),
]


EDITORIAL_SECTIONS = {
    "part_1": """
<section class="part-page">
  <p class="eyebrow">第一组 · 起点</p>
  <h1>一个稳定世界，能否直接作为解释的起点？</h1>
  <p>本组保留序章与完整第一幕。它承担哲学读者最需要先审查的部分：给定性是否只是效果，对象边界是否需要生成史，前对象场是否被偷写成实体，以及最低非中立性究竟是公设、溯因赌注，还是被伪装成结论。</p>
</section>
""",
    "part_2": """
<section class="part-page">
  <p class="eyebrow">第二组 · 生成机制</p>
  <h1>“选择”能否超出心理挑选，而不变成无限泛化？</h1>
  <p>新增的“选材章”先从排开、定形、写入三步逼出命名；第五章再正面处理“你只是重新定义了选择”的反对。二者必须连读。</p>
</section>
""",
    "bridge_to_value": """
# 编者桥页：从选择结构到价值

以下八章在本试读版中省略，但论证不能假装它们不存在：

- 第六章追踪被排开方向留下的阴影与摩擦；
- 第七章说明显现如何通过留痕、承重和再入场获得锚定；
- 第八章处理选择写回地形后的不可清零差异；
- 第九章把反复承重、支付与再入场描述为现实厚度；
- 第十章说明厚度如何退入背景，沉积成默认地形；
- 第十一章转向地形如何预裁剪后来出现的选项；
- 第十二章追问后果何时真正回到一个承受位置；
- 第十三章说明后果回流后，生活如何围绕它重新组织。

因此，第十四章不是从“人有偏好”直接跳到价值，而是接过一条已经展开的链：选择留下痕迹，痕迹形成地形，地形重写后续选择，后果回到承受位置，生活开始围绕某些后果重新组织。哲学审查的关键是：这条链是否足以逼出“价值”，还是只解释了复杂偏好的形成。
""",
    "part_3": """
<section class="part-page">
  <p class="eyebrow">第三组 · 主体与意识</p>
  <h1>价值、主体与意识，是起点还是沉积结果？</h1>
  <p>本组保留价值、主体和意识三处高风险论证。意识章中的“感受性安置”明确是候选模型，不是难问题的终结判决。</p>
</section>
""",
    "bridge_to_subject": """
# 编者桥页：从价值到主体

第十四章之后，原书还有两步：

第一，第十五章把价值深度与关切宽度分开，追问后果回流的边界能展开到多少条脆弱性轴线；第二，能动性章追问一个位置如何不只被动承受后果，还能把后果带回下一次选择。

本试读版不收录这两章全文。进入第十六章时，应把它的前提读成：已经存在一个能够承受后果、形成价值锚定并把历史用于下一次选择的位置。第十六章要论证的不是“痕迹自动等于主体”，而是这些条件反复咬合后，怎样沉积出一个能够说“这是我”的持续位置。
""",
    "bridge_to_direction": """
# 编者桥页：从意识到方向

第十八至二十一章把论证从主体内部推向秩序：

- 秩序并非自由的简单反面，它也可能是自由得以发生的地面；
- 脚手架在帮助能力形成时是支撑，在替代能力形成时可能成为牢笼；
- 遮蔽不是隐藏一个现成事实，而是改写事实进入判断的格式；
- 苦难不只由疼痛量决定，还涉及痛苦是否失去可修正、可回流的方向。

第二十二章由此提出三个方向判据：一条路是否自耗、是否把后果外包给无法回推的位置、是否在条件变化后锁死重新选择。哲学读者应重点追问：这些判据只是审慎建议，还是能够跨过事实与规范之间的门槛。
""",
    "part_4": """
<section class="part-page">
  <p class="eyebrow">第四组 · 规范压力</p>
  <h1>方向能否从生成结构中读出？</h1>
  <p>这一章承受全书最直接的规范性压力：从“怎样生成”到“哪种方向较健康”，中间是否发生了未经说明的跳跃。</p>
</section>
""",
    "bridge_to_ai": """
# 编者桥页：从方向到 AI

第二十三章把共同体理解为一种跨位置的后果回流结构：决定、承受与修正不能长期被切断。第二十四章的 AI 分析建立在这一步上。

因此，AI 章首先问的不是“机器有没有心”，而是 AI 正在怎样改变人类选择的可见性、摩擦、默认路径与后果分配。意识归属仍是合法问题，但不是唯一入口，也未必是最先需要处理的入口。
""",
    "part_5": """
<section class="part-page">
  <p class="eyebrow">第五组 · 当代压力与理论自限</p>
  <h1>AI 改写了什么？理论又怎样允许自己失败？</h1>
  <p>本组先以 AI 检验“地形改写”框架，再划定选择与意识的边界，最后连续保留失败条件、理论自反与终章。它们不是礼貌性的谦虚，而是判断这套哲学是否会把自身变成新地板的必要部分。</p>
</section>
""",
}


CSS = """
@page {
  size: A5;
  margin: 19mm 16mm 19mm 16mm;
}

html {
  color: #191715;
  background: white;
  font-family: "Songti SC", "STSong", "PingFang SC", serif;
  font-size: 10.4pt;
  line-height: 1.76;
  text-rendering: optimizeLegibility;
}

body {
  margin: 0;
}

.cover {
  min-height: 155mm;
  display: flex;
  flex-direction: column;
  justify-content: center;
  text-align: center;
  break-after: page;
}

.cover .kicker {
  font-family: "PingFang SC", sans-serif;
  font-size: 9pt;
  letter-spacing: .22em;
  color: #756b61;
  margin-bottom: 12mm;
}

.cover h1 {
  break-before: auto;
  font-size: 28pt;
  letter-spacing: .08em;
  margin: 0 0 7mm;
}

.cover .subtitle {
  font-size: 14pt;
  letter-spacing: .08em;
  margin: 0 0 18mm;
}

.cover .author {
  font-size: 11pt;
  margin: 0 0 4mm;
}

.cover .edition {
  font-family: "PingFang SC", sans-serif;
  font-size: 8.5pt;
  color: #756b61;
}

.part-page {
  min-height: 150mm;
  display: flex;
  flex-direction: column;
  justify-content: center;
  break-before: page;
  break-after: page;
}

.part-page .eyebrow {
  font-family: "PingFang SC", sans-serif;
  font-size: 8.5pt;
  letter-spacing: .16em;
  color: #806f5e;
  margin: 0 0 8mm;
  text-align: center;
}

.part-page h1 {
  break-before: auto;
  font-size: 21pt;
  margin-bottom: 10mm;
}

.part-page p {
  color: #4d4640;
  text-align: left;
  max-width: 92%;
  margin-left: auto;
  margin-right: auto;
}

h1 {
  break-before: page;
  font-size: 20pt;
  line-height: 1.36;
  font-weight: 700;
  text-align: center;
  margin: 0 0 11mm;
}

h2 {
  break-after: avoid;
  font-size: 14.2pt;
  line-height: 1.45;
  margin: 10mm 0 4mm;
}

h3 {
  break-after: avoid;
  font-size: 12pt;
  line-height: 1.45;
  margin: 7mm 0 3mm;
}

p {
  margin: 0 0 4mm;
  text-align: justify;
  orphans: 3;
  widows: 3;
}

strong {
  font-weight: 700;
}

blockquote {
  margin: 5mm 1mm 6mm;
  padding: 3mm 0 3mm 4mm;
  border-left: 1.2mm solid #c9b8a5;
  color: #3f3832;
}

blockquote p:last-child {
  margin-bottom: 0;
}

ul, ol {
  margin: 0 0 5mm;
  padding-left: 7mm;
}

li {
  margin-bottom: 1.5mm;
}

table {
  border-collapse: collapse;
  width: 100%;
  margin: 5mm 0 7mm;
  font-size: 8.2pt;
  line-height: 1.48;
}

th, td {
  border: .35pt solid #aaa098;
  padding: 1.5mm 1.7mm;
  vertical-align: top;
}

th {
  background: #f1ede8;
}

hr {
  border: 0;
  border-top: .4pt solid #bdb4ab;
  margin: 9mm 0;
}

a {
  color: inherit;
  text-decoration: none;
}

code {
  font-family: "SF Mono", Menlo, monospace;
  font-size: .88em;
}

pre {
  white-space: pre-wrap;
  border: .3pt solid #d1cbc5;
  background: #f7f4f1;
  padding: 3mm;
  font-size: 8.3pt;
}

.front-note {
  color: #4d4640;
}

.status-box {
  border: .45pt solid #b9aa9b;
  padding: 4mm;
  margin: 6mm 0;
  background: #faf8f5;
}

.status-box p:last-child {
  margin-bottom: 0;
}

.toc li {
  margin-bottom: 2mm;
}

.feedback li {
  margin-bottom: 3mm;
}

.footnotes {
  font-size: 8.5pt;
  line-height: 1.55;
}

.footnote-back {
  display: none;
}
"""


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text.lstrip("\n")
    closing = text.find("\n---\n", 4)
    if closing == -1:
        raise ValueError("unterminated frontmatter")
    return text[closing + 5 :].lstrip("\n")


def keep_inline_notes_in_place(markdown: str) -> str:
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


def heading(text: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return "未命名章节"


def source_body(item: SourceItem) -> tuple[Path, str]:
    path = DRAFTS_DIR / item.filename
    if not path.exists():
        raise FileNotFoundError(path.relative_to(ROOT))
    raw = path.read_text(encoding="utf-8")
    return path, keep_inline_notes_in_place(strip_frontmatter(raw).strip()) + "\n"


def cover(export_date: str) -> str:
    return f"""
<section class="cover">
  <p class="kicker">生成哲学 · 论证审查样本</p>
  <h1>从存在到秩序</h1>
  <p class="subtitle">哲学读者试读版</p>
  <p class="author">张宇鑫</p>
  <p class="edition">更新至 {export_date} · 可复制文本 PDF</p>
</section>
"""


def front_matter() -> str:
    return """
# 本版说明

《从存在到秩序》是一部关于现实如何生成、秩序如何形成，以及秩序如何不封闭生成的哲学书。SRT 是它背后的理论发动机、问题链来源和概念脚手架，但本书不是 SRT 的教材、说明书或 canonical 注释。

本试读版面向有哲学背景、愿意审查论证而不只判断文风的读者。它不是全书缩写，而是一次有意暴露承重位置的取样，集中检验五组问题：

1. 稳定世界能否直接作为解释起点；
2. “选择”能否扩展为排开、定形、写入的生成结构，而不成为无限泛化；
3. 价值、主体与意识能否被安置为生成结果；
4. 方向判断是否跨越了事实与规范之间的门槛；
5. 理论是否给出了真实的失败条件，并允许自己的工具反过来审查自身。

<div class="status-box">
<p><strong>地位说明：</strong>所收章节均为书稿表达（companion exposition），不是 canonical 定义。第一幕的最低非中立性保留其溯因赌注地位；意识章的感受性与反身意识属于候选安置；选择起源、感受质、规范性来源等问题仍有开放张力。本版不把这些问题伪装成已经封闭的定理。</p>
</div>

## 阅读方式

第一、二组建议连续阅读。之后为跨章取样，所有跳跃处都加入了“编者桥页”，只负责交代被省略的论证职务，不替代原章。章末专业注释予以保留，供读者核查相邻传统、经验材料与边界声明。

最有价值的反馈不是“赞同”或“反对”，而是指出：哪一个结论推不出、哪一个概念偷换了、哪一个反对者被写弱了，以及哪一项失败条件其实无法失败。
"""


def contents(source_titles: list[str]) -> str:
    lines = [
        "# 目录与论证路线",
        "",
        '<div class="toc">',
        "",
        "1. 第一组：起点",
        "2. 第二组：生成机制",
        "3. 编者桥页：从选择结构到价值",
        "4. 第三组：主体与意识",
        "5. 编者桥页：从意识到方向",
        "6. 第四组：规范压力",
        "7. 编者桥页：从方向到 AI",
        "8. 第五组：当代压力与理论自限",
        "9. 哲学读者反馈页",
        "",
        "</div>",
        "",
        "## 收录正文",
        "",
    ]
    lines.extend(f"- {title}" for title in source_titles)
    return "\n".join(lines) + "\n"


def feedback_page() -> str:
    return """
# 哲学读者反馈页

<div class="feedback">

请尽量标明章、节和原句。以下问题不要求全部回答。

1. 第一幕是否真正说明了“给定感不是起点”，还是只把一个认识论问题改写成本体论断言？
2. 前对象场是否被写成了新的隐藏实体或可能性仓库？
3. 最低非中立性的溯因策略是否成立？拒绝它的代价真的高于接受它吗？
4. “排开、定形、写入”是否足以支持对选择的扩展定义？哪个反例最可能击穿它？
5. 从选择结构到价值的链条中，最薄弱的一步在哪里？
6. 主体沉积是否解释了主体，还是只解释了主体的历史连续性？
7. 意识章的候选安置是否提供了真实解释增量？若失败，它究竟退回到什么较弱主张？
8. “自耗、外包、锁死”能否产生方向判断，还是仍然预设了未经说明的价值立场？
9. AI 章把入口从“它有没有心”移到“它改写了什么”，是必要的重排，还是回避了主体性问题？
10. 第二十六章的失败条件中，哪一条最可操作？哪一条看似可失败、实际总能被重新解释？
11. 第二十七章是否真的允许本书成为牢笼，还是只完成了修辞性的自我豁免？
12. 如果只能指出一处必须在出版前重写的地方，你会选哪里？为什么？

</div>

反馈时也欢迎只写三件事：你停在哪里；你最不相信哪一句；哪一个问题值得继续追。
"""


def run(args: list[str]) -> None:
    completed = subprocess.run(args, cwd=ROOT)
    if completed.returncode:
        raise RuntimeError("command failed: " + " ".join(args))


def render_pdf(
    markdown: Path,
    output_pdf: Path,
    *,
    title: str = "从存在到秩序：哲学读者试读版",
    subject: str = "生成哲学论证审查样本",
) -> None:
    if not CHROME.exists():
        raise FileNotFoundError(f"Google Chrome not found: {CHROME}")
    TMP_DIR.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="philosophy-reader-", dir=TMP_DIR) as tmpdir:
        tmp = Path(tmpdir)
        css = tmp / "book.css"
        html = tmp / "book.html"
        plain_pdf = tmp / "plain.pdf"
        css.write_text(CSS, encoding="utf-8")
        run(
            [
                "pandoc",
                "--standalone",
                "--from",
                "markdown+raw_html",
                "--css",
                str(css),
                "--wrap=none",
                str(markdown),
                "-o",
                str(html),
            ]
        )
        run(
            [
                str(CHROME),
                "--headless",
                "--disable-gpu",
                "--no-pdf-header-footer",
                "--print-to-pdf=" + str(plain_pdf),
                "file://" + str(html),
            ]
        )
        add_page_numbers(plain_pdf, output_pdf, title=title, subject=subject)


def add_page_numbers(
    input_pdf: Path,
    output_pdf: Path,
    *,
    title: str,
    subject: str,
) -> None:
    reader = PdfReader(str(input_pdf))
    writer = PdfWriter()
    with tempfile.TemporaryDirectory(prefix="page-numbers-", dir=TMP_DIR) as tmpdir:
        tmp = Path(tmpdir)
        for index, page in enumerate(reader.pages):
            if index > 0:
                width = float(page.mediabox.width)
                height = float(page.mediabox.height)
                overlay_path = tmp / f"page-{index + 1}.pdf"
                c = canvas.Canvas(str(overlay_path), pagesize=(width, height))
                c.setFillColorRGB(0.42, 0.39, 0.36)
                c.setFont("Helvetica", 7.5)
                c.drawCentredString(width / 2, 13, str(index))
                c.save()
                overlay = PdfReader(str(overlay_path)).pages[0]
                page.merge_page(overlay)
            writer.add_page(page)
        writer.add_metadata(
            {
                "/Title": title,
                "/Author": "张宇鑫",
                "/Subject": subject,
            }
        )
        with output_pdf.open("wb") as fh:
            writer.write(fh)


def build(export_date: str) -> tuple[str, str]:
    sources: list[tuple[SourceItem, Path, str, str]] = []
    for entry in ITEMS:
        if isinstance(entry, SourceItem):
            path, body = source_body(entry)
            sources.append((entry, path, heading(body), body))

    title_lookup = {item.filename: title for item, _path, title, _body in sources}
    chunks = [
        cover(export_date).strip(),
        front_matter().strip(),
        contents([title for _item, _path, title, _body in sources]).strip(),
    ]
    for entry in ITEMS:
        if isinstance(entry, str):
            chunks.append(EDITORIAL_SECTIONS[entry].strip())
        else:
            body = next(body for item, _path, _title, body in sources if item == entry)
            chunks.append(body.strip())
    chunks.append(feedback_page().strip())
    manuscript = "\n\n".join(chunks).rstrip() + "\n"

    manifest_lines = [
        "# 《从存在到秩序：哲学读者试读版》来源清单",
        "",
        f"- 导出日期：{export_date}",
        f"- 导出脚本：`{Path(__file__).relative_to(ROOT)}`",
        f"- 正文章节数：{len(sources)}",
        "- 版本说明：使用当前工作区 `Drafts_26Q/` 文件；不修改源章。",
        "- 编辑说明：新增定位说明、五组论证导语、四张桥页与哲学读者反馈页。",
        "",
        "## 正文来源",
        "",
    ]
    for index, (item, path, _title, body) in enumerate(sources, start=1):
        digest = sha256(body.encode("utf-8")).hexdigest()[:12]
        manifest_lines.append(
            f"{index}. `{item.role}` · {title_lookup[item.filename]} · "
            f"`{path.relative_to(ROOT)}` · sha256 `{digest}`"
        )
    manifest = "\n".join(manifest_lines).rstrip() + "\n"
    return manuscript, manifest


def main() -> None:
    parser = ArgumentParser()
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--no-pdf", action="store_true")
    args = parser.parse_args()

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    stem = f"从存在到秩序_哲学读者试读版_{args.date}"
    markdown_path = OUTPUT_DIR / f"{stem}.md"
    manifest_path = OUTPUT_DIR / f"{stem}_来源清单.md"
    pdf_path = OUTPUT_DIR / f"{stem}.pdf"

    manuscript, manifest = build(args.date)
    markdown_path.write_text(manuscript, encoding="utf-8")
    manifest_path.write_text(manifest, encoding="utf-8")
    if not args.no_pdf:
        render_pdf(markdown_path, pdf_path)

    print(markdown_path.relative_to(ROOT))
    print(manifest_path.relative_to(ROOT))
    if not args.no_pdf:
        print(pdf_path.relative_to(ROOT))
    print(f"bytes={len(manuscript.encode('utf-8'))}")
    print(f"source_chapters={sum(isinstance(item, SourceItem) for item in ITEMS)}")


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        raise SystemExit(1)
