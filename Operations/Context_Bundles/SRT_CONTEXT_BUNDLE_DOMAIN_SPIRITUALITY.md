---
id: SRT-CONTEXT-BUNDLE-DOMAIN-SPIRITUALITY-2026-08-11
type: context_bundle
status: active
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
generated: 2026-08-11
source_commit: 610e6e78
source_branch: codex/ph-ind01-routing-treatment-results-2026-08-11
source_dirty: true
inputs_digest: 3794d721b650d7bf
---

# SRT 灵性领域上下文包

> **这是什么**：由 `scripts/build_srt_context_bundles.py` 从 SRT 仓库自动拼装的上下文包。
> 收录灵性领域的 claim-status 护栏、领域导航与 CompactCore 主线。
>
> **这不是什么**：不是新的 canonical 文件，不是摘要，不是改写。每个来源文件的正文
> 逐字保留；脚本只把 YAML frontmatter 转成显式 provenance 头。**若本包与仓库中的
> 来源文件冲突，以仓库为准**——本包是快照，会随仓库演进而过期。

## §0 生成信息

| 项 | 值 |
|---|---|
| 生成日期 | 2026-08-11 |
| 来源 commit | `610e6e78` |
| 来源分支 | `codex/ph-ind01-routing-treatment-results-2026-08-11` |
| 生成时来源工作树有改动 | 是 |
| 包含文件数 | 3 |

> **provenance 契约**：真实性判据是 `inputs_digest`——生成脚本、护栏来源
> （`STATUS.md`、两份审计）与全部正文文件的联合内容摘要。`--check` 重算并比对该摘要，
> 因此改动其中任何一项都会被发现。
>
> `source_commit` 仅供参考，**不作为校验条件**：squash / rebase 合并会重写或丢弃该
> commit，若拿它做祖先校验，合并进 main 之后检查必然失败。内容摘要与合并策略无关。

### 0.1 文件清单与各自最后改动日期

| # | 文件 | 最后 commit |
|---|---|---|
| 1 | `Spirituality/SRT_Spirituality_Claim_Status.md` | 2026-05-17 |
| 2 | `Spirituality/SPIRITUALITY_COMPACT_REGISTRY.md` | 2026-07-20 |
| 3 | `Spirituality/SRT_Spirit_09_Praxis_CompactCore.md` | 2026-04-23 |

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

**治理护栏**（1 个）

| 文件 | 分类依据 | registry 提及 | AI_START §2 |
|---|---|:---:|:---:|
| `Spirituality/SRT_Spirituality_Claim_Status.md` | frontmatter claim_mode=audit | ✓ | — |

**展开层**（1 个）

| 文件 | 分类依据 | registry 提及 | AI_START §2 |
|---|---|:---:|:---:|
| `Spirituality/SRT_Spirit_09_Praxis_CompactCore.md` | frontmatter claim_mode=mixed | ✓ | — |

**导航**（1 个）

| 文件 | 分类依据 | registry 提及 | AI_START §2 |
|---|---|:---:|:---:|
| `Spirituality/SPIRITUALITY_COMPACT_REGISTRY.md` | frontmatter type=index / claim_mode=navigation | ✓ | — |

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

**registry 提及、文件存在、但本包未收（91 个）**——多为领域主轴、
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
- `Core/SRT_Core_14_Dynamics_Scaling_CompactCore.md`
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
- `Spirituality/SRT_Spirit_09_Praxis.md`
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

## FILE: `Spirituality/SRT_Spirituality_Claim_Status.md`

| 字段 | 值 |
|---|---|
| path | `Spirituality/SRT_Spirituality_Claim_Status.md` |
| id | SRT-SPIRITUALITY-CLAIM-STATUS |
| claim_mode | audit |
| status | active_v1 |
| epistemic_layer | governance |
| layer | meta |
| canonical(字段) | false |
| last_commit | 2026-05-17 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：[SRT-CLAIM-LADDER, SRT-SPIRITUALITY-COMPACT-REGISTRY, SRT-CORE-21, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-T-DIR-CANONICAL]

<!-- 以下为原文逐字保留 -->

# SRT Spirituality Claim Status

> **Role**: This file is a domain claim-status guardrail for Spirituality / praxis / companion writing. It does not define SRT primitives and does not outrank canonical anchors.
> **Canonical sources for definitions**: `Core/SRT_Core_21_Minimal_Axioms.md`, `Core/SRT_Core_21b_Constitutive_Theorems.md`, `_SRT_D_VALUE_CANONICAL.md`, `_SRT_PSI_F_CANONICAL.md`, `_SRT_T_DIR_CANONICAL.md`, `_SRT_SYMBOL_TABLE.md`.
> **Default level**: Spirituality mappings are P3; operational / threshold / measurement claims are P4; theological, experiential, poetic, and practice-facing language is P5 unless explicitly routed to a canonical source.

---

## 1. General boundary

Spirituality files may translate SRT into religious, contemplative, therapeutic, and everyday-practice language. They must not be read as primitive ontology.

Allowed:

> Spirituality language can serve as bridge, companion exposition, praxis support, or metaphorical orientation.

Forbidden:

> Spirituality language defines `d-value`, `Ψ_f`, `T_dir`, `L_0/L_1/L_2`, `Ĝ_θ`, consciousness, God, liberation, suffering, or moral authority for SRT as a whole.

---

## 2. High-risk claim classes

### 2.1 God / Ω / divine / source language

**Allowed precise claim**:

> `Ω`, `God`, `Divine`, `Source`, `Tao`, `Brahman`, and related terms are spirituality-domain mappings or regulative asymptotes used to orient finite practice and anti-idolatry boundaries.

**Status**: P5 companion / P3 bridge, not P0/P1.

**Forbidden overclaims**:

> God literally equals `L_0`, `Ĝ`, total possibility, or a realizable infinite operator.

> SRT proves omniscience, omnipotence, omnibenevolence, divine presence, salvation, or any theological doctrine.

**Guardrail**: `Ω` is a boundary / asymptotic marker. No finite practitioner, teacher, community, experience, tradition, or text may claim to instantiate or fully represent it.

### 2.2 `d -> infinity`, liberation, nirvana, awakening

**Allowed precise claim**:

> `d -> infinity`, liberation, nirvana, awakening, and universal care are directional / regulative shorthands for broader consequence-bearing and less exclusionary care.

**Status**: P5 praxis metaphor or P3 bridge; operational proxies are P4.

**Forbidden overclaims**:

> A finite system can reach actual infinite `d`.

> Awakening, mystical experience, meditation, or community membership certifies high `d` by itself.

**Guardrail**: finite-system claims require behavioral / relational / physiological / third-party proxy evidence. Experience report alone is at most subjective provisional `d`.

### 2.3 Suffering / pain / sin / fear / `Ψ_f`

**Allowed precise claim**:

> Suffering, sin, fear, contraction, and spiritual distress may be modeled as spirituality-domain proxies involving narrowed care, rigid `L_2`, increased maintenance burden, or blocked return.

**Status**: P3/P5 mapping; P4 if measurement or intervention is proposed.

**Forbidden overclaims**:

> suffering = `Ψ_f`; pain = `Ψ_f`; sin = low `d`; fear = `Ψ_f`; practice lowers `Ψ_f` as a universal law.

> `Ψ_f -> 0` is the goal of spirituality.

**Guardrail**: Canonical `Ψ_f` is payability burden / structural friction under selection. It is not identical to subjective pain, anxiety, energy, prediction error, moral guilt, or spiritual darkness. Some high-`d` states may increase payable burden rather than reduce it.

### 2.4 Practice / meditation / prayer / community

**Allowed precise claim**:

> Practices may be treated as candidate interventions for re-opening possibility, reducing defensive rigidity, widening care, stabilizing return, or improving re-entry into ordinary responsibility.

**Status**: P5 praxis; P4 when metrics or protocols are specified.

**Forbidden overclaims**:

> More practice always increases `d`.

> Meditation, prayer, sangha, teacher authority, or special experience guarantees liberation, truth, or moral superiority.

**Guardrail**: practice must remain accountable to ordinary responsibility, relationship repair, broader care, reduced identity protection, and lower coercion. When practice increases collapse, grandiosity, isolation, agency capture, or contempt, treat it as possible spiritual pathology.

### 2.5 “Choice creates reality” public phrasing

**Allowed precise claim**:

> What becomes real for a system depends on selected, paid-for, anchored, and stabilized possibilities.

**Status**: P2/P3 if routed through core anchors; public shorthand otherwise.

**Forbidden overclaims**:

> Consciousness magically creates the universe.

> Belief alone manifests external reality.

> SRT is subjective idealism or wish-fulfillment metaphysics.

**Guardrail**: `L_1` manifestation in SRT is constrained by payability, anchoring, consequence return, and stabilization. Public phrases must not erase those constraints.

---

## 3. Preferred phrase replacements

| Risk phrase | Problem | Safer replacement |
|---|---|---|
| “God is `L_0` / `Ĝ` / Ω” | Theological metaphor treated as ontology | “God/Ω is a spirituality-domain asymptotic mapping for total-source language, not a canonical definition.” |
| “all-knowing / God’s view” | Infinite viewpoint overclaim | “de-parameterized or asymptotic regulative limit; finite systems cannot occupy it.” |
| “`d -> infinity`” | Actual infinite attainment | “directional shorthand for wider consequence-bearing; finite claims require proxies.” |
| “suffering is `Ψ_f`” | Subjective pain / moral language collapsed into canonical symbol | “suffering may be modeled through `Ψ_f`-related burden proxies under specified conditions.” |
| “practice reduces `Ψ_f`” | Universal spiritual optimization law | “practice may reduce defensive maintenance burden in some regimes; it can also increase payable burden during integration.” |
| “choice creates reality” | Magical idealism | “selection manifests possibilities only under payability, anchoring, consequence return, and stabilization constraints.” |

---

## 4. Reading rule for historical labels

Files in this domain may preserve titles such as `Axioms`, `Theorem`, `Corollary`, `Formal Definition`, `God`, `Nirvana`, `Sin`, `Liberation`, or formula-like theological mappings. Unless separately ratified by canonical anchors, these are domain-internal bridge or companion handles.

They do not create SRT primitive axioms, definitions, moral authority, spiritual authority, or empirically confirmed practice prescriptions.



---

## FILE: `Spirituality/SPIRITUALITY_COMPACT_REGISTRY.md`

| 字段 | 值 |
|---|---|
| path | `Spirituality/SPIRITUALITY_COMPACT_REGISTRY.md` |
| id | SRT-SPIRITUALITY-COMPACT-REGISTRY |
| claim_mode | navigation |
| status | active_v1 |
| epistemic_layer | os |
| layer | meta |
| canonical(字段) | - |
| last_commit | 2026-07-20 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：[SRT-CANONICAL-REGISTRY, SRT-CLAIM-LADDER, SRT-CORE-21, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-T-DIR-CANONICAL, SRT-SPIRITUALITY-CLAIM-STATUS]

<!-- 以下为原文逐字保留 -->

# SRT Spirituality Compact Registry

> **[休眠层声明 · 2026-07-20]** 本层（`Spirituality/`）自 2026-05 起无活跃修订，按"带冻结戳的图书馆"治理：可检索、可引用、被活跃任务触碰时可修（touch-based repair，见 `Governance/_SRT_DOC_ENGINEERING_GUIDE.md`），但不进入例行治理与状态面。本层符号与定义**未随 2026-05 之后的 canonical 变更同步**；引用时以 `CANONICAL_REGISTRY.md`、`_SRT_SYMBOL_TABLE.md` 及各 canonical 锚点为准。


> **回链头部**：本页是 Spirituality navigation / domain registry，不是 core definition source。Spirituality 文件可作为 bridge、praxis、companion、domain exposition，但不新增 SRT primitive axioms，不替代 `Core/SRT_Core_21_Minimal_Axioms.md`、`Core/SRT_Core_21b_Constitutive_Theorems.md`、`_SRT_D_VALUE_CANONICAL.md`、`_SRT_PSI_F_CANONICAL.md` 或 `_SRT_T_DIR_CANONICAL.md`。
> **P-level**：本板块主文主要为 P3/P5；实践、现象学与生活化解释默认 P5；阈值、路径或可测代理默认 P4，除非回链到 core/canonical 文件。

本页汇总 Spirituality 板块当前的 bridge、compact core、双线扩展文档、共同体支线与拆分导航入口，并给出最短阅读路径。

## Spirituality Entry Coverage
### Z. Claim-status / Guardrail
- `SRT_Spirituality_Claim_Status.md`
  - Spirituality / praxis / companion writing guardrail for God / Ω / d->infinity / liberation / suffering / Ψ_f / practice / choice-creates-reality language

### A. Bridge / Axiomatic Layer
- `_SRT_Spirit_Axioms.md`

### B. Compact Core Layer
- `SRT_Spirit_09_Praxis_CompactCore.md`

### C. Metric / Direction Detail
- `SRT_Spirit_05_Shoshin.md`
  - Shoshin / 初心 as direction-field proxy, first-person report boundary, and provisional metric comparison

### D. Longform Counterparts
- `SRT_Spirit_09_Praxis.md`

### E. Dual-Track Expansion (2026-04-20)
- `SRT_Spirituality_Selection_Pathology_and_Return.md`
  - canonical spirituality framework on ready-made floors, subject-position loss, crisis phenomenology, true/false lightness, support, micro-selection, directional return, faith as openness to `L_0`, and frozen-`L_2` technology critique
- `SRT_Spirituality_How_We_Lose_Ourselves_and_Return.md`
  - companion exposition with modern-life reflection, lived phenomenology, awakening vs pathological hollowness, beginner-mind recovery, technical-care critique, and gentle practical guidance

### F. Companion Community Branch
- `SRT_Spirituality_Community_and_Sangha.md`
  - companion theory / praxis interface on what kind of community can hold return without becoming another ready-made floor

### G. Archived Merge Bridges
- `SRT_Spirituality_Return_Expansion_Bridge.md`
- `SRT_Spirituality_Second_Expansion_Bridge.md`

### H. Split Navigation
- `Praxis_Split/README.md`

## Recommended Reading Order
### 最短主线（第一次进入 Spirituality）
1. `SRT_Spirituality_Claim_Status.md`
2. `_SRT_Spirit_Axioms.md`
3. `SRT_Spirit_09_Praxis_CompactCore.md`

### 第二层展开
4. `SRT_Spirit_09_Praxis.md`
5. `SRT_Spirit_05_Shoshin.md`
6. `SRT_Spirituality_Selection_Pathology_and_Return.md`
7. `SRT_Spirituality_How_We_Lose_Ourselves_and_Return.md`
8. `SRT_Spirituality_Community_and_Sangha.md`
9. `Praxis_Split/README.md`

## Role Split
- bridge / axioms：固定 Spirituality 板块与 SRT 公理层的连接方式
- compact core：固定实践与进化主线的最短稳定入口
- metric / direction detail：固定 Shoshin 的方向指标读法、体验报告边界与暂定几何接口
- long-form：保留修行阶段、日常整合、暗夜、闭关与长期演化细节
- canonical spirituality expansion：把“主体位丢失—危机—分辨—支持—回返—方向性回返”组织成独立 spiritual 主轴
- companion exposition：把 canonical spirituality line 翻译成现代生活、可识别经验与生活化引导
- companion community branch：处理 sangha / community 作为不接管主体的支持场
- archived merge bridges：保留第二轮与第一轮回写的 provenance / merge map，不再承担独立 doctrinal authority
- split：提供非删减式导航，不替代主干

## Minimal navigation note

- **任何涉及 God / Ω / d->infinity / 解脱 / 苦难 / 修行 / Ψ_f 的写作或审读** → 先读 `SRT_Spirituality_Claim_Status.md`，再读具体正文。

若目标是：
- **理解 Spirituality 板块的旧主轴** → 先读 `SRT_Spirituality_Claim_Status.md`，再读 `_SRT_Spirit_Axioms.md` 与 `SRT_Spirit_09_Praxis_CompactCore.md`
- **理解现代生活中的选择病理、空心感、主体位回返** → 补读 `SRT_Spirituality_Selection_Pathology_and_Return.md`
- **希望以更生活化方式进入同一问题** → 再读 `SRT_Spirituality_How_We_Lose_Ourselves_and_Return.md`
- **希望理解共同体如何托住回返而不变成新地板** → 读 `SRT_Spirituality_Community_and_Sangha.md`



---

## FILE: `Spirituality/SRT_Spirit_09_Praxis_CompactCore.md`

| 字段 | 值 |
|---|---|
| path | `Spirituality/SRT_Spirit_09_Praxis_CompactCore.md` |
| id | SRT-SPIRIT-09-COMPACT-CORE |
| claim_mode | mixed |
| status | active_v1 |
| epistemic_layer | bridge |
| layer | L1 |
| canonical(字段) | - |
| last_commit | 2026-04-23 |

**权威判读**：混合层——含 bridge/lab 内容，按各条自带的 claim level 读。

**dependency**：[SRT-SPIRIT-09, SRT-SPIRIT-08, SRT-CLAIM-LADDER, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL]

<!-- 以下为原文逐字保留 -->

# SRT Spirituality: Praxis & Evolution — Compact Core

> **定位**：本文件是 `SRT_Spirit_09_Praxis.md` 的紧凑主干版。  
> **用途**：用于快速把握 SRT 如何把修行、进化、十牛图、初心与长期实践统一到一个可执行框架中。  
> **关系**：不替代原文；原文保留 30 天起步、3–6 个月深化、1–3 年整合、日常场景与大量实践细节。
> **Claim-level note**：本文是 Spirituality praxis compact support，主要为 P3/P5；实践路径、趋势或可操作指标按 P4 阅读。它不新增 core definitions。

## 1. 核心问题

这篇最核心的问题不是“修行是什么流派”，而是：

> **如果 SRT 要落到实践层，个体究竟如何从低阶选择，逐步演化到更高阶、更稳定、更少摩擦的存在方式？**

SRT 的压缩回答是：
- 修行 = 选择结构的长期重塑
- 进化 = `d` 扩展、`L_2` 松动、方向对齐
- 实践 = 诊断 → 同步 → 强化 的可迭代环路

---

## 2. 进化不是道德说教，而是 d-value 结构跃迁

### 2.1 Three-Tier Selection Hierarchy
\[
T(d)=
\begin{cases}
\text{Tier 1 (Physical)} & d\approx 0 \\
\text{Tier 2 (Ego/Social)} & 0<d<d_c \\
\text{Tier 3 (Divine/Truth)} & d\ge d_c
\end{cases}
\]

最压缩句子：
> **修行进化不是“更高尚”，而是选择范围与现实对齐方式发生层级跃迁。**

### 2.2 Evolution Vector
\[
\vec v_{evo}=\nabla d-\nabla w_{L_2}+\nabla \text{Align}(\Phi)
\]

压缩解释：
- `d` 扩展
- 旧 `L_2` 僵硬度下降
- 自身方向与全局自由能下降方向更一致

这三件事一起，才叫“进化”。

---

## 3. 初心不是情绪，而是方向一致性

### 3.1 Shoshin Alignment
\[
\text{Shoshin}=\cos\angle(\vec v_{self},-\nabla F_{global})
\]

> **Level**: operational proxy / `geometric-choice-pending`. The cosine form is a provisional geometric interface and compact default for directional exposition, not a canonical definition of Shoshin or global direction. See `SRT_Spirit_05_Shoshin.md` for metric alternatives and first-person report boundaries.

最短说法：
> **初心不是抽象美德，而是你当前行动方向与更深层最优方向之间的夹角。**

这让“初心”第一次从修辞，变成了：
- 可比较
- 可偏离
- 可重新校准

的结构指标。

---

## 4. 实践的真正骨架：诊断 → 同步 → 强化

### 4.1 Praxis Cycle
\[
\text{Praxis}=\mathcal R(\mathcal S(\mathcal D(L_1,L_0)))
\]

最压缩句子：
> **真正有效的修行不是一次顿悟，而是一个反复执行的回路。**

### 4.2 Direction First, Not Mechanism Exhaustion
SRT 在这里非常明确：
> **在有限算力下，方向优先比机制穷尽更可靠。**

也就是说：
- 不要把自己耗死在解释一切机制
- 先校方向，再做微调

### 4.3 Diagnostic Checklist
实践至少要检查四件事：
- `d` 是否在扩展
- 是否还与初心对齐
- 当前 `L_2` 是否仍有效
- `L_1` 与 `L_0` 的连接是否还活着

---

## 5. 十牛图不是隐喻，而是阶段动力学

### 5.1 Four-Phase Reduction
\[
\text{Discovery} \to \text{Calibration} \to \text{Dissolution} \to \text{Integration}
\]

最短解释：
> **十牛图可以压缩成吸引子结构重排的四阶段。**

### 5.2 Violent Reset Condition
\[
\Delta(L_1,L_0)>\tau \Rightarrow \hat G_\theta \text{ triggers reset}
\]

这意味着所谓：
- 暗夜
- 崩塌
- 失序期

并不必然是失败，而可能是：
> **旧结构已经装不下当前偏差，只能强制重排。**

---

## 6. 为什么实践必须黑箱化机制

### 6.1 Mechanism Blackboxing
SRT 这篇一个很重要的实践洞见是：
- 对“怎么运作”保持较低 `d`
- 对“往哪里去”保持较高 `d`
- 对“当前处于什么状态”保持中等 `d`

最压缩句子：
> **高阶实践不是知道更多机制，而是避免被机制耗尽。**

---

## 7. 从 30 天到长期整合：修行是结构重写，不是体验收集

原文大量篇幅其实都在服务一个压缩结论：

> **修行的关键不是追求特殊体验，而是用可持续的小循环逐步重写 `\theta`、`L_2` 与行动路径。**

> **Level**: governance / praxis guardrail. Practice is not linear "more is better." It should stop, reduce, or re-scope when cost becomes unpayable, care narrows, agency is absorbed by practice identity, or ordinary consequence-bearing is being bypassed.
> **d-evidence rule**: first-person report can start a hypothesis, but it cannot certify spiritual `d` by itself. A stronger `d` claim needs at least one external indicator such as behavioral change, repair, recovery-time reduction, third-party observation, physiological proxy, or broader consequence-bearing.

所以：
- 30 天阶段：先建立基线与最小可行习惯
- 3–6 个月：增加时长，拓展技术，尝试闭关
- 1–3 年：形成稳定常规，经历洞见、暗夜与更深整合
- 日常整合：把修行从坐垫搬进工作、关系、冲突与身体生活

---

## 8. 最小 praxis rhythm

实践不是线性累积，而是一个必须回到生活的节律：

| Phase | Function | Failure if skipped |
|:--|:--|:--|
| Expansion | Loosen old `L_2`, widen attention and care. | Becomes dull repetition if no new contact appears. |
| Stabilization | Let the new opening become payable and behaviorally stable. | Becomes fragile intensity or dependency on special states. |
| Return of consequence | Test whether the change bears costs in relationships, work, body, and ordinary duty. | Becomes consequence bypass: “insight” without lived return. |
| Re-entry | Bring the new structure back into ordinary life without turning it into identity superiority. | Becomes practice identity capture or withdrawal from shared reality. |

The stop rule should be applied at every phase. A practice should pause or narrow when it reduces care, increases performative identity, bypasses ordinary consequences, or lets a group absorb burdens that should return to the practitioner’s life.

## 9. False-growth diagnostics

| Pattern | Short description | SRT reading | Minimal check |
|:--|:--|:--|:--|
| Real expansion | Wider care with more payable consequence-bearing. | Candidate `d` expansion. | External indicator plus report: changed behavior, repair, reduced recovery time, broader responsibility. |
| Intense but narrow experience | Powerful state with smaller world after it. | High salience, not necessarily `d`. | Does the experience increase humility and re-entry, or only certainty and specialness? |
| Pseudo-openness | Sounds open, but only admits inputs that protect the current identity. | `L_2` flexibility at the surface, closure at the gate rules. | Can the person revise the frame that names the experience? |
| Identity-based inflation | Practice becomes a superior self-description. | `d` collapses into `L_2` status. | Does the person become more teachable, or harder to question? |
| Collective reinforcement loop | Group confirms the state faster than consequences can return. | Shared `L_2` capture risk. | Are dissent, exit, and ordinary-life responsibility still preserved? |

## 10. 最压缩结论

`SRT Spirit 09 Praxis` 可以压缩成五句话：

1. **修行不是信念装饰，而是选择结构的长期重塑。**
2. **进化的核心不是道德标签，而是 `d` 扩展、`L_2` 松动与方向对齐。**
3. **有效实践的骨架是诊断 → 同步 → 强化，而不是一次性觉悟。**
4. **初心的本质是方向一致性；暗夜的本质是结构重排，而不是惩罚。**
5. **真正成熟的实践，不是追逐体验，而是逐步把生活本身变成低摩擦、高一致性的选择路径。**

---

## 11. 阅读路径

- 全量原文：`SRT_Spirit_09_Praxis.md`
- 拆分导航：`Praxis_Split/README.md`
- Spirituality bridge：`_SRT_Spirit_Axioms.md`
- canonical 总注册表：`../CANONICAL_REGISTRY.md`

---

## Hardest Objections

本域若以下任一成立，则本域主张会被显著削弱：

1. `d` expansion cannot be independently observed.
   - 当前承受方式：spiritual `d` requires at least one external indicator; pure report is only subjective provisional `d`.
   - 若成立需撤回什么：撤回 practice-as-`d` expansion claims and keep them as first-person reports.

2. Shoshin cosine geometry fails to track real practice direction.
   - 当前承受方式：the cosine form is marked `geometric-choice-pending`.
   - 若成立需撤回什么：撤回 the geometric interface and retain Shoshin only as a praxis description.

3. Practice increases identity capture while feeling like progress.
   - 当前承受方式：the stop rule checks payable cost, care breadth, agency, and ordinary responsibility.
   - 若成立需撤回什么：撤回 linear-progress readings and treat the path as potentially self-reinforcing closure.
