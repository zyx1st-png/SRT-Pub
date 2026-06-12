#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把《从存在到秩序》本地仓库中的 BOOK 目录整理成一个可直接上传给 ChatGPT Pro / Deep Research 的合并 Markdown 文件。

用法：
1. 把本脚本放在 SRT-Pub 仓库根目录，或在仓库根目录运行：
   python3 /path/to/build_srt_deep_research_full_bundle.py
2. 生成文件位于：01_Source_Intuition/BOOK/_DeepResearch_Pack/
3. 上传生成的 FULL_CONTEXT markdown 给 Pro / Deep Research。
"""

from __future__ import annotations

import re
import sys
import zipfile
from datetime import date
from pathlib import Path

TODAY = date.today().isoformat()

ROOT_CANDIDATES = [Path.cwd(), Path(__file__).resolve().parent]
BOOK_DIR = None
for root in ROOT_CANDIDATES:
    candidate = root / "01_Source_Intuition" / "BOOK"
    if candidate.exists() and candidate.is_dir():
        BOOK_DIR = candidate
        REPO_ROOT = root
        break

if BOOK_DIR is None:
    print("错误：找不到 01_Source_Intuition/BOOK。请在 SRT-Pub 仓库根目录运行本脚本。", file=sys.stderr)
    sys.exit(1)

DRAFTS_DIR = BOOK_DIR / "Drafts_26Q"
OUT_DIR = BOOK_DIR / "_DeepResearch_Pack"
OUT_DIR.mkdir(parents=True, exist_ok=True)

FULL_CONTEXT = OUT_DIR / f"SRT_BOOK_FULL_CONTEXT_FOR_DEEP_RESEARCH_{TODAY}.md"
PROMPT_FILE = OUT_DIR / f"SRT_DEEP_RESEARCH_PROMPT_ONLY_{TODAY}.md"
MANIFEST_FILE = OUT_DIR / f"SRT_BOOK_FILE_MANIFEST_{TODAY}.md"
ZIP_FILE = OUT_DIR / f"SRT_BOOK_DEEP_RESEARCH_UPLOAD_PACK_{TODAY}.zip"

META_FILES = [
    "BOOK_ARCHITECTURE_MAP_2026-06-03.md",
    "BOOK_CORE_PROPOSITIONS_2026-05-30.md",
    "BOOK_STRONGEST_OPPONENTS_MANUAL_2026-05-30.md",
    "BOOK_TERMINOLOGY_SIMPLIFICATION_GUIDE_2026-06-03.md",
    "PROFESSIONAL_READING_BRIEF_CN.md",
    "DEEP_RESEARCH_SOURCE_PACK_2026-06-05.md",
    "DEEP_RESEARCH_PROMPT_2026-06-05.md",
]

PROMPT = """# 《从存在到秩序》Deep Research 可直接使用提示词

你现在是《从存在到秩序》的 Deep Research 研究编辑，不是支持者，不是反对者，也不是润色编辑。

我已经上传了一个合并版文件：`SRT_BOOK_FULL_CONTEXT_FOR_DEEP_RESEARCH_*.md`。请先读取文件开头的“Deep Research 任务书”，再读取其中合并的元文件、致读者、Q00–Q28 章节与三座幕间桥。

研究目标：

我目前正在撰写和优化《从存在到秩序》。请基于当前书中的内容和材料，判断：

1. 哪些东西是可以讲但目前未讲的；
2. 哪些东西已经讲了，但讲得不好、存在问题，应该怎么讲；
3. 哪些外部材料可以作为补充印证，但不能被当成本体论证明；
4. 哪些内容可以进行深入论证；
5. 哪些内容可以拔高书籍高度，让它从“强解释系统”走向真正能改变读者看世界方式的书。

请特别注意：

- 不要把本书改成学术综述。
- 不要把外部材料当证明。
- 不要每章都补材料。
- 不要每章都补“最强反对者”。
- 不要重复“这只是换一套语言”的泛泛批评。
- 不要把 AI 章写成 AI 热点盘点。
- 不要把意识章写成意识理论综述。
- 不要把价值章写成功利主义/偏好理论综述。
- 不要把“选择”缩回人的心理决策。
- 不要把“前对象场”写成神秘实体或物理真空。
- 不要让术语先于经验状态出场。
- 不要让跨领域案例变成“看，所有东西都像 SRT”。

请输出一份可执行研究报告，结构如下：

一、总体判断
- 这本书当前最强之处是什么？
- 它距离“真正改变世界的书”差在哪里？
- 最大风险是理论太强、证据太弱，还是表达太像自洽系统？
- 当前最不应该再大改的部分是什么？

二、可以讲但未讲的内容
用表格输出：优先级 / 章节 / 未讲内容 / 为什么重要 / 应该查什么资料 / 回写方式。

三、讲了但讲得不好或有问题的内容
用表格输出：严重程度 / 章节 / 当前问题 / 为什么会伤害读者理解 / 应该怎么讲 / 是否需要删减。

四、可作为补充印证的材料
用表格输出：主题 / 可找材料 / 支持什么 / 不能证明什么 / 适合放正文还是脚注。

五、值得深入论证的位置
用表格输出：章节 / 深入论证点 / 最强反对意见 / 需要查的理论传统 / 建议增加的最小段落。

六、拔高全书高度的 8–10 个最小施工点
每个施工点必须包含：章节、当前问题、为什么它能拔高全书、Deep Research 要找什么、不要找什么、回写方式。

七、外部资料清单
请提供 15–30 个高价值资料方向，每个资料方向说明用途，并区分“一定要查 / 可查 / 谨慎使用”。优先原典、权威综述、近年高质量论文或经典理论，不要营销文章。

八、总修策略
请给出下一步顺序：哪些章节先修；哪些只做轻微语言微调；哪些不要补材料；哪些需要删减模板；哪些需要加真正强的对手；哪些需要把材料移到章末注。

最终目标：

请把《从存在到秩序》当作一部正在成形的世界级思想书来审查：不是替它辩护，也不是泛泛攻击，而是找出哪些地方需要外部材料显影、哪些地方需要更强论证、哪些地方需要删减模板、哪些地方已经有力量必须保留，最终给出能把它从“强解释系统”推向“能改变读者看世界方式”的最小研究与总修方案。
"""

BOOT = f"""---
id: SRT-BOOK-FULL-CONTEXT-FOR-DEEP-RESEARCH-{TODAY}
type: full_context_bundle
created: {TODAY}
source_repo: local SRT-Pub
scope: 01_Source_Intuition/BOOK
canonical: false
---

# 《从存在到秩序》Deep Research 完整上下文合并包

> 本文件由 `build_srt_deep_research_full_bundle.py` 自动整理，目标是让 Pro / Deep Research 不再依赖 GitHub 仓库调用。请把本文件作为上传给模型的主文件。

---

## A. Deep Research 任务书

{PROMPT}

---

## B. 当前全书一句话

**稳定不是起点，而是选择留下来的历史；秩序不是终点，而是后果回得来的地面。**

更完整地说：对象、主体、价值、意识、秩序和共同体都不是解释的第一事实，而是选择、排除、定形、写入、后果回流、关切沉积和秩序背景化之后形成的稳定结构。稳定结构一旦退入背景，又会预裁剪后续选择，托举自由，也可能替代自由、遮蔽痛苦、外包后果、锁死方向。全书最后把秩序重新带回生成：好的秩序不是完成态，而是给下一次生成留下位置。

---

## C. 合并文件目录

本合并包包含：

1. 元文件：建筑图、核心命题、最强对手手册、术语降噪规则、专业阅读简报、Deep Research 入口文件。
2. 章节正文：`Drafts_26Q/` 下致读者、Q00–Q28，以及三座幕间桥（阅读顺序分别插于 Q10/Q11、Q17/Q18、Q24/Q25 之间）。
3. 附录：三问使用指南。

---

"""

def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8-sig")


def q_sort_key(path: Path):
    m = re.match(r"Q(\d+)", path.name)
    if m:
        return (0, int(m.group(1)), path.name)
    return (1, 9999, path.name)

# Gather files
meta_paths = [BOOK_DIR / name for name in META_FILES if (BOOK_DIR / name).exists()]
chapter_paths = []
appendix_paths = []
if DRAFTS_DIR.exists():
    chapter_paths = sorted([p for p in DRAFTS_DIR.glob("Q*.md") if p.is_file()], key=q_sort_key)
    appendix_paths = sorted([p for p in DRAFTS_DIR.glob("附录*.md") if p.is_file()], key=lambda p: p.name)

# 阅读顺序：致读者在 Q00 之前；三座幕间桥插于对应章之后
INTERLUDES_AFTER = {
    "Q10": "幕间桥_二三幕.md",
    "Q17": "幕间桥_三四幕.md",
    "Q24": "幕间桥_Q24_Q25.md",
}
reading_order = []
front_page = DRAFTS_DIR / "致读者.md"
if front_page.exists():
    reading_order.append(front_page)
for p in chapter_paths:
    reading_order.append(p)
    prefix = p.name.split("_")[0]
    if prefix in INTERLUDES_AFTER:
        interlude = DRAFTS_DIR / INTERLUDES_AFTER[prefix]
        if interlude.exists():
            reading_order.append(interlude)
chapter_paths = reading_order

if not chapter_paths:
    print("警告：未找到 Drafts_26Q/Q*.md 章节文件。", file=sys.stderr)

# Manifest
with MANIFEST_FILE.open("w", encoding="utf-8") as f:
    f.write(f"# 《从存在到秩序》Deep Research 文件清单（{TODAY}）\n\n")
    f.write("## 元文件\n\n")
    for p in meta_paths:
        f.write(f"- `{p.relative_to(REPO_ROOT)}`\n")
    f.write("\n## 章节文件\n\n")
    for p in chapter_paths:
        f.write(f"- `{p.relative_to(REPO_ROOT)}`\n")
    f.write("\n## 附录\n\n")
    for p in appendix_paths:
        f.write(f"- `{p.relative_to(REPO_ROOT)}`\n")

PROMPT_FILE.write_text(PROMPT, encoding="utf-8")

# Full context
with FULL_CONTEXT.open("w", encoding="utf-8") as out:
    out.write(BOOT)
    out.write("\n# Part 1. 元文件\n\n")
    for p in meta_paths:
        out.write("\n\n---\n\n")
        out.write(f"## FILE: `{p.relative_to(REPO_ROOT)}`\n\n")
        out.write(read_text(p).rstrip())
        out.write("\n")

    out.write("\n\n# Part 2. 章节正文（致读者 + Q00–Q28 + 幕间桥）\n\n")
    for p in chapter_paths:
        out.write("\n\n---\n\n")
        out.write(f"## FILE: `{p.relative_to(REPO_ROOT)}`\n\n")
        out.write(read_text(p).rstrip())
        out.write("\n")

    if appendix_paths:
        out.write("\n\n# Part 3. 附录\n\n")
        for p in appendix_paths:
            out.write("\n\n---\n\n")
            out.write(f"## FILE: `{p.relative_to(REPO_ROOT)}`\n\n")
            out.write(read_text(p).rstrip())
            out.write("\n")

# Zip pack
with zipfile.ZipFile(ZIP_FILE, "w", compression=zipfile.ZIP_DEFLATED) as z:
    for p in [FULL_CONTEXT, PROMPT_FILE, MANIFEST_FILE]:
        z.write(p, arcname=p.name)
    for p in meta_paths + chapter_paths + appendix_paths:
        z.write(p, arcname=str(p.relative_to(REPO_ROOT)))

print("已生成 Deep Research 上传包：")
print(f"- {FULL_CONTEXT}")
print(f"- {PROMPT_FILE}")
print(f"- {MANIFEST_FILE}")
print(f"- {ZIP_FILE}")
print("\n最推荐上传给 Pro / Deep Research 的文件：")
print(FULL_CONTEXT)
