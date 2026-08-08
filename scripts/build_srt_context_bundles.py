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
4. **可复现且可验真。** provenance 在任何写入之前一次性捕获；`inputs_digest` 覆盖
   生成脚本、护栏来源与全部正文，`--check` 重算摘要并在临时目录重新生成逐字比对。
   刻意不做 commit 祖先校验——那会让 squash / rebase 合并后的 main 必红。

用法：
    uv run python scripts/build_srt_context_bundles.py
    uv run python scripts/build_srt_context_bundles.py --check
产出：
    Operations/Context_Bundles/
"""

from __future__ import annotations

import argparse
import hashlib
import json
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
    # 七命题摘要 + Reference_Axioms / Reference_Ontology 三者一并移出（2026-07-27）。
    # 起因是预算：估算是字符启发式而非真实 tokenizer，必须留够误差余量。取舍逻辑是
    # 连带的——registry §B.5 说七命题摘要"不替代"那两个 Reference 文件，所以先前
    # 「收摘要、漏 Reference」是不自洽的；把摘要一并移出后，骨架只留真正的 canonical
    # 定义锚点（d / Ψ_f / T_dir / Core_21* / Core_22 / 符号表）与治理护栏，自洽且更瘦。
    # 三者都在 §0.4「未收录支持文件」里逐条列名并说明关系，不是被悄悄丢掉。
    # 三者均不在 AI_START §2 First Sources 内，故 First Sources 覆盖率不受影响。
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

# token 数是**字符启发式估算**，不是任何目标模型的真实 tokenizer。系数刻意取在偏高
# 一侧（CJK 实际约 1.0–1.1 tok/字，此处按 1.2；拉丁实际约 0.25，此处按 0.29），所以
# 估算值倾向于高估——对预算而言这是安全方向。但"偏保守"不等于"精确"，因此额外留
# 出误差余量，且不把预算校验称作保证。
CONTEXT_WINDOW = 200_000
# 系统提示 + 用户问题 + 一次较长回答，再加上估算误差的缓冲。
HEADROOM_RESERVE = 45_000
MAX_RECOMMENDED_LOAD = CONTEXT_WINDOW - HEADROOM_RESERVE  # 155_000

# 推荐装载路线。两条路线互斥：骨架路线用于裁定定义，轻量路线用于领域问答。
RECOMMENDED_LOADOUTS: list[tuple[str, list[str], str]] = [
    ("骨架路线（裁定定义时用）", ["SPINE"], "需要确定 SRT 术语、公理、方程、符号含义时，只装这一个。"),
    ("轻量跨域", ["COMPACTCORE"], "只需领域主线、不需裁定定义时用。"),
    # 不推荐 COMPACTCORE + DOMAIN_X：COMPACTCORE 已含全部领域的 CompactCore，
    # 领域包会把同一批文件再装一遍（Philosophy 情形下重复 3 个文件）。领域包自带
    # claim-status 护栏与导航，单独使用即可。
    ("单域（体量最大者：Philosophy）", ["DOMAIN_PHILOSOPHY"],
     "单领域问答；领域包自带 claim-status 护栏与导航。"),
    ("单域（体量最小者：Core 动力学）", ["DOMAIN_CORE"], "最省的一种装法。"),
]

# 明确禁止的组合，附禁止理由。它们会被 check_budgets() 验证为**确实超预算**——
# 禁令必须由数字支撑，不能只是一句话。
#
# 注意这里只列 SPINE + COMPACTCORE。此前还写过一条"SPINE + 任一领域包"，但它只拿最大的
# Philosophy 做校验，而骨架瘦身后 `SPINE + DOMAIN_CORE` 实际落在预算内——那条禁令的
# 措辞覆盖不了它验证过的范围。逐个领域的实际数字改由 README 的对照表给出。
FORBIDDEN_LOADOUTS: list[tuple[str, list[str], str]] = [
    ("SPINE + COMPACTCORE", ["SPINE", "COMPACTCORE"],
     "旧版曾把它推荐为跨域方案；两包合计已**超出**整个窗口，装不下。"),
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
    digest: str = ""   # 输入闭包的内容摘要；这是真实性判据，sha 仅供参考


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


# --------------------------------------------------------------------------
# 输入闭包与内容摘要
# --------------------------------------------------------------------------
# 生成结果不只依赖正文文件：§0.2 护栏读 STATUS.md 与两份审计，§0.4 读 registry 与
# AI_START，输出形态还取决于生成脚本本身。只对正文列表做校验，会漏掉这些隐式输入。
GENERATOR_SELF = "scripts/build_srt_context_bundles.py"
ACTIVE_THEORY_MANIFEST = "Operations/Audits/data/srt_active_theory_nodes.json"
GUARDRAIL_SOURCES = [
    "STATUS.md",
    "CANONICAL_REGISTRY.md",
    "SRT_AI_START.md",
    "Core/SRT_Core_21b_Constitutive_Theorems.md",
    "Operations/Audits/SRT_P1_T07_PROOF_HARDENING_AUDIT.md",
    "Operations/Audits/Hook_Closure_Audit_2026-07-25.md",
    ACTIVE_THEORY_MANIFEST,
]


def load_active_theory_nodes() -> list[dict]:
    """节点清单是**人工维护**的，脚本只读不写。

    这条通道解决的问题是：包定义是静态人工清单，新建的 bridge / 快速层不会自动
    进入任何包，于是"理论增量存在"和"下一轮 AI 读得到"之间没有连接。让生成器读
    一份显式清单，比让生成器去猜哪些新文件重要要诚实——清单里写了什么，包里就有
    什么，谁加的、什么 claim level，都能在清单里查到。
    """
    raw = json.loads(read_text(ACTIVE_THEORY_MANIFEST))
    nodes = raw.get("nodes")
    if not isinstance(nodes, list) or not nodes:
        fail(f"{ACTIVE_THEORY_MANIFEST} 中没有可用的 `nodes` 列表")
    return nodes


def active_theory_compacts() -> list[str]:
    """清单中标了 `bundle: true` 且尚未被任何领域包收录的快速层文件。

    去重是必须的：某个节点的 compact 可能本来就是领域 CompactCore（例如意识节点
    指向 `Neuroscience/..._CompactCore.md`），那种情况下不能再装一遍。
    """
    already = {f for cfg in DOMAINS.values() for f in cfg["cores"]}
    extra: list[str] = []
    for node in load_active_theory_nodes():
        compact = node.get("compact_layer")
        if not node.get("bundle") or not compact or compact in already or compact in extra:
            continue
        if not (REPO_ROOT / compact).is_file():
            fail(f"{ACTIVE_THEORY_MANIFEST} 的 `{node.get('node_id')}` 指向不存在的快速层：{compact}")
        extra.append(compact)
    return extra


def all_inputs() -> list[str]:
    """生成结果依赖的**全部**输入：生成脚本 + 护栏来源 + 各包正文。"""
    files = [GENERATOR_SELF, *GUARDRAIL_SOURCES, *SPINE, *active_theory_compacts()]
    for cfg in DOMAINS.values():
        files += [*cfg["guards"], *cfg["nav"], *cfg["cores"]]
    return sorted(set(files))


def inputs_digest() -> str:
    """输入闭包的联合内容摘要。

    这才是"包是否与来源一致"的判据。此前用的是 commit 祖先关系，有两个毛病：
    squash / rebase 合并会重写或丢弃该 commit，导致合并后 main 上 `--check` 必红；
    而且祖先关系只覆盖显式正文列表，改 STATUS.md、审计文件或生成脚本都绕得过去。
    内容摘要与合并策略无关，且覆盖全部输入。
    """
    h = hashlib.sha256()
    for rel in all_inputs():
        path = REPO_ROOT / rel
        if not path.is_file():
            fail(f"输入闭包中的文件不存在：{rel}")
        h.update(rel.encode("utf-8") + b"\0")
        h.update(hashlib.sha256(path.read_bytes()).hexdigest().encode() + b"\n")
    return h.hexdigest()[:16]


def capture_provenance(generated_date: str | None) -> Provenance:
    """`source_commit` 只能是**实际的 HEAD**。

    此前有个 `--source-ref` 可以把任意字符串写进 provenance，而内容始终读自工作树——
    等于允许声明一个与内容无关的来源 commit，且 `--check` 也验证不出来。既然内容读自
    工作树，唯一诚实的记法就是记工作树所在的 commit。
    """
    return Provenance(
        sha=git("rev-parse", "--short", "HEAD") or "unknown",
        branch=git("rev-parse", "--abbrev-ref", "HEAD") or "unknown",
        generated=(generated_date or date.today().isoformat()),
        dirty=working_tree_dirty(),
        digest=inputs_digest(),
    )


def verify_provenance(prov: Provenance) -> None:
    """校验包所声明的输入摘要与当前输入闭包一致。

    刻意**不**校验 commit 祖先关系：squash / rebase 合并会重写或丢弃生成时的 commit，
    那样合并到 main 之后本检查必然失败，属于"PR 内绿、合入即红"。内容摘要不受合并
    策略影响，且覆盖生成脚本与护栏来源等隐式输入。
    """
    if not prov.digest:
        fail(
            "包的 frontmatter 缺少 `inputs_digest`——无法验证它与来源一致。\n"
            "  这是旧版格式，请重新运行生成脚本并提交。"
        )
    current = inputs_digest()
    if prov.digest != current:
        fail(
            f"输入闭包摘要不一致：包记录 `{prov.digest}`，当前为 `{current}`。\n"
            "  说明生成脚本、护栏来源（STATUS.md / 审计文件）或某个正文文件在生成之后\n"
            "  发生过改动，包已过期。请重新运行生成脚本并提交。"
        )


def read_provenance(path: Path) -> Provenance:
    """从既有包的 frontmatter 回读 provenance，供 --check 复现同一份输出。"""
    if not path.exists():
        fail(f"--check 需要既有产出，但找不到 {path}")
    fm, _ = split_frontmatter(path.read_text(encoding="utf-8"))
    missing = [k for k in ("generated", "source_commit", "source_branch",
                           "source_dirty", "inputs_digest") if k not in fm]
    if missing:
        fail(f"{path.name} frontmatter 缺少 provenance 字段：{', '.join(missing)}")
    return Provenance(
        sha=fm["source_commit"],
        branch=fm["source_branch"],
        generated=fm["generated"],
        dirty=fm["source_dirty"].strip().lower() == "true",
        digest=fm["inputs_digest"].strip(),
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


def guard_active_theory() -> Guardrail:
    """G5：清单里哪些理论节点**还没有**进入活跃层。

    这条护栏存在的理由，与 G3 是同一类但更根本：G3 说"某笔回写没落地"，G5 说
    "整个节点从未进入 AI 会读到的层"。没有它，装了包的模型会以为包里没有的东西
    就是仓库里没有的东西——而实际情况是内容在仓库深处，只是没有任何入口指过去。
    """
    nodes = load_active_theory_nodes()
    bundled = set(active_theory_compacts())

    def derived(node: dict) -> bool:
        return (
            node.get("assimilation_state") == "active_complete"
            and node.get("behavior_validation") == "passed"
        )

    rows = []
    for node in nodes:
        if derived(node):
            continue
        compact = node.get("compact_layer") or "—"
        gates = "；".join(node.get("author_gates") or []) or "—"
        rows.append(
            f"| `{node.get('node_id')}` | {node.get('assimilation_state', '')} | "
            f"{node.get('behavior_validation', '')} | "
            f"{'`' + compact + '`' if compact != '—' else '—'} | {gates} |"
        )
    if not rows:
        rows.append("| — | 全部节点均已结构激活且行为验证通过 | — | — | — |")

    loaded = "\n".join(f"- `{f}`" for f in sorted(bundled)) or "- （无）"
    assimilated = [n for n in nodes if derived(n)]
    complete_untested = [
        n for n in nodes
        if n.get("assimilation_state") == "active_complete"
        and n.get("behavior_validation") == "untested"
    ]

    return Guardrail(
        gid="G5",
        title="多数理论节点未进入活跃层；进入的也未经行为验证",
        severity="中",
        affected="下表所列节点；这些节点的理论增量在本包中**不存在**，也不在任何默认读取路径上",
        extracts=[
            (
                f"来自 `{ACTIVE_THEORY_MANIFEST}`（逐条抽取 `assimilation_status` 非 "
                f"`effectively_assimilated` 的节点）",
                "| node_id | Axis A 结构 | Axis B 行为 | 快速层 | 作者门 |\n"
                "|---|---|---|---|---|\n" + "\n".join(rows),
            )
        ],
        interpretation=(
            f"清单共 {len(nodes)} 个节点。状态分**两个轴**，不可合并读：\n\n"
            f"- **Axis A（结构）**：{len(complete_untested) + len(assimilated)} 个达到 "
            f"`active_complete`——理论增量已进入 owner、有检索路径、默认路径读得到。\n"
            f"- **Axis B（行为）**：**{len(assimilated)} 个**有已记录的通过运行。"
            f"其余 {len(complete_untested)} 个结构完整的节点是 `untested`：**没有任何证据表明"
            "它们真的改变了判断**。\n\n"
            "`effectively_assimilated` 是这两轴的推导结果，不是可以手写的标签。"
            "回归测试文件存在**不等于**回归测试通过。\n\n"
            "其余节点的内容可能已有 SourceCard、patch、hook 或 bridge——那只证明它被"
            "**保存**和**安排**了，不证明它进入了任何 AI 默认会读的文件。\n\n"
            "本包按清单额外装载了以下快速层（除各领域 CompactCore 之外）：\n\n"
            f"{loaded}\n\n"
            "轴的含义见清单 `axes` 与 "
            "`Operations/Audits/SRT_ACTIVE_THEORY_ASSIMILATION_AUDIT_2026-08-06.md`。"
        ),
        policy=(
            "- 回答涉及上表任一节点时，**不要**因为本包没有相关内容就断言仓库没有；"
            "先按清单的 `active_owners` 去取。\n"
            "- `author_gate` 状态的节点带有明确禁运（如 `d/q/o`），不得绕过。\n"
            "- 额外装载的快速层均为 **P2-P3**，不得用于裁定任何 canonical 定义。\n"
            "- 不要把「有 patch / 有 hook / 文件能被搜到」当作该节点已进入理论。\n"
            "- 更不要把「Axis A = active_complete」当作该节点已被验证会改变判断。"
        ),
        policy_source=f"`{ACTIVE_THEORY_MANIFEST}` 的 `status_rule` 与 `Governance/SRT_CLAIM_LADDER.md`",
    )


def build_guardrails() -> str:
    return "\n\n".join(
        render_guardrail(g)
        for g in (guard_p1_t07(), guard_dqo(), guard_hooks(), guard_active_theory(), guard_shorthands())
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
    "_SRT_SYMBOL_TABLE.md": ("定义源", "AI_START §2 First Sources；符号与记号的定义权"),
    "Core/SRT_OPEN_TENSIONS.md": ("治理护栏", "registry §A.4c；未闭合登记，claim_mode: open"),
    "_SRT_CROSS_DOMAIN_MATRIX.md": ("治理护栏", "registry §A.4d 自称 governance-canonical usage layer"),
    "Governance/SRT_CLAIM_LADDER.md": ("治理护栏", "registry §B.5b；P0–P5 硬度阶梯"),
    "Governance/SRT_CLAIM_MODE_AUDIT.md": ("治理护栏", "registry §B.5c；降级台账"),
    "CANONICAL_REGISTRY.md": ("导航", "权威层级注册表本身"),
    "SRT_AI_START.md": ("导航", "AI 最小首读入口，frontmatter 自标 ai_do_not_use_for_definition"),
}


def registry_mentions() -> tuple[set[str], set[str]]:
    """registry 提及的全部 .md 路径，拆成 (文件存在, 文件不存在)。

    **不能把不存在的路径静默丢掉。** 早先的写法用 `is_file()` 过滤，结果是 registry 指向
    已删除 / 拼错 / 尚未创建的条目会从差异报告里彻底消失——而报告的存在理由恰恰是
    "把差异讲清楚"。失效路径本身就是一种差异，必须单列出来。
    """
    text = read_text("CANONICAL_REGISTRY.md")
    found = set(re.findall(r"`([A-Za-z0-9_][A-Za-z0-9_/.-]*\.md)`", text))
    if not found:
        fail("锚点缺失：CANONICAL_REGISTRY.md 中解析不到任何 .md 路径")
    exists = {p for p in found if (REPO_ROOT / p).is_file()}
    return exists, found - exists


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


BUNDLE_KIND_BLURB = {
    "spine": "**人工选择的高优先级 canonical 骨架**，不是定义权的完备闭包",
    "compactcore": "**轻量跨域包**（各领域 CompactCore 主线），**不含定义源**",
    "domain": "**单领域支持包**（claim-status 护栏 + 导航 + CompactCore），**不含定义源**",
}


def build_manifest_report(bundled: list[str], kind: str = "spine") -> str:
    mentioned, broken = registry_mentions()
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
        f"> 本包是 {BUNDLE_KIND_BLURB[kind]}。",
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

    # First Sources 拆成三态：已收录 / 存在但未收 / 路径失效。
    fs_missing = [p for p in first_sources
                  if p not in bundled and (REPO_ROOT / p).is_file()]
    fs_broken = [p for p in first_sources if not (REPO_ROOT / p).is_file()]
    missing_reg = sorted(p for p in mentioned if p not in bundled)

    parts += ["### 未收录支持文件", ""]
    if fs_broken:
        parts += [
            f"**⚠ 高严重度：`SRT_AI_START.md` §2 First Sources 中有 {len(fs_broken)} 条路径"
            "指向不存在的文件**——这类条目既收不进来，也不该被算作「已覆盖」：",
            "",
            *[f"- `{p}`" for p in fs_broken],
            "",
        ]
    if fs_missing:
        parts += [
            f"**First Sources 点名、文件存在、但本包未收（{len(fs_missing)} 个）**"
            "——回答涉及它们时本包不足以裁定：",
            "",
            *[f"- `{p}`" for p in fs_missing],
            "",
        ]
    if not fs_broken and not fs_missing:
        parts += [
            f"`SRT_AI_START.md` §2 First Sources **已全部收录**（{len(first_sources)} 条，"
            "且全部指向存在的文件）。",
            "",
        ]

    if broken:
        parts += [
            f"**⚠ 高严重度：registry 提及但文件不存在（{len(broken)} 个）**——"
            "指向已删除、拼错或尚未创建的路径。**这类条目不会被静默过滤掉**，"
            "因为它本身就是一种 manifest 差异：",
            "",
            "| 失效路径 | 说明 |",
            "|---|---|",
            *[
                f"| `{p}` | "
                + (f"见 §0.2 G4：这是 `{PATH_SHORTHANDS[p]}` 的行文简写，非真实路径"
                   if p in PATH_SHORTHANDS else "registry 指向的文件在仓库中不存在")
                + " |"
                for p in sorted(broken)
            ],
            "",
        ]

    parts += [
        f"**registry 提及、文件存在、但本包未收（{len(missing_reg)} 个）**——多为领域主轴、",
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
                  purpose: str, files: list[str], kind: str = "spine") -> str:
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
inputs_digest: {prov.digest}
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

> **provenance 契约**：真实性判据是 `inputs_digest`——生成脚本、护栏来源
> （`STATUS.md`、两份审计）与全部正文文件的联合内容摘要。`--check` 重算并比对该摘要，
> 因此改动其中任何一项都会被发现。
>
> `source_commit` 仅供参考，**不作为校验条件**：squash / rebase 合并会重写或丢弃该
> commit，若拿它做祖先校验，合并进 main 之后检查必然失败。内容摘要与合并策略无关。

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

{build_manifest_report(files, kind)}

---
"""


SPINE_POINTER = """
> **注意**：本包**不含** canonical 骨架（`d` / `Ψ_f` / `T_dir` 定义、核心公理、
> 主方程、符号表），因此**仅凭本包不得裁定任何 SRT 术语的定义**。
>
> 需要裁定定义时，请**改用骨架路线**——新开一次对话，只装
> `SRT_CONTEXT_BUNDLE_SPINE.md`。**不要在本包之上再叠加骨架包**：两者合计会超出
> 上下文预算（见 `README.md` 的预算表）。两条路线互斥，是切换关系，不是叠加关系。
"""


def generate(prov: Provenance, out_dir: Path) -> list[tuple[str, str, int]]:
    """生成全部包，返回 [(label, filename, n_files)]。"""
    require_full_history()
    out_dir.mkdir(parents=True, exist_ok=True)
    plan: list[tuple[str, str, str, str, list[str], str, str]] = [
        (
            "骨架 spine", SPINE_BUNDLE_NAME, f"SRT-CONTEXT-BUNDLE-SPINE-{prov.generated}",
            "SRT Canonical 骨架上下文包",
            SPINE,
            "",
            "spine",
        ),
        (
            "CompactCore 全集", "SRT_CONTEXT_BUNDLE_COMPACTCORE.md",
            f"SRT-CONTEXT-BUNDLE-COMPACTCORE-{prov.generated}",
            "SRT CompactCore 全集上下文包",
            [*(f for cfg in DOMAINS.values() for f in cfg["cores"]), *active_theory_compacts()],
            SPINE_POINTER,
            "compactcore",
        ),
    ]
    purposes = {
        SPINE_BUNDLE_NAME: "收录承载定义权的 canonical 主干，供大模型确定 SRT 术语、公理、方程与符号的含义。",
        "SRT_CONTEXT_BUNDLE_COMPACTCORE.md": (
            f"收录全部 {sum(len(cfg['cores']) for cfg in DOMAINS.values())} 个领域 CompactCore"
            f"（AI / 物理 / 哲学 / 神经 / 灵性 / 核心动力学），"
            f"外加 `{ACTIVE_THEORY_MANIFEST}` 标记为需装载的 "
            f"{len(active_theory_compacts())} 个跨域快速层。"
        ),
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
                "domain",
            )
        )
        purposes[name] = f"收录{cfg['title']}的 claim-status 护栏、领域导航与 CompactCore 主线。"

    results = []
    for label, name, bid, title, files, note, kind in plan:
        parts = [bundle_header(prov, bid, title, purposes[name], files, kind)]
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
    # 逐个领域列出，而不是拿最大的一个代表"任一领域包"。
    spine_plus_rows = "\n".join(
        ["| 组合 | 合计 ≈token | 是否在预算内 |", "|---|---:|:---:|"]
        + [
            f"| `SPINE` + `DOMAIN_{k.upper()}` | {total(['SPINE', f'DOMAIN_{k.upper()}']):,} | "
            + ("在预算内（但仍不推荐，见下）"
               if total(["SPINE", f"DOMAIN_{k.upper()}"]) <= MAX_RECOMMENDED_LOAD
               else "**超预算**")
            + " |"
            for k in DOMAINS
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
inputs_digest: {prov.digest}
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

> **这里的 token 数是字符启发式估算，不是任何目标模型的真实 tokenizer 计数。**
> 系数刻意取在偏高一侧（CJK 按 1.2 tok/字，实际约 1.0–1.1；拉丁按 0.29，实际约 0.25），
> 所以估算值倾向于**高估**——对预算而言这是安全方向。但偏保守不等于精确，因此预留量
> 里额外含一段误差缓冲，且本节不把校验结果称作"保证"。

窗口按 **{CONTEXT_WINDOW:,} token** 计，预留 **{HEADROOM_RESERVE:,}** 给系统提示、
用户问题、模型输出**与估算误差**，因此单次装载上限 **{MAX_RECOMMENDED_LOAD:,} token**。

下表由生成脚本计算并校验：**超出上限的组合不能作为推荐出现**——`check_budgets()`
会让构建直接失败。

### 推荐装载路线

{loadout_rows}

### 禁止的组合

{forbidden_rows}

### `SPINE` + 各领域包（逐个列出，均不推荐）

{spine_plus_rows}

**两条路线互斥。** 骨架路线用于裁定定义；轻量路线用于领域问答。

上表中部分组合虽在预算内，仍不推荐叠加：领域包已自带 claim-status 护栏与导航，
叠加骨架会把大量与该领域无关的定义正文压进上下文，稀释注意力，收益远低于成本。
需要裁定定义时，**换一次对话只装 `SPINE`**。

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

`--check` 先核对 `inputs_digest`（输入闭包的联合内容摘要，覆盖生成脚本、护栏来源与
全部正文），再按既有产出 frontmatter 记录的 provenance 重新生成到临时目录逐字比对。
唯一的固定参数是 `--generated-date`，且它只是日期标签，不声称内容来源。

护栏层按锚点抽取自 `Operations/` 审计台账与 `STATUS.md`。**任一锚点失效，脚本会
直接以非零码退出**，而不会产出一个缺护栏的包。P1-T07 若日后被修订，脚本同样会
失败，强制复核该护栏是否仍适用——这是刻意的防漂移设计。

真实性判据是 `inputs_digest`（输入闭包的联合内容摘要），不是 `source_commit`。
后者仅供参考——squash / rebase 合并会重写它，拿它做祖先校验会让合并后的 main 必红。
""",
        encoding="utf-8",
    )


# --------------------------------------------------------------------------
# 入口
# --------------------------------------------------------------------------

def run_check(out_dir: Path) -> None:
    prov = read_provenance(out_dir / SPINE_BUNDLE_NAME)
    verify_provenance(prov)
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
    # 刻意不提供 `--source-ref`：内容读自工作树，能诚实记录的只有工作树所在的 commit。
    ap.add_argument("--generated-date",
                    help="固定记录的生成日期 YYYY-MM-DD（默认今天）；仅为标签，不声称内容来源")
    ap.add_argument("--out-dir", default=str(DEFAULT_OUT_DIR), help="产出目录")
    args = ap.parse_args()

    out_dir = Path(args.out_dir)
    if args.check:
        run_check(out_dir)
        return

    # provenance 在任何写入之前一次性捕获，保证同一次生成的所有包记录一致。
    prov = capture_provenance(args.generated_date)
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
