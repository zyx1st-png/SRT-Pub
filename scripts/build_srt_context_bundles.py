#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
把 SRT 仓库拼装成若干个可直接喂给大模型的上下文包（canonical 骨架 / CompactCore / 分领域）。

设计纪律（与仓库既有治理一致）：

1. **只拼装，不改写。** 每个来源文件的正文逐字保留；脚本只剥离 YAML frontmatter，
   并把其中承载权威信号的字段（claim_mode / status / canonical / dependency）
   重新渲染成显式的 provenance 头。不做摘要、不做润色、不合并同类项。
2. **护栏三段分离。** §0.2 每条护栏拆成 SOURCE EXTRACT（逐字来源）、
   GENERATED INTERPRETATION（生成器归纳）、USAGE POLICY（规则及其授权依据）。
   不把生成器的判断混进"来源原文"里冒充权威。
3. **锚点失效即失败。** 抽取锚点找不到 → 非零退出码，绝不静默产出缺护栏的包。
4. **可复现。** provenance 在任何写入之前一次性捕获；`--source-ref` /
   `--generated-date` 可固定；`--check` 在临时目录重新生成并逐字比对。

用法：
    uv run python scripts/build_srt_context_bundles.py
    uv run python scripts/build_srt_context_bundles.py --check
产出：
    Operations/Context_Bundles/
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT_DIR = REPO_ROOT / "Operations" / "Context_Bundles"
BUNDLE_DIR_REL = "Operations/Context_Bundles/"
SPINE_BUNDLE_NAME = "SRT_CONTEXT_BUNDLE_SPINE.md"


# --------------------------------------------------------------------------
# 包定义
# --------------------------------------------------------------------------

# 骨架：**人工选择的高优先级 spine**，不是定义权的完备闭包。
#
# 收录依据是 `SRT_AI_START.md` §2 First Sources 与 `CANONICAL_REGISTRY.md` §A/§B，
# 但 registry 列名的文件有 90 余个，本表只取其中一部分。哪些收了、哪些没收、各自在
# registry 里的角色，由 §0.4 的 manifest 差异报告逐条列出——那份报告是本包对
# "完备性"的唯一诚实交代，不要用本表的长度替代它。
SPINE = [
    "SRT_AI_START.md",
    "CANONICAL_REGISTRY.md",
    "Governance/SRT_CLAIM_LADDER.md",
    "Governance/SRT_CLAIM_MODE_AUDIT.md",
    "Core_Law/SRT_L0_Metaphysics.md",
    "Core_Law/SRT_Constitution_Seven_Theses.md",
    # registry §B.5 明写七命题摘要"不替代"以下两个文件。旧版收了摘要却漏了它们。
    "Core_Law/SRT_Reference_Axioms.md",
    "Core_Law/SRT_Reference_Ontology.md",
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

DOMAINS = {
    "AI": {
        "title": "AI 领域",
        "guards": ["AI/SRT_AI_Claim_Status.md", "AI/AI_POSITIONING_NOTE.md"],
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

# --------------------------------------------------------------------------
# 上下文预算
# --------------------------------------------------------------------------
# 旧版把 `SPINE + COMPACTCORE`（合计约 199K token）推荐为 200K 窗口下的跨域方案，
# 等于不给系统提示、用户问题和模型输出留任何余量。现在预算是显式常量，推荐组合必须
# 通过 check_budgets()，超预算的组合无法作为推荐出现。

CONTEXT_WINDOW = 200_000
# 系统提示 + 用户问题 + 一次较长回答所需的余量。
HEADROOM_RESERVE = 30_000
MAX_RECOMMENDED_LOAD = CONTEXT_WINDOW - HEADROOM_RESERVE  # 170_000

# 推荐装载路线。两条路线互斥：骨架路线用于裁定定义，轻量路线用于领域问答。
RECOMMENDED_LOADOUTS: list[tuple[str, list[str], str]] = [
    ("骨架路线（裁定定义时用）", ["SPINE"], "需要确定 SRT 术语、公理、方程、符号含义时，只装这一个。"),
    ("轻量跨域", ["COMPACTCORE"], "只需领域主线、不需裁定定义时用。"),
    ("轻量单域", ["COMPACTCORE", "DOMAIN_PHILOSOPHY"], "跨域主线 + 单个领域（此处以最大的 Philosophy 为例）。"),
    ("最小单域", ["DOMAIN_AI"], "只做单领域问答的最省装法。"),
]

# 明确禁止的组合，附禁止理由。它们会被 check_budgets() 验证为确实超预算——
# 禁令必须由数字支撑，不能只是一句话。
FORBIDDEN_LOADOUTS: list[tuple[str, list[str], str]] = [
    ("SPINE + COMPACTCORE", ["SPINE", "COMPACTCORE"],
     "旧版曾把它推荐为跨域方案；两包合计已**超出**整个窗口，装不下。"),
    ("SPINE + 任一领域包", ["SPINE", "DOMAIN_PHILOSOPHY"],
     "骨架已占大部分预算，叠加后余量不足以容纳系统提示与一次完整回答。"),
]


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


def is_shallow_repo() -> bool:
    return git("rev-parse", "--is-shallow-repository").strip() == "true"


def require_full_history() -> None:
    """浅克隆下 `git log -1 -- <file>` 不返回空，而是返回 graft commit 的日期，
    于是每个文件的"最后改动日期"都变成克隆当天——看似合理，实则全错，恰好摧毁
    本包用来反映陈旧度的那一列。宁可失败也不产出这种数据。"""
    if is_shallow_repo():
        fail(
            "当前是浅克隆（shallow clone），无法取得各文件真实的最后改动日期。\n"
            "  浅克隆下 git 会把所有文件报成 graft commit 的日期，生成的包会声称\n"
            "  每个 canonical 文件都是今天改的——这正好抹掉本包要传达的陈旧度信号。\n"
            "  修复：`git fetch --unshallow`，CI 中设置 actions/checkout 的 fetch-depth: 0。"
        )


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
    return "\n".join(("> " + ln) if ln.strip() else ">" for ln in text.splitlines())


def extract_section(text: str, heading_pattern: str, source: str) -> str:
    m = re.search(rf"^(##\s+{heading_pattern}.*?)$", text, re.M)
    if not m:
        fail(f"锚点缺失：在 {source} 中找不到标题 /{heading_pattern}/")
    start = m.start()
    nxt = re.search(r"^##\s+", text[m.end():], re.M)
    end = m.end() + nxt.start() if nxt else len(text)
    return text[start:end].strip()


# --------------------------------------------------------------------------
# Provenance：任何写入之前一次性捕获
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Provenance:
    sha: str
    branch: str
    generated: str
    dirty: bool


def porcelain_path(line: str) -> str:
    """从 `git status --porcelain` 的一行里取出路径。

    不能用定宽切片：`git()` 会 strip 整个 stdout，第一行的前导空格因此消失，
    ` M path` 变成 `M path`，定宽切法会多切掉一个字符。改为按空白切分。
    """
    rest = line.strip().split(None, 1)
    if len(rest) < 2:
        return ""
    path = rest[1].strip()
    if " -> " in path:  # 重命名：以目的路径为准
        path = path.split(" -> ", 1)[1]
    return path.strip().strip('"')


def working_tree_dirty() -> bool:
    """判断来源工作树是否有未提交改动；生成物目录本身不计入。"""
    for line in git("status", "--porcelain").splitlines():
        path = porcelain_path(line)
        if path and not path.startswith(BUNDLE_DIR_REL):
            return True
    return False


def capture_provenance(source_ref: str | None, generated_date: str | None) -> Provenance:
    return Provenance(
        sha=(source_ref or git("rev-parse", "--short", "HEAD") or "unknown"),
        branch=git("rev-parse", "--abbrev-ref", "HEAD") or "unknown",
        generated=(generated_date or date.today().isoformat()),
        dirty=working_tree_dirty(),
    )


def read_provenance(path: Path) -> Provenance:
    """从既有包的 frontmatter 回读 provenance，供 --check 复现同一份输出。"""
    if not path.exists():
        fail(f"--check 需要既有产出，但找不到 {path}")
    fm, _ = split_frontmatter(path.read_text(encoding="utf-8"))
    missing = [k for k in ("generated", "source_commit", "source_branch", "source_dirty") if k not in fm]
    if missing:
        fail(f"{path.name} frontmatter 缺少 provenance 字段：{', '.join(missing)}")
    return Provenance(
        sha=fm["source_commit"],
        branch=fm["source_branch"],
        generated=fm["generated"],
        dirty=fm["source_dirty"].strip().lower() == "true",
    )


# --------------------------------------------------------------------------
# §0.2 护栏：三段分离（来源原文 / 生成器归纳 / 使用规则）
# --------------------------------------------------------------------------

@dataclass(frozen=True)
class Guardrail:
    gid: str
    title: str
    severity: str
    affected: str
    extracts: list[tuple[str, str]]  # (来源路径说明, 逐字原文)
    interpretation: str
    policy: str
    policy_source: str


def render_guardrail(g: Guardrail) -> str:
    parts = [f"### {g.gid} — {g.title}（严重度：{g.severity}）\n", f"**受影响**：{g.affected}\n"]
    parts.append("#### SOURCE EXTRACT — 来源原文（逐字抽取）\n")
    for label, text in g.extracts:
        parts.append(f"**{label}**：\n\n{blockquote(text)}\n")
    parts.append("#### GENERATED INTERPRETATION — 生成器归纳（**非**来源原文）\n")
    parts.append(g.interpretation.strip() + "\n")
    parts.append("#### USAGE POLICY — 使用规则\n")
    parts.append(f"*授权依据：{g.policy_source}*\n")
    parts.append(g.policy.strip() + "\n")
    return "\n".join(parts)


def guard_p1_t07() -> Guardrail:
    src = "Operations/Audits/SRT_P1_T07_PROOF_HARDENING_AUDIT.md"
    text = read_text(src)

    m = re.search(r"^>\s+\*\*Status\*\*:.*?(?=\n\s*\n)", text, re.M | re.S)
    if not m:
        fail(f"锚点缺失：{src} 中找不到 `> **Status**:` 区块")
    status_para = re.sub(r"^>\s?", "", m.group(0), flags=re.M).strip()
    status_para = status_para.split("\n**Proof Audit")[0].strip()

    # 1.3 修订的语义分层条款。**必须保留**：它限定了 `τ<∞` 只能推出 S1/pathwise
    # 层面的结论；缺了它，读者会把结论提升成无条件的 process-level 判断。
    m13 = re.search(
        r"\(a\)\s*`τ<∞`\s*verdicts stratified by semantics.*?(?=\(b\))", text, re.S
    )
    if not m13:
        fail(f"锚点缺失：{src} 中找不到 1.3 修订的 `τ<∞` 语义分层条款")
    stratification = m13.group(0).strip().rstrip(".")

    m5 = re.search(r"^5\.\s+\*\*What can P1-T07 prove at most\?\*\*.*?$", text, re.M)
    if not m5:
        fail(f"锚点缺失：{src} 中找不到 §0 第 5 问")
    q5 = m5.group(0).strip()

    thm_src = "Core/SRT_Core_21b_Constitutive_Theorems.md"
    thm = read_text(thm_src)
    if "cumulative probability tends toward 1" not in thm:
        fail(
            f"锚点缺失：{thm_src} 中找不到 P1-T07 Proof Sketch Step 3 的原文。"
            "定理可能已被修订——请复核本护栏是否仍然适用，再重新生成。"
        )

    return Guardrail(
        gid="G1",
        title="P1-T07 证明未闭合",
        severity="高",
        affected=f"`{thm_src}` 的 **P1-T07 Constitutive Asymmetry Theorem**（claim level **P1**）",
        extracts=[
            (f"审计自述，来自 `{src}`", status_para),
            (f"审计 1.3 修订的语义分层条款，来自 `{src}`", stratification),
            (f"审计 §0 第 5 问，来自 `{src}`", q5),
        ],
        interpretation=(
            f"该定理 Proof Sketch 第 3 步（"
            f"*neutral `P` ... cumulative probability tends toward 1*）以肯定句写成，"
            f"正文未标注任何保留。上述审计判定恰恰是这一步不闭合：语料并未*确立*每步正 hazard，"
            f"而且即使每步 hazard 为正也不蕴含 almost-sure 终止；`ε-neutral` 在语料中从未被形式定义；"
            f"P1-T06 的 stable ISP 定义是非概率的，S1/S2/S3 随机语义尚未选定。\n\n"
            f"另需注意：`Core/SRT_OPEN_TENSIONS.md` 目前**未登记**本缺口。"
        ),
        policy=(
            "- 不得把 P1-T07 当作已证 P1 定理引用。\n"
            "- 关于 `τ<∞` 只能作**语义分层**的陈述：若某条 realized history 满足 `τ<∞`，"
            "可无条件断言的仅是**该历史上的 S1 / pathwise stability 失败**；"
            "process-level 的 S2 需 `P(τ<∞)>0`，S3 需 `P(τ=∞)=0`。"
            "**在 S1/S2/S3 语义未选定之前，不得据此推出无条件的 process-level "
            "「not a stable ISP」。**\n"
            "- 不要假装 `ε-neutral` 有形式定义。\n"
            "- 「查过 `OPEN_TENSIONS` 没找到」**不**足以证明本命题已封口——该缺口尚未登记在那里。"
        ),
        policy_source="`Governance/SRT_CLAIM_LADDER.md`（P0–P5 阶梯）与 `SRT_AI_START.md` §5 / §8",
    )


def guard_dqo() -> Guardrail:
    src = "STATUS.md"
    text = read_text(src)
    m = re.search(r"已加下游护栏[：:][^。]*。", text)
    if not m:
        fail(f"锚点缺失：{src} 中找不到 d/q/o 下游护栏原句")

    return Guardrail(
        gid="G2",
        title="`d`/`q`/`o` 三轴处于禁运状态",
        severity="中",
        affected="`_SRT_D_VALUE_CANONICAL.md` 的 `d` 定义，以及任何涉及 `q` / `o` 的表述",
        extracts=[(f"来自 `{src}`（2026-07-25 条目）", m.group(0).strip())],
        interpretation=(
            "2026-07-23 至 07-25 的三份对话材料提出具身位重写与 `d`/`q`/`o` 三轴，"
            "台账记录为**全部路由为候选，无一落地**。已知触雷点包括：`d` 取参与率与 "
            "`Def-d-canonical` 的范数定义冲突；`q` 的五个成分中两项落在 `Def-w_i` 的 "
            "`C_i` 定义文字内。\n\n"
            "本包所含 canonical 正文**不含** `d/q/o` 内容——这是正确状态，不是遗漏。"
        ),
        policy=(
            "- 不要从外部对话材料把三轴引入回答。\n"
            "- 不要据此改写 `d` 的定义。\n"
            "- 禁运范围按上述原句：书稿、公共内容、bridge、论文。"
        ),
        policy_source="`STATUS.md` 2026-07-25 条目所记的下游护栏裁决",
    )


def parse_open_hooks() -> tuple[list[dict[str, str]], dict[str, list[str]]]:
    """解析 hook 闭环审计表，按**阻塞目标**分组。

    评审指出的事实错误就出在这里：三张 partial 并非共同受阻于 `T_dir`——两张是
    `T_dir`，第三张是 `Occlusion_Dynamics`。因此分组必须从表格解析得出，
    不能手写成一句摘要。
    """
    src = "Operations/Audits/Hook_Closure_Audit_2026-07-25.md"
    text = read_text(src)

    rows: list[dict[str, str]] = []
    for line in text.splitlines():
        if not line.startswith("|") or line.count("|") < 4:
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        verdict = cells[-1].replace("*", "").strip()
        if not verdict.startswith(("partial", "pending")):
            continue
        rows.append(
            {
                "hook": cells[0].strip("`"),
                "declared": cells[1],
                "actual": cells[2],
                "verdict": verdict,
            }
        )
    if not rows:
        fail(f"锚点缺失：{src} 中解析不到任何 partial/pending 的 hook 行")

    groups: dict[str, list[str]] = {}
    for r in rows:
        if r["verdict"].startswith("partial"):
            m = re.search(r"`([^`]+)`\s*(?:canonical\s*)?\*\*未落地\*\*", r["actual"])
            if not m:
                fail(f"锚点失效：{src} 中 partial 行 `{r['hook']}` 解析不出阻塞目标")
            key = f"`{m.group(1)}` 回写未落地"
        else:
            key = "planned target 从未创建"
        groups.setdefault(key, []).append(r["hook"])
    return rows, groups


def guard_hooks() -> Guardrail:
    src = "Operations/Audits/Hook_Closure_Audit_2026-07-25.md"
    rows, groups = parse_open_hooks()

    planned = re.search(
        r"`(Physics/SRT_Physics_Bridge_v0_2\.md)`", read_text(src)
    )
    if not planned:
        fail(f"锚点缺失：{src} 中找不到 planned target 路径")

    table = "\n".join(
        f"| `{r['hook']}` | {r['declared']} | {r['actual']} | {r['verdict']} |" for r in rows
    )
    grouped = "\n".join(
        f"| {key} | {len(hooks)} | " + ", ".join(f"`{h}`" for h in hooks) + " |"
        for key, hooks in groups.items()
    )

    return Guardrail(
        gid="G3",
        title="存在已裁决但未落地的回写",
        severity="中",
        affected="下表所列各阻塞目标对应的主文；相关正文在本包中是不完整的",
        extracts=[
            (
                f"来自 `{src}` 的 partial / pending 行（逐字）",
                "| Hook | 声明状态 | 实际 | 判定 |\n|---|---|---|---|\n" + table,
            )
        ],
        interpretation=(
            "按**阻塞目标**分组如下（分组由脚本从上表解析得出，非手写摘要）：\n\n"
            "| 阻塞目标 | hook 数 | hooks |\n|---|---:|---|\n" + grouped + "\n\n"
            f"三张 pending 的 target 文档 `{planned.group(1)}` 从未创建。"
            "改 canonical 主定义属 `Governance/SRT_EDIT_PROTOCOL.md` C 类高风险编辑，"
            "须作者授权，ledger 记 `blocked_by: canonical freeze`。"
        ),
        policy=(
            "- 回答涉及上表任一阻塞目标时，注意本包中对应正文**尚未吸收**该笔回写。\n"
            "- 各阻塞目标彼此独立：不要把某一目标的缺口范围套用到另一个上。\n"
            "- 不要把 planned-but-never-created 的 target 当作已存在的文件引用。"
        ),
        policy_source="`Governance/SRT_EDIT_PROTOCOL.md`（C 类编辑）与 `Operations/_SRT_MATERIAL_PIPELINE.md` §5.6.1（ledger 契约）",
    )


def guard_shorthands() -> Guardrail:
    rows = "\n".join(f"| `{k}` | {v} |" for k, v in PATH_SHORTHANDS.items())
    return Guardrail(
        gid="G4",
        title="行文简写路径对照",
        severity="低",
        affected="骨架正文中若干人读简写",
        extracts=[],
        interpretation=(
            "正文中以下写法是人读简写，按字面当作路径解析会落空。原文未改，对照如下：\n\n"
            "| 正文写法 | 实际所指 |\n|---|---|\n" + rows
        ),
        policy="- 遇到上表左列写法时按右列解析，不要报告「文件不存在」。",
        policy_source="生成器维护的对照表（`PATH_SHORTHANDS`）",
    )


def build_guardrails() -> str:
    return "\n\n".join(
        render_guardrail(g) for g in (guard_p1_t07(), guard_dqo(), guard_hooks(), guard_shorthands())
    )


# --------------------------------------------------------------------------
# §0.4 Manifest 差异报告：本包收了什么、没收什么、各自在 registry 里是什么角色
# --------------------------------------------------------------------------

# 分桶。**这是生成器的判断，不是 registry 的原话**，所以每条都附依据，一屏可复核。
#
# 为什么不逐条从 registry 反推：registry 对文件的归属并不规整——同一路径可能只出现在
# 某条目的"注意"散文里（如 `SRT_Reference_Axioms` 只在 §B.5 的注意行被提到），也可能
# 出现在嵌套子项里。按"首次出现即归属"去解析会把文件挂到错误条目上。因此归属用下面的
# 显式表，而**完备性**（哪些没收）用"registry 是否提及该路径"的集合运算——后者可靠。
SPINE_BUCKETS: dict[str, tuple[str, str]] = {
    "_SRT_D_VALUE_CANONICAL.md": ("定义源", "registry §A.1 主锚点"),
    "_SRT_PSI_F_CANONICAL.md": ("定义源", "registry §A.2 主锚点"),
    "_SRT_T_DIR_CANONICAL.md": ("定义源", "registry §A.3 主锚点"),
    "Core/SRT_Core_21_Formal_Axioms.md": ("定义源", "registry §A.4 主锚点（公理路由索引）"),
    "Core/SRT_Core_21_Minimal_Axioms.md": ("定义源", "registry §A.4 分层正文 P0"),
    "Core/SRT_Core_21b_Constitutive_Theorems.md": ("定义源", "registry §A.4 分层正文 P1"),
    "Core/SRT_Core_21c_Bridge_Hypotheses.md": ("定义源", "registry §A.4 分层正文 P2/P3/P4"),
    "Core/SRT_Core_22_Equations.md": ("定义源", "registry §A.4b 主锚点"),
    "Core_Law/SRT_L0_Metaphysics.md": ("定义源", "AI_START §2 First Sources 第 4 位"),
    "Core_Law/SRT_Reference_Axioms.md": ("定义源", "registry §B.5 注：七命题摘要不替代本文件"),
    "Core_Law/SRT_Reference_Ontology.md": ("定义源", "registry §B.5 注：七命题摘要不替代本文件"),
    "_SRT_SYMBOL_TABLE.md": ("定义源", "AI_START §2 First Sources；符号与记号的定义权"),
    "Core/SRT_OPEN_TENSIONS.md": ("治理护栏", "registry §A.4c；未闭合登记，claim_mode: open"),
    "_SRT_CROSS_DOMAIN_MATRIX.md": ("治理护栏", "registry §A.4d 自称 governance-canonical usage layer"),
    "Governance/SRT_CLAIM_LADDER.md": ("治理护栏", "registry §B.5b；P0–P5 硬度阶梯"),
    "Governance/SRT_CLAIM_MODE_AUDIT.md": ("治理护栏", "registry §B.5c；降级台账"),
    "Core_Law/SRT_Constitution_Seven_Theses.md": ("展开层", "registry §B.5；顶层摘要，明写不替代定义源"),
    "CANONICAL_REGISTRY.md": ("导航", "权威层级注册表本身"),
    "SRT_AI_START.md": ("导航", "AI 最小首读入口，frontmatter 自标 ai_do_not_use_for_definition"),
}


def registry_mentions() -> set[str]:
    """registry 中提及的、且确实存在的全部 .md 路径。

    只做成员判定，不做逐条归属——归属见 `SPINE_BUCKETS`。成员判定对这份来源是可靠的，
    也正是"完备性差异"唯一需要的信息。
    """
    text = read_text("CANONICAL_REGISTRY.md")
    found = {
        p for p in re.findall(r"`([A-Za-z0-9_][A-Za-z0-9_/.-]*\.md)`", text)
        if (REPO_ROOT / p).is_file()
    }
    if not found:
        fail("锚点缺失：CANONICAL_REGISTRY.md 中解析不到任何存在的 .md 路径")
    return found


def parse_first_sources() -> list[str]:
    """解析 `SRT_AI_START.md` §2 First Sources 的有序清单。"""
    text = read_text("SRT_AI_START.md")
    start = text.find("## 2. First Sources")
    end = text.find("## 2A.")
    if start == -1 or end == -1:
        fail("锚点缺失：SRT_AI_START.md 中找不到 §2 First Sources 区段")
    seen: list[str] = []
    for path in re.findall(r"`([^`]+\.md)`", text[start:end]):
        if path not in seen:
            seen.append(path)
    if not seen:
        fail("锚点缺失：SRT_AI_START.md §2 中解析不到任何路径")
    return seen


def bucket_for(path: str) -> tuple[str, str]:
    """返回 (分类, 依据)。骨架文件用显式表；其余按自身 frontmatter 判定。"""
    if path in SPINE_BUCKETS:
        return SPINE_BUCKETS[path]
    fm, _ = split_frontmatter(read_text(path))
    mode, ftype = fm.get("claim_mode", "-"), fm.get("type", "-")
    if ftype in {"index", "retrieval_profile"} or mode in {"index", "navigation"}:
        return "导航", f"frontmatter type={ftype} / claim_mode={mode}"
    if mode in {"governance", "open", "audit"}:
        return "治理护栏", f"frontmatter claim_mode={mode}"
    if mode == "canonical":
        return "定义源", "frontmatter claim_mode=canonical"
    return "展开层", f"frontmatter claim_mode={mode}"


def build_manifest_report(bundled: list[str]) -> str:
    mentioned = registry_mentions()
    first_sources = parse_first_sources()

    rows: dict[str, list[str]] = {}
    for path in bundled:
        bucket, basis = bucket_for(path)
        reg = "✓" if path in mentioned else "—"
        fs = "✓" if path in first_sources else "—"
        rows.setdefault(bucket, []).append(f"| `{path}` | {basis} | {reg} | {fs} |")

    parts = [
        "> **这份报告回答一个问题：本包相对 `CANONICAL_REGISTRY.md` 到底缺了什么。**",
        ">",
        "> 本包**不是**定义权的完备闭包，而是**人工选择的高优先级 spine**。",
        "> 下面的分类是**生成器的判断**，不是 registry 的原话；每行都附依据供复核。",
        "> 「registry 提及」「AI_START §2」两列是机械判定的事实。",
        "",
        "### 已收录",
        "",
    ]
    for bucket in ("定义源", "治理护栏", "展开层", "导航"):
        if bucket not in rows:
            continue
        parts += [
            f"**{bucket}**（{len(rows[bucket])} 个）",
            "",
            "| 文件 | 分类依据 | registry 提及 | AI_START §2 |",
            "|---|---|:---:|:---:|",
            *sorted(rows[bucket]),
            "",
        ]

    missing_fs = [p for p in first_sources if p not in bundled and (REPO_ROOT / p).is_file()]
    missing_reg = sorted(p for p in mentioned if p not in bundled)

    parts += ["### 未收录支持文件", ""]
    if missing_fs:
        parts += [
            f"**`SRT_AI_START.md` §2 First Sources 点名但本包未收（{len(missing_fs)} 个）**"
            "——这是最需要注意的一类，回答涉及它们时本包不足以裁定：",
            "",
            *[f"- `{p}`" for p in missing_fs],
            "",
        ]
    else:
        parts += [
            "`SRT_AI_START.md` §2 First Sources **已全部收录**"
            f"（{len(first_sources)} 个）。",
            "",
        ]

    parts += [
        f"**registry 提及但本包未收（{len(missing_reg)} 个）**——多为领域主轴、",
        "展开层与 PH-SS 护栏文件，按需走领域包或直接读仓库，不在骨架路线内：",
        "",
        "<details><summary>展开完整清单</summary>",
        "",
        *[f"- `{p}`" for p in missing_reg],
        "",
        "</details>",
        "",
    ]
    return "\n".join(parts)


# --------------------------------------------------------------------------
# 预算校验
# --------------------------------------------------------------------------

def estimate_tokens(text: str) -> int:
    cjk = len(re.findall(r"[一-鿿]", text))
    return int(cjk * 1.2 + (len(text) - cjk) * 0.29)


def bundle_filename(key: str) -> str:
    if key == "SPINE":
        return SPINE_BUNDLE_NAME
    if key == "COMPACTCORE":
        return "SRT_CONTEXT_BUNDLE_COMPACTCORE.md"
    return f"SRT_CONTEXT_BUNDLE_{key}.md"


def check_budgets(out_dir: Path) -> list[str]:
    """推荐组合必须在预算内；禁止组合必须确实超预算。返回问题列表。"""
    def total(keys: list[str]) -> int:
        return sum(
            estimate_tokens((out_dir / bundle_filename(k)).read_text(encoding="utf-8"))
            for k in keys
        )

    problems = []
    for label, keys, _ in RECOMMENDED_LOADOUTS:
        got = total(keys)
        if got > MAX_RECOMMENDED_LOAD:
            problems.append(
                f"推荐组合超预算：{label} = {got:,} tok > {MAX_RECOMMENDED_LOAD:,}"
                f"（窗口 {CONTEXT_WINDOW:,} − 余量 {HEADROOM_RESERVE:,}）"
            )
    for label, keys, _ in FORBIDDEN_LOADOUTS:
        got = total(keys)
        if got <= MAX_RECOMMENDED_LOAD:
            problems.append(
                f"禁止组合并未超预算：{label} = {got:,} tok ≤ {MAX_RECOMMENDED_LOAD:,}"
                f"——禁令失去数字依据，请复核 FORBIDDEN_LOADOUTS"
            )
    return problems


def build_claim_discipline() -> str:
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
    fm, body = split_frontmatter(read_text(rel))
    claim_mode = fm.get("claim_mode", "(未标注)")
    authority = AUTHORITY_NOTE.get(
        claim_mode, "**非定义源**——可作检索与支持上下文，不得用于确定术语定义。"
    )
    meta = "\n".join(
        f"| {k} | {v} |"
        for k, v in [
            ("path", f"`{rel}`"),
            ("id", fm.get("id", "-")),
            ("claim_mode", claim_mode),
            ("status", fm.get("status", "-")),
            ("epistemic_layer", fm.get("epistemic_layer", "-")),
            ("layer", fm.get("layer", "-")),
            ("canonical(字段)", fm.get("canonical", "-")),
            ("last_commit", last_commit_date(rel)),
        ]
    )
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


def bundle_header(prov: Provenance, bundle_id: str, title: str,
                  purpose: str, files: list[str]) -> str:
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
generated: {prov.generated}
source_commit: {prov.sha}
source_branch: {prov.branch}
source_dirty: {str(prov.dirty).lower()}
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
| 生成日期 | {prov.generated} |
| 来源 commit | `{prov.sha}` |
| 来源分支 | `{prov.branch}` |
| 生成时来源工作树有改动 | {"是" if prov.dirty else "否"} |
| 包含文件数 | {len(files)} |

> **source_commit 契约**：该值是**生成本包时 HEAD 所指的来源快照**。把本包纳入版本库的
> 那个 commit 必然晚于它，因此 `source_commit` 与本文件所在 commit 不相等是正常的，
> 不是漂移。要复核一致性，用 `--check`：它按本 frontmatter 记录的 provenance 重新生成
> 并逐字比对。

### 0.1 文件清单与各自最后改动日期

| # | 文件 | 最后 commit |
|---|---|---|
{manifest}

## §0.2 状态护栏

> **这些是本包正文里读不出来的信息。** 正文中相关命题写得像已经成立，
> 而仓库自己知道它们没有。回答前先读本节。
>
> **每条护栏分三段，权威等级不同，请分别对待**：
>
> - **SOURCE EXTRACT** — 从 `Operations/` 审计台账与 `STATUS.md` 按锚点逐字抽取的原文。
>   锚点若失效，生成脚本直接失败而不会产出缺护栏的包。
> - **GENERATED INTERPRETATION** — **生成器的归纳，不是来源原文**。它压缩了上面的抽取内容，
>   可能丢失限定条件。有疑问时以 SOURCE EXTRACT 为准，再有疑问回查来源文件。
> - **USAGE POLICY** — 由标注的治理文件授权的使用规则。

{build_guardrails()}

## §0.3 claim 阶梯与回答纪律

{build_claim_discipline()}

## §0.4 Manifest 差异报告（本包 vs `CANONICAL_REGISTRY.md`）

{build_manifest_report(files)}

---
"""


SPINE_POINTER = """
> **注意**：本包**不含** canonical 骨架（`d` / `Ψ_f` / `T_dir` 定义、核心公理、
> 主方程、符号表）。领域内容依赖那些定义。若需确定术语含义，请同时加载
> `SRT_CONTEXT_BUNDLE_SPINE.md`；仅凭本包不得裁定任何 SRT 术语的定义。
"""


def generate(prov: Provenance, out_dir: Path) -> list[tuple[str, str, int]]:
    """生成全部包，返回 [(label, filename, n_files)]。"""
    require_full_history()
    out_dir.mkdir(parents=True, exist_ok=True)
    plan: list[tuple[str, str, str, str, list[str], str]] = [
        (
            "骨架 spine", SPINE_BUNDLE_NAME, f"SRT-CONTEXT-BUNDLE-SPINE-{prov.generated}",
            "SRT Canonical 骨架上下文包",
            SPINE,
            "",
        ),
        (
            "CompactCore 全集", "SRT_CONTEXT_BUNDLE_COMPACTCORE.md",
            f"SRT-CONTEXT-BUNDLE-COMPACTCORE-{prov.generated}",
            "SRT CompactCore 全集上下文包",
            [f for cfg in DOMAINS.values() for f in cfg["cores"]],
            SPINE_POINTER,
        ),
    ]
    purposes = {
        SPINE_BUNDLE_NAME: "收录承载定义权的 canonical 主干，供大模型确定 SRT 术语、公理、方程与符号的含义。",
        "SRT_CONTEXT_BUNDLE_COMPACTCORE.md": "收录全部 18 个 CompactCore 文件，覆盖 AI / 物理 / 哲学 / 神经 / 灵性 / 核心动力学的领域主线。",
    }
    for key, cfg in DOMAINS.items():
        name = f"SRT_CONTEXT_BUNDLE_DOMAIN_{key.upper()}.md"
        plan.append(
            (
                f"领域 {key}", name,
                f"SRT-CONTEXT-BUNDLE-DOMAIN-{key.upper()}-{prov.generated}",
                f"SRT {cfg['title']}上下文包",
                [*cfg["guards"], *cfg["nav"], *cfg["cores"]],
                SPINE_POINTER,
            )
        )
        purposes[name] = f"收录{cfg['title']}的 claim-status 护栏、领域导航与 CompactCore 主线。"

    results = []
    for label, name, bid, title, files, note in plan:
        parts = [bundle_header(prov, bid, title, purposes[name], files)]
        if note:
            parts.append(note)
        parts.extend(render_file_block(rel) for rel in files)
        (out_dir / name).write_text("\n".join(parts).rstrip() + "\n", encoding="utf-8")
        results.append((label, name, len(files)))

    write_readme(prov, out_dir, results)

    # 预算是交付契约的一部分：超预算的推荐组合不允许被生成出来。
    problems = check_budgets(out_dir)
    if problems:
        fail("上下文预算校验失败：\n  " + "\n  ".join(problems))
    return results


def write_readme(prov: Provenance, out_dir: Path,
                 results: list[tuple[str, str, int]]) -> None:
    rows = []
    for label, name, n in results:
        text = (out_dir / name).read_text(encoding="utf-8")
        est = estimate_tokens(text)
        rows.append(f"| `{name}` | {label} | {n} | {len(text):,} | ~{est:,} |")

    def total(keys: list[str]) -> int:
        return sum(
            estimate_tokens((out_dir / bundle_filename(k)).read_text(encoding="utf-8"))
            for k in keys
        )

    loadout_rows = "\n".join(
        ["| 路线 | 装载 | 合计 ≈token | 余量 | 用途 |", "|---|---|---:|---:|---|"]
        + [
            f"| {label} | {' + '.join('`'+k+'`' for k in keys)} | {total(keys):,} | "
            f"{CONTEXT_WINDOW - total(keys):,} | {note} |"
            for label, keys, note in RECOMMENDED_LOADOUTS
        ]
    )
    forbidden_rows = "\n".join(
        ["| 组合 | 合计 ≈token | 为什么禁止 |", "|---|---:|---|"]
        + [
            f"| {label} | **{total(keys):,}** | {note} |"
            for label, keys, note in FORBIDDEN_LOADOUTS
        ]
    )

    (out_dir / "README.md").write_text(
        f"""---
id: SRT-CONTEXT-BUNDLES-README
type: index
status: active
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
generated: {prov.generated}
source_commit: {prov.sha}
source_branch: {prov.branch}
source_dirty: {str(prov.dirty).lower()}
---

# SRT 上下文包

由 `scripts/build_srt_context_bundles.py` 自动生成，用于把仓库喂给 Claude Project、
ChatGPT Project 或任何单次对话。**目录内所有文件都是生成物，不要手工编辑**——
改动会在下次运行时被覆盖。要改内容请改来源文件或生成脚本。

## 包清单

| 文件 | 内容 | 来源文件数 | 字符数 | ≈token |
|---|---|---:|---:|---:|
{chr(10).join(rows)}

## 上下文预算

窗口按 **{CONTEXT_WINDOW:,} token** 计，预留 **{HEADROOM_RESERVE:,}** 给系统提示、
用户问题与模型输出，因此单次装载上限 **{MAX_RECOMMENDED_LOAD:,} token**。

下表由生成脚本计算并校验；**超预算的组合无法作为推荐存在**——`check_budgets()`
会让构建直接失败。

### 推荐装载路线

{loadout_rows}

### 禁止的组合

{forbidden_rows}

**两条路线互斥。** 骨架路线用于裁定定义；轻量路线用于领域问答。不要把 `SPINE`
和其他包叠加——骨架本身已占去大部分预算。

## 三条使用纪律

1. **本目录不是 canonical，也不是定义权的完备闭包。** `SPINE` 是**人工选择的高优先级
   spine**：registry 列名的文件有 90 余个，骨架只取其中一部分。收了什么、漏了什么、
   各自角色如何，见每个包的 **§0.4 Manifest 差异报告**。与仓库来源文件冲突时以仓库为准。
2. **§0.2 状态护栏必读**，并注意其三段的权威等级不同：SOURCE EXTRACT 是逐字原文，
   GENERATED INTERPRETATION 是生成器归纳（可能丢失限定条件），USAGE POLICY 是
   由治理文件授权的规则。有疑问以 SOURCE EXTRACT 为准。
3. **仓库内部工作不要读本目录。** 直接读来源文件。本目录是给外部对话用的。

## 重新生成与校验

```bash
uv run python scripts/build_srt_context_bundles.py
uv run python scripts/build_srt_context_bundles.py --check     # 确定性校验
```

`--check` 按既有产出 frontmatter 记录的 provenance 重新生成到临时目录并逐字比对，
因此可在 CI 中确定性运行。`--source-ref` / `--generated-date` 可固定 provenance。

护栏层按锚点抽取自 `Operations/` 审计台账与 `STATUS.md`。**任一锚点失效，脚本会
直接以非零码退出**，而不会产出一个缺护栏的包。P1-T07 若日后被修订，脚本同样会
失败，强制复核该护栏是否仍适用——这是刻意的防漂移设计。

`source_commit` 记录生成时 HEAD 的来源快照；引入本目录的 commit 必然晚于它，
两者不相等属正常。
""",
        encoding="utf-8",
    )


# --------------------------------------------------------------------------
# 入口
# --------------------------------------------------------------------------

def run_check(out_dir: Path) -> None:
    prov = read_provenance(out_dir / SPINE_BUNDLE_NAME)
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        generate(prov, tmp)
        expected = sorted(p.name for p in tmp.glob("*.md"))
        actual = sorted(p.name for p in out_dir.glob("*.md"))
        if expected != actual:
            fail(f"文件集合不一致：\n  重新生成 {expected}\n  既有产出 {actual}")
        diffs = [
            name
            for name in expected
            if (tmp / name).read_text(encoding="utf-8")
            != (out_dir / name).read_text(encoding="utf-8")
        ]
        if diffs:
            fail(
                "以下产出与来源不一致（请重新运行生成脚本并提交）：\n  "
                + "\n  ".join(diffs)
            )
    print(f"check: {len(expected)} 个文件逐字一致（provenance: {prov.sha} @ {prov.generated}）")


def main() -> None:
    ap = argparse.ArgumentParser(description="生成 SRT 上下文包")
    ap.add_argument("--check", action="store_true",
                    help="按既有产出的 provenance 重新生成到临时目录并逐字比对，不写入")
    ap.add_argument("--source-ref", help="固定记录的来源 commit（默认取当前 HEAD 短 SHA）")
    ap.add_argument("--generated-date", help="固定记录的生成日期 YYYY-MM-DD（默认今天）")
    ap.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR), help="产出目录")
    args = ap.parse_args()

    out_dir = Path(args.out_dir)
    if args.check:
        run_check(out_dir)
        return

    # provenance 在任何写入之前一次性捕获，保证同一次生成的所有包记录一致。
    prov = capture_provenance(args.source_ref, args.generated_date)
    results = generate(prov, out_dir)

    print(f"已生成 {len(results)} 个上下文包 + README → {out_dir}/")
    print(f"provenance: commit={prov.sha} date={prov.generated} dirty={prov.dirty}\n")
    print(f"{'包':<22}{'文件数':>6}{'字符数':>10}{'≈token':>10}  文件名")
    print("-" * 88)
    total = 0
    for label, name, n in results:
        text = (out_dir / name).read_text(encoding="utf-8")
        chars = len(text)
        cjk = len(re.findall(r"[一-鿿]", text))
        total += chars
        print(f"{label:<22}{n:>6}{chars:>10,}{int(cjk*1.2+(chars-cjk)*0.29):>10,}  {name}")
    print("-" * 88)
    print(f"{'合计':<22}{'':>6}{total:>10,}")


if __name__ == "__main__":
    main()
