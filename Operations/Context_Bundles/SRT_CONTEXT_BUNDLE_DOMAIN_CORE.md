---
id: SRT-CONTEXT-BUNDLE-DOMAIN-CORE-2026-11-26
type: context_bundle
status: active
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
generated: 2026-11-26
source_commit: 31c23e20c
source_branch: canon/r4-c2-physics-cross-scale-generation-2026-11-26
source_dirty: false
inputs_digest: 2de9734a3735ab21
---

# SRT 核心动力学上下文包

> **这是什么**：由 `scripts/build_srt_context_bundles.py` 从 SRT 仓库自动拼装的上下文包。
> 收录核心动力学的 claim-status 护栏、领域导航、CompactCore 主线。
>
> **这不是什么**：不是新的 canonical 文件，不是摘要，不是改写。每个来源文件的正文
> 逐字保留；脚本只把 YAML frontmatter 转成显式 provenance 头。**若本包与仓库中的
> 来源文件冲突，以仓库为准**——本包是快照，会随仓库演进而过期。

## §0 生成信息

| 项 | 值 |
|---|---|
| 生成日期 | 2026-11-26 |
| 来源 commit | `31c23e20c` |
| 来源分支 | `canon/r4-c2-physics-cross-scale-generation-2026-11-26` |
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
| 1 | `Core/SRT_Core_14_Dynamics_Scaling_CompactCore.md` | 2026-11-26 |

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
> 本包是 **单领域支持包**（claim-status 护栏 + 导航 + CompactCore），**不含定义源**。
> 下面的分类是**生成器的判断**，不是 registry 的原话；每行都附依据供复核。
> 「registry 提及」「Registry §C」两列是机械判定的事实。

### 已收录

**展开层**（1 个）

| 文件 | 分类依据 | registry 提及 | Registry §C |
|---|---|:---:|:---:|
| `Core/SRT_Core_14_Dynamics_Scaling_CompactCore.md` | frontmatter claim_mode=mixed | ✓ | — |

### 未收录支持文件

**Registry §C priority 点名、文件存在、但本包未收（19 个）**——回答涉及它们时本包不足以单独裁定（已显式分流条目附去向）：

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
- `Core/SRT_Core_22_Equations.md` — 已拆至独立 `FORMAL` 路线（`Operations/Context_Bundles/SRT_CONTEXT_BUNDLE_FORMAL.md`）；默认 `SPINE` §0.5 保留方程目录索引与检索指针
- `Core/SRT_Core_21_Minimal_Axioms.md`
- `Core/SRT_Core_21b_Constitutive_Theorems.md`
- `Core/SRT_Core_21c_Bridge_Hypotheses.md` — 已移至按需桥接层（P2/P3/P4，按需直接读仓库原文件）；默认 `SPINE` §0.5 保留 B01–B14 条目标引与检索指针
- `Core/SRT_Core_14_Dynamics_Scaling.md`
- `Core_Law/SRT_Reference_Dynamics.md`
- `AI/SRT_AI_01_Ontology.md`
- `Core/SRT_OPEN_TENSIONS.md`

**⚠ 高严重度：registry 提及但文件不存在（1 个）**——指向已删除、拼错或尚未创建的路径。**这类条目不会被静默过滤掉**，因为它本身就是一种 manifest 差异：

| 失效路径 | 说明 |
|---|---|
| `Core_21_Formal_Axioms.md` | 见 §0.2 G4：这是 `Core/SRT_Core_21_Formal_Axioms.md` 的行文简写，非真实路径 |

**registry 提及、文件存在、但本包未收（97 个）**——多为领域主轴、
展开层与 PH-SS 护栏文件，按需走对应路线包或直接读仓库，不在本包路线内：

<details><summary>展开完整清单</summary>

- `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_SPINE_MINIMAL_KERNEL_L0L1L2_REFLEXIVE_FACETS_2026-09-24.md`
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


> **注意**：本包**不含** canonical 定义骨架（`Spine` / `L0` / `One Formation` / `d` / `Ψ_f` / `T_dir` 定义、
> `P0/P1` 核心公理、符号表），亦**不含** `Core_22` 主方程正文，因此**仅凭本包不得裁定任何 SRT 术语的定义**。
>
> 需要裁定定义时，请**改用骨架路线**——新开一次对话，只装
> `SRT_CONTEXT_BUNDLE_SPINE.md`（其 §0.5 亦提供主方程索引与按需桥接指针）；
> 需要查阅 `Core_22` 主方程正文时，请改用独立形式方程路线 `SRT_CONTEXT_BUNDLE_FORMAL.md`。
> **不要在本包之上再叠加骨架包**：叠加会稀释注意力或超出上下文预算（见 `README.md` 的预算表）。各路线在默认整包意义下互斥（是切换关系，不是整包叠加关系）；若具备仓库直读能力，仍可围绕具体研究问题按需联合读取局部方程与对应定义 owner 原文件。



---

## FILE: `Core/SRT_Core_14_Dynamics_Scaling_CompactCore.md`

| 字段 | 值 |
|---|---|
| path | `Core/SRT_Core_14_Dynamics_Scaling_CompactCore.md` |
| id | SRT-CORE-14-COMPACT-CORE |
| claim_mode | mixed |
| status | active |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | - |
| last_commit | 2026-11-26 |

**权威判读**：混合层——含 bridge/lab 内容，按各条自带的 claim level 读。

**dependency**：[SRT-CANONICAL-REGISTRY, SRT-CORE-14, SRT-D-VALUE-CANONICAL, SRT-CORE-22]

<!-- 以下为原文逐字保留 -->

# SRT Core 14 — Dynamics & Scaling Compact Core

> **定位**：本文件是 `Core/SRT_Core_14_Dynamics_Scaling.md` 的紧凑主干版（已随 `R4-B2` 同步）。  
> **用途**：用于快速把握 SRT 跨尺度五机制、容量代理与动力学接口的最短核心骨架。  
> **关系**：不替代原文；原文保留长篇机制推演、接口批次、案例扩展与 annex 沉积。

## 1. 核心问题与跨尺度五机制分工（`R3-08 / R4-B2`）

`Core 14` 解决的是 SRT 中的跨尺度接口问题：

> **不同尺度上的选择动力学与组织结构，通过哪些不同机制彼此相容与转承？**

严格区分五项独立跨尺度机制，**严禁将所有跨尺度接口泛称 `Proxy`**：
1. **装配（Assembly）**：依赖重组形成新整体有效组织（不单独等于 `One`）；
2. **归一化（Normalization）**：条件性调整相对作用与资源分配（非所有装配必要条件）；
3. **有效作用接口（Effective Action Interface）**：已形成整体在声明映射下参与粗粒化比较（`P3-Scale-01 / T-Scale-02C1`）；
4. **`Proxy`（中介转承）**：满足对应条件时中介转承生成关系；
5. **`Delegation`（委托）**：具主体与规范条件时的选择域委托与责任转承（须核查成员 $C_i$ 非外包与可再选择性，`O2-M = HOLD`）。

---

## 2. 跨尺度结构相容候选（P3）

### 2.1 Self-Similar Selection Candidate
\[
\pi_\lambda \circ \hat{G}_\theta
\approx
\hat{G}_{\theta,\lambda} \circ \pi_\lambda
\]

含义：
- 只有在状态空间、尺度映射、保留观测量、比较范数和容差均已声明时，才能检验选择与粗粒化是否近似交换
- 量子测量、神经决策、社会选择或宏观稳定可以接受“是否共享选择语法”的比较；它们并未被证明为同一机制

旧式 \(\hat{G}_{S_2}=\Lambda\circ\hat{G}_{S_1}\circ\Lambda^{-1}\) 只在 \(\Lambda\) 是可逆表征变换时保留为严格共轭候选。通常的粗粒化是多对一映射，不得预设 \(\Lambda^{-1}\)。旧 `\Delta S=H(L_0)-H(L_1)` 与“所有尺度共同满足最小作用”均不再承担证明。

> **注（P3-B06／P3-B07）**：当前跨尺度共同项只到选择—约束—可支付性语法，不是熵量、单位、主体性或意识同一。见 `Core/SRT_Core_21c_Bridge_Hypotheses.md`。

这不是说所有尺度对象或机制相同，而是把结构相容性作为一个可失败的 P3 接口：不满足近似交换条件时，撤回的是跨尺度桥，不是 P0/P1 核心。

### 2.2 P3-Scale-NB1：首个有界实例

神经除法归一化只输出相对响应。通向任务行为选择，必须另外冻结候选身份映射与神经读出，声明阈值／证据累积或采样规则及执行门，并在 held-out 条件下同时通过误差容差、rival 判别增益和具名干预跟踪。广义“归一化 → 行为选择”为红灯；上述合同是尚待数据转绿的黄灯 P3 接口。局部通过也不推出 actualisation、agency、subjecthood 或 consciousness。

---

## 3. 跨尺度容量代理（`D_eff` / $B_{\text{cap}}$）与规范 `d` 严格分离（`R4-A / R4-B2`）

### 3.1 Capacity Bandwidth Proxy vs Canonical `d`
几何/信息论容量代理（$B_{\text{cap}}$ / $D_{\text{eff}}$）**不需要 `Bearer (P+E)` 强承载准入**，但具体跨尺度比较仍须显式建立相容的度量、状态空间与尺度映射：
\[
B_{\text{cap}}(\hat{G}_\theta) \equiv \text{declared channel/manifold capacity bandwidth proxy under } \Psi_f
\]

规范 **$d(x) \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$**（`_SRT_D_VALUE_CANONICAL.md`）则严格限定于已独立建立 `Bearer (P+E)` 不可逆风险承载的模型，刻画**风险敏感强度**，**严分于**无赌注容量 `D_eff`、赌注谱参与率 `D_stake` 与广义关切四维（范围/深度/强度/方向），退出旧式单标量 `d` 最大化叙事。

### 3.2 三尺度分工

- **量子 / 物理域**：相干窗口与可分辨态空间有效维数（`D_eff` 容量代理；规范 `d` 为 `NOT ADMITTED / NOT APPLICABLE`）
- **生物 / 认知域**：感官/通道容量 `D_eff` 与在已建立 `Bearer (P+E)` 模型下准入的规范 `d`、`D_stake` 及广义关切四维
- **宇宙 / 几何域**：宏观相干与拓扑自由度代理（物理投影类比；规范 `d` 为 `NOT ADMITTED / NOT APPLICABLE`）

最重要的边界是：
> 跨尺度可比的是具名容量/结构代理，不是把规范风险梯度 `d` 或意识赋值外推至量子与宇宙域。

在声明的生物/认知模型中，`d`、`\Psi_f` 与 formed `\hat G` 均不单独或合取构成意识的普遍必要或充分条件。

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
- 跨尺度可比较的是具名 capacity / structure proxy，不自动是 canonical stake-coupled `d`
- 意识不是跨尺度默认属性
- proxy compatibility、`d`、`\Psi_f` 或 formed `\hat G` 的单项与合取均不在本文件建立 consciousness
- consciousness / phenomenality admission 由独立 owner 承担，exact sufficiency 保持 OPEN

所以：
- 量子可有相干带宽，不等于有主观体验
- 宇宙可有拓扑整合，不等于有拟人化意识

---

## 9. 最压缩结论

`Core 14` 的主干可以压缩成五句话：

1. **跨尺度关系区分装配、归一化、有效作用接口、`Proxy` 与 `Delegation` 五类机制；结构相容（`P3-Scale-01`）是可失败的 P3 候选，不是普遍同构定理。**
2. **几何/信息容量代理（`D_eff` / $B_{\text{cap}}$）不需要 `Bearer (P+E)` 强承载准入（但跨尺度比较仍须建立相容度量与尺度映射），严格区分于须经 `Bearer (P+E)` 准入的规范风险敏感强度 `d`、赌注谱 `D_stake` 与广义关切四维。**
3. **现实演化由自由展开、选择锚定与耗散三项共同决定。**
4. **对象边界来自误差、摩擦与切换成本的平衡，而非绝对刻线。**
5. **即使跨尺度相容成立，也不推出跨尺度泛心；意识的精确充分性保持 OPEN，额外维度仅可作候选证据。**

---

## 10. 阅读路径

- 全量原文：`SRT_Core_14_Dynamics_Scaling.md`
- split 导航：`Dynamics_Scaling_Split/README.md`
- annex 导航：`Dynamics_Scaling_Annex/README.md`
- d-value 规范：`../_SRT_D_VALUE_CANONICAL.md`
- Core 主方程：`SRT_Core_22_Equations.md`
- canonical 总注册表：`../CANONICAL_REGISTRY.md`
