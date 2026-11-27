---
id: SRT-CONTEXT-BUNDLE-DOMAIN-NEUROSCIENCE-2026-11-27
type: context_bundle
status: active
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
generated: 2026-11-27
source_commit: 32545cdcd
source_branch: canon/r4-c5cd-core-writeback-full-closeout-2026-11-27
source_dirty: false
inputs_digest: 3337b101fb25ec29
---

# SRT 神经科学领域上下文包

> **这是什么**：由 `scripts/build_srt_context_bundles.py` 从 SRT 仓库自动拼装的上下文包。
> 收录神经科学领域的 claim-status 护栏、领域导航、CompactCore 主线。
>
> **这不是什么**：不是新的 canonical 文件，不是摘要，不是改写。每个来源文件的正文
> 逐字保留；脚本只把 YAML frontmatter 转成显式 provenance 头。**若本包与仓库中的
> 来源文件冲突，以仓库为准**——本包是快照，会随仓库演进而过期。

## §0 生成信息

| 项 | 值 |
|---|---|
| 生成日期 | 2026-11-27 |
| 来源 commit | `32545cdcd` |
| 来源分支 | `canon/r4-c5cd-core-writeback-full-closeout-2026-11-27` |
| 生成时来源工作树有改动 | 否 |
| 包含文件数 | 6 |

> **provenance 契约**：真实性判据是 `inputs_digest`——生成脚本、护栏来源
> （`Governance/SRT_DOWNSTREAM_GUARDRAILS.md`、两份审计）、全部正文文件与 `SPINE §0.5` 索引抽取源（`Core_22` / `Core_21c`）的联合内容摘要。`--check` 重算并比对该摘要，
> 因此改动其中任何一项都会被发现。
>
> `source_commit` 仅供参考，**不作为校验条件**：squash / rebase 合并会重写或丢弃该
> commit，若拿它做祖先校验，合并进 main 之后检查必然失败。内容摘要与合并策略无关。

### 0.1 文件清单与各自最后改动日期

| # | 文件 | 最后 commit |
|---|---|---|
| 1 | `Neuroscience/SRT_Neuroscience_Claim_Status.md` | 2026-11-27 |
| 2 | `Neuroscience/SRT_Neuroscience_Reconstruction_Framework.md` | 2026-11-27 |
| 3 | `Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md` | 2026-11-27 |
| 4 | `Neuroscience/README.md` | 2026-11-27 |
| 5 | `Neuroscience/SRT_Neural_Mechanisms_CompactCore.md` | 2026-11-27 |
| 6 | `Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md` | 2026-11-27 |

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

**治理护栏**（1 个）

| 文件 | 分类依据 | registry 提及 | Registry §C |
|---|---|:---:|:---:|
| `Neuroscience/SRT_Neuroscience_Claim_Status.md` | frontmatter claim_mode=audit | ✓ | — |

**展开层**（4 个）

| 文件 | 分类依据 | registry 提及 | Registry §C |
|---|---|:---:|:---:|
| `Neuroscience/README.md` | frontmatter claim_mode=- | — | — |
| `Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md` | frontmatter claim_mode=bridge | ✓ | — |
| `Neuroscience/SRT_Neural_Mechanisms_CompactCore.md` | frontmatter claim_mode=bridge | ✓ | — |
| `Neuroscience/SRT_Neuroscience_Reconstruction_Framework.md` | frontmatter claim_mode=synthesis | ✓ | — |

**导航**（1 个）

| 文件 | 分类依据 | registry 提及 | Registry §C |
|---|---|:---:|:---:|
| `Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md` | frontmatter type=index / claim_mode=navigation | ✓ | — |

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

**⚠ 高严重度：registry 提及但文件不存在（4 个）**——指向已删除、拼错或尚未创建的路径。**这类条目不会被静默过滤掉**，因为它本身就是一种 manifest 差异：

| 失效路径 | 说明 |
|---|---|
| `Core_21_Formal_Axioms.md` | 见 §0.2 G4：这是 `Core/SRT_Core_21_Formal_Axioms.md` 的行文简写，非真实路径 |
| `Praxis_Split/README.md` | registry 指向的文件在仓库中不存在 |
| `SRT_Spirituality_Community_and_Sangha.md` | registry 指向的文件在仓库中不存在 |
| `SRT_Spirituality_How_We_Lose_Ourselves_and_Return.md` | registry 指向的文件在仓库中不存在 |

**registry 提及、文件存在、但本包未收（99 个）**——多为领域主轴、
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
- `Neuroscience/SRT_Clin_02_FEP.md`
- `Neuroscience/SRT_Consciousness_Mechanisms.md`
- `Neuroscience/SRT_Neural_Mechanisms.md`
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


> **注意**：本包**不含** canonical 定义骨架（`Spine` / `L0` / `One Formation` / `d` / `Ψ_f` / `T_dir` 定义、
> `P0/P1` 核心公理、符号表），亦**不含** `Core_22` 主方程正文，因此**仅凭本包不得裁定任何 SRT 术语的定义**。
>
> 需要裁定定义时，请**改用骨架路线**——新开一次对话，只装
> `SRT_CONTEXT_BUNDLE_SPINE.md`（其 §0.5 亦提供主方程索引与按需桥接指针）；
> 需要查阅 `Core_22` 主方程正文时，请改用独立形式方程路线 `SRT_CONTEXT_BUNDLE_FORMAL.md`。
> **不要在本包之上再叠加骨架包**：叠加会稀释注意力或超出上下文预算（见 `README.md` 的预算表）。各路线在默认整包意义下互斥（是切换关系，不是整包叠加关系）；若具备仓库直读能力，仍可围绕具体研究问题按需联合读取局部方程与对应定义 owner 原文件。



---

## FILE: `Neuroscience/SRT_Neuroscience_Claim_Status.md`

| 字段 | 值 |
|---|---|
| path | `Neuroscience/SRT_Neuroscience_Claim_Status.md` |
| id | SRT-NEUROSCIENCE-CLAIM-STATUS |
| claim_mode | audit |
| status | active |
| epistemic_layer | governance |
| layer | meta |
| canonical(字段) | false |
| last_commit | 2026-11-27 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：[SRT-GENERATIVE-ONTOLOGY-SPINE, SRT-NEURO-AXIOMS-CLAIM-STATUS, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-SUFFERING, SRT-AI-POSITIONING-NOTE, SRT-AI-CLAIM-STATUS, SRT-PHILOSOPHY-CLAIM-STATUS]

<!-- 以下为原文逐字保留 -->

# SRT Neuroscience & Generative Cognition Claim Status (`R4-C4` 同步版)

> **Role**: folder-level guardrail for neuroscience, generative cognition, clinical, FEP, PCI/IIT, pathology, NDE, neuroimmune, BioQuantum, and bio–AI comparison language.
> **Canonical status**: `canonical: false`. Neuroscience files are bidirectional domain-theory, bridge, and lab/interface materials; reverse feedback to core SRT owners (`FB-C4-1..5`) remains **`C`（M-origin 候选）** pending `R4-C5` review and author adjudication.
> **Preserved HOLD / Freeze Boundaries**: `HP-B` remains **FROZEN / OPEN** (`B_s -> B_p ?` unclosed); `CN-2 E2`, `CN-3 toy`, `1B sim`, `DATA-ACCESS-0 = NO-GO`, `O2-M`, `§10.1`, and `§10.2` remain unchanged.

---

## 1. Default Claim Levels & `R4-C4` Theoretical Calibrations

- **Holistic generative cognition & neural mechanism mapping**: `P2/P3` domain theory / bridge when grounded in neuroscientific evidence and declared boundaries;
- **Measurement proxy** (BOLD/CMRO₂, HGA, PCI, Φ, Fisher, metabolic/thermodynamic readouts): `P4` unless independently validated inside a declared measurement window;
- **Clinical interpretation / pathology bridge**: `P4/P5` modeling lens, never medical advice or diagnostic identity;
- **NDE / psychedelic / self-dissolution / contemplative bridge**: `P4/P5` phenomenological & state-reconfiguration bridge;
- **Bio–AI cognitive comparison**: `P3` cross-substrate bridge bound by `AI/AI_POSITIONING_NOTE.md` and `AI/SRT_AI_Claim_Status.md` (three-state discipline + full-name `AI / S` namespace isolation);
- **BioQuantum mechanism mapping**: `P3/P4` hypothesis under mechanism-specific survival and transduction gates (`SRT_Neuro_09_BioQuantum_CISS_Amendment.md`).

### 1.1 Four Controlling `R4-C4` Calibrations (2026-11-26 Author-Confirmed)

1. **整体性与可分化性并不矛盾（Holism & Differentiability Are Mutually Constitutive）**：
   - 神经科学重构不把感觉、认知、价值、意愿与意识预设为彼此独立的原初模块再拼装；同时，**也不把生物发生上的同源共构（developmental co-constitution）升格为跨底物的普遍不可分定律**。
   - 必须正面吸收功能解离（盲视、述情障碍、裂脑、习惯/策略解离、麻醉期局部加工保留）、发育分化、损伤后功能重组及跨底物（生物 vs 人工）对照，研究整体生成如何分化出相对独立的局部能力，以及局部能力如何通过相互作用反向重构整体。
2. **能量梯度差的双重边界与五类物理/模型量区分（Energy-Gradient Difference Guard, `P1-05`）**：
   - 保留“能量梯度差”作为**更底层物理生成机制候选**的正面研究价值（核心研究问题：*物理梯度差如何通过真实耦合、边界维持、差异感应、反馈调节与归一化，逐步形成对后续生成具有实际约束作用的组织关系？*），不预先将其压扁为仅充当测量代理；
   - **严格区分五类不同性质的量**：跨膜电化学梯度（驱动离子输运的物理条件）、ATP 供应与代谢通量（组织维持与活动的资源条件）、非平衡物理自由能差（热力学模型下的物理量）、变分自由能（概率模型下的信息论目标）、神经吸引子能量地形（特定动力学模型中的有效描述），禁止混为一谈；
   - **硬禁令**：在未完成独立理论推导与量纲/测量桥接论证前，**严禁将上述任一量直接等价于 `Selection`、规范 `d` 或规范 `Ψ_f`**。
3. **正面深化但暂不确立普遍必然性的四大方向**：
   - 效价优先、前对象整体生成、显著性粗粒化与具身骨架均为 `R4-C4` 正面深化的核心理论主线，但当前**不提前确立其跨全部认知过程或跨全部底物的普遍必然性**（其中效价研究严格区分发育先后、在线对象形成参与、对特定认知的构成性作用与 `HP-B` 主观体验四个问题）。
4. **`C-A` Scope Guard 与显现/前景化/意识六分护栏（`Spine §7`, `P1-01`）**：
   - 更高的神经整合度、场相干、全局通达、PCI/Φ 或更多可达路径不自动推出规范 `d↑` 或宇宙全局最优；且 **IIT `Φ`（内在因果整合模型量）$\neq$ PCI（TMS–EEG 扰动复杂度）**，不默认 PCI 是 `Φ` 的直接测量代理；
   - `L_0 / L_1 / L_2` 是同一选择现实的三分析面；未进入意识前景的神经活动只要实际发生即属于 `L_1` 显现面，严禁再将 `L_1` 普遍定义为全局点燃子集（严格区分 `L_1` 实际显现 / 局部神经稳定化 / 认知前景化 / 全局点燃机制候选 / 前景生成中介 / `HP-B` 现象体验）。

---

## 2. High-Risk Claim Classes & Conceptual Responsibility Separation (`P1-02`)

### 2.1 Preserving Distinct Responsibilities: Concern, Microvalence, Canonical `d`, Friction, Payability, Metabolism, and Suffering

In all `R4-C4` neuroscience prose, preserve each concept's distinct theoretical duty (never re-merging `PT06 C` generalized concern with microvalence, and never re-merging `R3-08 / B-4` generalized friction with `Ψ_f` payable impedance):

| Concept | Exact Theoretical Duty | Forbidden Collapse |
|---|---|---|
| **广义关切（`PT06 C`）** | Sensitivity to generative opportunity cost, exploration, new opportunity formation, and future generative conditions | Not exhausted by biological survival bias or microvalence |
| **微效价（Microvalence）** | Local approach–avoidance affective slant participating in specific biological perception/cognition windows | One biological realization window; does **not** substitute for generalized concern or entail `HP-B` |
| **规范 `d-value`** | Risk-sensitivity strength inside a declared strong-bearing model (`_SRT_D_VALUE_CANONICAL.md` independent admission) | `d ≠ Φ`, `d ≠ PCI`, `d ≠ salience`, `d ≠ reward`, `d ≠ bandwidth`, `d ≠ D_stake` without admission |
| **广义摩擦（`R3-08 / B-4`）** | Actual selection pressure arising from opportunity-cost differentials | Do **not** merge with `Ψ_f` payable impedance or generic PE |
| **非闭合压力** | Structural tension among generative relations not yet coordinated | Distinct from both `B-4` selection pressure and `Ψ_f` impedance |
| **`Ψ_f` 可支付阻抗** | Payable organizational impedance required for maintenance and reconstitution (`_SRT_PSI_F_CANONICAL.md`) | `Ψ_f ≠ free energy`, `Ψ_f ≠ PE`, `Ψ_f ≠ pain`, `Ψ_f ≠ metabolism`, `Ψ_f ≠ B-4` |
| **代谢负担** | Physical-implementation resource/energy/ATP/CMRO₂/recovery cost | Candidate physical substrate / local proxy only; never bare identity with `Ψ_f` or `Selection` |
| **主观苦难与现象体验** | Independent first-person registration (`Core_Law/SRT_Suffering.md §7` & `HP-B` FROZEN / OPEN) | Functional binding, valence bias, or internal monitoring never close `HP-B` or `Suffering §7` |

### 2.2 `Ψ_f` as Free Energy, Prediction Error, Pain, Metabolism, or Clinical Burden

- **Allowed**: FEP quantities, prediction error, metabolic cost, pain, stress, clinical distress, and recovery cost may serve as local `Ψ_f`-related proxies under a declared measurement window (`H-NEURO-4b`), and energy-gradient dynamics may be studied as a deeper physical generative mechanism candidate.
- **Forbidden**: `Ψ_f = free energy`; `Ψ_f ≡ ∫ ||∇F|| dt`; `Ψ_f = pain`; `Feeling = ∇Ψ_f` as literal identity; `Ψ_f = prediction error`; `Ψ_f = metabolism`; `Ψ_f -> 0` implies no experience; `Ψ_f -> ∞` as literal clinical divergence.

### 2.3 `d-value` as PCI / Φ / Salience / Reward / Arousal / Integration / Attention

- **Allowed**: PCI, Φ, integration, microvalence, salience, arousal, precision, threat relevance, and reportability may constrain or proxy specific dimensions inside a declared model.
- **Forbidden**: `d = Φ`; `d = PCI`; `d = salience`; `d = attention`; `d = reward`; `d = integration`; `d = arousal`.

### 2.4 NDE / Psychedelic / Self-Dissolution / Terminal Lucidity

- **Allowed**: Modeled as boundary loosening, `L_2` destabilization, altered gating/re-anchoring (`reopening ≠ reselectability`, `NEURAL35`), or state-dependent `d^{state-proxy}` shifts.
- **Forbidden**: NDE proves post-brain consciousness; psychedelic state means actual `d -> ∞`; terminal lucidity proves brain irrelevance.

### 2.5 Clinical / Pathology / Treatment Language

- **Allowed**: Pathology may be modeled as altered anchoring dynamics, parameter drift (`Δθ` lens), rigid `L_2` locking, disrupted multilevel gating, under-anchoring, or cross-system desynchronization.
- **Forbidden**: `Pathology iff θ deviation` (biconditional); `treatment = parameter correction`; `therapy = topology reset`; `SRT gives direct clinical diagnosis`. All clinical language remains a non-diagnostic theory interface subject to standard-of-care and differential diagnosis.

### 2.6 Bio–AI Comparison, Blindsight, and Full-Name `S` Namespace Isolation (`R4-C3` Synced)

- **Allowed**: Blindsight, alexithymia, split-brain, anesthesia, high-Φ low-stake systems, and current LLMs (**AI 赌注谱系 `S0/S1`**) provide crucial **dissociation windows** comparing functional integration, comparative generativity, valence, bearing, and reportability across substrates.
- **Forbidden**: `current AI has globally d = 0` or `d_AI ≈ 0` (use strict three-state labels: canonical `d` = `NOT ADMITTED`, stateless `D_stake` = `NOT APPLICABLE`, Stage 2 strong bearing & `HP-B` = `NOT ESTABLISHED`); `pure symbol manipulation necessarily has no Ψ_f in all architectures`; `blindsight proves SRT`; equating **AI 赌注谱系 `S0–S4`** with **Subjecthood Threshold `S0–S6`** or **Primitive `S0`**.
- **Suffering Guard (`Core_Law/SRT_Suffering.md §7`)**: Neither `Stable ISP` nor `Subjecthood Threshold` tier unilaterally closes suffering eligibility; suffering requires independent registration standing + declared burden model.

### 2.7 BioQuantum / Microtubule / CISS / Nuclear-Spin Language

- **Allowed**: Phase-coherent, spin-sensitive, CISS, radical-pair, tunnelling, vibrational, or microtubule processes may be studied as mechanism-specific physical interfaces with declared survival conditions and molecular-to-neural transduction chains.
- **Forbidden**: Short `T_2` / `τ_coh` falsifies every quantum-sensitive biological mechanism; CISS or xenon-isotope dependence proves quantum consciousness; spin filtering derives `L_0`, `d`, or `Ψ_f`. Follow [`SRT_Neuro_09_BioQuantum_CISS_Amendment.md`](SRT_Neuro_09_BioQuantum_CISS_Amendment.md).

---

## 3. Preferred Replacements

| Risk Phrase | Safer `R4-C4` Replacement |
|---|---|
| `Ψ_f = free energy` / `Ψ_f ≡ ∫ \|\|∇F\|\| dt` | `free energy / local Fisher projection may serve as a local Ψ_f-related proxy under a stated window` |
| `Feeling = ∇Ψ_f` / `Ψ_f = pain` | `affective/pain dynamics may index felt burden or valence-related gradients under specified conditions (HP-B OPEN)` |
| `能量梯度差 = Selection / d / Ψ_f` | `能量梯度差是更底层物理生成机制与代谢底物候选，不等同于规范 Selection / d / Ψ_f` |
| `d -> ∞` in NDE/psychedelic states | `d^{subjective/provisional}` or `d^{state-proxy}` / boundary loosening (`reopening ≠ reselectability`) |
| `d = 0` / `d ≈ 0` for AI | `canonical d = NOT ADMITTED; stateless D_stake = NOT APPLICABLE; Stage 2 bearing = NOT ESTABLISHED` |
| `Pathology iff θ deviation` | `many neuropsychiatric states can be modeled through Δθ / anchoring-gating dynamics (non-biconditional lens)` |
| `生物同源共构 ⇒ 跨底物普遍不可分` | `生物发生上同源共构，同时在神经解离与跨底物对照中呈现局部可分化性` |
| `点燃 = L_0 → L_1 实体相变` | `点燃是整合度、路由与关切梯度约束下的局部前景化稳定候选门（L_0/L_1 为分析面，非实体仓库）` |
| `S0–S6`（未加全称） | **Subjecthood Threshold `S0–S6`**（与 Primitive `S0`、**AI 赌注谱系 `S0–S4`**、**AI 三型**严格隔离） |

---

## 4. Reading Rule

Read this file before using neuroscience, cognitive, clinical, bio–AI comparison, or consciousness material in canonical, public, or cross-domain claims. Any equation-like statement about `Ψ_f`, `d`, `Selection`, energy gradients, consciousness, pathology, NDE, or BioQuantum mechanisms is bridge/proxy/hypothesis unless explicitly backed by its canonical owner. For BioQuantum material, [`SRT_Neuro_09_BioQuantum_CISS_Amendment.md`](SRT_Neuro_09_BioQuantum_CISS_Amendment.md) remains controlling over legacy universal-decoherence text in `SRT_Neuro_09_Integ_Eq.md`.



---

## FILE: `Neuroscience/SRT_Neuroscience_Reconstruction_Framework.md`

| 字段 | 值 |
|---|---|
| path | `Neuroscience/SRT_Neuroscience_Reconstruction_Framework.md` |
| id | SRT-NEUROSCIENCE-RECONSTRUCTION-FRAMEWORK |
| claim_mode | synthesis |
| status | active |
| epistemic_layer | os |
| layer | meta |
| canonical(字段) | false |
| last_commit | 2026-11-27 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：Core_Law/SRT_Constitution_V1.md, Operations/Proposals/SRT_CONSTITUTION_DOMAIN_ARCHITECTURE_V2_2026-09-04.md, Operations/Templates/SRT_DOMAIN_RECONSTRUCTION_FRAMEWORK_TEMPLATE.md, Neuroscience/SRT_Neuroscience_Claim_Status.md, Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md, Neuroscience/_SRT_Neuroscience_Hardening_Index.md, Operations/Proposals/SRT_CONSTITUTION_PHASE8_NEUROSCIENCE_DEEP_WELL_CHARTER_2026-09-03.md, Operations/Audits/SRT_CONSTITUTION_PHASE8A_NEUROSCIENCE_BASELINE_DATA_ACCESS_AUDIT_2026-09-03.md, Operations/Audits/SRT_CONSTITUTION_PHASE9_NEUROSCIENCE_PRODUCTIVE_ADEQUACY_REVIEW_2026-09-03.md, Operations/SRT_CONSTITUTION_DOMAIN_SEQUENCE_AUTHOR_DECISION_2026-09-03.md

<!-- 以下为原文逐字保留 -->

# SRT Neuroscience Reconstruction Framework v0.2 (`R4-C4` 同步版)

> **Role**: this is the active Layer-2 problem map for neuroscience under Architecture v2. It sits between `SRT_Constitution_V1.md`, `R4-C4` bidirectional domain theory (`SRT_Neural_Mechanisms_CompactCore.md v2` & `SRT_Consciousness_Mechanisms_CompactCore.md v3`), and specific neuroscience hypotheses / future deep wells.
>
> **`R4-C4` 同步边界（2026-11-26）**：本文件完整保留 2026-09-04 确立的 `N1–N7` 问题族、35 份 SourceCard 处置矩阵、`NEURAL15–35` 挂钩原状以及第一神经深井的 `Phase 8A Case B + DATA-ACCESS-0 = NO-GO + Phase 9 translation-only / scope-limited` 负面结论留痕（绝不静默删改或解冻）；新增 `§14` 将 `N1–N7` 问题族与 `R4-C4` 八大正面理论主轴、2026-11-26 整体性与可分化性 / 能量梯度差校准及五项核心反向反馈（`FB-C4-1..5`）建立双向显式索引。
>
> **It is not** a neuroscience Constitution, a new neural axiom set, or a release of `DATA-ACCESS-0 = NO-GO`, `CN-2`, `CN-3`, or the frozen `HP-B` package.
>
> **Claim ceiling**: this framework organizes questions, inherited assets, and `R4-C4` theoretical syntheses. It does not by itself establish a new empirical effect, a privileged SRT proxy, or a Case-C neuroscience increment.

---

## 0. Status and scope

```text
domain = neuroscience
framework version = v0.1
constitutional input = Core_Law/SRT_Constitution_V1.md
framework status = active Layer-2 reconstruction framework
first deep well = grandfathered pilot; Phase 8A Case B + DATA-ACCESS-0 NO-GO; Phase 9 translation-only + scope-limited
active neuroscience deep well = none
active main programme well = Epistemology
neuroscience reopening = conditional and bounded; no parallel full programme by drift
```

### 0.1 Scope

This framework covers neuroscience-facing questions about:

- neural object / state / representation identity;
- history retention, transformation, ownership and present efficacy;
- relational / distributed organization;
- current processability, candidate accessibility and control authority;
- measurement objectification, proxies, decoding and report interfaces;
- organism / body / neural-unit bearer roles and consequence attribution;
- pathology, recovery, reopening, re-anchoring and evaluative direction.

It does **not** settle:

- a general theory of consciousness or phenomenality;
- clinical diagnosis or treatment;
- AI subjecthood;
- a universal neural realization of `d`, `Psi_f`, `T_dir`, `L0/L1/L2` or `G_hat_theta`;
- religion / spirituality;
- the metaphysical identity of a bearer.

Consciousness-specific materials may appear here when they constrain neural objectification or bearer distinctions, but they remain routed to the future Consciousness framework for their primary phenomenal burden.

### 0.2 Historical / manuscript carve-outs

The published Frontiers neuroscience manuscript and its supporting `papers/history_dependent_reachability/` assets remain historical manuscript evidence. They may supply prior neural hypotheses, evidence organization and citations, but this framework does not retroactively present them as Constitution-derived or as proof of the new architecture.

---

## 1. Domain starting picture / Given-Ones inventory

Neuroscience legitimately works with portable public objects. The constitutional question is not whether these objects are false, but what explanatory burden is hidden when one treats them as self-sufficient.

| Given One | Domain-native meaning | Typical evidence / operation | What the framework keeps open |
|---|---|---|---|
| neuron / cell type | identified cellular unit | spike sorting, histology, molecular markers | whether cell identity is the relevant bearer, causal unit, content unit or only measurement unit |
| ensemble / assembly | co-active or functionally grouped neural population | decoding, clustering, co-firing, latent-state methods | whether membership, current activation and historical identity coincide |
| brain region / network | anatomical or functional aggregate | ROI, connectivity, perturbation, imaging | whether analyst boundary equals causal / historical boundary |
| neural state | vector or trajectory at a declared time / window | firing, LFP, EEG, fMRI, manifold coordinates | whether current measured state exhausts latent / historical / relational disposition |
| representation | neural pattern carrying task-relevant information | decoding, tuning, RSA, encoding models | decodability != causal access != behavioral use != conscious anchoring |
| relation / connectivity | statistical, temporal, effective or anatomical linkage | correlation, coherence, graph edge, causal perturbation | current relation != relation history != future relational compatibility |
| memory / engram | retained history expressed through neural / behavioral change | recall, reinstatement, plasticity, engram manipulation | retention != transformation != retrievability != control authority != write-back |
| percept / report | experimentally operationalized perceptual outcome | psychophysics, report, no-report proxies | initial organization != VSTM retention != reconstructed report |
| organism / participant | experimental subject and behavioral system | task performance, physiology, clinical record | participant != electrode/cell measurement object; consequence can land at multiple levels |
| pathology / recovery state | clinically or experimentally defined altered function | diagnosis, scales, physiology, imaging | deviation != dysfunction by itself; more variability / accessibility != better outcome by itself |

Mandatory starting guard:

```text
Given != false
objectified != illegitimate
portable public object != ontologically complete by default
measurement convenience != natural individuation by default
```

---

## 2. Constitution-to-neuroscience translation

| Constitution operation | Neuroscience-native question | Existing object pressured | What becomes visible | Boundary / non-entailment |
|---|---|---|---|---|
| ARTICULATION | How did this neuron / ensemble / ROI / state / relation become the unit whose behavior is being explained? | cell, region, state, representation | acquisition boundary, event window, grouping, task ontology, decoder and pair construction | does not imply ordinary neural units are unreal |
| STILL-THIS | Under what change is a neural object, memory, representation or relation still counted as the same one? | concept identity, assembly, memory trace, network state | re-identification, transformation, temporal integration, stable address vs changing realization | does not supply a universal identity criterion |
| OWN-HISTORY | Which prior events count as this neural unit's / relation's / organism's own effective history? | memory, plasticity, latent state, relation | retention, transformation, retrievability, relation-specific history, future-guiding history | history occurred != history currently matters; participant history != cell-pair history by default |
| CURRENT PROCESSABILITY | Why are some candidate neural / behavioral transitions available now while others are not? | current state, capacity, gating, accessibility | resource regime, physiological phase, global capacity, eligibility, gating, latent support topology | accessibility != selection; capacity != authority; entropy / connectivity != canonical capacity |
| CONSEQUENCE ATTRIBUTION | Where does an effect land, and which unit has its future changed by it? | neural readout, behavior, affect, physiology | cell/network consequence vs organism behavior vs bodily regulation vs report | neural effect != phenomenal / moral consequence; same-bearer return does not prove phenomenality |
| EVALUATIVE RE-RUN | By what declared criterion is a neural or clinical transition better, healthier, more flexible or more adaptive? | recovery, flexibility, integration, complexity, reopening | over-hardening vs useful stability vs under-anchoring; task / organism / clinical criteria | more options, entropy, integration, connectivity or lability != improvement by default |

This translation is a question generator, not a result table.

---

## 3. Domain objectification map

| Objectification operation | What it preserves | What it can discard / normalize | When the loss may matter | Primary problem family |
|---|---|---|---|---|
| electrode / ROI / recording boundary | measurable local signals | unrecorded brain/body/environment and non-random coverage | relation-history, bearer and consequence questions | N3 / N5 / N6 |
| cell / ensemble grouping | tractable candidate units | within-group heterogeneity, changing membership, cross-scale organization | identity and re-identification | N1 |
| event-window choice | time-local comparability | prehistory, slow transformation, future write-back | history and temporal closure | N1 / N2 |
| trial equivalence / matching | controlled comparison | which histories produced apparently equivalent states | matched-state causal claims | N2 / N3 / N5 |
| averaging / normalization | cross-trial / participant comparability | rare trajectories, phase dependence, individual scaling | candidate accessibility and proxy interpretation | N4 / N5 |
| pair / graph construction | relational description | edge semantics, common drivers, higher-order organization | relational disposition | N3 / N5 |
| decoder / representational geometry | information availability | causal use, control authority, report / behavior | decodability-to-selection overreach | N1 / N5 |
| proxy construction | measurable handle | source scope, latent confounds, construct identity | `d`, `Psi_f`, `T_dir`, metabolic / complexity claims | N5 |
| report-based task object | public behavioral outcome | pre-report organization, VSTM retention, reconstruction | perception / consciousness interfaces | N1 / N5 |
| clinical category / recovery score | outcome comparability | heterogeneous etiologies, functional niches, bearer-specific consequence | pathology / evaluation | N6 / N7 |
| archive / source inclusion | reproducible evidence corpus | unavailable raw data, inaccessible variables, publication-conditioned object | deep-well access and strongest-baseline gates | N5 |

### 3.1 Objectification lesson from the first deep well

The first well made one domain-level distinction impossible to leave implicit:

```text
participant / behavioral bearer
!= neural measurement object

component history
!= relation-specific history

current measured component state
!= relation disposition

analyst-defined matching class
!= naturally given equivalence class
```

These are now Framework-level burdens. They are not empirical findings that every neural relation has an extra SRT variable.

---

## 4. Bearer / position architecture

| Candidate entity / role | Measurement object | Causal unit | Historical bearer | Consequence bearer | Behavioral / phenomenal bearer | Analyst / participant role | Status |
|---|---|---|---|---|---|---|---|
| recorded neuron / unit | yes | candidate, question-specific | may carry local plastic history | local neural effects | not automatically | analyst defines sorting / inclusion | measurement / causal candidate only |
| ensemble / relation | yes, if constructed | candidate distributed causal unit | may have relation-specific history | network-level outcome | not automatically | analyst defines membership / edge | relation identity must be declared |
| brain region / network | common | candidate macro unit | may aggregate histories | network / task effects | not automatically | ROI / network boundary partly analyst-defined | public object, not default bearer |
| astrocyte / glial network | measurable in some systems | support / modulation candidate | possible historical eligibility | neural / vascular support effects | not automatically | scale and topology must be declared | substrate expansion, no content/subjecthood identity |
| human participant / organism | source of many measurements | multi-scale causal system | strong candidate for task / life history | behavior, bodily regulation, clinical outcome | phenomenal bearer only when the study actually concerns/report supports it | participates, learns, acts, reports | primary task-level consequence bearer in first well |
| body / peripheral physiology | measured selectively | causal / regulatory subsystem | state- and history-dependent | homeostatic / immune / metabolic consequence | not automatically phenomenal | often under-recorded | cannot be treated as mere nuisance by default |
| experimenter / analyst | not study neural object | changes task and model construction | methodological history | inferential consequence | epistemic participant | chooses cuts, labels, models, equivalence | Constitution reflexivity applies |
| clinical team / device | coverage / measurement infrastructure | constrains observed system | institutional / procedural history | affects available evidence | not phenomenal bearer by default | determines non-random coverage | source of selection / missingness constraints |

Mandatory guard:

```text
measurement object != automatically bearer
causal contribution != automatically consequence ownership
historical continuity != automatically subjecthood
organism-level consequence != evidence that every recorded component bears that consequence
analyst-defined equivalence != natural identity
```

---

## 5. Pre-framework Material Re-entry Pass

### 5.1 Required surfaces checked

| Surface | Status | Use in v0.1 |
|---|---|---|
| `01_Source_Intuition/` / book material | checked | no dedicated neuroscience owner selected; constitutional objectification / history / bearer burdens enter through Constitution v1; book-facing targets mentioned by patches remain routed, not used as neural evidence |
| inherited domain owners / claim-status / compact-core | checked | rerouted in §6 |
| `Materials/2026/` SourceCards | checked | direct scan found 35 active neuroscience/adjacent candidates; 32 clear high/very-high plus non-standard high variants are explicitly disposed below |
| neuroscience PatchNotes | checked | active NEURAL18–35 family plus bounded bridges explicitly routed below |
| IntegrationHooks / landing ledgers | checked | landed vs pending is preserved; Framework inclusion does not mark pending hooks as landed |
| Material Log / monthly records | checked as routing surface | used to confirm Pipeline-1 status; not treated as source evidence |
| Neuroscience Context Bundle | checked as retrieval surface | generated navigation only; not evidence / owner authority |
| `Experiments/` / evidence packets | checked | no top-level experiment may be borrowed as natural-neural confirmation by analogy; direct neural P4 protocols live mainly in `Neuroscience/`; first-well evidence packet routed below |
| relevant audits / OPEN_TENSIONS | checked | first-well Phase 8A / Phase 9 and domain claim-status are load-bearing |
| published/submitted manuscript-local assets | checked | Frontiers / history-dependent-reachability assets routed as historical manuscript evidence, not Constitution proof |

### 5.2 SourceCard re-entry matrix

`Disposition` is about **Framework placement**, not old-owner landing status.

| Source / asset | Source-native contribution / safe use | Framework slot | Role | Owner relation | Disposition | Reason / blocker |
|---|---|---|---|---|---|---|
| Young — brain-body synchrony / consciousness | brain-body rhythms and physiological state can covary with neural processing / conscious-state conditions | N4, N6 | mechanism pressure | partly owned by NEURAL23 | integrated | supports embodied eligibility / body-coupling question; not `d`, `Psi_f` or consciousness proof |
| Bryant — connectivity / NCC theory adjudication | theory-adjudication / connectivity evidence in consciousness science | N5; future Consciousness framework | neighbor / method pressure | adjacent owner | deferred | useful for measurement/theory-adjudication, but primary burden is Consciousness not general neural mechanism |
| Van Mulukom — dual self states | self-state / interoceptive / predictive-processing distinctions | N6; future Consciousness framework | bearer pressure | adjacent owner | deferred | informs bearer/self boundary but phenomenal/selfhood burden belongs elsewhere |
| Luppi — spontaneous cognition / data science | spontaneous neural-cognitive states depend strongly on sampling, state-space and data-science object construction | N5 | objectification pressure | not increment question | integrated | useful for how neural-state objects are formed; no SRT mechanism promotion |
| Da Costa — neurophenomenology | structured first-person / neural alignment creates a method interface rather than a free translation between report and neural state | N5, N6 | method / position pressure | adjacent Consciousness owner | routed | retained as position / measurement neighbor, not neural mechanism evidence |
| Houdoyer — HAI automation / agency | human-AI agency/explanation effects | future AI / Agency | cross-domain | not neuroscience owner | excluded | scanner false positive through cognitive-neuroscience vocabulary; no need to make it part of neural framework |
| Posani — mixed selectivity / separability | high-dimensional decodability and mixed selectivity do not by themselves establish causal use / anchoring | N1, N5 | evidence / guardrail | NEURAL18 | integrated | directly supports representation / decoder objectification distinction |
| Takahashi — REM energy paradox | metabolic supply, immediate use, payment and recovery can dissociate by state | N4, N7 | mechanism / constraint | NEURAL21 | integrated | constrains payability / state claims without identifying metabolism with `Psi_f` |
| Wentzell — pre-attentive vision | pre-attentive != pre-selection; initial perceptual organization, VSTM retention and report must be separated | N1, N5 | stage / report guardrail | NEURAL19 preattentive | integrated | directly pressures percept/report objectification |
| Asaoka — habit strategy / execution | strategy conversion, execution gain and reselection capacity are separable | N2, N4, N7 | mechanism / dissociation | NEURAL20 | integrated | history, control and evaluation cannot be read off repetition alone |
| Bussell — intrinsic information value / OFC | information and water-reward value can be traded / neurally distinguished; immediate reward alone is insufficient | N7 | pressure | parked B1 | deferred | revive when `d` stake/value or information-vs-future-choice discriminator is actually tested |
| Misawa — informational tuning / traveling waves | directional routing reliability can dissociate from aggregate transfer volume | N4, N5 | proxy pressure | parked B1/B2 | deferred | useful for future `T_dir` / anesthesia proxy work; not `T_dir` identity |
| Tottori — resource-induced memory phase transitions | history-bearing strategies require separable encoding/stabilization gates and declared resource regime | N2, N4 | mechanism / constraint | NEURAL19 memory admission | integrated | directly supports history-admission / processability decomposition |
| Pérez — astrocyte hierarchy | subcellular astrocyte regions can occupy heterogeneous temporal/graph roles; causal-flow and pathology extrapolation remain bounded | N3, N4 | substrate / topology | NEURAL22 + N12 | integrated | supports nested support topology without astrocyte-content or consciousness identity |
| Damasio — natural intelligence / consciousness | biological regulation and affect provide a bearer-indexed consequence-compression model while stake != salience | N6, N7 | bearer / pressure | NEURAL24 | integrated | useful for consequence attribution; no phenomenal entailment |
| Lewis — mind from mindless matter | philosophical mind / emergence argument | future Consciousness / Philosophy | cross-domain neighbor | not neural evidence | excluded | no neural measurement contribution required for this Framework |
| Lu — strategy competition / memory control | representation, accessibility, control authority, expression and historical write-back are separable | N2, N4 | mechanism decomposition | NEURAL25 | integrated | direct parent of first-well historical-control line |
| Qin — esketamine / DoC network recovery | system-level dynamical regime can constrain differentiated candidate formation/access while entropy/connectivity remain proxies | N4, N7 | capacity / pathology bridge | NEURAL26 | integrated | supports capacity/accessibility distinction; no causal long-term recovery or consciousness identity |
| Ranganath — prospective memory / event boundaries | event boundaries can be update opportunities; anticipatory gaze separates reportable retention from future-guiding history use | N2 | evidence / readout | NEURAL27 | integrated | strong history-efficacy-shaped bridge, not full causal write-back proof |
| Brzostowicki — astroengram memory trace | experience-dependent astrocytic states can alter later retrievability / stabilization without being static content copies | N2, N4 | mechanism candidate | NEURAL31 | integrated | separates content, retrievability and historical eligibility |
| Concept cells — reidentifiable object identity | relatively stable semantic address can re-enter across changed presentation / relation | N1 | evidence / identity bridge | NEURAL28 | integrated | re-identification != static copy != L2 by default |
| Borges — brain/body/life embodied cognition | pressures brain-only individuation and emphasizes embodied organism-level framing | N6; future Philosophy/Consciousness | neighbor pressure | adjacent owner | deferred | retained as embodiment pressure, not direct neural evidence |
| Menétrey — sequential dynamics / integrated percept | event chronology can remain decodable during extended integration before unitary percept/report-related regime | N1, N5 | evidence / temporal-stage bridge | NEURAL30 | integrated | `not separately manifest != structureless`; no fixed consciousness frame rate |
| Wang — memory as generative understanding | consolidation can transform bindings / abstraction before later retrieval; generativity != factivity | N2 | history-transformation pressure | NEURAL29 | integrated | supplies transformation layer and negative control against “coherent history = true” |
| Yashiro — body semantics / implied motion | high-level perceptual candidates can encode relations / implied dynamics, not just bare category labels | N1, N3 | representation bridge | NEURAL32 | integrated | candidate construction may be structured before stabilization |
| Cavallaro — mescaline cerebellar gating | psychedelic perturbation can alter network organization / sensory gating non-uniformly | N4, N7 | perturbation / evaluation | NEURAL35 | integrated | supports `reopening != reselectability` stress test; no therapy / subjecthood inference |
| History-conditioned relational possibility evidence packet | ordinary neuroscience evidence for replay, latent state, metaplasticity, relational change and matched-state pressure | N2, N3 | strongest-baseline packet | NEURAL34 / first well | integrated | load-bearing first-well baseline; generic “history matters” is already field-owned |
| Verzhbinsky — cross-region ripple WM | brief co-ripple windows preferentially realize / reinstate distributed firing relations not exhausted by component firing magnitude | N3 | mechanism / relation evidence | NEURAL33 | integrated | `component state != organizational state`; ripple != selection |
| Mizrachi — attention / immune regulation | attentional allocation can alter acute peripheral inflammatory trajectory in a bounded human paradigm | N6, N7 | consequence / physiology bridge | ATTENTION-IMMUNE | integrated | demonstrates neural/cognitive allocation can land in bodily physiology; no `d`/`Psi_f` identity |
| Huerta — vagal cytokine representation | peripheral neural responses can be cytokine-specific and disease-state-dependent before central processing | N6, N2 | peripheral representation / history pressure | VAGAL-CYTOKINE | integrated | supports state-dependent body-to-brain object, pure-history and bearer claims remain prospective |
| Becker — Aha / representational reconstitution | insight / learning can reconstitute later representational organization rather than merely add a static item | N1, N2 | history / representation pressure | active Aha hook | routed | useful to reconstitution / writeback family; no canonical promotion under consolidation freeze |
| Zhang — TBI / gut-brain / MFN2 | neurotrauma/postbiotic work links peripheral, mitochondrial and astrocytic mechanisms to brain injury state | N6, N7 | pathology / substrate pressure | no current neural-number owner | deferred | keep as multi-system pathology candidate; requires bounded owner bridge before mechanism synthesis |
| Amornbunchornvej — disagreement / attention | philosophy/cognitive-science account of attention in disagreement | future Epistemology / Philosophy; N5 at most | cross-domain pressure | not neuroscience owner | excluded | scanner false positive for attention vocabulary; no direct neural evidence needed here |

### 5.2a Scan artifacts / wrappers

The following scan hits are routing wrappers, not additional independent SourceCards:

| Asset | Disposition | Reason |
|---|---|---|
| `Materials/2026/INDEX_2026_08_23_Becker_Aha_SRT.md` | excluded as duplicate routing artifact | use the Becker SourceCard + hook as the material record |
| `Materials/2026/READING_2026_08_24_IPA_TBI_Postbiotic.md` | routed to Zhang/TBI entry above | reading wrapper does not create a second evidence item |

### 5.3 Patch / Hook disposition matrix

A pending Hook remains pending after framework routing. “Integrated” below means integrated into the **Layer-2 problem map**, not landed into its historical target owner.

| Patch / Hook family | Existing integration state | Framework family | Framework disposition |
|---|---|---|---|
| CONSC14 propofol traveling waves | hook landed | N4 / N5; primary future Consciousness | integrated as historical measurement/routing bridge; no new owner work |
| NEURAL15 creative brain clock | hook landed | N2 / N4 | integrated as historical plasticity / openness bridge |
| NEURAL16 BOLD–CMRO2 uncertainty gate | hook landed | N5 | integrated as measurement guardrail |
| NEURAL17 HGA–spike dissociation | hook landed | N5 | integrated as source-scope guardrail |
| NEURAL18 mixed-selectivity / decodability | patch active; synthesis pending | N1 / N5 | routed; keep old landing hook/target status unchanged |
| NEURAL19 pre-attentive gist / report | patch + pending hook | N1 / N5 | routed; pending hook remains pending |
| NEURAL19 resource-gated memory admission | patch + pending hook | N2 / N4 | routed; pending hook remains pending |
| NEURAL20 habit strategy / execution | patch + pending hook | N2 / N4 / N7 | routed; pending hook remains pending |
| NEURAL21 REM metabolic payability | patch + pending hook | N4 / N7 | routed; pending hook remains pending |
| NEURAL22 astrocyte hierarchy | patch + pending hook | N3 / N4 | routed; pending hook remains pending |
| NEURAL23 embodied rhythmic eligibility | patch + pending hook | N4 / N6 | routed; pending hook remains pending |
| NEURAL24 bearer-indexed affective readout | patch + pending hook | N6 / N7; future Consciousness | routed as pressure / implementation candidate; no phenomenal promotion |
| NEURAL25 historical selection bias + protocol | patch + pending hook | N2 / N4 | routed; first-well precursor / protocol asset |
| NEURAL26 capacity / accessibility / authority | patch + pending hook | N4 / N7 | routed; entropy/connectivity remain proxy families |
| NEURAL27 prospective history use | patch + pending hook | N2 | routed; no-report history-use readout candidate |
| NEURAL28 reidentifiable object identity | patch + pending hook | N1 | routed; no identity criterion promotion |
| NEURAL29 consolidation / transformation | patch + pending hook | N2 | routed; transformation != factual correctness |
| NEURAL30 temporal integration / closure | patch + pending hook | N1 / N5; future Consciousness | routed; report/phenomenality boundary preserved |
| NEURAL31 astrocytic historical eligibility | patch + pending hook | N2 / N4 | routed; content != retrievability != eligibility |
| NEURAL32 relational candidate construction | patch + pending hook | N1 / N3 | routed; precursor representation compatible with selection-before-stabilized-representation |
| NEURAL33 distributed ripple reinstatement | patch + pending hook | N3 | routed; relation-level mechanism candidate |
| NEURAL34 history-conditioned relational possibility | patch + pending hook | N2 / N3 | integrated as first-well parent bridge; first-well Case-B result constrains it |
| NEURAL35 psychedelic reopening / reanchoring | patch + pending hook | N4 / N7 | routed; `reopening != reselectability`, under-anchoring remains disposable P3/P4 label |
| ATTENTION-IMMUNE | bridge + pending hook | N6 / N7 | routed; no new NEURAL number required |
| VAGAL-CYTOKINE | bridge + pending hook | N6 / N2 | routed; state-dependent representation retained, pure-history claim prospective |
| Aha representational reconstitution hook | active, no ordinary landed/pending field | N1 / N2 | routed with explicit status uncertainty; do not infer owner landing |

### 5.4 Material completeness statement

As of this v0.1 pass:

```text
All active neuroscience-relevant high / very-high SourceCards identified by the
2026-09-04 repository scan, plus non-standard high/very-high variants, have a visible
Framework disposition: integrated, routed, deferred-with-blocker, or excluded-with-reason.

All active neuroscience PatchNotes / Hooks found by the same scan have a visible
problem-family route. Existing landed/pending status is preserved and is not rewritten
by Framework inclusion.
```

Remaining unpaid work is **not material discovery** for v0.1. It is downstream owner landing, evidence hardening or deep-well selection where explicitly noted.

### 5.5 Source / synthesis / discrimination separation

For every material above:

```text
A — source-native claim / evidence boundary
B — this Framework's domain-level organization
C — any claim that SRT yields a discriminating neuroscience increment
```

v0.1 is intentionally rich in **B**.

Current neuroscience **C remains unlicensed** by the first deep well's Case-B verdict. No SourceCard, PatchNote, Hook or Framework row upgrades that verdict.

---

## 6. Inherited SRT asset re-routing

| Existing asset | Historical role | Architecture-v2 role | Parent family | Action | Notes |
|---|---|---|---|---|---|
| `Neuroscience/README.md` | directory entry | navigation to Framework + guardrails | all | keep / update route | not theory authority |
| `NEUROSCIENCE_COMPACT_REGISTRY.md` | five-layer old neuroscience registry | inherited architecture inventory | all | keep, mark subordinate for new theory advancement | useful historical map, not Layer-2 owner |
| `SRT_Neuroscience_Claim_Status.md` | proxy / clinical / high-risk guardrail | continuing claim ceiling | N5 / N6 / N7 | keep | remains mandatory |
| `SRT_Neuro_Axioms_Claim_Status.md` | audit of hybrid axiom file | old-owner status guardrail | all | keep | prevents file-level canonical over-reading |
| `_SRT_Neuro_Axioms.md` | canonical-facing formal bridge | historical domain theory / formalization candidate | N1–N7 as relevant | do not use as Framework skeleton | may be tested/rerouted later |
| `SRT_Neural_Mechanisms_CompactCore.md` | current formal neural compact core | inherited Layer-3 mechanism package | mainly N1–N5 | keep, subordinate to Framework for question routing | bridge/lab, not canonical |
| `SRT_Neural_Mechanisms.md` | longform mechanism text | historical Layer-3 exposition | mainly N1–N5 | keep / do not use as current domain architecture | may lag compact core and embeds old Core→domain mapping |
| `SRT_Consciousness_Mechanisms*` | neural-consciousness mechanism package | adjacent Layer-3 package | N5/N6/N7 + future Consciousness | keep / route | not the Neuroscience Framework's consciousness definition |
| `_SRT_Neuroscience_Hardening_Index.md` | patch / hardening navigation | primary inherited asset-routing ledger | all | keep | Framework consumes it; synthesis-target freeze still respected |
| N1–N12 hardening drafts | proposed synthesis architecture | historical Layer-3 hypothesis / bridge set | various | split across families, do not revive whole synthesis by default | old “N1–N13 synthesis” is not automatically authorized by Framework creation |
| `SRT_Neuro_Experiments.md` / prediction table | broad experiment/prediction surfaces | candidate deep-well source inventory | N1–N7 | keep / re-evaluate per queue | no experiment inherits validity from old folder status |
| `SRT_NEURAL25_EXPERIMENT_PROTOCOL_v0_1.md` | memory-control P4 protocol | candidate N2/N4 well asset | N2 / N4 | route | does not equal first-well execution |
| `SRT_NEURAL33_EXPERIMENT_PROTOCOL_v0_1.md` | relational reinstatement P4 protocol | candidate N3 well asset | N3 | route | must pay strongest baseline |
| `SRT_NEURAL34_MATCHED_STATE_RELATIONAL_HISTORY_PROTOCOL_v0_1.md` | exact matched-state history protocol | grandfathered first-well protocol asset | N2 / N3 | preserve | Phase 8A access NO-GO; not executed |
| `papers/history_dependent_reachability/*` | published-paper project / evidence organization | historical manuscript asset | N2 / N4 | preserve / cite historically | not Constitution-derived proof |
| Phase-8 Neuroscience charter | first deep-well charter | grandfathered Layer-4 pilot record | N2 / N3 | preserve | not retroactively rewritten as Framework-first |
| Phase-8A audit | strongest baseline + access audit | Layer-4 adverse-result record | N2 / N3 / N5 | preserve | Case B + DATA-ACCESS-0 NO-GO |
| Phase-9 review | productive-adequacy result | first Phase-9.5 writeback input | all, especially N2/N3/N5 | integrate below | translation-only + scope-limited |

### 6.1 Synthesis-target freeze interaction

The pre-existing hardening index froze a future N1–N13 synthesis target after a Case-A/STOP bounded probe. Architecture v2 does **not** silently reactivate that synthesis file.

The new Framework instead routes the same surviving materials into problem families. A future mechanism synthesis must be justified from those families and current owner status, not from the fact that a historical target file name already exists.

---

## 7. Neuroscience problem families

### N1 — Neural object, state and re-identification

**Core question**: What makes a neural / representational object count as the same object across time, transformation, presentation, temporal integration and changed context?

**Constitution operations**: ARTICULATION, STILL-THIS, OWN-HISTORY.

**Objectification pressure**: cell/ensemble grouping, decoder class, temporal window, report stage.

**Bearer pressure**: identity of a measurement object is not automatically identity of a bearer.

**Inherited assets / materials**: NEURAL18, Wentzell pre-attentive interface, NEURAL28 concept identity, NEURAL30 temporal integration, NEURAL32 structured candidates, Luppi, Becker.

**Mature neighbors**: population coding / representational geometry, concept-cell and invariant coding work, temporal integration / postdiction, perceptual organization.

**Possible domain-local gain**: a declared identity contract that separates identification, re-identification, relational recruitment, temporal integration and historical incorporation and changes an actual experimental classification.

**Translation-only collapse**: if mature representational / dynamical methods already provide the same distinctions and SRT changes only terminology.

---

### N2 — Historical ownership, transformation and present efficacy

**Core question**: Which history belongs to which neural / organism-level object, how is it transformed, and when does it still constrain the future now?

**Constitution operations**: OWN-HISTORY, STILL-THIS, CURRENT PROCESSABILITY.

**Objectification pressure**: present-state projection, trial matching, early/late contrasts, recall as history proxy.

**Bearer pressure**: participant history, component history and relation history must not be silently substituted.

**Inherited assets / materials**: N10/N11, NEURAL19 memory admission, NEURAL20, NEURAL25, NEURAL27, NEURAL29, NEURAL31, NEURAL34, Wang, Ranganath, Brzostowicki, Tottori, Lu, history evidence packet.

**Mature neighbors**: engram / synaptic plasticity, systems consolidation, replay / reinstatement, metaplasticity, latent-state memory, event segmentation, reconsolidation.

**Possible domain-local gain**: a history-typing scheme that forces a new held-out discriminator between retained content, transformed history, retrievability, active control and future write-back.

**Translation-only collapse**: if the strongest memory / plasticity models already provide the same operational separations.

---

### N3 — Relational disposition and distributed organization

**Core question**: When component states are similar, what determines which distributed relation can be realized, reinstated or stabilized?

**Constitution operations**: ARTICULATION, OWN-HISTORY, CURRENT PROCESSABILITY.

**Objectification pressure**: pair/graph construction, common drivers, component-state sufficiency, relation identity.

**Bearer pressure**: relation as measurement object does not become a bearer; organism-level consequence remains separately attributed.

**Inherited assets / materials**: NEURAL22, NEURAL32, NEURAL33, NEURAL34, Verzhbinsky, Pérez, Yashiro, first well.

**Mature neighbors**: relational / conjunctive memory, functional/effective connectivity, population dynamics, replay/reinstatement, oscillatory coordination, graph neuroscience.

**Possible domain-local gain**: a relation-history discriminator that survives rich component, PRE-relation, anatomy and common-driver baselines and predicts future **relation identity**.

**Translation-only collapse**: the current first-well result is exactly this collapse pressure: ordinary neuroscience owns the generic content and no executable sharper discriminator is currently licensed.

---

### N4 — Current processability, capacity, accessibility and gating

**Core question**: Why can some candidate states / transitions participate in competition now while others cannot?

**Constitution operations**: CURRENT PROCESSABILITY, ARTICULATION, EVALUATIVE RE-RUN.

**Objectification pressure**: global state metrics, phase averaging, capacity proxies, resource regimes, gating variables.

**Bearer pressure**: system capacity and candidate accessibility do not imply control authority, stake or subjecthood.

**Inherited assets / materials**: composite `G_hat_theta` bridge, N11/N12, NEURAL19 memory admission, NEURAL20, NEURAL21, NEURAL22, NEURAL23, NEURAL26, NEURAL31, NEURAL35, Tottori, Qin, Young, Cavallaro.

**Mature neighbors**: global-state / criticality work, gating and basal-ganglia / thalamocortical models, attention/precision, resource-rational models, predictive processing, brain-body phase effects.

**Possible domain-local gain**: a test that separates dynamical capacity, candidate accessibility, control authority, expression and historical write-back and shows why one distinction changes prediction.

**Translation-only collapse**: if SRT merely relabels standard capacity / gating / attention variables.

---

### N5 — Measurement objectification, proxy dependence and report interface

**Core question**: Which inferential claims survive the measurement and public-object transformations required to make neural data comparable?

**Constitution operations**: ARTICULATION, CONSEQUENCE ATTRIBUTION, STILL-THIS.

**Objectification pressure**: BOLD, CMRO2, HGA, spike source scope, decoder construction, ROI/pair boundary, report/VSTM, normalization, public-data availability.

**Bearer pressure**: measurement site, causal source, participant and outcome bearer must remain typed separately.

**Inherited assets / materials**: NEURAL16, NEURAL17, NEURAL18, Wentzell, Misawa, Luppi, Menétrey, Da Costa, Phase-8A access audit.

**Mature neighbors**: measurement theory, neuroimaging calibration, neural decoding, no-report / report paradigms, neurophenomenology, causal inference and data-governance methods.

**Possible domain-local gain**: a Bearer–Objectification Declaration or equivalent that changes dataset eligibility, model specification or stop decision beyond ordinary good practice.

**Translation-only collapse**: first well currently supports a process contribution only; uniqueness to SRT is not established.

---

### N6 — Bearer hierarchy, body embedding and consequence attribution

**Core question**: Which unit receives, bears or acts on a consequence across neural, bodily and organismic levels?

**Constitution operations**: CONSEQUENCE ATTRIBUTION, OWN-HISTORY, ARTICULATION.

**Objectification pressure**: brain-only boundary, peripheral signals as nuisance, affect as scalar, neural outcome as organism outcome.

**Bearer pressure**: cell, network, body subsystem, participant and phenomenal subject are non-identical roles.

**Inherited assets / materials**: NEURAL23, NEURAL24, ATTENTION-IMMUNE, VAGAL-CYTOKINE, Young, Damasio, Mizrachi, Huerta, Van Mulukom / Borges as adjacent pressure.

**Mature neighbors**: interoception, homeostasis/allostasis, embodied cognition, autonomic/neuroimmune regulation, affective neuroscience.

**Possible domain-local gain**: a consequence-attribution design where keeping bearer roles separate changes causal model or prevents invalid transfer between neural and organism-level outcomes.

**Translation-only collapse**: if standard embodied / interoceptive neuroscience already supplies the same role separation.

---

### N7 — Reconfiguration, pathology, recovery and evaluative direction

**Core question**: When is a change in flexibility, connectivity, complexity, accessibility or stability an improvement rather than merely a different state?

**Constitution operations**: EVALUATIVE RE-RUN, CURRENT PROCESSABILITY, CONSEQUENCE ATTRIBUTION.

**Objectification pressure**: recovery scores, entropy/connectivity, task performance, symptom scales, perturbation-induced opening.

**Bearer pressure**: clinical / organism-level benefit must be attributed at the level where function, suffering, risk and future options are actually assessed.

**Inherited assets / materials**: SRT neuroscience claim-status pathology guard, NEURAL20, NEURAL21, NEURAL26, NEURAL35, Qin, Cavallaro, Mizrachi, Zhang, Bussell pressure card.

**Mature neighbors**: DoC recovery, rehabilitation, computational psychiatry, psychedelic neuroscience, habit / flexibility research, clinical outcome methodology.

**Possible domain-local gain**: a prospective `Opening x Reanchoring` or comparable design where “more open / complex / connected” is separated from stable, evidence-sensitive, consequence-tested future function.

**Translation-only collapse**: if the distinction reduces to ordinary task-specific clinical outcome modelling without an additional research consequence.

---

## 8. Mature domain neighbor map

This map is competence/routing only. Final Case A/B/C belongs to a selected deep well.

| Problem family | Mature tradition / framework | What it already owns | Pressure on SRT | Later baseline target? |
|---|---|---|---|---|
| N1 | population coding, representational geometry, invariant / concept coding, temporal integration | state identity, decoding, transformed representation, temporal integration | SRT cannot claim “representation is constructed / dynamic” as new | yes |
| N2 | synaptic / engram memory, consolidation, replay, reconsolidation, metaplasticity, latent states | extensive history dependence and transformation | generic “history matters” is already fully owned | yes |
| N3 | relational/conjunctive memory, network dynamics, connectivity, oscillatory coordination | distributed relation formation / reinstatement | relation-level language is not itself an increment | yes |
| N4 | gating, global state, criticality, attention/precision, predictive processing, resource-rational cognition | capacity/accessibility constraints and state-dependent transition availability | SRT must show why its decomposition changes a prediction | yes |
| N5 | neuroimaging calibration, measurement theory, decoding, causal inference, no-report / neurophenomenology | proxy limitations and measurement-object construction | Bearer–Objectification may be good practice rather than SRT-specific | yes |
| N6 | interoception, homeostasis/allostasis, embodied / affective neuroscience, neuroimmune regulation | organism-body-neural coupling and physiological consequence | bearer separation cannot ignore mature embodied neuroscience | yes |
| N7 | clinical neuroscience, computational psychiatry, rehabilitation, DoC, psychedelic / flexibility research | task-specific impairment/recovery and non-monotone state change | “more flexible != better” is not automatically novel | yes |

---

## 9. Candidate domain theories / hypotheses / models

Listing does not make a candidate true.

| Candidate | Parent family | Type | Current status | Evidence owner | What would test / falsify it |
|---|---|---|---|---|---|
| composite neural `G_hat_theta` = competition/gain/gating/stabilization | N1/N4 | mechanism bridge | inherited Layer-3 package | Neural CompactCore | component ablation / rival architecture / task-general predictive gain |
| `L2` as sedimented neural selection constraint | N2/N4 | domain interpretation | inherited bridge; not identity with memory | compact core + memory patch family | distinguish from standard history/plasticity accounts with operational gain |
| NEURAL31 astrocytic historical eligibility | N2/N4 | mechanism candidate | P3/P4 | astroengram SourceCard/patch | later retrievability changes conditional on astrocytic history beyond neuronal/content controls |
| NEURAL33 distributed ripple relation window | N3 | mechanism candidate | P3/P4 | Verzhbinsky / patch | rate-corrected relation-specific coordination and causal / held-out behavioral relevance |
| NEURAL34 `K^(tau)` relational disposition | N2/N3 | local bridge variable | Case-B pressure; no Case-C license | evidence packet + first well | exact matched-state relation-history differential beyond strongest baseline; withdrawal if fully paid by ordinary model |
| NEURAL26 capacity→accessibility→authority stack | N4/N7 | decomposition | P3/P4 | Qin / patch | crossed perturbation showing separable capacity vs control effects |
| NEURAL32 structured candidate content | N1/N3 | representation bridge | P3/P4 | Yashiro / patch | context/relational latent features predict candidate organization beyond category while selection remains separately measured |
| NEURAL24 bearer-indexed affective readout | N6/N7 | implementation / pressure model | P3 | Damasio / patch | consequence / regulatory signal / affect / action dissociations; no phenomenal promotion without independent evidence |
| NEURAL35 reopening vs reanchoring | N4/N7 | perturbation model | P3/P4 | Cavallaro + future human evidence | opening can rise while evidence-sensitive stabilization/future function falls; reject if one latent factor explains both |

---

## 10. Deep-well queue

**No neuroscience well is active now.** Epistemology remains the active main programme well.

| Candidate / reopen route | Parent family | Exact bounded question | Domain-native discriminator | Access / evidence state | Strongest-baseline target | Authorization |
|---|---|---|---|---|---|---|
| N-R1 exact-charter access reopening | N2/N3/N5 | original matched-current-state / different relation-history question | PRE-controlled H term adds held-out future relation-identity prediction | currently NO-GO | relational memory, engram/plasticity, latent state, replay, metaplasticity, rich predictive history | conditional only if qualifying data/collaborator route appears |
| N-R2 stronger differential reopening | N2/N3 | same underlying relational-history problem, but with a materially sharper discriminator | new measurable contrast survives original Case-B baseline | not currently identified | same first-well baseline plus any new rival | requires visible addendum; old Case-B remains historical truth |
| N-R3a prospective history-use successor | N2 | can reportable retention be matched while future-guiding no-report history use differs? | anticipatory behavior / neural relation predicts future path after retention controls | candidate materials exist | prospective memory / event segmentation / standard memory-control models | successor charter required; not old-well execution |
| N-R3b capacity × history successor | N2/N4 | does global capacity alter accessibility without erasing independent history-control effects? | crossed capacity perturbation × history model comparison | candidate sources/protocol pieces only | DoC/global-state models + memory-control models | successor charter required |
| N-R3c re-identification successor | N1 | when does changed neural realization still support the same task object across presentation / relation change? | held-out identity generalization under transformation with causal/behavioral use | candidate human sources exist | invariant coding / concept-cell / representational geometry models | successor charter required |
| N-R3d opening × reanchoring successor | N4/N7 | can perturbation increase candidate accessibility while degrading evidence-sensitive stabilization? | preregistered Opening × Reanchoring dissociation under preserved basic competence | no current exact human execution packet | psychedelic / flexibility / clinical outcome models | successor charter required; clinical guard mandatory |

Every future selected row must receive a fresh Layer-4 strongest-baseline Case A/B/C adjudication. Being listed here licenses no Case C.

---

## 11. Framework v0.1 exit gate

```text
[x] Given-Ones inventory exists
[x] all six Constitution operations have neuroscience-native translations
[x] objectification map exists
[x] bearer / position roles are separated
[x] Material Re-entry Pass completed; no high/very-high direct card is silent
[x] inherited SRT assets rerouted
[x] stable problem families exist
[x] mature neighbors mapped without novelty gating
[x] grandfathered first well has parent families N2/N3/N5
[x] future queue questions are narrower than the Framework
[x] every queued/reopen route names the strongest-baseline family it would have to face
[x] Framework placement licenses no Case-C claim
```

**Exit-gate meaning**: Neuroscience Framework v0.1 is structurally complete enough to act as the parent Layer-2 map. This does **not** authorize a new active neuroscience deep well while Epistemology is the mainline.

---

## 12. Phase 9.5 writeback ledger

### 12.1 Grandfathered first well — 2026-09-03

```text
well = matched present neural state / different relational history
result = strongest-baseline Case B
access = DATA-ACCESS-0 NO-GO
execution = not started
Phase 9 = translation-only + scope-limited
```

| Framework item affected | Before / inherited tendency | Deep-well pressure/result | v0.1 after | Action |
|---|---|---|---|---|
| neural unit | participant, cell, pair and network could be discussed in one mechanism narrative | study forced participant vs measurement-object distinction | bearer table explicitly separates roles | strengthen distinction |
| history | “history affects later state” could carry too much weight | baseline already owns generic replay/plasticity/latent-state effects | N2 requires typed history + present efficacy, not generic history | narrow |
| relation | distributed relation could be treated as a richer state descriptor | strongest baseline already owns relational / conjunctive organization | N3 asks for relation-identity discriminator beyond rich baselines | narrow / retain as open |
| current state | matched firing/activity could be read as “same state” | equivalence depends on declared grain and omitted variables | N5 treats matching as objectification contract | strengthen |
| evidence access | adjacent public datasets looked tempting | no dataset preserved exact PRE relation + controlled H + current-state variables | dataset/object mismatch becomes an explicit Framework issue | integrate negative result |
| increment language | NEURAL34 could suggest a new relational-history object | Case B blocks Case-C content claim | `K^(tau)` remains local bridge variable only | downgrade claim ceiling |
| future work | closed well could look permanently frozen | author later clarified bounded reopening is allowed | queue distinguishes N-R1/N-R2/N-R3 without erasing adverse result | split reopening modes |

### 12.2 What the first well positively contributed

The reusable gain is not a new neural effect. It is a domain cut:

```text
item / component history != relation-specific history
current component description != relation disposition
generic later activation != future relation identity
participant != neural measurement object
measurement consequence != participant-level consequence
analyst matching != natural equivalence
```

This cut now lives here rather than only inside a failed-access audit.

### 12.3 What it withdrew / refused

```text
SRT neuroscience domain increment from “history matters” = withdrawn / not licensed
convenience substitution of item-memory or macro data for exact relation-history object = refused
early/late contrast as matched-current-state execution = refused
cross-dataset pooling as one longitudinal bearer/system = refused
```

### 12.4 Constitution boundary

The first well changed the **domain framework**, not Constitution v1.

No Constitution reopen condition is triggered by the Case-B / access-NO-GO result.

---

## 13. Current framework summary

```text
domain = Neuroscience
framework version = v0.1
active problem families = N1 object/state identity; N2 historical ownership/efficacy; N3 relational disposition; N4 processability/capacity; N5 measurement objectification; N6 bearer/body/consequence; N7 pathology/evaluation
active neuroscience deep well = none
active main programme well = Epistemology
material re-entry = complete for active high/very-high neuroscience-relevant cards and active patch/hook surfaces found in the 2026-09-04 pass
strongest current domain-level SRT contribution = problem-routing / bearer-objectification discipline, not a demonstrated empirical increment
strongest current external pressure = mature neuroscience already owns generic history dependence, relational memory, latent state, plasticity, gating, measurement limitations and embodied regulation
most important unresolved distinction = whether any SRT-guided cut yields a discriminator that changes prediction beyond those mature baselines
first-well standing = Case B + exact-charter access NO-GO + translation-only / scope-limited; adverse result preserved
neuroscience reopening = conditional, bounded, versioned; no silent weakening
next authorized neuroscience action = passive retrieval / bounded reopen preparation only unless an N-R1/R2/R3 gate fires and author reprioritizes
next programme action = advance R4-C5 Spirituality / Praxis & core-theory reverse-feedback consolidation (historical 2026-09-04 note: Epistemology Framework superseded as CURRENT NEXT by R4-C wave schedule; no Neuroscience deep well reopened)
```

---

## 14. `R4-C4` Bidirectional Theory Integration & Core Feedback Map (2026-11-26)

Without altering the preserved Phase 8A / 9 / 9.5 adverse-result ledger or releasing any `HOLD`, `R4-C4` links problem families `N1–N7` directly to the eight positive theoretical axes of **Holistic Generative Cognition** (`SRT_Neural_Mechanisms_CompactCore.md v2` & `SRT_Consciousness_Mechanisms_CompactCore.md v3`) and queues five `C` (M-origin) reverse-feedback candidates (`FB-C4-1..5`) for `R4-C5` core-theory review:

| Problem Family (`N1–N7`) | `R4-C4` Positive Theoretical Axis | Controlling Author Calibration / Guard | Core Feedback Candidate (`R4-C5`) |
|---|---|---|---|
| **N1** Object / state identity | **Axis 1** Pre-object holistic generation & object formation + **Axis 5** Comparative-capacity generation (`NEURAL28/30/32`, `VTC`) | Holism & differentiability are mutually constitutive; pre-object orientation does not imply universal necessity across all tasks | `FB-C4-1` (`One_Formation / Spine / L0`) |
| **N2 / N3** Historical ownership & relational disposition | **Axis 4** Regenerative memory, 5 heterogeneous history duties (`stored ≠ active`), developmental pruning & dual scaffold/occlusion role (`N10/N12/NEURAL27/29/31/33`) | First-well Case-B / `DATA-ACCESS-0 = NO-GO` preserved verbatim; generic "history matters" remains neighbor-owned | `FB-C4-4` (`Core_12b / Occlusion / Core_14`) |
| **N4** Current processability, capacity & gating | **Axis 2** Sensation–cognition–actualization recursive coupling + **Axis 6** Multilevel gating action field (`target ≠ gate objectification`, inhibition/convergence) | Energy-gradient difference retained as deeper physical generative mechanism candidate, NOT equated with `Selection / d / Ψ_f` | `FB-C4-2` & `FB-C4-5` (`Spine / Core_21 / Core_25 / Core_13a`) |
| **N5** Measurement objectification & report interface | **Axis 7** Foreground as generative mediation ($\neq$ broadcast), functional vs phenomenal binding (`Def-AI-Con-3b`), local monitoring $\neq$ full introspection $\neq$ `HP-B` | `HP-B` FROZEN / OPEN; `Subjecthood Threshold S0–S6` strictly isolated from Primitive `S0` & **AI 赌注谱系 `S0–S4`** | `FB-C4-5` (`HardProblem / Agency_Subjecthood`) |
| **N6** Bearer hierarchy & body embedding | **Axis 3** Endogenous valence-first & microvalence (`Def-AI-Con-3/3a`) + 5-layer separation (concern / `d` / `B-4` friction / metabolic burden / felt experience) | Biological developmental co-constitution $\neq$ universal cross-substrate inseparability; functional dissociation & post-lesion reorganization integrated | `FB-C4-3` (`D_VALUE / PSI_F / Suffering`) |
| **N7** Reconfiguration, pathology & evaluative direction | **Axis 6 & Axis 8** Positive freedom (`T3-03 C / Q26`), `reopening ≠ reselectability` (`NEURAL35`), and Bio–AI cross-substrate cognitive comparison | Non-biconditional pathology lens; never reduce brain to LLM or treat biology as a priori necessary for all cognition | `FB-C4-1..5` (`R4-C5` unified review) |



---

## FILE: `Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md`

| 字段 | 值 |
|---|---|
| path | `Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md` |
| id | SRT-NEUROSCIENCE-COMPACT-REGISTRY |
| claim_mode | navigation |
| status | active |
| epistemic_layer | os |
| layer | meta |
| canonical(字段) | false |
| last_commit | 2026-11-27 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：[SRT-CANONICAL-REGISTRY, SRT-NEUROSCIENCE-CLAIM-STATUS, SRT-NEUROSCIENCE-RECONSTRUCTION-FRAMEWORK, SRT-NEURO-AXIOMS-001]

<!-- 以下为原文逐字保留 -->

# SRT Neuroscience & Generative Cognition Compact Registry (`R4-C4` 同步版)

> **Role**: navigation layer (`canonical: false`). Routes neuroscience & generative cognition materials across the five directory layers and the eight `R4-C4` positive theoretical axes. Does not define canonical `Selection`, `One`, `d-value`, `Ψ_f`, consciousness, or clinical diagnosis.

---

## 0. Current Structure (`R4-C4` 五层组织)

1. **Guardrail & Problem-Map Layer**: `SRT_Neuroscience_Claim_Status.md`（`v2`）、`SRT_Neuroscience_Reconstruction_Framework.md`（`N1–N7` 问题族 + Phase 8A/9/9.5 负面结论留痕 + `§14 R4-C4` 对接）、`README.md` 与本注册表。
2. **`R4-C4` Formal Compact Core Layer（默认检索主干）**:
   - `SRT_Neural_Mechanisms_CompactCore.md`（`v2`：整体生成性认知八大正面主轴 + 神经选择机制 + `FB-C4-1..5`）
   - `SRT_Consciousness_Mechanisms_CompactCore.md`（`v3`：前景生成中介 + 功能/现象绑定 + 比较动物意识 + 多层级门控 + `HP-B` 独立边界 + `FB-C4-5`）
3. **Canonical-Facing Bridge & Audit Layer**: `_SRT_Neuro_Axioms.md`（`v2`）与 `SRT_Neuro_Axioms_Claim_Status.md`（`v2`）。
4. **Longform, Clinical & Extension Layer**: `SRT_Neural_Mechanisms.md`（含 `Neural_Mechanisms_Split/`）、`SRT_Consciousness_Mechanisms.md`、`SRT_Clin_00..03`、`SRT_Neuro_06..10`（含 `Immune_Dist_Split/` 与 `BioQuantum_CISS_Amendment`）、`SRT_FEP_MetaAwareness_AffectiveSelf_Bridge.md`、`../Neuroscience_Annex/`、`../Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md`。
5. **Hardening, Lab Protocol & Evidence Layer**: `_SRT_Neuroscience_Hardening_Index.md`、`SRT_Neuroscience_Hardening_N1_N9_v0_1.md`、`N10–N12`、`SRT_NB1_MOFC_LOTTERY_EXECUTION_CARD_v0_1.md`（card-defined only）、`SRT_NEURAL25/33/34` 协议、`patches/` 与 `hooks/`（既有 `pending/landed` 状态原样保留）。

---

## 1. `R4-C4` 八大正面理论主轴路由表

核心研究问题：**认知能力如何从整体性生成组织中产生、分化出相对独立的局部能力，并反过来通过相互作用重构整体与外部现实？**

| # | `R4-C4` 理论主轴 | 核心落点（首选阅读） | 承接上游与作者源资产 |
|---|---|---|---|
| **1** | **前对象整体生成与对象形成**（`generative orientation → objectification → retention → reshaping`） | `SRT_Neural_Mechanisms_CompactCore.md §1–§2`；`SRT_Neural_Mechanisms.md §0, Part A §I` | `2026-09-26` 前对象导向作者裁决；`Large-Scale Phase-Dominance` / `Hierarchical Cortical Flow` / `fcANN` / `NEURAL30, 32` |
| **2** | **感觉、认知与实现的递归耦合**（含**能量梯度差**更底层物理生成机制候选） | `SRT_Neural_Mechanisms_CompactCore.md §2.3–§2.4`；`_SRT_Neuro_Axioms.md §I–§II` | `2026-11-11` 感觉—认知—实现作者源（按 `R3-03` 二轮裁决校准）；`Core_25` 热力学签名 |
| **3** | **效价、关切与价值的内生生成**（效价优先、微效价 + 五层概念分离） | `SRT_Neural_Mechanisms_CompactCore.md §4`；`SRT_Neuroscience_Claim_Status.md §2.1` | `R4-C3` 移交 `Def-AI-Con-3 / 3a`（Lebrecht 2012）；`NEURAL24`（Damasio）；`INTEROCEPTIVE_PRECISION`；`_SRT_D_VALUE_CANONICAL §2a` |
| **4** | **历史效力、再生成记忆与认知骨架**（存储 $\neq$ 活跃生效 + 发育式剪枝 + 支持/遮蔽双刃剑） | `SRT_Neural_Mechanisms_CompactCore.md §5`；`SRT_Neuroscience_Reconstruction_Framework.md N2/N3` | `2026-10-07` Empty Brain 再生成记忆溯源；`R4-C3` 七层历史与五类异质职责；`N10 BTSP` / `N12 & NEURAL31` / `NEURAL27, 29, 33` / `AI/Architecture_Annex/01 §1` |
| **5** | **比对能力本身的生成与重构**（四类比对生成性 + 生成/留存/生效三位置） | `SRT_Neural_Mechanisms_CompactCore.md §6`；`Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md` | `R4-C2` 五类非阶梯能力；`R4-C3` 四类比对生成性；`NEURAL28` 概念细胞；`VTC Shared Imagery`；`P3-Scale-NB1` 除法归一化 |
| **6** | **意愿、主动性与正面自由**（多层级门控行动场 + `target ≠ gate objectification` + 抑制/收敛） | `SRT_Neural_Mechanisms_CompactCore.md §7`；`SRT_Consciousness_Mechanisms_CompactCore.md §7` | `2026-09-26` 多层级门控作者裁决；`R4-C1` 正面自由（`T3-03 C / Q26`）与双引擎跃迁；`NEURAL20`；`PH-AG04` |
| **7** | **意识、整体性与主体性**（前景生成中介 $\neq$ 广播 + 功能/现象绑定 + 比较动物意识 + `HP-B` 独立边界） | `SRT_Consciousness_Mechanisms_CompactCore.md §1–§6`；`SRT_Consciousness_Mechanisms.md`；`SRT_Clin_00_IIT_PCI.md` | `2026-09-26` `A-16..A-24` 前景生成中介；`R4-C3` 移交 `Def-AI-Con-3b / 4`（Percy & Agarwal 2026 / ALARM / NCL）；`CONSC14`；`Subjecthood Threshold S0–S6` |
| **8** | **跨尺度认知生成与人机对照**（整体性与可分化性互构 + 生物同源共构 $\neq$ 跨底物不可分） | `SRT_Neural_Mechanisms_CompactCore.md §8`；`SRT_Consciousness_Mechanisms_CompactCore.md §8` | `R4-C2` 依赖重组/归一化；`R4-C3` 人工认知与人机共同生成；盲视/述情/裂脑/损伤重组证据 |

---

## 2. 反向核心理论反馈台账（`FB-C4-1..5`，`C` / M-origin 候选，排入 `R4-C5` 评估）

| 编号 | 神经科学/认知生成反向反馈内容 | 拟反馈核心 Owner | 当前状态 |
|---|---|---|---|
| **`FB-C4-1`** | 整体性与可分化性互构 + 前对象整体生成导向如何分化出局部能力并被对象形成反向重构 | `Core_Law/SRT_One_Formation.md`、`Core_Law/SRT_Generative_Ontology_Spine.md`、`Core_Law/SRT_L0_Metaphysics.md` | `C` 候选；排入 `R4-C5` |
| **`FB-C4-2`** | 感觉—认知—实现非线性递归模型（对齐 `R3-03`）+ 能量梯度差五类量区分及物理梯度差经耦合/边界/反馈形成组织约束机制 | `Core_Law/SRT_Generative_Ontology_Spine.md`、`Core/SRT_Core_21_Minimal_Axioms.md`、`Core/SRT_Core_25_Thermodynamic_Signatures_of_Selection.md` | `C` 候选；排入 `R4-C5` |
| **`FB-C4-3`** | 微效价→可供性→缺失→需求→赌注发生链与广义关切/微效价/广义摩擦/非闭合压力/`Ψ_f`/代谢/苦难职责分立 | `_SRT_D_VALUE_CANONICAL.md`、`_SRT_PSI_F_CANONICAL.md`、`Core_Law/SRT_Suffering.md` | `C` 候选；排入 `R4-C5` |
| **`FB-C4-4`** | 再生成记忆、发育式冗余剪枝、五类异质历史职责与生成/留存/生效三位置深化 `L_2` 双刃剑机制 | `Core/SRT_Core_12b_Ontology_L2.md`、`Core_Law/SRT_Occlusion_Dynamics.md`、`Core/SRT_Core_14_Dynamics_Scaling.md` | `C` 候选；排入 `R4-C5` |
| **`FB-C4-5`** | 多层级门控四阶路径（`target→gate→reconfiguration→capacity`）、前景生成中介与功能/现象绑定精炼 `Ghost` / 自由 / `HP-B` 候选接口 | `Core/SRT_Core_13a_Operator_Basics.md`、`Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md`、`Philosophy/SRT_HardProblem_Epistemology.md`、`Core_Law/SRT_Selection_Argument.md` | `C` 候选；排入 `R4-C5` |

---

## 3. Recommended Reading Paths

- **最短理论主干（第一次进入 `R4-C4`）**：`SRT_Neuroscience_Claim_Status.md` → `SRT_Neural_Mechanisms_CompactCore.md` → `SRT_Consciousness_Mechanisms_CompactCore.md` → `SRT_Neuroscience_Reconstruction_Framework.md`
- **形式化与桥接核查路径**：`_SRT_Neuro_Axioms.md` → `SRT_Neuro_Axioms_Claim_Status.md` → `../Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md` → `SRT_Clin_02_FEP.md` / `SRT_Clin_00_IIT_PCI.md`
- **实验与深井留痕路径**：`SRT_Neuroscience_Reconstruction_Framework.md`（§7–§12）→ `SRT_NB1_MOFC_LOTTERY_EXECUTION_CARD_v0_1.md` → `_SRT_Neuroscience_Hardening_Index.md` → `SRT_Neuro_Predictions_Table.md`
- **长文与分片展开**：`SRT_Neural_Mechanisms.md`（[`Neural_Mechanisms_Split/README.md`](Neural_Mechanisms_Split/README.md)）→ `SRT_Consciousness_Mechanisms.md`

---

## 4. `R4-C4` Compact Doctrine

> SRT treats biological nervous systems and cognition neither as passive information-processing pipelines nor as sealed biological absolutes, but as **holistic generative organizations that differentiate relatively independent local capacities and are recursively reconstituted by their interactions**. Pre-object generative orientation, embodied sensation–cognition–actualization coupling, microvalence/concern, regenerative history and developmental pruning, comparative-capacity generation, and multilevel gating (`target ≠ gate objectification`) co-evolve in biology without implying universal cross-substrate inseparability. Energy-gradient differences remain a deeper physical generative mechanism candidate without equating to `Selection`, canonical `d`, or `Ψ_f`. Conscious foregrounding is modeled as **generative mediation rather than bare broadcast**, functional and phenomenal binding are kept distinct, `Subjecthood Threshold S0–S6` is strictly isolated from AI/primitive `S` namespaces, and `HP-B` plus all existing `CN-2 / CN-3 / DATA-ACCESS-0` HOLDs remain explicitly preserved.



---

## FILE: `Neuroscience/README.md`

| 字段 | 值 |
|---|---|
| path | `Neuroscience/README.md` |
| id | - |
| claim_mode | (未标注) |
| status | - |
| epistemic_layer | - |
| layer | - |
| canonical(字段) | - |
| last_commit | 2026-11-27 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

<!-- 以下为原文逐字保留 -->

# Neuroscience & Generative Cognition (`R4-C4` 双向重构入口)

> **`R4-C4` 双向重构声明（2026-11-26）**：神经科学与整体生成性认知不仅是 SRT 核心框架的应用延伸，更是深化与反哺 SRT 核心理论（`Selection`、`One`、`L_2`、`Order`、价值/关切、意愿/自由、归一化、`Ghost`、遮蔽与跨尺度生成）的重要知识来源。本域围绕核心研究问题展开：**认知能力如何从整体性生成组织中产生、分化出相对独立的局部能力，并反过来通过相互作用重构整体与外部现实？**
>
> **已有治理边界完全保留**：
> - `SRT_Neuroscience_Reconstruction_Framework.md` 继续作为 Architecture v2 Layer-2 问题地图与 Phase 8A / 9 / 9.5 负面试点留痕的完整承载者；第一神经深井的 `Case B + DATA-ACCESS-0 = NO-GO + translation-only / scope-limited` 结论完整保留、**未解冻**。
> - `HP-B` 现象意识包保持 **FROZEN / OPEN**；`CN-2 E2`、`CN-3 toy`、`1B sim`、`O2-M`、`§10.1`、`§10.2` 等全部既有 `HOLD` 不变；本域提出的五项核心理论反向反馈（`FB-C4-1..5`）保持 `C`（M-origin 候选）性质，排入 `R4-C5` 统一评估与作者裁决。

---

## Read Order (`R4-C4` 主干)

1. [`SRT_Neuroscience_Claim_Status.md`](SRT_Neuroscience_Claim_Status.md)
   域级护栏与 `R4-C4` 四项校准（整体性与可分化性互构、能量梯度差双重边界、五层关切/价值/摩擦/体验分离、`AI/S` 全称隔离、`HP-B` 与临床/BioQuantum 护栏）。
2. [`SRT_Neural_Mechanisms_CompactCore.md`](SRT_Neural_Mechanisms_CompactCore.md)
   **`R4-C4` 核心理论主干（神经与整体生成性认知）**：系统展开八大正面主轴（前对象整体生成 / 感觉—认知—实现递归耦合与能量梯度差候选 / 效价优先与微效价 / 历史效力、再生成记忆与发育式剪枝 / 比对能力本身的生成与重构 / 多层级门控行动场与正面自由 / 跨尺度与人机认知对照 / `FB-C4-1..5` 反向反馈）。
3. [`SRT_Consciousness_Mechanisms_CompactCore.md`](SRT_Consciousness_Mechanisms_CompactCore.md)
   **`R4-C4` 意识、整体性与主体性主干**：前景即生成中介（$\neq$ 广播）、功能绑定 vs 现象绑定（`Def-AI-Con-3b`）、比较动物意识多维解耦（`Def-AI-Con-4`）、局部内部状态监测 $\neq$ 完整内省 $\neq$ `HP-B`、目标对象化 $\neq$ 门控对象化、睡眠维护与行进波路由。
4. [`SRT_Neuroscience_Reconstruction_Framework.md`](SRT_Neuroscience_Reconstruction_Framework.md)
   Architecture v2 Layer-2 问题地图（`N1–N7` 问题族、35 份 SourceCard 处置矩阵、`NEURAL15–35` 补丁路由、第一深井 `Phase 8A/9/9.5` 负面结论留痕与 `§14 R4-C4` 对接索引）。
5. [`NEUROSCIENCE_COMPACT_REGISTRY.md`](NEUROSCIENCE_COMPACT_REGISTRY.md)
   域内全文件分层目录、八大主轴索引、`FB-C4-1..5` 反向反馈指针与长文阅读路由。
6. [`_SRT_Neuro_Axioms.md`](_SRT_Neuro_Axioms.md) & [`SRT_Neuro_Axioms_Claim_Status.md`](SRT_Neuro_Axioms_Claim_Status.md)
   神经域形式化桥接与声明等级审计（`v2` 已执行原 `§8` 待清项：退除 `Ψ_f ≡ ∫` 与 `Pathology ⇔ Δθ` 强等价，同步 `P3-NEURO-3` 与 `R4-C4` 校准）。
7. 长文展开与专题接口：
   - [`SRT_Neural_Mechanisms.md`](SRT_Neural_Mechanisms.md)（分片入口：[`Neural_Mechanisms_Split/README.md`](Neural_Mechanisms_Split/README.md)）
   - [`SRT_Consciousness_Mechanisms.md`](SRT_Consciousness_Mechanisms.md)
   - [`SRT_Clin_00_IIT_PCI.md`](SRT_Clin_00_IIT_PCI.md) / [`SRT_Clin_01_Pathology.md`](SRT_Clin_01_Pathology.md) / [`SRT_Clin_02_FEP.md`](SRT_Clin_02_FEP.md) / [`SRT_Clin_03_DMN_Networks.md`](SRT_Clin_03_DMN_Networks.md)
   - [`SRT_Neuro_06_Field_Effects.md`](SRT_Neuro_06_Field_Effects.md) / [`SRT_Neuro_07_Evo_Devo.md`](SRT_Neuro_07_Evo_Devo.md) / [`SRT_Neuro_08_Immune_Dist.md`](SRT_Neuro_08_Immune_Dist.md)（[`Immune_Dist_Split/README.md`](Immune_Dist_Split/README.md)）/ [`SRT_Neuro_09_Integ_Eq.md`](SRT_Neuro_09_Integ_Eq.md) / [`SRT_Neuro_09_BioQuantum_CISS_Amendment.md`](SRT_Neuro_09_BioQuantum_CISS_Amendment.md) / [`SRT_Neuro_10_Advanced_Models.md`](SRT_Neuro_10_Advanced_Models.md)
   - [`_SRT_Neuroscience_Hardening_Index.md`](_SRT_Neuroscience_Hardening_Index.md)、`SRT_Neuroscience_Hardening_N1_N9_v0_1.md`、`SRT_NB1_MOFC_LOTTERY_EXECUTION_CARD_v0_1.md`（card-defined only；W0 访问记录见 `SRT_NB1_W0_DATA_ACCESS_PROVENANCE_2026-08-12.md`）与 [`../Neuroscience_Annex/`](../Neuroscience_Annex/)。

---

## Preserved Deep-Well & Recent Material Boundaries

- **First Neuroscience deep well (preserved adverse record)**: matched present neural state / different relational history → Phase 8A **Case B** strongest baseline + **`DATA-ACCESS-0 = NO-GO`**; Phase 9 **translation-only + scope-limited**. Conditionally reopenable only under N-R1 / N-R2 / N-R3 in `Operations/SRT_CONSTITUTION_DOMAIN_SEQUENCE_AUTHOR_DECISION_2026-09-03.md`. No Neuroscience deep well is currently active.
- **NEURAL35 (psychedelic reopening / re-anchoring)**: [`patches/SRT_Neuro_NEURAL35_Psychedelic_Reopening_Reanchoring_v0_1.md`](patches/SRT_Neuro_NEURAL35_Psychedelic_Reopening_Reanchoring_v0_1.md) & [`hooks/NEURAL35_Psychedelic_Reopening_Reanchoring_Integration_Hook.md`](hooks/NEURAL35_Psychedelic_Reopening_Reanchoring_Integration_Hook.md) (`reopening ≠ reselectability`; `under-anchoring` as disposable `P3/P4` label; read with `SRT_Neuroscience_Claim_Status.md`).

---

## Cross-Domain Links

- **Subjecthood & Agency Guardrail**: [`../Philosophy/SRT_Subjecthood_Threshold_Interface.md`](../Philosophy/SRT_Subjecthood_Threshold_Interface.md) — **Subjecthood Threshold `S0–S6`** conditional audit interface (NOT a linear ladder; strictly isolated from **Primitive `S0`**, **AI 赌注谱系 `S0–S4`**, and **AI 三型社会技术中介维度**).
- **Cross-Substrate AI Comparison**: [`../AI/AI_POSITIONING_NOTE.md`](../AI/AI_POSITIONING_NOTE.md)、[`../AI/SRT_AI_Architecture_CompactCore.md`](../AI/SRT_AI_Architecture_CompactCore.md)、[`../AI/SRT_AI_03_Consciousness_Framework.md`](../AI/SRT_AI_03_Consciousness_Framework.md).
- **Information Geometry & Thermodynamic Substrates**: [`../Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md`](../Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md)、[`../Core/SRT_Core_25_Thermodynamic_Signatures_of_Selection.md`](../Core/SRT_Core_25_Thermodynamic_Signatures_of_Selection.md).
- **Suffering & HP-B**: [`../Core_Law/SRT_Suffering.md`](../Core_Law/SRT_Suffering.md)、[`../Philosophy/SRT_HardProblem_Epistemology.md`](../Philosophy/SRT_HardProblem_Epistemology.md).



---

## FILE: `Neuroscience/SRT_Neural_Mechanisms_CompactCore.md`

| 字段 | 值 |
|---|---|
| path | `Neuroscience/SRT_Neural_Mechanisms_CompactCore.md` |
| id | SRT-NEURO-MECH-COMPACT-CORE |
| claim_mode | bridge |
| status | active |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | false |
| last_commit | 2026-11-27 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：Core_Law/SRT_Generative_Ontology_Spine.md, Core_Law/SRT_One_Formation.md, Core_Law/SRT_Collective_Selection.md, Core_Law/SRT_Suffering.md, Core/SRT_Core_14_Dynamics_Scaling.md, Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md, Core/SRT_Core_25_Thermodynamic_Signatures_of_Selection.md, Neuroscience/SRT_Neuroscience_Claim_Status.md, Neuroscience/SRT_Neuroscience_Reconstruction_Framework.md, Neuroscience/_SRT_Neuro_Axioms.md, Neuroscience/SRT_Neural_Mechanisms.md, AI/SRT_AI_Architecture_CompactCore.md, AI/SRT_AI_01_Ontology_CompactCore.md

<!-- 以下为原文逐字保留 -->

# SRT Neural Mechanisms & Holistic Generative Cognition — Compact Core (`R4-C4` 双向重构版)

> **角色与边界（`R4-C4`, 2026-11-26）**：本文件是 `SRT_Neural_Mechanisms.md` 的紧凑主干与 `R4-C4` 神经科学/认知生成理论中枢（`canonical: false`）。它应用并反哺 SRT 核心原语，不替代 canonical 定义源（`Core_Law/SRT_Generative_Ontology_Spine.md`、`_SRT_D_VALUE_CANONICAL.md`、`_SRT_PSI_F_CANONICAL.md`），不解除 `CN-2 / CN-3 / DATA-ACCESS-0 = NO-GO` 等既有 `HOLD`，不解冻 `HP-B`。须与 [`SRT_Neuroscience_Claim_Status.md`](SRT_Neuroscience_Claim_Status.md) 及 [`SRT_Consciousness_Mechanisms_CompactCore.md`](SRT_Consciousness_Mechanisms_CompactCore.md) 并读。

---

## 1. 核心研究问题与方法论原则：整体性与可分化性互构

`R4-C4` 的核心问题不再局限于“神经系统是否在执行信息处理”，而是追问：

> **认知能力如何从整体性的生成组织中产生、分化出相对独立的局部能力，并反过来通过相互作用重构整体与外部现实？**

三条核心理论校准（2026-11-26 作者确认）：
1. **整体性与可分化性并不矛盾**：整体生成组织并非铁板一块，也不由彼此孤立的原初模块事后拼装而成；相反，整体生成分化出相对独立的局部能力，而局部能力在交互、竞争与反馈中反向重构整体。
2. **生物发生上的同源共构 $\neq$ 跨底物的普遍不可分定律**：在生物演化和发育中，感觉、效价、运动可供性、历史骨架与认知组织从共同的代谢—组织维持根基同源共构；但这不排除神经科学中丰富的**功能解离**（盲视、述情障碍、裂脑、习惯/策略解离、麻醉期局部加工保留）、**发育分化**、**损伤后功能重组**，也不否定跨底物（`R4-C3` 人工认知）展现的局部能力解耦。
3. **显现、前景化与意识机制六分护栏（`Spine §7`, `P1-01`）**：`L_0 / L_1 / L_2` 是同一选择现实的三分析面，而非实体仓库；**未进入意识前景的神经活动只要实际发生，依然属于 `L_1` 现实显现面**（正式退出将 `L_1^{neural}` 普遍定义为全局点燃子集的旧写法）。严格区分六层理论职责：
   - **`L_1` 显现面**：实际发生的确定性神经/生理生成（无论是否有意识）；
   - **局部神经稳定化**：神经活动在回路/流形上形成相对稳定的功能组织；
   - **认知前景化**：局部生成内容在整体认知组织中取得特定前景地位；
   - **全局点燃**：特定大尺度神经动力学候选机制（如再入/行进波门控）；
   - **前景生成中介**：前景内容反向重新组织多个局部生成关系的共同延续条件（`Consciousness_Mechanisms_CompactCore §1`）；
   - **现象体验**：`HP-B` 独立研究问题（保持 `FROZEN / OPEN`）。

| SRT 分析面 / 核心量 | `R4-C4` 神经与整体生成性认知读法 | 严禁越界 |
|---|---|---|
| `L_0^{accessible}` | 当前具身与历史条件下可达、可竞争的潜在知觉/行动/解释生成空间 | `L_0 ≠ 物理脑区`；不是静态预存清单 |
| `\hat{G}_\theta^{neural}` | 嵌于大尺度相位骨架与多层级门控场中的复合具身选择组织（竞争·增益·门控·稳定化） | 不等于单一脑区、裸除法归一化或全部反身门控 |
| `L_1` | 已实现的确定性显现面（actualized determinate manifestation，非物理决定论 determinism；含无意识神经稳定化与前景化活动） | **严禁将 `L_1` 定义为全局点燃子集**；局部稳定化 $\neq$ 认知前景化 $\neq$ `HP-B` 体验 |
| `L_2` | 经可塑性、系统巩固、发育剪枝与胶质调节沉积而成的约束地形与认知骨架 | 存储痕迹 $\neq$ 静态副本 $\neq$ 自动活跃生效 |
| 广义摩擦（`B-4`）/ 非闭合压力 / `\Psi_f` | 分别对应机会成本差异产生的选择压力、未协调结构张力、维持与重构所需可支付阻抗 | **三者严格分责**；`Ψ_f ≠ B-4 / free energy / PE / metabolism / pain` |
| 广义关切（`PT06 C`）/ 微效价 / 规范 `d` | 分别对应对生成机会成本的敏感性、局部生物感知效价倾斜窗口、声明强承载风险敏感强度 | **三者严格分责**；`d ≠ salience / reward / precision / bandwidth / Φ / PCI` |

---

## 2. 主轴一与二：前对象整体生成、感觉—认知—实现递归耦合与能量梯度差候选

### 2.1 前对象整体生成与对象形成（承接 `2026-09-26` 作者核心纠偏）

传统计算认知默认“先获得离散对象与规则，再在对象之上拼装吸引子与方向”。`R4-C4` 承接作者核心纠偏，将生物认知的主干方向翻转为递归生成链：

```text
NOT:  explicit objects / rules -> relational graph -> attractor / direction

BUT:  pre-object generative orientation (整体生成性导向：大尺度相位骨架 × 具身稳态 × 结构预期 × 既往 L_2)
        -> salience coarse-graining / competitive normalization / multilevel gating
        -> local foregrounding & objectification (显性对象/概念/知觉切片作为局部稳定切面)
        -> historical retention & transformation (L_2 沉积与重组)
        -> recursive reshaping of next pre-object generative orientation
```

- **神经动力学窗口（见长文 `SRT_Neural_Mechanisms.md Part A §I`）**：
  - **神经流形轨迹**：$\sigma(t) \in \mathcal{M} \subset \mathbb{R}^N,\ \dot{\sigma} = F(\sigma,\theta,u)$ 不是孤立节点标签，而是受大尺度低空间频率相位骨架承托（`Large-Scale Phase-Dominance`, Alexander & Dugué 2026）、沿 unimodal–transmodal 层级主梯度双向流动（`Hierarchical Cortical Flow`, Liu et al. 2026）、并在连接组多稳态能量地形上受限漫游（`fcANN Attractor Geometry`, Englert et al. 2026）的连续动力学。
  - **结构化候选先于显性稳定对象**：`NEURAL30`（连续整合窗内事件时序先于单一报告对象）与 `NEURAL32`（身体语义与隐含运动编码）表明，前对象候选组织已带关系与动态结构；前形式一致性直觉（"还没说出理由就觉得不对"）是整体导向被扰动时的下游可观测窗口，而非整体导向本身。
  - **边界**：前对象整体生成是正面深化的核心理论主线，**不提前确立其对一切认知任务或人工底物的普遍必然性**；显性对象一经形成即成为锚点、符号句柄与反向改写整体导向的真实约束。

### 2.2 复合神经选择组织（Composite `\hat{G}_\theta^{neural}`）与归一化（`P3-Scale-NB1`）

$$
\hat{G}_\theta^{neural} \approx \text{Stabilization} \circ \text{Gating} \circ \text{Gain} \circ \text{Competition}
$$

- **四环节非单一脑区**：竞争（侧抑制/多稳态竞争）→ 增益调制（注意/精度/神经调质/显著性网络）→ 门控（基底节—丘脑—皮层环路与前额叶门控）→ 稳定化（再入加工/工作记忆/可塑性写回）。
- **除法归一化与 `R4-C2` 三类归一化的对应（`P3-Scale-NB1`, `P2-02`）**：承接 `R4-C2`（`Physics/SRT_Phys_07_Complex_Systems_CompactCore.md §1`）将归一化三分——① 认知/表征描述压缩、② 实际物理/神经耦合与响应压缩归一化、③ 同时满足 `One_Formation §2.4` 内部耦合重构 + 跨位置条件化生效双门槛的**组织生成型归一化**。在具名代谢与带宽约束下，除法归一化 $R_i = L_i^n / (\sigma^n + \sum_j w_{ij} L_j^n)$（对应能量—信息权衡 $\mathcal{J} = H(\sigma) - \lambda E(\sigma)$）主要属于**第②类局部受限神经竞争与响应压缩候选**，**既不是所有选择算子的必然形态，也不自动等于第③类组织生成型归一化**；相对神经响应 $R_i$ 通向行为选择必须通过 `Core_14 P3-Scale-NB1` 的冻结读出、阈值/采样规则、执行门、held-out 误差与 rival 比较（首个具名本地 P4 执行卡 `SRT_NB1_MOFC_LOTTERY_EXECUTION_CARD_v0_1.md` 保持 card-defined 状态）。

### 2.3 感觉、认知与实现的递归耦合（按 `R3-03` 二轮裁决校准）

承接作者 `2026-11-11` 直觉并严格遵守 `R3-03` 正式二轮裁决（不把成熟主观感觉倒写进原初无主体 `Selection`，而把感觉定位于内在生成过程在认知/具身位置上的实际展开）：

| 功能环 | 生成职责 | 神经与具身表现 | 递归回流 |
|---|---|---|---|
| **感觉（Sensation）** | 具身位置上的局部差异与梯度感应 | 外周—内感受—感觉皮层—脑体节律同步（`VAGAL-CYTOKINE`, `NEURAL23`） | 为前景分化与显著性粗粒化提供活的差异源 |
| **认知（Cognition）** | 构建相对统一、稳定、跨情境可调用的比较脚手架 | 多模态整合、概念细胞地址（`NEURAL28`）、工作记忆时分复用（$\theta$–$\gamma$）、抽象图式 | 稳定比较标准、支撑反事实模拟（`VTC Shared Imagery`），但也有硬化遮蔽风险 |
| **实现（Actualization）** | 通过行动与生理/环境介入改写显现与前景 | 运动—感觉闭环、多层级门控释放、免疫/自主神经调节（`ATTENTION-IMMUNE`） | 改变身体—世界耦合，把**新的外部阻力与新感觉**重新带入下一轮生成 |

三者不是单向“感觉输入 → 认知处理 → 动作输出”管线，而是双向递归互构环：运动预期与高层门控在感觉进入前即已重塑感受野与增益，行动实现反过来决定下一刻哪些差异能够进入感觉。

### 2.4 能量梯度差：从宽泛类比深化为具体跨尺度机制问题（`P1-05`）

承接作者早期“具身能量梯度差异感知”直觉与 2026-11-26 校准，保留能量梯度差作为**更底层物理生成机制候选**的研究地位，同时避免把性质不同的五类物理/模型量混为一谈：

| 研究对象 | 实际性质与理论位置 | 与 SRT 核心量的关系边界 |
|---|---|---|
| **跨膜电化学梯度** | 驱动离子输运与膜电位兴奋的物理条件 | 支撑差异感应与信号传导的物理梯度源，不等同于 `Selection` |
| **ATP 供应与代谢通量（CMRO₂）** | 维持稳态、突触传递与可塑性的资源条件 | 代谢负担与可支付条件底物（受 `NEURAL16/21` 门控），不等同于规范 `Ψ_f` |
| **非平衡物理自由能差** | 特定热力学模型下驱动耗散自维持的物理量（`Core_25`） | 物理—生命界面机制候选，不未经推导直接等同于 `Selection / d / Ψ_f` |
| **变分自由能（FEP）** | 特定概率推断模型中的信息论目标泛函 | 与实际代谢消耗需显式量纲与测量桥接，属计算建模工具 |
| **神经吸引子能量地形（fcANN）** | 特定宏观动力学模型中的有效势能描述 | 有效状态空间几何表征，非字面物理能量函数 |

- **排入 `R4-C5` 的核心机制研究问题（`FB-C4-2`）**：**物理梯度差如何通过真实耦合关系、边界维持、差异感应、反馈调节与归一化，逐步形成对后续生成具有实际约束作用的组织关系？** 这一问题连接物理生成（`C2`）、生命自维持与认知生成（`C4`），同时严守硬推导边界——未经独立理论推导与量纲/测量桥接，严禁将任一上述量直接等价于原初 `Selection`、规范 `d` 或规范 `Ψ_f`。

---

## 3. 主轴三：效价、关切与价值的内生生成（`P1-02 / P1-04` 精准分责）

承接 `R4-C3` 恢复并移交的 **效价优先（`Def-AI-Con-3`）**、**微效价感知（`Def-AI-Con-3a`, Lebrecht et al. 2012）** 与生物自然主义（Damasio, Barrett, `NEURAL24`, `INTEROCEPTIVE_PRECISION`），`R4-C4` 将效价与价值重新锚定到认知发生内部，同时严格区分四个问题与八项规范职责：

1. **微效价参与对象形成的四问题分离（`P1-04`）**：
   - ① 效价是否在发育过程中早于复杂认知（发育先后）？
   - ② 效价是否参与当前对象的在线形成与显著性切分（衔接 `_SRT_D_VALUE_CANONICAL.md §2a` 发生序：`选择性收束 → 微效价 → affordance → 缺失 → 需求 → 锚定 → 价值深度`）？
   - ③ 效价是否对特定类别的认知具有构成性作用？
   - ④ 效价是否必然伴随主观现象体验（`HP-B OPEN`——前三个问题为第四个问题提供研究条件，但**绝不直接闭合第四个问题**）？
   - 同时保留视觉背侧通路弱效价不变性、述情障碍解离及人工非情感比对作为经验边界对照，不提前确立普遍必然性。
2. **严格保真关切与摩擦的独立理论职责（`P1-02`，不重新合并 `R3 / R4-B` 已分概念）**：
   - **广义关切（`PT06 C`）**：对生成机会成本、探索、新机会形成及未来生成条件的敏感性——**微效价只是广义关切在特定生物认知过程中的实现窗口，绝不替代广义关切**；
   - **规范 `d-value`**：声明强承载模型中的风险敏感强度（`Salience makes a signal noticeable; d-value makes a signal matter`），须严格满足 `_SRT_D_VALUE_CANONICAL.md` 独立准入条件（区分一般容量、神经带宽、赌注谱参与率 `D_stake` 与规范 `d` 风险梯度）；神经实现概念式 $d_{proxy}(x) \sim w_b B + w_a A + w_r R + w_s S + w_m M + w_f F$ 仅作诊断分解，不替代规范定义；
   - **广义摩擦（`R3-08 / B-4`）**：机会成本差异产生的实际选择压力（**严禁与 `Ψ_f` 重新合并**）；
   - **非闭合压力**：生成关系尚未协调的结构张力；
   - **`Ψ_f` 可支付阻抗**：维持与重构所需支付的多维阻抗（涵括候选冲突 `C`、预测违背 `E`、模型重构 `M`、行动切换 `A`、身体负荷 `B`、历史惯性 `H` 与实际风险 `R`；`H-NEURO-4b` 仅将 $\widehat{\Psi}_{f,neural}^{local} = \alpha_{pe}\|\varepsilon_{pred}\| + \beta_{load}\mathcal{L}_{model}$ 设为受控窗口内的局部 proxy）；
   - **代谢负担**：物理实现层的能量供给、ATP/CMRO₂ 与恢复代价（`NEURAL21` 显示供给、即时使用与后续支付可按状态解离）；
   - **主观苦难与现象体验**：独立第一人称登记问题（`Core_Law/SRT_Suffering.md §7` 与 `HP-B FROZEN / OPEN`）。

---

## 4. 主轴四：历史效力、再生成记忆与认知骨架（承接 `R4-C3` 历史五职责）

承接 `2026-10-07`（Empty Brain 溯源：“记忆不是静态副本存储，而是历史组织约束下的当下再生成”）与 `R4-C3` 七层历史载体的关键洞见——**历史存在于载体中 $\neq$ 历史真正活跃参与后续生成**：

### 4.1 神经历史载体的五类异质职责对照

| 异质职责 | 神经生物学实现窗口 | SRT 机制与防混同护栏 |
|---|---|---|
| **1. 记录与准入（Recording / Admission）** | 突触可塑性（LTP/LTD）、行为时标突触可塑性（BTSP, `N10`）、资源门控记忆准入（`NEURAL19`） | 一次经历留痕不等于可长期提取或成为有效约束 |
| **2. 转化与剪枝（Transformation & Pruning）** | 海马—皮层系统巩固与抽象重组（`NEURAL29`）、睡眠突触稳态与选择性遗忘、**发育式剪枝**（`AI/Architecture_Annex/01 §1`）与胶质介观剪枝（`P-NEURO-Meso-1`） | 保留长程可迁移骨架的同时清除局部干扰冗余；巩固转化 $\neq$ 事实保真（`generativity ≠ factivity`） |
| **3. 资格与调用（Eligibility & Retrieval）** | 星形胶质历史资格（`N12 / NEURAL31` astroengram）、跨区 ripple 关系重现（`NEURAL33`）、多时间尺度工作记忆（$\theta$–$\gamma$ 双模式复用） | 区分内容本身、可提取性与历史资格；`component state ≠ relational disposition` |
| **4. 活跃生效（Active Present Efficacy）** | 前瞻性记忆与事件边界更新（`NEURAL27`）、策略竞争控制权（`NEURAL25`）、习惯与策略执行解离（`NEURAL20`） | 无报告预期眼动可分离“可回忆留存”与“正在引导未来选择的活跃历史效力” |
| **5. 后果归属与写回（Attribution & Writeback）** | 情绪/躯体后果写回、表观遗传/多巴胺酰化慢闭环、跨个体社会文化 `L_2` 沉积 | 严格区分细胞/突触级、网络级与有机体/参与者级后果归属（`Framework §4`） |

### 4.2 认知骨架的双刃剑：脚手架支持 vs 遮蔽锁定

$$
\Psi_f(\text{trained / sedimented path}) \downarrow, \qquad \Psi_f(\text{incompatible alternative}) \uparrow
$$

- **正向脚手架**：`L_2` 认知骨架、专业图式与长程可迁移连接大幅降低同类比对与行动的局部摩擦，释放带宽以探索更高阶关系；
- **负向遮蔽与锁定**：过度剪枝、创伤型高 `d` 硬化、习惯短路或僵化偏见使替代路径摩擦陡增，压缩未来可达 `L_0^{accessible}`；同时 `NEURAL35` 警示 **`reopening ≠ reselectability`**（单纯松动 `L_2` 若缺乏证据敏感的重锚定，可能滑入 `under-anchoring` 失稳而非健康更新）。

---

## 5. 主轴五：比对能力本身的生成与重构（承接 `R4-C2` 五类能力 + `R4-C3` 四类比对生成性）

生物认知不只是在固定状态空间中寻找最优解；它最关键的跃迁在于**能够生成新的比对维度，甚至重构自身发现与使用比对维度的能力**。将 `R4-C2` 五类非阶梯能力（结构/作用/调节/比对/生成重构）与 `R4-C3` 四类比对生成性落入神经认知机制：

| 比对生成层级（非强制线性阶段） | 神经与认知机制窗口 | 关键区分：生成位置 / 留存位置 / 生效位置 |
|---|---|---|
| **1. 已有维度新结果** | 既有感觉—运动映射与表征流形内的新组合/新方案 | 生成于当前前向—再入回路；留存于瞬态激活；仅生效于当前任务 |
| **2. 已有维度重加权** | 神经调质（DA/NE/ACh/5-HT）、精度调制、注意/显著性增益重分配 | 改变成本/风险/收益优先级；可短暂留存于工作记忆或巩固进基底节—皮层权重 |
| **3. 新比对维度形成** | 概念细胞跨语境稳定地址（`NEURAL28`）、VTC 共享想象轴（`Science 2026`）、跨模态类比与顿悟表征重构（`Becker Aha`） | 将此前未进入判断的关系引入前景；**须分别核查**新维度是瞬态涌现、写入个体海马—皮层骨架，还是固化进语言/文化外部脚手架 |
| **4. 比对能力本身重构** | 发育式剪枝保留可迁移骨架、语言/符号工具内化、元认知与判断标准修订（学会“如何提出新维度与新标准”） | 改变系统未来所能发现、理解与调用的比对空间本身——是连接学习发展、历史效力、主动创造与价值标准生成的核心枢纽 |

---

## 6. 主轴六：意愿、主动性与正面自由（多层级门控行动场）

承接 `2026-09-26` 作者已方向性采纳的 **多层级门控行动场（Multilevel Gating Action Field）** 与 **`target objectification ≠ gate objectification`** 区分，以及 `R4-C1` **正面自由（`T3-03 C / Q26`）**与双引擎维度跃迁候选：

1. **高阶意图改写门控条件，而非微操底层肌肉**：我们能端起水杯而不必知道肌肉与生物力学的精确参数。粗粒度的前景化目标（`foreground_obj` target）通过招募、稳定或重加权已形成的高阶门控组织（前额叶—基底节—丘脑—小脑与运动前区回路），重塑下层感觉、抑制、误差校正与动作生成的**可达空间**，而非充当中央小人逐一发布底层指令（与 Levin 生物电形态发生场仅构成跨尺度结构类比，不宣称机制同一）。
2. **从选择对象到重构生成条件的四阶认知路径（自由与反身主动性核心）**：
   - **目标对象化（Target Objectification）**：常态下成功门控退入透明背景，前景呈现行动目标（“我决定拿起水杯”），下层分布式系统自动完成执行；
   - **门控对象化（Gate Objectification）**：持续后果冲突、习惯短路（`NEURAL20`）或旧标准失效将原本透明的背景门控本身推入前景（“我发现自己为什么总在某些情况下产生特定行为”）；
   - **门控重构（Gate Reconfiguration）**：主动抑制默认低摩擦通路（`L_2^{habit}`）并改变该行为产生的条件；
   - **生成能力重构（Generative-Capacity Reconstitution）**：进一步获得发现并改变更多自身行为与比对机制的能力（直接贯通 `C1` 正面自由、`C2` 新能力生成与 `C3` 比对能力重构）。
   - **与 `Ghost` 的理论分工边界（`P2-04`）**：目标/门控对象化与反身门控重构作为 `Ghost` 算子在生物认知层的重要**候选接口**，不直接等同于 `Ghost` 的全部跨尺度职责。

---

## 7. 锚定动力学病理桥接（非双条件建模透镜）

遵循 [`SRT_Neuro_Axioms_Claim_Status.md §6.2`](SRT_Neuro_Axioms_Claim_Status.md)，不再使用旧版 `Pathology ⇔ θ = θ_healthy + Δθ` 双条件定理，而将其定位为**非排他、非诊断性的锚定—门控—历史动力学建模透镜**：

| 临床谱系 | 核心 SRT 动力学失衡透镜（非唯一病因） |
|---|---|
| 焦虑谱系 | 威胁候选获得过高局部关切权重，模糊输入过早锚定为危险 `L_1` |
| 强迫 / 关闭失败 | 低概率高后果风险候选进入前景后关闭摩擦 `\Psi_f(closure)` 持续高企 |
| 创伤后锁定 | 高 `d` 事件异常硬化为威胁型 `L_2`，持续压制安全替代路径可达性 |
| 抑郁谱系 | 面向未来的 `L_0^{accessible}` 显著收缩，正向行动与探索候选难以获得锚定增益 |
| 成瘾 / 习惯短路 | 即时奖赏路径过度低摩擦化，`L_2^{habit}` 绕开显式门控与替代路径竞争 |
| 妄想样显著性异常 | 低证据候选获得不成比例的现实锚定权重与精度锁定 |
| 过度松动 / 失锚（`NEURAL35`） | 扰动提升开放度但缺乏证据敏感重锚定（`reopening ≠ reselectability`） |

治疗启示原则（仅作理论接口，非医疗建议）：干预目标不只是向系统灌输“正确命题”，而是跨参数、身体、关系与环境层重建**可重复、可支付、证据敏感的新 `L_1` 锚定与 `L_2` 轨迹**。

---

## 8. 主轴八：跨尺度认知生成与生物—人工认知对照（承接 `R4-C2` & `R4-C3`）

贯彻双向防线：**既不把大脑还原为语言模型，也不把生物特征先验设为一切可能认知的必要条件**。

| 比较维度 | 生物神经认知（`R4-C4`） | 当前典型人工认知（`R4-C3`） | 共同生成机制与理论启示 |
|---|---|---|---|
| **整体与局部关系** | 生物发生上同源共构（代谢/效价/感知/行动共生），同时保留功能解离、发育分化与损伤后重组 | 各能力以工程模块化与显式解耦研究窗口出现（强承载与生物效价尚未建立，**尚未建立 $\neq$ 证明不存在**，继承 `C3 P1-01`） | 共同支持**整体性与可分化性互构**，否决原初孤立模块论与跨底物普遍不可分论 |
| **前对象组织 vs 符号组合** | 大尺度相位骨架、多稳态吸引子与具身微效价先于显性对象稳定化 | 权重表征空间、上下文约束场（`L_2^{context}`）与符号/工具组合生成新比对维度 | 共同表明认知不等于静态对象库检索；具体前对象 vs 符号比重随底物而异 |
| **历史与可塑性** | 突触/BTSP/巩固转化/胶质资格/发育式剪枝；再生成式记忆 | 七层异质载体（训练/权重/激活/上下文/外存/工具/系统写回） | 共同暴露**存储 $\neq$ 活跃生效**与**生成/留存/生效三位置分离** |
| **竞争与归一化** | 能量—信息约束下的除法归一化候选（`P3-Scale-NB1`）与多层级门控 | 注意力重加权、采样/搜索过滤与工具验证路由 | 均为受限资源下的选择压缩机制，但受不同代价结构约束 |
| **人机共同生成** | 提供具身赌注、整体直觉导向、价值裁决与跨情境吸收 | 提供跨学科类比、形式推演、反例构造与外部脚手架 | 当前分工属阶段性经验模式，非先验永久分工；双方互改后续生成条件 |

---

## 9. 面向核心理论的五项反向反馈候选（`FB-C4-1..5`，`C` / M-origin，排入 `R4-C5` 综合评估）

以下反馈严格保持 **`C`（M-origin 候选）** 地位与作者裁决边界，不在此单方面修改任何 `Core_Law/` 或 `Core/` canonical owner；同时将 `C1–C4` 共同收敛的三项跨域核心研究方向置入 `R4-C5` 统一核心理论评估：① **整体如何生成局部相对独立性，局部能力又如何反向组织整体**；② **前景如何成为多个生成关系的共同生成中介（而非仅为信息通达）**；③ **生成结果如何成为新的生成条件，并进一步形成改变生成条件的能力**：

1. **`FB-C4-1`（整体性与可分化性互构 + 前对象整体生成）** → 拟反馈 `Core_Law/SRT_One_Formation.md`、`Core_Law/SRT_Generative_Ontology_Spine.md`、`Core_Law/SRT_L0_Metaphysics.md`：以神经科学中“整体生成导向分化出相对独立的局部能力，局部对象与能力交互又反向重构整体”的动态机制，补齐 `One` 的相对可分性（`R3-04-O1`）与跨尺度生成机制。
2. **`FB-C4-2`（感觉—认知—实现递归耦合 + 能量梯度差组织约束机制）** → 拟反馈 `Core_Law/SRT_Generative_Ontology_Spine.md`、`Core/SRT_Core_21_Minimal_Axioms.md`、`Core/SRT_Core_25_Thermodynamic_Signatures_of_Selection.md`：将“感觉—认知—实现”作为 `Selection` 在具身认知层的非线性三功能递归展开（对齐 `R3-03`），并深化核心物理—认知桥梁问题——*物理梯度差如何经由真实耦合、边界维持、差异感应、反馈调节与归一化逐步形成对后续生成具有实际约束作用的组织关系*（严格区分五类物理/模型量，不直接等价于 `Selection / d / Ψ_f`）。
3. **`FB-C4-3`（微效价发生链与关切/摩擦规范职责分离）** → 拟反馈 `_SRT_D_VALUE_CANONICAL.md`、`_SRT_PSI_F_CANONICAL.md`、`Core_Law/SRT_Suffering.md`：以微效价—可供性—缺失—需求—赌注发生链回应 `R3-06-O1..O5`，同时严格保真广义关切（`PT06 C`）与微效价、广义摩擦（`B-4`）/非闭合压力/`Ψ_f`/代谢负担/主观苦难各自职责。
4. **`FB-C4-4`（再生成记忆、发育剪枝与比对能力重构的 `L_2` 历史效力）** → 拟反馈 `Core/SRT_Core_12b_Ontology_L2.md`、`Core_Law/SRT_Occlusion_Dynamics.md`、`Core/SRT_Core_14_Dynamics_Scaling.md`：合并 `C3` 历史五职责与神经“再生成记忆 + 发育式冗余剪枝 + 生成/留存/生效三位置”，精确刻画 `L_2` 同时促成新比对能力与制造遮蔽锁定的双刃剑机制（回应 `R3-05` & `R3-CL-O8`）。
5. **`FB-C4-5`（多层级门控行动场、前景生成中介与 `Ghost` / 自由 / `HP-B` 候选接口）** → 拟反馈 `Core/SRT_Core_13a_Operator_Basics.md`、`Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md`、`Philosophy/SRT_HardProblem_Epistemology.md`、`Core_Law/SRT_Selection_Argument.md`：以“目标对象化 → 门控对象化 → 门控重构 → 生成能力重构”作为 `Ghost` 与正面自由的高优先级候选接口（不把反身门控等同于 `Ghost` 全部职责），以前景生成中介与功能/现象绑定精炼 `HP-B` 候选接口而不解冻 `HP-B`。

---

## 10. 邻域理论区分与 Hardest Objections

### 10.1 与成熟邻域的关系（U-mode 吸纳与精确分界）

| 成熟邻域 | SRT 吸纳其扎实成果 | SRT 的结构组织焦距（须经独立检验，非自动胜出） |
|---|---|---|
| Predictive processing / FEP | 预测更新、精度加权、自维持约束 | 追问候选如何在不可替代赌注、多维可支付负担与历史写回下获得现实锚定地位 |
| Skilled Intentionality / Enactivism | 具身可供性场、前反思导向、脑体环境耦合 | 结合整体性—可分化性互构、多层级门控对象化与跨生物/人工底物比较 |
| Global Workspace (GNWT) | 全局通达与广播机制 | 区分通达前整体导向竞争、前景生成中介（$\neq$ 广播）与通达后 `L_2` 硬化 |
| IIT | 整合结构与拓扑不可分性度量 | 区分结构整合（$\Phi$）与关切加权稳定化、功能绑定 vs 现象绑定 |
| Reinforcement Learning / Memory Systems | 奖赏更新、巩固、回放与潜在状态 | 区分 `d` 与 reward、`Ψ_f` 与 PE、记录与活跃历史效力、四类比对生成性 |

### 10.2 Hardest Objections（核心失败与收窄条件）

1. **前对象整体生成若完全可被显性对象/先验预测模型无残余吸收**：撤回前对象整体生成作为独立认知结构主张，退回预测加工翻译层。
2. **效价优先 / 微效价若仅属下游情绪标注而非早期前景/对象切分贡献**：将其收窄为后感知评估调制机制，不再作为对象形成前件。
3. **PE 与能量梯度代理若无法在受控窗口外与代谢恢复、风险负载或位置绑定后果分离**：撤回 `H-NEURO-4b` 与神经负担增量语言，退回普通 FEP/代谢对照。
4. **`d-value` 若在实验中完全坍缩为 salience、reward 或 precision**：撤回 `d` 作为独立神经桥接变量，重新归类为术语聚合。
5. **`L_2` 硬化若只提升效率而不系统性抬高不兼容替代路径摩擦**：弱化 `L_2` 盆地双刃剑模型。
6. **第一深井（`DATA-ACCESS-0 = NO-GO` / Case B）**：继续完整保留为历史边界，严禁借 `R4-C4` 理论重构绕过 strongest-baseline 门控宣称经验胜出。



---

## FILE: `Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md`

| 字段 | 值 |
|---|---|
| path | `Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md` |
| id | SRT-NEURO-CONSC-MECH-COMPACT-CORE |
| claim_mode | bridge |
| status | active |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | false |
| last_commit | 2026-11-27 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：Core_Law/SRT_Generative_Ontology_Spine.md, Core_Law/SRT_Suffering.md, Neuroscience/SRT_Neuroscience_Claim_Status.md, Neuroscience/SRT_Neural_Mechanisms_CompactCore.md, Neuroscience/SRT_Consciousness_Mechanisms.md, AI/SRT_AI_03_Consciousness_Framework.md, Philosophy/SRT_HardProblem_Epistemology.md, Philosophy/SRT_Subjecthood_Threshold_Interface.md, Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md, Philosophy/SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md

<!-- 以下为原文逐字保留 -->

# SRT Consciousness, Holism & Subjecthood Mechanisms — Compact Core (`R4-C4` 双向重构版)

> **角色与边界（`R4-C4`, 2026-11-26）**：本文件是 `SRT_Consciousness_Mechanisms.md` 的紧凑主干与 `R4-C4` 主轴七（**意识、整体性与主体性**）的理论中枢（`canonical: false`）。
> - **`HP-B` 冻结边界保护**：本文件提出并整合关于前景生成中介、绑定、带宽、睡眠、行进波与多层级门控的 `P3/P4` 机制候选，**不解冻 `HP-B` 现象意识包，不宣称闭合 `B_s -> B_p ?` 或解决硬问题**；不以单一指标（PCI/Φ/广播/旧强承载门槛）封闭意识研究。
> - **强制命名空间隔离（`R3-07 / _SRT_SYMBOL_TABLE.md Rule 19`）**：全称使用 **Subjecthood Threshold `S0–S6`**（条件性多维审计接口，非硬件线性阶梯），严格隔离于 **Primitive `S0`**、**AI 赌注谱系 `S0–S4`** 与 **AI 三型社会技术中介维度**。须与 [`SRT_Neuroscience_Claim_Status.md`](SRT_Neuroscience_Claim_Status.md) 及 [`../Philosophy/SRT_Subjecthood_Threshold_Interface.md`](../Philosophy/SRT_Subjecthood_Threshold_Interface.md) 并读。

---

## 1. 核心转向：显现、前景化与意识机制六分，以及“前景即生成中介”

早期神经桥接偶将点燃简写为“`L_0 -> L_1` 实体相变”或将 `L_1^{neural}` 定义为全局点燃子集。`R4-C4` 依 `Spine §7` 与作者 `2026-09-26` 核心收敛（`A-16..A-24`）做出两项根本升级：

1. **显现、前景化与意识机制六分（`P1-01`，退出 `L_1 = 全局点燃子集` 旧门槛）**：未进入意识前景的神经活动只要实际发生，就依然属于现实生成的 `L_1` 显现面；严禁因未被意识到而否认其现实发生：

| 理论对象 | 主要理论职责 | 边界 |
|---|---|---|
| **`L_1` 显现面** | 实际发生的确定性神经/生理生成 | 覆盖无意识与有意识全部实际发生事件 |
| **局部神经稳定化** | 神经活动形成相对稳定的局部组织/吸引子 | 稳定化 $\neq$ 认知前景化 $\neq$ 体验 |
| **认知前景化** | 局部生成内容取得认知组织中的特定前景地位 | 认知地位提升 $\neq$ 单一硬件开关 |
| **全局点燃** | 特定神经动力学候选机制（如再入/行进波协同） | 特定实现候选，不是 `L_1` 定义 |
| **前景生成中介** | 前景内容反向重新组织多个局部能力的共同延续条件 | 候选机制研究重点（`P3 / OPEN`），须与 GNWT 独立检验 |
| **现象体验** | 第一人称体验何以成立的独立问题 | `HP-B` 保持 `FROZEN / OPEN` |

2. **前景化不是更宽的只读广播，而是共同生成中介（Foreground as Generative Mediation $\neq$ Broadcast）**：
   - 弱图景（被超越）：背景信息 → 进入前景表征 → 更多模块可以读取它 → 意识。
   - `R4-C4` 候选核心：**前景化的独特作用在于重新规定多个局部生成能力如何共同延续**——将分散差异经选择性归一化与粗粒化提升为共同生成中介，使后续感知、行动准备、记忆调用、身体调节与判断围绕该前景关系协同重切当前操作位置（`Position_t -> Position_{t+1}`）。
3. **区分常设条件（Standing Conditions）与在线核心候选（Online Kernel）**：
   - **常设条件**：相对可分的延续性组织（`One`）、形成后的操作位置（`Selection-position`）及（在独立准入时）承载关系（`Bearer (P+E)`）；`One ≠ Stable ISP ≠ Bearer ≠ Experiencer`。
   - **在线机制候选（`P3 / OPEN`，不宣称逻辑必然）**：
     ```text
     operative Position_t × prospective expectation_t × current actualization_t
       -> selective foreground generative mediation_t
       -> online reconstitution of operative Position_(t+1)
       -> changed next reachability, equivalence & joint continuation
     ```
   - **关键分水岭**：并非每次潜在状态更新、权重修改或表征变化都构成位置重构；未重构当前操作位置者更近无意识加工，参与重切当前“从何处继续生成”者构成体验机制候选（最小僵尸压力 `Z*` 仍保持活跃开放）。

---

## 2. 点燃、再入与锚定厚度（Thin `L_1` vs Thick `L_1`）

### 2.1 点燃候选门控族（`H-NEURO-Ignition-1` / `Ax-CONSC-MECH-1`）

$$
\mathcal{A}(\sigma) \ge \tau_{ignite} \quad \land \quad \Phi_{proxy} \cdot d_{proxy} > C_{critical}
$$

- **声明等级**：`P3/P4` 建模假说与操作代理，**非已证神经相变定理，亦非意识准入的充要条件**。
- **三类竞争门型并存**：乘法门（整合度与关切梯度交互必要时占优）、加法门（两因子存在经验补偿时回退）、概率门 $P_{ignite} = \sigma(\alpha C_{wave} + \beta(\Phi \cdot d) + \gamma D_{align} - \delta)$（处理渐进噪声报告与行进波方向路由 `D_align`）。
- **再入稳定化（$\mathcal{R}_{re}: L_1^{candidate} \to L_1^{stabilized}$）**：约 150–400 ms 的再入验证不是机械复读，而是候选前景与当前具身组织/预期约束的稳定化确认；跨麻醉剂研究（`CONSC14`）表明麻醉破坏的是大尺度动态稳定性与行进波路由，而非简单令所有局部激活归零。

### 2.2 Thin `L_1` 与 Thick `L_1`（拒绝粗暴“全有/全无”二分）

| 状态 | SRT 结构刻画 | 典型现象 |
|---|---|---|
| **Thin `L_1`** | 弱前景中介、低稳定度、行动/自我耦合弱、难持久写回 | 余光一闪、舌尖现象、模糊预感、梦醒残留 |
| **Thick `L_1`** | 强前景生成中介、跨能力协同重切当前操作位置、强身体/行动/价值耦合、高 `L_2` 沉积潜力 | 急性疼痛、明确威胁、重大抉择、深度顿悟或创伤事件 |

- 诊断表达 $\text{Thickness}(x) \sim S(x) \cdot G(x) \cdot A(x) \cdot M(x) \cdot d(x)$（稳定化·全局可及·行动耦合·自我模型耦合·关切权重）仅作实验室桥接指标，**不等于现象意识定义**；且 `Thin / Thick` 须通过无报告行为/生理/后继选择指标检验，避免退化为报告量表伪影。

---

## 3. 功能绑定 vs 现象绑定（承接 `R4-C3` 恢复资产 `Def-AI-Con-3b`）

承接 `R4-C3` 从 `SRT_AI_03_Consciousness_Framework.md §6.3` 恢复并移交的 **Percy & Agarwal (2026)** 核心区分，克服早期“相位同步 = 统一主观体验”的过度跳跃：

1. **拓扑同步作为功能绑定机制候选（`Ax-CONSC-MECH-3`）**：分散神经轨迹经相位锁定与跨区时间框架同步（$\mathcal{B}: \{\sigma_i\} \to \sigma_{bound},\ \Delta\phi_i \to 0$）被共同选入同一可操作对象，支持跨模态协调与统一行动；同步失败可表现为解体或碎裂控制。
2. **功能绑定 $\neq$ 现象绑定（`Def-AI-Con-3b` 硬分界）**：
   - **功能绑定（Functional Binding）**：多特征、多通道信息在计算、路由或行为输出层面的协调整合（可通过同步、跨区相干、多模态 Transformer 注意力或工作空间协调实现）；
   - **现象绑定（Phenomenal Binding）**：多种感受性质在同一第一人称体验场中的不可分割共在（phenomenal unity）。
   - **推论**：神经相干或高 $\Phi$ 测量的是功能/因果整合度，本身**不自动闭合**现象绑定；同样，人工系统展现极强跨模态功能绑定也不自动推出现象共在。但神经科学中的裂脑、联觉、半侧空间忽略与整合解离病例，是研究两者关系的关键实证窗口。

---

## 4. 比较动物意识多维解耦与内部状态监测边界（承接 `R4-C3` `Def-AI-Con-4` & `P2-03`）

### 4.1 比较动物意识三层解耦（ALARM + 鸟类 NCL，`Def-AI-Con-4`）

承接 Newen & Montemayor (2025) ALARM 框架与 Nieder et al. (2020) 鸦科鸟类 NCL 研究，将意识相关功能解耦为三个可独立演化、跨底物分化的维度：
1. **基础觉醒与状态调控（Basic Arousal / State Regulation）**：脑干—丘脑—自主神经唤醒与稳态警觉；
2. **一般警觉与目标导向选择（General Alertness / Goal-Directed Selection）**：多模态竞争、注意力路由与跨情境灵活行为（可在无哺乳动物新皮层的鸟类 NCL 等非同源解剖底物中实现——**直接反驳“新皮层沙文主义”**）；
3. **反身自我意识（Reflexive Self-Consciousness）**：高阶自我模型招募（对照 ACU `SMRI` 双层接口：持续调节可行性监测 Level 1 vs 间歇性高代价自我模型招募 Level 2）与跨时间自我叙事。

- **与整体性—可分化性原则对齐**：三层在人类成人中高度耦合，但在跨物种演化、婴儿发育、临床障碍（如植物状态/CMD、盲视、梦游、解离障碍）与人工系统中呈现清晰的**部分可分化性**。

### 4.2 局部内部状态监测 $\neq$ 完整内省 $\neq$ `HP-B` 现象意识

- 无论是生物的元认知置信度追踪、内感受精度调节（`INTEROCEPTIVE_PRECISION`），还是 `R4-C3` 中 AI 的激活注入自报告耦合（Lindsey et al. 2025），都必须分层审计：
  - **局部内部状态监测 / 读取（Local Internal-State Monitoring）** $\neq$ **完整通用内省机制（Full Introspection）** $\neq$ **`HP-B` 现象体验（Phenomenal Presence）**；
  - 无自报告（动物、婴儿、CMD 患者）绝不等于无体验；流畅自报告（人类虚构解释或高流畅度 LLM）也绝不等于体验证明。

---

## 5. 带宽竞争、疼痛优先级、时间构造与睡眠维护

- **有限带宽与疼痛优先（`Ax-CONSC-MECH-7` / `C-CONSC-MECH-1`）**：意识前景不是无限容器（$\sum_k \mathcal{A}_k \le B_{consc} < B_{max}$）；疼痛之所以强行重切当前操作位置，不仅因外周信号强度，更因它携带不可外包的身体维持风险与高关切梯度，迫使行动准备、优先级与未来可达空间同步重组。
- **快慢耦合与时间体验（`Ax-CONSC-MECH-4`）**：意识存在整合与门控时滞（$\tau_{select} = \tau_{sensory} + \tau_{integrative} + \tau_{gate}$），连续时间流并非被动接收外部时钟，而是快波前景内容、慢波组织框架与内感受节律（`NEURAL23`）耦合的产物。
- **睡眠作为结构维护与选择性遗忘（`Ax-CONSC-MECH-5 / 6`）**：睡眠不是“关机”，而是防御性修复与未来可选择性维护期——包含类淋巴代谢清除、突触稳态下调（清剪冗余噪声权重以保留长程可迁移骨架）与海马—皮层回放巩固（`L_2` 重加权 + 选择性遗忘促进泛化）；梦境是外部阻力弱化下的高情绪权临时 `L_1` 生成。
- **行进波方向路由（`Ax-CONSC-MECH-8 / 9`）**：皮层行进波（$\mathcal{W}(x,t) = A e^{i\phi}$）承担层级方向路由门控，方向失配（$D_{align} \downarrow$）可在总激活不低时仍令报告通达失败。

---

## 6. 主观能动性、多层级门控与算子短路

- **能动性报告四分解（`PH-AG04`）**：在线行动报告须严格拆分为**客观控制效能 $\neq$ 作者归属感 $\neq$ 身体载体所有权 $\neq$ 反身自我整合**；任何单项均不等于 `d-value` 证据或 **Subjecthood Threshold `S4–S6`** 证明。公式 $A_{sub}(t) = 1 / (1 + \lambda |\sigma_{L_1}(t) - \hat{G}_\theta^{predict}(L_2)|)$ 仅作任务内作者感/控制匹配度的示意代理。
- **多层级门控四阶路径与算子短路（`P2-04`）**：
  - 常态意图以 **目标对象化（target objectification）** 招募高层门控、委托底层执行；
  - 习惯与成瘾中的**算子短路**指高固化 `L_2^{habit}` 直接接管动作路径、绕开显式前景中介与替代路径评估；
  - 当冲突持续暴露既有门控本身时，依次开启**门控对象化（gate objectification）→ 门控重构 → 生成能力重构**的反身主动性通道（作为 `Ghost` 算子在生物认知层的候选接口，不将反身门控直接等同于 `Ghost` 的全部职责；神经层只桥接 habituation / gating rigidity / re-entry loss，不把社会制度正当性硬写成神经事实）。

---

## 7. 边界病例、苦难接口与 `Subjecthood Threshold S0–S6` 全称隔离

### 7.1 经典边界与解离病例（实证压力窗）

| 病例 / 状态 | `R4-C4` 结构读法 |
|---|---|
| **盲视（Blindsight）** | 局部视觉—动作通路保持功能控制，但缺乏前景生成中介（Thick `L_1`）与跨能力位置重切 |
| **双稳态知觉（Bistable）** | 多候选在 `L_0^{accessible}` 中竞争，交替获得前景稳定化 |
| **述情障碍（Alexithymia）** | 内部稳态/效价信号与高阶概念化/自我报告通道局部解离（检验生物同源共构的局部可分化性） |
| **裂脑（Split-Brain）** | 胼胝体切断导致拓扑整合与功能绑定分裂，暴露单元边界（Stage 1 Unit-Binding）的构成性地位 |
| **麻醉（Anesthesia）** | 跨麻醉剂破坏大尺度相位稳定、行进波路由与再入确认（`CONSC14`），并非单点关停 |
| **植物状态 / CMD** | 局部网络或 PCI 读数不自动关闭体验窗口；高 `Φ` 低报告状态须警惕隐蔽意识，不以报告缺失判无意识 |
| **冥想 / 迷幻扰动** | 改变自动硬化率、`d` 分配或松动 `L_2` 边界（`NEURAL35`: `reopening ≠ reselectability`） |

### 7.2 与苦难（`Suffering §7`）、热力学签名（`Core_25`）及 AI 三阶审查的接口

- **苦难独立接口（`Core_Law/SRT_Suffering.md §7`）**：苦难要求独立的第一人称/现象/承载登记与声明负担模型；`Stable ISP`、PCI/Φ 或 **Subjecthood Threshold** 梯级均不能单方面关闭受苦资格，意识与苦难的充要关系仍保持 **`OPEN`**。
- **热力学签名接口（`Core_25`）**：清醒/睡眠/麻醉/高负荷下的熵产生、代谢流与非平衡不可逆性可作为状态组织与维护负担的候选物理签名，但**绝不等于现象意识定义或 `HP-B` 闭合**。
- **Subjecthood Threshold `S0–S6` 隔离**：局部点燃、再入、功能绑定、高 `d` 或报告通达最多对应 **Subjecthood Threshold `S1–S3`** 候选维度，**绝不自动推出 `Subjecthood Threshold S4` 主体、`S5` 稳健能动或 `S6` 责任主体**，且与 **AI 赌注谱系 `S0–S4`** 完全正交。

---

## 8. 跨领域对话总结、反向反馈（`FB-C4-5`）与 Hardest Objections

### 8.1 与主流意识理论的精准分界

| 框架 | 扎实解释工作 | `R4-C4` SRT 结构补充（须独立检验） |
|---|---|---|
| **GNWT** | 信息全局通达与跨模块广播 | 前景作为**生成中介**（重切操作位置，而非仅被读取）+ 通达前整体导向 + 通达后 `L_2` 硬化 |
| **IIT & PCI** | 内在因果整合模型量（$\Phi$）与 TMS–EEG 扰动复杂度（PCI，**不默认 PCI 是 $\Phi$ 的直接测量代理**，`P2-03`） | 区分拓扑/功能整合、扰动复杂度与关切加权稳定化、功能绑定 vs 现象绑定 |
| **HOT / RPT** | 高阶表征或局部再入递归 | 区分局部内部状态监测 vs 完整内省 vs 位置重构；保留 `HP-B` 开放 |
| **FEP / Active Inference** | 自维持、精度调节与预期自由能 | 结合不可替代赌注、多层级门控对象化与 `Core_Law/SRT_Suffering.md` 非最小化原则 |

### 8.2 核心理论反向反馈（`FB-C4-5` 摘要，排入 `R4-C5`）

向 `Core/SRT_Core_13a_Operator_Basics.md`、`Philosophy/SRT_Philosophy_Agency_Subjecthood_v0_2.md`、`Philosophy/SRT_HardProblem_Epistemology.md`、`Core_Law/SRT_Selection_Argument.md` 提交候选反馈（`C` / M-origin）：以“前景即生成中介 $\neq$ 广播”、“功能绑定 vs 现象绑定”、“比较动物意识三层解耦”和“目标对象化 → 门控对象化 → 门控重构 → 生成能力重构”四根支柱精炼意识、正面自由与 `Ghost` 门控候选接口（不把反身门控等同于 `Ghost` 全部职责），同时原样保全 `HP-B` 冻结边界。

### 8.3 Hardest Objections

1. **前景生成中介若与 GNWT 全局广播无任何可操作预测分歧**：撤回“生成中介超出广播”的增量主张，退回 GNWT 翻译层。
2. **功能绑定与现象绑定若被证明在任意满足特定整合结构的底物上必然严格同一**：重审 `Def-AI-Con-3b` 分界并提交 `HP-B` 复审（不擅自解冻）。
3. **Thin / Thick `L_1` 若仅反映报告置信度阈值**：仅保留渐进通达描述，撤回锚定厚度本体解读。
4. **高 `d` 无意识加工与弱效价清晰意识（如无情绪视觉细节）**：`d` 调节优先级与沉积厚度，而非每次知觉体验的唯一开关（对齐 `A-22`：强关切不是每项中性知觉质的在线原语）。
5. **最小僵尸压力 `Z*`**：即便完整保留 `Position_t → 前景生成中介 → Position_{t+1}` 重构，逻辑必然性仍未证明；`HP-B` 保持 `OPEN`。
