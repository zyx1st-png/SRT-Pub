#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把 SRT 仓库拼装成若干个可直接喂给大模型的上下文包（canonical 骨架 / CompactCore / 分领域）。

设计纪律（与仓库既有治理一致）：

1. **只拼装，不改写。** 每个来源文件的正文逐字保留；脚本只剥离 YAML frontmatter，
   并把其中承载权威信号的字段（claim_mode / status / canonical / dependency）
   重新渲染成显式的 provenance 头。不做摘要、不做润色、不合并同类项。
2. **§0 护栏层全部自动抽取。** 未闭合命题、下游禁令、被冻结的回写，一律从
   Operations/ 台账与 STATUS.md 里按锚点抽取原话。任一锚点找不到 → 脚本以非零
   退出码失败，绝不静默产出一个没有护栏的包。
3. **claim level 不得被拼装抹平。** P0-P5 阶梯与最小回答协议从 `SRT_AI_START.md`
   原样注入每个包，使不含该文件的 CompactCore / 领域包也带着同一套边界。

用法：
    uv run python scripts/build_srt_context_bundles.py
产出：
    Operations/Context_Bundles/
"""

from __future__ import annotations

import re
import subprocess
import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = REPO_ROOT / "Operations" / "Context_Bundles"
TODAY = date.today().isoformat()


# --------------------------------------------------------------------------
# 包定义
# --------------------------------------------------------------------------

# 骨架：承载定义权的 canonical 主干。顺序即建议阅读顺序。
SPINE = [
    "SRT_AI_START.md",
    "CANONICAL_REGISTRY.md",
    "Governance/SRT_CLAIM_LADDER.md",
    "Core_Law/SRT_L0_Metaphysics.md",
    "Core_Law/SRT_Constitution_Seven_Theses.md",
    "Core/SRT_Core_21_Formal_Axioms.md",
    "Core/SRT_Core_21_Minimal_Axioms.md",
    "Core/SRT_Core_21b_Constitutive_Theorems.md",
    "Core/SRT_Core_21c_Bridge_Hypotheses.md",
    "_SRT_D_VALUE_CANONICAL.md",
    "_SRT_PSI_F_CANONICAL.md",
    "_SRT_T_DIR_CANONICAL.md",
    "_SRT_CROSS_DOMAIN_MATRIX.md",
    "Core/SRT_Core_22_Equations.md",
    "_SRT_SYMBOL_TABLE.md",
    "Core/SRT_OPEN_TENSIONS.md",
]

# 领域包：每个领域先放 claim-status（反过度声称护栏），再放导航，最后放 CompactCore。
DOMAINS = {
    "AI": {
        "title": "AI 领域",
        "guards": [
            "AI/SRT_AI_Claim_Status.md",
            "AI/AI_POSITIONING_NOTE.md",
        ],
        "nav": ["AI/README.md"],
        "cores": [
            "AI/SRT_AI_01_Ontology_CompactCore.md",
            "AI/SRT_AI_Architecture_CompactCore.md",
            "AI/SRT_AI_03_Consciousness_Framework_CompactCore.md",
        ],
    },
    "Physics": {
        "title": "物理领域",
        "guards": ["Physics/SRT_Physics_Claim_Status.md"],
        "nav": ["Physics/PHYSICS_COMPACT_REGISTRY.md", "Physics/README.md"],
        "cores": [
            "Physics/SRT_Quant_00_Intro_CompactCore.md",
            "Physics/SRT_Quant_01_Selection_CompactCore.md",
            "Physics/SRT_Quant_02_Cosmology_CompactCore.md",
            "Physics/SRT_Physics_Cosmology_CompactCore.md",
            "Physics/SRT_Phys_07_Complex_Systems_CompactCore.md",
            "Physics/SRT_Phys_08_Ontology_Ext_CompactCore.md",
            "Physics/SRT_Phys_09_Formalism_Ext_CompactCore.md",
            "Physics/SRT_Phys_10_Integration_CompactCore.md",
        ],
    },
    "Philosophy": {
        "title": "哲学领域",
        "guards": [
            "Philosophy/SRT_Philosophy_Claim_Status.md",
            "Philosophy/00_READ_FIRST_Philosophy_Hardening_Soft_Spots.md",
        ],
        "nav": ["Philosophy/_PHILOSOPHY_MACHINE_INDEX.md"],
        "cores": [
            "Philosophy/SRT_Philosophy_Foundations_CompactCore.md",
            "Philosophy/SRT_Social_Economics_CompactCore.md",
            "Philosophy/SRT_Political_Philosophy_CompactCore.md",
        ],
    },
    "Neuroscience": {
        "title": "神经科学领域",
        "guards": ["Neuroscience/SRT_Neuroscience_Claim_Status.md"],
        "nav": ["Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md", "Neuroscience/README.md"],
        "cores": [
            "Neuroscience/SRT_Neural_Mechanisms_CompactCore.md",
            "Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md",
        ],
    },
    "Spirituality": {
        "title": "灵性领域",
        "guards": ["Spirituality/SRT_Spirituality_Claim_Status.md"],
        "nav": ["Spirituality/SPIRITUALITY_COMPACT_REGISTRY.md"],
        "cores": ["Spirituality/SRT_Spirit_09_Praxis_CompactCore.md"],
    },
    "Core": {
        "title": "核心动力学",
        "guards": [],
        "nav": [],
        "cores": ["Core/SRT_Core_14_Dynamics_Scaling_CompactCore.md"],
    },
}

# 已知的行文简写 → 真实路径。骨架正文里这些是人读简写，机器按字面找会落空。
# 不改原文，只在 §0 给出对照表。
PATH_SHORTHANDS = {
    "Core_21_Formal_Axioms.md": "Core/SRT_Core_21_Formal_Axioms.md",
    "_SRT_SYMBOL_QUICK_GUARD.md": "SRT_AI_START.md §3（已于 2026-07-20 并入，原文件不再存在）",
}


# --------------------------------------------------------------------------
# 基础工具
# --------------------------------------------------------------------------

def fail(msg: str) -> None:
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def read_text(rel: str) -> str:
    p = REPO_ROOT / rel
    if not p.exists():
        fail(f"来源文件不存在：{rel}")
    return p.read_text(encoding="utf-8")


def git(*args: str) -> str:
    try:
        return subprocess.run(
            ["git", *args], cwd=REPO_ROOT, capture_output=True, text=True, check=True
        ).stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return ""


def last_commit_date(rel: str) -> str:
    return git("log", "-1", "--format=%ad", "--date=short", "--", rel) or "unknown"


def split_frontmatter(text: str) -> tuple[dict[str, str], str]:
    """剥离 YAML frontmatter，返回 (字段字典, 正文)。容忍列表型取值。"""
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end == -1:
        return {}, text
    raw = text[3:end].strip("\n")
    body = text[end + 4 :].lstrip("\n")

    fields: dict[str, str] = {}
    current: str | None = None
    for line in raw.splitlines():
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if m:
            current = m.group(1)
            fields[current] = m.group(2).strip()
        elif current and re.match(r"^\s+-\s+", line):
            item = re.sub(r"^\s+-\s+", "", line).strip()
            fields[current] = (fields[current] + ", " + item).strip(", ")
    return fields, body


def blockquote(text: str) -> str:
    """把多行文本整体转成 markdown 引用块（每行都加 `>`）。"""
    return "\n".join(("> " + ln) if ln.strip() else ">" for ln in text.splitlines())


def extract_section(text: str, heading_pattern: str, source: str) -> str:
    """抽取 `## <heading>` 到下一个同级标题之间的内容。找不到即失败。"""
    m = re.search(rf"^(##\s+{heading_pattern}.*?)$", text, re.M)
    if not m:
        fail(f"锚点缺失：在 {source} 中找不到标题 /{heading_pattern}/")
    start = m.start()
    nxt = re.search(r"^##\s+", text[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(text)
    return text[start:end].strip()


# --------------------------------------------------------------------------
# §0 护栏层：全部自动抽取，锚点缺失即失败
# --------------------------------------------------------------------------

def guard_p1_t07() -> str:
    src = "Operations/Audits/SRT_P1_T07_PROOF_HARDENING_AUDIT.md"
    text = read_text(src)

    # 审计自述的 Status 区块（首个 blockquote 段），说明它改动了什么、没改什么。
    # 只取首段：其后的 1.1/1.2/1.3 修订史属版本噪音，不进护栏。
    m = re.search(r"^>\s+\*\*Status\*\*:.*?(?=\n\s*\n)", text, re.M | re.S)
    if not m:
        fail(f"锚点缺失：{src} 中找不到 `> **Status**:` 区块")
    status_para = re.sub(r"^>\s?", "", m.group(0), flags=re.M).strip()
    status_para = status_para.split("\n**Proof Audit")[0].strip()

    # §0 第 5 问：这条定理最多能证到什么。
    m5 = re.search(r"^5\.\s+\*\*What can P1-T07 prove at most\?\*\*.*?$", text, re.M)
    if not m5:
        fail(f"锚点缺失：{src} 中找不到 §0 第 5 问")
    q5 = m5.group(0).strip()

    # 定理原文所在位置，确认 Proof Sketch Step 3 仍是原样。
    thm_src = "Core/SRT_Core_21b_Constitutive_Theorems.md"
    thm = read_text(thm_src)
    if "cumulative probability tends toward 1" not in thm:
        fail(
            f"锚点缺失：{thm_src} 中找不到 P1-T07 Proof Sketch Step 3 的原文。"
            "定理可能已被修订——请复核本护栏是否仍然适用，再重新生成。"
        )

    return f"""### G1 — P1-T07 证明未闭合（严重度：高）

**受影响**：`{thm_src}` 的 **P1-T07 Constitutive Asymmetry Theorem**（claim level **P1**）。

**问题**：该定理 Proof Sketch 第 3 步以肯定句写成，正文并未标注任何保留。
但 `{src}`（已合入 main）判定恰恰是这一步不闭合。

**审计自述（原文）**：

{blockquote(status_para)}

**审计 §0 第 5 问（原文）**：

{blockquote(q5)}

**使用规则**：
- 不得把 P1-T07 当作已证 P1 定理引用；
- 唯一可无条件陈述的是 "if `τ<∞` then not a stable ISP"；
- `ε-neutral` 在语料中**从未被形式定义**，不要假装它有定义；
- 注意：`Core/SRT_OPEN_TENSIONS.md` **尚未登记**本缺口，所以"查过 OPEN_TENSIONS"
  不足以证明这条命题已封口。
"""


def guard_dqo() -> str:
    src = "STATUS.md"
    text = read_text(src)
    m = re.search(r"已加下游护栏[：:][^。]*。", text)
    if not m:
        fail(f"锚点缺失：{src} 中找不到 d/q/o 下游护栏原句")
    embargo = m.group(0).strip()

    return f"""### G2 — `d`/`q`/`o` 三轴处于禁运状态（严重度：中）

**来源**：`{src}`（2026-07-25 条目）

**原话**：

> {embargo}

**背景**：2026-07-23 至 07-25 的三份对话材料提出具身位重写与 `d`/`q`/`o` 三轴。
台账记录为**全部路由为候选，无一落地**。已知触雷点包括：`d` 取参与率与
`Def-d-canonical` 的范数定义冲突；`q` 的五个成分中两项落在 `Def-w_i` 的 `C_i`
定义文字内。

**使用规则**：本包所含 canonical 正文**不含** `d/q/o` 内容，这是正确状态。
不要从外部对话材料把三轴引入回答，也不要据此改写 `d` 的定义。
"""


def guard_hooks() -> str:
    src = "Operations/Audits/Hook_Closure_Audit_2026-07-25.md"
    text = read_text(src)

    rows = []
    for line in text.splitlines():
        if not line.startswith("|") or line.count("|") < 4:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        verdict = cells[-1].replace("*", "").strip()
        if verdict.startswith(("partial", "pending")):
            rows.append(cells)
    if not rows:
        fail(f"锚点缺失：{src} 中解析不到任何 partial/pending 的 hook 行")

    table = "\n".join("| " + " | ".join(c for c in r) + " |" for r in rows)
    return f"""### G3 — 存在已裁决但未落地的回写（严重度：中）

**来源**：`{src}`（18 张 hook 实证体检）

以下 hook 的目标内容**尚未写入**对应主文，因此本包的相关正文是不完整的：

| Hook | 声明状态 | 实际 | 判定 |
|---|---|---|---|
{table}

**要点**：其中三张 partial 的共同阻塞点是 **`_SRT_T_DIR_CANONICAL.md` 未落地**——
改 `T_dir` 主定义属 `Governance/SRT_EDIT_PROTOCOL.md` C 类高风险编辑，须作者授权，
ledger 记 `blocked_by: canonical freeze`。三张 pending 的 target 文档
`Physics/SRT_Physics_Bridge_v0_2.md` **从未创建**。

**使用规则**：回答涉及 `T_dir` 时，注意本包中的 `T_dir` canonical 尚未吸收
agency 侧的三笔回写；不要把它当作已完整的 `T_dir` 论述。
"""


def guard_shorthands() -> str:
    rows = "\n".join(f"| `{k}` | {v} |" for k, v in PATH_SHORTHANDS.items())
    return f"""### G4 — 行文简写路径对照（严重度：低）

正文中以下写法是人读简写，按字面当作路径会落空。原文未改，对照如下：

| 正文写法 | 实际所指 |
|---|---|
{rows}
"""


def build_guardrails() -> str:
    parts = [guard_p1_t07(), guard_dqo(), guard_hooks(), guard_shorthands()]
    return "\n\n".join(parts)


def build_claim_discipline() -> str:
    """从 SRT_AI_START 原样注入 claim 阶梯与最小回答协议。"""
    text = read_text("SRT_AI_START.md")
    ladder = extract_section(text, r"5\.\s+Claim-Level Guard", "SRT_AI_START.md")
    protocol = extract_section(text, r"8\.\s+Minimal Answer Protocol", "SRT_AI_START.md")
    return (
        "以下两节从 `SRT_AI_START.md` 原样抄入，适用于本包全部内容。\n\n"
        + ladder.replace("## ", "### ", 1)
        + "\n\n"
        + protocol.replace("## ", "### ", 1)
    )


# --------------------------------------------------------------------------
# 拼装
# --------------------------------------------------------------------------

AUTHORITY_NOTE = {
    "canonical": "**定义源**——可用于确定 SRT 术语含义。",
    "open": "**未闭合登记**——其中条目不得被陈述为已封口。",
    "mixed": "混合层——含 bridge/lab 内容，按各条自带的 claim level 读。",
}


def render_file_block(rel: str) -> str:
    raw = read_text(rel)
    fm, body = split_frontmatter(raw)

    claim_mode = fm.get("claim_mode", "(未标注)")
    authority = AUTHORITY_NOTE.get(
        claim_mode, "**非定义源**——可作检索与支持上下文，不得用于确定术语定义。"
    )

    meta_rows = [
        ("path", f"`{rel}`"),
        ("id", fm.get("id", "-")),
        ("claim_mode", claim_mode),
        ("status", fm.get("status", "-")),
        ("epistemic_layer", fm.get("epistemic_layer", "-")),
        ("layer", fm.get("layer", "-")),
        ("canonical(字段)", fm.get("canonical", "-")),
        ("last_commit", last_commit_date(rel)),
    ]
    meta = "\n".join(f"| {k} | {v} |" for k, v in meta_rows)
    dep = fm.get("dependency", "").strip()
    dep_line = f"\n**dependency**：{dep}\n" if dep else ""

    return f"""

---

## FILE: `{rel}`

| 字段 | 值 |
|---|---|
{meta}

**权威判读**：{authority}
{dep_line}
<!-- 以下为原文逐字保留 -->

{body.rstrip()}
"""


def bundle_header(bundle_id: str, title: str, purpose: str, files: list[str]) -> str:
    sha = git("rev-parse", "--short", "HEAD") or "unknown"
    branch = git("rev-parse", "--abbrev-ref", "HEAD") or "unknown"
    dirty = "是（工作树有未提交改动）" if git("status", "--porcelain") else "否"

    manifest = "\n".join(
        f"| {i} | `{f}` | {last_commit_date(f)} |" for i, f in enumerate(files, 1)
    )

    return f"""---
id: {bundle_id}
type: context_bundle
status: active
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
generated: {TODAY}
source_commit: {sha}
source_branch: {branch}
---

# {title}

> **这是什么**：由 `scripts/build_srt_context_bundles.py` 从 SRT 仓库自动拼装的上下文包。
> {purpose}
>
> **这不是什么**：不是新的 canonical 文件，不是摘要，不是改写。每个来源文件的正文
> 逐字保留；脚本只把 YAML frontmatter 转成显式 provenance 头。**若本包与仓库中的
> 来源文件冲突，以仓库为准**——本包是快照，会随仓库演进而过期。

## §0 生成信息

| 项 | 值 |
|---|---|
| 生成日期 | {TODAY} |
| 来源 commit | `{sha}` |
| 来源分支 | `{branch}` |
| 生成时工作树有改动 | {dirty} |
| 包含文件数 | {len(files)} |

### 0.1 文件清单与各自最后改动日期

| # | 文件 | 最后 commit |
|---|---|---|
{manifest}

## §0.2 状态护栏（自动抽取自仓库台账）

> 本节内容不是拼装者的判断，全部按锚点抽取自 `Operations/` 审计台账与 `STATUS.md`。
> 抽取锚点若失效，生成脚本会直接失败而不会产出缺护栏的包。
>
> **这些是本包正文里读不出来的信息。** 正文中相关命题写得像已经成立，
> 而仓库自己知道它们没有。回答前先读本节。

{build_guardrails()}

## §0.3 claim 阶梯与回答纪律

{build_claim_discipline()}

---
"""


def write_bundle(filename: str, bundle_id: str, title: str, purpose: str,
                 files: list[str], extra_note: str = "") -> Path:
    parts = [bundle_header(bundle_id, title, purpose, files)]
    if extra_note:
        parts.append(extra_note)
    for rel in files:
        parts.append(render_file_block(rel))

    out = OUT_DIR / filename
    out.write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
    return out


SPINE_POINTER = """
> **注意**：本包**不含** canonical 骨架（`d` / `Ψ_f` / `T_dir` 定义、核心公理、
> 主方程、符号表）。领域内容依赖那些定义。若需确定术语含义，请同时加载
> `SRT_CONTEXT_BUNDLE_SPINE.md`；仅凭本包不得裁定任何 SRT 术语的定义。
"""


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    results: list[tuple[str, Path, int]] = []

    # 1) 骨架包
    p = write_bundle(
        "SRT_CONTEXT_BUNDLE_SPINE.md",
        f"SRT-CONTEXT-BUNDLE-SPINE-{TODAY}",
        "SRT Canonical 骨架上下文包",
        "收录承载定义权的 canonical 主干，供大模型确定 SRT 术语、公理、方程与符号的含义。",
        SPINE,
    )
    results.append(("骨架 spine", p, len(SPINE)))

    # 2) CompactCore 全集
    all_cores: list[str] = []
    for cfg in DOMAINS.values():
        all_cores.extend(cfg["cores"])
    p = write_bundle(
        "SRT_CONTEXT_BUNDLE_COMPACTCORE.md",
        f"SRT-CONTEXT-BUNDLE-COMPACTCORE-{TODAY}",
        "SRT CompactCore 全集上下文包",
        "收录全部 18 个 CompactCore 文件，覆盖 AI / 物理 / 哲学 / 神经 / 灵性 / 核心动力学的领域主线。",
        all_cores,
        extra_note=SPINE_POINTER,
    )
    results.append(("CompactCore 全集", p, len(all_cores)))

    # 3) 分领域包
    for key, cfg in DOMAINS.items():
        files = [*cfg["guards"], *cfg["nav"], *cfg["cores"]]
        p = write_bundle(
            f"SRT_CONTEXT_BUNDLE_DOMAIN_{key.upper()}.md",
            f"SRT-CONTEXT-BUNDLE-DOMAIN-{key.upper()}-{TODAY}",
            f"SRT {cfg['title']}上下文包",
            f"收录{cfg['title']}的 claim-status 护栏、领域导航与 CompactCore 主线。",
            files,
            extra_note=SPINE_POINTER,
        )
        results.append((f"领域 {key}", p, len(files)))

    # 统计
    stats = []
    total = 0
    for label, path, n in results:
        text = path.read_text(encoding="utf-8")
        chars = len(text)
        cjk = len(re.findall(r"[一-鿿]", text))
        est = int(cjk * 1.2 + (chars - cjk) * 0.29)
        total += chars
        stats.append((label, path, n, chars, est))

    write_readme(stats)

    print(f"已生成 {len(results)} 个上下文包 + README → {OUT_DIR.relative_to(REPO_ROOT)}/\n")
    print(f"{'包':<22}{'文件数':>6}{'字符数':>10}{'≈token':>10}  文件名")
    print("-" * 88)
    for label, path, n, chars, est in stats:
        print(f"{label:<22}{n:>6}{chars:>10,}{est:>10,}  {path.name}")
    print("-" * 88)
    print(f"{'合计':<22}{'':>6}{total:>10,}")


def write_readme(stats: list[tuple[str, Path, int, int, int]]) -> None:
    sha = git("rev-parse", "--short", "HEAD") or "unknown"
    rows = "\n".join(
        f"| `{p.name}` | {label} | {n} | {c:,} | ~{e:,} |" for label, p, n, c, e in stats
    )
    (OUT_DIR / "README.md").write_text(
        f"""---
id: SRT-CONTEXT-BUNDLES-README
type: index
status: active
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
generated: {TODAY}
source_commit: {sha}
---

# SRT 上下文包

由 `scripts/build_srt_context_bundles.py` 自动生成，用于把仓库喂给 Claude Project、
ChatGPT Project 或任何单次对话。**目录内所有文件都是生成物，不要手工编辑**——
改动会在下次运行时被覆盖。要改内容请改来源文件或生成脚本。

## 包清单

| 文件 | 内容 | 来源文件数 | 字符数 | ≈token |
|---|---|---:|---:|---:|
{rows}

## 该用哪个

- **只装一个** → `SPINE`。它含承载定义权的 canonical 主干（`d` / `Ψ_f` / `T_dir`
  定义、核心公理、主方程、符号表、未闭合登记），约 13–14 万 token，可整个塞进
  一次 200K 对话，不必依赖检索命中。
- **要跨域回答** → `SPINE` + `COMPACTCORE`。
- **只做单领域** → `SPINE` + 对应 `DOMAIN_*`。领域包**不含**定义源，单独使用
  不足以裁定任何 SRT 术语。

## 三条使用纪律

1. **本目录不是 canonical。** 与仓库来源文件冲突时以仓库为准。包是快照。
2. **§0.2 状态护栏必读。** 那里记录了正文读不出来的东西——未闭合的证明、
   处于禁运的概念、被冻结挡住的回写。正文里这些命题写得像已经成立。
3. **仓库内部工作不要读本目录。** 直接读来源文件。本目录是给外部对话用的。

## 重新生成

```bash
uv run python scripts/build_srt_context_bundles.py
```

护栏层按锚点抽取自 `Operations/` 审计台账与 `STATUS.md`。**任一锚点失效，脚本会
直接以非零码退出**，而不会产出一个缺护栏的包。P1-T07 若日后被修订，脚本同样会
失败，强制复核该护栏是否仍适用——这是刻意的防漂移设计。
""",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
