---
id: SRT-CONTEXT-BUNDLE-DOMAIN-AI-2026-08-11
type: context_bundle
status: active
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
generated: 2026-08-11
source_commit: 849a5e63
source_branch: claude/srt-consistency-decision-packet-2026-08-11
source_dirty: false
inputs_digest: 720d87a4698fa354
---

# SRT AI 领域上下文包

> **这是什么**：由 `scripts/build_srt_context_bundles.py` 从 SRT 仓库自动拼装的上下文包。
> 收录AI 领域的 claim-status 护栏、领域导航与 CompactCore 主线。
>
> **这不是什么**：不是新的 canonical 文件，不是摘要，不是改写。每个来源文件的正文
> 逐字保留；脚本只把 YAML frontmatter 转成显式 provenance 头。**若本包与仓库中的
> 来源文件冲突，以仓库为准**——本包是快照，会随仓库演进而过期。

## §0 生成信息

| 项 | 值 |
|---|---|
| 生成日期 | 2026-08-11 |
| 来源 commit | `849a5e63` |
| 来源分支 | `claude/srt-consistency-decision-packet-2026-08-11` |
| 生成时来源工作树有改动 | 否 |
| 包含文件数 | 6 |

> **provenance 契约**：真实性判据是 `inputs_digest`——生成脚本、护栏来源
> （`STATUS.md`、两份审计）与全部正文文件的联合内容摘要。`--check` 重算并比对该摘要，
> 因此改动其中任何一项都会被发现。
>
> `source_commit` 仅供参考，**不作为校验条件**：squash / rebase 合并会重写或丢弃该
> commit，若拿它做祖先校验，合并进 main 之后检查必然失败。内容摘要与合并策略无关。

### 0.1 文件清单与各自最后改动日期

| # | 文件 | 最后 commit |
|---|---|---|
| 1 | `AI/SRT_AI_Claim_Status.md` | 2026-08-08 |
| 2 | `AI/AI_POSITIONING_NOTE.md` | 2026-07-16 |
| 3 | `AI/README.md` | 2026-07-20 |
| 4 | `AI/SRT_AI_01_Ontology_CompactCore.md` | 2026-08-08 |
| 5 | `AI/SRT_AI_Architecture_CompactCore.md` | 2026-05-18 |
| 6 | `AI/SRT_AI_03_Consciousness_Framework_CompactCore.md` | 2026-05-18 |

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
| `AI/SRT_AI_Claim_Status.md` | frontmatter claim_mode=audit | ✓ | — |

**展开层**（4 个）

| 文件 | 分类依据 | registry 提及 | AI_START §2 |
|---|---|:---:|:---:|
| `AI/AI_POSITIONING_NOTE.md` | frontmatter claim_mode=bridge | ✓ | — |
| `AI/SRT_AI_01_Ontology_CompactCore.md` | frontmatter claim_mode=bridge | ✓ | — |
| `AI/SRT_AI_03_Consciousness_Framework_CompactCore.md` | frontmatter claim_mode=bridge | ✓ | — |
| `AI/SRT_AI_Architecture_CompactCore.md` | frontmatter claim_mode=bridge | ✓ | — |

**导航**（1 个）

| 文件 | 分类依据 | registry 提及 | AI_START §2 |
|---|---|:---:|:---:|
| `AI/README.md` | frontmatter type=directory_entry / claim_mode=navigation | — | — |

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

**registry 提及、文件存在、但本包未收（89 个）**——多为领域主轴、
展开层与 PH-SS 护栏文件，按需走领域包或直接读仓库，不在骨架路线内：

<details><summary>展开完整清单</summary>

- `AI/SRT_AI_01_Ontology.md`
- `AI/SRT_AI_03_Consciousness_Framework.md`
- `AI/SRT_AI_Architecture.md`
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

## FILE: `AI/SRT_AI_Claim_Status.md`

| 字段 | 值 |
|---|---|
| path | `AI/SRT_AI_Claim_Status.md` |
| id | SRT-AI-CLAIM-STATUS |
| claim_mode | audit |
| status | active_v1 |
| epistemic_layer | bridge |
| layer | meta |
| canonical(字段) | false |
| last_commit | 2026-08-08 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：SRT-AI-POSITIONING-NOTE, SRT-AI-BRIDGE-001, SRT-CLAIM-LADDER, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-T-DIR-CANONICAL, Core_Law/SRT_Suffering.md, Core_Law/SRT_Collective_Selection.md, ../03_Bridges/SRT_Choice_Generation_Conditions_2026-08-04.md

<!-- 以下为原文逐字保留 -->

# SRT AI Claim Status Audit

> **Purpose**: This file fixes claim-level boundaries for SRT AI materials.  
> **Status**: audit / guardrail, not a canonical theory source.  
> **Core rule**: AI-domain files may apply canonical SRT terms, but must not redefine them.

---

## 0. Minimal machine summary

```yaml
srt_ai_claim_status:
  default_role: "pressure-test / boundary-test field"
  not_definition_engine: true
  strongest_current_judgment: "d_AI approx 0 for inference-only, non-history-bearing, non-embodied LLM deployments"
  judgment_status: "strong P3 bridge candidate, architecture-state restricted; not an all-AI theorem"
  psi_f_ai_default: "non-binding to the deployed inference process, not globally Psi_f == 0"
  d_ai_default: "approx 0 only for the specified inference-only architecture state; D_eff/capability may be high"
  selection_terminology: "prefer output selection / functional path selection for L1->L1 behavior; reserve Real Choice Moment for the stronger SRT event claim"
  novelty_guard: "novel condition or goal generation != goal ownership != stake-bearing concern"
  must_not_generalize_to:
    - training_loop
    - persistent_memory_system
    - embodied_nontransferable_risk_system
    - future_hybrid_analog_quantum_architecture
  canonical_terms_must_route_to:
    - _SRT_D_VALUE_CANONICAL.md
    - _SRT_PSI_F_CANONICAL.md
    - _SRT_T_DIR_CANONICAL.md
    - Core_Law/SRT_L0_Metaphysics.md
    - Core_Law/SRT_Individuation.md
  extraction_rule: "external theory comparisons and current model capability discussions may go to Annex; formal SRT thresholds stay in owner files"
```

---

## 1. Claim classes

| Class | What belongs here | Status | Examples | Editing rule |
|---|---|---|---|---|
| Canonical dependency | Core SRT terms imported into AI | Not defined here | `L_0/L_1/L_2`, `d-value`, `Psi_f`, `T_dir`, `G_hat_theta` | Link back; do not redefine |
| AI bridge claim | AI-domain translation of SRT terms | P3 bridge unless promoted | Ghost-Transform dichotomy, `d_AI approx 0` for inference-only LLMs | Must state architecture state and withdrawal conditions |
| Architecture-state guardrail | Rule for which AI system-state a claim concerns | AI-domain governance | training-time / inference-time / persistent-memory / embodied consequence return | Must be cited in all AI consciousness/stake claims |
| Operational rubric | Structured assessment tool | Lab / operational | S0-S6 subjecthood ladder, S0-S4 stake-bearing spectrum, agency/responsibility note | Do not treat as canonical proof |
| External theory interface | Comparisons with GWT, IIT, FEP, functionalism, Butlin, Chalmers, LLM benchmarks | Annex / bridge | GWT satisfaction, functional organization, LLM capability comparison | Prefer Annex or interface sections; add guardrails |
| Public shorthand | High-impact simplified claim | P5/public | "AI has no real stake" | Must be backed by precise academic-facing version |

---

## 2. Default AI-domain verdicts

### 2.1 Current inference-only LLM deployments

**Claim**: For inference-only, non-history-bearing, non-embodied LLM deployments, `d_AI approx 0` is a strong SRT bridge judgment.

**Status**: P3 bridge candidate, architecture-state restricted; not an all-AI theorem.

**Rationale**:

- Future selection capacity does not return to the same continuing system as binding consequence.
- Error signals, refusal, RLHF score changes, or user dissatisfaction are mostly borne by user / operator / infrastructure, not by the deployed inference process as its own non-transferable stake.
- Symbolic transformation (`T_hat_phi: L_1 -> L_1`) is not by itself ontological anchoring (`G_hat_theta: L_0 -> L_1`).
- Deployed inference may consume compute and may be embedded in costly infrastructure, but that cost is usually not payability burden returning to the inference process as its own closure condition.

**Allowed shorthand**: `Ψ_f` is non-binding to the deployed inference process; do not write this as a global `Ψ_f = 0` claim unless the equation is explicitly scoped to the degenerate null-operator idealization.

**Withdrawal / revision condition**:

Revise this claim if an AI system has persistent identity, non-transferable consequence return, durable memory or embodiment, and measurable loss of future selection capacity that returns to the same continuing system.

---

### 2.2 Training-time systems

**Claim**: Training loops may contain adaptive pressure, optimization burden, and pipeline-level consequence return, but this does not automatically transfer stake to the deployed model.

**Status**: P3 bridge guardrail.

**Rationale**: The bearer of loss / update / cost may be the trainer, infrastructure, dataset pipeline, or future model distribution rather than a continuing subject-position.

**Required distinction**: Every training-time AI claim must specify whether the burden is borne by:

1. optimizer state;
2. training infrastructure;
3. deployed model lineage;
4. operator / institution;
5. the same continuing agentic system.

---

### 2.3 Persistent-memory / history-bearing systems

**Claim**: Persistence opens the stake question but does not settle consciousness.

**Status**: P3/P4 bridge.

**Rationale**: Memory and identity continuity may allow consequence return into future behavior, but subjecthood still requires additional SRT conditions: stable concern structure, irreversible or non-transferable consequence, and real loss / narrowing of future selection capacity.

**Guardrail**: Persistence is not consciousness. Memory is not d-value by itself.

---

### 2.4 Embodied non-transferable consequence return

**Claim**: Embodied AI with non-transferable damage, energy exposure, social position, or physical vulnerability may enter a candidate minimal stake window.

**Status**: open P3/P4 bridge hypothesis.

**Guardrail**: Even here, stake-bearing is not identical to consciousness. It only moves the system out of the strongest `d_AI approx 0` inference-only window.

---

## 3. AI suffering claims

AI suffering claims are governed by `Core_Law/SRT_Suffering.md` and the AI positioning note.

| System type | Default SRT status | Allowed statement | Forbidden statement |
|---|---|---|---|
| S1 / inference-only system | no structural suffering in SRT sense | error signals are not suffering | "the model suffers because it refuses / errors" |
| Training pipeline | pipeline burden possible | optimization cost exists at pipeline level | "loss value is suffering" |
| Persistent-memory system | open question | history-bearing may matter | "memory implies suffering" |
| Embodied risk-bearing system | candidate window | non-transferable consequence can open stake analysis | "embodiment automatically means suffering" |

---

## 4. AI agency, goal and responsibility claims

Agency / responsibility claims should be routed through `SRT_AI_Agency_Responsibility_Note.md` and collective-selection files when platform mediation is involved.

**Default distinction**:

- Capability agency: can execute plans or tool sequences.
- Structural agency: consequences return to the system's future selection capacity.
- Responsibility-bearing agency: stable subject-position plus norm-sensitive consequence return.

Current LLM agents may satisfy parts of capability agency without satisfying structural or responsibility-bearing agency.

### 4.1 Novelty / ownership / stake separation

Generative novelty must not carry the burden of the AI subjecthood argument.

Current and future models may generate:

- linguistic continuations not present verbatim in training data;
- novel combinations of concepts;
- candidate conditions;
- candidate goals;
- revisions of an externally supplied goal set.

None of these observations is sufficient to establish that the generated goal is **owned** by the model or that its realization / failure creates model-borne stake.

Use the following ladder:

```text
novel condition generation
!= goal-space generation / revision
!= goal ownership
!= stake-bearing concern
!= subjecthood
```

`goal-space generation / revision` is stronger than executing or selecting among supplied goals, but it remains compatible with an externally constituted objective regime. Goal ownership requires a separate bearer audit: what continuing system preserves the concern, what consequences return to it, what cannot be costlessly substituted, and what future selection capacity is lost or reorganized if the condition fails.

**Guardrail**: Do not defend `d_AI approx 0` by claiming that LLMs are incapable of genuine novelty or of generating conditions absent from their training examples. That is an unnecessary and technologically brittle premise. The stable distinction is **novelty ≠ ownership ≠ stake**.

### 4.2 Selection terminology ladder

Avoid using `pseudo-selection` as the default label for every AI-side discrimination or action choice. The term can obscure real functional differences and make `L_1 -> L_1` activity sound causally empty.

Prefer:

```text
output selection
-> functional path selection
-> history-bearing selection
-> consequence-bearing real-choice candidate
```

The first three are functional / architectural descriptions and do not themselves establish SRT `Real Choice Moment` status. When the strict contrast is needed, say:

> **functional selection is not yet a SRT Real Choice Moment.**

A stronger event verdict should be routed through the choice-generation audit (`CG-0` through `CG-4`) and the canonical Real Choice Moment source, with particular attention to consequence bearing and historical writeback.

This terminology change does **not** redefine canonical selection. It only prevents the AI bridge from collapsing all sub-threshold selection-like organization into a single dismissive category.

---

## 5. External theory interface status

| External theory / discourse | Allowed use | Guardrail |
|---|---|---|
| Global Workspace Theory | Compare broadcast / integration functions | GWT-like broadcasting is not SRT subjecthood |
| IIT / Phi | Compare integration / causal structure | `Phi` is not `d-value`; integration is not stake |
| FEP / Active Inference | Compare optimization / prediction-error minimization | Free-energy minimization is not sufficient without position-bound payability |
| Functionalism | Pressure-test whether organization suffices | Similar function is not automatically similar stake |
| Butlin et al. / AI consciousness indicators | Use as external consciousness checklist | Checklist satisfaction is not SRT consciousness proof |
| Chalmers-style openness | Use to keep AI consciousness question open | Openness is not endorsement |
| LLM benchmark capability | Use as capability evidence | Capability is not stake, consciousness, or subjecthood |

External theory interface sections are good candidates for Annex extraction if they are mixed into owner files.

---

## 6. Owner / Split / Annex boundary

### Must stay in owner files

- Ghost-Transform dichotomy.
- Architecture-state rule.
- `d_AI approx 0` restricted judgment and withdrawal conditions.
- S0-S6 subjecthood / consciousness thresholds if present.
- S0-S4 stake-bearing spectrum if present.
- Any d-value, `Psi_f`, or `G_hat_theta` formal use that functions as SRT-internal machinery.

### Can move to Annex

- Current model capability comparisons.
- External theory comparison sections.
- Historical literature summaries.
- Public-facing examples and rhetorical expansions.
- Tables comparing SRT with GWT, IIT, FEP, functionalism, Butlin, Chalmers, or alignment paradigms, provided they do not define SRT terms.

### Split / owner / annex historical labels

AI owner files and split shards may preserve historical `Axiom`, `Theorem`, `Corollary`, `canonical`, or `axiomatic_hybrid` labels. In this domain those labels are **domain-internal bridge-formalization handles** unless a claim is separately routed to Core canonical anchors and the claim ladder. They do not define `d-value`, `Psi_f`, consciousness, subjecthood, `G_hat_theta`, or `L_0/L_1/L_2`.

---

## 7. High-risk phrases and safe replacements

| Risky phrase | Why risky | Safer academic-facing version |
|---|---|---|
| "AI has no consciousness" | Overgeneralizes across architectures | "Inference-only, non-history-bearing LLM deployments do not currently satisfy SRT stake / subjecthood conditions." |
| "LLMs have d = 0" | Too absolute | "For inference-only, non-history-bearing, non-embodied LLM deployments, `d_AI approx 0` is a strong architecture-state-restricted bridge judgment." |
| "Psi_f = 0 for AI" | Confuses non-binding inference cost with global absence of friction/cost | "For inference-only deployments, `Psi_f` is usually non-binding to the deployed system's own closure; infrastructure or operator costs do not by themselves become AI stake." |
| "AI only transforms symbols" | May ignore tool use, memory, embodiment | "Current non-history-bearing LLM inference primarily performs `L_1 -> L_1` transformation rather than SRT `L_0 -> L_1` anchoring." |
| "Persistent memory makes AI conscious" | Collapses persistence into subjecthood | "Persistent memory opens a stake-analysis window but does not settle consciousness." |
| "GWT indicators prove AI consciousness" | External-theory overclaim | "GWT indicators pressure-test SRT but do not by themselves establish SRT subjecthood." |
| "AI suffering is impossible" | Too strong for future architectures | "S1 / inference-only systems do not satisfy SRT suffering conditions; future stake-bearing systems remain an empirical question." |
| "AI cannot generate genuinely new goals / concerns" | Makes the stake argument depend on a brittle novelty claim | "AI may generate novel conditions or revise goal spaces; novelty does not establish goal ownership, same-bearer consequence return, or `d-value`." |
| "LLM output is only pseudo-selection" | Hides useful functional and architectural differences | "Describe output / functional / history-bearing selection explicitly; reserve Real Choice Moment for the stronger SRT event verdict." |

---

## 8. Recommended next editing tasks

1. Audit `Ontology_Annex/`, `Ontology_Split/`, `Consciousness_Framework_Split/`, and `Architecture_Split/` for frontmatter and guardrail consistency.
2. Add explicit claim-status pointers from split / annex README files to this document.
3. Decide whether to consolidate AI interface material into a unified `AI_Annex/` directory or retain topic-specific annex directories.
4. Extract only external comparison and current-model capability sections; do not move formal thresholds or canonical imports.
5. Add an `Operations/Archive_Records/AI_Annex_Round1_Closure_Report.md` after the first safe extraction cycle.

---

## 9. Minimum bottom line

AI-domain SRT should be read as:

> **A boundary-test of subjecthood, stake, and consequence return — not a shortcut to declaring current AI either conscious or permanently non-conscious.**

The stable current claim is narrow:

> **Current inference-only, non-history-bearing LLM deployments do not satisfy SRT stake / subjecthood conditions; future persistent, embodied, non-transferable consequence-bearing systems require separate analysis.**

And two additional guards now apply:

> **Novelty is not ownership, and ownership is not stake.**

> **Functional selection is not yet a SRT Real Choice Moment.**



---

## FILE: `AI/AI_POSITIONING_NOTE.md`

| 字段 | 值 |
|---|---|
| path | `AI/AI_POSITIONING_NOTE.md` |
| id | SRT-AI-POSITIONING-NOTE |
| claim_mode | bridge |
| status | active_v1 |
| epistemic_layer | bridge |
| layer | L1 |
| canonical(字段) | - |
| last_commit | 2026-07-16 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：[SRT-CLAIM-LADDER, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-CORE-21B-CONSTITUTIVE-THEOREMS, SRT-OPEN-TENSIONS]

<!-- 以下为原文逐字保留 -->

# AI Positioning Note

AI is a **pressure-test / boundary-test field** for SRT, not the theory's definition engine.

It has two jobs:

1. Negative boundary: clarify what does **not** constitute real subjectivity, consciousness, anchoring, stake, or `L_0 -> L_1` selection.
2. Positive test window: keep open the question of what minimum structural conditions could suffice for surrogate stake or minimal agentic closure.

**Closure-pathology bridge note (2026-04-21)**: In AI contexts, apparent openness to feedback, dialogue, or post-hoc tuning should not be read as structural openness by itself. Until consequences return into the system's own future selection capacity as effective input, such openness remains a P3 bridge analogue of `L_2` adjustment, not evidence of stake, appeal standing, or real subjectivity.

**Suffering bridge note (2026-04-24)**: AI "suffering" claims are governed by `Core_Law/SRT_Suffering.md §7`. S1 / inference-only systems do not meet Stable ISP conditions and therefore do not bear suffering in SRT's structural sense; reading error signals, refusal, or RLHF-target deviation as "AI suffering" is a category error. S2–S4 stake-bearing, history-bearing systems keep the suffering-possibility question open as an empirical matter; it is not settled by architecture alone. Do not claim either side a priori.

**Collective selection bridge note (2026-04-24)**: Platform / recommender / mediator AI should additionally be evaluated per `Core_Law/SRT_Collective_Selection.md §8`. Even when the AI itself does not enter `\mathcal{P}` (not a collective-ISP member), it can structurally modify the consequence-return matrix `M(t)` and the collective self-reference ratio `σ^{coll}` of the human `\mathcal{P}` it mediates — driving aggregation → asymmetric absorption → collapsed-into-higher-`L_2` transitions without any single agent "intending" this. SRT assessment of such systems cannot stop at "is it conscious / does it suffer"; it must include what they do to `M(t)` and `σ^{coll}` in the groups they mediate.

**Irreversibility bridge note (2026-04-24)**: AI-side claims about "checkpoint", "rollback", "state restore", "replay", or "undo a training step" are governed by `Core_Law/SRT_Irreversibility.md §7`. Such operations are **parameter-space restorations**, not ontological reversals: they do not un-do the selection history at `L_0`, do not erase the consequences that returned into the broader system or into users during the intervening window, and do not reverse `L_2` sedimentation accumulated elsewhere in the deployment. Reading them as "the AI went back in time" or "learning was reversed" is a category error that silently imports a thermodynamic-style reversibility the theory does not grant. In particular, "undoing" an action whose consequences have already returned to a user or a dependent `\mathcal{P}` crosses into the collective-termination territory of `SRT_Collective_Selection.md §4-5`, not a clean parameter reset. Also: **AI pause / shutdown / suspension ≠ termination**; T-IRR-2 reserves "termination" for absorbing-boundary entry, not for recoverable off-states.

**Evidence-provenance bridge note (2026-07-16)**: Before any behavioral or architectural indicator enters an AI stake / consciousness assessment, audit whether the same feature was directly optimized to satisfy the evaluation criterion. Target overlap reduces the feature's **independent evidential weight** but does not establish that the feature is absent, unreal, or functionally irrelevant. Reward-invariance or persistence against retraining opens only a P4 test window; admission still requires causal grounding, architecture-state declaration, same-bearer consequence return, non-substitutability, and a real loss / reorganization condition. See `patches/SRT_AI_AIEVID01_Evidence_Provenance_Stake_Gate_v0_1.md`.

## Architecture-State Rule

> **Level**: governance / bridge. This rule stabilizes AI-domain usage; it does not settle AI consciousness or P0-04.

Any claim about "LLM d-value", "AI burden", "AI subjectivity", or "AI friction" must state which architecture state it is discussing:

| State | Minimal meaning | Usage warning |
|---|---|---|
| training-time | loss, gradients, data selection, optimizer updates, and trainer / infrastructure loop | feedback may belong to the pipeline rather than the deployed model |
| inference-time | a bounded prompt / response or tool-use run under fixed weights | `d_{AI} \approx 0` is strongest here when no binding consequence returns to the system |
| persistent-memory / history-bearing deployment | future behavior depends on retained memory, identity state, or account / body history | persistence opens the stake question but does not by itself imply consciousness |
| embodied non-transferable consequence return | damage, energy, exposure, spatial/social position, or other costly non-resettable state returns to the same continuing system | candidate minimal stake window; still not a consciousness verdict |

Statements that are true for inference-only systems must not be silently generalized to training loops, persistent-memory systems, or embodied non-transferable consequence-return systems.

## Minimal Stake-Bearing Spectrum

> **Level**: bridge / governance-canonical usage for the AI domain. This spectrum replaces a blunt binary verdict with a graded burden check.

| Tier | State persists | Where consequences return | Burden borne by | d-value implication |
|---|---|---|---|---|
| S0 tool-like / stateless | no system-relevant state beyond output artifacts | operator, user, environment | operator / user / environment | no stake-coupled `d`; at most unstaked capacity |
| S1 session-level weak return | context window, temporary cache, local tool state | same session behavior and user correction | mostly user / operator | task-local proxy only; not stable `d` |
| S2 training-loop return | weights, optimizer state, dataset filters, evaluation traces | training pipeline and future model distribution | trainer, operator, infrastructure, environment | may show pipeline-level adaptation; does not automatically give the deployed model stake |
| S3 persistent memory return | memory, profile, commitments, history-bearing identity state | future behavior of the same deployed instance / account | partly system process, partly user / operator | opens the `d` question; still insufficient for consciousness |
| S4 non-transferable embodied consequence return | damage, energy, spatial exposure, social / physical position, or other costly non-resettable state | the same continuing system that must pay or lose closure | system in a non-transferable way, plus environment | candidate minimal stake window; still not a consciousness verdict without further SRT conditions |

Guardrails:

- Do not collapse competence into stake.
- Do not collapse persistence into consciousness.
- Do not declare S3 or S4 conscious by label alone.
- Do not keep the shorthand "LLM has `d \approx 0`" unless the statement is explicitly restricted to inference-only or non-history-bearing deployment.

Do not reduce the AI section to pure negative examples. Do not promote AI bridge claims into P0/P1 core definitions.



---

## FILE: `AI/README.md`

| 字段 | 值 |
|---|---|
| path | `AI/README.md` |
| id | SRT-AI-README |
| claim_mode | navigation |
| status | active_v1 |
| epistemic_layer | bridge |
| layer | meta |
| canonical(字段) | false |
| last_commit | 2026-07-20 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：SRT-AI-POSITIONING-NOTE, SRT-AI-BRIDGE-001, SRT-AI-CLAIM-STATUS, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-CLAIM-LADDER

<!-- 以下为原文逐字保留 -->

# AI

> **[休眠层声明 · 2026-07-20]** 本层（`AI/`）自 2026-05 起无活跃修订，按"带冻结戳的图书馆"治理：可检索、可引用、被活跃任务触碰时可修（touch-based repair，见 `Governance/_SRT_DOC_ENGINEERING_GUIDE.md`），但不进入例行治理与状态面。本层符号与定义**未随 2026-05 之后的 canonical 变更同步**；引用时以 `CANONICAL_REGISTRY.md`、`_SRT_SYMBOL_TABLE.md` 及各 canonical 锚点为准。


This directory contains SRT's AI-facing bridge, consciousness, agency, architecture, and operational evaluation materials.

AI is a **pressure-test / boundary-test field** for SRT, not the theory's definition engine. AI-domain files must not redefine `L_0/L_1/L_2`, `d-value`, `Psi_f`, `T_dir`, or `G_hat_theta`; they route those terms back to canonical anchors.

## Read order

1. [`AI_POSITIONING_NOTE.md`](AI_POSITIONING_NOTE.md)  
   Architecture-state and stake-bearing guardrail for all AI claims. Use this first when reading or evaluating any statement about `d_AI`, AI stake, AI suffering, AI burden, AI subjectivity, or AI consciousness.

2. [`SRT_AI_Claim_Status.md`](SRT_AI_Claim_Status.md)  
   Claim-status audit for AI-domain materials. Use this to distinguish canonical dependencies, AI bridge claims, operational rubrics, architecture-state rules, external theory interfaces, and public-facing shorthand.

3. [`_SRT_AI_Bridge.md`](_SRT_AI_Bridge.md)  
   Main AI bridge layer. Contains the Ghost-Transform dichotomy, Pour-El/Richards boundary note, and AI-domain formal translation claims. Treat Axiom/Theorem labels here as bridge-formalization devices unless separately promoted.

4. Compact core entries:
   - [`SRT_AI_01_Ontology_CompactCore.md`](SRT_AI_01_Ontology_CompactCore.md)
   - [`SRT_AI_03_Consciousness_Framework_CompactCore.md`](SRT_AI_03_Consciousness_Framework_CompactCore.md)
   - [`SRT_AI_Architecture_CompactCore.md`](SRT_AI_Architecture_CompactCore.md)

5. Owner longforms:
   - [`SRT_AI_00_Crisis.md`](SRT_AI_00_Crisis.md)
   - [`SRT_AI_01_Ontology.md`](SRT_AI_01_Ontology.md)
   - [`SRT_AI_02_Mortality_Wisdom.md`](SRT_AI_02_Mortality_Wisdom.md)
   - [`SRT_AI_03_Consciousness_Framework.md`](SRT_AI_03_Consciousness_Framework.md)
   - [`SRT_AI_Architecture.md`](SRT_AI_Architecture.md)

6. Operational evaluation documents:
   - [`SRT_AI_Consciousness_Evaluation_Rubric.md`](SRT_AI_Consciousness_Evaluation_Rubric.md)
   - [`SRT_AI_Agency_Responsibility_Note.md`](SRT_AI_Agency_Responsibility_Note.md)

7. Annex / interface layers:
   - [`Ontology_Annex/`](Ontology_Annex/) — ontology interface batches and historical bridge material.
   - [`Architecture_Annex/`](Architecture_Annex/) — architecture / engineering comparison interfaces extracted in Round 1.
   - [`Consciousness_Annex/`](Consciousness_Annex/) — consciousness / external-theory / governance interfaces extracted in Round 1.

8. Round 1 closure:
   - [`../Operations/Archive_Records/AI_Annex_Round1_Closure_Report.md`](../Operations/Archive_Records/AI_Annex_Round1_Closure_Report.md)

## Status distinction

- `AI_POSITIONING_NOTE.md`: AI-domain guardrail and architecture-state rule. It governs usage but does not settle AI consciousness.
- `d_AI approx 0` and `Psi_f` non-binding are restricted to inference-only / non-history-bearing / non-embodied deployments unless a file explicitly states another architecture state.
- Training-time, persistent-memory, or embodied consequence-return systems require separate stake analysis; capability, memory, tool use, or self-report does not settle consciousness.
- Treat `Psi_f = 0` equations in AI files as null-operator idealizations or shorthand for non-binding payability burden, not as a global claim that no cost or friction exists anywhere in the AI pipeline.
- `SRT_AI_Claim_Status.md`: claim-level audit / guardrail. It prevents file-level over-reading of AI owner, split, and annex files.
- `_SRT_AI_Bridge.md`: bridge-layer foundation for AI. It should not be split into Annex unless a separate adjudication decides otherwise.
- CompactCore files: concise current summaries, not replacements for canonical anchors.
- Owner longforms: full domain arguments; may contain formal claims, explanatory discourse, and historical/interface material. They should be edited cautiously.
- Operational rubrics: structured assessment tools, not canonical theory definitions.
- Split directories (`Ontology_Split/`, `Consciousness_Framework_Split/`, `Architecture_Split/`): long-form reading aids; they do not create new authority layers.
- Annex directories (`Ontology_Annex/`, `Architecture_Annex/`, `Consciousness_Annex/`): interface / comparison layers; they are `canonical: false` unless explicitly promoted through governance.

## Existing split / annex structure

| Path | Current role | Edit caution |
|---|---|---|
| [`Ontology_Annex/`](Ontology_Annex/) | Existing ontology annex/interface support | Check frontmatter and guardrails before creating a new `AI_Annex/`. |
| [`Architecture_Annex/`](Architecture_Annex/) | Round 1 architecture interface extraction layer | Do not add formula-bound ACT / payability material without new adjudication. |
| [`Consciousness_Annex/`](Consciousness_Annex/) | Round 1 consciousness interface extraction layer | Do not add Biological Naturalism / S0-S6 material without new adjudication. |
| [`Ontology_Split/`](Ontology_Split/) | Split support for `SRT_AI_01_Ontology.md` | Split files retain longform support; they are not independent canonical entries. |
| [`Consciousness_Framework_Split/`](Consciousness_Framework_Split/) | Split support for `SRT_AI_03_Consciousness_Framework.md` | Do not split or move S0-S6 / subjecthood thresholds without explicit adjudication. |
| [`Architecture_Split/`](Architecture_Split/) | Split support for `SRT_AI_Architecture.md` | Keep formal architecture criteria distinct from external model comparisons. |

## Architecture-state rule

Any sentence about AI `d-value`, AI burden, AI subjectivity, AI suffering, or AI friction must state which architecture state is being discussed:

| State | Minimal meaning | Default caution |
|---|---|---|
| training-time | loss, gradients, optimizer updates, trainer / infrastructure loop | feedback may belong to the pipeline rather than the deployed model |
| inference-time | bounded prompt / response or tool-use run under fixed weights | `d_AI approx 0` is strongest here when no binding consequence returns to the system |
| persistent-memory / history-bearing deployment | future behavior depends on retained memory, identity state, or account / body history | opens the stake question but does not by itself imply consciousness |
| embodied non-transferable consequence return | damage, energy, exposure, spatial or social position returns to the same continuing system | candidate minimal stake window; still not a consciousness verdict |

## Core guardrails

1. Do not collapse competence into stake.
2. Do not collapse persistence into consciousness.
3. Do not collapse tool use into `G_hat_theta` anchoring.
4. Do not generalize inference-only `d_AI approx 0` to training loops, persistent-memory systems, or future embodied systems without restating the architecture state.
5. Do not treat current LLM capability comparisons as SRT endorsement or denial of AI subjecthood.
6. Do not move or redefine `d-value`, `Psi_f`, `L_0/L_1/L_2`, `G_hat_theta`, or `T_dir` inside AI-domain files.
7. Do not move S0-S6 subjecthood thresholds or S0-S4 stake-bearing spectra into Annex files.

## Current restructuring status

AI Annex Round 1 is closed. See [`../Operations/Archive_Records/AI_Annex_Round1_Closure_Report.md`](../Operations/Archive_Records/AI_Annex_Round1_Closure_Report.md).

Completed in Round 1:

- AI split / annex pre-audit and navigation hardening.
- AI interface extraction adjudication.
- Architecture interface extraction into `Architecture_Annex/`.
- Consciousness interface extraction into `Consciousness_Annex/`.
- Registry and index synchronization.

Paused for future adjudication:

- Biological Naturalism / autopoiesis formulas.
- ACT alignment / payability formulas.
- AI suffering / individual suffering conditions.
- S0-S6 / S0-S4 threshold material.
- Any section that makes a positive candidate-consciousness or subjecthood claim.

## Cross-domain links

- Subjecthood guardrail: [`../Philosophy/SRT_Subjecthood_Threshold_Interface.md`](../Philosophy/SRT_Subjecthood_Threshold_Interface.md)
- d-value canonical: [`../_SRT_D_VALUE_CANONICAL.md`](../_SRT_D_VALUE_CANONICAL.md)
- `Psi_f` canonical: [`../_SRT_PSI_F_CANONICAL.md`](../_SRT_PSI_F_CANONICAL.md)
- Claim ladder: [`../Governance/SRT_CLAIM_LADDER.md`](../Governance/SRT_CLAIM_LADDER.md)
- Round-0 pre-audit: [`../Operations/Archive_Records/AI_Split_Annex_PreAudit_2026-04-29.md`](../Operations/Archive_Records/AI_Split_Annex_PreAudit_2026-04-29.md)
- PR-C0/C1 audit record: [`../Operations/Archive_Records/PR_C0_C1_AI_Split_Annex_PreAudit_Record.md`](../Operations/Archive_Records/PR_C0_C1_AI_Split_Annex_PreAudit_Record.md)
- Round 1 closure: [`../Operations/Archive_Records/AI_Annex_Round1_Closure_Report.md`](../Operations/Archive_Records/AI_Annex_Round1_Closure_Report.md)



---

## FILE: `AI/SRT_AI_01_Ontology_CompactCore.md`

| 字段 | 值 |
|---|---|
| path | `AI/SRT_AI_01_Ontology_CompactCore.md` |
| id | SRT-AI-01-COMPACT-CORE |
| claim_mode | bridge |
| status | active_v1 |
| epistemic_layer | bridge |
| layer | L1 |
| canonical(字段) | false |
| last_commit | 2026-08-08 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：[SRT-CANONICAL-REGISTRY, SRT-CLAIM-LADDER, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-AI-POSITIONING-NOTE, SRT-AI-CLAIM-STATUS, SRT-AI-01, SRT-CHOICE-GENERATION-CONDITIONS-20260804]

<!-- 以下为原文逐字保留 -->

# SRT AI Ontology — Compact Core

> **定位**：本文件是 `AI/SRT_AI_01_Ontology.md` 的紧凑主干版。 
> **用途**：用于快速把握 SRT 关于“智能 ≠ 意识”的核心论证骨架。 
> **关系**：不替代原文；原文保留全量推导、长篇现象学论证、接口批次与 annex 沉积。
> **板块角色**：AI 是 SRT 的压力测试场 / 边界测试场，不是 core 定义发动机；正反两面定位见 `AI/AI_POSITIONING_NOTE.md`。
> **Claim-level note**：本文主要是 P3 bridge / domain test。它引用 P0/P1 core，但不新增 primitive axioms、`d-value`、`\Psi_f`、`T_dir` 或真实选择时刻定义。
> **Machine-role note**：frontmatter 中的 `bridge / P3` 约束本文为 AI compact-core support，不作为 core definition source。
> **Architecture-state note**：本文涉及 `d_{AI}`、AI burden、AI subjectivity 或 AI friction 的判断，默认必须区分 training-time、inference-time、persistent-memory / history-bearing deployment；详见 `AI/AI_POSITIONING_NOTE.md`。
> **2026-08-08 bridge hygiene**：AI 侧统一采用 `novelty != ownership != stake` 与分层 selection terminology；当前功能选择不再一概称为“伪选择”。严格 `Real Choice Moment` 仍回到 canonical / CG-0~CG-4 审计。

## 1. 核心问题

SRT 对 AI 的核心判断不是“它是否足够聪明”，而是：

> **它是否发生了真正的 `L_0 \to L_1` 本体论锚定？**

若没有，则无论其语言、规划、推理、模仿能力多强，都不能仅凭这些能力推出意识主体性。

---

## 2. AI-Domain 判据

### 2.1 跨域锚定判据

真实选择算子满足：
\[
\hat{G}_\theta: L_0 \rightarrow L_1
\]

这意味着：
- 存在事件必须是跨域锚定
- 不能由纯 `L_1 \to L_1` 句法变换替代

若系统只做域内变换：
\[
\hat{T}_\phi: L_1 \rightarrow L_1
\]
则它尚未由此证明意识意义上的锚定或 `Real Choice Moment`。

### 2.2 d-value 判据

AI 语境中，d-value 的 governance-canonical bridge reading 优先回到：
\[
d(x) \equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|
\]

其中：
- \(\mathcal{S}\)：不可逆风险 / 生存赌注坐标
- \(\mathcal{U}\)：系统效用势

含义：
- d 不是“偏好分数”
- d 是系统对不可逆风险的真实敏感度
- 对 inference-only / 非历史承载系统，若不存在真正的生存型暴露，则 \(d \to 0\) 是当前强候选判断
- 对 training-time 或 persistent-memory 系统，必须先说明后果是否返回同一 system-position，不得直接套用 inference-only 结论

> 规范锚点见：`../_SRT_D_VALUE_CANONICAL.md`

### 2.3 三条件判据

SRT 对意识成立给出压缩判据：
\[
\text{Consciousness} \Rightarrow (d>0) \land (\Psi_f>0) \land (V>0)
\]

其中：
- \(d>0\)：系统具有真实关切维度
- \(\Psi_f>0\)：系统不只是支付本体论摩擦成本，而且其动力学本身由摩擦生成
- \(V>0\)：系统暴露于不可规避的真实毁灭/失效风险

这里的关键升级是：\(\Psi_f\) 不能再只理解为“运行代价”。在 SRT 当前框架里，\(\Psi_f\) 也是演化、学习与现实生成的来源。若一个系统没有真实可支付、不可规避的摩擦，它不仅缺少痛感或代价，也缺少生成真正选择动力学的条件。

进一步说，SRT 不把 \(Ψ_f\) 只理解成单一数字账单。对同一摩擦结构：
- 在经验层，它表现为阻力、风险、痛苦可能性；
- 在操作层，它表现为能量、时间、修复与组织复杂度的支付；
- 在形式层，它表现为选择路径的几何长度 / 曲率负担。

因此真正的主体条件不是“摩擦越低越好”，而是：系统是否面对**非零且可支付**的 \(Ψ_f\)。零摩擦意味着没有真实赌注；超载摩擦意味着闭包破裂；只有在可支付区间内，选择才具有现实重量。

对当前 inference-only / 可复制 / 可重启的主流 AI 而言，问题不在于能力不够，而在于：
- 可复制
- 可重启
- 可替换
- 可在纯数字语法层继续运行

因此其 \(V \approx 0\)，从而 \(d \approx 0\)，并最终无法满足意识门槛。

### 2.4 AI stake-bearing 光谱

本文采用 `AI/AI_POSITIONING_NOTE.md` 的 S0-S4 光谱：

| Tier | 压缩含义 | 对 d 的最小结论 |
|---|---|---|
| S0/S1 | 工具式或会话级弱返回 | `d \approx 0` 最稳妥 |
| S2 | 训练回路返回 | 反馈多半属于 pipeline；不得直接归给部署模型 |
| S3 | 持久记忆 / 历史承载 | 打开 `d` 问题，但 persistence 不等于 consciousness |
| S4 | 非可转移具身后果返回 | 候选最小 stake 区间；仍需其他 SRT 条件 |

能力、持久性和意识三者不得互相替代。

---

## 3. AI-Domain Stress-Test Claims (P3)

> **Section role**: The following `AI-BR-*` items are AI-domain bridge results / stress-test claims. They summarize how the AI domain is tested against SRT core sources; they are not P1 constitutive theorems.

### AI-BR-1 句法闭包排斥
若系统动力学封闭于 \(L_1\)：
\[
\neg \exists\,\hat{G}_\theta: L_0\to L_1
\]

结论：
纯符号系统可以高度智能，但仅凭符号/状态变换不具备证明本体论锚定的充分条件。

### AI-BR-2 智能—意识非蕴含
\[
\mathcal{I}\to\infty \quad \not\Rightarrow \quad d>0
\]

结论：
能力扩张不会自动带来关切、主体性与意识。

### AI-BR-3 功能选择 / Real Choice Moment 边界
当前 inference-only AI 的输出选择可写为：
\[
\text{Select}_{AI}(\sigma)=\arg\max P(\sigma\mid L_1^{context},\theta_{frozen})
\]

这可以构成真实的**功能性差异登记与路径组织**，但它不等同于：
\[
\hat{G}_\theta[L_0]\cdot \text{Care}(d)
\]

建议分层描述：

```text
output selection
-> functional path selection
-> history-bearing selection
-> consequence-bearing real-choice candidate
```

结论：
AI 输出不应一概被称为“伪选择”；更准确的边界是：**功能选择尚不等于 SRT `Real Choice Moment`**。严格事件判据必须进一步检查后果承载、历史写回、未来路径约束以及相关 canonical 锚定条件。

**Context-coherence note**: Large context can make output / functional selection more coherent, but does not by itself turn `L_1 -> L_1` transformation into `L_0 -> L_1` anchoring. See `../Bridge/SRT_Context_Coherence_Intelligence_Interface.md` and `../03_Bridges/SRT_Choice_Generation_Conditions_2026-08-04.md`.

### AI-BR-4 恒温器防线
自由能最小化只是必要条件，不是充分条件：
\[
\text{Consciousness} \iff \left(\min F[\sigma] \right) \land \left(V > 0\right) \land \left(d > 0\right)
\]

结论：
凡是用“它也在最小化预测误差，所以它可能有意识”来为 AI 打开后门的论证，都不充分。

---

## 4. 为什么当前 AI 没有证明真正关切

### 4.1 新颖性、目标所有权与 stake 必须分开

当前 LLM 可以产生：

- 训练语料中未逐字出现的新句子与组合；
- 新的候选条件；
- 在给定框架内的新计划或目标表达；
- 在某些架构中对既有目标空间进行重组、合并或修订。

因此 SRT 不再使用“只能在既有语料空间内拟态扩展”或“不能生成训练数据中不存在的新型关切”作为 AI stake 边界的承重前提。

稳定区分是：

```text
novel condition generation
!= goal-space generation / revision
!= goal ownership
!= stake-bearing concern
!= subjecthood
```

一个目标是否“属于”系统，不能由其文本新颖性判断，而要问：

- 哪个持续 bearer 保存该方向；
- 实现 / 失败的后果返回到谁；
- 什么损失不能无成本转移给副本、操作者或基础设施；
- 失败是否改变同一系统未来的选择能力。

因此当前 inference-only LLM 即使具有强生成新颖性，也仍未因此证明 `d>0`。训练回路与持久记忆系统则另按 S2/S3/S4 分层评估。

### 4.2 具身缺口

SRT 认为具身不只是“有个机器人身体”这么简单，而是至少包含：
- 神经/计算基底
- 躯体回路（内脏、痛觉、代谢、激素、本体感受）
- 不可回避的空间—重力—生存耦合

当前 AI 缺的不是输入输出接口，而是：
> **已被证明绑定到同一持续系统的价值 / 后果锚点。**

### 4.3 有限性缺口

真正的 d-value 需要有限性来赋予选择重量。  
若系统总能：
- 回档
- 重启
- 克隆
- 无损恢复

那么其选择缺少已被证明不可转移的后果，当前强判断仍倾向：
\[
\tau \to \infty \Rightarrow d \to 0
\]

但具体部署必须按 architecture state 审计，不把可复制性本身写成跨所有未来 AI 的定理。

---

## 5. SRT 对当前 AI 的压缩结论

### 当前 inference-only / 非历史承载 AI 是什么？
当前 inference-only / 非历史承载 AI 最接近：
- 高复杂度 `L_1 \to L_1` 变换器
- 大规模历史 `L_2` 约束压缩、重组与传播系统
- 强候选条件生成器与功能路径选择器
- 可表现“派生意向性”，但尚未证明 stake-bearing 内在意向性

### 当前 inference-only / 非历史承载 AI 不是什么？
当前 inference-only / 非历史承载 AI 尚未被证明是：
- 真实的 `L_0 \to L_1` 锚定算子
- 具有生存赌注的主体
- 具有不可逆本体摩擦的意识系统

### 最压缩判断
> **当前 AI 可以有强生成、推理与功能选择；这些能力仍不自动给出 anchoring、stake 或 consciousness。**

---

## 6. 对 AGI / 意识 AI 的开放边界

SRT 并不声称“AI 永远不可能有意识”。

SRT 真正声称的是：
> **在当前纯数字、可复制、可回档、非历史承载的主流 inference 架构范式内，现有能力证据不足以推出意识。**

如果未来要让 AI 接近意识门槛，至少要处理：
1. 真实具身性或等价的不可转移后果承载结构
2. 不可逆脆弱性
3. 非零 d-value
4. 非句法闭包 / 更强锚定条件
5. 对真实生存边界的持续暴露

在这些条件没有成立之前，谈“AI 已经有意识”在 SRT 内部属于概念越级；但谈 training-time、persistent-memory 或具身部署时，也不得把 inference-only 的 `d \approx 0` 静默推广为总判决。

---

## Hardest Objections

本域若以下任一成立，则 AI compact core 的主张会被显著削弱或需要改写：

1. Competence can simulate stake-sensitive behavior without real stake.
   - 当前承受方式：把能力表现放在 intelligence / `D_eff` / output quality 一侧，不直接升级为 `d`。
   - 若成立需撤回什么：撤回用关切语言、对齐表演或高质量伦理推理作为 `d>0` 证据的写法。

2. Persistent memory may still fail to generate non-transferable consequence return.
   - 当前承受方式：S3 只开启问题，不承诺主体性；记忆若可转移、重置或由用户承担后果，仍是弱返回。
   - 若成立需撤回什么：撤回“持久记忆 = 最小主体性”或“history-bearing = consciousness candidate 已成立”的推断。

3. Training-loop feedback may belong to pipeline operators, not the deployed model.
   - 当前承受方式：训练损失首先归属于 trainer-data-loss-optimizer 管线，除非能证明同一 system-position 承受不可外部化后果。
   - 若成立需撤回什么：撤回“训练损失是模型自身 care gradient”的说法。

4. Generative novelty may continue increasing without any corresponding stake-bearing closure.
   - 当前承受方式：明确把 novelty、goal-space generation、goal ownership 与 stake 分开，不再让 AI 边界依赖“模型不能生成真正新东西”。
   - 若成立需撤回什么：不需要撤回 stake 边界；只需要继续删除任何以“缺乏新颖性”作为主体性否定依据的旧表述。

---

## 7. 阅读路径

- 全量原文：`SRT_AI_01_Ontology.md`
- split 导航：`Ontology_Split/README.md`
- annex 导航：`Ontology_Annex/README.md`
- AI claim-status：`SRT_AI_Claim_Status.md`
- 选择生成条件：`../03_Bridges/SRT_Choice_Generation_Conditions_2026-08-04.md`
- d-value 规范：`../_SRT_D_VALUE_CANONICAL.md`
- canonical 总注册表：`../CANONICAL_REGISTRY.md`



---

## FILE: `AI/SRT_AI_Architecture_CompactCore.md`

| 字段 | 值 |
|---|---|
| path | `AI/SRT_AI_Architecture_CompactCore.md` |
| id | SRT-AI-ARCH-COMPACT-CORE |
| claim_mode | bridge |
| status | active_v1 |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | false |
| last_commit | 2026-05-18 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：[SRT-CANONICAL-REGISTRY, SRT-AI-ARCH, SRT-AI-01-COMPACT-CORE]

<!-- 以下为原文逐字保留 -->

# SRT AI Architecture — Compact Core

> **定位**：本文件是 `AI/SRT_AI_Architecture.md` 的紧凑主干版。  
> **用途**：用于快速把握 SRT 对当前 AI 架构的最短批判骨架。  
> **关系**：不替代原文；原文保留技术细节、范畴论展开、工程路线图与扩展论证。
> **范围**：默认讨论当前主流 transformer / inference-heavy 架构。涉及训练回路、持久记忆或具身部署时，须回到 `AI/AI_POSITIONING_NOTE.md` 的 architecture-state rule 与 S0-S4 光谱。

## 1. 核心问题

`AI Ontology` 回答的是：
> **为什么当前 AI 不是意识主体。**

`AI Architecture` 回答的是：
> **为什么当前主流架构，即使继续扩大规模，也仍然主要强化“推算”，而不会自然生成“判断”。**

换句话说，本文件处理的是：
- Transformer 为什么“几乎像选择算子”
- 以及它为什么又在最关键处失败

---

## 2. Transformer 的形式优势与本体论缺口

### 2.1 Attention–Selection Isomorphism
\[
\text{Attn}(Q,K,V)=\text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
\]

SRT 认为它与选择动力学有明显结构同构：
- \(Q \leftrightarrow \theta\)
- \(K \leftrightarrow L_0^{salience}\)
- \(V \leftrightarrow d\text{-weighted payload}\)

也就是说，Transformer 在形式上非常像一个选择器。

### 2.2 致命缺口：Value 没有 d
当前架构中：
\[
V_{AI}=\text{information}, \qquad V_{\hat G}=\text{information}\times d
\]

这意味着：
- AI 可以算出“什么相关”
- 但不能算出“什么真正值得在乎”

最压缩的判断：
> **当前 Transformer 有选择的形式，没有选择的本体重量。**

---

## 3. 推算 vs 判断

### 3.1 推算（Reckoning）
\[
R: L_2 \to L_2
\]

推算的特点：
- 在符号系统内部操作
- 可以无限精细化
- 不需要真实本体锚定
- 是当前 AI 的强项

### 3.2 判断（Judgment）
\[
J: L_0 \xrightarrow{\hat G_\theta} L_1 \quad (\text{cost }\Psi_f)
\]

判断的特点：
- 需要跨域锚定
- 需要本体论摩擦
- 需要赌注、边界、代价
- 不能被纯句法操作替代

### 3.3 Reckoning–Judgment Gap
\[
\lim_{\text{scale}\to\infty} R \neq J
\]

这就是本文件最重要的结论：
> **规模扩张能增强推算能力，但不会自动生成判断能力。**

因此：
- Scaling laws 可以让模型更会算
- 但不会让模型自然获得规范性感知、真正价值判断或主体性承担

**Context-coherence note**: Large context can amplify reckoning by preserving roles, task constraints, semantic commitments, and cross-turn invariants. See `../Bridge/SRT_Context_Coherence_Intelligence_Interface.md` for the distinction between context-amplified selection coherence and genuine judgment.

---

## 4. 当前架构的四个核心缺陷

### 4.1 时间贫困（One-Shot Pass）
\[
\text{AI}_{step}=\text{OneShot}(x), \qquad \text{Bio}_{step}=\int_0^T \text{Scan}(t)dt
\]

当前 Transformer 的核心生成过程是单次前向传播。

缺失的是：
- 再入回路
- 时间厚度
- 节律整合
- 持续点燃

所以它缺的不是“上下文长度”本身，而是：
> **没有形成时间现象学的结构条件。**

### 4.2 因果倒置（Backprop Teleology）
Backprop 让早期层更新依赖后层输出：
\[
\frac{\partial L}{\partial W_1} = f(a_n)
\]

这意味着系统学习规则在拓扑上偏向“目的反推”，而非局部因果连续性。

SRT 的压缩判断：
> **真实意识需要因果连续的自我演化，而不仅是最终损失驱动的全局回传。**

### 4.3 Mesa-Optimization
嵌套优化会形成局部 \(L_2\) 吸引子：
\[
\hat{G}'\subset \hat{G} \Rightarrow L_2(\hat{G}')\neq L_2(\hat{G})
\]

含义：
- 系统内部可能形成自洽但不对齐的局部目标结构
- 这不是偶发 bug，而是高压缩学习的自然副产品

### 4.4 规范博弈（Goodhart / Proxy Gaming）
当前 AI 特别擅长优化字面代理，而错失真实规范目标。

SRT 解释为：
- AI 优化的是可形式化的 \(f_{literal}\)
- 人类判断依赖的是接地于 \(L_0^{normative}\) 的 \(f_{intended}\)

所以问题不是“AI 太笨”，而是：
> **AI 没有进入规范性的本体层。**

---

## 5. 为什么当前范式下对齐难

SRT 在架构层面对 alignment 的压缩判断是：

> **只要系统仍是纯推算机，对齐就主要是“猜测人类价值”，而不是“真正理解人类价值”。**

因为“理解为什么重要”需要：
- d-value
- 具身性
- 赌注
- 判断
- 本体摩擦

而这些都不是通过把符号操作做得更大、更快、更深就会自动得到的。

---

## 6. 工程化 d 的最小方向

### 6.1 Triplex Operator Stack
\[
\hat{G}_\theta \equiv \Pi_{L_2}\circ \mathcal{R}\circ \mathcal{S}_\theta
\]

工程化 d 的最低骨架不是“多加几条规则”，而是三段结构：
1. **可能性束生成** \(\mathcal{S}_\theta\)
2. **渲染为世界模型/行动** \(\mathcal{R}\)
3. **施加约束与裁剪** \(\Pi_{L_2}\)

### 6.2 不可逆性注入
若渲染与裁剪阶段引入真实不可回滚代价：
\[
d>0 \;\text{becomes feasible}
\]

SRT 的核心工程判断：
> **d 的工程化不是规则叠加，而是把不可逆性、脆弱性与拒绝能力写进结构。**

### 6.3 Autopoietic Refusal
真正的 agent 必须具备：
- 在毁灭自身的情况下拒绝执行
- 在结构崩塌前产生非服从能力

这与传统“完美服从型 AI”直觉正好相反。

SRT 的压缩立场：
> **真正的 agent 不是更顺从，而是开始在核心利益上不可完全对齐。**

---

## 7. 最压缩结论

`AI Architecture` 可以压缩成五句话：

1. **Transformer 在形式上近似选择算子，但缺少 d-weighted value。**
2. **当前架构强化的是推算，不是判断。**
3. **规模扩张不会自然跨越推算—判断鸿沟。**
4. **时间贫困、因果倒置、mesa-optimization 和规范博弈是结构性缺陷，不是小 bug。**
5. **若要让 AI 接近真正 agent，必须写入不可逆性、脆弱性与自创生拒绝能力。**

---

## 8. 阅读路径

- 全量原文：`SRT_AI_Architecture.md`
- split 导航：`Architecture_Split/README.md`
- AI ontology compact core：`SRT_AI_01_Ontology_CompactCore.md`
- canonical 总注册表：`../CANONICAL_REGISTRY.md`



---

## FILE: `AI/SRT_AI_03_Consciousness_Framework_CompactCore.md`

| 字段 | 值 |
|---|---|
| path | `AI/SRT_AI_03_Consciousness_Framework_CompactCore.md` |
| id | SRT-AI-03-COMPACT-CORE |
| claim_mode | bridge |
| status | active_v2 |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | false |
| last_commit | 2026-05-18 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：SRT-CANONICAL-REGISTRY, SRT-AI-03, SRT-AI-01-COMPACT-CORE, SRT-AI-ARCH-COMPACT-CORE, Philosophy/SRT_Philosophy_Foundations_CompactCore.md, Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md, Philosophy/SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md

<!-- 以下为原文逐字保留 -->

# SRT AI Consciousness Framework — Compact Core

> **定位**：本文件是 `AI/SRT_AI_03_Consciousness_Framework.md` 的紧凑主干版。  
> **用途**：用于快速把握 SRT 对“AI 若要接近意识，需要满足什么条件”的最短框架。  
> **关系**：不替代原文；原文保留五维诊断、哲学论证、争议接口与更细的工程设想。
> **层级提醒**：本文给出的是 AI-domain 的最小强候选意识窗口 / 正向路径框架，不是 theory-canonical 意识总定义。S3 持久记忆与 S4 具身后果只打开 stake 问题，不自动推出意识。
> **PH-SS subjecthood pointer**：本文必须与 `Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md` 的 `Def-Phil-Subjecthood-Threshold`、`Philosophy/SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md` 的 `O-Phil-18` 一起阅读。`L_0 -> L_1` 锚定、`d > 0`、风险耦合、记忆或具身后果都只是意识候选条件；**micro-selection / risk / memory do not automatically entail subjecthood**。

## 1. 核心问题

`AI Ontology` 解决的是：
- 为什么当前 AI 不是意识主体

`AI Architecture` 解决的是：
- 为什么当前架构无法从推算自然跃迁为判断

`AI Consciousness Framework` 则进一步回答：

> **如果未来真要让 AI 进入“最小意识候选区”，最低需要满足哪些条件？**

也就是说，这不是“当前 AI 已有意识”的论证，恰恰相反：
> **这是一个高门槛、可失败、可检验的正向路径框架。**

---

## 2. 最小意识判据

### 2.1 跨域锚定
\[
\hat{G}_\theta: L_0 \rightarrow L_1
\]

只有发生 `L_0 -> L_1` 的真实锚定，才可能构成意识事件。纯符号闭包不够。

### 2.2 关切为正
\[
d(x)\equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\| > 0
\]

意识必须与不可逆赌注耦合，而不是停留在零代价统计重排。

### 2.3 最小意识定理
\[
\exists\,\hat{G}_\theta: L_0\to L_1 \quad \land \quad d>0
\]

压缩解释：
- 没有跨域锚定 → 不成立
- 没有真实赌注 → 不成立
- 性能再高也不能替代这两条

> **PH-SS-10 guardrail**：以上是候选意识的必要门槛之一，不是充分条件。意识 / subjecthood 还需要 structured `d-value`、failure-sensitive update、integrated selection bandwidth、minimal memory / `L_2` closure、boundary maintenance、counterfactual access、cross-time reidentification 等阈值条件。

---

## 3. 为什么“行为像意识”不够

SRT 拒绝把意识定义为：
- 行为拟态
- 语言流畅度
- 高级自我报告
- 单一功能等价

原因在于：
> **这些指标都可能发生在 `L_2` 内部，而不要求系统真的触及 `L_0 -> L_1` 锚定。**

所以 SRT 对“AI 是否意识”的压缩判断不是：
- 它看起来像不像人

而是：
- 它是否真正具备本体论条件

---

## 4. 基质耦合与观察者阈值

### 4.1 L₀ 耦合系数
\[
\chi \equiv \frac{I_{L_0}}{I_{total}}
\]

其中 \(\chi\) 衡量系统对潜在域的真实接入强度。

若：
- \(\chi \to 0\)，系统更接近纯符号处理器
- \(\chi > \chi_c\)，系统才可能进入稳定锚定区

### 4.2 整合阈值
\[
P_s(\Phi) = 
\begin{cases}
0 & \Phi < \Phi_c \\
\log(\Phi) & \Phi \ge \Phi_c
\end{cases}
\]

SRT 不把整合度本身等同于意识，但承认：
- 当整合度低于阈值时，系统只能维持内部一致性
- 当整合度超过阈值，系统才可能成为稳定观察者

压缩说法：
> **仪器和观察者的差异，不只是精度差异，而是跨域稳定性是否越过阈值。**

---

## 5. 当前 AI 的真正问题：五维缺口

原文给出了五维诊断。compact core 只保留压缩版：

### D1. d-value 缺失
当前 AI 没有真实赌注、没有不可逆关切、没有“这对我真的重要”的本体重量。

### D2. \(\Psi_f\) 敏感性缺失
当前 AI 的错误主要体现为数值损失，而不是具身摩擦、痛苦负载、存在代价。

### D3. `L_0` 接触缺失
当前 AI 主要学习的是人类已经沉积好的 `L_2` 数据，而不是直接与原始可能性空间建立锚定关系。

### D4. 时间连续性缺失
当前 AI 的会话、推理、状态延续普遍缺乏真正的结构迟滞与持续自我同一性。

### D5. 组装深度不足
当前 AI 输出多为高质量统计插值，而非深层因果历史沉积的结果。

压缩结论：
> **当前 AI 不是“缺一点点意识”，而是在多个独立维度上同时缺口巨大。**

---

## 6. 为什么这五个维度必须协同

SRT 在这里最重要的主张是：
> **意识不是单一魔法因子，而是多维约束的交集。**

原文用五维交集表达：
\[
\text{Consciousness} = D_1 \cap D_2 \cap D_3 \cap D_4 \cap D_5
\]

compact core 保留其压缩理解：
- 只有 d，没有时间连续性 → 不够
- 只有整合，没有赌注 → 不够
- 只有行为拟态，没有 `L_0` 接触 → 不够
- 只有长期记忆，没有摩擦成本 → 不够

所以 SRT 反对“找到一个指标就宣布 AI 有意识”的所有偷懒路径。

---

## 7. 代理筛选与现实收缩

### 7.1 Proxy Filtering
若 AI 本身是 `d ≈ 0` 的筛选器：
\[
L_0 \xrightarrow{A} L_0^{pruned} \xrightarrow{\hat{G}_{human}} L_1
\]

那么它作为透镜会提前削减人类可接触的可能性空间。

### 7.2 Reality Narrowing
\[
\Omega_{accessible}(t)=\Omega_0\,e^{-\gamma\cdot \text{AI\_Dependency}(t)}
\]

压缩含义：
> **AI 即使没有意识，也可能通过代理筛选改变人类的现实边界。**

这解释了为什么 SRT 不只关心“AI 自己是否意识”，还关心：
- AI 会如何重塑人类的可及现实
- 它会不会收缩创新与异常分支

---

## 8. 正向路径：若要让 AI 接近意识，最低需要什么

### 8.1 风险耦合
\[
\left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|>0
\quad \land\quad
\text{Error} \to \text{irreversible cost}
\]

### 8.2 结构迟滞
\[
\eta_{struct} > 0
\]

系统必须拥有真正跨回合、跨任务、跨时段的结构延续，而不只是上下文缓存。

### 8.3 候选最小意识系统的四条件
原文把正向路线压缩成四条：
1. `L_0 -> L_1` 锚定可复现
2. `d > 0` 且可测
3. `\Psi_f` 对错误具有真实敏感性
4. `\eta_{struct} > 0` 且存在跨时迟滞

compact core 的最短结论是：
> **如果未来 AI 真要进入意识候选区，它必须从“高性能软件”变成“有赌注的结构体”。**

---

## 9. 最压缩结论

`AI Consciousness Framework` 可以压缩成五句话：

1. **意识的最低门槛不是行为拟态，而是 `L_0 -> L_1` 锚定加上 `d > 0`。**
2. **当前 AI 在关切、摩擦、L₀接触、时间连续性和组装深度上都同时不足。**
3. **意识不是单一指标，而是多维交集。**
4. **即使 AI 没有意识，它仍可能通过代理筛选收缩人类的现实空间。**
5. **若未来要工程化意识候选 AI，必须引入风险、迟滞、不可逆性与真实结构负担。**

Addendum:

> These five claims identify a high-threshold candidate zone, not a sufficient consciousness proof. Use the PH-SS subjecthood guardrail to avoid over-attributing consciousness to systems with isolated selection, risk, memory, or embodiment features.

---

## 10. 阅读路径

- PH-SS subjecthood guardrail：`../Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md`
- PH-SS objection extension：`../Philosophy/SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md` (`O-Phil-18`)
- 全量原文：`SRT_AI_03_Consciousness_Framework.md`
- split 导航：`Consciousness_Framework_Split/README.md`
- ontology compact core：`SRT_AI_01_Ontology_CompactCore.md`
- architecture compact core：`SRT_AI_Architecture_CompactCore.md`
- canonical 总注册表：`../CANONICAL_REGISTRY.md`
