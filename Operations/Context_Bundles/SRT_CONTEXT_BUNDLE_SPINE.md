---
id: SRT-CONTEXT-BUNDLE-SPINE-2026-11-26
type: context_bundle
status: active
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
generated: 2026-11-26
source_commit: eff704179
source_branch: canon/r4-a-unified-generative-ontology-foundation-2026-11-26
source_dirty: false
inputs_digest: 80ecabcfa202ae95
---

# SRT Canonical 骨架上下文包

> **这是什么**：由 `scripts/build_srt_context_bundles.py` 从 SRT 仓库自动拼装的上下文包。
> 收录承载定义权的 canonical 主干（含跨 owner 生成主轴、One Formation、P0/P1 核心公理、符号表与治理护栏），供大模型确定 SRT 术语、公理与符号含义；Core_22 主方程已分流至独立 `FORMAL` 路线（本包 §0.5 留索引与指针），Core_21c 移至按需桥接层。
>
> **这不是什么**：不是新的 canonical 文件，不是摘要，不是改写。每个来源文件的正文
> 逐字保留；脚本只把 YAML frontmatter 转成显式 provenance 头。**若本包与仓库中的
> 来源文件冲突，以仓库为准**——本包是快照，会随仓库演进而过期。

## §0 生成信息

| 项 | 值 |
|---|---|
| 生成日期 | 2026-11-26 |
| 来源 commit | `eff704179` |
| 来源分支 | `canon/r4-a-unified-generative-ontology-foundation-2026-11-26` |
| 生成时来源工作树有改动 | 否 |
| 包含文件数 | 15 |

> **provenance 契约**：真实性判据是 `inputs_digest`——生成脚本、护栏来源
> （`Governance/SRT_DOWNSTREAM_GUARDRAILS.md`、两份审计）、全部正文文件与 `SPINE §0.5` 索引抽取源（`Core_22` / `Core_21c`）的联合内容摘要。`--check` 重算并比对该摘要，
> 因此改动其中任何一项都会被发现。
>
> `source_commit` 仅供参考，**不作为校验条件**：squash / rebase 合并会重写或丢弃该
> commit，若拿它做祖先校验，合并进 main 之后检查必然失败。内容摘要与合并策略无关。

### 0.1 文件清单与各自最后改动日期

| # | 文件 | 最后 commit |
|---|---|---|
| 1 | `SRT_AI_START.md` | 2026-10-19 |
| 2 | `CANONICAL_REGISTRY.md` | 2026-09-24 |
| 3 | `Core_Law/SRT_Generative_Ontology_Spine.md` | 2026-11-26 |
| 4 | `Governance/SRT_CLAIM_LADDER.md` | 2026-10-19 |
| 5 | `Governance/SRT_CLAIM_MODE_AUDIT.md` | 2026-09-19 |
| 6 | `Core_Law/SRT_L0_Metaphysics.md` | 2026-11-26 |
| 7 | `Core_Law/SRT_One_Formation.md` | 2026-11-26 |
| 8 | `Core/SRT_Core_21_Formal_Axioms.md` | 2026-09-19 |
| 9 | `Core/SRT_Core_21_Minimal_Axioms.md` | 2026-09-23 |
| 10 | `Core/SRT_Core_21b_Constitutive_Theorems.md` | 2026-09-15 |
| 11 | `_SRT_D_VALUE_CANONICAL.md` | 2026-11-26 |
| 12 | `_SRT_PSI_F_CANONICAL.md` | 2026-11-26 |
| 13 | `_SRT_T_DIR_CANONICAL.md` | 2026-11-26 |
| 14 | `_SRT_CROSS_DOMAIN_MATRIX.md` | 2026-11-26 |
| 15 | `_SRT_SYMBOL_TABLE.md` | 2026-11-26 |

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
> | `NODE-D-VALUE` | author_gate | not_applicable | — | RQ-2026-08-A02: whether q is an independent axis or a post-stake-gate depth profile; whether o is operationalized and gets a symbol |
> | `NODE-PSI-F` | active_complete | untested | — | — |
> | `NODE-T-DIR` | active_complete | untested | — | — |
> | `NODE-GHOST-OPERATOR` | partially_active | untested | — | — |
> | `NODE-SUBJECTHOOD` | active_complete | untested | — | — |
> | `NODE-NEURAL-DECODABILITY` | active_complete | observed (bounded) | `Neuroscience/SRT_Neural_Mechanisms_CompactCore.md` | Whether Neuroscience/SRT_Neuroscience_Hardening_N1_N12_v0_2.md is created at all, or NEURAL18/21/22 retarget the compact core |
> | `NODE-LIFE-DISSIPATIVE` | partially_active | untested | `03_Bridges/SRT_Selection_Event_CompactCore.md` | — |
> | `NODE-PHYSICS-MEASUREMENT` | active_complete | observed (bounded) | — | RQ-2026-08-A04: P03/P04/P05 land in a new SRT_Physics_Bridge_v0_2.md or merge into the existing _SRT_Phys_Bridge.md |
> | `NODE-SOCIAL-L2` | partially_active | untested | `Philosophy/SRT_Political_Philosophy_CompactCore.md` | — |
> | `NODE-ENTROPY-REORG` | partially_active | untested | `03_Bridges/SRT_Selection_Event_CompactCore.md` | — |
> | `NODE-BOOK-BACKFLOW` | engineered_not_active | untested | — | — |

#### GENERATED INTERPRETATION — 生成器归纳（**非**来源原文）

清单共 16 个节点。状态分**两个轴**，不可合并读：

- **Axis A（结构）**：10 个达到 `active_complete`——仅表示既有登记增量在当前运行结构中已进入 owner、有检索路径、默认路径读得到，**不表示 `R3` 新裁决已完成 `R4` canonical 回写**。
- **Axis B（行为）**：**3 个**达到 `robustly_observed (bounded)`（满足 `effectively_assimilated`），2 个为 `observed`（尚缺重复有界运行），其余 5 个结构完整的节点是 `untested`：**没有任何证据表明它们真的改变了判断**。

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
> 本包是 **人工选择的高优先级 canonical 骨架（ENG-01 分层瘦身版）**，不是定义权的完备闭包。
> 下面的分类是**生成器的判断**，不是 registry 的原话；每行都附依据供复核。
> 「registry 提及」「Registry §C」两列是机械判定的事实。

### 已收录

**定义源**（10 个）

| 文件 | 分类依据 | registry 提及 | Registry §C |
|---|---|:---:|:---:|
| `Core/SRT_Core_21_Formal_Axioms.md` | registry §A.4 主锚点（公理路由索引） | ✓ | ✓ |
| `Core/SRT_Core_21_Minimal_Axioms.md` | registry §A.4 分层正文 P0 | ✓ | ✓ |
| `Core/SRT_Core_21b_Constitutive_Theorems.md` | registry §A.4 分层正文 P1 | ✓ | ✓ |
| `Core_Law/SRT_Generative_Ontology_Spine.md` | registry §A.0 跨 owner 生成主轴 | ✓ | ✓ |
| `Core_Law/SRT_L0_Metaphysics.md` | registry §C local-owner layer | ✓ | ✓ |
| `Core_Law/SRT_One_Formation.md` | registry §B.13 / §C #4 One / Selection-position 形成层 owner | ✓ | ✓ |
| `_SRT_D_VALUE_CANONICAL.md` | registry §A.1 主锚点 | ✓ | ✓ |
| `_SRT_PSI_F_CANONICAL.md` | registry §A.2 主锚点 | ✓ | ✓ |
| `_SRT_SYMBOL_TABLE.md` | symbol owner；Registry/local routing as applicable | ✓ | — |
| `_SRT_T_DIR_CANONICAL.md` | registry §A.3 主锚点 | ✓ | ✓ |

**治理护栏**（3 个）

| 文件 | 分类依据 | registry 提及 | Registry §C |
|---|---|:---:|:---:|
| `Governance/SRT_CLAIM_LADDER.md` | registry §B.5b；P0–P5 硬度阶梯 | ✓ | ✓ |
| `Governance/SRT_CLAIM_MODE_AUDIT.md` | registry §B.5c；降级台账 | ✓ | ✓ |
| `_SRT_CROSS_DOMAIN_MATRIX.md` | registry §A.4d 自称 governance-canonical usage layer | ✓ | ✓ |

**导航**（2 个）

| 文件 | 分类依据 | registry 提及 | Registry §C |
|---|---|:---:|:---:|
| `CANONICAL_REGISTRY.md` | 权威层级注册表本身 | ✓ | ✓ |
| `SRT_AI_START.md` | AI 最小首读入口，frontmatter 自标 ai_do_not_use_for_definition | — | — |

### 未收录支持文件

**Registry §C priority 点名、文件存在、但本包未收（6 个）**——回答涉及它们时本包不足以单独裁定（已显式分流条目附去向）：

- `Core/SRT_Core_22_Equations.md` — 已拆至独立 `FORMAL` 路线（`Operations/Context_Bundles/SRT_CONTEXT_BUNDLE_FORMAL.md`）；默认 `SPINE` §0.5 保留方程目录索引与检索指针
- `Core/SRT_Core_21c_Bridge_Hypotheses.md` — 已移至按需桥接层（P2/P3/P4，按需直接读仓库原文件）；默认 `SPINE` §0.5 保留 B01–B14 条目标引与检索指针
- `Core/SRT_Core_14_Dynamics_Scaling.md`
- `Core_Law/SRT_Reference_Dynamics.md`
- `AI/SRT_AI_01_Ontology.md`
- `Core/SRT_OPEN_TENSIONS.md`

**⚠ 高严重度：registry 提及但文件不存在（1 个）**——指向已删除、拼错或尚未创建的路径。**这类条目不会被静默过滤掉**，因为它本身就是一种 manifest 差异：

| 失效路径 | 说明 |
|---|---|
| `Core_21_Formal_Axioms.md` | 见 §0.2 G4：这是 `Core/SRT_Core_21_Formal_Axioms.md` 的行文简写，非真实路径 |

**registry 提及、文件存在、但本包未收（84 个）**——多为领域主轴、
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
- `Core/SRT_Core_14_Dynamics_Scaling.md`
- `Core/SRT_Core_14_Dynamics_Scaling_CompactCore.md`
- `Core/SRT_Core_21c_Bridge_Hypotheses.md`
- `Core/SRT_Core_22_Equations.md`
- `Core/SRT_OPEN_TENSIONS.md`
- `Core_Law/SRT_Collective_Selection.md`
- `Core_Law/SRT_Collective_Tower_Hardening_Notes.md`
- `Core_Law/SRT_Constitution_Seven_Theses.md`
- `Core_Law/SRT_Constitution_V1.md`
- `Core_Law/SRT_Individuation.md`
- `Core_Law/SRT_Irreversibility.md`
- `Core_Law/SRT_L1_Formalism.md`
- `Core_Law/SRT_L1_Hardening_Notes.md`
- `Core_Law/SRT_Occlusion_Dynamics.md`
- `Core_Law/SRT_Reference_Axioms.md`
- `Core_Law/SRT_Reference_Dynamics.md`
- `Core_Law/SRT_Reference_Ontology.md`
- `Core_Law/SRT_Suffering.md`
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
- `_SRT_VERTICAL_INTEGRATION.md`

</details>

## §0.5 分层外置路线、方程索引与完备性声明

> **分层完备性声明（`ENG-01`）**：默认 `SPINE` 仅装载承担核心定义权、形成层 owner（`Core_Law/SRT_One_Formation.md`）、`P0/P1` 核心公理、符号表与治理护栏（含 `Governance/SRT_CLAIM_MODE_AUDIT.md` 全文与 `_SRT_CROSS_DOMAIN_MATRIX.md`）的主干文件。以下三类材料**刻意不内置全文于本包**，也不因外置而被废止或降权：
>
> 1. **`FORMAL` 独立方程路线（`Core/SRT_Core_22_Equations.md`）**：主动力学/热力学/桥接方程正文已拆至独立包 `Operations/Context_Bundles/SRT_CONTEXT_BUNDLE_FORMAL.md`；需要完整方程推导时请切换至 `FORMAL` 路线或直接读仓库原文件。局部方程语义仍从属于本包 `SPINE` 对应 canonical owner 与 `Governance/SRT_CLAIM_LADDER.md`。（注：外部单次对话禁止默认整包叠加 `SPINE + FORMAL`，但**不禁止**具备仓库访问能力的工具或研究者围绕具体问题按需联合读取局部方程与对应定义 owner 原文件。）
> 2. **按需桥接层（`Core/SRT_Core_21c_Bridge_Hypotheses.md`）**：`P2/P3/P4` 桥接假说与规范诠释不入默认 `SPINE`，按需直接回读仓库原文件；下游不得将其中任何 `B*` 假说提升为 `P0/P1` 核心定理。
> 3. **动态运行状态与非 canonical 作者裁决（含 `R3` 骨架裁决）**：`STATUS.md`、`01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_*` 与 `Operations/Proposals/SRT_R3_*` 刻意不纳入静态上下文包（避免高 churn 状态更新使全量包频繁过期）；涉及当前 `CURRENT NEXT`、`HOLD`、`OPEN` 进展或最新作者裁决时，必须直接读取仓库 `STATUS.md §Fast Status` 及其控制指针。

### 0.5.1 `Core/SRT_Core_22_Equations.md` 主方程索引（独立 `FORMAL` 路线）

- **原文件**：`Core/SRT_Core_22_Equations.md`（last_commit: `2026-11-26`）
- **独立上下文包**：`Operations/Context_Bundles/SRT_CONTEXT_BUNDLE_FORMAL.md`（单独装载，不叠加在 `SPINE` 上）
- **条目数**：自动抽取 50 条 `Eq-* / Def-*`（已纳入 `inputs_digest` 闭包）

| 编号 | 标题 | 所属章节 | 仓库定位 |
|---|---|---|---|
| `Def-Protocol-1` | Protocol Layer Π (协议层 Π) | 0-B. Protocol and Foundation (协议与基础) | `Core/SRT_Core_22_Equations.md#L52` |
| `Def-Protocol-2` | Absolute-vs-Relative Constraint Split（新增） | 0-B. Protocol and Foundation (协议与基础) | `Core/SRT_Core_22_Equations.md#L62` |
| `Def-Protocol-3` | Methodological Closure Guard（方法论闭包护栏，新增） | 0-B. Protocol and Foundation (协议与基础) | `Core/SRT_Core_22_Equations.md#L71` |
| `Eq-Multi-01` | Collective Free Energy Landscape（集体自由能景观） | 0-C. Multi-Operator Coupled Equations（多算子耦合方程） | `Core/SRT_Core_22_Equations.md#L84` |
| `Eq-Multi-02` | Individual Operator as Landscape Gradient（个体算子为集体景观的梯度表达） | 0-C. Multi-Operator Coupled Equations（多算子耦合方程） | `Core/SRT_Core_22_Equations.md#L90` |
| `Eq-Multi-03` | d_collective as Landscape Effective Dimension（集体 d 容量 proxy 为景观有效维度） | 0-C. Multi-Operator Coupled Equations（多算子耦合方程） | `Core/SRT_Core_22_Equations.md#L95` |
| `Eq-Bridge-IG-01` | Fisher-Induced Local Ψ_f Cost | 0-D. Bridge Equations: Information Geometry / Complexity / Neural Computation | `Core/SRT_Core_22_Equations.md#L111` |
| `Eq-Bridge-IG-02` | Fisher Path Functional | 0-D. Bridge Equations: Information Geometry / Complexity / Neural Computation | `Core/SRT_Core_22_Equations.md#L125` |
| `Eq-Bridge-D-01` | Threshold-Gated Model Instance of `D_stake` (`D_stake^{thresh}`) | 0-D. Bridge Equations: Information Geometry / Complexity / Neural Computation | `Core/SRT_Core_22_Equations.md#L141` |
| `Eq-Bridge-G-01` | Ghost Operator Normalization Proxy | 0-D. Bridge Equations: Information Geometry / Complexity / Neural Computation | `Core/SRT_Core_22_Equations.md#L161` |
| `Eq-Bridge-L2-01` | L2 Path-Trace Writeback | 0-D. Bridge Equations: Information Geometry / Complexity / Neural Computation | `Core/SRT_Core_22_Equations.md#L177` |
| `Eq-Bridge-Loop-01` | Minimal L0-L1-L2 Loop | 0-D. Bridge Equations: Information Geometry / Complexity / Neural Computation | `Core/SRT_Core_22_Equations.md#L193` |
| `Eq-DValue-Max-1` | Maximum Achievable d-Value（d 值可达上限） | 0-D. Bridge Equations: Information Geometry / Complexity / Neural Computation | `Core/SRT_Core_22_Equations.md#L221` |
| `Eq-Rhythm-1` | Budget Overload Implies Non-Zero Temporal Bandwidth（预算超载推出非零时间带宽） | 0-D. Bridge Equations: Information Geometry / Complexity / Neural Computation | `Core/SRT_Core_22_Equations.md#L253` |
| `Eq-Rhythm-4a` | Bandwidth-Duty Tradeoff（频谱丰富度—占空比权衡） | 0-D. Bridge Equations: Information Geometry / Complexity / Neural Computation | `Core/SRT_Core_22_Equations.md#L289` |
| `Eq-DValue-Mobile-1` | Operator Re-alignment Capacity（算子再对齐能力 d_mobile） | 0-D. Bridge Equations: Information Geometry / Complexity / Neural Computation | `Core/SRT_Core_22_Equations.md#L334` |
| `Def-Payable-Chi-1` | Payability Gate for Ψ_f Change（摩擦变化可支付门函数） | 0-D. Bridge Equations: Information Geometry / Complexity / Neural Computation | `Core/SRT_Core_22_Equations.md#L361` |
| `Eq-Evo-01` | Ghost Evolution Equation | I. Evolution Dynamics (演化动力学) | `Core/SRT_Core_22_Equations.md#L390` |
| `Eq-Evo-01b` | Metabolic Gain Modulation | I. Evolution Dynamics (演化动力学) | `Core/SRT_Core_22_Equations.md#L398` |
| `Eq-Evo-02` | Parameter Update (Slow Variable) | I. Evolution Dynamics (演化动力学) | `Core/SRT_Core_22_Equations.md#L405` |
| `Eq-Evo-02b` | Theta Tensor Inertia (θ张量惯性) | I. Evolution Dynamics (演化动力学) | `Core/SRT_Core_22_Equations.md#L425` |
| `Eq-Evo-03` | Coupled Fast–Slow System | I. Evolution Dynamics (演化动力学) | `Core/SRT_Core_22_Equations.md#L432` |
| `Eq-Evo-03b` | Intra-Selection Re-entry (选择内再入通道) | I. Evolution Dynamics (演化动力学) | `Core/SRT_Core_22_Equations.md#L439` |
| `Eq-Evo-03c` | D-Value Forward Criterion (d 值前向判据) | I. Evolution Dynamics (演化动力学) | `Core/SRT_Core_22_Equations.md#L465` |
| `Eq-Force-01` | Conditional Reference-Trajectory Friction Proxy | II. Thermodynamics of Agency (能动性热力学) | `Core/SRT_Core_22_Equations.md#L512` |
| `Eq-Pain-01` | Hazard / Pain-Risk Proxy | II. Thermodynamics of Agency (能动性热力学) | `Core/SRT_Core_22_Equations.md#L524` |
| `Eq-Friction-Comp` | 计算摩擦桥接候选 (Computational Friction Bridge Candidate) | II. Thermodynamics of Agency (能动性热力学) | `Core/SRT_Core_22_Equations.md#L529` |
| `Eq-Select-Thermo` | 选择热力学宪法不等式 (Constitutional Inequality of Selection Thermodynamics) | II. Thermodynamics of Agency (能动性热力学) | `Core/SRT_Core_22_Equations.md#L543` |
| `Eq-AI-LowRoad-01` | Selection Cost Minimization Form（低阶主动推断映射，新增） | II. Thermodynamics of Agency (能动性热力学) | `Core/SRT_Core_22_Equations.md#L557` |
| `Eq-AI-LowRoad-02` | Expected Selection Cost（对应 EFE，新增） | II. Thermodynamics of Agency (能动性热力学) | `Core/SRT_Core_22_Equations.md#L567` |
| `Eq-Stab-01` | Fixed Point Condition | III. Stability & Phase Transition (稳定性与相变) | `Core/SRT_Core_22_Equations.md#L587` |
| `Eq-Phase-01` | Ontological Phase Transition | III. Stability & Phase Transition (稳定性与相变) | `Core/SRT_Core_22_Equations.md#L592` |
| `Eq-Sleep-01` | L2 Optimization | IV. Sleep & Maintenance (睡眠与维护) | `Core/SRT_Core_22_Equations.md#L599` |
| `Def-LDP-1` | Empirical Measure (经验测度) | V. Statistical Mechanics of Selection (选择的统计力学) | `Core/SRT_Core_22_Equations.md#L606` |
| `Eq-LDP-01` | Hydrodynamic Limit (水动力极限) | V. Statistical Mechanics of Selection (选择的统计力学) | `Core/SRT_Core_22_Equations.md#L610` |
| `Eq-LDP-02` | SRT Action Functional (SRT 作用量泛函) | V. Statistical Mechanics of Selection (选择的统计力学) | `Core/SRT_Core_22_Equations.md#L616` |
| `Eq-Phantom-01` | Phantom Operator Effect (幽灵算子残响) | VI. Social-Ontological Dynamics (社会本体论动力学) | `Core/SRT_Core_22_Equations.md#L626` |
| `Eq-Phantom-01b` | Collective Phantom Resonance (集体幻肢共振) | VI. Social-Ontological Dynamics (社会本体论动力学) | `Core/SRT_Core_22_Equations.md#L632` |
| `Eq-Phantom-02` | Homeostatic Rebuild Time Constant (稳态重建时间常数) | VI. Social-Ontological Dynamics (社会本体论动力学) | `Core/SRT_Core_22_Equations.md#L637` |
| `Eq-Frame-01` | Frame-First Normalization | §X. Selection Thermodynamics: From Philosophy to Physics (选择热力学：从哲学到物理学) | `Core/SRT_Core_22_Equations.md#L695` |
| `Eq-Frame-02` | Observable Reparameterization | §X. Selection Thermodynamics: From Philosophy to Physics (选择热力学：从哲学到物理学) | `Core/SRT_Core_22_Equations.md#L702` |
| `Eq-Res-01` | Delay-Constrained Resonance Selection | 参数注册表（Parameter Registry, v2） | `Core/SRT_Core_22_Equations.md#L737` |
| `Eq-Res-02` | Cross-Scale Coordination Energy | 参数注册表（Parameter Registry, v2） | `Core/SRT_Core_22_Equations.md#L743` |
| `Eq-Topo-01` | Simplicial Assembly–Collapse Dynamics | VII. Topological Selection Dynamics（拓扑选择动力学，新增） | `Core/SRT_Core_22_Equations.md#L752` |
| `Eq-Topo-02` | Dual-Layer Selection over Deterministic Envelope | VII. Topological Selection Dynamics（拓扑选择动力学，新增） | `Core/SRT_Core_22_Equations.md#L764` |
| `Eq-Topo-03` | Persistence-Weighted Order Parameter | VII. Topological Selection Dynamics（拓扑选择动力学，新增） | `Core/SRT_Core_22_Equations.md#L775` |
| `Eq-CogE-01` | Baseline–Active Friction Decomposition | VIII. Cognitive Energy Partition Interface（Quanta 95/5 接口，2026-03-07） | `Core/SRT_Core_22_Equations.md#L854` |
| `Eq-CogE-02` | 95/5 Selection Ratio (Embodied Constraint) | VIII. Cognitive Energy Partition Interface（Quanta 95/5 接口，2026-03-07） | `Core/SRT_Core_22_Equations.md#L865` |
| `Eq-CogE-03` | Subjective Effort as Friction Gradient | VIII. Cognitive Energy Partition Interface（Quanta 95/5 接口，2026-03-07） | `Core/SRT_Core_22_Equations.md#L874` |
| `Eq-CogE-04` | AI–Human Energetic Asymmetry Index | VIII. Cognitive Energy Partition Interface（Quanta 95/5 接口，2026-03-07） | `Core/SRT_Core_22_Equations.md#L881` |

### 0.5.2 `Core/SRT_Core_21c_Bridge_Hypotheses.md` 按需桥接假说索引

- **原文件**：`Core/SRT_Core_21c_Bridge_Hypotheses.md`（last_commit: `2026-09-11`；按需直接读仓库，不入默认 `SPINE`）
- **条目数**：自动抽取 14 条 `P2/P3/P4-B*`（已纳入 `inputs_digest` 闭包）

| 编号 | 标题 | 仓库定位 |
|---|---|---|
| `P2/P3-B01` | Information-Existence Equivalence | `Core/SRT_Core_21c_Bridge_Hypotheses.md#L50` |
| `P3/P4-B02` | Fitness Beats Truth | `Core/SRT_Core_21c_Bridge_Hypotheses.md#L66` |
| `P4-B03` | Assembly Criterion | `Core/SRT_Core_21c_Bridge_Hypotheses.md#L84` |
| `P3/P4-B04` | Holographic Duality | `Core/SRT_Core_21c_Bridge_Hypotheses.md#L106` |
| `P2/P3-B05` | Topological Normativity | `Core/SRT_Core_21c_Bridge_Hypotheses.md#L124` |
| `P3-B06` | Scale Consistency | `Core/SRT_Core_21c_Bridge_Hypotheses.md#L140` |
| `P3-B07` | Ghost Operator Universality | `Core/SRT_Core_21c_Bridge_Hypotheses.md#L156` |
| `P2/P3-B08` | `\Psi_f` as Generative Principle | `Core/SRT_Core_21c_Bridge_Hypotheses.md#L196` |
| `P2/P3-B09` | Strong Selection-Information Creation Equivalence | `Core/SRT_Core_21c_Bridge_Hypotheses.md#L223` |
| `P3/P4-B10` | Deep Time / Assembly Mass | `Core/SRT_Core_21c_Bridge_Hypotheses.md#L252` |
| `P3-B11` | `D_eff` as d-Value Capacity Proxy | `Core/SRT_Core_21c_Bridge_Hypotheses.md#L268` |
| `P2/P3-B12` | Information-Geometry / Complexity / Neural-Computational Hardening | `Core/SRT_Core_21c_Bridge_Hypotheses.md#L291` |
| `P2/P3-B13` | ST-A Structural Stabilisation and Generative Reselectability | `Core/SRT_Core_21c_Bridge_Hypotheses.md#L320` |
| `P2/P3-B14` | EX-A Anchoring-Persistence Readout | `Core/SRT_Core_21c_Bridge_Hypotheses.md#L354` |

### 0.5.3 动态运行状态、未闭合张力与当前作者裁决检索指针

| 检索目标 | 仓库权威入口（实时读取，不入静态包） | 说明 |
|---|---|---|
| 当前执行焦点 / `CURRENT NEXT` / `HOLD` | `STATUS.md`（`§Fast Status`） | 唯一当前状态与最新作者裁决路由入口 |
| 作者直觉裁决与 `R3` 骨架裁决溯源 | `01_Source_Intuition/`（由 `STATUS.md §Fast Status` 指向具体 `SRT_AUTHOR_ADJUDICATION_*` / `SRT_AUTHOR_DECISION_*`） | 非 canonical 作者源与决策边界 |
| `R3` 阶段性收敛主稿与全局减法地图 | `Operations/Proposals/`（由 `STATUS.md §Fast Status` 指向具体 `SRT_R3_*` 主稿） | 非 canonical 理论骨架收敛提案 |
| 未封口核心张力登记 | `Core/SRT_OPEN_TENSIONS.md` | 按条件检索；其中条目不得陈述为已封口 |

---



---

## FILE: `SRT_AI_START.md`

| 字段 | 值 |
|---|---|
| path | `SRT_AI_START.md` |
| id | SRT-AI-START |
| claim_mode | index |
| status | active |
| epistemic_layer | os |
| layer | meta |
| canonical(字段) | - |
| last_commit | 2026-10-19 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：[SRT-CANONICAL-REGISTRY, SRT-CLAIM-LADDER, SRT-AGENT-RETRIEVAL-PROFILE, SRT-STATUS]

<!-- 以下为原文逐字保留 -->

# SRT AI Start

> **Runtime / bootstrap entry only.** This file is not the final source of SRT definitions and must not silently replace canonical files.
> `AGENTS.md §Session Start` is the single authority for fresh-session read order.

## 1. Current one-sentence orientation

**SRT is currently in an author-led ontology re-entry phase. Constitution v1 remains the active natural-language reader-interface prototype, but it does not exhaust SRT ontology; bearer/position is one important structural problem among a wider open field involving multiplicity/unity, Selection/determination, manifestation/One-formation, persistence, history/write-back, relation/constraint, future selectability, order/convergence and objectification. Research starts from SRT questions, absorbs source-native theories into candidate relational organizations, and develops new questions and conclusions under author direction and critical checks. Named-neighbor increment pressure is conditional on the actual comparative claim; new deep wells retain their separate HOLD gates.**

This is a programme orientation, not a new canonical definition or a replacement final ontology label.

Current status and author decisions are resolved through `STATUS.md §Fast Status` controlling pointers. `AGENTS.md §Session Start` owns conditional reads; do not start a second bootstrap from this page. Historical programme documents are interpreted under the 2026-09-05 governance amendment and subsequent scoped author adjudications.

## 1.1 Selection term-of-art hard guard — 2026-09-22

**Do not read SRT `Selection` with the ordinary default meaning of choosing among pre-given alternatives.** This is a machine/bootstrap guard; exact definition authority remains with `Core_Law/SRT_L0_Metaphysics.md`, `Core/SRT_Core_21_Minimal_Axioms.md`, and `Core_Law/SRT_Generative_Ontology_Spine.md`.

Current author-confirmed semantic boundary:

~~~text
Selection
!= conscious choice
!= decision among a pre-given menu
!= Darwinian winner-picking by default
!= bare filtering
!= arbitrary descriptive / modelled change.
~~~

SRT Selection is a term of art for **genuine actualised non-neutral differentiation**. A completed alternative set is not required in advance; alternatives, positions, relations and reachable possibilities may themselves be generated through Selection. Selection occurrence does **not** require later sediment, retained historical efficacy or generative inheritance; terminal Selection remains genuine.

Fresh-session rule:

> When the word `Selection` appears in SRT / GRG work, never silently substitute the conventional option-choice meaning. If exact scope matters, read the canonical owners and the later same-day correction: `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GRG_GENERATIVE_CAPACITY_INTERVENTION_GRAMMAR_2026-09-22.md`.

Current guard: `Selection occurrence != retained historical efficacy != sedimentation != generative inheritance`. Terminal Selection remains genuine. The OPEN problem is narrower: what distinguishes genuine actualised Selection from merely descriptive / modelled change? Do not answer that by smuggling retained consequence back into the occurrence definition.

## 2. Current identity guard

Do not restart SRT as a project whose highest burden is to derive every domain from a formal P0 theorem ladder.

Also do not reduce the current reconstruction to a bearer ontology.

Current working separation:

```text
Author-led ontology reconstruction
= recover and pressure open SRT ontological questions;
  AI does not fill in the final answer from historical files

Constitution v1
= perspective / reader-entry operation / boundary / problem-opening interface
  != exhaustive ontology inventory

Open ontology problem field
= may include multiplicity / unity / Selection / manifestation / persistence /
  history-writeback / relation-constraint / bearer-position / future selectability /
  order-convergence / objectification
  without fixing their final relations or forcing a ladder

Domain Reconstruction Framework
= author/ontology status × domain starting picture × mature-neighbor adaptation
  × common-problem extraction × Constitution interface × inherited SRT assets × materials
  -> provisional problem families / candidate response / eventual deep-well queue

Domain Theory / Hypothesis / Model
= mechanisms / formalizations / proxies / candidate explanations

Deep Well / Evidence
= later bounded question / strongest baseline / experiment / data / archive / proof /
  rival comparison after a bounded author-owned SRT response exists
```

The Domain Reconstruction Framework is **not** a Domain Constitution and not a domain axiom system. Its job is to organize a domain problem-space, neighbor pressure and candidate SRT response before one specific experiment, dataset or favorite theory carries the whole burden.

### Constitution non-formalization

Constitution does not use equations, scalar thresholds or fully specified state spaces as constitutional authority.

Reason: formalization is itself an objectification/public-convergence practice that stabilizes unit, boundary, grain, equivalence and normalization so a representation can travel. This makes formalization a legitimate subject of reflection as well as a legitimate domain tool.

This is **not** a claim that mathematics cannot express indexical/contextual relations.

### Bearer scope guard

```text
bearer-as-position
!=
bearer-as-modeled-variable
```

Adding `observer`, `agent i`, `theta` or another variable does not by itself reproduce a participation/bearing relation when that relation is load-bearing.

But equally:

```text
bearer / position / participation
!=
whole SRT ontology
```

Bearer may become relevant only after or alongside other questions about formation, persistence, history, relation and future selectability. Do not force every domain problem into bearer language.

### Reflexivity guard

The Constitution and ontology reconstruction have no God-view exemption. They are proposed from positions and are evaluated through cross-position re-enactability, neighbor pressure, internal coherence and domain-side productive adequacy.

```text
position-indexed access
!= general epistemic privilege
!= infallibility
```

### Ontology / methodology guard

Do not conflate:

```text
A. bearer-/position-indexed relations may be ontologically constitutive in some phenomena
B. research should preserve participatory/bearer information in those cases
```

If B is claimed, state the preservation reason: a method should not delete a possibly constitutive relation before testing whether it matters.

Neither A nor B defines the whole SRT ontology.

## 3. Constitution / ontology dialogue guard

Use `AGENTS.md §Constitution / Ontology Dialogue Hard Guard` and the governance amendment §4.2 for author convergence, U/N-mode, neighbor adaptation and HOLD gates. These protect substantive decisions; they do not require repeated approval for authorized mechanical work.

**Generative-first collaboration (2026-10-18):** See `AGENTS.md §Generative research collaboration` and the controlling governance amendment §4.2; **AI** retrieves task-relevant SRT concepts and mature neighboring theories, proposes `C` (M-origin) alternatives without silently changing `K`, and follows the 10-07 three-item comparison format only at its phase-appropriate scope. HOLD and `CURRENT NEXT` still govern formal execution, not provisional thinking.

## 4. Source recovery before invention

For ontology / Constitution work, recover existing value before greenfield writing:

- active 26Q book source intuition;
- `SRT_Constitution_One_Page_CN.md` / Seven Theses as historical/interface inputs;
- Chinese Core Text / Euclid;
- L0 prose;
- Individuation / Hard Problem / Collective distinctions;
- SourceCards, readings and patches;
- 2026-08 source-mining, bearer, sigma and subtraction audits;
- the 2026-09-05 author-reentry correction.

Use `Operations/Proposals/SRT_CONSTITUTION_SOURCE_RECOVERY_MAP_2026-08-29.md`.

Current open ontology prompts may include, without being promoted to definitions:

```text
多如何形成一？
为什么这个而不是别的成为确定 / 显现？
Selection 的 recurrent self-conditioning 在什么条件下构成 One-formation？
一个已形成的 One 如何持续、留下并改变后来结构？
历史 write-back 如何改变后来可处理 / 可选择的方向？
何时 history / consequence 成为 own-history / bearer 问题？
关系、约束与更高阶秩序如何进入？
objectification 如何把这些过程变成可共享对象，又可能丢失什么？
```

Do not fill these answers by repository interpolation alone.

## 5. Domain reconstruction and deep-well guard

Do not jump directly from Constitution v1 to a specific domain dataset, experiment, proof programme or favored external theory when the domain and the relevant SRT ontology question are not mature enough.

For a newly selected or substantially revised domain, use:

```text
author / ontology status
-> domain starting picture
-> relevant SRT open-question selection
-> mature-neighbor adaptation
-> common-problem extraction
-> Constitution/interface translation
-> objectification and bearer/position diagnostics where relevant
-> inherited SRT assets + Material Re-entry
-> author review of any candidate SRT response
-> only then choose one deep well
-> deep-well charter
-> evidence / strongest baseline / Case A-B-C when an increment claim actually exists
-> productive-adequacy review
-> framework writeback
```

A Domain Reconstruction Framework should answer, before a new deep well:

```text
Which parts are explicit current author intuition, recovered historical SRT, AI synthesis, or unresolved pressure?
What does the field treat as Given Ones?
Which open SRT ontology questions are genuinely relevant here?
What do the strongest neighboring theories already explain in their own terms?
What recurring/common problem remains after fair adaptation?
What do Constitution v1 operations help reopen here?
What objectification choices matter?
Is bearer/position actually load-bearing here, and if so in what limited role?
Where do inherited SRT files and materials belong?
Is there an author-owned candidate SRT response yet?
Only if yes: which bounded question is worth a deep well next?
```

The framework does not by itself establish a causal mechanism, empirical prediction, privileged formalism or SRT superiority claim.

Before an SRT-sensitive domain formalization, a Bearer–Objectification Declaration may still be useful when those dimensions are load-bearing:

```text
unit
boundary
grain
equivalence
normalization
history loss
position loss
bearer substitution
consequence attribution
participation
```

This is a diagnostic method candidate, not a complete ontology checklist or universal standard.

### Pilot / grandfather guard

The Neuroscience and Epistemology wells opened during the earlier sequence remain valid pilot records. Do not erase their adverse, translation-only, high-Case-B-pressure or access-blocked results.

But do not generalize them into a whole-SRT ontology verdict. The first well primarily calibrated a history/relation/objectification/bearer slice; the second currently remains partly an evidence-infrastructure / inherited-method pilot.

Bounded archive/evidence work may continue. A third main well is on hold until explicit author release after ontology re-entry.

## 6. Current formal/canonical sources remain historically authoritative until audited

The 2026-08-29 programme reconstruction and 2026-09-05 sequencing correction are prospective. They do not silently rewrite frozen owners.

When exact **current registered** meanings are required, do **not** maintain or infer a second complete authority chain from this bootstrap file. Follow `CANONICAL_REGISTRY.md §C` as the single complete citation-priority owner.

For current cross-owner ontology generation order, non-identities, and OPEN routing, consult `Core_Law/SRT_Generative_Ontology_Spine.md` after the Registry and before compatible local owners. Local owners retain their detailed definitions only where compatible with that routing.

This runtime entry is a projection of the Registry, not an independent authority list. A later Core/Core_Law role-reclassification audit may still retype local owners without changing this single-source rule.

## 7. Symbol quick guard

| Symbol / term | Fast guard | Current definition authority |
|---|---|---|
| `L_0` | model-facing notation for Selection's open / non-preclosed analytic aspect; not a pregiven completed possibility inventory, independent prior field, or automatically measurable state space | Registry -> Generative Ontology Spine -> L0 / symbol owners |
| `L_1` | current manifest selected actuality in existing formal architecture; occurrence != persistence | Core/symbol owners |
| `L_2` | convergence-history / stable constraint domain in existing architecture | symbol/open-tension owners |
| `G_hat_theta` | formed / formal / model-level role-carrier for a declared Selection realization, not primitive Selection or a prior chooser entity | Registry -> Generative Ontology Spine -> symbol table / compatible local owners |
| `d` | stake-coupled concern / irreversible-risk sensitivity in current canonical system; proxies are conditional | `_SRT_D_VALUE_CANONICAL.md` |
| `D_eff` | capacity/geometric proxy candidate, not canonical `d` | d owner / 21C |
| `Psi_f` | payability/friction construct in current canonical system; projections are conditional | `_SRT_PSI_F_CANONICAL.md` |
| `T_dir` | operational direction-readability proxy, not reward/confidence/valence | `_SRT_T_DIR_CANONICAL.md` |
| `sigma_sr` | model-local/conventional individuation-related proxy under current owner reading; do not use it to bootstrap bearer identity | Individuation / current sigma decision records |

### Proxy rule

If a statement says `proxy X = SRT variable Y`, rewrite unless the current owner explicitly licenses identity.

Safer:

- candidate proxy under declared conditions;
- one projection, not the thing itself;
- domain bridge/lab readout, not constitutional definition.

## 8. Pre-objectification / world-formation guard

Existing SRT contains a valuable methodological insight: a complete formal object space cannot be silently used to explain how objects become available as objects.

But the current author correction requires two distinct questions to remain open:

```text
world-side formation / manifestation / persistence
!=
epistemic-public objectification / representation
```

When the target is world-side formation, do not let an objectification critique substitute for the ontology question.

When the target is public knowledge construction, objectification may be central.

Domain science may legitimately start from a declared object when its research question is already downstream of object formation.

## 9. Sigma worked-example guard

Use `Operations/Audits/SRT_SIGMA_PREMATURE_DEINDEXING_WORKED_EXAMPLE_2026-08-29.md` as a repository-local warning:

- coordinate sensitivity;
- trace-attribution ambiguity;
- provenance/control dissociation;
- boundary-relative semantics.

Allowed lesson: under-declared index/objectification choices can make a supposedly natural scalar unstable or semantically overloaded.

Forbidden lessons:

- mathematics cannot model indexicality;
- every SRT problem is fundamentally a bearer problem;
- sigma pressure establishes the new ontology.

## 10. Existing important theory boundaries still apply

Until separately changed:

- primitive actualisation != persistence;
- occurrence != stable ISP;
- object != bearer != subject-position != phenomenality;
- `B_s != B_p`, `B_s -> B_p ?` remains open;
- Selection != Agency;
- One-formation is a stronger recurrent self-conditioning organization of Selection, not a second ontic substance; its exact necessary-and-sufficient formation theorem remains open;
- `Selection = Order ?` remains open;
- stabilization does not automatically establish bearerhood;
- historical facticity / write-back does not automatically establish own-history;
- sigma cannot bootstrap the bearer domain it presupposes;
- d/`Psi_f`/`T_dir` proxies must not be silently identified with their measured surrogates;
- published/submitted manuscripts are protected by the reconstruction carve-out.

Use `Core/SRT_OPEN_TENSIONS.md` when an existing concept is known to remain open.

## 11. Materials and external theory

Pipeline 1 continues and remains the source-intake / source-fidelity / material-status owner.

External theories/sources may function as:

```text
source-native evidence
resonance
contrast
pressure
translation
realization
mechanism example
domain constraint
```

They do not prove Constitution or ontology.

### Mature-neighbor adaptation

During the 2026-09-05 correction phase, external theory work must do more than collect nearby citations.

For each strong neighbor, ask:

```text
What does it claim in its own vocabulary?
What problem does it already solve?
How can its established explanation contribute to the SRT root question?
What relation is reorganized, and what question or conclusion follows?
What SRT wording does it pressure, and what must remain domain-specific?
Is the gain supported rather than merely relabeling?
If a beyond-neighbor claim is made, what exact residual/comparative burden does it carry?
```

A neighbor is allowed to force SRT revision.

### Domain Material Re-entry

Once a domain is selected for reconstruction, already processed material must not remain stranded as passive SourceCards / PatchNotes / Hooks.

Before a mature framework/deep-well decision, recover and route relevant:

```text
01_Source_Intuition / book material
inherited domain owners / claim-status / compact-core
Materials/YYYY SourceCards
domain PatchNotes
IntegrationHooks / landing ledgers
Material Log / monthly logs
domain Context Bundle
Experiments / evidence packets
relevant audits / OPEN_TENSIONS
manuscript-local assets where historically relevant
```

At minimum, all domain-relevant active `high` / `very_high` SourceCards, active PatchNotes / Hooks, obvious inherited owners and directly relevant experiment/evidence assets need an explicit disposition.

Preserve Pipeline 1's three-layer discipline:

```text
A — source-derived claim
B — SRT-side domain synthesis
C — discriminating SRT claim, if any
```

The Domain Reconstruction Framework may be rich in B while C remains absent. C requires an author-owned SRT response plus later deep-well/rival evidence.

## 12. Domain increment / subtraction

Subtraction, bounded probes and rival comparison are not discarded.

Their primary location is now later in the sequence:

```text
Ontology formation: SRT-led absorption / problem generation / justified conclusions / critical checks; no novelty permission gate
Constitution: interface red-team / anti-overclaim
Domain Framework: owner-routing / mature-neighbor adaptation / common-problem extraction
Deep Well: gate on a concrete claim that SRT adds something
Repository: owner/status consistency
```

Apply amendment §4.2: task-requested novelty comparison or an actual uniqueness, irreducibility, superiority or additional predictive/intervention claim triggers the scoped audit. Do not force Case A/B/C unless:

```text
bounded SRT response exists
+ author explicitly owns/adjudicates it
+ strongest neighbors have been fairly mapped
+ common residual problem is stated independently of SRT vocabulary
+ a domain-native discriminator is possible
```

Otherwise the correct state is `theory formation / mapping still open`, not an automatic Case B.

A domain is still allowed to conclude `SRT adds no increment here` once those prerequisites are paid.

## 13. AI-specific guard

AI is one domain/pressure-test site, not the theory's definition engine.

Do not infer subjecthood, stake or consciousness from performance alone. Do not use AI models as the constitutional prototype of bearer unless the author explicitly converges on such a claim after the current workflow.

For identity-level work, separate machine roles when useful: source auditor, internal red-team, strong-neighbor advocate, counterexample generator, relabeling detector, hidden-commitment extractor, cross-domain semantic-invariance checker, author-intent drift checker, and only later increment auditor.

## 14. Minimal answer protocol

For substantive SRT answers:

1. Use the selected retrieval profile and current STATUS controlling sources. Architecture v2 is conditional on domain framework work, not every technical task.
2. Resolve definitions through Registry §C and compatible owners; distinguish author intuition, candidate reconstruction, canonical claim, bridge/model, evidence and governance.
3. Check the relevant owner boundaries and OPEN tensions before claiming closure. Use source-native evidence and allow counterexamples to change the answer.
4. For ontology/Constitution work, preserve author convergence and U/N-mode. An asserted comparative gain requires its bounded claim and comparator; ordinary O-track work has no novelty permission gate.
5. Apply domain/deep-well gates only when that programme is in scope. Pilot results do not establish whole-SRT identity.
6. Complete the requested answer or edit, report relevant evidence and remaining gaps, and avoid re-asking settled decisions.

---

## 15. Claim-Level Guard

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



---

## FILE: `CANONICAL_REGISTRY.md`

| 字段 | 值 |
|---|---|
| path | `CANONICAL_REGISTRY.md` |
| id | SRT-CANONICAL-REGISTRY |
| claim_mode | canonical |
| status | active |
| epistemic_layer | os |
| layer | meta |
| canonical(字段) | - |
| last_commit | 2026-09-24 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：[SRT-INDEX, SRT-GENERATIVE-ONTOLOGY-SPINE, SRT-CLAIM-LADDER, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-T-DIR-CANONICAL, SRT-CROSS-DOMAIN-MATRIX, SRT-CORE-22]

<!-- 以下为原文逐字保留 -->

# SRT Canonical Registry

本页用于固定 SRT 当前应优先引用的 **canonical 主干层**。
原则：
- canonical 文件优先短、稳、少歧义
- 长文负责展开、推导、接口批次与历史沉积
- split 文件负责导航，不替代 canonical 定义
- 本页是 router：它压缩并指向当前 owner，不以注册或摘要创建第二份定义 authority

## 0. 定位说明（Epistemic Note）

- `canonical` 在本仓库内表示“当前内部优先引用的稳定锚点”，**不自动等于**“外部已证实的自然定律”。
- `governance-canonical` 表示为防止全仓漂移而采用的稳定用法规则；它可以是当前主读、默认符号口径或工作代理，不自动声称已完成本体推导。
- `theory-canonical` 表示由 core 结构推出或在 core 中具有更强优先权的定义 / 命题；只有明确回链 P0/P1/P2 来源时才按此读。
- `operational proxy` 表示为了测量、比较或建模而采用的工作性读数；它可以近似 canonical 对象，但不得反向改写 canonical 对象。
- `bridge hypothesis` 表示跨域映射或解释性接口；它可以承载候选结构，但不得被下游引用成 core theorem。
- 旧文件名、旧 theorem/axiom 标签或 glossary 历史条目若仍保留，均按当前 claim ladder、claim-mode audit 与本注册表的本地说明判读；历史命名不恢复更高等级。
- 自 `2026-03-17` 起，SRT 默认按 `OS / Bridge / Lab` 三层理解；详见 `Governance/SRT_POSITIONING.md`。
- 自 `2026-04-20` 起，SRT 额外按命题级硬度 `P0-P5` 管理；详见 `Governance/SRT_CLAIM_LADDER.md`。
- 本注册表中的大多数条目默认属于 **OS** 或 **Bridge**，用于收口词汇、语法与高阶接口；真正的硬赌点应优先沉淀到实验与假说文件，而不是混在 canonical 锚点里。

## A. 核心定义层（Definitions）

### 0. Generative Ontology Spine — 跨 owner 生成主轴
- 主锚点：`Core_Law/SRT_Generative_Ontology_Spine.md`
- id：`SRT-GENERATIVE-ONTOLOGY-SPINE`
- layer：L0-L2 / epistemic：os / status：active / version：v4 / claim-mode：canonical
- 角色：固定当前 SRT 的**跨层生成顺序、非同一性与 OPEN gate**，作为旧 canonical 清洗和后续本体研究的第一路由；它不替代各局部 owner 的详细定义。
- 当前 routing compression：`primitive Selection = reality's one generative mode -> determinate actuality / manifestation -> retained historical efficacy where established -> recurrent self-conditioning / One formation -> formed Selection-position -> stronger recurrent standing / Stable ISP -> prospective self-exposure / Bearer under P+E -> reflexive condition-rewriting / Agency -> separately typed normativity routes`。这是路由压缩，不是对 Spine 或各局部 owner 的替代定义。
- Selection 术语硬护栏（2026-09-22/23）：`Selection` 是 SRT 自定义原语，不按 ordinary pre-given-option choice 读取；canonical owners 要求 genuine actualised non-neutral differentiation，且 prior option set 不作为前提。Selection occurrence 不要求 retained historical efficacy / sedimentation / generative inheritance；terminal Selection remains genuine。仍 OPEN 的是 genuine actualised Selection 与 merely descriptive / modelled change 的精确 anti-tautology 分界。精确定义回到 L0 / P0 / Spine。
- 分层护栏：primitive Selection 在规范上无内容；existence 是 Selection under determinate actuality；history 只在 prior Selection 的效力被保留并建立时进入路由。`L_0 / L_1 / L_2` 是 analytic / model-facing aspects，不是三种 ontic substances；primitive Selection 不等于 formed `\hat{G}`。Normativity routes 需分别定型，O2-M 保持 OPEN。
- 当前 Bearer gate：已形成的 `One / Selection-position + P prospective self-indexing + E same-One prospective exposure -> Bearer`，按 semantic / architectural canonical 读取；不是跨所有实现域的形式化或实证 N&S theorem。
- typed layering：One-level endogenous perspective、A1/A2/P/E 分层须保留；`all Ones automatically perspective-bearing` 仍未建立。历史 `A3` 仅作为 R1 gate lineage 标签，不作为当前 canonical token。
- supersession：旧文件若在**跨层推论**上与本 spine 冲突，旧推论转为 cleanup / retyping target；局部数学或语义内容在不冲突范围内继续有效。
- 硬边界：history/writeback 不作为 verticality 的本体来源；Stable ISP 不作为 One 的形成源；`sigma_sr` / d / T_dir / Psi_f 不得反向生成 One / Bearer / subject；Bearer 不按定义等同于承担 / concern / subject / experiencer。
- OPEN：精确 L0 primitive decomposition、One-level perspective 普遍充分性、Bearer↔承担、Bearer→concern/d、agency、positive subject gate、cognition、phenomenality、collective subject sufficiency、new Level、Level 2 均未由本文件自动关闭。
- 引用规则：涉及当前**生成顺序、跨 owner 层级关系、旧 canonical 是否越权**时先回链本文件；随后再进入 L0、One Formation、P1-T06、d / Psi_f / T_dir 等局部 owner。
- 待落地重构方向（2026-09-24，noncanonical）：`01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_SPINE_MINIMAL_KERNEL_L0L1L2_REFLEXIVE_FACETS_2026-09-24.md` 与 `Operations/Audits/SRT_GENERATIVE_ONTOLOGY_SPINE_SEMANTIC_THINNING_AUDIT_2026-09-24.md`（两角色 Spine、L0/L1/L2 标签、未来 C 类落地合同）。C1/C2 尚未授权；在其落地前，本条目只承担当前路由记录，现行 Spine 与其兼容的 local owners 继续承担现行定义与语义 authority。

### 1. d-value
- 主锚点：`_SRT_D_VALUE_CANONICAL.md`
- 说明：统一 d-value 的 governance-canonical 默认用法、域内投影、误用边界；bare `d` 默认采用标量摘要形式，向量 / 门读须显式标注；`D_eff`、Fisher 读数、d-vector 与 d-gate 均为 proxy / judgment tool，不能反向替代 `Def-d-canonical`
- 引用规则：首次出现 d-value 时优先回链本文件

### 2. Ψ_f（本体论摩擦）
- 主锚点：`_SRT_PSI_F_CANONICAL.md`
- 说明：统一 `Ψ_f` 的 v1 governance-canonical 信息论代价 / 可支付性主读、几何 / 代谢投影、可支付性条件与物理弱相容边界；几何与代谢表达是有条件 projection，不是最终唯一推导
- 引用规则：首次出现 `Ψ_f`、本体论摩擦、可支付性条件或“引力是否只是类比”时优先回链本文件

### 3. T_dir（方向透明度）与价值遮蔽
- 主锚点：`_SRT_T_DIR_CANONICAL.md`
- 说明（Part I §1-§10）：`T_dir` 是 formed system / relation / model 相对于 independently typed、declared direction signal 的 self-readability / reorientation v0 operational proxy；它尚不是 theory-canonical 形式基础。无 declared direction 时，该 claim 中的 `T_dir` 不准入／未定义；`T_dir > 0` 不建立 good、legitimacy、generative health 或 O2-M。
- 说明（Part II §11-§16）：扩展至价值动力学底层机制——L₂ 磁带/DNA 类比（§11）、三层价值结构（§12）、价值归纳 vs 理性归纳（§13）、时空对称性感知机制（§14）、价值作为暂时吸引子而非守恒结构（§15）、吸引子上升/退化动力学（§16）；这些段落按 bridge / theory-clarifying 读，不因文件名而升级为 core theorem
- 引用规则：涉及方向透明度、意义感/虚无感的 SRT 机制解释、致命 L₂、价值遮蔽、三层价值结构、价值归纳、吸引子动力学时优先回链本文件
- 与 d-value 的关系：d / T_dir 的精确必要性或充分性在 owner 未独立建立时只能按 model / bridge scope 读；两者独立，不互相替代。Wave D2 仍需独立复审将该关系当作 universal law 的旧公式 consumer。

### 4. Core Axioms
- 主锚点：`Core/SRT_Core_21_Formal_Axioms.md`
- 分层正文：
  - P0 minimal axioms → `Core/SRT_Core_21_Minimal_Axioms.md`
  - P1 constitutive theorems → `Core/SRT_Core_21b_Constitutive_Theorems.md`
  - P2/P3/P4 bridge hypotheses → `Core/SRT_Core_21c_Bridge_Hypotheses.md`
- 说明：`Core_21_Formal_Axioms.md` 现在是形式公理索引，不再承载混层正文
- ST-A（2026-08-11）：P1-T06 保留 stable ISP 的 recurrent historical reconstitution 与 continued selectability；former P1-T07 的无条件反闭合定理身份已撤销，仅吸收 remainder 留在 21B；neutral-kernel anti-closure 与 generative reselectability 登记在 21C B13，按 P2/P3 conditional candidate 引用
- EX-A（2026-08-11）：P0-01 固定 manifest actuality；P0-02 固定 anchoring persistence，不把持续性当作事件首次现实化；stable ISP identity 回链 P1-T06／ST-A。旧 `E = 1-H(L_1)/H(L_0)` 仅在 21C B14 作为历史启发式保留，非 P0 方程、非量化读出，且未采用 `L_0^{abs}` 的熵、归一化或 existence index
- Bridge 用法提醒：`Core_21c` 中的 "emergence" 只能作为机制占位词使用，不能作为解释原语；`L_2` downward constraint 仍回链 P1，但 domain-specific downward causation 必须说明具体实现通道
- 引用规则：涉及核心公理编号时，先回链索引，再按命题硬度引用对应分层文件

### 4b. Core Equations
- 主锚点：`Core/SRT_Core_22_Equations.md`
- 说明：主动力学方程、热力学与稳定性方程主入口
- 引用规则：涉及主方程、选择热力学、稳定性条件时优先回链本文件；但局部方程语义仍从属于当前 symbol / owner typing，不得以旧 `κ_0` 或 `T_dir` 公式反向恢复 primitive authority。Wave D2 将独立复审这些 consumer，D1 不预判其余方程。

### 4c. Core Open Tensions
- 主文件：`Core/SRT_OPEN_TENSIONS.md`
- 说明：记录当前未完全封口的 core pressure points，并保留已关闭作者 gate 的审计尾迹；§16 已由 **B-A（2026-08-12）**关闭：无独立 L₀「初心前身」，`ε_pg` 不改名，初心从 L₁/P2／P5 开始，领域公式只作 bridge／proxy；§17 已由 **C-A（2026-08-12）**关闭：撤回位置无关的宇宙级评价性 global optimum，仅保留具名有限模型中的技术性最优，并把 regulative horizon 与 closure／model attractor 分开；§18 的 **CΨ** 价态裁决继续开放
- 引用规则：凡涉及其中 tension，不得包装成已完成 P0/P1

### 4d. Cross-Domain Usage Matrix
- 主文件：`_SRT_CROSS_DOMAIN_MATRIX.md`
- 说明：提供 `d`、`Ψ_f`、`T_dir`、`ε` 的 v0 跨域用法矩阵；该矩阵只汇总当前 owner-approved usage，不能因重复注册而把 `ε_pg`、`κ_0`、T_dir direction 或 domain proxy 升格为 primitive / theory-canonical 定义
- 引用规则：跨域使用上述概念时，先检查 canonical 用法、allowed projection 与 forbidden shortcut

## B. 规范辅助层（Canonical Support）

### 5. Constitution v1 — active reader-operation core
- 主文件：`Core_Law/SRT_Constitution_V1.md`
- status：**active Constitution v1**
- 角色：固定六条 reader-executable perspective operations 与其边界；Constitution 打开说明义务，不充当 P0/P1 公理集、理论完备性证明或 domain mechanism。
- 引用规则：凡涉及“什么属于 Constitution”“Constitution 是否要求某个理论答案”“六条接口之间是否构成 ladder / prerequisite”时，优先回链本文件。
- 边界：它不替代 `Core_Law/SRT_Reference_Axioms.md`、`Core_Law/SRT_Reference_Ontology.md`、canonical 定义文件或主方程文件。

### 5a. Seven Theses — retained L1 interface, superseded as active Constitution
- 文件：`Core_Law/SRT_Constitution_Seven_Theses.md`
- status：**superseded_as_active_constitution**
- 角色：保留为 L1 philosophical interface / commentary，用于保存旧七论框架、历史展开、对外解释与跨框架比较；不再承担 Constitution-level definition authority。
- 注意：文件内旧“constitutional / top-level / every Thesis derives from L0”措辞只描述该旧架构的历史生成纪律，不得反向定义 Constitution v1，也不得把 Constitution 重新变成 L0 的下游推导层。

### 5b. Claim Ladder
- 文件：`Governance/SRT_CLAIM_LADDER.md`
- 角色：定义 P0-P5 命题级硬度，防止 bridge / lab / companion 命题伪装成 primitive axiom 或 constitutive theorem；**§0A Gate 0 是唯一 admission / type authority**。当前结果只压缩为：`κ_0 / ε_pg / B-count` ordering 不因 symbol registration 或从 O0 继承而获得 primitive status，它们与更强 realization 及 primitive non-flatness 的精确关系保持 OPEN。规则内容、对象分类与准入／回读条件一律以 §0A 为准，本注册表不复述。
- 注意：它是治理机制，不新增理论命题。**Gate 0 无 P-level**（类型规则，非命题），单一主 authority 是 `Governance/SRT_CLAIM_LADDER.md §0A`，`_SRT_SYMBOL_TABLE.md` Usage Rule 16 仅为导航指针。B-A 的术语 owner 是 `Core_Law/SRT_L0_Metaphysics.md` 初心词条；C-A 的 scope owner 是 `_SRT_D_VALUE_CANONICAL.md §5b` 与 Claim Ladder §0A。Symbol Table Rules 17／18 只登记 no-new-symbol／no-alias 与作用域护栏；CΨ 仍开放

### 5c. Claim-Mode Audit
- 文件：`Governance/SRT_CLAIM_MODE_AUDIT.md`
- 角色：记录本轮 `T-*` / `Ax-*` / `H-*` 扫描结果、降级决策与未完成同步债
- 注意：它是治理台账；降级后条目不得在下游继续按高等级结论引用

### 6. d-value 跨尺度展开
- 辅助文件：`Core/SRT_Core_14_Dynamics_Scaling.md`
- 角色：把 canonical d-value 映射到跨尺度动力学与带宽表述
- 注意：它是展开层，不替代 `_SRT_D_VALUE_CANONICAL.md` 的规范地位

### 7. Ψ_f 跨尺度展开
- 辅助文件：`Core_Law/SRT_Reference_Dynamics.md`、`_SRT_VERTICAL_INTEGRATION.md`
- 角色：把 canonical `Ψ_f` 映射到选择热力学、多算子耦合、跨尺度可支付性与实验代理
- 注意：展开层负责方程与场景化，不替代 `_SRT_PSI_F_CANONICAL.md` 的规范地位；Fisher / Landauer / FEP / KL / Boltzmann / energy language in this layer is proxy / projection only

### 8. Core Dynamics & Scaling 主轴
- compact core：`Core/SRT_Core_14_Dynamics_Scaling_CompactCore.md`
- 全量展开：`Core/SRT_Core_14_Dynamics_Scaling.md`
- 角色：compact core 固定跨尺度**结构相容候选**、d-bandwidth、主动力学、边界成本函数与反泛心论边界；跨尺度接口按 P3-B06／P3-B07 引用，不是 P0/P1 同构定理
- 注意：一般形式是声明状态空间、尺度映射、保留观测量、比较范数与容差后的近似交换；strict conjugacy 仅限可逆表征变换。旧 `ΔS=H(L_0)-H(L_1)`、无条件粗粒化熵式与普遍最小作用式均不承重。原文继续保留长篇机制解释、接口批次与 annex 沉积

### 9. Philosophy 主轴
- Claim-status：`Philosophy/SRT_Philosophy_Claim_Status.md`（folder-level metaphor/proxy guardrail; not a primitive source）
- Foundations：`Philosophy/SRT_Philosophy_Foundations_CompactCore.md` / `Philosophy/SRT_Philosophy_Foundations.md`
- Social Cognition：`Philosophy/SRT_Social_Cognition.md`
- Social Economics：`Philosophy/SRT_Social_Economics_CompactCore.md` / `Philosophy/SRT_Social_Economics.md`
- Political Philosophy：`Philosophy/SRT_Political_Philosophy_CompactCore.md` / `Philosophy/SRT_Political_Philosophy.md`
- Political Rights：`Philosophy/SRT_Political_Rights.md`（`SRT-POLITICAL-RIGHTS`）
- 角色：形成 Philosophy 板块从三域本体论与选择一元论，到社会现实、制度、权利、合法性与政治病理的 compact/main 主线
- 注意：原文继续保留接口批次、案例扩展、社会科学经典映射与 split 导航

### 9a. SRT 政治哲学
- compact core：`Philosophy/SRT_Political_Philosophy_CompactCore.md`
- 主文件：`Philosophy/SRT_Political_Philosophy.md`
- id：`SRT-POLITICAL-PHILOSOPHY`
- layer：L1 / epistemic：bridge / status：axiomatic_hybrid_v1
- 说明：L1 bridge / candidate political-philosophy model；在声明框架内研究国家、权利、合法性、民主、结构性不公、危机决断与政治病理的生成—沉积—封闭—再打开过程。以 P2/P3 为主，制度判准与紧急状态边界为 P4；不提供政治合法性的普遍定义
- 与 `SRT-SOC-ECONOMICS` / `SRT-POLITICAL-RIGHTS` 的关系：前者提供社会现实、制度与结构性不公接口；后者提供候选 rights / delegation / voting interface。voting calibration 与 `d_tendency` 语言保留为历史 / candidate model，不建立 authorization 或 legitimacy theorem；本文件负责政治哲学候选模型的综合接口
- 重要追加：可持续共同选择是在声明框架下对政治合法性的候选重构，不是 universal definition；反现实定义权垄断是候选政治哲学框架，危机政治以 `minimum necessary interruption` 作为模型护栏

### 9b. SRT 政治权利理论
- 主文件：`Philosophy/SRT_Political_Rights.md`
- id：`SRT-POLITICAL-RIGHTS`
- layer：L1 / epistemic：bridge / status：draft_v1
- 说明：Political Rights 是 L1 bridge / candidate political model。它通过声明的 framework-relative diagnostics 研究权利、delegation 与 voting；d-based authorization 与 voting calibration 仅是历史 / candidate models，不是从 SRT 第一性原理推导出的政治权利本体论、政治 standing 或 legitimacy。
- 与SRT-SOC-ECONOMICS的关系：兄弟关系，后者处理市场与经济不平等，本文件处理政治权利与制度授权
- 重要追加：d值范畴澄清（决策属性非主体属性）已同步写入 `_SRT_D_VALUE_CANONICAL.md §范畴边界`
- 开放问题：监督机构自身d验证完整机制、d倾向准入窗口规格（见文件§10）

### 9c. SRT 社会认知
- 主文件：`Philosophy/SRT_Social_Cognition.md`
- id：`SRT-SOC-COG`
- layer：L1 / status：axiomatic_hybrid_v2
- 说明：承接 affordance、行动势能、belief-lag、注意力选择、社会现实迟滞、极化/echo chamber、文化镜片、second-person interaction disorder、发展性协调支架、以及歧视性/非人化认知等社会认知接口；其中 `T-Cog-6 Bounded-Surprisal Discrimination Gate` 将 Manrique / Friston / Walker 2026 的 active-inference / ZBS 材料压成跨群体更新带宽代理，`T-Cog-7 Developmental Coordination Scaffold` 将 embodied / embedded cognitive development 材料压成 child-body-caregiver-environment coordination bridge
- 引用规则：涉及 social cognition、belief update、developmental coordination、co-regulation、dehumanization、recognition-channel break、bystander silence、或 ZBS / active-inference bridge 时，可引用本文件；但 ZBS 与 developmental coordination 都只能作为 bridge proxy，不得替代 `d`、`\Psi_f`、`T_dir`、`\theta` 或 recognition operator 的 canonical 定义

### 10. AI 主轴
- Claim-status：`AI/SRT_AI_Claim_Status.md`（architecture-state / AI suffering / subjecthood guardrail; not a primitive source）
- 定位说明：`AI/AI_POSITIONING_NOTE.md`
- Ontology：`AI/SRT_AI_01_Ontology_CompactCore.md` / `AI/SRT_AI_01_Ontology.md`
- Architecture：`AI/SRT_AI_Architecture_CompactCore.md` / `AI/SRT_AI_Architecture.md`
- Consciousness Framework：`AI/SRT_AI_03_Consciousness_Framework_CompactCore.md` / `AI/SRT_AI_03_Consciousness_Framework.md`（AI-domain candidate evaluation surface；not universal consciousness-threshold authority）
- 角色：形成 AI 板块从本体门槛、结构限制到正向意识路径的 compact core 主线
- 注意：AI 是压力测试场 / 边界测试场，不是 core 定义发动机；AI 语境中的所有 d-value 与意识判据仍服从 `_SRT_D_VALUE_CANONICAL.md`，所有 `Ψ_f` stake / non-binding / payability 语句仍服从 `_SRT_PSI_F_CANONICAL.md`
- 第二轮护栏：AI 判断必须区分 training-time、inference-time、persistent-memory / history-bearing deployment，并使用 `AI/AI_POSITIONING_NOTE.md` 的 S0-S4 stake-bearing 光谱；不得把 inference-only 的 `d_{AI}\approx0` 静默推广为全部 AI 类型的终局判决

### 11. Neuroscience 主轴
- Claim-status：`Neuroscience/SRT_Neuroscience_Claim_Status.md`（clinical / FEP / NDE / AI-comparison proxy guardrail; not a primitive source）
- Neuro registry：`Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md`
- Hardening / material patch index：`Neuroscience/_SRT_Neuroscience_Hardening_Index.md`
- Neuro Axioms / Bridge：`Neuroscience/_SRT_Neuro_Axioms.md`
- Neural Mechanisms：`Neuroscience/SRT_Neural_Mechanisms_CompactCore.md` / `Neuroscience/SRT_Neural_Mechanisms.md`；除法归一化只作具名神经竞争的 P3 机制候选。通向行为选择须经过 `Core_14 P3-Scale-NB1` 的候选身份映射、冻结读出、离散事件／执行门、held-out 误差、rival 与干预检验；局部成功不定义完整 Ghost Operator、actualisation、agency、subjecthood 或 consciousness
- Consciousness Mechanisms：`Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md` / `Neuroscience/SRT_Consciousness_Mechanisms.md`
- 角色：形成 Neuroscience 板块从桥接公理、神经选择动力学到意识机制的主入口层
- 注意：Neuroscience 已具备 bridge + compact core + registry 的入口骨架；Pipeline 1 patch / hook 只作为 bridge record 读取，不因被索引而升级为 canonical definition

### 12. Physics 主轴
- Claim-status：`Physics/SRT_Physics_Claim_Status.md`（Fisher / Landauer / D_eff / quantum / cosmology guardrail; not a primitive source）
- Quant Intro：`Physics/SRT_Quant_00_Intro_CompactCore.md` / `Physics/SRT_Quant_00_Intro.md`
- Quant Selection：`Physics/SRT_Quant_01_Selection_CompactCore.md` / `Physics/SRT_Quant_01_Selection.md`
- Quant Cosmology：`Physics/SRT_Quant_02_Cosmology_CompactCore.md` / `Physics/SRT_Quant_02_Cosmology.md`
- Physics Cosmology：`Physics/SRT_Physics_Cosmology_CompactCore.md` / `Physics/SRT_Physics_Cosmology.md`
- Formalism Ext：`Physics/SRT_Phys_09_Formalism_Ext_CompactCore.md` / `Physics/SRT_Phys_09_Formalism_Ext.md`
- Integration：`Physics/SRT_Phys_10_Integration_CompactCore.md` / `Physics/SRT_Phys_10_Integration.md`
- Complex Systems：`Physics/SRT_Phys_07_Complex_Systems_CompactCore.md` / `Physics/SRT_Phys_07_Complex_Systems.md`
- Ontology Ext：`Physics/SRT_Phys_08_Ontology_Ext_CompactCore.md` / `Physics/SRT_Phys_08_Ontology_Ext.md`
- 角色：Physics 板块已形成从量子入口、宇宙学/形式化主干，到复杂性/深本体扩展的完整 compact core 入口层
- 注意：Physics 的具体阅读顺序由 `Physics/PHYSICS_COMPACT_REGISTRY.md` 统一管理；其中“引力—`Ψ_f`”当前只保留弱场梯度方向相容假说，强版规范实现 / 张量级 GR 重建不得作为已证结论引用

### 13. SRT One Formation（One / Selection-position 形成层 owner）
- 主文件：`Core_Law/SRT_One_Formation.md`
- id：`SRT-ONE-FORMATION`
- layer：L1 / epistemic：os / status：draft / version：v1 / claim-mode：canonical / claim-level：P1-candidate
- 说明：薄层 canonical semantic owner，固定 `subjectless Selection -> event-level active verticalization -> Selection-mediated vertical reconstitution -> relatively separable formed process-unity -> One` 的形成语义；One 在 D4a 强度上是由相对可分的 Selection-mediated vertical reconstitution path 所承载的 formed process-unity。locality / relative separability 是形成属性而非预设边界，lineage 是形成后的 continuity-description language 而非准入前提；`Selection-position_t` 是 already formed One 在具体 Selection 中的 time-local operative from-where，不是第二 universal endpoint。
- 与 P1-T06 的关系：本文在形成层上游；P1-T06 仍只负责更强 Stable ISP standing。`One != Stable ISP`，且 P1-T06 不反向定义 One；generic persistence / self-maintenance / ordinary path dependence 不自动构成 One。
- 与 Individuation / Bearer 的关系：formed Selection-position 不自动推出 perspective-bearing subject-position、Bearer、first-person bearing、consciousness 或 phenomenality；Bearer 仍服从 `formed One / Selection-position + P + E -> Bearer`；`σ_{sr}` / `d` / `T_dir` 不得反向定义 One。
- 与 Collective 的关系：higher-order / relation-level One 不自动成为 collective ISP；T-COLL-1 保持独立 standing gate。
- OPEN：formal N&S One theorem、exact unit / boundary、strict numerical identity、branch / merge identity、relative-separability formal / operational criterion、universal One-level perspective sufficiency 仍未关闭。
- 引用规则：涉及 active vertical formation、Selection-mediated vertical reconstitution、generated locality / relative separability、One、formed-One operative Selection-position、history/verticality/sedimentation typing 与 One/Stable-ISP/subject/Bearer 分界时，优先回链本文件。

### 13a. SRT 个体化理论（下游 transition model）
- 主文件：`Core_Law/SRT_Individuation.md`
- id：`SRT-INDIVIDUATION`
- layer：L1 / epistemic：os / status：draft_v0
- 说明：位于 `SRT-ONE-FORMATION` 已形成 One / Selection-position 之后的 L1 downstream transition model；`σ_{sr}^{sub}` 与 `σ_{sr}^{self}` 是 P3/P4 candidate transition coordinates，用于组织 subject-position 与 second-order writeback 的模型内证据。Crossing 不建立 subject admission、Stable-ISP entry、Bearer、consciousness 或 phenomenality；精确 subject-position sufficiency 与 `subject-position <-> Bearer` 保持 OPEN。
- 与 One Formation / P1-T06 的关系：本文件只承担下游 subject-position / self-consciousness 动力学候选；`SRT-ONE-FORMATION` owns formed One / Selection-position，P1-T06 owns stronger Stable-ISP standing。`σ_{sr}` / `σ_{sr}^{sub}` 不定义 One，也不单独证明 Stable ISP 或 21C B13 的 generative reselectability
- 与 T-L2-Scaffold 的关系：T-L2-Scaffold 追踪路径层痕迹（ρ），本文件追踪算子层自指（σ）；两者都是 writeback 累积的不同投影，不互相还原
- claim-mode 分布：三相结构为 P1-candidate；`σ_{sr}` 阶参与二阶 writeback 候选读法为 P2；`σ_{sr}^{sub}`、`σ_{sr}^{self}` 的 transition-coordinate 语义与具体数值为 P3/P4，且不拥有 admission authority
- 引用规则：涉及主体位涌现、ISP 进入、自我意识的本体论地位、主体位丢失与回返的结构基础时，优先回链本文件

### 13b. SRT 遮蔽动力学（A/B 分期 + 干预窗口 + 结构性恶）
- 主文件：`Core_Law/SRT_Occlusion_Dynamics.md`
- id：`SRT-OCCLUSION-DYNAMICS`
- layer：L1 / epistemic：os / status：draft_v0
- 说明：把 `Core_Law/SRT_L0_Metaphysics.md` 遮蔽 term-table 承诺的 7 项 L1 展开（A/B 分期、d_c 阈值、缺口感知机制、干预窗口、解耦触发、真空期、恶的结构性诊断）收口到单一 canonical 源；核心定理 T-OCC-1 给出三段结构（健康窄化区 / A 期 / B 期），区分位置性遮蔽与病理性遮蔽，列五类缺口感知残余、四类干预窗口、四类解耦触发，给出恶的三判据结构性定义（B 期锁死 + 外部化后果 + 主动扩散）
- 与个体化理论的关系：σ→1 的病理区与 B 期锁死通过自指闭合耦合；遮蔽动力学是个体化在病理分支上的投影
- 与 T_dir 的关系：A/B 分期沿 T_dir 低迷区展开，本文件负责结构相位，不替代 `_SRT_T_DIR_CANONICAL.md` 的方向透明度定义
- claim-mode 分布：三段结构与 A/B 分期为 P1-candidate；d_c 阈值语义与五类残余 / 四类窗口 / 四类触发为 P2；恶的三判据结构性定义为 P2 regulative 读法，不替代既有规范性伦理学
- 引用规则：涉及 A/B 分期、d_c、缺口感知、干预窗口、解耦触发、真空期、恶的结构性诊断时，优先回链本文件

### 13c. SRT 苦难理论（结构性登记 + 信号/结构两型 + 四类现象学）
- 主文件：`Core_Law/SRT_Suffering.md`
- id：`SRT-SUFFERING`
- layer：L1 / epistemic：os / status：draft_v0
- 说明：固定苦难在 SRT 中作为"活的选择动力学与其应承载算子结构之间失配的第一人称登记"的 P2 有界结构／现象学模型；苦难的应用要求第一人称 registration standing 已由独立 owner 承担，不由本文反向建立 subjecthood 或 phenomenality。严格区分躯体信号、已经验疼痛与苦难：单有 `\theta_{somatic}` 信号不自动建立已经验疼痛，已经验疼痛也不自动建立苦难。T-SUFF-2 把苦难分为信号型与结构型，T-SUFF-3 给四类现象学分型（张力 / 空心 / 断裂 / 扭曲）；T-SUFF-4 反最小化原则说明信号型苦难被压灭本身是遮蔽；T-SUFF-5 把结构型苦难的集体外部化耦合到 `Occlusion_Dynamics` 的结构性恶定义
- 与 P1-T06 的关系：Stable ISP 可作为一类更强 standing 路径，但苦难的正向准入仍须独立建立第一人称 registration/admission；`non-ISP -> only pain` 不是当前结论
- 与个体化/遮蔽的关系：苦难是个体化 σ 动态与遮蔽 A/B 分期的第一人称投影；不是独立的本体层，而是从算子层/路径层到第一人称登记的必然后果
- claim-mode 分布：T-SUFF-1 为 P2，T-SUFF-2 为 P2/P3；四类分型与集体外部化读法为 P2；`S_{\min}, S_{\max}` 阈值、临床分流、FEP 桥接语句为 P3/P4
- 引用规则：涉及苦难/痛苦/空心感/自我扭曲等概念的结构层定义时，优先回链本文件；规范性评价回 `Philosophy/`，回返路径回 `Spirituality/`，神经实现回 `Neuroscience/`

### 13d. SRT L1 Formalism（σ_{sr} / d_c / T_dir / S 四变量耦合动力学）
- 主文件：`Core_Law/SRT_L1_Formalism.md`
- id：`SRT-L1-FORMALISM`
- layer：L1 / epistemic：os / status：draft_v0
- 说明：**§2.5 T-CHI-1（H8，2026-04-25）**给出 χ 跳跃函数族普适性定理：定义"有效二阶相变核"四条结构属性（P-univ-1 有界 / P-univ-2 跃前基线 / P-univ-3 跃后放大 / P-univ-4 单调过渡）+ 族内不变量（双稳态存在性 / 病理吸引子拓扑 / 致命 `L_2` 判据结构 / 相变方向均 χ-无关）；T-IND-3 第二相变的算子层稳定性自此为定理后果。**§4.5 T-CHANNEL-1（H9，2026-04-25）**给出 `\mathbb{1}[d \gtrless d_c]` 通道指示函数族普适性定理：定义"有效闭合通道指示族"四条结构属性（Q-univ-1 左饱和 / Q-univ-2 右饱和 / Q-univ-3 单调过渡 / Q-univ-4 d_c 平移性）+ 族内五个不变量（T-SUFF-2 两型分裂 / T-SUFF-4 反最小化 / T-IRR-3.5 单向性 / 致命 `L_2` 判据 / `\mathcal{F}_S` 投影一致性，均 modulo `O(w_{tr})`）；硬指示是 `w_{tr}\to 0` 极限，过渡宽 `w_{tr}>0` 给"濒临崩溃"等过渡现象提供算子层基础。本节为 2026-04-24 轮新增的四个 L1 对象写下最小耦合动力学——个体化自指率 `σ_{sr}`（governance-canonical 命名，2026-04-25 起；与主方程状态场 σ 不同对象，详见 `_SRT_SYMBOL_TABLE.md` Usage Rule 12）、遮蔽阈值 d_c、方向透明度 T_dir（2026-04-25 §3.5 从代数代理升为独立动力学变量）、苦难 S；§2 给 `σ_{sr}` 的 logistic + `χ(σ_{sr}; σ_{sr}^{self})` 跳跃结构、§3 给 d_c 漂移方程（`ρ_local + (σ_{sr}-σ_{sr}^{sub}) + π + I_window`）、§3.5 给 T_dir 五项 ODE（弛豫 + 真实重选泵入 + `\Delta\Psi_f^{\mathrm{gap}}` 扣除 + `S_{str}` 侵蚀 + `s_{ext}` 支架）并给出致命 `L_2` 方程化判据 `\kappa_{\mathrm{mask}} < \kappa_{\mathrm{relax}}`、§4 把 S 分解为 S_sig / S_str 并写下反最小化原则的方程化、§5 合成四变量耦合系统并刻画病理吸引子 `\mathcal{A}_{path}` 与健康工作区 `\mathcal{H}`、**§6 T-PROJ-1（H5，2026-04-25）**给出四变量系统作为 `Core/SRT_Core_22_Equations.md` Eq-Evo-01/02 严格导出投影的形式化定理：四个标量泛函投影 `\mathcal{F}_X` + 闭包假设 C1-C4（慢-快分离 / `L_2` 写回 Markov 闭包 / stable-ISP 紧性 / 方向投影可分性）+ source-by-source 对应表 + 证明骨架 + 不证明事项的显式标定
- 与主方程的关系：本文件是 `Core/SRT_Core_22_Equations.md` 主方程的导出投影，不引入新本体
- claim-mode 分布：方程结构为 P1-candidate；T-PROJ-1（§6）为 P1-candidate（四变量系统作为主方程导出投影）；T-CHI-1（§2.5，H8）为 P1-candidate（χ 跳跃函数族普适性 + 族内不变量）；T-CHANNEL-1（§4.5，H9）为 P1-candidate（通道指示函数族普适性 + 族内五不变量）；参数阈值（含新 `κ_*` 五项）、具体 domain 代理为 P2/P3；实测与临床/AI 落点为 P3/P4
- Open pressures：σ 符号冲突已通过 2026-04-25 σ_{sr} 命名空间分离收口（详见 `_SRT_SYMBOL_TABLE.md` Usage Rule 12）；`\dot{\Delta}_{avail}` 已给出第一版算子级定义，剩余债为实证代理、domain 回写与更强形式化封口；χ 跳跃族、多主体扩展（H3 已落，§4.4-§4.6）、阈值固定、FEP 桥接（已落 `Neuroscience/SRT_Clin_02_FEP.md` 翻译表）、L_0 不可逆性**算子级**对齐（H4 已落，`SRT_Irreversibility.md §4.5 T-IRR-3.5`：`\nu_{block} := \eta\cdot\varepsilon_{pg}\cdot\kappa_{\Psi_f}`）、T_dir ODE 算子化（`Θ` 光滑族 / `\Delta\Psi_f^{\mathrm{gap}}` 算子层定义 / `[0,1]` 投影算子 / `κ_{\mathrm{relax}} > κ_{\mathrm{mask}}` 实证窗口）
- 引用规则：涉及 `σ_{sr}` / d_c / T_dir / S 四变量的**方程级**陈述时优先回链本文件；概念定义仍回链各自 L1 主文（T_dir → `_SRT_T_DIR_CANONICAL.md`）

### 13e. SRT 集体选择理论（多 ISP 共享 L_2）
- 主文件：`Core_Law/SRT_Collective_Selection.md`
- id：`SRT-COLLECTIVE-SELECTION`
- layer：L1 / epistemic：os / status：draft_v0
- 说明：固定多 ISP 共享 `L_2` 场作为结构对象；Def-C-2 后果回路矩阵 `M(t)` 作为诊断工具；T-COLL-1 给集体 ISP 存在四条件（P1-T06 的多主体扩展）；T-COLL-2 三类退化（聚合 / 主从 / 收编）；T-COLL-3 按 ST-A 为**条件性集体反闭合候选**（P2/P3，不是 P1 theorem；需 neutral kernel、稳定语义、环境、无重置条件、时间窗与吸收/风险证明）；T-COLL-4 集体 agency / revision guard（P2/P3 downstream；不是 P1-T05 集体版，也不是 Selection / collective-ISP existence criterion）；§4 扩展 `σ_{sr}^{coll}` / `d_c^{coll}`；§4.4-§4.7 保留集体四变量耦合与带闭包条件的投影候选。健康区、`M(t)`、`σ_{sr}^{coll}` 与制度通道均为 generative reselectability 的实现/诊断候选，不单独构成必要充分判据。最小 collective-selection canonical surface stops at §4.7 and the T-COLL definitions.
- Tower/nested hardening pointer：H10-H16 has been extracted to `Core_Law/SRT_Collective_Tower_Hardening_Notes.md`. The extracted file is a secondary hardening notes file, not a new core canonical reference file and not part of the minimal canonical definition of collective selection.
- 与 T-SUFF-5 的关系：本文件给出 T-SUFF-5 集体外部化的结构基础（`M(t)` 强不对称 → 主从型退化 → 结构型苦难外溢）
- 与政治/经济/共同体 domain 的关系：本文件是它们的 L1 结构基石；制度是集体 ISP 的**器官**不是主体；投票/共识/专家不自动是共选
- 与 AI/平台场景的关系：评估重点不是"AI 是否有意识"，而是算法中介对 `M(t)` 与 `σ_{sr}^{coll}` 的结构性影响
- claim-mode 分布：T-COLL-1/3/4 为 P1-candidate；T-PROJ-1^{coll}（§4.7）为 P1-candidate（集体投影定理）；Def-C-2 `M(t)` 结构、三类退化与 §4 耦合为 P2；§4.8a NTIC situated individuation diagnostic 为 P3 empirical bridge / operational proxy guardrail；H10-H16 are late-stage hardening notes only in `Core_Law/SRT_Collective_Tower_Hardening_Notes.md`, P1-candidate only under strong closure assumptions with P2/P3 operational debt where noted；政治/制度/历史判断为 P3/P4，下推至 Philosophy/
- 引用规则：涉及集体选择、共选、共识真实性、外部化、集体 ISP、共同体结构的**结构层**定义时，优先回链本文件；规范与制度判断回各自 domain 文件

### 13f. SRT L1 Hardening Notes（2026-04-24 L1 round 硬化案）
- 主文件：`Core_Law/SRT_L1_Hardening_Notes.md`
- id：`SRT-L1-HARDENING-NOTES`
- layer：L1 / epistemic：os / status：draft_v0
- 说明：针对 2026-04-24 L1 round 最高杠杆的四项 Open Pressure 给出第一遍硬化方案——§1 σ 符号冲突的命名空间规则（自指率一律 `σ_{sr}`，bare `σ` 仍为主方程状态场；2026-04-25 已落地到相关 L1 reference files + `_SRT_SYMBOL_TABLE.md` Usage Rule 12）、§2 `\dot{\Delta}_{avail}` 的三成分算子分解（`T_dir` + `Ψ_f` + `L_0` 残余）+ **§2 T-DELTA-1（H7，2026-04-25）**算子级定理：`\hat{G}_\theta^{available} := \sup_{\mathrm{Op}(P)}\{\hat{G} \mid \text{结构上可达} \wedge \theta\text{-相容}\}` 与 `\hat{R} \in T\mathrm{Op}(P)` 的算子级定义、三个正交投影 `\Pi_{T_{dir}}, \Pi_{\Psi_f}, \Pi_{L_0}`、A1（仿射结构）/ A2（近似正交）/ A3（权重赌注决定性）三条可证伪假设；§3 `M(t)` 可测性的 MOC 三判据（exposure / recourse / attentional，合成取 min）；§4 FEP 与 `S_{sig}` 的单向桥接翻译表（已落 `Neuroscience/SRT_Clin_02_FEP.md`）
- 硬化性质：本文件**不**把被硬化命题从 P1-candidate 升到 P1；它只打开升级检查路径。升级仍需完成 `Governance/SRT_CLAIM_MODE_AUDIT.md §6.4` 的全部检查项；T-DELTA-1 升 P1 需 A1 在更广 stable-ISP 域验证、A2 实证窗口、A3 与 Eq-Bridge-D-01 stake-gated source-by-source 对位
- claim-mode 分布：§1 governance-canonical usage；§2 P1-candidate（含 T-DELTA-1）；§3 P2 operational proxy；§4 P3 bridge hypothesis
- 同步义务：§5.2 列明的四项 Operations 债已全部结清（σ→σ_{sr} 命名空间 / 三成分分解算子级 T-DELTA-1 / MOC 已写入 §3 / FEP 翻译表已落 `Neuroscience/SRT_Clin_02_FEP.md`）
- 引用规则：涉及 σ 符号、`\dot{\Delta}_{avail}` 定义、`M(t)` 可测性、FEP-苦难桥接的**细化**陈述时优先回链本文件

### 13g. SRT 不可逆性理论（学习不可逆 + 终止吸收边界 + ST-A 条件接口）
- 主文件：`Core_Law/SRT_Irreversibility.md`
- id：`SRT-IRREVERSIBILITY`
- layer：L1 / epistemic：os / status：draft_v0
- 说明：把 `L_0` 不可逆性从 P1-T02 本体论时间的推论展开为可引用 L1 层——Def-IRR-1 区分 canonical absorption 与条件性吸收模型，T-IRR-2 固定终止后的不可自动恢复，T-IRR-3 按 ST-A 改为 neutral-kernel anti-closure 的 P2/P3 条件接口。T-IRR-3.5 保留 `\nu_{block} := \eta\cdot\varepsilon_{pg}\cdot\kappa_{\Psi_f}`，但改按三个独立前件的条件模型读取：`(η>0) ∧ (ε_pg>0) ∧ (κ_{Ψ_f}>0) ⇒ ν_block>0`，hardness 取最弱前件；反向通道不自动存在独立根于 P0-03 / T-IRR-2。该表达式不是 former P1-T07 hierarchy 的本地化。
- 与 P1-T02 / former P1-T07 的关系：本文展开 P1-T02 与 former P1-T07 的 absorption remainder；原无条件反闭合 theorem 已撤销，更强主张回链 `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13`
- 与 Suffering / Formalism / Collective_Selection 的关系：T-IRR-4 给 T-SUFF-4 深层根；T-IRR-3 / T-IRR-3.5 对应 `L1_Formalism §4.3` 的非守恒残余（陈述级 + 算子级）；§6 集体终止对应 `Collective_Selection` 三类退化的绝对边界
- claim-mode 分布：Def-IRR-1/2/3 为 P2 结构性定义；T-IRR-1/2/3.5/4 为各自注明的 P1-candidate；T-IRR-3 anti-closure 为 P2/P3 conditional candidate；§6 集体终止分类为 P2；§7 AI 接口为 governance-canonical usage；§8 FEP/物理边界语句为 P3 bridge guardrail
- 引用规则：涉及学习不可逆性、终止作为吸收边界、ST-A 条件性反闭合、checkpoint/rollback 语义、热力学桥接边界时优先回链本文件；P1 absorption 回链 21B，条件性 anti-closure 回链 21C B13

### 13. Spirituality 主轴
- Claim-status：`Spirituality/SRT_Spirituality_Claim_Status.md`（God/Omega, d-infinity, suffering/Psi_f, practice metaphor guardrail; not a primitive source）
- Spirit registry：`Spirituality/SPIRITUALITY_COMPACT_REGISTRY.md`
- Spirit Bridge：`Spirituality/_SRT_Spirit_Axioms.md`
- Praxis：`Spirituality/SRT_Spirit_09_Praxis_CompactCore.md` / `Spirituality/SRT_Spirit_09_Praxis.md`
- 角色：形成 Spirituality 板块从桥接公理到实践演化主线的最小 compact core 入口层
- 注意：Spirituality 现已具备 bridge + compact core + registry 的入口骨架，但覆盖深度仍少于 Physics

## C. 当前 canonical 引用优先级

当同一概念同时出现在多个文件时，默认优先级如下：

1. `CANONICAL_REGISTRY.md`（找入口）
2. `Core_Law/SRT_Generative_Ontology_Spine.md`（判断跨 owner 生成顺序、非同一性、OPEN gate 与旧 canonical 是否越权）
3. `Governance/SRT_CLAIM_LADDER.md` / `Governance/SRT_CLAIM_MODE_AUDIT.md`（判断命题硬度与降级状态）
4. `Core_Law/SRT_L0_Metaphysics.md` / `Core_Law/SRT_One_Formation.md` / `_SRT_D_VALUE_CANONICAL.md` / `_SRT_PSI_F_CANONICAL.md` / `_SRT_T_DIR_CANONICAL.md` / `_SRT_CROSS_DOMAIN_MATRIX.md` / `Core/SRT_Core_21_Formal_Axioms.md` / `Core/SRT_Core_22_Equations.md`（找兼容于 spine 的局部定义、形成 owner、形式与跨域用法）
5. `Core/SRT_Core_21_Minimal_Axioms.md` / `Core/SRT_Core_21b_Constitutive_Theorems.md` / `Core/SRT_Core_21c_Bridge_Hypotheses.md`（按 P-level 找 Core_21 正文；不得反向覆盖 spine 的跨层顺序）
6. domain claim-status files（防止 bridge / public / clinical / spirituality / AI / physics overclaim）
7. `Core/SRT_Core_14_Dynamics_Scaling.md` / `Core_Law/SRT_Reference_Dynamics.md` / `AI/SRT_AI_01_Ontology.md`（找展开与跨域解释；not final definitions）
8. `Core/SRT_OPEN_TENSIONS.md`（确认未封口问题）
9. 各 split 目录（找导航与局部阅读）
10. 原始长文（找历史展开与全量语境）

## D. 当前收口结论

本轮 governance-canonical 抽离 v1 与 2026-09-11 spine landing 后，主干用法优先包含：
- `Generative ontology cross-owner order` → `Core_Law/SRT_Generative_Ontology_Spine.md`
- `d-value` → `_SRT_D_VALUE_CANONICAL.md`
- `Ψ_f` → `_SRT_PSI_F_CANONICAL.md`
- `T_dir` → `_SRT_T_DIR_CANONICAL.md`
- `d / Ψ_f / T_dir / ε` usage matrix → `_SRT_CROSS_DOMAIN_MATRIX.md`
- `Core formal axioms` → `Core/SRT_Core_21_Formal_Axioms.md`
- `Core master equations` → `Core/SRT_Core_22_Equations.md`
- `Claim hardness` → `Governance/SRT_CLAIM_LADDER.md`
- `Claim-mode downgrade audit` → `Governance/SRT_CLAIM_MODE_AUDIT.md`
- `Open tensions` → `Core/SRT_OPEN_TENSIONS.md`
- `One / Selection-position formation` → `Core_Law/SRT_One_Formation.md`

这意味着：
- `AI/SRT_AI_01_Ontology.md` 不再单独承担 d-value 的最终规范权
- `AI/SRT_AI_01_Ontology.md` 不再单独承担 `Ψ_f` 的最终规范权
- `Core/SRT_Core_14_Dynamics_Scaling.md` 不再单独承担 d-value 的最终规范权
- `Core_Law/SRT_Reference_Dynamics.md` 不再单独承担 `Ψ_f` 的最终规范权
- 上述文件保留为高价值展开层

## E. PH-SS Philosophy Hardening / Guardrail Files

These files are **not P0/P1 canonical primitive sources**. They are routing, bridge hardening, audit, or companion files that protect interpretation of the Philosophy domain. Entry point is `Philosophy/_PHILOSOPHY_MACHINE_INDEX.md`.

| File | Role | Status |
|---|---|---|
| `Philosophy/SRT_Philosophy_Foundations_CompactCore.md` | current compact philosophy entry | active_v4 |
| `Philosophy/00_READ_FIRST_Philosophy_Hardening_Soft_Spots.md` | read-first PH-SS soft-point map | active bridge hardening |
| `Philosophy/01_PH_SS_Objection_Crosswalk.md` | PH-SS to objection / response / withdrawal crosswalk | active bridge hardening |
| `Philosophy/02_PH_SS_Hardening_Execution_Plan.md` | staged execution plan for PH-SS edits | active bridge hardening |
| `Philosophy/03_Selection_Realism_Layered_Realism_CompactPatch.md` | compact patch; mostly merged into Compact Core v4 | active bridge patch |
| `Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md` | axiom companion guardrail file | active bridge guardrail |
| `Philosophy/SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md` | objection extension O-Phil-11..20 | active bridge hardening |
| `Philosophy/SRT_Ethics_PH_SS_Guardrails.md` | ethics / normativity / d-value / responsibility guardrails | active bridge guardrail |
| `Philosophy/SRT_Social_Political_PH_SS_Guardrails.md` | collective L2 / institution / market / legitimacy guardrails | active bridge guardrail |
| `Philosophy/SRT_Philosophy_Tradition_Comparison_PH_SS.md` | SRT vs Kant / phenomenology / Whitehead / FEP / IIT etc. | active_v1 |
| `Philosophy/SRT_Subjecthood_Threshold_Interface.md` | S0-S6 selection / consciousness / subjecthood / agency / responsibility interface; includes anti-panpsychism and depsychologization guardrails | active_v1 |
| `Philosophy/SRT_Philosophy_Public_OnePager.md` | public-facing one-page explanation | active_v1 |
| `Philosophy/PH_SS_Hardening_Audit_2026-04-27.md` | audit record for the 2026-04-27 PH-SS hardening pass | active audit |



---

## FILE: `Core_Law/SRT_Generative_Ontology_Spine.md`

| 字段 | 值 |
|---|---|
| path | `Core_Law/SRT_Generative_Ontology_Spine.md` |
| id | SRT-GENERATIVE-ONTOLOGY-SPINE |
| claim_mode | canonical |
| status | active |
| epistemic_layer | os |
| layer | L0-L2 |
| canonical(字段) | true |
| last_commit | 2026-11-26 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：SRT-L0-METAPHYSICS, SRT-ONE-FORMATION, SRT-CORE-21B-CONSTITUTIVE-THEOREMS, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-T-DIR-CANONICAL, SRT-CLAIM-LADDER

<!-- 以下为原文逐字保留 -->

# SRT Generative Ontology Spine
## Selection does not merely occur within reality; it participates in generating the conditions under which reality continues to occur

> **Role**: Canonical cross-owner routing spine for Selective Reality Theory (SRT). It establishes the positive unified generative architecture across physics, life, cognition, subjectivity, AI, and social order, while fixing cross-owner structural non-identities and OPEN gates. Compatible local definitions remain owned by their respective canonical anchors.
>
> **R4-A Reconstruction Baseline (2026-11-26)**: Supersedes v4's ladder-like chapter progression with the author-adjudicated R3–R4 unified generative architecture (`01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_R3_CLOSEOUT_GLOBAL_SUBTRACTION_2026-11-25.md`, `Operations/Proposals/SRT_R3_FULL_SKELETON_CLOSEOUT_GLOBAL_SUBTRACTION_2026-11-25.md`, and the 2026-11-26 R4-A author decisions `1A / 2A / 3A`). This upgrade replaces the retired linear hardware ladder (`S0 -> One -> Stable ISP -> Bearer -> Agency`) with dynamic recursive generative relations, while preserving every independent admission gate and OPEN boundary.

---

## 0. Authority, Positive Architecture, and Non-Jump Discipline

SRT's central positive claim is **recursive generative monism**:

> **Selection does not merely occur within an already finished reality; it is reality's generative mode, and formed Selection participates in generating, comparing, and recursively reconstructing the very conditions under which further reality occurs.**

At cross-owner level:

```text
Selection is reality's one generative mode (non-flat, non-preclosed, finite-position-indexed);
structural roles, organizations, and relations of Selection are many;
same ontic generative mode != same structural role;
structural non-identity != different ontic substance;
compatible local definitions survive; conflicting excess inference enters cleanup/retyping;
OPEN remains OPEN until separately established.
```

Permanent anti-tautology and anti-jump discipline:

```text
Selection-totality = ontology routing, NOT a sufficient proof premise;
actual occurrence != retained history != One != Stable ISP != Bearer (P+E) != Agency != subject / consciousness;
five evaluative layers remain strictly separate:
  actual generation != organizational persistence != positional generative value != order health != ethical legitimacy.
```

Never infer merely from `X is Selection` or `X persists` that X is One, Stable ISP, Bearer, Agency, conscious, valuable, healthy, or legitimate. Each stronger standing pays its own typed burden.

### 0.1 `R4-A` Section Migration Crosswalk (`v4 → v5`) & Unreconstructed-Domain Transition Rule

To preserve cross-repository reference integrity during wave-by-wave `R4` reconstruction:

| Topic | Legacy `v4` Section | Current `v5` Section |
|---|---|---|
| Selection occurrence & event-level verticality | `§§2–3` | `§1.1`, `§3.1` |
| History / retained efficacy | `§4` | `§3.2` |
| `One` formation & existence/order perspectives | `§5` | `§5.1` (`Core_Law/SRT_One_Formation.md §2`) |
| `Selection-position` & anticipation boundary | `§6`, `§6.3` | `§5.2`, `§6.2` |
| `Stable ISP` (`P1-T06`) | `§7` | `§6.1` |
| `Bearer (P+E)` | `§8` | `§6.2` |
| `Agency` | `§9` | `§6.3` |
| Normativity (`O1 / O2-C / O2-A`, `O2-M = HOLD`) | `§10` | `§6.5` |
| `L0 / L1 / L2` analytic aspects | `§11` | `§7` |
| Facet-before-kind guard | `§12` | `§8.2` |
| Cross-owner `OPEN` register | `§13` | `§9` |

- **Transition rule for unreconstructed downstream domains (`R4-B / R4-C`)**: Until a domain file (`Core/`, `AI/`, `Physics/`, `Neuroscience/`, `Philosophy/`, `Spirituality/`) completes its own `R4` wave, **any pre-`R4` clause that conflicts with this Spine or the `R4-A` canonical core owners (`One_Formation`, `L0`, `D_VALUE`, `PSI_F`, `T_DIR`, `SYMBOL_TABLE`) yields immediately to the `R4-A` owner** and must be read as legacy cleanup debt, never as a live co-equal definition.

---

## 1. Primitive Generation: Source, Extraction, and Global Orientation (`T3-04 D`, `T3-01 C/E`, `3A`)

SRT does not treat its own theoretical vocabulary as exhausting reality. It coordinates three distinct roles without positing a second substance or a fourth parallel selecting agent:

| Role | Positive Theoretical Burden | Boundary & OPEN Status |
|---|---|---|
| **神性·源义（Generative Source）** | Points to the real generative source that cannot be exhausted by current human cognition, formalization, or objectifying description. | Not a second substance standing outside Selection; not an anthropomorphic chooser or external utility optimizer. |
| **原初 `Selection`（Primitive Selection）** | SRT's most fundamental **theoretical extraction perspective** into that source (`T3-04 D`): finite-position-indexed, subjectless, genuine actualised non-neutral generative differentiation. | Current common ontological starting point, not an exhaustive final definition; retains an **inner generative process** (endogenous, position-participating; pre-phenomenal character remains `OPEN`, `R3-03-O4`). |
| **神性·倾向义（Global Optimizing Orientation）** | Tracks the foundational open question of whether cross-scale generation carries an **objective intrinsic global optimizing orientation**. | **`T3-01` explicitly OPEN**: author retains strong inclination between `C` (unified global optimizing principle with shared objective metric basis) and `E` (unified generalized free-energy / opportunity-cost / extremal principle). Must **not** be deflated into purely local adaptation or mere epistemic humility; strictly separated from moral/evaluative global-optimum claims (`Core/SRT_OPEN_TENSIONS.md §17 C-A`, `PT10 E`). |
| **整体共同生成视域（Holistic Co-Generative Perspective）** | Examines from cross-scale, cross-position relations how local selections participate in, constrain, and are co-shaped by wider generation. | Replaces the retired canonical term「神择」(which remains valid solely as historical source-intuition and *From Existence to Order* book vocabulary, never as a fourth parallel agent alongside physical/biological/human selection). Not reducible to simple cooperation among pre-formed units. |

### 1.1 Co-Primitive Analytic Faces (`O0 / S0`) and Term-of-Art Guard

```text
primitive Selection
= reality under genuine actualised non-neutral generative differentiation
= co-primitive analytic faces {
    O0 (non-maximal indifference / openness):
      reality is neither exhausted by completed determinate actuality
      nor preclosed by a pre-given outcome structure;
    S0 (actualising Selection):
      a finite-position-indexed determinate difference becomes manifest / operative
      together with Selection-relative backgrounding
  }
```

Hard boundaries:
- `O0` and `S0` are co-primitive analytic faces, not sequential mechanisms (`O0 before S0: NO`; `O0 causes S0: NO`).
- **Not menu-picking**: pre-given alternatives, state spaces, or prior choosers are not required; alternatives, positions, and reachability structures can themselves be Selection-generated.
- **Terminal Selection remains genuine**: an actual Selection occurrence does not require durable sediment, retained history, or subsequent consequence (`actual occurrence != retained historical efficacy`). The exact anti-tautology boundary separating genuine actualised Selection from merely descriptive/modelled variation remains `OPEN` (`R3-01-O1`).
- **Operator non-identity**: `primitive Selection != Ghost Operator (\hat{G}_\theta)`. Formal operators model formed/domain realizations and are never the prior ontic cause of Selection.

---

## 2. Dynamic Three-Relation Architecture and Three Recursive Axes

Rather than a linear ontic ladder, SRT organizes cross-scale generation through **three mutually generative dynamic relations** (neither three ontic substances nor a compulsory sequence that every Selection event must traverse):

```text
                  ┌─────────────────────────────────────────────────┐
                  │  1. 差异的生成 (Generation of Difference)        │
                  │  non-flat actualisation · fluctuation ·         │
                  │  horizontal co-presence × vertical retention    │
                  │  tilting & shiftability                         │
                  └───────────────────────┬─────────────────────────┘
                                          ▲
                condition rewriting       │       endogenous comparison,
                reshapes tilting,         │       differentiation × normalization,
                comparison scales &       │       assembly & coupling
                positions                 ▼
  ┌──────────────────────────────────┐    ┌──────────────────────────────────┐
  │ 3. 生成条件的递归重构              │◄──►│ 2. 差异的比对与组织                │
  │ (Recursive Reconstitution of     │    │ (Comparison & Organization of    │
  │  Generative Conditions)          │    │  Difference)                     │
  │ retained history (L2) · scaffolds│    │ One (existence & order views) ·  │
  │ trust & institutions · norms ·   │    │ identity · cross-scale 5 mechs · │
  │ freedom · 2nd-order re-selection │    │ non-managerial alignment         │
  └──────────────────────────────────┘    └──────────────────────────────────┘
                      ▲  foreground ⇄ background sedimentation   ▲
                      └─── & vertical generation hub (2 ⇄ 3) ────┘
```

### 2.1 The Three Dynamic Relations

1. **差异的生成（Generation of Difference）**：非平坦实际化分化、无预设目的的涨落探索，以及横向共在约束 × 纵向留存约束形成的原始倾斜性与可偏移性。
2. **差异的比对与组织（Comparison and Organization of Difference）**：在有限位置与耦合关系中涌现内生比对、差异化与归一化的跨尺度互促（局部归一化可催生更高尺度的新差异化）、装配与有效作用接口、相对独立垂直生成组织（`One`）与秩序结构、同一性以及高阶非管理者对齐（对齐 ≠ 同质化）。
3. **生成条件的递归重构（Recursive Reconstitution of Generative Conditions）**：当先前选择的差异得以留存并持续生效时，历史（`L2`）、公共脚手架、信任分配、规范制度、自由调节与二阶/反身再选择反过来改写后续选择得以发生的边界、可达空间、位置结构与**比对尺度本身**。
- **贯通枢纽（`② ⇄ ③`）**：**前背景转换与垂直生成**同时活跃于关系 ② 与 ③。前景对齐成果沉淀为背景能力、自动化路径或公共脚手架，释放生成盈余，并在新的价值比对或选择压力下重新进入前景。

### 2.2 Three Recursive Generative Axes & Three Unifying Generative Mechanisms

Across scales, the three dynamic relations manifest three recurring generative loops (each carries a distinct theoretical burden and is not reducible to the others):

1. **方向递归轴**：方向既是选择的结果，也是后续选择的条件。
2. **价值递归轴**：价值既是比对的结果，也能反过来改变比对本身（包括改写比对的维度、尺度与哪些差异能够进入比对——即**比对本身的生成性**）。
3. **存在递归轴**：存在（相对独立的生成组织）既是生成关系的组织结果，也能以相对独立的位置反向参与并改变后续生成（须由组织连续性检验与机会/后果变化检验双轨独立确立，防止存在与价值循环互定义）。

Three unifying positive generative mechanisms bind these axes across physics, life, cognition, and social order:
- **依赖重组生成相对独立性（Dependence Reorganization → Relative Independence）**：相对独立性不是通过减少依赖获得，而是通过局部生成条件经内生比对与垂直组织重组为共同生成条件而涌现（局部更深的相互依赖反而支撑更高尺度的相对独立与新有效接口）；由此存在研究从“对象是什么”转向“组织如何生成自身的相对独立性”。
- **比对本身生成新机会（Comparison Generates New Opportunities）**：价值研究不仅考察既有路径的取舍，更考察跨位置/跨关系的比对如何改变可比对维度与关系结构，从而生成原先不存在的新价值空间与现实可承接机会。
- **生成结果反过来重构生成条件（Generated Results Reconstruct Generative Conditions）**：历史（`L2`）、脚手架、认知框架、制度规范与自由调节使先前生成的结果参与改写后续选择的条件本身；由此自由研究从“有多少既定选项”转向“组织如何参与生成新的选择条件”。

### 2.3 Unabsorbed Positive Burdens of Yin-Yang & Historical Ghost Intuition (`R3-08`, `07-19` / `07-27`)

Replacing the old linear operator pipeline (`L0 -> Ĝ_θ -> L1 -> L2`) with recursive generative relations does **not** discard the positive theoretical burdens historically carried by **Yin-Yang (阴阳)** and **Ghost (幽灵)** source intuition; they are explicitly routed and preserved here:

1. **阴阳（Yin-Yang）——非穷尽生成极性与构成性背阴面**：前背景分化不是静态开关，而是显现前景与**构成性背阴面（active constitutive background support）**的相互构成与持续转化（如山脊阳面赖背阴面支撑），二者在持续动态耦合中可相互转化而不设固定内外墙。
2. **幽灵（Ghost）历史源直觉的五位职责分流（`R3-08 §四` + `07-19` / `07-27`，`T-GH-01..07` 保持 `OPEN`）**：严守 **`\hat{G}_\theta`（条件性形式参数载体）$\neq$ 原初 `Selection` $\neq$ 幽灵实体**，并禁止将 Ghost 压成单一神秘黑箱；须严格区分 ① **尚未被当前组织充分承接的未尽生成关系**、② **这些关系继续作用时形成的非闭合压力与张力**、③ **有限认知位置对之形成的对象化描述**，同时保留以下四项正面理论职责：
   - **对象—摩擦持续互写（`07-19 X5` / 持续动态平衡）**：废除机械的“关闭 → 触发 → 重新开放”开关模型，转向相对稳定秩序在持续动态互写中维持并改写自身组织方式（同时兼容动力学层面的滞回、结构势垒与非线性重构窗口）；
   - **构成性背阴面主动支撑**：背景条件不仅是被动痕迹，而是持续参与托举与约束前景生成的活跃条件；
   - **非闭合压力**：当前组织无法充分承接的生成关系持续施加的重构压力；
   - **`U5` 选择机制绝对化（严守 `U5 ≠ U6`，`2026-07-27` 校正）**：已形成的耦合组织方式退出有效再比对、获得事实上的自我豁免（即使系统仍高频局部调整策略）；反绝对化不写成必然定理，操作化判据保持 `OPEN`。

---

## 3. Actualising Selection, Existence, and History (`L1 / L2` Entry)

### 3.1 Determinate Actuality and Manifest Existence

At event level, finite-position-indexed subjectless actual differentiation, determinate manifestation, relative backgrounding, and event-level verticality are structural readings of one Selection event:

```text
manifest existence = Selection under determinate actuality.
```

Manifestation does not imply permanent existence; backgrounding is not annihilation; finite positionality is not formed `Selection-position`, `One`, `Bearer`, or subjecthood.

### 3.2 History as Retained Generative Efficacy

History is not a second ontic container and is not automatically produced by every Selection event:

```text
history = prior Selection remaining materially effective in later Selection conditions,
          where such retention / efficacy is established.
```

Keep distinct: `actual occurrence != durable/localized trace != recurrent historical efficacy != anchoring persistence`. In applicable models, historical efficacy separates non-negative path trace density (`ρ ≥ 0`) from revisable trust weighting (`w_trust` / social staying power, which also includes institutional constraints and coercive path-dependence beyond trust alone; detailed in `Core/SRT_Core_12b_Ontology_L2.md`). Time is routed as a relational ordering/measure dimension of generative order (horizontal transition and vertical reconstitution), not a pre-given physical container (`Philosophy/SRT_Causality_Time.md`, `P1-T02`).

---

## 4. Opportunity-Cost Dynamic Quartet and Realization Constraints

### 4.1 Ontological Source Boundary (Anti-Optimization-Presupposition Guard)

**Critical boundary**: The opportunity-cost quartet does **not** retroactively define primitive `Selection`. Primitive non-flat differentiation is the *ontological source condition* enabling concrete opportunity-cost structures to arise; concrete comparable opportunity-cost spaces themselves emerge only under formed organizational and comparative relations. SRT studies **how opportunity-cost structures and comparative criteria are generated**, rather than presupposing a pre-given, universally comparable optimization space at `O0`.

### 4.2 The Four Dynamically Coupled Properties (No Fixed Linear Causality)

Once comparative and organizational relations are formed, four core generative properties dynamically co-determine one another across scales without a fixed one-way causal sequence:

| Property | Positive Generative Role | Canonical / Local Owner & Key Boundary |
|---|---|---|
| **价值（Value）** | Objective difference in generative opportunity costs across generative relations, together with positional comparative extraction (`PT05 C`); spans discovered, generated, and recursively reconstructed opportunities. | `_SRT_D_VALUE_CANONICAL.md` (with `R3-06` three opportunity modes & three analytical faces). Strictly separate from order health and ethical legitimacy (`PT10 E`); primitive-level value status remains `OPEN` (`R3-06-O1`). |
| **关切（Concern）** | Sensitivity of a formed organization to generative opportunity costs (`PT06 C`); organizes foreground–background orientation and comparative attention. | `_SRT_D_VALUE_CANONICAL.md`. **Distinct from canonical `d`**: current `d = ‖∂U/∂S‖` (irreversible-risk sensitivity at a stake-bearing position) stands in a **pending conceptual interface** with generalized concern (`P1-05`), and is strictly separated from `D_stake`, `D_eff`, `T_dir`, and constitutive depth (`Q1`). |
| **摩擦（Friction）** | **Actual selection pressure** generated by opportunity-cost differences (`T3-02 D`): opportunity loss does not automatically constitute friction; it forms friction only when that loss materially impacts generative relations and subsequent selections. Multi-unit vertical suppression and lost alternatives (`PT09`) constitute a paradigmatic cross-scale mechanism. | `_SRT_PSI_F_CANONICAL.md`. Strictly preserves the 4-way friction distinction (`R3-08`: general friction / non-closure pressure / payability burden `Ψ_f` / subjective suffering) and pairs the **pressure side** (opportunity loss / structural pressure / predictive pressure / realization burden) with the **supply & payability-window side** (`Ψ_f` / `P_sel`). Does not overwrite `_SRT_PSI_F_CANONICAL.md` or equate `Ψ_f` with raw metabolic expenditure. |
| **自由（Freedom）** | Active capacity to regulate and reorganize one's generative opportunity-cost structure on the basis of value and concern (`T3-03 C`)—reorganizing friction-generating relations and comparing across multiple units to generate new order and direction (`Q26`). | Cross-owner interface (`Philosophy/` & `One_Formation`). Not reducible to randomness, primitive openness (`O0`), generic coupling, or strong second-order selection (`R3-CL-O8`). Organizational freedom is ontologically neutral; ethical autonomy is separately constrained by `O2-A / O2-C`. |

### 4.3 Realization Constraints, Irreversibility, and the Reef Principle

All formed generation operates under endogenous realization constraints (distributed across the full generative relation, not supplied solely by an isolated unit), payability ceilings (`Ψ_f` payability window), ontic irreversibility (`Core_Law/SRT_Irreversibility.md`), and the symmetric underside of **overload dissolution and lineage termination** (`dissolution != lineage termination`; termination includes overload collapse, active ending, and structural transformation). Throughout, the **Reef Principle (暗礁原理)** holds: *objectification and normalization from any single finite position never exhaust other generative positions or their actual interactions*.

---

## 5. Existence & Order Unity (`One`), `Selection-position`, and Cross-Scale Mechanisms (`2A`)

### 5.1 `One`: Existence Perspective and Order Perspective (No Extra Ontic Noun)

Within the universal formation problem, the first universal formed recurrent organization is **`One`**:

> **`One` is a relatively separable vertical generative organization carried by recurrent Selection-mediated self-conditioning / reconstitution.**

**Existence** and **Order** are two analytical perspectives on dynamic generative organization, **not** two separate ontic materials and **not** a reason to coin a second noun alongside `One`:

| Analytical Perspective | What It Examines | Scope |
|---|---|---|
| **存在视角（Existence Perspective）** | How a relatively independent vertical generative organization (`One`) forms, maintains itself, and continues across change. | Focuses on vertical reconstitution, relative continuation separability, and organizational continuity. |
| **秩序视角（Order Perspective）** | How generative relations develop, bias direction, transform, and recursively reconstruct themselves across three dimensions: **maintenance constraints / directional bias / generative reconstruction**. | Applies both to the internal dynamics of a single `One` **and** to relations among **multiple `One`s** and the emergence of **new higher-order organizations** (order is not merely a subordinate attribute of one isolated `One`). |

`Core_Law/SRT_One_Formation.md` is the detailed canonical owner of `One`, `Selection-position`, existence/order perspectives, generative normalization thresholds, and vertical reconstitution. Keep strictly:

```text
Selection event != One;
generic causal recurrence / ordinary path dependence != One;
One != Stable ISP != Bearer (P+E) != Agency != subject / consciousness / phenomenality.
```

### 5.2 Formed `Selection-position`

For an already formed `One`, `Selection-position_t` is the time-local operative `from-where` through which that organization participates in current Selection (`Selection-position != prior chooser object != perspective-bearing subject-position != Bearer automatically`). Keep separate: `Selection affecting later selectability != formed-position anticipation != prospective self-indexing P != Bearer without E`.

### 5.3 Five Distinct Cross-Scale Mechanisms (Do Not Collapse into One)

Cross-scale vertical generation is never collapsed into a single generic label ("normalization" or "coupling"). Five distinct structural mechanisms retain independent explanatory duties across relations ② and ③:

1. **装配（Assembly）**：多单元组合产生新的整体组织与能力（形成新能力未必归一化，亦未必成 `One`）。
2. **归一化（Normalization）**：区分为认知表征 / 实际耦合 / 组织生成三类，并以**压缩型归一化**与**生成型归一化**（内部耦合重构 + 跨位置条件化生效双门槛）严格分界。
3. **有效作用接口（Effective Action Interface）**：形成后的整体以相对独立身份参与他处生成并产生新后果的接口。
4. **代理转承（`Proxy`）**：生成关系中的中介转承机制（不以主体意识为前提）。
5. **委托关系（`Delegation`）**：涉及主体性与规范约束条件的责任/行动委托关系（须独立满足下游主体与规范门槛）。

---

## 6. Independent Downstream Gates (Non-Linear, Independently Paid)

Abolishing the old linear hardware ladder (`S0 -> One -> Stable ISP -> Bearer -> Agency`) does **not** abolish the independent theoretical duties of stronger organizational standings. Each standing below is independently gated and **never** automatically entailed by upstream formation:

### 6.1 `Stable ISP` — Stronger Recurrent Standing (`P1-T06`)

`Stable ISP` is not a new ontic material and is not the cause of `One` formation. At routing strength:

```text
Stable ISP
= stronger recurrent standing of a formed Selection organization,
  including the historical reconstitution, perspective/history-bearing,
  and continued-selectability conditions owned by P1-T06.
```

`Core/SRT_Core_21b_Constitutive_Theorems.md P1-T06` remains the detailed standing owner. Strictly preserve:

```text
One != Stable ISP;
Stable ISP != Bearer;
Stable ISP != subjecthood automatically.
```

### 6.2 `Bearer (P+E)` — Prospective Self-Exposure (`2A`)

`Bearer` retains its focused strong-bearing canonical route:

```text
formed One / Selection-position + P + E -> Bearer.
```

where:
- **`P` (prospective self-indexing)**: future branches differ by what this continuing `One` itself may undergo, preserve, lose, enable, or become unable to continue;
- **`E` (same-One prospective exposure)**: at least some such potential consequences genuinely expose that same `One` and cannot be completely outsourced while claiming the same `Bearer` relation.

External normalization never erases internal non-outsourcable breakdown. Positive independently applicable establishment of `E` remains `OPEN` (`R3-04-O3`). Strictly preserve:

```text
P alone != Bearer;  E alone != Bearer;
Bearer -/> Concern / Agency / subjecthood / cognition / phenomenality automatically.
```

### 6.3 `Agency` — Partially Orthogonal Condition-Rewriting Capacities

`Agency` is downstream and separately gated as a partially orthogonal multi-dimensional capability space (functional control / generative initiative / bearing initiative / reflexive initiative / accountability), not a single rung above `Bearer`:

```text
Agency
= a stronger Selection organization capable of participating in the rewriting
  of conditions of its own and/or relational future Selection,
  once the relevant agency burdens are independently paid.
```

Whether functional control or generative initiative requires `Bearer (P+E)` remains `OPEN` (`R3-04-O5`). `Selection-totality -/> pan-agency; Selection-totality -/> pan-consciousness`.

### 6.4 Feeling, Cognition, Consciousness, and `HP-B` Independent Boundary

Feeling is the actual unfolding and participation of the inner generative process at a cognitive position; cognition and consciousness are vertical generative organizations, not external passive readouts (`R3-03`). Yet **organizational coordination does not automatically entail phenomenality**: `Philosophy/SRT_HardProblem_Epistemology.md` (`B_s != B_p`, `HP-B OPEN`) and `Core_Law/SRT_Suffering.md §7` (neither `Stable ISP` nor architecture tiers alone close suffering qualification) remain independent boundaries.

### 6.5 Normativity Routing (`O1 / O2-C / O2-A` and `O2-M = HOLD`)

Primitive Selection carries no primitive moral content (`actual occurrence != correctness != legitimacy`; `continuation != goodness`; `more options != better`; `generative optimization != ethical legitimacy`, `PT10 E`). Because formed and relational Selection can alter the conditions under which further Selection proceeds, normativity becomes possible along four strictly typed routes:

```text
formed-position Selection          -> O1 indexed generative comparison;
relation-transforming Selection    -> O2-C constitutive relation-integrity constraints;
agency-qualified relation-rewriting -> O2-A answerability (independent of O2-M);
all-things-considered cross-position moral conflict -> O2-M = OPEN / HOLD.
```

---

## 7. `L0 / L1 / L2` Analytic Aspect Routing

`L0`, `L1`, and `L2` are **three analytic / model-facing aspects of one Selection reality**, never three ontic substances or a compulsory three-stage warehouse pipeline:

```text
L0-side = Selection in its open / non-preclosed generative aspect relative to determinate actuality;
L1-side = Selection under determinate manifestation / actuality;
L2-side = prior Selection remaining effective as retained constraint / sediment / history on later Selection.
```

Scoped formal objects named `L0`, `L1`, and `L2` remain valid inside declared domain models (owned by their formal/reference anchors) and must not back-define this metaphysical routing.

---

## 8. Positive Generative Frontiers & Facet-Before-Kind Discipline

### 8.1 Open Positive Generative Candidates (R4/R5 Research Frontiers, Non-Axiomatic)

To prevent canonical hardening from closing live generative inquiry, three AI/author-synthesized candidate mechanisms are routed here strictly as **open positive research frontiers** (not axioms, not exhaustive classifications, not proven laws):
1. **Dual-engine dimensional transition (non-exhaustive)**: (a) *orthogonalization under vertical suppression* (persistent friction drives mediation/compartmentalization/symbolic decoupling into a new low-interference dimension); (b) *surplus cross-domain discovery* (automation/backgrounding lowers maintenance opportunity cost, releasing surplus for free multi-unit comparison without crisis).
2. **Quartet co-variation (non-necessarily synchronous)**: during condition reconstruction, value metric, concern scope, friction source, and generative position may vary independently or co-vary in specific transitions.
3. **Generativity of comparison itself**: recursive condition reconstruction alters not only costs and reachable states, but the very **dimensions, scales, and objectifications** by which subsequent comparison operates (`R3-CL-O8`).

### 8.2 Facet-Before-Kind Governance Guard

Before introducing a new repo-wide ontological noun: (1) state its distinct structural burden; (2) test whether it is a mode, perspective, organization, or relation of Selection; (3) add a new ontic kind only if that reading fails under explicit argument.

---

## 9. OPEN Register (Cross-Owner)

This spine preserves all 63 deduplicated R3 `OPEN` items (`Operations/Proposals/SRT_R3_FULL_SKELETON_CLOSEOUT_GLOBAL_SUBTRACTION_2026-11-25.md` View ④) without closing any by rewording. Key cross-owner gates include:

```text
T3-01 C (global optimizing principle) vs E (global extremal principle) & relation to C-A;
anti-tautology boundary between genuine actualised Selection and merely descriptive/modelled change;
whether primitive inner generative process includes any pre-phenomenal character (R3-03-O4);
exact primitive Selection vs operator-carrier (\hat{G}_\theta) formalization;
exact L0/L1/L2 aspect-vs-domain crosswalk & kappa_0 / epsilon_pg inheritance;
formal N&S One theorem, exact boundary / unit identification, strict & branch/merge identity;
non-circular independent criteria for existence continuity vs value opportunity-change & generative normalization;
positive E establishment & Bearer <-> Concern / Agency / cognition / consciousness necessity directions;
R3-CL-O8 five independent sub-questions (freedom conditions, freedom vs strong 2nd-order selection, dual-engine transitions, quartet co-variation, recursive generation of comparison scales);
HP-B phenomenality / experiencer transition & PT07 bce undecided inclination;
O2-A exact sufficiency & O2-M cross-position moral conflict (HOLD);
cross-domain scientific distinctiveness, Level 2 / HOLD exit, and whole-architecture non-substitutability.
```

---

## 10. Citation Rule

Use this file first for:
- unified recursive generative ontology routing (`差异生成 ⇄ 差异比对与组织 ⇄ 生成条件递归重构`);
- source / theoretical extraction / global orientation coordination (`神性·源义 / 原初 Selection / 神性·倾向义 / 整体共同生成视域`);
- three recursive axes, opportunity-cost dynamic quartet boundaries, and cross-scale five-mechanism separation;
- existence vs order perspectives on `One` and cross-owner non-identities (`One != Stable ISP != Bearer (P+E) != Agency != subject/consciousness`);
- five-layer evaluative separation, normativity routing (`O1 / O2-C / O2-A / O2-M=HOLD`), and `L0/L1/L2` aspect routing.

Then follow the detailed local canonical owners:
- Primitive metaphysical floor: `Core_Law/SRT_L0_Metaphysics.md`
- `One`, existence/order perspectives, vertical reconstitution & `Selection-position`: `Core_Law/SRT_One_Formation.md`
- `Stable ISP` stronger recurrent standing: `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T06`
- `Bearer`: `formed One / Selection-position + P + E -> Bearer.`
- Value, generalized concern, `d`, `D_stake`, `D_eff`: `_SRT_D_VALUE_CANONICAL.md`
- Opportunity-cost friction, pressure/supply split & `Ψ_f`: `_SRT_PSI_F_CANONICAL.md`
- Direction transparency (`T_dir`): `_SRT_T_DIR_CANONICAL.md`
- Symbols & cross-domain usage discipline: `_SRT_SYMBOL_TABLE.md`, `_SRT_CROSS_DOMAIN_MATRIX.md`



---

## FILE: `Governance/SRT_CLAIM_LADDER.md`

| 字段 | 值 |
|---|---|
| path | `Governance/SRT_CLAIM_LADDER.md` |
| id | SRT-CLAIM-LADDER |
| claim_mode | canonical |
| status | active_v1_1 |
| epistemic_layer | os |
| layer | meta |
| canonical(字段) | - |
| last_commit | 2026-10-19 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：[SRT-CANONICAL-FREEZE, SRT-EDIT-PROTOCOL, SRT-CANONICAL-REGISTRY]

<!-- 以下为原文逐字保留 -->

# SRT Claim Ladder

> **Purpose**: This file defines proposition-level hardness. File role and claim role are related but not identical: a canonical file may contain bridge claims, and a bridge file may quote primitive axioms. The claim level must be explicit whenever hardness matters.

## 0. Core Rule

Never let a lower-hardness claim wear the voice of a higher-hardness claim.

In particular, domain files must not present P3/P4/P5 claims as if they were P0/P1.

**Claim hardness is not a research-idea admission score (2026-10-18 clarification).** P-levels determine what may be asserted, cited or promoted at a given evidence/authority strength. They do not determine whether an author-origin question or marked AI-origin candidate may be formulated, explored or retained. A candidate may challenge a current P0/P1 or K commitment without being represented as accepted doctrine; any actual promotion, replacement or publication still follows owner, author and evidence gates.

---

## 0A. Gate 0 — L₀ Contentless Structurality Boundary

> **Status**: governance-canonical **type / boundary rule**. Adopted 2026-08-11.
> **This file is the single primary authority for Gate 0.** `_SRT_SYMBOL_TABLE.md` Usage Rule 16 is a cross-reference for symbol users and does not restate the rule's content.
> **Gate 0 carries no P-level.** It is **not** a P0 axiom, **not** a P1 theorem, **not** a physics claim, and **not** a new ontological quantity. §0 governs the *hardness* a claim may wear; §0A governs the *kind* of object that may sit at L₀. The two are orthogonal.
> **Adjudication record**: `Operations/Proposals/SRT_GATE0_L0_CONTENTLESS_STRUCTURALITY_DECISION_2026-08-11.md`.
> **2026-09-15 Selection-totality override**: Gate 0 governs admissibility and typing; it does not independently define primitive ontology. Primitive / L0-side burdens are supplied by the current L0 owner and Generative Ontology Spine.

### The rule

**A primitive / L0-side claim may carry only contentless structural burdens already licensed by the current L0 / Spine owners.** A contentful direction, goal, optimum, value or semantic order is not primitive merely because it can be written globally; neither does contentlessness alone promote a formal object to primitive status.

```text
L0-side != pregiven possibility warehouse;
primitive Selection != operator acting on a prior inventory.
```

### The three classes

| Class | Nature | Members currently admitted / named | Admission at bare L₀ |
|---|---|---|---|
| **A** | already-owner-licensed contentless structural burden | non-maximal indifference / minimum non-flatness · openness not exhausted or fully preclosed by completed determinate actuality · finite positional indexing without a prior formed operator / subject | **allowed only at current owner strength** |
| **B** | reference-, model-, realization- or derivation-dependent candidate | probability measure / prior · entropy over a declared state space · reachability / accessibility ordering · `κ₀` anisotropy · `ε_pg` · `B >= 2` vs `B <= 1` option-count preference · any formal cost, gradient or direction requiring a model, reference structure or stronger realization | **admission gap** — see below |
| **C** | semantic / evaluative / contentful | semantic target · good / value · telos · 「order」 as content · 初心 as a global contentful direction · universe-wide preferred world-state · global semantic or evaluative optimum | **not admissible as a bare L₀ primitive** |

**Class A is open, not closed.** Its examples summarize current L0 / Spine owner commitments; Gate 0 does not make them independent new primitives, does not assert that they are jointly complete or irreducible, and cannot promote a future invariant without its own owner-level admission.

**Class B is an admission gap, not a prohibition in kind.** The rule is:

> Current core does not license such an object unless its required reference structure is **stated or independently derived**.

This must **not** be written as "L₀ forbids a natural measure" or "κ₀ / ε_pg are impossible." They are not primitive by inheritance from O0; their exact relation to primitive non-flatness remains OPEN unless separately adjudicated and re-established. Gate 0's function is to stop global or contentless notation from hiding a missing commitment.

### Ordering discipline

```text
structural ordering in a declared model != primitive value ranking;
structural ordering in a declared model != preferred endpoint / telos;
formal anisotropy does not inherit primitive status merely because it is contentless;
option-count preservation is not the primitive direction of Selection.
```

In particular, Gate 0 does not establish a primitive two-class preference of `B >= 2` over `B <= 1`.

### Declaration requirement for situated / contentful objects

A situated or contentful object must **declare the reference structures its content actually depends on**.

Required **conditionally, when and only when the construct depends on them**:

- a declared formed position, relation or operator interface;
- a declared admissible or reachable domain when comparison requires one;
- historical constraints — only when the object is history-dependent;
- a probability measure — only when probability or entropy is used;
- a payability / reachability horizon — when claiming reachable- or accessibility-relative quantities;
- any other index the construct depends on.

These are **typing / admission requirements, not a sufficient construction recipe.** Satisfying them makes an object well-posed; it does not make any particular content correct. A prior finite formed operator is not universally required, because primitive Selection is not already a chooser entity. History is likewise not universally required: a first situated manifestation may arise before any `L_2` historical sediment exists (`Core_Law/SRT_L0_Metaphysics.md` Ax-L0-Bootstrap; `Core/SRT_Core_12a` T-L0-Kappa0).

### Read-back rule

「order」, 「初心 / original intention」, 「good」, and situated convergence / direction language may exist as **L₁/P2 read-back, regulative language, or domain bridge** — but may not back-define primitive Selection or L0-side openness. `ε_pg` may remain lineage / stronger-realization material; it does not currently name the primitive direction of Selection or O0. Current canonical does not admit an independent L₀「初心前身」; 初心 begins from L₁ read-back.

### C-A — `global optimum` scope discipline

> **Status**: author-decided and landed 2026-08-12. Adjudication／floor record: `Operations/SRT_GLOBAL_OPTIMUM_AUTHOR_DECISION_PACKET_2026-08-12.md`.

C-A adds no L₀ object and no symbol. It separates four objects that previously shared one name:

1. A **universe-wide semantic／evaluative optimum** is not a current positive SRT object. It may remain only as historical provenance, quotation, or an explicitly unestablished high-commitment worldview claim; it may not carry canonical proof load.
2. An **operator-relative reachable optimum** is admissible only as a situated P2/P3 object with the finite position, reachable／admissible domain, comparison rule, horizon, constraints, and relevant failure conditions stated.
3. A **regulative horizon** is non-attainable L₁/P2 or P5 orientation language. It is not a formula endpoint, achieved state, or L₀ object.
4. A **closure／model attractor** is a P3/P4 object of a named finite dynamics. Stability, low friction, or reachability does not by itself make it optimal, good, or generatively healthy.

Technical uses of “global optimum” inside a fully declared optimization problem remain allowed; C-A blocks the slide from **model-global** to **universe-global／normatively complete**. `d ↑` alone entails neither a reachable optimum nor Shoshin alignment. The separate Core／Spirituality `Ψ_f → 0` valence question remains open under the CΨ author gate and is not decided by C-A.

**"Back-define" includes the indirect route**: a canonical anchor may not import an L₀-level reading of these terms by cross-referencing a `canonical: false` bridge or translation file. **Direction of citation is part of this rule**, not a separate courtesy.

### What Gate 0 does not do

Gate 0 本身没有裁决 Gate A、Gate B 或 Gate C（`Core/SRT_OPEN_TENSIONS.md §15 / §16 / §17`），只约束了它们的选项空间。后续作者裁决已分别以 EX-A 关闭 Gate A、以 B-A 关闭 Gate B、以 C-A 关闭 Gate C；`Core/SRT_OPEN_TENSIONS.md §18` 的 CΨ 仍为独立开放作者门。

Gate 0 does not settle `κ₀` / `ε_pg` necessity or inheritance, does not supply a primitive value direction, and does not make `T_dir`'s reference direction primitive. It does not resolve O1 / O2-C / O2-A, and O2-M remains outside this rule and OPEN. It remains neutral among positions in `Philosophy/SRT_L0_Ontological_Status.md` because it governs typing, not mode of existence. It introduces no symbol.

---

## 1. Claim Levels

| Level | Name | Definition | Allowed Voice |
|---:|---|---|---|
| P0 | Primitive axiom | A minimal SRT axiom without which the core grammar fails. It does not depend on a domain bridge, empirical threshold, or external theory. | "SRT assumes..."; "Within SRT, this is primitive..."; "Without this, the framework does not stand..." |
| P1 | Constitutive theorem | A claim treated as following from the SRT core structure. It is not primitive, but it is internally constitutive once P0 is granted. | "SRT entails..."; "Constitutively..."; "Given the core axioms..." |
| P2 | Canonical interpretation | A stable interpretive reading used across SRT, but not a primitive or theorem. It organizes meaning and usage. | "SRT reads this as..."; "Canonical interpretation..."; "Use this as the default reading..." |
| P3 | Bridge mapping | A mapping between SRT and another theory, domain, model, or scale. It may be useful and strong, but it depends on an interface. | "maps to..."; "can be modeled as..."; "bridge claim..."; "under this mapping..." |
| P4 | Lab hypothesis | A testable, measurable, empirical, or threshold-bearing claim. It may generate predictions or operational proxies. | "hypothesis..."; "candidate proxy..."; "to be tested..."; "under these measurement conditions..." |
| P5 | Phenomenological / companion exposition | A lived, pedagogical, literary, praxis, or companion explanation. It may be valuable but does not bear core-theory proof load. | "as exposition..."; "phenomenologically..."; "companion reading..."; "helps describe..." |

### 1A. P0 / Empirical Discrimination Boundary — PD-A (2026-08-17)

A `P0` primitive is an explicit constitutive starting commitment of SRT. **Direct D2/D3 rival discrimination is not an admission condition for P0.** Requiring a primitive axiom to depend on an empirical threshold or external rival would contradict the P0 definition above.

This separation has four consequences:

1. **P0 is not empirical proof.** `SRT assumes X as primitive` must never be rewritten as `experiments prove X is ontologically primitive`.
2. **Scientific distinctiveness must be paid downstream.** Any claim that SRT is empirically or scientifically discriminative must be carried by a P3/P4 bridge or lab hypothesis that freezes a bounded rival and produces prospective `D2` (`O_SRT != O_R`) or `D3` preregistered empirical discrimination.
3. **A downstream D2 does not directly prove the primitive ontology.** One D2-positive workline supports the empirical fruitfulness of that specific derivation / workline and counts as one architecture-fruitfulness exhibit; it does **not** by itself license architecture-wide empirical superiority.
4. **Persistent empirical underdetermination limits scientific claims, not automatically P0 membership.** If mature P3/P4 bridges repeatedly fail to produce D2, SRT must say that its Selection-first ontology remains empirically underdetermined relative to the tested rivals. P0 may still be reassessed for redundancy, incoherence, lack of derivational fruitfulness, or by a later author architecture decision, but `D2 = 0` alone is not a mechanical demotion rule.

**PD-A governance trigger (not a statistical confidence threshold).** A workline counts as `mature` for this trigger only if it freezes, before outcome inspection: an independently motivated middle-level consequence, a bounded rival state/update/calibration family, a common intervention and observable, symmetric failure criteria, and a terminal disposition (`spec-stage NO-GO`, executed D2-negative/rival-equivalent, or D2-positive). Mere dataset swaps or rephrasings of the same derivation do not count as independent worklines.

- **Negative trigger**: after **3 independent mature worklines** spanning at least **2 distinct middle-level consequences** end D2-negative / rival-equivalent, `Core/SRT_OPEN_TENSIONS.md §13` must open a P0-01 fruitfulness / redundancy review **before a fourth substantially similar mature workline is authorized**. The review owner is §13; any P0 change remains author-gated.
- **Positive attribution rule**: architecture-level empirical-fruitfulness language requires at least **2 independent D2-positive worklines grounded in distinct middle-level consequences**. A single positive remains local to its derivation / workline.
- Historical A2 / P24 NO-GO results inform the review but are **not automatically back-counted** under this trigger because they were not all frozen under the PD-A maturity contract. The qualifying count at PD-A adoption is therefore `0`.

Decision record: `Operations/SRT_PD_A_P0_D2_BOUNDARY_AUTHOR_DECISION_PACKET_2026-08-17.md`.

Therefore the correct research sequence is:

```text
P0 primitive commitment
-> P1 internal consequences
-> P2/P3 operational or domain structure
-> P4 measurable prediction
-> D2/D3 rival discrimination
```

Do not reverse this arrow by using a downstream proxy as the definition or proof of the P0 primitive.

---

## 2. Relation to File Roles

File roles and claim levels do not automatically determine each other.

| File role | Typical claim levels | Rule |
|---|---|---|
| canonical | P0-P2, with occasional marked P3/P4 | Must mark mixed lower-hardness claims clearly |
| compact core | P1-P3 | May summarize P0/P1 but should link to canonical sources |
| bridge | P2-P4 | Must not silently upgrade mappings into axioms |
| lab | P4 | Must keep measurement/proxy conditions visible |
| navigation / registry / index | usually no substantive claim level | Should route to sources, not define theory |
| companion / praxis / public exposition | P5 plus quoted P0-P2 | Must distinguish explanation from definition |

The same file may mix P-levels. If it does, mark the level at least at section level. Inline marking is preferred for high-risk statements.

---

## 2A. `claim_mode: manifesto`

A `manifesto` claim mode authorizes worldview-level rhetorical compression while keeping the claim ladder load-bearing. It exists so that SRT can have a public-facing front-edge document without inviting silent P3-as-P0 inflation.

**Scope**: applies to files under `Manifesto/` and to any first-screen reference block in `README.md` that quotes a manifesto center sentence.

**Allowed**:

- Restate already-canonical P0/P1/P2 claims in slogan, compressed, or metaphorical form.
- Place P0 (hard) and P3 (bridge) claims in the same paragraph or center sentence, **provided the paragraph itself carries inline claim-level tags distinguishing them**.
- Bilingual parallel passages (e.g., Chinese + English) where the non-Chinese line is a rhetorical mirror, not an independent assertion.

**Forbidden**:

- Introducing any new P0 or P1 claim. New claims must first pass through `Core/`, `Core_Law/`, or `Governance/` promotion before a manifesto may quote them.
- Hiding P3/P4 hardness behind P0-style phrasing. Bridge claims must remain bridge claims even in slogan form.
- Coining new symbols, operators, or domain names. Manifestos only reference symbols already registered in `_SRT_SYMBOL_TABLE.md`.
- Single-file deferred footers as a substitute for inline tagging.

**Inline tag rule**:

- Every reversal proposition, center sentence, and free-standing assertion paragraph must carry an inline claim tag in `[P0-XX]` / `[P1, canonical]` / `[P2, canonical]` / `[P3, bridge]` / `[P3, conjectural]` / `[P4, speculative]` / `[P5, exposition]` form.
- Tags must appear in the same line or paragraph as the claim, not in a separate footnote section.
- When a center sentence compresses (a) P0 + (b) P3, the two halves must be sub-labeled `(a)` and `(b)` and tagged separately at least once in the file.

**Frontmatter requirement**:

A manifesto-mode file's YAML frontmatter must include:

- `claim_mode: manifesto`
- `audience: human_public`
- `manifesto_version: vX.Y`
- `anchored_claims:` — explicit list of canonical anchor IDs (e.g., `P0-01`, `P3-B07`, `PSI-F-CANONICAL`) the manifesto draws from
- `last_review: YYYY-MM-DD`
- `review_window_until: YYYY-MM-DD` — date for the next mandated reception review

**Versioning and trace**:

Any change to a manifesto's center sentence (Layer A / Layer B / Layer C) must be logged as a separate `Operations/` entry on the day of the change.

**AI session boundary**:

Manifesto files are human-first entries. They are **not** part of the AI session bootstrap defined in `AGENTS.md §Session Start`. AI agents read manifesto material only when the task involves user-facing framing.

**Relation to existing modes**:

- `claim_mode: manifesto` is rhetorically less constrained than `canonical` but governance-wise more constrained than `mixed`: it authorizes compression in exchange for mandatory inline tagging.
- It does not grant manifestos any authority over canonical files. Canonical files always outrank manifesto restatements.

---

## 3. Level-Specific Tests

### P0 Test

A statement can be P0 only if:

1. Removing it breaks SRT's core grammar.
2. It does not require empirical data to become meaningful.
3. It does not borrow authority from another theory.
4. It is not more cleanly derivable from other SRT claims.

Failure of any condition means demote.

### P1 Test

A statement can be P1 only if:

1. Its premises are already P0 or accepted P1.
2. The derivation path is stated or obvious from the formal context.
3. Its negation would break the SRT structure or carry a high internal contradiction cost.

If it depends on a domain mapping or threshold, it is not P1.

### P2 Test

A statement can be P2 when:

1. SRT repeatedly uses it as a stable interpretation.
2. It clarifies the meaning of core terms.
3. It does not by itself claim external validation.

P2 may be canonical in practice without becoming P0/P1.

### P3 Test

A statement is P3 when it says that an SRT structure maps onto another theory, domain, or scale.

Typical markers:

- "physics-scale realization"
- "AI analogue"
- "neuroscience implementation"
- "Fisher / information-theory expression"
- "spirituality / praxis reading"

P3 can be strong. It is still not a primitive axiom.

### P4 Test

A statement is P4 when it involves:

- thresholds
- empirical proxies
- measurable predictions
- falsification conditions
- operational criteria
- lab or field validation

P4 should name its measurement boundary whenever possible.

### P5 Test

A statement is P5 when its main function is:

- human orientation
- lived description
- metaphor
- companion exposition
- practice guidance
- pedagogical compression

P5 may be important for understanding, but it cannot carry proof load.

---

## 4. Mixed Files

A file may contain different P-levels if one of the following is true:

1. The frontmatter declares `claim_mode: mixed`.
2. The file has a claim-level map near the top.
3. Each major section marks its level.

Recommended section prefix:

- `P0-Ax`
- `P1-T`
- `P2-Interp`
- `P3-Bridge`
- `P4-Hyp`
- `P5-Companion`

For older files, a short header block is enough:

```md
> Claim-level note: this file is mainly P3 bridge. It quotes P0/P1 claims but does not define them.
```

---

## 5. Promotion and Demotion

### Promotion

A claim may be promoted only when the missing support is explicit:

- P4 -> P3: empirical proxy becomes a stable bridge mapping.
- P3 -> P2: mapping becomes a stable SRT interpretation not dependent on the external domain.
- P2 -> P1: interpretation is shown to follow from the core structure.
- P1 -> P0: only in rare cases where the theorem is discovered to be primitive and non-derivable.

Promotions touching P0/P1 must cross-check:

1. `_SRT_SYMBOL_TABLE.md`
2. `CANONICAL_REGISTRY.md`
3. the relevant core/canonical file

### Demotion

Demotion is not deletion. It means:

- the claim remains available;
- its proof burden is lowered;
- its voice becomes more honest;
- domain files lose permission to quote it as primitive.

This is the default response to ambiguity **in the claim's asserted level**; where warranted, demotion also requires narrowing the actual proposition to a supported scope. For a substantive demotion/revision, distinguish (a) wrong or unsupported asserted force, (b) warranted evidence-scoped correction including genuine semantic narrowing, and (c) an independently viable question or candidate relation that remains exploratory. Preserve the original proposition and its provenance where relevant; do not convert lack of verification into disproof, or a local no-increment result into global deletion. Do not retain a disproven proposition as if it were still established.

---

## 6. Domain Rule

Domain files may support, test, interpret, or expose SRT. They may not reverse-define the SRT core.

Minimum header for domain main files:

```md
> Role: [bridge / companion / praxis / domain exposition]
> Claim level: mainly P3/P4/P5, with explicit back-links to P0/P1 sources.
> Does not define: primitive axioms, d-value, Ψ_f, T_dir, L0/L1/L2, or real choice moment.
> Depends on: [canonical files]
```

If a domain file needs a new P0/P1 claim, it must be moved or mirrored into the appropriate core/canonical file through the edit protocol.

---

## 7. Citation Rules

When citing a claim:

- Cite P0/P1 claims from core/canonical files.
- Cite P2 interpretations with the phrase "canonical interpretation" when hardness matters.
- Cite P3 mappings with the phrase "bridge" or "mapping."
- Cite P4 claims with the phrase "hypothesis," "proxy," or "candidate criterion."
- Cite P5 material as exposition, not evidence.

Forbidden citation pattern:

> "Because the AI file says X, SRT's primitive axiom is X."

Allowed citation pattern:

> "The AI file uses X as a P3 bridge mapping back to the P0/P1 core in..."

---

## 8. Current Immediate Application

`Core/SRT_Core_21_Formal_Axioms.md` has been split into:

- `Core/SRT_Core_21_Minimal_Axioms.md` — P0
- `Core/SRT_Core_21b_Constitutive_Theorems.md` — P1
- `Core/SRT_Core_21c_Bridge_Hypotheses.md` — P2/P3/P4

This split changes epistemic placement, not the underlying intended theory.



---

## FILE: `Governance/SRT_CLAIM_MODE_AUDIT.md`

| 字段 | 值 |
|---|---|
| path | `Governance/SRT_CLAIM_MODE_AUDIT.md` |
| id | SRT-CLAIM-MODE-AUDIT |
| claim_mode | governance |
| status | active_ledger_v1 |
| epistemic_layer | os |
| layer | meta |
| canonical(字段) | false |
| last_commit | 2026-09-19 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：[SRT-CLAIM-LADDER, SRT-EDIT-PROTOCOL, SRT-CANONICAL-REGISTRY, SRT-CROSS-DOMAIN-MATRIX]

<!-- 以下为原文逐字保留 -->

# SRT Claim-Mode Audit

> **Role**: first-pass governance ledger for claim-mode hardening. This file records downgrades and exposure controls; it does not create new theory or promote any claim.
> **2026-06-05 note**: this is a dated ledger, not a full current repository state. Use it as historical claim-mode evidence and pair it with current canonical anchors when exact authority matters.
> **2026-09-19 authority sync**: rows explicitly synchronized below mirror the current local owners after PR #976. This audit may record owner standing; it may not restore a harder level than the owner. Unrelated historical rows retain their dated-ledger role.

## 1. Scan Scope

Full-repo markdown scan on 2026-04-22 found approximately:

| Label family | Occurrences | Files containing any scanned label |
|---|---:|---:|
| `T-*` | 1887 | 209 |
| `Ax-*` | 2803 | 209 |
| `H-*` | 603 | 209 |

This round does **not** claim to finish all historical label cleanup. It handles only high-leverage, low-risk demotions and adds guardrails where old labels remain for compatibility.

## 2. Demotion Decisions

| Old label / phrase | New label / status | Level | Action |
|---|---|---|---|
| `T-Phys-2` | `H-Phys-2` | hypothesis / bridge | Demote discrete-time claim from theorem voice to candidate bridge reading. |
| `T-Phys-4` | `H-Phys-4` | hypothesis / bridge | Demote gravity-friction claim from theorem voice to weak compatibility hypothesis. |
| `Ax-NEURO-4b` | `H-NEURO-4b` | hypothesis / operational proxy | Demote prediction-error friction mapping to P3/P4 candidate. |
| “不可言说性定理” / `T-Phil-1` where used as theorem of principle | `H-Phil-Ineffability` | hypothesis / bridge | Demote from theorem voice to dimensional-mismatch hypothesis with counterexample slots. |
| `Ax-Spirit-*` domain theology / praxis mappings | `H-Spirit-*` in active spirituality bridge files | bridge / hypothesis / companion | Demote obvious spiritual bridge labels that were historically written as axioms. |

## 3. Quick Rationale

| Claim | Can it be derived from L0/L1 alone? | Current honest status |
|---|---|---|
| `H-Phys-2` | No; depends on physical time interpretation and possible QG bridges. | P3/P4 candidate. |
| `H-Phys-4` | No; tensor-level GR reconstruction is missing. | P3/P4 weak compatibility hypothesis. |
| `H-NEURO-4b` | No; depends on measurable PE / metabolic coupling. | P3/P4 operational proxy. |
| `H-Phil-Ineffability` | Not as a theorem; depends on language capacity and dimensional assumptions. | P3 hypothesis with explicit escape routes. |
| `H-Spirit-*` | No; theology and praxis mappings do not define core necessity. | P3/P5 bridge / companion material. |

## 4. Downstream Reminder Rule

Any downstream conclusion that relies on a demoted item must add a level reminder in the nearest relevant section:

> **Level reminder**: this conclusion depends on a demoted bridge / hypothesis. It may guide interpretation or testing, but cannot be cited as a P0/P1 theorem.

## 5. Open Audit Debt

- Many older files still use `Theorem` and `Axiom` in historical or domain-local senses.
- Split / annex files mirror old labels and were not globally rewritten in this round.
- Generated / public / video material contains stronger rhetorical versions; those require a separate public-surface cleanup pass.
- **Superseded status note（2026-08-11）**：AM-A now treats P0-01/P0-04 as the declared primitive actualisation boundary. No derivation theorem has been added; the remaining open burden concerns plural domain realization and selector individuation, not an internal promise to derive the primitive from a prior non-selective ground.

## 6. 2026-04-24 Round: New L1 Canonical Files Audit

本轮 2026-04-24 引入 six L1 theory/formalism canonical reference files。本小节固定它们的 claim-mode 分布，防止将来被误读成 P0/P1。`SRT_L1_Hardening_Notes.md` 为 this L1 round 的 hardening notes file，单列于下方 hardening notes table；因此 this L1 round 的 `Core_Law/` 相关文件总数为 seven（six L1 reference files + one hardening notes file）。`SRT_Collective_Tower_Hardening_Notes.md` 是后续结构抽取出的 secondary hardening notes file，不计入 six L1 reference files，也不改变 this L1 round 的七文件计数。

### 6.1 Scope of New Files

| File | id | status | Nominal Level Range |
|---|---|---|---|
| `Core_Law/SRT_Individuation.md` | `SRT-INDIVIDUATION` | draft_v0 | P1-candidate / P2 / P3-P4 |
| `Core_Law/SRT_Occlusion_Dynamics.md` | `SRT-OCCLUSION-DYNAMICS` | draft_v0 | P1-candidate / P2 / P3-P4 |
| `Core_Law/SRT_Suffering.md` | `SRT-SUFFERING` | draft_v0 | P1-candidate / P2 / P3-P4 |
| `Core_Law/SRT_L1_Formalism.md` | `SRT-L1-FORMALISM` | draft_v0 | P1-candidate / P2-P3 |
| `Core_Law/SRT_Collective_Selection.md` | `SRT-COLLECTIVE-SELECTION` | draft_v0 | P1-candidate / P2 / P3-P4 |
| `Core_Law/SRT_Irreversibility.md` | `SRT-IRREVERSIBILITY` | draft_v0 | P1-candidate / P2 / P3（FEP/热力学桥接 guardrail） |

**当前约束**：上表是 2026-04-24 文件引入记录，不再统括决定六份 owner 的当前 claim level。精确引用必须以当前 local owner 为准；本节下方已同步的 T-IND-2、T-SUFF-1/2/4 与 Def/T-IRR 条目不得被上表的历史 nominal range 升格。

Hardening notes files outside the six L1 theory/formalism canonical reference files:

| File | id | status | Role |
|---|---|---|---|
| `Core_Law/SRT_L1_Hardening_Notes.md` | `SRT-L1-HARDENING-NOTES` | draft_v0 | this L1 round hardening notes file |
| `Core_Law/SRT_Collective_Tower_Hardening_Notes.md` | `SRT-COLLECTIVE-TOWER-HARDENING-NOTES` | draft_v0 | secondary late-stage tower/nested hardening notes; not minimal canonical definition |

### 6.2 Per-File Claim-Level Map

#### SRT-INDIVIDUATION

| Label | Statement | Level |
|---|---|---|
| Def-σ | 自指率 `σ := ‖θ^{trace}‖ / (‖θ^{trace}‖ + ‖θ^{ext}‖)` | Def, P1-candidate as operational proxy |
| T-IND-1 | 个体化作为相变 | P1-candidate |
| T-IND-2 | 已声明模型中的 subject-position 候选转变坐标；跨越只是 model-local evidence，不是 subjecthood / ISP admission | P3/P4 model-coordinate claim |
| T-IND-3 | 第二相变（自我意识凝结）条件 | P2（结构性假说） |
| σ_sub, σ_self, σ_health 具体数值 / 阈值 | — | P3/P4（未实测，不得引用为定值） |
| 自我意识 = 关于 θ 的 θ 二阶写回 | — | P2 canonical interpretation |

**Downstream rule**：T-IND-1 仍按其当前 owner standing 引用；T-IND-2 只得标为 `P3/P4 model-coordinate evidence`，不得当作 subject-position 或 ISP 的必要／充分准入条件；T-IND-3 须标 `P2`；任何具体阈值须标 `P3/P4 pending`。

#### SRT-OCCLUSION-DYNAMICS

| Label | Statement | Level |
|---|---|---|
| T-OCC-1 | 三段结构（healthy narrow / A-phase / B-phase）由 `d_c, d_{narrow}` 分开 | P1-candidate |
| 位置性遮蔽 vs 病理性遮蔽区分 | — | P2 canonical interpretation |
| 五类缺口感知残余类型 | — | P2（结构性分型） |
| 四类干预窗口 | — | P2 |
| 四类解耦触发 | — | P2 |
| 真空期 | — | P2 |
| 恶的三判据结构性定义 | — | P2 regulative reading，不替代规范性伦理学 |
| `d_c` 具体数值 / 临床阈值 | — | P3/P4 |

**Downstream rule**：T-OCC-1 须标 `P1-candidate`；分型与判据须标 `P2`；恶的三判据不得升格为 P0/P1 规范理论。

#### SRT-SUFFERING

| Label | Statement | Level |
|---|---|---|
| Def-PAIN | 疼痛作为 `\theta_{somatic}` 信号 | Def |
| Def-SUFFERING | 苦难作为稳定 ISP 的结构性登记 | Def, P1-candidate as operational proxy |
| T-SUFF-1 | 在独立 first-person registration admission 与声明模型下组织 registered suffering 候选证据 | P2 structural / phenomenology model candidate；非充要定理 |
| T-SUFF-2 | 在 suffering 已独立准入后的 signal-type / structural-type 模型分类 | P2/P3 model taxonomy；非 universal phase theorem |
| T-SUFF-3 | 四类现象学（张力 / 空心 / 断裂 / 扭曲） | P2 |
| T-SUFF-4 | 仅降低报告信号不足以证明 underlying modeled burden 已消除 | P2 anti-signal-suppression sufficiency guard；不产生普遍伦理定理 |
| T-SUFF-5 | 集体外部化 → 结构性恶耦合 | P2 |
| `[S_{min}, S_{max}]` 阈值 | — | P3/P4 |
| FEP / prediction error 作为 `Δ` 的神经代理 | — | P3 bridge hypothesis，不得反向定义苦难 |

**Downstream rule**：T-SUFF-1 须标 `P2 model candidate`并保留独立 registration/admission；T-SUFF-2 须标 `P2/P3 model taxonomy`；T-SUFF-4 须标 `P2 sufficiency guard`。三者都不得按旧 `P1-candidate` 充要定理或规范定理引用。T-SUFF-3/5 须标 `P2`；AI 苦难判断严格走 `AI_POSITIONING_NOTE.md` stake-bearing 光谱，不得一侧先验判定。

#### SRT-L1-FORMALISM

| Label | Statement | Level |
|---|---|---|
| §2 σ 最小动力学（logistic + χ 跳跃） | — | P1-candidate 结构形式；具体函数族普适性由 §2.5 T-CHI-1 升 P1-candidate（H8） |
| §2.5 T-CHI-1 χ 跳跃函数族普适性（H8，2026-04-25） | "有效二阶相变核"四条结构属性 + 族内四个不变量（双稳态 / 病理吸引子 / 致命 `L_2` / 相变方向） | P1-candidate（χ 形式无关性升为定理后果） |
| §3 d_c 漂移方程 | — | P1-candidate 结构形式；系数 P2/P3 |
| §3.4 T_{dir}^{alg} 代数目标值 | — | P2 operational proxy（`\Theta` 光滑族留作 Open Pressure） |
| §3.5 T_dir 独立 ODE（弛豫 + ΔΨ_f^gap 扣除 + S_str 侵蚀 + s_ext 支架） | — | P1-candidate 结构形式；former-P1-T05-derived `r(t)` pump 已由 RC-A subtractive probe 删除；其余 κ_* 系数 P2/P3 |
| §3.5.3 致命 `L_2` 方程化判据 `\kappa_{\mathrm{mask}} < \kappa_{\mathrm{relax}}` | — | P1-candidate（本轮新增；与 `_SRT_T_DIR_CANONICAL §5-§6` 现象学层面一致） |
| §4 S 两型耦合方程 | — | P1-candidate 结构形式 |
| §4.4 反最小化原则的方程语言 | — | P1-candidate（T-SUFF-4 的方程化同级） |
| §4.5 T-CHANNEL-1 通道指示函数族普适性（H9，2026-04-25） | "有效闭合通道指示族"四条结构属性 + 族内五个不变量（两型分裂 / 反最小化 / 单向性 / 致命 L_2 / 投影一致性，均 modulo `O(w_{tr})`） | P1-candidate（硬指示 → 光滑族升为族内不变量定理） |
| §5 病理吸引子 `\mathcal{A}_{path}` | — | P1-candidate |
| §5 健康工作区 `\mathcal{H}` 须主动维持 | — | P2/P3 generative-reselectability implementation candidate under ST-A；不再以 P1-T07 必要性背书 |
| Former §5.1 第 6 条"苦难-可读性正反馈环"（`S_{str} \to T_{dir} \downarrow \to r \downarrow \to S_{sig}`） | — | RC-A 已删除该 former-P1-T05-derived feedback path；不再列为当前 P1-candidate 通道 |
| §6 T-PROJ-1 主方程投影定理（H5，2026-04-25） | 四个标量泛函投影 `\mathcal{F}_X` + 闭包假设 C1-C4 + 证明骨架 + source-by-source 对应表 | P1-candidate（"四变量是主方程导出"从陈述升为带条件证明的形式定理） |
| 全部参数 `α, β, γ, μ, ν, λ, κ` | — | P3/P4，任何具体值不得在下游引用为已证 |

**Downstream rule**：方程结构可按 `P1-candidate` 引用；T-PROJ-1 投影对应可按 `P1-candidate` 引用，但 C1-C4 闭包假设须保留显式标注（任何应用文件不得静默移除闭包条件）；参数值、数值求解结果、曲线拟合结果一律按 `P3/P4 pending` 引用；任何将方程读成"已经过实证的定量定律"的下游使用为误用。

#### SRT-COLLECTIVE-SELECTION

| Label | Statement | Level |
|---|---|---|
| Def-C-1 多 ISP 共享 L_2 场 | — | Def |
| Def-C-2 后果回路矩阵 `M(t)` | — | Def / P2（具体可测性未解决） |
| Def-C-3 共享选择空间 `A_{\mathcal{P}}` | — | Def |
| T-COLL-1 集体 ISP 存在四条件 | — | P1-candidate（P1-T06 集体版的对应） |
| T-COLL-2 三类退化（聚合 / 主从 / 收编） | — | P2 |
| T-COLL-3 条件性集体反闭合候选 | neutral kernel + stability semantics + environment/horizon + absorption/comparative-risk proof required | P2/P3 conditional candidate under ST-A；非 P1 theorem |
| T-COLL-4 collective agency / revision guard | — | P2/P3 downstream guard under RC-A；不是 P1-T05 集体版，也不是 Selection occurrence / T-COLL-1 的必要条件 |
| §4 `σ^{coll}` / `d_c^{coll}` 耦合 | — | P2 |
| §4.4.1 集体场定义（`\Theta^{coll,trace}` / `\Theta^{coll,ext}` 含共享 `L_2` 独立项） | — | P2 structural；权重 `w_i(t)` 依赖 M(t) 可测性（P3） |
| §4.4.2 σ^{coll} ODE（含 `\lambda_M\,\mathrm{tr}\,M` 内向后果放大项） | — | P1-candidate 结构形式；`\lambda_M` P2/P3 |
| §4.4.3 d_c^{coll} ODE（含 `\gamma_{asym}\|M_{asym}\|` 主从型形式化） | — | P1-candidate 结构形式；`\gamma_{asym}` P2/P3 |
| §4.4.4 T_{dir}^{coll} ODE + 集体层致命 `L_2` 判据 `\kappa_{mask}^{coll} < \kappa_{\mathrm{relax}}^{coll}` | — | P1-candidate 结构形式；RC-A 已删除 former-P1-T05-derived `r^{coll}` pump；其余 κ_*^{coll} 系数 P2/P3 |
| §4.4.5 S^{coll} 两型 ODE（含 `\nu_{ext}\|M_{ext}\|` 外部化项，T-SUFF-5 方程化） | — | P1-candidate 结构形式；`\nu_{ext}` P2/P3 |
| §4.5 个体↔集体双向耦合三路径 | — | P1-candidate（声明"不穷尽"） |
| §4.6 集体病理吸引子 `\mathcal{A}_{path}^{coll}` / 集体健康区 `\mathcal{H}^{coll}` | — | P1-candidate / P2-P3 mixed；RC-A 已删除 `r^{coll} > r^{coll}_{min}` 硬条件，generative-health / revision standing 不与 T-COLL-1 混写 |
| §4.7 T-PROJ-1^{coll} 集体投影定理（H6，2026-04-25） | 四个集体标量泛函投影 `\mathcal{F}_X^{coll}` + 闭包假设 C1^{coll}-C5^{coll}（含 `M(t)` 可测性 MOC 闭包 C5^{coll}）+ `M(t)` 三成分作为 `\Psi_f` 交叉项的结构投影 + 证明骨架 | P1-candidate（"集体四变量是多算子主方程导出"从陈述升为带条件证明的形式定理） |
| §4.8 late-stage tower/nested hardening pointer | H10-H16 tower/nested material has been extracted to `Core_Law/SRT_Collective_Tower_Hardening_Notes.md` | Pointer only; not part of the minimal canonical definition of collective selection |
| §8 平台 / 算法 AI 结构性影响评估 | — | P3 bridge |

**Tower / nested scope note**：H10-H16 are late-stage tower/nested hardening notes extracted to `Core_Law/SRT_Collective_Tower_Hardening_Notes.md`, not part of the minimal canonical definition of collective selection. They remain P1-candidate only under strong closure assumptions and should not be cited as closed P1.

**Downstream rule**：T-COLL-1 须标 `P1-candidate`；T-COLL-3 / T-COLL-4 须标 `P2/P3 downstream`；三类退化的判据须标 `P2`；T-PROJ-1^{coll} 投影对应可按 `P1-candidate` 引用，但 C1^{coll}-C5^{coll} 闭包假设须保留显式标注（特别是 C5^{coll} `M(t)` 可测性 MOC 仍是 P2 operational proxy；任何应用文件不得静默移除该闭包条件）；H10-H16 不得作为 minimal canonical definitions 引用；政治 / 经济 / 制度判断仍走 `Philosophy/*` P2-P4。投票 / 共识 / 专家决定本身既不证明更强 collective agency，也不得反推“没有 Selection”；若审计 consequence-sensitive revision，只能把降级后的 T-COLL-4 当 P2/P3 input。

#### SRT-COLLECTIVE-TOWER-HARDENING-NOTES

| Label | Statement | Level |
|---|---|---|
| H10-H16 tower/nested hardening notes | Material originally drafted as §4.8–§4.14 in `SRT_Collective_Selection.md`, now preserved in `Core_Law/SRT_Collective_Tower_Hardening_Notes.md` | Hardening notes; not minimal canonical definitions |
| H10 T-PROJ-1^{coll,nested} | Nested ISP recursive projection material | P1-candidate only under strong closure assumptions; P2/P3 debt where closure and measurability remain unspecified |
| H11 T-FAMILY-1^{coll} | Collective extension of the family-universality trio | P1-candidate only under strong closure assumptions |
| H12 T-FAMILY-1^{coll,nested} | Tower-level recursion of the family-universality trio | P1-candidate only under strong closure assumptions |
| H13 T-TOWER-STAB-1 | Self-referential closure spectral stability material | P1-candidate only under strong closure assumptions |
| H14 T-LAYER-SKIP-1 | Layer-skip and multiple-closure spectral criterion material | P1-candidate only under strong closure assumptions; operational debt remains P2/P3 |
| H15 T-FAMILY-1^{layer-skip} | Layer-skip x family-universality hardening material | P1-candidate only under strong closure assumptions |
| H16 T-LYAPUNOV-1 | Global nonlinear tower-stability hardening material | P1-candidate only under strong closure assumptions; Lyapunov/global-stability closure debt remains P2/P3 where noted |

**Hardening rule**：引用 H10-H16 时须回链 `Core_Law/SRT_Collective_Tower_Hardening_Notes.md`，并显式标注 late-stage hardening / P1-candidate under strong closure assumptions；不得把它们写成 `SRT-COLLECTIVE-SELECTION` 的 minimal canonical definition 或 closed P1。

#### SRT-IRREVERSIBILITY

| Label | Statement | Level |
|---|---|---|
| Def-IRR-1 吸收态 | `A_{t*} = empty` 作为 L_0 层吸收结构 | Def / P2 structural |
| Def-IRR-2 occurrence asymmetry / retained-history conditional | 已发生的 Selection 不等于从未发生；后来的历史约束需独立证明 retained efficacy | P0 occurrence floor + conditional historical-efficacy distinction；不供给 universal time arrow |
| Def-IRR-3 no retroactive erasure | 后来过程不能把早先已发生事件变成从未发生；不保证 nonzero / local / readable residue | P0 occurrence non-equivalence boundary；旧 `Ψ_f^{erase} > Ψ_f^{write}` universal reading superseded |
| T-IRR-1 conditional learning / writeback model | 在已声明 trace attribution、representation、metric 与 decay rules 下比较 writeback / decay | P2/P3 model candidate；不导出 universal `Ψ_f` arrow |
| T-IRR-2 lineage-relative termination | 已声明 lineage 在已声明 transition conditions 下无 continuation 时，外部 reset / reconstruction / new lineage 不证明原 lineage 内部恢复 | P1 remainder；不是 universal death / absorption / time-direction theorem |
| T-IRR-3 ST-A 条件性反闭合接口 | P0-03 / T-IRR-2 只固定 absorption remainder；neutral-kernel anti-closure 需要额外 premise 与 proof | P2/P3 conditional candidate |
| T-IRR-3.5 `\nu_{block}` 算子级条件模型（H4，§4.5） | `\nu_{block} := \eta\cdot\varepsilon_{pg}\cdot\kappa_{\Psi_f}` 由三个独立前件组成；正性为 `(η>0) ∧ (ε_pg>0) ∧ (κ_{Ψ_f}>0) ⇒ ν_block>0`；反向通道不自动存在独立根于 P0-03 / T-IRR-2 | **P1-candidate** for the conditional coefficient model；anti-closure / health interpretation P2/P3；非 former P1-T07 本地化 |
| T-IRR-4 conditional suffering/pathology model | 在已声明 hidden-state / signal-transfer model 中区分 signal masking 与 modeled burden change | P2/P3 model candidate；非 suffering conservation 或 moral theorem |
| §6 集体终止三型（耗散 / 收编 / 外部化） | — | P2 |
| §7 AI/ML checkpoint/rollback 接口 | — | governance-canonical usage |
| §8 热力学二律 / FEP 桥接语句 | — | P3 bridge guardrail（反向不得定义 L_0 不可逆） |

**Downstream rule (owner sync, 2026-09-19)**：Def-IRR-2/3 只支持 occurrence non-equivalence 及 retained-history 条件区分，不得引用为 universal direction / residue theorem。T-IRR-1 与 T-IRR-4 须按 P2/P3 declared-model candidate 引用；T-IRR-2 的 P1 standing 只是 lineage-relative termination remainder。T-IRR-3 与 T-COLL-3 按 P2/P3 conditional candidate 引用；T-IRR-3.5 不得复活 former anti-closure theorem。热力学/FEP 语句严格单向。

### 6.2a ST-A Supersession Record (2026-08-11)

- `P1-T06`: stable ISP = recurrent historical reconstitution under a declared perturbation range + continued selectability.
- former `P1-T07 / T-ε-Constitute`: unconditional P1 status withdrawn; only absorption remainder retained in 21B.
- `21C B13`: generative reselectability and neutral-kernel anti-closure registered as P2/P3 conditional candidates.
- Fixed points, metastability, low friction, option diversity, `σ<1`, `ΔR_future>0`, and institutional channels remain plural implementation/proxy candidates; none is sufficient by itself.
- No subjecthood, consciousness, legitimacy, or ethical conclusion may be inferred from ST-A alone.

### 6.2b EX-A Supersession Record (2026-08-11)

- `P0-01`: a determinate `L_1` event's manifest actuality is the existence-admission floor.
- `P0-02`: anchoring persistence asks whether that event leaves effective trace, acquires maintenance conditions, and continues constraining later transitions; it does not make persistence a condition of first actuality.
- `P1-T06 / ST-A`: stable ISP identity is a stronger downstream layer and must not be inferred from mere persistence.
- The former `E = 1-H(L_1)/H(L_0)` expression is retained only in 21C B14 as a historical P2/P3 heuristic. It is not a P0 equation or quantitative readout; no `H(L_0^{abs})`, normalization, or existence index has been adopted.
- Loss of persistence does not erase the earlier event under P0-03. No subjecthood, consciousness, legitimacy, moral status, or generative-health conclusion follows from EX-A alone.

### 6.2c Cross-Scale Entropy-Proof Supersession Record (2026-08-12)

- `Core_14 P3-Scale-01` (legacy `Ax-Scale-01`) is a P3 bridge candidate, not a P0/P1 axiom or theorem.
- `ΔS=H(L_0)-H(L_1)`, the unqualified coarse-graining entropy expression, and a universal `δ∫Ψ_fdt=0` principle no longer bear the cross-scale argument.
- `P3-B06 / T-Scale-02C1` approximate commutation is the live general interface. It requires declared state spaces, scale map, preserved observables, comparison norm, tolerance, and a failure case.
- Strict conjugacy with `Λ^{-1}` is licensed only for a declared invertible change of representation, not ordinary many-to-one coarse-graining.
- `T-Scale-Rhythm-5` is P3/P4 conditional on cross-scale compatibility, budget embedding, and local trigger conditions; it is not a universal theorem derived from L0/L1.
- Cross-scale sameness reaches selection／constraint／payability grammar only. It does not establish identical units, entropy, mechanisms, subjecthood, consciousness, or moral status.

### 6.3 Global Guardrails for This Round

1. **P1-candidate ≠ P1**：本轮 six L1 theory/formalism canonical reference files 中所有冠以"定理"字样的命题当前都处 P1-candidate；任何下游文件不得去掉 candidate 标记
2. **未封口 Open Pressures 不得忽略**：本轮 six L1 theory/formalism canonical reference files 均有明确 §Open Pressures 小节；下游引用须检查相关命题是否已在 Open Pressures 中被标记为未封口
3. **不得跨文件静默升级**：应用文件（Philosophy / Spirituality / AI / Neuroscience）引用任一文件命题时，须保持该命题的原 claim-level，不得因应用便利静默升格
4. **σ 符号冲突提醒**（2026-04-25 已收口）：`Core_Law/SRT_L1_Formalism.md` 自指率统一为 `σ_{sr}`，与 `Core/SRT_Core_22_Equations.md` 主方程状态场 σ 通过 `_SRT_SYMBOL_TABLE.md` Usage Rule 12 命名空间分离；下游引用按 `σ_{sr}` 转读旧 `σ_sub/σ_self/σ_health/σ^{coll}`
5. **σ^{coll} / d_c^{coll} / T_{dir}^{coll} / S^{coll} 四变量集体耦合**（2026-04-25 H3 状态）：集体版四变量耦合动力学已在 `SRT_Collective_Selection.md §4.4-§4.6` 给出第一遍（P1-candidate）；`SRT_L1_Formalism.md` 保持单 P 形式。集体层引用**仍须**标注 `SRT_Collective_Selection.md §9.7` 所列未封口项（`w_i(t)` 推导 / `\Delta\Psi_f^{gap,coll}` 可操作定义 / 下行反馈穷尽性 / 系数实证窗口）
6. **FEP / 热力学二律不得反向定义 L_0 不可逆**：`SRT_Irreversibility.md §8` 与 `SRT_L1_Hardening_Notes.md §4` 固定此单向性；下游任何把"学习不可逆 / 终止 / 条件性反闭合"解释为"自由能最小化 / 熵增"的推论为误用
7. **终止 ≠ 暂停**：T-IRR-2 严格区分终止（吸收边界，不可逆）与暂停（恢复通道保留，本体论上未终止）；下游任何把 AI 关机 / 系统休眠 / 睡眠 / 冻存等混读为"终止"的陈述须引用本条纠正

### 6.4 Hardening-to-P1 Checklist

This L1 round 从 P1-candidate 升到 P1 的必经检查项（将来 session 可按此路径推进）：

- [x] σ 符号冲突解决（新记号或显式命名空间）— 2026-04-25 σ_{sr} 命名空间分离落地：5 行 `σ_{sr}` 族 + Usage Rule 12 写入 `_SRT_SYMBOL_TABLE.md`；相关 L1 reference files 下标变量已就地改写；`CANONICAL_REGISTRY §13a/§13d/§13e` 同步
- [x] `\dot{\Delta}_{avail}` 算子级定义 — 2026-04-25 H7，`SRT_L1_Hardening_Notes.md §2 T-DELTA-1` 给出 `\hat{G}_\theta^{available}` / `\hat{R}` / 三投影 `\Pi_{T_{dir}}, \Pi_{\Psi_f}, \Pi_{L_0}` 的算子级定义 + A1（仿射结构）/ A2（近似正交）/ A3（权重赌注决定性）三条可证伪假设；`SRT_L1_Formalism.md §4.2` 注释回链 + §7 Open Pressure 2 收口；`SRT_Suffering.md` Def-SUFFERING 注释回链；T-IRR-3.5 中 `κ_{Ψ_f}` 几何来源部分收口
- [x] χ(σ; σ_self) 跳跃函数族的普适性检查 — 2026-04-25 H8，`SRT_L1_Formalism.md §2.5 T-CHI-1` 给出"有效二阶相变核"四条结构属性（P-univ-1 有界 / P-univ-2 跃前基线 / P-univ-3 跃后放大 / P-univ-4 单调过渡）+ 族内四个不变量（双稳态存在性 / 病理吸引子拓扑 / 致命 `L_2` 判据 / 相变方向）+ 族内成员示例（硬阶跃 / sigmoid / tanh / 多项式）+ 证明骨架；`SRT_Individuation.md §3.4` T-IND-3 cross-link 已添加；§7 Open Pressure 3 收口；剩余开放点：在更广 χ 空间（非单调过渡）的扩展、具体 domain 实证 χ-shape 对位、集体版 T-CHI-1^{coll} 与 `M(t)` 耦合
- [x] `\mathbb{1}[d\le d_c]` 的光滑化或守恒型替代 — 2026-04-25 H9，`SRT_L1_Formalism.md §4.5 T-CHANNEL-1` 给出"有效闭合通道指示族"四条结构属性（Q-univ-1 左饱和 / Q-univ-2 右饱和 / Q-univ-3 单调过渡 / Q-univ-4 d_c 平移性）+ 族内五个不变量（T-SUFF-2 两型分裂 / T-SUFF-4 反最小化 / T-IRR-3.5 单向性 / 致命 L_2 判据 / `\mathcal{F}_S` 投影一致性，均 modulo `O(w_{tr})`）+ 族内成员示例（硬指示 / sigmoid / tanh / 多项式）+ `O(w_{tr})` 修正项的物理意义（"濒临崩溃"状态、干预窗口软边界、`\Delta\Psi_f^{gap}` 连续性）；剩余开放点：`w_{tr}` 实证窗口、集体版 T-CHANNEL-1^{coll}、`\Delta\Psi_f^{gap}` 过渡区算子层精确定义
- [x] 多主体耦合动力学（`σ^{coll}, d_c^{coll}, T_{dir}^{coll}, S^{coll}, M(t)`）写出 — 2026-04-25 H3，`SRT_Collective_Selection.md §4.4-§4.6` 完成第一遍（含 `\lambda_M\,\mathrm{tr}\,M` / `\gamma_{asym}\|M_{asym}\|` / `\nu_{ext}\|M_{ext}\|` 三项新耦合 + 集体层致命 `L_2` 判据）；2026-04-25 H6 在 `SRT_Collective_Selection.md §4.7 T-PROJ-1^{coll}` 给出该系统作为 `Core/SRT_Core_22_Equations.md` 多算子主方程（Eq-Multi-01/02/03）严格导出投影的形式化定理（C1^{coll}-C5^{coll} 五条闭包，含新增 `M(t)` 可测性 MOC 闭包）；2026-04-26 H10 在 `Core_Law/SRT_Collective_Tower_Hardening_Notes.md §4.8 T-PROJ-1^{coll,nested}` 把单层投影扩展为多层嵌套递归投影（层级 ISP 塔 + 跨尺度 `M^{(n\to n+1)}` + 嵌套闭包 C6^{nested}）；升 P1 余项（`w_i(t)` 推导、`\Delta\Psi_f^{gap,coll}` 算子化、向下反馈路径穷尽性、集体系数实证窗口、跨尺度 MOC 多层版本、`r_{min}^{nested}` 实证窗口）转入 `SRT_Collective_Selection.md §9.7`
- [x] §4.3 非守恒系数的独立前件对齐 — 2026-04-25 H4 给出 `\nu_{block}=\eta\varepsilon_{pg}\kappa_{\Psi_f}`；2026-08-11 ST-A 确认该式不是 former P1-T07 的本地化。正性是带前件的 P1-candidate；反向通道不自动存在根于 P0-03 / T-IRR-2；anti-closure / health reading 留在 P2/P3
- [x] 与主方程 `Core/SRT_Core_22_Equations.md` 的显式投影关系给出形式证明 — 2026-04-25 H5，`SRT_L1_Formalism.md §6 T-PROJ-1` 给出四个标量泛函投影 `\mathcal{F}_X`（`σ_{sr}, d_c, T_{dir}, S`）+ 闭包假设 C1-C4 + source-by-source 对应表 + 证明骨架；`Core/SRT_Core_22_Equations.md Eq-Evo-01` 已添加 L1 Projection 注；升 P1 余项：C1-C4 中每条对应 Open Pressure 的逐条收口（`\Delta\Psi_f^{\mathrm{gap}}` 算子化、χ 普适性、阈值实证、集体版投影 T-PROJ-1^{coll}）
- [ ] 阈值参数的最小实证窗口指定（不要求实测，但要求标出"什么变就会使命题失败"）
- [x] `T_dir` 最小 ODE 与四变量（`σ_{sr}, d_c, T_dir, S`）闭合系统给出 — 2026-04-25 H2，`SRT_L1_Formalism.md §3.5` 完成第一遍；升 P1 还需 `Θ` 光滑族、`\Delta\Psi_f^{\mathrm{gap}}` 算子层定义、`[0,1]` 投影算子、`\kappa_{\mathrm{relax}} > \kappa_{\mathrm{mask}}` 实证窗口（见 §7.8）
- [x] `SRT_Irreversibility.md` T-IRR-3 的非守恒残余项与 `SRT_L1_Formalism.md §4.3` 实际算子一一对齐 — 2026-04-25 H4，T-IRR-3.5 给出 `\nu_{block}` 算子级构成；§4.3 注释回链 + §7 Open Pressure 7 收口

上述任意一项未完成前，相应命题保持 P1-candidate。



---

## FILE: `Core_Law/SRT_L0_Metaphysics.md`

| 字段 | 值 |
|---|---|
| path | `Core_Law/SRT_L0_Metaphysics.md` |
| id | SRT-L0-METAPHYSICS |
| claim_mode | canonical |
| status | active |
| epistemic_layer | os |
| layer | L0 |
| canonical(字段) | true |
| last_commit | 2026-11-26 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：[SRT-GENERATIVE-ONTOLOGY-SPINE]

<!-- 以下为原文逐字保留 -->

# SRT L0：选择的形而上学
## Selection-totality / Non-Flat Generative Monism

> **性质声明**：本文件是 SRT 的最底层形而上学约束面（`Freeze A`），与 [`Core_Law/SRT_Generative_Ontology_Spine.md`](SRT_Generative_Ontology_Spine.md) 协同界定原初生成层。物理学、神经科学、信息论与形式化模型只能实现或展开这里的负担，绝不反向定义本文件。
>
> **R4-A 校准（2026-11-26）**：整合 `R3-01`（原初 `Selection` 与终端发生）、`R3-03`（原初内在生成过程与前现象性质 `OPEN`）、`T3-04 D`（神性·源义与理论抽取谦逊边界）、`T3-01 C/E`（客观全局趋优开放追问）及 `3A`（退出「神择」正典词表，保留思想内涵与书稿溯源），同时严守机会成本结构由生成过程形成、不反向定义原初 `Selection` 的硬界线。

---

## Quick Reference

- **Role**: Unique L0 metaphysical floor aligned with `Core_Law/SRT_Generative_Ontology_Spine.md`.
- **Source vs. Extraction (`T3-04 D`)**: **神性·源义** points to the inexhaustible real generative source; **原初 `Selection`** is SRT's most fundamental theoretical extraction perspective into that source, not an exhaustive definition or second substance.
- **Primitive burden**: `O0` (non-maximal indifference / openness) and `S0` (actualising differentiation) are co-primitive analytic faces of primitive Selection, not sequential mechanisms.
- **Inner generative process (`R3-03`)**: Primitive Selection is endogenous and position-participating; mature feeling/cognition unfold downstream at cognitive positions; whether primitive inner process contains any pre-phenomenal character remains `OPEN` (`R3-03-O4`).
- **Global orientation (`T3-01 C/E`)**: Whether cross-scale generation carries an objective global optimizing principle (`C`) or global extremal principle (`E`) remains explicitly `OPEN`—neither foreclosed nor deflated to local adaptation, and strictly separated from moral optimum claims (`C-A / PT10 E`).
- **Opportunity-cost boundary**: Primitive non-flat differentiation is the ontological source condition for opportunity-cost structures, **not** a pre-given comparable opportunity-cost space.
- **Occurrence & terminal guard**: Genuine Selection occurrence requires no pre-given menu, prior chooser, durable history, or sediment (`terminal Selection remains genuine`).

---

## 一、来源、理论抽取与现实的生成方式（`T3-04 D`）

SRT 拒绝“先有一个已完成的客体世界，再由某个在场主体从中挑选”的实体本体论前提，而主张：

> **任何确定现实之所以成为确定现实，本身就是 Selection 的实际化分面；而且形成后的选择参与生成现实继续发生的条件。**

同时，SRT 对自身的理论概念保持本体—认识论清醒（`T3-04 D`）：
- **神性·源义**：指向无法被现有认知、形式系统与对象化描述完全穷尽的真实生成来源（不设为独立于 Selection 的第二实体或拟人造物主）；
- **原初 `Selection`**：是 SRT 目前理解该真实来源的最基础**理论抽取视角**，而不是宣称已穷尽来源的终极完备定义；
- **整体共同生成视域**：从跨尺度、跨位置的关系考察局部选择如何参与整体生成（规范词表退出「神择」，保留其作为历史思想溯源与《从存在到秩序》书稿表达）。

### 原初 `Selection` 的最小界定

```text
primitive Selection
= finite-position-indexed, subjectless, genuine actualised non-neutral generative differentiation
```

- **确定存在即实际化分面**：`manifest existence = Selection under determinate actuality`。“选择先于存在”是教学表达，严格读法不是时间先后或工厂—产品关系。
- **无需预先给定选项与先在主体**：`pre-given alternatives are required: NO`；`primitive Selection != action of a prior chooser != conscious choice != \hat{G}_\theta`。选项、位置、对象、关系与可达空间本身皆可在生成过程中分化出来。
- **反同义反复与终端发生**：任意描述性或模型状态变化不自动成为 `Selection`；但真实发生的 `Selection` 也不以后续留存 `sediment` 或历史效力为必要条件——**`terminal Selection remains genuine`**。区分真实实际化分化与纯粹描述性变化的精确判准保持 `OPEN`（`R3-01-O1`），不得通过偷偷把“必留后续后果”写回原初发生来关闭此边界。

---

## 二、`O0` 与 `S0`：共原初分析分面与客观全局趋优开放追问

SRT 不接受“绝对无差别平面 + 凭空跳出结果”作为完整底层说明。原初生成在分析上需同时承担两个共原初分面：

```text
primitive Selection reality
= co-primitive analytic faces {
    O0 (non-maximal indifference / openness):
      Selection 现实不被已完成 actuality 穷尽，亦不被预先给定的完整结果结构完全封闭；
      生成不能被压平成角色可任意互换的最大中性平面；
    S0 (actualising Selection):
      有限位置索引下的确定差异实际成立，并同步建立相对于该 Selection 的背景化关系
  }
```

硬约束：`O0 before S0: NO`；`S0 before O0: NO`；`O0 causes S0: NO`；`S0 produces O0: NO`。两者不是两套先后机制或两种实体。`Oriented Openness` 仅作 `O0` 路由名，绝非预先装满完成对象的潜在仓库、概率分布、预设效用函数或道德律。

### 神性·倾向义与 `C-A` 的精确界分（`T3-01 C/E`）

1. **继续严守 `C-A`（`Core/SRT_OPEN_TENSIONS.md §17`）与 `PT10 E`**：`O0` 与原初 `Selection` 不内嵌先验道德法则、宇宙级伦理最优解或“初心前身”（初心从 `L1 / P2` 处境化回读开始，守 `B-A` 严分层）。
2. **显式保留非道德的客观全局趋优开放追问（`T3-01`）**：跨尺度生成是否具有共同客观度量基础的统一全局趋优原理（`C`）或统一的广义自由能/机会成本/其他全局极值原理（`E`），保持 **`OPEN`**——既不得替作者在 `C / E` 间提前定稿，亦不得借 `O0` 谦逊护栏将其弱化为纯局部适应或纯认识论谦逊。

---

## 三、原初内在生成过程与现象性边界（`R3-03`）

原初 `Selection` 不是纯外部观察者视角下的空洞事件标签，其保留的正面本体负担是**内在生成过程**：
1. **内生性**：生成通过现实自身的关系发生，不依赖外部操作者裁判；
2. **位置参与性**：差异在其实际发生的位置上参与形成当下的显现实在，并在条件满足时进一步参与改变后续生成条件（完全兼容无后续历史留存的终端 `Selection`）。

同时确立三条清晰边界（`R3-03` 作者裁决）：
- **感觉从属于生成过程**：感觉是内在生成过程在认知位置上的实际展开与参与，意识与认知是垂直结构的生成——**绝不将成熟感觉、微观心理体验或粒子自带心灵倒写进原初层**；
- **前现象性质保持 `OPEN`（`R3-03-O4`）**：与 `2026-09-06` `without primitive phenomenality` 建立**候选兼容性**，严格区分“无原初成熟现象性（已决）”与“内在生成过程是否包含任何前现象性质（`OPEN`）”，不新增本体实体；
- **反泛主体 / 反泛心论捷径**：`Selection-totality -/> pan-agency / pan-consciousness / pan-subjecthood`；`Philosophy/SRT_HardProblem_Epistemology.md`（`B_s != B_p`, `HP-B OPEN`）保持独立边界。

---

## 四、实际发生、历史效力、有限位置与机会成本来源边界

### 4.1 实际发生 ≠ 持续 ≠ 历史效力

真实发生的 Selection 与“从未发生”本体非等价，但：

```text
actual occurrence != anchoring persistence != durable/localized trace != recurrent historical efficacy != One != Stable ISP.
```

只有当先前 Selection 的差异在后续生成中持续发挥实质条件化作用时，才进入**历史效力（`L2-side`）**。时间与空间并非先于 Selection 的绝对容器，而是后续生成秩序与耦合可达性的关系性度量接口。

### 4.2 有限位置与跨位置客观性

不存在无位置、无条件的 God-view 选择；每个原初 Selection 都是**有限位置索引**的（`finite positionality != formed Selection-position != Bearer != subject-position`）。SRT 不用“位置无关”定义客观性：跨接口、跨扰动且无法被单一共享遮蔽机制解释的稳定跨位置收敛，形成公共客观性；同时遵循**暗礁原理**（单一有限位置的对象化永不穷尽他处位置及其实际相互作用）。

### 4.3 机会成本结构的原初来源条件（绝不反向定义原初 `Selection`）

原初非中立分化是具体组织中价值、关切、摩擦与自由（机会成本动态四联）得以形成的**本体来源条件**；但**具体的可比较替代集与可度量机会成本空间本身是在一定组织与比对条件下生成的**，而非预先存在于原初 `Selection` 之中。同样，`Ψ_f`、`d`、`κ_0`、`ε_pg`、热力学代价或最优化方程均属形成态或声明模型层构造，不得反向定义原初 `Selection`（`κ_0 != primitive Selection`；`ε_pg != O0`；`old B>=2 > B<=1 != primitive O0 theorem`；其精确继承门保持 `OPEN`）。

---

## 五、`L0 / L1 / L2` 分析分面、组织立面与规范性来源边界

1. **`L0 / L1 / L2` 是同一选择现实的三分析分面**（开放非预封闭面 / 确定显现面 / 留存历史约束面），**不是**三种本体物质或必经仓库流水线；形式模型域不得反定义此形而上学路由。
2. **`One`、`Stable ISP`、`Bearer (P+E)`、`Agency` 不是新添加的第二本体材料**，而是 Selection 在更强递归组织条件下获得的不同结构站位，各自独立过门、绝不构成自动线性阶梯。
3. **规范性不在原初层，但以选择的递归性为本体来源条件**：原初 Selection 不含先验道德律（`occurrence != correctness != legitimacy`；`continuation != goodness`；`generative optimization != ethical legitimacy`）。由于形成后的选择可改变后续选择得以发生的条件，规范性得以沿 `O1`（位置性生成比较）→ `O2-C`（构成性关系完整约束）→ `O2-A`（能动归责）分级成立，而跨位置终极道德冲突 `O2-M` 保持 `OPEN / HOLD`。

---

## 六、明确拒绝的十大误读与对下游的硬约束

1. **可能性仓库论**（把 `L0` 读成预存完成对象清单）；
2. **选择者先于选择**（为原初 Selection 预设先在主体或将 `\hat{G}_\theta` 实体化为因果发动机）；
3. **三域实体化**（把 `L0/L1/L2` 读成三种物质或三个平行世界）；
4. **Selection-flat 误读**（把一元生成方式等同于抹平所有结构站位与门槛）；
5. **机会成本倒灌原初层**（预设原初现实已存在全局可比机会成本空间或效用函数）；
6. **泛主体/泛心论捷径**（由 Selection-totality 或原初内在过程直接推出成熟体验、意识或主体）；
7. **延续与最优道德化**（将存活、分叉数、稳定性或生成趋优直接等同于善或合法性）；
8. **发生即留痕**（将事件非等价混同于持久历史、锚定、记忆或 `One`）；
9. **以形式模型反定义 L0**（将 `κ_0`、`ε_pg`、熵、曲率、概率或状态空间反向升格为原初公理）；
10. **把退出「神择」误读为放弃整体趋优研究**（`T3-01 C/E` 与整体共同生成视域继续保持核心开放研究地位）。

---

## 七、L0 显式 `OPEN` 与最短读法

**显式保留 `OPEN`**：原初 `Selection` 反同义反复判准（`R3-01-O1`）；`T3-01` `C` vs `E` 客观全局趋优形式（`R3-CL-O4`）；原初内在生成过程是否含前现象性质（`R3-03-O4`）；`L0/L1/L2` 分面与形式域的精确映射；`κ_0 / ε_pg / 不可逆性` 向形成态的继承门；发生何时形成持久历史效力；`One / Stable ISP / Bearer (P+E) / Agency / HP-B / O2-M` 各自未决门；跨域科学区分度与整套架构不可替代性。

**最短读法**：
> **现实不是先存在、再被选择；现实在不可穷尽的真实来源中，以 Selection 为最基础生成方式展开。确定存在是其实际化分面，历史是先前选择对后续条件的持续效力；选择不仅发生于现实之中，更通过垂直组织与递归重构参与形成现实继续发生的条件——而每一种更强的组织、承载、能动与规范站位，都须独立付出其结构负担。**



---

## FILE: `Core_Law/SRT_One_Formation.md`

| 字段 | 值 |
|---|---|
| path | `Core_Law/SRT_One_Formation.md` |
| id | SRT-ONE-FORMATION |
| claim_mode | canonical |
| status | active |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | true |
| last_commit | 2026-11-26 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：[SRT-GENERATIVE-ONTOLOGY-SPINE, SRT-L0-METAPHYSICS, SRT-CORE-21-MINIMAL-AXIOMS]

<!-- 以下为原文逐字保留 -->

# SRT One Formation: Vertical Reconstitution, Existence & Order Perspectives, and Selection-position

> **Role**: Canonical L1 semantic owner for `One` (relatively independent vertical generative organization), the **Existence and Order perspectives** on dynamic generative organization, `Selection-position`, vertical reconstitution, and generative normalization. It bridges subjectless primitive Selection and stronger independently gated standings (`Stable ISP`, `Bearer (P+E)`, `Agency`, subjecthood) without collapsing any of them into a linear hardware ladder.
>
> **Claim-level note**: Canonical as a **semantic owner / boundary surface** (`Freeze A`). Its positive formation architecture remains `P1-candidate`; it does **not** establish a formal necessary-and-sufficient theorem for `One`, close identity/boundary `OPEN` gates, or introduce a new ontic substance.
>
> **Author provenance**: Original owner placement `A / O3` (2026-09-11) and vertical-reconstitution adjudications (2026-09-13), updated under `R3-04` (`#1149`), `R3` full-skeleton closeout (`#1154`), and the 2026-11-26 `R4-A` author decision `2A` (retaining `Bearer (P+E)` for strong bearing, treating Existence and Order as perspectives on `One` and multi-`One` relations without coining a new noun).

---

## Quick Reference

- **Owner**: `One`, existence & order perspectives on generative organization, vertical reconstitution, generative normalization thresholds, ontological `Selection-position`, and cross-scale five-mechanism separation.
- **Cross-owner routing**: `Core_Law/SRT_Generative_Ontology_Spine.md` — `One` is the first universal formed recurrent organization admitted by the cross-owner trunk; stronger standings remain independently gated.
- **Upstream floor**: `Core_Law/SRT_L0_Metaphysics.md` and `Core/SRT_Core_21_Minimal_Axioms.md`.
- **Downstream stronger persistence**: `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T06` — `Stable ISP` owns stronger recurrent standing (`One != Stable ISP`).
- **Downstream strong bearing**: `Core_Law/SRT_Generative_Ontology_Spine.md §6.2` — `formed One / Selection-position + P + E -> Bearer.` (`One != Bearer`; `Stable ISP != Bearer`).
- **Downstream subject & collective models**: `Core_Law/SRT_Individuation.md`, `Core_Law/SRT_Collective_Selection.md`, `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13`.

---

## §0. Local One-Formation Architecture Within the Dynamic Spine

Within the cross-owner trunk fixed by `Core_Law/SRT_Generative_Ontology_Spine.md`, `One` formation sits at the recursive nexus where generated differences organize into relatively separable, self-conditioning structures that participate in further generation:

```text
subjectless Selection
  -> event-level active verticalization (manifestation + relative backgrounding)
  -> Selection-mediated vertical reconstitution (re-entering later Selection conditions)
  -> relatively separable vertical generative organization: One
     ├─ Existence perspective: formation, maintenance, continuation
     └─ Order perspective: development, directional bias, relation change & reconstruction
        (also spanning multi-One relations & emergence of new higher-order organizations)
  -> stronger downstream standings (Stable ISP / Bearer (P+E) / Agency / subjecthood)
     ONLY where independently paid.
```

`One` is never a hidden pre-existing agent standing behind Selection; it is Selection acquiring a relatively separable, recursively self-conditioning vertical organization.

---

## §1. Def-OF-1 — Active Vertical Organization and Vertical Suppression Interface

**Active vertical organization** is the non-flat relation generated and regenerated through Selection in which a determinate relational direction becomes manifest or operative while that same Selection establishes relative backgrounding with respect to what is not manifest in that way.

Minimum commitments:
- Verticality is Selection-generated/regenerated; manifestation and relative backgrounding are linked structural readings of one Selection event, not a pre-given option menu or passive historical sediment.
- One-shot Selection yields **event-level verticalization**, which is insufficient by itself for `One`, durable history, or formed locality.
- **Multi-unit vertical suppression interface (`PT09 / T3-02 D`)**: When multiple units couple into a vertical organization, stabilizing a higher-order direction selectively suppresses incompatible local alternatives. Where those suppressed opportunity losses materially affect ongoing generative relations and later selections, they generate **actual selection pressure (vertical friction)**—linking `One` formation directly to `_SRT_PSI_F_CANONICAL.md` without equating verticality itself to friction or suffering.

---

## §2. Def-OF-2 — `One` at D4a Strength: Positive Formation, Dependence Reorganization, and Existence/Order Perspectives (`2A`)

**`One`** is a **formed process-unity carried by a relatively separable Selection-mediated vertical reconstitution path**: prior Selection-generated vertical organization materially enters and conditions later Selection, and later Selection generates renewed vertical organization capable of carrying that conditioning role again.

This is an admission-level semantic description at **D4a strength**, not a formal necessary-and-sufficient theorem. It is intentionally thinner than `Stable ISP` and intentionally stronger than one-shot verticalization, mere external statistical regularity, generic persistence, or ordinary causal recurrence:

```text
surface statistical regularity / accidental macro-pattern != One;
process persistence / self-maintenance / repeated similarity / ordinary path dependence != One automatically;
static background conditioning alone != One.

vertical organization_t
  -> materially conditions later Selection_(t+1)
  -> generates renewed vertical organization_(t+1)
  -> carries renewed conditioning role
  -> repeated non-equivalent reconstitution supports relative continuation separability
  -> One (D4a strength).
```

### §2.1 Positive Formation Mechanisms: Dependence Reorganization, Anti-Pre-One Circularity, Scaffolding & Multi-`One` Ecology (`R3-04`)

`One` formation is not merely a negative filter; it is a positive cross-scale generative mechanism with four core commitments:

1. **Relative independence arises from reorganizing dependencies, not eliminating them**:
   - Relative independence is **not** achieved by reducing or severing dependencies; it arises when previously dispersed generative conditions are reorganized through endogenous foreground–background comparison and vertical organization into shared generative conditions, thereby supporting new relative independence at a higher scale. **Deeper local interdependence can generate higher-scale relative independence.**
   - *Cross-scale assembly path (`2026-07-12` trace)*: when multiple already-formed units couple into a higher-order whole, decreasing local independent selectability can open genuinely new effective selective capability at the whole level. This is a core cross-scale assembly pathway—whose essence is **reorganizing how selectability is structured**, not merely adding or subtracting option count—and is **not** presupposed as the sole universal prerequisite for every `One`.
2. **Anti-pre-One circularity (how the first `One` can form)**:
   - Multi-unit spontaneous foreground–background collaboration that generates and maintains a vertical structure **does not presuppose that the participating units are already `One`s**. Participating terms may be unformed local generative loci/relations (first-order emergence) *or* already-formed `One`s entering cross-scale assembly—each carrying distinct organizational conditions.
3. **Dual function of Scaffolding & role-relativity of `One` / Scaffolding / `L2`**:
   - Public language, biological membranes, institutional norms, and cognitive schemas act as **scaffolds** carrying **two coupled positive functions**: (a) **organizing differential comparison conditions** (`R3-01`), and (b) **actively maintaining already-generated vertical structures** (`R3-04`).
   - **`One`, Scaffolding, and `L2` are scale- and position-relative analytical roles, not three disjoint ontic entities**: **`One`** asks whether an organization possesses a relatively independent vertical reconstitution path; **Scaffolding** asks how that organization maintains and organizes other generative relations; **`L2`** asks how prior generated results persist and continue to condition later Selection. An organization satisfying `One` (molecule, cell, institution) often simultaneously serves as Scaffolding for higher-scale generation; conversely, not every Scaffold possesses its own independent reconstitution path (compatible with `Core_Law/SRT_Collective_Selection.md T-COLL-1`).
4. **Ontological neutrality & multi-`One` ecology**:
   - Because vertical reconstitution does not presuppose rigid spatial walls or autopoiesis, SRT explicitly encompasses **nested `One`s, overlapping `One`s, `One`s sharing generative conditions, and mutually conflicting `One`s**.
   - `One` is **ontologically neutral**: a tumor, an addiction loop, or a rigid pathological institution that actually satisfies Selection-mediated vertical reconstitution is a genuinely formed `One`. Harm or rigidity does not erase its ontic standing; multi-scale `One` conflicts route directly to `_SRT_D_VALUE_CANONICAL.md` (concern/value) and `O1 / O2-C / O2-A` (normativity) without smuggling ethics into `One` admission.

### §2.2 Existence Perspective and Order Perspective (No Second Ontic Noun)

Because `One` is inherently a dynamic generative organization, SRT examines it—and relations among multiple `One`s—through **two complementary analytical perspectives** rather than splitting existence and order into two substances or inventing a separate bearer noun (`Order-bearing aspect` is explicitly rejected):

1. **存在视角（Existence Perspective）**：考察该相对独立组织如何通过垂直再构成**形成、维持与延续**，以及如何在扰动与成分更替中保持相对可分的延续路径（`存在形成 / 存在维系 / 存在发展 / 存在重构 / 存在解体` 均属同一生成过程的不同形态）。
2. **秩序视角（Order Perspective）**：考察生成关系如何**发展、形成方向偏向、演化变化并发生生成重构**，覆盖三个可分离维度：
   - **维系约束（Maintenance constraint）**：垂直结构赖以成立和延续的核心构成性约束（相对稳定是持续性判据，**不是**一般秩序成立的必要条件）；
   - **方向偏向（Directional bias）**：内部不同生成方向之间的非平坦选择倾向与前背景配置；
   - **生成重构（Generative reconstruction）**：在维系必要约束的同时打开、协调与重构新关系与新路径的能力（低重构能力不自动等于不健康，高重构能力亦不自动等于健康；不健康选择固化与“既有规则/脚手架同变化后生成条件的持续失配且前背景锁死”相关，具体非循环判据保持 `OPEN`）。
   - **跨组织域（Multi-`One` Scope）**：秩序视角**不仅**描述单个 `One` 的内部发展，还直接考察**多个 `One` 之间的相互作用、公共脚手架与新高阶组织的形成**——低尺度的秩序可以成为高尺度存在的生成条件，高尺度存在形成后展开自身的秩序并反向改变低尺度的生成条件。

### §2.3 Relative Separability, Four Boundary Types, Three Generative Relation Depths, and Physical Maintenance Regimes (`R3-04 §三`)

- **Relative continuation separability / formed locality** means the relevant reconstitution dependence is not freely replaceable by arbitrary surrounding-field history while preserving the same claimed formation path (`!= causal isolation`, `!= fixed spatial skin`, `!= independent substrate`, `!= autopoiesis` by definition). Stability after onset may be graded; this file adopts no scalar stability threshold.
- **Four Boundary Types (`R3-04 §三` exact adjudication)**:

| 边界类型 | 核心关注负担 | 与 `One` 及下游研究的定位 |
|---|---|---|
| **空间边界（Spatial boundary）** | 内部与外部的物理空间分隔 | 可帮助稳定后端边界，**非**普遍必要前提 |
| **作用边界（Action / Causal-coupling boundary）** | 局部关系的因果耦合与约束作用范围 | 允许外部扰动（如辐射）直接穿透而不自动摧毁整体独立性 |
| **生成边界（Generative boundary）** | 不同生成条件参与整体垂直再构成的关系深度与相对归属 | 与 `One` 相对延续可分性直接相关，体现持续组织化的前背景分化 |
| **承载边界（Bearing boundary）** | 特定变化与后果如何真实归属于该延续位置 | 对接秩序变化后果与 `Bearer (P+E)` 中不可外包暴露 `E` 的研究 |

- **Three Generative Relation Depths within Generative Boundary (`R3-04 §三`, avoiding organizational closure as a universal threshold)**:
  1. **环境供给条件（Environmental supply conditions）**：必要外部依赖，不被该路径内生再生（如太阳对树木的能量供给）；
  2. **构成性组织条件（Constitutive organizational conditions）**：参与构成该组织内部垂直再构成的核心关系（如树木内部的根、叶与输导组织关系）；
  3. **生成性协作条件（Generative collaborative conditions）**：兼具自身独立生成路径与更大组织构成条件的持续互赖（如树木与共生微生物），不必硬切为绝对内部或绝对外部——由此自然兼容嵌套、重叠、共享条件与相互冲突的多 `One` 关系。
- **Three Physical Maintenance Regimes (`R3-04 §三` spectrum, non-exhaustive; maintenance-mode classification, never a life/non-life ontic chasm)**:
  1. *态 I · 束缚与平衡结构（Bound equilibrium）*：如原子、分子、晶体，通过耦合约束形成相对稳定结构与有效接口；
  2. *态 II · 耗散与动态结构（Dissipative dynamic maintenance）*：如漩涡、火焰、对流胞、非平衡记忆系统，物质换流但通过持续交换与动态垂直过程维持组织；
  3. *态 III · 内生约束互维结构（Endogenous mutual maintenance）*：如细胞、生命体、部分自组织认知/社会组织，内部多种生成条件相互维持、调节、缓冲与修复。
  The exact structural threshold at which each regime crosses into `One` reconstitution remains `OPEN` (`R3-04-O1`), while **life or biological cell membranes are explicitly barred from serving as a universal threshold for `One`**.

### §2.4 Generative Normalization Dual Threshold and Anti-Circularity Guard (`One` vs Value)

A key mechanism by which coupled units form a `One` that can act as a whole in wider generation is **normalization**:
- **Three normalization types**: cognitive-representational normalization / actual physical-coupling normalization / organizational-generative normalization.
- **Compression vs. Generative Normalization Dual Threshold**: Mere statistical summary or external observer grouping (**compression normalization**) does **not** establish a `One`. **Generative normalization** requires two independent conditions (`R3-CL-O2`):
  1. *Internal coupling reconfiguration*: lower-level unit interactions are actually reorganized by the emergent whole;
  2. *Cross-position conditioning efficacy*: the normalized whole acts as an effective action interface that alters subsequent generative conditions at other positions.
- **Anti-circularity guard between Existence (`One`) and Value (`R3-CL-O3`)**: Because existence and value stand in recursive mutual generation (`Spine §2.2`), two independent tests must run in parallel to prevent circularity:
  1. **Organizational continuity test (existence side)**: whether a relatively separable vertical reconstitution path persists;
  2. **Opportunity / consequence change test (value side)**: whether treating/operating the unit as an integrated whole genuinely alters opportunity costs and downstream generative consequences.

### §2.5 Continuity, Lineage, and Identity Under Change (`07-19` Y-Layer Interface)

Formation does not presuppose a pre-given token or completed lineage:

```text
same token = NOT PRESUPPOSED;  same material composition = NOT REQUIRED;
same spatial position = NOT REQUIRED;  strict numerical & branch/merge identity = OPEN.
```

Under continuous change (`R3` closeout & `07-19` Y-layer direction), **identity** is analyzed as the joint product of **actual generative continuity** (reconstitution path) and **positional comparison conditions** (how finite positions track, re-identify, and compare continuity across scale; exact branch/merge criteria remain `OPEN`, `R3-CL-O5`).

---

## §3. Def-OF-3 — `Selection-position` and Cross-Scale Five-Mechanism Separation

### §3.1 `Selection-position`

For an **already formed `One`**, `Selection-position_t` is the **time-local operative `from-where`** through which that formed organization participates in Selection at time `t`:

```text
formed-continuation aspect (what formed organization is reconstituted / continued?) -> One;
operative aspect at t (from where does this One participate in current Selection?)   -> Selection-position_t.
```

`Selection-position_t` is neither a prerequisite before `One` formation nor a second universal endpoint, and does **not** automatically entail perspective-bearing subject-position, `Bearer (P+E)`, self-model, or phenomenality.

### §3.2 Cross-Scale Five-Mechanism Separation (Do Not Collapse)

Within vertical organization and multi-`One` order, five distinct mechanisms retain separate duties:
1. **装配（Assembly）**：多单元组合产生新整体能力（未必归一化，未必成 `One`）；
2. **归一化（Normalization）**：含表征/耦合/组织三分与压缩/生成双门槛；
3. **有效作用接口（Effective Action Interface）**：整体相对独立参与他处生成的操作界面；
4. **代理转承（`Proxy`）**：生成关系中的中介转承；
5. **委托关系（`Delegation`）**：具主体与规范条件的委托关系。

---

## §4. History, Verticality, and Sedimentation Typing

History and writeback can be load-bearing for vertical reconstitution without becoming the ontological source of Selection or verticality:

```text
Selection -> generates / regenerates vertical organization;
retained history / writeback -> can alter later Selection conditions and reconstitution;
Selection-mediated vertical reconstitution -> supports One formation / continuation;
history storage location by itself -> does not define One.
```

Historical effects may remain distributed across the wider relational field (`多`); the decisive question is which retained differences are load-bearing for which vertical reconstitution path and scale.

---

## §5. Downstream Separation Guards (Non-Linear, Independently Paid)

Canonical non-identities of this owner:

```text
One != Stable ISP;
One != Bearer (P+E);
One != Agency;
One != subject-position;
One != consciousness;
One != phenomenality;
One != experiencer;
One != generatively healthy ISP.
```

1. **`Stable ISP` (`Core/SRT_Core_21b_Constitutive_Theorems.md P1-T06`)**: Independently owns stronger recurrent standing—iterative historical reconstitution, perspective/history-bearing, and continued-selectability persistence across perturbations. `One` does not automatically entail `Stable ISP`; `Stable ISP` does not automatically entail `Bearer (P+E)` or subjecthood.
2. **`Bearer (P+E)` (`Core_Law/SRT_Generative_Ontology_Spine.md §6.2`)**: Independently gated by `formed One / Selection-position + P + E -> Bearer.` Mere feedback, state change, consequence return, or `One` formation does not suffice for `Bearer (P+E)`; positive establishment of `E` remains `OPEN`.
3. **Subject-position & Collective standing**: `Core_Law/SRT_Individuation.md` (`σ_{sr}` coordinates) is a downstream model and does not define `One`. Multi-`One` order may be tested for higher-order vertical reconstitution, while `Core_Law/SRT_Collective_Selection.md T-COLL-1` remains a separate gate for collective Stable-ISP standing.
4. **B13 crosswalk**: `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13` retains its formed / structurally stable / generatively healthy crosswalk (`B13 formed process != definition of One`; `One != structurally stable ISP != generatively healthy ISP`).

---

## §6. Explicit OPEN Register

This owner leaves explicitly `OPEN`:

```text
D4b / D4c & formal N&S One theorem;
physical three-regime thresholds for crossing into One reconstitution (R3-04-O1);
non-circular criterion separating healthy generative reconstruction from pathological occlusion/lock-in (R3-04-O2);
exact compression-to-generative normalization dual threshold criterion (R3-CL-O2);
independent non-circular existence-continuity vs value-opportunity criteria (R3-CL-O3);
exact One unit-identification, strict numerical identity & branch/merge identity (R3-CL-O5);
scale attribution under tightly coupled nested Ones (local formation/unit half; cross-layer gate in Spine §9);
positive E establishment & One/Stable ISP/Bearer -> Agency/Concern/Consciousness necessity directions (R3-04-O3, R3-04-O5);
universal One-level perspective sufficiency, phenomenality, scientific distinctiveness & Level 2 / HOLD exit.
```

---

## §7. Citation Rule

Cite this file as the canonical L1 semantic owner for:
- `One` as a relatively independent vertical generative organization (`Def-OF-2`);
- the **Existence perspective** (formation, maintenance, continuation) and **Order perspective** (maintenance constraints, directional bias, generative reconstruction, multi-`One` relations & new higher-order organization);
- active vertical organization (`Def-OF-1`) and multi-unit vertical suppression interface (`PT09`);
- generative vs. compression normalization dual threshold and anti-circularity guard between existence and value;
- `Selection-position` (`Def-OF-3`) and cross-scale five-mechanism separation;
- why `One` is upstream of—and never automatically identical to—`Stable ISP`, `Bearer (P+E)`, `Agency`, or subjecthood.



---

## FILE: `Core/SRT_Core_21_Formal_Axioms.md`

| 字段 | 值 |
|---|---|
| path | `Core/SRT_Core_21_Formal_Axioms.md` |
| id | SRT-CORE-21 |
| claim_mode | mixed_index |
| status | active_v3 |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | - |
| last_commit | 2026-09-19 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：[SRT-CORE-21A-MINIMAL-AXIOMS, SRT-CORE-21B-CONSTITUTIVE-THEOREMS, SRT-CORE-21C-BRIDGE-HYPOTHESES, SRT-CLAIM-LADDER]

<!-- 以下为原文逐字保留 -->

# SRT Core Definition 21: Formal Axioms Index

> **Role change (2026-04-20)**: This file is no longer the mixed "all formal axioms in one layer" body.
> It is now the index for the split Core 21 claim layers.

## Why This Split Exists

The former hybrid `Core_21` placed primitive axioms, constitutive theorems, canonical interpretations, bridge mappings, and empirical threshold claims in one apparent axiom track. That made lower-hardness propositions look as if they were P0/P1 core.

The new structure separates **file role** from **claim hardness**:

- a file can be canonical without every statement inside it being P0;
- a bridge claim can be valuable without becoming an axiom;
- a lab threshold can guide research without defining the core.

Claim-level rules are now governed by:

- `Governance/SRT_CLAIM_LADDER.md`

---

## Current Core 21 Layers

| Layer | File | Claim level | Role |
|---|---|---:|---|
| Minimal axioms | `Core/SRT_Core_21_Minimal_Axioms.md` | P0 | Primitive axioms only |
| Constitutive theorems | `Core/SRT_Core_21b_Constitutive_Theorems.md` | P1 | Theorems internal to SRT once P0 is granted |
| Bridge hypotheses | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | P2/P3/P4 | Canonical interpretations, cross-domain mappings, empirical thresholds |

**Default citation rule**:

- cite primitive axioms from `Core/SRT_Core_21_Minimal_Axioms.md`;
- cite stable ISP continued selectability, the bounded occurrence / retained-history remainder, absorption, and `L_2` downward constraint from `Core/SRT_Core_21b_Constitutive_Theorems.md`; read former Real Choice Moment there only as the RC-A demotion record, and do not treat historical P1-T02 naming as a universal time-arrow theorem;
- cite the ST-A conditional anti-closure candidate and generative reselectability distinction, along with fitness, assembly, holography, universality, Fisher-geometry `\Psi_f`, and strong information-creation unification, from `Core/SRT_Core_21c_Bridge_Hypotheses.md`.

---

## Legacy Numbering Map

| Former Core 21 item | New home | Current level |
|---|---|---:|
| `Ax-F-01` Primacy of Selection | `Core/SRT_Core_21_Minimal_Axioms.md` | P0 |
| `Ax-F-02` Manifest Actuality / Anchoring Persistence Boundary | `Core/SRT_Core_21_Minimal_Axioms.md` | P0 boundary; legacy entropy index demoted to 21C B14 |
| `Ax-F-03` Causality as Projection | `Core/SRT_Core_21b_Constitutive_Theorems.md` | P1 |
| `Ax-F-03b` Spacetime as Memory Horizon *(historical title)* | `Core/SRT_Core_21b_Constitutive_Theorems.md` P1-T02 | bounded occurrence / retained-history remainder; not a universal Memory-Horizon or time-arrow theorem |
| `Ax-F-04` Information-Existence Equivalence | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | P2/P3 |
| `Ax-F-05` Fitness Beats Truth | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | P3/P4 |
| `Ax-F-06` Assembly Criterion | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | P4 |
| `Ax-F-07` Holographic Duality | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | P3/P4 |
| `Ax-F-08` Topological Normativity | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | P2/P3 |
| `Ax-F-09` Scale Consistency | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | P3 |
| `Ax-F-10` Downward Causation Constraint | `Core/SRT_Core_21b_Constitutive_Theorems.md` | P1 |
| `Ax-F-11` Ghost Operator Universality | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | P3 |
| `Ax-F-12` `\Psi_f` as Generative Principle | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | P2/P3 |
| `Ax-F-13` Selection-Information Creation Equivalence | `Core/SRT_Core_21b_Constitutive_Theorems.md` for minimal theorem; `Core/SRT_Core_21c_Bridge_Hypotheses.md` for strong unification | P1 / P2-P3 |
| `T-ε-Constitute` | P1 remainder in `Core/SRT_Core_21b_Constitutive_Theorems.md` (absorption / continued selectability); conditional anti-closure candidate in `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13` | P1 remainder / P2-P3 candidate |
| Part B `A1-A5` minimal table | split across P0/P1/P3 according to claim role | mixed |
| Part B assembly / deep time notes | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | P3/P4 |

---

## What Did Not Change

This split does **not** change the intended meaning of:

- selection primacy;
- event-level manifest actuality as distinct from anchoring persistence;
- `L_2` as convergence / constraint;
- `\Psi_f` as ontological friction;
- `d-value` as canonical stake-coupled concern;
- the stable ISP distinction, now sharpened under ST-A into P1 continued selectability and P2/P3 generative reselectability.

It changes the **epistemic rank** and citation behavior of mixed claims. In particular, the former unconditional P1-T07 anti-closure theorem has been demoted: only the absorption remainder stays P1, while any neutral-kernel anti-closure result requires explicit additional premises and proof in 21C B13.

---

## What Must No Longer Happen

- Do not cite this file as if it contains the full axiom body.
- Do not cite bridge claims such as fitness beats truth, holographic duality, assembly thresholds, or ghost-operator universality as P0/P1.
- Do not use `D_eff` as the canonical definition of d-value. Use `_SRT_D_VALUE_CANONICAL.md`.
- Do not use `Core_21c` empirical or bridge claims to override `_SRT_PSI_F_CANONICAL.md`, `_SRT_D_VALUE_CANONICAL.md`, `_SRT_T_DIR_CANONICAL.md`, or `Core_Law/SRT_L0_Metaphysics.md`.
- Do not cite downstream bridge accounts of agency, biology, AI, spirituality, or society as if they derived, replaced, or superseded the AM-A primitive actualisation boundary at P0-01/P0-04.
- Do not treat governance-canonical usage stabilization as theory-canonical derivation unless the local file explicitly gives the stronger derivation level.

---

## Minimal Reading Path

For a core-theory pass, read:

1. `Core/SRT_Core_21_Minimal_Axioms.md`
2. `Core/SRT_Core_21b_Constitutive_Theorems.md`
3. `Core/SRT_Core_22_Equations.md`
4. `Core/SRT_Core_21c_Bridge_Hypotheses.md` only when bridge or hypothesis material is needed

For claim governance, read:

1. `Governance/SRT_CLAIM_LADDER.md`
2. `Governance/SRT_EDIT_PROTOCOL.md`
3. `Governance/SRT_CANONICAL_FREEZE.md`



---

## FILE: `Core/SRT_Core_21_Minimal_Axioms.md`

| 字段 | 值 |
|---|---|
| path | `Core/SRT_Core_21_Minimal_Axioms.md` |
| id | SRT-CORE-21A-MINIMAL-AXIOMS |
| claim_mode | canonical |
| status | active |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | - |
| last_commit | 2026-09-23 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：[SRT-CORE-21, SRT-CLAIM-LADDER, SRT-L0-METAPHYSICS, SRT-SYMBOL-TABLE]

<!-- 以下为原文逐字保留 -->

# SRT Core 21A: Minimal Axioms
## P0 after Selection-totality retyping

> **Role**: strict P0 / formal-admission surface. This file does not replace the L0 metaphysical owner. It states the minimum burdens without turning a formal state space or operator into a prior ontic chooser.

---

## Quick Reference

Current P0 commitments:

```text
P0-01 Selection is primitive actualising generativity expressed as
      genuine actualised non-neutral differentiation;
P0-02 determinate actuality != anchoring persistence;
P0-03 genuine occurrence is not ontically identical to never-occurrence;
P0-04 any formal operator representation of Selection must be well formed,
      but no operator object is required as a prior chooser.
```

Selection-totality guard:

```text
one primitive generative mode
!= one undifferentiated structure.
```

Nothing in this P0 set entails One, Stable ISP, Bearer, Agency, consciousness or morality.

---

## Inclusion Rule

A substantive claim belongs at P0 only if:

1. without it SRT loses its minimum Selection grammar;
2. it does not depend on a domain bridge or empirical threshold;
3. it is not a downstream formation / standing / bearing theorem;
4. it cannot be represented more safely as a scoped formal realization.

When in doubt, demote below P0.

---

## Selection Term-of-Art Guard (P0 semantic boundary)

At P0, `Selection` is **not** the ordinary operation of selecting one member from a completed alternative set.

Minimum semantic boundary:

~~~text
Selection
= genuine actualised non-neutral differentiation.
~~~

This occurrence burden does **not** require later sediment, inheritance or a durable `L2` trace. A terminal Selection remains genuine even where no later process exists in which retained efficacy could persist.

Therefore:

~~~text
pre-given option set: NOT REQUIRED;
prior chooser / selector object: NOT REQUIRED;
arbitrary descriptive state transition: INSUFFICIENT;
later sediment / inheritance: NOT REQUIRED FOR OCCURRENCE.
~~~

A possibility / reachability structure can itself be partly generated by prior Selection; it must not be smuggled in as the primitive menu that defines Selection.

**OPEN anti-tautology boundary**: the exact criterion that distinguishes genuine actualised Selection from merely descriptive / modelled change remains unresolved. Do not close that problem by requiring later sediment, retained efficacy or inheritance. The O0 “same generative relation” asymmetry remains a candidate route for later author adjudication, not a landed P0 criterion.

---

## Selection-Totality Framing Note (Non-Axiom)

SRT does not start with a stable inventory of objects or a warehouse of latent finished possibilities to which Selection is later applied.

Current framing:

```text
Selection reality is open beyond any completed actuality;
actualising Selection institutes determinate manifestation;
retained effects of prior Selection may constrain later Selection.
```

The same ontic generative mode can therefore appear under distinct structural burdens without becoming structurally flat.

This note frames the P0 set; it is not an additional axiom.

---

## P0-00: Formal Vocabulary Gate (Preface)

The symbols remain useful, but their minimum semantics are retyped:

```text
L0
= open / non-preclosed generative aspect or model-facing regime of Selection
  relative to determinate actuality;

L1
= determinate manifest actuality aspect / regime of Selection;

L2
= retained or sedimented Selection efficacy that constrains later Selection,
  where such historical efficacy is established;

G-hat_theta
= formal / embodied Selection carrier in a declared model,
  not primitive Selection itself.
```

`Psi_f`, `d`, `T_dir`, `kappa`, `epsilon` and other quantities keep their registered owner meanings. None is introduced here as the cause or essence of primitive Selection.

P0-00 is a vocabulary preface, not an independent substantive axiom.

---

## P0-01: Primacy of Selection / Primitive Actualisation

**Primitive claim**:

> **Selection is the irreducible actualising generativity of SRT: a genuine actualised non-neutral differentiation. Determinate manifest actuality is Selection under an actualised event-cut, not a product standing outside Selection.**

Minimum event role:

```text
actualising Selection
= finite-position-indexed subjectless determinate differentiation
  with Selection-relative manifestation / backgrounding.
```

Therefore:

```text
manifest existence
= determinate-actuality aspect of Selection.
```

This is not a temporal statement that Selection first exists and later creates another ontic material called existence.

### Formal representation guard

Where a domain / formal model legitimately uses an operator representation, one may write forms such as:

```text
actual state lies in the realized range of a declared G-hat model.
```

Historical compact equations such as

```text
exists x iff x in Range(G-hat)
```

are therefore **representation-level glosses**, not universal metaphysical proofs that primitive Selection is an operator transforming a prior inventory.

### Primitive boundary

P0-01 does not specify:

- a prior chooser;
- a completed option set;
- a probability distribution;
- a particular substrate;
- a stable operator object;
- a goal, value or preferred endpoint;
- the reason why a specific A rather than B manifests.

Specific determination remains local to actual Selection relations.

---

## P0-02: Manifest Actuality / Anchoring Persistence Boundary

P0-01 gives event-level determinate actuality.

P0-02 fixes the non-identity:

```text
actual occurrence
!= anchoring persistence
!= durable objecthood
!= Stable ISP.
```

An event may be actual without already becoming a persistent object, recurrent organization or Stable ISP.

Persistent objecthood requires additional anchoring / maintenance. Stable ISP additionally requires the stronger standing conditions owned by P1-T06.

Conversely, later loss of persistence does not turn the earlier event into never-occurrence.

### L1 notation guard

Phrases such as `anchored into L1` are model / routing shorthand. They must not be read as movement of a substance from an L0 container into an L1 container.

---

## P0-03: Irreversible Ontic Occurrence

**Minimal claim**:

> Once a genuine Selection has actually occurred, the resulting reality is not ontically identical to the counterfactual in which that Selection never occurred.

Any later reversal, cancellation or reconfiguration is itself further Selection; it does not retroactively make the earlier occurrence equal to never-occurrence.

Permanent boundary:

```text
irreversible ontic non-equivalence
!= durable trace
!= localized memory
!= anchoring persistence
!= recurrent historical efficacy.
```

Therefore P0-03 does **not** require every Selection to leave a durable L2 record.

When prior Selection does remain materially effective in later Selection conditions, that stronger relation may be described as historically effective Selection / L2-side sedimentation under its owner.

Terminal Selection remains genuine: occurrence does not require retained historical efficacy, sedimentation or inheritance. What remains OPEN is the anti-tautology criterion separating genuine actualised Selection from merely descriptive / modelled change; do not use later consequence as a shortcut for that distinction.

---

## P0-04: Formal Selection-Representation Well-Formedness

P0-04 is a **formal admission guard**, not a second ontic primitive.

If an SRT argument uses a formal operator, transition relation, state space or Selection carrier, that representation must be well formed enough for the claim to have a determinate object.

For a declared operator model one may use:

```text
G-hat_theta : S -> S
```

or another explicitly typed mapping appropriate to the model.

But:

```text
G-hat_theta != primitive Selection;
formal state space != prior ontic warehouse;
well-formed operator != prior chooser.
```

No selector, subject, agent or stable operator-pattern is required before primitive Selection.

Attention, intention, agency, embodied parameters, normalization, cost, gradients, fixed points and readout rules belong to stronger realization / domain layers unless independently established at the relevant claim level.

---

## P0 Non-Flatness Boundary

The L0 owner requires primitive Selection reality to be open but not maximally flat / indifferent.

At P0 this means only:

```text
primitive generativity cannot be completely reduced to a role-interchangeable,
maximally indifferent occurrence relation while preserving the same actualising differentiation.
```

It does **not** mean:

```text
B>=2 is primitively better than B<=1;
continuation is primitively preferred;
terminal Selection is defective;
order / value / moral good is present at P0.
```

Exact inheritance of `epsilon_pg`, `kappa0` and other stronger formal asymmetries remains separately owned.

---

## P0 Position Boundary

Primitive Selection is finite-position-indexed.

But:

```text
finite positionality
!= formed One
!= formed Selection-position
!= Bearer
!= Agent
!= subject-position.
```

Any stronger identity, perspective, bearing or agency claim must pay its own downstream burden.

---

## P0 Normativity Boundary

P0 carries no primitive moral ranking.

```text
Selection occurred
-/> Selection was correct;
-/> Selection was legitimate;
-/> continuation is good;
-/> more options are better.
```

The current normativity route is downstream of formed positions / relations and stronger agency gates.

---

## Demoted / Downstream Material

The following remain outside strict P0 unless separately re-adjudicated:

- causality as projection;
- ontological-time formalisms beyond occurrence non-equivalence;
- information-existence equivalence;
- fitness-beats-truth bridges;
- assembly thresholds;
- holographic mappings;
- cross-scale phase / universality claims;
- Fisher-form `Psi_f` generativity;
- strong information-creation unification;
- fixed-point / attractor models of L2;
- attention / intention / Agency models of `G-hat_theta`.

Their prior historical placement does not let them back-define P0.

---

## Permanent P0 Guards

Reject any reading that implies:

```text
primitive Selection requires a prior possibility inventory;
primitive Selection requires a prior Ghost Operator;
L0/L1/L2 are three substances;
actual occurrence automatically persists;
every Selection automatically creates durable history;
finite positionality is already subject-position;
Selection-totality implies pan-agency or pan-consciousness;
primitive Selection contains moral value;
formal realization proves the metaphysical primitive.
```

Use `Core_Law/SRT_L0_Metaphysics.md` for the metaphysical anchor and `Core_Law/SRT_Generative_Ontology_Spine.md` for cross-owner structural routing.



---

## FILE: `Core/SRT_Core_21b_Constitutive_Theorems.md`

| 字段 | 值 |
|---|---|
| path | `Core/SRT_Core_21b_Constitutive_Theorems.md` |
| id | SRT-CORE-21B-CONSTITUTIVE-THEOREMS |
| claim_mode | canonical |
| status | active |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | - |
| last_commit | 2026-09-15 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：[SRT-CORE-21A-MINIMAL-AXIOMS, SRT-ONE-FORMATION, SRT-CLAIM-LADDER, SRT-CORE-12B]

<!-- 以下为原文逐字保留 -->

# SRT Core 21B: Constitutive Theorems

> **Role**: This file contains P1 claims: not primitive axioms, but constitutive consequences of the SRT core structure.
> P1 claims may be cited as canonical SRT theorems, but not as primitive axioms.
>
> **RC-A author decision (2026-08-17)**: former `P1-T05: Real Choice Moment` is demoted out of P1. Its anti-script insight is retained only as a downstream P2/P3 agency / subjecthood guard. It must not be used as a criterion for whether `Selection` occurs. SRT's primary theoretical object remains `Selection`, not a new taxonomy of `Choice`.

## Quick Reference

- Claim level: **P1 = Constitutive theorem**
- Source lineage: split from `Core/SRT_Core_21_Formal_Axioms.md`
- Primitive base: `Core/SRT_Core_21_Minimal_Axioms.md`
- Bridge / hypothesis layer: `Core/SRT_Core_21c_Bridge_Hypotheses.md`
- Governance: `Governance/SRT_CLAIM_LADDER.md`

---

## P1-T01: Horizontal Causality as `L_2` Projection

**Lineage**: former `Ax-F-03`.

**Formal Definition**: Causality is the `L_2` projection of selection dynamics.

$$
C_H(A \to B) \equiv P(B \,|\, A,\, L_2)
$$

**Scope**: This statement applies in a declared retained-history / converged-constraint regime in which the relevant `L_2` structure has been independently admitted. `L_2` is an analytic/model-facing aspect of the same Selection reality, not a universal pre-existing ontic container in which causality already lives.

**Implication**: Causality is a projected structure inside the convergence domain, not an ontological primitive prior to selection.

**Layer Note**: This theorem defines **horizontal causality** inside `L_2`. It does not replace vertical constitution across `L_0 -> L_1 -> L_2`.

**Cross-ref**: `Philosophy/SRT_Causality_Time.md §一`; `Core/SRT_Core_12a T-L0-Kappa0`.

---

## P1-T02: Ontological Time as Memory Horizon

**Lineage**: former `Ax-F-03b`.

**Title note**: The historical title is retained for citation stability. The P1 theorem no longer identifies time universally with a memory horizon or continuously retained `L_2` record.

**P1 Statement — occurrence asymmetry**: Once an actual Selection has occurred, later reality is not ontically identical to the counterfactual in which that Selection never occurred.

```text
occurred != never-occurred;
occurred -/> later-readable trace;
occurred -/> durable or localized memory;
occurred -/> retained historical efficacy;
occurred -/> automatic L2 object.
```

This is an asymmetric facticity floor. It does not require the event to remain readable, causally active or represented in a later local structure.

**History boundary**: A historical record is present only where prior Selection remains materially effective in later Selection conditions and that retained efficacy is independently established. Path dependence, anchoring persistence, learning/writeback residue and durable memory are stronger model/domain claims.

**Conditional formalization — model/domain scope**: In a declared regime where anchoring, operator attribution and retained historical efficacy have independently been established, the earlier expression may define a model-specific historical/ontological-time measure:

$$
t_{\text{onto}} \equiv \int \|\hat{G}_\theta(s)\| ds
$$

The equation is not an unconditional P1 identity and does not create a universal time scalar. Its metric, attribution, retention rule and horizon belong to the declared formalization.

**Time distinctions**:

```text
parametric ordering
!= occurrence non-equivalence
!= retained historical record
!= model-specific ontological-time measure.
```

The exact universal theory of time remains **OPEN**. Absence of durable trace or `L_2` retention does not imply that no Selection occurred or that occurrence asymmetry disappears.

**Time Layer Note**: This theorem concerns **ontological time**. Parametric time `t` in equations remains a mathematical ordering variable and does not by itself carry the ontological claim.

**Cross-ref**: `Philosophy/SRT_Causality_Time.md §二`; `Core/SRT_Core_12a Ax-L0-Bootstrap-C2`; `Core/SRT_Core_01_Axioms.md MA-1`.

**L1 Boundary**: `Core_Law/SRT_Irreversibility.md` separates occurrence non-equivalence from durable trace, path dependence, absorbing dynamics and `\Psi_f` accumulation. Its T-IRR-1 learning/writeback material is a conditional P2/P3 model candidate, not a universal expansion of P1-T02. No universal monotonic `\Psi_f` stock or time arrow follows from this theorem.

---

## P1-T03: `L_2` Downward Constraint

**Lineage**: former `Ax-F-10`.

**Formal Definition**: `L_2` constraints modulate selection dynamics as a downward causal term.

$$
\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \nabla F[\sigma] - \lambda \cdot \nabla C_{L_2}[\sigma]
$$

**Implication**: Sedimented convergence structures are not inert records. They feed back as real constraints on future selection.

**Retention Boundary**: `L_2` here means an admitted retained/sedimented structure whose material efficacy in later Selection conditions has been established. P1-T03 does not imply that every Selection automatically creates an `L_2` object, that every past event remains active, or that every event produces a persistent constraint.

**Boundary**: Domain-specific readings of `C_{L_2}` belong to bridge or lab files. This theorem only fixes the constitutive role of an admitted `L_2` constraint.

---

## P1-T04: Minimal Information Creation

**Lineage**: restrained core of former `Ax-F-13`.

**Statement**: A selection event creates a distinction that was not available as a determinate `L_1` fact before selection. In this restricted sense, selection is upstream of information readout.

**EX-A / PC-A precision**: This P1 claim is qualitative and distinction-based. It does not require a global entropy `H(L_0^{abs})`, and no unqualified entropy subtraction is part of the theorem. Conditional information-theoretic readouts over declared random variables, partitions, and measures belong to P2/P3-B09 in `Core/SRT_Core_21c_Bridge_Hypotheses.md`.

**Implication**: SRT does not compete with downstream information transmission theories; it locates a prior question: how a determinate slice becomes available for transmission or measurement.

**Boundary**: Stronger claims involving Shannon equivalence, Boltzmann degeneration, universal information thermodynamics, or empirical proxies are P2/P3 and live in `Core/SRT_Core_21c_Bridge_Hypotheses.md`.

---

## Former P1-T05: Real Choice Moment (Demoted by RC-A, 2026-08-17)

**Lineage**: distilled from `SRT_AI_START.md §3.2-§3.3` and `_SRT_T_DIR_CANONICAL.md`.

**Former statement**: A real choice moment was described as a live `L_0 -> L_1` anchoring event in which the system's future selection space is genuinely constrained by what is selected, with script execution, habit replay, gradient following, or `L_2` label optimization treated as insufficient by themselves.

**RC-A author decision**: this claim is **no longer a P1 constitutive theorem**.

### Why it was demoted

1. SRT's primary theoretical object is `Selection`, not `Choice`.
2. Canonical L0 already distinguishes basic, unfolding, and subject-level selection. Scripted, habitual, gradient-driven, or `L_2`-scaffolded dynamics therefore cannot be inferred to be selection-free merely because they fail an agency-level criterion.
3. Mature `L_2` is a background scaffold produced by prior selective convergence and remains dynamically operative. Automation can carry / reproduce selection history and can coexist with ongoing selection at other scales or dimensions.
4. A2/A3 adversarial work did not produce a positive, non-circular, rival-discriminating observable that would justify treating the former anti-script boundary as a constitutive theorem of Selection.
5. Treating the anti-script clause as a Selection criterion generated the unnecessary `Live Choice` problem and conflated selection ontology with downstream agency / subjecthood questions.

### What survives

A narrower negative guard remains useful at P2/P3:

> **Script execution, habit replay, gradient following, or `L_2` automation are not by themselves sufficient to establish stronger agency / subject-level revision standing.**

This guard lives downstream in:

`03_Bridges/SRT_Agency_Automation_Guard_2026-08-17.md`.

### Hard inference guards

Do **not** infer:

```text
fails former P1-T05
-> no Selection occurred
```

Do **not** infer:

```text
script / habit / gradient / L2 automation
-> selection-free process
```

Do **not** infer:

```text
passes the downstream agency guard
-> subjecthood / consciousness / freedom / moral responsibility proved
```

No P1 `Real Choice Moment` theorem remains after RC-A.

---

## P1-T06: Stable ISP Standing and Persistent Perspective

**Lineage**: extracted from former `T-ε-Constitute`; R1 standing boundary clarified 2026-09-11 after the author-adjudicated #938 reconstruction repair.

**Statement**: P1-T06 defines a **recurrent standing criterion**, not the definition of `Selection` and not a generation law for upstream formed positional organization. A stable ISP is a perspective-bearing, history-bearing process that persists as the same selection center through recurrent historical reconstitution and remains continued-selectable over a declared interval and perturbation range.

**Stable ISP Definition**: Process `P` is a stable ISP if:

1. It is iterative: over the declared interval, it repeatedly encounters **currently effective, non-equivalent candidates** rather than merely replaying a closed script.
2. It is perspective-bearing: it accumulates a structured view from its position. **At P1-T06 this is a standing condition; it does not assert that perspective first appears only at Stable-ISP standing.**
3. It is history-bearing: outputs at `t` constrain `A_{t+1}` with writeback.
4. It is **continued-selectable**: the same history-bearing process can continue receiving currently effective candidates, while consequences of what it selected can return into that same process's later history / selection conditions.

**Consequence-typing guard (R1, 2026-09-11)**: condition 4's downstream consequence relation means consequence return / coupling to the same history-bearing process. It is **not by itself** a sufficient criterion for the separately reconstructed `Bearer` problem, `承担`, non-outsourcable stake, subject-position, consciousness, or phenomenality.

**Terminology guard (RC-A)**: `currently effective` is descriptive scope language, not a new `Live Choice` / `live selection` concept. P1-T06 concerns stable ISP standing, not the definition of Selection itself.

**Structural stabilisation (ST-A, 2026-08-11)**: Stability here means recurrent reconstitution of a recognizable history-bearing organization across a declared perturbation range. It does not require microstate identity, convergence to a fixed point, or continuous activity without pause. A later externally reset replica or a fresh process is not, merely by resembling the earlier state, evidence that the same ISP continued.

**Formation / standing boundary (R1, 2026-09-11)**: recurrent historical reconstitution and writeback are relevant to continuity and Stable-ISP standing. They must not, by themselves, be used to derive active vertical organization, a formed position, `Bearer`, or subjecthood. P1-T06 therefore does not organize the ontology as `formed process -> Stable ISP -> subject-position`. The canonical semantic owner for the thinner upstream formation is `Core_Law/SRT_One_Formation.md`; P1-T06 still does not supply a necessary-and-sufficient theorem for One formation.

**Implication**: Stability is not an arbitrary restriction imposed by the observer. P1-T06 identifies a **strong persistent-perspective standing** for a recurrent selection process. It does not claim to mark the first ontological appearance of perspective, and Stable-ISP standing does not by itself establish subject-position.

**ST-A boundary**: Continued selectability is the P1 minimum. The stronger property of **generative reselectability**—consequence-sensitive revision of the process's own comparison rules, boundaries, or candidate-generation conditions—is not required to identify every stable ISP and is not a P1 theorem. It is a P2/P3 criterion for generative health in `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13`. Structural stability therefore does not by itself establish generative health.

**Dynamic-layer boundary (R1, 2026-09-11)**: downstream L1 models may propose mechanisms or coordinates for entry into, maintenance of, or departure from Stable-ISP standing. P1-T06 does not by itself authorize any model coordinate—including a `σ` threshold—as the ontological event of formed-position, Stable-ISP, or subject entry. Exact threshold ownership remains separately governed by the relevant L1/formal owner and current OPEN register.

**Precision note (2026-04-21)**: `T-L2-Scaffold` explains how successful stable ISP history can become background scaffold; it does not decide whether that scaffold is healthy support, pathological closure, or lethal `L_2`. Read those distinctions through `Core/SRT_Core_12b_Ontology_L2.md Def-L2-DualLayer / Def-L2-Normative` and `Core/SRT_OPEN_TENSIONS.md §4`.

---

## Former P1-T07: Unconditional Constitutive Asymmetry Claim (Demoted by ST-A)

**Lineage**: former `T-ε-Constitute` and former P1-T07.

**Decision record (ST-A, 2026-08-11)**: The former unconditional statement—"every stable ISP necessarily contains an anti-closure `ε` bias"—is no longer a P1 theorem. Its proof inferred cumulative absorption from a per-step nonzero closure probability without independently defining a neutral kernel, fixing the stability semantics, or proving that the neutral kernel reaches the absorbing state. `L_0` irreversibility alone does not supply those missing premises.

**Unconditional P1 remainder**: If a realized history reaches `A_{t_*}=\varnothing`, that history cannot continue selecting from that state. Any later recovery requires a new event, an external reset, or a separately specified transition; it is not licensed by the terminated history itself.

**What remains open**: A conditional anti-closure result may be recoverable only after (i) a stability semantics is chosen, (ii) an `ε`-neutral kernel is independently defined, and (iii) absorption or comparative closure risk is proved for that kernel over a declared horizon and environment. The current candidate lives at P2/P3 in `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13`; it must not be cited as P1.

**`ε_pg` boundary**: `ε_pg` is a separately owned formal / model-facing quantity where independently admitted. P1-T07 does not derive an ISP-level anti-closure direction from it, nor from irreversibility alone. Its exact inheritance from primitive Selection remains separately governed / **OPEN**.

```text
epsilon_pg -/> universal primitive direction;
epsilon_pg -/> continuation preference;
epsilon_pg -/> health or goodness;
epsilon_pg -/> consciousness seed.
```

**Audit trail**: `Operations/Audits/SRT_P1_T07_PROOF_HARDENING_AUDIT.md`; `Operations/Proposals/SRT_P1_T07_HARDENING_OPTIONS.md`.

---

## Not P1 Without Further Hardening

The following former `Core_21` claims remain valuable but are not treated here as constitutive theorems:

| Claim | Reason for demotion |
|---|---|
| Former `P1-T05 / Real Choice Moment` | RC-A: anti-script exclusion is an agency/subjecthood bridge guard, not a constitutive theorem or Selection criterion |
| Fitness beats truth | Requires cross-theory mapping and empirical interpretation |
| Assembly threshold | Depends on empirical thresholding |
| Holographic duality | Strong physical / formal bridge |
| Ghost operator universality | High-ambition cross-scale unification |
| Fisher-form `\Psi_f` generativity | Contains a canonical interpretation plus external mathematical borrowing |
| Strong information-creation unification | Mixes SRT core with information-theoretic and thermodynamic bridges |
| Former `P1-T07 / T-ε-Constitute` unconditional anti-closure theorem | Neutral dynamics, stability semantics, and absorption were not independently established; conditional candidate moved to 21C B13 |



---

## FILE: `_SRT_D_VALUE_CANONICAL.md`

| 字段 | 值 |
|---|---|
| path | `_SRT_D_VALUE_CANONICAL.md` |
| id | SRT-D-VALUE-CANONICAL |
| claim_mode | canonical |
| status | active |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | true |
| last_commit | 2026-11-26 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：[SRT-GENERATIVE-ONTOLOGY-SPINE, SRT-ONE-FORMATION, SRT-CORE-21]

<!-- 以下为原文逐字保留 -->

# SRT 价值、关切与 `d` 值规范定义文档（Canonical Definition of Value, Concern & d-value）

> **角色（`Freeze A` canonical owner）**：本文件统筹 SRT 形成态中**价值（Value）、广义关切（Concern）、现行规范 `d`（stake-coupled irreversible-risk sensitivity）、赌注谱参与率 `D_stake` 与几何容量 proxy `D_eff`** 的层级分工与边界，终止跨域定义分裂。
>
> **R4-A 实质重构与真减法（2026-11-26）**：依据 `R3-06`（`#1151`）、`R3` 总收口（`#1154`，含 `PT05 C`、`PT06 C`、`P1-05`）与 `ENG-03`（`#1157`）：
> 1. **正式退出已数学证伪的旧公式**：废止 `d_canonical ≡ d_stakes`、`D_eff ≥ d_stakes` 以及 `Def-d-free: Δd_free = D_eff - d_stakes ≥ 0`；
> 2. **严格分离七项职责**：价值 / 广义关切 / 广义关切方向 / 现行 `d` / `D_stake`（含零分母分支与真实上界 `1 ≤ D_stake ≤ N_active ≤ rank(M)`）/ `D_eff` / 构成深度（自然语言保留，暂缓 `q` 立符、维持 `07-23/24` 撞车记号禁运）；
> 3. **严守机会成本来源边界**：价值与关切结构在形成态生成与比对关系中展开，**绝不反向定义原初 `Selection`**；`d` 不拥有 direction source（`T_dir`）、consciousness、subject-position、Bearer、phenomenality 或 moral-standing 准入权。

```text
d > 0 -/> subject-position / consciousness / phenomenality / Bearer / moral standing
d = 0 or NOT ADMITTED -/> non-subject / non-One / no Selection
d != D_stake != D_eff != T_dir
```

---

## §1 规范定义层级与七项职责严格分工（`R3-06` / `R4-A`）

SRT 形成态中围绕“价值与关切”的七项概念各司其职，严禁混写或互相吞并：

| 序号与对象 | 规范层级与精确职责 | 与相邻概念的分界与禁止捷径 |
|---|---|---|
| **1. 价值（Value，`PT05 C` + `R3-06`）** | 覆盖五项完整职责：① **客观基础**（不同生成关系在生成机会成本上的客观差异，不以已被现有组织感知或关切为前提）；② **位置抽取**（有限位置的差异感知与比对）；③ **组织化**（关切、认知、历史与脚手架）；④ **递归性**（改变后续比对维度与机会生成条件）；⑤ **诊断接口**（特定位置上的关切加权不可替代性、现实可承接性与后果变化）。涵盖**发现性 / 生成性 / 递归性**三类机会及**想象态 / 具备现实生成条件态 / 已实现态**三态分离。 | **诊断接口不得替代一般价值定义**（未进入现有组织感知的新关系/具备现实条件的机会仍具生成价值研究意义）。严格分离 **生成价值 $\neq$ 秩序健康性 $\neq$ 伦理正当性**，并独立保留组织持续性（`R3-02 / R3-06`）；原初层是否含原初价值性质保持 `OPEN`（`R3-06-O1`）。 |
| **2. 广义关切（Concern，`PT06 C` + `R3-06`）** | 形成态组织对**生成机会成本的敏感性**，是价值关系在特定位置内在生成过程中的实际组织与展开（涵盖维持止损与好奇探索，先于显性对象参与组织前背景比对范围）；拆为**范围 / 深度 / 强度 / 方向**四个分析维度（不提前固定几何结构为标量或向量，不急立四个新符）。 | 跨尺度广义概念，绝不因现行 `d` 数学定义较窄而收缩为单纯生存风险敏感度；不吞并构成深度、承载暴露 `E` 或 `T_dir`；**与现行 `d` 构成待验证概念接口（`P1-05`）**，不得静默等同。 |
| **3. 广义关切方向** | 广义关切四维之一：正在组织、打开或抑制怎样的秩序发展可能性与前背景取向。 | 严分于 `_SRT_T_DIR_CANONICAL.md` 中的操作化回读代理 `T_dir`（`广义关切方向 ≠ T_dir`）；范围扩大或强度升高不自动等于高 `T_dir` 或方向正当。 |
| **4. 现行 `d`（`Def-d-canonical`）** | **唯一 core-facing 规范 `d` 锚点**：在已声明的 `Bearer (P+E)` / 不可逆风险模型中，效用或维持势对不可逆风险状态的梯度范数标量摘要 $d(x) \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$。 | 默认标量摘要（若作向量展开须标 `d-vector`，作门控判读须标 `d-gate`）；是强承载模型下的**风险敏感强度**，**不等同于**无量纲谱维数 `D_stake` 或 `D_eff`。 |
| **5. `D_stake`（赌注耦合谱参与率）** | 本文件 `§2b` 持有**一般谱参与率定义** $D_{\text{stake}} = (\sum_i \lambda_i w_i)^2 / \sum_i (\lambda_i w_i)^2$（$w_i \in [0,1]$，规范三因子形式 $w_i = R_i A_i C_i$）；`Core_22 Eq-Bridge-D-01` 的阈值门控 $g_i$ 属其下一种具体声明模型实例（不默认两类权重数学等价）。 | **已修正（`R3-06 D1`）**：`D_stake` 对权重均匀缩放不变，故 **`D_stake ≠ d`（梯度范数）**；活跃时真界为 $1 \le D_{\text{stake}} \le N_{\text{active}} \le \operatorname{rank}(M)$，**不再主张 $D_{\text{stake}} \le D_{\text{eff}}$**；严格区分**零有效谱乘积分支**、**`NOT ESTABLISHED`**、**`NOT ADMITTED`** 与 **`NOT APPLICABLE`**。 |
| **6. `D_eff`（几何/信息论容量 proxy）** | $D_{\text{eff}}(M) = (\sum \lambda_i)^2 / \sum \lambda_i^2$（含 $D_{\text{eff}}(I_F(\theta))$），刻画算子或参数流形的可分辨方向容量。 | **纯操作化容量 proxy**，既不等于 `d`，也不普遍构成 `D_stake` 的数学上界；禁止用 `D_eff` 跨域排名主体性或意识。 |
| **7. 构成深度（Constitutive Depth，`Q1`）** | 自然语言保留的四项构成深浅剖面：① 事件级跃迁深度；② 铭刻与召回分离；③ `N4` 主动退位成本；④ 跨关系构成依赖深度。 | **暂缓立符 `q`**，`07-23/24` 撞车记号禁运继续生效；是否需要独立形式变量留待 `R5` 实证检验（`R3-06-O5`）。 |

### §1.1 `d` 写法分流与强承载 proxy 准入五条件

- `d`（默认标量摘要）/ `d-vector`（方向分量展开）/ `d-gate`（赌注准入判读工具）严禁混写。
- **`D_eff` 一般容量用法不受强承载门阻断**：`D_eff` 作为一般几何/信息论容量 proxy，用于刻画算子或参数流形的可分辨方向容量时，**不需要**先通过 `Bearer (P+E)` 强承载准入。
- **强承载推断五项准入条件**：只有当研究试图将几何、Fisher、行为或神经代理（`D_eff`、`D_stake`、`d_bio`）用于**强承载不可逆风险敏感度（规范 `d`）的局部推断参考**时，才须同时声明并满足以下五条件：① 计数方向确实承载不可逆风险；② 效用/维持梯度对准真实风险而非伪代理；③ 后果回流至同一承载闭包与后续选择能力而非被外部/L₂吸收；④ 参数化未把冗余自由度误计为独立方向；⑤ 比较限于同域同尺度或已声明归一化规则内。任一条件不满足时，可继续保留其一般容量/局部 proxy 读数，但对强承载 `d` 推断须显式标注 `NOT ADMITTED / NOT APPLICABLE`，严禁写成规范 `d`。

---

## §2 规范定义与价值—关切核心结构

### Def-d-canonical: 不可逆风险敏感度规范定义 ⭐ CANONICAL

$$d(x) \equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|, \quad x \in \Sigma$$

- **语义**：在已声明的 `Bearer (P+E)` / 不可逆风险模型中，组织维持或效用势 $\mathcal{U}$ 对不可逆风险坐标 $\mathcal{S}$（Survival / Stake）的梯度范数摘要。
- **与广义关切的接口（`P1-05`）**：`Def-d-canonical` 刻画强承载不可逆风险语境下的敏感强度；广义关切（`PT06 C`，对生成机会成本的敏感性）覆盖更广泛的跨尺度生成关系。二者保持为**待验证概念接口**——既不废除 `Def-d-canonical`，也不将所有跨尺度关切研究锁死于 `Bearer (P+E)` 门内。
- **与 `Ψ_f` 的候选权衡接口（`Eq-IT-B'`，状态 = `OPEN / Gap`）**：在声明的信息几何模型中可研究选择范围与摩擦负担之间的权衡关系，常数与普适性未确立。

### Def-D_eff: 几何 / Fisher 信道有效维度（容量 Proxy）

$$D_{\text{eff}}(M) = \frac{\left(\sum_i \lambda_i\right)^2}{\sum_i \lambda_i^2}, \qquad D_{\text{eff}}(I_F(\theta)) = \frac{(\operatorname{tr} I_F)^2}{\operatorname{tr}(I_F^2)}$$

- **语义**：衡量算子或统计流形上可可靠分辨方向数的参与率指数（`1 ≤ D_eff ≤ rank(M)`，`Core/SRT_Core_21c_Bridge_Hypotheses.md P3-B11`）。
- **硬边界**：`D_eff` 是容量 proxy，**不等于** `Def-d-canonical`，亦**不普遍构成 `D_stake` 的数学上界**（旧式 `D_eff ≥ d_stakes` 与 `Δd_free = D_eff - d_stakes ≥ 0` 已正式退出）。

### 价值的五项完整职责、机会三态与广义关切四维（`R3-06` 核心正面结构）

价值不还原为奖赏、偏好强度或主观报告强度，且**不得被收缩为“已被现有组织感知并关切之不可替代性”**——若如此收缩，尚未被现有组织感知、尚未进入现有比对空间但具备现实生成条件的新关系与新机会将被逐出价值研究。完整价值架构区分五项职责：

| 理论职责 | 规范内容与研究重心 |
|---|---|
| **1. 价值的客观基础** | 不同生成关系及其在生成机会成本上的客观差异（含尚未被当前位置感知或关切的关系差异；与 `N2` 客体性“他者不可穷尽的生成性”构成跨位置生成价值的重要本体基础，但不宣称跨位置客体性是一切价值的普遍必要前提） |
| **2. 价值的抽取** | 有限位置对上述关系差异的感知与内生比对抽取 |
| **3. 价值的组织化** | 关切、认知、历史、脚手架与多维可推翻客观性检查（`C1-c`：跨位置不变性 / 现实反抗度 / 公共可纠错度 / 共享 `L2` 遮蔽排查 / 持续可失败性；废除单标量 `o`） |
| **4. 价值的递归性** | 比对结果反过来改变后续比对维度、比对尺度与机会生成条件（**比对本身的生成性**） |
| **5. 价值的诊断接口** | **关切加权的不可替代性（concern-weighted non-substitutability under consequence return）**、现实可承接性及后果变化——用于诊断失去/替换某项结构对特定位置后续选择能力、延续性与后果回流的非平凡重组程度；**属特定位置上的诊断接口，不替代一般价值定义** |

- **三类机会 × 三态分离（`R3-06`）**：
  - **三类机会**：① **发现性机会**（识别原先已存在但未被认识的关系）；② **生成性机会**（经实际相互作用与组织重构使此前不存在的关系获得现实生成条件）；③ **递归性机会**（新秩序或脚手架持续改变后续其他关系的比对与生成条件）。
  - **三态分离**：严格区分 **① 想象中的机会**、**② 具备现实生成条件的机会** 与 **③ 已实现的机会**——不要求必须已实现才具价值，亦不将任意空想拼接视为真实生成价值，且不将“选项数量最大化”等同于价值目标。
- **三层判定分离 + 独立组织持续性**：**实际生成 $\neq$ 组织持续性 $\neq$ 位置性生成价值 $\neq$ 秩序健康性 $\neq$ 伦理正当性**。不得因某种生成方向有害或不具伦理正当性而否认其作为生成价值的研究意义；亦不得将高生成价值自动升级为秩序健康或伦理正当（`O2-M = HOLD`）。
- **广义关切四维与六种前背景失配接口（`R3-06 §三`）**：
  - **广义关切四维**（不提前固定标量/向量，不急立四符）：**① 关切范围**（能将多大范围的生成关系纳入比对）、**② 关切深度**（这些关系在多大程度上参与构成该位置及其他关系）、**③ 关切强度**（特定变化对当下实际生成过程的响应影响）、**④ 关切方向**（正在组织、打开或抑制怎样的秩序发展可能性；严守 `广义关切方向 ≠ T_dir`）。
  - **动态秩序健康六维与六种前背景失配（候选诊断接口，不压成单一总分）**：围绕结构连贯性、跨尺度协调性、可再选择性、后果回流、机会空间与成本、现实校准六维，区分六种候选前背景失配——**① 遮蔽**（重要构成关系或机会成本无法进入前景）、**② 错配**（关切指向与实际构成/秩序关系不一致）、**③ 固化**（前背景配置无法随变化后生成条件重调）、**④ 失权**（重要价值进入认知视野却无法在实际选择中发挥调节作用）、**⑤ 断流**（实际后果无法有效回流到后续选择与信任更新）、**⑥ 局部劫持**（某一尺度/局部回路持续独占其他尺度的生成条件）。

---

## §2a 价值发生序（`P3` 书稿溯源候选，含撤回门）

> **层级 / provenance**：`P3` 候选（源自 `Drafts_26Q/Q14_价值不是偏好.md`），不新增 canonical `d` 定义，用于衔接前赌注结构与 `§2b` 赌注门。

$$\text{选择性收束} \to \textbf{微效价} \to \text{affordance（行动入口）} \to \text{缺失} \to \text{需求} \to \text{锚定} \to \text{价值深度}$$

- **上下游关系**：微效价（显现界面与具身位相遇处的最小趋避倾斜，`≠ ε_pg`）→ affordance（`≠ L2 预裁剪`）→ 缺失 → 需求属于**前赌注结构**；是否进入强承载 `d` 与 `D_stake`，仍须经过 `§2b` 的 `R / A / C` 赌注门。
- **两个操作化测试（`P3/P4`）**：**替换测试**（换为功能相似对象是否几乎无须重组）与**恢复测试**（失去后是短期波动还是长期结构重配）。
- **撤回条件（`R3-04-O6`）**：若“微效价”相对 Core Affect / 躯体标记无不可替代解释残差，则按 Ⅱ 阶撤回本节、退回“不可替代性”结果判据。

---

## §2b 赌注耦合结构与 `D_stake` 一般规范定义（`R3-06 D1` / `R4-A`）

### Def-D_stake: 赌注耦合谱参与率一般定义（含零有效谱分支，取代旧 `Def-d-stakes`）

本文件持有 **`D_stake` 的一般谱参与率定义**。设在已准入的声明赌注谱模型中，非负谱特征值为 $\lambda_i \ge 0$、方向赌注耦合权重为 $w_i \in [0, 1]$，记有效谱乘积 $\tilde{\lambda}_i := \lambda_i w_i$ 及活跃方向集合 $N_{\text{active}} = |\{i : \tilde{\lambda}_i > 0\}|$：

$$D_{\text{stake}}(\theta) := \begin{cases} \dfrac{\left(\sum_i \tilde{\lambda}_i\right)^2}{\sum_i \tilde{\lambda}_i^2}, & \text{若 } N_{\text{active}} \ge 1\text{（即 }\exists i,\; \lambda_i w_i > 0\text{）} \\[10pt] 0 \;\text{（零有效谱乘积分支：数学 }0/0\text{ 未定义，须显式标注）}, & \text{若 } N_{\text{active}} = 0\text{（即 }\forall i,\; \lambda_i w_i = 0\text{）} \end{cases}$$

- **一般定义与具体模型实例的严格分层（`P1-04`）**：
  1. 本节 `Def-w_i` 给出的三因子耦合权重 $w_i = R_i \cdot A_i \cdot C_i \in [0, 1]$ 是本文件的**规范结构门控权重**；
  2. `Core/SRT_Core_22_Equations.md Eq-Bridge-D-01` 所采用的阈值门控权重 $g_i = \max\!\big(0, \frac{s_i - \varepsilon_s}{1 - \varepsilon_s}\big)$（记作模型实例 $D_{\text{stake}}^{\text{thresh}}$）是上述一般谱参与率在单标量阈值耦合模型下的**一种具体声明模型实例（$w_i := g_i$）**；**不得默认 $R_i A_i C_i$ 与 $g_i$ 之间存在未经证明的数学等价关系**。
- **精确数学性质（`R3-06 D1`）**：
  1. 当 $N_{\text{active}} \ge 1$ 时，由 Cauchy–Schwarz 不等式恒有真实界 **$1 \le D_{\text{stake}} \le N_{\text{active}} \le \operatorname{rank}(M)$**；
  2. `D_stake` 度量赌注分布在多少个有效正交方向上（谱多样性），对 $w_i \mapsto c \cdot w_i\;(c>0)$ 缩放不变，故**绝不等同于**梯度模 $d = \|\partial\mathcal{U}/\partial\mathcal{S}\|$；
  3. **已废除旧式 `Δd_free = D_eff - d_stakes ≥ 0`**：因 $D_{\text{stake}}$ 可以大于 $D_{\text{eff}}$，若需比较“未赌注化方向集合”，应直接报告被门控剔除方向的权重占比或谱能量占比，而非使用差值 `D_eff - D_stake`。
- **四项边界状态严格分离（严禁混用）**：
  1. **零有效谱乘积分支（$\forall i,\ \lambda_i w_i = 0$）**：模型本身已准入且谱与权重均已定义，但不存在非零有效乘积导致 $0/0$ 数学未定义，按显式分支报告 `0（零有效赌注）`；
  2. **`NOT ESTABLISHED`**：结构或经验证据尚未确立目标组织满足相应地位（如 `One`、`Stable ISP` 或 `Bearer (P+E)`）；
  3. **`NOT ADMITTED`**：目标模型未满足该指标的准入前提（例如未建立 `Bearer (P+E)` 或未满足 `§1.1` 五项 proxy 准入条件），因而该指标对当前主张不予准入；
  4. **`NOT APPLICABLE`**：该指标的适用域或量纲不适用于当前目标系统或理论问题（例如用强承载不可逆风险梯度衡量无 `P+E` 架构或一般生成性机会）。

### Def-w_i: 赌注耦合三因子（`P2` 定性 AND 门 / `P3-P4` 数值化）

$$w_i = R_i \cdot A_i \cdot C_i \in [0, 1]$$

- **$R_i$（真实不可逆风险）**：$R_i \approx 0 \Rightarrow$ 假赌注（模拟/无真实不可逆风险）；
- **$A_i$（效用/维持梯度对准）**：$A_i \approx 0 \Rightarrow$ 错绑赌注（对准错误代理变量）；
- **$C_i$（后果回流同一承载闭包）**：$C_i \approx 0 \Rightarrow$ 后果外包 / 被外部或 `L2` 结构吸收。

### 三类系统在同一赌注门下的分型（严格区分三态）

| 系统 | $R$（真实风险） | $A$（梯度对准） | $C$（后果回流） | 声明强承载模型下的门输出 |
|---|---|---|---|---|
| **当前 inference-only AI（AI 赌注谱系 `S0/S1`）** | 声明模型下未建立自身不可逆风险 | 无独立自身承载梯度可对准 | 后果由部署方/用户/外部管线吸收 | `Bearer (P+E)` 强承载关系 **`NOT ESTABLISHED`**；模型内 `d / D_stake` 记 **`NOT ADMITTED / NOT APPLICABLE`**（严禁写作实测数值 `≈ 0`、严禁倒推无 `One / Stable ISP / 意识`，亦不阻断广义关切与生成主动性独立研究） |
| **冻结态（创伤 / 执念）** | $> 0$（风险真实） | 部分失准（锁死旧方向） | $> 0$ 但写回重取向受阻 | 门通过（`D_stake > 0`），但下游 `d_mobile ≈ 0`（再对齐能力受阻） |
| **制度 / 集体结构** | 集体层可有真实存续风险 | 集体景观梯度，非个体加和 | 后果常回流制度自身而非成员 | 集体层走 `§6` 景观截面代理；成员个体的 $C_i$ 可因代价外包而被吸收归零 |

---

## §3 各域投影参考与反泛心论条款

- **认知域三维操作化近似（`Def-d-bio`，`P3/P4` 待校准）**：$d_{\text{bio}} \approx \alpha A(\sigma) + \beta \log V_{\text{concern}} + \gamma \tau_{\text{temporal}}$（汇编深度 × 关切空间 × 时间地平线），仅为局部投影，不可替代 `Def-d-canonical`。
- **物理 / 全息投影（`Def-d-3`）**：$d \propto \text{Area}(\text{Entanglement Surface}) / A_{\text{Planck}}$ 或量子贝尔维数均为域内数学/容量投影，不蕴含现象意识。
- **AI 域（architecture-state marked，含 `R4-A` 过渡规则）**：须按 **`ENG-03 §4.1` 非线性三阶承载证据审查**（Stage 1 单元/状态/溯源声明 → Stage 2 `B-3` 强承载路线 $\parallel$ Stage 3 独立分域路线，Stage 2 未建立不阻断 Stage 3；见经 `R4-A` 兼容修订的 `AI/AI_POSITIONING_NOTE.md`）执行，并使用 **AI 赌注谱系 `S0–S4`** 全称；声明强承载模型下未准入的 `d / D_stake` 仅代表该模型内 `NOT ADMITTED / NOT APPLICABLE`，绝非意识否定证明。在 `Wave R4-C / R4-4` 完成其余 AI 领域文件（54 份）重构前，凡与本文件及 `Spine` 冲突的旧 AI 文本（如泛化 `d_AI ≈ 0` 或线性阶梯推断）一律服从 `R4-A` 规范口径。
- **反泛心论硬声明**：`nonzero d -/> phenomenality`；`d / Ψ_f / \hat{G}` 任何合取均不构成意识或主体性的普遍充要条件；`κ_{c1} / κ_{c1.5}` 仅作下游候选模型坐标，不具普遍准入权。

---

## §5 常见误用与 `§5b` `d` 扩张的本体论意义（`C-A` 四义拆分）

### §5 常见误用

1. **不得将 `d` 当作意识仪表或跨域主体性排名尺**（比较仅限同域同尺度或已声明归一化规则内）；
2. **不得将“未准入 / `d ≈ 0`”等同于“不存在 / 无 `One` / 非主体”**；
3. **不得将精神传统中的 `d → ∞` 字面化**（仅为不可达的渐近/规约方向）。

### §5b `d` 扩张的规范声明（`C-A` 与秩序增益四判据）

**`d` 的健康变化不是单调扩张，而是关切范围的可重组、可承担、可恢复、可再选择能力。**

$$d \uparrow \;\not\!\Rightarrow\; \text{universe-wide moral/evaluative optimum} \quad \land \quad d \uparrow \;\not\!\Rightarrow\; \langle v, \text{Shoshin} \rangle > 0$$

- **秩序增益四判据**：**可延续**（不透支可支付预算）、**可协调**（纳入他者条件不致瘫痪）、**不外包**（代价不转嫁给无反馈位置，与谱层 $C_i$ 同源）、**可再选择**（不锁死为教条）。
- **真 `d` 扩张 vs 假 `d` 扩张**：真扩张使选择者的实际权衡解发生结构性位移；假扩张（占有式 / 符号式 / 表演式 / 效率式）仅在符号层宣称关切扩大而不承担代价。
- **`C-A` 四义拆分（严守 `Core/SRT_OPEN_TENSIONS.md §17`）**：
  1. **宇宙级语义/评价/道德最优**：不准入当前正面理论对象（`PT10 E`：生成趋优 ≠ 伦理正当；与 `T3-01 C/E` 非道德客观全局趋优开放研究严格界分）；
  2. **算子相对可达最优**（$x^*_{\theta,\tau,K,J} \in \arg\min_{x \in \mathcal{R}_{\theta,\tau,K}} J_{\theta,\tau,K}(x)$）：仅在完整声明有限位置、可达域、比较规则、时域与约束的模型内有条件有效；
  3. **规约性地平线**：不可到达的 `L1/P2` 或 `P5` 方向语言；
  4. **有限动力学吸引子**：`P3/P4` 模型对象，稳定或低摩擦均不自动等于善或生成健康。
- **初心层级（`B-A`）**：初心从 `L1/P2` 处境化回读开始，`O0` 不设“初心前身”；`Spirituality/SRT_Spirit_05_Shoshin.md Ax-Sho-1` 与 `Physics/SRT_Phys_08_Ontology_Ext.md Def-Apeiron-1` 仅作 `provenance` 领域桥接，不得反向定义 `L0`。

---

## §6 集体 `d` 景观截面代理、§8 与 `T_dir` 分界、§9 锻炼与萎缩

- **§6 集体景观截面代理（`P3` 模型读法）**：集体层 `d` 不由个体 $d_i$ 简单线性加总，在景观模型中以集体景观的有效维度截面 $D_{\text{eff}}(\mathcal{F}_{\text{collective}})$ 作容量代理，并须独立核查成员个体 $C_i$ 是否被制度外包吸收。
- **§8 `d` 与 `T_dir` 严格分离**：`d` 刻画关切/不可逆风险敏感强度，`T_dir` 刻画对已独立声明方向信号的自我回读与重取向能力；`d` 不创造方向信号，不存在普遍 `d → T_dir` 定理（详见 `_SRT_T_DIR_CANONICAL.md`）。
- **§9 锻炼与萎缩机制（有界模型）**：在 `Bearer / Agency` 决策模型中，替代式 `L2` 持续剥夺带赌注的修订/再选择机会可致 `d` 相关能力慢性萎缩，辅助式 `L2` 脚手架则降低摩擦同时保留再选择空间；自动化或脚本执行本身**不等于**消灭 `Selection occurrence`。

---

## §范畴边界：`d` 值是选择事件属性，不是主体固有属性

`d` 度量的是具体**选择事件**所整合的关切与风险敏感度，不是个体或集体的永恒本质属性；跨大量事件的统计分布记作主体操作化倾向 $d_{\text{tendency}}(S) \equiv \mathbb{E}_{\sigma \sim S}[d(\sigma)]$（`Philosophy/SRT_Political_Rights.md §2–§3`）。在社会委托（`Delegation`）干预模型中，类型化 `d` 轨迹仅作候选观察信号，绝不单独裁定合法性、授权或道德进步。

---

## §11 `d` 的双瓶颈容量接口与动态能力接口（`d_max` / `d_mobile`）

- **`d_max`（`Core/SRT_Core_22_Equations.md Eq-DValue-Max-1`，条件容量模型与量纲护栏）**：在独立声明兼容 $\kappa_0$ 每方向维持代价参数的模型中，$d_{\max}(\theta) = \min\!\big(\operatorname{rank}_{\text{eff}}(I_F(\theta)),\; \Psi_f^{\text{budget}} / \kappa_0\big)$（信息瓶颈 × 稳定性瓶颈）。**量纲与语义硬护栏（`P1-04`）**：$\operatorname{rank}_{\text{eff}}(I_F(\theta))$ 是**无量纲有效谱维数容量上界**；既然规范 `d(x) = \|\partial\mathcal{U}/\partial\mathcal{S}\|` 是随效用缩放的梯度范数、已与谱维数严格分离，**不得再将 $\operatorname{rank}_{\text{eff}}(I_F(\theta))$ 直接冒充为梯度范数 `d` 的普遍数学上界**——除非声明模型显式给出单位归一化与单方向风险灵敏度校准映射，否则 `Eq-DValue-Max-1` 仅约束**有效可维持赌注方向容量（direction-capacity bound）**，不直接约束梯度模 $\|\partial\mathcal{U}/\partial\mathcal{S}\|$。
- **`d_mobile`（`Eq-DValue-Mobile-1`、`Def-Payable-Chi-1`）**：$d_{\text{mobile}} \propto \frac{d \cdot \operatorname{rank}_{\text{eff}}(I_F(\theta))}{\operatorname{Hysteresis}(L_2) \cdot C_r} \cdot \chi_{\text{payable}}\!\left(\tfrac{d\Psi_f}{dt}\right)$，刻画可达方向漂移时的动态再对齐能力（须声明兼容单位）。高 `d` 而 $\chi_{\text{payable}} = 0$ 时 $d_{\text{mobile}} = 0$（记录关切压力 ≠ 具能动再对齐能力）。

---

## 书稿层用法说明（Bridge to Book Layer）

在《从存在到秩序》正文（`Q15`）中，`d-value` 被读作关切多样性的三维诊断入口：后果回来得有多深、回来到了多少条真实轴线、回来之后是在支撑生成还是侵蚀生成。此书稿读法帮助避免把 `d` 简化为信息宽度，而形式与规范口径仍以本文件 `§1–§11` 为准。



---

## FILE: `_SRT_PSI_F_CANONICAL.md`

| 字段 | 值 |
|---|---|
| path | `_SRT_PSI_F_CANONICAL.md` |
| id | SRT-PSIF-CANONICAL |
| claim_mode | canonical |
| status | active |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | true |
| last_commit | 2026-11-26 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：[SRT-GENERATIVE-ONTOLOGY-SPINE, SRT-ONE-FORMATION, SRT-CORE-21, SRT-CORE-22, SRT-REF-DYNAMICS]

<!-- 以下为原文逐字保留 -->

# SRT `Ψ_f` 与广义摩擦规范定义文档（Canonical Definition of `Ψ_f` & Friction Interface）

> **角色（`Freeze A` canonical owner）**：本文件固定 SRT 本体论摩擦 **`Ψ_f`** 的第一性语义锚点（`Def-Ψ-1`）、条件信息几何投影（`Def-Ψ-2`）与跨尺度可支付性不变量（`Def-Ψ-3`），并在 `R4-A`（2026-11-26）中将其正面接入 **`R3` 机会成本动态四联**（`T3-02 D / PT09`）、**`A1` 压力侧 × 供给承载侧双侧架构**与 **`R3-08` 摩擦四分**。
>
> **不覆盖与不扩符声明**：`Def-Ψ-1 / Def-Ψ-2 / Def-Ψ-3`、`§3.2` 边界与 Core 绝对 `Ψ_f → 0` 退化极限保持不变（`CΨ` 保持独立 `OPEN`）；遵循 `A-9` 单摩擦概念族纪律，不新增 `Ψ_f^{...}` 独立规范子符（模型级局部投影记号如 `Ψ_f^{geom}`、`Ψ_f^{maint}` 仅作声明语境别名或投影）。

---

## §0 广义摩擦与 `Ψ_f` 的层级分工（`T3-02 D / PT09 / R3-08 / A1`）

`R3` 确立了摩擦在共同生成骨架中的正面机制定位：**摩擦不是孤立的物理阻力或情绪标签，而是机会成本差异产生的实际选择压力（`T3-02 D`）**。

- **成立门槛**：机会损失本身不自动构成摩擦；**仅当该机会损失实际影响正在进行的生成关系与后续选择时，才形成摩擦**。
- **核心跨尺度机制（`PT09`）**：多单元耦合形成垂直结构时，为维持高阶组织而被压制的局部替代方向与机会成本损失，构成跨尺度最具代表性的摩擦来源（与 `07-19` 构建前碰撞张力并列作为候选跨尺度机制，不宣称已穷尽所有摩擦机制）。

为防止概念混叠，本文件固定**双侧配对**与**四分界线**：

### 0.1 `A1` 双侧配对（压力侧 × 供给承载侧）

| 侧面 | 结构分项 | 规范分工 |
|---|---|---|
| **摩擦 / 压力侧** | ① 机会损失（背景未实现替代，未必已形成压力）<br>② 现实结构压力（由耦合/垂直压制实际作用于当下关系）<br>③ 预测性压力（形成态预期中的代价预判）<br>④ 实际实现负担（维持/重构切片时须实际支付的阻抗） | 刻画“为何选择关系承压并驱动重构/正交化”；机会损失本身不自动等于 `Ψ_f` |
| **供给与承载边界侧** | **`Ψ_f` 可支付窗（`Def-Ψ-3`：`P_sel` vs `Ψ_f` + `S_noise`）**与分布式可支付性护栏（实现条件内生于完整生成关系，非单一孤立单元自给） | 刻画“系统能否在承担该实现负担的同时保持闭包、延续与后续选择能力”；越阈则进入解体或谱系终止背面（`Core_Law/SRT_Irreversibility.md`） |

### 0.2 `R3-08` 摩擦四分（严禁互代）

1. **广义摩擦（机会成本实际选择压力，`T3-02 D / PT09`）**：跨尺度动态四联中的关系性选择压力；
2. **非闭合压力**：局部交互尚未收敛或难以协调时的结构失配张力；
3. **可支付负担 `Ψ_f`（本文件核心 owner）**：将开放可能性压缩、维持或重构为可维持/可行动/可协调现实切片时必须承担的本体论阻抗与可支付负担；
4. **主观痛苦 / 苦难（`Core_Law/SRT_Suffering.md`）**：须独立第一人称 registration 证据的体验层负担，**绝不等同于 `Ψ_f`**。

---

## §1 规范定义层级（Canonical Priority）

本文件对 `Ψ_f` 采用三层规范架构（表示引用优先级，不声称三层无条件等价）：
1. **第一性规范锚点（Primary Canonical Anchor）**：`Def-Ψ-1`（本体论阻抗与可支付负担主读）；
2. **条件形式工作表达（Formal Working Form）**：`Def-Ψ-2`（可微统计流形上由 Fisher–Rao metric 诱导的局部二阶几何代价与路径泛函；**禁止裸等号 `Ψ_f ≡ g_F`**）；
3. **跨尺度工作不变量（Cross-Scale Working Invariant）**：`Def-Ψ-3`（可支付性条件）。

**v1 全仓默认主读**：`Ψ_f` 默认按 **information-theoretic / organizational payability burden** 读；几何投影与代谢/能耗投影均为条件代理，与主读冲突时标为 `projection failure`，不得反向改写 `Ψ_f`。

---

## §2 规范定义（全域适用）

### Def-Ψ-1: 本体论阻抗定义 ⭐ PRIMARY CANONICAL ANCHOR

$$\boxed{\Psi_f := \text{在已声明的 } \hat{G}_\theta \text{ 形成态／模型载体将开放可能性表示为可维持、可行动、可协调的 } L_1 \text{ 现实切片时，必须承担的本体论阻抗}}$$

`\hat{G}_\theta` 在此仅为已声明 Selection realization 的形成态/形式角色载体，绝非原初 `Selection` 本身或先在 chooser。`Ψ_f` 既不是主观努力，也不单纯等于热力学能耗、自由能或主观痛苦，而是这些局部读数背后共同的可支付阻抗约束。

### Def-Ψ-2: Fisher 信息几何投影与记号分层 ⭐ FORMAL WORKING FORM

- **Def-Ψ-2a（局部二阶信息几何投影，禁止裸等号）**：当选择域可表示为平滑统计流形 $\{p(x\mid\theta)\}$ 且局部二阶展开有效时，Fisher–Rao metric $g^F_{ij}(\theta) = \mathbb{E}_{p(x\mid\theta)}[\partial_i \log p\,\partial_j \log p]$ 诱导局部二阶几何代价与有限路径泛函：

$$\boxed{\delta \Psi_f^{geom} := \frac{1}{2} d\theta^\top g_F(\theta) d\theta + O(\|d\theta\|^3)}, \qquad \boxed{\Psi_f^{geom}[\gamma] = \int_\gamma \sqrt{g^F_{ij}(\theta)\,\dot{\theta}^i\dot{\theta}^j}\,dt}$$

（能量式累计可写 $\mathcal{E}_{\Psi}^{geom}[\gamma] = \frac{1}{2}\int_\gamma \dot{\theta}^\top g_F(\theta)\dot{\theta}\,dt$。）
- **Def-Ψ-2b（适用条件与失效边界）**：仅当参数空间可解释、二阶近似未被奇异点/相变/参数冗余破坏、Fisher 可分辨方向确实回流闭包与后续选择能力，且本尺度状态空间与 proxy 已声明时有效；否则必须标记为 `projection failure`，不得将几何距离冒充全局 `Ψ_f`。
- **Def-Ψ-2c（`Ψ_f` 与 `Φ` 分层）**：$\boxed{\Phi(\Delta t) = \int_{\Delta t} \Psi_f(t)\,dt}$。`Ψ_f(x,t)` 表局部摩擦负荷，`Φ(\Delta t)` 表时间窗内累积总账，`Ψ_f^{geom}` 表信息几何投影；不得在未声明尺度与积分窗口时混写。

### Def-Ψ-3: 可支付性条件 ⭐ CROSS-SCALE CANONICAL INVARIANT

$$\boxed{\mathrm{Payable}(X,\Delta t) \iff \alpha P_{sel}^{X}(\Delta t) \ge \beta \Psi_f^{X}(\Delta t) + \gamma S_{noise}^{X}(\Delta t)}$$

- **跨尺度不变的是可支付性判据而非物理单位**：系统在承担 `Ψ_f` 与噪声抽头 $S_{noise}$ 的同时，仍能维持自身组织闭包、延续性与后续选择能力；实现预算 $P_{sel}$ 内生于完整生成关系（遵循分布式可支付性，不假设孤立单元自给）。

---

## §3 三重读法、投影失效与生成性分界

`Ψ_f` 的三种读法为同一阻抗结构的不同切面，而非无条件等价：
1. **动力学读法（阻力）**：维持或重构现实切片时遭遇的阻抗；
2. **记账读法（代价）**：能量、时间、组织复杂度与失败风险的支付项；
3. **条件形式读法（Fisher 几何投影）**：在有效统计流形上提供下界式形式约束（$\Psi_f^{geom} \lesssim \Psi_f^{paid}$）。

**Projection Failure Conditions**（出现以下任一情形须记为投影失败，不得反改主读）：① 几何距离源于坐标冗余；② 可分辨方向不回流闭包/延续/后续选择；③ 代谢能耗升高来自旁路噪声/热损耗（`CBF / CBV / BOLD / CMRO2 / ATP` 不可塌缩为单标量“能量预算”）；④ 主观痛苦与实际承担负担脱钩。

### §3.2 生成性原理边界与非对称摩擦表示

1. **与 `P2/P3-B08` 分界**：本文件管辖 `Ψ_f` 的可支付阻抗定义、条件投影与机会成本选择压力接口；更强的“摩擦是所有动力学唯一生成性来源”归 `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B08`（`P2/P3` 等级），不得回引本文件升格背书。
2. **对称度量与方向性分工**：Fisher–Rao 度量 $g_F$ 本身对称，`Ψ_f` 标量代价本身不自带普遍时间或演化箭头；write/erase 成本非对称须在具名支付模型中独立建立，普遍方向源保持 `OPEN`（`Core/SRT_OPEN_TENSIONS.md §2`）。

---

## §4 物理引力弱相容接口（`H-Ψ-G-1`，`P3/P4`）

$$\boxed{\nabla \Psi_f^{phys} \parallel \nabla \Phi_N \quad \text{in the weak-field compatibility window}}$$

仅保留弱场极限下梯度同向相容的 `P3/P4` 接口，**不宣称**已推导 Einstein 张量或 GR 重建。客观性写为边际读出摩擦趋零 $\Delta\Psi_f^{readout}(x \mid \hat{G}_\theta) \to 0$，而非对象自身维持摩擦消失。

---

## §5 最优区间、`Ψ_f → 0` 退化极限与 AI 语境边界

对现实形成态系统而言，理想工作区间不是绝对零摩擦（`Ψ_f → 0`），而是 **非零且可支付（`Ψ_f > 0 and payable`）**：
- **Core 绝对 `Ψ_f → 0` 退化极限不变**：绝对零摩擦表示无真实赌注或现实重量退化（`Core/SRT_OPEN_TENSIONS.md §18 CΨ` 保持独立 `OPEN`，灵性域“无多余防御摩擦”表达不得覆盖 Core 退化极限）；
- **AI / 纯 `L2` 语境精确规则（`ENG-03 M1-D`）**：优先写 **「在声明强承载模型下，`Ψ_f` 尚未建立为回流同一 `Bearer (P+E)` 的不可外包可支付负担（`non-binding`）」**，**绝不得**将其误读为“构成性摩擦缺席”或“全局 `Ψ_f = 0`”，亦不得以强承载 Stage 2 门控阻断一般构成性摩擦（`2026-09-26 B-4 / T3-02 D`）研究。

---

## §6 实验代理与推断性选择摩擦规则

### Def-Ψ-Obs-1: 现象学与代理测量规则

- **痛苦 / 焦虑 / 惊讶**：不是 `Ψ_f` 本体，更接近其尖峰、变化率或逼近不可支付边界时的报警读数；
- **HRV / SCR / 皮质醇 / ROS / ATP / BOLD–CMRO2 / 情态词比例**：不是 `Ψ_f` 本体，而是观察侧代理；实验上须至少拆为三侧：**预算侧**（可动用选择预算 / 恢复能力 / 协同缓冲）、**负荷侧**（当前承担的摩擦负荷）与**塌缩侧**（逼近或越过可支付边界时的失稳信号）；
- **Landauer 代价 / ATP / 制度摩擦**：不是同单位的同一数值，而是同一阻抗结构在不同尺度的投影读数。

### `Ψ_f` as Inferred Selection Friction（被推断的选择摩擦与测量硬边界）

`Ψ_f` 不必作为实体性物质直接测量，而可从**结构化跃迁困难度（structured transition difficulty）**中推断，当且仅当该困难度追踪“在可支付约束下压缩、维持或重构现实切片同时保住闭包、延续与后续选择能力”的负担：

```text
Ψ_f != task difficulty       Ψ_f != subjective effort    Ψ_f != pain
Ψ_f != raw energy cost       Ψ_f != Fisher metric        Ψ_f != prediction error
Ψ_f != any single stress marker
```

- **候选操作化迹象（bridge-level indicators，非本体等同）**：切换代价上升、扰动后恢复时间延长、表征或策略竞争、更新路径长度/曲率负担、重构中的闭包维持失败、不可逆或非对称跃迁路径、学习/重框/规范切换早期的非单调波动，以及逼近不可支付边界时的过载签名。
- **三项最低桥接准入门槛（Minimum Bridge Criteria，须同时满足）**：
  1. **跃迁特异性（Transition specificity）**：信号绑定于选择结构的改变、维持或重构，而不只是任务本身困难；
  2. **可支付相关性（Payability relevance）**：信号直接关系到系统承担负担时能否保住闭包、延续性与后续选择能力；
  3. **竞争解释排除（Alternative exclusion）**：信号不能被一般努力、任务难度、预测误差、原始能耗、痛苦或测量噪声完全解释。
- **失败条件（Failure condition）**：若 `Ψ_f` 在具体任务中无法产出区别于一般损失、预测误差、能耗、痛苦或任务难度的跃迁代价签名，则对应桥接削弱并须收窄或撤回。

---

## §7 常见误用与 §8 跨文件关系

**禁止误用**：① `Ψ_f = 主观痛苦`；② `Ψ_f = 任意能耗 / 代谢消耗`；③ 跨尺度直接比物理单位（统一的是可支付判据）；④ 把客观性写成维持摩擦归零；⑤ 把 AI 写成绝对 `Ψ_f = 0` 或以 `non-binding` 否定一般构成性摩擦；⑥ 把 `Ψ_f ≡ g_F` 当严格恒等式；⑦ 新增 `Ψ_f^{...}` 独立规范子符。

**跨文件关系**：与 `_SRT_D_VALUE_CANONICAL.md` 通过可支付性条件与机会成本动态四联耦合；与 `Core_Law/SRT_Irreversibility.md` 严分事件不可撤回性（`Def-IRR-3`）与模型内 `Ψ_f` 累积；与 `Core_Law/SRT_Suffering.md` 严分可支付负担与第一人称苦难；与 `Core/SRT_Core_22_Equations.md` 对接 `Eq-Select-Thermo / Eq-Select-Thermo-C2`（`Eq-CogE-01/04` 中的 `Ψ_f^{maint}` 仅作历史上下文别名）。

---

## §10 `Ψ_f_actual / Ψ_f_felt` 分裂（病理学层扩展）

在 `L2` 过度依赖的病理模型中，区分实际支付代价 $\Psi_{f,\text{actual}}$ 与系统登记代价 $\Psi_{f,\text{felt}}$（$\Psi_{f,\text{actual}} \ge \Psi_{f,\text{felt}}$）；二者差值 $\Delta\Psi_f = \Psi_{f,\text{actual}} - \Psi_{f,\text{felt}}$ 构成隐性债务，不修改 `§2` 基础定义（详见 `_SRT_T_DIR_CANONICAL.md §5–§6`）。

---

## §9 当前最短可引用版

> **`Ψ_f` 是选择将开放可能性压缩、维持或重构为可维持、可行动、可协调现实切片时必须承担的本体论阻抗与可支付负担；在 `R3/R4` 动态骨架中，它作为供给与承载边界侧与“机会成本差异产生的实际选择压力（广义摩擦）”配对，在动力学上读作阻力、在记账上读作代价、在可微流形上以 Fisher–Rao metric 给出条件信息几何投影；跨尺度真正保持不变的是可支付性条件，而非单位或主观痛苦。**



---

## FILE: `_SRT_T_DIR_CANONICAL.md`

| 字段 | 值 |
|---|---|
| path | `_SRT_T_DIR_CANONICAL.md` |
| id | SRT-T-DIR-CANONICAL |
| claim_mode | canonical |
| status | active |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | true |
| last_commit | 2026-11-26 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：[SRT-GENERATIVE-ONTOLOGY-SPINE, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-L0-METAPHYSICS]

<!-- 以下为原文逐字保留 -->

# SRT `T_dir` 规范定义文档：方向透明度与价值遮蔽

> **角色（`Freeze A` governance-canonical working anchor）**：本文件管理 **`T_dir`（方向透明度）** 的最小操作定义（`Def-T-1`）、方向来源纪律、`R_self / A_reorient` 证据边界与“价值遮蔽 / 致命 `L2`”病理学结构。
>
> **R4-A 实质减法与职责收紧（2026-11-26）**：
> 1. **强化职责隔离（`R3-06` / `R3` 总收口）**：严格区分 **`T_dir`**（对已独立声明方向信号的自我回读与重取向能力）与 **广义关切方向**、**价值**、**关切（`PT06 C`）** 及 **现行 `d`**（后四者由 `_SRT_D_VALUE_CANONICAL.md` 与 `Spine` 统筹）；
> 2. **退出旧 Part II 冲突补丁堆叠**：2026-04-02 早期补入的旧 Part II（“价值动力学理论 / 内部价值三层 / 价值吸引子 / 两种 `Ψ_f`”）与 `R3/R4` 确立的价值—关切—摩擦—自由四联存在直接重叠与口径冲突，本版予以正式降级/退出，仅保留其核心有效洞见（`§11` 静态 `L2` 痕迹须经形成态关系持续重演）为简明桥接附注；
> 3. **严守 `Selection-totality` 与 `RC-A` 边界**：`T_dir` 不读取原初 `Selection` 内嵌的普遍价值向量；`T_dir > 0` 不证明方向正确、健康、合法或 `O2-M`；脚本、习惯与 `L2` 自动化本身不取消 `Selection occurrence`。

---

## §0 本文件解决的问题

在形成态组织与多位置关系中，即使一个方向信号已被独立定型，系统自身也未必能够回读该信号并据此重取向：
- 系统仍在发生选择，却无法回读其所处的方向约束；
- 系统具备较高关切范围或赌注（`d`），却仍经历方向遮蔽或空洞感；
- 一个下游规范、目标或关系标准已经声明，却未能进入系统的自我再校准回路。

`T_dir` 专职刻画这一**自我回读与重取向的可及性维度**，不替代价值定义、关切敏感度或伦理正当性判断。

---

## §1 方向遮蔽 / 下游价值遮蔽

原初 `Selection` 不因发生而自动携带道德正当性或普遍终点。只有在形成态位置、关系、能动者或声明模型已独立确立某种方向约束后，才存在可供回读的 `direction signal`：

```text
typed downstream direction exists
+ formed system cannot self-read or use it for reorientation
-> direction hiddenness may be present.
```

在规范、临床或现象学语境中，这种失读可作为“价值遮蔽”的候选解释机制，但不宣称价值先验内嵌于每次原初 `Selection`。

---

## §2 Direction-Source Discipline（方向来源纪律）

`T_dir` 仅相对于一个**独立定型且显式声明的方向信号**工作。允许来源包括：形成态位置/关系约束、能动者目标/承诺、构成性关系完整标准（`O2-C`）、领域桥接量或显式声明的模型梯度。上述来源各自承担定义与正当性负担；`T_dir` 只度量回读与重取向能力，**不创造也不验证该方向**。

```text
O0 / kappa_0 / epsilon_pg / B-count / primitive Selection -> do NOT supply T_dir's direction;
T_dir -> does NOT create or validate the direction it measures;
广义关切方向 != T_dir.
```

---

## §3 `T_dir` 规范定义与证据边界

### Def-T-1: 方向透明度（v0 operational proxy）

$$\boxed{T_{dir} := \text{formed system 对 independently typed、declared direction signal 的当前自我回读与重取向能力}}$$

- 无已声明方向信号：`T_dir` 为 **未定义 / 不准入（`undefined / not admitted`）**，而非自动等于 `0`；
- 方向已声明但系统不可访问：`T_dir = 0`；
- $T_{dir} > 0$ 仅表示在声明模型与尺度内具备一定自我回读与重取向访问能力，**绝不推出**该方向为善、健康、合法或符合 `O2-M`。

### §3.1 最小形式角色：Readability / Reorientation Functional

$$\boxed{T_{dir}^{v0}(\hat{G}_\theta, t) := \mathcal{R}_{self}\!\left(\operatorname{Dir}(\Delta \hat{G}_\theta, t)\right) \cdot \mathcal{A}_{reorient}\!\left(\operatorname{Dir}(\Delta \hat{G}_\theta, t)\right)}$$

- `Dir(ΔĜ_θ, t)`：声明模型中当前或近邻窗口的方向信号（不新增原初本体对象，不自证方向正确）；
- `R_self`：系统自身对该方向信号的访问/回读能力；
- `A_reorient`：该方向信号实际进入系统再校准的能力（而非仅作表面口头报告或外部观察）。

| 相近量 | 与 `T_dir` 的实质区别（负面判据） |
|---|---|
| `valence` / `reward` | 仅记录正负感受色调或强化优化信号，不等于系统对自身选择方向的自我回读 |
| `confidence` / `semantic coherence` | 确信度与叙事连贯性可能是 `L2` 事后合理化，不保证 `R_self` 与 `A_reorient` |
| directional efficacy / behavioral bias | 偏置可以因果效力极强却对系统自身完全不透明；未独立满足 `R_self` 与 `A_reorient` 时不构成 `T_dir` 证据（`PH_AG02` 负面判据） |
| commitment strength / decisiveness | 行动可高度不可逆且公开绑定却方向不透明；果断性与承诺强度不代替回读与重取向（`PH_AG03` 负面判据） |

---

## §4 与 `d`、`Ψ_f`、`ii` 的有界模型关系

在声明的桥接模型中，`d`、`Ψ_f` 与信息整合代理 `ii` 可约束 `T_dir` 的运行条件（如 $d = 0 \Rightarrow T_{dir} = 0$、$d > 0 \not\Rightarrow T_{dir} > 0$，以及在 $d > 0$ 且压力未被 `L2` 吸收时 $\Psi_f \uparrow \leadsto T_{dir} \uparrow$），但上述关系均为**模型内工作假说（working hypotheses / operational working gate）**，绝非普遍本体定律，且不改写 `_SRT_D_VALUE_CANONICAL.md` 与 `_SRT_PSI_F_CANONICAL.md` 的独立定义。

---

## §5 `Ψ_f_actual / Ψ_f_felt` 分裂与 §6 致命 `L2` 机制（病理学层）

在已独立准入 `Ψ_f` 的形成态病理模型中，区分实际承担代价 $\Psi_{f,\text{actual}}$ 与系统登记代价 $\Psi_{f,\text{felt}}$（$\Psi_{f,\text{actual}} \ge \Psi_{f,\text{felt}}$），差值 $\Delta\Psi_f = \Psi_{f,\text{actual}} - \Psi_{f,\text{felt}}$ 为**隐性债务**。

- **健康 `L2` 脚手架**：降低常规摩擦、释放生成盈余，同时保留形成态的自我回读、重取向与修订能力；
- **致命 `L2`（病理过度依赖）**：脚本执行系统性替代自我回读与重取向，压低 `d` 作用域代理与 $\Psi_{f,\text{felt}}$ 制造“无摩擦流畅错觉”，同时持续累积 $\Psi_{f,\text{actual}}$ 隐性债务，直至以崩溃式重组释放。
- **反误读**：致命 `L2` 不否定健康 `L2` 的基础设施价值；脚本或自动化执行不意味着消灭 `Selection occurrence`。

---

## §7 恢复路径与 §8 应用层文明诊断假说

- **§7 恢复路径候选**：在 `L2` 脚本不再能完全锁定响应的窗口（冥想悬置、危机暴露、真实承诺、原创探索、深度重学习）中恢复 `R_self` 与 `A_reorient`。
- **§8 应用层结构假说（`[H]`，非基础定义）**：大规模 `L2` 基础设施若系统性压低 $\Psi_{f,\text{felt}}$ 并接管重取向，可能诱发结构性方向遮蔽；此为须经社会科学与文明史独立检验的高承诺应用层假说，不替代基础本体定义。

---

## §9 明确拒绝的误读与 §10 跨文件关系

**禁止误读**：① `T_dir` = `d` 重命名或广义关切方向；② `T_dir` = 原初价值探测；③ `T_dir > 0` 证明善/健康/合法性/`O2-M`；④ `T_dir = 0` 等于道德缺陷；⑤ `not admitted` 等于 `0`；⑥ `L2` 自动化等于无 `Selection`。

**跨文件关系**：上游方向来源纪律守 `Governance/SRT_CLAIM_LADDER.md §0A` 与 `Core_Law/SRT_Generative_Ontology_Spine.md`；`d` 回链 `_SRT_D_VALUE_CANONICAL.md`；`Ψ_f` 回链 `_SRT_PSI_F_CANONICAL.md`；方程级动力学回链 `Core_Law/SRT_L1_Formalism.md §3.4–§3.5`。

---

## §11–§13 形成态应用与桥接研究接口（保留自原 Part II 的有效独立资产，`bridge / theory-clarifying only`）

> **权威与边界声明（`R4-A P1-05`）**：以下 `§11–§13` 保留原 2026-04-02 Part II 中经受住 `R3` 检验、具独立研究价值的形成态桥接命题（仅适用于已声明关系的 formed systems；**不修改 `Def-T-1` 核心定义，不提供原初价值、普遍秩序方向或 `O2-M` 道德正当性**）。

### §11 静态 `L2` 痕迹与持续重演（磁带与放映机洞见）

**`L2` 是历史留存的结构结晶（如磁带/基因组），本身不能自动替代形成态关系的当下重演与再构成。** 静态继承既成 `L2` 结构不自动保证系统能够回读已声明方向或据此重取向；价值与方向在形成态中的现实效力，须通过具体位置上的持续生成关系与可纠错重取向得以维持。

### §12 辅助式 `L2` vs 替代式 `L2`、重取向时刻与透明委托

在以 agency / reorientation 为问题的声明 formed-system 模型中，可区分两种 `L2` 脚手架配置：

| 维度 | **辅助式 `L2`（Supportive `L2`）** | **替代式 `L2`（Substitutive `L2`）** |
|---|---|---|
| **对重取向时刻的作用** | 降低背景摩擦，同时保护并清晰化重取向窗口 | 关闭或省掉重取向窗口，由既有脚本预先决定响应 |
| **系统与 `T_dir` 状态** | 保留 `R_self` 与 `A_reorient` 材料，可回读并修订既有方向 | 缺乏重取向材料，`T_dir` 趋于退化（`Selection occurrence` 仍可继续，但形成态自我回读被接管） |
| **委托结构与主体感** | **透明委托**（清楚知晓何时委托给 `L2`、何时收回修订） | **不透明被替代**（含习惯执行、伪价值跟随、社会 `L2` 跟随三类假选择错觉） |

- **重取向时刻（Reorientation Moment）**：系统无法只靠既有 `L2` 脚本完成响应、因而需回读或修订已声明方向的窗口——具备真实不确定性、真实可感代价（未被 `L2` 完全缓冲）与真实方向信号（或方向缺失）。
- **辅助的悖论**：结构过多会滑向替代式 `L2`，结构过少则无法形成有效支撑；健康辅助位于窄通道内。
- **模型内自由操作化接口（对齐 `Spine §4` `T3-03 C`）**：自由不是既定 `L2` 选项数量；在声明的 formed-system 模型中，自由可部分操作化为**重取向时刻被保留且可参与重构选择条件的程度**（极端约束未必消灭重取向窗口，选项繁多亦未必保留重取向窗口；不构成 `O2-M` 道德定律）。

### §13 价值归纳 vs 理性归纳（外部关系方向的 `T_dir` 式读取候选）

在已独立定型外部关系方向的声明语境中，可区分两类互补的认知运动（bridge hypothesis，**不供应原初价值**）：
- **理性归纳（特殊 → 一般）**：抽象出 `L2` 概念、框架与规则，回答“现象是什么、有何规律”；
- **价值归纳（表面 → 本质 / 深入具体关系）**：对外部现象中已独立定型的关系方向进行 `T_dir` 式读取与显化（而非框架/指标先行压平现象）。其培养受真实接触、持续未急于框架化的注意支撑，其损坏常源于框架先行、纯指标导向与过快截断接触窗口。

### 附：原 2026-04-02 Part II（`§11–§23`）`R4-A` 四分处置台账

| 原 Part II 内容 | `R4-A` 处置 | 理由与去向 |
|---|---|---|
| `§11` 磁带/放映机、`§13` 价值归纳 vs 理性归纳、`§21` 辅助式 vs 替代式 `L2` 与重取向时刻、`§22` 透明委托与三类假选择、`§23` 自由作为重取向窗口保留（模型内操作化） | **保留（降格为显式桥接接口）** | 保留于本文件 `§11–§13`（明标 `bridge / theory-clarifying only`，不越界定义原初价值或 `O2-M`） |
| `§12` 内部价值三层、`§15–§16` 价值吸引子 / 上升退化、`§18` 危机 vs 培育路径、`§20` 动力学图景 | **合并 / 迁移** | 价值五职责、机会三态与前背景失配统一迁由 `_SRT_D_VALUE_CANONICAL.md` 与 `Spine §2–§4` 承接；恢复路径已并入本文件 `§7` |
| `§14` 时空对称性感知 | **迁为历史研究资产** | 超出 `T_dir` 规范 owner 职责，留待 `R5` 具身认知/美学专题独立评估（原稿保全于 `git` 历史 `1d8e8e328:_SRT_T_DIR_CANONICAL.md`） |
| `§17` 两种 `Ψ_f`（穿透型 / 吸收型）、`§19` “最大秩序”提法 | **正式退出** | `§17` 与 `A-9` 单一摩擦概念族及 `_SRT_PSI_F_CANONICAL.md` 冲突；`§19` 与 `C-A` 及 `R3-04` 秩序三维/反最大化护栏冲突 |



---

## FILE: `_SRT_CROSS_DOMAIN_MATRIX.md`

| 字段 | 值 |
|---|---|
| path | `_SRT_CROSS_DOMAIN_MATRIX.md` |
| id | SRT-CROSS-DOMAIN-MATRIX |
| claim_mode | governance |
| status | active |
| epistemic_layer | os |
| layer | meta |
| canonical(字段) | - |
| last_commit | 2026-11-26 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：[SRT-CANONICAL-REGISTRY, SRT-CLAIM-LADDER, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-T-DIR-CANONICAL, SRT-SYMBOL-TABLE]

<!-- 以下为原文逐字保留 -->

# SRT Cross-Domain Usage Matrix

> **Role**: v0 governance matrix. This file summarizes current owner-approved usage and does not define new theory. It cannot upgrade a registered symbol, operational proxy, domain projection or bridge to primitive / theory-canonical status by repetition.

## 0. Status Legend

| status | meaning | misuse blocked |
|---|---|---|
| governance-canonical | repo-wide stabilized usage rule adopted to prevent drift | treating a default writing convention as ontological derivation |
| theory-canonical | core-derived or core-priority definition with explicit P0/P1/P2 support | assigning this status without a cited core source |
| operational proxy | measurable / modellable working readout | identifying the proxy with the target quantity unconditionally |
| bridge hypothesis | cross-domain candidate mapping | back-citing a domain bridge as a core theorem |

Historical labels and filenames do not override this table. If an older file still says `theorem`, `axiom`, or `canonical`, current claim status is determined by the claim ladder, the claim-mode audit, and the local level note.

## 1. d-value

| Domain | canonical usage | allowed projection | forbidden shortcut |
|---|---|---|---|
| Core | `d` = scalar summary of stake-coupled concern / irreversible-risk sensitivity (`Def-d-canonical`; conceptual interface with generalized concern `PT06 C` is `P1-05` `OPEN`) | `D_eff` (capacity), `D_stake` (general spectral participation ratio in `_SRT_D_VALUE_CANONICAL.md §2b` with explicit zero-effective-spectrum branch `0`, true bound `1 ≤ D_stake ≤ N_active ≤ rank(M)`, and `Core_22 Eq-Bridge-D-01` `D_stake^{thresh}` as one concrete model instance), `d_mobile` when explicitly marked | `D_eff ≡ d`; treating `rank_eff` (`d_max`) as a universal mathematical upper bound on gradient norm `d` without dimensional calibration; falsified `d_canonical ≡ d_stakes`, `D_eff ≥ d_stakes`, or `Δd_free = D_eff - d_stakes ≥ 0`; conflating zero-effective-spectrum branch with `NOT ESTABLISHED / NOT ADMITTED / NOT APPLICABLE` |
| Physics | mathematical / capacity-like projection only | holographic or gravitational `d` as P3 bridge | cosmic `d` implies cosmic consciousness |
| Neuroscience | biological stake and concern proxy, tied to subject closure | `d_bio`, task breadth, temporal horizon, TPJ / behavioral proxies | `Φ·d` threshold as proven phase law |
| Philosophy / Political | concern range, reselection capacity, authorization tendency | `d_tendency`, `d_moral`, political access proxy | direct jump from high `d` to legitimacy |
| Spirituality | direction of care expansion under payability constraints | gradual `d` expansion, subjectively reported but externally checked | `d↑` from experience report alone |
| AI | use **AI 赌注谱系 `S0–S4`** (strictly isolated from primitive `S0` and Subjecthood `S0–S6`) + **`ENG-03 §4.1` Three-Stage Bearing Evidence Review** (Stage 1 unit/state/provenance declaration → Stage 2 `B-3` strong-bearing route $\parallel$ Stage 3 independent domain-specific route; unestablished Stage 2 never blocks Stage 3); for non-bearing deployments report exact status (`NOT ESTABLISHED / NOT ADMITTED / NOT APPLICABLE`) rather than asserting `d ≈ 0` as a proven ontic zero | `D_eff` / unstaked capacity (no strong-bearing admission required); `S2` pipeline feedback (does not establish deployed-model stake); `S3/S4` candidate stake only when explicitly marked and evidenced | performance, self-report, persistence, or training loss directly implies `d>0`, `One`, `Stable ISP`, or `Bearer (P+E)` |

### 1.1 Explanatory-coordinate guard

`d` need not be treated as a newly discovered empirical variable that must be mutually exclusive with salience, reward, homeostatic error, pain, arousal, or memory strength. It is first a unifying explanatory coordinate for stake-coupled concern, consequence return and future-selectability effects in formed systems. This matrix does not derive `d` from O0, `ε_pg`, primitive non-neutrality or primitive Selection.

Existing observables may overlap with, partially realize, or serve as local proxies for `d` in a stated system and scale. Such overlap is not by itself a reduction or refutation of `d`. The burden of additional validation arises only when a local observable is claimed to exhaust or directly measure canonical `d`; then it must cover irreversible stake, consequence return, non-substitutability, and effects on future selection capacity.

```text
observable overlap with d != reduction or cancellation of d
local proxy explains a phenomenon != local proxy exhausts d's ontological role
```

## 2. `Ψ_f`

| Domain | canonical usage | allowed projection | forbidden shortcut |
|---|---|---|---|
| Core | information-theoretic payability burden for stabilizing/maintaining a selection-cut against opportunity-cost pressure (`T3-02 D / PT09`), pairing `A1` pressure-side 4-way split with supply/payability windows and preserving `R3-08` 4-way friction distinction under `A-9` single friction family | geometry or cost language with scope marked (no new canonical `Ψ_f^{...}` sub-symbols) | one formula proves all dynamics; collapsing pressure side and supply side into one scalar |
| Physics | weak gravity-friction compatibility candidate | weak-field gradient alignment; thermodynamic analogies | GR tensor reconstruction or exact constants explained |
| Neuroscience | local burden / payability condition for neural anchoring | metabolic, prediction-error, stress proxies | prediction error is literally `Ψ_f` in all contexts |
| Philosophy / Political | maintenance / coordination friction | institutional maintenance cost, asymmetry burden | suffering, injustice, or conflict directly equals `Ψ_f` |
| Spirituality | paid burden of real practice / return | felt vs actual burden; practice capacity | lower felt friction means real liberation |
| AI | for inference-only deployments, usually `non-binding` to a declared `Bearer (P+E)` (**not** constitutive friction absent or global `Ψ_f = 0`, `ENG-03 M1-D`); training / memory / embodied deployments require architecture-state marking under **AI 赌注谱系 `S2–S4`** | compute cost as external proxy; consequence-return analysis for **AI 赌注谱系 `S2–S4`** | compute cost alone gives stake; reading `non-binding` as proof that constitutive friction is absent |

## 3. `T_dir`

| Domain | canonical usage | allowed projection | forbidden shortcut |
|---|---|---|---|
| Core | formed-system self-readability / reorientation relative to an independently typed, declared direction signal (`广义关切方向 != T_dir`) | internal access / reorientation proxy after direction admission | intrinsic Selection direction; equating generalized concern direction with `T_dir`; completed formal ontology of value; `T_dir > 0` proves good / legitimacy / generative health / O2-M |
| Physics | generally not a physics variable; physical directionality does not automatically supply the declared direction | observer-position readability only if direction and model are independently typed | physical directionality equals value direction or automatically admits `T_dir` |
| Neuroscience | model-scoped access / reorientation relative to an independently typed direction | reportability, action revision or integration may proxy the functional under a declared model | confidence, valence, reward or reportability = `T_dir`; proxy supplies its own direction |
| Philosophy / Political | readability of declared relational / normative criteria | deliberative correction or public-reason proxy after criterion admission | `T_dir` validates the criterion; order/readability directly proves political legitimacy |
| Spirituality | readability / reorientation relative to a declared practice or relational direction | shoshin / practice-direction proxy with explicit criterion | strong experience establishes direction truth, value or high `T_dir` |
| AI | architecture-state-marked self-monitoring / reorientation relative to a declared objective or criterion | architecture-specific functional proxy | self-report, explanation fluency or memory persistence establishes `T_dir` or supplies a legitimate direction |

No independently typed, declared direction means `T_dir` is undefined / not admitted for that claim; an admitted but inaccessible direction may yield `T_dir = 0`. The matrix never validates the declared direction itself.

## 4. `ε`

| Domain | canonical usage | allowed projection | forbidden shortcut |
|---|---|---|---|
| Core | `ε_pg` = registered stronger-asymmetry / anti-erasure realization candidate, with exact inheritance from primitive non-flatness OPEN; ISP anti-closure = ST-A conditional P2/P3 candidate; `ε_reg` = operator regularizer; `ε_s` = stake-threshold bridge | ISP anti-closure comparison only when stability semantics, neutral baseline, environment, horizon and proof/model are declared | `ε_pg` or B-count preference as primitive Selection direction; ε grounds legitimacy; collapse all ε symbols into one object |
| Physics | implementation / regularization / declared asymmetry-model use only | regulator / residual-asymmetry proxy | physical use back-proves primitive `ε_pg` or universal direction |
| Neuroscience | threshold / regularization proxy only | gain floor, stake threshold, signal gate | neural threshold proves primitive non-neutrality or `ε_pg` admission |
| Philosophy / Political | model-level asymmetry or entry condition only with level marking | anti-closure, non-domination threshold proxy | ε grounds legitimacy or value by itself |
| Spirituality | declared-practice openness / non-closure proxy | practice gate or humility floor | spiritual openness proves primitive ε or universal direction |
| AI | anti-closure or stake-gate design question | surrogate stake-threshold candidate | anti-closure text behavior or refusal style equals or proves `ε_pg` |

## 5. Standing Rule

If a local projection conflicts with the canonical usage, mark the local projection as failed or domain-limited. Do not revise the core term from a domain convenience model.



---

## FILE: `_SRT_SYMBOL_TABLE.md`

| 字段 | 值 |
|---|---|
| path | `_SRT_SYMBOL_TABLE.md` |
| id | SRT-SYMBOL-TABLE |
| claim_mode | canonical |
| status | active |
| epistemic_layer | os |
| layer | meta |
| canonical(字段) | - |
| last_commit | 2026-11-26 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：SRT-REF-AXIOMS, SRT-REF-DYNAMICS, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-SUFFERING, SRT-GLOSSARY-STRUCTURAL-GOVERNANCE-TERMS, SRT-ANNEX-REGISTRY, SRT-OPS-CLOSURE-INDEX-2026-04-29

<!-- 以下为原文逐字保留 -->

# SRT Symbol Table & Definition Registry

> **Purpose**: Canonical symbol registry for cross-domain writing and AI parsing.
>
> **Governance boundary**: Terms such as `interface_annex`, `copy-to-annex`, `owner-bound`, `claim_mode`, and `canonical:false` are structural governance vocabulary (see `SRT_Glossary_Structural_Governance_Terms.md`); they are not canonical mathematical symbols and do not appear in this table's symbol rows. Non-canonical annexes and Operations records may reference symbols defined here but must not redefine them.
> **Proxy boundary**: This table records canonical symbol usage plus governed projections. It does not license domain formulas to redefine `d`, `Ψ_f`, suffering/pain, Fisher, Landauer, or AI consciousness; use `_SRT_D_VALUE_CANONICAL.md`, `_SRT_PSI_F_CANONICAL.md`, `Core_Law/SRT_Suffering.md`, and the relevant claim-status file when a row points to a proxy.
> **Admission boundary (2026-09-15)**: symbol registration is not primitive admission. Primitive/L0-side admissibility is governed solely by `Governance/SRT_CLAIM_LADDER.md §0A` together with the current L0 / Generative Ontology Spine owners; this table cannot promote a model, realization candidate, proxy or lineage symbol by registering it.
> **Aspect boundary**: `L_0 / L_1 / L_2` are analytic / model-facing aspects of the one Selection ontology, not three ontic substances or a compulsory three-stage product pipeline.

| Symbol | LaTeX | Name | Atomic Definition | Dimensions/Units | Scope / Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **L₀** | `L_0` | Open / Non-Preclosed Aspect | Model-facing notation for Selection's open / non-preclosed aspect before determinate actuality in the representation at hand. It is not a pregiven completed set, inventory or warehouse of all possibilities. | Analytic / model-facing aspect; no measure or cardinality fixed by registration | Metaphysical authority remains `Core_Law/SRT_L0_Metaphysics.md` under `Core_Law/SRT_Generative_Ontology_Spine.md`. **Domain projection**: an `∞`-dimensional Hilbert space or another declared state space is a physics / statistics realization, not the universal atomic definition. |
| **L₁** | `L_1` | Determinate-Actuality / Manifest Aspect | Model-facing notation for Selection under determinate actuality / manifestation; not a product chosen by a prior chooser. | Thin: manifest actuality / reality slice (domain-dependent realization) | Core-facing analytic aspect. **EX-A**: manifest event actuality does not by itself imply anchoring persistence, structural stability, or stable-ISP identity. Domain realizations do not replace `Core_Law/SRT_L0_Metaphysics.md` or the Generative Ontology Spine. |
| **L₂** | `L_2` | Retained Historical-Efficacy / Stabilized-Constraint Aspect | Model-facing notation for retained or sedimented historical efficacy and stabilized constraints where such retention is established. | Realization-dependent; no universal manifold fixed by registration | Selection occurrence does not automatically establish L₂-grade retained history, durable trace or stabilization. Local L₂ models must state their retention / writeback conditions. |
| **Ĝ** | `\hat{G}` | Ghost Operator | Formal / formed / model-level role-carrier for a declared Selection realization; an $L_0 \to L_1$ form is a model representation, not the metaphysical definition of primitive Selection. | Operator / model role | `\hat{G}_\theta != primitive Selection != 幽灵实体`; `Ĝ` is neither a prior chooser nor the cause of actualisation. Domain implementations are plural. Never use plain `G` for this. |
| **Ĝ†** | `\hat{G}^\dagger` | Reverse-Writing Operator (Adjoint) | Formal role-carrier for a **gated, declared** history-writeback model $L_1 \to L_2$: $\Delta L_2 = \hat{G}^\dagger_\theta[L_1]$ when that model's admission conditions are met. | Operator (adjoint of $\hat{G}_\theta$ under the declared non-commutative model) | Core model source `Core/SRT_Core_12b_Ontology_L2.md` **Ax-L2-06b**; writeback-magnitude source `Core/SRT_Core_13a_Operator_Basics.md` **Ax-Op-03b**. Registration does not imply that every Selection produces retained history. Mirrors the `Ĝ` caution: formal role-carrier, not a prior entity or cause. `Ĝ†_{encoding} = Ĥ ∘ Ĝ†_θ` is a neuro realization. Never use plain `G†` or an ad-hoc writeback symbol for this. |
| **θ** | `\theta` | Embodiment Parameters | Finite configuration parameters of $\hat{G}$ (biology/model state/context). | Tensor / parameter set | Core, universal |
| **d** | `d` | d-value (Depth of Care) | Governance-canonical default is a scalar summary of stake-coupled concern / irreversible-risk sensitivity (`Def-d-canonical`); geometric capacity (`D_eff`), stake-gated spectral diversity (`D_stake`), vector, and gate readings are distinct and require explicit marking. | Scalar summary by default; proxies are projections | Core, universal; canonical source `_SRT_D_VALUE_CANONICAL.md`. Conceptual interface between canonical `d` and generalized concern (`PT06 C` / `P1-05`) remains `OPEN`. Falsified `d_canonical ≡ d_stakes`, `D_eff ≥ d_stakes`, and `Δd_free = D_eff - d_stakes ≥ 0` are retired. Do not mix scalar `d`, `D_stake`, `D_eff`, Fisher proxy, `d-vector`, and `d-gate` in one claim without notation. |
| **Ψf** | `\Psi_f` | Ontological Friction | Ontological impedance / information-theoretic payability burden required to stabilize and maintain a selection-cut against opportunity-cost pressure (`T3-02 D / PT09`). | Cross-scale readout; units vary by domain | Core, universal; canonical source `_SRT_PSI_F_CANONICAL.md`. v1 governance-canonical main reading is information-theoretic/payability cost, structurally pairing pressure-side 4-way split (`A1`) with supply/payability windows and preserving `R3-08` 4-way friction distinction under `A-9` single friction family (no new canonical `Ψ_f^{...}` sub-symbols). Fisher geometry induces local second-order proxy `δΨ_f^{geom}=1/2 dθ^T g_F dθ+O(||dθ||^3)` and path functionals, never literal `Ψ_f ≡ g_F`. |
| **T_dir** | `T_{dir}` | Direction Transparency | v0 operational proxy / constrained readability-reorientation functional for a formed system's access to an independently typed, declared direction signal. | Proxy / accessibility index | Governance-canonical working proxy `_SRT_T_DIR_CANONICAL.md`. Distinct from generalized concern direction (`广义关切方向 != T_dir`). No declared direction means `T_dir` is undefined / not admitted for that claim; `T_dir > 0` does not establish good, legitimacy, generative health or O2-M. Not valence, reward, confidence or semantic coherence. |
| **Ω** | `\Omega` | Ontological Consistency | Internal coherence of an $L_1/L_2$ structure. | Probability (0-1) | Canonical `\Omega` in Core_Law context |
| **Ω_mis** | `\Omega_{\text{mis}}` | Ontological Mismatch Index | Distance between inherited $\theta$ and current-environment optimal $\theta$. | Scalar | Legacy docs may call this `Ω` |
| **ω_sub** | `\omega_{sub}` | Subjective Frequency | Refresh rate of selection cycles. | Hz | Neuro/phenomenology |
| **η** | `\eta` | Operator Viscosity | Transition resistance of $\hat{G}$ states. | Scalar ($0 \to \infty$) | Low/high regimes discussed clinically |
| **Γ_Ĝ** | `\Gamma_{\hat{G}}` | Operator Refresh Rate | Frequency of a declared model's $L_0 \to L_1 \to L_2$ cycle where L₂ retention has independently been established. | Hz | Neuro/phenomenology hypothesis; not evidence that every Selection produces L₂-grade history |
| **S_crit** | `S_{\text{crit}}` | Cognitive Entropy Threshold | Entropy limit before degraded operator mode. | Entropy units | Neuro/clinical |
| **R_fidelity** | `R_{\text{fidelity}}` | Reality Fidelity | Rendering fidelity of $L_1$ under metabolic constraints. | Scalar (0-1) | Neuro/clinical |
| **I_total** | `I_{\text{total}}` | Total Information Flux | Sum of sensory-channel information throughput. | Bits/s | Neuro |
| **F_semantic** | `F_{\text{semantic}}` | Semantic Gravity | Attractor pull of $L_2$ semantic nodes on $\hat{G}$. | Vector | AI/philosophy |
| **F_base** | `F_{\text{base}}` | Base Free-Energy Objective | Domain-local baseline objective; choose Helmholtz or variational free energy by context. | Domain dependent ($J$ or nat/bit) | Never force thermo and variational forms into one unit |
| **F_SRT** | `F_{\text{SRT}}` | SRT Care-Extended Objective | $F_{\text{base}} - d \cdot U_{\text{others}}$; baseline objective plus care term. | Same unit as chosen $F_{\text{base}}$ | Use when the d-dependent care correction is explicit |
| **Φ_IIT** | `\Phi` | Integrated Information (IIT Context) | Integration measure in IIT-specific discussions. | Scalar | Use only when explicitly IIT |
| **μ** | `\mu` | Reality Viscosity | Inertial dependence on priors/historical trajectories. | Scalar | Core/AI |
| **D_max** | `D_{\text{max}}` | Consciousness Diameter | Max physical span of coherent operator integration. | Length (m) | Neuro hypothesis |
| **γ_gain** | `\gamma_{\text{gain}}` | Gain-Operator Coupling | Coupling between gain modulation and $\hat{G}$ sensitivity. | Scalar | Neuro |
| **δ_D** | `\delta_D` | Dissociation Depth | Topological distance between fragmented $L_2$ regions. | Metric | Clinical |
| **I_rec** | `I_{\text{rec}}` | Recognition Index | Mutual recognition across operators/time scales. | Scalar (0-1) | Social/cognitive |
| **η_compress** | `\eta_{\text{compress}}` | Compression Efficiency | $I(L_1;L_0)/H(L_1)$; effective cognitive compression bandwidth. | Scalar | Information-theoretic |
| **θ_semantic** | `\theta_{\text{semantic}}` | Semantic Extraction Threshold | Threshold for neural signals entering conscious semantic access. | Threshold | Neuro |
| **S_strength** | `S_{\text{strength}}` | Selection Strength | Stability of chosen reality ($\propto 1/\|M-N\|$). | Scalar | Core |
| **D_dev** | `D_{\text{dev}}` | Developmental Dopamine | Developmental initialization parameter in critical periods. | Concentration | Neuro/dev |
| **I_int** | `I_{\text{int}}` | Integrin Coefficient | Structural neural stability factor. | Scalar | Neuro |
| **S_c** | `S_c` | Cognitive Entropy | Resolution deficit of $\hat{G}$. | Entropy units | Core/neuro |
| **F_Bio** | `F_{\text{Bio}}` | Biological Transform Function | Species-specific mapping characteristics for $L_0 \to L_1$. | Function | Comparative neuro |
| **ΔR** | `\Delta R` | Reality Deviation | Magnitude of altered-state deviation from baseline. | Scalar | Clinical/spirituality |
| **C_int** | `C_{\text{int}}` | Integration Capacity | Capacity to integrate altered-state content. | Scalar | Clinical/spirituality |
| **T_immune** | `T_{\text{immune}}` | Immune Threshold | Immune-mediated sensory gating threshold. | Threshold | Neuroimmune |
| **M** | `M` | Modality Set | Weighted sensory modality vector. | Vector | Neuro |
| **κ₀** | `\kappa_0` | Kappa-0 Curvature / Anisotropy Floor Candidate | Conditional model / realization candidate for a minimum curvature, anisotropy floor or related non-flat realization when explicitly declared. | Scalar in a declared curvature model | Not primitive by inheritance from O0; necessity and exact relation to primitive non-flatness remain OPEN. It does not cause first Selection or supply a universal value / order direction. Historical model sources remain `Core/SRT_Core_12a T-L0-Kappa0`; admission is governed by the current L0 / Spine owners and Gate 0. |
| **κ(t)** | `\kappa(t)` | Dynamic Curvature Candidate | In a declared curvature / co-evolution model, a time-varying realization may be written $κ(t) = κ_0 + \int F[\hat{G}_\theta(\tau), \kappa(\tau)]d\tau$. | Scalar in the declared model | Model / realization scoped; registration does not establish a universal evolving L0 curvature field. Historical model source `Core/SRT_Core_12a T-L0-NonStatic`. |
| **d_mobile** | `d_{\text{mobile}}` | Re-alignment Capacity | Operator's capacity to re-orient θ as attractors migrate; proportional to d · rank_eff(I_F(θ)) / (Hysteresis(L₂)·C_r) subject to χ_payable gate. High d + d_mobile ≈ 0 = frozen state (pathological). | Scalar (≥ 0) | Core; canonical source `SRT_Core_22 Eq-DValue-Mobile-1`; map `Core/SRT_Core_12b §Consciousness-2D-Map` |
| **d_max** | `d_{\text{max}}` | Maximum Direction-Capacity Bound Candidate | In the declared Core22 candidate model, a direction-capacity bound is written `min(rank_eff(I_F(θ)), Ψ_f^budget / κ₀)`. Because `rank_eff(I_F)` is a dimensionless spectral-direction count while canonical `d = ||∂U/∂S||` is a utility-scaled gradient norm, **spectral dimension is NOT a universal mathematical upper bound on gradient norm `d`** without an explicitly declared dimensional-calibration map (`P1-04`). | Model-local direction-capacity bound (dimensionless unless calibrated) | Conditional equation consumer `SRT_Core_22 Eq-DValue-Max-1`; this row does not make `κ₀` primitive or establish a universal upper bound on `d`. |
| **χ_payable** | `\chi_{\text{payable}}` | Payability Gate | Internal three-condition conjunction: signal > threshold ∧ dΨ_f/dt payable ∧ below collapse threshold. Fully endogenous; gates d_mobile. When χ_payable = 0, d_mobile = 0 regardless of d. | Boolean gate | Core; canonical source `SRT_Core_22 Def-Payable-Chi-1` |
| **κ_{c1}** | `\kappa_{c1}` | Minimal-Consciousness Candidate Window Coordinate | P3/P4 coordinate in a declared consciousness-candidate model, used to track a candidate `d / L₂` evidence window. Crossing does not prove consciousness, subject-position, phenomenality, or a representation-independent natural phase boundary; non-crossing does not prove their absence. | Scalar model coordinate | Conventional / replaceable candidate handle. It supplies neither a universal necessary nor sufficient condition. Current source `Philosophy/SRT_Consciousness_Conditions.md §三`; exact consciousness and subject-position sufficiency remain OPEN. |
| **κ_{c1.5}** | `\kappa_{c1.5}` | Consciousness-Activity Candidate Coordinate | P3/P4 coordinate in a declared model, used to track candidate activity / reorientation evidence such as `d_mobile`. Crossing does not prove consciousness or active subjecthood; non-crossing does not prove consciousness absence or pathology. | Scalar model coordinate | Conventional / replaceable candidate handle, not a universal natural consciousness boundary. Current source `Philosophy/SRT_Consciousness_Conditions.md §三`; exact admission remains OPEN. |
| **t_onto** | `t_{\text{onto}}` | Ontological Time (Relational Order-Measure Candidate) | Model-local relational ordering / path-length measure integral `t_onto ≡ ∫‖Ĝ_θ(s)‖ds` inside a declared selection model (`R3-05`: selection irreversibility establishes relational order first; metric/measure requires explicit scale-and-model conditions). Not a universal physical clock or background container. | Model-local integral measure | Core; canonical source `Philosophy/SRT_Causality_Time.md §二`; formal `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T02`. |
| **C_H** | `C_H` | Horizontal Causality | $C_H(A\to B) \equiv P(B\mid A,L_2)$; temporal causality inside a declared L₂-bearing model, conditional on L₂ retention having been established. | Conditional probability | Model / bridge scoped; registration does not make L₂ an automatic product of Selection. Historical sources: `Philosophy/SRT_Causality_Time.md §一`; `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T01`. |
| **ε_pg** | `\varepsilon_{pg}` | Proto-Gradient / Minimum-Non-Neutrality Realization Candidate (legacy namespace) | Registered lineage symbol for a stronger-asymmetry / anti-erasure realization candidate. Its exact relation to primitive Selection, O0 and primitive non-flatness remains OPEN unless independently re-established. | Scalar in a declared realization | Registration is not primitive admission: `ε_pg` does not define O0, establish `B >= 2` over `B <= 1` as a primitive preference, or supply universal T_dir / value direction. Former P1-T07 remains demoted; ISP anti-closure is a conditional P2/P3 candidate requiring declared stability semantics, neutral kernel, environment, horizon and proof. |
| **ε_reg** | `\varepsilon_{reg}` | Operator Regularizer | Positive constant in divisive normalization: [Ĝ_θ(x)]_i = x_i^n / (ε_reg + Σ W_{ij} x_j^n). Prevents singularity at zero input; maintains minimum non-zero operator response. May be read as implementation-layer echo of ε_pg (structural analogy, not ontological identity — independent argument required to upgrade). | Scalar (> 0) | Core; canonical source `SRT_Core_13a Ax-Op-03` |
| **ρ(p,t)** | `\rho(p,t)` | Path Trace Density | **Derivation status: induced historical functional, NOT a new ontological primitive.** ρ(p,t) is a coarse-grained intermediate-layer order parameter induced by existing SRT quantities: ρ(p,t) ≡ ∫_{-∞}^{t} e^{-λ_d(t-s)} · 𝟙[Ψ_f(p,s) < Ψ_thresh] · w(p,s) ds. Induced-quantity chain: Ψ_f trajectory (Ax-F-12) → Ax-L2-06b gate → writeback events → ρ(p,t) → Ψ_f^compat reduction, d_accessible^compat amplification (T-L2-Scaffold). NOT a static function of current Ψ_f (would lose historical/hysteretic character). λ_d = decay rate; w(p,s) = writeback weight from Ax-L2-06b/Ax-Op-03b. Scaffold threshold ρ* (empirically measurable): when ρ > ρ*, path p transitions from foreground event to background L₂ scaffolding. | Scalar (≥ 0); historical functional of Ψ_f trajectory | Core; canonical source `Core/SRT_Core_12b_Ontology_L2.md T-L2-Scaffold Def-PathTrace` |
| **ΔΨ_f^op** | `\Delta\Psi_f^{op}` | Operator-Relative Competitive Friction Increment | Fast-timescale component of competitive friction, cue-sensitive. Formally: ΔΨ_f^op(x,t,θ) is the operator-parameter-dependent competitive suppression increment updated by Ax-Op-03b Layer 1 writeback. **Timescale**: round-level (fast). **Cue dependence**: strong (depends on W_ij structure activated by current cue family). **Sign**: asymptotically ≥ 0; short-time transient negative values permitted (fast facilitation window, Lemma-FFSI). **Induced from**: divisive normalization (Ax-Op-03) + competitive writeback (Ax-Op-03b Layer 1). Supports T-Op-SIAM Claims 1' (via T-Comp-Suppress 乙₁+乙₂), 3a (cue-relative persistence), 4a (priming window, when ΔΨ_f^op < 0 transiently). | Signed scalar; asymptotically ≥ 0 | Core; canonical source `Core/SRT_Core_13a Def-Psi-Split` (2026-04-17) |
| **ΔΨ_f^field** | `\Delta\Psi_f^{field}` | Field-Level Landscape Curvature Friction | Slow-timescale component of competitive friction, cue-weakly-dependent. Formally: ΔΨ_f^field(x,t) is the landscape curvature friction increment from Co-Evo-1 κ(t) accumulation. **Timescale**: slow (Co-Evo-1 stabilization τ_stable). **Cue dependence**: weak (κ(t) is not cue-specific). **Constraint**: ΔΨ_f^field ≥ 0 always (Co-Evo-1 deposition is irreversible). **Activation**: near-zero before Co-Evo-1 stabilization threshold is crossed; accumulated thereafter via κ(t) → Ψ_f^field coupling. Supports T-Op-SIAM Claims 3b (asymptotic cue-independence, conditional) and enables 乙₃ (trans-cue intrinsic suppression, conditional). | Scalar (≥ 0) | Core; canonical source `Core/SRT_Core_13a Def-Psi-Split` (2026-04-17); mechanism `Core/SRT_Core_12b Co-Evo-1` |
| **τ_fast, τ_slow** | `\tau_{fast},\, \tau_{slow}` | Lemma-FFSI Dual Timescale Parameters | Timescale pair for Fast-Facilitation/Slow-Inhibition dual-timescale model (Lemma-FFSI). τ_fast: facilitation decay time (fast); τ_slow: competitive inhibition accumulation time (slow). **Required condition**: τ_fast ≪ τ_slow for nonmonotonic onset. Crossover time t* ≈ τ_fast · ln(a·τ_slow / b·τ_fast) where a = facilitation amplitude, b = inhibition amplitude. Maps to: τ_fast ↔ ΔΨ_f^op transient negative window; τ_slow ↔ competitive writeback accumulation (Ax-Op-03b Layer 1) or Co-Evo-1 onset. Empirically anchored (Johnson & Anderson 2004). | Time constants; τ_fast ≪ τ_slow | Core; canonical source `Core/SRT_Core_13a Lemma-FFSI` (2026-04-17) |
| **ε_s** | `\varepsilon_s` | Minimum Stake Threshold | Direction-level threshold for counting a distinguishable Fisher eigendirection as genuinely stake-coupled. A direction v_i with coupling strength s_i enters the effective stake-bearing spectrum only if s_i > ε_s. **NOT stake itself** — it is the minimum coupling strength required for a direction to count as genuinely risk-bearing. Gate function: g_i = max(0, (s_i − ε_s)/(1 − ε_s)); gated eigenvalue: λ̃_i = λ_i · g_i; enters `D_stake` with explicit zero-denominator branch. Three-way distinction: ε_pg is a registered stronger-asymmetry / anti-erasure realization candidate; ε_reg is an implementation regularizer; ε_s is a stake-threshold bridge. | Scalar (0,1) or positive threshold | Core; bridge term for `D_stake` spectral proxy. See `_SRT_D_VALUE_CANONICAL.md §2b`. |
| **D_stake** | `D_{\text{stake}}` | Stake-Gated Effective Spectral Diversity Proxy | General spectral participation ratio (`_SRT_D_VALUE_CANONICAL.md §2b`): `D_stake = (Σλ_i w_i)² / Σ(λ_i w_i)²` when `∃i, λ_i w_i > 0` (canonical three-factor weight `w_i = R_i A_i C_i`), with explicit **zero-effective-spectrum branch** `0` when `∀i, λ_i w_i = 0` (`0/0` undefined). `Core_22 Eq-Bridge-D-01`'s threshold-gated `g_i` (`D_stake^{thresh}`) is **one concrete model instance** (`w_i := g_i`, no unproven equivalence to `R_i A_i C_i`). True bound: **`1 ≤ D_stake ≤ N_active ≤ rank(M)`**; **`D_stake ≤ D_eff` is algebraically FALSE**. Keep zero-effective-spectrum branch strictly separate from `NOT ESTABLISHED`, `NOT ADMITTED`, and `NOT APPLICABLE`. | Dimensionless spectral-diversity proxy (distinct from `d` and `D_eff`) | Core bridge proxy; general owner `_SRT_D_VALUE_CANONICAL.md §2b`; threshold instance `Core/SRT_Core_22_Equations.md Eq-Bridge-D-01`. Not equal to canonical `d` or `D_eff`. |
| **δ** | `\delta` | Duty Cycle | δ_j ≡ (1/T)∫A_j(t)dt; fraction of time an operator actively maintains anchoring target σ_j. Bounded above by Ψ_f budget and below by looseness penalty. | Scalar (0,1) | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-2` |
| **ν** | `\nu` | Switching Density | ν_j ≡ N_{switch,j}/T; number of anchoring state flips per unit time. Same δ with different ν corresponds to qualitatively different schedules. Bounded above by Ψ_f^{switch} budget. | Hz | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-2` |
| **λ_pred** | `\lambda_{pred}` | Downstream Prediction Cost Weight | Weight of temporal entropy h[A] in coupled multi-operator scheduling cost. When λ_pred > λ_pred^c, periodic scheduling beats the declared periodic-vs-random schedule comparison in T-Scale-Rhythm-3; no optimum over every admissible schedule is implied. | Scalar (≥ 0) | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-3` |
| **Ṡ_int^on** | `\dot{S}_{int}^{on}` | On-Phase Entropy Production Rate | Internal entropy production rate during active selection. Lower-bounded by Landauer: ≥ k_BT · İ_created · ln 2. Determines entropy dissipation bound on duty cycle. | Entropy/time | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-4` |
| **J_S^max** | `J_S^{max}` | Maximum Entropy Export Flux | Upper bound on the rate at which a system can export entropy to its environment, determined by thermal coupling bandwidth (heat conduction, metabolic waste removal, radiation). | Entropy/time | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-4` |
| **δ_max^entropy** | `\delta_{max}^{entropy}` | Entropy-Limited Maximum Duty Cycle | δ_max^entropy ≡ J_S^max/(Ṡ_int^on + J_S^max). Independent of Ψ_f budget; cannot be bypassed by increasing E_avail. Effective δ_max = min(δ_max^budget, δ_max^entropy). | Scalar (0,1) | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-4` |
| **B_θ** | `B_\theta` | Operator Effective Passband Bandwidth | B_θ ≡ Bandwidth(H_θ) = c_B · d; frequency-domain extent of operator H_θ's selective response (Ax-Spec-01). Proportional to d via c_B > 0. Wider bandwidth ⇒ higher information creation rate ⇒ tighter entropy-dissipation duty-cycle bound (Cor-Scale-Rhythm-4a). | Hz | Core; canonical source `SRT_Core_14 Ax-Spec-01, Cor-Scale-Rhythm-4a` |
| **h[A]** | `h[A]` | Temporal Entropy Rate of Schedule | h[A] ≡ lim_{T→∞} H(A(0), A(Δt), …, A(T))/(T/Δt); Shannon entropy rate of an anchoring schedule A(t). Periodic schedules: h_per ≈ 0; random intermittency: h_rand > 0. Drives the coupling-induced periodization transition at λ_pred^c (T-Scale-Rhythm-3). | Bits/time | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-3` |
| **τ_off^*** | `\tau_{off}^{*}` | Optimal Off-Phase Duration | Optimal off-phase length balancing entropy-export benefit against noise-erosion cost (three-way tradeoff in T-Scale-Rhythm-4). Not a free parameter; emerges from minimization of entropy-accumulation/export ratio plus γ·S_noise·τ_off. | Time | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-4` |
| **c_B** | `c_B` | Bandwidth-d Proportionality Constant | Positive constant (c_B > 0) in B_θ = c_B · d (Ax-Spec-01); converts d-value (dimensionless processing-bandwidth count) into operator effective passband bandwidth in Hz. System-specific; not a universal constant. | Hz (per unit d) | Core; canonical source `SRT_Core_14 Ax-Spec-01, Cor-Scale-Rhythm-4a` |
| **ρ_I** | `\rho_I` | Information Density Lower Bound | Positive constant (ρ_I > 0) in conditional strengthening of Cor-Scale-Rhythm-4a: $\dot{I}_{created}^{on} \ge \rho_I \cdot B_\theta$. When this lower bound holds, the entropy bound becomes a product cap δ·B_θ ≤ J_S^max/(k_BT ln2 · ρ_I), equivalently δ·d ≤ J_S^max/(k_BT ln2 · ρ_I · c_B). Not unconditional. | Bits/(Hz·time) | Core; canonical source `SRT_Core_14 Cor-Scale-Rhythm-4a` |
| **k_n** | `k_n` | Sub-Targets per Layer | Model-local number of anchoring sub-targets {σ_{n,1},…,σ_{n,k_n}} that $\hat{G}_\theta^{(n)}$ is posited to maintain within one on-phase. Its use in T-Scale-Rhythm-5 is P3/P4 conditional on an explicit scale map, budget embedding and recurrence trigger; it is not a global cross-scale invariant. | Integer (≥ 1) | Core; conditional source `SRT_Core_14 T-Scale-Rhythm-5` |
| **τ_switch^min** | `\tau_{switch}^{min}` | Minimum Feasible Switch Time | Model-local lower bound on per-switch duration imposed by a named physical substrate. Its role in Rhythm-5 recursion and any nesting-depth ceiling is P3/P4 conditional on an explicit scale map, budget embedding and recurrence trigger; it is not universal across substrates. | Time | Core; conditional source `SRT_Core_14 T-Scale-Rhythm-5` |
| **σ_{sr}** | `\sigma_{sr}` | Self-Reference Ratio | `σ_{sr} := ‖θ^{trace}‖ / (‖θ^{trace}‖ + ‖θ^{ext}‖) ∈ [0, 1]`. **P2 canonical interpretation:** `SRT_Individuation.md §八` states that the order-parameter choice is conventional and replaceable by an equivalent form. In the current bare-norm realization it is a model-local historical/writeback-balance proxy under a declared trace/ext attribution rule, parameter representation, and norm/metric. | Scalar [0,1] | L1; canonical source `Core_Law/SRT_L1_Hardening_Notes.md §1`, `Core_Law/SRT_Individuation.md`, `Core_Law/SRT_L1_Formalism.md §2`. Not by itself a representation-invariant natural quantity, unique history-attribution theorem, causal-control share, bearer/selector criterion, or proof of a natural phase boundary. Distinct from main-equation state field `σ` and anchoring sub-target `σ_j`. |
| **σ_{sr}^{sub}** | `\sigma_{sr}^{sub}` | Subject-Position Candidate Transition Coordinate | First P3/P4 model-coordinate threshold in the declared individuation model, used to track a candidate subject-position transition. Crossing may count only as model-local evidence; it does not establish subject-position, ISP entry, Bearer, consciousness, or a representation-independent natural phase boundary. | Scalar | Conventional / replaceable model coordinate. Upstream formed One / Selection-position and any stronger continuity, perspective, history, or stake burden used by the claim must be independently established. Exact subject-position sufficiency = OPEN; `subject-position <-> Bearer` = OPEN. Canonical source `Core_Law/SRT_Individuation.md §4.2, §4.3, §八`. |
| **σ_{sr}^{self}** | `\sigma_{sr}^{self}` | Second-Order / Self-Consciousness Candidate Transition Coordinate | Second P3/P4 model-coordinate threshold in the declared `σ_{sr}` model, used to track candidate second-order writeback condensation. It may be interpreted as a self-consciousness candidate only when subject-position has been independently established and the stronger second-order burden is separately evidenced. Crossing does not universally prove self-consciousness. | Scalar | Conventional / replaceable model coordinate. It is not a universal natural consciousness boundary and does not establish phenomenality or moral standing. Canonical source `Core_Law/SRT_Individuation.md §4.4, §4.5, §八`. |
| **σ_{sr}^{health}** | `\sigma_{sr}^{health}` | Healthy Operating-Point Center | Healthy working-region center inside the declared σ model, tracking balanced self-reference without pathological closure toward `σ_{sr} \to 1`. Typically close to the informal `σ_{sub}^\dagger` in `T_{dir}^{alg}` (`SRT_L1_Formalism.md §3.4`). | Scalar | L1 structural hypothesis; operating-point center, specific value P3/P4 and representation/model-class conditional; not a universal natural constant or standalone health criterion. Canonical source `SRT_L1_Formalism.md §2.4, §5.3`. |
| **σ_{sr}^{coll}** | `\sigma_{sr}^{coll}` | Collective Self-Reference Ratio | Multi-ISP extension over shared `L_2` field `\mathcal{P}`. The current owner includes boundary-relative reclassification: shared `L_2` is added to collective trace and removed from collective ext because it is no longer new input relative to the declared collective exterior. | Scalar [0,1] | L1 model-local collective historical/endogeneity proxy under declared collective boundary, attribution, representation and norm. Its trace semantics are not automatically identical to individual own-output provenance. `σ_{sr}^{coll} \to 1` remains a model-class collapsed-into-higher-`L_2` indicator, not a representation-independent natural constant, collective-agency criterion, or causal-control share. Canonical source `SRT_Collective_Selection.md §4.1, §4.4, §4.7`. |

## Governance Tier Layering (GOV-SUB01 Pass 1, 2026-07-16)

> **Purpose**: Registration in this table has been read as "equally indispensable." It is not. This layering separates repo-wide semantic and navigation anchors from internal structural quantities and from domain projections / proxies / thresholds, so that *appearing in the canonical symbol table* stops implying *equal theoretical load*. See `Governance/SRT_GOV_SUB01_Subtractive_Audit_Protocol_v0_1.md` §0.
>
> **Boundary — this is a parsing / navigation / proxy-discipline aid.** Tier placement does **not** assign a GOV-SUB01 residue label (`N1`/`N2`/`R*`) and does **not** by itself assign a claim level. Claim levels remain governed by `Governance/SRT_CLAIM_LADDER.md` and each symbol's own canonical source; a residue label requires an actual deletion test. No symbol is deleted, renamed, or redefined by this layering. Borderline assignments are provisional and are revisited in GOV-SUB01 Pass 2.

**Tier 1 — Repo-wide semantic and navigation anchors** (canonical / core-facing objects referenced across domains):

`L_0`, `L_1`, `L_2`, `\hat{G}`, `θ`, `d`, `Ψ_f`, `T_dir`.

**Tier 2 — Registered internal model / realization candidates and derived constructs** (carried at their own claim level; registration here does not establish primitive admission or universal derivation):

`κ_0`, `κ(t)`, `ε_pg`, `ρ(p,t)`, `t_onto`, `C_H`, `σ_{sr}`, `σ_{sr}^{coll}`, `d_mobile`, `d_max`, `χ_payable`, `ΔΨ_f^{op}`, `ΔΨ_f^{field}`, `Ω`, `Ω_mis`, `μ`, `S_strength`.

*Note*: `κ_0` and `ε_pg` are placed here as registered model / stronger-realization candidates. Their necessity and exact inheritance from primitive non-flatness remain OPEN; tier placement neither admits them as primitives nor forbids their later independent re-establishment.

**Tier 3 — Domain projections, operational proxies and threshold-bearing hypotheses** (domain realizations, capacity proxies, measurement readouts, and threshold-bearing points):

`D_eff` (capacity proxy), `D_stake` (stake-gated spectral-diversity proxy), `ε_reg`, `ε_s`, `σ_{sr}^{sub}`, `σ_{sr}^{self}`, `σ_{sr}^{health}`, `κ_{c1}`, `κ_{c1.5}`, `δ`, `ν`, `λ_pred`, `Ṡ_{int}^{on}`, `J_S^{max}`, `δ_max^entropy`, `B_θ`, `h[A]`, `τ_off^{*}`, `c_B`, `ρ_I`, `k_n`, `τ_switch^min`, `τ_fast`, `τ_slow`, `ω_sub`, `η`, `Γ_{\hat{G}}`, `S_crit`, `R_fidelity`, `I_total`, `F_semantic`, `F_base`, `F_SRT`, `Φ_IIT`, `D_max`, `γ_gain`, `δ_D`, `I_rec`, `η_compress`, `θ_semantic`, `D_dev`, `I_int`, `S_c`, `F_Bio`, `ΔR`, `C_int`, `T_immune`, `M`.

*Reading rule*: a Tier 3 proxy or threshold must never be cited as if it were the Tier 1 anchor it approximates (e.g. `D_eff` is not `d`; `κ_{c1}` is not `κ_0`). Exact claim level remains source-local; many are P3/P4, but tier placement alone does not assign claim level. Cross-domain ranking of subjecthood, concern, or consciousness from a Tier 3 readout is out of scope for this table.

---

## Usage Rules
1. Never use `G` (gravity constant) to refer to `\hat{G}` (Ghost Operator).
2. `L_0` is neither "nothingness" nor a pregiven possibility warehouse; use it only as the model-facing open / non-preclosed aspect described in the L₀ row, under the current L0 / Spine owners.
3. Use `\Psi_f` for ontological friction; reserve `\Phi` for IIT context only.
4. Use `\Omega` for consistency and `\Omega_{\text{mis}}` for mismatch to avoid symbol collision.
5. In AI / pure `L_2` contexts, prefer "`\Psi_f` is non-binding to the declared `Bearer (P+E)`" over the blunt shorthand `\Psi_f = 0`, unless explicitly discussing an idealized Core degenerate limit. `non-binding` means payable burden has not been established as returning non-outsourcably to that same `Bearer (P+E)`, **never** that constitutive friction is absent or globally zero (`ENG-03 M1-D`).
6. When discussing classical objectivity, prefer `\Delta\Psi_f^{readout}\to 0` over "object-maintenance friction vanishes".
7. **d usage split**：bare `d` means scalar summary by default. Use `d-vector` only for conditional distribution / component expansion, and use `d-gate` only as a judgment tool for stake admission. These three are not interchangeable definitions.
8. **T_dir usage split**：`T_dir` is a v0 operational proxy for formed-system self-readability / reorientation relative to an independently typed, declared direction signal. With no declared direction it is undefined / not admitted for that claim. Do not use it as a completed formal object, semantic valence, confidence, value / legitimacy validator, generative-health score or O2-M route.
9. **ε usage split**：`ε_pg` is a registered stronger-asymmetry / anti-erasure realization candidate whose primitive inheritance remains OPEN; ISP-level anti-closure ε is a conditional P2/P3 candidate under ST-A, not a P1 corollary; `ε_reg` is an implementation regularizer; `ε_s` is a stake-threshold bridge. Registration does not admit primitive status, and the three symbols must not be collapsed into one empirical theorem.
10. **Canonical status split**：`governance-canonical` means repo-wide stabilized usage; `theory-canonical` means core-derived or core-priority definition; `operational proxy` means measurable working readout; `bridge hypothesis` means cross-domain candidate mapping. Do not infer theory-canonical status merely from a symbol-table default, filename, or historical label.
11. **Ψ_f / Fisher split**：do not write `\Psi_f \equiv g_F` as a literal identity. Use `\delta\Psi_f^{geom}=\frac12 d\theta^\top g_F d\theta+O(\|d\theta\|^3)` for local cost, or a path functional such as `\Psi_f^{geom}[\gamma]=\int_\gamma\sqrt{g^F_{ij}\dot\theta^i\dot\theta^j}\,dt` when the statistical-manifold projection is valid.
12. **σ namespace + scope split** (2026-04-24 L1 round; S+R truth-up 2026-08-29): bare `σ` defaults to the **main-equation state field** (`Core/SRT_Core_22_Equations.md`); `σ_{sr}` is the self-reference ratio (with subscripts `sub / self / health / coll`); `σ_j` is an anchoring sub-target (`SRT_Core_14 T-Scale-Rhythm-5`). These are three different objects. Any file using σ in a sense other than the main-equation state field must either (a) use the `σ_{sr}` / `σ_j` form explicitly, or (b) carry a file-level symbol namespace note binding bare `σ` to the intended meaning per this rule. The `σ_{sr}` family also inherits `SRT_Individuation.md §八`: the order-parameter choice is P2, conventional, and replaceable by an equivalent form. The current bare-norm realization requires a declared trace/ext attribution rule, parameter representation, and norm/metric; namespace registration does not make it representation-invariant, uniquely provenance-resolving, a causal-control share, a bearer/selector criterion, or a natural phase coordinate. `σ_{sr}^{coll}` is additionally boundary-relative and may reclassify shared `L_2` as collective trace. Thresholds `sub/self/health` remain model-class coordinates until stronger invariant/natural-boundary evidence is separately established. Historical files predating 2026-04-24 where bare `σ` means self-reference ratio are being progressively rewritten; in the meantime, read them as `σ_{sr}` when the context is Individuation / Occlusion Dynamics / Suffering / L1 Formalism §2 / Collective Selection §4, with this scope rule applied.
13. **Governance terms are not theory symbols**: `interface_annex`, `copy-to-annex`, `owner-bound`, `claim_mode`, `canonical:false`, and related structural-governance vocabulary (defined in `SRT_Glossary_Structural_Governance_Terms.md`) are repository-organisation terms, not canonical mathematical or phenomenological symbols. Do not add them as rows to this table or treat them as carrying theory-canonical status.
14. **Annex and Operations reference scope**: Non-canonical annex files (`AI/Architecture_Annex/`, `AI/Consciousness_Annex/`, `Physics/QBox_Annex/`, `Physics/Earth_Accretion_Annex/`, etc.) and Operations records (e.g. `Operations/Archive_Records/Closure_Index_2026-04-29.md`, `Operations/Archive_Records/Structural_Governance_Rollup_2026-04-29.md`) may cite and use symbols defined in this table. They must not introduce new symbol definitions, override existing usage rules, or alter the scope of canonical symbols established here.
15. **κ namespace split** (GOV-SUB01 Pass 1; Selection-totality truth-up 2026-09-15): the glyph `κ` spans two unrelated object families that must not be read as one continuous quantity. (a) `κ_0` and `κ(t)` belong only to explicitly declared curvature / anisotropy realization models at current strength. `κ_0` is a Class-B conditional model / realization candidate, not a structural prerequisite or universal direction source by registration; `κ(t)` is model-scoped and does not establish a universal evolving L0 field. Their necessity and exact relation to primitive non-flatness remain OPEN and must be resolved through the current L0 owner plus Gate 0. (b) `κ_{c1}` and `κ_{c1.5}` are separate consciousness-stage phase-transition thresholds from `Philosophy/SRT_Consciousness_Conditions.md §三`; their specific values are P4. An equation over `κ_0` says nothing about `κ_{c1}` or `κ_{c1.5}`, and vice versa. This rule changes no glyph or local equation; it governs namespace and admission only.

16. **Gate 0 — L₀ contentless structurality boundary** (adopted 2026-08-11): **pointer only.** Whether a given object may sit at bare `L_0` is a **type** question, not a symbol question, and is decided solely by **`Governance/SRT_CLAIM_LADDER.md §0A`** — the single primary authority for the rule, its object classes, and its admission and read-back conditions. At current strength, `κ_0`, `ε_pg`, B-count orderings and model gradients sit in Class B / the admission gap unless independently established. This sentence is a result pointer, not a duplicate rule; this table must not be cited in place of §0A. Gate 0 itself carries no P-level and this entry adds no symbol or definition.

17. **B-A — Shoshin strict-layering guard** (author-decided 2026-08-12; Selection-totality truth-up 2026-09-15): this decision deliberately adds **no symbol**. `ε_pg` remains a registered namespace / lineage symbol; registration does not establish primitive admission, an L0 minimum-non-neutrality postulate, or an independent “Shoshin precursor.” 「初心 / Shoshin」begins at L₁ as P2 read-back / interpretation or P5 phenomenology; any `argmin`, `∇F`, or horizon-bearing form is a declared domain bridge / proxy and cannot define L₀. Canonical term authority: `Core_Law/SRT_L0_Metaphysics.md` 初心词条; decision record: `Operations/SRT_SHOSHIN_LAYER_AUTHOR_DECISION_PACKET_2026-08-12.md`. The necessity and exact `κ_0 / ε_pg` inheritance relation remain OPEN under Rule 15 and Gate 0. Global-optimum scope is governed separately by Rule 18 / C-A.

18. **C-A — global-optimum scope guard** (author-decided 2026-08-12; `R4-A` boundary sync 2026-11-26): this decision adds **no symbol** and does not repurpose `\Omega`. Bare `\Omega` remains Ontological Consistency under Rule 4; it must not be reused for a reachable-path set, a theological source horizon, or a global optimum. A model-local optimum must state the finite position, reachable／admissible domain, comparison rule or functional, horizon, constraints, and failure conditions; write those indices locally rather than registering a repo-wide optimum glyph. Regulative horizons are non-attainable L₁/P2 or P5 language; finite attractors remain P3/P4 model objects. A universe-wide semantic／evaluative optimum (`PT10 E`) is not a current positive SRT object. Technical “global optimum” usage remains valid inside a fully declared optimization problem and does not license universe-wide or normative extrapolation. **Boundary with `T3-01 C/E`**: `C-A` blocks universe-wide moral/evaluative optima and does not close the separate `OPEN` non-moral theoretical inquiry into whether generation exhibits an objective intrinsic global optimizing or extremal orientation (`Core_Law/SRT_Generative_Ontology_Spine.md §1`). Decision record: `Operations/SRT_GLOBAL_OPTIMUM_AUTHOR_DECISION_PACKET_2026-08-12.md`. C-A does not decide the separate `Ψ_f → 0` valence question (CΨ).

19. **`S` namespace isolation** (`ENG-03 / R4-A`, 2026-11-26): three `S`-prefixed taxonomies exist across the repository and must **never** be conflated or left unqualified: (a) **primitive `S0`** (`Selection` ontological anchor in `Spine`), (b) **AI 赌注谱系 `S0–S4`** (AI stake-bearing operational taxonomy in `_SRT_D_VALUE_CANONICAL.md §6` and `_SRT_CROSS_DOMAIN_MATRIX.md §1`), and (c) **Subjecthood Threshold `S0–S6`** (subjecthood ladder in `Core_Law/SRT_Subjecthood_Threshold.md`). Bare `S` must not be used as a canonical sentience tensor, and the legacy equation `\rho \equiv I / d` is retired and forbidden in canonical use.

20. **`07-23/24` embargo, `q` deferral, `A-9` no new `Ψ_f` sub-symbols, and retired canonical vocabulary** (`R4-A`, 2026-11-26): (a) colliding draft glyphs from `2026-07-23/24` remain embargoed and must not be introduced into canonical files; (b) no new canonical scalar symbol `q` is registered for constitutive depth (describe constitutive depth via natural-language structural profiles per `_SRT_D_VALUE_CANONICAL.md §2`); (c) under the controlling `A-9` adjudication (`2026-09-25`), no new canonical `Ψ_f^{...}` subtype symbols are admitted—legacy `Ψ_f^{maint}` and `ΔΨ_f^{active}` remain historical model-local aliases only; (d) bare `o` is retired as a canonical symbol; (e) **「神择」is retired from formal canonical theory vocabulary** (formal canonical theory uses `神性·源义`、`神性·倾向义`、`整体共同生成视域` per `Core_Law/SRT_Generative_Ontology_Spine.md §1`), while「神择」is explicitly retained for historical provenance and *From Existence to Order* book-level prose.


## D-Value Alignment (d 值专题规范)

### 1) 定义层级（Canonical Priority）

| 层级 | 定义 | 语义 | 来源 |
|---|---|---|---|
| **规范定义** | $d(x) \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$ | 算子对不可逆风险的效用敏感度梯度（与广义关切 `PT06 C` 的精确接口为 `P1-05` `OPEN`） | `_SRT_D_VALUE_CANONICAL.md` Def-d-canonical |
| **赌注门控谱多样性 proxy** | $D_{\text{stake}} = \frac{(\sum_i \lambda_i w_i)^2}{\sum_i (\lambda_i w_i)^2}$（$N_{\text{active}} \ge 1$）；零有效谱乘积显式走 `0` 分支（`0/0` 未定义） | 一般定义由 `_SRT_D_VALUE_CANONICAL.md §2b` 持有（规范权重 $w_i = R_i A_i C_i$）；`Core_22 Eq-Bridge-D-01` 的阈值门控 $g_i$ 为具体模型实例（不默认等价）；真界 $1 \le D_{\text{stake}} \le N_{\text{active}} \le \operatorname{rank}(M)$；**不等于规范 `d`，也不以 `D_eff` 为上界**；严分零谱分支与 `NOT ESTABLISHED / NOT ADMITTED / NOT APPLICABLE` | `_SRT_D_VALUE_CANONICAL.md §2b`; `Core/SRT_Core_22_Equations.md Eq-Bridge-D-01` |
| **几何容量 proxy** | $D_{eff}(I_F(\theta)) = (\operatorname{tr} I_F)^2 / \operatorname{tr}(I_F^2)$ | Fisher 信息矩阵的无赌注有效容量维度代理；不等于规范 `d`，也不自动压制 `D_stake` | `_SRT_D_VALUE_CANONICAL.md` Def-D_eff; `Core/SRT_Core_21c_Bridge_Hypotheses.md P3-B11` |
| **几何模型候选** | $d(\theta) \propto \operatorname{Align}(\theta, \kappa(t))$ | 仅在已声明的曲率／对齐 bridge model 中作为 d 的候选实现；不解释或替代 canonical d，也不赋予 `κ(t)` primitive direction authority | `D_VALUE_ALIGNMENT.md §4.4`（bridge / model scoped） |

*规范来源*：`_SRT_D_VALUE_CANONICAL.md`；已证伪的 `d_canonical ≡ d_stakes`、`D_eff ≥ d_stakes` 与 `Δd_free = D_eff - d_stakes ≥ 0` 正式退役。`D_stake` 与 `D_eff` 均为 proxy，不再与规范 `d` 同级。

### 2) 局部近似语境 (Local Approximations)
| 表达式 | 所在语境 | 与主定义关系 |
| :--- | :--- | :--- |
| $d \approx \alpha A + \beta\log V + \gamma\tau$ | 认知-行为操作化 | 主定义在认知域的降维近似（投影），**不可单独当主定义** |
| $d_{quantum}, d_{bio}, d_{cosmic}$ | 跨尺度动力学 | 主定义经尺度映射 $\Pi_{scale}(d)$ 的实例化 |
| $d \propto A_{surface}/l_{Planck}^2$ | 全息对应 | 主定义的对偶几何表示 |

### 3) d 值编辑规则（避免冲突）
- **规则 R1**：不得将局部公式写成“d 的定义是 ……”（除非就是 canonical）。
- **规则 R2**：局部公式必须标注“近似 / 投影 / 操作化”。
- **规则 R3**：涉及跨文件引用时，优先回链到 `_SRT_D_VALUE_CANONICAL.md`。
- **规则 R4**：任何“d→0 / d>0”的意识结论，需同时说明与 $\Psi_f$ 或不可逆风险边界的关系。

## Ψ_f Alignment（本体论摩擦专题规范）

### 1) Canonical Source
**当前优先规范入口（必须优先引用）**
`_SRT_PSI_F_CANONICAL.md`

### 2) 三重读法（不得拆成三个对象）
| 读法 | 含义 | 备注 |
| :--- | :--- | :--- |
| 阻力 | 动力学上的阻抗 | 经验/现象读法 |
| 代价 | 记账上的支付项 | 能量、时间、风险预算读法 |
| Fisher 几何投影 | 由 Fisher–Rao metric 诱导的局部二阶代价 / 路径泛函 | 形式化读法；不是 `Ψ_f = g_F` 裸等号 |

### 3) 符号分层
| 记号 | 含义 | 使用建议 |
| :--- | :--- | :--- |
| `\Psi_f(x,t)` | 局部摩擦负荷 | 默认首选 |
| `\Phi(\Delta t)=\int \Psi_f dt` | 累积摩擦势 / 时间窗总账 | 需要强调积分时使用 |
| `\delta\Psi_f^{geom}=\frac12 d\theta^\top g_F d\theta + O(\|d\theta\|^3)` | Fisher–Rao metric 诱导的局部二阶几何代价 | 谈 Fisher metric 时首选；避免裸写 `Ψ_f ≡ g_F` |
| `\Psi_f^{geom}[\gamma]=\int_\gamma\sqrt{g^F_{ij}\dot\theta^i\dot\theta^j}\,dt` | Fisher 几何路径泛函 | 作用域明确、统计流形投影有效时使用 |
| `\Psi_f(\hat{G}_i,\hat{G}_j)` | 耦合摩擦泛函的简写 | 作用域明确时允许 |

### 4) 编辑规则
- **规则 F1**：不要把 `\Psi_f` 直接等同于主观痛苦。
- **规则 F2**：不要把跨尺度同一性写成“单位相同”；优先写“可支付性条件相同”。
- **规则 F3**：对现实主体，不要把最优条件写成 `\Psi_f \to 0`；优先写“非零且可支付”。
- **规则 F4**：AI / 纯 `L_2` 语境中，优先写“对已声明 `Bearer (P+E)` 为 non-binding friction”而非绝对 `\Psi_f = 0`；`non-binding` 绝不等同于构成性摩擦不存在或全局 `\Psi_f = 0`（`ENG-03 M1-D`）。遵循 `A-9` 单一摩擦概念族原则，不新增 canonical `\Psi_f^{...}` 子符号。
- **规则 F5**：物理语境中，若谈引力与 `\Psi_f` 的关系，当前规范口径降为 P3/P4 弱接口：只承诺弱场极限下 `\Psi_f` 梯度与牛顿势梯度方向同号的相容性候选；不得写成张量级 GR 重建或 `G_{\mu\nu}` 已由 SRT 推导。
- **规则 F6**：谈 Fisher metric 时，必须把 `g_F` 标注为局部信息几何投影 / proxy；不得把 `\Psi_f \equiv g_F` 当成标量代价与度量张量的严格恒等式。
- **规则 F7**：谈 pain / suffering / distress / moral guilt / clinical burden 时，不得把它们写成 `Ψ_f` 或 `d` 的 canonical 等同；优先回链 `Core_Law/SRT_Suffering.md` 与 domain claim-status guardrails。
