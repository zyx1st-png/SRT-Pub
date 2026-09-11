from pathlib import Path
import re


def replace_between(path: str, start: str, end: str, replacement: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    i = text.find(start)
    if i < 0:
        raise SystemExit(f"start marker not found in {path}: {start}")
    j = text.find(end, i + len(start))
    if j < 0:
        raise SystemExit(f"end marker not found in {path}: {end}")
    p.write_text(text[:i] + replacement.rstrip() + "\n\n" + text[j:], encoding="utf-8")


def replace_once(path: str, old: str, new: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    if text.count(old) != 1:
        raise SystemExit(f"expected exactly one match in {path}: {old[:80]!r}; got {text.count(old)}")
    p.write_text(text.replace(old, new, 1), encoding="utf-8")


def replace_line_regex(path: str, pattern: str, replacement: str) -> None:
    p = Path(path)
    text = p.read_text(encoding="utf-8")
    out, n = re.subn(pattern, replacement, text, count=1, flags=re.MULTILINE)
    if n != 1:
        raise SystemExit(f"expected one regex line match in {path}: {pattern}; got {n}")
    p.write_text(out, encoding="utf-8")


# CANONICAL_REGISTRY: replace 13a and simplify 13d so registry no longer routes subjecthood through sigma.
replace_between(
    "CANONICAL_REGISTRY.md",
    "### 13a. SRT 个体化理论",
    "### 13b. SRT 遮蔽动力学",
    """### 13a. SRT 个体化模型（自指动力学 + subject/self-model 开放接口）
- 主文件：`Core_Law/SRT_Individuation.md`
- id：`SRT-INDIVIDUATION`
- layer：L1 / epistemic：os / status：draft_v0 / claim-mode：hybrid
- 说明：位于 `SRT-ONE-FORMATION` 已形成 `One / Selection-position` 之后的模型 / 假说层。`σ_{sr}` 只作为已声明 representation / attribution rule 下的 model-local 历史—自指平衡 proxy；它不定义 One、Stable ISP、Bearer 或 subject-position。
- B1 supersession：former T-IND-2 `σ_{sr}^{sub}` iff subject-entry gate 已退役；`σ_{sr}^{sub}` 只保留为第一模型区 crossing / balance coordinate 的 legacy compatibility symbol（P3/P4），不得再称 canonical 主体位 / Stable-ISP threshold。
- T-IND-1：P2 phase-like self-reference dynamics hypothesis，不是 subject theorem。
- T-IND-3：P2 conditional second-order self-model / writeback hypothesis；`σ_{sr}^{self}` 只作为模型内二阶写回激活坐标候选，不证明 consciousness / phenomenality。
- 当前正向 subject gate：OPEN。当前 Bearer 重构 checkpoint 为作者裁决的 `P prospective self-indexing + E same-One prospective exposure`；Bearer 到承担 / 关切 / subject / experiencer 仍分别 OPEN。
- 与 P1-T06 的关系：P1-T06 owns Stable-ISP standing；Individuation 不把任何 `σ_{sr}` 阈值等同于 Stable-ISP entry。
- 引用规则：涉及 `σ_{sr}` 模型、自指动力学、二阶 self-model 候选时回链本文件；涉及 One 回链 `SRT-ONE-FORMATION`，Stable ISP 回链 P1-T06，Bearer 当前重构回链 #944 author adjudication，subject sufficiency 不得引用旧 T-IND-2 作为已成立结论。""",
)

replace_between(
    "CANONICAL_REGISTRY.md",
    "### 13d. SRT L1 Formalism",
    "### 13e. SRT 集体选择理论",
    """### 13d. SRT L1 Formalism（`σ_{sr}` / d_c / T_dir / S 四变量模型动力学）
- 主文件：`Core_Law/SRT_L1_Formalism.md`
- id：`SRT-L1-FORMALISM`
- layer：L1 / epistemic：os / status：draft_v0
- 说明：四变量的最小耦合 formalism / projection hub；方程结构与 family-invariance 命题保持其各自 P1-candidate / P2 / P3 标注，但**数学稳态或 threshold coordinate 不自动获得本体 subject 语义**。
- `σ_{sr}`：model-local self-reference/history balance proxy。§2 的 `σ_{sr}^{sub}` 现在只解释为第一模型区 balance/crossing coordinate；former subject-entry semantics 已由 B1 退役。
- `σ_{sr}^{self}` / T-CHI-1：可以研究二阶 self-model/writeback kernel 的模型稳定性；kernel-family 形式稳健性不推出 subjecthood、consciousness 或 phenomenality。
- d_c / T_dir / S：继续由各自 owner 提供概念定义；本文件只写耦合 / 投影动力学，不得反向用 `σ_{sr}^{sub}` 或任一联立变量构成 subject gate。
- 与主方程的关系：T-PROJ-1 等仍按其显式 closure assumptions 读取；“projection theorem”只说明给定 projection 定义下的形式关系，不提升下游本体语义。
- 引用规则：方程级陈述回链本文件；One / Stable ISP / Bearer / subject / d / T_dir / suffering 的概念定义分别回各自 owner / 当前 adjudication。""",
)

# Claim-mode ledger: replace Individuation claim map and add a clean B1 supersession rule.
replace_between(
    "Governance/SRT_CLAIM_MODE_AUDIT.md",
    "#### SRT-INDIVIDUATION",
    "#### SRT-OCCLUSION-DYNAMICS",
    """#### SRT-INDIVIDUATION

| Label | Statement | Level / status |
|---|---|---|
| Def-`σ_{sr}` | 历史 / 自指平衡 proxy `‖θ^{trace}‖ / (‖θ^{trace}‖ + ‖θ^{ext}‖)` | P2 model-local operational proxy; representation / attribution dependent |
| T-IND-1 | phase-like self-reference dynamics may occur | P2 modelling hypothesis; **not** a subject theorem |
| former T-IND-2 | `σ_{sr}^{sub}` + historical/bearing/concern/direction bundle iff subject entry | **RETIRED as current sufficiency / P1-candidate claim** |
| `σ_{sr}^{sub}` | first model-regime balance / crossing coordinate (legacy symbol) | P3/P4 candidate; **not** subject / Stable-ISP / Bearer threshold |
| T-IND-3 | second-order self-model / self-description writeback condensate | P2 conditional structural hypothesis |
| `σ_{sr}^{self}` | second-order writeback activation coordinate | P3/P4 model-local candidate; **not** consciousness threshold |
| positive subject-position sufficiency | — | **OPEN** |
| phenomenality / experiencer transition | — | **OPEN** |

**B1 downstream rule (2026-09-11)**：不得再引用 T-IND-1/2 或 `σ_{sr}^{sub}` 作为 P1-candidate subject-entry theorem。`σ_{sr}` 只在声明 unit / scale / lineage / attribution / representation / metric / time-window 后作为 model-local proxy。T-IND-3 与 `σ_{sr}^{self}` 只允许描述二阶 self-model/writeback 候选；不得据此推出 consciousness / phenomenality。One 回链 `SRT-ONE-FORMATION`；Stable ISP 回链 P1-T06；Bearer 当前路线按 `P+E` author adjudication；Bearer -> bearing / concern / subject 继续 OPEN。""",
)

# L1 Formalism: retype the two threshold coordinates and sever ontology inference.
replace_between(
    "Core_Law/SRT_L1_Formalism.md",
    "### §2.3 相变结构",
    "### §2.5 T-CHI-1",
    """### §2.3 模型稳态 / regime coordinates（B1 语义清洗）

把 `dσ/dt = 0` 作为**模型稳态条件**，可以定义若干 coordinate；这些 coordinate 属于所声明 `σ_{sr}` 模型，不自动是本体相变。

1. **`σ_{sr}^{sub}`（legacy first-regime coordinate）**：保留旧符号以兼容历史方程；它表示 writeback 项与外部输入/衰减项达到所声明平衡关系的模型坐标：

   $$
   \sigma_{sr}^{sub} : \alpha w\phi(\sigma_{sr}^{sub}) = \beta i + \lambda_{trace}T\sigma_{sr}^{sub}.
   $$

   **B1 guard**：该坐标不再称 canonical “主体位涌现门槛”，也不等于 Stable-ISP entry、Bearer onset、承担 / 关切 onset 或 phenomenality threshold。

2. **`σ_{sr}^{self}`（second-order writeback activation coordinate）**：作为 `χ` kernel 的模型参数，可用于研究二阶 self-model/writeback 增益何时被激活。它不自动等于 self-consciousness / consciousness 的自然阈值。

3. **`σ_{sr} -> 1` high-self-reference regime**：可以作为外部接入减弱 / self-closure 过强的模型候选区。是否构成病理、遮蔽、subject breakdown 或 suffering，必须分别由相应 owner / domain 证据支付。

### §2.4 与 Individuation 的新对齐

- T-IND-1 现在是 P2 phase-like modelling hypothesis；§2 ODE 可作为它的一个实现模型。
- former T-IND-2 iff subject gate 已退役；`σ_{sr}^{sub}` 只保留模型 coordinate 意义。
- T-IND-3 是 P2 conditional second-order self-model/writeback hypothesis；`χ` 激活只承载该模型的二阶 writeback 结构。
- 所有 fixed point / bifurcation / family-invariance 结果首先是**方程族性质**，不是 One / Stable ISP / Bearer / subject / consciousness 的定义或充分条件。
""",
)

formalism = Path("Core_Law/SRT_L1_Formalism.md")
ft = formalism.read_text(encoding="utf-8")
needle = "### §2.5 T-CHI-1：χ 跳跃函数族的普适性（H8，2026-04-25）\n"
if needle not in ft:
    raise SystemExit("T-CHI marker missing")
ft = ft.replace(
    needle,
    needle + "\n> **B1 ontology guard (2026-09-11)**：本节若证明某个 `χ` family 下的 fixed-point / direction / topology invariance，结论只属于所声明的二阶 writeback **模型族**。历史正文中的 `T-IND-3 / self-consciousness transition` 字样按 legacy model label 读取；它们不把数学 family-invariance 转换成 subjecthood、consciousness 或 phenomenality theorem。\n",
    1,
)
formalism.write_text(ft, encoding="utf-8")

# Claim ledger: formalism rows get an explicit ontology guard without deleting mathematical candidates.
replace_once(
    "Governance/SRT_CLAIM_MODE_AUDIT.md",
    '| §2 σ 最小动力学（logistic + χ 跳跃） | — | P1-candidate 结构形式；具体函数族普适性由 §2.5 T-CHI-1 升 P1-candidate（H8） |',
    '| §2 `σ_{sr}` 最小动力学（logistic + χ 跳跃） | — | P1-candidate **model/equation structure only**；`σ_{sr}^{sub}` subject-entry semantics 已退役，不能由方程稳态推出 subject / Bearer |',
)
replace_once(
    "Governance/SRT_CLAIM_MODE_AUDIT.md",
    '| §2.5 T-CHI-1 χ 跳跃函数族普适性（H8，2026-04-25） | "有效二阶相变核"四条结构属性 + 族内四个不变量（双稳态 / 病理吸引子 / 致命 `L_2` / 相变方向） | P1-candidate（χ 形式无关性升为定理后果） |',
    '| §2.5 T-CHI-1 χ 跳跃函数族普适性（H8，2026-04-25） | 有效 kernel family 下的 fixed-point / topology / direction invariance | P1-candidate mathematical/model-family result；**不提升 T-IND-3 为 subject/consciousness theorem** |',
)

# Hardening note symbol names are governance namespace, not ontology thresholds.
replace_line_regex(
    "Core_Law/SRT_L1_Hardening_Notes.md",
    r"^\| σ_sub（主体位进入门槛） \|.*$",
    "| σ_sub（legacy 第一模型区坐标） | **`σ_{sr}^{sub}`** | first model-regime balance/crossing coordinate; **retired as canonical subject / Stable-ISP threshold** | `SRT_Individuation.md`, `SRT_L1_Formalism.md §2` |",
)
replace_line_regex(
    "Core_Law/SRT_L1_Hardening_Notes.md",
    r"^\| σ_self（自我意识凝结门槛） \|.*$",
    "| σ_self（二阶 writeback 激活坐标） | **`σ_{sr}^{self}`** | model-local second-order self-model/writeback activation coordinate; not a consciousness threshold | `SRT_Individuation.md`, `SRT_L1_Formalism.md §2` |",
)

# Symbol table: same semantic truth-up.
replace_line_regex(
    "_SRT_SYMBOL_TABLE.md",
    r"^\| \*\*σ_\{sr\}\^\{sub\}\*\* \|.*$",
    "| **σ_{sr}^{sub}** | `\\sigma_{sr}^{sub}` | Legacy First-Regime Coordinate | Model-local balance / regime-crossing coordinate in the `σ_{sr}` self-reference model. **B1 supersession:** retired as a canonical subject-position, Stable-ISP, Bearer, or consciousness threshold. | Model-local threshold coordinate | L1; P3/P4 candidate; legacy symbol retained for compatibility; source `SRT_Individuation.md` / `SRT_L1_Formalism.md §2`. |",
)
replace_line_regex(
    "_SRT_SYMBOL_TABLE.md",
    r"^\| \*\*σ_\{sr\}\^\{self\}\*\* \|.*$",
    "| **σ_{sr}^{self}** | `\\sigma_{sr}^{self}` | Second-Order Writeback Coordinate | Model-local activation coordinate for a second-order self-model / writeback kernel. It is **not** an established self-consciousness / consciousness / phenomenality threshold. | Model-local threshold coordinate | L1; P3/P4 candidate; source `SRT_Individuation.md` / `SRT_L1_Formalism.md §2`. |",
)

# Open tensions: rewrite the central subject-boundary row.
replace_line_regex(
    "Core/SRT_OPEN_TENSIONS.md",
    r"^\| Stable ISP natural boundary / phenomenal necessity \|.*$",
    "| Bearer / subject natural boundary / phenomenal necessity | One formation is separately owned; P1-T06 remains Stable-ISP standing; #944 fixes current noncanonical Bearer onset as `P+E`; B1 retires `σ_{sr}^{sub}` as subject/Stable-ISP threshold | the additional minimal relation from Bearer to actual bearing / concern / subject-position; whether any natural phase boundary exists; whether a subject/experiencer can be phenomenally empty | neither `σ_{sr}` thresholds, Stable ISP, Bearer, `d>0`, `T_dir`, historical writeback, nor second-order self-model may by itself prove subjecthood or phenomenality |",
)

print("B1 central routing cleanup applied")
