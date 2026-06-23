#!/usr/bin/env python3
"""
Compile SRT book drafts into output files.
Strips YAML frontmatter, assembles chapters in order.
Outputs:
  Output/从存在到秩序_完整版_2026-06-23.md        — full book
  Output/从存在到秩序_哲学读者试读版_2026-06-23.md — philosophical reader sample
"""

import re
from pathlib import Path

ROOT = Path(__file__).parent.parent
DRAFTS = ROOT / "01_Source_Intuition/BOOK/Drafts_26Q"
OUT = ROOT / "Output"
OUT.mkdir(exist_ok=True)

TODAY = "2026-06-23"


def strip_frontmatter(text: str) -> str:
    """Remove YAML frontmatter block (--- ... ---)."""
    if text.startswith("---"):
        end = text.find("\n---", 3)
        if end != -1:
            return text[end + 4:].lstrip("\n")
    return text


def load(filename: str) -> str:
    path = DRAFTS / filename
    raw = path.read_text(encoding="utf-8")
    return strip_frontmatter(raw)


def section_break(title: str = "") -> str:
    if title:
        return f"\n\n---\n\n# {title}\n\n"
    return "\n\n---\n\n"


# ── Full book chapter order ────────────────────────────────────────────────────

FULL_BOOK_PARTS = [
    # file, separator_before
    ("致读者.md",          None),
    ("Q00_序章.md",        "序章"),
    # 第一幕
    ("Q01_给定性.md",      "第一幕　给定性、对象化、前对象场、最低非中立性"),
    ("Q02_对象化.md",      None),
    ("Q03_前对象场.md",    None),
    ("Q04_最低非中立性.md", None),
    # 幕间一
    ("幕间桥_一二幕.md",   "幕间　换上新镜片：没有现成的起点"),
    # 第二幕
    ("Q05_选择不是挑选.md", "第二幕　选择结构与现实厚度"),
    ("Q06_排除与阴影.md",  None),
    ("Q07_锚定.md",        None),
    ("Q08_不可逆性.md",    None),
    ("Q09_现实厚度.md",    None),
    ("Q10_秩序背景化.md",  None),
    # 幕间二
    ("幕间桥_二三幕.md",   "幕间　选择留下来的，是自由还是牢笼？"),
    # 第三幕
    ("Q11_被选择.md",      "第三幕　后果回流、价值与主体"),
    ("Q12_攸关.md",        None),
    ("Q13_在乎.md",        None),
    ("Q14_价值不是偏好.md", None),
    ("Q15_关切维度.md",    None),
    ("Q16_主体沉积.md",    None),
    ("Q17_意识.md",        None),
    # 幕间三
    ("幕间桥_三四幕.md",   "幕间　意识照亮了什么，秩序又遮住了什么？"),
    # 第四幕
    ("Q18_秩序与自由.md",  "第四幕　秩序、自由、遮蔽与方向"),
    ("Q19_脚手架与牢笼.md", None),
    ("Q20_遮蔽.md",        None),
    ("Q21_苦难.md",        None),
    ("Q22_方向.md",        None),
    ("Q23_共同体.md",      None),
    # 幕间四
    ("幕间桥_Q23_Q24.md",  "幕间　AI 来了，共同体还在吗？"),
    ("Q24_AI.md",          None),
    # 幕间五
    ("幕间桥_Q24_Q25.md",  "幕间　选择广于意识，还是意识装不下选择？"),
    ("Q25_选择广于意识.md", None),
    ("Q26_可证伪性.md",    None),
    ("Q27_理论自反.md",    None),
    ("Q28_回到生成.md",    None),
    # 附录
    ("附录_三问使用指南.md",       "附录一　三问使用指南"),
    ("附录_术语表.md",             "附录二　术语表"),
    ("附录_跨域难题_重述而非解决.md", "附录三　跨域难题：重述而非解决"),
]

# ── Philosophical reader sample ────────────────────────────────────────────────
# Arc: 完整第一幕 + 核心机制章 + 价值论 + 意识 + 方向 + 可证伪性 + 自反 + 终章

PHIL_INTRO = """# 选择实在论（SRT）——哲学读者试读版

**《从存在到秩序》哲学读者试读版**

---

> 本试读版面向有哲学背景的读者。收录完整第一幕（序章 + 第一至四章 + 幕间），加上核心机制章（第五章）、价值论（第十四章）、意识（第十七章）、方向（第二十二章）、可证伪性（第二十六章）、理论自反（第二十七章）与终章（第二十八章）。
>
> 章末注（标注"专业读者，可跳过"）在本版保留并供阅读：它们是本书与现象学、过程哲学、科学实在论、理性选择理论、IIT/GWT/FEP 等传统之间的显性对话接口。
>
> 如需完整书稿或形式公理文件（P0 公理、P1 定理、符号表），请联系作者。

---

"""

PHIL_PARTS = [
    ("致读者.md",          None),
    ("Q00_序章.md",        "序章"),
    ("Q01_给定性.md",      "第一幕　给定性、对象化、前对象场、最低非中立性"),
    ("Q02_对象化.md",      None),
    ("Q03_前对象场.md",    None),
    ("Q04_最低非中立性.md", None),
    ("幕间桥_一二幕.md",   "幕间　换上新镜片：没有现成的起点"),
    ("Q05_选择不是挑选.md", "第二幕（节选）　选择结构"),
    ("Q14_价值不是偏好.md", "第三幕（节选）　价值不是偏好"),
    ("Q17_意识.md",        "第三幕（节选）　意识"),
    ("Q22_方向.md",        "第四幕（节选）　方向"),
    ("Q26_可证伪性.md",    "第四幕（节选）　可证伪性"),
    ("Q27_理论自反.md",    None),
    ("Q28_回到生成.md",    "终章　回到生成"),
]


def compile_parts(parts, title_block: str) -> str:
    chunks = [title_block]
    for i, (filename, sep_title) in enumerate(parts):
        content = load(filename)
        if sep_title:
            chunks.append(f"\n\n---\n\n")
            # Don't add a redundant H1 if the content already starts with one
            if not content.lstrip().startswith("# "):
                chunks.append(f"## {sep_title}\n\n")
        elif i > 0:
            chunks.append("\n\n")
        chunks.append(content.strip())
    return "\n".join(chunks)


# ── Full book ─────────────────────────────────────────────────────────────────

FULL_TITLE = f"""# 从存在到秩序

**选择实在论（SRT）完整书稿**

版本：{TODAY}

---

"""

full_text = compile_parts(FULL_BOOK_PARTS, FULL_TITLE)
full_path = OUT / f"从存在到秩序_完整版_{TODAY}.md"
full_path.write_text(full_text, encoding="utf-8")
print(f"✓ 完整版  →  {full_path.name}  ({len(full_text):,} chars)")

# ── Philosophical reader version ───────────────────────────────────────────────

phil_text = compile_parts(PHIL_PARTS, PHIL_INTRO)
phil_path = OUT / f"从存在到秩序_哲学读者试读版_{TODAY}.md"
phil_path.write_text(phil_text, encoding="utf-8")
print(f"✓ 哲学试读 →  {phil_path.name}  ({len(phil_text):,} chars)")
