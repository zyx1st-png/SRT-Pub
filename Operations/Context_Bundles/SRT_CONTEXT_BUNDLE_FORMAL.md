---
id: SRT-CONTEXT-BUNDLE-FORMAL-2026-11-28
type: context_bundle
status: active
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
generated: 2026-11-28
source_commit: 4308fe99a
source_branch: errata/math-hard-errors-20261128
source_dirty: false
inputs_digest: 8634979bfd7f12e6
---

# SRT Formal 主方程上下文包

> **这是什么**：由 `scripts/build_srt_context_bundles.py` 从 SRT 仓库自动拼装的上下文包。
> 收录 `Core/SRT_Core_22_Equations.md` 主动力学、热力学与桥接方程正文，作为从默认 `SPINE` 分流出的独立形式方程路线（定义裁定仍回 `SPINE`）。
>
> **这不是什么**：不是新的 canonical 文件，不是摘要，不是改写。每个来源文件的正文
> 逐字保留；脚本只把 YAML frontmatter 转成显式 provenance 头。**若本包与仓库中的
> 来源文件冲突，以仓库为准**——本包是快照，会随仓库演进而过期。

## §0 生成信息

| 项 | 值 |
|---|---|
| 生成日期 | 2026-11-28 |
| 来源 commit | `4308fe99a` |
| 来源分支 | `errata/math-hard-errors-20261128` |
| 生成时来源工作树有改动 | 否 |
| 包含文件数 | 1 |

> **provenance 契约**：真实性判据是 `inputs_digest`——生成脚本、护栏来源
> （`Governance/SRT_DOWNSTREAM_GUARDRAILS.md`、两份审计）、全部正文文件与 `SPINE §0.5` 索引抽取源（`Core_22` / `Core_21c`）的联合内容摘要。`--check` 重算并比对该摘要，
> 因此改动其中任何一项都会被发现。
>
> `source_commit` 仅供参考，**不作为校验条件**：squash / rebase 合并会重写或丢弃该
> commit，若拿它做祖先校验，合并进 main 之后检查必然失败。内容摘要与合并策略无关。

### 0.1 文件清单与各自最后改动日期

| # | 文件 | 最后 commit |
|---|---|---|
| 1 | `Core/SRT_Core_22_Equations.md` | 2026-11-28 |

## §0.2 状态护栏

> **这些是本包正文里读不出来的信息。** 正文中相关命题写得像已经成立，
> 而仓库自己知道它们没有。回答前先读本节。
>
> **每条护栏分三段，权威等级不同，请分别对待**：
>
> - **SOURCE EXTRACT** — 从 `Operations/` 审计台账与 `Governance/SRT_DOWNSTREAM_GUARDRAILS.md` 按锚点逐字抽取的原文。
>   锚点若失效，生成脚本直接失败而不会产出缺护栏的包。
> - **GENERATED INTERPRETATION** — **生成器的归纳，不是来源原文**。它压缩了上面的抽取内容，
>   可能丢失限定条件。有疑问时以 SOURCE EXTRACT 为准，再有疑问回查来源文件。
> - **USAGE POLICY** — 由标注的治理文件授权的使用规则。

### G1 — former P1-T07 已降阶；条件证明负担仍开放（严重度：高）

**受影响**：`Core/SRT_Core_21b_Constitutive_Theorems.md` 的 former P1-T07 absorption remainder，及 `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13` 的 conditional anti-closure candidate

#### SOURCE EXTRACT — 来源原文（逐字抽取）

**ST-A canonical 裁决，来自 `Core/SRT_Core_21b_Constitutive_Theorems.md`**：

> **Decision record (ST-A, 2026-08-11)**: The former unconditional statement—"every stable ISP necessarily contains an anti-closure `ε` bias"—is no longer a P1 theorem. Its proof inferred cumulative absorption from a per-step nonzero closure probability without independently defining a neutral kernel, fixing the stability semantics, or proving that the neutral kernel reaches the absorbing state. `L_0` irreversibility alone does not supply those missing premises.

**审计 1.3 修订的语义分层条款，来自 `Operations/Audits/SRT_P1_T07_PROOF_HARDENING_AUDIT.md`**：

> (a) `τ<∞` verdicts stratified by semantics — on a realized terminating history only **S1 pathwise** stability fails; **S2** fails only if `P(τ<∞)>0`, **S3** only if `P(τ=∞)=0`; no unconditional *process-level* stable-ISP verdict before the S1/S2/S3 choice (fixed in §0 Q5, §8, Proof Gate)

#### GENERATED INTERPRETATION — 生成器归纳（**非**来源原文）

ST-A 已经吸收旧审计结果：former P1-T07 不再是 P1 theorem。P1 只保留 realized history 到达吸收态后不能自行继续的 remainder，以及 P1-T06 continued selectability。neutral-kernel anti-closure 留在 P2/P3，仍须独立定义 neutral kernel、选择 S1/S2/S3 稳定语义，并声明环境、外部重置规则、终止条件与时间窗，再证明吸收或比较性 closure risk。

该降阶与剩余证明负担已登记在 `Core/SRT_OPEN_TENSIONS.md`。

#### USAGE POLICY — 使用规则

*授权依据：`Governance/SRT_CLAIM_LADDER.md`（P0–P5 阶梯）与 `SRT_AI_START.md` §14 / §15*

- 不得把 former P1-T07 当作已证 P1 定理引用；P1 引用仅限 absorption remainder。
- Stable ISP 的 P1 最低条件是 continued selectability；generative reselectability 与 ISP-level anti-closure 按 P2/P3 conditional candidate 引用。
- 关于 `τ<∞` 只能作**语义分层**的陈述：若某条 realized history 满足 `τ<∞`，可无条件断言的仅是**该历史上的 S1 / pathwise stability 失败**；process-level 的 S2 需 `P(τ<∞)>0`，S3 需 `P(τ=∞)=0`。**在 S1/S2/S3 语义未选定之前，不得据此推出无条件的 process-level 「not a stable ISP」。**
- 不要假装 `ε-neutral` 已有形式定义，也不要从 `ε_pg`、irreversibility、fixed point、metastability 或 `σ<1` 单独推出 anti-closure。


### G2 — `d`/`q`/`o` 三轴处于禁运状态（严重度：中）

**受影响**：`_SRT_D_VALUE_CANONICAL.md` 的 `d` 定义，以及任何涉及 `q` / `o` 的表述

#### SOURCE EXTRACT — 来源原文（逐字抽取）

**来自 `Governance/SRT_DOWNSTREAM_GUARDRAILS.md` §G-DQO**：

> 已加下游护栏：符号重命名与 `q` / `o` 的形式选择做出前，`d/q/o` 不得进入书稿、公共内容、bridge 或论文。

#### GENERATED INTERPRETATION — 生成器归纳（**非**来源原文）

2026-07-23 至 07-25 的三份对话材料提出具身位重写与 `d`/`q`/`o` 三轴，台账记录为**全部路由为候选，无一落地**。已知触雷点包括：`d` 取参与率与 `Def-d-canonical` 的范数定义冲突；`q` 的五个成分中两项落在 `Def-w_i` 的 `C_i` 定义文字内。

本包所含 canonical 正文**不含** `d/q/o` 内容——这是正确状态，不是遗漏。

#### USAGE POLICY — 使用规则

*授权依据：`Governance/SRT_DOWNSTREAM_GUARDRAILS.md` §G-DQO 所记的 2026-07-25 下游护栏裁决*

- 不要从外部对话材料把三轴引入回答。
- 不要据此改写 `d` 的定义。
- 禁运范围按上述原句：书稿、公共内容、bridge、论文。


### G3 — 历史 hook 闭环快照（2026-07-25）与现行未落地回写核验（严重度：中）

**受影响**：2026-07-25 历史快照所列阻塞目标；仅当对应 hook 实时 `landing_ledger` 仍为 `pending` 时，目标正文才仍未吸收该笔回写

#### SOURCE EXTRACT — 来源原文（逐字抽取）

**来自 `Operations/Audits/Hook_Closure_Audit_2026-07-25.md` 的 2026-07-25 历史审计快照 partial / pending 行（逐字，不代表当前实时状态）**：

> | Hook | 声明状态 | 实际 | 判定 |
> |---|---|---|---|
> | `PH_AG02_Reasoning_Bias` | active_v0_1 | agency 主文已落地；`T_dir` canonical **未落地** | partial |
> | `PH_AG03_Constitutive_Commitment` | active_v0_1 | agency 主文已落地；`T_dir` canonical **未落地** | partial |
> | `PH_SEM01_Bilateral_Incompatibility` | active_v0_1 | agency 主文已落地；`Occlusion_Dynamics` **未落地** | partial |
> | `P03_Cosmological_Principle` | pending | target 文档**从未创建** | pending（planned target） |
> | `P04_Spontaneous_Collapse_Classicality` | pending | target 文档**从未创建** | pending（planned target） |
> | `P05_Quantum_Proper_Time_Optical_Clocks` | pending | target 文档**从未创建** | pending（planned target） |

#### GENERATED INTERPRETATION — 生成器归纳（**非**来源原文）

按 `2026-07-25` 历史审计快照的**阻塞目标**分组如下（分组由脚本从上表解析得出，非手写摘要）：

| 阻塞目标（2026-07-25 快照） | hook 数 | hooks |
|---|---:|---|
| `T_dir` 回写未落地 | 2 | `PH_AG02_Reasoning_Bias`, `PH_AG03_Constitutive_Commitment` |
| `Occlusion_Dynamics` 回写未落地 | 1 | `PH_SEM01_Bilateral_Incompatibility` |
| planned target 从未创建 | 3 | `P03_Cosmological_Principle`, `P04_Spontaneous_Collapse_Classicality`, `P05_Quantum_Proper_Time_Optical_Clocks` |

三张 pending 的 target 文档 `Physics/SRT_Physics_Bridge_v0_2.md` 至今从未创建。改 canonical 主定义属 `Governance/SRT_EDIT_PROTOCOL.md` C 类高风险编辑，须作者授权，ledger 记 `blocked_by: canonical freeze`。

**历史快照 vs 实时状态分界**：上表是 `2026-07-25` 闭环审计快照，不自动等同于当前仍未落地。逐张 hook 的实时落地状态以对应 hook 文件 frontmatter 的 `landing_ledger` 与 `scripts/check_hooks.py` 为准——其中 `PH_AG02` / `PH_AG03` 对 `_SRT_T_DIR_CANONICAL.md` 的负面判据补注已于 `2026-08-11` 落地（见 `_SRT_T_DIR_CANONICAL.md §3.1`，两张 hook 仍为 `partial` 仅因停驻的 ChoiceMap 孵化目标保持 `pending`）；`PH_SEM01 -> Core_Law/SRT_Occlusion_Dynamics.md` 及三张 Physics planned target 则仍未落地。

#### USAGE POLICY — 使用规则

*授权依据：`Governance/SRT_EDIT_PROTOCOL.md`（C 类编辑）与 `Operations/_SRT_MATERIAL_PIPELINE.md` §5.6.1（ledger 契约）*

- 上表为 `2026-07-25` 历史快照，**不得仅凭该历史表无条件断言某目标当前仍未落地**；判断现行吸收状态须核对对应 hook 的实时 `landing_ledger` 与目标 owner 正文。
- 仅当对应 hook 的实时 `landing_ledger` 对该目标仍记为 `pending`（如 `PH_SEM01 -> Core_Law/SRT_Occlusion_Dynamics.md`）时，按对应正文尚未吸收该笔回写处理。
- 各阻塞目标彼此独立：不要把某一目标的缺口范围套用到另一个上。
- 不要把 planned-but-never-created 的 target（如 `Physics/SRT_Physics_Bridge_v0_2.md`）当作已存在的文件引用。


### G5 — 部分理论节点未进入活跃层；已进入的多数仍未经有界重复行为验证（严重度：中）

**受影响**：下表所列节点；未达到 `effectively_assimilated` 的节点在默认读取路径上仍存在结构或行为验证缺口

#### SOURCE EXTRACT — 来源原文（逐字抽取）

**来自 `Operations/Audits/data/srt_active_theory_nodes.json`（逐条抽取派生状态非 `effectively_assimilated` 的节点）**：

> | node_id | Axis A 结构 | Axis B 行为 | 快速层 | 作者门 |
> |---|---|---|---|---|
> | `NODE-SELECTION-ONTOLOGY` | active_complete | untested | — | — |
> | `NODE-L0-L1-L2` | active_complete | untested | — | — |
> | `NODE-D-VALUE` | author_gate | not_applicable | — | RQ-2026-08-A02: whether q is an independent axis or a post-stake-gate depth profile (q symbol deferred pending R5 residual tests; colliding 2026-07-23/24 draft glyphs remain embargoed; bare scalar o retired in R4-A) |
> | `NODE-PSI-F` | active_complete | untested | — | — |
> | `NODE-T-DIR` | active_complete | untested | — | — |
> | `NODE-GHOST-OPERATOR` | active_complete | untested | — | — |
> | `NODE-SUBJECTHOOD` | active_complete | untested | — | — |
> | `NODE-NEURAL-DECODABILITY` | active_complete | observed (bounded) | `Neuroscience/SRT_Neural_Mechanisms_CompactCore.md` | Whether Neuroscience/SRT_Neuroscience_Hardening_N1_N12_v0_2.md is created at all, or NEURAL18/21/22 retarget the compact core |
> | `NODE-LIFE-DISSIPATIVE` | active_complete | untested | `03_Bridges/SRT_Selection_Event_CompactCore.md` | — |
> | `NODE-PHYSICS-MEASUREMENT` | active_complete | observed (bounded) | — | RQ-2026-08-A04: P03/P04/P05 land in a new SRT_Physics_Bridge_v0_2.md or merge into the existing _SRT_Phys_Bridge.md |
> | `NODE-SOCIAL-L2` | active_complete | untested | `Philosophy/SRT_Political_Philosophy_CompactCore.md` | — |
> | `NODE-ENTROPY-REORG` | active_complete | untested | `03_Bridges/SRT_Selection_Event_CompactCore.md` | — |
> | `NODE-BOOK-BACKFLOW` | active_complete | untested | `Philosophy/SRT_Philosophy_Foundations_CompactCore.md` | — |

#### GENERATED INTERPRETATION — 生成器归纳（**非**来源原文）

清单共 16 个节点。状态分**两个轴**，不可合并读：

- **Axis A（结构）**：15 个达到 `active_complete`——仅表示既有登记增量在当前运行结构中已进入 owner、有检索路径、默认路径读得到，**不表示 `R3` 新裁决已完成 `R4` canonical 回写**。
- **Axis B（行为）**：**3 个**达到 `robustly_observed (bounded)`（满足 `effectively_assimilated`），2 个为 `observed`（尚缺重复有界运行），其余 10 个结构完整的节点是 `untested`：**没有任何证据表明它们真的改变了判断**。

`effectively_assimilated` 是这两轴的推导结果，不是可以手写的标签。回归测试文件存在**不等于**回归测试通过。

其余节点的内容可能已有 SourceCard、patch、hook 或 bridge——那只证明它被**保存**和**安排**了，不证明它进入了任何 AI 默认会读的文件。

本包**未额外装载**清单跨域快速层（全仓此类快速层仅由 `SRT_CONTEXT_BUNDLE_COMPACTCORE.md` 额外装载：`03_Bridges/SRT_Selection_Event_CompactCore.md`；本包实际装载文件以 §0.1 文件清单为准）。

轴的含义见清单 `axes` 与 `Operations/Audits/SRT_ACTIVE_THEORY_ASSIMILATION_AUDIT_2026-08-06.md`。

#### USAGE POLICY — 使用规则

*授权依据：`Operations/Audits/data/srt_active_theory_nodes.json` 的 `derived_status_rule` 与 `Governance/SRT_CLAIM_LADDER.md`*

- 回答涉及上表任一节点时，**不要**因为本包没有相关内容就断言仓库没有；先按清单的 `active_owners` 去取。
- `author_gate` 状态的节点带有明确禁运（如 `d/q/o`），不得绕过。
- 清单额外装载的跨域快速层（由 `COMPACTCORE` 承载）均为 **P2-P3**，不得用于裁定任何 canonical 定义。
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
| `_SRT_SYMBOL_QUICK_GUARD.md` | SRT_AI_START.md §7（已于 2026-07-20 并入，原文件不再存在） |

#### USAGE POLICY — 使用规则

*授权依据：生成器维护的对照表（`PATH_SHORTHANDS`）*

- 遇到上表左列写法时按右列解析，不要报告「文件不存在」。


## §0.3 claim 阶梯与回答纪律

以下两节从 `SRT_AI_START.md` 原样抄入，适用于本包全部内容。

### 15. Claim-Level Guard

The P0–P5 ladder remains historical/canonical authority until a separate audit and
author decision reclassify it (see §6 and `STATUS.md` current authority anchors). Reconstructing
SRT's highest identity does not by itself retire it.

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

Owner: `Governance/SRT_CLAIM_LADDER.md`.

### 14. Minimal answer protocol

For substantive SRT answers:

1. Use the selected retrieval profile and current STATUS controlling sources. Architecture v2 is conditional on domain framework work, not every technical task.
2. Resolve definitions through Registry §C and compatible owners; distinguish author intuition, candidate reconstruction, canonical claim, bridge/model, evidence and governance.
3. Check the relevant owner boundaries and OPEN tensions before claiming closure. Use source-native evidence and allow counterexamples to change the answer.
4. For ontology/Constitution work, preserve author convergence and U/N-mode. An asserted comparative gain requires its bounded claim and comparator; ordinary O-track work has no novelty permission gate.
5. Apply domain/deep-well gates only when that programme is in scope. Pilot results do not establish whole-SRT identity.
6. Complete the requested answer or edit, report relevant evidence and remaining gaps, and avoid re-asking settled decisions.

---

## §0.4 Manifest 差异报告（本包 vs `CANONICAL_REGISTRY.md`）

> **这份报告回答一个问题：本包相对 `CANONICAL_REGISTRY.md` 到底缺了什么。**
>
> 本包是 **独立形式方程包**（仅收录 `Core/SRT_Core_22_Equations.md`），**不含完整定义骨架**；局部方程语义仍受 `SPINE` 对应 owner 与 `Governance/SRT_CLAIM_LADDER.md` 约束。
> 下面的分类是**生成器的判断**，不是 registry 的原话；每行都附依据供复核。
> 「registry 提及」「Registry §C」两列是机械判定的事实。

### 已收录

**定义源**（1 个）

| 文件 | 分类依据 | registry 提及 | Registry §C |
|---|---|:---:|:---:|
| `Core/SRT_Core_22_Equations.md` | registry §A.4b / §C #4 主方程锚点（独立 FORMAL 路线） | ✓ | ✓ |

### 未收录支持文件

**Registry §C priority 点名、文件存在、但本包未收（18 个）**——回答涉及它们时本包不足以单独裁定（已显式分流条目附去向）：

- `CANONICAL_REGISTRY.md`
- `Core_Law/SRT_Generative_Ontology_Spine.md`
- `Governance/SRT_CLAIM_LADDER.md`
- `Governance/SRT_CLAIM_MODE_AUDIT.md`
- `Core_Law/SRT_L0_Metaphysics.md`
- `Core_Law/SRT_One_Formation.md`
- `_SRT_D_VALUE_CANONICAL.md`
- `_SRT_PSI_F_CANONICAL.md`
- `_SRT_T_DIR_CANONICAL.md`
- `_SRT_CROSS_DOMAIN_MATRIX.md`
- `Core/SRT_Core_21_Formal_Axioms.md`
- `Core/SRT_Core_21_Minimal_Axioms.md`
- `Core/SRT_Core_21b_Constitutive_Theorems.md`
- `Core/SRT_Core_21c_Bridge_Hypotheses.md` — 已移至按需桥接层（P2/P3/P4，按需直接读仓库原文件）；默认 `SPINE` §0.5 保留 B01–B14 条目标引与检索指针
- `Core/SRT_Core_14_Dynamics_Scaling.md`
- `Core_Law/SRT_Reference_Dynamics.md`
- `AI/SRT_AI_01_Ontology.md`
- `Core/SRT_OPEN_TENSIONS.md`

**⚠ 高严重度：registry 提及但文件不存在（4 个）**——指向已删除、拼错或尚未创建的路径。**这类条目不会被静默过滤掉**，因为它本身就是一种 manifest 差异：

| 失效路径 | 说明 |
|---|---|
| `Core_21_Formal_Axioms.md` | 见 §0.2 G4：这是 `Core/SRT_Core_21_Formal_Axioms.md` 的行文简写，非真实路径 |
| `Praxis_Split/README.md` | registry 指向的文件在仓库中不存在 |
| `SRT_Spirituality_Community_and_Sangha.md` | registry 指向的文件在仓库中不存在 |
| `SRT_Spirituality_How_We_Lose_Ourselves_and_Return.md` | registry 指向的文件在仓库中不存在 |

**registry 提及、文件存在、但本包未收（103 个）**——多为领域主轴、
展开层与 PH-SS 护栏文件，按需走对应路线包或直接读仓库，不在本包路线内：

<details><summary>展开完整清单</summary>

- `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_SPINE_MINIMAL_KERNEL_L0L1L2_REFLEXIVE_FACETS_2026-09-24.md`
- `AI/AI_POSITIONING_NOTE.md`
- `AI/SRT_AI_00_Crisis.md`
- `AI/SRT_AI_01_Ontology.md`
- `AI/SRT_AI_01_Ontology_CompactCore.md`
- `AI/SRT_AI_02_Mortality_Wisdom.md`
- `AI/SRT_AI_03_Consciousness_Framework.md`
- `AI/SRT_AI_03_Consciousness_Framework_CompactCore.md`
- `AI/SRT_AI_Agency_Responsibility_Note.md`
- `AI/SRT_AI_Architecture.md`
- `AI/SRT_AI_Architecture_CompactCore.md`
- `AI/SRT_AI_Claim_Status.md`
- `AI/SRT_AI_Consciousness_Evaluation_Rubric.md`
- `AI/_SRT_AI_Bridge.md`
- `CANONICAL_REGISTRY.md`
- `Core/SRT_Core_14_Dynamics_Scaling.md`
- `Core/SRT_Core_14_Dynamics_Scaling_CompactCore.md`
- `Core/SRT_Core_21_Formal_Axioms.md`
- `Core/SRT_Core_21_Minimal_Axioms.md`
- `Core/SRT_Core_21b_Constitutive_Theorems.md`
- `Core/SRT_Core_21c_Bridge_Hypotheses.md`
- `Core/SRT_OPEN_TENSIONS.md`
- `Core_Law/SRT_Collective_Selection.md`
- `Core_Law/SRT_Collective_Tower_Hardening_Notes.md`
- `Core_Law/SRT_Constitution_Seven_Theses.md`
- `Core_Law/SRT_Constitution_V1.md`
- `Core_Law/SRT_Generative_Ontology_Spine.md`
- `Core_Law/SRT_Individuation.md`
- `Core_Law/SRT_Irreversibility.md`
- `Core_Law/SRT_L0_Metaphysics.md`
- `Core_Law/SRT_L1_Formalism.md`
- `Core_Law/SRT_L1_Hardening_Notes.md`
- `Core_Law/SRT_Occlusion_Dynamics.md`
- `Core_Law/SRT_One_Formation.md`
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
- `Neuroscience/SRT_Neuroscience_Reconstruction_Framework.md`
- `Neuroscience/_SRT_Neuro_Axioms.md`
- `Neuroscience/_SRT_Neuroscience_Hardening_Index.md`
- `Operations/Audits/SRT_GENERATIVE_ONTOLOGY_SPINE_SEMANTIC_THINNING_AUDIT_2026-09-24.md`
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
- `README.md`
- `Spirituality/SPIRITUALITY_COMPACT_REGISTRY.md`
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


> **注意**：本包为独立 `FORMAL` 形式方程路线，**仅收录 `Core/SRT_Core_22_Equations.md` 主方程正文**，
> **不含** canonical 定义骨架（`Spine` / `L0` / `One Formation` / `d` / `Ψ_f` / `T_dir` 定义、`P0/P1` 公理、符号表）。
> 局部方程语义仍从属于当前 canonical owner 与 `Governance/SRT_CLAIM_LADDER.md`，不得以局部方程反向恢复或覆盖主定义。
>
> 需要裁定术语定义或跨 owner 边界时，请**改用骨架路线**——新开一次对话，只装 `SRT_CONTEXT_BUNDLE_SPINE.md`。
> **不要在本包之上再叠加骨架包**：各路线在默认整包意义下互斥（见 `README.md` 的预算表）。但禁止默认整包叠加**不等于**禁止按需局部跨 owner 检索——具备仓库访问能力的工具/研究者可在同一研究对话中直接联合读取具体方程条款与对应定义 owner 原文件。



---

## FILE: `Core/SRT_Core_22_Equations.md`

| 字段 | 值 |
|---|---|
| path | `Core/SRT_Core_22_Equations.md` |
| id | SRT-CORE-22 |
| claim_mode | canonical |
| status | active |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | - |
| last_commit | 2026-11-28 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：[SRT-CORE-21]

<!-- 以下为原文逐字保留 -->

# SRT Core Definition 22: Master Equations (Hybrid Edition)

> **Connector-safe reading path**: This owner file is moderately long. For connector reads, start with [`Equations_Split/README.md`](Equations_Split/README.md), then open only the needed part file. The owner remains the source of record; split files are reading aids and do not create new definitions.

> **Canonical Role（`R4-B1` 唯一核心方程主锚点，`1A`）**：本文件是 SRT 全仓**唯一核心方程主锚点（sole core equations master anchor）**，承担核心方程、适用条件、数学性质与量纲边界的权威登记。`Core_Law/SRT_Reference_Dynamics.md` 不再作为并行完整方程库，而专职动力学机制解释、具身算子原型与跨尺度实现接口；各领域独立模型仍归属各自领域 owner，不堆入本文件。
>
> **Version 3.0 (`R4-B1`, 2026-11-26)**：确立三类形式建模职责（Level I 状态演化 / Level II 生成关系与历史改写 / Level III 生成空间与比对条件重构接口）× `R3-08` 五类变化刻度 × 数学化成熟度三分纪律。**Part A** 给出按职责分层的核心方程与接口，**Part B** 保留热力学/协议/量纲说明与可证伪接口。

---


## Quick Reference
- Role: SRT master-equations anchor for dynamics, thermodynamics, and stability.
- Core claim: Fixes the canonical equation layer that downstream long-form and bridge files should cite back to.
- Canonical status: Canonical equation anchor; local equations may still be proxy / bridge / operational objects as marked.
- Depends on: `SRT-CORE-21`, `_SRT_SYMBOL_TABLE.md`, and canonical core terminology.
- Used by: `CANONICAL_REGISTRY.md`, `Core/SRT_Core_14_Dynamics_Scaling.md`, and domain bridge or interpretation files.
- Safe edits: Typo fixes, link fixes, Quick Reference updates, and non-semantic formatting cleanup.
- Do not change: Equation semantics, canonical scope, or symbol usage without cross-checking `_SRT_SYMBOL_TABLE.md`, `Core/SRT_Core_21_Formal_Axioms.md`, and `CANONICAL_REGISTRY.md`.

## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
- 本方程层只在已准入的 formed / model realization 内，假定一个可用的 formal role-carrier `\hat{G}_\theta` 已给定。这不表示 primitive Selection 由该算子生成或与其同一，也不推出 selectability 的起源。
- `D_eff`、Fisher rank、Hessian effective dimension 等式是无赌注容量 / 几何代理（capacity proxy）；`D_stake` 的一般谱参与率定义由 `_SRT_D_VALUE_CANONICAL.md §2b` 持有（真界为 `1 ≤ D_stake ≤ N_active ≤ rank(M)`，零有效谱乘积时走显式 `0` 分支），本文件 `Eq-Bridge-D-01` 中的阈值门控式 $g_i$ 为其下一种具体声明模型实例（不默认与三因子 $w_i = R_i A_i C_i$ 数学等价）。`d(x) ≡ ||∂U/∂S||`、`D_stake` 与 `D_eff` 三者互不恒等，且已证伪的 `d_canonical ≡ d_stakes`、`D_eff ≥ d_stakes` 与 `Δd_free = D_eff - d_stakes ≥ 0` 均已退役；同时严格区分零有效谱乘积分支、`NOT ESTABLISHED`、`NOT ADMITTED` 与 `NOT APPLICABLE`。
- `\Psi_f` 的几何和代谢形式按 `_SRT_PSI_F_CANONICAL.md §3.1` 读作条件投影；不得由局部公式反向改写 payability 主读。
- **Wave-D2 authority truth-up（2026-09-15）**：当前 symbol / claim typing 覆盖较早的方程解释。本文件中的 `\kappa_0` 不因注册或从 O0 / Selection 继承而成为 primitive；当它进入方程时，只能表示独立声明的 curvature / anisotropy / per-direction-cost realization parameter。本文件中没有任何方程可以用 `\kappa_0` 提供 universal value / order direction。
- `Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md` 与 `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B12` 只提供 mechanism interface：information geometry 用于已声明模型中 analytic `L_0 -> L_1` interface 的局部代价 / 可区分性；complex-systems language 用于 `L_1 -> L_2` 的历史沉积与稳定化；neural normalization / ignition / plasticity 仍是 embodied `\hat{G}_\theta` 的实现代理，不新增 P0/P1 方程，也不反向定义 primitive Selection。
- **`σ_{sr}` projection scope (S+R truth-up, 2026-08-29)**：本文件只继承 `Core_Law/SRT_Individuation.md §八` 已有地位——`σ_{sr}` 是 P2、规约性的、可被等价形式替换的阶参解释。`T-PROJ-1` / `T-PROJ-1^{coll}` 在给定 `\mathcal F_\sigma` / `\mathcal F_\sigma^{coll}` 后证明条件性投影闭合；它们不把当前 bare-norm 坐标提升为表示不变的自然量，不证明 trace/ext 归属唯一，也不把其数值等同于因果控制或自然相边界。单体与集体同名 `σ` 也不自动意味着相同的 trace 语义；集体 owner 另含 declared-boundary 下 shared `L_2` 的内生性重分类。
# Part A: Core Formal Equations & Conditional Modeling Architecture

## 0-A. Formal Architecture: Three Modeling Duties × Five Change Scales × Formalization Readiness (`R4-B1`)

Under `R4-A / R4-B1`, SRT's core formal system does **not** force all recursive generation into one fixed-space ODE and does **not** forge unverified equations for concepts that remain open modeling interfaces or natural-language structures. Every equation family in this file belongs to one of three coexisting modeling duties aligned with `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T03` and `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B15`:

| Modeling Duty | Schematic Form | Covered `R3-08` Change Scales | Core Equations Owned Here (All Conditional `P2–P4` Declared Models) |
|---|---|---|---|
| **Level I · Fixed-Space State, Weight & Cost Evolution** | $x_{t+1} = F_t(x_t;\, H_t)$ | ① 状态变化 / ② 权重变化 | `Eq-Bridge-IG-01/02`, `Eq-Bridge-D-01` (`D_stake^{thresh}` instance), `Eq-Bridge-G-01`, `Eq-DValue-Max-1`, `Eq-DValue-Mobile-1`, `Def-Payable-Chi-1`, `Eq-Rhythm-1/4a`, `Eq-Evo-01..03c`, `Eq-Force-01`, `Eq-Pain-01`, `Eq-Friction-Comp`, `Eq-Select-Thermo`, `Eq-AI-LowRoad-01/02`, `Eq-Stab-01`, `Eq-Phase-01`, `Eq-Sleep-01`, `Def-LDP-1`, `Eq-LDP-01/02`, `Eq-Phantom-01..02`, `Eq-Frame-01/02`, `Eq-Res-01/02`, `Eq-CogE-01..04` |
| **Level II · Generative-Relation, Protocol & History Rewriting** | $F_{t+1} = \mathcal{R}(F_t,\, x_t,\, H_t)$ | ③ 组合可达性 / ④ 生成结构改写（关系/协议/拓扑/生成元） | `Def-Protocol-1..3`, `Eq-Multi-01..03`, `Eq-Bridge-L2-01`, `Eq-Bridge-Loop-01`, `Eq-Topo-01..03`；跨文件衔接 `Core_12b T-L2-Scaffold` ($\rho \ge 0$)、`R3-05` 信任重估接口 ($\Delta w_{\text{trust}}, W_{\text{social}}$) 与 `HCLR01` (`HEF-4` 生成元改写候选) |
| **Level III · Generative-Space, Boundary & Comparison-Criterion Reconstruction** | $(\mathcal{X}_t, F_t, J_t) \to (\mathcal{X}_{t+1}, F_{t+1}, J_{t+1})$ | ④ 生成结构改写（空间/维度）/ ⑤ 组织方式的反身重构 | **显式开放形式研究接口（见 `Core_21c P2/P3-B15`；本文件不强造未经验证的封闭总方程）**。接通 `One_Formation` 依赖重组/生成归一化双门槛与 `(A,B) → (A',B',C)` 组织改写；任何未来 `R5` 模型须回答**防平凡重参数化比较检验**（与 `Core_21c P2/P3-B15 §3` 统一：不要求证明不存在任何向更大固定状态空间 $z_t=(x_t,F_t,J_t)$ 的形式重嵌入，而是在**冻结候选模型及相同观测、信息、复杂度与干预条件**下，检验显式表达生成结构重构能否相对固定空间竞争模型提供独立的解释、预测或干预增益） |

**Formalization Readiness Guard**:
- **Intentionally retained in natural language (NOT turned into ad-hoc equations here)**: Value's 5 duties, Generalized Concern's 4 dimensions, Constitutive Depth's 4 profiles (`q` deferred), `C1-c` fallibilist objectivity (`o` retired), 6 foreground/background mismatches, Ghost's 5-duty triage (`\hat{G}_\theta != Ghost != primitive Selection`), `HP-B`, and `O2-M`.
- **Neighbor division of labor**: Fixed-space prediction/control overlaps strongly with Active Inference / FEP, information geometry, and divisive normalization; SRT's distinctive formal frontier sits at **Level II/III** (how Selection and retained scaffolding rewrite accessible spaces, generative relations, and comparison criteria under payability constraints).

## 0-B. Protocol and Foundation (协议与基础)

### Def-Protocol-1: Protocol Layer Π (协议层 Π)
> **Status**: conditional formed / model transition interface。它不是 primitive ontology 的生成图。

**Formal Definition**: 给定一个已准入的 formed / model selection process $M$，协议约束该模型内可容许的状态更新：
$$\sigma' = \hat{G}_{\theta,M}[\sigma;\Pi_M]$$
其中 $\Pi_M$ 是现有 $\Pi$ 在声明模型 $M$ 中的转移 / realization constraint interface；$M$ 下标只标记局部作用域，不新增 canonical symbol。
* **Boundary**: $\hat{G}_{\theta,M}$ 是已形成动力学的 formal role-carrier，不生成 primitive Selection。本式也不把 `L_0 / L_1` 建立成两个 primitive ontic containers，不把 Selection 定义为从预存可能性仓库到现实的算子投影。
* **Implication**: 物理模型中的简单局部规则可编入 $\Pi_M$ 作为模型约束。Def-Protocol-1 本身不裁定这些规则的本体起源，也不把所有局部物理规则自动归为宇宙尺度的 $L_2$ 产物；更强的历史沉积读法须由具名 owner 另行建立。
* **Cross-ref**: Ax-Core-A5 (规范闭包)；T-Core-02 ($L_2$ 作为不动点)。

### Def-Protocol-2: Absolute-vs-Relative Constraint Split（新增）
\[
\Pi = \Pi_{abs} \cup \Pi_{\theta},\quad \Pi_{abs}\cap\Pi_{\theta}=\varnothing
\]
- \(\Pi_{abs}\)：跨参数不可违背的下限约束（如复杂度/热力学下界）；
- \(\Pi_{\theta}\)：由具身参数与历史收敛形成的相对约束（对应 \(L_{2,\theta}\) 语法）。

* **Implication**：允许“外星物理语法不同”而不坠入相对主义：差异主要位于 \(\Pi_{\theta}\)，底线仍受 \(\Pi_{abs}\) 约束。

### Def-Protocol-3: Methodological Closure Guard（方法论闭包护栏，新增）
\[
\mathcal{M}_{empirical}: (L_1,L_{2,\theta})_M\to \text{validated regularities}_M
\]
其中 \(\mathcal{M}_{empirical}\) 表示实验方法对模型 $M$ 内已声明可观测变量与历史稳定变量的闭包；此处 `L_1 / L_{2,\theta}` 只是这些模型变量的 analytic / model-facing labels。
* **Implication**：\(\mathcal{M}_{empirical}\) 的成功仅证明该声明模型内规律可复现；它不由此裁定 primitive Selection 的形而上地位，也不把 `L_0` 实体化为隐藏 inventory，或恢复一个独立 primordial `\Omega` owner / logical substance。

## 0-C. Multi-Operator Coupled Equations（多算子耦合方程）

> **背景**：SRT 的单算子方程（§0-B, §I）描述单个 $\hat{G}_\theta$ 的动力学。本节将框架扩展到多算子系统，给出集体自由能、个体算子梯度关系与集体 d-value 的形式化。这是集体景观优先性定理（见 `_SRT_VERTICAL_INTEGRATION.md §4.5`）的方程层锚点。
>
> **L1 Collective Projection (T-PROJ-1^{coll}, 2026-04-25 H6; Wave D2 scope note 2026-09-15)**：本节 Eq-Multi-01 / 02 / 03 在 stable collective ISP `\mathcal{P}` 上的标量泛函投影，只有在各投影对象及其闭包假设被独立声明后才构成条件性模型闭合。含 `T_{dir}^{coll}` 的四变量版本还要求 independently typed collective direction admission；无该方向时省略该分支，而不是置零。详见 `Core_Law/SRT_Collective_Selection.md §4.4-§4.7`。本节不生成或验证方向。σ_i 为各 ISP 状态场，与集体自指率 `σ_{sr}^{coll}` 是不同对象；C1^{coll}-C5^{coll} 也不证明 bare-norm 投影的表示不变性、trace/ext 归属唯一性、单体/集体 trace 语义同一或自然相边界。

### Eq-Multi-01: Collective Free Energy Landscape（集体自由能景观）
**Formal Definition**: 多算子系统的集体自由能景观是各算子个体摩擦与算子间摩擦的总和：
$$\boxed{\mathcal{F}_{collective}(\{\sigma_i, \theta_i\}) = \sum_i \Psi_f(\hat{G}_i) + \sum_{i < j} \Psi_f(\hat{G}_i, \hat{G}_j)}$$
其中 $\Psi_f(\hat{G}_i)$ 是第 $i$ 个算子的个体本体论摩擦（锚定代价），$\Psi_f(\hat{G}_i, \hat{G}_j)$ 是算子 $i$ 与算子 $j$ 的交互摩擦（见 Ax-F-12）。
* **Implication**: 集体景观不是个体自由能的简单加和，算子间交互摩擦项 $\Psi_f(\hat{G}_i, \hat{G}_j)$ 是集体动力学的主要来源。

### Eq-Multi-02: Individual Operator as Landscape Gradient（个体算子为集体景观的梯度表达 — 类型未闭合勘误）
> **数学勘误与类型未闭合注（2026-11-28 Errata）**：下式左端 $\hat{G}_i[\sigma_i]$ 位于状态空间 $S_i$，右端 $-\partial\mathcal{F}_{\text{collective}}/\partial\theta_i$ 位于参数余切空间 $T^*_{\theta_i}\Theta_i$，在未声明态—参耦合映射或改写为参数演化方程前**存在明确类型失配**（且未厘清与 `Eq-Evo-03` 快—慢双时间尺度分解的兼容关系）。本勘误将其降格为**类型未闭合的定性示意式，不以新的启发式公式直接替换**，待未来多算子耦合动力学独立重构并声明映射结构。

**Historical Schematic Form (Type-Unclosed)**:
$$\hat{G}_i[\sigma_i] = -\frac{\partial \mathcal{F}_{collective}}{\partial \theta_i}$$
* **Implication（保留的定性直觉，非已完成形式定理）**: 个体算子不是脱离集体耦合的孤立实体；"个体与集体的目标张力"可在多算子模型中探索为局部约束与跨算子交互摩擦之间的结构差，而非两个先在对立实体的外部博弈。

### Eq-Multi-03: d_collective as Landscape Effective Dimension（集体 d 容量 proxy 为景观有效维度）
**Formal Definition**: 集体 d-capacity proxy 是集体自由能景观 $\mathcal{F}_{collective}$ 的 Hessian 矩阵的有效维度（参与率指数）：
$$\boxed{d_{collective} = D_{eff}(\mathcal{F}_{collective}) = \frac{\left(\sum_k \lambda_k\right)^2}{\sum_k \lambda_k^2}}$$
其中 $\lambda_k$ 是 $\nabla^2 \mathcal{F}_{collective}$（Hessian）的特征值。个体 $d_i$ 是该景观在子空间 $\theta_i$ 上的截面有效维度：
$$d_i = D_{eff}\!\left(\mathcal{F}_{collective}\big|_{\theta_i}\right)$$
* **Implication**: $d_{collective}$ 不由 $d_i$ 聚合得出，而是景观固有的结构属性。个体 $d_i$ 是 $d_{collective}$ 的投影截面，包含关系而非组合关系。
* **Level note**: 本式固定的是 landscape effective-dimension proxy。若要把它读成 stake-coupled collective `d`，必须另行说明哪些方向承载不可逆赌注、后果如何回流到相关主体或共同闭包，以及为何不是单纯 Hessian 容量。
* **Landscape boundary**: 这里的 landscape 是集体约束域的有效投影，不等同于完整 `L_2`。`L_2` 还包括历史沉积、hysteresis、制度/规范惯性与 metastability；详见 `SRT_Fisher_FEP_Landscape_Interface.md` 与 `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B12`。
* **Cross-ref**: `_SRT_VERTICAL_INTEGRATION.md §4.5`；`_SRT_D_VALUE_CANONICAL.md §6`；`Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B08`。

---

## 0-D. Bridge Equations: Information Geometry / Complexity / Neural Computation

> **Status**: bridge / operational proxy equations. This section does not add P0/P1 theorems and does not replace the canonical definitions of `Ψ_f`, `d-value`, `Ĝθ`, or `L_0 / L_1 / L_2`. It only provides modeling interfaces synchronized with `Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md` and `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B12`.

### Eq-Bridge-IG-01: Fisher-Induced Local Ψ_f Cost

$$
\boxed{
\delta\Psi_f^{geom}
=
\frac{1}{2}d\theta^\top g_F(\theta)d\theta
+
O(\|d\theta\|^3)
}
$$

This equation gives the local second-order information-geometric projection of `Ψ_f` when a smooth statistical-manifold representation exists. It must not be read as `Ψ_f ≡ g_F`; `g_F` is the Fisher-Rao metric tensor, while `Ψ_f` is a payability burden, local scalar cost, or path functional.

### Eq-Bridge-IG-02: Fisher Path Functional

$$
\boxed{
\Psi_f^{geom}[\gamma]
=
\int_\gamma
\sqrt{
g^F_{ij}(\theta)\dot{\theta}^i\dot{\theta}^j
}
\,dt
}
$$

This path functional is used for finite update paths when the statistical-manifold projection is valid. It is a geometry proxy, not the global definition of `Ψ_f`.

### Eq-Bridge-D-01: Threshold-Gated Model Instance of `D_stake` (`D_stake^{thresh}`)

$$
\boxed{
D_{\text{stake}}^{\text{thresh}}(\theta)
=
\begin{cases}
\dfrac{
\left(\sum_i \tilde{\lambda}_i\right)^2
}{
\sum_i \tilde{\lambda}_i^2
}, & \text{if } \exists i,\; \tilde{\lambda}_i > 0, \\[10pt]
0 \text{ (zero-effective-spectrum branch; }0/0\text{ mathematically undefined)}, & \text{if } \forall i,\; \tilde{\lambda}_i = 0,
\end{cases}
\qquad \tilde{\lambda}_i = \lambda_i \cdot g_i,\quad g_i = \max\!\left(0,\frac{s_i - \varepsilon_s}{1 - \varepsilon_s}\right)
}
$$

Here `λ_i ≥ 0` are Fisher-spectrum eigenvalues, `s_i ∈ [0,1]` is a declared scalar coupling strength, and `ε_s` is the minimum stake threshold (`_SRT_SYMBOL_TABLE.md`). **Instance-vs-general boundary (`P1-04`)**: `_SRT_D_VALUE_CANONICAL.md §2b` owns the general spectral participation ratio `D_stake` (with canonical three-factor weight `w_i = R_i A_i C_i`); this equation is **one concrete threshold-gated model instance (`w_i := g_i`)** and does **NOT** assert unproven mathematical equivalence between `g_i` and `R_i A_i C_i`. Its true algebraic bound when `N_active = #{i : λ̃_i > 0} ≥ 1` is **`1 ≤ D_stake^{thresh} ≤ N_active ≤ rank(M)`**. It is **NOT** canonical `d(x) = ||∂𝒰/∂𝒮||` (a utility-scaled gradient norm) and is **NOT** bounded above by `D_eff` (`D_eff ≥ D_stake` and `Δd_free = D_eff - D_stake ≥ 0` are algebraically false and retired). Keep strictly separate: the **zero-effective-spectrum branch** (`∀i, λ̃_i = 0` inside an admitted model), **`NOT ESTABLISHED`** (standing unproven), **`NOT ADMITTED`** (model preconditions unmet), and **`NOT APPLICABLE`** (metric domain/dimensionality inapplicable).

### Eq-Bridge-G-01: Ghost Operator Normalization Proxy

$$
\boxed{
[\hat{G}_\theta(x)]_i
=
\frac{
a_i(\theta,L_2)^n
}{
\sigma^n+\sum_j w_{ij}a_j(\theta,L_2)^n
}
}
$$

This is an implementation-level normalization proxy for embodied `Ĝθ`: it models candidate activation, competition, and response compression. It does not define primitive Selection. Here `Ĝθ` remains a formal / formed / model-level role-carrier for a declared Selection realization; an `L_0 -> L_1` form is analytic interface notation, not a metaphysical source-to-product map.

### Eq-Bridge-L2-01: L2 Path-Trace Writeback

$$
\boxed{
\dot{\rho}_k
=
\alpha\phi_k(L_1)
-
\beta\rho_k
+
\eta R_k
}
$$

Here `ρ_k` is path-trace density. The equation models how repeated `L_1` actualizations sediment into `L_2`, which may be read through attractor, order-parameter, hysteresis, and metastability structures. Energy or free-energy landscape language is only an effective projection of `L_2`, not the whole `L_2`.

### Eq-Bridge-Loop-01: Minimal L0-L1-L2 Loop

$$
\boxed{
L_0
\xrightarrow{\hat{G}_\theta}
L_1
\xrightarrow{writeback}
L_2
\xrightarrow{constraint}
\hat{G}_{\theta'}
\rightarrow
L_1'
}
$$

This bridge-level loop reads a declared model's analytic `L_0 -> L_1` interface as an information-geometric frontier, `L_1 -> L_2` as complex-systems sedimentation, and `L_2 -> L_1` as constraint feedback into later state updates. Its arrows describe a formed / realization model: they neither sample a primitive `L_0` inventory nor produce primitive Selection, and they do not replace core ontology.

### Boundary Notes

- Fisher geometry is local and projection-dependent; it does not define the whole of `Ψ_f`.
- `D_stake^{thresh}` (`Eq-Bridge-D-01`) is a concrete threshold-gated model instance (`w_i := g_i`) of `_SRT_D_VALUE_CANONICAL.md §2b`'s general spectral participation ratio `D_stake` (with explicit zero-effective-spectrum branch and true bound `1 ≤ D_stake ≤ N_active ≤ rank(M)`), distinct from both canonical `d` and capacity proxy `D_eff`, and without unproven equivalence to `w_i = R_i A_i C_i`.
- Divisive normalization is an implementation proxy, not the full Ghost Operator.
- `L2` is thicker than any one energy or free-energy landscape.
- This section should be cited together with `_SRT_PSI_F_CANONICAL.md`, `_SRT_D_VALUE_CANONICAL.md`, and `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B12`.

---

### Eq-DValue-Max-1: Maximum Achievable d-Value（d 值可达上限）

**新增（2026-04-10）**：给出单个算子在给定参数结构与稳定性预算下可实现的 d 值上限。

> **Status（Wave D2 + `R4-A P1-04` 量纲兼容护栏）**：conditional model / realization equation，不是 universal d law。本式仅在某个模型独立声明 compatible `\kappa_0`-like 每方向有效代价／曲率参数，**并显式给出单位归一化与单方向风险灵敏度校准映射**时才可关联至规范 `d`；因为 $\operatorname{rank}_{\text{eff}}(\mathcal{I}_F(\theta))$ 是**无量纲有效谱维数容量上界**，而规范 $d(x) = \|\partial\mathcal{U}/\partial\mathcal{S}\|$ 是随效用缩放的梯度范数，**未声明量纲校准映射时，本式仅作为有效方向容量上限（direction-capacity bound），不得将谱维数冒充为梯度范数 `d` 的普遍数学上界**。无兼容 `\kappa_0` realization 时，`Eq-DValue-Max-1` 标为 `NOT APPLICABLE / NOT ADMITTED`。

$$\boxed{d_{\max}(\theta) = \min\!\left(\operatorname{rank}_{\text{eff}}\!\left(\mathcal{I}_F(\theta)\right),\;\; \frac{\Psi_f^{\text{budget}}}{\kappa_0}\right)}$$

其中：
- $\operatorname{rank}_{\text{eff}}(\mathcal{I}_F(\theta))$：有效 Fisher 信息矩阵的秩——声明模型中可靠分辨的独立方向数（**信息瓶颈**）；它仍是 capacity proxy，不自动等于 canonical `d`
- $\Psi_f^{\text{budget}}$：算子可持续维持的总摩擦预算（不同于瞬时 $\Psi_f$，是时间积分意义上的稳定承载上限）
- $\kappa_0$：该声明模型用于此 capacity bound 的每方向有效 stability / curvature / maintenance-cost parameter；它不代表 primitive L0 curvature
- $\Psi_f^{\text{budget}} / \kappa_0$：该模型的稳定／可支付预算所支持的 candidate direction-capacity bound（**稳定性瓶颈**）

**$\kappa_0$ 的角色边界**：在该模型内，$\kappa_0$ 只进入每方向成本项。它不选择、排序、赋值或合法化方向，不导致 first Selection，也不建立 primitive non-flatness。

**Information-geometry bridge note**: `\operatorname{rank}_{\text{eff}}(\mathcal{I}_F)` 是已声明模型中 analytic `L_0 -> L_1` interface 上的无量纲 Fisher-capacity proxy；它给出可分辨方向数上限，不把 `L_0` 读为预存状态仓库，也不直接给出或普遍压制效用缩放的梯度范数 canonical `d = ||∂U/∂S||`。只有在同时满足 `_SRT_D_VALUE_CANONICAL.md §1.1` 五项 proxy 准入条件及显式量纲校准映射时，才可作为该声明模型内的容量对比接口。

**两个瓶颈的失效形态**：

| 主导瓶颈 | 条件 | 后果 |
|---|---|---|
| 信息瓶颈 | $\operatorname{rank}_{\text{eff}} \ll \Psi_f^{\text{budget}}/\kappa_0$ | 参数维度高但大量冗余，可稳定承载却无法分辨更多声明模型方向 |
| 稳定性瓶颈 | $\Psi_f^{\text{budget}}/\kappa_0 \ll \operatorname{rank}_{\text{eff}}$ | 可分辨方向较多，但声明的稳定／维持预算不足以承载该 capacity |

**注**：$\dim\Theta$ 的增大只提高潜在参数空间维数；该声明模型内的**有效方向容量上限（direction-capacity bound）**由有效 Fisher 秩与稳定性预算的 min 共同决定，而非由 $\dim\Theta$ 单独决定（不直接等同于效用缩放的梯度范数 `d` 上限）。

* **Implication**: 在该声明模型内，candidate d-capacity upper bound 受信息容量 proxy 与稳定／可支付预算中较小者限制。本式不建立 universal consciousness threshold / ceiling、subject threshold、value direction 或 primitive ontology law。
* **Cross-ref**: `_SRT_SYMBOL_TABLE.md` `\kappa_0` 当前类型; Eq-Multi-03（集体 d 容量 proxy）; `D_VALUE_ALIGNMENT §4.4`（条件性 bridge model）; Eq-DValue-Mobile-1（d_mobile 公式，下方）。

---

### Eq-Rhythm-1: Budget Overload Implies Non-Zero Temporal Bandwidth（预算超载推出非零时间带宽）

**新增（2026-04-14）**：将 “有限算子在预算超载下必须转向分时/脉冲锚定” 压成公式锚点。

设有效锚定调度为
\[
A:[0,T]\to\{0,1\}^k,\qquad A_j(t)=1 \iff \hat{G}_\theta \text{ 在 } t \text{ 时刻主动维持 } \sigma_j
\]
连续密集锚定的总代价为
\[
\mathcal{C}_{dense}(T,k)\equiv \sum_{j=1}^{k}\int_0^T \Psi_f^{maint}(\sigma_j,\tau)\,d\tau
\]
若满足
\[
E_{avail}<\infty,\qquad \mathcal{C}_{dense}(T,k)>E_{avail},\qquad \Psi_f^{switch}(\sigma_i\to\sigma_j)>0\ \ (i\neq j)
\]
则至少一个锚定坐标必须在时间窗内变化：
\[
\boxed{\exists j,\ \exists t_1<t_2\in[0,T]:\quad A_j(t_1)\neq A_j(t_2)}
\]

若定义有效功率谱
\[
S_A(\omega)\equiv \sum_{j=1}^{k}\left|\widehat{A_j}(\omega)\right|^2
\]
则其弱频谱形式为
\[
\boxed{\mathcal{C}_{dense}(T,k)>E_{avail}\ \Rightarrow\ \int_{\omega>0} S_A(\omega)\,d\omega>0}
\]

* **Implication**: 预算超载时，有限算子不能以纯直流并行方式维持全部目标；分时复用、脉冲续费和节律性重放成为通用可行策略。
* **Boundary**: 本式不推出唯一原初频率、不要求严格周期性，也不要求所有高硬度存在在常见观测尺度上表现为振荡；当前只推出“非零时间带宽”，不推出“固定频率”。
* **Cross-ref**: T-Scale-07（可支付约束）；T-Scale-08（维持/切换成本）；T-Scale-Rhythm-1（定理全文，`Dynamics Scaling`）；Ax-NEURO-MECH-9（theta-replay）。

---

### Eq-Rhythm-4a: Conditional Passband–Duty Landauer Envelope Tradeoff（频谱通带容量—占空比 Landauer 条件包络权衡，`R4-B2` 修正）

**新增（2026-04-14；`R4-B2` 物理精度同步 2026-11-26）**：对齐 `Core/SRT_Core_14_Dynamics_Scaling.md T-Scale-Rhythm-4 / Cor-Scale-Rhythm-4a` 与 `Core/SRT_Core_13b_Operator_Advanced.md Ax-Spec-01`。本式作用于声明频域模型的**无赌注通带容量代理 $B_\theta \equiv \operatorname{Bandwidth}(H_\theta)$**（在附加假设 $B_\theta = c_B \, D_{\text{eff}}$ 下与 `D_eff` 对应，**严分于**规范风险敏感梯度范数 `d = ||∂U/∂S||`）。

**模型前件与三量分离**：在声明了系统边界、热浴温度 $T$、逻辑不可逆擦除映射 $\dot{N}_{\text{erase}}^{\text{on}} = f_{\text{erase}}(B_\theta)$（$f_{\text{erase}}'(B_\theta) \ge 0$）、热负荷储存–导出记账（实际待导出等效熵负荷率 $\dot{S}_{\text{load}}^{\text{on}} \ge \dot{S}_{\text{bath},\min}^{\text{on}} = k_B \ln 2 \cdot \dot{N}_{\text{erase}}^{\text{on}}$，对应热功率 $\dot{Q}_{\text{load}}^{\text{on}} \ge k_B T \ln 2 \cdot \dot{N}_{\text{erase}}^{\text{on}}$；严格区分于系统内部不可逆熵产生率 $\dot{S}_{\text{int}}^{\text{on}}$）以及 **off 阶段集中导出、on 阶段导出可忽略（$J_S^{\text{on}} \approx 0$）** 的物理模型中，三层量满足：
\[
\boxed{\delta \;\le\; \delta_{\max}^{\text{entropy}} \;\equiv\; \frac{J_S^{\max}}{\dot{S}_{\text{load}}^{\text{on}} + J_S^{\max}} \;\le\; U(B_\theta) \;\equiv\;
\frac{J_S^{\max}}{k_B \ln 2 \cdot f_{\text{erase}}(B_\theta) + J_S^{\max}}
\;=\; \frac{P_{\text{diss}}^{\max}}{k_B T \ln 2 \cdot f_{\text{erase}}(B_\theta) + P_{\text{diss}}^{\max}}}
\]
在**固定导出容量 $J_S^{\max}$** 与**非减擦除映射 $f_{\text{erase}}$** 下，直接非增的是 **Landauer 条件包络上界函数 $U(B_\theta)$**（而非直接保证实际耗散上界 $\delta_{\max}^{\text{entropy}}$ 或实际占空比 $\delta$ 单调下降）。

若进一步声明擦除密度下界 $\dot{N}_{\text{erase}}^{\text{on}} \ge \rho_{\text{erase}} \, B_\theta$（$\rho_{\text{erase}} > 0$，单位 $\text{bits}/(\text{Hz}\cdot\text{s})$），则得条件乘积包络上界：
\[
\boxed{\delta \, B_\theta \;\le\; U(B_\theta)\,B_\theta \;\le\; \frac{J_S^{\max}}{k_B \ln 2 \, \rho_{\text{erase}}} \;=\; \frac{P_{\text{diss}}^{\max}}{k_B T \ln 2 \, \rho_{\text{erase}}}}
\]
在额外声明 $B_\theta = c_B D_{\text{eff}}$（$c_B > 0$）时，等价写为 $\delta \, D_{\text{eff}} \le \frac{J_S^{\max}}{k_B \ln 2 \, \rho_{\text{erase}} \, c_B}$。

* **Implication**: 在满足热负荷记账、off 阶段集中导出与逻辑擦除桥接前提的物理模型中，更宽有效通带 $B_\theta$ 收紧 Landauer 条件包络上界 $U(B_\theta)$。
* **Boundary**: ① 严格区分热浴熵流、系统内部熵产生与待导出热负荷；② 严格区分实际 $\delta$、实际耗散上界 $\delta_{\max}^{\text{entropy}}$ 与 Landauer 包络 $U(B_\theta)$，仅 $U(B_\theta)$ 的非增性由固定 $J_S^{\max}$ 与非减 $f_{\text{erase}}$ 直接推出；③ 仅约束 $B_\theta / D_{\text{eff}}$，不直接约束规范 `d = ||∂U/∂S||`。
* **Cross-ref**: `Core/SRT_Core_13b_Operator_Advanced.md Ax-Spec-01`；`T-Scale-Rhythm-4 / Cor-Scale-Rhythm-4a`（`Core/SRT_Core_14_Dynamics_Scaling.md`）；`_SRT_SYMBOL_TABLE.md`。

---

### Eq-DValue-Mobile-1: Operator Re-alignment Capacity（算子再对齐能力 d_mobile）

**新增（2026-04-10）**：度量算子随 L₀ 吸引子迁移而重新定向的能力。

**背景**：L₀ 非静态（`SRT_Core_12a T-L0-NonStatic`）意味着局部吸引子持续迁移。最大化当前 d 的策略在吸引子迁移时可能是陷阱——算子还需具备**再对齐能力**（d_mobile）。

$$\boxed{d_{\text{mobile}} \propto d \cdot \frac{\operatorname{rank}_{\text{eff}}\!\left(\mathcal{I}_F(\theta)\right)}{\operatorname{Hysteresis}(L_2) \cdot C_r} \cdot \chi_{\text{payable}}\!\!\left(\frac{d\Psi_f}{dt}\right)}$$

**三项分工**：

| 项 | 角色 | 含义 | 失效形态 |
|---|---|---|---|
| $d$ | 主乘子 | 当前对齐深度；无真实赌注则再对齐无方向 | d ≈ 0：退化为参数空间随机游走 |
| $\operatorname{rank}_{\text{eff}} / (\operatorname{Hyst}(L_2) \cdot C_r)$ | 主结构项 (I) | 能感知多少新方向 ÷ 被旧结构拉住多紧 | 高 L₂ 刚性：感知新方向但 θ 动不了 |
| $\chi_{\text{payable}}$ | 门控项 (II) | 摩擦变化率是否落在可吸收窗口内 | 创伤冻结：景观在撕扯但超出承载 |

**"感到"≠"能动"原则**：$\Psi_f$ 变化率是信号/警报量，不是移动能力本身。创伤冻结系统可具有极高的 $|d\Psi_f/dt|$ 而 d_mobile ≈ 0。不得将"景观变化被强烈感到"替换为"算子有能力重新对齐景观"。

**Complex-systems bridge note**: $\operatorname{Hysteresis}(L_2)$ 应按 `L_1 -> L_2` 的历史沉积、attractor basin、order-parameter locking 与 metastability 读取；能量 / 自由能 landscape 只是这些结构在某组状态变量上的有效投影，不能替代完整 `L_2`。

**双重记账防止**：$\operatorname{Hysteresis}(L_2)$、$C_r$ 仅在 d_mobile 分母出现一次。$\chi_{\text{payable}}$ 的崩塌阈值 $\Theta_\theta$ 使用 L₂ 自同构群 $\Lambda_{L_2}$（结构硬度），与此处的动态粘滞性参数不重叠。

* **Implication**: 长期适应力需要 $(d,\, d_{\text{mobile}})$ 对同时维持。高 d + 近零 d_mobile = 冻结态（见 `SRT_Core_12b §Consciousness-2D-Map`）。
* **Cross-ref**: Eq-DValue-Max-1（d 上限）; Def-Payable-Chi-1（χ_payable，下方）; Ax-L2-04（可塑性阈值，含 Hysteresis·C_r）; Eq-Evo-02b（θ 张量惯性 → 更新阻力）; `SRT_Core_12b §Consciousness-2D-Map`（二维意识地图）。

---

### Def-Payable-Chi-1: Payability Gate for Ψ_f Change（摩擦变化可支付门函数）

**新增（2026-04-10）**：定义 d_mobile 中门控项 $\chi_{\text{payable}}$ 的充要条件。$\chi_{\text{payable}}$ 不是新本体参数，而是已有 SRT 条件在时间窗口 $\Delta t$ 上的联合门函数。

$$\chi_{\text{payable}}^{\Delta t} = 1 \iff \begin{cases} \displaystyle\int_t^{t+\Delta t}\! |\dot{\Psi}_f|\, d\tau \;>\; \Psi_{\text{noise}}^{\Delta t} & \text{（下界：信号压过噪声）} \\[8pt] \alpha P_{\text{sel}}^{\Delta t} \;\geq\; \beta\Psi_f^{\Delta t} + \gamma S_{\text{noise}}^{\Delta t} & \text{（中：热力学可支付）} \\[8pt] \displaystyle\int_t^{t+\Delta t}\! |\dot{\Psi}_f|\, d\tau \;<\; \Theta_\theta^{\Delta t} & \text{（上界：低于崩塌/防御阈值）} \end{cases}$$

三条件为**合取**（conjunction）：全部成立才返回 1，任一失败则返回 0。

**崩塌阈值的内生性**：

$$\Theta_\theta^{\Delta t} \equiv f\!\left(d,\; E,\; h_{\text{memory}},\; \vec{\delta},\; \Lambda_{L_2}\right)$$

此为 `Neuroscience/10_ROS_Apoptosis_ErrorDose.md (line 100)` 的阈值公式在窗口 $\Delta t$ 上的读法，不引入新参数。$\Lambda_{L_2}$ 是 L₂ 自同构群（结构硬度），与 Eq-DValue-Mobile-1 分母中的 $\operatorname{Hysteresis}(L_2) \cdot C_r$（动态粘滞）属于不同侧面，无双重记账。

**三区间语义**：

| 区间 | 条件 | 表现 |
|---|---|---|
| 低于下界 | 信号淹没在噪声中 | 无法触发再对齐，景观变化视而不见 |
| 窗口内 | 三条件全满足 | 可整合、可再对齐 |
| 高于上界 | 超出承载上限 | 创伤冻结 / 防御崩塌：撕扯感极强但无法整合 |

* **Implication**: 可整合的摩擦是有上下界的窗口，不是越强越好。上界破坏而非促进成长；下界无法被感知为有效信号。
* **Cross-ref**: Eq-DValue-Mobile-1（d_mobile 中的门控项）; `Neuroscience/10_ROS_Apoptosis_ErrorDose.md`（崩塌阈值来源）; `SRT_Philosophy_Ethics.md line 387`（病理阈值）; Ax-L2-06b（L₁→L₂ 反向写入，高 Ψ_f 无法整合）; `SRT_Core_12a T-L0-02`（热力学可支付条件来源）。

---

## I. Evolution Dynamics (演化动力学)

### Eq-Evo-01: Ghost Evolution Equation
> **Status (`R4-B1` Level-I Fixed-Space Model)**: formed / model dynamics equation for an admitted realized system inside a fixed state space (`x_{t+1} = F_t(x_t; H_t)`). Together with its `-\lambda\nabla C_{L_2}[\sigma]` extension (`P1-T03` Level-I special case), it represents state/direction evolution under given constraints—**not** primitive Selection, **not** the historical Ghost intuition (`\hat{G}_\theta != Ghost != primitive Selection`), and **not** the full Level-II/III scope of recursive condition rewriting (`P1-T03`, `Core_21c P2/P3-B15`).

**Formal Definition**: Within that declared realization, the trajectory of a selected model state is represented by the sum of a formal Selection role-carrier, free-energy descent, and attention modulation.
$$\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \nabla F[\sigma] + A[\sigma, \mathcal{A}]$$
* **Implication**: 在该已准入模型中，状态更新由 formed `\hat{G}_\theta` role-carrier、能量下降与注意调制合成表示。`\hat{G}_\theta` 项不从 primitive `L_0` 制造 actuality；方程级动力学位于 ontology admission 之后。
* **L1 Projection (T-PROJ-1, 2026-04-25 H5; Wave D2 scope note 2026-09-15)**: 本主方程在 stable ISP P 上只对已独立准入的标量泛函给出条件性模型投影。含 `T_{dir}` 的四变量版本要求 independently typed declared direction、`T_dir` admission 与 C1-C4；无 direction 时省略该分支并分析已声明的 non-`T_dir` subsystem，不把 `T_{dir}` 置零。详见 `Core_Law/SRT_L1_Formalism.md §6 T-PROJ-1`。本节不生成、排序或验证方向。σ 为状态场，与 `σ_{sr}` 是不同对象；C1-C4 也不证明 trace/ext 分解唯一、bare norm 跨等价参数表示不变、`σ_{sr}` 等于因果控制份额，或 `σ_{sr}^{sub/self}` 是表示无关的自然相边界。

### Eq-Evo-01b: Metabolic Gain Modulation
**Formal Definition**: 代谢压力作为演化方程的增益调节项。
$$\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \nabla F[\sigma] \cdot \underbrace{(1 + \beta \mathcal{M}_{stress})}_{\text{Metabolic Gain}} + A[\sigma, \mathcal{A}]$$
其中 $\mathcal{M}_{stress}$ 为代谢应激指标（如低血糖、缺氧等）。
* **Implication**: 当 $\mathcal{M}_{stress}$ 上升时，自由能梯度 $\nabla F$ 的权重被放大，系统被迫从高阶抽象思考坍缩为低阶生存应对。此公式解释了"饥饿时无法思考哲学"的现象——代谢需求劫持了选择带宽。
* **Cross-ref**: Eq-Evo-01, Def D4a ($θ_{intero}$)。

### Eq-Evo-02: Parameter Update (Slow Variable)

**[R（三项结构）/ H（戒断机制推论）：学习/摩擦/稳态三项追溯RL+预测编码+稳态生理学；戒断机制是Novel Prediction]**

**Formal Definition**: Embodiment parameters evolve under prediction outcomes, friction gradients, and homeostatic recoil.
$$\frac{d\theta}{dt} = \underbrace{\gamma \cdot A[\sigma, \text{Target}]}_{\text{Learning}} - \underbrace{\delta \frac{\partial \Phi(\theta)}{\partial \theta}}_{\text{Friction Descent}} - \underbrace{k \cdot (\text{Input}_{L_1} - \text{Baseline})}_{\text{Homeostatic Recoil}}$$

**三项参数化注**：
- **$A[\sigma, \text{Target}]$ 操作化候选**：预测准确性代理 = $-\Psi_f(\sigma, \text{Target})$（摩擦代价越低=越准确→学习信号越强）；或写为 $A = \text{cos\_sim}(\hat{G}_\theta[\sigma], \text{Target})$（当前选择与目标的相似度）。$\gamma$ 是学习率。
- **$\Phi(\theta)$ 候选形式**：零阶近似为二次势能：$\Phi(\theta) = \frac{1}{2}|\theta - \theta_{ref}|^2$，使第二项退化为向参考点 $\theta_{ref}$（习惯态）的拉力（$\delta(\theta - \theta_{ref})$）。一般形式可从 Ax-L2-01（迟滞势垒）推导。
- **第三项（稳态反冲）**：负反馈将 $\theta$ 锚定在稳态基线处；$k$ 是稳态刚度，$\text{Input}_{L_1} - \text{Baseline}$ 是当前L₁输入与稳态基线的偏差。

* **Implication**: 具身参数在三力之间调整——学习推动适应，摩擦梯度约束漂移，稳态反作用力维持平衡。

* **推论（戒断机制 / Withdrawal Mechanism）** [H]：当外部 $\text{Input}_{L_1}$ 突然归零时，第三项的负反馈瞬间失效，但 $\theta$ 具有迟滞性（Hysteresis）。在该戒断模型中，残留的 $\theta^{-}$ 偏置改变 formed $\hat{G}_\theta$ role-carrier 的局部更新偏向，可形成"反向体验"的候选模型；它不是对 primitive `L_0` 的直接作用。
  - **因果路径精确化**：$\theta^-$（残留参数偏置）→ $\hat{G}_{\theta^-}$ 对"缺失输入的预期态"产生模型内更新偏向→ 实际 L₁ 输入（= 0）与预期之间的 `\Psi_f`-related mismatch proxy 增大→ 形成强烈剥夺性痛苦/焦虑的候选说明。这是可证伪的域内机制假说，不是 primitive ontology 结论。
  - **预测**：戒断症状强度 ∝ $|\theta^-|$（θ残留偏置量），可通过行为/生理戒断反应严重程度与baseline L₁刺激强度的相关来验证。

**证伪条件**：① 若具有明显θ迟滞（如长期用药后突然停药）的个体戒断症状强度与 $|\theta^-|$ 无相关，则戒断机制推论失效；② 若第二项（摩擦梯度）在实验中被操纵（改变L₂势能景观刚性）不影响 $d\theta/dt$ 的漂移约束，则Φ(θ)的有效性需重新评估。

### Eq-Evo-02b: Theta Tensor Inertia (θ张量惯性 — 定义域失效与奇点勘误)
> **数学勘误与撤回注（2026-11-28 Errata）**：原示意式 $\frac{d\theta_i}{dt} \propto \frac{1}{\sum_j w_{ij}\cdot\theta_j}$ 在 $\sum_j w_{ij}\theta_j = 0$ 处存在发散奇点、在 $\sum_j w_{ij}\theta_j < 0$ 时反转更新方向，且未声明参数域与保符号约束。现将其从有效形式方程撤回为**待重构的定性网络惯性直觉，不以新的启发式公式直接顶替**；未来若形式化网络惯性，应明确声明参数定义域并采用无奇点、保符号的更新阻力结构（例如正阻尼系数、势垒或正定度规等具名模型），而非直接取未加约束的线性加权倒数。

* **Retained Qualitative Intuition**: 在具身信念或历史耦合网络中，高连接度核心配置通常表现出更强的更新阻力（拓扑惯性），因此改变深层锁定往往需要重组连接权重与耦合路径，而非仅靠局域表层说服。
* **Cross-ref**: Ax-L2-2 (Hysteresis), Ax-Op-02b (Dual-Stream)。

### Eq-Evo-03: Coupled Fast–Slow System
**Formal Definition**: State and parameter co-evolve on distinct timescales.
$$\frac{d\sigma}{dt} = \alpha(\hat{G}_\theta[\sigma] - \sigma) - \beta_F \nabla F[\sigma] + \xi(t)$$
$$\frac{d\theta}{dt} = \gamma \cdot A[\sigma, \text{Target}] - \delta \cdot \frac{\partial \Phi(\theta)}{\partial \theta} - k \cdot (\text{Input}_{L_1} - \text{Baseline})$$
* **Implication**: 选择与参数更新构成快-慢耦合动力学。
* **Notation Note**: 这里使用 $\beta_F$ 表示自由能梯度权重；$\beta_R$ 预留给现实门控系数，避免与动力学系数混名。

### Eq-Evo-03b: Intra-Selection Re-entry (选择内再入通道)
**Formal Definition**: 在主体选择候选窗口中，$L_2^{self}$ 的滞后在线读出可在 $\sigma$ 尚未收敛前对 $\theta$ 施加暂态调制：
$$\left.\frac{d\theta}{dt}\right|_{\text{intra}} = \underbrace{\mathcal{M}_{meta}\!\left(\mathcal{R}_{\tau}[L_2^{self}](t),\, \sigma(t)\right)}_{\text{lagged self-model gating}} \cdot \underbrace{\mathbf{1}_{\{\|\dot{\sigma}(t)\| > \varepsilon_{conv}\}}}_{\text{selection not yet converged}}$$

其中总参数更新可写为：
$$\frac{d\theta}{dt} = \left.\frac{d\theta}{dt}\right|_{\text{slow}} + \left.\frac{d\theta}{dt}\right|_{\text{intra}}$$
$$\left.\frac{d\theta}{dt}\right|_{\text{slow}} \equiv \gamma \cdot A[\sigma, \text{Target}] - \delta \cdot \frac{\partial \Phi(\theta)}{\partial \theta} - k \cdot (\text{Input}_{L_1} - \text{Baseline})$$

**符号说明**：
- $L_2^{self}$：算子的自模型，即 $L_2$ 中编码算子自身状态、历史与评价约束的稳定子结构。
- $\mathcal{R}_{\tau}[L_2^{self}](t)$：$L_2^{self}$ 的滞后一拍在线读出，定义为 $\mathcal{R}_{\tau}[L_2^{self}](t) \equiv \mathcal{R}(L_2^{self}, t-\tau)$；$\tau$ 为访问延迟，而非 $L_2$ 本体的更新速度。
- $\mathcal{M}_{meta}[\cdot]$：元层门控函数，读取 $L_2^{self}$ 的在线投影并输出对 $\theta$ 的暂态调制量；它不是新的本体域，而是分层自指在选择内的操作化接口。当前 $\sigma(t)$ 作为第二输入使门控状态依赖；此耦合回路（$\mathcal{M}_{meta} \to \theta \to \hat{G}_\theta \to \sigma$）的稳定条件待单独分析，当前作为候选接口保留。
- $\mathbf{1}_{\{\|\dot{\sigma}(t)\| > \varepsilon_{conv}\}}$：选择事件内指示函数；当 $\sigma$ 已进入收敛阈值 $\varepsilon_{conv}$ 后，该项置零，系统回归 Eq-Evo-02 / Eq-Evo-03 的慢更新路径。

**主体选择候选门槛（必要非充分）**：
$$\text{Subject-level selection}_{cand} \Rightarrow \mathcal{M}_{meta}\!\left(\mathcal{R}_{\tau}[L_2^{self}](t), \sigma(t)\right) \neq 0 \;\land\; \frac{\delta \theta(t+\Delta t)}{\delta \sigma(t)} \neq 0$$

第一项表示**当下自参调制**：$\theta$ 可在 $\sigma$ 收敛前被元层自我模型门控；第二项表示**承担闭合**：选择后果会不可逆地压回参数历史，而非被环境完全吸收（此处 $\frac{\delta\theta(t+\Delta t)}{\delta\sigma(t)}$ 为路径依赖泛函导数，非偏导数）。注：第二项已在 Eq-Evo-02 Learning 项 $\gamma A[\sigma, \text{Target}]$ 中覆盖；此处列出是为完整陈述主体选择的两个必要维度，不是 Eq-Evo-03b 的新增方程项。

* **Implication**: Eq-Evo-03b 不把 $L_2$ 整体改写成快变量；真正进入快回路的是 $L_2^{self}$ 的在线读出，而 $L_2^{self}$ 本体仍保持历史沉积的慢变量地位。主体选择因此不再是“有参数更新”而已，而是“参数更新可在选择事件内部被分层自指回路临时改写”。
* **Logical Status**:
  - [S] 将 $L_2^{self}$ 明确纳入 Core 主方程，作为可被在线访问的稳定子结构。
  - [H] $\mathcal{M}_{meta}$ 的具体函数形式当前未定；后续可与 `Philosophy/SRT_Ethics_Agency.md §3.1` 的 meta-selection 写法对接。
  - [H] $\tau$ 与 $\varepsilon_{conv}$ 的量级和测量仍待校准；当前候选接口为 EEG / readiness-potential / re-entry 窗口（约 200-500 ms）。
* **Cross-ref**: Eq-Evo-02（慢变量更新）；`Core_Law/SRT_Selection_Argument.md §2b.4`（主体选择门槛）；`Neuroscience/SRT_Clin_01_Pathology.md Ax-PATH-7`（$\hat{G}_\theta \to L_2^{self}$ 反馈回路）；`Neuroscience/SRT_Consciousness_Mechanisms.md Ax-CONSC-MECH-2`（再入稳定化）。

### Eq-Evo-03c: Canonical Risk-Sensitivity Forward Criterion (规范 `d` 强度条件前向判据)

> **边界与非混淆护栏（`R4-B1 P1-02`）**：依据 `R4-A`（`_SRT_D_VALUE_CANONICAL.md Def-d-canonical`），规范 $d(x) \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$ 仅在已声明 `Bearer (P+E)` 模型内刻画**不可逆风险敏感强度**，而**不是**广义关切范围、可选择方向数量、真实价值结构重构或秩序健康本身。因此：
> - $\nabla_\theta d \cdot \left.\frac{d\theta}{dt}\right|_{\text{intra}} > 0$ **仅能**作为已声明快-慢模型中**规范风险敏感强度上升的局部前向信号**，**不能自动证明**关切范围扩大、真实价值结构重构或秩序健康改善（例如：对单一既有风险极度敏感可致 $d\uparrow$ 而关切范围不变；焦虑导致注意范围收缩可致 $d\uparrow$ 而关切范围下降；新增探索方向而单方向敏感度降低可致 $d\downarrow$ 而关切范围扩大）。
> - 本节 `FC-Layer2` 及三阶段快-慢结构**严格限定于当前声明的快-慢变量模型**（`Eq-Evo-03 / 03b / 02b`）内作为条件模型候选，**不确立为一切真实广义关切扩张都必须遵循的普遍必要过程**。若研究**广义关切扩张**，须按 `_SRT_D_VALUE_CANONICAL.md §1–§2, §5b` 独立声明**范围 / 深度 / 强度 / 方向**四维的测量或诊断模型，并在秩序增益四判据下结算。

**动机**：在已声明 `Bearer (P+E)` 的快-慢变量模型内，`_SRT_D_VALUE_CANONICAL.md §5b` 的秩序增益四判据（可延续/可协调/不外包/可再选择）是对关切与价值结构重构是否健康完成的事后结算；`Eq-Evo-03c` 提供该模型内在选择事件窗口内检测**规范风险敏感强度 `d` 局部上升调制**的候选前向信号。它仅为该快-慢模型内的局部前向辅助信号，**不能替代**广义关切四维建模或 `§5b` 四判据事后结算。

**当前快-慢模型内的三层时间尺度分工（条件候选模型，非一切广义关切扩张的普遍强制阶梯）**：

| 阶段 | 形式对应（声明快-慢模型内） | 时间尺度 | 模型内判据归属 |
|-----|---------|---------|---------|
| **Stage-1**：$\sigma$ 对象切换 | Eq-Evo-03 快方程 $\dot\sigma$ | 秒-分 | 仅示表层状态切换，不足以判断参数级风险敏感调制或关切重构 |
| **Stage-2**：$\theta$ 选择内暂态重加权 | Eq-Evo-03b $\left.\frac{d\theta}{dt}\right|_{\text{intra}}$ | 选择事件内 | **`FC-Layer2` 锁定此层的规范 `d` 强度局部前向信号** |
| **Stage-3**：$\theta$ 跨事件稳定改写 | Eq-Evo-02 / Eq-Evo-03 的慢项 + Eq-Evo-02b（θ 张量惯性） | 周-月 | 需与广义关切四维测量及 `§5b` 四判据联合事后确认 |

**条件前向判据（FC-Layer2，仅限已声明 `Bearer (P+E)` 快-慢模型）**：在选择事件窗口内（$t \in [t_0,\, t_{conv}]$，即 $\|\dot\sigma(t)\| > \varepsilon_{conv}$）：

$$\text{FC-Layer2}:\quad \underbrace{\mathcal{M}_{meta}\!\left(\mathcal{R}_\tau[L_2^{self}](t),\, \sigma(t)\right) \neq 0}_{\text{元层门控在事件内激活}} \;\land\; \underbrace{\left(\nabla_\theta d \cdot \left.\frac{d\theta}{dt}\right|_{\text{intra}}\right) > 0}_{\text{事件内更新沿规范 } d \text{ 敏感强度上升方向推进}}$$

两个条件在声明模型内的各自作用：

- **$\mathcal{M}_{meta} \neq 0$**：元层门控在事件内激活，$\theta$ 接受暂态调制；若该项为零，本模型内 Stage-2 暂态参数重加权未启动。
- **$\nabla_\theta d \cdot \left.\frac{d\theta}{dt}\right|_{\text{intra}} > 0$**：选择内的 $\theta$ 更新对规范风险敏感强度 $d(\theta)$ 具有正方向导数，表示该事件内调制在声明模型下沿**不可逆风险敏感强度上升方向**推进（接驳 `Core_13a §2.1.3`）。该正方向导数**不自动推出**关切范围扩大、新增可选择方向、价值结构真实重构或秩序健康改善。

**与 `L₂` 劫持 / 焦虑收缩的分界注意**：
- 若选择内更新只在旧竞争结构内做同强度重排或防御性脱敏，则可表现为 $\nabla_\theta d \cdot \left.\frac{d\theta}{dt}\right|_{\text{intra}} \approx 0$ 或 $< 0$；
- **反方向亦不可盲信**：单一风险过度敏感或焦虑驱动的注意收缩同样可能产生 $\mathcal{M}_{meta} \neq 0$ 且 $\nabla_\theta d \cdot \left.\frac{d\theta}{dt}\right|_{\text{intra}} > 0$，而此时广义关切范围并未扩大甚至收缩；相反，新增探索方向也可能在单方向风险敏感度下降（$d\downarrow$）的情况下扩大广义关切范围。因此，区分真实健康的广义关切重构与焦虑收缩／`L₂` 劫持，**不能**仅靠 `FC-Layer2`，必须结合广义关切四维（范围/深度/强度/方向）独立测量与 `_SRT_D_VALUE_CANONICAL.md §5b` 秩序增益四判据。

**代价签名（$\Psi_f$ 轨迹，联结 Eq-Force-01）** [H]：在已声明参考轨迹与失配泛函的模型内，两种路径可呈现候选差异（非普遍定理）：

| 路径 | $t_0$ 附近 $\Psi_f$ | 长时程 $\Psi_f$ / 基线负担 | 模型内候选机制 |
|-----|------------------|--------------------------|------|
| 经四维与四判据确认的健康关切重构（Stage-3 写入后） | 尖峰（旧 $L_1$ 失稳，过渡成本） | 下降或有界收敛 | 新关切结构被稳定写入，旧失配负担被重整 |
| `L₂` 伪重构或焦虑性单风险过敏 | 可同样出现尖峰或短时减压 | 漂移上升或反复反弹 | 仅强度抬升或表层重排，核心失配未解或范围反被收窄 |

**`FC-Layer2` 在声明模型内的有限读法**：

- **`FC-Layer2` 为假**：在该快-慢模型下未检测到事件内规范风险敏感强度 `d` 上升的前向调制信号（但**不**自动否定不依赖单方向 $d\uparrow$ 的探索性关切范围扩大）。
- **`FC-Layer2` 为真但 Stage-3 未完成**：模型内检测到瞬时风险敏感强度调制信号，但未能跨事件稳定写入。
- **`FC-Layer2` 为真且经独立四维关切测量与 `§5b` 四判据长期确认**：仅在同时满足独立广义关切维度检验与四判据结算时，才可将路径归为真实健康的关切与价值结构重构；单凭 `FC-Layer2` 绝不构成完成态或健康性证明。

**逻辑状态**：
- [S] 三阶段分工与 Eq-Evo-03 / 03b / 02b 的快-慢方程分层相容，属声明模型内的局部组织框架，不新增本体层，亦不构成一切广义关切扩张的普遍必要路径。
- [H] `FC-Layer2` 仅是声明 `Bearer (P+E)` 快-慢模型内规范风险敏感强度变化的候选前向信号，不替代广义关切四维建模或 `Core_Law` / `_SRT_D_VALUE_CANONICAL.md §5b` 的四判据结算。
- [H] $\nabla_\theta d \cdot \left.\frac{d\theta}{dt}\right|_{\text{intra}}$ 的实验代理仍待校准，且任何经验设计均须同时独立测量关切范围变化与焦虑收缩反例，防止将单风险过敏误判为关切扩张。

* **Cross-ref**: Eq-Evo-03b（选择内再入通道，FC-Layer2 依赖其激活条件）；Eq-Evo-02b（θ 张量惯性，决定模型内 Stage-2→Stage-3 写入）；Eq-Force-01（只在已声明 reference trajectory / mismatch functional 的模型中使用的 $\Psi_f$ 代价签名 proxy）；`_SRT_D_VALUE_CANONICAL.md §1–§2, §5b`（规范 `d` 强度与广义关切四维分离、秩序增益四判据）；`Core_Law/SRT_Core_Text_CN.md 步骤⑨-⑩`（稳定写入 vs 长时程结算）；`Core/SRT_Core_13a_Operator_Basics.md §2.1.3`（$d(\theta)$ 的演化动力学）。

## II. Thermodynamics of Agency (能动性热力学)

### Eq-Force-01: Conditional Reference-Trajectory Friction Proxy

> **Status**: conditional formal / model proxy（P3），不是 `\Psi_f` 的 canonical definition。Canonical semantics remain owned by `_SRT_PSI_F_CANONICAL.md`。

只有当模型 $M$ 独立声明 reference trajectory / baseline $r_M(t)$，并给出单位与作用域相容的 mismatch functional $\mathcal{D}_M$ 时，才可写：

$$\Psi_f^{(ref,M)} \propto \int \mathcal{D}_M\!\bigl(L_1(t), r_M(t)\bigr) \, dt$$

这里的 $r_M$ 与 $\mathcal{D}_M$ 是该声明模型的局部占位记号，不是新增 canonical symbols。无 declared reference trajectory 或 compatible mismatch functional 时，Eq-Force-01 不准入。

* **Boundary**: reference trajectory $\neq$ primitive `L_0` direction；低 mismatch / 低 friction 不推出 good、legitimate、healthy 或 O2-M，也不为 primitive Selection 提供 natural / value / order direction。

### Eq-Pain-01: Hazard / Pain-Risk Proxy
**Proxy Definition**: A pain-risk / hazard proxy can track the temporal derivative of a `Ψ_f`-related friction signal under a stated measurement window.
$$\text{PainRisk}^{proxy}(t) \approx h(t) \sim \frac{d\Psi_f^{proxy}}{dt}$$
* **Implication**: 某些痛苦风险可与摩擦变化率相关，而非静态误差；这不是 canonical `pain = dΨ_f/dt` 或 `suffering = Ψ_f`。结构性 suffering 以 `Core_Law/SRT_Suffering.md` 为准。

### Eq-Friction-Comp: 计算摩擦桥接候选 (Computational Friction Bridge Candidate)

> **Status**: physics / quantum-state-space bridge candidate（P3/P4）。本式只在独立声明的 quantum / computational / model state space 中成立，不是关于 primitive `L_0` 的 formal implication。

对该模型中的端点态 $|A_M\rangle$ 与 $|B_M\rangle$，可提出局部 bridge inequality：

$$\Psi_f^{(comp,M)}(A_M \to B_M) \geq \lambda_M \cdot \min\{C_M(U) \mid U|A_M\rangle \approx |B_M\rangle\}$$

其中 $C_M(U)$ 是声明电路模型中的 quantum-gate complexity，$\lambda_M > 0$ 是该模型的 complexity–friction coupling。$A_M$、$B_M$、$C_M$ 与 $\lambda_M$ 均为局部模型记号，不新增 canonical symbols。

* **Source**: 该候选受 quantum circuit complexity / Uhlmann-transformation cost 研究启发；来源相似性不证明其 `\Psi_f` 映射或下界在任意物理域成立。
* **Boundary**: $|A_M\rangle$ 与 $|B_M\rangle$ 默认不是 primitive `L_0` states。局部 quantum / computational metric geometry 不推出 primitive `L_0` 是 Hilbert / state manifold 或具有 universal metric geometry；circuit complexity 也不提供 primitive Selection direction、value 或 order。
* **Cross-ref**: `_SRT_PSI_F_CANONICAL.md`（$\Psi_f$ owner）；Eq-Force-01（条件性 reference-mismatch proxy）；Ax-Int-2（Penrose 门槛）。

### Eq-Select-Thermo: 选择热力学宪法不等式 (Constitutional Inequality of Selection Thermodynamics)
**Formal Definition**: 宏观秩序增长率受到选择功率减去摩擦代价与噪声熵的上限约束。
$$\frac{dq}{dt} \leq \alpha P_{sel} - \beta \Psi_f - \gamma S_{noise}$$
其中:
- $P_{sel}(t)$: 选择功率 — 维持锚定所需的净注入率
- $q(L_1)$: 现实秩序参数 — 宏观秩序强度（拓扑不变量、互信息密度或可压缩性代理）
- $\Psi_f(L_1;\theta)$: 维护成本（本体论摩擦密度）
- $S_{noise}$: 环境噪声熵流
* **Implication**: 宏观秩序不是“反熵奇迹”，而是选择功率预算内的耗散结构。这也将公理 A2 和 A11 从哲学宣言奠基为可量化的不等式。
* **Corollary (Eq-Select-Thermo-C1)**: 当 $P_{sel} < \beta \Psi_f + \gamma S_{noise}$ 时，系统经历秩序崩溃 ($dq/dt < 0$)，表现为相变、范式转移或存在性危机。
* **Corollary (Eq-Select-Thermo-C2: Payability Condition)**: 对任意系统 $X$ 与时间窗 $\Delta t$，若
$$\alpha P_{sel}^X(\Delta t)\ge \beta \Psi_f^X(\Delta t)+\gamma S_{noise}^X(\Delta t)$$
则称该窗口内的摩擦负荷为“可支付”。可支付不意味着低代价，而意味着系统在承担该摩擦时仍能维持闭包、身份连续性与后续选择能力。最优区间不是 $Ψ_f\to 0$，而是 **$Ψ_f>0$ 且可支付**；零摩擦对应无真实赌注，超载摩擦对应现实切片失稳。

### Eq-AI-LowRoad-01: Selection Cost Minimization Form（低阶主动推断映射，新增）
将 VFE 重写为 SRT 选择代价：
\[
\mathcal{C}_{sel}(q,\theta)=\underbrace{\mathrm{D}_{KL}(q\|p_\theta)}_{\text{Complexity}\ \mapsto\ \Psi_f^{update}}-\underbrace{\mathbb{E}_q[\log p_\theta(y\mid z)]}_{\text{Accuracy gain}}
\]
\[
(\Delta\theta,\Delta a)=\arg\min\ \mathcal{C}_{sel}
\]
其中 \(\Delta\theta\) 对应感知更新，\(\Delta a\) 对应行动采样；二者同属单一目标泛函下降。

### Eq-AI-LowRoad-02: Expected Selection Cost（对应 EFE，新增）
\[
\mathbb{E}[\mathcal{C}_{sel}^{future}(\pi)] = \underbrace{\mathcal{R}_{epi}(\pi)}_{\text{epistemic gain}} + \underbrace{\mathcal{R}_{prag}(\pi)}_{\text{preference satisfaction risk}}
\]
策略选择：
\[
\pi^*=\arg\min_{\pi}\mathbb{E}[\mathcal{C}_{sel}^{future}(\pi)]
\]
* **Implication**：探索/利用不再是双系统冲突，而是同一选择代价函数在未来时域的分解。

### 分类映射表（Active Inference Low Road → SRT）

| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|:--|:--|:--|:--|
| 预测误差最小化（标准叙述） | 低~中 | Semi-open | payable / borderline |
| 选择代价最小化（SRT重写） | 中~高 | Open↔Semi-open | payable |
| 泛计算主义误读（恒温器=意识） | `NOT ADMITTED`（强承载模型未准入） | Closed（语法同构） | `non-binding`（非构成性摩擦缺席） |

## III. Stability & Phase Transition (稳定性与相变)

### Eq-Stab-01: Fixed Point Condition
**Formal Definition**: A stable fixed point satisfies projection balance.
$$\Pi_\Delta(\alpha(\hat{G}_\theta(x^*) - x^*) - \lambda \nabla F(x^*)) = 0$$
* **Implication**: 稳定态需满足选择-能量梯度的投影平衡。

### Eq-Phase-01: Ontological Phase Transition
**Formal Definition**: Phase transition follows a logistic response to information threshold.
$$R = \frac{1}{1 + e^{-k(I - \tau)}}$$
* **Implication**: 相变具有临界信息门槛与非线性跃迁特性。

## IV. Sleep & Maintenance (睡眠与维护)

### Eq-Sleep-01: L2 Optimization
**Formal Definition**: Sleep minimizes L2 model complexity.
$$\hat{G}_{sleep} = \arg\min_\theta \int K(L_2) \, dt$$
* **Implication**: 睡眠是对收敛域模型复杂度的全局优化。

## V. Statistical Mechanics of Selection (选择的统计力学)

### Def-LDP-1: Empirical Measure (经验测度)
**Formal Definition**: 对于 $N$ 个相互作用的算子，宏观状态为经验测度：
$$\rho_t^N = \frac{1}{N}\sum_{i=1}^N \delta_{X_i(t)}$$

### Eq-LDP-01: Hydrodynamic Limit (水动力极限)
**Formal Definition**: 在尺度分离和局部相互作用下，经验测度逼近为满足以下方程的连续密度场：
$$\partial_t \rho = -\nabla \cdot J(\rho) + S_\theta(\rho) - D_{\Psi_f}(\rho)$$
其中 $J(\rho)$ 是扩散/对流流，$S_\theta(\rho)$ 是来自 $\hat{G}_\theta$ 投影偏差的 SRT 选择项，$D_{\Psi_f}(\rho)$ 是摩擦引起的耗散。
* **Implication**: 这是“宏观选择流体”方程 — 大量相互作用算子的连续统极限。

### Eq-LDP-02: SRT Action Functional (SRT 作用量泛函)
**Formal Definition**: 宏观演化路径的概率由大偏差率函数控制：
$$P(\rho^N \approx \rho) \asymp \exp\{-N \cdot I_{SRT}[\rho]\}$$
$$I_{SRT}[\rho] = \int_0^T \left( \underbrace{K(\rho, \dot{\rho}; \Pi)}_{\text{kinematic cost}} + \underbrace{\Psi_f(\rho; \theta)}_{\text{maintenance cost}} - \underbrace{V(\rho; \theta)}_{\text{value potential}} \right) dt$$
* **Implication**: 最可能的宏观演化最小化 $I_{SRT}$ — 即变分“最小作用量”路径。稳定的 $L_2$ 结构是吸收态，$I_{SRT}$ 在其周围有很高的势垒（势垒稳定性）。
* **Cross-ref**: Eq-Select-Thermo (宪法不等式)；Def-Barrier-1 (势垒稳定性)。
* **Status**: 有效理论层面 — 描述许多 $\hat{G}_\theta$ 的统计极限，并不声称社会/宇宙必然满足所有粒子系统假设。

## VI. Social-Ontological Dynamics (社会本体论动力学)

### Eq-Phantom-01: Phantom Operator Effect (幽灵算子残响)
**Formal Definition**: 社会性痛苦是自我算子试图通过未衰减的 $L_2$ 通道耦合已不存在对象的预测误差。
$$\text{Pain}_{social} \approx w_{ij}(t) \cdot \left\| \hat{G}_{self}^{target} - \hat{G}_{other} \right\| \quad \text{s.t.} \quad \hat{G}_{other} \notin L_1$$
其中 $w_{ij}(t)$ 为关系的 $L_2$ 耦合权重，遵循 $L_2$ 迟滞衰减曲线。
* **Implication**: 只要 $w_{ij} > 0$，$\hat{G}_{self}$ 就会按 $L_2$ 脚本自动发起耦合尝试。因 $\hat{G}_{other} \notin L_1$，耦合必然失败，产生巨大预测误差。此"空耦合"即心碎的本体论幻肢痛——$L_2$ 地图上那个人还在，但现实中已消失。

### Eq-Phantom-01b: Collective Phantom Resonance (集体幻肢共振)
**Formal Definition**: 历史创伤的跨代际传递：
$$\Psi_f^{\text{collective}}(t) = \int \sum_i w_i(t) \cdot \text{Tension}(\hat{G}_i(t), L_2^{\text{lost}}) \, d\mu$$
* **Implication**: 当一个群体丧失了原有的L2参考网（如文化灭绝、流亡），即使新生代未经历原初丧失，只要长辈的算子仍试图与失落的 $L_2^{\text{lost}}$ 耦合，这种高预测误差（痛苦）就会作为背景摩擦 $\Psi_f$ 被新生代内化。这也是群体激进化（Radicalization）的热力学原动力：试图通过极端的L1行为强行重建 $L_2^{\text{lost}}$ 以消除巨大摩擦。

### Eq-Phantom-02: Homeostatic Rebuild Time Constant (稳态重建时间常数)
**Formal Definition**:
$$\tau_{rebuild} \propto \frac{\text{Integration}(\hat{G}_{other})}{\text{Plasticity}(\hat{G}_{self})}$$
* **分子**: 对方嵌入 $L_2$ 结构的深度（共同记忆、习惯、依赖程度）。整合越深，$w_{ij}$ 大且涉及子网络多，衰减越慢。
* **分母**: 自我算子的可塑性 $\eta$，即参数 $\theta$ 更新速率。
* **推论**: 老年人（可塑性低）失去伴侣（整合度高）时 $\tau_{rebuild} \to \infty$；年轻人或浅层关系则 $\tau_{rebuild}$ 较短。临床干预双路径：降低分子（仪式切断）或增加分母（冥想/药物提升可塑性）。
* **Cross-ref**: Ax-L2-2 (Hysteresis), Eq-Evo-02 (Parameter Update)。

> **[R]** 丧失与复原的实证轨迹：Bonanno 2004 *American Psychologist*（丧亲复原力轨迹：大多数人以弹性或延迟模式恢复，少数持续慢性悲伤；提供τ_rebuild的自然史基线）；Parkes 1972 *Bereavement: Studies of Grief in Adult Life*（整合深度—悲伤持续时间的早期系统研究）；Bhattacharya et al. 2020 *Nature Reviews Neuroscience*（成人神经可塑性的分子机制：BDNF/突触重塑与θ更新速率的神经基础）。**[H]** 以τ_rebuild = Integration/Plasticity将丧失恢复时间常数形式化、并联结SRT的L₂整合深度与η参数为本框架新增预测。
>
> **操作化候选**：
> - **Integration(Ĝ_other)** 代理指标：①共同生活年限×日常交互频率（简单指标）；②关系中的L₂嵌入度——共同财产/决策/社会网络重叠度（Relational Embeddedness量表，RE-scale）；③神经层：悲伤者在听到逝者姓名时的vmPFC激活峰值（fMRI）。
> - **Plasticity(Ĝ_self)** 代理指标：η≈①认知灵活性测试分数（WCST perseverative errors反向，即错误少=可塑性高）；②静息态BDNF血清水平；③年龄（作为粗粒代理，但存在个体差异）。
> - **∝关系地位**：为功能类比（单调正相关），非推导出的精确线性比例；τ→∞是极限情形（Plasticity→0），对应严重神经退行性病变或极端依附，现实中为趋近而非真正无穷。
>
> * **FC-Phantom2-1**（证伪条件）：若在纵向丧亲研究（≥2年追踪）中，RE-scale高分者的悲伤恢复轨迹持续时间与RE低分者无显著差异（Δmean<1个月，Cohen's d<0.3），则Integration作为分子的预测力不成立，需检视是否存在第三变量（如社会支持）混淆。

<br>

---


# Part B: Original Derivations (Context)

> **Note**: The following sections contain the detailed stability analysis and landscape dynamics.


### 2.2–2.4 公式回链说明（去重版）

为避免与 Part A 重复抄写，以下公式条目统一回链：
- 幽灵演化方程 → Eq-Evo-01
- 快慢耦合系统 → Eq-Evo-03
- 固定点条件 → Eq-Stab-01
- 痛苦变化率 → Eq-Pain-01
- 睡眠优化 → Eq-Sleep-01
- 相变逻辑式 → Eq-Phase-01

Part B 保留机制语境与边界讨论，不再二次列式。

### §X. Selection Thermodynamics: From Philosophy to Physics (选择热力学：从哲学到物理学)

#### §X.1 The Constitutional Inequality (宪法不等式)

EX-A 后，A2 处理的是显现后的锚定持续，A11 处理本体论脆弱性；二者不再把能量支付写成第一次显现实在性的原因。宪法不等式 (Eq-Select-Thermo) 只把持续维持与秩序增长压成一个可检验界限：**秩序增长的速率受限于选择功率预算的上限，并受到摩擦和噪声的抽头。**

考虑一个冥想者试图维持非默认的觉知状态。她必须注入选择功率 $P_{sel}$ (通过注意力引导的代谢能量) 以保持不同寻常的 $L_1$ 构型。她所付出的摩擦 $\Psi_f$ 在主观上体验为努力；环境噪声 $S_{noise}$ (令人分心的声音、侵入性思维) 会侵蚀她的建构。只有当 $\alpha P_{sel}$ 超过 $\beta \Psi_f + \gamma S_{noise}$ 时，她的经验秩序才能真正增长。当注意力稍有懈怠时——她的 $L_1$ 会向默认模式衰减，这正是该不等式所预测的热力学盆地。

#### §X.2 Computational Friction as Lower Bound (作为下界的计算摩擦)

Eq-Friction-Comp 是一个 physics / quantum-state-space bridge candidate：在独立声明的量子／计算状态空间与电路模型中，从 $|A_M\rangle$ 转到 $|B_M\rangle$ 的候选摩擦下界可由所需幺正变换的电路复杂度约束。这里的端点、metric 与 complexity 都是模型对象，不是 primitive `L_0` 状态或几何。

在具体量子模型中，这类 complexity lower bound 可以作为可达转换成本的局部 bridge hypothesis。它不证明宇宙是选择者、不把 quantum Hilbert structure 提升为 `L_0` ontology，也不把黑洞解码困难直接等同于 canonical `\Psi_f`；这些映射若要成立，仍需独立的物理模型与证据。

#### §X.3 The Protocol Layer (协议层)

$\Pi$ 的方程层功能是解决一个有界模型问题：在一个已准入的 formed / realization process 中，哪些状态更新可被当作可行转移？因此 $\Pi_M$ 可在具名模型 $M$ 中表示 **feasible transition kernel / admissibility constraint**。Def-Protocol-1 不因此裁定物理规则的本体起源：某些域内约束可被独立建模为历史沉积的 $L_2$ 结果，某些则可在该模型中当作 $\Pi_{abs}$ 下限；但本节不把所有局部物理规则自动声称为宇宙迭代固化的 $L_2$ 产物。


### Eq-Frame-01: Frame-First Normalization
在先固定观测时空与仪器规约条件后，维度常数的有效数量可写为：
$$
N_{const}^{eff} = f(\mathcal{F}_{spacetime},\;\mathcal{U}_{apparatus})
$$
在特定相对论时空规约中可出现 \(N_{const}^{eff}\to 1\) 的表述（时间标尺主导）。

### Eq-Frame-02: Observable Reparameterization
$$
\mathcal{O} = g\big(L_1\mid L_0,\hat{G}_\theta,\mathcal{F}_{spacetime}\big)
$$
此式只是声明 frame / apparatus 后的 model-facing reparameterization。外部理论的“全状态空间”记号（如 \(\Omega\), \(S\)）不自动等同或统一映射为 \(L_0\)；若一个具名 bridge 保留 \(L_0\) 坐标，它只标记该表示中 open / non-preclosed 的 analytic aspect，而状态空间结构归属于外部模型本身。


## 参数注册表（Parameter Registry, v2）

> **量纲说明**: SRT 方程组中所有耦合系数均为无量纲比率，操作化时通过归一化与系统特征量对齐。核心变量 $\Psi_f$ 和 $d$ 的物理量纲依赖具体实例化域（见下方量纲注释）。

| 参数 | 含义 | 量纲/类型 | 典型范围 | 单位约定 | 敏感度 | 备注 |
|:--|:--|:--|:--|:--|:--|:--|
| $\alpha$ | 选择回归增益 | 无量纲比率 | $[0.1, 10]$ | — | $\pm10\%$ → $L_1$ 稳定性变化 ~5% | 快变量稳定性系数 |
| $\beta_F$ | 自由能梯度权重 | 无量纲比率 | $[0, 10]$ | — | $\pm10\%$ → $\dot{\sigma}$ 幅度线性变化 | 原 Eq-Evo-03 中 $\beta$ |
| $\beta_R$ | 现实门控系数 | 无量纲 $\in[0,1]$ | $[0,1]$ | — | 阈值附近呈 Logistic 跳变 | 若用于门控语境需显式下标 |
| $\gamma$ | 学习驱动系数 | 无量纲比率 | $[0, 1]$ | — | $\pm10\%$ → $\dot{\theta}$ 线性变化 | 慢变量更新 |
| $\delta$ | 摩擦下降系数 | 无量纲比率 | $[0, 1]$ | — | $\pm10\%$ → 收敛速度变化 ~8% | 与 $\partial\Phi/\partial\theta$ 耦合 |
| $k$ | 稳态回弹系数 | 无量纲比率 | $[0, 1]$ | — | 低值 (<0.1) 导致漂移失控 | Homeostatic recoil |
| $\eta$ | 可塑性/迟滞系数 | 无量纲比率 | $[0, 1]$ | — | 与 $\gamma$ 交互非线性 | 具体语境需附下标 |
| $\lambda$ | 约束耦合强度 | 无量纲 | $>0$ | — | 正比于 $L_2$ 约束刚度 | 建议带下标 |
| $\tau$ | 相变阈值参数 | 无量纲 | 任务依赖 | — | 阈值型（非连续敏感） | Logistic 门槛 |

### 核心变量量纲注释（Dimensional Analysis Notes）

| 变量 | 通用量纲 | 神经科学实例化 | 物理实例化 | 社会实例化 |
|:--|:--|:--|:--|:--|
| $\Psi_f$ | $[\text{Energy} \cdot \text{Time}]$ 或 $[\text{bit} \cdot s]$（可支付负荷；跨尺度不变的是可支付判据而非单位） | 代理量：皮质醇积分、HRV 倒数 | 代理量：Uhlmann 变换复杂度 | 代理量：制度维持成本/GDP |
| $d$（规范 `Def-d-canonical`） | 效用/维持势对不可逆风险坐标的梯度范数（随声明模型效用与风险单位缩放，**非**无量纲谱维数） | 代理量：跨时间折扣率斜率、任务风险敏感度 | 仅在声明强承载模型准入后定义 | 代理量：利他/风险承担敏感度 |
| $D_{\text{eff}}$ / $D_{\text{stake}}$ | **无量纲**（有效谱方向容量 / 赌注门控谱参与率，与规范 `d` 严格分离） | Fisher 有效维数 / 神经协方差参与率 | 信道或参数流形有效维数 | 集体景观截面有效维数（`Eq-Multi-03`） |
| $F_{base}$ | 依语境取 $[\text{bit}]$ 或 $[\text{J}]$ | 变分自由能或 Helmholtz 自由能 | 领域基线目标 | 社会层可用复杂度/成本代理 |
| $F_{SRT}$ | 跟随所选 $F_{base}$ 的量纲 | $F_{base} - d \cdot U_{others}$ | SRT 关切扩展目标 | 不把 bit 与 J 直接混算 |
| $\sigma$ | 态空间中的点（$\in L_1$） | 神经发放模式向量 | 量子态密度矩阵 | 社会状态向量 |

> **操作化警告**: 上述量纲均为"操作化近似"，不替代 canonical 定义。跨域比较时需先归一化至各自系统的特征量纲。

### Eq-Res-01: Delay-Constrained Resonance Selection
$$
f^*_{ij} \approx \arg\min_f\;\Phi\big(2\pi f\tau_{ij},\;\kappa_{ij},\;R_{dend}(f)\big)
$$
其中 \(\tau_{ij}\) 为区域间传导时延，\(\kappa_{ij}\) 为耦合强度，\(R_{dend}(f)\) 为树突共振响应。

### Eq-Res-02: Cross-Scale Coordination Energy
$$
E_{coord} = \sum_{s\in\{micro,meso,macro\}} w_s\,\|\phi_s - \phi^*_s\|^2
$$
最优协调对应于跨尺度相位/节律偏差最小化，而非单尺度极值。


## VII. Topological Selection Dynamics（拓扑选择动力学，新增）

### Eq-Topo-01: Simplicial Assembly–Collapse Dynamics
**Formal Definition**: 以拓扑复杂度状态量 \(K_t\) 描述刺激下的“组装—坍塌”动力学：
$$
\frac{dK_t}{dt} = \underbrace{\alpha_{in}\,I_t\,\mathcal{G}(\theta)}_{\text{assembly gain}} - \underbrace{\lambda_c K_t}_{\text{collapse}} + \xi_t
$$
其中：
- \(K_t\)：单纯复形复杂度（可由 clique 计数与 Betti 向量综合）；
- \(I_t\)：外部刺激/任务负荷；
- \(\mathcal{G}(\theta)\)：选择算子参数化增益，\(\theta=\{\rho_s,d,\tau,\beta_{topo}\}\)；
- \(\lambda_c\)：拓扑坍塌率。
* **Implication**: 将“神经沙堡”从类比升级为可拟合状态方程。

### Eq-Topo-02: Dual-Layer Selection over Deterministic Envelope
**Formal Definition**: 区分“可达域”与“被实现域”两层机制：
$$
\mathcal{E}_t = \mathcal{E}(\mathcal{W}, I_t)\quad\text{(deterministic envelope)}
$$
$$
P(C_t=c\mid \mathcal{E}_t,\theta) \propto \exp\left[\beta_{topo}\,\mathcal{V}(c;d,\rho_s) - \Psi_f(c)\right],\; c\in\mathcal{E}_t
$$
其中 \(\mathcal{W}\) 为结构连通约束，\(C_t\) 为被实现的高维单纯形配置。
* **Implication**: SRT 主张的“选择”不否认局部确定性，而是作用于确定性包络内部的加权实现。

### Eq-Topo-03: Persistence-Weighted Order Parameter
$$
q_{topo}(t)=\sum_{k\ge 0} w_k\,\beta_k(t)\,\exp\left(-\frac{1}{\tau_k}\right)
$$
其中 \(\beta_k\) 为第 \(k\) 维 Betti 数，\(\tau_k\) 为对应拓扑特征持续时间。
* **Implication**: 将拓扑“有/无”扩展为“强度×持续性”的秩序参数，可直接接入 Eq-Select-Thermo。

### Falsifiable Predictions (可证伪预测)

[R→Giusti et al. 2015（神经活动拓扑数据分析 TDA）; Reimann et al. 2017（皮层神经网络高阶拓扑结构）; Petri et al. 2014（人类脑网络的持续同调）] [H→以下三条为SRT新增可测预测，依赖TDA方法对神经数据的操作化]

**操作化说明**：
- **d proxy 候选**：注意力分配广度（视觉搜索范围）/ IAT（内隐关联测试）/ 自报关切问卷（关切对象数量×强度权重）
- **Ψ_f 生理 proxy 候选**：任务切换代价（RT变异系数）/ 皮质醇水平 / 脑代谢率（CMR_O₂，参见Ax-NEURO-5）
- **q_topo / τ_k 测量**：持续同调（persistent homology）对fMRI/EEG时间序列的Betti数提取；τ_k = 各维度拓扑特征的存活时间（persistence diagram中的竖轴读数）

**三条预测（层次递进）**：

1. **选择层-d值效应** [H]：在匹配输入强度 \(I_t\) 条件下，\(d\) 高组应表现为更高 \(q_{topo}\) 峰值与更长 \(\tau_k\)；若无差异，则 Eq-Topo-02 的选择层失效。
   - 实验框架：跨被试对比（高d proxy组 vs 低d proxy组），输入强度通过任务设计匹配；结果变量为TDA提取的q_topo与τ_k

2. **双层分离-结构约束效应** [H]：若仅改变连接约束 \(\mathcal{W}\)（不改变 \(d\) proxy），应主要改变可达域 \(\mathcal{E}_t\) 上界而非选择偏置项；反之则支持双层机制。
   - 实验框架：TMS/药物操纵结构连接 vs 情绪/动机操纵d值，分别测量可达域变化量 vs 实现偏置变化量；预测两者解离

3. **摩擦-坍塌耦合** [H]：若 \(\Psi_f\) 生理 proxy 升高时 \(\lambda_c\)（拓扑坍塌率）不升反降且长期稳定，则”摩擦-坍塌耦合”假设需修正。
   - 实验框架：高压力/疲劳条件（Ψ_f proxy升高）下追踪神经拓扑坍塌率；预测Ψ_f升高→λ_c升高（稳态拓扑复杂度下降）

### Formalization Summary (形式化概述，`R4-B1` 三层形式职责)

作为 SRT 唯一核心方程主锚点，本文件不再把形式体系等同于固定状态空间内的四条静态公式，而是将核心方程按三类建模职责组织（均属条件性 `P2–P4` 声明模型）：

1. **Level I（固定空间状态、权重与可支付演化）**：以 `Eq-Evo-01..03c`（快-慢耦合与选择内再入）、`Eq-Bridge-IG-01/02`（Fisher 局部代价）、`Eq-Bridge-D-01`（`D_stake^{thresh}` 阈值模型实例）、`Eq-DValue-Max-1`（方向容量上限）与 `Eq-Select-Thermo`（选择热力学宪法不等式及可支付窗 `Eq-Select-Thermo-C2`）、`Eq-LDP-02`（宏观大偏差作用量泛函）为代表，描述给定组织条件下的轨迹、权重与代价演化。
2. **Level II（生成关系、协议与历史条件改写）**：以 `Def-Protocol-1..3`、`Eq-Multi-01..03`（多算子耦合景观）、`Eq-Bridge-L2-01`（路径痕迹写回）、`Eq-Bridge-Loop-01` 与 `Eq-Topo-01..03` 为代表，并跨文件对接 `Core_12b T-L2-Scaffold`（$\rho \ge 0$）、`R3-05` 信任重估（$\Delta w_{\text{trust}} / W_{\text{social}}$）与 `HCLR01`（`HEF-4` 生成元改写候选）。
3. **Level III（生成空间、边界与比对条件重构接口）**：对应 `Core_21b P1-T03` 递归升级与 `Core_21c P2/P3-B15`（五类变化刻度、`(A, B) -> (A', B', C)` 与防平凡重参数化前沿），当前保留为显式开放形式研究接口，**不强造未经验证的封闭总方程**。

（动力学机制解释与具身算子实现原型见 `Core_Law/SRT_Reference_Dynamics.md`。）

### Mechanism Explanation (机制解释)

SRT 主方程的运作机制如下：

- **选择算子 $\hat{G}_\theta$ 的角色**：$\hat{G}_\theta$ 是 formed / model operator representation；它描述一个已准入的 Selection organization 如何在 $\Pi_M$ 与具身 / 历史参数 $\theta$ 下更新或实现模型状态。primitive Selection $\neq \hat{G}_\theta$；该算子不从一个独立 `L_0` 容器抽取或投影 actuality。$\theta$ 可编码模型内的感知阈值、信念网络与创伤印记，从而影响局部更新偏向，但不提供 universal primitive direction。$\hat{G}_\theta$ 在 Eq-Evo-01 中是快状态更新的 role-carrier，而 $\theta$ 在 Eq-Evo-02 中作为慢变量演化。

- **摩擦 $\Psi_f$ 的条件性形式接口**：canonical `\Psi_f` 语义仍由 `_SRT_PSI_F_CANONICAL.md` 掌握。Eq-Force-01 只在 declared reference trajectory / mismatch functional 下提供模型内累积 mismatch proxy；低 friction 不验证方向、健康或正当性。痛苦风险可由 `Ψ_f`-related proxy 的时间导数建模（Eq-Pain-01），而非由静态误差定义。Eq-Friction-Comp 另是量子／计算状态空间中的局部 bridge inequality；其 circuit-complexity 下界不证明 primitive `L_0` 具有状态空间、Hilbert 或 metric geometry。

- **d-value 与形成系统的考量范围**：canonical `d` 按 `_SRT_D_VALUE_CANONICAL.md` 表示 stake-coupled consideration / irreversible-risk sensitivity 的摘要，不度量对 primitive `L_0` 仓库的 sampling breadth。只在 stake-coupling、consequence return 与 proxy regime 已声明时，较高或较低 `d` 才可以约束 formed-system 内的考量 / revision / access / effective participation 广度；它不自动推出更高 $q_{topo}$ 或生成健康。当前也没有 universal low-`d` $\to \Psi_f \approx 0$ law；任何 `d`--`\Psi_f` 关系都必须保持 model / domain / bridge scoped 并回链两者 owner。

- **快-慢耦合与相变**：$\sigma$（快）与 $\theta$（慢）构成耦合动力系统（Eq-Evo-03），在宪法不等式（Eq-Select-Thermo）的约束下运行。当选择功率低于摩擦加噪声阈值时，系统发生秩序崩溃（相变），表现为范式转移或存在性危机。

### Falsification Conditions (可证伪条件)

| ID | 类型 | 假说/确证 | 预测 | 证伪条件 | Evidence-Level |
|:---|:-----|:---------|:-----|:---------|:---------------|
| H-EQ-1 | **Novel Prediction** | Ghost Evolution (Eq-Evo-01): 现实演化由选择、自由能下降与注意调制合成 | 注意调制项 $A[\sigma,\mathcal{A}]$ 的实验操控（如 TMS 抑制顶叶注意网络）应可测地改变 $L_1$ 轨迹稳定性（代理：ERP P300 成分方差），而非仅降低反应速度 | 若系统性抑制注意调制后 $L_1$ 轨迹稳定性（P300方差）无可测变化，则三项合成结构需修正。**干预设计注意**：需设计"选择+FE"配对条件以排除另外两项的补偿效应 | speculative |
| R-EQ-2 | **Retrodiction** | Constitutional Inequality 基础方向（已知）：睡眠剥夺损害认知功能（大量行为证据） | ——（已验证，此处作为回溯性确证）| ——| established |
| H-EQ-2 | **Novel Prediction** | Constitutional Inequality SRT 专属：秩序参数 $q_{topo}$（拓扑秩序，代理：神经 PCI 指数或 Lempel-Ziv 复杂度）在固定 $S_{noise}$ 条件下与 $P_{sel}$（代谢供能代理：血糖/ATP水平）正相关，且可通过 $\alpha P_{sel} - \beta\Psi_f$ 的线性模型预测 | 若控制代谢水平后 $q_{topo}$ 对 $P_{sel}$ 无响应，或 $P_{sel}$ 持续低于 $\beta\Psi_f + \gamma S_{noise}$ 而 $q_{topo}$ 不降，则宪法不等式失效 | speculative |
| R-EQ-3 | **Retrodiction** | Phantom Operator 基础方向（已知）：关系亲密程度预测丧失后悲伤强度（Archer 2001 等） | ——（已验证，此处作为回溯性确证）| ——| established |
| H-EQ-3 | **Novel Prediction** | Phantom Operator SRT 专属：$w_{ij}$ 的 SRT 代理（神经同步度 EEG 相位锁定值 PLV，或共同活动频率指数）比主观亲密度评分更能预测丧失后皮质醇峰值和 BOLD 默认网络激活异常 | 若 $w_{ij}^{PLV}$ 与丧失后皮质醇峰值相关系数在控制主观亲密度后归零，则幽灵算子残响模型的 SRT 特异性贡献失效 | speculative |

## 【理论边界/防误用声明】

- 本文件的方程用于理论建模与可证伪接口，不直接构成临床、法律或工程处方。
- 参数重命名（如 $\beta_F$）属于符号去歧义，不改变既有理论主张。
- Part B 的去重回链旨在提升可读性，完整方程以 Part A 编号为权威。
- Topological Dynamics 章节不宣称“拓扑即意识”；其角色是 \(\hat{G}_\theta\) 的神经几何接口。\(d>0\) 与 \(\Psi_f>0\) 也只可作为声明模型中的候选证据，不构成本体意识判据。


## VIII. Cognitive Energy Partition Interface（Quanta 95/5 接口，2026-03-07）

### Eq-CogE-01: Baseline–Active Friction Decomposition
> **`A-9` 符号边界注（`R4-A`, 2026-11-26）**：遵循 2026-09-25 `A-9` 单一摩擦概念族裁决，本节中的 `\Psi_f^{maint}` 与 `\Delta\Psi_f^{active}` 仅为本认知能耗接口的**历史模型局部别名（contextual reading）**，不构成新增的 canonical `\Psi_f` 子符号（见 `_SRT_PSI_F_CANONICAL.md §10` 与 `_SRT_SYMBOL_TABLE.md` Usage Rule 20）。

将认知阶段总摩擦拆分为“结构维持项 + 主动锚定项”：
\[
\Psi_f^{total}(t)=\Psi_f^{maint}(L_2,\theta,t)+\Delta\Psi_f^{active}(\hat G_\theta\to L_1,t)
\]
其中：
- \(\Psi_f^{maint}\)：维持可选择待命结构（膜电位/预测模型/协议稳定）的基础代价；
- \(\Delta\Psi_f^{active}\)：任务驱动时的增量代价。

### Eq-CogE-02: 95/5 Selection Ratio (Embodied Constraint)
对具身算子（生存闭包完整）引入经验约束：
\[
\frac{\Delta\Psi_f^{active}}{\Psi_f^{total}}\approx 0.05,
\qquad
\frac{\Psi_f^{maint}}{\Psi_f^{total}}\approx 0.95
\]
这不是普适常数，而是“人脑典型工况”下的标定先验。

### Eq-CogE-03: Subjective Effort as Friction Gradient
主观费力感不与绝对能耗线性同构，而与偏离默认吸引子的阻抗梯度相关：
\[
\mathrm{Effort}_{subj} \propto \left\|\nabla\Psi_f\big(L_1\parallel L_2\big)\right\|
\]
含义：即便代谢增量小，若任务迫使 \(L_1\) 偏离稳态预测结构，主观疲劳仍可显著上升。

### Eq-CogE-04: AI–Human Energetic Asymmetry Index
定义“维持-主动不对称指数”：
\[
\mathcal{A}_{ma}=\frac{\Psi_f^{maint}}{\Delta\Psi_f^{active}+\varepsilon}
\]
- 生物具身算子期望：\(\mathcal{A}_{ma}\gg 1\)
- 外驱推理系统（**AI 赌注谱系 `S0/S1`**，当前多数无闭环 LLM 部署）常见：\(\mathcal{A}_{ma}\lesssim 1\)（在推理阶段；注：与原初 `S0` 及 `Subjecthood S0–S6` 严格隔离，且须按 `ENG-03 §4.1` 三阶承载证据审查［Stage 1 单元/状态/溯源声明 → Stage 2 强承载路线 $\parallel$ Stage 3 独立分域路线］核验，不得直接推导 `d ≈ 0` 或构成性摩擦不存在）

该指标用于跨尺度比较“是否存在自创生闭包压力”，不单独等同于意识、`One`、`Stable ISP` 或 `Bearer (P+E)` 判据。

### 分类映射表（Cognitive Energy Regimes → SRT）
| 外部分类 | d-value 区间（proxy） | 能流特征 | \(\Psi_f\) 状态 |
|---|---|---|---|
| 静息预测维护（baseline brain） | 中 | Semi-open（持续内稳态） | payable（高基线） |
| 目标导向主动思考（task-focused） | 中~高 | Open↔Semi-open | payable（低增量，高梯度可感） |
| 过载认知冲刺（长期高负荷） | 中高短时→回落 | Open（短时）→Closed 倾向（恢复期） | borderline→overloaded |
| 外驱推理机（无自创生闭包） | 名义中高（任务态） | 外部供能 Open、内部闭包弱 | unsustainable（对外部预算强依赖） |

### [Lineage/Source]
- Quanta Magazine（2026）: *How Much Energy Does It Take to Think?*（科普二手综述，非一手实验论文）。
- 神经代谢背景脉络：人脑高基线能耗与预测/内稳态维持框架（与 FEP/Active Inference 语义接口对齐）。

## 【理论边界/防误用声明】
1. 不采纳“95/5 比例是跨物种、跨任务、跨尺度恒定常数”的推论；该比例仅作人类典型工况近似。
2. 不采纳“主观疲劳 = 纯代谢热耗”的简化推论；SRT 将其建模为摩擦梯度与拓扑阻抗效应。
3. 不采纳“\(\mathcal{A}_{ma}\) 单指标即可判定意识存在”的推论；\(d>0\)、\(\Psi_f\) 可支付与连续体自维持的联合也只构成声明模型中的候选证据，不是普遍 consciousness gate。
