---
id: SRT-CONTEXT-BUNDLE-DOMAIN-CORE-2026-08-11
type: context_bundle
status: active
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
generated: 2026-08-11
source_commit: c511c5ca
source_branch: claude/srt-theory-consistency-tension-dabe30
source_dirty: true
inputs_digest: 44548633c809b90e
---

# SRT 核心动力学上下文包

> **这是什么**：由 `scripts/build_srt_context_bundles.py` 从 SRT 仓库自动拼装的上下文包。
> 收录核心动力学的 claim-status 护栏、领域导航与 CompactCore 主线。
>
> **这不是什么**：不是新的 canonical 文件，不是摘要，不是改写。每个来源文件的正文
> 逐字保留；脚本只把 YAML frontmatter 转成显式 provenance 头。**若本包与仓库中的
> 来源文件冲突，以仓库为准**——本包是快照，会随仓库演进而过期。

## §0 生成信息

| 项 | 值 |
|---|---|
| 生成日期 | 2026-08-11 |
| 来源 commit | `c511c5ca` |
| 来源分支 | `claude/srt-theory-consistency-tension-dabe30` |
| 生成时来源工作树有改动 | 是 |
| 包含文件数 | 1 |

> **provenance 契约**：真实性判据是 `inputs_digest`——生成脚本、护栏来源
> （`STATUS.md`、两份审计）与全部正文文件的联合内容摘要。`--check` 重算并比对该摘要，
> 因此改动其中任何一项都会被发现。
>
> `source_commit` 仅供参考，**不作为校验条件**：squash / rebase 合并会重写或丢弃该
> commit，若拿它做祖先校验，合并进 main 之后检查必然失败。内容摘要与合并策略无关。

### 0.1 文件清单与各自最后改动日期

| # | 文件 | 最后 commit |
|---|---|---|
| 1 | `Core/SRT_Core_14_Dynamics_Scaling_CompactCore.md` | 2026-04-20 |

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

### G1 — P1-T07 证明未闭合（严重度：高）

**受影响**：`Core/SRT_Core_21b_Constitutive_Theorems.md` 的 **P1-T07 Constitutive Asymmetry Theorem**（claim level **P1**）

#### SOURCE EXTRACT — 来源原文（逐字抽取）

**审计自述，来自 `Operations/Audits/SRT_P1_T07_PROOF_HARDENING_AUDIT.md`**：

> **Status**: non-canonical Operations record. **Proof audit only.** It modifies no theorem, no axiom, no definition, no equation. It does not resolve the proof; it maps exactly where the current proof does and does not close, and hands options to a later controlled amendment PR. Prior Claude/ChatGPT statements about P1-T07 were treated as hypotheses; the only source of truth is `origin/main @ 14c0d7f8`. Archive/book files were read for context but are **not** used to establish anything about the canonical theorem.

**审计 1.3 修订的语义分层条款，来自 `Operations/Audits/SRT_P1_T07_PROOF_HARDENING_AUDIT.md`**：

> (a) `τ<∞` verdicts stratified by semantics — on a realized terminating history only **S1 pathwise** stability fails; **S2** fails only if `P(τ<∞)>0`, **S3** only if `P(τ=∞)=0`; no unconditional *process-level* stable-ISP verdict before the S1/S2/S3 choice (fixed in §0 Q5, §8, Proof Gate)

**审计 §0 第 5 问，来自 `Operations/Audits/SRT_P1_T07_PROOF_HARDENING_AUDIT.md`**：

> 5. **What can P1-T07 prove at most?** Two things must be separated, and the first is **semantics-relative**, not process-unconditional. **(i) True and derivable, per level**: on any realized history with `τ<∞`, that history enters the absorbing `∅` and no further selection is possible — so **S1 (pathwise) stability fails on that history**. At the *process* level, **S2** stability fails only when `P(τ<∞)>0`, and **S3** stability fails only when `P(τ=∞)=0`. Before S1/S2/S3 is chosen, **no unconditional process-level stable-ISP verdict may be issued** from `τ<∞`. **(ii) NOT derivable as written**: *neutral `P` terminates a.s., therefore neutral `P` is not stable* — because a.s. termination of a neutral process is exactly what Step 3 fails to establish. "Positive termination probability" is also **not** unconditional (it needs positive hazard at a surviving step). (§4, §8)

#### GENERATED INTERPRETATION — 生成器归纳（**非**来源原文）

该定理 Proof Sketch 第 3 步（*neutral `P` ... cumulative probability tends toward 1*）以肯定句写成，正文未标注任何保留。上述审计判定恰恰是这一步不闭合：语料并未*确立*每步正 hazard，而且即使每步 hazard 为正也不蕴含 almost-sure 终止；`ε-neutral` 在语料中从未被形式定义；P1-T06 的 stable ISP 定义是非概率的，S1/S2/S3 随机语义尚未选定。

另需注意：`Core/SRT_OPEN_TENSIONS.md` 目前**未登记**本缺口。

#### USAGE POLICY — 使用规则

*授权依据：`Governance/SRT_CLAIM_LADDER.md`（P0–P5 阶梯）与 `SRT_AI_START.md` §5 / §8*

- 不得把 P1-T07 当作已证 P1 定理引用。
- 关于 `τ<∞` 只能作**语义分层**的陈述：若某条 realized history 满足 `τ<∞`，可无条件断言的仅是**该历史上的 S1 / pathwise stability 失败**；process-level 的 S2 需 `P(τ<∞)>0`，S3 需 `P(τ=∞)=0`。**在 S1/S2/S3 语义未选定之前，不得据此推出无条件的 process-level 「not a stable ISP」。**
- 不要假装 `ε-neutral` 有形式定义。
- 「查过 `OPEN_TENSIONS` 没找到」**不**足以证明本命题已封口——该缺口尚未登记在那里。


### G2 — `d`/`q`/`o` 三轴处于禁运状态（严重度：中）

**受影响**：`_SRT_D_VALUE_CANONICAL.md` 的 `d` 定义，以及任何涉及 `q` / `o` 的表述

#### SOURCE EXTRACT — 来源原文（逐字抽取）

**来自 `STATUS.md`（2026-07-25 条目）**：

> 已加下游护栏：符号重命名与 `q` / `o` 的形式选择做出前，`d/q/o` 不得进入书稿、公共内容、bridge 或论文。

#### GENERATED INTERPRETATION — 生成器归纳（**非**来源原文）

2026-07-23 至 07-25 的三份对话材料提出具身位重写与 `d`/`q`/`o` 三轴，台账记录为**全部路由为候选，无一落地**。已知触雷点包括：`d` 取参与率与 `Def-d-canonical` 的范数定义冲突；`q` 的五个成分中两项落在 `Def-w_i` 的 `C_i` 定义文字内。

本包所含 canonical 正文**不含** `d/q/o` 内容——这是正确状态，不是遗漏。

#### USAGE POLICY — 使用规则

*授权依据：`STATUS.md` 2026-07-25 条目所记的下游护栏裁决*

- 不要从外部对话材料把三轴引入回答。
- 不要据此改写 `d` 的定义。
- 禁运范围按上述原句：书稿、公共内容、bridge、论文。


### G3 — 存在已裁决但未落地的回写（严重度：中）

**受影响**：下表所列各阻塞目标对应的主文；相关正文在本包中是不完整的

#### SOURCE EXTRACT — 来源原文（逐字抽取）

**来自 `Operations/Audits/Hook_Closure_Audit_2026-07-25.md` 的 partial / pending 行（逐字）**：

> | Hook | 声明状态 | 实际 | 判定 |
> |---|---|---|---|
> | `PH_AG02_Reasoning_Bias` | active_v0_1 | agency 主文已落地；`T_dir` canonical **未落地** | partial |
> | `PH_AG03_Constitutive_Commitment` | active_v0_1 | agency 主文已落地；`T_dir` canonical **未落地** | partial |
> | `PH_SEM01_Bilateral_Incompatibility` | active_v0_1 | agency 主文已落地；`Occlusion_Dynamics` **未落地** | partial |
> | `P03_Cosmological_Principle` | pending | target 文档**从未创建** | pending（planned target） |
> | `P04_Spontaneous_Collapse_Classicality` | pending | target 文档**从未创建** | pending（planned target） |
> | `P05_Quantum_Proper_Time_Optical_Clocks` | pending | target 文档**从未创建** | pending（planned target） |

#### GENERATED INTERPRETATION — 生成器归纳（**非**来源原文）

按**阻塞目标**分组如下（分组由脚本从上表解析得出，非手写摘要）：

| 阻塞目标 | hook 数 | hooks |
|---|---:|---|
| `T_dir` 回写未落地 | 2 | `PH_AG02_Reasoning_Bias`, `PH_AG03_Constitutive_Commitment` |
| `Occlusion_Dynamics` 回写未落地 | 1 | `PH_SEM01_Bilateral_Incompatibility` |
| planned target 从未创建 | 3 | `P03_Cosmological_Principle`, `P04_Spontaneous_Collapse_Classicality`, `P05_Quantum_Proper_Time_Optical_Clocks` |

三张 pending 的 target 文档 `Physics/SRT_Physics_Bridge_v0_2.md` 从未创建。改 canonical 主定义属 `Governance/SRT_EDIT_PROTOCOL.md` C 类高风险编辑，须作者授权，ledger 记 `blocked_by: canonical freeze`。

#### USAGE POLICY — 使用规则

*授权依据：`Governance/SRT_EDIT_PROTOCOL.md`（C 类编辑）与 `Operations/_SRT_MATERIAL_PIPELINE.md` §5.6.1（ledger 契约）*

- 回答涉及上表任一阻塞目标时，注意本包中对应正文**尚未吸收**该笔回写。
- 各阻塞目标彼此独立：不要把某一目标的缺口范围套用到另一个上。
- 不要把 planned-but-never-created 的 target 当作已存在的文件引用。


### G5 — 多数理论节点未进入活跃层；进入的也未经行为验证（严重度：中）

**受影响**：下表所列节点；这些节点的理论增量在本包中**不存在**，也不在任何默认读取路径上

#### SOURCE EXTRACT — 来源原文（逐字抽取）

**来自 `Operations/Audits/data/srt_active_theory_nodes.json`（逐条抽取 `assimilation_status` 非 `effectively_assimilated` 的节点）**：

> | node_id | Axis A 结构 | Axis B 行为 | 快速层 | 作者门 |
> |---|---|---|---|---|
> | `NODE-CHOICE-GENERATION` |  |  | `03_Bridges/SRT_Selection_Event_CompactCore.md` | — |
> | `NODE-SELECTION-ONTOLOGY` |  |  | — | — |
> | `NODE-L0-L1-L2` |  |  | — | — |
> | `NODE-D-VALUE` |  |  | — | RQ-2026-08-A02: whether q is an independent axis or a post-stake-gate depth profile; whether o is operationalized and gets a symbol |
> | `NODE-PSI-F` |  |  | — | — |
> | `NODE-T-DIR` |  |  | — | Two PH_AG partial hooks are blocked on a T_dir canonical writeback; that edit is C-class and needs separate authorization |
> | `NODE-GHOST-OPERATOR` |  |  | — | — |
> | `NODE-SUBJECTHOOD` |  |  | — | — |
> | `NODE-CONSCIOUSNESS` |  |  | `Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md` | — |
> | `NODE-AI-REASONING` |  |  | `AI/SRT_AI_Architecture_CompactCore.md` | — |
> | `NODE-NEURAL-DECODABILITY` |  |  | `Neuroscience/SRT_Neural_Mechanisms_CompactCore.md` | Whether Neuroscience/SRT_Neuroscience_Hardening_N1_N12_v0_2.md is created at all, or NEURAL18/21/22 retarget the compact core |
> | `NODE-LIFE-DISSIPATIVE` |  |  | `03_Bridges/SRT_Selection_Event_CompactCore.md` | — |
> | `NODE-PHYSICS-MEASUREMENT` |  |  | — | RQ-2026-08-A04: P03/P04/P05 land in a new SRT_Physics_Bridge_v0_2.md or merge into the existing _SRT_Phys_Bridge.md |
> | `NODE-SOCIAL-L2` |  |  | `Philosophy/SRT_Political_Philosophy_CompactCore.md` | — |
> | `NODE-ENTROPY-REORG` |  |  | `03_Bridges/SRT_Selection_Event_CompactCore.md` | — |
> | `NODE-BOOK-BACKFLOW` |  |  | — | — |

#### GENERATED INTERPRETATION — 生成器归纳（**非**来源原文）

清单共 16 个节点。状态分**两个轴**，不可合并读：

- **Axis A（结构）**：0 个达到 `active_complete`——理论增量已进入 owner、有检索路径、默认路径读得到。
- **Axis B（行为）**：**0 个**有已记录的通过运行。其余 0 个结构完整的节点是 `untested`：**没有任何证据表明它们真的改变了判断**。

`effectively_assimilated` 是这两轴的推导结果，不是可以手写的标签。回归测试文件存在**不等于**回归测试通过。

其余节点的内容可能已有 SourceCard、patch、hook 或 bridge——那只证明它被**保存**和**安排**了，不证明它进入了任何 AI 默认会读的文件。

本包按清单额外装载了以下快速层（除各领域 CompactCore 之外）：

- `03_Bridges/SRT_Selection_Event_CompactCore.md`

轴的含义见清单 `axes` 与 `Operations/Audits/SRT_ACTIVE_THEORY_ASSIMILATION_AUDIT_2026-08-06.md`。

#### USAGE POLICY — 使用规则

*授权依据：`Operations/Audits/data/srt_active_theory_nodes.json` 的 `status_rule` 与 `Governance/SRT_CLAIM_LADDER.md`*

- 回答涉及上表任一节点时，**不要**因为本包没有相关内容就断言仓库没有；先按清单的 `active_owners` 去取。
- `author_gate` 状态的节点带有明确禁运（如 `d/q/o`），不得绕过。
- 额外装载的快速层均为 **P2-P3**，不得用于裁定任何 canonical 定义。
- 不要把「有 patch / 有 hook / 文件能被搜到」当作该节点已进入理论。
- 更不要把「Axis A = active_complete」当作该节点已被验证会改变判断。


### G4 — 行文简写路径对照（严重度：低）

**受影响**：骨架正文中若干人读简写

#### SOURCE EXTRACT — 来源原文（逐字抽取）

#### GENERATED INTERPRETATION — 生成器归纳（**非**来源原文）

正文中以下写法是人读简写，按字面当作路径解析会落空。原文未改，对照如下：

| 正文写法 | 实际所指 |
|---|---|
| `Core_21_Formal_Axioms.md` | Core/SRT_Core_21_Formal_Axioms.md |
| `_SRT_SYMBOL_QUICK_GUARD.md` | SRT_AI_START.md §3（已于 2026-07-20 并入，原文件不再存在） |

#### USAGE POLICY — 使用规则

*授权依据：生成器维护的对照表（`PATH_SHORTHANDS`）*

- 遇到上表左列写法时按右列解析，不要报告「文件不存在」。


## §0.3 claim 阶梯与回答纪律

以下两节从 `SRT_AI_START.md` 原样抄入，适用于本包全部内容。

### 5. Claim-Level Guard

Use the claim ladder:

- P0: primitive axiom
- P1: constitutive theorem
- P2: canonical interpretation
- P3: bridge mapping
- P4: lab hypothesis
- P5: companion / phenomenological exposition

Do not promote bridge or lab claims into core claims. In particular:

- fitness beats truth is not P0;
- assembly thresholds are not P0/P1;
- holographic duality is not P0/P1;
- ghost-operator universality is a bridge unless separately hardened;
- AI-domain claims do not define the SRT core.

---

### 8. Minimal Answer Protocol

When answering about SRT:

1. Name the canonical source you rely on.
2. State the claim level if hardness matters.
3. Mark bridge, lab, or companion material explicitly.
4. If a point is listed in `Core/SRT_OPEN_TENSIONS.md`, do not present it as closed.
5. For non-trivial questions, name the retrieval route or task profile used.
6. Prefer short, hard claims over broad unification language unless the question explicitly asks for bridge speculation.

## §0.4 Manifest 差异报告（本包 vs `CANONICAL_REGISTRY.md`）

> **这份报告回答一个问题：本包相对 `CANONICAL_REGISTRY.md` 到底缺了什么。**
>
> 本包是 **单领域支持包**（claim-status 护栏 + 导航 + CompactCore），**不含定义源**。
> 下面的分类是**生成器的判断**，不是 registry 的原话；每行都附依据供复核。
> 「registry 提及」「AI_START §2」两列是机械判定的事实。

### 已收录

**定义源**（1 个）

| 文件 | 分类依据 | registry 提及 | AI_START §2 |
|---|---|:---:|:---:|
| `Core/SRT_Core_14_Dynamics_Scaling_CompactCore.md` | frontmatter claim_mode=canonical | ✓ | — |

### 未收录支持文件

**First Sources 点名、文件存在、但本包未收（15 个）**——回答涉及它们时本包不足以裁定：

- `CANONICAL_REGISTRY.md`
- `Governance/SRT_CLAIM_LADDER.md`
- `Governance/SRT_CLAIM_MODE_AUDIT.md`
- `Core_Law/SRT_L0_Metaphysics.md`
- `Core/SRT_Core_21_Minimal_Axioms.md`
- `Core/SRT_Core_21b_Constitutive_Theorems.md`
- `_SRT_D_VALUE_CANONICAL.md`
- `_SRT_PSI_F_CANONICAL.md`
- `_SRT_T_DIR_CANONICAL.md`
- `_SRT_CROSS_DOMAIN_MATRIX.md`
- `Core/SRT_Core_22_Equations.md`
- `_SRT_SYMBOL_TABLE.md`
- `Core/SRT_Core_21_Formal_Axioms.md`
- `Core/SRT_Core_21c_Bridge_Hypotheses.md`
- `Core/SRT_OPEN_TENSIONS.md`

**⚠ 高严重度：registry 提及但文件不存在（1 个）**——指向已删除、拼错或尚未创建的路径。**这类条目不会被静默过滤掉**，因为它本身就是一种 manifest 差异：

| 失效路径 | 说明 |
|---|---|
| `Core_21_Formal_Axioms.md` | 见 §0.2 G4：这是 `Core/SRT_Core_21_Formal_Axioms.md` 的行文简写，非真实路径 |

**registry 提及、文件存在、但本包未收（93 个）**——多为领域主轴、
展开层与 PH-SS 护栏文件，按需走领域包或直接读仓库，不在骨架路线内：

<details><summary>展开完整清单</summary>

- `AI/AI_POSITIONING_NOTE.md`
- `AI/SRT_AI_01_Ontology.md`
- `AI/SRT_AI_01_Ontology_CompactCore.md`
- `AI/SRT_AI_03_Consciousness_Framework.md`
- `AI/SRT_AI_03_Consciousness_Framework_CompactCore.md`
- `AI/SRT_AI_Architecture.md`
- `AI/SRT_AI_Architecture_CompactCore.md`
- `AI/SRT_AI_Claim_Status.md`
- `CANONICAL_REGISTRY.md`
- `Core/SRT_Core_14_Dynamics_Scaling.md`
- `Core/SRT_Core_21_Formal_Axioms.md`
- `Core/SRT_Core_21_Minimal_Axioms.md`
- `Core/SRT_Core_21b_Constitutive_Theorems.md`
- `Core/SRT_Core_21c_Bridge_Hypotheses.md`
- `Core/SRT_Core_22_Equations.md`
- `Core/SRT_OPEN_TENSIONS.md`
- `Core_Law/SRT_Collective_Selection.md`
- `Core_Law/SRT_Collective_Tower_Hardening_Notes.md`
- `Core_Law/SRT_Constitution_Seven_Theses.md`
- `Core_Law/SRT_Individuation.md`
- `Core_Law/SRT_Irreversibility.md`
- `Core_Law/SRT_L0_Metaphysics.md`
- `Core_Law/SRT_L1_Formalism.md`
- `Core_Law/SRT_L1_Hardening_Notes.md`
- `Core_Law/SRT_Occlusion_Dynamics.md`
- `Core_Law/SRT_Reference_Axioms.md`
- `Core_Law/SRT_Reference_Dynamics.md`
- `Core_Law/SRT_Reference_Ontology.md`
- `Core_Law/SRT_Suffering.md`
- `Governance/SRT_CLAIM_LADDER.md`
- `Governance/SRT_CLAIM_MODE_AUDIT.md`
- `Governance/SRT_POSITIONING.md`
- `Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md`
- `Neuroscience/SRT_Clin_02_FEP.md`
- `Neuroscience/SRT_Consciousness_Mechanisms.md`
- `Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md`
- `Neuroscience/SRT_Neural_Mechanisms.md`
- `Neuroscience/SRT_Neural_Mechanisms_CompactCore.md`
- `Neuroscience/SRT_Neuroscience_Claim_Status.md`
- `Neuroscience/_SRT_Neuro_Axioms.md`
- `Neuroscience/_SRT_Neuroscience_Hardening_Index.md`
- `Operations/Audits/SRT_P1_T07_PROOF_HARDENING_AUDIT.md`
- `Philosophy/00_READ_FIRST_Philosophy_Hardening_Soft_Spots.md`
- `Philosophy/01_PH_SS_Objection_Crosswalk.md`
- `Philosophy/02_PH_SS_Hardening_Execution_Plan.md`
- `Philosophy/03_Selection_Realism_Layered_Realism_CompactPatch.md`
- `Philosophy/PH_SS_Hardening_Audit_2026-04-27.md`
- `Philosophy/SRT_Ethics_PH_SS_Guardrails.md`
- `Philosophy/SRT_Philosophy_Claim_Status.md`
- `Philosophy/SRT_Philosophy_Foundations.md`
- `Philosophy/SRT_Philosophy_Foundations_CompactCore.md`
- `Philosophy/SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md`
- `Philosophy/SRT_Philosophy_Public_OnePager.md`
- `Philosophy/SRT_Philosophy_Tradition_Comparison_PH_SS.md`
- `Philosophy/SRT_Political_Philosophy.md`
- `Philosophy/SRT_Political_Philosophy_CompactCore.md`
- `Philosophy/SRT_Political_Rights.md`
- `Philosophy/SRT_Social_Cognition.md`
- `Philosophy/SRT_Social_Economics.md`
- `Philosophy/SRT_Social_Economics_CompactCore.md`
- `Philosophy/SRT_Social_Political_PH_SS_Guardrails.md`
- `Philosophy/SRT_Subjecthood_Threshold_Interface.md`
- `Philosophy/_PHILOSOPHY_MACHINE_INDEX.md`
- `Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md`
- `Physics/PHYSICS_COMPACT_REGISTRY.md`
- `Physics/SRT_Phys_07_Complex_Systems.md`
- `Physics/SRT_Phys_07_Complex_Systems_CompactCore.md`
- `Physics/SRT_Phys_08_Ontology_Ext.md`
- `Physics/SRT_Phys_08_Ontology_Ext_CompactCore.md`
- `Physics/SRT_Phys_09_Formalism_Ext.md`
- `Physics/SRT_Phys_09_Formalism_Ext_CompactCore.md`
- `Physics/SRT_Phys_10_Integration.md`
- `Physics/SRT_Phys_10_Integration_CompactCore.md`
- `Physics/SRT_Physics_Claim_Status.md`
- `Physics/SRT_Physics_Cosmology.md`
- `Physics/SRT_Physics_Cosmology_CompactCore.md`
- `Physics/SRT_Quant_00_Intro.md`
- `Physics/SRT_Quant_00_Intro_CompactCore.md`
- `Physics/SRT_Quant_01_Selection.md`
- `Physics/SRT_Quant_01_Selection_CompactCore.md`
- `Physics/SRT_Quant_02_Cosmology.md`
- `Physics/SRT_Quant_02_Cosmology_CompactCore.md`
- `Spirituality/SPIRITUALITY_COMPACT_REGISTRY.md`
- `Spirituality/SRT_Spirit_09_Praxis.md`
- `Spirituality/SRT_Spirit_09_Praxis_CompactCore.md`
- `Spirituality/SRT_Spirituality_Claim_Status.md`
- `Spirituality/_SRT_Spirit_Axioms.md`
- `_SRT_CROSS_DOMAIN_MATRIX.md`
- `_SRT_D_VALUE_CANONICAL.md`
- `_SRT_PSI_F_CANONICAL.md`
- `_SRT_SYMBOL_TABLE.md`
- `_SRT_T_DIR_CANONICAL.md`
- `_SRT_VERTICAL_INTEGRATION.md`

</details>


---


> **注意**：本包**不含** canonical 骨架（`d` / `Ψ_f` / `T_dir` 定义、核心公理、
> 主方程、符号表），因此**仅凭本包不得裁定任何 SRT 术语的定义**。
>
> 需要裁定定义时，请**改用骨架路线**——新开一次对话，只装
> `SRT_CONTEXT_BUNDLE_SPINE.md`。**不要在本包之上再叠加骨架包**：两者合计会超出
> 上下文预算（见 `README.md` 的预算表）。两条路线互斥，是切换关系，不是叠加关系。



---

## FILE: `Core/SRT_Core_14_Dynamics_Scaling_CompactCore.md`

| 字段 | 值 |
|---|---|
| path | `Core/SRT_Core_14_Dynamics_Scaling_CompactCore.md` |
| id | SRT-CORE-14-COMPACT-CORE |
| claim_mode | canonical |
| status | active_v1 |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | - |
| last_commit | 2026-04-20 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：[SRT-CANONICAL-REGISTRY, SRT-CORE-14, SRT-D-VALUE-CANONICAL, SRT-CORE-22]

<!-- 以下为原文逐字保留 -->

# SRT Core 14 — Dynamics & Scaling Compact Core

> **定位**：本文件是 `Core/SRT_Core_14_Dynamics_Scaling.md` 的紧凑主干版。  
> **用途**：用于快速把握 SRT 跨尺度动力学的最短核心骨架。  
> **关系**：不替代原文；原文保留长篇机制推演、接口批次、案例扩展与 annex 沉积。

## 1. 核心问题

`Core 14` 解决的是 SRT 中最关键的统一问题：

> **同一套选择动力学，如何在量子—生物—社会—宇宙等不同尺度上保持结构同构？**

它的核心主张不是“万物都一样”，而是：

> **不同尺度上的现实形成，服从同一类选择—摩擦—边界代价语法。**

---

## 2. 跨尺度同构

### 2.1 Self-Similar Selection
\[
\hat{G}_{S_2} = \Lambda \circ \hat{G}_{S_1} \circ \Lambda^{-1}
\]

含义：
- 选择算子在尺度变换 \(\Lambda\) 下保持共轭不变性
- 量子坍缩、神经决策、社会选择、宏观结构稳定可以共享同一种拓扑逻辑

> **注（Ax-F-11 / P3-B07）**：粗粒化映射 \(\Lambda\) 本身即幽灵算子在尺度变换下的禀赋展开——量子坍缩、侧抑制、归一化、范畴化均为同一结构的不同尺度实现形式，而非形式类似的独立过程。见 `Core/SRT_Core_21c_Bridge_Hypotheses.md P3-B07`。

这不是说“所有尺度的对象完全一样”，而是说：
- 它们的**形成机制**存在同构性
- 差异主要体现为参数、耦合、预算与带宽条件不同

---

## 3. d-value 的跨尺度角色

### 3.1 Ontological Bandwidth
\[
d \equiv \max\text{-bandwidth}(\hat{G}_\theta \text{ against } \Psi_f)
\]

这里的 d 不作为最终规范锚点，而作为：
> **d-value 在跨尺度动力学中的功能性展开。**

它与规范定义
\[
d \equiv \left\|\frac{\partial\mathcal{U}}{\partial\mathcal{S}}\right\|
\]
保持一致：
- 风险梯度越大，算子需要的带宽越高
- 可承受风险梯度的范围越大，说明带宽越高

因此：
\[
d_{bandwidth} = \sup\left\{\left\|\frac{\partial\mathcal{U}}{\partial\mathcal{S}}\right\| : \hat{G}_\theta \text{ remains stable}\right\}
\]

### 3.2 三尺度投影

- **量子域**：相干窗口 / 海森堡切口范围
- **生物认知域**：关切范围 / 注意力与自由能最小化带宽
- **宇宙域**：时空共识与拓扑紧致度

最重要的边界是：
> d 是跨尺度数学标尺，不等于跨尺度意识赋值。

只有在生物/认知域满足充要三条件时，d 才表现为意识相关关切，而不是纯数学量。

---

## 4. 主动力学

### 4.1 Generalized Selection Equation
\[
\frac{d\rho_{L_1}}{dt} = -\frac{i}{\hbar}[\hat{H}, \rho] - \hat{G}_\theta[\rho - \rho_{target}] + \mathcal{D}[\rho]
\]

这条方程给出 SRT 对现实演化的最压缩刻画：

1. **自由展开**：系统沿自身动力学展开
2. **选择锚定**：算子把状态拉向目标结构
3. **退相干/耗散**：环境引入损失与稳定化

所以现实不是“纯自然演化”，也不是“纯意志控制”，而是三项竞争平衡。

### 4.2 被动选择极限
当约束远强于主动选择时：
\[
\|\hat{G}_\theta[\rho-\rho_{target}]\| \ll \|\nabla C_{L_2}[\rho]\|
\]
系统进入：
> **constraint-dominated glide**

即轨迹主要沿既有约束滑行，主动能动窗口收缩。

---

## 5. 语义边界与自创生

### 5.1 Semantic Boundary Maintenance
\[
\frac{d\theta}{dt} = -\alpha \nabla_\theta \Psi_f + \text{Learning}
\]

含义：
- 自我不是静态实体
- 而是一个持续调节摩擦与学习的边界维持过程

### 5.2 Insight as Phase Transition
\[
\text{Insight} = \hat{G}_\theta[\theta \to \theta_c^+] - \hat{G}_\theta[\theta \to \theta_c^-]
\]

顿悟因此不是“信息多一点”，而是：
> **参数跨阈值导致的拓扑相变。**

---

## 6. 适应度优先而非真相优先

### 6.1 Fitness-over-Truth Inequality
\[
\Psi_f^{Truth}(\theta) \gg \Psi_f^{Fitness}(\theta)
\]

在有限预算下：
\[
\Psi_f^{Truth}>E_{avail} \Rightarrow \text{unsustainable}
\]
\[
\Psi_f^{Fitness}\le E_{avail} \Rightarrow \text{stable anchoring}
\]

SRT 的压缩判断：
> **有限算子优先维持可支付界面，而不是无损重建全部真相。**

这解释了：
- 为什么生命系统倾向低摩擦对象化
- 为什么知觉常偏向稳定可用，而非全信息保真
- 为什么“适应度追踪”在很多情况下比“真相追踪”更可持续

---

## 7. 对象、边界与模糊性

### 7.1 同步个体化—分类原则
\[
(\mathcal{B}_{obj},\mathcal{C}_{attr})_t
=\arg\min_{\mathcal{B},\mathcal{C}}\Big(\mathcal{L}_{pred}+\lambda\Psi_f^{maint}\Big)
\]

对象边界与分类属性不是先后两步，而是同一坍缩过程的双视角。

### 7.2 Boundary Demarcation Cost
\[
F_{boundary}(\tau)=\mathcal{L}_{class}(\tau)+\lambda_1\Psi_f^{maint}(\tau)+\lambda_2\Psi_f^{switch}(\tau)
\]

合法边界必须满足：
\[
F_{boundary}(\tau)\le U_{survival}(d)
\]

含义：
- 边界不是绝对刻线
- 边界是分类误差、维持摩擦、切换代价三者平衡后的结果
- 若代价过高，系统宁可保留模糊区

### 7.3 Sorites / 模糊性解释
因此：
> **模糊性不是单纯语言失败，而是有限分辨率与能量预算下的边界相变问题。**

---

## 8. 反泛心论边界

SRT 在 `Core 14` 中最容易被误读的地方，是把 d 的跨尺度统一误读成“跨尺度意识统一”。

SRT 的压缩立场是：
- d 是跨尺度数学标尺
- 意识不是跨尺度默认属性
- 只有当以下条件同时满足时，才有意识相关成立：
\[
\text{Consciousness} \iff \Psi_f > 0 \land d > 0 \land \hat{G}[\theta] \neq \emptyset
\]

所以：
- 量子可有相干带宽，不等于有主观体验
- 宇宙可有拓扑整合，不等于有拟人化意识

---

## 9. 最压缩结论

`Core 14` 的主干可以压缩成五句话：

1. **选择动力学在不同尺度上保持结构同构。**
2. **d-value 是算子对抗摩擦的跨尺度带宽表征。**
3. **现实演化由自由展开、选择锚定与耗散三项共同决定。**
4. **对象边界来自误差、摩擦与切换成本的平衡，而非绝对刻线。**
5. **跨尺度统一不等于跨尺度泛心；意识仍需额外满足严格条件。**

---

## 10. 阅读路径

- 全量原文：`SRT_Core_14_Dynamics_Scaling.md`
- split 导航：`Dynamics_Scaling_Split/README.md`
- annex 导航：`Dynamics_Scaling_Annex/README.md`
- d-value 规范：`../_SRT_D_VALUE_CANONICAL.md`
- Core 主方程：`SRT_Core_22_Equations.md`
- canonical 总注册表：`../CANONICAL_REGISTRY.md`
