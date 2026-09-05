---
id: SRT-CONTEXT-BUNDLE-DOMAIN-NEUROSCIENCE-2026-09-05
type: context_bundle
status: active
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
generated: 2026-09-05
source_commit: f5bb1965
source_branch: theory/author-reentry-cycle1-one-formation-20260905
source_dirty: false
inputs_digest: 10c8811b1d3d1bb0
---

# SRT 神经科学领域上下文包

> **这是什么**：由 `scripts/build_srt_context_bundles.py` 从 SRT 仓库自动拼装的上下文包。
> 收录神经科学领域的 claim-status 护栏、领域导航与 CompactCore 主线。
>
> **这不是什么**：不是新的 canonical 文件，不是摘要，不是改写。每个来源文件的正文
> 逐字保留；脚本只把 YAML frontmatter 转成显式 provenance 头。**若本包与仓库中的
> 来源文件冲突，以仓库为准**——本包是快照，会随仓库演进而过期。

## §0 生成信息

| 项 | 值 |
|---|---|
| 生成日期 | 2026-09-05 |
| 来源 commit | `f5bb1965` |
| 来源分支 | `theory/author-reentry-cycle1-one-formation-20260905` |
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
| 1 | `Neuroscience/SRT_Neuroscience_Claim_Status.md` | 2026-08-12 |
| 2 | `Neuroscience/SRT_Neuroscience_Reconstruction_Framework.md` | 2026-09-04 |
| 3 | `Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md` | 2026-08-12 |
| 4 | `Neuroscience/README.md` | 2026-09-04 |
| 5 | `Neuroscience/SRT_Neural_Mechanisms_CompactCore.md` | 2026-08-12 |
| 6 | `Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md` | 2026-05-19 |

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

*授权依据：`Governance/SRT_CLAIM_LADDER.md`（P0–P5 阶梯）与 `SRT_AI_START.md` §5 / §8*

- 不得把 former P1-T07 当作已证 P1 定理引用；P1 引用仅限 absorption remainder。
- Stable ISP 的 P1 最低条件是 continued selectability；generative reselectability 与 ISP-level anti-closure 按 P2/P3 conditional candidate 引用。
- 关于 `τ<∞` 只能作**语义分层**的陈述：若某条 realized history 满足 `τ<∞`，可无条件断言的仅是**该历史上的 S1 / pathwise stability 失败**；process-level 的 S2 需 `P(τ<∞)>0`，S3 需 `P(τ=∞)=0`。**在 S1/S2/S3 语义未选定之前，不得据此推出无条件的 process-level 「not a stable ISP」。**
- 不要假装 `ε-neutral` 已有形式定义，也不要从 `ε_pg`、irreversibility、fixed point、metastability 或 `σ<1` 单独推出 anti-closure。


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

For non-trivial SRT work:

1. recover current programme direction from the 2026-09-05 author correction + governance amendment; treat stale `STATUS.md` wording as historical until synchronized;
2. read Architecture v2 under that amendment for the retained Domain Reconstruction Layer;
3. distinguish current historical/canonical authority from prospective ontology reconstruction;
4. state whether the claim is author intuition, open ontology problem, Constitution interface, Domain Framework synthesis, domain model/hypothesis, Deep Well/evidence, bridge/lab, material evidence or governance;
5. do not close listed open tensions;
6. for ontology / Constitution work, use author re-entry + source recovery + mature-neighbor pressure rather than greenfield or historical-file auto-completion;
7. for a newly selected/revised domain, map relevant open ontology questions, strongest neighbors and common residual problem before forcing a deep well;
8. do not treat bearer/objectification as the whole domain ontology;
9. for domain increment, use Case A/B/C only after a bounded author-owned SRT response exists;
10. preserve the two existing deep wells as local calibration pilots; do not infer whole-SRT identity from them;
11. do not open a third main well until explicit author release;
12. prefer explicit boundaries to broad unification language.

---

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
| `Neuroscience/SRT_Neuroscience_Claim_Status.md` | frontmatter claim_mode=audit | ✓ | — |

**展开层**（4 个）

| 文件 | 分类依据 | registry 提及 | AI_START §2 |
|---|---|:---:|:---:|
| `Neuroscience/README.md` | frontmatter claim_mode=- | — | — |
| `Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md` | frontmatter claim_mode=bridge | ✓ | — |
| `Neuroscience/SRT_Neural_Mechanisms_CompactCore.md` | frontmatter claim_mode=bridge | ✓ | — |
| `Neuroscience/SRT_Neuroscience_Reconstruction_Framework.md` | frontmatter claim_mode=synthesis | — | — |

**导航**（1 个）

| 文件 | 分类依据 | registry 提及 | AI_START §2 |
|---|---|:---:|:---:|
| `Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md` | frontmatter type=index / claim_mode=navigation | ✓ | — |

### 未收录支持文件

**First Sources 点名、文件存在、但本包未收（14 个）**——回答涉及它们时本包不足以裁定：

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

**⚠ 高严重度：registry 提及但文件不存在（1 个）**——指向已删除、拼错或尚未创建的路径。**这类条目不会被静默过滤掉**，因为它本身就是一种 manifest 差异：

| 失效路径 | 说明 |
|---|---|
| `Core_21_Formal_Axioms.md` | 见 §0.2 G4：这是 `Core/SRT_Core_21_Formal_Axioms.md` 的行文简写，非真实路径 |

**registry 提及、文件存在、但本包未收（90 个）**——多为领域主轴、
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
- `Core_Law/SRT_Constitution_V1.md`
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
- `Neuroscience/SRT_Clin_02_FEP.md`
- `Neuroscience/SRT_Consciousness_Mechanisms.md`
- `Neuroscience/SRT_Neural_Mechanisms.md`
- `Neuroscience/_SRT_Neuro_Axioms.md`
- `Neuroscience/_SRT_Neuroscience_Hardening_Index.md`
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

## FILE: `Neuroscience/SRT_Neuroscience_Claim_Status.md`

| 字段 | 值 |
|---|---|
| path | `Neuroscience/SRT_Neuroscience_Claim_Status.md` |
| id | SRT-NEUROSCIENCE-CLAIM-STATUS |
| claim_mode | audit |
| status | active_v1 |
| epistemic_layer | governance |
| layer | meta |
| canonical(字段) | false |
| last_commit | 2026-08-12 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：[SRT-NEURO-AXIOMS-CLAIM-STATUS, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-AI-CLAIM-STATUS, SRT-PHILOSOPHY-CLAIM-STATUS]

<!-- 以下为原文逐字保留 -->

# SRT Neuroscience / Clinical Claim Status

> **Role**: folder-level guardrail for neuroscience, clinical, FEP, PCI/IIT, pathology, NDE, neuroimmune, advanced-model, and BioQuantum language.
> **Canonical status**: not canonical. Neuroscience files are bridge / lab / interface materials unless separately promoted through the claim ladder.

---

## 1. Default claim levels

- neural mechanism mapping: P2/P3 bridge if tied to evidence;
- measurement proxy: P4 unless validated;
- clinical interpretation / treatment implication: P4/P5 and never medical advice;
- NDE / psychedelic / self-dissolution interpretation: P4/P5 phenomenological bridge;
- AI consciousness comparison: P3 bridge only when architecture-state is explicit;
- BioQuantum mechanism mapping: P3/P4 hypothesis unless independently replicated and causally bridged from molecular to neural scale.

**C-A scope guard（2026-08-12）**: broader neural integration, field coherence, global availability, higher PCI／Φ, or more accessible paths do not imply canonical `d↑` or approach to a universe-wide optimum. Any neural optimization claim must name its task, candidate set, readout, horizon, constraints and rival models; “global” in global workspace／whole-brain state is a system-scope term, not C-A's prohibited universe-global optimum.

---

## 2. High-risk claim classes

### 2.1 `Ψ_f` as free energy, prediction error, pain, metabolism, or clinical burden

Allowed:

> FEP quantities, prediction error, metabolic cost, pain, stress, clinical distress, and recovery cost may be used as local `Ψ_f`-related proxies under a stated measurement window.

Forbidden:

> `Ψ_f = free energy`; `Ψ_f = pain`; `Ψ_f = prediction error`; `Ψ_f = metabolism`; `Ψ_f -> 0` means no experience; `Ψ_f -> infinity` as literal clinical divergence.

Guardrail: canonical `Ψ_f` is not any single neural, metabolic, subjective, or clinical variable. Use `Ψ_f^{proxy}`, `selection-friction proxy`, `felt burden`, `prediction-error proxy`, or `metabolic/recovery-cost proxy`.

### 2.2 `d-value` as PCI/Φ/salience/reward/arousal/integration/attention

Allowed:

> PCI, Φ, integration, salience, arousal, precision, threat relevance, and reportability may constrain or proxy aspects of consciousness-state assessment.

Forbidden:

> `d = Φ`; `d = PCI`; `d = salience`; `d = attention`; `d = reward`; `d = integration`; `d = arousal`.

Guardrail: `d-value` requires stake-coupled consequence sensitivity. High neural complexity or high subjective intensity is not sufficient.

### 2.3 NDE / psychedelic / self-dissolution / terminal lucidity

Allowed:

> These states may be modeled as boundary loosening, `L2` destabilization, altered anchoring, increased subjective openness, or state-dependent `d` proxies.

Forbidden:

> NDE proves post-brain consciousness; NDE is not hallucination as a settled fact; psychedelic state means actual `d -> infinity`; terminal lucidity proves brain irrelevance.

Guardrail: use `d^{subjective/provisional}` or `d^{state-proxy}`. Do not write actual infinite `d` for finite neurophysiological states.

### 2.4 Clinical / pathology / treatment language

Allowed:

> Pathology may be modeled as altered anchoring, parameter drift, rigid `L2`, disrupted gating, or cross-system desynchronization.

Forbidden:

> pathology is only θ deviation; treatment = parameter correction; therapy = topology reset; immune/neural intervention treats everything; SRT gives direct clinical diagnosis.

Guardrail: all clinical claims require differential diagnosis, standard-of-care boundaries, and functional impairment / suffering / risk checks. SRT files are theory interfaces, not medical advice.

### 2.5 AI / blindsight / high-Φ low-d comparisons

Allowed:

> Blindsight, high-Φ systems, Chinese-room cases, and current LLMs may be compared as dissociation cases between processing/integration and stake-coupled anchoring.

Forbidden:

> current AI has globally `d=0`; pure symbol manipulation necessarily has no `Ψ_f` in all possible architectures; blindsight proves SRT.

Guardrail: AI claims must follow `AI/AI_POSITIONING_NOTE.md` and `AI/SRT_AI_Claim_Status.md`: inference-only / non-history-bearing / non-embodied deployment unless stated otherwise.

### 2.6 BioQuantum / microtubule / CISS / nuclear-spin language

Allowed:

> A phase-coherent, spin-sensitive, CISS, radical-pair, tunnelling, vibrational, or microtubule process may be treated as a mechanism-specific physical interface when its own survival condition and molecular-to-neural transduction chain are stated.

Forbidden:

> short `T_2` or `τ_coh` falsifies every quantum-sensitive biological mechanism; CISS or nuclear-spin dependence proves consciousness is quantum; a microtubule effect establishes Orch-OR; quantum-sensitive anaesthesia explains subjectivity; spin filtering directly derives `L_0`, `d-value`, `Ψ_f`, or value.

Guardrail: do not use a universal decoherence threshold for the whole BioQuantum family. Separate phase-coherence gates (`T_2`) from spin/CISS gates (`T_1`, chirality, orientation, permeability/binding), radical-pair gates, tunnelling gates, and substrate-specific confounds. The 2018 xenon-isotope result remains a single-study empirical anchor pending independent replication; the 2026 CISS account is a perspective plus kinetic model, not direct molecular confirmation. Follow [`SRT_Neuro_09_BioQuantum_CISS_Amendment.md`](SRT_Neuro_09_BioQuantum_CISS_Amendment.md).

---

## 3. Preferred replacements

| Risk phrase | Safer replacement |
|---|---|
| `Ψ_f = free energy` | `free energy may serve as a local Ψ_f-related proxy under a stated FEP window` |
| `Ψ_f = pain` | `pain / distress may index Ψ_f-related felt burden under specified conditions` |
| `d -> infinity` in NDE/psychedelic states | `d^{subjective/provisional}` or `d^{state-proxy}` increases / boundary loosening |
| `d = 0` for AI or blindsight | `stake-coupled d proxy is near-null in this specified dissociation case` |
| `treatment = parameter correction` | `treatment may target parameter, context, body, relation, and stabilization layers` |
| `pathology iff θ deviation` | `many pathologies can be modeled as θ-space deviations; not a biconditional` |
| `immune/neural intervention treats X` | `candidate interface; clinical use requires standard evidence and differential diagnosis` |
| `τ_coh < τ_min, therefore no quantum contribution` | `this weakens the specified coherence-dependent mechanism; test other mechanisms with their own survival and transduction gates` |
| `CISS proves quantum consciousness` | `CISS is a candidate molecular transduction mechanism for a reported isotope-sensitive anaesthetic effect` |

---

## 4. Reading rule

Read this file before using neuroscience or clinical material in canonical, public, medical, AI-consciousness, spirituality-facing, or quantum-consciousness claims. If a neuroscience sentence contains equation-like language about `Ψ_f`, `d`, consciousness, pathology, NDE, treatment, AI, microtubules, CISS, nuclear spin, or quantum mechanisms, assume it is bridge/proxy/hypothesis until proven otherwise. For BioQuantum material, the mechanism-family boundary in [`SRT_Neuro_09_BioQuantum_CISS_Amendment.md`](SRT_Neuro_09_BioQuantum_CISS_Amendment.md) overrides the universal-decoherence wording in `SRT_Neuro_09_Integ_Eq.md` §IV until direct owner-file integration.



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
| last_commit | 2026-09-04 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：Core_Law/SRT_Constitution_V1.md, Operations/Proposals/SRT_CONSTITUTION_DOMAIN_ARCHITECTURE_V2_2026-09-04.md, Operations/Templates/SRT_DOMAIN_RECONSTRUCTION_FRAMEWORK_TEMPLATE.md, Neuroscience/SRT_Neuroscience_Claim_Status.md, Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md, Neuroscience/_SRT_Neuroscience_Hardening_Index.md, Operations/Proposals/SRT_CONSTITUTION_PHASE8_NEUROSCIENCE_DEEP_WELL_CHARTER_2026-09-03.md, Operations/Audits/SRT_CONSTITUTION_PHASE8A_NEUROSCIENCE_BASELINE_DATA_ACCESS_AUDIT_2026-09-03.md, Operations/Audits/SRT_CONSTITUTION_PHASE9_NEUROSCIENCE_PRODUCTIVE_ADEQUACY_REVIEW_2026-09-03.md, Operations/SRT_CONSTITUTION_DOMAIN_SEQUENCE_AUTHOR_DECISION_2026-09-03.md

<!-- 以下为原文逐字保留 -->

# SRT Neuroscience Reconstruction Framework v0.1

> **Role**: this is the active Layer-2 problem map for neuroscience under Architecture v2. It sits between `SRT_Constitution_V1.md` and specific neuroscience theories / hypotheses / deep wells.
>
> **It is not** a neuroscience Constitution, a new neural axiom set, a replacement for domain claim-status files, or a promotion of the old `SRT_Neural_Mechanisms*` architecture.
>
> **Claim ceiling**: this framework may reorganize questions and inherited assets. It does not by itself establish a new neural mechanism, a new empirical effect, a privileged SRT proxy, or a Case-C neuroscience increment.

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
next programme action = construct Epistemology Domain Reconstruction Framework before extending the active second well
```



---

## FILE: `Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md`

| 字段 | 值 |
|---|---|
| path | `Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md` |
| id | SRT-NEUROSCIENCE-COMPACT-REGISTRY |
| claim_mode | navigation |
| status | active_v2 |
| epistemic_layer | os |
| layer | meta |
| canonical(字段) | false |
| last_commit | 2026-08-12 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：[SRT-CANONICAL-REGISTRY, SRT-NEUROSCIENCE-CLAIM-STATUS, SRT-NEURO-AXIOMS-001]

<!-- 以下为原文逐字保留 -->

# SRT Neuroscience Compact Registry

> **Metadata cleanup note（2026-05）**：本 registry 是 navigation layer，`canonical: false`；它路由 neuroscience materials，不定义 `d-value`、`Ψ_f`、consciousness、clinical diagnosis 或 treatment claims。
本页汇总 Neuroscience 板块当前的 compact core、桥接入口、claim-status guardrail 与 hardening draft，并给出最短阅读路径。

## 0. Current structure

Neuroscience 现在采用五层结构：

1. **Directory / Registry Layer**：目录入口、compact registry、机器可读分流。
2. **Canonical-facing Bridge Layer**：神经科学三域映射、公理化桥接、历史 theorem / hypothesis 标签。
3. **Formal Compact Core Layer**：当前正式 compact core，承载最新神经机制与意识机制主干。
4. **Hardening / Lab Draft Layer**：N1-N9 工作草稿、实验路线、未来 citation 层。
5. **Longform / Measurement Layer**：长文、临床测量、IIT/PCI 接口与扩展讨论。

重要警戒：`_SRT_Neuro_Axioms.md` 是 canonical-facing hybrid bridge，不应被整文件当作 all-canonical definition source。claim-level 状态必须参考 `SRT_Neuro_Axioms_Claim_Status.md`。

---

## 1. Neuroscience Entry Coverage

### A. Directory / Registry Layer

- `README.md` — human-facing directory entry; separates canonical-facing material, compact cores, and hardening drafts.
- `NEUROSCIENCE_COMPACT_REGISTRY.md` — this compact registry.
- `SRT_Neuroscience_Claim_Status.md` — folder-level guardrail for clinical, FEP, NDE, AI-comparison, `Psi_f` proxy, and `d-value` proxy language.
- `SRT_Neuro_Axioms_Claim_Status.md` — claim-status audit for `_SRT_Neuro_Axioms.md`; prevents file-level canonical over-reading.

### B. Canonical-facing Bridge Layer

- `_SRT_Neuro_Axioms.md` — historical / formal neuroscience bridge. Use with claim-status audit. Do not assume every internal theorem/proxy/discourse claim is canonical.

### C. Formal Compact Core Layer

- `SRT_Neural_Mechanisms_CompactCore.md` — current formal compact core for neural mechanisms. Integrates the 2026-04 N1-N5 / N7-N9 hardening.
- `SRT_Consciousness_Mechanisms_CompactCore.md` — current formal compact core for consciousness mechanisms. Integrates N6: consciousness as stable concern-weighted `L1` anchoring.

### D. Hardening / Lab Draft Layer

- `SRT_Neuroscience_Hardening_N1_N9_v0_1.md` — full staging draft for the 2026-04 N1-N9 neuroscience hardening cycle. Non-canonical unless later promoted through the claim ladder.
- `SRT_NB1_MOFC_LOTTERY_EXECUTION_CARD_v0_1.md` — local P4 execution card for one bounded neural divisive-normalization → frozen readout → task-choice test. Card-defined only; not formally locked or executed.
- `SRT_NB1_W0_DATA_ACCESS_PROVENANCE_2026-08-12.md` — W0 public-source inventory, Lane A access gate, and unsent minimum data/code request; access remains unknown.
- `_SRT_Neuroscience_Hardening_Index.md` — domain index for hardening drafts and Pipeline 1 material patches.
- `patches/` and `hooks/` — Pipeline 1 patch notes and integration hooks. These are bridge records, not canonical definitions.

### E. Longform Counterparts

- `SRT_Neural_Mechanisms.md` — longform neural mechanisms text. May lag behind compact core until fully synchronized.
- `SRT_Consciousness_Mechanisms.md` — longform consciousness mechanisms text. May lag behind compact core until fully synchronized.

### F. Clinical / Measurement Layer

- `SRT_Clin_00_IIT_PCI.md` — clinical / measurement interface around IIT, PCI, and consciousness-state measurement. Should be read with the N6 hardening: PCI/Φ-like measures are not by themselves identical with SRT consciousness; SRT also requires `L1` anchoring, `d-value`, action/self coupling, and possible `L2` sedimentation.

---

## 2. Recommended Reading Order

### 最短主线（第一次进入 Neuroscience）

1. `README.md`
2. `SRT_Neuroscience_Claim_Status.md`
3. `SRT_Neuro_Axioms_Claim_Status.md`
4. `SRT_Neural_Mechanisms_CompactCore.md`
5. `SRT_Consciousness_Mechanisms_CompactCore.md`
6. `SRT_Neuroscience_Hardening_N1_N9_v0_1.md`（if you need the full N1-N9 staging record）

### canonical-facing bridge path

1. `_SRT_Neuro_Axioms.md`
2. `SRT_Neuro_Axioms_Claim_Status.md`
3. `SRT_Neural_Mechanisms_CompactCore.md`
4. `SRT_Consciousness_Mechanisms_CompactCore.md`

### research / lab path

1. `SRT_Neuroscience_Hardening_N1_N9_v0_1.md`
2. `SRT_NB1_MOFC_LOTTERY_EXECUTION_CARD_v0_1.md`（for the selected local P4 workline）
3. `SRT_Neural_Mechanisms_CompactCore.md` §10 experimental roadmap
4. `SRT_Consciousness_Mechanisms_CompactCore.md` boundary cases and hardest objections
5. `SRT_Clin_00_IIT_PCI.md`

### 第二层展开

1. `SRT_Neural_Mechanisms.md`
2. `SRT_Consciousness_Mechanisms.md`

---

## 3. Role Split

| Layer | File(s) | Role | Canonical caution |
|---|---|---|---|
| Directory / Registry | `README.md`, this file | navigation and read order | not a theory source |
| Claim-status audit | `SRT_Neuro_Axioms_Claim_Status.md` | classifies claim status of `_SRT_Neuro_Axioms.md` | audit, not replacement |
| Canonical-facing bridge | `_SRT_Neuro_Axioms.md` | formal neuro bridge and historical axiom/discourse container | hybrid; not all internal claims are canonical |
| Compact core | `SRT_Neural_Mechanisms_CompactCore.md`, `SRT_Consciousness_Mechanisms_CompactCore.md` | current concise formal neuroscience summary | hardening content is bridge/lab unless promoted |
| Hardening draft / lab card / material patches | `SRT_Neuroscience_Hardening_N1_N9_v0_1.md`, `SRT_NB1_MOFC_LOTTERY_EXECUTION_CARD_v0_1.md`, `_SRT_Neuroscience_Hardening_Index.md`, `patches/`, `hooks/` | full N1-N9 staging record, bounded P4 execution card, and Pipeline 1 neuroscience patch records | non-canonical working drafts / bridge records |
| Longform | `SRT_Neural_Mechanisms.md`, `SRT_Consciousness_Mechanisms.md` | expanded material | may lag compact core |
| Measurement | `SRT_Clin_00_IIT_PCI.md` | clinical / PCI / IIT interface | measurement proxies are not identities |

---

## 4. N1-N9 Integration Map

| N-claim | Primary integrated file | Secondary reference |
|---|---|---|
| N1 neural systems as embodied selection systems | `SRT_Neural_Mechanisms_CompactCore.md` | `_SRT_Neuro_Axioms.md` Ax-NEURO-1 |
| N2 composite `G_hat_theta` | `SRT_Neural_Mechanisms_CompactCore.md` | N1-N9 draft |
| N3 `Psi_f` as selection friction | `SRT_Neural_Mechanisms_CompactCore.md` | `_SRT_Neuro_Axioms.md` H-NEURO-4b / Ax-NEURO-5 |
| N4 `L2` sedimentation | `SRT_Neural_Mechanisms_CompactCore.md` | N1-N9 draft |
| N5 `d-value` | `SRT_Neural_Mechanisms_CompactCore.md` | N1-N9 draft |
| N6 consciousness as stable concern-weighted `L1` | `SRT_Consciousness_Mechanisms_CompactCore.md` | `SRT_Clin_00_IIT_PCI.md` |
| N7 psychopathology | both compact core files | N1-N9 draft |
| N8 experimental roadmap | `SRT_Neural_Mechanisms_CompactCore.md` | `SRT_NB1_MOFC_LOTTERY_EXECUTION_CARD_v0_1.md` for the first selected bounded workline |
| N9 mainstream-theory distinction | `SRT_Neural_Mechanisms_CompactCore.md` | N1-N9 draft |

---

## 5. Current Open Optimization Tasks

1. Add citation layer for N1-N9.
2. Refine the `Psi_f` proxy hierarchy: core proxies, physiological proxies, neural proxies, historical proxies, forbidden identities.
3. Further distinguish `d-value` from salience, reward, precision, motivational relevance, subjective value, affective valence, arousal, and self-relevance.
4. Formally lock and preregister `NB1-MOFC-Lottery-v0`: data access, recovery/power simulation, rival/readout/tolerance/event freeze, ethics/SOP, and immutable adjudication code.
5. Add sync warnings to longform files if compact cores remain ahead of them.
6. Regenerate graphify-out / wiki artifacts after merge.

---

## 6. Compact Doctrine

The current neuroscience compact doctrine is:

> SRT treats the nervous system as an embodied selection system. Candidate percepts, actions, judgments, and conscious contents emerge from accessible latent spaces through competition, gain modulation, gating, and stabilization. `Psi_f` captures multidimensional anchoring friction; `d-value` captures concern-weighted consequence; `L2` captures sedimented selection constraints. Consciousness is stable concern-weighted `L1` anchoring. Psychopathology is a distortion of anchoring dynamics. Existing neuroscience theories are treated as partial mechanisms inside a broader selection-anchoring architecture, not as direct equivalents of SRT.



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
| last_commit | 2026-09-04 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

<!-- 以下为原文逐字保留 -->

# Neuroscience

> **Architecture v2 routing · 2026-09-04**: `SRT_Neuroscience_Reconstruction_Framework.md` is the active Layer-2 problem map for new/backfilled neuroscience research. It does not replace claim-status owners or promote legacy mechanisms. The pre-Architecture mechanism / axiom / compact-core layer remains a historically governed library unless a current framework problem family or active task explicitly routes into it.
>
> **Legacy-layer dormancy note**: the older `Neuroscience/` mechanism corpus was placed under a dormancy/library policy after the 2026-05 cycle. Its symbols and definitions may lag later canonical changes; exact definitions still follow `CANONICAL_REGISTRY.md`, `_SRT_SYMBOL_TABLE.md` and named canonical owners. The new Layer-2 Framework is an active routing surface, not a blanket reactivation of every old neuroscience file.

This directory contains SRT's neuroscience-facing reconstruction, bridge and lab materials.

## Read order

1. [`SRT_Neuroscience_Reconstruction_Framework.md`](SRT_Neuroscience_Reconstruction_Framework.md)
   Active Architecture-v2 Layer-2 problem map. Read this before opening a new neuroscience theory synthesis or deep well. It routes Given Ones, objectification choices, bearer roles, high-value materials, inherited assets and the deep-well queue.

2. [`SRT_Neuroscience_Claim_Status.md`](SRT_Neuroscience_Claim_Status.md)
   Folder-level guardrail for neuroscience, clinical, FEP, NDE, AI-comparison, `Psi_f` proxy, and `d-value` proxy language.

3. [`_SRT_Neuro_Axioms.md`](_SRT_Neuro_Axioms.md)
   Historical canonical-facing / axiomatic hybrid neuroscience bridge. Use with its claim-status audit; do not treat it as the architecture for the whole domain or as all-canonical by default.

4. [`SRT_Neuro_Axioms_Claim_Status.md`](SRT_Neuro_Axioms_Claim_Status.md)
   Claim-status audit for `_SRT_Neuro_Axioms.md`. Use this to distinguish bridge axioms, operational proxies, theorem candidates, contextual discourse, and claims needing downgrade/guardrails.

5. [`SRT_Neural_Mechanisms_CompactCore.md`](SRT_Neural_Mechanisms_CompactCore.md)
   Formal Layer-3 compact core for inherited neural mechanisms. It is a candidate mechanism package under the reconstruction framework, not the framework itself.

6. [`SRT_Consciousness_Mechanisms_CompactCore.md`](SRT_Consciousness_Mechanisms_CompactCore.md)
   Formal compact core for consciousness mechanisms. Consciousness-specific burdens remain routed to the future Consciousness Reconstruction Framework.

7. [`SRT_Neuroscience_Hardening_N1_N9_v0_1.md`](SRT_Neuroscience_Hardening_N1_N9_v0_1.md)
   Bridge / lab working draft that records the older N1-N9 hardening cycle. Architecture v2 reroutes surviving pieces by problem family rather than treating this draft as a domain skeleton.

8. [`SRT_NB1_MOFC_LOTTERY_EXECUTION_CARD_v0_1.md`](SRT_NB1_MOFC_LOTTERY_EXECUTION_CARD_v0_1.md)
   Local P4 execution card for the bounded `P3-Scale-NB1` neural divisive-normalization → frozen readout → task-choice workline. Card-defined only; not formally locked, preregistered, or executed. W0 access record: [`SRT_NB1_W0_DATA_ACCESS_PROVENANCE_2026-08-12.md`](SRT_NB1_W0_DATA_ACCESS_PROVENANCE_2026-08-12.md).

## Architecture-v2 deep-well status

- First Neuroscience deep well: matched present neural state / different relational history.
- Phase 8A: **Case B** strongest baseline + `DATA-ACCESS-0 = NO-GO` for the exact charter.
- Phase 9: **translation-only + scope-limited**.
- The adverse result is preserved; Neuroscience is conditionally reopenable under the named N-R1 / N-R2 / N-R3 rules in `Operations/SRT_CONSTITUTION_DOMAIN_SEQUENCE_AUTHOR_DECISION_2026-09-03.md`.
- No Neuroscience deep well is currently active; Epistemology remains the selected second main workline.

## Recent material bridge

- **NEURAL35 — psychedelic reopening / re-anchoring:** [`patches/SRT_Neuro_NEURAL35_Psychedelic_Reopening_Reanchoring_v0_1.md`](patches/SRT_Neuro_NEURAL35_Psychedelic_Reopening_Reanchoring_v0_1.md), with [`hooks/NEURAL35_Psychedelic_Reopening_Reanchoring_Integration_Hook.md`](hooks/NEURAL35_Psychedelic_Reopening_Reanchoring_Integration_Hook.md). P3/P4 only: its surviving increment is `reopening != reselectability`, plus `under-anchoring` as a positively testable but disposable mirror-failure label and `Opening × Reanchoring` as a complexity-controlled differential-test form. It does not redefine ST-A / Core 21C B13, and it inherits NEURAL16's BOLD proxy gate and NEURAL26's capacity/accessibility/control/write-back distinctions. **Any clinical, therapeutic, safety, or public-facing use must also retrieve [`SRT_Neuroscience_Claim_Status.md`](SRT_Neuroscience_Claim_Status.md).**

## Status distinction

- `SRT_Neuroscience_Reconstruction_Framework.md`: active Layer-2 domain problem map; question routing, material re-entry and Phase-9.5 writeback only; not canonical and not a neural mechanism owner.
- `SRT_Neuroscience_Claim_Status.md`: folder-level proxy/clinical guardrail. Read before public, clinical, AI-consciousness, FEP, NDE, or treatment-facing use.
- `_SRT_Neuro_Axioms.md`: canonical-facing hybrid bridge. Changes here require canonical caution; internal claims must be read through the claim-status audit.
- `SRT_Neuro_Axioms_Claim_Status.md`: audit / status guardrail. It does not replace the axiom file, but prevents file-level canonical over-reading.
- `SRT_Neural_Mechanisms_CompactCore.md`: inherited Layer-3 formal mechanism compact core; it does not define the domain problem architecture.
- `SRT_Consciousness_Mechanisms_CompactCore.md`: formal consciousness compact core; now treated as an adjacent Layer-3 package for future Consciousness routing.
- `SRT_Neuroscience_Hardening_N1_N9_v0_1.md`: non-canonical staging draft for theory hardening, experimental design, and future citation work.
- `SRT_NB1_MOFC_LOTTERY_EXECUTION_CARD_v0_1.md`: non-canonical local P4 protocol candidate. It may adjudicate one task-level bridge but cannot define Core terms or establish agency, subjecthood, or consciousness.
- [`../Neuroscience_Annex/`](../Neuroscience_Annex/) contains bridge/interface Annex files extracted from Neuroscience owner files. Annex files are `canonical: false` and do not define Core primitives or replace owner-file formal anchors.

## Current research path

Architecture v2 replaces the old assumption that the next step is automatically a larger N1–N13 mechanism synthesis. Current order is:

1. use `SRT_Neuroscience_Reconstruction_Framework.md` to locate the problem family;
2. recover relevant high-value SourceCards / PatchNotes / Hooks and existing owner status;
3. choose a bounded question only if the main programme sequence authorizes it;
4. run a strongest-baseline Case A/B/C gate before any SRT increment claim;
5. after a completed or legitimately blocked well, write the result back into the Framework;
6. only then decide whether any inherited mechanism synthesis actually needs revision.

The old N1-N9 / N10-N12 / NEURAL patch corpus remains available as inherited Layer-3 / evidence material, but folder location or historical “integration candidate” status does not automatically authorize synthesis.

## Cross-domain links

- PH-SS subjecthood guardrail: [`../Philosophy/SRT_Subjecthood_Threshold_Interface.md`](../Philosophy/SRT_Subjecthood_Threshold_Interface.md) — S0-S6 ladder distinguishing selection, anchoring, conscious content, subjecthood, agency, and responsibility; use when making consciousness attribution claims.



---

## FILE: `Neuroscience/SRT_Neural_Mechanisms_CompactCore.md`

| 字段 | 值 |
|---|---|
| path | `Neuroscience/SRT_Neural_Mechanisms_CompactCore.md` |
| id | SRT-NEURO-MECH-COMPACT-CORE |
| claim_mode | bridge |
| status | active_v1 |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | false |
| last_commit | 2026-08-12 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：[SRT-NEURO-AXIOMS-001, SRT-NEURO-MECH-001]

<!-- 以下为原文逐字保留 -->

# SRT Neural Mechanisms — Compact Core

> **Claim-status note（2026-05）**：This neuroscience file is bridge / lab / translation material. It applies SRT primitives but does not define `d-value`, `Ψ_f`, consciousness, pathology, diagnosis, treatment, NDE, or AI subjecthood. Read with `SRT_Neuroscience_Claim_Status.md` and, where relevant, `SRT_Neuro_Axioms_Claim_Status.md`.
> **定位**：本文件是 `SRT_Neural_Mechanisms.md` 的紧凑主干版。  
> **用途**：用于快速把握 SRT 如何把神经机制重写为选择动力学，而不是单纯信息处理。  
> **关系**：不替代原文；原文保留病理参数化、免疫接口、量子基质与工作记忆振荡等展开层。  
> **2026-04 hardening note**：本版吸收 `SRT_Neuroscience_Hardening_N1_N9_v0_1.md` 的神经选择主干，尤其是 N1-N5 / N8-N9。新增内容在功能上是 bridge / lab hardening；除非另经 claim-ladder 提升，不自动升格为 primitive axiom。

## 1. 核心问题

这篇最核心的问题是：

> **神经系统到底是在“处理信息”，还是在执行一种具身选择？**

SRT 的压缩回答是：
- 神经系统不是被动传输器
- 而是 `\hat G_\theta` 的具身实现
- 它在神经流形上把 `L_0` 压成可显现的 `L_1`

### 1.1 2026 hardening: neural selection before representation

本轮神经科学硬化把本文件的核心命题压成更可防守的形式：

> **神经系统不只是表征器；表征是选择稳定后的产物。**

因此，感知、行动、判断与意识内容不应被理解为外部输入的直接复制，而应被理解为候选状态在身体状态、注意增益、行动准备、历史权重与关切价值约束下被稳定出来的 `L_1`。

| SRT term | Neuroscience-facing interpretation |
|---|---|
| `L_0^{accessible}` | 当前系统可访问、可激活、可竞争的候选知觉 / 行动 / 解释空间 |
| `\hat G_\theta` | 竞争、增益、门控、稳定化构成的具身选择过程 |
| `L_1` | 当前被锚定的知觉、行动、判断、意识内容 |
| `L_2` | 选择历史沉积成的先验、习惯、图式、技能、情绪标记与规范内化 |
| `\Psi_f` | 候选状态稳定为 `L_1` 所需支付的多维选择摩擦 |
| `d-value` | 候选状态对身体调节、行动后果、自我模型与未来可选择性的关切权重 |

---

## 2. 神经流形与选择投影

### 2.1 Neural Manifold
\[
\sigma(t)\in \mathcal M \subset \mathbb R^N,\qquad \dot\sigma = F(\sigma,\theta,u)
\]

最压缩解释：
> **神经状态不是离散标签，而是高维流形上的连续轨迹。**

### 2.2 L0 → L1 Projection
\[
\Pi_{ignite}: \mathcal M \to \mathcal M_*
\]

其中 `\mathcal M_*` 是满足点燃阈值的稳定子集。

最短说法：
> **意识相关显现不是“活动更强”，而是轨迹被成功投影到可锚定区域。**

### 2.3 Composite `\hat G_\theta` architecture

2026 hardening 将神经层面的 `\hat G_\theta` 明确写成复合选择架构，而不是单一脑区或单一机制：

\[
\hat G_\theta^{neural}\approx \text{Stabilization}\circ \text{Gating}\circ \text{Gain}\circ \text{Competition}
\]

| Stage | Role | Candidate neural realization |
|---|---|---|
| Competition | 多个候选状态共激活但尚未稳定为 `L_1` | 侧抑制、多稳态知觉、表征竞争 |
| Gain modulation | 根据身体、注意、情绪、精度与 `d-value` 改变候选胜率 | 注意增益、精度加权、神经调质、salience network |
| Gating | 决定候选能否进入行动、报告、工作记忆或意识通达 | 基底节-丘脑-皮层环路、前额叶门控、动作选择 |
| Stabilization | 候选获得持续性并可指导行为或报告 | 递归加工、工作记忆、全局通达、可塑性 |

约束条件：不是所有神经活动都算完整的 `\hat G_\theta` 实例。只有当存在候选竞争、theta/d/L2/Psi_f 相关偏置、门控许可与稳定化结果时，才构成 SRT 意义上的现实锚定事件。

---

## 3. 归一化的 P3 机制地位

### 3.1 Canonical Normalization
\[
R_i = \frac{L_i^n}{\sigma^n + \sum_j w_{ij}L_j^n}
\]

SRT 在这里保留的主张是：
> **除法归一化是具名代谢／带宽约束下的神经竞争机制候选，不是所有选择系统的必然形式。**

### 3.2 Energy–Information Extremum
\[
\mathcal J = H(\sigma) - \lambda E(\sigma)
\]

压缩结论：
- 神经系统同时受信息收益与能量成本约束
- 归一化可作为两者权衡下的候选解；目标泛函若未指定成本函数、约束与动态，不能推出唯一解
- 相对神经响应通向行为选择还需冻结读出、阈值／累积或采样规则、执行门与 held-out 检验（P3-Scale-NB1）
- 首个具名 P4 工作线为 `SRT_NB1_MOFC_LOTTERY_EXECUTION_CARD_v0_1.md`；当前只到 card-defined 黄灯，跨研究证据不可拼成通过

---

## 4. 学习不是记忆堆叠，而是 L2 收敛

### 4.1 Predictive Update
\[
\Delta\theta \propto -\nabla_\theta F
\]

最压缩解释：
> **学习不是在 L1 上堆内容，而是在 L2 上重写未来选择规则。**

也就是说：
- 突触改变不是“存东西”这么简单
- 而是在塑造下一次 `\hat G_\theta` 如何取值

### 4.2 L2 as sedimented selection constraint

2026 hardening 将 `L_2` 的神经科学解释从“记忆/先验”扩展为：

> **`L_2` 是过往选择沉积形成的结构，它通过降低稳定路径内部的 `\Psi_f`、提高不兼容替代路径的 `\Psi_f`，来约束未来选择动力学。**

| Phenomenon | SRT reading |
|---|---|
| Habit | 重复 `L_1` 行动沉积为低摩擦 `L_2` 路径 |
| Expert intuition | 专业图式降低领域相关候选的锚定摩擦 |
| Trauma | 高 `d-value` 事件异常硬化为威胁型 `L_2` |
| Bias | 某些解释路径低摩擦化，导致过早现实锚定 |
| Norm internalization | 社会 `L_2` 被内化为个体选择地形的一部分 |

核心预测：
\[
\Psi_f(\text{trained path})\downarrow,\qquad \Psi_f(\text{incompatible alternative})\uparrow
\]

这意味着 `L_2` 硬化同时带来效率提升与可能性收缩。

---

## 5. 多尺度神经算子

### 5.1 Loop-Gating
丘脑—基底节回路不是简单通路，而是：
> **决定哪些轨迹有资格进入显现层的门控结构。**

### 5.2 Meso-Operator / Glial Pruning
\[
\hat G_{meso}: L_2^{micro} \to L_2^{pruned}
\]

压缩含义：
- 胶质剪枝不是附属维护
- 而是慢时标的结构性选择

### 5.3 Stability–Pruning Link
过度剪枝会导致：
- `L_2` 硬化
- 可塑性下降
- 病理锁定增加

---

## 6. 点燃、离散帧与摩擦

### 6.1 Ignition as Candidate Gate Family
\[
\mathcal A(\sigma) \ge \tau_{ignite} \land \Phi_{proxy}\cdot d_{proxy} > C_{critical}
\]

> **Level**: hypothesis / operational proxy. The product gate is a current structural preference; ignition as threshold or phase transition is not yet a proven neural theorem.

最短说法：
> **点燃不是激活增强；当前最小模型把它写成整合度 proxy 与关切梯度 proxy 共同约束的候选门。**

| Gate | Use | What would favor it |
|------|-----|---------------------|
| Multiplicative | structural preference when both integration and concern-gradient look jointly necessary | Either factor being low blocks ignition, and an interaction term predicts access better than linear terms alone. |
| Additive | operational fallback when compensation is observed | High integration can partly compensate low `d_proxy`, or high `d_proxy` can partly compensate low integration. |
| Probabilistic | lab-facing model for noisy / graded reports | Trial-level access is better fit by sigmoid probability than by hard threshold. |

### 6.2 Discrete Frame Theorem
\[
L_1(t)=\sum_n \text{Frame}_n\,\delta(t-t_n)
\]

压缩结论：
- 显现是离散更新帧
- 连续意识感是高频帧序列的结果

### 6.3 Prediction Error as Local Friction Proxy
\[
\widehat{\Psi}_{f,neural}^{local}(t)=\alpha_{pe}\|\varepsilon_{pred}(t)\|+\beta_{load}\mathcal L_{model}(t)
\]

> **Level**: hypothesis / operational proxy, downstream of `H-NEURO-4b`. This bridge must not be used to promote PE-based conclusions to theorem level.

这一步很关键，因为它把：
- 预测误差
- 自由能更新
- 模型竞争负荷
- 局部摩擦 proxy

压到同一条可测桥上，但不把它们写成同一对象。

`L_model` 在此指竞争内部假设的负荷：候选 latent cause、行动策略、身体状态解释或社会意图解释之间的后验歧义、有效复杂度与分歧度。实验上可用解码器后验熵、候选解释数量、ACC/PFC conflict proxy、反应时/眼动歧义指标近似；这些近似不能单独定义 `Ψ_f`。

### 6.4 `\Psi_f` as multidimensional selection friction

2026 hardening 将 `\Psi_f` 明确降格为可测潜变量，而非单一神经标记：

\[
\Psi_f(\theta)=\alpha_\theta C+\beta_\theta E+\gamma_\theta M+\delta_\theta A+\eta_\theta B+\lambda_\theta H+\rho_\theta R
\]

| Term | Meaning |
|---|---|
| `C` | 候选冲突 |
| `E` | 预测违背 / epistemic mismatch |
| `M` | 模型重构成本 |
| `A` | 行动切换与门控成本 |
| `B` | 身体负荷 / interoceptive strain |
| `H` | 历史惯性 / `L_2` 阻力 |
| `R` | 情绪、社会或实际风险 |

区别：
- `\Psi_f` 不是 cognitive effort；effort 只是其主观/行为表现之一。
- `\Psi_f` 不是 prediction error；PE 衡量不匹配，`\Psi_f` 衡量锚定成本。
- `\Psi_f` 不是 uncertainty；uncertainty 衡量候选分布分散，`\Psi_f` 衡量把分散压缩成现实承诺的成本。

---

## 7. 工作记忆与时间复用

### 7.1 Theta–Gamma Dual Mode
SRT 将工作记忆重写为：
- 持续活动模式
- theta 节律下的多吸引子分时复用模式

最压缩句子：
> **工作记忆容量不是神秘常数，而是时间调度带宽的结果。**

这也意味着：
- `d_temporal` 有可计算上限
- 容量限制是动力学结果，不是简单缺陷

---

## 8. 病理学：参数漂移，而不是症状堆叠

### 8.1 Parameter Drift
\[
\theta = \theta_{healthy} + \Delta\theta
\]

SRT 对病理学的最强改写之一是：
> **精神病理首先是参数空间的偏移，其次才表现为症状。**

这带来三个后果：
- 病理可几何化
- 病理可量化
- 治疗目标变成参数校正而不是只压表象

### 8.2 Anchoring-dynamics pathology bridge

2026 hardening 对病理学作出更细分的 reality-anchoring 解释：

| Condition | Core SRT imbalance |
|---|---|
| Anxiety | 威胁候选获得过高 `d-value`，模糊输入过早锚定为危险 `L_1` |
| Compulsion / OCD-like closure failure | 低概率高后果风险候选进入 `L_1` 后无法关闭，`\Psi_f(closure)` 持续升高 |
| Trauma | 高 `d-value` `L_1` 事件异常沉积为威胁型 `L_2` |
| Depression | 面向未来的可访问 `L_0` 收缩，正向行动候选难以锚定 |
| Addiction | 即时奖赏路径低摩擦化，替代路径摩擦升高 |
| Delusion-like salience abnormality | 低证据候选获得不成比例现实锚定权 |

原则：治疗不是把正确信息塞入系统，而是帮助系统形成新的、可重复、低摩擦、可行动的 `L_1` 锚定，并逐渐重塑 `L_2`。

---

## 9. `d-value`: concern-weighted selectability

本文件把 `d-value` 明确区别于 salience、attention、reward 与 precision：

| Concept | Question answered |
|---|---|
| Salience | 什么突出？ |
| Attention | 什么被资源处理？ |
| Reward | 什么被趋近或强化？ |
| Precision | 什么被系统信任为信息源？ |
| `\Psi_f` | 锚定需要支付多大成本？ |
| `d-value` | 什么真正关系到系统？ |

核心句：

> **Salience makes a signal noticeable; d-value makes a signal matter.**

神经层面，`d-value` 不定位于单一区域，而是内感受、奖赏/威胁、行动后果、自我相关、社会评价和未来可选择性系统的整合变量。

概念式：
\[
d(x)=w_bB(x)+w_aA(x)+w_rR(x)+w_sS(x)+w_mM(x)+w_fF(x)
\]

其中 `B` 为身体相关性，`A` 为行动后果，`R` 为奖赏/威胁，`S` 为自我模型相关性，`M` 为记忆/身份共振，`F` 为未来选择空间影响。

---

## 10. Experimental roadmap and mainstream-theory distinction

### 10.1 Minimal experimental variables

| SRT variable | Manipulation | Measures |
|---|---|---|
| `L_0^{accessible}` | 模糊图像、多稳态刺激、多义词、动作选择 | 候选报告、选择分布、眼动 |
| `d-value` | 自我相关、健康风险、金钱、威胁、身份、声誉 | 记忆、行动改变、生理唤醒、主观重要性 |
| `\Psi_f` | 冲突、规则切换、不确定反馈、关闭需求、责任负荷 | RT、错误率、瞳孔、皮电、信心、修改率 |
| `L_2` | 训练、重复、情绪标记、奖惩强化 | 迁移、偏置、逆转成本、保持率 |

旗舰实验候选：
1. 模糊知觉 × `d-value` × `L_2` 训练；
2. 规则硬化与逆转成本；
3. 高责任关闭成本任务；
4. 安全重锚定任务；
5. 未来 `L_0` 可访问性任务；
6. 成瘾替代路径摩擦任务。

### 10.2 Distinction from neighboring frameworks

| Theory | SRT absorbs as | SRT distinction |
|---|---|---|
| Predictive processing | 候选生成、误差、precision/gain | SRT 解释现实锚定，不只是模型更新 |
| FEP | 自维持底层与稳定约束 | SRT 加入 lived anchoring、`d-value` 与 `L_1 -> L_2` 沉积 |
| Active inference | 行动门控与策略选择层 | SRT 把行动解释为现实承诺与沉积路径 |
| Global workspace | `L_1` 稳定化/通达路径之一 | SRT 包含通达前竞争与通达后硬化 |
| IIT | 可能的整合结构约束 | SRT 强调关切加权锚定，而非整合度本身 |
| Reinforcement learning | `L_2` 形成机制之一 | `d-value` 宽于 reward；`\Psi_f` 宽于 prediction error |
| Embodied cognition | `\theta`、身体 d、行动 affordances | SRT 主张 reality-selection itself is bodily |

压缩区分：
> Predictive processing explains how the brain guesses the world. FEP explains how systems maintain themselves. Global workspace explains access. RL explains value updating. Embodied cognition explains bodily dependence. SRT explains how a candidate possibility, under bodily, concern-weighted, cost-constrained, and historically sedimented conditions, becomes real for the system.

---

## 11. 最压缩结论

`SRT Neural Mechanisms` 可以压缩成七句话：

1. **神经系统不是单纯信息处理器，而是具身选择算子的实现。**
2. **表征不是选择之前的原始事实，而是选择稳定后的产物。**
3. **神经显现来自流形轨迹经竞争、增益、门控、稳定化后投影进可锚定区域。**
4. **除法归一化是受限神经竞争的 P3 机制候选；它不单独产生行为选择，也不是本体必然。**
5. **学习、剪枝与工作记忆都可被统一写成多时标选择动力学。**
6. **`\Psi_f` 是候选进入 `L_1` 的多维锚定成本；`d-value` 是候选对系统的关切后果。**
7. **病理最深层上是现实锚定动力学的扭曲，而不是表面症状清单。**

---

## 12. 阅读路径

- 全量原文：`SRT_Neural_Mechanisms.md`
- Neuro bridge：`_SRT_Neuro_Axioms.md`
- Consciousness 机制：`SRT_Consciousness_Mechanisms.md`
- N1-N9 hardening draft：`SRT_Neuroscience_Hardening_N1_N9_v0_1.md`
- canonical 总注册表：`../CANONICAL_REGISTRY.md`

---

## Hardest Objections

本域若以下任一成立，则本域主张会被显著削弱：

1. Prediction error is not an independent friction proxy.
   - 当前承受方式：`H-NEURO-4b` only treats PE as a local measurable candidate, not an identity with `Ψ_f`.
   - 若成立需撤回什么：撤回 PE-to-local-friction-proxy 的局部线性桥，把相关段落降为普通 FEP comparison.

2. `Φ` and `d` cannot be independently measured in neural systems.
   - 当前承受方式：the product gate is an operational proxy and can be replaced by additive or probabilistic gates.
   - 若成立需撤回什么：撤回 `Φ_proxy·d_proxy` candidate gate as a subjectivity criterion and keep only separated diagnostic dimensions.

3. Ignition is continuous, report-mediated, or task-dependent rather than a phase transition.
   - 当前承受方式：phase-transition language is marked as hypothesis and must be tied to explicit observation windows.
   - 若成立需撤回什么：撤回 “crossing threshold” as ontology and rewrite ignition as graded stabilization.

4. Neural burden is fully reducible to generic predictive error.
   - 当前承受方式：`H-NEURO-4b` requires residual burden proxies such as metabolic cost, recovery half-life, stress load, or position-bound consequence beyond PE itself.
   - 若成立需撤回什么：撤回 SRT-specific neural burden language and keep the section as a predictive-processing translation note.

5. `d-value` collapses into salience, reward, precision, or motivational relevance.
   - 当前承受方式：`d-value` is defined as concern-weighted consequence for body, action, self-model, and future selectability, not as stimulus prominence or reward alone.
   - 若成立需撤回什么：撤回 d-value as an independent bridge variable and reclassify it as a terminological aggregation of existing constructs.

6. `L_2` hardening improves trained-path efficiency without increasing alternative-path friction.
   - 当前承受方式：the efficiency-flexibility tradeoff is an explicit empirical prediction, not a definitional truth.
   - 若成立需撤回什么：weaken the `L_2` basin-hardening model and treat hardening as ordinary learning unless alternative-path cost is demonstrated.



---

## FILE: `Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md`

| 字段 | 值 |
|---|---|
| path | `Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md` |
| id | SRT-NEURO-CONSC-MECH-COMPACT-CORE |
| claim_mode | bridge |
| status | active_v2 |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | false |
| last_commit | 2026-05-19 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：SRT-NEURO-MECH-001, SRT-NEURO-MECH-B, SRT-NEURO-MECH-COMPACT-CORE, Philosophy/SRT_Philosophy_Foundations_CompactCore.md, Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md, Philosophy/SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md

<!-- 以下为原文逐字保留 -->

# SRT Consciousness Mechanisms — Compact Core

> **Claim-status note（2026-05）**：This neuroscience file is bridge / lab / translation material. It applies SRT primitives but does not define `d-value`, `Ψ_f`, consciousness, pathology, diagnosis, treatment, NDE, or AI subjecthood. Read with `SRT_Neuroscience_Claim_Status.md` and, where relevant, `SRT_Neuro_Axioms_Claim_Status.md`.
> **定位**：本文件是 `SRT_Consciousness_Mechanisms.md` 的紧凑主干版。  
> **用途**：用于快速把握 SRT 如何把点燃、绑定、睡眠、带宽竞争、行进波与能动性统一到意识选择机制中。  
> **关系**：不替代原文；原文保留 GNWT/IIT 对照、睡眠维护、算子短路与实验预测的完整展开。  
> **2026-04 hardening note**：本版吸收 `SRT_Neuroscience_Hardening_N1_N9_v0_1.md` 的 N6 意识硬化主干，并与 N3/N5/N7 的 `\Psi_f`、`d-value`、病理桥接保持一致。新增内容为 bridge / lab hardening，不自动升格为 primitive axiom。
> **PH-SS subjecthood pointer**：本文必须与 `../Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md` 的 `Def-Phil-Subjecthood-Threshold`、`../Philosophy/SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md` 的 `O-Phil-18` 一起阅读。局部神经点燃、薄 `L_1`、高 `d-value`、再入稳定或报告通达都不是 subjecthood 的充分条件；**micro-selection / access / salience / high d-value do not automatically entail consciousness-as-subjecthood**。

## 1. 核心问题

这篇最核心的问题是：

> **意识不是“信息被广播”这么简单，那么神经系统究竟如何把候选内容确认成可报告、可维持的现实？**

SRT 的压缩回答是：
- 意识 = 选择被确认并稳定化
- 点燃 = `L_0 -> L_1` 的相变
- 绑定 = 同步进入同一显现对象
- 睡眠 = 维持未来选择能力的结构维护

### 1.1 2026 hardening: consciousness as stable concern-weighted L1 anchoring

本轮神经科学硬化将意识命题压成：

> **意识不是单纯的信息处理，而是关切加权的稳定 `L_1` 锚定。**

也就是说，意识内容不是任何局部处理、局部激活或刺激复杂度本身，而是某个候选状态在足够激活、增益调节、门控通过、递归稳定，并与报告、行动、自我模型或未来沉积链条发生耦合时形成的 `L_1`。

`d-value` 本身不产生意识，但会调节意识内容的厚度、优先级、持续性和沉积潜力。

> **PH-SS-10 guardrail**：`d-value`、局部锚定和 thick `L_1` 只能支持意识内容 / access / anchoring 的候选解释；subjecthood 还需要 integrated selection bandwidth、memory / `L_2` closure、boundary maintenance、counterfactual access、cross-time reidentification 等阈值条件。

---

## 2. 点燃：不是广播，而是候选门控

### 2.1 Ignition Candidate Gate
\[
\mathcal A(\sigma) \ge \tau_{ignite} \land \Phi_{proxy}\cdot d_{proxy} > C_{critical}
\]

> **Level**: hypothesis / operational proxy. The multiplicative gate is a structural preference, not an established neural theorem; additive and probabilistic gate models remain live alternatives.

最压缩句子：
> **点燃不是“更强激活”，而是一个候选内容在可测门控条件下被稳定选入现实。**

这一步是 SRT 对 GNWT 的候选重写核心；它需要独立测量窗口，不能仅凭报告率反推出本体相变。

| Gate reading | Current status | Boundary |
|--------------|----------------|----------|
| Multiplicative `Φ_proxy · d_proxy` | structural preference | favored only if low values in either factor block ignition and interaction terms improve prediction |
| Additive `w_ΦΦ_proxy + w_dd_proxy` | operational fallback | favored if one factor can compensate for the other |
| Probabilistic `P(ignite)` | lab-facing model | favored if access is graded, noisy, or report-confidence mediated |

### 2.2 Re-entrant Selection
\[
\mathcal R_{re}: L_1^{candidate} \to L_1^{stabilized}
\]

含义：
- 再入回路不是重复播放
- 而是把候选显现稳定为可报告现实

### 2.3 Thin L1 and thick L1

为避免“有意识/无意识”的粗二分，本版引入 `thin L_1` / `thick L_1` 区分：

| State | SRT description | Examples |
|---|---|---|
| Thin `L_1` | 弱锚定、不稳定、难报告、行动/自我耦合弱 | 模糊预感、舌尖现象、余光一闪、梦醒残留 |
| Thick `L_1` | 稳定、可报告或可行动、与身体/自我/价值耦合强、更可能沉积为 `L_2` | 疼痛、明确危险、重大决定、羞耻、创伤或顿悟 |

结构性表达：
\[
\text{Conscious thickness}(x) \sim S(x)\cdot G(x)\cdot A(x)\cdot M(x)\cdot d(x)
\]

其中 `S` 为稳定化，`G` 为全局可访问性，`A` 为行动耦合，`M` 为自我模型耦合，`d` 为关切权重。

这不是物理定律，而是意识厚度的 bridge/lab 指标结构。

---

## 3. 绑定：不是拼接，而是拓扑同步

### 3.1 Binding as Synchrony
\[
\mathcal B: \{\sigma_i\} \to \sigma_{bound},\qquad \Delta\phi_i \to 0
\]

最短说法：
> **绑定不是把现成特征拼在一起，而是让分散特征在同一时间-相位框架中被共同选入。**

### 3.2 Binding Failure
若相位无法收敛，则：
\[
\sigma_{bound} \not\exists
\]

这意味着：
- 碎裂体验
- 解离
- 统一对象感失稳

---

## 4. 意识不是无限带宽

### 4.1 Bandwidth Competition
\[
B_{consc} < B_{max}, \qquad \sum_k \mathcal A_k \le B_{consc}
\]

SRT 在这里给出很硬的一句：
> **意识是带宽竞争系统，不是无限容器。**

### 4.2 Pain Priority
高风险梯度内容会优先抢占带宽。

压缩解释：
- 疼痛优先不是因为它“更响”
- 而是因为它携带更高生存风险梯度

2026 hardening 将其重写为 `d-value` 语言：疼痛之所以具有强意识性，不只是因为信号强，而是因为它对身体维持、行动中断、自我牵连和未来行为具有高后果权重。

---

## 5. 时间：连续感来自离散选择的耦合

### 5.1 Selection Latency
\[
\tau_{select}=\tau_{sensory}+\tau_{integrative}+\tau_{gate}
\]

SRT 在这里强调：
- 意识有时滞
- 不是实时呈现
- 而是整合与门控完成后的延迟结果

### 5.2 Fast–Slow Coupling
原文更深的方向是：
> **连续时间体验并不是直接给定，而是快波内容与慢波框架耦合后的主观产物。**

---

## 6. 睡眠：不是关机，而是结构维护

### 6.1 Defensive Activation
\[
\mathcal S_{sleep}: \hat G_\theta \to \hat G_\theta^{repair}
\]

最压缩解释：
> **睡眠不是暂停意识，而是为未来意识保持结构可用性。**

### 6.2 L2 Consolidation
\[
\Delta L_2 \propto \int_{sleep} \nabla_\theta F\,dt
\]

这一步说明：
- 梦与回放不是纯噪声
- 而是对未来选择规则的重加权和固化

梦境可被重读为：内部候选在弱外部约束下形成的临时 `L_1`，其情绪 `d-value` 可很高，但与现实行动链和稳定 `L_2` 检验的耦合较弱，因此醒后容易崩解。

---

## 7. 行进波：谁先进入现实，不只是看强度

### 7.1 Traveling Wave Routing
\[
\mathcal W(x,t)=A(x,t)e^{i\phi(x,t)}
\]

SRT 的关键重写是：
> **行进波不是背景节律，而是意识路由场。**

### 7.2 Wave–Ignition Coupling
\[
P_{ignite}=\sigma(\alpha C_{wave}+\beta(\Phi\cdot d)+\gamma D_{align}-\delta)
\]

> **Level**: probabilistic gate variant. This formula is a candidate lab model for wave-routing effects, not a proof that `Φ·d` is the unique ignition criterion.

压缩结论：
- 点燃不只取决于总激活强度
- 还取决于相干度与方向是否匹配任务

### 7.3 Directional Access
若方向失配，则：
- 可报告性下降
- 不是因为“没激活”
- 而是因为“路由错了”

---

## 8. 主观能动性与算子短路

### 8.1 Agency Scalar
\[
A_{sub}(t)=\frac{1}{1+\lambda\,|\sigma_{L_1}(t)-\hat G_\theta^{predict}(L_2)|}
\]

最压缩解释：
> **“我是作者”的感觉，来自当前显现与内在预测结构之间的匹配度。**

### 8.2 Operator Short-Circuit
SRT 很有力的一点是：
- 习惯与成瘾可被重写为 `L_2` 直接劫持行为路径
- 绕开原本需要的显式选择过程

**Closure-pathology bridge note (2026-04-21)**：神经科学语境只把这一路径桥接到 habituation、gating rigidity 与 re-entry loss：旧通路越能自动放行，显式再选择越少进入回路。这里不把 legitimacy、appeal standing 或制度性 pseudo-openness 强行写成神经层事实。

这解释了为什么：
- 人会“知道不对”却仍执行
- 行为先发生，意识后补叙述

---

## 9. Boundary cases and psychopathology pressure tests

### 9.1 Boundary cases

| Case | SRT reading |
|---|---|
| Blindsight | 信息可以进入局部处理与行动通道，但缺少 thick `L_1` 锚定 |
| Bistable perception | 多个候选在 `L_0^{accessible}` 中竞争，交替获得 `L_1` 稳定化 |
| Pain | 高 `d-value` 候选强制重构当前 `L_1` |
| Dreaming | 内部候选在弱外部约束下形成临时 `L_1` |
| Meditation | 训练可能降低候选自动硬化，改变 `d-value` 与 `\Psi_f` 分配 |
| Anesthesia | 候选激活、递归稳定或全局门控链条被破坏，信息无法形成 thick `L_1` |

### 9.2 Psychopathology bridge

意识机制中的病理不是简单“意识太多/太少”，而是候选状态的锚定厚度、关切权重、关闭摩擦与 `L_2` 沉积发生扭曲：

- **社交焦虑**：他人评价候选获得过高 `d-value`，公开行动的 `\Psi_f` 上升。
- **羞耻创伤**：社会性高 `d-value` `L_1` 过度沉积为自我相关 `L_2`。
- **强迫**：风险候选进入 `L_1` 后无法低成本关闭。
- **成瘾/习惯短路**：低摩擦 `L_2` 通道绕开显式再选择。
- **妄想样显著性异常**：低证据候选被过度赋予现实锚定权。

---

## 10. Relation to GNWT, IIT, and SRT-specific addition

| Framework | What it explains | SRT-specific addition |
|---|---|---|
| GNWT / Global workspace | 信息如何全局通达、可报告、可被多个系统使用 | SRT 追问通达之前的候选竞争、通达时的 `\Psi_f`、通达后的 `L_2` 硬化 |
| IIT | 信息整合 / 内在因果结构与经验的关系 | SRT 追问什么对系统有后果，以及这种后果如何成为稳定 `L_1` |
| Predictive processing / FEP | 模型如何解释输入、系统如何自维持 | SRT 追问候选如何获得现实地位、何以具有 `d-value`、何以沉积为未来地形 |

压缩区分：

> Global workspace explains access; SRT explains anchoring.  
> IIT emphasizes integration; SRT emphasizes concern-weighted stabilization.  
> Predictive processing explains model updating; SRT explains lived reality anchoring.

---

## 11. 最压缩结论

`SRT Consciousness Mechanisms` 可以压缩成七句话：

1. **意识不是广播本身，而是候选内容被确认并稳定为现实的选择相变。**
2. **意识不是信息亮起来，而是候选可能性被身体、行动、自我和关切牵连锚定成 `L_1`。**
3. **绑定不是特征拼接，而是分散轨迹被同步选入同一显现对象。**
4. **意识带宽是有限的，`d-value` 高的内容会优先占用显现资源。**
5. **睡眠不是关机，而是对 `L_2` 与未来选择能力的必要维护。**
6. **可报告性与能动性感不只看激活强度，还取决于路由方向、预测匹配与是否发生算子短路。**
7. **病理意识状态是现实锚定厚度、关闭摩擦与历史硬化的失衡。**

Addendum:

> These seven claims concern consciousness mechanisms and conscious-content anchoring. They do not by themselves prove full subjecthood. Use the PH-SS subjecthood guardrail to avoid over-attributing subjecthood to access, salience, high `d-value`, local anchoring, or reportability alone.

---

## 12. 阅读路径

- PH-SS subjecthood guardrail：`../Philosophy/_SRT_Phil_Axioms_PH_SS_Guardrails.md`
- PH-SS objection extension：`../Philosophy/SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md` (`O-Phil-18`)
- 全量原文：`SRT_Consciousness_Mechanisms.md`
- Neural Mechanisms compact core：`SRT_Neural_Mechanisms_CompactCore.md`
- Neuro bridge：`_SRT_Neuro_Axioms.md`
- N1-N9 hardening draft：`SRT_Neuroscience_Hardening_N1_N9_v0_1.md`
- canonical 总注册表：`../CANONICAL_REGISTRY.md`

---

## Hardest Objections

1. Conscious access may be fully explained by global workspace access.
   - 当前承受方式：SRT does not deny access; it adds pre-access selection, `d-value`, `\Psi_f`, and post-access hardening as incremental variables.
   - 若成立需撤回什么：撤回 “anchoring beyond access” 的增量主张，把本文件退回 GNWT translation layer。

2. `d-value` may collapse into arousal, salience, or report confidence.
   - 当前承受方式：`d-value` must predict memory, bodily reaction, action change, and L2 sedimentation beyond salience/confidence.
   - 若成立需撤回什么：撤回 concern-weighted consciousness thickness as independent bridge claim.

3. Thin/thick L1 may be a report-scale artifact.
   - 当前承受方式：thin/thick distinction must be tested through non-report markers: action coupling, memory persistence, bodily reaction, and future-selection change.
   - 若成立需撤回什么：保留 graded access language but remove L1-thickness ontological interpretation.

4. High d-value unconscious processes challenge d-value-consciousness coupling.
   - 当前承受方式：d-value is not sufficient for consciousness; it modulates priority and thickness only after gating and stabilization.
   - 若成立需撤回什么：若 d-value has no measurable effect on stabilization or sedimentation, weaken it to a peripheral motivational variable.

5. Subjecthood may require more than conscious-content anchoring.
   - 当前承受方式：this file treats consciousness mechanisms and conscious-content anchoring; subjecthood is routed through PH-SS-10 threshold conditions.
   - 若成立需撤回什么：撤回 any claim that local access, salience, high `d-value`, or reportability is sufficient for subjecthood.
