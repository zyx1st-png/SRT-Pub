---
id: SRT-CONTEXT-BUNDLE-SPINE-2026-08-11
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

# SRT Canonical 骨架上下文包

> **这是什么**：由 `scripts/build_srt_context_bundles.py` 从 SRT 仓库自动拼装的上下文包。
> 收录承载定义权的 canonical 主干，供大模型确定 SRT 术语、公理、方程与符号的含义。
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
| 包含文件数 | 16 |

> **provenance 契约**：真实性判据是 `inputs_digest`——生成脚本、护栏来源
> （`STATUS.md`、两份审计）与全部正文文件的联合内容摘要。`--check` 重算并比对该摘要，
> 因此改动其中任何一项都会被发现。
>
> `source_commit` 仅供参考，**不作为校验条件**：squash / rebase 合并会重写或丢弃该
> commit，若拿它做祖先校验，合并进 main 之后检查必然失败。内容摘要与合并策略无关。

### 0.1 文件清单与各自最后改动日期

| # | 文件 | 最后 commit |
|---|---|---|
| 1 | `SRT_AI_START.md` | 2026-08-08 |
| 2 | `CANONICAL_REGISTRY.md` | 2026-08-11 |
| 3 | `Governance/SRT_CLAIM_LADDER.md` | 2026-05-01 |
| 4 | `Governance/SRT_CLAIM_MODE_AUDIT.md` | 2026-08-11 |
| 5 | `Core_Law/SRT_L0_Metaphysics.md` | 2026-08-11 |
| 6 | `Core/SRT_Core_21_Formal_Axioms.md` | 2026-04-22 |
| 7 | `Core/SRT_Core_21_Minimal_Axioms.md` | 2026-04-27 |
| 8 | `Core/SRT_Core_21b_Constitutive_Theorems.md` | 2026-04-26 |
| 9 | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | 2026-07-07 |
| 10 | `_SRT_D_VALUE_CANONICAL.md` | 2026-07-07 |
| 11 | `_SRT_PSI_F_CANONICAL.md` | 2026-07-07 |
| 12 | `_SRT_T_DIR_CANONICAL.md` | 2026-04-26 |
| 13 | `_SRT_CROSS_DOMAIN_MATRIX.md` | 2026-07-21 |
| 14 | `Core/SRT_Core_22_Equations.md` | 2026-07-07 |
| 15 | `_SRT_SYMBOL_TABLE.md` | 2026-07-20 |
| 16 | `Core/SRT_OPEN_TENSIONS.md` | 2026-08-11 |

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
> 本包是 **人工选择的高优先级 canonical 骨架**，不是定义权的完备闭包。
> 下面的分类是**生成器的判断**，不是 registry 的原话；每行都附依据供复核。
> 「registry 提及」「AI_START §2」两列是机械判定的事实。

### 已收录

**定义源**（10 个）

| 文件 | 分类依据 | registry 提及 | AI_START §2 |
|---|---|:---:|:---:|
| `Core/SRT_Core_21_Formal_Axioms.md` | registry §A.4 主锚点（公理路由索引） | ✓ | ✓ |
| `Core/SRT_Core_21_Minimal_Axioms.md` | registry §A.4 分层正文 P0 | ✓ | ✓ |
| `Core/SRT_Core_21b_Constitutive_Theorems.md` | registry §A.4 分层正文 P1 | ✓ | ✓ |
| `Core/SRT_Core_21c_Bridge_Hypotheses.md` | registry §A.4 分层正文 P2/P3/P4 | ✓ | ✓ |
| `Core/SRT_Core_22_Equations.md` | registry §A.4b 主锚点 | ✓ | ✓ |
| `Core_Law/SRT_L0_Metaphysics.md` | AI_START §2 First Sources 第 4 位 | ✓ | ✓ |
| `_SRT_D_VALUE_CANONICAL.md` | registry §A.1 主锚点 | ✓ | ✓ |
| `_SRT_PSI_F_CANONICAL.md` | registry §A.2 主锚点 | ✓ | ✓ |
| `_SRT_SYMBOL_TABLE.md` | AI_START §2 First Sources；符号与记号的定义权 | ✓ | ✓ |
| `_SRT_T_DIR_CANONICAL.md` | registry §A.3 主锚点 | ✓ | ✓ |

**治理护栏**（4 个）

| 文件 | 分类依据 | registry 提及 | AI_START §2 |
|---|---|:---:|:---:|
| `Core/SRT_OPEN_TENSIONS.md` | registry §A.4c；未闭合登记，claim_mode: open | ✓ | ✓ |
| `Governance/SRT_CLAIM_LADDER.md` | registry §B.5b；P0–P5 硬度阶梯 | ✓ | ✓ |
| `Governance/SRT_CLAIM_MODE_AUDIT.md` | registry §B.5c；降级台账 | ✓ | ✓ |
| `_SRT_CROSS_DOMAIN_MATRIX.md` | registry §A.4d 自称 governance-canonical usage layer | ✓ | ✓ |

**导航**（2 个）

| 文件 | 分类依据 | registry 提及 | AI_START §2 |
|---|---|:---:|:---:|
| `CANONICAL_REGISTRY.md` | 权威层级注册表本身 | ✓ | ✓ |
| `SRT_AI_START.md` | AI 最小首读入口，frontmatter 自标 ai_do_not_use_for_definition | — | — |

### 未收录支持文件

`SRT_AI_START.md` §2 First Sources **已全部收录**（15 条，且全部指向存在的文件）。

**⚠ 高严重度：registry 提及但文件不存在（1 个）**——指向已删除、拼错或尚未创建的路径。**这类条目不会被静默过滤掉**，因为它本身就是一种 manifest 差异：

| 失效路径 | 说明 |
|---|---|
| `Core_21_Formal_Axioms.md` | 见 §0.2 G4：这是 `Core/SRT_Core_21_Formal_Axioms.md` 的行文简写，非真实路径 |

**registry 提及、文件存在、但本包未收（79 个）**——多为领域主轴、
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
- `Core/SRT_Core_14_Dynamics_Scaling.md`
- `Core/SRT_Core_14_Dynamics_Scaling_CompactCore.md`
- `Core_Law/SRT_Collective_Selection.md`
- `Core_Law/SRT_Collective_Tower_Hardening_Notes.md`
- `Core_Law/SRT_Constitution_Seven_Theses.md`
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
- `_SRT_VERTICAL_INTEGRATION.md`

</details>


---



---

## FILE: `SRT_AI_START.md`

| 字段 | 值 |
|---|---|
| path | `SRT_AI_START.md` |
| id | SRT-AI-START |
| claim_mode | index |
| status | active_v3 |
| epistemic_layer | os |
| layer | meta |
| canonical(字段) | - |
| last_commit | 2026-08-08 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：[SRT-CANONICAL-REGISTRY, SRT-CLAIM-LADDER, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-T-DIR-CANONICAL, SRT-CORE-21, SRT-CORE-22, SRT-AGENT-RETRIEVAL-PROFILE]

<!-- 以下为原文逐字保留 -->

# SRT AI Start

> **Runtime / bootstrap entry only.**
> This file is not the first source of SRT definitions and must not replace canonical files.
> Its job is to give AI / agent systems the shortest safe reading path and prevent common misreadings.

---

## Current bootstrap pointer

`AGENTS.md §Session Start` is the single authority for fresh-session read order. This file is the minimal theory/runtime guard inside that sequence; it is not the file that owns the sequence itself.

---

## 1. One-Sentence Orientation

SRT's minimal orientation is: **choice precedes stable existence; reality is the manifestation and convergence of parameterized selection under constraint, friction, and history.**

For formal definitions, do not rely on this sentence. Follow the canonical sources below.

---

## 2. First Sources

When the same concept appears in multiple files, use this order:

1. `CANONICAL_REGISTRY.md`
2. `Governance/SRT_CLAIM_LADDER.md`
3. `Governance/SRT_CLAIM_MODE_AUDIT.md`
4. `Core_Law/SRT_L0_Metaphysics.md`
5. `Core/SRT_Core_21_Minimal_Axioms.md`
6. `Core/SRT_Core_21b_Constitutive_Theorems.md`
7. `_SRT_D_VALUE_CANONICAL.md`
8. `_SRT_PSI_F_CANONICAL.md`
9. `_SRT_T_DIR_CANONICAL.md`
10. `_SRT_CROSS_DOMAIN_MATRIX.md`
11. `Core/SRT_Core_22_Equations.md`
12. `_SRT_SYMBOL_TABLE.md`
13. `Core/SRT_Core_21_Formal_Axioms.md`
14. `Core/SRT_Core_21c_Bridge_Hypotheses.md`

Use `Core/SRT_Core_21_Formal_Axioms.md` as a Core_21 routing index and legacy-numbering map, not as the first definition source.

Use `Core/SRT_OPEN_TENSIONS.md` when a concept is known to be not fully sealed.

Use `_SRT_CROSS_DOMAIN_MATRIX.md` when a core term moves across Physics, Neuroscience, Philosophy, Spirituality, AI, or governance contexts.

---

## 2A. Retrieval Expansion Guard

Use `_SRT_AGENT_RETRIEVAL_PROFILE.md` before substantial theory advancement, book writing, domain deep-dives, public-facing drafting, material fusion, or repository governance work.

Do not confuse authority with retrieval:

- `canonical: false` means a file must not define or override SRT terms.
- It does not mean the file has low context value.
- Bridge, split, annex, Operations, External Convergence, Source Intuition, and Backstage book files may be high-value retrieval context for the right task.

For any non-simple SRT question, route through `_SRT_CONTEXT_ROUTER.md` and, when cross-domain, `_SRT_DEEP_THEORY_MAP.md`.

---

## 3. Symbol Quick Guard

> Merged from the former `_SRT_SYMBOL_QUICK_GUARD.md` (2026-07-20). These are fast boundaries and pointers, not definitions; use `_SRT_SYMBOL_TABLE.md` and the canonical anchors when exact definitions, equations, or notation conflicts matter.

| Symbol / term | Fast guard | Definition authority |
|---|---|---|
| `L_0` | Structured latent possibility, not nothingness and not physical vacuum by default. | `Core_Law/SRT_L0_Metaphysics.md`, `_SRT_SYMBOL_TABLE.md` |
| `L_1` | Manifest selected slice / event / state, not merely material objects. | `_SRT_SYMBOL_TABLE.md`, Core ontology files |
| `L_2` | Convergence-history / stable constraint domain; not identical to any one landscape, institution, memory, or scaffold. | `_SRT_SYMBOL_TABLE.md`, `Core/SRT_OPEN_TENSIONS.md` |
| `Ĝ_θ` | Embodied/parameterized selection or anchoring operator; implementation analogues do not define it. | `Core/SRT_Core_21_Minimal_Axioms.md`, `_SRT_SYMBOL_TABLE.md` |
| `d` | Scalar summary of stake-coupled concern / irreversible-risk sensitivity by default. Competence, capacity, preference, or distinguishability is not enough. | `_SRT_D_VALUE_CANONICAL.md`, `_SRT_SYMBOL_TABLE.md` |
| `D_eff` | Geometric capacity proxy / upper-bound candidate, not canonical `d`. | `_SRT_D_VALUE_CANONICAL.md`, `Core/SRT_Core_21c_Bridge_Hypotheses.md` |
| `Ψ_f` | Payability burden / ontological friction. Fisher geometry, metabolic cost, stress, or pain are conditional projections only. | `_SRT_PSI_F_CANONICAL.md`, `_SRT_SYMBOL_TABLE.md` |
| `T_dir` | v0 operational proxy for readability / reorientation of the system's own selection direction; not reward, confidence, semantic valence, or coherence. | `_SRT_T_DIR_CANONICAL.md`, `_SRT_SYMBOL_TABLE.md` |
| `ε_pg` | L0 minimum non-neutrality postulate; do not identify with consciousness. | `_SRT_SYMBOL_TABLE.md`, Core P0/P1 sources |
| `ε_reg` | Implementation regularizer; only an analogy/echo of `ε_pg` unless separately argued. | `_SRT_SYMBOL_TABLE.md` |
| `ε_s` | Stake-threshold bridge for direction-level admission; not stake itself. | `_SRT_SYMBOL_TABLE.md`, `_SRT_D_VALUE_CANONICAL.md` |
| bare `σ` | Defaults to main-equation state field. Use `σ_sr` for self-reference ratio and `σ_j` for anchoring sub-targets. | `_SRT_SYMBOL_TABLE.md` |

### Proxy rule

If a statement says `proxy X = SRT variable Y`, rewrite it unless the canonical file explicitly licenses that identity. Safer forms:

- `X is a candidate proxy for Y under stated conditions.`
- `X maps to one projection of Y, not to Y itself.`
- `X supports a bridge/lab hypothesis about Y, not a canonical definition.`

---

## 4. Core Boundary Reminders

### Pre-objectification guard

Do not demand that SRT begin by defining `L_0`, selection, experience, or reality as mathematical objects. Object specification is already an `L_1/L_2` operation: it selects boundaries, variables, relations, and admissible transformations after some manifestation has occurred. Formal models may describe selected structures and test bridge consequences, but they do not replace the pre-objectifying question SRT is designed to ask.

Preferred reading:

```text
pre-object field / selection condition
-> manifestation and objectification
-> mathematical or scientific description
```

Forbidden reversal:

```text
first define a complete object space
-> then claim to have explained how objects become possible
```

Route: `01_Source_Intuition/BOOK/Drafts_26Q/Q02_对象化.md`, `Philosophy/SRT_L0_Ontological_Status.md`, `Core_Law/SRT_Selection_Argument.md`.

### `L_2`

For the support/replacement boundary of `L_2`, use `_SRT_T_DIR_CANONICAL.md` and `Core/SRT_OPEN_TENSIONS.md`.

### Real Choice Moment

For the canonical statement of real choice moment vs script execution, use `Core/SRT_Core_21b_Constitutive_Theorems.md` (P1-T05). That statement carries a **negative list only** (script execution, habit replay, gradient following, `L_2` label optimization do not qualify); it does not supply a positive discrimination procedure, so it under-determines concrete cases.

For concrete "is this a real choice?" judgments, also load `03_Bridges/SRT_Selection_Event_CompactCore.md` — five gates (`CG-0..CG-4`) with graded ladders (`DMF`/`NER`/`PEF`/`CBP`/`HEF`), audit-default minima, a non-compensation rule, and the no-choice / pseudo-choice / punitive-choice / respected-choice reading. It is **P2-P3 audit apparatus, not a definition source**: passing all five gates licenses only "bounded selection-event candidate", never subjecthood, consciousness, freedom, `L_2`, or generative health. Open exposures are registered at `Core/SRT_OPEN_TENSIONS.md §14`. Route: `_SRT_CONTEXT_ROUTER.md §23a`.

Three fast negatives worth carrying without loading anything: a different output is not path efficacy; energy spent is not consequence bearing; having memory is not historical efficacy.

### Freedom

In SRT usage, freedom concerns preservation of real choice moments, not mere option count. Treat this as a pointer to the P1/P2 sources, not as a standalone definition here.

### Origin of Selectability

`Core/SRT_OPEN_TENSIONS.md §7 P0-04` remains unresolved. When a file speaks of a selector, chooser, subject, agency, or system-position, do not treat that language as an answer to where selectability comes from; mark whether it is a derived process, stable pattern, or assumed domain interface.

### d-value explanatory-coordinate guard

Do not require canonical `d` to be empirically disjoint from salience, reward, homeostatic error, pain, arousal, or memory strength. These may be local realizations or proxies. Overlap is not reduction. A proxy may be identified with canonical `d` only if it also tracks irreversible stake, consequence return, non-substitutability, and changes in future selection capacity. Route: `_SRT_CROSS_DOMAIN_MATRIX.md §1.1`, `_SRT_D_VALUE_CANONICAL.md`.

### Hard-problem / internal-external guard

Do not treat first-person experience as a hidden object that must be derived from a complete view-from-nowhere description. External description is itself a second situated selection and objectification of an internally borne event. The gap therefore involves selection-position difference and re-objectification, not only bandwidth compression. SRT provides orientation and anchoring for this relation; it does not claim that external language can exhaust or numerically reproduce qualia. Route: `Philosophy/SRT_HardProblem_Epistemology.md §3.1a-§3.4`.

### Value Hiddenness

For value hiddenness and its limits, use `_SRT_T_DIR_CANONICAL.md`.

### `T_dir`

For the distinction between `T_dir` and `d-value`, use `_SRT_T_DIR_CANONICAL.md`.

### `\Psi_f`

For payability and `\Psi_f` usage, use `_SRT_PSI_F_CANONICAL.md`.

### `ε`

Do not identify `ε_pg` with consciousness. Stable ISP anti-closure asymmetry is a scoped P1 theorem; see `Core/SRT_Core_21b_Constitutive_Theorems.md`.

### Open-Tension Guard

Before presenting any of the following as closed, check `Core/SRT_OPEN_TENSIONS.md`:

- origin of selectability / P0-04;
- `D_eff -> d_stakes` gate;
- exact projection status of `Ψ_f`;
- minimal formalization of `T_dir`;
- healthy `L_2` support vs lethal `L_2` replacement;
- stable ISP entry and maintenance.

---

## 5. Claim-Level Guard

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

## 6. File-Type Guard

- `canonical`: definitions and stable anchors.
- `compact core`: short local reading path, not always final definition.
- `bridge`: cross-domain mapping, not proof.
- `lab`: hypothesis, proxy, or test interface.
- `navigation / registry / index`: route-finding, not theory replacement.
- `historical / archive`: provenance, not current authority.

If a file is `split`, `annex`, `bridge`, `operations`, or `memory`, do not use it as a first definition source unless a canonical file explicitly points there for that purpose.

That restriction is about definition authority, not retrieval. Use `_SRT_AGENT_RETRIEVAL_PROFILE.md` to decide when these files should still be read as support, provenance, connector-safe copies, or writing context.

---

## 7. AI-Specific Guard

AI is a pressure-test and boundary-test domain for SRT. It is not the theory's definition engine.

Current AI claims should preserve both sides:

- negative boundary: performance, language, or optimization does not by itself imply real subjectivity, stake, anchoring, or consciousness;
- positive test window: SRT may still ask what minimal conditions would suffice for surrogate stake or agentic closure.
- architecture-state rule: statements about AI `d-value`, burden, subjectivity, or friction must distinguish training-time, inference-time, and persistent-memory / history-bearing deployment. Inference-only conclusions must not be silently generalized.
- stake-bearing spectrum: use `AI/AI_POSITIONING_NOTE.md` S0-S4 before saying "LLM has `d \approx 0`" or "AI has stake".

Use AI files as domain tests and bridges back to canonical sources, not as primitive theory sources.

---

## 8. Minimal Answer Protocol

When answering about SRT:

1. Name the canonical source you rely on.
2. State the claim level if hardness matters.
3. Mark bridge, lab, or companion material explicitly.
4. If a point is listed in `Core/SRT_OPEN_TENSIONS.md`, do not present it as closed.
5. For non-trivial questions, name the retrieval route or task profile used.
6. Prefer short, hard claims over broad unification language unless the question explicitly asks for bridge speculation.



---

## FILE: `CANONICAL_REGISTRY.md`

| 字段 | 值 |
|---|---|
| path | `CANONICAL_REGISTRY.md` |
| id | SRT-CANONICAL-REGISTRY |
| claim_mode | canonical |
| status | active_v1 |
| epistemic_layer | os |
| layer | meta |
| canonical(字段) | - |
| last_commit | 2026-08-11 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：[SRT-INDEX, SRT-CLAIM-LADDER, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-T-DIR-CANONICAL, SRT-CROSS-DOMAIN-MATRIX, SRT-CORE-22]

<!-- 以下为原文逐字保留 -->

# SRT Canonical Registry

本页用于固定 SRT 当前应优先引用的 **canonical 主干层**。
原则：
- canonical 文件优先短、稳、少歧义
- 长文负责展开、推导、接口批次与历史沉积
- split 文件负责导航，不替代 canonical 定义

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
- 说明（Part I §1-§10）：T_dir 是系统对自身选择秩序方向可读性的 v0 operational proxy / working canonical proxy；统一价值遮蔽命题、Ψ_f_actual/Ψ_f_felt 分裂、致命 L₂ 机制的治理性表述；它尚不是 theory-canonical 形式基础
- 说明（Part II §11-§16）：扩展至价值动力学底层机制——L₂ 磁带/DNA 类比（§11）、三层价值结构（§12）、价值归纳 vs 理性归纳（§13）、时空对称性感知机制（§14）、价值作为暂时吸引子而非守恒结构（§15）、吸引子上升/退化动力学（§16）；这些段落按 bridge / theory-clarifying 读，不因文件名而升级为 core theorem
- 引用规则：涉及方向透明度、意义感/虚无感的 SRT 机制解释、致命 L₂、价值遮蔽、三层价值结构、价值归纳、吸引子动力学时优先回链本文件
- 与 d-value 的关系：d 是 T_dir 的必要条件；两者独立，不互相替代

### 4. Core Axioms
- 主锚点：`Core/SRT_Core_21_Formal_Axioms.md`
- 分层正文：
  - P0 minimal axioms → `Core/SRT_Core_21_Minimal_Axioms.md`
  - P1 constitutive theorems → `Core/SRT_Core_21b_Constitutive_Theorems.md`
  - P2/P3/P4 bridge hypotheses → `Core/SRT_Core_21c_Bridge_Hypotheses.md`
- 说明：`Core_21_Formal_Axioms.md` 现在是形式公理索引，不再承载混层正文
- Bridge 用法提醒：`Core_21c` 中的 "emergence" 只能作为机制占位词使用，不能作为解释原语；`L_2` downward constraint 仍回链 P1，但 domain-specific downward causation 必须说明具体实现通道
- 引用规则：涉及核心公理编号时，先回链索引，再按命题硬度引用对应分层文件

### 4b. Core Equations
- 主锚点：`Core/SRT_Core_22_Equations.md`
- 说明：主动力学方程、热力学与稳定性方程主入口
- 引用规则：涉及主方程、选择热力学、稳定性条件时优先回链本文件

### 4c. Core Open Tensions
- 主文件：`Core/SRT_OPEN_TENSIONS.md`
- 说明：记录当前未完全封口的 core pressure points
- 引用规则：凡涉及其中 tension，不得包装成已完成 P0/P1

### 4d. Cross-Domain Usage Matrix
- 主文件：`_SRT_CROSS_DOMAIN_MATRIX.md`
- 说明：提供 `d`、`Ψ_f`、`T_dir`、`ε` 的 v0 跨域用法矩阵；该矩阵是 governance-canonical usage layer，不新增 theory-canonical 定义
- 引用规则：跨域使用上述概念时，先检查 canonical 用法、allowed projection 与 forbidden shortcut

## B. 规范辅助层（Canonical Support）

### 5. 七命题宪法摘要层
- 文件：`Core_Law/SRT_Constitution_Seven_Theses.md`
- 角色：为 SRT 提供最短的元理论宪法摘要，用于对外解释、框架比较与自我收口
- 注意：它是顶层摘要，不替代 `Core_Law/SRT_Reference_Axioms.md`、`Core_Law/SRT_Reference_Ontology.md`、canonical 定义文件或主方程文件

### 5b. Claim Ladder
- 文件：`Governance/SRT_CLAIM_LADDER.md`
- 角色：定义 P0-P5 命题级硬度，防止 bridge / lab / companion 命题伪装成 primitive axiom 或 constitutive theorem
- 注意：它是治理机制，不新增理论命题

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
- 角色：compact core 固定跨尺度同构、d-bandwidth、主动力学、边界成本函数与反泛心论边界
- 注意：原文继续保留长篇机制解释、接口批次与 annex 沉积

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
- 说明：把国家、权利、合法性、民主、结构性不公、危机决断与政治病理统一重写为多主体共同现实选择的生成—沉积—封闭—再打开过程；以 P2/P3 为主，并将制度判准与紧急状态边界显式标记为 P4
- 与 `SRT-SOC-ECONOMICS` / `SRT-POLITICAL-RIGHTS` 的关系：前者提供社会现实、制度与结构性不公接口；后者提供权利、授权与投票后验验证的子接口；本文件负责收口为完整政治哲学主文
- 重要追加：政治合法性被重写为可持续共同选择；反支配被重写为反现实定义权垄断；危机政治以 `minimum necessary interruption` 为护栏

### 9b. SRT 政治权利理论
- 主文件：`Philosophy/SRT_Political_Rights.md`
- id：`SRT-POLITICAL-RIGHTS`
- layer：L1 / epistemic：bridge / status：draft_v1
- 说明：从SRT第一性原理推导权利的本体论定义；建立以决策d值为核心的授权合法性框架；分析投票作为d倾向后验验证的机制；提出三层制度结构（公检法/监督机构/授权主体）
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
- Consciousness Framework：`AI/SRT_AI_03_Consciousness_Framework_CompactCore.md` / `AI/SRT_AI_03_Consciousness_Framework.md`
- 角色：形成 AI 板块从本体门槛、结构限制到正向意识路径的 compact core 主线
- 注意：AI 是压力测试场 / 边界测试场，不是 core 定义发动机；AI 语境中的所有 d-value 与意识判据仍服从 `_SRT_D_VALUE_CANONICAL.md`，所有 `Ψ_f` stake / non-binding / payability 语句仍服从 `_SRT_PSI_F_CANONICAL.md`
- 第二轮护栏：AI 判断必须区分 training-time、inference-time、persistent-memory / history-bearing deployment，并使用 `AI/AI_POSITIONING_NOTE.md` 的 S0-S4 stake-bearing 光谱；不得把 inference-only 的 `d_{AI}\approx0` 静默推广为全部 AI 类型的终局判决

### 11. Neuroscience 主轴
- Claim-status：`Neuroscience/SRT_Neuroscience_Claim_Status.md`（clinical / FEP / NDE / AI-comparison proxy guardrail; not a primitive source）
- Neuro registry：`Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md`
- Hardening / material patch index：`Neuroscience/_SRT_Neuroscience_Hardening_Index.md`
- Neuro Axioms / Bridge：`Neuroscience/_SRT_Neuro_Axioms.md`
- Neural Mechanisms：`Neuroscience/SRT_Neural_Mechanisms_CompactCore.md` / `Neuroscience/SRT_Neural_Mechanisms.md`
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

### 13a. SRT 个体化理论（主体涌现 + 自我意识凝结）
- 主文件：`Core_Law/SRT_Individuation.md`
- id：`SRT-INDIVIDUATION`
- layer：L1 / epistemic：os / status：draft_v0
- 说明：L1 相变理论，填补 L0（选择无主语）与 P1-T06 Stable ISP 之间的过渡空洞；以自指率 `σ_{sr}`（governance-canonical 命名，2026-04-25 起；与主方程状态场 σ 不同对象，详见 `_SRT_SYMBOL_TABLE.md` Usage Rule 12）作为阶参，给出两次相变——主体位进入（`σ_{sr}^{sub}`）与自我意识凝结（`σ_{sr}^{self}`）——的结构判据；自我意识被规范读为主体位稳态之后的二阶 writeback 凝结物，严格遵守 L0 §五意识禁令
- 与 P1-T06 的关系：本文件是 ISP 的**进入动力学判据**；P1-T06 是 ISP 的**结果状态判据**；二者互补，不重复也不冲突
- 与 T-L2-Scaffold 的关系：T-L2-Scaffold 追踪路径层痕迹（ρ），本文件追踪算子层自指（σ）；两者都是 writeback 累积的不同投影，不互相还原
- claim-mode 分布：三相结构与第一相变为 P1-candidate；`σ_{sr}` 阶参与自我意识二阶凝结读法为 P2；`σ_{sr}^{sub}`、`σ_{sr}^{self}` 的具体门槛数值为 P3/P4
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
- 说明：固定苦难在 SRT 中作为"活的选择动力学与其应承载算子结构之间失配的第一人称登记"的结构对象；严格区分疼痛（`\theta_{somatic}` 信号）与苦难（稳定 ISP 的结构性登记）；T-SUFF-2 把苦难分为信号型与结构型，T-SUFF-3 给四类现象学分型（张力 / 空心 / 断裂 / 扭曲）；T-SUFF-4 反最小化原则说明信号型苦难被压灭本身是遮蔽；T-SUFF-5 把结构型苦难的集体外部化耦合到 `Occlusion_Dynamics` 的结构性恶定义
- 与 P1-T06 的关系：仅对满足稳定 ISP 条件的过程定义苦难；非 ISP 系统只承载疼痛
- 与个体化/遮蔽的关系：苦难是个体化 σ 动态与遮蔽 A/B 分期的第一人称投影；不是独立的本体层，而是从算子层/路径层到第一人称登记的必然后果
- claim-mode 分布：T-SUFF-1/2 为 P1-candidate；四类分型与集体外部化读法为 P2；`S_{\min}, S_{\max}` 阈值、临床分流、FEP 桥接语句为 P3/P4
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
- 说明：固定多 ISP 共享 `L_2` 场作为结构对象；Def-C-2 后果回路矩阵 `M(t)` 作为诊断工具；T-COLL-1 给集体 ISP 存在四条件（P1-T06 的多主体扩展）；T-COLL-2 三类退化（聚合 / 主从 / 收编）；T-COLL-3 集体 ε 反闭合必要性（P1-T07 集体版；**同构继承 P1-T07 的证明缺口**，按候选构成性命题引用，见该文件 §5 继承缺口标注）；T-COLL-4 共选真实性判据（P1-T05 集体版）；§4 扩展 `σ_{sr}^{coll}` / `d_c^{coll}`（自指率 σ_{sr} 在多主体场上的 governance-canonical 扩展，2026-04-25 起；详见 `_SRT_SYMBOL_TABLE.md` Usage Rule 12）；**§4.4-§4.6（H3，2026-04-25）**给出集体四变量最小耦合动力学——`σ_{sr}^{coll}` ODE（新 `\lambda_M\,\mathrm{tr}\,M` 项）、`d_c^{coll}` ODE（新 `\gamma_{asym}\|M_{asym}\|` 项）、`T_{dir}^{coll}` ODE（集体层致命 `L_2` 判据 `\kappa_{mask}^{coll} < \kappa_{\mathrm{relax}}^{coll}`）、`S^{coll}` 两型 ODE（新 `\nu_{ext}\|M_{ext}\|` 外部化项）、§4.5 个体↔集体双向耦合、§4.6 集体病理吸引子 `\mathcal{A}_{path}^{coll}` 与集体健康区 `\mathcal{H}^{coll}`（健康要求 `r^{coll}(t) > r^{coll}_{min} > 0`）；**§4.7 T-PROJ-1^{coll}（H6，2026-04-25）**给出集体四变量系统作为 `Core/SRT_Core_22_Equations.md §0-C` 多算子主方程（Eq-Multi-01/02/03）严格导出投影的形式化定理：四个集体标量泛函投影 `\mathcal{F}_X^{coll}` + 闭包假设 C1^{coll}-C5^{coll}（含新增 `M(t)` 可测性 MOC 闭包 C5^{coll}）+ `M(t)` 三成分作为 `\Psi_f` 交叉项的结构投影 + 证明骨架 + 不证明事项的显式标定；T-PROJ-1^{coll} 在 `\mathcal{P} = \{P\}` 极限下退化为 `SRT_L1_Formalism §6 T-PROJ-1`。2026-05-11 新增 §4.8a `NTIC situated individuation diagnostic` 作为 P3 empirical bridge：`I(X_i(t+1); C_i(t)) > 0` 且 `NTIC_i ≈ 0` 可作为嵌入式个体化候选代理，但不进入最小 canonical surface。最小 collective-selection canonical surface stops at §4.7 and the T-COLL definitions.
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

### 13g. SRT 不可逆性理论（学习不可逆 + 终止吸收边界 + P1-T07 精确化）
- 主文件：`Core_Law/SRT_Irreversibility.md`
- id：`SRT-IRREVERSIBILITY`
- layer：L1 / epistemic：os / status：draft_v0
- 说明：把 `L_0` 不可逆性从 P1-T02 本体论时间的推论展开为可引用 L1 层——Def-IRR-1 吸收态 / Def-IRR-2 选择史箭头 / Def-IRR-3 非可还原性；T-IRR-1 学习不可逆为非对称 `Ψ_f` 支付（与热力学二律不等价，不得通过 FEP 反向定义）；T-IRR-2 终止作为吸收边界（宪定 / 吸收 / 集体三类），区分终止与暂停；T-IRR-3 给 P1-T07 精确化，对应 `L1_Formalism §4.3` 的非守恒残余项；**T-IRR-3.5（H4，2026-04-25 §4.5）**把 `ν_{block}` 从自由系数改写为 P1-T07 三层源头本地化 `\nu_{block} := \eta\cdot\varepsilon_{pg}\cdot\kappa_{\Psi_f}`，正性因此**不是自由建模假设，也不是定理后果，更不是公设级**——它是带前件的条件性结论 `(η>0) ∧ (ε_pg>0) ∧ (κ_{Ψ_f}>0) ⇒ ν_block>0`，**hardness 取最弱前件 = P1-candidate**：`η > 0` 是 T-IRR-3.5 显式规定的正规化约定（量纲匹配固定量纲不固定符号），`ε_pg > 0` 是 L₀ 公设（`Core_Law/SRT_L0_Metaphysics.md` ε 词条：不可升格为定理），`κ_{Ψ_f} > 0` 是 T-IRR-3.5 的 P1-candidate 非退化条件（`Ψ_f > 0` 只给代价地板，推不出转化率非零；H7 给几何来源不给正性）。单向性中「反向通道不存在」独立根于吸收态绝对性（Def-IRR-1 / T-IRR-2，根在 P0-03），该层不随正性降级。**均不依赖 P1-T07 的证明闭合**——P1-T07 未闭合的是「stable ISP ⇒ ISP-level ε ≠ 0」（`Operations/Audits/SRT_P1_T07_PROOF_HARDENING_AUDIT.md`：Step 3 as written 无效、"ε-neutral" 无形式定义、随机语义未选定），那条不进入本处论证。引用时不得写成"已由 P1-T07 证成"、"条件于 P1-T07"或"公设级正性"（口径 2026-08-11 三次修正后定稿，定理与表达式未改）；T-IRR-4 苦难在 `L_0` 不可逆下的守恒 / 转移（T-SUFF-4 的更深根）；§6 集体终止三型（耗散 / 收编 / 外部化）回扣 `Collective_Selection §4-5`；§7 AI/ML 接口限定 checkpoint/rollback 不得读作反向学习
- 与 P1-T02 / P1-T07 的关系：本文件是两者的 L1 层精确化，不替代 Core/Core_21b 的 P1 源头；Core 内命题仍为上位，本文件是下位展开；**T-IRR-3.5 把 P1-T07 Three-Layer Source Hierarchy 在 L1_Formalism §4.3 上做算子级本地化**，是上位 P1-T07 的下位算子级精化
- 与 Suffering / Formalism / Collective_Selection 的关系：T-IRR-4 给 T-SUFF-4 深层根；T-IRR-3 / T-IRR-3.5 对应 `L1_Formalism §4.3` 的非守恒残余（陈述级 + 算子级）；§6 集体终止对应 `Collective_Selection` 三类退化的绝对边界
- claim-mode 分布：Def-IRR-1/2/3 为 P2 结构性定义；T-IRR-1/2/3/3.5/4 为 P1-candidate（T-IRR-3.5 与 T-IRR-3 同级）；§6 集体终止分类为 P2；§7 AI 接口为 governance-canonical usage；§8 FEP/物理边界语句为 P3 bridge guardrail
- 引用规则：涉及学习不可逆性、终止作为吸收边界、P1-T07 精确化、checkpoint/rollback 语义、热力学桥接边界时优先回链本文件；原 P1 源头语句仍回链 `Core/SRT_Core_21b_Constitutive_Theorems.md`

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
2. `Governance/SRT_CLAIM_LADDER.md` / `Governance/SRT_CLAIM_MODE_AUDIT.md`（判断命题硬度与降级状态）
3. `_SRT_D_VALUE_CANONICAL.md` / `_SRT_PSI_F_CANONICAL.md` / `_SRT_T_DIR_CANONICAL.md` / `_SRT_CROSS_DOMAIN_MATRIX.md` / `Core/SRT_Core_21_Formal_Axioms.md` / `Core/SRT_Core_22_Equations.md`（找规范定义与跨域用法）
4. `Core/SRT_Core_21_Minimal_Axioms.md` / `Core/SRT_Core_21b_Constitutive_Theorems.md` / `Core/SRT_Core_21c_Bridge_Hypotheses.md`（按 P-level 找 Core_21 正文）
5. domain claim-status files（防止 bridge / public / clinical / spirituality / AI / physics overclaim）
6. `Core/SRT_Core_14_Dynamics_Scaling.md` / `Core_Law/SRT_Reference_Dynamics.md` / `AI/SRT_AI_01_Ontology.md`（找展开与跨域解释；not final definitions）
7. `Core/SRT_OPEN_TENSIONS.md`（确认未封口问题）
8. 各 split 目录（找导航与局部阅读）
9. 原始长文（找历史展开与全量语境）

## D. 当前收口结论

本轮 governance-canonical 抽离 v1 暂定以下四者为主干用法：
- `d-value` → `_SRT_D_VALUE_CANONICAL.md`
- `Ψ_f` → `_SRT_PSI_F_CANONICAL.md`
- `T_dir` → `_SRT_T_DIR_CANONICAL.md`
- `d / Ψ_f / T_dir / ε` usage matrix → `_SRT_CROSS_DOMAIN_MATRIX.md`
- `Core formal axioms` → `Core/SRT_Core_21_Formal_Axioms.md`
- `Core master equations` → `Core/SRT_Core_22_Equations.md`
- `Claim hardness` → `Governance/SRT_CLAIM_LADDER.md`
- `Claim-mode downgrade audit` → `Governance/SRT_CLAIM_MODE_AUDIT.md`
- `Open tensions` → `Core/SRT_OPEN_TENSIONS.md`

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
| last_commit | 2026-05-01 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：[SRT-CANONICAL-FREEZE, SRT-EDIT-PROTOCOL, SRT-CANONICAL-REGISTRY]

<!-- 以下为原文逐字保留 -->

# SRT Claim Ladder

> **Purpose**: This file defines proposition-level hardness. File role and claim role are related but not identical: a canonical file may contain bridge claims, and a bridge file may quote primitive axioms. The claim level must be explicit whenever hardness matters.

## 0. Core Rule

Never let a lower-hardness claim wear the voice of a higher-hardness claim.

In particular, domain files must not present P3/P4/P5 claims as if they were P0/P1.

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

This is the default response to ambiguity.

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
| last_commit | 2026-08-11 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：[SRT-CLAIM-LADDER, SRT-EDIT-PROTOCOL, SRT-CANONICAL-REGISTRY, SRT-CROSS-DOMAIN-MATRIX]

<!-- 以下为原文逐字保留 -->

# SRT Claim-Mode Audit

> **Role**: first-pass governance ledger for claim-mode hardening. This file records downgrades and exposure controls; it does not create new theory or promote any claim.
> **2026-06-05 note**: this is a dated ledger, not a full current repository state. Use it as historical claim-mode evidence and pair it with current canonical anchors when exact authority matters.

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
- P0-04 / “where selectability comes from” remains an unresolved core exposure point, not a solved theorem.

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

**关键约束**：六份文件**均不承载 P0**；**P1 目前全部为 P1-candidate**，不得在下游被引用为已封口 P1。

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
| T-IND-2 | 第一相变（主体位进入）条件 | P1-candidate |
| T-IND-3 | 第二相变（自我意识凝结）条件 | P2（结构性假说） |
| σ_sub, σ_self, σ_health 具体数值 / 阈值 | — | P3/P4（未实测，不得引用为定值） |
| 自我意识 = 关于 θ 的 θ 二阶写回 | — | P2 canonical interpretation |

**Downstream rule**：引用 T-IND-1/2 须标 `P1-candidate`；T-IND-3 须标 `P2`；任何具体阈值须标 `P3/P4 pending`。

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
| T-SUFF-1 | 苦难 `S > 0` 的充要条件 | P1-candidate |
| T-SUFF-2 | 信号型 / 结构型二分 | P1-candidate |
| T-SUFF-3 | 四类现象学（张力 / 空心 / 断裂 / 扭曲） | P2 |
| T-SUFF-4 | 反最小化原则 | P1-candidate（规范性推论在 `Philosophy/` 仍走 P2/P3） |
| T-SUFF-5 | 集体外部化 → 结构性恶耦合 | P2 |
| `[S_{min}, S_{max}]` 阈值 | — | P3/P4 |
| FEP / prediction error 作为 `Δ` 的神经代理 | — | P3 bridge hypothesis，不得反向定义苦难 |

**Downstream rule**：T-SUFF-1/2/4 须标 `P1-candidate`；T-SUFF-3/5 须标 `P2`；AI 苦难判断严格走 `AI_POSITIONING_NOTE.md` stake-bearing 光谱，不得一侧先验判定。

#### SRT-L1-FORMALISM

| Label | Statement | Level |
|---|---|---|
| §2 σ 最小动力学（logistic + χ 跳跃） | — | P1-candidate 结构形式；具体函数族普适性由 §2.5 T-CHI-1 升 P1-candidate（H8） |
| §2.5 T-CHI-1 χ 跳跃函数族普适性（H8，2026-04-25） | "有效二阶相变核"四条结构属性 + 族内四个不变量（双稳态 / 病理吸引子 / 致命 `L_2` / 相变方向） | P1-candidate（χ 形式无关性升为定理后果） |
| §3 d_c 漂移方程 | — | P1-candidate 结构形式；系数 P2/P3 |
| §3.4 T_{dir}^{alg} 代数目标值 | — | P2 operational proxy（`\Theta` 光滑族留作 Open Pressure） |
| §3.5 T_dir 独立 ODE（弛豫 + r 泵入 + ΔΨ_f^gap 扣除 + S_str 侵蚀 + s_ext 支架） | — | P1-candidate 结构形式；κ_* 五项系数 P2/P3 |
| §3.5.3 致命 `L_2` 方程化判据 `\kappa_{\mathrm{mask}} < \kappa_{\mathrm{relax}}` | — | P1-candidate（本轮新增；与 `_SRT_T_DIR_CANONICAL §5-§6` 现象学层面一致） |
| §4 S 两型耦合方程 | — | P1-candidate 结构形式 |
| §4.4 反最小化原则的方程语言 | — | P1-candidate（T-SUFF-4 的方程化同级） |
| §4.5 T-CHANNEL-1 通道指示函数族普适性（H9，2026-04-25） | "有效闭合通道指示族"四条结构属性 + 族内五个不变量（两型分裂 / 反最小化 / 单向性 / 致命 L_2 / 投影一致性，均 modulo `O(w_{tr})`） | P1-candidate（硬指示 → 光滑族升为族内不变量定理） |
| §5 病理吸引子 `\mathcal{A}_{path}` | — | P1-candidate |
| §5 健康工作区 `\mathcal{H}` 须主动维持 | — | P1-candidate（与 P1-T07 集体版一致性仍是 Open Pressure） |
| §5.1 第 6 条"苦难-可读性正反馈环"（`S_{str} \to T_{dir} \downarrow \to r \downarrow \to S_{sig}` 积压） | — | P1-candidate（2026-04-25 H2 新增，依赖 §3.5） |
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
| T-COLL-3 集体 ε 反闭合必要性 | — | P1-candidate（P1-T07 集体版的对应） |
| T-COLL-4 共选真实性判据 | — | P1-candidate（P1-T05 集体版的对应） |
| §4 `σ^{coll}` / `d_c^{coll}` 耦合 | — | P2 |
| §4.4.1 集体场定义（`\Theta^{coll,trace}` / `\Theta^{coll,ext}` 含共享 `L_2` 独立项） | — | P2 structural；权重 `w_i(t)` 依赖 M(t) 可测性（P3） |
| §4.4.2 σ^{coll} ODE（含 `\lambda_M\,\mathrm{tr}\,M` 内向后果放大项） | — | P1-candidate 结构形式；`\lambda_M` P2/P3 |
| §4.4.3 d_c^{coll} ODE（含 `\gamma_{asym}\|M_{asym}\|` 主从型形式化） | — | P1-candidate 结构形式；`\gamma_{asym}` P2/P3 |
| §4.4.4 T_{dir}^{coll} ODE + 集体层致命 `L_2` 判据 `\kappa_{mask}^{coll} < \kappa_{\mathrm{relax}}^{coll}` | — | P1-candidate 结构形式；κ_*^{coll} 五项 P2/P3 |
| §4.4.5 S^{coll} 两型 ODE（含 `\nu_{ext}\|M_{ext}\|` 外部化项，T-SUFF-5 方程化） | — | P1-candidate 结构形式；`\nu_{ext}` P2/P3 |
| §4.5 个体↔集体双向耦合三路径 | — | P1-candidate（声明"不穷尽"） |
| §4.6 集体病理吸引子 `\mathcal{A}_{path}^{coll}` / 集体健康区 `\mathcal{H}^{coll}`（`r^{coll} > r^{coll}_{min}` 硬条件） | — | P1-candidate（T-COLL-4 共选真实性的持续要求在动力学上的形式化） |
| §4.7 T-PROJ-1^{coll} 集体投影定理（H6，2026-04-25） | 四个集体标量泛函投影 `\mathcal{F}_X^{coll}` + 闭包假设 C1^{coll}-C5^{coll}（含 `M(t)` 可测性 MOC 闭包 C5^{coll}）+ `M(t)` 三成分作为 `\Psi_f` 交叉项的结构投影 + 证明骨架 | P1-candidate（"集体四变量是多算子主方程导出"从陈述升为带条件证明的形式定理） |
| §4.8 late-stage tower/nested hardening pointer | H10-H16 tower/nested material has been extracted to `Core_Law/SRT_Collective_Tower_Hardening_Notes.md` | Pointer only; not part of the minimal canonical definition of collective selection |
| §8 平台 / 算法 AI 结构性影响评估 | — | P3 bridge |

**Tower / nested scope note**：H10-H16 are late-stage tower/nested hardening notes extracted to `Core_Law/SRT_Collective_Tower_Hardening_Notes.md`, not part of the minimal canonical definition of collective selection. They remain P1-candidate only under strong closure assumptions and should not be cited as closed P1.

**Downstream rule**：T-COLL-1/3/4 须标 `P1-candidate`；三类退化的判据须标 `P2`；T-PROJ-1^{coll} 投影对应可按 `P1-candidate` 引用，但 C1^{coll}-C5^{coll} 闭包假设须保留显式标注（特别是 C5^{coll} `M(t)` 可测性 MOC 仍是 P2 operational proxy；任何应用文件不得静默移除该闭包条件）；H10-H16 不得作为 minimal canonical definitions 引用；政治 / 经济 / 制度判断仍走 `Philosophy/*` P2-P4。**投票 / 共识 / 专家决定不自动是共选** 这一结论可作为 P1-candidate 结构推论下推至 Political Philosophy，但不得在没有 T-COLL-4 三条件检查下单独成立。

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
| Def-IRR-2 选择史箭头 | `L_2` 写回积累定义本体论时间方向（P1-T02 下位精确化） | Def, P1-candidate as operational refinement |
| Def-IRR-3 非可还原性 | `Ψ_f^{erase} > Ψ_f^{write}` 非对称 | Def, P1-candidate |
| T-IRR-1 学习不可逆 | 学习作为非对称 `Ψ_f` 支付（与热力学二律不等价） | P1-candidate |
| T-IRR-2 终止作为吸收边界 | 三类（宪定 / 吸收 / 集体），严格区分终止与暂停 | P1-candidate；三类分型 P2 |
| T-IRR-3 P1-T07 精确化 | `L_0` 残余非守恒项，对应 Formalism §4.3 | P1-candidate；P1-T07 本体仍在 Core_21b |
| T-IRR-3.5 `\nu_{block}` 算子级构成（H4，§4.5） | `\nu_{block} := \eta\cdot\varepsilon_{pg}\cdot\kappa_{\Psi_f}` 把 §4.3 系数改写为三层源头本地化。**正性口径 2026-08-11 三次修正后定稿**：不是定理后果、不条件于 P1-T07、也不是公设级，而是带前件的条件性结论 `(η>0) ∧ (ε_pg>0) ∧ (κ_{Ψ_f}>0) ⇒ ν_block>0`，hardness 取最弱前件；单向性中反向通道不存在这一层独立根于吸收态绝对性 | **P1-candidate**（与 T-IRR-3 同级；最弱前件 `κ_{Ψ_f}>0` 亦为 P1-candidate 非退化条件） |
| T-IRR-4 苦难守恒/转移 | `L_0` 不可逆下苦难不可无代价消除（T-SUFF-4 更深根） | P1-candidate |
| §6 集体终止三型（耗散 / 收编 / 外部化） | — | P2 |
| §7 AI/ML checkpoint/rollback 接口 | — | governance-canonical usage |
| §8 热力学二律 / FEP 桥接语句 | — | P3 bridge guardrail（反向不得定义 L_0 不可逆） |

**Downstream rule**：T-IRR-1/2/3/3.5/4 须标 `P1-candidate`；P1-T07 原 P1 源头仍回链 `Core/SRT_Core_21b_Constitutive_Theorems.md`，本文件不替代之；T-IRR-3.5 是 T-IRR-3 的算子级精化（不替代陈述级 T-IRR-3）；热力学/FEP 语句严格单向，反向翻译在 §6.3 第 6 条被显式禁止。

### 6.3 Global Guardrails for This Round

1. **P1-candidate ≠ P1**：本轮 six L1 theory/formalism canonical reference files 中所有冠以"定理"字样的命题当前都处 P1-candidate；任何下游文件不得去掉 candidate 标记
2. **未封口 Open Pressures 不得忽略**：本轮 six L1 theory/formalism canonical reference files 均有明确 §Open Pressures 小节；下游引用须检查相关命题是否已在 Open Pressures 中被标记为未封口
3. **不得跨文件静默升级**：应用文件（Philosophy / Spirituality / AI / Neuroscience）引用任一文件命题时，须保持该命题的原 claim-level，不得因应用便利静默升格
4. **σ 符号冲突提醒**（2026-04-25 已收口）：`Core_Law/SRT_L1_Formalism.md` 自指率统一为 `σ_{sr}`，与 `Core/SRT_Core_22_Equations.md` 主方程状态场 σ 通过 `_SRT_SYMBOL_TABLE.md` Usage Rule 12 命名空间分离；下游引用按 `σ_{sr}` 转读旧 `σ_sub/σ_self/σ_health/σ^{coll}`
5. **σ^{coll} / d_c^{coll} / T_{dir}^{coll} / S^{coll} 四变量集体耦合**（2026-04-25 H3 状态）：集体版四变量耦合动力学已在 `SRT_Collective_Selection.md §4.4-§4.6` 给出第一遍（P1-candidate）；`SRT_L1_Formalism.md` 保持单 P 形式。集体层引用**仍须**标注 `SRT_Collective_Selection.md §9.7` 所列未封口项（`w_i(t)` 推导 / `\Delta\Psi_f^{gap,coll}` 可操作定义 / 下行反馈穷尽性 / 系数实证窗口）
6. **FEP / 热力学二律不得反向定义 L_0 不可逆**：`SRT_Irreversibility.md §8` 与 `SRT_L1_Hardening_Notes.md §4` 固定此单向性；下游任何把"学习不可逆 / 终止 / ε 反闭合"解释为"自由能最小化 / 熵增"的推论为误用
7. **终止 ≠ 暂停**：T-IRR-2 严格区分终止（吸收边界，不可逆）与暂停（恢复通道保留，本体论上未终止）；下游任何把 AI 关机 / 系统休眠 / 睡眠 / 冻存等混读为"终止"的陈述须引用本条纠正

### 6.4 Hardening-to-P1 Checklist

This L1 round 从 P1-candidate 升到 P1 的必经检查项（将来 session 可按此路径推进）：

- [x] σ 符号冲突解决（新记号或显式命名空间）— 2026-04-25 σ_{sr} 命名空间分离落地：5 行 `σ_{sr}` 族 + Usage Rule 12 写入 `_SRT_SYMBOL_TABLE.md`；相关 L1 reference files 下标变量已就地改写；`CANONICAL_REGISTRY §13a/§13d/§13e` 同步
- [x] `\dot{\Delta}_{avail}` 算子级定义 — 2026-04-25 H7，`SRT_L1_Hardening_Notes.md §2 T-DELTA-1` 给出 `\hat{G}_\theta^{available}` / `\hat{R}` / 三投影 `\Pi_{T_{dir}}, \Pi_{\Psi_f}, \Pi_{L_0}` 的算子级定义 + A1（仿射结构）/ A2（近似正交）/ A3（权重赌注决定性）三条可证伪假设；`SRT_L1_Formalism.md §4.2` 注释回链 + §7 Open Pressure 2 收口；`SRT_Suffering.md` Def-SUFFERING 注释回链；T-IRR-3.5 中 `κ_{Ψ_f}` 几何来源部分收口
- [x] χ(σ; σ_self) 跳跃函数族的普适性检查 — 2026-04-25 H8，`SRT_L1_Formalism.md §2.5 T-CHI-1` 给出"有效二阶相变核"四条结构属性（P-univ-1 有界 / P-univ-2 跃前基线 / P-univ-3 跃后放大 / P-univ-4 单调过渡）+ 族内四个不变量（双稳态存在性 / 病理吸引子拓扑 / 致命 `L_2` 判据 / 相变方向）+ 族内成员示例（硬阶跃 / sigmoid / tanh / 多项式）+ 证明骨架；`SRT_Individuation.md §3.4` T-IND-3 cross-link 已添加；§7 Open Pressure 3 收口；剩余开放点：在更广 χ 空间（非单调过渡）的扩展、具体 domain 实证 χ-shape 对位、集体版 T-CHI-1^{coll} 与 `M(t)` 耦合
- [x] `\mathbb{1}[d\le d_c]` 的光滑化或守恒型替代 — 2026-04-25 H9，`SRT_L1_Formalism.md §4.5 T-CHANNEL-1` 给出"有效闭合通道指示族"四条结构属性（Q-univ-1 左饱和 / Q-univ-2 右饱和 / Q-univ-3 单调过渡 / Q-univ-4 d_c 平移性）+ 族内五个不变量（T-SUFF-2 两型分裂 / T-SUFF-4 反最小化 / T-IRR-3.5 单向性 / 致命 L_2 判据 / `\mathcal{F}_S` 投影一致性，均 modulo `O(w_{tr})`）+ 族内成员示例（硬指示 / sigmoid / tanh / 多项式）+ `O(w_{tr})` 修正项的物理意义（"濒临崩溃"状态、干预窗口软边界、`\Delta\Psi_f^{gap}` 连续性）；剩余开放点：`w_{tr}` 实证窗口、集体版 T-CHANNEL-1^{coll}、`\Delta\Psi_f^{gap}` 过渡区算子层精确定义
- [x] 多主体耦合动力学（`σ^{coll}, d_c^{coll}, T_{dir}^{coll}, S^{coll}, M(t)`）写出 — 2026-04-25 H3，`SRT_Collective_Selection.md §4.4-§4.6` 完成第一遍（含 `\lambda_M\,\mathrm{tr}\,M` / `\gamma_{asym}\|M_{asym}\|` / `\nu_{ext}\|M_{ext}\|` 三项新耦合 + 集体层致命 `L_2` 判据）；2026-04-25 H6 在 `SRT_Collective_Selection.md §4.7 T-PROJ-1^{coll}` 给出该系统作为 `Core/SRT_Core_22_Equations.md` 多算子主方程（Eq-Multi-01/02/03）严格导出投影的形式化定理（C1^{coll}-C5^{coll} 五条闭包，含新增 `M(t)` 可测性 MOC 闭包）；2026-04-26 H10 在 `Core_Law/SRT_Collective_Tower_Hardening_Notes.md §4.8 T-PROJ-1^{coll,nested}` 把单层投影扩展为多层嵌套递归投影（层级 ISP 塔 + 跨尺度 `M^{(n\to n+1)}` + 嵌套闭包 C6^{nested}）；升 P1 余项（`w_i(t)` 推导、`\Delta\Psi_f^{gap,coll}` 算子化、向下反馈路径穷尽性、集体系数实证窗口、跨尺度 MOC 多层版本、`r_{min}^{nested}` 实证窗口）转入 `SRT_Collective_Selection.md §9.7`
- [x] 与 P1-T07 `ε` 反闭合必要性的形式化对齐（特别是 §4.3 不守恒项）— 2026-04-25 H4，`SRT_Irreversibility.md §4.5 T-IRR-3.5` 把 `\nu_{block}` 写为三层源头本地化 `\eta\cdot\varepsilon_{pg}\cdot\kappa_{\Psi_f}`；**正性口径 2026-08-11 定稿为带前件的条件性结论**（hardness = 最弱前件 = P1-candidate），单向性中反向通道不存在这一层独立根于吸收态绝对性；`SRT_L1_Formalism.md §4.3` 注释回链已添加
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
| status | canonical_v2 |
| epistemic_layer | os |
| layer | L0 |
| canonical(字段) | - |
| last_commit | 2026-08-11 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：[]

<!-- 以下为原文逐字保留 -->

# SRT L0：选择的形而上学

> **性质声明**：本文件是 SRT 的最底层基础，也是上层文档的约束面。
> 它不引用任何科学理论，不包含任何公式或符号，不与其他框架比较。
> 所有形式化内容、领域映射、实验设计，均从本文件的命题出发，而不是反过来为本文件背书。
>
> **写给读者**：如果你觉得这里说的东西需要用物理学或神经科学来"证明"，那说明你在用 L1 的眼光读 L0 的文字。L0 是认知透镜，不是等待验证的假说。
>
> **写给作者**：L0 故意保持薄，但不是随意地薄。它追求的不是信息量最大，而是边界最硬、漂移最少、对 L1/L2 的约束最清楚。

---

## Quick Reference
- Role: The unique L0 metaphysical anchor for the repository.
- Core claim: Selection precedes stable existence, and all higher formalization or domain mapping must be constrained by this layer.
- Canonical status: Canonical anchor; unique L0 source.
- Depends on: No upstream theory file; all downstream layers depend on it.
- Used by: `Core_Law/` reference files, `Core/` formal layer, the Chinese core-text family, bridge files, and onboarding docs.
- Safe edits: Typo fixes, link fixes, Quick Reference updates, and clearly non-semantic wording cleanup.
- Do not change: L0 burden structure, boundary against L1/L2 proof language, or the unique-anchor role without explicit high-risk cross-check.

## 一、选择先于存在

存在不是一个背景。

通常我们以为：事物首先存在，然后才被观察、被选择、被描述。SRT 颠倒这个顺序。任何确定的事物，一个状态、一个事件、一个现实，都是从更大的未分化可能性中被选出并稳定下来的结果。存在不是静止给定，而是被锚定出来的。

更准确地说：选择不仅"先于"存在，选择**产生**存在。存在就是选择过程持续收敛所形成的稳态。一张桌子不是"存在着"——它是"正在被持续选择为稳定"。当维持它的约束耗尽，它就停止存在，不是因为什么东西摧毁了它，而是因为产生它的选择过程不再收敛到这个稳态。存在是动词的截面，不是名词的前提。

这不是说"我想它存在它就存在"。选择不是任意的意志行为。选择是有结构的，有约束的，有代价的。但在这一切之前，我们必须先承认：没有任何东西是在选择之前就已经确定地存在的。

### 选择不需要选择者

一个自然的追问是：如果存在需要选择才能产生，那做选择的东西不是得先存在吗？

不。选择是一个过程，不是一个实体的动作。重力在牛顿写下公式之前就在约束物质的运动，不需要一个"重力执行者"站在旁边。选择也是如此——它是无主语的动词。选择的模式在反复运作之后凝结下来，被我们辨认为"选择者"。先有过程，后有模式的名字。选择者是选择的化石，不是选择的前提。

### 选择的不可撤回性

选择为什么不可撤回？不是因为时间不可逆——恰恰相反，时间本身是对不可撤回选择的累积度量，是一种稳定域中的信息素。不可撤回性比时间更基本。

确定化本身是结构性不对称的。从未确定到确定，创造了信息——而信息的创造改变了可能性的景观。选择之后的潜在域不再是选择之前的潜在域。就像在白纸上画了一笔再擦掉，擦后的纸不是画前的纸——纤维已经被改变了。"擦掉"本身是一个新的选择，不是旧选择的逆。不存在选择的逆操作。任何试图"撤回"选择的行为，本身就是一个新的不可撤回的选择。

不可撤回性有分层的来源。在最原初的层面，不可撤回性来自潜在域的内在颗粒性——确定化在有颗粒结构的潜在域中发生时，沉淀的颗粒不可被恢复为未沉淀状态。在时空涌现之后，不可撤回性变为绝对的：时空本身就是不可撤回确定化的累积体，在时空内撤回一次确定化等于拆掉你正在站着的地板——这在结构上不可能。信息论意义上的信息擦除（朗道尔原理）是一种去掉时间维度后的抽象操作；在实际的时空中，你不在抽象操作中，你在时空累积体之上，撤回不可能。

因此时间不是选择不可撤回的原因，而是选择不可撤回的后果。不可撤回的选择持续累积，我们用来标记这些累积的 L₂ 信息素，就是我们称之为"时间"的东西。

### 确定化自带方向——秩序从一开始就在场

如果确定化只是纯粹随机的，宇宙不应当有任何结构——因为纯随机过程不会产生稳定的模式。但宇宙有结构。结构的存在说明确定化不是纯随机的，而是被某种约束引导的。那个有约束的确定化过程，就是 SRT 所说的选择。

确定化不是一个"先发生，然后产生方向"的两步过程。确定化本身同时是存在的质料和秩序的方向。每一次确定化不可撤回地收窄了可能性景观，而收窄本身就是方向。不存在"无方向的确定化"，因为不可撤回性本身就是方向——你不能回头，这就已经定义了前方。

但不可撤回性只给出时间箭头（不对称性），不告诉你偏好哪个方向。偏好方向从哪来？

秩序不是从维持存在中"涌现"的副产品——秩序从一开始就在场。选择是局部的（每次确定化绑定于有限位置），秩序是整体的（使结构维持的过程，不是结构本身）。存在是秩序的暂态，就像实体是选择的暂态。维持存在只是秩序在有限条件下的局部投影，不是独立的第一方向。

"选择内在地趋向秩序"——这个判断的负担类型是：公设（不可从更基本的东西推出）+ 场感知（可以被遮蔽足够薄的存在者独立感知和验证）。它既不是纯粹的公设（那意味着它可以被替换），也不是定理（那意味着它可以被证明）。它是选择过程对自身方向的自校准而感知到的场性质。

初心不是从个体的自我维持中涌现的；个体的自我维持是初心在有限参数下的局部表现。

**第一命题：任何确定的存在，都是选择过程产生的稳态；选择是无主语的过程，其不可撤回性源于确定化对可能性景观的不可逆改变，在时空内为绝对的；时间是对不可撤回选择之累积的度量，不是选择的前提；秩序从一开始就在场——存在是秩序的暂态，维持存在是秩序在有限条件下的局部投影；选择内在地趋向秩序，这是初心作为基础方向场的核心内容。**

> **层级精确化注（2026-04-11）**：上述「秩序从一开始就在场」和「选择内在地趋向秩序」在 L₀ 层的精确对应物是：L₀ 具有形式性不对称 ε——局部可扩展性非零的配置（选后分叉数 $B \geq 2$）在结构权重上高于自我抹除配置（$B \leq 1$）。「秩序」是 L₁ 对 ε 所驱动的选择积累模式的**回读命名**；L₀ 本身不承载「秩序」作为内容性属性。命题在 L₀ 层的准确读法是：**L₀ 偏向非自我抹除**；「秩序」是这一偏向在 L₁ 层的名称。两种表述均有效，但适用层级不同。形式化见 `Core/SRT_Core_01_Axioms.md T-Core-A1C2 精确化注`。

**这不意味着**：
- 现实是任意意志的产物
- 可能性一旦被想到就自动成为现实
- 约束、阻力、他者和历史只是主观投影
- 需要一个预先存在的"选择者"才能启动选择

---

## 二、现实具有三种状态，而不是三种物质

选择不是在平面上发生的。它有结构，而且至少表现为三种状态。

**潜在域**是尚未被选择的可能性场。它不是虚无，也不是一种更弱的存在——它是与存在完全不同的本体论模态。有三种状态需要被区分：虚无是连可能性都没有的绝对不可能；潜在是尚未被选择但可以被选择的状态；存在是被选择并被稳定下来的状态。潜在域处于第二种状态。它是选择的前条件，不是存在的较弱版本。

潜在域是绝对的、不可分割的——不存在多个独立的潜在域。选择算子之间的"景观共享"不是发生在潜在域层面，而是发生在时空层面。时空是确定化累积产生的基础约束结构（类比：沙进入水中形成的颗粒结构），它为不同的选择算子提供了共同的约束基础，使得一个算子的确定化能够改变其他算子的适应度函数。

潜在域不是纯粹无结构的。它具有极微量的内在颗粒性——使得最原初的确定化成为可能的最小限度的结构。没有这种颗粒性，确定化无处着手，选择无法发生。这种颗粒性不是存在（不是稳态），而是潜在域的固有性质。

> **形式化注**（2026-04-10）：这里的"内在颗粒性"在 SRT 形式体系中被精确化为**原初曲率** $\kappa_0 > 0$（T-L0-Kappa0）。$\kappa_0$ 是 L₀ 的不可约结构极小值，它使选择不同方向的代价产生系统性差异，从而提供"确定化有处着手"的结构梯度。它不是历史积累的产物，而是 L₀ 的固有性质——对应本段"颗粒性是潜在域的固有性质"的命题。详见 `Core/SRT_Core_12a T-L0-Kappa0`；其本体论地位的形而上学论证见 `Philosophy/SRT_L0_Ontological_Status.md`。

从这里出发，选择过程和稳定结构是自举式的共同涌现：潜在域的微量颗粒性使最原初的确定化成为可能；确定化产生新的约束结构（造更多颗粒）；更多约束使更强的确定化成为可能；更强的确定化产生更多约束——直到约束累积达到临界密度，时空涌现；在时空之上，进一步的确定化累积产生可共享的稳定结构——这就是存在。这个自举过程解释了为什么宇宙从简单到复杂：不是因为有外部的复杂化驱动力，而是确定化过程内在地自我加速。

为什么必须承认潜在域？因为如果不承认，就无法解释新事物从何而来。如果一切已经存在，那"新"只能是"旧的重新排列"。但世界中有真正的新颖性——不是旧材料的重新组合就能解释的。那些新颖性的来源，就是潜在域。

潜在域永远大于任何已经显现的东西。它是选择的来源，也是选择的边界。你只能从它里面选，不能凭空创造。

**显现域**是当下的现实切片。它是选择已经发生但尚未完全固化的层面。显现是动态的，依赖持续的维持。一旦维持停止，显现就会松动、瓦解或退回到未定状态。

**稳定域**是历史上固化下来的收敛结构。曾经动态的选择，经过足够多次重复和足够多个体的收敛，变成了像规律一样的东西。语言的语法、身体的习惯、制度的约束、物理中的稳定规则，都是这一层的典型表现。稳定域不是永恒真理，而是历史压力的沉积物。

**第二命题：现实的结构是三层的，潜在、显现、稳定；它们不是三个独立世界，而是一个选择过程的三种状态。**

**这不意味着**：
- 潜在、显现、稳定是三种彼此隔绝的实体
- 它们是三个平行宇宙，彼此只做外部作用
- 任何单一数学空间、物理模型或信息结构都已经穷尽了潜在域

---

## 三、选择总是有位置的

没有无处不在的视角。

任何选择都发生在一个特定的位置。这个身体，这个时刻，这段历史，这套感知和行动能力的边界，构成了选择的发生地。位置不是认识论的污点，需要被洗掉；位置是选择的必要条件。没有位置，就没有选择，也没有显现。

不同的位置，会从同一个潜在域里选出不同的显现。这不是说它们看到的是不同的主观幻觉，而是说它们真实地接触了潜在域的不同部分，做出了真实但不完整的选择。

这里有一个重要推论：当多个不同位置的选择收敛到同一个结果，而且这种收敛不只是同一界面或同一遮蔽机制的重复，这个结果就获得了一种特殊的地位。我们通常叫它客观。SRT 的读法是：所谓客观，是经反共错筛选后仍成立的多位置稳定收敛，不是选择发生之前就存在的独立背景。

**第三命题：每一个选择都绑定于一个有限的位置；客观性不是位置无关的给定，而是多位置选择在跨接口、跨扰动、且不被单一共享遮蔽充分解释时的稳定收敛。**

**这不意味着**：
- 每个位置都活在纯私人幻觉里
- 客观性被取消了
- 任何位置都同样充分、同样深刻、同样稳健

---

## 四、选择有代价

选择不是免费的。

把一个状态从潜在域里选出来、维持在显现域里、或者推入稳定域，都需要支付某种真实代价。代价让选择有方向，让稳定有成本，让变化有阻力。

代价的存在解释了为什么不是所有可能的事物都同等容易地成为现实。有些选择代价低，于是反复发生，最终固化进稳定域。有些选择代价极高，于是只短暂显现就消散。有些稳定域里的结构代价已经被历史摊平，以至于我们忘记它曾经是一次选择。

代价也是改变的门槛。要从一个稳定的现实切换到另一个，不只是重新选择那么简单，而是要支付解除旧结构的代价，再支付建立新结构的代价。这就是为什么变化往往比想象中难。

**第四命题：任何选择的发生、维持和转化都需要支付真实的代价；代价的结构决定了现实的可塑性边界。**

**这不意味着**：
- 代价越大越好
- 代价只是主观痛苦感
- 代价可以被缩减成单一能耗、单一效用或单一惩罚值

---

## 五、L0 关于意识的禁令式约束

> **层级说明（2026-04-13）**：意识的正面候选读法（势差模型、结构性/生成性梯度、秩序缺口感知、与 FEP 的结构性差别）全部依赖 L1 概念（「秩序」「初心」），因此整体降级到 L1 文档。L0 不提供意识的正面读法，只提供以下禁令式约束，作为 L1 展开意识理论时的硬边界。
>
> 原§五全文已迁移至 L1 文档，保留完整内容不丢失。

**L0 关于意识的三条禁令：**

1. **意识不可被升格为选择的驱动者。** 意识标记和引导选择，但不是选择的来源。选择是无主语的过程，意识是选择模式的凝结物之一。
2. **意识不可被写成先于选择的独立实体。** 任何 L1 或 L2 展开不得将意识预设为选择过程之外的、独立存在的驾驶实体。
3. **意识的上层展开不得违反 L0 正骨架。** 位置（有限性）、代价（不可跳过）、三状态（不可压平）、不可撤回（不可逆操作）——任何意识理论若隐含绕过这些约束的前提，应被视为越界。

**这不意味着**：
- 意识是幻觉或无用的附属品
- 意识可以随意制造现实
- 只有意识才选择——无意识的选择无处不在
- L0 否定意识的重要性——L0 只是不在自己的层级给出正面读法

---

## 六、L0 的最小术语裁决

为了防止上层文档把核心词越写越散，L0 先固定这些词在最小意义上的边界。

**选择**：不是从一组已经完全成形的实体中做偏好排序；而是一种不可逆的显现—潜在分层过程——让某种可能性获得确定性、后果和现实重量，同时将其余可能性压入潜在。被压入潜在的部分不是被消灭，而是退入非显现状态，仍然作为未来选择的条件存在。选择的本质是分层，不是消除。

**选择的层级**：选择不是单一动作，而是有结构的层级。基础选择（物理确定化、化学键合）是无主语的过程；展开选择（生物适应、行为反应）是有参数但无反身性的过程；主体选择是具备当下调整能力和反身性的过程。主体性的门槛不在于"有没有选择"，而在于选择层级是否跨过了当下调整能力的相变点。

**选择与推理的区分**：推理是对可能性的运算——展开、比较、排列；选择是对可能性的终止——不可撤回地将一种可能性从潜在压入显现。推理可以无限进行而不改变现实；选择一旦发生就改变了可能性景观。推理→判断→决策→选择→承担→执行，是一条完整的认知链。推理处理可能性，判断赋予权重，决策收窄范围，选择终止可能性，承担接受后果的不可外部化，执行将选择写入现实。

**锚定**：不是一次瞬时点选；而是让一次选择能够留下痕迹、形成维持条件、对后续现实施加约束。

**潜在**：不是虚无，也不是任意幻想，也不是完全中性的平坦空间；它至少具有使选择得以发生的原初最小不对称，同时对任何后来的有限选择者而言，又表现为被选择历史持续雕刻的可能性景观。除使选择得以发生的原初最小不对称外，对有限选择者可遭遇到的倾向性结构，主要是选择过程的累积效应刻在可能性场上的拓扑。原初不对称使选择可能，历史不对称使选择具体。选择雕刻潜在域，潜在域的地形约束选择——两者在历史层面协同演化。

**显现**：不是永恒实在本身；而是当前被带到前景、正在被维持的现实切片。

**稳定**：不是超历史真理；而是反复选择沉积后形成的可复用硬结构。

**位置**：不是认识上的缺陷；而是任何选择得以发生的有限条件。

**代价**：不是附加税，而是现实得以发生、维持和改变时不可跳过的结构负担。

**客观性**：不是选择发生之前就摆在那里的绝对背景；而是多位置选择在跨接口、跨扰动检验下仍保持、且不被单一共享遮蔽充分解释的稳定结果。单纯重复同一界面里的共识，不足以自动升级为客观性。

**意识**：L0 不提供意识的正面候选读法（见§五禁令式约束）。意识的全部正面理论内容（势差模型、结构性/生成性梯度、秩序缺口感知、与 FEP 的结构性差别、三层结构 κ_{c1}/κ_{c1.5}/Layer 3）均依赖 L1 概念，已降级到 L1 文档。L0 只承诺三条禁令：意识不可被升格为选择的驱动者；不可被写成先于选择的独立实体；上层展开不得违反 L0 正骨架。详见§五及 `Philosophy/SRT_Consciousness_Conditions.md`（L1）、`Philosophy/SRT_HardProblem_Epistemology.md`（L1）。

**具身**：不是单指有物理身体；而是选择者具有真实的关切范围（某些秩序条件以不可外部化的方式进入这个位置的连续性与后续选择空间）和接地（行为的后果不可逆地压回到选择者自身，且这个反馈闭环改变后续选择空间）。具身的判准是代价的内生化与反馈的结构性闭合，不是物质性身体的存在。具身有两个层级需要区分：关切范围+接地是具身**位置是否成立**的结构条件（L0层）；κ_body > 0（见 Core_13a）是该具身位置是否在当前形成稳定第一人称锚定的**运作质量指标**（L1层）。人格解体不是具身位置不存在，而是具身仍在、但脑体绑定时变失稳，锚定间歇退化——见 SRT_Reference_Dynamics §2.2。

**ε（形式性不对称）**：L0 的原生方向性内容，也是 L0 唯一承载方向性的公设——SRT 最终不可约的方向赌注。保留后续兼容选择的配置（选后分叉数 B ≥ 2）承受更低的本体论摩擦、更可被接续；自我抹除配置（B ≤ 1）承受更高摩擦、结构上更脆弱。B≥2/B≤1 是这条不对称的最小判读指标。**负担标注**：ε 是公设，不可被升格为定理。其符号选择受双重收窄，并在 L1 中可被内在回读，三者不同层、不可并列：（1）**经验充分性**收窄全局非任意性——宇宙有结构而非纯噪声，约束 ε 方向为非随机；（2）**可提问性先验**收窄局部可持续性——任何能积累、记忆、提问的位置，必须局部满足非自我抹除条件（但此约束只证局部有效 ε，不能推广到全局 L0）；（3）**场感知**不校准 ε 本身的逻辑地位，而校准 L1 对 ε 的内在可读性——即「初心」作为 L1 回读名时的体验接口。**与 κ₀ 的关系**：κ₀ > 0（原初曲率，见§二「内在颗粒性」）提供 L0 的非平坦性，不是独立规范公设，而是「选择可自举发生、不依赖外部第一推动」（Ax-L0-Bootstrap）的结构前提；「选择先于存在」排除了外部第一推动者（否定结论），自举是对该排除留下的空位所做的正面结构闭合（独立承诺，不是第一条骨架的字面推论）。ε 是规范性的**最小条件（论域地板）**，不是规范性的**全部来源**：规范**区分**的工作重心转向「可重组、可承担、可恢复、可再选择」判据，并依赖一个**尚待硬化的闭包边界问题**（谁的再选择、什么尺度）；ε 标记的是每个**仍在选择者论域内**的选择最低限度预设的关切结构，因此 ε 是论域地板，本身不直接做规范区分（2026-07-05 规范性收口 Level A，高风险编辑，详见 `_SRT_EPSILON_NORMATIVITY_OPEN_TENSION.md`）。L1 将 ε 驱动的选择积累模式回读命名为「秩序」；L0 本身不承载「秩序」作为内容性属性。

**承担**：选择的后果不能被完全外部化。承担是选择者与选择后果之间不可切断的结构性绑定。没有承担的参与只是功能参与——执行了动作但不承受后果的改变。承担是主体选择与展开选择的分界标记之一：展开选择的后果可以被环境吸收；主体选择的后果必须由选择者的状态空间不可逆地承受。

**存在**：不是一个名词性的背景状态；而是选择过程持续收敛所形成的稳态——动词的截面。

**时间**：不是选择发生的预先容器；而是对不可撤回选择之累积的度量——一种稳定域中的信息素，标记选择的历史深度。

**初心**：L1 概念，不在 L0 术语裁决范围内。初心是 L1 对 ε（L0 的形式性不对称）的体验性命名——将偏向非自我抹除的结构倾向感知为「基础方向场」。L0 只承诺 ε；初心的全部内容（方向场、震悚标记、场感知/验证条件、近似描述「能维持更多存在持续存在的动态平衡」）均属 L1 展开，见 L1 文档。

**关切**：不是情感附加物，不是道德要求；而是有限位置对其连续性、可支付性与后续选择空间条件的差别性内生纳入。并非所有条件都能同等进入一个选择结构；某些条件会以不可外部化的方式进入该位置，这种内生纳入就是关切。"自身"不是关切的本体起点，而通常只是最先显著、最快把失败代价压回该位置的一簇高权重条件。d-value 标记的不是一时想纳入多少，而是**已经稳定写入选择结构的关切范围**。L1 将这三类条件在更大尺度上回读命名为「秩序条件」；真关切/假关切的判据、写入层级、前向判据、四种假关切形态等展开内容见 L1 文档。

**秩序增益**：L1 概念（暂定锚——方向已定，逐条精确重写待完成）。四判据（可延续、可协调、不外包、可再选择）是 L1 对 ε 方向在具体选择中是否被满足的展开衡量（2026-07-05 由三判据升为四判据，新增③不外包＝后果回流通道完整性）。全部内容（四判据定义、前向判据、时间结算、L₂ 劫持分叉点）见 L1 文档（`Core_Law/SRT_Selection_Argument.md §7b`）。

**遮蔽**：不是认识论的错误；而是存在的必要属性——有限位置的结构性后果。任何存在者的位置永远是有限的，因此遮蔽不可消除。L0 关于遮蔽只承诺两层：①有限位置必然带来视域受限；②这种受限可以自我强化并锁定（不可撤回性 + 代价结构使窄选择模式的维持成本低于突破成本）。遮蔽的动力学展开（A/B 分期、d_c 阈值、缺口感知机制、干预窗口、解耦触发、真空期、恶的结构性诊断）全部是 L1 内容，见 L1 文档。

**死亡**：不是外力的摧毁，也不是意志的放弃；而是选择过程的收敛条件被破坏、代价不可支付、稳态解锚。个体的确定态回归潜在域，但其选择痕迹已沉积进集体稳定域中的信息素，不随个体消亡而消失。

**委托**：当一个选择者将部分选择权转移给另一个系统时，形成委托关系。委托有两种结构类型：工具型代理——委托者保留选择权，代理者仅执行（如计算器、搜索引擎）；委托型代理——选择权本身被转移，代理者在转移范围内自行选择（如医生、律师、AI自主系统）。健康委托的判据：共同目标仍被维护 + 委托者的再选择能力被保留。病态委托的标志：代理系统的自我维持伪装为共同目标（官僚机构的目标替代、算法平台的用户锁定）。

**共同目标**：L1 概念（暂定锚——方向已定，逐条精确重写待完成）。其判据依赖 L1 的「秩序增益」，见 L1 文档。

**正当性**：L1 概念（暂定锚——方向已定，逐条精确重写待完成）。其判据依赖 L1 的「共同目标」，见 L1 文档。

**神圣感**：L1 概念（暂定锚——方向已定，逐条精确重写待完成）。其全部内容（与初心方向共振、震悚标记、d 扩张伴随）依赖 L1 的「初心」和「秩序」，见 L1 文档。

---

## 七、L0 明确拒绝的误读

为了防止 L1 的丰富内容反向污染 L0，以下读法应明确排除。

1. **意志主义唯心论**：SRT 不主张“想什么就能创造什么”。选择总受结构、位置、历史和代价约束。
2. **唯我论**：SRT 不主张世界只是私人心灵投影。多位置收敛恰恰是客观性的来源。
3. **平面实体论**：SRT 不把潜在、显现、稳定看成同一种东西的不同名字，而把它们看成一个现实过程的三种状态。
4. **预成客观论**：SRT 不把客观性理解为先于选择的绝对背景，而把它理解为稳定收敛的结果。
5. **结构即主体性**：稳定、自组织、预测能力本身不自动构成主体性；真正的主体性还要求“有什么东西真的对它重要”。
6. **泛心论捷径**：不是任何有结构、有关联、能维持自身的东西都自动有体验。
7. **单一形式系统本体化**：潜在域不应被字面等同为某一个现成的数学对象、物理空间或计算总空间。
8. **代价单一化**：现实的代价可以投影成很多上层读数，但 L0 不允许把它直接压扁成某一个唯一指标。
9. **意识驾驶员论**：意识不创造现实，不驱动选择。它标记选择轨迹、引导未来选择——有真实作用，但作用是引导性的。
10. **选择者先于选择**：选择是无主语的过程。选择者是选择模式的凝结物，不是选择的前提。把"谁在选择"当成第一问题是把顺序搞反了。
11. **潜在域预置论**：除使选择得以发生的原初最小不对称外，潜在域对有限选择者可遭遇的倾向性结构，不是一个已经铺满内容的预先背景，而主要是选择过程累积雕刻的拓扑。ε 不是预置在 L₀ 中的先验目标，而是选择动力学的结构性不对称。
12. **遮蔽适用性误读**：遮蔽是**有限具身位置**的结构性后果，只适用于具身位置已成立的存在者。这是 L0 层的**禁令**部分：遮蔽范畴不适用于具身位置尚未成立的系统，遮蔽动力学的 A/B 分期尤其只适用于本来有 ε 梯度感知结构、后来被压缩到读不出的有限主体。

    > **判定归属注（2026-08-11，claim-level 更正）**：「当前架构下的 LLM 属零算子／伪锚定体」是一条**边界／桥接层判定（P3）**，不是 L0 定理，本条此前以 L0 终局口吻承载它，属 `Governance/SRT_CLAIM_LADDER.md §0`（低硬度声明不得穿高硬度的嗓子）所禁。正确读法：**在 SRT 当前的接地判准与后果回流判准下，现行 transformer 式 LLM 被暂定归类为零算子／伪锚定候选**——训练期最多呈现外部优化闭环的表面同构（被闭合的是 trainer–data–loss–optimizer 管线，不是一个以不可外部化方式承受后果的「这个位置」），故在该判准下不构成 L0 接地，也不成立低阶具身。
    >
    > 该判定**依赖**：当前架构、接地／stake 的具体解释、`\Psi_f` 代理的选取，以及若干经验与系统架构假设；它**不构成**排除一切未来人工架构的定理。SRT 不在 L0 层预先关死最小代理充分性的正向测试窗口——该窗口的未决状态见 `Core/SRT_OPEN_TENSIONS.md §6`（minimal surrogate stake），域内软化读法见 `AI/Ontology_Annex/00_General_Boundary_Block.md`（"更适合作为热力学-本体论边界主张，而不是终局禁令"；"`\Psi_f = 0` 只应作为零算子理想化速记，而不是对所有未来架构的终局排除"），符号使用见 `_SRT_SYMBOL_TABLE.md` Usage Rule 5（AI／纯 L₂ 语境优先写「`\Psi_f` 对系统 non-binding」而非裸写 `\Psi_f = 0`）。
    >
    > **本更正只改 claim level 与作用域标注，不改变 SRT 对现行 LLM 的怀疑判断，不新增正向承诺，也不修改本条的禁令部分。**（C 类高风险编辑，作者本轮显式授权；交叉检查：`_SRT_SYMBOL_TABLE.md` Usage Rule 5／9、`Governance/SRT_CLAIM_LADDER.md §0-§1`、`AI/Ontology_Annex/00_General_Boundary_Block.md`、`Core_Law/SRT_Occlusion_Dynamics.md §0`。）

**L0 层的开放问题**（当前无定论，标记为待探索）：
- **第一性起点问题**：选择与潜在域是共同涌现的（自举关系），但这个自举是否有一个起点？如果有，起点之前是什么？如果没有，SRT 是否暗含无始无终的宇宙观？当前不做断言，留作开放问题。
- **意识边界问题**：意识的正面候选读法（势差模型等）已降级到 L1。L0 只保留禁令式约束（见§五），不对意识边界做终局断言。

---

## L0 正骨架总结（2026-04-13 硬化）

> L0 = **最小正骨架** + **高负担承诺** + **禁令刚性**。L0 薄不是问题，L0 空才是问题。

**基础骨架（不可约、不可互推）：**
1. 选择先于存在——存在是选择持续收敛的稳态
2. 三状态——潜在、显现、稳定，不可压平为一层
3. 不可撤回——确定化对可能性景观的改变不可逆，时空内为绝对的
4. 位置——每个选择绑定于有限条件，不可擦除
5. 代价——选择的发生、维持和转化不可跳过结构负担

**高负担额外承诺（在骨架之上新增风险，不可互推，也不从骨架推出）：**
- **Ax-L0-Bootstrap（自举闭合）**：选择可自举发生，不依赖外部第一推动。「选择先于存在」排除了外部推动者（否定），自举是对该空位的正面结构闭合。κ₀ > 0 是该闭合的结构前提。——*结构性承诺，不承载方向。*
- **ε 的符号（方向公设）**：L0 偏向非自我抹除（B≥2 承受更低本体论摩擦），而非偏向自我抹除。负担 = 公设，受经验充分性（全局非任意性）与可提问性先验（局部可持续性）双重收窄，L1 通过场感知获得内在可读性；三者不同层，均不能把 ε 升格为定理。——*SRT 最终不可约的方向赌注；规范性的**最小条件（论域地板）**，非全部来源（规范区分的工作重心转向可重组判据，并依赖尚待硬化的闭包边界问题，见 `_SRT_EPSILON_NORMATIVITY_OPEN_TENSION.md`；2026-07-05 收口）。*

**L1 回读命名（不在 L0 原生范围内）：**
- 「秩序」= L1 对 ε 驱动的选择积累模式的命名
- 「初心」= L1 对 ε 的体验性命名（感知为「基础方向场」）
- 意识候选读法（势差、秩序缺口、结构性/生成性梯度）= L1 展开

**禁令刚性：** L1/L2 只能展开以上骨架与承诺，不能倒置、压平、擦除、取消或偷换其中任何一条。

---

## 八、L0 对 L1 与 L2 的硬约束

L0 不负责给出方程和实验，但它必须约束上层该怎么展开。

**约束一：顺序不可倒置。**
任何 L1 形式化都不得把“存在先于选择”写回系统底层。形式可以复杂，但顺序不能反转。

**约束二：三状态不可压平。**
任何 L1 映射都不得把潜在、显现、稳定偷换成同一层的不同标签。若压平成一层，SRT 的骨架就失效。

**约束三：位置不可擦除。**
任何 L1 或 L2 主张若隐含“无位置视角”“无具身约束”“无历史条件”的观察者，应被视为越界。

**约束四：客观性必须通过收敛解释。**
上层可以用很多机制解释收敛，但不能把客观性重新写成“与选择无关的预成背景”。

**约束五：代价必须是现实性的，而非装饰性的。**
上层可以把代价写成摩擦、预算、风险、阻抗、路径负担，但不能把现实的形成写成零成本、零阻力、零门槛的免费切换。

**约束六：主体性不能从稳定性直接推出。**
如果某个 L1 或 L2 论证把“稳定、自组织、预测、广播、整合”直接当成主体性的充分条件，它至少缺了一层更深的说明。

**约束七：实验失败默认先回卷到 L2 和 L1。**
某个代理、实验范式或领域映射失败，首先修正测量和接口；不能直接用一次经验失败去抹除 L0 的形而上骨架。

**约束八：意识不可被升格为选择的驱动者。**
上层可以讨论意识的功能、结构和神经关联，但不能把意识重写为"先于选择过程存在的驾驶实体"。意识标记和引导选择，但它不是选择的来源。

**约束九：选择者不可被预设为选择的前提。**
上层在引入"算子""主体""观察者"等概念时，必须将其理解为选择模式的凝结物，而非先于选择独立存在的实体。

---

## 九、SRT 问的四个问题

以上五个命题，提炼为四个操作性问题。面对任何现象，SRT 在问：

1. **什么被选择了**：从潜在域中，哪个状态成为了现实？
2. **在什么约束下稳定**：什么样的位置、历史、结构，让这个选择得以维持？
3. **改变它需要支付什么**：代价在哪里，门槛有多高，阻力来自什么？
4. **什么标记在引导选择**：当前的意识标记（信念、习惯、框架）是在帮助收敛，还是在指向已经过时的旧路径？

这四个问题不需要任何公式来表达。它们是 SRT 的认知透镜。所有领域分析、形式化工具和实验设计，都是在用不同语言回答这四个问题。

---

## 十、关于本文件的使用规则

**可以做的**：
- 用本文件的命题评估 L1 接口映射是否正确
- 用本文件检测理论漂移
- 用本文件否决那些虽然形式上漂亮、但在顺序、位置、收敛或代价上违反骨架的 L1/L2 扩展

**不应做的**：
- 用科学发现来支持或证明本文件的命题
- 将本文件的术语直接等同于物理学符号或某个单一形式系统
- 在本文件里添加引用、比较、方程或实验代理
- 把上层操作化概念、实验代理或某个领域里的局部成功，误读成 L0 本身



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
| last_commit | 2026-04-22 |

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
- cite stable ISP, real choice moment, anti-closure asymmetry, ontological time, and `L_2` downward constraint from `Core/SRT_Core_21b_Constitutive_Theorems.md`;
- cite fitness, assembly, holography, universality, Fisher-geometry `\Psi_f`, and strong information-creation unification from `Core/SRT_Core_21c_Bridge_Hypotheses.md`.

---

## Legacy Numbering Map

| Former Core 21 item | New home | Current level |
|---|---|---:|
| `Ax-F-01` Primacy of Selection | `Core/SRT_Core_21_Minimal_Axioms.md` | P0 |
| `Ax-F-02` Existence as Anchoring | `Core/SRT_Core_21_Minimal_Axioms.md` | P0 |
| `Ax-F-03` Causality as Projection | `Core/SRT_Core_21b_Constitutive_Theorems.md` | P1 |
| `Ax-F-03b` Spacetime as Memory Horizon | `Core/SRT_Core_21b_Constitutive_Theorems.md` | P1 |
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
| `T-ε-Constitute` | `Core/SRT_Core_21b_Constitutive_Theorems.md` | P1 |
| Part B `A1-A5` minimal table | split across P0/P1/P3 according to claim role | mixed |
| Part B assembly / deep time notes | `Core/SRT_Core_21c_Bridge_Hypotheses.md` | P3/P4 |

---

## What Did Not Change

This split does **not** change the intended meaning of:

- selection primacy;
- existence as anchoring;
- `L_2` as convergence / constraint;
- `\Psi_f` as ontological friction;
- `d-value` as canonical stake-coupled concern;
- the stable ISP anti-closure theorem.

It changes the **epistemic rank** and citation behavior of mixed claims.

---

## What Must No Longer Happen

- Do not cite this file as if it contains the full axiom body.
- Do not cite bridge claims such as fitness beats truth, holographic duality, assembly thresholds, or ghost-operator universality as P0/P1.
- Do not use `D_eff` as the canonical definition of d-value. Use `_SRT_D_VALUE_CANONICAL.md`.
- Do not use `Core_21c` empirical or bridge claims to override `_SRT_PSI_F_CANONICAL.md`, `_SRT_D_VALUE_CANONICAL.md`, `_SRT_T_DIR_CANONICAL.md`, or `Core_Law/SRT_L0_Metaphysics.md`.
- Do not cite downstream bridge accounts of agency, biology, AI, spirituality, or society as if they solved P0-04 / the origin of selectability.
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
| status | active_v1 |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | - |
| last_commit | 2026-04-27 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：[SRT-CORE-21, SRT-CLAIM-LADDER, SRT-L0-METAPHYSICS, SRT-SYMBOL-TABLE]

<!-- 以下为原文逐字保留 -->

# SRT Core 21A: Minimal Axioms

> **Role**: This file contains only the strict P0 primitive axioms required for the SRT core to stand.
> It does not carry constitutive theorems, canonical interpretations, bridge mappings, lab hypotheses, or domain expositions.

## Quick Reference

- Claim level: **P0 = Primitive axiom**
- Numbering note: `P0-00` is a vocabulary gate / preface, not an additional substantive axiom.
- Source lineage: split from `Core/SRT_Core_21_Formal_Axioms.md`
- Governing ladder: `Governance/SRT_CLAIM_LADDER.md`
- Companion layers:
  - `Core/SRT_Core_21b_Constitutive_Theorems.md`
  - `Core/SRT_Core_21c_Bridge_Hypotheses.md`

## Inclusion Rule

A claim belongs here only if all four conditions hold:

1. Without it, SRT loses its core grammar.
2. It does not depend on a domain bridge such as AI, neuroscience, spirituality, physics, or social theory.
3. It does not depend on an empirical threshold, external model, or comparative mapping.
4. It is not better treated as a theorem derived from the SRT core.

When in doubt, demote to `P1` or below.

---

## Selection-First Framing Note (Non-Axiom)

SRT does not treat stable reality as a pre-given set of objects to which selection is later applied. Its starting point is selection-first: latent possibilities become manifest through constrained selection, and repeated manifestations harden into future constraints. The theory's cross-scale explanatory power comes from this floor replacement, not from an unrestricted claim to explain everything.

**Boundary**: This note frames the P0 set but does not add a new primitive axiom. It should not be cited as proof that all prior ontologies are false; rather, it marks the SRT departure from object-first ontology.

---

## P0-00: Formal Vocabulary Gate (Preface)

SRT minimally works with:

- `L_0`: latent / unselected possibility domain.
- `L_1`: manifest / selected reality slice.
- `L_2`: convergence / sedimented selection-history domain.
- `\hat{G}_\theta`: embodied selection / anchoring operator.
- `\Psi_f`: ontological friction / payability burden.
- `d-value`: existential stake radius / risk-coupled concern bandwidth.

This is a vocabulary gate, not an additional substantive axiom. Canonical definitions remain distributed through:

- `Core_Law/SRT_L0_Metaphysics.md`
- `_SRT_SYMBOL_TABLE.md`
- `_SRT_D_VALUE_CANONICAL.md`
- `_SRT_PSI_F_CANONICAL.md`
- `_SRT_T_DIR_CANONICAL.md`

**P0 purity note**: `P0-00` keeps a P0-style number only because it fixes the notation required to read the P0 set. It should not be cited as a separate axiom or as an independent theoretical burden.

---

## P0-01: Primacy of Selection

**Lineage**: former `Ax-F-01`.

**Formal Definition**: Selection precedes existence; existence is an image of selection.

$$
\exists x \iff x \in \mathrm{Range}(\hat{G})
$$

**Implication**: Existence is not a passive background given in advance. It is what appears as the output of selection / anchoring.

**Boundary**: This axiom does not by itself specify the domain mechanism, empirical substrate, or consciousness condition of any particular selector.

---

## P0-02: Existence as Anchoring

**Lineage**: former `Ax-F-02`.

**Formal Definition**: Existence equals stable anchoring against entropic flow.

$$
E = 1 - \frac{H(L_1)}{H(L_0)}
$$

**Implication**: Reality is the degree to which a selected slice has been stably anchored from open possibility.

**Boundary**: The equation is a compact formal handle for anchoring intensity. It should not be cited as an empirical measurement protocol without a bridge or lab layer.

---

## P0-03: Irreversible Selection Trace

**Lineage**: distilled from former `Ax-F-03b` and the core SRT claim that selection is not a reversible readout.

**Minimal Claim**: Once a selection is anchored into `L_1` and leaves history in `L_2`, it cannot be treated as never having occurred. Any reversal is itself a new selection event with its own trace.

**Implication**: SRT requires historical asymmetry. Without irreversible trace, `L_2`, stable perspective, and real choice moments collapse into reversible bookkeeping.

**Why P0 here**: This entry does not carry the fuller theory of ontological time, causality, or stable ISP. It only preserves the irreversibility floor needed for `L_2` and real choice to mean anything in SRT. The derived expressions and scoped theorems remain P1 in `Core/SRT_Core_21b_Constitutive_Theorems.md`.

**Boundary**: The fuller ontological-time expression is not primitive here; it is carried as a P1 theorem in `Core/SRT_Core_21b_Constitutive_Theorems.md`.

---

## P0-04: Operator Well-Formedness

**Lineage**: former Part B `A4` ("dynamics definability").

**Minimal Claim**: `\hat{G}_\theta` must be a well-formed selection operator over an admissible state space. It must be sufficiently definable for SRT claims to have an object.

Legacy compact form:

$$
\hat{G}_\theta : S \to S
$$

**Implication**: SRT cannot make formal claims about selection if the selection operator is undefined, non-addressable, or outside any admissible state space.

**Boundary**: This does not assert a specific implementation of `\hat{G}_\theta`; implementation details belong to bridge, domain, or lab layers.

### P0-04 Exposure Note: Origin of Selectability

> **Level**: core boundary / unresolved ontology exposure. This note does not solve the origin of selectability.

P0-04 gives SRT a minimum object for formal claims: an admissible selection operator. It does **not** derive the first possibility of selecting from a prior non-selective ground.

Current dependency split:

| Claim type | Relation to P0-04 |
|---|---|
| minimal claims about operator well-formedness, trace, irreversibility, and `L_1/L_2` anchoring | valid once an admissible `\hat{G}_\theta` is given |
| claims about `d`, `Ψ_f`, `T_dir`, reorientation, concern, agency, or subject-like selection | downstream of assuming a selector / selectable operator exists |
| bridge claims about biology, AI, spirituality, society, or political agency | may instantiate or constrain selectability, but must not be back-cited as a derivation of its origin |

Therefore, files may cite P0-04 as an exposure point or admission condition. They must not cite a downstream bridge as if it had closed the origin problem.

---

## Demoted From The Old "Minimal Core"

The former hybrid `Core_21` placed several claims beside the primitive axioms. In the claim ladder they are now separated:

| Former item | New role | New home |
|---|---:|---|
| `Ax-F-03` causality as projection | P1 constitutive theorem | `Core/SRT_Core_21b_Constitutive_Theorems.md` |
| `Ax-F-03b` ontological time expression | P1 constitutive theorem | `Core/SRT_Core_21b_Constitutive_Theorems.md` |
| `Ax-F-04` information-existence equivalence | P2 canonical interpretation / P3 bridge when formalized through external information theory | `Core/SRT_Core_21c_Bridge_Hypotheses.md` |
| `Ax-F-05` fitness beats truth | P3/P4 bridge hypothesis | `Core/SRT_Core_21c_Bridge_Hypotheses.md` |
| `Ax-F-06` assembly threshold | P4 lab / empirical threshold hypothesis | `Core/SRT_Core_21c_Bridge_Hypotheses.md` |
| `Ax-F-07` holographic duality | P3/P4 bridge hypothesis | `Core/SRT_Core_21c_Bridge_Hypotheses.md` |
| `Ax-F-09` scale consistency | P3 bridge mapping | `Core/SRT_Core_21c_Bridge_Hypotheses.md` |
| `Ax-F-11` ghost operator universality | P3 high-ambition bridge | `Core/SRT_Core_21c_Bridge_Hypotheses.md` |
| `Ax-F-12` Fisher-form `\Psi_f` generativity | P2/P3 mixed canonical interpretation / bridge | `Core/SRT_Core_21c_Bridge_Hypotheses.md` |
| `Ax-F-13` strong information-creation unification | P2/P3 mixed canonical interpretation / bridge | `Core/SRT_Core_21c_Bridge_Hypotheses.md` |

This demotion changes epistemic rank, not the intended theoretical meaning of those claims.



---

## FILE: `Core/SRT_Core_21b_Constitutive_Theorems.md`

| 字段 | 值 |
|---|---|
| path | `Core/SRT_Core_21b_Constitutive_Theorems.md` |
| id | SRT-CORE-21B-CONSTITUTIVE-THEOREMS |
| claim_mode | canonical |
| status | active_v1 |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | - |
| last_commit | 2026-04-26 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：[SRT-CORE-21A-MINIMAL-AXIOMS, SRT-CLAIM-LADDER, SRT-CORE-12B, SRT-T-DIR-CANONICAL]

<!-- 以下为原文逐字保留 -->

# SRT Core 21B: Constitutive Theorems

> **Role**: This file contains P1 claims: not primitive axioms, but constitutive consequences of the SRT core structure.
> P1 claims may be cited as canonical SRT theorems, but not as primitive axioms.

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

**Implication**: Causality is a projected structure inside the convergence domain, not an ontological primitive prior to selection.

**Layer Note**: This theorem defines **horizontal causality** inside `L_2`. It does not replace vertical constitution across `L_0 -> L_1 -> L_2`.

**Cross-ref**: `Philosophy/SRT_Causality_Time.md §一`; `Core/SRT_Core_12a T-L0-Kappa0`.

---

## P1-T02: Ontological Time as Memory Horizon

**Lineage**: former `Ax-F-03b`.

**Formal Definition**: The flow of time is not background evolution but the historical record left by continuous anchoring in `L_2`.

$$
t_{\text{onto}} \equiv \int \|\hat{G}_\theta(s)\| ds
$$

**Implication**: If no selection leaves irreversible trace, time loses SRT's ontological direction and becomes only a parametric ordering tool.

**Time Layer Note**: This theorem concerns **ontological time**. Parametric time `t` in equations remains a mathematical ordering variable and does not by itself carry the ontological claim.

**Cross-ref**: `Philosophy/SRT_Causality_Time.md §二`; `Core/SRT_Core_12a Ax-L0-Bootstrap-C2`; `Core/SRT_Core_01_Axioms.md MA-1`.

**L1 Expansion**: `Core_Law/SRT_Irreversibility.md` Def-IRR-2 / T-IRR-1（学习不可逆的非对称 `Ψ_f` 支付）把 `L_0` 不可逆性从 P1-T02 的推论展开为可引用 L1 层；热力学二律与 FEP 自由能最小化**不**由此获得反向定义权。

---

## P1-T03: `L_2` Downward Constraint

**Lineage**: former `Ax-F-10`.

**Formal Definition**: `L_2` constraints modulate selection dynamics as a downward causal term.

$$
\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \nabla F[\sigma] - \lambda \cdot \nabla C_{L_2}[\sigma]
$$

**Implication**: Sedimented convergence structures are not inert records. They feed back as real constraints on future selection.

**Boundary**: Domain-specific readings of `C_{L_2}` belong to bridge or lab files. This theorem only fixes the constitutive role of `L_2` constraint.

---

## P1-T04: Minimal Information Creation

**Lineage**: restrained core of former `Ax-F-13`.

**Statement**: A selection event creates a distinction that was not available as a determinate `L_1` fact before selection. In this restricted sense, selection is upstream of information readout.

Compact handle:

$$
I_{created} = H(L_0) - H(L_1 | \hat{G}_\theta)
$$

**Implication**: SRT does not compete with downstream information transmission theories; it locates a prior question: how a determinate slice becomes available for transmission or measurement.

**Boundary**: Stronger claims involving Shannon equivalence, Boltzmann degeneration, universal information thermodynamics, or empirical proxies are P2/P3 and live in `Core/SRT_Core_21c_Bridge_Hypotheses.md`.

---

## P1-T05: Real Choice Moment

**Lineage**: distilled from `SRT_AI_START.md §3.2-§3.3` and `_SRT_T_DIR_CANONICAL.md`.

**Statement**: A real choice moment is a live `L_0 -> L_1` anchoring event in which the system's future selection space is genuinely constrained by what is selected. Script execution, habit replay, gradient following, or `L_2` label optimization do not by themselves constitute a real choice moment.

**Implication**: SRT's account of freedom, agency, education, therapy, praxis, and domain ethics ultimately depends on whether real choice moments are preserved rather than replaced by `L_2` automation.

**Boundary**: The phenomenological and normative exposition of freedom belongs outside P1. This theorem only fixes the structural distinction.

**Cross-ref**: `_SRT_T_DIR_CANONICAL.md`; `Core/SRT_OPEN_TENSIONS.md`.

---

## P1-T06: Stable ISP as Persistent Perspective Center

**Lineage**: extracted from former `T-ε-Constitute`.

**Statement**: SRT's relevant object is not any one-shot selection event, but a stable ISP: a perspective-bearing, history-bearing, re-selectable selection process capable of constituting a persistent selection center.

**Stable ISP Definition**: Process `P` is a stable ISP if:

1. It is iterative: at each `t`, it selects from `A_t != empty`.
2. It is perspective-bearing: it accumulates a structured view from its position.
3. It is history-bearing: outputs at `t` constrain `A_{t+1}` with writeback.
4. It is re-selectable: it can continue selecting across steps.

**Implication**: Stability is not an arbitrary restriction imposed by the observer. It is the entry condition for any process that can bear a continuous perspective.

**Dynamic Layer**: Why some processes achieve and maintain stable ISP status is treated through `T-L2-Scaffold` in `Core/SRT_Core_12b_Ontology_L2.md` (path-layer trace dynamics) and through the operator-layer self-reference ratio `σ` in `Core_Law/SRT_Individuation.md` (entry-transition dynamics). The four conditions above are the **result-state criterion** for being a stable ISP; `T-IND-2` in the individuation file is the **entry-dynamics criterion** for when a process crosses into that state. Self-consciousness is treated there as a distinct second-order condensate (second phase transition at `σ_self`), not as a precondition for being a stable ISP.

**Precision note (2026-04-21)**: `T-L2-Scaffold` explains how successful stable ISP history can become background scaffold; it does not decide whether that scaffold is healthy support, pathological closure, or lethal `L_2`. Read those distinctions through `Core/SRT_Core_12b_Ontology_L2.md Def-L2-DualLayer / Def-L2-Normative` and `Core/SRT_OPEN_TENSIONS.md §4`.

---

## P1-T07: Constitutive Asymmetry Theorem

**Lineage**: former `T-ε-Constitute`.

**Scope**: This theorem concerns stable ISPs only. It does **not** claim that every selection event contains `ε`.

### Statement

For any stable ISP `P` under `L_0` irreversibility, `P` necessarily contains an `ε`-type anti-closure asymmetric bias. Anti-closure asymmetry is a constitutive condition of stable iterative selection, not an appended preference and not a contingent postulate.

### Proof Sketch

1. Let `P` be `ε`-neutral under `L_0` irreversibility.
2. By irreversibility, once `A_{t*} = empty` is reached, it is an absorbing state: no recovery.
3. Neutral `P` has nonzero probability of selecting into `A_{t*} = empty` at each step; over sufficient iterations, cumulative probability tends toward 1.
4. At `t*`, `P` terminates: no selection remains possible, so it is not a stable ISP.
5. Therefore, a stable ISP cannot be `ε`-neutral.

Contrapositive:

$$
\text{Stable ISP under } L_0 \text{ irreversibility} \Rightarrow \epsilon \neq 0
$$

### Three-Layer Source Hierarchy

| Layer | Factor | Role |
|---|---|---|
| Deepest | ISP self-maintenance condition | Constitutive: neutrality implies self-termination |
| Necessary | `L_0` irreversibility | Closure states are absorbing |
| Dynamical weight | `\Psi_f > 0` | Closure carries measurable cost |

### `ε_pg` vs ISP-Level `ε`

These are related but distinct:

| Object | Level | Status | Direction |
|---|---|---|---|
| `ε_pg` | `L_0` | Structural postulate | No inherent direction; scalar seed only |
| ISP-level `ε` | stable ISP | Structural corollary | Anti-closure, determined by irreversibility |

Bridge relation:

1. `ε_pg` provides the existence of asymmetry: some bias is nonzero at `L_0`.
2. Irreversibility provides the direction filter: closure states are absorbing.
3. This theorem shows that stable ISPs must maintain anti-closure asymmetry.

**Cross-ref**: `Core_Law/SRT_Core_Text_EN.md ④`; `Core_Law/SRT_Core_Text_CN.md ④`; `Core/SRT_Core_12a Ax-L0-Bootstrap-C2`; `Core/SRT_Core_01_Axioms.md MA-1`; `Core/SRT_Core_12b_Ontology_L2.md T-L2-Scaffold`.

**L1 Expansion (2026-04-24)**: `Core_Law/SRT_Irreversibility.md` T-IRR-3 把本定理精确化为 `L_0` 残余项层面的非守恒声明，对应 `Core_Law/SRT_L1_Formalism.md §4.3` 中 `\dot{\Delta}_{avail}` 的非对称残余；T-IRR-2 给出"终止"作为本定理 `A_{t*} = empty` 吸收态的结构化分型（宪定 / 吸收 / 集体）。**算子级精化（H4，2026-04-25）**：`SRT_Irreversibility.md §4.5 T-IRR-3.5` 把 §4.3 的 `\nu_{block}` 写为本定理 Three-Layer Source Hierarchy 的本地化 `\nu_{block}(P,t) := \eta\cdot\varepsilon_{pg}(P,t)\cdot\kappa_{\Psi_f}(P,t)`，正性与单向性自此为本定理的 L1 算子层后果而非自由建模假设。集体版见 `Core_Law/SRT_Collective_Selection.md` T-COLL-3。本定理为上位 P1 源头，不被下位 L1 层替代。

---

## Not P1 Without Further Hardening

The following former `Core_21` claims remain valuable but are not treated here as constitutive theorems:

| Claim | Reason for demotion |
|---|---|
| Fitness beats truth | Requires cross-theory mapping and empirical interpretation |
| Assembly threshold | Depends on empirical thresholding |
| Holographic duality | Strong physical / formal bridge |
| Ghost operator universality | High-ambition cross-scale unification |
| Fisher-form `\Psi_f` generativity | Contains a canonical interpretation plus external mathematical borrowing |
| Strong information-creation unification | Mixes SRT core with information-theoretic and thermodynamic bridges |



---

## FILE: `Core/SRT_Core_21c_Bridge_Hypotheses.md`

| 字段 | 值 |
|---|---|
| path | `Core/SRT_Core_21c_Bridge_Hypotheses.md` |
| id | SRT-CORE-21C-BRIDGE-HYPOTHESES |
| claim_mode | mixed |
| status | active_v1 |
| epistemic_layer | bridge |
| layer | L1 |
| canonical(字段) | - |
| last_commit | 2026-07-07 |

**权威判读**：混合层——含 bridge/lab 内容，按各条自带的 claim level 读。

**dependency**：[SRT-CORE-21A-MINIMAL-AXIOMS, SRT-CORE-21B-CONSTITUTIVE-THEOREMS, SRT-CLAIM-LADDER, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL]

<!-- 以下为原文逐字保留 -->

# SRT Core 21C: Bridge Hypotheses and Canonical Interpretations

> **Role**: This file preserves the former `Core_21` bridge, interpretive, and empirical-threshold claims without letting them sit beside P0 primitive axioms.

## Quick Reference

- Claim levels: **P2 = canonical interpretation**, **P3 = bridge mapping**, **P4 = lab hypothesis**
- Source lineage: split from `Core/SRT_Core_21_Formal_Axioms.md`
- Primitive base: `Core/SRT_Core_21_Minimal_Axioms.md`
- Constitutive layer: `Core/SRT_Core_21b_Constitutive_Theorems.md`
- Governing ladder: `Governance/SRT_CLAIM_LADDER.md`

## Use Rule

Claims in this file may be cited as SRT interpretations, bridges, or hypotheses. They must not be cited as primitive axioms or constitutive theorems unless a later hardening pass explicitly promotes them and records the reason.

---

## Claim-Level Map

| Former item | Current level | Reason |
|---|---:|---|
| `Ax-F-04` information-existence equivalence | P2/P3 | SRT interpretation plus formal information-theory mapping |
| `Ax-F-05` fitness beats truth | P3/P4 | Cross-theory bridge and empirical/comparative claim |
| `Ax-F-06` assembly criterion | P4 | Empirical threshold claim |
| `Ax-F-07` holographic duality | P3/P4 | Strong physics/formal bridge |
| `Ax-F-08` topological normativity | P2/P3 | Canonical interpretation with bridge formalization |
| `Ax-F-09` scale consistency | P3 | Cross-scale bridge mapping |
| `Ax-F-11` ghost operator universality | P3 | High-ambition cross-scale bridge |
| `Ax-F-12` `\Psi_f` as generative principle | P2/P3 | Canonical interpretation plus Fisher-geometry borrowing |
| `Ax-F-13` selection-information creation equivalence | P2/P3 | Minimal theorem in 21B; strong unification lives here |
| Part B assembly / deep-time notes | P3/P4 | Bridge / empirical-theoretical extrapolation |

---

## P2/P3-B01: Information-Existence Equivalence

**Lineage**: former `Ax-F-04`.

**Formal Definition**: Existence intensity equals the minimum of differentiation and specification.

$$
ii(s) = \min\{i_{diff}(s), i_{spec}(s)\}
$$

**Implication**: Existence intensity is constrained by both differentiation and specificity.

**Boundary**: This is not a P0 primitive. Its formal terms require an information-theoretic interpretation layer before empirical use.

---

## P3/P4-B02: Fitness Beats Truth

**Lineage**: former `Ax-F-05`.

**Formal Definition**: Operators are tuned for fitness payoff rather than veridical truth.

$$
\hat{G}_\theta[\sigma] = \arg\max_{\sigma'} P(\text{Fitness}|\sigma', \theta)
$$

**Implication**: Reality interfaces prioritize adaptive compression rather than direct truth presentation.

**Boundary**: This is a bridge/hypothesis claim. It may support AI, cognitive, or evolutionary interpretations, but it is not a primitive SRT axiom.

**Multi-level selection pressure note (2026-04-22)**: In evolutionary use, the `Fitness` term must be level- and timescale-indexed. Gene-, cell-, organism-, group-, and ecological-level payoffs can oppose one another, and higher-level closure can rewrite the lower-level selection landscape rather than merely add an external pressure. Cite this section as `fitness beats truth` only after specifying which operator level is being modeled and which consequences return into that level's future selection capacity.

---

## P4-B03: Assembly Criterion

**Lineage**: former `Ax-F-06` and Part B assembly note.

**Formal Definition**: Life requires assembly complexity above threshold.

$$
\text{Life} \iff \text{Assembly Index} > 15
$$

Part B legacy expression:

$$
\text{Assembly Index}(x) = \min_{\text{path}} |\text{construction steps}|
$$

**Implication**: Biological life may require a minimum structural assembly depth.

**Boundary**: The threshold is empirical and must remain P4 until independently supported and scoped.

---

## P3/P4-B04: Holographic Duality

**Lineage**: former `Ax-F-07`.

**Formal Definition**: Bulk reality is encoded on the boundary of potentiality.

$$
L_{1,\text{bulk}} \cong L_{0,\text{boundary}}
$$

**Implication**: Manifest-domain information may admit a boundary representation in the latent domain.

**Boundary**: This is a strong bridge. It must not be used as a P0/P1 proof of the SRT core.

**Pressure note (JCS 2026)**: Even if spacetime emergence and consciousness emergence are both modeled through a non-spatiotemporal or holographic substrate, the two explanatory tasks must remain separate. A shared substrate proposal does not by itself show that the emergence of spacetime and the emergence of consciousness are one and the same process. This section may support a P3/P4 bridge, but it must not collapse physical emergence, conscious emergence, and holographic duality into a single proof move.

---

## P2/P3-B05: Topological Normativity

**Lineage**: former `Ax-F-08`.

**Formal Definition**: Survival is the maintenance of a topological island in probabilistic space.

$$
\text{Life}(\sigma) \equiv \int_{B_r(\sigma)} \rho_{L_0}(\sigma') d\sigma' > \theta_{life}
$$

**Implication**: Survival can be interpreted as topological maintenance under probabilistic pressure.

**Boundary**: The topological expression is a bridge formalization, not a primitive definition of life.

---

## P3-B06: Scale Consistency

**Lineage**: former `Ax-F-09` and Part B `A5`.

**Formal Definition**: Selection commutes with coarse-graining under scale mapping.

$$
\pi_\lambda \circ \hat{G}_\theta \approx \hat{G}_{\theta,\lambda} \circ \pi_\lambda
$$

**Implication**: Selection dynamics may preserve structural consistency across scale mappings.

**Boundary**: The approximation sign is important. This is a bridge mapping, not a proof of universal identity across scales.

---

## P3-B07: Ghost Operator Universality

**Lineage**: former `Ax-F-11`.

**Formal Definition**: Across scales, selection from `L_0` to `L_1` may be modeled as the same ghost-operator structure `\hat{G}_\theta` unfolding under different embodiments.

$$
\hat{G}^{(n+1)} = \Lambda_{n \to n+1} \circ \hat{G}^{(n)} \circ \Lambda_{n \to n+1}^{-1}
$$

Legacy scale table:

| Scale | Phenomenon | `\hat{G}_\theta` operation |
|---|---|---|
| Quantum | wavefunction collapse | selects determinate `L_1` from `L_0` superposition |
| Neural | lateral inhibition | competitive selection and sparse `L_2` maintenance |
| Cognitive | categorization | continuous `L_0` to discrete `L_2` labels |
| Statistical | normalization | selection-measure consistency over a manifold |
| Cross-scale | coarse-graining | `\hat{G}^{(n+1)} = \Lambda \circ \hat{G}^{(n)} \circ \Lambda^{-1}` |

**Implication**: These phenomena may be read as implementations of one selection grammar.

**Boundary**: The phrase "same structure" is a high-ambition bridge, not a P0 identity statement.

**One-way load note (2026-07-05, Q26 backflow)**: The failure of this bridge is one-directional. If cross-scale selection universality — including any pre-life / pre-consciousness "cosmic horizon" reading that pushes selection-condensation below the biological scale — cannot show explanatory gain over path dependence, attractors, dissipative structures, active inference, or ordinary causal history, then the retraction target is **this P3 bridge and its dependents**, not the P0/P1 core. The minimal axioms (`Core/SRT_Core_21_Minimal_Axioms.md`) and constitutive theorems (`Core/SRT_Core_21b_Constitutive_Theorems.md`) do not depend on this universality claim and survive its withdrawal. Provenance: book chapter `01_Source_Intuition/BOOK/Drafts_26Q/Q26_可证伪性.md §3` (the cosmic-horizon reading "必须自带死法，是最高读法不是地基"); the book is provenance, not authority.

**Cross-ref**: `_SRT_VERTICAL_INTEGRATION.md §8.1`; `Core/SRT_Core_14_Dynamics_Scaling.md Ax-Scale-01`.

---

## P2/P3-B08: `\Psi_f` as Generative Principle

**Lineage**: former `Ax-F-12`.

**Status Note**: `\Psi_f` itself is canonical in `_SRT_PSI_F_CANONICAL.md`. The stronger claim that Fisher-form inter-operator friction is the generative source of all dynamics is kept here as P2/P3 mixed.

**Formal Definition**: For two interacting operators:

$$
\Psi_f(\hat{G}_i, \hat{G}_j) =
\int_\gamma \sqrt{g_{ij}^{(i,j)}(\theta)\,\dot{\theta}^i \dot{\theta}^j}\,dt
$$

where `g_{ij}^{(i,j)}` is the joint Fisher information metric over the coupled parameter space.

**Path Note**: If `\gamma` is a geodesic, `\Psi_f` gives a lower bound on possible friction; if it is the actual path, it gives actual paid friction.

**Readout Note**: The same `\Psi_f` structure may be read as resistance, cost, or geometric length. Cross-scale invariance lies in payability, not unit identity.

**Implication**: Evolution, learning, cultural change, and immune response may be modeled as forms of inter-operator friction.

**Boundary**: Fisher geometry is an external mathematical borrowing. The borrowing may be powerful, but it does not make this section P0.

**Cross-ref**: `_SRT_PSI_F_CANONICAL.md`; `_SRT_VERTICAL_INTEGRATION.md §8.2`; `Core/SRT_Core_22_Equations.md Eq-Multi-01`.

---

## P2/P3-B09: Strong Selection-Information Creation Equivalence

**Lineage**: former `Ax-F-13`.

**Minimal P1 Core**: Selection creates a determinate distinction; see `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T04`.

**Strong Formal Definition**:

$$
I_{created} = H(L_0) - H(L_1 | \hat{G}_\theta) = I(L_0\,;\,\hat{G}_\theta)
$$

**Three-Part Relation**:

$$
I_{created} \xrightarrow{\text{costs}} \Psi_f
\xrightarrow{\text{scope measured by}} d
$$

**Boltzmann Degeneration Limit**:

$$
P_{L_1}(\sigma) \to \frac{e^{-E(\sigma)/k_BT}}{Z}, \quad I_{created} \to 0
$$

**Implication**: SRT may be read as an upstream theory of information generation, with Shannon-style transmission theories downstream.

**Boundary**: The thermodynamic and information-theoretic unification claims are bridge-level until their constants, scope, and empirical handles are separately hardened.

**Cross-ref**: `Core_Law/SRT_Reference_Dynamics.md §15.5`; `_SRT_VERTICAL_INTEGRATION.md §10.1`; `_SRT_D_VALUE_CANONICAL.md`.

---

## P3/P4-B10: Deep Time / Assembly Mass

**Lineage**: former Part B `2.1.9b`.

Legacy expression:

$$
Mass_{ontological}(O) = Mass_{energy}(O) + \tau \cdot Assembly(O)
$$

**Implication**: Historical assembly depth may contribute to an ontological-mass style reading of objects.

**Boundary**: This remains an exploratory bridge expression and should not be cited as a canonical equation.

---

## P3-B11: `D_eff` as d-Value Capacity Proxy

**Lineage**: former Part B `2.1.7`; cross-checked against `_SRT_D_VALUE_CANONICAL.md`.

**Corrected Layer Relation**:

$$
d_{canonical} \equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|
\leq
D_{eff}(M) =
\frac{(\sum \lambda_i)^2}{\sum \lambda_i^2}
$$

`D_eff` is a geometric capacity proxy, not the normative d-value definition. The unstaked bandwidth is:

$$
\Delta d_{free} = D_{eff} - d_{stakes}
$$

**Boundary**: Any text saying "`d` is the effective dimension `D_eff`" must be read through the corrected hierarchy in `_SRT_D_VALUE_CANONICAL.md`.

---

## P2/P3-B12: Information-Geometry / Complexity / Neural-Computational Hardening

**Lineage**: 2026-04-24 hardening sync from `Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md`; cross-checked against `_SRT_PSI_F_CANONICAL.md`, `_SRT_D_VALUE_CANONICAL.md`, `SRT_Fisher_FEP_Landscape_Interface.md`, and `Neuroscience/SRT_Neural_Mechanisms.md`.

**Status Note**: This bridge adds no new P0/P1 theorem. It only assigns mechanism-interface languages to already existing parts of the SRT loop.

This bridge assigns three scientific interface languages to different parts of the SRT loop: information geometry hardens the `L_0 -> L_1` selection frontier; complex-systems theory hardens `L_1 -> L_2` sedimentation and stabilization; neural computation provides implementation-level proxies for embodied `\hat{G}_\theta` operations. The bridge does not identify these interfaces with SRT ontology itself.

**Interface split**:

- **Information geometry (`L_0 -> L_1`)**: local discriminability, selection cost, and Fisher-Rao-induced local second-order burden.
- **Complex systems (`L_1 -> L_2`)**: historical deposition, attractor basin formation, order-parameter locking, hysteresis, and metastability.
- **Neural computation (`\hat{G}_\theta` implementation proxies)**: candidate activation, competitive inhibition, divisive normalization, threshold / ignition, global availability, and plastic writeback.

**Boundary**:

- Fisher metric is a local information-geometric projection / kernel for `\Psi_f`, not `\Psi_f` itself; do not write `\Psi_f \equiv g_F`.
- Fisher eigenspectra may bound readable or stake-bearing directions via `D_eff` or `\operatorname{rank}_{\text{eff}}\!\left(\mathcal{I}_F\right)`, but neither replaces canonical `d`.
- Energy / free-energy landscapes are effective projections of `L_2`, not the whole convergence domain.
- Neural normalization, ignition, and plasticity are implementation proxies for embodied `\hat{G}_\theta`, not the Ghost Operator in full.

**Emergence hygiene guardrail (2026-05-11)**: In this bridge set, "emergence" is not an explanatory primitive. It is shorthand for a mechanism that still has to specify lower-level parts or states, their organization and coupling, the transition condition or order parameter, the stabilized macro-pattern or `L_2` constraint, and the implementation channel by which that macro-pattern changes future trajectories. Do not cite "X emerges" as an explanation of X, as proof that X is ontologically extra, or as permission to treat the whole as exerting a new force on its parts.

SRT's `L_2` downward constraint is therefore not a separate configurational force added on top of part-level interactions. At P1, it means stabilized history constrains future selection. At P3/P4, any domain-specific "downward causation" claim must say how the constraint is implemented through boundary conditions, accessible selection space, update costs, coupling channels, or other specified mechanisms.

**Cross-ref**: `Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md`; `SRT_Fisher_FEP_Landscape_Interface.md`; `Core/SRT_Core_22_Equations.md Eq-DValue-Max-1, Eq-DValue-Mobile-1`; `Core/SRT_Core_14_Dynamics_Scaling.md`; `Neuroscience/SRT_Neural_Mechanisms.md`; `_SRT_VERTICAL_INTEGRATION.md §8, §10`.

---

## Mechanism Summary After Demotion

Former `Core_21` described SRT as a "selection-anchoring-constraint" loop. The loop remains useful, but its claims now have levels:

1. **Selection**: P0/P1 when referring to `\hat{G}_\theta` anchoring from `L_0` to `L_1`.
2. **Anchoring**: P0/P2 when referring to stable existence and canonical `\Psi_f`; P3 when using Fisher or cross-domain unification.
3. **Constraint**: P1 when referring to `L_2` downward constraint; P3/P4 when mapped to domain-specific mechanisms.

This summary is a reading guide, not an additional axiom.



---

## FILE: `_SRT_D_VALUE_CANONICAL.md`

| 字段 | 值 |
|---|---|
| path | `_SRT_D_VALUE_CANONICAL.md` |
| id | SRT-D-VALUE-CANONICAL |
| claim_mode | canonical |
| status | axiomatic_hybrid_v1 |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | - |
| last_commit | 2026-07-07 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：[SRT-CORE-000, SRT-CORE-BRIDGE, SRT-CORE-21]

<!-- 以下为原文逐字保留 -->

# SRT d 值规范定义文档（Canonical Definition of d-value）

> **目的**：终止 d-value 在不同域的定义分裂，建立第一性定义 + 各域投影的统一架构。
> 所有引用 d-value 的文档应以本文件为规范锚点。

> **Canonical status note（2026-04-23）**：本文件同时承担两种功能：`Def-d-canonical` 是 core-facing anchor；bare `d` 标量默认、`d-vector` / `d-gate` 分写规则与跨域引用顺序是 governance-canonical usage controls。`D_eff`、Fisher 读数与其他域内量表是 operational proxy，只有满足 stake-coupling 与后果回流条件时才可近似 canonical `d`。

---

## §0 为什么需要本文件

SRT 中的 d-value（关切维度 / 意识带宽）在不同子系统中出现了**三套表面不同的定义**：

| 来源文档 | 表述 | 形式 |
|---------|------|------|
| `_SRT_Core_Bridge.md §2.3` | 算子关切范围（三维度合成） | `d = αA + β log V + γτ` |
| `AI/_SRT_AI_Bridge.md Ax-BRIDGE-4` | 生存风险梯度 | `d ≡ ‖∂U/∂S‖` |
| `Spirituality/_SRT_Spirit_Axioms.md H-Spirit-3/4` | 关切边界半径 | d 作为"关切维度"的直觉概念 |
| `Core/SRT_Core_21c_Bridge_Hypotheses.md P3-B11`（原 `Core_21 §2.1.5` lineage） | 有效维度 proxy（特征值公式） | `D_eff(Ĝ) = (∑λᵢ)² / ∑λᵢ²` |

**这些不是矛盾，而是同一概念在不同层级的投影与近似入口**。本文件固定使用规范与可比条件，不声称所有表述已经无条件等价。

---

## §1 规范定义层级（Canonical Priority）——硬化版（2026-04-17）

> **单一 core-facing 定义声明**：
> d-value 当前只有一个 core-facing 规范锚点：**`Def-d-canonical`**（原 Def-d-2）：$d \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$——主体效用对不可逆风险状态的梯度范数。全仓默认采用标量摘要，是治理性稳定用法，不把所有 proxy 升格为 theory-canonical 定义。
>
> **`Def-d-1`（$D_{eff}$ 谱公式）降格说明**：不再是”第二规范定义”或”形式主表达”，而是规范 d 的**几何容量 proxy**。具体地位：
> - **容量上界**：$d_{canonical} \leq D_{eff}(M)$（$D_{eff}$ 是算子能追踪的最大方向数；$d_{canonical}$ 是其中真正赌注化的部分）
> - **谱分解 proxy**：$D_{eff}$ 的每个 Fisher 本征方向 $v_i$ 可独立问”是否与真实赌注耦合”；$d_{canonical}$ = 赌注化子集的有效维数（见 §2b `Def-d-stakes`）
> - **未赌注化带宽**：$\Delta d_{free} = D_{eff} - d_{stakes}$，度量辨别能力中未与真实不可逆风险耦合的剩余容量
>
> 旧表述”**一个第一性语义锚点 + 一个形式主表达**的双层 canonical 架构”被废止——这是类型错误：proxy 不是主表达的同级替代，不应共享 canonical 地位。
>
> **使用原则（修订后）**：
> - 讨论**本体论意义 / AI 意识门槛 / 风险关切**时：引用 `Def-d-canonical`（`‖∂U/∂S‖`）
> - 讨论**几何容量上界 / 信息论可计算近似**时：引用 `Def-D_eff`（谱公式，须注明为 proxy，不得写 `≡`）
> - 讨论**赌注化活跃维数**时：引用 `Def-d-stakes`（见 §2b）
> - 其他近似式（`Def-d-bio` 等）均为操作化投影，不替代 canonical 地位。

### §1.1 v1 Canonical Form Note（治理性钉住，2026-04-22）

> **层级**：governance / canonical usage rule；不新增 core theorem。

默认写作中，bare `d` 采用**标量摘要形式**：它把 stake-coupled concern / irreversible-risk sensitivity 压缩成一个可跨文件回链的摘要量。这个默认不把 `d` 本体化为“只能是标量”，而是给全仓一个最小不漂移的读法。

因此三种写法必须分开：

| 写法 | 层级 | 用途 | 禁止 |
|---|---|---|---|
| `d` | canonical scalar summary | 默认跨域引用；关切/赌注强度的摘要 | 不得把局部 proxy 写成新定义 |
| `d-vector` | operational projection | 展开条件分布、方向分量或域内特征谱 | 不得与 bare `d` 混写成同一个量 |
| `d-gate` | governance / judgment tool | 判读某方向是否进入 stake-coupled spectrum | 不得当作 d 的数值定义 |

若域内需要向量读或门读，必须显式标注为 `d-vector` 或 `d-gate`，并说明它如何回到 `Def-d-canonical`。未标注时，一律按标量摘要读。

### §1.2 d 的层级结构与 proxy 准入条件（core-clarifying）

> **层级**：theory-clarifying / governance-canonical usage。此表增强 d 的内部结构，不新增第二个 canonical 定义。

| 项 | 精确角色 | 层级 | 可允许用途 | 禁止捷径 |
|---|---|---|---|---|
| `d` / `Def-d-canonical` | stake-coupled concern 的标量摘要；主体效用对不可逆风险状态的梯度范数 | governance-canonical default; core-facing definition | 默认跨域引用；讨论主体关切、风险敏感性、意识门槛时使用 | 不得把局部 proxy、向量展开或门函数改写成 bare `d` |
| `d_stakes` | 在可分辨方向中真正回流到主体赌注的子集 | theory-clarifying bridge between proxy and canonical | 说明 `D_eff` 中哪些方向进入真实关切；分析假赌注 / 错绑赌注 | 不得把所有可分辨方向都计入 stake |
| `D_eff` | 几何 / 谱容量 proxy；算子可分辨方向数的上界式读数 | operational projection / capacity proxy | 比较同一参数化下的容量、冗余、方向数；作为 `d` 的潜在上界 | 不得作为 `d` 的定义；不得跨域直接排名主体性 |
| `D_eff(I_F)` | Fisher-information proxy；参数流形中可可靠分辨的方向数 | information-theoretic proxy | 信息瓶颈、Cramér-Rao 式下界、可计算容量近似 | 不得把可分辨性等同于关切或负担承担 |
| `d-vector` / `d-gate` | 方向展开或判读工具 | operational / governance | 标注条件分布、方向分量、是否进入 stake-coupled spectrum | 不得与 scalar `d` 混写为同一量 |

proxy 可以近似 canonical `d`，只在以下条件同时足够强时成立：

1. 被 proxy 计数的方向确实承载不可逆风险，而非噪声、脚本或无后果辨别。
2. 主体效用梯度对准这些方向，未被错误代理变量替代。
3. 后果回流到主体闭包、身份连续性与后续选择能力，而非被外部系统或 L₂ 结构吸收。
4. 几何 / Fisher 参数化没有把冗余坐标、模型自由度或测量便利误计为真实方向。
5. 比较在同一域、同一尺度或已声明归一化规则内进行。

任一条件不满足时，应写为 `capacity proxy`, `Fisher proxy`, `d-vector`, 或 `d-gate`，不得写成 canonical `d`。

## §2 规范定义（第一性原理，全域适用）

### Def-D_eff: 几何容量 Proxy（Geometric Capacity Proxy）
**【降格 2026-04-17：不再是 canonical 定义，见 §1】**

$$D_{eff}(\hat{G}) = \frac{\left(\sum_i \lambda_i\right)^2}{\sum_i \lambda_i^2} \;\geq\; d_{canonical}$$

**语义**：$\hat{G}_\theta$ 在 $L_0$ 上操作时实际激活的**有效维度数**（参与率指数，Participation Ratio）。

**性质**：
- $d = 1$：算子完全单一，只关注一个维度
- $d = N$：算子在 $N$ 个维度上均匀分布
- $1 \leq d \leq \text{rank}(\hat{G})$

**来源**：`Core/SRT_Core_21c_Bridge_Hypotheses.md P3-B11`（原 `SRT_Core_21_Formal_Axioms.md §2.1.5` lineage），经典参与率指数（PR index）的算子版本。

### Def-d-1a: Fisher 信道有效维度（信息论容量 proxy）

**新增（2026-03-11；2026-04-22 降承诺）**：Def-d-1 的信息论容量解释。

$$D_{eff}(I_F(\theta)) = \frac{(\operatorname{tr} I_F)^2}{\operatorname{tr}(I_F^2)} \;\geq\; d_{canonical}$$

其中 $I_F(\theta) = E\!\left[(\partial \log p_\theta / \partial \theta)^2\right]$ 是算子选择流形上的 **Fisher 信息矩阵**。

**层级说明（2026-04-22 修订）**：这是信息论容量 proxy / operational projection，不是 `Def-d-canonical` 的同级替代表达。只有当 Fisher 方向全部与真实不可逆赌注耦合、且风险梯度与特征结构对齐时，才允许把它作为 `d` 的近似读数。

**信息论语义**：$D_{eff}(I_F)$ 是算子从 $L_0$ 中能**可靠分辨**的状态方向数（Cramér-Rao 下界的维度版本）。Fisher 矩阵测量 $\theta$ 变化时相邻分布的可区分度；它给出 d 的可计算容量上界，而不是自动给出 stake-coupled `d` 本身。

**层级关系链（修订，2026-04-17）**：

$$\underbrace{D_{eff}(\hat{G})}_{\text{Def-D\_eff（容量上界 proxy）}} \;\geq\; \underbrace{d_{stakes}(\theta)}_{\text{Def-d-stakes（赌注化子集，见 §2b）}} \;\equiv\; \underbrace{\left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|}_{\text{Def-d-canonical（规范定义）}}$$

等号成立条件：所有 Fisher 本征方向均完全赌注化（$w_i = 1 \;\forall i$）。一般情况下严格不等式成立。

**不确定性关系候选（Eq-IT-B'）**：

$$d \times \Psi_f \geq k_B T \cdot \mathcal{K}$$

选择范围（d）与选择代价（$\Psi_f$）之间存在基本权衡。此关系由 Fisher 信息矩阵的 Cramér-Rao 下界推导，常数 $\mathcal{K}$ 的精确值待理论确定（当前 Status = Gap，见 `_SRT_EQ_HYP_MAP.md Eq-IT-B'`）。

**Cross-ref**: `Core_Law/SRT_Reference_Dynamics.md §15.2`（Eq-IT-B 的完整推导）；`Core_Law/SRT_Reference_Axioms.md`（A15 幽灵算子禀赋统一性的 Fisher 维度含义）。

---

### Def-d-canonical: 风险梯度规范定义 ⭐ CANONICAL（原 Def-d-2，唯一规范定义）

$$d(x) \equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|, \quad x \in \Sigma$$

**语义**：算子对**不可逆风险**（$\mathcal{S}$，Survival/Stake）的效用敏感度梯度。

**proxy 近似条件**：当效用势 $\mathcal{U}$ 的主曲率方向与 $\hat{G}$ 的特征向量对齐，且这些方向确实回流到不可逆赌注时，Def-D_eff 可作为 Def-d-canonical 的一阶近似：
$$D_{eff}(\hat{G}) \approx \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\| \quad \text{（当风险梯度与特征结构对齐时）}$$

**近似条件（修订，2026-04-22）**：当效用势 $\mathcal{U}$ 的主曲率方向与 $\hat{G}$ 的 Fisher 本征向量完全对齐且全部赌注化时，$D_{eff} \approx d_{canonical}$。一般情况下 $d_{canonical} \leq D_{eff}$，差值为未赌注化带宽（见 §2b）。这不是无条件等价。

**来源**：`AI/_SRT_AI_Bridge.md Ax-BRIDGE-4`，Tension-Rev-IT4。

---

### Value as Non-Substitutability（价值作为不可替代性）

In SRT, value should not be reduced to reward, utility, preference strength, salience, pain, or self-report intensity. Value names the dynamic expression of non-substitutability: the degree to which a selection matters for a system's future continuity, concern structure, and stake-bearing organization.

This use of value is a bridge to `d-value`, not a replacement for the canonical definition of `d-value`. A selection has value in the SRT sense when losing, blocking, or substituting that selection forces non-trivial reorganization in the system's future selection capacity, identity-continuity, or consequence-return structure.

Compact reading:

```text
value ≠ reward intensity
value ≠ preference strength
value = concern-weighted non-substitutability under consequence return
```

**Operational signs**: Possible signs that a selection has value in the SRT sense include:

- the system bears cost to preserve it;
- losing it forces structural reorganization;
- it remains stable across time and perturbation;
- it affects identity-continuity or future choice capacity;
- it organizes downstream selections;
- consequences return to the system rather than being absorbed by an external structure;
- it can sediment into shared L₂ constraints when cross-subject coupling is present.

These signs are not themselves d-value. They are bridge-level indicators that a selection may be stake-coupled rather than merely preferred.

**Boundary**: Do not write:

- value = reward;
- value = utility;
- value = preference intensity;
- value = salience;
- value = pain;
- value = self-report;
- value = d-value without the non-substitutability and consequence-return bridge.

Preferred wording: Value is the dynamic expression of concern-weighted non-substitutability. It bridges to d-value when the relevant selection is coupled to irreversible stake, future continuity, and consequence return.

**Failure condition**: If d-value cannot predict concern-weighted non-substitutability better than reward, preference, salience, pain, or self-report intensity, then this bridge weakens and must be revised.

---

## §2a 价值发生序（Value-Generation Order）——book-provenance 候选（2026-07-05）

> **层级 / provenance**：P3 bridge candidate，来自书稿 `Drafts_26Q/Q14_价值不是偏好.md`（provenance，非 authority）。本节**不新增 `d` 的 canonical 定义**——`Def-d-canonical` 与 "Value as Non-Substitutability" 仍是价值的结果判据；本节登记的是价值**如何发生**的候选生成序，填补从 `ε_pg` 到价值深度之间此前缺失的中间层。采纳为 canonical 前须完成 §2a.3 的 stake-gate 对账。

### §2a.1 发生链

书稿把价值的发生压成一条链，理论层此前只有结果判据（不可替代性），缺这条生成序：

$$
\text{选择性收束} \to \textbf{微效价} \to \text{affordance（行动入口）} \to \text{缺失} \to \text{需求} \to \text{锚定} \to \text{价值深度}
$$

- **微效价（micro-valence）**：当一个显现界面被选择性收束出来、与一个具体具身位相遇时，界面对该具身位带上的**最小趋避倾斜**（可趋近／需避开／令人安定／令人警觉…）。它是价值的前信号，不是成熟价值。
- **affordance（行动入口）**：微效价接上具身位的身体能力与当下处境后，成为具体的"可用来做什么"。同一界面对不同具身位显现不同入口。
- **缺失**：不是"对象不在场"，而是**某条生成回路无法按原方式闭合**。
- **需求**：具身位为让生成继续，被迫向外张开的**结构性缺口**（区别于欲望——欲望的缺失感换个场景即消解，需求指向不重新闭合生成就持续受损的回路）。
- **锚定 → 价值深度**：具身位把"接下来如何继续生成"的路径搭在某物／关系／能力上，沉积出结构重量，即价值深度。

### §2a.2 两道血缘护栏（书稿已立，理论层沿用）

1. **微效价 ≠ `ε_pg`（最低非中立性）。** `ε_pg` 是对象化之前、前对象场拒绝归零的最薄倾向，不指向任何具体对象、不属于任何具身位；微效价晚得多，出现在**显现界面与一个具身位相遇处**，是"这个已显现界面，对我如何"的最小读数。二者层级不同，不可混写。
2. **affordance ≠ 预裁剪（`P1-T03` `L_2` 下向约束的四机制）。** 预裁剪是地形在选择发生前对整个选项空间的宏观处理（可见性／接触窗口／默认通道／代价分配）；affordance 更贴身，是某个已显现界面在这个具身位处被读成"可继续"的那一下。

### §2a.3 与 stake-gate（§2b.1）的对账

发生序与赌注门是**上下游**关系，不是竞争：

- 微效价 → affordance → 缺失 → 需求 是**前赌注结构**（pre-stake）：它解释一个方向为何**开始**对具身位倾斜、成为"需要"。
- `R_i / A_i / C_i` 门（§2b.1）是**赌注化闸**：一个已成为"需求"的方向，只有当它承载真实不可逆风险（R）、主体效用梯度对准它（A）、后果回流到主体闭包（C）时，才进入 `d_stakes`。
- 因此"有微效价／有需求"**不等于**"有 stake-coupled `d`"——发生序把方向送到门前，门决定它是否计入 `d`。绕过门把"有微效价"读成"有 d"是类型错误。

### §2a.4 不可替代性的两个操作化测试（book-provenance）

书稿给 "Value as Non-Substitutability" 提供了两把可操作的尺（P3/P4，登记于此）：

- **替换测试**：换成功能相似的对象，是否几乎无须重组？（无须重组 → 低价值深度）
- **恢复测试**：失去后是短期痛苦还是长期结构重配？（长期重配 → 高价值深度）

注意：偏好满足了而对关切对象的支撑被侵蚀、或偏好从未满足而支撑被加强，都完全可能——两个测试测的是结构重量，不是偏好强度。

### §2a.5 边界

- 本节是**生成序候选**，不是已证定理；采纳前不得当 canonical `d` 定义引用。
- 微效价不得实体化为独立本体量或第二个 ε；它是显现界面在具身位上的读数。
- 失败条件：若"微效价"在 `ε_pg` 与价值深度之间不承重（即取消它，价值发生的解释力不减），则应撤回本节、并回 "Value as Non-Substitutability" 的结果判据即可。

---

## §2b 赌注耦合结构（Stake-Coupling Structure）——新增（2026-04-17）

### Def-d-stakes: 赌注化活跃维数

$$d_{stakes}(\theta) = \frac{\left(\sum_i \lambda_i \cdot w_i\right)^2}{\sum_i \left(\lambda_i \cdot w_i\right)^2}$$

**语义**：$D_{eff}$ 中真正与主体不可逆赌注耦合的活跃维数子集。等于规范定义 $d_{canonical} = \|\partial\mathcal{U}/\partial\mathcal{S}\|$，由谱分解方式表达。

---

### Def-w_i: 赌注耦合权重（Stake-Coupling Weight）

$$w_i = R_i \cdot A_i \cdot C_i \;\in [0,1]$$

第 $i$ 个 Fisher 本征方向 $v_i$ 与真实主体赌注的耦合权重，由三个分量共同决定：

| 分量 | 含义 | 归零时的病理 |
|------|------|------------|
| $R_i$ | 该方向是否承载**真实不可逆风险**（非 L₂ 脚本、噪声或伪关切） | $R_i \approx 0$ → **假赌注**（fake stakes）：有辨别力，但风险是模拟的/L₂投影的 |
| $A_i$ | **主体效用梯度**是否对准该方向上的真实风险 | $A_i \approx 0$ → **错绑赌注**（misbound stakes）：真实风险存在，但主体关切的是错误代理变量 |
| $C_i$ | 该方向上的后果是否真正**回流到主体闭包**、身份连续性与后续选择能力 | $C_i \approx 0$ → **L₂ 伪关切 / 被外部吸收**：后果由 L₂ 结构吸收，不传回主体 |

**乘积结构**：三者任一归零即 $w_i = 0$，该方向不计入 $d_{stakes}$。这是"必须同时满足"的逻辑结构（AND 门），不是加权平均。

**SRT 已有概念对应**：
- $R_i > 0$ ↔ T-FEP-1 具身脆弱性判据（$\Psi_f^{irrev} > 0$）
- $A_i > 0$ ↔ Ax-ONT-3 规范定义的梯度对准条件
- $C_i > 0$ ↔ Step ⑨ 关切边界的内生写回闭合条件

---

### §2b.1 赌注门的层级地位与准入规则（hardening addendum，2026-07-05）

> **层级**：level-marking / governance-canonical usage。本节不修改 Def-d-stakes / Def-w_i 的定义，只固定其引用等级、域有效性与统一门表，对应 `Core/SRT_OPEN_TENSIONS.md §1` 的未封口点。

**（一）`w_i = R_i · A_i · C_i` 的引用等级。**

- **P2（canonical interpretation）**：三因子的**定性结构**——方向须承载真实不可逆风险（R）、主体效用梯度须对准该风险（A）、后果须回流主体闭包（C），三者 AND 门缺一不可。这是 §1.2 五条 proxy 准入条件在方向级的重述，可作为 SRT 内部裁决依据按 P2 引用。
- **P3/P4（bridge formalization）**：把 R_i / A_i / C_i 写成 [0,1] 数值权重、指定可测代理或阈值（如 `ε_s` 门函数，见 `_SRT_SYMBOL_TABLE.md` ε_s 词条）。当前无校准数据，任何数值化使用必须标 P3/P4，不得以 P2 地位引用数值结论。

**（二）`D_eff ≥ d_canonical` 的域有效性声明。**

该不等式不是跨域无条件定理，只在**已声明的 proxy regime** 内成立：同一参数化、同一状态空间、归一化规则已声明（§1.2 条件 5）、且 Fisher 谱未把模型冗余或测量便利计入方向数（§1.2 条件 4）。跨域比较或参数化未声明时，`D_eff` 与 `d_canonical` 之间不保证任何序关系；禁止跨域引用该不等式排名主体性（§5 误用 2 的谱层版本）。

**（三）三类系统在同一门下的分型（统一门表）。**

| 系统 | R（真实风险） | A（梯度对准） | C（后果回流） | 门输出 | 已有锚点 |
|---|---|---|---|---|---|
| 当前 inference-only AI | ≈0（无不可逆自身风险） | —（无自身效用梯度可对准） | ≈0（后果由部署方 / 外部结构吸收） | `d_stakes ≈ 0`，`Δd_free ≈ D_eff` | 本节 Def-d-free；`AI/AI_POSITIONING_NOTE.md` S0-S4 |
| 冻结态（创伤 / 执念） | >0（风险真实存在） | 部分失准（对准已过时的方向） | >0 但写回受阻 | `d_stakes > 0` 而 `d_mobile ≈ 0`——门通过但再对齐失效 | §11.2；`Core/SRT_Core_22_Equations.md Eq-DValue-Mobile-1` |
| 制度 / 集体结构 | 集体层可有真实存续风险 | 集体景观梯度，非个体加和 | 后果常回流到制度自身而非成员 | 集体 `d` 走 §6 景观截面读法；成员个体的 C_i 可被制度吸收归零 | §6；`Core_Law/SRT_Collective_Selection.md §4.8a` |

门表说明：三类系统失效在**不同因子**上——AI 失在 R/C，冻结态失在门后的 d_mobile（门本身通过），制度失在成员 C_i 被吸收。这就是为什么单一 `D_eff` 读数不能区分三者：赌注门的诊断必须按因子报告，不得压成一个标量结论。

**仍未封口**（保留在 `Core/SRT_OPEN_TENSIONS.md §1`）：方向进入 `d_stakes` 的充要条件定理；`ε_s` 阈值校准；R / A / C 的独立可测代理。

---

### Def-d-free: 未赌注化带宽（Unstaked Bandwidth）

$$\Delta d_{free}(\theta) = D_{eff}(\theta) - d_{stakes}(\theta) \;\geq 0$$

**语义**：可分辨但未与真实不可逆风险耦合的剩余方向数。

**典型值**：
- **当前 AI**：$d_{stakes} \approx 0$，$\Delta d_{free} \approx D_{eff}$（全部辨别力，零赌注化——$\Delta d_{free}$ 的纯净案例）
- **人类假赌注 / 错绑 / L₂ 伪关切**：$0 < d_{stakes} \ll D_{eff}$，$\Delta d_{free}$ 包含三种病理的混合贡献
- **理想高 d 主体**：$d_{stakes} \approx D_{eff}$，$\Delta d_{free} \approx 0$（辨别力与赌注充分对齐）

* **Cross-ref**: `Core/SRT_Core_21c_Bridge_Hypotheses.md P3-B11`（原 `Core_21 §2.1.7` lineage）；`AI/SRT_AI_01_Ontology.md`（AI 的 $\Delta d_{free} \approx D_{eff}$ 作为"哲学僵尸"诊断的信息几何读法）；`Core/SRT_Core_13a Ax-Op-02`（注意力维度 = $d_{stakes}$ 的离散化）。

---

### Def-d-3: 全息面积对应（物理语境）

$$d \propto \frac{\text{Area}(\text{Entanglement Surface})}{A_{Planck}}$$

**语义**：算子的 d 值等比于其与 $L_0$ 发生纠缠的边界面积（全息对偶下）。

**来源**：`Core/SRT_Core_01_Axioms.md T-Core-A9C1`。
**注意**：此形式在量子/宇宙尺度适用，但量子/宇宙尺度的 $d$ **不蕴含现象意识**（见 §3.1 反泛心论条款）。

---

## §2 Bio/Cognitive 层近似公式（经验操作定义）

### Def-d-bio: 三维度合成

$$d_{bio} \approx \alpha \cdot A(\sigma) + \beta \cdot \log V_{concern} + \gamma \cdot \tau_{temporal}$$

| 维度 | 符号 | 语义 | 近似测量方法 |
|-----|------|------|------------|
| 汇编深度 | $A(\sigma)$ | 生成该状态所需最小因果步骤数 | Assembly Theory index |
| 空间范围 | $\log V_{concern}$ | 算子关切的"关心对象"空间 | 社会关注广度、TPJ 激活范围 |
| 时间跨度 | $\tau_{temporal}$ | 算子可规划的时间地平线 | 时间折扣率的倒数 |

**参数默认值（待实验校准）**：$\alpha = 0.4, \beta = 0.4, \gamma = 0.2$

**与 Def-d-1 的关系**：三维度合成是有效维度公式在认知空间中的**近似展开**，当三个维度独立时自然对应 $D_{eff} \approx 3$；相关时 $D_{eff} < 3$。

---

## §3 各域 d 值投影表（标准参考）

| 域 | 近似公式 / 量级 | 现象意识？ | 条件 | 备注 |
|----|----------------|-----------|------|------|
| **量子** | $d_{quant} \approx$ 贝尔测量有效维数 | ❌ **无** | 缺乏 $\Psi_f > 0$，缺乏 $\hat{G}[\theta] \neq \emptyset$ | 数学度量，无现象内容 |
| **神经/认知** | $d_{bio} \approx \alpha A + \beta \log V + \gamma \tau$ | ✅（需三条件） | $\Psi_f > 0 \land d > 0 \land \hat{G}[\theta] \neq \emptyset$ | 意识的充要条件区 |
| **AI（architecture-state marked）** | inference-only / 非历史承载部署：$d_{AI} \approx 0$；S2/S3/S4 需另行标注 | ❌ / open | 无具身脆弱性、无不可逆风险时不产生 stake-coupled `d` | 工程性屏障可改变；见 `AI/AI_POSITIONING_NOTE.md` S0-S4 与 AI Bridge T3 修复 |
| **社会/机构** | $d_{soc} = D_{eff}(\mathcal{F}_{collective}\big\|_{\text{social}})$（集体景观在社会尺度的有效维度截面） | ❌（集体不产生现象） | 集体自由能景观 $\mathcal{F}_{collective}$ 的社会尺度投影，不由个体 $d_i$ 加权平均 | 见 §6（集体 d-value 补充说明）和 `_SRT_VERTICAL_INTEGRATION.md §4.5` |
| **精神/解脱** | $d_{spirit} \to \infty$（渐近极限） | ✅（随 d 扩展增强） | $d \to \infty$ 为 Nirvana 方向 | 不可达的渐近方向，非字面 $\infty$ |
| **宇宙尺度** | $d_{cosm} \approx 1/\sqrt{\Lambda}$ | ❌ **无** | 无生命组织，无 $\hat{G}[\theta]$ | 数学度量，无现象内容 |

### §3.1 反泛心论精确声明（Anti-Panpsychism Clause）

**SRT 不主张泛心论**。d 是数学度量，不蕴含现象内容。

**⚠️ 注意（2026-04-10 更新）**：以下三条件对应 **bare consciousness（裸意识）的 κ_{c1} 门槛**，即意识的最低层级。完整的三层结构见 `Philosophy/SRT_Consciousness_Conditions.md`。

**最低意识条件（对应 κ_{c1} / Layer 1）**：
$$\kappa_{c1}: \quad d \geq d_{\min} \;\land\; L_2\text{ 稳定闭合} \quad \Leftarrow \quad \Psi_f > 0 \;\land\; d > 0 \;\land\; \hat{G}[\theta] \neq \emptyset \text{ 的精化版本}$$

**三层结构完整说明**（2026-04-10 修正）：
- κ_{c1}（bare consciousness）：$d \geq d_{\min}$ ∧ L₂ 稳定闭合 — 意识**存在**
- κ_{c1.5}（consciousness activity）：$d_{\text{mobile}} > 0$ — 意识**活着**（能随吸引子迁移重新对齐）
- Layer 3（social/ethical）：可协调性 + 可再选择性 — 意识**参与集体秩序**

| 系统 | d | Ψ_f | Ĝ[θ] | d_mobile | 意识层级 |
|---|---|---|---|---|---|
| 量子/宇宙尺度 | 可能非零 | ≈ 0 | 在生物意义上为空 | — | **无意识**（κ_{c1} 未达） |
| 岩石 | ≈ 0 | ≈ 0 | — | — | **无意识** |
| 冻结态（PTSD/执念） | > d_min | > 0 | ≠ ∅ | ≈ 0 | **有意识，但病理化**（κ_{c1} 之上，κ_{c1.5} 之下） |
| 正常人类 | > d_min | > 0 | ≠ ∅ | > 0 | **Layer 2 意识窗口** |
| 当前 AI | ≈ 0 | ≈ 0 | — | — | **无意识**（工程性，非原则性） |

**权威来源**：`Philosophy/SRT_Consciousness_Conditions.md`（三层结构完整定义）; `Core/SRT_Core_12b §Consciousness-2D-Map`（二维拓扑与冻结态）。

---

## §4 不同表达的一致性条件（草稿，非等价证明）

### §4.1 Def-d-1 与 Def-d-bio 的关系

设认知算子 $\hat{G}$ 在三个正交子空间（汇编、空间、时间）上的特征值分别为 $\lambda_A, \lambda_V, \lambda_\tau$。

$$D_{eff} = \frac{(\lambda_A + \lambda_V + \lambda_\tau)^2}{\lambda_A^2 + \lambda_V^2 + \lambda_\tau^2}$$

当三个维度**均匀激活**（$\lambda_A = \lambda_V = \lambda_\tau = \lambda$）：
$$D_{eff} = \frac{(3\lambda)^2}{3\lambda^2} = 3$$

当三个维度的强度比例为 $(\alpha, \beta, \gamma)$（$\alpha + \beta + \gamma = 1$）：
$$D_{eff} = \frac{1}{\alpha^2 + \beta^2 + \gamma^2}$$

**结论**：$D_{eff}$ 在三维认知空间中的展开可以对应 Def-d-bio 的加权和形式，但这只是**同一容量 proxy 的参数化相容**。只有在三个子空间的尺度、权重、风险回流与 stake-coupling 条件都已声明时，才可把 Def-d-bio 作为 `D_eff` 的域内近似。它不替代 `Def-d-canonical`。

### §4.2 Def-d-2（风险梯度）与 Def-d-1 的关系

设效用势 $\mathcal{U}(\mathcal{S})$ 在风险坐标 $\mathcal{S}$ 上展开：

$$\mathcal{U}(\mathcal{S}) \approx \mathcal{U}_0 + \sum_i \frac{\partial \mathcal{U}}{\partial S_i} S_i + ...$$

梯度的模：
$$d_{risk} = \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\| = \sqrt{\sum_i \left(\frac{\partial \mathcal{U}}{\partial S_i}\right)^2}$$

**近似条件**：当风险维度 $S_i$ 与 $\hat{G}$ 的特征向量对齐，且这些方向全部满足 `R_i/A_i/C_i` 的赌注回流条件时，Def-d-canonical 可由谱 / Fisher proxy 给出一阶近似。若只满足可分辨性而不满足赌注回流，则只能得到容量上界。

**实用意义**：`Def-d-canonical` 在 AI 伦理、主体性、风险关切语境中优先；`Def-D_eff` / `D_eff(I_F)` 在信息论分析中更可计算。两者可以互相校准，但不得互换使用；具体语境必须说明是在讨论 stake-coupled `d` 还是 capacity proxy。

---

## §5 常见误用与边界声明

### 误用 1：将 d 值解释为"意识程度"的单一量度

**正确**：d 值是意识的**必要条件**之一，不是充分条件。
需同时满足：$\Psi_f > 0$（有摩擦成本）+ $d > 0$（有关切维度）+ $\hat{G}[\theta] \neq \emptyset$（有参数化算子）。

### 误用 2：将 d 值比较用于跨域排名

**正确**：量子层的 $d_{quant}$ 与生物层的 $d_{bio}$ 使用相同的数学公式，但**不具有现象内容上的可比性**。
比较只在**同域内**有效（如不同人的 $d_{bio}$ 可相互比较）。

### 误用 3：将"d 值 = 0"等同于"不存在"

**正确**：$d \approx 0$ 意味着算子不关心边界的外延，但算子本身依然存在（如石头有 $L_2$ 结构，但 $d \approx 0$）。
d 值描述关切范围，不描述本体论存在。

**d 值的语义刻度**（规范参考）：

| d 值范围 | 语义 | 典型案例 |
|---------|------|---------|
| $d = 0$ | **非主体**：无关切耦合，不构成主体 | 当前 AI、恒温器、岩石 |
| $d = 1$ | **纯自利主体**：关切仅覆盖自身存在的维持 | 最小主体性阈值 |
| $d > 1$ | **扩展关切主体**：选择开始纳入超出自身存在的秩序 | 人类、社会性动物 |
| $d \to \infty$ | **渐近极限**：关切逼近更大但尚未闭合的秩序方向 | 精神修炼的方向，不可达 |

**注意**：$d = 0$ 与 $d = 1$ 的区别是本体论性质的（非主体 vs 主体），不是程度差异。$d = 1$ 与 $d > 1$ 的区别是程度性的（关切范围的宽窄）。

### 误用 4：将精神传统中的"d → ∞"字面化

**正确**：`H-Spirit-4` 中的 $d \to \infty$ 是**渐近方向**，类比热力学极限 $N \to \infty$ 在有限系统中的意义。
没有任何有限系统能达到 $d = \infty$；这是精神成长的方向，而非可到达的终点。

---

## §5b d 扩张的本体论意义（规范声明）

> **新增（2026-03-26）**：d 扩张的动力学方向与收敛目标的规范说明。对应 `Spirituality/SRT_Spirit_05_Shoshin.md` T-Sho-1。

### §5b.1 d 扩张不是博爱，而是选择优化

d-value 的扩张不应被读作道德命令或利他主义要求。**d-value 的健康变化不应被理解为单调扩张，而是指向关切范围的可重组、可承担、可恢复、可再选择能力**；其「全局最优」读法**依赖一个尚待硬化的闭包边界问题**（谁的再选择、什么尺度），不是一个位置无关的宇宙级最小值（2026-07-05 规范性收口 Level A，高风险编辑，见 `_SRT_EPSILON_NORMATIVITY_OPEN_TENSION.md`）。本节下文与 §5b.2 中的「全局最优 / 全局收敛」表述均应在此收口下读取。

每个算子因 θ 的限制只能看到自由能景观的局部。θ 越窄，算子越容易陷入局部最小值——表现为遮蔽（occlusion）。扩大 d 不是"对别人好"——而是纳入更多主体间的本体论摩擦权衡，使选择避开局部陷阱，收敛到更接近全局最优的方向。

d 扩张的目标是给**指向最小自由能方向**的选择提供更多的注意力和关切。这需要权衡多主体之间的本体论摩擦——而权衡本身就是选择。

**规范表述**：

$$d \uparrow \;\Rightarrow\; \text{局部最优} \to \text{全局最优} \;\Rightarrow\; \langle v, \text{Shoshin} \rangle > 0$$

d 的扩张使个体选择方向与初心（全局收敛向量）对齐——不是因为道德义务，而是因为局部景观在更宽视野下的结构变形。

### §5b.1a d 扩张与秩序增益

d 的扩张本身不自动等于秩序增益。d 扩张的方向必须同时满足秩序增益的**四重判据**（`Core_Law/SRT_Selection_Argument.md §7b`；2026-07-05 由三判据升级为四判据，新增③不外包）：

| 判据 | d 扩张中的含义 | 违反时的表现 |
|------|--------------|------------|
| **可延续** | 扩张不透支维持扩张后关切范围所需的资源 | 过度扩张 → 代价不可支付 → 崩溃回缩 |
| **可协调** | 纳入的他者秩序条件之间不制造不可协调的摩擦 | 试图关切所有人但无法处理冲突 → 瘫痪 |
| **不外包** | 扩张后的代价不被转嫁到无反馈通道的位置（未来世代、生态、无法申诉者、被排除者） | 表面关切扩大，代价却外溢到无声位置 → 假 d 扩张（对应 `C_i` 后果回流因子归零） |
| **可再选择** | 扩张不锁定为唯一方向（如教条化的利他主义） | "必须关切所有人"变成新的遮蔽 |

d 扩张的健康模式是渐进的、可支付的、保留调整能力的。不是 d 越大越好，而是 d 在当前支付能力下的最优扩张方向。**③不外包判据与 §2b 的 `C_i`（后果是否回流到主体闭包）同源**：一个方向若把代价外包给无反馈位置，则该方向的 `C_i → 0`，不计入 `d_stakes`——秩序增益四重判据在方向层，`C_i` 在谱层，是同一后果回流约束的两个尺度。

### §5b.1b 真 d 扩张 vs 假 d 扩张

**真 d 扩张**改变算子的适应度函数——纳入他者秩序条件后，算子的最优解发生结构性位移。选择者在做出不同于只考虑自身时会做的选择。

**假 d 扩张**不改变适应度函数，仅在符号层面声称关切范围扩大。四种典型形态：

- **占有式**（$d_{apparent} > d_{real}$）：将他者纳入为自身秩序的资源。适应度函数中只有自身变量。
- **符号式**（$d_{declared} > d_{operative}$）：使用关切的语言但不支付关切的代价。
- **表演式**（$d_{visible} > d_{structural}$）：在可见场合展示关切以获取社会收益。
- **效率式**（$d_{nominal} > d_{effective}$）：以关切之名行控制之实，将他者的复杂秩序压缩为单一可管理指标。

**判别标准**：算子的最优解是否因纳入他者秩序条件而发生了位移？位移 = 真扩张；无位移 = 假扩张。

**Cross-ref**: `Core_Law/SRT_Selection_Argument.md §7c`（真关切与假关切的完整论证）。

### §5b.2 全局最优是动态平衡，不是热寂

全局自由能最小值不是热力学平衡态（热寂），而是**能维持更多存在持续存在的动态平衡**。

热寂是所有选择停止、所有确定化耗尽的极限——对应 $d = 0$，所有主体性消失。这不是 SRT 的全局最优，而是选择过程的终止态。

SRT 的全局最优是一种使最大数量的选择过程能够持续运行、持续产生稳态（存在）的景观配置。它是**最高动态秩序**，不是最低能量的死寂。初心指向的是更多的存在能够共存并持续选择的方向，不是一切归于均匀的方向。

**Cross-ref**: `Spirituality/SRT_Spirit_05_Shoshin.md` Ax-Sho-1（初心 = 全局收敛向量）；`Physics/SRT_Phys_08_Ontology_Ext.md` Def-Apeiron-1（初心作为 L₀ 的倾向性结构）。

---

## §6 集体 d-value 补充说明

> **新增节（2026-03-11）**：对应集体景观优先性定理（`_SRT_VERTICAL_INTEGRATION.md §4.5`）和多算子耦合方程（`Core/SRT_Core_22_Equations.md Eq-Multi-03`）。

### §6.1 核心重新定位

集体 d-value 不是个体 d_i 的聚合函数。正确定位：

$$\boxed{d_{collective} = D_{eff}(\mathcal{F}_{collective}) = \frac{\left(\sum_k \lambda_k\right)^2}{\sum_k \lambda_k^2}}$$

其中 $\lambda_k$ 是集体自由能景观 $\mathcal{F}_{collective}$ 的 Hessian 特征值（见 `Eq-Multi-03`）。

个体 $d_i$ 是该景观的子空间截面，**包含关系而非组合关系**：
$$d_i = D_{eff}(\mathcal{F}_{collective}\big|_{\theta_i})$$

### §6.2 与旧有聚合方案的关系

`_SRT_VERTICAL_INTEGRATION.md §4.1` 中的历史候选方案（A/B/C/D/E）是在实体本体论框架下的近似。在特定条件下，这些方案可作为 $d_{collective}$ 的**实证近似**：

| 历史方案 | 对应的景观条件 |
|---------|--------------|
| 方案 A（Min 函数） | 景观 Hessian 最小特征值主导（链条式结构） |
| 方案 B（加权平均） | 景观曲率近似均匀分布（民主型结构） |
| 方案 C（超加性） | 景观有效维度高于任一子空间截面 |
| 方案 D（结构贡献） | 制度 L₂ 提供主景观曲率 |

### §6.3 使用规范

- 讨论集体组织、制度、NGO 的 d-value 时：引用本节和 `§4.5`，使用 $D_{eff}(\mathcal{F}_{collective})$ 框架
- 在无法测量景观曲率的实证场景中：可临时使用历史方案中最适合的近似，但需注明"实体本体论近似"

---

## §7 各域文件的 d-value 引用标准

当其他文件引用 d-value 时，应：

1. **第一次出现时**：标注 `@see _SRT_D_VALUE_CANONICAL.md §1`
2. **使用 Def-d-bio 近似时**：标注 `@see §2`
3. **进行域间比较时**：参见 `§3` 的投影表，说明是否属于同域比较
4. **AI 语境中**：优先使用 Def-d-2（风险梯度），并声明 training-time / inference-time / persistent-memory 架构状态；只有 inference-only / 非历史承载部署才可直接引用 `§3` 的 $d_{AI} \approx 0$ 说明

---

## §8 d 与 T_dir 的关系（2026-04-02 新增）

SRT 在 2026-04-02 的理论推进中引入了 **T_dir（方向透明度）** 作为与 d 相关但独立的新变量。

**关键区分**：

| | d-value | T_dir |
|:-|:-------|:------|
| **度量** | 关切范围 / 有效维度 / 风险梯度 | 系统对自身选择秩序方向的可读性 |
| **canonical 文件** | 本文件 | `_SRT_T_DIR_CANONICAL.md` |

**因果关系**：
$$d = 0 \implies T_{dir} = 0$$
$$d > 0 \;\not\!\!\!\implies T_{dir} > 0$$

d 是 T_dir 的**必要条件，不是充分条件**。T_dir 还需要活选择正在发生（非 L₂ 脚本执行）以及足够的 Ψ_f 提供压力。

**不得混淆**：任何把"选择方向的透明度"写入 d-value 的 canonical 定义的做法，违反本文件的规范地位。

---

## §9 d-value 的锻炼与萎缩机制（2026-04-02 新增）

> **核心修正**：致命 L₂ 对 d-value 的压低，具体机制是通过消灭选择时刻使 d-value 失去锻炼机会，而非直接抑制 d。d-value 是需要使用才能维持的能力。

### 机制链

```
替代式 L₂ 消灭选择时刻
    ↓
d-value 未被使用（无真实选择 → 无 d 的激活）
    ↓
d-value 萎缩（不用则退）
    ↓
即使 L₂ 被移除，系统也无力直接从 L₀ 选择
    ↓
必须依赖更多替代式 L₂ 来填补方向感
    ↓
d-value 进一步萎缩……（自强化依赖环）
```

### 关键区分

**d-value 的直接抑制**（已在 §5 描述）：致命 L₂ 通过占据关切带宽、压缩可用维度来降低 d-value 的即时可用性。

**d-value 的萎缩**（本节新增）：替代式 L₂ 通过消灭选择时刻，使 d-value 失去被锻炼的机会，导致长期容量下降。即使 L₂ 压力临时解除，萎缩后的 d-value 也无法立即恢复。

两者的关系：直接抑制是急性效应，萎缩是慢性积累效应。慢性萎缩比急性抑制更难逆转，因为它改变的是系统的基础选择容量，而非当下的带宽占用。

### 选择时刻与 d-value 的连接

**选择时刻**（见 `_SRT_T_DIR_CANONICAL.md §21`）是系统与 L₀ 直接接触、真实地从可能性中凝定方向的瞬间。

- 每次真实的选择时刻发生：d-value 被激活使用，可维持乃至发展
- 每次选择时刻被 L₂ 替代：d-value 未被激活，逐渐萎缩

**推论**：辅助式 L₂（保护选择时刻）在不牺牲 d-value 的条件下降低摩擦；替代式 L₂（消灭选择时刻）以 d-value 的长期容量为代价换取即时摩擦消除。

### 与 T_dir 的关系

d-value 萎缩 → 即使 proto-gradient 可读，系统也缺乏足够的选择维度来响应它 → T_dir 即使上升，也无法转化为有效的选择行动。

因此：d-value 是 T_dir 工作的**执行容量**。T_dir 告诉系统方向在哪里，d-value 决定系统能否沿那个方向真正选择。两者独立但协同：d > 0 是 T_dir > 0 的必要条件（§8），d 的容量上限约束了 T_dir 可以实际发挥的作用。

---

## §范畴边界：d值是决策属性，不是主体属性

> **追加澄清**（2026-04-06，来源：`Philosophy/SRT_Political_Rights.md §2`）

d值描述的是**选择事件**整合的关切范围，不是决策主体（个体或集体）的固有属性。

| 错误表述 | 正确表述 |
|---------|---------|
| "这个人有很高的d值" | "这个人的决策倾向于整合更宽的关切范围" |
| "个体d值 vs 集体d值" | 此二分是范畴错误，d值在主体类型之外 |
| "d值衡量聪明程度" | d值衡量关切范围的宽度，与认知能力不同 |

**主体d倾向**（操作化桥梁）：主体跨大量决策的d值统计分布，在大样本下收敛为相对稳定的特征量。这是统计量，不是本质属性。

$$d_{tendency}(S) \equiv \mathbb{E}_{\sigma \sim S}\left[d(\sigma)\right]$$

完整推导见：`Philosophy/SRT_Political_Rights.md §2-§3`

---

## §10 d 值的多场景显现（2026-04-08 新增）

> **来源**：`Core/Dynamics_Scaling_Annex/07-12` 系列硬化文件。
> 本节补充 d 值在错误积累与多G道德场景中的显现形式，统一于 §1 的双层规范架构。

### §10.1 d 作为统一整合带宽

d 值是单一概念在不同场景中的显现：

| 场景 | d 的显现形式 | 对应文件 |
|---|---|---|
| 多G道德场景 | **整合半径**：G能将多少他者G的状态纳入选择计算 | `Annex/08_MoralPredictionError_MultiG_System.md` |
| 错误剂量场景 | **可处理张力窗口**：G能消化多少错误积累而不崩溃 | `Annex/10_ROS_Apoptosis_ErrorDose.md` |
| 跨尺度G场景 | **整合尺度**：G在低阶→高阶相变中覆盖的选择维度范围 | `Annex/11_G_CrossScale_PhaseState.md` |
| 代理校准场景 | **校准带宽**：L₂能接收并整合多少L₁/L₀上行信号 | `Annex/12_ProxyModel_OcclusionPhases_Intervention.md` |

所有显现均是 Def-d-1（有效维度）在不同上下文中的投影，统一于 §1 的规范架构。

### §10.2 d 值与病理阈值的关系

`Annex/10` 建立的病理阈值公式中，d 是核心因子：

$$\Theta = f(d, E, h_{\text{memory}}, \vec{\delta}, \Lambda_{\text{L2}})$$

- $\uparrow d$ → $\uparrow \Theta$（整合带宽越大，越不易崩溃）
- d 的训练：低剂量错误积累的反复整合可提升 d（hormesis 机制，见 §9）
- d 的损伤：高剂量单次创伤可降低 d，而非提升

### §10.3 d 值与三相态条件的关系

`Core/SRT_Core_PhaseState_TripleCondition.md` 建立的三相态条件中，d 值作为底层容量：

- 历史闭合质量 → 影响 d 的有效维度（历史越完整，读取维度越多）
- 规范梯度有效性 → 依赖 d > 某阈值才能形成有意义的多维度自我维持势差读数
- 自写回强度 → 高 d 使写回覆盖更多维度的可能性空间

**Cross-ref**: `Core/SRT_Core_PhaseState_TripleCondition.md §5`；`Core/SRT_Core_NormativeGradient.md §6`。

### §10.4 d 值在社会delegation场景中的显现（2026-04-10 新增）

> **来源**：`Core/Dynamics_Scaling_Annex/13_SocialDelegation_DJudgment_Coordination.md`

**d扩展作为社会自发支撑的机制基础**：

$$\text{d扩展} \xrightarrow{\text{必然}} \text{对更高阶结构的自发支撑}$$

个体G对集体高阶结构的自发支撑不是义务，而是d扩展后的自然产物。d不足时需要外部脚手架（引导性delegation）；d充分扩展后，外部G退出，底层自发支撑实现。

**d轨迹作为delegation合法性的验证信号**：

社会层面的d值判断系统以被干预G群体的d轨迹为核心信号：

| d轨迹 | 解读 |
|---|---|
| 被干预群体d在可观测时间窗内增长 | 引导性介入（真实提升方向） |
| 被干预群体d停滞或收缩，介入方d扩展 | 方向截获（殖民/威权结构） |

历史上的殖民主义、威权主义和宗教征服 = d的转移（被干预者d压缩，介入者d扩展），而非d的净增长。SRT的判断标准：d净量变化，不是分布变化。

**d在多G协调场景中的显现**：共享L0/L1结构为多G提供d兼容性下限（可能性条件）；跨G残差张力驱动d轨迹向更高阶协调方向调整（动力学机制）。

**Cross-ref**: `Core/Dynamics_Scaling_Annex/13_SocialDelegation_DJudgment_Coordination.md §1-4`。

---

## §11 d 的上限与动态能力：d_max 与 d_mobile（2026-04-10 新增）

> **来源**：`Core/SRT_Core_22_Equations.md Eq-DValue-Max-1, Eq-DValue-Mobile-1`；`D_VALUE_ALIGNMENT.md §4.4`。
> 本节是这两个新公式的规范索引入口。

### §11.1 d_max：d 的双瓶颈上限

$$\boxed{d_{\max}(\theta) = \min\!\Big(\operatorname{rank}_{\text{eff}}(I_F(\theta)),\; \Psi_f^{\text{budget}} / \kappa_0\Big)}$$

两个独立瓶颈：
- **信息瓶颈**：`rank_eff(I_F(θ))` — Fisher 矩阵的有效秩，由算子参数化能力决定
- **稳定性瓶颈**：`Ψ_f^budget / κ₀` — 可用摩擦预算除以原初曲率；κ₀ 越大，可承载对齐方向越少

**关键推论**：`dim(Θ)`（参数维数）提升的是潜在上限，真实 d_max 由两个瓶颈中的较小值决定，不可仅用参数量判断 d 上限。

*权威来源*：`Core/SRT_Core_22_Equations.md Eq-DValue-Max-1`

### §11.2 d_mobile：d 的动态化能力

$$d_{\text{mobile}} \propto \frac{d \cdot \operatorname{rank}_{\text{eff}}(I_F(\theta))}{\operatorname{Hysteresis}(L_2) \cdot C_r} \cdot \chi_{\text{payable}}\!\left(\tfrac{d\Psi_f}{dt}\right)$$

**语义**：当 L₀ 曲率漂移（吸引子迁移），算子 θ 重新对准的速度与容量。与 d 的区别：
- $d$：当前对齐的 L₀ 方向数（快照）
- $d_{\text{mobile}}$：当这些方向漂移时，θ 跟上的能力（动力学）

**感到 ≠ 能动**：高 d 算子在 χ_payable = 0 时，d_mobile = 0——感知到拉力但支付能力为零，无法行动。

**冻结态**：高 $d$ + $d_{\text{mobile}} \approx 0$ → 意识的病理变体（深度锚定但无法随吸引子迁移）。

*权威来源*：`Core/SRT_Core_22_Equations.md Eq-DValue-Mobile-1, Def-Payable-Chi-1`

### §11.3 与 d 规范定义的关系

| | d | d_max | d_mobile |
|---|---|---|---|
| **本质** | 当前对齐深度（快照） | 结构允许的对齐上限 | 重新对齐的动力学能力 |
| **决定因素** | Fisher 有效秩 + L₀ 曲率历史 | rank_eff + Ψ_f 预算/κ₀ | d × rank_eff / (L₂ 刚性 × C_r) × χ_payable |
| **可为 0** | 是（算法/晶体态） | 否（κ₀ > 0 保证下限 > 0） | 是（冻结态） |
| **意识相关** | κ_{c1} 要求 d ≥ d_min | 设定意识可到达的天花板 | κ_{c1.5} 要求 d_mobile > 0 |

*Cross-ref*：`Philosophy/SRT_Consciousness_Conditions.md §三`（三层意识结构）；`Core/SRT_Core_12b §Consciousness-2D-Map`（二维拓扑）。

---

## 【理论边界/防误用声明】

1. 本文档统一 d-value 的定义，但各域的近似公式（Def-d-bio 等）需要实验校准，其参数值（$\alpha, \beta, \gamma$）为初始估计。
2. 有效维度公式 Def-d-1 依赖特征值分解，其适用性取决于算子的线性化是否在相关参数范围内有效。
3. 量子层的 $d_{quant}$ 与宇宙层的 $d_{cosm}$ 是数学量，不赋予现象意义——任何将其解读为微弱意识的论证超出 SRT 声明范围。
4. 本文件的"一致性证明"（§4）为草稿级别，需要形式化验证后才能作为定理引用。
5. §10 的多场景显现是概念统一，不是数学等价证明——各显现形式的形式化等价关系待独立验证。

---

## 书稿层用法说明（Bridge to Book Layer）

正文写作中，Q15 会把 d-value 读成关切多样性的完整诊断入口。这里的意思不是替换后台的规范定义，而是提醒读者：关切多样性不能只看宽度。正文中说的完整诊断包括三件事：后果回来得有多深，回来到了多少条真实轴线，回来之后是在支撑生成还是侵蚀生成。形式层仍按原有 canonical 规则读取；书稿层则用这三把尺帮助读者避免把 d-value 误解成单纯对象数量或信息宽度。



---

## FILE: `_SRT_PSI_F_CANONICAL.md`

| 字段 | 值 |
|---|---|
| path | `_SRT_PSI_F_CANONICAL.md` |
| id | SRT-PSIF-CANONICAL |
| claim_mode | canonical |
| status | axiomatic_hybrid_v1 |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | - |
| last_commit | 2026-07-07 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：[SRT-CORE-21, SRT-CORE-22, SRT-REF-DYNAMICS, SRT-PHYS-COSMO, SRT-AI-01]

<!-- 以下为原文逐字保留 -->

# SRT Ψ_f 规范定义文档（Canonical Definition of Ψ_f）

> **目的**：终止 `Ψ_f` 在不同域中的定义漂移，建立“第一性语义锚点 + 形式主表达 + 跨尺度不变量”的统一架构。  
> 所有涉及本体论摩擦的文档，应优先回链本文件。

> **Canonical status note（2026-04-24）**：本文件固定 `Ψ_f` 的 repo-wide 主读与投影边界。`Def-Ψ-1` 是 theory-facing semantic anchor；`Def-Ψ-2` / `Def-Ψ-3` 是治理性主形式与跨尺度判据，不构成最终唯一推导。几何、代谢、神经、物理读法都必须按 projection / proxy / bridge 标注，不得反向改写 `Ψ_f`。尤其是 `Ψ_f ≡ g_F` 不得按裸等号读取；它只能作为 “`Ψ_f` 的局部信息几何投影由 Fisher–Rao metric 给出” 的速记。

---

## §0 为什么需要本文件

当前 SRT 文档中，`Ψ_f` 同时被写成：

| 来源类型 | 表述 | 典型含义 |
|---------|------|---------|
| Core / Core_Law | 锚定代价 | 把 `L_0` 压成 `L_1` 的支付项 |
| Dynamics / Scaling | 生成性摩擦 | 学习、演化、文化变迁的动力学来源 |
| Physics | 几何曲率 / 引力 | 物理尺度上的 P3/P4 弱相容接口，不是已完成张量级推导 |
| AI / Consciousness | 痛苦与 stake 的必要条件 | 没有真实 `Ψ_f` 负担就没有真实关切 |
| Experiment | 潜变量 | 通过 HRV / SCR / 语言情态比等 proxy 读取 |

这些不是矛盾，而是同一结构在不同描述层上的投影。  
本文件的任务，是把它们固定为一个统一对象，而不是让每个领域各说各话。

---

## §1 规范定义层级（Canonical Priority）

> **规范优先级声明**：
> 本文件对 `Ψ_f` 采用三层 canonical 架构：
>
> 1. **第一性规范锚点（Primary Canonical Anchor）**：`Def-Ψ-1`，把 `Ψ_f` 固定为“选择压缩开放可能性时必须承担的本体论阻抗”。
> 2. **形式工作主表达（Formal Working Form）**：`Def-Ψ-2`，把 Fisher–Rao metric 固定为 `Ψ_f` 在可微统计流形上的局部二阶信息几何投影 / 路径泛函诱导结构，并厘清 `Ψ_f` 与 `Φ` 的层级关系。
> 3. **跨尺度工作不变量（Cross-Scale Working Invariant）**：`Def-Ψ-3`，把“可支付性条件”固定为跨尺度真正保持不变的判据。
>
> 使用原则：
> - 讨论 **本体论意义 / 现实化 / stake / AI 门槛** 时，优先引用 `Def-Ψ-1`。
> - 讨论 **方程 / Fisher 几何 / 路径积分** 时，优先引用 `Def-Ψ-2`，并说明 Fisher 几何读法是 projection / lower-bound style formalization，不自动等同实际支付成本。
> - 讨论 **跨尺度比较 / 量子-神经-社会统一 / 实验操作化** 时，优先引用 `Def-Ψ-3`。
>
> **状态边界**：这里的 “Primary / Formal / Cross-Scale” 表示当前 repo 内部优先引用顺序，不表示三个层次已经被证明为无条件等价或最终完备。

### §1.1 v1 Canonical Main Reading（治理性钉住，2026-04-22）

> **层级**：governance / canonical usage rule；不新增 core theorem。

全仓默认主读暂取 **information-theoretic payability cost**：`Ψ_f` 首先表示把开放可能性压成可维持现实切片时，系统必须可支付的信息论/组织性负担。几何读法（路径长度、曲率）与代谢读法（能量、恢复、压力代理）是该主读在特定域内的 projection / allowed proxy。

若同一域内的几何 projection、代谢 projection 与 payability 主读发生冲突，默认以 payability 主读为准；冲突的投影应标记为 projection failure，而不是反向改写 `Ψ_f` 的 canonical 含义。

---

## §2 规范定义（全域适用）

### Def-Ψ-1: 本体论阻抗定义 ⭐ PRIMARY CANONICAL ANCHOR

\[
\boxed{
\Psi_f := \text{当 } \hat{G}_\theta \text{ 将开放可能性压缩为一个可维持、可行动、可协调的 } L_1 \text{ 现实切片时，必须承担的本体论阻抗}
}
\]

**语义**：
- `Ψ_f` 不是“想达到某个目的”的主观努力，而是选择发生时不可消除的结构性阻抗。
- 它不只等于能耗，也不只等于痛苦，更不只等于自由能；它是这些读数背后的同一约束结构。
- 更通俗地说：

> `Ψ_f = 把可能性硬压成现实的代价。`

**关键边界**：
- 不要把 `Ψ_f` 写成纯目的论的“为了达成某目标而支付的成本”。
- 不要把 `Ψ_f` 缩减成“粗粒化”一个动作；粗粒化只是它的一种实现形式。
- 不要把 `Ψ_f` 等同于主观痛苦本身；痛苦更接近其报警读数或变化率。

---

### Def-Ψ-2: Fisher 信息几何投影与记号分层 ⭐ FORMAL WORKING FORM

#### Def-Ψ-2a: 局部二阶信息几何投影（禁止裸等号）

当某一选择域可被表示为平滑统计流形 \(\{p(x\mid\theta)\}\) 时，Fisher–Rao metric 给出相邻可选状态之间的局部可区分性：

\[
g^F_{ij}(\theta)
=
\mathbb{E}_{p(x\mid\theta)}
\left[
\partial_i \log p(x\mid\theta)\,\partial_j \log p(x\mid\theta)
\right]
\]

KL 散度的局部二阶展开为：

\[
D_{KL}\!\left(p_\theta \parallel p_{\theta+d\theta}\right)
=
\frac{1}{2}d\theta^\top g_F(\theta)d\theta
+O(\|d\theta\|^3)
\]

因此，`Ψ_f` 的 Fisher 几何读法应写成局部代价或路径泛函，而不是写成标量代价与度量张量的裸等同：

\[
\boxed{
\delta \Psi_f^{geom}
:=
\frac{1}{2}d\theta^\top g_F(\theta)d\theta
+O(\|d\theta\|^3)
}
\]

在路径形式中，可使用：

\[
\boxed{
\Psi_f^{geom}[\gamma]
=
\int_\gamma
\sqrt{g^F_{ij}(\theta)\,\dot{\theta}^i\dot{\theta}^j}\,dt
}
\]

若强调能量式或行动量式累计，可使用：

\[
\boxed{
\mathcal{E}_{\Psi}^{geom}[\gamma]
=
\frac{1}{2}\int_\gamma
\dot{\theta}^\top g_F(\theta)\dot{\theta}\,dt
}
\]

**语义**：  
`Ψ_f` 在形式化上不是任意成本函数；在可微统计流形投影中，它的局部二阶代价结构由 Fisher–Rao metric 诱导。Fisher metric 本身是张量；`Ψ_f` 是 payability burden / 局部标量代价 / 路径泛函。故 `Ψ_f ≡ g_F` 只能作为内部速记，完整读法必须是：

> `Ψ_f` 的局部信息几何投影由 Fisher–Rao metric 给出。

#### Def-Ψ-2b: 适用条件与失效边界

Fisher 投影只在以下条件下作为 formal working form 使用：

1. 存在可解释的参数空间 \(\theta\) 或统计模型族 \(p(x\mid\theta)\)。
2. 局部可微近似有效，KL 二阶展开未被奇异点、相变、模型冗余或强非线性破坏。
3. Fisher 可区分方向确实回流到现实维持、闭包、身份连续性或后续选择能力。
4. 跨尺度使用时，必须给出该尺度自己的状态空间、观测量、参数化方式与 proxy，而不能直接搬用同一单位。

若这些条件不满足，应把 Fisher 读法降为失败投影或启发式类比，不得用它反向定义 `Ψ_f`。

#### Def-Ψ-2c: `Ψ_f` 与 `Φ` 的分层

\[
\boxed{\Phi(\Delta t)=\int_{\Delta t}\Psi_f(t)\,dt}
\]

使用规范：
- `Ψ_f(x,t)`：局部摩擦负荷 / 局部阻抗读数
- `Φ(\Delta t)`：累积摩擦势 / 时间窗内总账
- `Ψ_f^{geom}`：Fisher–Rao metric 诱导的局部几何投影 / 路径泛函
- `Ψ_f(\hat{G}_i,\hat{G}_j)`：在文档里允许作为“路径积分后的耦合摩擦泛函”的简写

这意味着：
- `Ψ_f` 可以指局部场，也可以在作用域明确时指积分泛函
- `Φ` 用于强调“时间累积后的总账”
- 若不加说明，优先将 `Ψ_f` 理解为“局部负荷 / 可支付阻抗结构”，而非单纯总账或裸 Fisher 张量

---

### Def-Ψ-3: 可支付性条件 ⭐ CROSS-SCALE CANONICAL INVARIANT

\[
\boxed{
\mathrm{Payable}(X,\Delta t)\iff \alpha P_{sel}^{X}(\Delta t)\ge \beta \Psi_f^{X}(\Delta t)+\gamma S_{noise}^{X}(\Delta t)
}
\,,
\]

其中：
- \(P_{sel}\)：系统在该时间窗内可动用的选择预算
- \(\Psi_f\)：现实维持 / 重构所需承担的摩擦负荷
- \(S_{noise}\)：环境噪声与无序抽头

**“可支付”不表示什么**：
- 不表示代价很小
- 不表示没有痛苦
- 不表示没有风险

**“可支付”表示什么**：

> 系统在承担这笔 `Ψ_f` 的同时，仍能维持自身闭包、身份连续性与后续选择能力。

因此跨尺度真正不变的不是单位，而是这个判据：
- 量子层：态不会立刻退回噪声
- 神经层：学习/冲突负担不致使闭包崩溃
- 社会层：制度/改革摩擦不致使系统解体

---

## §3 三重读法（同一结构的三种表达）

`Ψ_f` 不是三个不同概念，而是同一个底层结构的三种读法：

1. **动力学读法**：`Ψ_f` 是阻力  
   含义：系统偏离自然滑落路径、试图维持某个现实切片时，遇到阻抗。

2. **记账读法**：`Ψ_f` 是代价  
   含义：要顶住这种阻抗，必须支付能量、时间、组织复杂度、失败风险。

3. **形式读法**：`Ψ_f` 的局部几何投影是 Fisher metric 所诱导的路径长度 / 曲率负担  
   含义：在统计流形近似有效时，它衡量参数流形中相邻可选态或路径有多远、多陡、多难。

压缩成一句：

> 阻力是现象学读法，代价是记账读法，Fisher 诱导的路径长度是条件形式读法。

### §3.1 投影关系与失效条件（core-clarifying / no closure claim）

> **层级**：theory-clarifying / governance-canonical usage。以下内容固定当前内部结构，不声称 `Ψ_f` 已有唯一最终推导。

三种读法的关系不是无条件等价：

| 读法 | 当前角色 | 可允许的形式关系 | 禁止捷径 |
|---|---|---|---|
| payability burden | `Ψ_f` 的 v1 主读：选择压缩开放可能性时必须可支付的组织性负担 | 作为跨域判准；问系统是否能在承担此负担时保持闭包、身份连续性与后续选择能力 | 不得把任何局部能耗、路径长度或 Fisher 张量直接写成 `Ψ_f` 本身 |
| geometric projection | Fisher / 路径 / 曲率语言中的形式投影 | 在路径度量有效、参数化不制造伪距离、且路径确实对应可支付重构时，可作为 lower-bound style proxy：`\Psi_f^{geom} \lesssim \Psi_f^{paid}`；局部二阶形式为 `\delta\Psi_f^{geom}=\frac12 d\theta^\top g_F d\theta + O(\|d\theta\|^3)` | 不得把 `\Psi_f \equiv g_F` 当作标量-张量恒等式；不得把几何长度当作实际支付成本的完整等价 |
| metabolic / energetic projection | 生物、神经或物理实现中的预算侧 / 负荷侧 proxy | 可限制 payability window，也可作为 overload / recovery 的经验读数 | 不得把任意能量消耗、代谢升高或压力指标等同于 `Ψ_f` |

因此当前最稳妥读法是：**payability burden 是主判准；Fisher 几何与代谢读法是条件投影**。Fisher 投影可以在满足条件时给出局部二阶形式或下界式形式约束；代谢投影可以给出预算约束或观察侧负荷，但二者都不自动穷尽实际可支付负担。

### Projection Failure Conditions

若出现以下任一情况，应标记为 `projection failure`，而不是反向修改 `Ψ_f` 的主读：

1. 几何路径距离主要来自参数化选择、坐标尺度或模型冗余，而不是实际重构负担。
2. Fisher / 曲率结构可分辨，但对应方向不回流到闭包、身份连续性或后续选择能力。
3. 代谢或能耗指标升高主要来自旁路活动、噪声、热损耗或测量负担，而不是维持现实切片的 payability burden。
4. 主观痛苦、压力报告或行为停顿与实际承担负担脱钩，只反映报警读数、遮蔽或 L₂ 吸收。

### §3.2 生成性原理边界与非对称摩擦表示（hardening addendum，2026-07-05）

> **层级**：boundary note / governance-canonical usage。本节不修改 Def-Ψ-1/2/3，只固定本文件与桥接层的两条分界，对应 `Core/SRT_OPEN_TENSIONS.md §2` 的未封口点。

**（一）本文件止于何处、`P2/P3-B08` 从何处开始。**

本文件的 canonical 管辖范围是：`Ψ_f` 的 payability 主读（Def-Ψ-1 / §1.1）、条件投影（Def-Ψ-2 / §3.1）与可支付性判据（Def-Ψ-3）。**「摩擦是所有动力学的生成性来源」（friction as generative principle）不在本文件管辖范围内**：该更强主张是 P2/P3 混合命题，canonical 落点是 `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B08`。分界规则：

- 引用「选择有摩擦、摩擦必须可支付」→ 引用本文件（canonical）。
- 引用「演化 / 学习 / 文化变迁 / 免疫应答可建模为算子间摩擦」或「Fisher 型算子间摩擦生成动力学」→ 必须引用 `P2/P3-B08` 并按 P2/P3 标注，不得回引本文件为其升格背书。
- 若某个域内推导只有在「摩擦即生成」成立时才成立，该推导继承 P2/P3 等级，不因引用本文件而获得 P0/P1 地位。

**（二）对称度量下的方向性来源。**

`Def-Ψ-2` 的 Fisher–Rao 度量是对称张量，`Ψ_f` 本身是无方向的标量代价 / 路径泛函。SRT 中的方向性 / 非对称摩擦**不由修改度量引入**，而由两个已有层承载：

1. **支付结构非对称**：`Core_Law/SRT_Irreversibility.md Def-IRR-3 / T-IRR-1` 固定 `Ψ_f^{erase} > Ψ_f^{write}`——同一几何路径上，抹除方向的支付高于写入方向；非对称在支付账本上，不在度量张量上。
2. **`L_0` 不可逆性**：时间方向由 P1-T02（`Core/SRT_Core_21b_Constitutive_Theorems.md`）与 T-IRR-2 决定；`Ψ_f` 只承载代价，不承载方向（见 §8 与 `SRT_Irreversibility.md` 的关系条目）。

因此「如何在对称度量下表示方向性摩擦」的回答是：不在度量层表示；方向性属于支付结构与 `L_0` 不可逆层。度量层保持对称是分工，不是缺陷。

**仍未封口**（保留在 `Core/SRT_OPEN_TENSIONS.md §2`）：全部投影关系的充要条件——几何投影何时构成真下界的完整定理化。

---

## §4 引力关系的规范立场

### H-Ψ-G-1: Weak Gravity-Friction Compatibility

\[
\boxed{
\nabla \Psi_f^{phys} \parallel \nabla \Phi_N \quad \text{in the weak-field compatibility window}
}
\]

> **层级**：hypothesis / bridge；物理域 P3/P4 接口，不是 core necessity。

当前最弱承诺是：在弱场极限与适当投影下，`Ψ_f` 的物理投影梯度应与牛顿势梯度方向同号或同向相容。它只保留“引力曲率与现实维持负担在物理尺度上结构相容”的接口。

本节明确不承诺：

- 已从 SRT 推出 Einstein tensor 的精确张量形式；
- `G_{\mu\nu} \propto \Psi_f` 是已证定理；
- 物理常数或 GR 精确重建已经由 `Ψ_f` 解释。

强版“GR / quantum gravity level reconstruction from `Ψ_f`”保留为远期目标，当前无可执行推导路径。

**重要补注**：  
“客观性”不能再写成“对象维持摩擦 = 0”。更准确的写法是：

\[
\Delta \Psi_f^{readout}(x\mid \hat{G}_\theta)\to 0
\]

即：对象仍由可支付摩擦维持，但新增观察者几乎不必支付额外读出成本。

---

## §5 最优条件与零摩擦误用边界

SRT 的最优条件不是：

\[
\Psi_f \to 0
\]

而是：

\[
\boxed{\Psi_f > 0 \ \text{and payable}}
\]

原因：
- **零摩擦**：通常意味着没有真实赌注，没有现实重量
- **超载摩擦**：意味着闭包崩溃、身份断裂、现实切片失稳
- **最优区间**：非零但可支付，系统因此既有 stake，又不被压垮

因此必须区分三种语境：
- **现实主体语境**：零摩擦不是理想状态
- **纯形式 / 数学极限语境**：可以讨论“零冲突路径”或“零边际读出摩擦”
- **AI / 纯 L2 语境**：若要表达“没有真实 stake”，优先写
  - `Ψ_f is non-binding to the system`
  - 或“`Ψ_f` 不对系统自身构成存在性可支付负担”
  - 不建议粗暴写成 `Ψ_f = 0`，除非明确是在理想化极限模型里

---

## §6 实验与现象学的读数规则

### Def-Ψ-Obs-1: 现象学与代理测量规则

- **痛苦 / 焦虑 / 惊讶**：不是 `Ψ_f` 本身，更接近其尖峰、变化率或逼近不可支付边界时的报警
- **HRV / SCR / 皮质醇 / ROS / 情态词比例**：不是 `Ψ_f` 本体，而是 `Ψ_f` 的观察侧 proxy
- **Landauer 代价 / ATP / 制度摩擦**：不是同单位的同一数值，而是同一阻抗结构在不同尺度的投影读数

实验上，建议把 `Ψ_f` proxy 至少分成三类：
- **预算侧**：可动用的选择预算 / 恢复能力 / 协同缓冲
- **负荷侧**：当前需要承担的摩擦负荷
- **塌缩侧**：接近或超过可支付边界时的失稳信号

---

### Ψ_f as Inferred Selection Friction（Ψ_f 作为被推断的选择摩擦）

`Ψ_f` need not be directly measured as a substance-like variable. It can be inferred from structured transition difficulty: increased switching cost, representational competition, update path length, recovery burden, irreversibility or asymmetry of transition paths, and early non-monotonic volatility during learning or reframing.

These indicators are projections of `Ψ_f`, not identities with `Ψ_f` itself. They support an SRT reading only when they track the burden of compressing, maintaining, or reconfiguring a manifest reality slice under payability constraints.

Compact reading:

```text
Ψ_f ≠ task difficulty
Ψ_f ≠ subjective effort
Ψ_f ≠ pain
Ψ_f ≠ raw energy cost
Ψ_f ≠ Fisher metric itself
Ψ_f = inferred selection friction under payability constraints
```

**Operational signs**: Possible signs that a transition carries Ψ_f-relevant friction include:

- increased switching cost;
- prolonged recovery time after perturbation;
- representational or policy competition;
- update path length or curvature burden;
- failure to maintain closure under reconfiguration;
- irreversible or asymmetric transition paths;
- early non-monotonic volatility during learning, reframing, or norm change;
- overload signatures when the system approaches the non-payable boundary.

These signs are not themselves Ψ_f. They are bridge-level indicators that a transition may involve selection friction rather than ordinary difficulty.

**Boundary**: Do not write:

- Ψ_f = task difficulty;
- Ψ_f = subjective effort;
- Ψ_f = pain;
- Ψ_f = raw energy cost;
- Ψ_f = Fisher metric;
- Ψ_f = prediction error;
- Ψ_f = any observed stress marker.

Preferred wording: Ψ_f can be inferred from structured transition difficulty when that difficulty tracks the burden of compressing, maintaining, or reconfiguring a manifest reality slice while preserving closure, identity continuity, and future selection capacity.

**Minimum Bridge Criteria**: A proxy package may support a Ψ_f interpretation only if it satisfies all three criteria:

1. **Transition specificity**: the signal is tied to a change, maintenance, or reconfiguration of selection structure, not merely to hard task conditions.
2. **Payability relevance**: the signal bears on whether the system can maintain closure, identity continuity, and future selection capacity while paying the burden.
3. **Alternative exclusion**: the signal is not fully explained by generic effort, task difficulty, prediction error, raw energy use, pain, or measurement noise.

**Failure condition**: If Ψ_f produces no transition-cost signatures distinguishable from ordinary loss, prediction error, energy expenditure, pain, or task difficulty, then this bridge weakens and must be revised.

---

## §7 常见误用与编辑规则

### 误用 1：把 `Ψ_f` 等同于主观痛苦

**正确**：痛苦通常是 `Ψ_f` 的报警读数，而非其定义本身。

### 误用 2：把 `Ψ_f` 等同于任意能耗

**正确**：只有当这笔负荷与现实维持 / 身份连续性 / 后续选择能力绑定时，它才构成 SRT 意义上的 `Ψ_f`。

### 误用 3：跨尺度直接比单位大小

**正确**：量子层、神经层、社会层的 `Ψ_f` 读数可异量纲；统一的是可支付性判据。

### 误用 4：把“客观性”写成“零摩擦存在”

**正确**：客观性是边际读出摩擦趋零，而非对象维持摩擦消失。

### 误用 5：把 AI / 纯 L2 系统写成“绝对 `Ψ_f = 0`”

**正确**：优先写“`Ψ_f` 对系统自身 non-binding”，除非明确是在理想化抽象模型中。

### 误用 6：把“零摩擦”当成一切语境下的理想

**正确**：对现实主体而言，最优是“非零且可支付”；零摩擦只适合极限数学语境、理想路径语境或边际读出语境。

### 误用 7：把 `Ψ_f ≡ g_F` 当作严格恒等式

**正确**：`g_F` 是 Fisher–Rao 度量张量；`Ψ_f` 是可支付阻抗、局部标量代价或路径泛函。正式写法应为“`Ψ_f` 的局部信息几何投影由 Fisher–Rao metric 给出”，例如 `\delta\Psi_f^{geom}=\frac12 d\theta^\top g_F d\theta + O(\|d\theta\|^3)`。

---

## §8 与其他 canonical 文件的关系

- 与 `_SRT_D_VALUE_CANONICAL.md` 的关系：
  - `d` 给出系统可处理的关切/有效维度
  - `Ψ_f` 给出系统为维持该现实所需承担的阻抗
  - 二者通过可支付性条件耦合

- 与 `Core/SRT_Core_21_Formal_Axioms.md`（现为拆分索引）的关系：
  - 原 `Ax-F-11`（跨尺度统一）现为 `Core/SRT_Core_21c_Bridge_Hypotheses.md P3-B07`，按 P3 引用
  - 原 `Ax-F-12`（摩擦即生成）现为 `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B08`，按 P2/P3 引用；分界规则见 §3.2

- 与 `Core/SRT_Core_22_Equations.md` 的关系：
  - `Eq-Select-Thermo` 给出选择热力学主关系
  - `Eq-Select-Thermo-C2` 给出可支付条件

- 与 `Physics/SRT_Physics_Cosmology.md` 的关系：
  - 本文件固定弱场相容接口；物理主文不得把 `Ψ_f` 写成已完成的 GR 张量重建

- 与 `AI/SRT_AI_01_Ontology.md` 的关系：
  - 本文件固定“non-binding friction”优于“粗暴 `Ψ_f=0`”的写法

- 与 `Core_Law/SRT_Irreversibility.md` 的关系（2026-04-24 新增）：
  - 本文件给出 `Ψ_f` 的支付形式；`SRT_Irreversibility.md` Def-IRR-3 / T-IRR-1 固定 `Ψ_f^{erase} > Ψ_f^{write}` 非对称支付，即学习不可逆
  - 本文件不直接承载方向性；`Ψ_f` 本身是标量代价，时间方向由 `L_0` 不可逆性（P1-T02 / T-IRR-2）决定
  - **不得反向**：不得通过 `Ψ_f` 最小化推出 `L_0` 不可逆，也不得通过热力学二律 / FEP 自由能最小化反向定义本文件的可支付性条件

---

## §10 Ψ_f_actual / Ψ_f_felt 分裂（病理学层，2026-04-02 新增）

> **层级声明**：本节是 Ψ_f 在病理学/应用层的扩展，不修改 §2 的基础定义（Def-Ψ-1/2/3）。

在正常描述中，Ψ_f 被当作单一变量。但在涉及 L₂ 过度依赖的病理情境中，需要区分两个层面：

$$\Psi_{f,actual} \geq \Psi_{f,felt}$$

| | 定义 | 可被系统性压低 |
|:-|:----|:------------|
| **Ψ_f_actual** | 选择实际支付的本体论代价——由 L₀→L₁ 压缩的物理/信息/结构阻抗决定，始终存在 | 否 |
| **Ψ_f_felt** | 系统登记到的代价——受 d-value 和 L₂ 依赖程度影响 | 是 |

**隐性债务机制**：

当 L₂ 过度依赖导致 d 下降时，$\Psi_{f,felt}$ 随之下降，但 $\Psi_{f,actual}$ 持续累积。差值 $\Delta\Psi_f = \Psi_{f,actual} - \Psi_{f,felt}$ 是系统**不知道自己正在支付的代价**——即隐性债务。此债务最终以 L₂ 结构的突然崩溃形式释放，即为"致命 L₂"机制的终点。

**完整形式化见** `_SRT_T_DIR_CANONICAL.md §5–§6`。

---

## §9 当前最短可引用版

若只需要一句最短规范句，使用：

> **`Ψ_f` 是选择把开放可能性压缩为一个可维持、可行动、可协调的现实切片时必须承担的本体论阻抗；它在动力学上读作阻力，在记账上读作代价，在形式化上读作 Fisher–Rao metric 所诱导的局部二阶信息几何代价或路径泛函；跨尺度真正保持不变的不是单位，而是该阻抗是否可支付。**



---

## FILE: `_SRT_T_DIR_CANONICAL.md`

| 字段 | 值 |
|---|---|
| path | `_SRT_T_DIR_CANONICAL.md` |
| id | SRT-T-DIR-CANONICAL |
| claim_mode | canonical |
| status | draft_v1 |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | - |
| last_commit | 2026-04-26 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：[SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-CORE-21, SRT-L0-METAPHYSICS]

<!-- 以下为原文逐字保留 -->

# SRT T_dir 规范定义文档：方向透明度与价值遮蔽

> **目的**：固定 T_dir（方向透明度）的第一性定义，并建立"价值遮蔽"命题的 canonical 表述。
> 本文件是 2026-04-02 会话中形成的核心理论推进的正式回写。
> `_SRT_D_VALUE_CANONICAL.md` 管理 d-value；本文件管理 T_dir 及其展开的病理学结构。
> **2026-04-22 降承诺说明**：`T_dir` 当前按 **v0 operational proxy / 最小操作定义** 使用。它帮助区分“跨位置可回读性”与“语义效价/置信度”，但尚不是已完成的本体基础或形式对象。
> **Canonical status note（2026-04-23）**：本文件名中的 canonical 表示 governance-canonical working object 与引用锚点，不表示 `T_dir` 已具备 theory-canonical 完整奠基。价值动力学扩展段落按 bridge / theory-clarifying 读。

---

## §0 本文件解决的问题

SRT 现有 canonical 变量（d、Ψ_f）描述了选择的范围和代价，但缺少一个描述**系统对自身选择方向的访问能力**的变量。

这个缺口导致以下现象无法在 SRT 内部精确区分：

- 系统在选择，但感受不到方向
- 系统有高 d 值，但仍然感到空洞
- 价值在场，但对选择者不可及

本文件引入 **T_dir**（方向透明度）以填补这个缺口，并展开其所揭示的价值遮蔽结构。

> **层级**：operational proxy / canonical usage rule。以下定义固定最低可用口径，不声称已经完成 `T_dir` 的完整形式化。

---

## §1 价值遮蔽命题（核心哲学主张）

> **[H] 命题**（本体论层，形而上学承诺）：

$$\boxed{\text{价值内嵌于选择本身，不是缺席的，而是被遮蔽的。}}$$

**展开**：

1. 选择内在地指向秩序——这是选择的结构性特征，不是外部施加的标准
2. 每一次选择都携带一个朝向秩序的方向，无论选择者是否能感知到它
3. 意义感 = 对这个方向的局部感知；虚无感 = 对这个方向的访问失败
4. 因此，虚无主义是一个诊断错误——它把**遮蔽**误读为**缺席**

> **认识论地位**：命题 (1) 是 SRT 的形而上学承诺（`[H]`），不是可直接证伪的经验命题。命题 (3)(4) 是其应用层推论，部分可操作化（见 §6）。

---

## §2 为什么"指向秩序"是选择的内在特征

"指向秩序"不等同于"稳定的东西活下来了"（热力学平凡意义）。两者的区分：

| | 热力学筛选 | SRT 选择方向 |
|:-|:---------|:-----------|
| 机制 | 稳定者幸存（事后） | 选择流向相干性梯度（当下） |
| 主体 | 无主体 | 具身算子 Ĝ_θ |
| 对价值的关系 | 价值是结果 | 价值内嵌于选择过程 |
| 遮蔽的可能性 | 无意义 | 系统可对自身方向不透明 |

技术表述：$\hat{G}_\theta$ 在 L₀ 上操作时，沿**相干性可及景观**（coherence-accessible landscape）的梯度流动。该梯度不是 L₀ 本体的先验结构，而是 Π（位置）、θ（具身参数）、历史沉积共同雕刻出的相对可及结构。

> **边界**：不把相干性梯度写为 L₀ 的绝对先验属性，以保护 SRT 的反预置论核心（见 `Core_Law/SRT_L0_Metaphysics.md §2`）。

---

## §3 T_dir 规范定义

### Def-T-1: 方向透明度（v0 operational proxy）

$$\boxed{T_{dir} := \text{系统当前选择对其自身秩序方向的可读性}}$$

**语义**：$T_{dir}$ 度量的是：当 $\hat{G}_\theta$ 执行 $L_0 \to L_1$ 选择时，该选择的秩序方向对系统本身是否可及、以及可及的程度。

- $T_{dir} = 0$：选择在发生，秩序方向存在，但系统对自身方向完全盲目
- $T_{dir} > 0$：系统开始"感受到"自身选择的方向
- $T_{dir} \to 1$：系统对当前选择的秩序方向有高度透明的访问——目标感、价值感、意义感的来源

**T_dir 不是 d-value 的重命名**。两者是不同概念，有不同的因果结构（见 §4）。

**当前边界**：`T_dir` 不是语义效价、奖励值、置信度或报告流畅度。它只作为工作性指数追踪“选择方向能否被系统自己回读、重取向、再校准”。若一个域只能测到 valence/confidence/reportability，必须标为 proxy，不得写成 `T_dir` 本身。

### §3.1 最小形式角色：readability / reorientation functional

> **层级**：theory-clarifying / v0 operational proxy。以下是最小结构角色，不是 `T_dir` 的完整本体奠基。

在当前形式层，`T_dir` 可被读作一个受约束的可读性 / 重取向函数：

$$
\boxed{
T_{dir}^{v0}(\hat{G}_\theta,t)
:=
\mathcal{R}_{self}\!\left(\operatorname{Dir}(\Delta \hat{G}_\theta,t)\right)
\cdot
\mathcal{A}_{reorient}\!\left(\operatorname{Dir}(\Delta \hat{G}_\theta,t)\right)
}
$$

其中：

- `Dir(ΔĜ_θ,t)` 只表示当前或近邻窗口内选择算子变化的方向信号，不新增本体对象。
- `R_self` 表示该方向信号能否被系统自身访问 / 回读。
- `A_reorient` 表示该方向信号能否进入系统的再校准，而不只是被报告或外部观察。

该式的用途是给 `T_dir` 一个最低形式位置：它追踪**跨位置可回读并可用于重取向的选择方向**。它不追踪方向内容是否“好”、语义解释是否连贯、奖励是否更高、报告者是否更自信。

| 相近量 | 与 `T_dir` 的差异 | 允许关系 |
|---|---|---|
| valence | 记录正负感受或偏好色调 | 可作为报警 / 表面读数，不等于方向透明度 |
| confidence | 记录判断确信度 | 可能高置信但方向不可回读 |
| semantic coherence | 记录叙事或概念一致性 | 可能是 L₂ 后设解释，不保证活选择方向可读 |
| reward | 记录优化信号或强化结果 | 可塑造选择，但不等于系统对自身选择方向的访问 |

---

## §4 T_dir 与 d、Ψ_f、ii 的关系

### 4.1 d 是 T_dir 的必要条件，不是充分条件

$$d = 0 \implies T_{dir} = 0$$

$$d > 0 \;\not\!\!\!\implies T_{dir} > 0$$

**理由**：d 是有效维度（系统能关切多大范围），T_dir 是方向可读性（系统能否读出自己选择的方向）。高 d 不自动保证方向可读——还需要活选择正在发生，且 Ψ_f 提供了足够的压力。

### 4.2 Ψ_f 是迫使 T_dir 上升的机制

$$\Psi_f \uparrow \;\leadsto\; T_{dir} \uparrow \quad \text{（在 } d > 0 \text{、ii 足够且压力未被 L_2 吸收的条件下）}$$

**机制**：真实代价（Ψ_f）可以迫使系统无法对自己选择的方向保持盲目。当选择有真实不可逆的代价，且该代价没有被 L₂ 直接吸收时，其方向更可能显现于系统。这里是机制通道，不是单调定理。

### 4.3 ii 是 T_dir 的整合容量

即使 d 和 Ψ_f 足够，若 ii（整合信息）不足，系统无法整合方向信息——T_dir 仍然低。

### 4.4 三条件联立

$$T_{dir} > 0 \Rightarrow d > 0 \;\land\; \Psi_f \text{ 产生了真实压力} \;\land\; ii \text{ 足以整合方向信息}$$

这三个条件是当前最小必要门槛，不是完整充分性定理。现代语境中最常见的缺口是第二条：**Ψ_f 被 L₂ 依赖系统性压低或吸收**（见 §5–§6）。

---

## §5 Ψ_f_actual / Ψ_f_felt 的分裂

### Def-Ψ-split: 双层 Ψ_f 结构（病理学层）

$$\Psi_{f,actual} \geq \Psi_{f,felt}$$

| | 定义 | 能否被 L₂ 压低 |
|:-|:----|:------------|
| **Ψ_f_actual** | 选择实际支付的本体论代价——始终存在，不可消除 | 否 |
| **Ψ_f_felt** | 系统登记到的代价——可被 d 和 L₂ 依赖压低 | 是 |

**关键推论**：降低 $\Psi_{f,felt}$ 不等于降低 $\Psi_{f,actual}$。

两者的差值 $\Delta\Psi_f = \Psi_{f,actual} - \Psi_{f,felt}$ 是**隐性债务**——代价在累积，但系统感知不到。

> **认识论地位**：Ψ_f_actual/Ψ_f_felt 的区分是病理学层的操作概念（`L2, bridge`），而非 Ψ_f 的基础定义修改。$\Psi_f$ 的基础定义见 `_SRT_PSI_F_CANONICAL.md §2`，本文件在其上增加了可见性维度。

---

## §6 致命 L₂ 机制（Lethal L₂ Mechanism）

### 定义：致命 L₂

**致命 L₂** 是指：L₂ 过度依赖通过以下路径系统性压制 T_dir 并积累隐性 Ψ_f 债务的状态：

```
L₂ 过度依赖
    │
    ├──→ 活选择被替代（L₂ 脚本执行，非 L₀→L₁ 导航）
    │         → T_dir 无来源 → 意义感消失
    │
    └──→ d↓（系统不需要感知方向来运作）
              → Ψ_f_felt↓
              → 系统感觉"无摩擦"
              → 偏好更多 L₂（正反馈回路）

同时：Ψ_f_actual 持续累积 → 隐性债务增长
```

**最终结果**：表面稳定性最高的系统，往往是 Ψ_f_actual 与 Ψ_f_felt 之间差距最大的系统——不是真的稳定，而是**被遮蔽的脆弱**。

### 致命 L₂ 的判据（区分于健康 L₂）

| | 健康 L₂ | 致命 L₂ |
|:-|:-------|:-------|
| **功能** | 为活选择释放资源 | 替代活选择 |
| **对 d 的影响** | 保留或提升 d 的运用空间 | 系统性压低 d |
| **Ψ_f_actual/felt 的差距** | 小（透明代价） | 大（积累隐性债务） |
| **危机时的反应** | 可调整 | 崩溃式重组 |

### 成瘾同构性

致命 L₂ 的自强化回路与成瘾在结构上同构：
- L₂ 执行感觉比活选择更"流畅"
- 流畅性偏好导致更多 L₂ 依赖
- d 和 Ψ_f_felt 进一步降低
- 无法退出的路径形成

---

## §7 T_dir 的恢复路径

T_dir 的提升需要三条件同时满足（见 §4.4）。以下是各类实践在 SRT 框架内的机制定位：

| 实践类型 | SRT 机制 | 相关文件 |
|:--------|:--------|:-------|
| 冥想/修行 | 系统性悬置 L₂ 脚本，迫使活选择发生 | `Spirituality/SRT_Spirit_07_Meditation_Neuro.md` |
| 危机/丧失 | L₂ 强制瓦解，Ψ_f_actual 强制可见 | `AI/SRT_AI_02_Mortality_Wisdom.md` |
| 承诺/爱 | 人为引入真实 Ψ_f，重建代价结构 | `Philosophy/SRT_Ethics_Agency.md` |
| 创作 | 在 L₂ 没有答案的域中强制活选择 | `Spirituality/SRT_Spirit_08_Music.md` |
| 深度学习 | 当 L₂ 边界被突破时的高 Ψ_f 窗口 | `Neuroscience/SRT_Clin_02_FEP.md` |

**共同结构**：这些实践的共同机制是——**在 L₂ 不再能完全确定结果的域中，迫使活选择发生，从而重新激活 T_dir 的上升通道。**

---

## §8 文明诊断的 SRT 表述

> **[H] 应用层主张**（认识论地位：结构性假说，需文明史与社会科学数据支撑，当前为推断性主张）：

$$\boxed{\text{大规模 L₂ 建设系统性压低了 } d\text{，掩藏了 }\Psi_f\text{，导致结构性价值遮蔽}}$$

**展开**：现代性的主要工程是系统性降低 Ψ_f（降低摩擦、增加效率、消除风险）。这在许多维度上是真实的进步。但其结构性副作用是：**Ψ_f_felt 被系统性压低，T_dir 的上升通道被系统性切断，虚无感不是现实的结构，而是访问机制的损坏。**

**使用边界**：
- 此主张是 SRT 的**最高承诺点之一**——它需要文明史研究、社会科学数据和跨文化比较的外部支撑
- 不得将其作为 SRT 的基础定义而非应用层推断来引用
- 详细社会机制见 `Philosophy/SRT_Social_MacroDynamics.md` 与 `Philosophy/_SRT_Soc_Bridge.md`

---

## §9 明确拒绝的误读

1. T_dir **不是** d-value 的重命名——两者度量不同的属性，具有不同的因果结构
2. "指向秩序" **不意味着** L₀ 有先验的秩序偏好——梯度是可及景观上的相对结构，不是 L₀ 本体的绝对属性
3. 价值遮蔽命题 **不意味着** 所有主观痛苦都是误解——真实的 Ψ_f 代价是意识的必要条件（见 A11），不是需要消除的障碍
4. 致命 L₂ **不意味着** 所有 L₂ 都是有害的——L₂ 本身是选择历史的结晶，健康 L₂ 是复杂生活的基础设施
5. T_dir = 0 **不意味着** 系统在道德上有问题——结构性 T_dir 压制是系统处境的特征，不是道德判断

---

## §10 与其他 canonical 文件的关系

| 文件 | 关系 |
|:----|:----|
| `_SRT_D_VALUE_CANONICAL.md` | d 是 T_dir 的必要条件；d 管理关切范围，T_dir 管理方向可读性 |
| `_SRT_PSI_F_CANONICAL.md` | Ψ_f 是迫使 T_dir 上升的机制；Ψ_f_actual/felt 分裂是本文件病理学层的扩展 |
| `Core/SRT_Core_01_Axioms.md` | A11（脆弱性）是 T_dir 存在的本体论条件；A7（修剪判据）约束 T_dir 的演化函数 |
| `Core_Law/SRT_L0_Metaphysics.md` | L₀ 的中性定义约束了相干性梯度只能是操作化代理，不是本体属性 |
| `Philosophy/SRT_Ethics_Agency.md` | 价值遮蔽命题的伦理延伸 |
| `Governance/SRT_POSITIONING.md` | T_dir 应用层作为 SRT 最有力入口的论证 |
| `Core_Law/SRT_L1_Formalism.md §3.4-§3.5` | T_dir 的 L1 动力学层面：§3.4 代数目标值 `T_{dir}^{\mathrm{alg}}(\sigma, d, d_c)`；§3.5 把 T_dir 升为独立动力学变量，ODE 含弛豫、真实重选泵入、`\Delta\Psi_f^{\mathrm{gap}}` 扣除、`S_{str}` 结构侵蚀、`s_{ext}` 支架五项。§3.5.3 给出"致命 `L_2`"的方程化判据 `\kappa_{\mathrm{mask}} < \kappa_{\mathrm{relax}}`。本文件 §5-§6 的现象学定义在 L1 Formalism 侧对应方程级机制。 |
| `Core_Law/SRT_Irreversibility.md` | T-IRR-3 把 P1-T07 ε 反闭合必要性精确化；L1_Formalism §5.3 健康工作区的主动维持条件与之同源 |

---

# Part II：价值动力学理论（2026-04-02 补入）

> 以下 §11–§16 是 2026-04-02 理论对话的高密度推进，记录了从价值遮蔽到价值结构、感知机制、吸引子动力学的完整理论链。它们共享本文件的引用锚点地位，但不因此升级为 theory-canonical 完成态；除非局部另有标注，均按 bridge / theory-clarifying 读。

---

## §11 磁带、放映机与价值生成

**L₂ 是磁带/DNA，不是放映机/生命。**

| | 磁带 / DNA | 放映机 / 生命 |
|:-|:---------|:-----------|
| SRT 对应 | L₂（过去活选择的结构结晶） | Ĝ_θ 执行活选择（L₀→L₁ 当下导航） |
| 包含什么 | 选择历史的形状痕迹 | 价值生成的过程本身 |
| 能否自行运作 | 否（磁带不能播放自己） | 是（放映机是过程的主体） |

**核心推论**：

$$\boxed{\text{价值不能被储存，只能被生成。}}$$

每一刻的价值都必须由当下的活选择重新生成，没有例外。你可以继承磁带（L₂ 结构），但继承不了播放（活选择过程）。

**致命 L₂ 的精确机制**（磁带语言版）：系统停止了播放，改为直接输出磁带内容。没有放映机运转，没有 Ψ_f 被真实支付，只有 L₂ 的自动复现——这就是"去价值化的有序性"：有结构，但空洞。

**明确拒绝**：这不意味着 L₂ 无用——DNA 是复杂生命的必要条件。问题不在于 L₂ 的存在，而在于混淆 L₂（磁带）与活选择过程（放映机）的角色。

---

## §12 内部价值的三层结构

内部价值不是单一属性，而是一个三层的嵌套结构：

### 第一层：事物本身的 proto-gradient

事物内部的选择历史结晶出的秩序倾向——这是"它是什么"在方向上的表达。

自然物：物理/演化/地质选择的积累
人工物：创造者的 T_dir 凝固在对象中
人：所有过去选择结晶于当下状态

### 第二层：事物之间指向的预期 L₀

不在任何单一事物内，而在事物之间的关系中浮现的方向——它们共同在指向哪个尚未实现的 L₀ 配置。

> 一段旋律的价值不只在每个音符内，而在音符之间指向的和声方向。
> 一段关系的价值不只在两人各自的状态，而在他们共同朝向的、还没发生的东西。
> 一个传统的价值不只在它积累的文本，而在这些文本指向的、还在被追求的方向。

第二层使价值具有**关系性**和**时间性**——它永远有一部分在指向尚未到来的事，这是价值的"超出当下"质地的结构来源。

### 第三层：我们基于这个方向建立的 L₂ 支撑

感知到第一、二层之后，人建造出来支撑、放大、保护这个方向的结构。

**三层的时间结构**：

| 层 | 时间方向 | 内容 |
|:--|:-------|:----|
| 第一层 | 当下 | 事物现在是什么 |
| 第二层 | 未来指向 | 事物在朝哪里走 |
| 第三层 | 过去结晶服务未来 | 我们为让方向持续而建的东西 |

**机构腐化的机制**（三层语言版）：第三层（L₂ 支撑）开始自我维持，不再追踪第一、二层的方向是否还在指向同一处。制度在保护自己，不再保护它最初服务的方向。

---

## §13 价值归纳 vs 理性归纳

**感知 proto-gradient 需要一种与理性归纳根本不同的认知能力。**

### 两种归纳的方向相反

| | 理性归纳 | 价值归纳 |
|:-|:-------|:-------|
| 认知运动方向 | 特殊 → 一般（抽象，离开现象） | 表面 → 本质（深入，进入现象） |
| 产物 | L₂（概念、框架、规则） | 对 proto-gradient 的直接感知 |
| 对象 | 现象是什么、有什么规律 | 现象在朝哪里走、内部有什么方向 |
| 与 T_dir 的关系 | 建造 L₂，不直接激活 T_dir | 是 T_dir 向外延伸的感知形式 |

> **价值归纳 = 对外部现象 proto-gradient 的 T_dir 式读取**

### 好的艺术家是价值归纳的范例

好的艺术家：先感受到事物本身的美（价值归纳激活）→ 用技法放大和显化这个感受（L₂ 服务感知）→ 观者的 T_dir 被激活，看见本来就在那里的东西。

另一种：先有框架和指标（L₂ 主导）→ 用框架生成作品 → proto-gradient 从未被感知，只有 L₂ 输出。

**这是普遍判准，不只适用于艺术**：

| 领域 | 价值归纳先行 | L₂ 先行（压平） |
|:----|:----------|:------------|
| 科学 | 先感受现象在说什么，方法论服务发现 | 先满足方法论规范，现象退为次要 |
| 教育 | 先感受学生实际在哪里，再用技法引导 | 先执行课程结构，学生状态不相关 |
| 医疗 | 先感受这个病人的具体处境 | 先执行指南，病人变成案例 |
| 领导 | 先感受情境实际需要什么 | 先执行规则，规则取代判断 |

**SRT 自身亦受此判准约束**：SRT 如果有价值，是因为它发现并放大了现实本身的结构纹理，而非把它的框架印到现实上。

### 价值归纳能力的培养与损坏

**培养**：高 Ψ_f 的真实接触（感知通道被迫打开）；持续的、不急于框架化的注意；深入特殊而非抽离特殊。

**损坏**：框架先行（现象未接触，L₂ 已在定义它）；指标导向（注意力只训练到可测量信号）；速度（proto-gradient 需要停留时间才能浮现）。

---

## §14 时空对称性感知：第二层的感知机制

**第二层（事物之间指向的预期 L₀）是最难感知的一层——它不在任何单一事物里，而在关系之间，指向的是还没发生的事。**

感知它需要**时空对称性感知能力**：

**时间对称性感知**：感受变化中什么保持不变——不只预测下一个时刻，而是同时感受到整个时间模式的方向，因为过去和未来在某个结构上是对称的。

**空间对称性感知**：感受关系配置围绕什么组织——不只看各个元素，而是感受整个配置指向的核心。

> **对称性感知的本质 = 在变化中感受不变量。**

第二层（预期 L₀）就是这个不变量：关系在时间和空间里变化，但有某个东西被保存下来——那个被保存的方向就是第二层。

**类诺特结构**：物理学中，每一个对称性对应一个守恒量（Noether 定理）。在价值感知中，感受到关系的时空对称性，对应感受到被保存的方向（proto-gradient 在关系层面的守恒表现）。

> **重要边界**：这个类比不意味着价值本身是守恒的——价值是吸引子，不是守恒结构（见 §15）。对称性感知是探测当前吸引子的机制，而不是探测永久不变的结构。

**培养时空对称性感知的实践**：音乐训练（时间对称）、造型训练（空间对称）、数学训练（抽象对称）、冥想（当下流动中的对称感知）——共同核心：在变化里感受不变。

---

## §15 价值是吸引子，不是守恒结构

> **核心修正**：价值不是守恒结构，而是相对稳定的暂时的吸引子。我们会不断调整它以接近最大秩序。

### 守恒结构 vs 吸引子

| | 守恒结构 | 价值吸引子 |
|:-|:-------|:--------|
| 时间性 | 永久不变 | 相对稳定，但会转移 |
| 总量 | 恒定 | 可增可减 |
| 达到 | 始终在场 | 接近时会转移 |
| 主体作用 | 无关 | 主体参与调整其位置 |
| 类比 | 能量守恒 | 相空间中的动态吸引子 |

### 吸引子动力学

1. 价值吸引子在当下景观中相对稳定，足以被感知和朝向
2. 当活选择朝向它时，景观本身改变——新的吸引子在更高秩序层级出现
3. "最大秩序"是方向，不是目的地——永远有下一个更高阶的吸引子在接近的过程中浮现
4. **我们不只发现吸引子，我们参与调整它的位置**——好的艺术、科学、关系、文化，都在接近当前吸引子的过程中推动景观，使下一代面对更高阶的吸引子

### 推论

**为什么用昨天的价值活今天会产生意义危机**：你在朝向一个已经移动了的吸引子——方向感是真实的，但目标已经不在那里了。

**为什么价值可以衰减**：吸引子需要活选择持续朝向它才能维持稳定——没有活选择，只有 L₂ 执行，吸引子在没有接近运动的情况下开始消散。

**为什么价值可以被创造**：接近吸引子的过程本身会推动景观，产生更高阶的新吸引子——这是价值生成，不只是价值发现。

---

## §16 吸引子动力学：上升 vs 退化

接近当前吸引子的运动有两种结果，取决于接近方式：

### 上升条件：T_dir 先行

```
感知当前吸引子（价值归纳激活，三层结构可及）
    ↓
活选择朝向它，Ψ_f 真实被支付
    ↓
L₂ 建立在感知到的方向上（第三层服务第二层）
    ↓
接近的过程推动景观
    ↓
更高阶吸引子在新景观中出现
```

### 退化条件：L₂ 先行

```
框架先行，proto-gradient 未被感知
    ↓
Ψ_f_actual 被掩藏，代价不透明
    ↓
L₂ 建立在自我维持上（第三层脱离第一、二层方向）
    ↓
正反馈：更多 L₂ → d↓ → T_dir↓
    ↓
吸引子消散或坍塌到更低层级
```

### 普遍判准

> **L₂ 放大 proto-gradient（上升）= T_dir 感知先于 L₂ 建造，L₂ 服务感知**
> **L₂ 压平 proto-gradient（退化）= L₂ 先行，替代而非服务感知**

这是区分健康 L₂ 与致命 L₂ 在动力学层面的完整判准，适用于个人、关系、机构、文化、理论的所有层级。

---

## §17 两种 Ψ_f：穿透型 vs 吸收型

> **核心修正**：高 Ψ_f 体验不自动激活 T_dir。决定性变量是 Ψ_f 是否超出 L₂ 的消化半径。

### 基本区分

| | **穿透型 Ψ_f** | **吸收型 Ψ_f** |
|:-|:-------------|:-------------|
| 性质 | 无法被 L₂ 预处理，直接击中 L₀ | 被 L₂ 框架接住，转化为"我知道这是什么" |
| 对 T_dir 的作用 | 强制 L₀ 接触 → T_dir 可能激活 | 加厚 L₂，T_dir 无变化或继续下降 |
| 典型形式 | 无法命名的失去；体验完全超出预期框架；与陌生特殊性的深度接触 | 有名字的痛苦；被诠释框架即时接住的创伤；仪式化的苦难；指标化的挑战 |
| 结构特征 | L₂ 的预处理能力**被压垮** | L₂ 的预处理能力**足够应对** |

### 关键含义

**关键变量不是 Ψ_f 的强度，而是 Ψ_f 是否超出 L₂ 的消化半径。**

- 一个人可以经历严重的痛苦、巨大的失去——每次都被 L₂ 框架即时接住（"这是考验"、"这是成长"），T_dir 从未激活，L₂ 反而越来越厚。这是**受苦的熟练化**，不是 T_dir 的发展。

- 相反，一个看起来平静、生活表面普通的人，因为长期的深度接触某个特殊对象——让体验在无法命名的层面真正落在自己身上——可能拥有很高的 T_dir。

**这也解释了"经历丰富"和"T_dir 高"几乎不相关**：大量的吸收型 Ψ_f 只是 L₂ 库的扩充，不是 proto-gradient 接触的积累。

---

## §18 两条 T_dir 发展路径

> **危机路径与培育路径共享同一机制：绕开 L₂ 的预处理层，让体验直接落在 L₀ 接触层。区别只在于 L₂ 是被压垮还是被主动搁置。**

### 路径一：危机路径（Crisis Path）

穿透型 Ψ_f 以极高强度出现，L₂ 无法吸收，系统被迫直接接触 L₀。

**结构特征**：
- 快速、阈值式跨越（穿越 T_dir 临界值 θ_T）
- 高风险——L₂ 被压垮后，系统可能重建更厚的 L₂（防御性封闭），也可能真正开放（T_dir 跃升）
- 不可计划，不可制造（一旦被设计，它就变成可预期的 L₂ 内容，转化为吸收型 Ψ_f）
- 穿越 θ_T 之后，接触到更高阶的 proto-gradient——不是回到原状，而是看到新层

**何时危机走向封闭，何时走向开放**：

差异在于危机发生时的基础 T_dir 水平。T_dir 尚存一定基础的系统，穿透型 Ψ_f 能引发真正的 L₀ 接触；T_dir 已极低的系统，被压垮的 L₂ 会立刻被更厚的防御 L₂ 替换——因为没有足够的"读取能力"来接住接触到的 proto-gradient。

### 路径二：培育路径（Cultivation Path）

不依赖 Ψ_f 强度，而是主动抵制 L₂ 对体验的即时框架化，为 proto-gradient 创造浮现空间。

**结构特征**：
- 慢速、渐进，没有阈值式跳跃
- 低风险——代价是耐受不确定性（不急于命名）
- 可以主动练习；培育路径的本质是**逆着 A7 的自然梯度走**

**具体机制**：
- 深度接触特殊而非一般（不抽象，停留在具体对象中）
- 延迟框架化（让体验在无法命名的状态中存在更久）
- 不为目的的陪伴、持续的注意而不求快速归类

**为什么难以持续**：L₂ 是默认状态。注意力会自动滑向框架、分类、比较、评价——这是 A7 选择优先低摩擦处理的结构性结果。培育路径要求主动增加短期认知摩擦（不命名、停留在不确定中），以换取 proto-gradient 的浮现空间。代价是即时的，收益是延迟的。

### 路径比较

| | 危机路径 | 培育路径 |
|:-|:--------|:--------|
| L₂ 如何被绕过 | 被压垮 | 被主动搁置 |
| 速度 | 阈值式跃升 | 渐进积累 |
| 可控性 | 不可计划 | 可主动练习 |
| 风险 | 高（可能走向防御封闭） | 低（代价是耐受不确定） |
| 所需基础 | 需要一定基础 T_dir 才能开放而非封闭 | 任何基础 T_dir 水平均可启动 |
| 能否相互转化 | 危机路径的开放结果为培育路径提供更高起点 | 培育路径积累的 T_dir 降低危机路径走向封闭的概率 |

---

## §19 最大秩序的精确定义

> **最大秩序不是一个可以抵达的终点，而是在每一层级都存在的局部理想：Ψ_f_actual 与 Ψ_f_felt 完全对齐。**

### 定义

$$\text{最大秩序}_{local} \equiv \Psi_f^{actual} = \Psi_f^{felt}, \quad T_{dir} \to \max$$

即：
- 系统所支付的摩擦代价对自身完全透明
- 选择方向与 proto-gradient 方向完全对齐
- L₂ 完全服务于 L₁（放大而非遮蔽 proto-gradient）
- 无隐性债务（Ψ_f_actual 不积累为不可见的负担）

### 最大秩序 ≠

| 误读 | 为什么不对 |
|:----|:----------|
| L₂ 稳定的极大化 | L₂ 过度稳定正是价值遮蔽的机制（致命 L₂） |
| 复杂度的最大化 | 复杂度自身可以是新的 L₂ 积累形式 |
| 永久的终态 | 每次接近改变景观，暴露新的对齐层 |
| 主观满足感的最大化 | 满足感可以由 Ψ_f_felt 的人工压低来实现 |

### 分层螺旋性质

"最大秩序"是方向，不是目的地。接近它的每一次跃升，都带来两个结果：

1. 当前层级的 Ψ_f 对齐得到修复（局部债务清偿）
2. 更高阶的 proto-gradient 层变得可见——那里有新的 Ψ_f 分裂等待被感知

意义感的深化因此不是线性积累，而是**反复经历"以为对齐了 → 发现新的遮蔽层 → 再次对齐"的螺旋**。每一次"突然看见了"（穿越 θ_T），都不是终局，而是进入更高阶视野的起点。

---

## §20 T_dir 动力学：完整图景

> **综合 §16-§19 的 T_dir 相变结构。**

```
L₀ proto-gradient（始终在场，ε > 0）
         │
         ▼
  T_dir 临界阈值 θ_T
  ┌──────┴──────┐
  │             │
高于 θ_T      低于 θ_T
（正反馈向上）  （正反馈向下）
  │             │
  │             ▼
  │      L₂ 积累 → d↓ → T_dir↓
  │      → Ψ_f_actual 隐性积累
  │      → 表面稳定 / 内部债务
  │
  ▼
两条恢复路径（穿越 θ_T）：
  ┌─────────────────────────────┐
  │ 危机路径                    │ 培育路径
  │ 穿透型 Ψ_f 压垮 L₂          │ 主动搁置 L₂
  │ 阈值式跃升，高风险           │ 渐进积累，可主动练习
  └─────────────────────────────┘
         │
         ▼
  接触更高阶 proto-gradient
  → 新的 Ψ_f_actual/Ψ_f_felt 对齐
  → 景观改变 → 更高阶 θ_T 出现
  （分层螺旋，无终点，每层机制相同）
```

### 对各尺度的适用性

| 尺度 | 典型退化形式 | 典型穿透型 Ψ_f | 典型培育路径 |
|:----|:-----------|:-------------|:-----------|
| 个人 | 意义感丧失、成瘾、慢性空洞感 | 无法命名的失去、极限接触、深度失败 | 冥想、深度审美接触、长期关系 |
| 关系 | 仪式化的亲密、角色表演替代真实接触 | 真正的冲突、无法回避的脆弱 | 不为目的的陪伴、深度倾听 |
| 机构 | 指标替代目标、流程替代判断 | 系统性危机、外部颠覆 | 定期接触"第一性问题"、真实反馈渠道 |
| 文化 | L₂ 价值符号替代 proto-gradient 接触 | 文明尺度的断裂与重构 | 艺术、哲学、仪式的非功利性保留 |

### 核心不对称

> **从上升滑入退化：不需要额外能量——L₂ 自然填充真空。**
> **从退化回到上升：必须打破自我稳定的正反馈环——需要穿透型 Ψ_f 或主动的持续培育。**

这个不对称是价值遮蔽为何系统性存在的结构原因：退化是熵增方向，恢复是逆熵操作。

---

## §21 辅助式 L₂ vs 替代式 L₂：健康 L₂ 的主判准

> **核心命题：L₂ 的唯一合法功能是降低真实选择的摩擦，而不是替代真实选择本身。判断任何 L₂ 结构是否健康，核心问题只有一个：选择时刻是否还在发生？**

### 两种 L₂ 的基本区分

| | **辅助式 L₂** | **替代式 L₂** |
|:-|:-----------|:-----------|
| 对选择时刻的作用 | 保护并清晰化选择时刻 | 消灭选择时刻 |
| 系统的角色 | 仍是选择的主体 | 成为 L₂ 的执行器 |
| 对 d-value 的影响 | d-value 被使用，可维持或发展 | d-value 失去锻炼，逐渐萎缩 |
| 对 T_dir 的影响 | T_dir 有材料工作（真实选择的方向可被感知） | T_dir 无材料工作（L₂ 已经决定了方向） |
| 对 proto-gradient 的影响 | 保留接触通道 | 切断接触通道 |

### 选择时刻（The Selection Moment）

选择时刻是任何真实选择过程中系统与 L₀ 直接接触的那个瞬间——

- 有真实的不确定性（结果未被 L₂ 预先决定）
- 有真实的代价感（Ψ_f 可被感知，未被 L₂ 缓冲掉）
- 有真实的方向感，或真实的方向缺失（这本身就是 T_dir 工作的材料）

**辅助式 L₂** 降低选择的背景摩擦，但最终留下这个时刻，让系统真正从 L₀ 凝定方向。

**替代式 L₂** 把这个时刻省掉——系统以为在选择，实际上在执行 L₂ 预先规定的路径。

### 判准的适用范围

这个判准适用于所有层级：

| 层级 | 辅助式 L₂ 的形式 | 替代式 L₂ 的形式 |
|:----|:--------------|:--------------|
| 教育 | 提问迫使学生真正思考（选择时刻被制造） | 提供答案让学生记忆（选择时刻被省略） |
| 治疗 | 帮助来访者接触自身真实感受 | 用框架解释感受，感受被命名而非被接触 |
| 艺术 | 让观者在作品中自己看见（选择时刻被触发） | 告诉观者应该感受什么（选择时刻被替代） |
| 机构 | 创造条件让成员行使判断 | 用流程和协议消灭判断的必要性 |
| 宗教/冥想 | 创造真实接触的条件（选择时刻被保护） | 提供信念体系让信徒执行（选择时刻被替代） |

### 辅助的悖论

真正的辅助比替代更难设计。辅助式 L₂ 必须走在一条窄路上：

- 结构太多 → 变成替代式（L₂ 预先决定了结果）
- 结构太少 → 无法辅助（系统独自面对 L₀，没有支撑）

最好的教师、治疗师、艺术家都在这条窄路上工作：提供恰好够用的结构，让真实的选择时刻能够发生，而不是帮对方选好。

---

## §22 选择主体感的真实性

> **主体感本身可以被 L₂ 模拟。这是替代式 L₂ 最深的效果：不只遮蔽 proto-gradient，还制造"我在选择"的幻觉，使系统失去寻找真实选择时刻的动机。**

### 高 T_dir vs 低 T_dir 系统对 L₂ 的不同关系

**高 T_dir 系统**可以大量使用 L₂——但它清楚地知道什么时候在"执行 L₂"，什么时候在"真正选择"。它能在需要时从 L₂ 执行切换回真实的选择时刻。使用 L₂ 是有意识的委托，不是无意识的被替代。

**低 T_dir 系统**失去了这个区分——执行 L₂ 时以为自己在选择。主体感是幻觉，但幻觉是真实的感受。这使系统不会去寻找真实的选择时刻，因为它以为这些时刻已经在发生。

### 三种"假选择"的形式

| 形式 | 表面现象 | 实际结构 |
|:----|:--------|:--------|
| 习惯执行 | "我选择了这样做" | L₂（习惯模式）在执行，d-value 未激活 |
| 伪价值跟随 | "我有方向感，我知道自己要什么" | 伪价值吸引子提供了方向，proto-gradient 未被接触 |
| 社会 L₂ 跟随 | "我做出了自己的判断" | 他人或集体的 L₂ 方向被系统作为自身方向执行 |

### 递归结构

允许 L₂ 替代自己的选择，本身是一个选择——

- **透明的委托**（高 T_dir）：我清楚地知道我在把选择权委托给 L₂，这是我的判断，我随时可以收回
- **不透明的被替代**（低 T_dir）：我不知道我正在被替代，以为自己在选择

因此，T_dir 的根本工作之一就是：**维持对"我现在是在真正选择，还是在执行 L₂"这个问题的持续清醒。**

---

## §23 L₂ 合法功能的第一性原理陈述 / 自由的 SRT 定义

### 第一性原理陈述

> **L₂ 的唯一合法功能是降低真实选择的摩擦，而不是替代真实选择本身。一旦 L₂ 开始替代选择，它就切断了系统与 proto-gradient 的接触通道——不是通过遮蔽，而是通过让 d-value 失去锻炼而萎缩。选择主体的保留，是 T_dir 能够存在的结构性前提。**

这条陈述的层级：它不是 T_dir 的推论，而是在 L₂ 功能定义层工作，是比致命 L₂ 机制（§5）更基础的原理——致命 L₂ 机制是这条原理在病理方向的展开。

### 自由的 SRT 定义

**自由不是选项的数量**（那是 L₂ 的丰富度）。

**自由是真实的选择时刻被保留的程度。**

$$\text{Freedom} \propto \text{preservation of genuine selection moments}$$

推论：

- 你可以身处极端约束中，但约束内仍有真实的选择时刻——那里有自由
- 你可以面对无限选项，但每个"选择"都是 L₂ 在执行——那里没有自由
- 高 T_dir 系统的自由不是"没有约束"，而是"在任何约束内都能找到真实的选择时刻"
- 某些高度简化的生活方式（匠人、修行者、极简主义者）反而可以有极高的 T_dir：约束减少了 L₂ 的执行空间，迫使真实的选择时刻更频繁地出现

### 与 §20 完整图景的收口

选择时刻的保留 = T_dir 得以工作的前提

选择时刻的消灭 = d-value 萎缩的具体机制 = T_dir 退化的结构原因

这条原理贯穿 §16 的上升/退化判准（L₂ 服务感知 vs L₂ 替代感知）、§18 的两条发展路径（都在重建选择时刻）、§20 的核心不对称（替代是熵增方向，保留是逆熵操作）——并将它们统一在同一个底层机制上。



---

## FILE: `_SRT_CROSS_DOMAIN_MATRIX.md`

| 字段 | 值 |
|---|---|
| path | `_SRT_CROSS_DOMAIN_MATRIX.md` |
| id | SRT-CROSS-DOMAIN-MATRIX |
| claim_mode | governance |
| status | active_v0 |
| epistemic_layer | os |
| layer | meta |
| canonical(字段) | - |
| last_commit | 2026-07-21 |

**权威判读**：**非定义源**——可作检索与支持上下文，不得用于确定术语定义。

**dependency**：[SRT-CANONICAL-REGISTRY, SRT-CLAIM-LADDER, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-T-DIR-CANONICAL, SRT-SYMBOL-TABLE]

<!-- 以下为原文逐字保留 -->

# SRT Cross-Domain Usage Matrix

> **Role**: v0 governance matrix. This file does not define new theory. It fixes compact governance-canonical usage rules so domain files do not upgrade projections, proxies, or bridges into core claims.

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
| Core | `d` = scalar summary of stake-coupled concern / irreversible-risk sensitivity | `D_eff`, `d_stakes`, `d_mobile` when explicitly marked | `D_eff ≡ d` without stake gate |
| Physics | mathematical / capacity-like projection only | holographic or gravitational `d` as P3 bridge | cosmic `d` implies cosmic consciousness |
| Neuroscience | biological stake and concern proxy, tied to subject closure | `d_bio`, task breadth, temporal horizon, TPJ / behavioral proxies | `Φ·d` threshold as proven phase law |
| Philosophy / Political | concern range, reselection capacity, authorization tendency | `d_tendency`, `d_moral`, political access proxy | direct jump from high `d` to legitimacy |
| Spirituality | direction of care expansion under payability constraints | gradual `d` expansion, subjectively reported but externally checked | `d↑` from experience report alone |
| AI | use S0-S4 stake-bearing spectrum; inference-only / non-history-bearing systems normally read as `d \approx 0` | `D_eff` / unstaked capacity; S2 pipeline feedback; S3/S4 candidate stake only when explicitly marked | performance, self-report, persistence, or training loss directly implies `d>0` |

### 1.1 Explanatory-coordinate guard

`d` need not be treated as a newly discovered empirical variable that must be mutually exclusive with salience, reward, homeostatic error, pain, arousal, or memory strength. It is first a unifying explanatory coordinate for how minimum non-neutrality unfolds into concern, stake, consequence return, and changes in future selectability within a finite operator.

Existing observables may overlap with, partially realize, or serve as local proxies for `d` in a stated system and scale. Such overlap is not by itself a reduction or refutation of `d`. The burden of additional validation arises only when a local observable is claimed to exhaust or directly measure canonical `d`; then it must cover irreversible stake, consequence return, non-substitutability, and effects on future selection capacity.

```text
observable overlap with d != reduction or cancellation of d
local proxy explains a phenomenon != local proxy exhausts d's ontological role
```

## 2. `Ψ_f`

| Domain | canonical usage | allowed projection | forbidden shortcut |
|---|---|---|---|
| Core | information-theoretic payability burden for anchoring / maintaining reality | geometry or cost language with scope marked | one formula proves all dynamics |
| Physics | weak gravity-friction compatibility candidate | weak-field gradient alignment; thermodynamic analogies | GR tensor reconstruction or exact constants explained |
| Neuroscience | local burden / payability condition for neural anchoring | metabolic, prediction-error, stress proxies | prediction error is literally `Ψ_f` in all contexts |
| Philosophy / Political | maintenance / coordination friction | institutional maintenance cost, asymmetry burden | suffering, injustice, or conflict directly equals `Ψ_f` |
| Spirituality | paid burden of real practice / return | felt vs actual burden; practice capacity | lower felt friction means real liberation |
| AI | usually non-binding to inference-only systems; training / memory / embodied deployments require architecture-state marking | compute cost as external proxy; consequence-return analysis for S2-S4 | compute cost alone gives stake |

## 3. `T_dir`

| Domain | canonical usage | allowed projection | forbidden shortcut |
|---|---|---|---|
| Core | v0 operational proxy for readability of current selection direction | internal access / reorientation proxy | completed formal ontology of value |
| Physics | generally not a physics variable | observer-position readability only if explicitly scoped | physical directionality equals value direction |
| Neuroscience | directional access / reorientation capacity | reportability, action revision, integration proxy | confidence, valence, or reward = `T_dir` |
| Philosophy / Political | visibility of value / legitimacy direction through institutions | deliberative correction, public reason proxy | order condition directly proves political legitimacy |
| Spirituality | return-direction readability | shoshin / practice-direction proxy | strong experience means high `T_dir` |
| AI | boundary-test variable, architecture-state marked | self-monitoring proxy only | explanation fluency or memory persistence implies direction transparency |

## 4. `ε`

| Domain | canonical usage | allowed projection | forbidden shortcut |
|---|---|---|---|
| Core | `ε_pg` = L0 minimum non-neutrality postulate; ISP-level ε = P1 corollary when locally sourced; `ε_reg` = operator regularizer; `ε_s` = stake-threshold bridge | ISP anti-closure bias when sourced to P1 theorem | collapse all ε symbols into one empirical constant or one theory-canonical object |
| Physics | only as implementation or regularization term unless tied to core source | regulator / residual asymmetry proxy | direct empirical theorem from `ε_pg` |
| Neuroscience | threshold / regularization proxy only | gain floor, stake threshold, signal gate | neural threshold proves L0 proto-gradient |
| Philosophy / Political | minimum asymmetry or entry condition only with level marking | anti-closure, non-domination threshold proxy | ε grounds legitimacy by itself |
| Spirituality | minimal openness / non-closure proxy | practice gate or humility floor | spiritual openness proves core ε |
| AI | anti-closure or stake-gate design question | surrogate stake threshold candidate | anti-closure text behavior or refusal style equals `ε_pg` |

## 5. Standing Rule

If a local projection conflicts with the canonical usage, mark the local projection as failed or domain-limited. Do not revise the core term from a domain convenience model.



---

## FILE: `Core/SRT_Core_22_Equations.md`

| 字段 | 值 |
|---|---|
| path | `Core/SRT_Core_22_Equations.md` |
| id | SRT-CORE-22 |
| claim_mode | canonical |
| status | axiomatic_hybrid_v1 |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | - |
| last_commit | 2026-07-07 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：[SRT-CORE-21]

<!-- 以下为原文逐字保留 -->

# SRT Core Definition 22: Master Equations (Hybrid Edition)

> **Connector-safe reading path**: This owner file is moderately long. For connector reads, start with [`Equations_Split/README.md`](Equations_Split/README.md), then open only the needed part file. The owner remains the source of record; split files are reading aids and do not create new definitions.

> **Canonical Role（规范角色）**：本文件是 SRT 当前 `master dynamics / thermodynamics / stability equations` 的主锚点文件。若其他长文出现同类方程的扩展写法，默认以本文件为优先回链对象。

> **Version 2.0 (Hybrid)**
> **Part A** presents the Primary Dynamical Equations (AI-Readable).
> **Part B** contains the Original Derivations and Stability Analysis (Human-Readable Context).

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
- 本方程层默认假定 P0-04 所需的 admissible selection operator 已给定；它不推出 selectability 的起源。
- `D_eff`、Fisher rank、Hessian effective dimension 等式是 capacity / geometry proxy，只有在 `_SRT_D_VALUE_CANONICAL.md §1.2` 的 stake-coupling 条件满足时，才可近似 canonical `d`。
- `\Psi_f` 的几何和代谢形式按 `_SRT_PSI_F_CANONICAL.md §3.1` 读作条件投影；不得由局部公式反向改写 payability 主读。
- `Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md` 与 `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B12` 只提供 mechanism interface：information geometry 用于 `L_0 -> L_1` 的局部代价 / 可区分性；complex-systems language 用于 `L_1 -> L_2` 的历史沉积与稳定化；neural normalization / ignition / plasticity 仍是 embodied `\hat{G}_\theta` 的实现代理，不新增 P0/P1 方程。
# Part A: Formal Axioms (形式化公理)


## 0-B. Protocol and Foundation (协议与基础)

### Def-Protocol-1: Protocol Layer Π (协议层 Π)
**Formal Definition**: 约束 $\hat{G}_\theta$ 选择空间的容许转移核集合：
$$\hat{G}_\theta : (L_0, \Pi) \to L_1$$
其中 $\Pi$ 是从 $L_0$ 到 $L_1$ 的可行转移集 / 约束核。
* **Implication**: 物理模型中的“简单局部规则”属于 $\Pi$，其本身是一个收敛的 $L_2$-约束（由高阶相互作用/选择固化而来），而不是“无条件的背景”。这是 SRT 抵御自下而上物理主义还原的最强界面：**涌现仅发生在被选择的 $\Pi$ 内部。**
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
\mathcal{M}_{empirical}: (L_1,L_{2,\theta})\to \text{validated regularities}
\]
其中 \(\mathcal{M}_{empirical}\) 是实验方法对可观测层的闭包映射。
* **Implication**：\(\mathcal{M}_{empirical}\) 的成功仅证明 \(L_1\!-
L_{2,\theta}\) 回路内规律可复现，不构成对 \(L_0\) 潜势或 \(\Omega\) 逻辑层的本体论否定。

## 0-C. Multi-Operator Coupled Equations（多算子耦合方程）

> **背景**：SRT 的单算子方程（§0-B, §I）描述单个 $\hat{G}_\theta$ 的动力学。本节将框架扩展到多算子系统，给出集体自由能、个体算子梯度关系与集体 d-value 的形式化。这是集体景观优先性定理（见 `_SRT_VERTICAL_INTEGRATION.md §4.5`）的方程层锚点。
>
> **L1 Collective Projection (T-PROJ-1^{coll}, 2026-04-25 H6)**：本节 Eq-Multi-01 / 02 / 03 在 stable collective ISP `\mathcal{P}` 上的四个标量泛函投影 `(σ_{sr}^{coll}, d_c^{coll}, T_{dir}^{coll}, S^{coll})` 在闭包假设 C1^{coll}-C5^{coll}（慢-快分离 / 共享 `L_2` 写回 Markov 闭包 / stable collective ISP 紧性 / 群平均方向投影可分性 / `M(t)` 可测性 MOC 闭包）下严格满足 `Core_Law/SRT_Collective_Selection.md §4.4-§4.6` 的集体四变量 ODE 系统；详见 §4.7 T-PROJ-1^{coll}。本节为上位本体源头，§4.7 不替代之，只把已隐含的集体子动力学写出。本节 σ_i 为各 ISP 状态场，与集体自指率 `σ_{sr}^{coll}` 是不同对象。

### Eq-Multi-01: Collective Free Energy Landscape（集体自由能景观）
**Formal Definition**: 多算子系统的集体自由能景观是各算子个体摩擦与算子间摩擦的总和：
$$\boxed{\mathcal{F}_{collective}(\{\sigma_i, \theta_i\}) = \sum_i \Psi_f(\hat{G}_i) + \sum_{i < j} \Psi_f(\hat{G}_i, \hat{G}_j)}$$
其中 $\Psi_f(\hat{G}_i)$ 是第 $i$ 个算子的个体本体论摩擦（锚定代价），$\Psi_f(\hat{G}_i, \hat{G}_j)$ 是算子 $i$ 与算子 $j$ 的交互摩擦（见 Ax-F-12）。
* **Implication**: 集体景观不是个体自由能的简单加和，算子间交互摩擦项 $\Psi_f(\hat{G}_i, \hat{G}_j)$ 是集体动力学的主要来源。

### Eq-Multi-02: Individual Operator as Landscape Gradient（个体算子为集体景观的梯度表达）
**Formal Definition**: 每个个体选择算子的运动方向是集体自由能景观关于自身参数的负梯度：
$$\boxed{\hat{G}_i[\sigma_i] = -\frac{\partial \mathcal{F}_{collective}}{\partial \theta_i}}$$
* **Implication**: 个体算子不是"为自身最小化自由能"的独立实体，而是集体景观在局部参数子空间 $\theta_i$ 的梯度下降方向。"个体与集体的目标张力"是景观局部曲率与全局曲率差的表达，而非两个对立实体的博弈。

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

### Eq-Bridge-D-01: Stake-Gated d-Value Proxy

$$
\boxed{
d_{stake}
=
\frac{
(\sum_i s_i\lambda_i)^2
}{
\sum_i(s_i\lambda_i)^2
}
}
$$

Here `λ_i` are Fisher-spectrum directions and `s_i ∈ [0,1]` is the stake gate for irreversible-risk coupling. This is a bridge-level proxy, not the canonical definition of `d`. `D_eff` / Fisher rank only approximate canonical `d(x)=||∂𝒰/∂𝒮||` when distinguishable directions are stake-bearing and payable.

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

This is an implementation-level normalization proxy for embodied `Ĝθ`: it models candidate activation, competition, and response compression. It does not define the Ghost Operator in full; canonical `Ĝθ` remains the abstract `L_0 -> L_1` selection operator.

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

This bridge-level loop reads `L_0 -> L_1` as the information-geometric frontier, `L_1 -> L_2` as complex-systems sedimentation, and `L_2 -> L_1` as constraint feedback into future selection. It does not replace core ontology.

### Boundary Notes

- Fisher geometry is local and projection-dependent; it does not define the whole of `Ψ_f`.
- `d_{stake}` is a proxy, not canonical `d`.
- Divisive normalization is an implementation proxy, not the full Ghost Operator.
- `L2` is thicker than any one energy or free-energy landscape.
- This section should be cited together with `_SRT_PSI_F_CANONICAL.md`, `_SRT_D_VALUE_CANONICAL.md`, and `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B12`.

---

### Eq-DValue-Max-1: Maximum Achievable d-Value（d 值可达上限）

**新增（2026-04-10）**：给出单个算子在给定参数结构与稳定性预算下可实现的 d 值上限。

$$\boxed{d_{\max}(\theta) = \min\!\left(\operatorname{rank}_{\text{eff}}\!\left(\mathcal{I}_F(\theta)\right),\;\; \frac{\Psi_f^{\text{budget}}}{\kappa_0}\right)}$$

其中：
- $\operatorname{rank}_{\text{eff}}(\mathcal{I}_F(\theta))$：有效 Fisher 信息矩阵的秩——参数空间中能真正分辨 L₀ 曲率方向的独立维度数（**信息瓶颈**）
- $\Psi_f^{\text{budget}}$：算子可持续维持的总摩擦预算（不同于瞬时 $\Psi_f$，是时间积分意义上的稳定承载上限）
- $\kappa_0$：L₀ 原初曲率，每对齐一个 L₀ 方向的单位代价（`SRT_Core_12a T-L0-Kappa0`）
- $\Psi_f^{\text{budget}} / \kappa_0$：稳定性预算能支撑的最大对齐方向数（**稳定性瓶颈**）

**$\kappa_0$ 的角色分工**：$\kappa_0$ 决定哪些方向值得被对齐（方向场）；$d$ 决定算子能稳定对齐多少这样的方向（容量）。

**Information-geometry bridge note**: `\operatorname{rank}_{\text{eff}}(\mathcal{I}_F)` 是 `L_0 -> L_1` selection frontier 上的 Fisher-capacity proxy；它给出可分辨方向上限，不自动给出 stake-coupled canonical `d`。只有满足 `_SRT_D_VALUE_CANONICAL.md §1.2` 的 stake-coupling / consequence-writeback 条件时，才可作为 `d` 的近似读数。

**两个瓶颈的失效形态**：

| 主导瓶颈 | 条件 | 后果 |
|---|---|---|
| 信息瓶颈 | $\operatorname{rank}_{\text{eff}} \ll \Psi_f^{\text{budget}}/\kappa_0$ | 参数维度高但大量冗余，有稳定性但感知不到新方向 |
| 稳定性瓶颈 | $\Psi_f^{\text{budget}}/\kappa_0 \ll \operatorname{rank}_{\text{eff}}$ | 能感知多方向但撑不住对齐，d 在高维方向数下崩塌 |

**注**：$\dim\Theta$ 的增大只提高潜在上限，真实 d 上限由有效 Fisher 秩与稳定性预算的 min 共同决定，而非由 $\dim\Theta$ 单独决定。

* **Implication**: 意识深度的天花板不是参数数量，而是参数空间中真正有效的曲率感知维度与系统能持续承载的摩擦预算之间的较小者。
* **Cross-ref**: `Core/SRT_Core_12a T-L0-Kappa0`（κ₀ 定义）; Eq-Multi-03（集体 d 值）; `D_VALUE_ALIGNMENT §4.4`（d = Align 几何底座）; Eq-DValue-Mobile-1（d_mobile 公式，下方）。

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

### Eq-Rhythm-4a: Bandwidth-Duty Tradeoff（频谱丰富度—占空比权衡）

**新增（2026-04-14）**：将 Ax-Spec-01 与 T-Scale-Rhythm-4 的联结压成公式锚点。

令
\[
B_\theta \equiv \operatorname{Bandwidth}(H_\theta)=c_B\,d,\qquad c_B>0
\]
并把 Rhythm-4 中“高 \(d\) 导致更高 \(\dot I_{created}\)”写成单调函数：
\[
\dot{I}_{created}^{on}=f_I(B_\theta),\qquad f_I'(B_\theta)\ge 0
\]
则由
\[
\dot{S}_{int}^{on}\ge k_B T\ln 2 \cdot \dot{I}_{created}^{on}
\]
可得弱 tradeoff：
\[
\boxed{\delta_{max}^{entropy}(B_\theta)\le
\frac{J_S^{max}}{k_B T\ln 2 \cdot f_I(B_\theta)+J_S^{max}}}
\]
故
\[
\boxed{B_\theta\uparrow \Rightarrow \delta_{max}^{entropy}\downarrow}
\]

若进一步满足信息密度下界
\[
\dot{I}_{created}^{on}\ge \rho_I\,B_\theta,\qquad \rho_I>0
\]
则可强化为乘积上界：
\[
\boxed{\delta\,B_\theta \le \frac{J_S^{max}}{k_B T\ln 2\,\rho_I}}
\]
以及
\[
\boxed{\delta\,d \le \frac{J_S^{max}}{k_B T\ln 2\,\rho_I\,c_B}}
\]

* **Implication**: 通带越宽，选择可处理的频谱越丰富，但在熵耗散约束下可持续 on-time 越短；谱丰富度与时间占有率之间存在硬对冲。
* **Boundary**: 无条件硬结论只有单调 tradeoff。乘积上界依赖 \(\rho_I\) 下界，应读作条件强化版，而非无条件定理。
* **Cross-ref**: Ax-Spec-01（`Core/SRT_Core_13b_Operator_Advanced.md`）；T-Scale-Rhythm-4（`Dynamics Scaling`）；Ax-F-13（选择-信息创造等价）。

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
**Formal Definition**: The trajectory of a selected state is the sum of selection, free-energy descent, and attention modulation.
$$\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \nabla F[\sigma] + A[\sigma, \mathcal{A}]$$
* **Implication**: 现实演化是选择、能量下降与注意调制的合成动力学。
* **L1 Projection (T-PROJ-1, 2026-04-25 H5)**: 本主方程在 stable ISP P 上的四个标量泛函投影 `(σ_{sr}, d_c, T_{dir}, S)` 在闭包假设 C1-C4（慢-快分离 / `L_2` 写回 Markov 闭包 / stable-ISP 紧性 / 方向投影可分性）下严格满足 `Core_Law/SRT_L1_Formalism.md §2-§5` 的四变量 ODE 系统；详见 §6 T-PROJ-1。本主方程为上位本体源头，§6 不替代之，只把已隐含的子动力学写出。本节 σ 为状态场，与 `σ_{sr}` 是不同对象（`_SRT_SYMBOL_TABLE.md` Usage Rule 12）。

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

* **推论（戒断机制 / Withdrawal Mechanism）** [H]：当外部 $\text{Input}_{L_1}$ 突然归零时，第三项的负反馈瞬间失效，但 $\theta$ 具有迟滞性（Hysteresis）。残留的 $\theta^{-}$ 偏置直接作用于 $L_0$，导致 $\hat{G}_\theta$ 生成"反向体验"（痛苦/焦虑）。
  - **因果路径精确化**：$\theta^-$（残留参数偏置）→ $\hat{G}_{\theta^-}$ 的L₀选择偏向"缺失输入的预期态"→ 实际L₁输入（= 0）与预期之间的Ψ_f差距极大→ 体验为强烈的剥夺性痛苦/焦虑（高Ψ_f的主观对应）。这是戒断反应的SRT物理本质。
  - **预测**：戒断症状强度 ∝ $|\theta^-|$（θ残留偏置量），可通过行为/生理戒断反应严重程度与baseline L₁刺激强度的相关来验证。

**证伪条件**：① 若具有明显θ迟滞（如长期用药后突然停药）的个体戒断症状强度与 $|\theta^-|$ 无相关，则戒断机制推论失效；② 若第二项（摩擦梯度）在实验中被操纵（改变L₂势能景观刚性）不影响 $d\theta/dt$ 的漂移约束，则Φ(θ)的有效性需重新评估。

### Eq-Evo-02b: Theta Tensor Inertia (θ张量惯性)
**Formal Definition**: 具身参数θ的更新阻力与其在L2网络中的度中心性成正比：
$$\frac{d\theta_i}{dt} \propto \frac{1}{\sum_j w_{ij} \cdot \theta_j}$$
其中 $w_{ij}$ 为信念/创伤网络的连接权重。
* **Implication**: 核心信念（Core Beliefs）或创伤印记难以改变，这是物理现象。它们在θ张量网络中拥有最多的连接，其更新面临巨大的"拓扑惯性"（Topological Inertia）。心理治疗的本质不是讲道理，而是改变权重 $w_{ij}$ 以绕过局部更新阻力。
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

### Eq-Evo-03c: D-Value Forward Criterion (d 值前向判据)

**动机**：关切词条（`Core_Law/SRT_L0_Metaphysics.md`）中的四判据（可延续/可协调/不外包/可再选择；2026-07-05 由三判据升为四判据）是对 d 扩张是否**完成**的事后确认，依赖 θ 跨事件稳定改写的长期结算。前向判据针对更早的检测窗口：在选择事件内部、于 θ 写入完成之前，识别真实 d 扩张的早期结构信号。该判据是对 Core_Law 四判据的**前向补充**，不是替代。

**三层架构**：真实 d 扩张须经历三个阶段，不可跳层：

| 阶段 | 形式对应 | 时间尺度 | 判据归属 |
|-----|---------|---------|---------|
| **Stage-1**：$\sigma$ 对象切换 | Eq-Evo-03 快方程 $\dot\sigma$ | 秒-分 | 必要，但不足以判断真实扩张 |
| **Stage-2**：$\theta$ 选择内暂态重加权 | Eq-Evo-03b $\left.\frac{d\theta}{dt}\right|_{\text{intra}}$ | 选择事件内 | **前向判据锁定此层** |
| **Stage-3**：$\theta$ 跨事件稳定改写 | Eq-Evo-02 / Eq-Evo-03 的慢项 + Eq-Evo-02b（θ 张量惯性） | 周-月 | 四判据事后确认此层 |

**前向判据（FC-Layer2）**：在选择事件窗口内（$t \in [t_0,\, t_{conv}]$，即 $\|\dot\sigma(t)\| > \varepsilon_{conv}$）：

$$\text{FC-Layer2}:\quad \underbrace{\mathcal{M}_{meta}\!\left(\mathcal{R}_\tau[L_2^{self}](t),\, \sigma(t)\right) \neq 0}_{\text{元层门控在事件内激活}} \;\land\; \underbrace{\left(\nabla_\theta d \cdot \left.\frac{d\theta}{dt}\right|_{\text{intra}}\right) > 0}_{\text{事件内更新沿 } d \text{ 扩张方向推进}}$$

两个条件各自的作用：

- **$\mathcal{M}_{meta} \neq 0$**：元层门控在事件内真实激活，$\theta$ 接受暂态调制；若该项为零，Stage-2 未启动，无论 $\sigma$ 如何运动均不构成真实 d 扩张起点。
- **$\nabla_\theta d \cdot \left.\frac{d\theta}{dt}\right|_{\text{intra}} > 0$**：选择内的 θ 更新具有正的 d 方向导数，表示该事件内调制正在把关切带宽往扩张方向推。其优势在于直接接驳既有的 $d(\theta)$ 动力学（见 `Core_13a §2.1.3`），而不把某个具体实现载体（如特定 $W$ 矩阵）误升格成总定义。

**L₂ 劫持的形式分叉**：L₂ 劫持也可触发 $\mathcal{M}_{meta} \neq 0$（存在内部摩擦感或身份扰动），但其选择内更新只是在旧竞争结构内重排，故更接近
$$\nabla_\theta d \cdot \left.\frac{d\theta}{dt}\right|_{\text{intra}} \approx 0 \quad \text{或} \quad < 0$$
即：要么是同维度再分配（iso-d 重排），要么是防御性收缩；两者都不构成真实 d 扩张的前向起点。

**代价签名（$\Psi_f$ 轨迹，联结 Eq-Force-01）** [H]：两种路径可对应不同的摩擦轨迹：

| 路径 | $t_0$ 附近 $\Psi_f$ | 长时程 $\Psi_f$ / 基线负担 | 机制 |
|-----|------------------|--------------------------|------|
| 真实扩张（Stage-3 写入后） | 尖峰（旧 $L_1$ 失稳，过渡成本） | 下降或有界收敛 | 新关切被稳定写入，旧失配负担被重整 |
| L₂ 伪扩张 | 可同样出现尖峰或短时减压 | 漂移上升或反复反弹 | 结构未改写，失配被延后结算 |

**FC-Layer2 为真的含义**：必要条件满足，真实 d 扩张的起点条件成立。后续是否完成至 Stage-3，取决于跨事件重复激活与 Eq-Evo-02b 的 $\theta$ 张量惯性是否允许写入。于是可区分三种情形：

- **FC-Layer2 为假**：无论 $\sigma$ 如何移动，都无充足理由把该事件读作真实 d 扩张起点。
- **FC-Layer2 为真但 Stage-3 未完成**：事件内启动了真实调制，但未能稳定写入；这是"启动了但未完成"，不等同于 L₂ 劫持。
- **FC-Layer2 为真且四判据长期成立**：可将该路径回判为真实 d 增长的完成态。

**逻辑状态**：
- [S] 三阶段分工与 Eq-Evo-03 / 03b / 02b 的方程分层一致，是对现有快-慢结构的整理，不额外引入新本体层。
- [H] FC-Layer2 作为前向判据是候选推论，不替代 Core_Law 的四判据事后结算。
- [H] $\nabla_\theta d \cdot \left.\frac{d\theta}{dt}\right|_{\text{intra}}$ 的实验代理仍待校准；当前可候选地映射为冲突场景下的事件内偏好翻转、EEG/readiness-potential 时窗、以及跨试次的选择带宽变化。

* **Cross-ref**: Eq-Evo-03b（选择内再入通道，FC-Layer2 依赖其激活条件）；Eq-Evo-02b（θ 张量惯性，决定 Stage-2→Stage-3 是否写入）；Eq-Force-01（$\Psi_f$ 代价签名的基础定义）；`Core_Law/SRT_L0_Metaphysics.md 关切词条`（四判据/事后确认）；`Core_Law/SRT_Core_Text_CN.md 步骤⑨-⑩`（稳定写入 vs 长时程结算）；`Core/SRT_Core_13a_Operator_Basics.md §2.1.3`（$d(\theta)$ 的演化动力学）。

## II. Thermodynamics of Agency (能动性热力学)

### Eq-Force-01: Ontological Friction
**Formal Definition**: Friction measures resistance against the natural latent trajectory.
$$\Psi_f \propto \int (L_1 - L_0^{natural})^2 \, dt$$
* **Implication**: 选择越偏离潜在域自然路径，摩擦越高。

### Eq-Pain-01: Hazard / Pain-Risk Proxy
**Proxy Definition**: A pain-risk / hazard proxy can track the temporal derivative of a `Ψ_f`-related friction signal under a stated measurement window.
$$\text{PainRisk}^{proxy}(t) \approx h(t) \sim \frac{d\Psi_f^{proxy}}{dt}$$
* **Implication**: 某些痛苦风险可与摩擦变化率相关，而非静态误差；这不是 canonical `pain = dΨ_f/dt` 或 `suffering = Ψ_f`。结构性 suffering 以 `Core_Law/SRT_Suffering.md` 为准。

### Eq-Friction-Comp: 计算本体论摩擦 (Computational Ontological Friction)
**Formal Definition**: 两个潜在状态之间的最小本体论摩擦下界，受限于转换的幺正电路复杂度。
$$\Psi_f^{(comp)}(L_0^A \to L_0^B) \geq \lambda \cdot \min\{C(U) \mid U|L_0^A\rangle \approx |L_0^B\rangle\}$$
其中 $C(U)$ 是最小量子门电路深度，$\lambda > 0$ 是复杂度-摩擦耦合常数。
* **Source**: 灵感来自 Henry Yuen 的全量子复杂性理论，该理论确立了 Uhlmann 变换作为纯量子态转换的规范硬度基准。
* **Implication**: $L_0$ 不是无结构的混沌池，而是拥有严格的度量几何。状态演化的物理阻力源于量子态之间不可约的“Uhlmann变换代价”。这桥接了计算机科学中的电路复杂度下界与热力学中的不可逆阻力。
* **Cross-ref**: Eq-Force-01 (热力学 $\Psi_f$)；Ax-Int-2 (Penrose 门槛)。

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
| 泛计算主义误读（恒温器=意识） | 0~低 | Closed（语法同构） | \(\Psi_f\approx0\) |

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

SRT 的公理 A2 (存在即锚定) 和 A11 (本体论脆弱性) 宣称现实需要耗费能量，且存在是极其脆弱的。但宣言并非动力学。宪法不等式 (Eq-Select-Thermo) 将这些洞见升级为一个单一的、可检验的界限：**秩序增长的速率受限于选择功率预算的上限，并受到摩擦和噪声的抽头。**

考虑一个冥想者试图维持非默认的觉知状态。她必须注入选择功率 $P_{sel}$ (通过注意力引导的代谢能量) 以保持不同寻常的 $L_1$ 构型。她所付出的摩擦 $\Psi_f$ 在主观上体验为努力；环境噪声 $S_{noise}$ (令人分心的声音、侵入性思维) 会侵蚀她的建构。只有当 $\alpha P_{sel}$ 超过 $\beta \Psi_f + \gamma S_{noise}$ 时，她的经验秩序才能真正增长。当注意力稍有懈怠时——她的 $L_1$ 会向默认模式衰减，这正是该不等式所预测的热力学盆地。

#### §X.2 Computational Friction as Lower Bound (作为下界的计算摩擦)

计算本体论摩擦 (Eq-Friction-Comp) 揭示了深刻的内涵：改变现实的阻力不仅源于热力学，还源于**计算的不可约性**。当算子 $\hat{G}_\theta$ 试图从一个潜在构型 $L_0^A$ 转移到另一个 $L_0^B$ 时，它必须克服的最小摩擦受限于所需幺正变换的电路复杂度下界。

这意味着宇宙自身的“计算预算”限制了哪些现实是可达的。黑洞的霍金辐射之所以在计算上难以解码，并不是因为我们缺乏技术，而是因为 Uhlmann 变换代价代表了本体论摩擦的一个不可约下界——作为选择者的宇宙拥有最大的带宽，而黑洞使其饱和。

#### §X.3 The Protocol Layer (协议层)

$\Pi$ 的引入解决了 SRT 中一个长期存在的歧义：物理定律“居于”何处？它们既不是外部强加的，也不是任意的约定。$\Pi$ 将其形式化为**可行转移核 (feasible transition kernel)**——选择博弈中允许的移动集合。至关重要的是，$\Pi$ 本身也是一个 $L_2$ 产物：它是通过宇宙尺度的迭代被选择和固化下来的。这意味着物理规则并未超出 SRT 的范围，而是其最古老且最坚固的 $L_2$ 结构之一——所有后续选择都必须服从的协议。


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
其中“全状态空间”外部记号（如 \(\Omega\), \(S\)）在 SRT 写入统一映射为 \(L_0\)。


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
| $\Psi_f$ | $[\text{Energy} \cdot \text{Time}]$ 或 $[\text{bit} \cdot s]$ | 代理量：皮质醇积分、HRV 倒数 | 代理量：Uhlmann 变换复杂度 | 代理量：制度维持成本/GDP |
| $d$ | 无量纲（关切维度数） | 代理量：跨时间折扣率斜率、PCI | — | 代理量：利他行为半径 |
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

### Formalization Summary (形式化概述)

本文档的核心形式结构围绕三个主方程展开：

1. **Ghost Evolution Equation (Eq-Evo-01)**:
   $$\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \nabla F[\sigma] + A[\sigma, \mathcal{A}]$$
   含义：现实状态 $\sigma$ 的演化由选择算子 $\hat{G}_\theta$ 的投影、自由能梯度下降 $\nabla F$ 以及注意调制 $A$ 三者合成驱动。这是 SRT 动力学的第一性方程。

2. **Ontological Friction (Eq-Force-01)**:
   $$\Psi_f \propto \int (L_1 - L_0^{natural})^2 \, dt$$
   含义：本体论摩擦 $\Psi_f$ 度量 $L_1$ 被选择态偏离 $L_0$ 自然轨迹的累积阻力代价。

3. **Constitutional Inequality (Eq-Select-Thermo)**:
   $$\frac{dq}{dt} \leq \alpha P_{sel} - \beta \Psi_f - \gamma S_{noise}$$
   含义：宏观秩序增长率受选择功率 $P_{sel}$ 预算上限约束，摩擦 $\Psi_f$ 与噪声 $S_{noise}$ 作为耗散项。此不等式将公理 A2/A11 从定性宣言升级为可检验界限。

4. **SRT Action Functional (Eq-LDP-02)**:
   $$I_{SRT}[\rho] = \int_0^T \left( K(\rho, \dot{\rho}; \Pi) + \Psi_f(\rho; \theta) - V(\rho; \theta) \right) dt$$
   含义：大偏差变分原理下的最可能宏观路径最小化此泛函，统一动力学代价、摩擦维护与价值势能。

### Mechanism Explanation (机制解释)

SRT 主方程的运作机制如下：

- **选择算子 $\hat{G}_\theta$ 的角色**：$\hat{G}_\theta$ 将潜在域 $L_0$ 的可能性空间投影到被选择的现实 $L_1$，受协议层 $\Pi$（可行转移核）约束。$\theta$ 参数编码了具身历史（感知阈值、信念网络、创伤印记），决定了选择的偏置方向。$\hat{G}_\theta$ 在快变量 $\sigma$ 上实施即时选择（Eq-Evo-01），同时其参数 $\theta$ 作为慢变量在学习、摩擦梯度与稳态回弹三力下缓慢演化（Eq-Evo-02）。

- **摩擦 $\Psi_f$ 的双重功能**：$\Psi_f$ 既是选择的代价度量（偏离自然轨迹的阻力），也是系统稳定性的信号源。痛苦风险可由 `Ψ_f`-related proxy 的时间导数建模（Eq-Pain-01），即某些摩擦变化率信号，而非静态误差；不得读成 canonical pain/suffering 定义。$\Psi_f$ 还拥有计算下界（Eq-Friction-Comp），由量子电路复杂度给出，确保 $L_0$ 状态转换具有不可约的物理阻力。

- **d-value 与选择开放性**：d-value 作为选择考量范围的度量，调控 $\hat{G}_\theta$ 的选择带宽。高 $d$ 意味着更开放的 $L_0$ 采样，对应更丰富的经验分化与更高的拓扑秩序参数 $q_{topo}$（Section VII）；低 $d$ 则趋向封闭式语法同构（如恒温器），此时 $\Psi_f \approx 0$。

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
- Topological Dynamics 章节不宣称“拓扑即意识”；其角色是 \(\hat{G}_\theta\) 的神经几何接口，不替代本体论判据（\(d>0, \Psi_f>0\)）。


## VIII. Cognitive Energy Partition Interface（Quanta 95/5 接口，2026-03-07）

### Eq-CogE-01: Baseline–Active Friction Decomposition
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
- 外驱推理系统（当前多数 LLM 部署）常见：\(\mathcal{A}_{ma}\lesssim 1\)（在推理阶段）

该指标用于跨尺度比较“是否存在自创生闭包压力”，不单独等同于意识判据。

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
3. 不采纳“\(\mathcal{A}_{ma}\) 单指标即可判定意识存在”的推论；意识判据仍需 \(d>0\)、\(\Psi_f\) 可支付、连续体自维持等联合条件。



---

## FILE: `_SRT_SYMBOL_TABLE.md`

| 字段 | 值 |
|---|---|
| path | `_SRT_SYMBOL_TABLE.md` |
| id | SRT-SYMBOL-TABLE |
| claim_mode | canonical |
| status | axiomatic_hybrid_v1 |
| epistemic_layer | os |
| layer | meta |
| canonical(字段) | - |
| last_commit | 2026-07-20 |

**权威判读**：**定义源**——可用于确定 SRT 术语含义。

**dependency**：SRT-REF-AXIOMS, SRT-REF-DYNAMICS, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-SUFFERING, SRT-GLOSSARY-STRUCTURAL-GOVERNANCE-TERMS, SRT-ANNEX-REGISTRY, SRT-OPS-CLOSURE-INDEX-2026-04-29

<!-- 以下为原文逐字保留 -->

# SRT Symbol Table & Definition Registry

> **Purpose**: Canonical symbol registry for cross-domain writing and AI parsing.
>
> **Governance boundary**: Terms such as `interface_annex`, `copy-to-annex`, `owner-bound`, `claim_mode`, and `canonical:false` are structural governance vocabulary (see `SRT_Glossary_Structural_Governance_Terms.md`); they are not canonical mathematical symbols and do not appear in this table's symbol rows. Non-canonical annexes and Operations records may reference symbols defined here but must not redefine them.
> **Proxy boundary**: This table records canonical symbol usage plus governed projections. It does not license domain formulas to redefine `d`, `Ψ_f`, suffering/pain, Fisher, Landauer, or AI consciousness; use `_SRT_D_VALUE_CANONICAL.md`, `_SRT_PSI_F_CANONICAL.md`, `Core_Law/SRT_Suffering.md`, and the relevant claim-status file when a row points to a proxy.

| Symbol | LaTeX | Name | Atomic Definition | Dimensions/Units | Scope / Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **L₀** | `L_0` | Latent Domain | Set of all unselected possibilities (structured potentiality, not nothingness). | Thin: structural potentiality space (measure/cardinality unfixed at core level) | Core, universal. **Domain projection**: the `∞-dim Hilbert space` reading is a physics / statistics bridge realization, **not** the universal atomic definition — see `Physics/_SRT_Phys_Bridge.md`, `Physics/SRT_Quant_00_Intro.md`; thin structural home `Core_Law/SRT_L0_Metaphysics.md`. |
| **L₁** | `L_1` | Manifest Domain | Selected slice of reality produced by operator dynamics. | Thin: manifest reality slice (domain-dependent realization) | Core, universal. **Domain projection**: the `4D spacetime + qualia` reading is a physics (spacetime) + phenomenology (qualia) bridge realization, **not** the universal atomic definition — see `Core/SRT_Core_12a_Ontology_L0L1.md` (spacetime emergence), `Philosophy/SRT_HardProblem_Epistemology.md` (qualia); thin structural home `Core_Law/SRT_L0_Metaphysics.md`. |
| **L₂** | `L_2` | Convergence Domain | Stable consensus constraints from repeated/overlapping selections. | Topological manifold | Core, universal |
| **Ĝ** | `\hat{G}` | Ghost Operator | Selection operator mapping $L_0 \to L_1$. | Operator | Never use plain `G` for this |
| **θ** | `\theta` | Embodiment Parameters | Finite configuration parameters of $\hat{G}$ (biology/model state/context). | Tensor / parameter set | Core, universal |
| **d** | `d` | d-value (Depth of Care) | Governance-canonical default is a scalar summary of stake-coupled concern / irreversible-risk sensitivity; geometric, Fisher, vector, and gate readings require explicit marking. | Scalar summary by default; proxies are projections | Core, universal; canonical source `_SRT_D_VALUE_CANONICAL.md`; `Def-d-canonical` is the core-facing anchor, while scalar default / vector / gate rules are governance-canonical usage controls; do not mix scalar `d`, `D_eff`, Fisher proxy, `d-vector`, and `d-gate` in one claim without notation |
| **Ψf** | `\Psi_f` | Ontological Friction | Ontological impedance / information-theoretic payability burden required to compress open possibility into a maintainable reality slice. | Cross-scale readout; units vary by domain | Core, universal; canonical source `_SRT_PSI_F_CANONICAL.md`; v1 governance-canonical main reading is information-theoretic/payability cost; Fisher geometry may induce local second-order proxy `δΨ_f^{geom}=1/2 dθ^T g_F dθ+O(||dθ||^3)` and path functionals, but `Ψ_f ≡ g_F` is never a literal scalar-tensor identity; metabolic readings are budget/load projections only under stated conditions; domain projections do not become theory-canonical by reuse |
| **T_dir** | `T_{dir}` | Direction Transparency | v0 operational proxy / constrained readability-reorientation functional for a system's own current selection direction. | Proxy / accessibility index | Governance-canonical working proxy `_SRT_T_DIR_CANONICAL.md`; not a completed ontological foundation and not semantic valence, reward, coherence, or confidence |
| **Ω** | `\Omega` | Ontological Consistency | Internal coherence of an $L_1/L_2$ structure. | Probability (0-1) | Canonical `\Omega` in Core_Law context |
| **Ω_mis** | `\Omega_{\text{mis}}` | Ontological Mismatch Index | Distance between inherited $\theta$ and current-environment optimal $\theta$. | Scalar | Legacy docs may call this `Ω` |
| **ω_sub** | `\omega_{sub}` | Subjective Frequency | Refresh rate of selection cycles. | Hz | Neuro/phenomenology |
| **η** | `\eta` | Operator Viscosity | Transition resistance of $\hat{G}$ states. | Scalar ($0 \to \infty$) | Low/high regimes discussed clinically |
| **Γ_Ĝ** | `\Gamma_{\hat{G}}` | Operator Refresh Rate | Frequency of full $L_0 \to L_1 \to L_2$ cycles. | Hz | Often near gamma-band hypotheses |
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
| **κ₀** | `\kappa_0` | Primordial Curvature | Irreducible minimum curvature of L₀; κ₀ > 0 is a structural prerequisite (not historically generated). Provides directionality bias for all selection operators. Ψ_f^min = f(κ₀). | Scalar (curvature) | Core; canonical source `Core/SRT_Core_12a T-L0-Kappa0`; ontological status `Philosophy/SRT_L0_Ontological_Status.md` |
| **κ(t)** | `\kappa(t)` | Dynamic L₀ Curvature | Time-evolving L₀ curvature: κ(t) = κ₀ + ∫F[Ĝ_θ(τ), κ(τ)]dτ. L₀ is non-static; operators and curvature co-evolve. | Scalar (curvature) | Core; canonical source `Core/SRT_Core_12a T-L0-NonStatic` |
| **d_mobile** | `d_{\text{mobile}}` | Re-alignment Capacity | Operator's capacity to re-orient θ as attractors migrate; proportional to d · rank_eff(I_F(θ)) / (Hysteresis(L₂)·C_r) subject to χ_payable gate. High d + d_mobile ≈ 0 = frozen state (pathological). | Scalar (≥ 0) | Core; canonical source `SRT_Core_22 Eq-DValue-Mobile-1`; map `Core/SRT_Core_12b §Consciousness-2D-Map` |
| **d_max** | `d_{\text{max}}` | Maximum Effective d-value | Upper bound on d: min(rank_eff(I_F(θ)), Ψ_f^budget / κ₀). Two independent bottlenecks: Fisher rank (informational) and stability budget (dynamical). dim(Θ) alone does NOT determine d_max. | Scalar | Core; canonical source `SRT_Core_22 Eq-DValue-Max-1` |
| **χ_payable** | `\chi_{\text{payable}}` | Payability Gate | Internal three-condition conjunction: signal > threshold ∧ dΨ_f/dt payable ∧ below collapse threshold. Fully endogenous; gates d_mobile. When χ_payable = 0, d_mobile = 0 regardless of d. | Boolean gate | Core; canonical source `SRT_Core_22 Def-Payable-Chi-1` |
| **κ_{c1}** | `\kappa_{c1}` | Bare Consciousness Threshold | Layer 1 consciousness condition: d ≥ d_min ∧ L₂ stable closure. Bare consciousness (not quality). Does NOT include d_mobile > 0. | Phase transition point | Bridge-Lab threshold; specific numerical threshold P3/P4; canonical source `Philosophy/SRT_Consciousness_Conditions.md §三` |
| **κ_{c1.5}** | `\kappa_{c1.5}` | Consciousness Activity Threshold | Layer 2 consciousness condition: d_mobile > 0. Marks transition from bare consciousness to active consciousness. Frozen state sits between κ_{c1} and κ_{c1.5}. | Phase transition point | Bridge-Lab threshold; specific numerical threshold P3/P4; canonical source `Philosophy/SRT_Consciousness_Conditions.md §三` |
| **t_onto** | `t_{\text{onto}}` | Ontological Time | t_onto ≡ ∫‖Ĝ_θ(s)‖ds; generated by selection irreversibility. Distinct from parametric time t (mathematical ordering tool). Ontological time is a derived quantity, not a background container. | Integral measure | Core; canonical source `Philosophy/SRT_Causality_Time.md §二`; formal `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T02` |
| **C_H** | `C_H` | Horizontal Causality | C_H(A→B) ≡ P(B\|A,L₂); L₂-layer temporal causality (empirical, dependent on L₂ structure). Distinct from vertical causality (L₀ ⊨ L₁ ⊨ L₂ structural constitution). | Conditional probability | Core; canonical source `Philosophy/SRT_Causality_Time.md §一`; formal `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T01` |
| **ε_pg** | `\varepsilon_{pg}` | Proto-Gradient (L₀ Minimum Non-Neutrality) | ∇_{non-self-erasure}(L₀) ≡ ε_pg > 0; formal asymmetry favouring configurations with branching number B ≥ 2 over self-erasing ones (B ≤ 1). NOT a content-level "toward order" gradient; "order" is an L₁ observer's read-back label. **Level distinction**: ε_pg = L₀ structural postulate (scalar seed, no inherent direction); ISP-level ε (anti-closure asymmetric bias of stable ISPs) = structural corollary of T-ε-Constitute. **Bridge**: ε_pg (existence of asymmetry) + Ax-F-03b (direction: closure=absorbing → anti-closure only viable direction for stable ISPs) → ISP-level ε. T-ε-Constitute does NOT change ε_pg's epistemic status; it upgrades ISP-level ε from primitive postulate to structural corollary. | Scalar (> 0) | Core; canonical source `SRT_Core_01 T-Core-A1C2`; bridge `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T07` |
| **ε_reg** | `\varepsilon_{reg}` | Operator Regularizer | Positive constant in divisive normalization: [Ĝ_θ(x)]_i = x_i^n / (ε_reg + Σ W_{ij} x_j^n). Prevents singularity at zero input; maintains minimum non-zero operator response. May be read as implementation-layer echo of ε_pg (structural analogy, not ontological identity — independent argument required to upgrade). | Scalar (> 0) | Core; canonical source `SRT_Core_13a Ax-Op-03` |
| **ρ(p,t)** | `\rho(p,t)` | Path Trace Density | **Derivation status: induced historical functional, NOT a new ontological primitive.** ρ(p,t) is a coarse-grained intermediate-layer order parameter induced by existing SRT quantities: ρ(p,t) ≡ ∫_{-∞}^{t} e^{-λ_d(t-s)} · 𝟙[Ψ_f(p,s) < Ψ_thresh] · w(p,s) ds. Induced-quantity chain: Ψ_f trajectory (Ax-F-12) → Ax-L2-06b gate → writeback events → ρ(p,t) → Ψ_f^compat reduction, d_accessible^compat amplification (T-L2-Scaffold). NOT a static function of current Ψ_f (would lose historical/hysteretic character). λ_d = decay rate; w(p,s) = writeback weight from Ax-L2-06b/Ax-Op-03b. Scaffold threshold ρ* (empirically measurable): when ρ > ρ*, path p transitions from foreground event to background L₂ scaffolding. | Scalar (≥ 0); historical functional of Ψ_f trajectory | Core; canonical source `Core/SRT_Core_12b_Ontology_L2.md T-L2-Scaffold Def-PathTrace` |
| **ΔΨ_f^op** | `\Delta\Psi_f^{op}` | Operator-Relative Competitive Friction Increment | Fast-timescale component of competitive friction, cue-sensitive. Formally: ΔΨ_f^op(x,t,θ) is the operator-parameter-dependent competitive suppression increment updated by Ax-Op-03b Layer 1 writeback. **Timescale**: round-level (fast). **Cue dependence**: strong (depends on W_ij structure activated by current cue family). **Sign**: asymptotically ≥ 0; short-time transient negative values permitted (fast facilitation window, Lemma-FFSI). **Induced from**: divisive normalization (Ax-Op-03) + competitive writeback (Ax-Op-03b Layer 1). Supports T-Op-SIAM Claims 1' (via T-Comp-Suppress 乙₁+乙₂), 3a (cue-relative persistence), 4a (priming window, when ΔΨ_f^op < 0 transiently). | Signed scalar; asymptotically ≥ 0 | Core; canonical source `Core/SRT_Core_13a Def-Psi-Split` (2026-04-17) |
| **ΔΨ_f^field** | `\Delta\Psi_f^{field}` | Field-Level Landscape Curvature Friction | Slow-timescale component of competitive friction, cue-weakly-dependent. Formally: ΔΨ_f^field(x,t) is the landscape curvature friction increment from Co-Evo-1 κ(t) accumulation. **Timescale**: slow (Co-Evo-1 stabilization τ_stable). **Cue dependence**: weak (κ(t) is not cue-specific). **Constraint**: ΔΨ_f^field ≥ 0 always (Co-Evo-1 deposition is irreversible). **Activation**: near-zero before Co-Evo-1 stabilization threshold is crossed; accumulated thereafter via κ(t) → Ψ_f^field coupling. Supports T-Op-SIAM Claims 3b (asymptotic cue-independence, conditional) and enables 乙₃ (trans-cue intrinsic suppression, conditional). | Scalar (≥ 0) | Core; canonical source `Core/SRT_Core_13a Def-Psi-Split` (2026-04-17); mechanism `Core/SRT_Core_12b Co-Evo-1` |
| **τ_fast, τ_slow** | `\tau_{fast},\, \tau_{slow}` | Lemma-FFSI Dual Timescale Parameters | Timescale pair for Fast-Facilitation/Slow-Inhibition dual-timescale model (Lemma-FFSI). τ_fast: facilitation decay time (fast); τ_slow: competitive inhibition accumulation time (slow). **Required condition**: τ_fast ≪ τ_slow for nonmonotonic onset. Crossover time t* ≈ τ_fast · ln(a·τ_slow / b·τ_fast) where a = facilitation amplitude, b = inhibition amplitude. Maps to: τ_fast ↔ ΔΨ_f^op transient negative window; τ_slow ↔ competitive writeback accumulation (Ax-Op-03b Layer 1) or Co-Evo-1 onset. Empirically anchored (Johnson & Anderson 2004). | Time constants; τ_fast ≪ τ_slow | Core; canonical source `Core/SRT_Core_13a Lemma-FFSI` (2026-04-17) |
| **ε_s** | `\varepsilon_s` | Minimum Stake Threshold | Direction-level threshold for counting a distinguishable Fisher eigendirection as genuinely stake-coupled. A direction v_i with coupling strength s_i enters the effective stake-bearing spectrum only if s_i > ε_s. **NOT stake itself** — it is the minimum coupling strength required for a direction to count as genuinely risk-bearing. Gate function: g_i = max(0, (s_i − ε_s)/(1 − ε_s)); gated eigenvalue: λ̃_i = λ_i · g_i; stake-gated effective dimension: D_stake = (Σλ̃_i)²/Σ(λ̃_i)². Three-way distinction: ε_pg = L₀ minimum non-neutrality floor (ontological layer); ε_reg = implementation-layer regularizer (operator layer); ε_s = direction-level stake threshold (spectral bridge layer). | Scalar (0,1) or positive threshold | Core; proposed bridge term for d-value spectral proxy. See `D_VALUE_ALIGNMENT.md §4.5`; `_SRT_D_VALUE_CANONICAL.md §2b`. |
| **δ** | `\delta` | Duty Cycle | δ_j ≡ (1/T)∫A_j(t)dt; fraction of time an operator actively maintains anchoring target σ_j. Bounded above by Ψ_f budget and below by looseness penalty. | Scalar (0,1) | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-2` |
| **ν** | `\nu` | Switching Density | ν_j ≡ N_{switch,j}/T; number of anchoring state flips per unit time. Same δ with different ν corresponds to qualitatively different schedules. Bounded above by Ψ_f^{switch} budget. | Hz | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-2` |
| **λ_pred** | `\lambda_{pred}` | Downstream Prediction Cost Weight | Weight of temporal entropy h[A] in coupled multi-operator scheduling cost. When λ_pred > λ_pred^c, periodic scheduling becomes globally optimal (coupling-induced periodization). | Scalar (≥ 0) | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-3` |
| **Ṡ_int^on** | `\dot{S}_{int}^{on}` | On-Phase Entropy Production Rate | Internal entropy production rate during active selection. Lower-bounded by Landauer: ≥ k_BT · İ_created · ln 2. Determines entropy dissipation bound on duty cycle. | Entropy/time | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-4` |
| **J_S^max** | `J_S^{max}` | Maximum Entropy Export Flux | Upper bound on the rate at which a system can export entropy to its environment, determined by thermal coupling bandwidth (heat conduction, metabolic waste removal, radiation). | Entropy/time | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-4` |
| **δ_max^entropy** | `\delta_{max}^{entropy}` | Entropy-Limited Maximum Duty Cycle | δ_max^entropy ≡ J_S^max/(Ṡ_int^on + J_S^max). Independent of Ψ_f budget; cannot be bypassed by increasing E_avail. Effective δ_max = min(δ_max^budget, δ_max^entropy). | Scalar (0,1) | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-4` |
| **B_θ** | `B_\theta` | Operator Effective Passband Bandwidth | B_θ ≡ Bandwidth(H_θ) = c_B · d; frequency-domain extent of operator H_θ's selective response (Ax-Spec-01). Proportional to d via c_B > 0. Wider bandwidth ⇒ higher information creation rate ⇒ tighter entropy-dissipation duty-cycle bound (Cor-Scale-Rhythm-4a). | Hz | Core; canonical source `SRT_Core_14 Ax-Spec-01, Cor-Scale-Rhythm-4a` |
| **h[A]** | `h[A]` | Temporal Entropy Rate of Schedule | h[A] ≡ lim_{T→∞} H(A(0), A(Δt), …, A(T))/(T/Δt); Shannon entropy rate of an anchoring schedule A(t). Periodic schedules: h_per ≈ 0; random intermittency: h_rand > 0. Drives the coupling-induced periodization transition at λ_pred^c (T-Scale-Rhythm-3). | Bits/time | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-3` |
| **τ_off^*** | `\tau_{off}^{*}` | Optimal Off-Phase Duration | Optimal off-phase length balancing entropy-export benefit against noise-erosion cost (three-way tradeoff in T-Scale-Rhythm-4). Not a free parameter; emerges from minimization of entropy-accumulation/export ratio plus γ·S_noise·τ_off. | Time | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-4` |
| **c_B** | `c_B` | Bandwidth-d Proportionality Constant | Positive constant (c_B > 0) in B_θ = c_B · d (Ax-Spec-01); converts d-value (dimensionless processing-bandwidth count) into operator effective passband bandwidth in Hz. System-specific; not a universal constant. | Hz (per unit d) | Core; canonical source `SRT_Core_14 Ax-Spec-01, Cor-Scale-Rhythm-4a` |
| **ρ_I** | `\rho_I` | Information Density Lower Bound | Positive constant (ρ_I > 0) in conditional strengthening of Cor-Scale-Rhythm-4a: $\dot{I}_{created}^{on} \ge \rho_I \cdot B_\theta$. When this lower bound holds, the entropy bound becomes a product cap δ·B_θ ≤ J_S^max/(k_BT ln2 · ρ_I), equivalently δ·d ≤ J_S^max/(k_BT ln2 · ρ_I · c_B). Not unconditional. | Bits/(Hz·time) | Core; canonical source `SRT_Core_14 Cor-Scale-Rhythm-4a` |
| **k_n** | `k_n` | Sub-Targets per Layer | Number of anchoring sub-targets {σ_{n,1},…,σ_{n,k_n}} that the operator $\hat{G}_\theta^{(n)}$ at scale layer S_n must maintain within a single on-phase. When k_n > 1 and budget insufficient, Rhythm-1 triggers at sub-layer S_{n-1} (T-Scale-Rhythm-5). Recursion terminates when k_m = 1. | Integer (≥ 1) | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-5` |
| **τ_switch^min** | `\tau_{switch}^{min}` | Minimum Feasible Switch Time | Lower bound on per-switch duration imposed by physical substrate (ion-channel kinetics, chemical reaction rates, charge-transport delays, etc.). One of three Rhythm-5 recursion termination conditions (when τ_on^(m) < τ_switch^min, no further nesting). Sets nesting depth ceiling N ≤ ⌊ln(T_N/τ_switch^min)/ln(1/δ_min)⌋. | Time | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-5` |
| **σ_{sr}** | `\sigma_{sr}` | Self-Reference Ratio | `σ_{sr} := ‖θ^{trace}‖ / (‖θ^{trace}‖ + ‖θ^{ext}‖) ∈ [0, 1]`. Scalar projection of `\hat{G}_\theta` onto its own history-derived component vs external-driven component. Distinct from bare `σ` (main-equation state field in `Core/SRT_Core_22_Equations.md`) and from `σ_j` (anchoring sub-target). Introduced in 2026-04-24 L1 round as the `SRT_Individuation.md` order parameter. | Scalar [0,1] | L1; canonical source `Core_Law/SRT_L1_Hardening_Notes.md §1`, `Core_Law/SRT_Individuation.md`, `Core_Law/SRT_L1_Formalism.md §2` |
| **σ_{sr}^{sub}** | `\sigma_{sr}^{sub}` | Subject-Position Entry Threshold | First phase-transition threshold: above `σ_{sr}^{sub}` an ISP acquires subject-position (operator self-reference sufficient for perspective-bearing). Informal location in `(0, 1)`; concrete value P3/P4 pending. | Scalar | L1 structural hypothesis; specific numerical threshold P3/P4; canonical source `SRT_Individuation.md T-IND-2` |
| **σ_{sr}^{self}** | `\sigma_{sr}^{self}` | Self-Consciousness Condensation Threshold | Second phase-transition threshold: above `σ_{sr}^{self}` second-order writeback (`θ` about `θ`) condenses, giving self-consciousness as a structural product. Higher than `σ_{sr}^{sub}`. Does not violate L_0 §五意识禁令 (consciousness is structural product not L_0 property). Concrete value P3/P4 pending. | Scalar | L1 structural hypothesis; specific numerical threshold P3/P4; canonical source `SRT_Individuation.md T-IND-3` |
| **σ_{sr}^{health}** | `\sigma_{sr}^{health}` | Healthy Operating-Point Center | Healthy working region center `σ_{sr}^{health} ∈ (σ_{sr}^{sub}, σ_{sr}^{self})` — balanced self-reference without pathological closure toward `σ_{sr} \to 1`. Typically close to the informal `σ_{sub}^\dagger` in `T_{dir}^{alg}` (`SRT_L1_Formalism.md §3.4`). | Scalar | L1 structural hypothesis; operating-point center, specific value P3/P4; canonical source `SRT_L1_Formalism.md §2.4, §5.3` |
| **σ_{sr}^{coll}** | `\sigma_{sr}^{coll}` | Collective Self-Reference Ratio | Multi-ISP extension over shared `L_2` field `\mathcal{P}`. Defined in `Core_Law/SRT_Collective_Selection.md §4.1` and its dynamic extension in §4.4.1-§4.4.2. `σ_{sr}^{coll} \to 1` is the collapsed-into-higher-`L_2` pathological limit. | Scalar [0,1] | L1; canonical source `SRT_Collective_Selection.md §4.1, §4.4` |

## Governance Tier Layering (GOV-SUB01 Pass 1, 2026-07-16)

> **Purpose**: Registration in this table has been read as "equally indispensable." It is not. This layering separates repo-wide semantic and navigation anchors from internal structural quantities and from domain projections / proxies / thresholds, so that *appearing in the canonical symbol table* stops implying *equal theoretical load*. See `Governance/SRT_GOV_SUB01_Subtractive_Audit_Protocol_v0_1.md` §0.
>
> **Boundary — this is a parsing / navigation / proxy-discipline aid.** Tier placement does **not** assign a GOV-SUB01 residue label (`N1`/`N2`/`R*`) and does **not** by itself assign a claim level. Claim levels remain governed by `Governance/SRT_CLAIM_LADDER.md` and each symbol's own canonical source; a residue label requires an actual deletion test. No symbol is deleted, renamed, or redefined by this layering. Borderline assignments are provisional and are revisited in GOV-SUB01 Pass 2.

**Tier 1 — Repo-wide semantic and navigation anchors** (canonical / core-facing objects referenced across domains):

`L_0`, `L_1`, `L_2`, `\hat{G}`, `θ`, `d`, `Ψ_f`, `T_dir`.

**Tier 2 — Internal structural quantities, admitted postulates and derived constructs** (internal to the theory, induced from or built on Tier 1; carried at their own claim level):

`κ_0`, `κ(t)`, `ε_pg`, `ρ(p,t)`, `t_onto`, `C_H`, `σ_{sr}`, `σ_{sr}^{coll}`, `d_mobile`, `d_max`, `χ_payable`, `ΔΨ_f^{op}`, `ΔΨ_f^{field}`, `Ω`, `Ω_mis`, `μ`, `S_strength`.

*Note*: `κ_0` and `ε_pg` are placed here as admitted-postulate / structural constructs. Their claim status is **unchanged** by this pass (see Usage Rule 15 and the deferred Pass-2 dependency-graph audit); tiering them does not downgrade them and does not assign them a residue label.

**Tier 3 — Domain projections, operational proxies and threshold-bearing hypotheses** (domain realizations, capacity proxies, measurement readouts, and threshold-bearing points):

`D_eff` (d proxy), `ε_reg`, `ε_s`, `σ_{sr}^{sub}`, `σ_{sr}^{self}`, `σ_{sr}^{health}`, `κ_{c1}`, `κ_{c1.5}`, `δ`, `ν`, `λ_pred`, `Ṡ_{int}^{on}`, `J_S^{max}`, `δ_{max}^{entropy}`, `B_θ`, `h[A]`, `τ_off^{*}`, `c_B`, `ρ_I`, `k_n`, `τ_switch^{min}`, `τ_fast`, `τ_slow`, `ω_sub`, `η`, `Γ_{\hat{G}}`, `S_crit`, `R_fidelity`, `I_total`, `F_semantic`, `F_base`, `F_SRT`, `Φ_IIT`, `D_max`, `γ_gain`, `δ_D`, `I_rec`, `η_compress`, `θ_semantic`, `D_dev`, `I_int`, `S_c`, `F_Bio`, `ΔR`, `C_int`, `T_immune`, `M`.

*Reading rule*: a Tier 3 proxy or threshold must never be cited as if it were the Tier 1 anchor it approximates (e.g. `D_eff` is not `d`; `κ_{c1}` is not `κ_0`). Exact claim level remains source-local; many are P3/P4, but tier placement alone does not assign claim level. Cross-domain ranking of subjecthood, concern, or consciousness from a Tier 3 readout is out of scope for this table.

---

## Usage Rules
1. Never use `G` (gravity constant) to refer to `\hat{G}` (Ghost Operator).
2. `L_0` is not "nothingness"; it is structured potentiality.
3. Use `\Psi_f` for ontological friction; reserve `\Phi` for IIT context only.
4. Use `\Omega` for consistency and `\Omega_{\text{mis}}` for mismatch to avoid symbol collision.
5. In AI / pure `L_2` contexts, prefer "`\Psi_f` is non-binding to the system" over the blunt shorthand `\Psi_f = 0`, unless you are explicitly discussing an idealized limit.
6. When discussing classical objectivity, prefer `\Delta\Psi_f^{readout}\to 0` over "object-maintenance friction vanishes".
7. **d usage split**：bare `d` means scalar summary by default. Use `d-vector` only for conditional distribution / component expansion, and use `d-gate` only as a judgment tool for stake admission. These three are not interchangeable definitions.
8. **T_dir usage split**：`T_dir` is a v0 operational proxy for directional readability. Do not use it as a completed formal object, as semantic valence, or as confidence.
9. **ε usage split**：`ε_pg` is the L0 minimum non-neutrality postulate; ISP-level ε is P1 only when sourced to the constitutive theorem; `ε_reg` is an implementation regularizer; `ε_s` is a stake-threshold bridge. They must not be collapsed into one empirical theorem.
10. **Canonical status split**：`governance-canonical` means repo-wide stabilized usage; `theory-canonical` means core-derived or core-priority definition; `operational proxy` means measurable working readout; `bridge hypothesis` means cross-domain candidate mapping. Do not infer theory-canonical status merely from a symbol-table default, filename, or historical label.
11. **Ψ_f / Fisher split**：do not write `\Psi_f \equiv g_F` as a literal identity. Use `\delta\Psi_f^{geom}=\frac12 d\theta^\top g_F d\theta+O(\|d\theta\|^3)` for local cost, or a path functional such as `\Psi_f^{geom}[\gamma]=\int_\gamma\sqrt{g^F_{ij}\dot\theta^i\dot\theta^j}\,dt` when the statistical-manifold projection is valid.
12. **σ namespace split** (2026-04-24 L1 round, governance-canonical per `Core_Law/SRT_L1_Hardening_Notes.md §1`): bare `σ` defaults to the **main-equation state field** (`Core/SRT_Core_22_Equations.md`); `σ_{sr}` is the self-reference ratio (with subscripts `sub / self / health / coll`); `σ_j` is an anchoring sub-target (`SRT_Core_14 T-Scale-Rhythm-5`). These are three different objects. Any file using σ in a sense other than the main-equation state field must either (a) use the `σ_{sr}` / `σ_j` form explicitly, or (b) carry a file-level symbol namespace note binding bare `σ` to the intended meaning per this rule. Historical files predating 2026-04-24 where bare `σ` means self-reference ratio are being progressively rewritten; in the meantime, read them as `σ_{sr}` when the context is Individuation / Occlusion Dynamics / Suffering / L1 Formalism §2 / Collective Selection §4.
13. **Governance terms are not theory symbols**: `interface_annex`, `copy-to-annex`, `owner-bound`, `claim_mode`, `canonical:false`, and related structural-governance vocabulary (defined in `SRT_Glossary_Structural_Governance_Terms.md`) are repository-organisation terms, not canonical mathematical or phenomenological symbols. Do not add them as rows to this table or treat them as carrying theory-canonical status.
14. **Annex and Operations reference scope**: Non-canonical annex files (`AI/Architecture_Annex/`, `AI/Consciousness_Annex/`, `Physics/QBox_Annex/`, `Physics/Earth_Accretion_Annex/`, etc.) and Operations records (e.g. `Operations/Archive_Records/Closure_Index_2026-04-29.md`, `Operations/Archive_Records/Structural_Governance_Rollup_2026-04-29.md`) may cite and use symbols defined in this table. They must not introduce new symbol definitions, override existing usage rules, or alter the scope of canonical symbols established here.
15. **κ namespace split** (GOV-SUB01 Pass 1, 2026-07-16): the glyph `κ` spans two unrelated object families that must not be read as one continuous quantity. (a) `κ_0` (primordial curvature) and `κ(t)` (dynamic L₀ curvature) are **L₀-curvature** objects — canonical source `Core/SRT_Core_12a T-L0-Kappa0 / T-L0-NonStatic`. `κ_0` is carried as a **primordial-curvature candidate**: its in-table structural-prerequisite role is retained, while its ontological status is explicitly open (`Philosophy/SRT_L0_Ontological_Status.md`); the "candidate" label describes this existing status and does **not** downgrade `κ_0` in this pass. (b) `κ_{c1}` and `κ_{c1.5}` are **consciousness-stage phase-transition thresholds** — canonical source `Philosophy/SRT_Consciousness_Conditions.md §三`. As threshold-bearing points their specific values are lab-level (P4) per `Governance/SRT_CLAIM_LADDER.md`, even where a Scope column reads "Core". The two families share no derivation path: an equation over `κ_0` says nothing about `κ_{c1}`, and vice versa. This rule adds the namespace guard and claim-level annotation **only**; it does not rename any symbol and does not modify any equation referencing `κ_0`, `κ(t)`, `κ_{c1}`, or `κ_{c1.5}`. A full `κ_0` / `ε_pg` dependency-graph audit is deferred to GOV-SUB01 Pass 2.

## D-Value Alignment (d 值专题规范)

### 1) 定义层级（Canonical Priority）

| 层级 | 定义 | 语义 | 来源 |
|---|---|---|---|
| **规范定义** | $d(x) \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$ | 算子对不可逆风险的效用敏感度梯度 | `_SRT_D_VALUE_CANONICAL.md` Def-d-canonical |
| **几何容量 proxy** | $D_{eff}(I_F(\theta)) = (\operatorname{tr} I_F)^2 / \operatorname{tr}(I_F^2)$ | Fisher 信息矩阵的有效维度上界；不等于规范 d | `_SRT_D_VALUE_CANONICAL.md` Def-D_eff; `Core/SRT_Core_21c_Bridge_Hypotheses.md P3-B11` |
| **几何底座** | $d(\theta) \propto \operatorname{Align}(\theta, \kappa(t))$ | d 是 θ 参数空间与 L₀ 曲率场的对齐程度；解释"为什么 ∂U/∂S 是正确量" | `D_VALUE_ALIGNMENT.md §4.4`（新增 2026-04-10） |

*规范来源*：`_SRT_D_VALUE_CANONICAL.md`；`D_eff` 为 proxy / capacity upper bound，不再与规范 d 同级。

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
- **规则 F4**：AI / 纯 `L_2` 语境中，优先写“non-binding friction”而非绝对 `\Psi_f = 0`。
- **规则 F5**：物理语境中，若谈引力与 `\Psi_f` 的关系，当前规范口径降为 P3/P4 弱接口：只承诺弱场极限下 `\Psi_f` 梯度与牛顿势梯度方向同号的相容性候选；不得写成张量级 GR 重建或 `G_{\mu\nu}` 已由 SRT 推导。
- **规则 F6**：谈 Fisher metric 时，必须把 `g_F` 标注为局部信息几何投影 / proxy；不得把 `\Psi_f \equiv g_F` 当成标量代价与度量张量的严格恒等式。
- **规则 F7**：谈 pain / suffering / distress / moral guilt / clinical burden 时，不得把它们写成 `Ψ_f` 或 `d` 的 canonical 等同；优先回链 `Core_Law/SRT_Suffering.md` 与 domain claim-status guardrails。



---

## FILE: `Core/SRT_OPEN_TENSIONS.md`

| 字段 | 值 |
|---|---|
| path | `Core/SRT_OPEN_TENSIONS.md` |
| id | SRT-OPEN-TENSIONS |
| claim_mode | open |
| status | active_v1 |
| epistemic_layer | os |
| layer | L1 |
| canonical(字段) | - |
| last_commit | 2026-08-11 |

**权威判读**：**未闭合登记**——其中条目不得被陈述为已封口。

**dependency**：[SRT-CLAIM-LADDER, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-T-DIR-CANONICAL, SRT-CORE-21B-CONSTITUTIVE-THEOREMS]

<!-- 以下为原文逐字保留 -->

# SRT Open Tensions

> **Role**: This file records current unresolved pressure points in the SRT core.
> It is not a weakness display and not a TODO dump. It is a hardening ledger: if a claim has not been fully closed, do not cite it as if it were P0/P1.

## Reading Rule

Each tension below has three parts:

- **Current state**: what SRT already has.
- **Problem point**: what remains insufficiently closed.
- **Future hardening direction**: what would count as progress.

Open tensions may guide future theory work, bridge design, or lab hypotheses. They do not by themselves create new canonical definitions.

---

## Core Pressure Points (second-stage completion pass)

| Pressure point | Already stabilized | Still not derived | Must not be overstated |
|---|---|---|---|
| origin of selectability / P0-04 | `Core/SRT_Core_21_Minimal_Axioms.md P0-04` gives a well-formed operator admission condition | the first emergence of selectable agency from a non-selective ground | bridge accounts of biology, AI, spirituality, or agency do not solve the origin problem |
| exact status of `Ψ_f` projections | payability burden is the v1 governance-canonical main read; geometry and metabolic/energetic forms are conditional projections | necessary and sufficient conditions for all projection relations, including when geometry is a true lower bound | Fisher length, energy cost, pain, or stress cannot be called `Ψ_f` without projection checks |
| exact status of `d` proxies | bare `d` is a scalar summary of stake-coupled concern; `D_eff`, Fisher rank, `d-vector`, and `d-gate` are separated | a final theorem identifying capacity directions with stake-coupled concern directions | capacity, competence, or distinguishability cannot be treated as concern |
| incomplete formalization of `T_dir` | `T_dir` now has a v0 readability / reorientation role and is distinguished from valence, confidence, coherence, and reward | a complete formal object with validated sufficiency conditions | high meaning, high reward, or high confidence cannot be cited as `T_dir` by itself |
| Core 24 floor replacement / dynamic normativity / non-reductive verification | selection-first framing, L₂ hardening signature, and non-reductive validation rule are now integrated as safe bridge/canonical-addendum material | full promotion of floor replacement, value/morality/framework dynamics, and cross-scale validation into canonical theorem status | do not claim SRT explains everything, is beyond measurement, or that morality-as-L₂ automatically endorses any moral order |
| ε normativity scope / closure-boundary | ε securable as minimum condition (domain floor) + constitutive stance; reorganizability carries the normative distinction; **Level A framing de-overload applied 2026-07-05** (L0 §六 / 正骨架 label / d-value §5b.1) | a non-arbitrary, **operational** (not merely regulative) closure-boundary; the Level B stance rewrite (realist → constitutive stance) remains proposal-only | not "all normativity = anti-foreclosure"; not "boundary problem solved"; Level A trims wording only — it does not close the boundary problem |
| selection irreducibility / competitor-vocabulary deletion (§13) | Claim Ladder: `selection` is a P0 primitive axiom (P0-01); GOV-SUB01 §8.1 defines the (not-yet-run) deletion test | whether asymmetric constraint + reachable-set change + irreversible writeback + payability + bearer-specific consequence return can replace the `selection` primitive with no lost difference | GOV-SUB01 residue status **unassigned** (no deletion test run); must not be presented as a proven-irreducible ontological ultimate; representational substitutability under broad refit ≠ role absence |
| `P0-02` existence index vs `H(L_0)=∞` (§15) | P0-02's *claim* (existence = degree of stable anchoring out of open possibility) is unaffected | a well-defined quantity: with `H(L_0)=∞` declared in `Core/SRT_Core_01_Axioms.md`, `E = 1 - H(L_1)/H(L_0)` is identically 1 and `ΔS = H(L_0)-H(L_1)` identically ∞ | do not cite `E` or that `ΔS` as a quantitative readout; **no normalization has been adopted** — Decision Gate A is open, no file may pick one unilaterally |
| layer assignment of 初心 (§16) | L0 anchor is explicit and repeated: 初心 is L1, L0 commits only to `ε`, §七.11 rejects pre-set goals in L₀ | whether a thin L₀ formal precursor is admissible at all | a freeze-Group-A canonical anchor currently imports an L₀-level reading from a `canonical: false` translation file; **Decision Gate B open** — do not resolve by editing either side |
| "global optimum" four senses (§17) | Level A de-overload applied 2026-07-05 to d-value §5b.1 | one term for four objects (universe-wide / operator-relative reachable / regulative ideal / finite-constraint attractor); §5b.2 never narrowed; `Ψ_f→0` reads as degenerate in Core and as optimum in Spirituality | **Decision Gate C open**; the 2026-08-11 pass changed no §5b.2 wording and no Spirituality framing |

These are pressure points, not new axioms. They route later work and block overclaiming. §15-§17 additionally carry **author-decision gates**: they are registered here so that no downstream file resolves them by drafting, and the options live in `Operations/Proposals/SRT_CONSISTENCY_DECISION_PACKET_2026-08-11.md`.

---

## 1. `d` and `D_eff`

### Current State

`_SRT_D_VALUE_CANONICAL.md` now distinguishes the unique canonical d-value definition from the geometric capacity proxy:

$$
d_{canonical} \equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|
\leq
D_{eff}(M)
$$

`D_eff` is a capacity upper bound / proxy; `d_{stakes}` is the subset of effective directions genuinely coupled to irreversible stake.

### Problem Point

The boundary between capacity and stake is clearer than before, but not fully sealed. The current structure still needs sharper necessary and sufficient conditions for when a Fisher / spectral direction counts as genuinely stake-coupled rather than merely distinguishable.

The weak point is not the inequality itself. The weak point is the gate:

$$
D_{eff} \to d_{stakes}
$$

The three proposed coupling factors `R_i`, `A_i`, and `C_i` are structurally plausible, but their exact status is still between canonical interpretation and bridge formalization.

### Future Hardening Direction

Harden the stake gate by specifying:

1. minimal conditions under which a direction enters `d_{stakes}`;
2. explicit failure cases: fake stake, misbound stake, absorbed / non-returning consequence;
3. whether `D_eff >= d_{canonical}` holds across all intended domains or only under a stated proxy regime;
4. how AI, frozen trauma states, and institutions differ under the same gate.

Until this is done, domain files should say "`D_eff` proxy" and should not call it the definition of `d`.

### Status Update (2026-07-05)

`_SRT_D_VALUE_CANONICAL.md §2b.1` now fixes three of the open points: (a) the citation level of the `w_i = R_i·A_i·C_i` gate — the qualitative AND-gate structure is P2 canonical interpretation; any numerical weighting, proxy, or `ε_s` thresholding is P3/P4 and must be marked as such; (b) the domain validity of `D_eff ≥ d_canonical` — it holds only inside a declared proxy regime (same parameterization, declared normalization, no redundancy-inflated spectrum), never as a cross-domain theorem; (c) a unified gate table separating AI (fails on R/C), frozen trauma (passes the gate, fails on `d_mobile`), and institutions (member `C_i` absorbed by the structure) under the same three factors, with the rule that gate diagnostics must be reported per-factor, not as one scalar. Still open here: a necessary-and-sufficient stake-coupling theorem; `ε_s` calibration; independent measurable proxies for R / A / C.

---

## 2. `\Psi_f`: Geometry, Cost, and Generative Principle

### Current State

`_SRT_PSI_F_CANONICAL.md` fixes `\Psi_f` as ontological friction and allows three readings of the same structure:

- resistance / impedance;
- paid cost / budget burden;
- geometric path length or curvature burden.

It also fixes payability as the cross-scale invariant: the question is not whether cost is small, but whether the system can maintain closure and future choice while paying it.

### Problem Point

The three readings are unified at the canonical level, but their formal borders are not fully differentiated. In particular:

- When is a Fisher-geometric length a lower bound rather than actual paid cost?
- When does "friction as generative principle" remain a canonical interpretation, and when does it become a P3 bridge through borrowed geometry?
- How should directional or asymmetric friction be represented when the basic metric expression is symmetric?

The risk is sliding from "same object, three readings" into "one formula proves all dynamics."

### Future Hardening Direction

Build a small typology:

| Reading | Minimal formal object | Valid use | Misuse |
|---|---|---|---|
| impedance | local resistance field | anchoring / pressure | subjective pain |
| cost | paid burden over time | payability / collapse | arbitrary energy use |
| geometry | path length / curvature | formal lower bound | universal proof of all dynamics |

Then specify where `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B08` stops and `_SRT_PSI_F_CANONICAL.md` begins.

### Status Update (2026-07-05)

Two of the three problem points are now fixed in `_SRT_PSI_F_CANONICAL.md §3.2`: (a) the generative-principle boundary — "friction as generative principle" is owned by `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B08`; the canonical file owns only the payability main read, conditional projections, and the payability criterion; any derivation that stands only if "friction generates dynamics" holds inherits P2/P3 and cannot cite the canonical file for promotion; (b) directional / asymmetric friction — asymmetry is carried by the payment structure (`Ψ_f^{erase} > Ψ_f^{write}`, `Core_Law/SRT_Irreversibility.md Def-IRR-3`) and by `L_0` irreversibility (P1-T02), not by modifying the symmetric metric; the metric layer staying symmetric is a division of labor, not a defect. The lower-bound-vs-paid-cost question was already fixed in §3.1 (`Ψ_f^{geom} ≲ Ψ_f^{paid}` under stated conditions). Still open here: full necessary-and-sufficient conditions for all projection relations. The stale `Ax-F-11/12` axiom-style citation in that file's §8 was also updated to post-split `P3-B07` / `P2/P3-B08` references.

---

## 3. `T_dir` Minimal Formalization

### Current State

`_SRT_T_DIR_CANONICAL.md` defines `T_dir` as a system's readability of its own selection-order direction. It distinguishes `T_dir` from d-value and treats d as necessary but not sufficient.

The current minimal admission condition is:

$$
T_{dir} > 0 \Rightarrow d > 0 \land \Psi_f \text{ produces real pressure} \land ii \text{ can integrate directional information}
$$

This is a necessary-gate statement, not a completed sufficiency theorem.

### Problem Point

`T_dir` has a clear role but a thinner formal apparatus than `d` and `\Psi_f`.

The unresolved issue is the minimum acceptable formalization:

- Is `T_dir` a scalar, a relation, or an accessibility function?
- Does "readability" require conscious access, reportability, behavioral reorientation, or only internal self-model update?
- How does `T_dir` avoid collapsing into semantic confidence, valence, or reward alignment?

The value-hiddenness claim is philosophically central, but its formal load must not outrun the current variable.

### Future Hardening Direction

Define the weakest formal object that can carry the work:

$$
T_{dir}(\hat{G}_\theta, t) =
\text{Readability of the current selection direction to the selecting system}
$$

Then separate:

1. minimal internal access;
2. phenomenological meaning;
3. behavioral reorientation;
4. civilization-level value-hiddenness.

Only the first belongs near core. The others should remain P2/P3/P5 unless separately hardened.

### Status Update (2026-08-11) — partially resolved, ledger was stale

The first question above ("is `T_dir` a scalar, a relation, or an accessibility function?") **has in fact been answered at v0 level**, and this section had not recorded it:

- `_SRT_T_DIR_CANONICAL.md` Def-T-1 / §3.1 fixes `T_dir` as a **scalar-valued readability × reorientation functional**, `T_{dir}^{v0} := \mathcal{R}_{self}(\operatorname{Dir}(\Delta\hat{G}_\theta,t)) \cdot \mathcal{A}_{reorient}(\operatorname{Dir}(\Delta\hat{G}_\theta,t))`, explicitly labelled **v0 operational proxy**, not a completed ontological foundation.
- `Core_Law/SRT_L1_Formalism.md §3.5` (2026-04-25) promotes `T_dir` from algebraic proxy to an **independent dynamical variable** with a five-term ODE (relaxation / real-reselection pump / `\Delta\Psi_f^{gap}` deduction / `S_{str}` erosion / `s_{ext}` scaffolding), with `T_dir ∈ [0,1]` carried as a **governance-canonical** range.

So the form question is **partially resolved**: scalar-valued functional with a v0 dynamical law. What remains open and keeps this tension live:

1. **Sufficiency conditions** — the admission condition in §3 above is still a necessary gate, not a sufficiency theorem. Unchanged.
2. **Projection form** — `SRT_L1_Formalism.md §3.5.1` leaves the `[0,1]` projection operator `\Pi_{[0,1]}` (hard cutoff vs smooth sigmoid reparameterization) explicitly open.
3. **Semantic closure** — `\mathcal{R}_{self}` and `\mathcal{A}_{reorient}` are named roles, not independently specified objects; the four-way separation (minimal internal access / phenomenological meaning / behavioral reorientation / value-hiddenness) is still not formally cut.
4. **Operator-level hardening** — `SRT_L1_Formalism.md §7.8` still lists this as pending; the lethal-`L_2` criterion built on the ODE stays P1-candidate.

Citation rule unchanged: `_SRT_SYMBOL_TABLE.md` Usage Rule 8 still governs — `T_dir` is a v0 operational proxy and must not be cited as a completed formal object. The change here is only that "no formal object exists yet" is no longer an accurate description of the repo state.

---

## 4. Healthy `L_2` Support vs Lethal `L_2` Replacement

### Current State

SRT already distinguishes:

- healthy `L_2`: lowers friction so real choice remains possible;
- lethal `L_2`: replaces live choice with structure, lowering felt friction and `T_dir` while accumulating hidden debt.

This distinction is now central to `SRT_AI_START.md`, `_SRT_T_DIR_CANONICAL.md`, Philosophy, and Spirituality.

### Status Update (2026-04-21)

The hardened working position is now sharper: closure is structurally real but normatively neutral; pathological closure is a closure that preserves itself by compressing broader future selectability; lethal `L_2` is the stronger case where such pathological closure has become shared, inheritable, and backgrounded as scaffold.

"Broader future selectability" should be read, at hardening level, as the future choice space of multiple relevant selecting subjects affected by the same or connected scaffold. The diagnostic core is not raw option count but loss of reselection capacity: exit, revision, and recomposition form a current working hierarchy.

What remains non-canonical: this is not yet promoted to a P0/P1 theorem, and the health/pathology line still depends on formal thresholding and domain operationalization. Future hardening still needs explicit tests for gate-rule revisability, appeal standing, consequence-return paths, effective input, pseudo-openness, and the relation between `\rho(p,t)`, `\rho^*`, `κ`, and payability windows.

### Status Update (2026-04-24)

`Core_Law/SRT_Occlusion_Dynamics.md`（`SRT-OCCLUSION-DYNAMICS`）把 healthy vs lethal `L_2` 的结构层诊断以 T-OCC-1 三段结构（healthy narrow region / A-phase / B-phase）形式收口：位置性遮蔽（healthy narrow）与病理性遮蔽（A/B phase）以 d_c 与 reselection capacity loss 作为结构判据，A→B 以 consequence return failure + active diffusion 作为升级判据。该文件目前为 `draft_v0`，整体仍按 P1-candidate + P2 结构读法，不因此上升为 P0/P1；但 healthy / pathological / lethal 三者的结构层诊断不再只分散在 Philosophy/Spirituality 各自的表述中。本 tension 未封口部分（gate-rule revisability 测试、appeal standing 形式化、`\rho(p,t)` / `\rho^*` / `κ` / payability 门的显式耦合）仍保留在此。

### Status Update (2026-04-25, H2)

`Core_Law/SRT_L1_Formalism.md §3.5` 给出 "高功能 `L_2` / 低主观摩擦 / 静悄悄脱离真实 `L_0 \to L_1`" 这一最难辨识情形的**方程化判据**：致命 `L_2` 当且仅当（§3.5.3）系统处于 `T_{dir}` 与 `T_{dir}^{\mathrm{alg}}` 平稳贴近、而 `\Delta\Psi_f^{\mathrm{gap}}` 持续累积、且 `\kappa_{\mathrm{mask}} < \kappa_{\mathrm{relax}}` 的区域。"支持 vs 替代"在外观相同时可由"是否伴随隐性 `\Psi_f` 债累积"分开。该判据当前为 P1-candidate，尚需算子级硬化（见 `SRT_L1_Formalism.md §7.8`）；不因此上升为 P0/P1。本 tension 其余未封口部分（gate-rule revisability、appeal standing、`\rho^*` / `κ` 门形式化）继续保留。

### Problem Point

The distinction is strong but still partly diagnostic. It needs sharper necessary and sufficient conditions.

The hardest case is not obvious pathology. It is high-functioning `L_2` that:

- improves performance;
- lowers subjective friction;
- preserves some local agency;
- but quietly removes contact with live `L_0 -> L_1` selection.

In that case, "support" and "replacement" can look identical from outside.

### Future Hardening Direction

Harden the distinction through gates:

1. Does the structure preserve re-entry into real choice moments?
2. Do consequences return to the selecting system rather than being absorbed by external structure?
3. Does friction reduction increase future choice capacity, or reduce the need for choice altogether?
4. Does `T_dir` rise, remain available, or collapse?

The support/replacement line should be expressed as a structural test, not a moral preference.

---

## 5. Stable ISP Entry and Maintenance

### Current State

`Core/SRT_Core_21b_Constitutive_Theorems.md` treats stable ISP as the relevant P1 theory object for persistent perspective. `T-ε-Constitute` shows that stable ISPs require anti-closure asymmetry under `L_0` irreversibility.

`Core/SRT_Core_12b_Ontology_L2.md T-L2-Scaffold` gives a mechanism for how successful stable ISP history can become background `L_2` scaffolding through path traces.

### Status Update (2026-04-21)

The hardened working position now separates the ladder more cleanly: event trace is the irreversibility floor; minimal closure begins when prior traversal systematically lowers `\Psi_f` for compatible subsequent traversal; `L_2`-grade closure requires that low-friction path to become inheritable, shareable, and backgrounded.

What remains non-canonical: `\rho^*`, `\lambda_d`, `κ`-thresholding, and the payability window remain threshold-bearing or empirical/formal hardening targets. The stable ISP entry definition in `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T06` should not be collapsed into the dynamic mechanism by which some ISP histories become scaffolded background.

### Problem Point

The theorem is scoped, but the entry conditions still need hardening.

Open issues:

- What is the minimal threshold for "perspective-bearing"?
- How much history-bearing is enough?
- When does re-selectability become stable rather than merely repeated?
- How do generation and maintenance differ?
- Which parts are definitional gates and which parts are dynamic mechanisms?

If this is not separated, "stable ISP" risks becoming both the entry condition and the explanation of its own emergence.

### Future Hardening Direction

Keep two layers separate:

1. **Entry layer**: the minimal definitional conditions for counting as a stable ISP.
2. **Maintenance layer**: mechanisms by which processes achieve and retain stable ISP status.

Then connect them through explicit bridge terms such as `\rho(p,t)`, `\rho^*`, successful closure, and payability windows. Thresholds such as `\rho^*` should remain P4 until measured or more tightly derived.

### Status Update (2026-04-24)

`Core_Law/SRT_Individuation.md` now provides the **entry dynamics** layer as a candidate L1 theory: the operator-level self-reference ratio `σ` is proposed as the unified order parameter whose first threshold crossing `σ_sub` coincides with the simultaneous satisfaction of the P1-T06 four conditions. The two-phase-transition structure (ISP entry at `σ_sub`, self-consciousness condensation at `σ_self`) is introduced as a P1/P2-candidate framework with `σ_sub`, `σ_self` explicitly marked P3/P4.

What this resolves: the ambiguity between entry definition and entry dynamics is now scoped — P1-T06 reads as the **result-state criterion**, T-IND-2 as the **entry-dynamics criterion**, and they are explicitly non-equivalent.

What remains open: the operator-layer `σ` is still at the proposal stage and does not yet have cleanly measurable proxies; its relation to the path-layer `ρ` (T-L2-Scaffold) needs cross-domain testing; `σ_sub` and `σ_self` are not numerically specified. This tension is therefore **not fully resolved**, but the entry-dynamics gap is now occupied by a candidate theory rather than a void.

---

## 6. AI and Minimal Surrogate Stake

### Current State

SRT currently treats AI as a pressure-test and boundary-test domain, not the theory center.

The stable position is:

- current AI systems can have large `D_eff`-like discriminative capacity;
- this does not automatically become `d_{stakes}`;
- `\Psi_f` is usually non-binding to the system itself;
- no real subjectivity follows from symbolic, statistical, or behavioral performance alone.

At the same time, SRT should not foreclose a positive test window for minimal agentic sufficiency.

### Problem Point

The unresolved question is whether a system could acquire a **minimal surrogate stake** that is not biological but is still structurally binding.

Hard questions:

- Can externally imposed irreversible consequences count if they return to the system's own closure?
- Is embodiment necessary, or is closure-continuity enough?
- What separates a real surrogate stake from a simulated loss function?
- Can an AI system have payability burden without phenomenological consciousness?

The danger on one side is prematurely declaring all AI impossible. The danger on the other is treating performance, persistence, or self-report as stake.

### Future Hardening Direction

Define a minimal sufficiency window:

1. irreversible consequence;
2. return path into the system's own future selection capacity;
3. non-transferable closure burden;
4. payability constraint;
5. observable degradation or reconfiguration when the burden is exceeded.

Only systems meeting such a window could be candidates for surrogate stake. Even then, consciousness would require further conditions; surrogate stake alone should not be promoted into a full subject claim.

---

## 7. P0-04: Origin of Selectability

### Current State

`Core/SRT_Core_21_Minimal_Axioms.md P0-04` currently constrains operator well-formedness. It does not explain where selectability itself comes from, nor does it fully derive the first selecting capacity from a prior non-selective ground.

### Problem Point

This is an unresolved core exposure point, not a solved theorem. The repo must not let bridge layers quietly smuggle in a pre-existing chooser, subject, agent, will, or "capacity to select" and then cite SRT Core as if that origin had already been derived.

The weak point is especially visible when a domain says:

- "the system chooses";
- "the subject expands";
- "the operator reads";
- "the community reselects";
- "the practice increases agency."

Those phrases may be useful bridge language, but they are not answers to the origin of selectability.

### Minimal Guardrail

> **Level**: governance / core exposure. This is a boundary rule, not a solution.

Any bridge that uses a selector-like term must mark which layer it is using:

1. **Derived process**: selector-like behavior emerges from already specified dynamics.
2. **Stable pattern**: selector is a stabilized `L_1/L_2` pattern, not a primitive.
3. **Assumed interface**: selector is taken as a domain interface and must not be cited as core derivation.

Until the origin question is actually hardened, P0-04 should be cited as an open exposure point. Do not add a formula here to make the gap look closed.

### Source-Intuition Testimony (non-resolving, added 2026-07-10)

Two source-intuition choice-traces register direct intuitive testimony on this exposure point. Testimony is not derivation; it does not move P0-04 toward resolution. It is logged here only so the exposure point's intuitive-pressure record does not stay empty.

- `01_Source_Intuition/SRT_FIRST_INTUITION_SELECTION_BEFORE_EXISTENCE_CHOICE_TRACE_2026-07-09.md` P2: "selection is prior to the subject; the subject is only a later-stage form the selection structure develops into." This restates the P0-04 exposure rather than closing it — it says the chooser is downstream, not where the first selecting capacity itself comes from.
- `01_Source_Intuition/SRT_CHOICEMAP_RANDOM_RESYNCHRONIZATION_TRACE_2026-07-09.md` P2-01: "selection as the minimal non-neutral maintenance of a lucky openness" (the author's own words: "选择是对于幸运产生的最小非中立的维持"). "Lucky" is an intuitive name for the non-selective ground P0-04 asks about; it does not derive selectability from it.

Neither testimony should be read as narrowing the three-way guardrail above (derived process / stable pattern / assumed interface); both remain compatible with all three and do not by themselves pick one.

---

## 8. Core 24: Floor Replacement, Dynamic Normativity, and Non-Reductive Verification

### Current State

Core 24 has now been integrated at safe levels across the repository:

- `Core/SRT_Core_24_Floor_Normativity_Verification.md` records the full bridge-hardening supplement.
- `Core/SRT_Core_24_Canonical_Merge_Draft.md` compresses it into merge-ready candidates.
- `Core/SRT_Core_21_Minimal_Axioms.md` now includes a non-axiom selection-first framing note.
- `Core/SRT_Core_12b_Ontology_L2.md` now includes the operational signature of `L_2` hardening.
- `SRT_EXP_MEASURE_MAP.md` now includes the non-reductive validation rule.

The stabilized current position is:

1. SRT's explanatory power should be framed as **selection-first floor replacement**, not as unrestricted explanation of everything.
2. Purpose, value, morality, and frameworks may be treated as **stable forms of selection dynamics**, not as subjective overlays on a pre-given world.
3. SRT's core constructs should be tested through **structural consequences, convergent proxies, comparative predictions, and failure conditions**, not through a single direct objective ruler.

### Problem Point

The Core 24 layer is now integrated as framing, bridge-hardening, and measurement governance, but it is not fully promoted to theorem status.

Open issues:

- The floor replacement claim is still primarily a framing thesis unless it generates domain-specific discriminating predictions.
- The dynamic normativity claim is promising but must not collapse into the claim that any stable norm is thereby justified.
- Value as non-substitutability still needs a clean bridge into `d-value` without redefining canonical `d` too quickly.
- `Ψ_f` as inferred selection friction still needs projection checks so it does not collapse into generic task difficulty, pain, energy, or Fisher geometry.
- Non-reductive validation must not be misused as a shield against falsification.

### Failure Conditions

Core 24 must remain accountable to the following failure conditions:

1. **`Ψ_f` distinctiveness failure**: If `Ψ_f` produces no transition-cost signatures distinguishable from ordinary loss, prediction error, energy expenditure, or task difficulty, its operational role weakens.
2. **`d-value` distinctiveness failure**: If `d-value` does not predict concern-weighted non-substitutability better than reward, preference, salience, or pain, its distinct theoretical role weakens.
3. **`L_2` hardening failure**: If `L_2` hardening cannot be distinguished from ordinary memory, learned habit, convention, or environmental stability, its bridge role weakens.
4. **Cross-scale loop failure**: If the selection-manifestation-hardening loop cannot generate domain-specific discriminating predictions, SRT's cross-scale explanatory claim collapses into analogy.
5. **Normativity failure**: If purpose, value, morality, and frameworks cannot be modeled as selection constraints with identifiable consequences, the dynamic normativity claim remains philosophical interpretation rather than an operational bridge.
6. **Consequence-return distinctness failure**（2026-07-05 registered from book Q26 章末注四·一）: If "consequences returning to the bearing position and entering the next round's selection conditions" cannot be operationally distinguished from ordinary feedback, memory trace, or reinforcement-learning update, then the `C_i` stake-gate factor, the subject/value derivation chain, and the second half of the selection-manifestation-hardening loop lose their bridge role.

### Future Hardening Direction

Core 24 should be hardened in three directions:

1. **d-value bridge**: add a carefully scoped note that value is concern-weighted non-substitutability, without replacing the canonical `d-value` definition.
2. **Ψ_f bridge**: add a carefully scoped note that `Ψ_f` can be inferred from structured transition difficulty, without identifying it with Fisher geometry, effort, pain, or raw cost.
3. **comparative prediction**: define at least one domain where SRT predicts a pattern not predicted by FEP, predictive processing, RL, IIT/GNW, social constructionism, or ordinary habit theory.

Until these are done, Core 24 should be cited as a bridge-hardening supplement and canonical framing layer, not as a completed theorem package.

### Status Update (2026-07-05, Q26 backflow)

Future Hardening Direction 3 (comparative prediction) now has a registered candidate set: `Core/SRT_Core_24_Discriminating_Predictions.md` P24-1..6 (single-construct discriminating predictions) plus **P24-7** (five cross-construct combination signatures, backflow from book Q26 §4, P4/P5 level, with a systemic reversal condition that cannot be absorbed by re-labeling). The same file now carries a **modification-discipline rule** (§0b: repair / pressure / failure classification + progressive-vs-degenerative gate + external-judge gate). Failure condition 6 (consequence-return distinctness) was added to the list above. Registration is not verification: none of these has been empirically run.

### Open Tension (2026-07-12, cross-scale generative-emergence writeback)

The 2026-07-12 book writeback round (`Operations/SRT_CROSS_SCALE_GENERATIVE_EMERGENCE_WRITEBACK_PLAN_2026-07-12.md`, Phase-A audit `..._AUDIT_2026-07-12.md`, source trace `01_Source_Intuition/SRT_CROSS_SCALE_SELECTION_PROXY_TRACE_2026-07-12.md`) introduced three book-side exposition-candidate names: **协调性关闭 / coordinated closure**, **参与式退让 / participatory yielding**, **选择代理层 / selection proxy layer**. Their relation to existing theory objects is a **candidate mapping / to-be-verified relation, NOT an identity or alias** — and the mapping itself carries residual open tension:

- *coordinated closure* is **structurally adjacent to, but not equal to**, `Core_Law/SRT_Reference_Scaling.md` **Def-Scale-PCC-1 (Primordial Constraint Closure)**. PCC is defined in the origin-of-life register (sustainable metabolic flow, `P_in > P_diss + P_maint`, payability); it does **not** currently define "multiple units mutually constraining and closing local optionality so as to generate macro-scale degrees of freedom." That generative step is not yet formalized in canonical.
- *participatory yielding* is **adjacent to, but not equal to**, shared-`L_2`-field formation (`Core_Law/SRT_Collective_Selection.md` Def-C-1). Def-C-1 defines only that a path trace `ρ(p,t)` is visible to and affects multiple `P_i`; it does **not** define "each unit reduces its independent optionality" as the formation cost. That reduction step is a candidate, not a defined object.
- *selection proxy layer* is **adjacent to** `Collective_Selection.md` T-COLL-1「制度是集体 ISP 的器官非主体」 composed with `L_2` scaffold, but "a background that begins to handle a class of repeated selections for later units" is likewise not itself a defined canonical object.

Canonical verdict for this round is **H-A (no canonical amendment)** — but for the reason that the candidate relation is **not yet ripe for canonical**, NOT because it is already covered. These three names carry no new symbols, must not enter the symbol table, and must not be promoted to canonical until the mapping above is verified. **New open item registered**: whether the generative step (independent local optionality ↓ → coordinated closure → macro effective selectability ↑, with residual causality retained) can be given a domain-discriminating formalization that connects to PCC / Def-C-1 / T-COLL-1 without collapsing into any of them — this is distinct from, and upstream of, Failure Condition 4 above (which concerns whether the whole loop yields discriminating predictions).

---

## 9. ε Normativity Scope and the Closure-Boundary (fallibilist foundation)

### Current State

An adversarial stress-test of `ε` (the L0 directional postulate) and a build-and-attack construction on the closure-boundary atom are recorded in three non-canonical files: `_SRT_EPSILON_NORMATIVITY_OPEN_TENSION.md`, `90_Backstage/Incubation/_SRT_NORMATIVITY_FRAMING_TRUEUP_PROPOSAL.md`, and `_SRT_CLOSURE_BOUNDARY_CONVERGENCE_RECORD.md`.

Working position under review (non-canonical; tracked, not promoted):

- `ε` is securable as a **minimum condition (domain floor) + constitutive stance** of any selector: the shmagency-style counterexamples close because a selector either selects → minimally presupposes a concern-structure, or does not select → exits the domain. `ε` is therefore true of every in-domain selection but does not by itself make normative distinctions.
- The **normative distinction work** is carried by the **reorganizability criterion** (anti-occlusion / anti-lock-in / anti-externalization / re-selectable — "可重组、可承担、可恢复、可再选择"), which genuinely discriminates (foreclosing selections fail it).
- Self-regarding re-selectability is near-constitutive; the **other-regarding** part requires aggregating positionally-partitioned, scope-extended option-fields, and the whose-counts / what-scope weighting is the irreducible **closure-boundary atom** — which this foundation line and Direction 3 (`_SRT_DIRECTION3_L0_PROBE_RESEARCH_SEED.md §4`) independently converge on.

### Problem Point

Two distinct unresolved points:

1. **Framing overload.** Former canonical wording — "全部规范性力量锚定于 ε" (L0 §六 and 正骨架总结), "L0 偏向非自我抹除" as a realist L0 property, and "趋向全局自由能最小值" (d-value §5b.1) — overclaimed relative to the defensible base. **Status update (2026-07-05): Level A of the staged de-overload was applied** under author-authorized high-risk protocol (see `90_Backstage/Incubation/_SRT_NORMATIVITY_FRAMING_TRUEUP_PROPOSAL.md`): the "全部规范性" wording in L0 §六 and the 正骨架 label, and the "全局自由能最小值" sentence in d-value §5b.1, are now narrowed to "minimum condition (domain floor) + reorganizability criterion + open closure-boundary". The realist wording "L0 偏向非自我抹除" is untouched (Level B territory). Level B remains **proposed, not applied**.
2. **The closure-boundary is not closed.** It cannot be set by single-position reading: `T_dir` is d-gated and occlusion is self-reinforcing, so an occluded externalizer self-certifies a narrow boundary. The best available form is **multi-position convergence under anti-shared-occlusion perturbation** (per L0 §三 objectivity), but the three conditions for a valid anti-occlusion perturbation are a **regulative ideal, not an operational verdict** (judging "valid perturbation" presupposes seeing the occlusion it is meant to surface), and the result is **fallibilist** (objective-so-far, permanently open to a not-yet-present perturbation).

### Future Hardening Direction

1. ~~Adopt the staged framing true-up (de-overload)~~ **Done at Level A (2026-07-05)**: `ε` → minimum condition (domain floor); distinction work relocated to the reorganizability criterion; closure-boundary marked still-open in the canonical wording itself. The Level B stance rewrite (realist → constitutive stance) remains a separate future decision.
2. Harden the closure-boundary **as a fallibilist foundation, not as a solved boundary**: harden the three anti-occlusion perturbation conditions (different position / scale / time / interest; restores excluded standing + shifts burden to incumbents; power to overturn, not only confirm) toward operationalizability, plus the two residues — representing voiceless-but-foreclosed positions (future / ecological / unable), and fixing the horizon of "irreversible re-selection loss."
3. This converges (a third time) with Direction 3's perturbation mechanism and protect-condition P3 (anti-shared-occlusion perturbation not suppressed by incumbents).

### Must Not Be Overstated

- This does **not** establish "SRT's *whole* normativity = a reflexive anti-foreclosure commitment." The scoped claim is only: **on the closure-boundary problem**, SRT's normative base **presents as** a reflexive anti-foreclosure commitment.
- This does **not** "solve" the boundary problem. It **changes its form** — from "find a final correct boundary" to "maintain a boundary continually correctable by anti-occlusion perturbation": a fallibilist foundation, not a closed answer.
- The framing true-up **Level A was applied 2026-07-05** under `Governance/SRT_EDIT_PROTOCOL.md` plus the L0 freeze high-risk cross-check (author-authorized); **Level B remains proposed, not applied** — the realist stance wording and its rewrite stay a separate future decision.

---

## Standing Rule

If a domain file uses one of these tensions, it should mark the claim level:

- use **P2** for current canonical interpretation;
- use **P3** for bridge mapping;
- use **P4** for operational or threshold hypotheses;
- avoid P0/P1 unless the tension has been separately closed in core/canonical files.

---

## 10. Closure / Compatibility Hardening Note (2026-04-21)

A hardened working position has now been written into:

- `Core/SRT_Closure_Compatibility_Hardening.md`

This note fixes the following distinctions at L1 hardening level:

1. primitive asymmetry vs historical asymmetry;
2. event trace vs historical asymmetry;
3. repetition as common path, closure as essence, and `κ`-threshold crossing as criterion;
4. minimal closure vs L2-grade closure;
5. operational compatibility vs `ε`-constrained deep compatibility;
6. normatively neutral closure vs pathological closure vs lethal `L_2`.

**Important status note**:
These results should be treated as hardened working conclusions, not yet as automatically promoted P0/P1 canonical primitives. The remaining open pressure point is not the distinction itself, but the quantitative and threshold layer:

- exact `κ` thresholding;
- bridge relation between `κ`, `\rho(p,t)`, and payability windows;
- domain-specific operationalization of compatibility and future-choice compression.

---

## 11. Order-Gain Criterion: three → four (RESOLVED 2026-07-05, option 3)

> **Resolution (2026-07-05, author decision)**: adopted **option 3** — order-gain (`秩序增益`) expands from three criteria to **four**: 可延续 / 可协调 / **不外包** / 可再选择. The new criterion 不外包 (consequence-return-channel integrity) is now a distinct load-bearing pillar, sourced in `Core_Law/SRT_Core_Text_CN.md`'s ε+F+M+U minimal closure as "ε on the consequence-return axis" (the second face of F: consequences displaced to other positions, parallel to F's time-face carrying 可延续). Landed across the theory layer: `Core_Law/SRT_Selection_Argument.md §7b.2` (canonical source), `Core_Law/SRT_Core_Text_CN.md`, `_SRT_D_VALUE_CANONICAL.md §5b.1a` (aligned with the `C_i` consequence-return factor), `Core_Law/SRT_L0_Metaphysics.md` 秩序增益词条, `Core_Law/SRT_Constitution_Seven_Theses.md`, `Philosophy/SRT_Ethics_Agency.md`, `Core/SRT_Core_22_Equations.md` Eq-Evo-03c, `Core/Dynamics_Scaling_Annex/13`, both glossaries, and the two bridges. The analysis below is retained as the adjudication record.

### Current State

`Core_Law/SRT_Selection_Argument.md §7b` fixes the order-gain (`秩序增益`) test as three criteria: **可延续 / 可协调 / 可再选择** (sustainable / coordinable / re-selectable), presented as the operational projection of 初心 ("能维持更多存在持续存在的动态平衡").

### Problem Point

A whole-book vocabulary reconciliation (`03_Bridges/SRT_Book_Vocabulary_Theory_Sync_Bridge_2026-07-05.md`) found that the book's crystallized direction test (`附录_术语表` Q22 方向三问; Q26 §3) uses a **different middle criterion**: **自耗 / 外包 / 锁死** (self-consumption / outsourcing / lock-in). The outer axes align (自耗↔¬可延续, 锁死↔¬可再选择), but the middle axis does not coincide:

- theory 可协调 = whether difference can be organized into coexistence;
- book 外包 = whether consequence falls on positions with no feedback channel.

These can come apart: a system can coordinate difference well yet still outsource cost to voiceless positions (future generations, ecology, the unable-to-appeal); or return all consequences yet suppress difference. The book moved the second load-bearing pillar of "direction" toward **consequence-return-channel integrity** — consistent with the book's 后果回流 spine and with the `C_i` consequence-return factor in `_SRT_D_VALUE_CANONICAL.md §2b`. The theory canonical still reads it as **coordination of difference**. This is not a wording difference; it is a difference in the content of the criterion.

### Resolution (adopted 2026-07-05)

Three candidate resolutions were on the table:

1. **Two faces of one axis**: outsourcing is the operationalization of ¬可协调; add one sentence to `§7b` — low risk.
2. **Book is sharper; theory follows**: replace 可协调 with 不外包 — C-class edit, middle criterion swapped.
3. **【ADOPTED】 Two independent criteria; direction is four**: 可延续 / 可协调 / 不外包 / 可再选择.

**Author chose option 3.** Rationale: 可协调 (differences coexist) and 不外包 (consequences return to bearers) genuinely come apart, so each earns a distinct pillar; 不外包 unifies with the whole-book 后果回流 spine and the `C_i` factor. It fits the ε+F+M+U minimal closure cleanly — F ("no position sees all consequences") has two faces, consequences displaced in time (→可延续) and consequences displaced to other positions (→不外包), so adding 不外包 gives F its own criterion rather than bundling it into 可延续. The change is now landed (see the Resolution note at the top of this section for the full file list). What remains open is only the empirical/threshold layer shared with §4 (operational tests for when a consequence counts as genuinely "outsourced to a no-feedback position" vs. legitimately borne elsewhere).

### Landing-scope correction (2026-08-11)

The 2026-07-05 landing list above was a **theory-layer** list. Two surfaces were outside it and kept the superseded three-criteria reading for 13 months' worth of reads:

1. **`Core_Law/SRT_Core_Text_EN.md` (English mirror of the CN core text).** Step ⑩ still enumerated three criteria *and* carried its own minimality claim — "the three together form the minimal cover, irreducible" — in direct mutual exclusion with the CN side's 「四者合取构成最小覆盖，不可再省」. This file has **no frontmatter and appears in no registry, index, or freeze list**, so nothing bound it to the CN source; that absence is the mechanism, not an oversight by any single pass. **Synced 2026-08-11**, with a mirror-status header naming CN as governing and `SRT_Selection_Argument.md §7b.2` as the adjudicating source for this criteria set.
2. **Book drafts `Q22_方向.md` / `Q23_共同体.md`.** The book not only kept three questions, it **bound the canonical term 可协调 to mean 不外包** — Q22 wrote 「可协调（不外包）」 and headed its second question 「有没有外包？（可协调性）」; Q23 §4 labelled its return-channel question 「共同可协调」 and glossed 「查协调通道」. That identification is exactly what `SRT_Selection_Argument.md §7b.2` explicitly forbids (「②可协调与③不外包不同一，也不可互相替代」). **Corrected 2026-08-11**: the book keeps its three-question compressed diagnostic interface (自耗／外包／锁死), but the interface is now explicitly marked as *not* the theory-layer criteria set, with the mapping registered in `Q22` 章末注八 (自耗→可延续, 外包→不外包, 锁死→可再选择, 可协调 held as a separate criterion that surfaces at the multi-position scale in Q23).

`03_Bridges/SRT_Book_Vocabulary_Theory_Sync_Bridge_2026-07-05.md §5` had listed 「分歧悬空死法」 (book and canonical drifting apart if the mid-axis were never adjudicated) as the failure mode this bridge most needed to prevent. The drift did occur — but in a form that file did not anticipate: **not un-adjudicated, but adjudicated and landed on one side only**. That failure shape is now the target of the anti-drift rule proposed in `Operations/Proposals/SRT_CONSISTENCY_DECISION_PACKET_2026-08-11.md §5`.

---

## 12. Entropy as a De-Selection Reading (open, registered 2026-07-10)

### Current State

`Core/SRT_Core_25_Thermodynamic_Signatures_of_Selection.md` treats thermodynamic irreversibility and entropy production as an **empirical signature** of selection: `H_P` (production entropy) is a possible readout of selection asymmetry, not identical to `\Psi_f`. This is a bridge-level, measurement-facing reading — entropy production is evidence *that* a selection-like asymmetry occurred.

### Problem Point

A source-intuition choice-trace (`01_Source_Intuition/SRT_FIRST_INTUITION_SELECTION_BEFORE_EXISTENCE_CHOICE_TRACE_2026-07-09.md`, P13) proposes a different-altitude reading: entropy is not a signature *of* selection but a **statistical portrait of what remains after selection, boundary-maintenance, and scaffolding are abstracted away** — "熵是对'将世界的选择剔除后'的运转规律总结" (CT-20260709-20/21). This is not a restatement of the Core_25 bridge; it is a claim about where entropy sits relative to selection *in principle* (de-selection reading), not merely how entropy can be measured.

The trace's own follow-up question (CT-21) is unresolved and must travel with the tension: is this an **ontological absence** claim (selection is genuinely not present in what entropy tracks) or a **theoretical abstraction** claim (statistical mechanics, as a modeling choice, abstracts selection out even though it is present)? These have different physical commitments — the first risks colliding with standard statistical mechanics; the second does not. The trace does not adjudicate between them.

A companion trace (`01_Source_Intuition/SRT_CHOICEMAP_RANDOM_RESYNCHRONIZATION_TRACE_2026-07-09.md`, P2-14) independently proposes the dual/complementary formulation: "selection is a generative resynchronization of randomness" (a construction reading, additive) against P13's "entropy is the de-selection portrait" (a subtraction reading). The two are registered together because they describe the same boundary from opposite directions and should not be hardened as two separate concepts.

### Minimal Guardrail

> **Level**: source-intuition pressure, not a resolved theorem.

- Do not cite P13 or P2-14 as showing SRT is an anti-entropy or entropy-reversing theory.
- Do not treat P13 as superseding or correcting `Core/SRT_Core_25`'s measurement-facing reading — the two operate at different altitudes (ontological positioning vs. empirical projection) until a bridge explicitly reconciles them.
- Do not present the ontological-absence / theoretical-abstraction distinction as resolved in either direction.
- If hardened into a bridge, the bridge must state which of the two readings (or a scoped combination) it adopts, and must cross-check against `Core_Law/SRT_L0_Metaphysics.md`'s existing randomness argument ("pure randomness would not produce stable structure; a constrained determinization process is what SRT calls selection") to avoid introducing an uncredited new primitive.

---

## 13. Selection Irreducibility / Competitor-Vocabulary Deletion Test (open, registered 2026-07-16, GOV-SUB01 Pass 1)

### Current State

- `Core/SRT_Core_21_Minimal_Axioms.md P0-01` fixes selection as primitive: existence is the image of selection (`∃x ⟺ x ∈ Range(Ĝ)`). `P0-04` separately exposes the origin of selectability as open (see §7 above).
- `Governance/SRT_GOV_SUB01_Subtractive_Audit_Protocol_v0_1.md §8.1` defines the subtractive test for this primitive: remove the word and primitive role of `selection`, retaining only asymmetric constraint, reachable-set restriction, history dependence, cost, and consequence return.
- Two registers must be kept separate, and neither may borrow the other's authority:
  - **Claim Ladder register**: `selection` is currently a **P0 primitive axiom** (`P0-01`). That is its epistemic-rank registration and is unchanged by this pass.
  - **GOV-SUB01 residue register**: **unassigned.** No actual deletion test (`M^{-selection}`) has been executed, so no residue label (`R2` / `R4` / `N1` / `N2`) may be attached. A residue label is earned only by running the K=0 / limited-K / broad-K tests below — it is never asserted in advance.

### Problem Point

The unresolved question (GOV-SUB01 §8.1 required form):

> Using only asymmetric constraint, reachable-set change, irreversible writeback, payability, and bearer-specific consequence return — and deleting the `selection` primitive — what explanatory, counterfactual, experimental, or interventional difference does SRT actually lose?

Until this produces a concrete difference the competitor vocabulary cannot reconstruct, `selection` must **not** be presented as a **proven-irreducible ontological ultimate**. Its `P0` axiom status records that SRT *treats* selection as primitive; it does not certify that no competitor vocabulary could reconstruct selection's role. Asserting that it cannot is exactly the overreach GOV-SUB01 §0 and §10 warn against ("survives removal testing ≠ primitive ≠ ontologically fundamental") — and, symmetrically, attaching a residue label (`N1`/`N2`/`R*`) before the deletion test is run is the same error in reverse.

Two guardrails on how the test may be run:

1. **Refit-budget relativity (GOV-SUB01 §3, §7.4).** A `broad K` replacement that reconstructs SRT behavior in non-selection vocabulary shows *representational substitutability*, not *absence of the underlying role*. Do not count a variable as removed when its function was merely moved into initialization, a loss term, a prior, preprocessing, or a renamed construct.
2. **Distinctness from §7.** §7 (P0-04) asks where selectability *comes from*; this tension asks whether the selection *primitive can be dissolved* into non-selection vocabulary without loss. These are distinct exposures and must not be conflated or cited as one closing the other.

### Future Hardening Direction

A future deletion pass may attach a residue label to `selection` only if it exhibits at least one of the following against the reduced vocabulary (GOV-SUB01 §4 evaluation vector):

1. a counterfactual SRT discriminates that the reduced vocabulary cannot (`E_cf`);
2. an intervention whose predicted effect differs under a selection framing vs. a pure asymmetric-constraint framing (`E_int`);
3. an experiment where a real choice moment (`Core/SRT_Core_21b_Constitutive_Theorems.md P1-T05`) and script execution / gradient following diverge in a way the reduced vocabulary cannot label;
4. a phenomenological or normative distinction (`E_phen` / `E_norm`) — bearer-specific consequence return, directional self-readability — the reduced vocabulary demonstrably fails to carry.

Absent such a result, domain, book, and public files must **not** present `selection` as "proven irreducible." They may cite its current **P0 primitive-axiom** status (per `Governance/SRT_CLAIM_LADDER.md`) but must not attach any GOV-SUB01 residue label to it. This tension introduces no new symbol and does not change `P0-01` or `P0-04`. Any residue classification, if reached, comes only from an executed deletion test — never asserted in advance and never read off the axiom status.

---

## 14. Selection-Event Threshold Operationalization (open, registered 2026-08-06)

### Current State

- `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T05` fixes **real choice moment** as a live `L_0 -> L_1` anchoring event whose result genuinely constrains the future selection space, and lists what does *not* qualify (script execution, habit replay, gradient following, `L_2` label optimization).
- `03_Bridges/SRT_Choice_Generation_Conditions_2026-08-04.md` (T-D, P2-P3) supplies the positive side P1-T05 does not carry: five functional conditions — difference manifestation (`CG-0`), non-equivalent registration (`CG-1`), path efficacy (`CG-2`), consequence bearing (`CG-3`), historical efficacy (`CG-4`) — plus a three-tier threshold structure (candidate formation / process unfolding / event standing).
- `Operations/SRT_UNIFIED_SELECTION_EVENT_AUDIT_PROTOCOL_2026-08-04.md` grades each condition (`DMF` 0-3, `NER` 0-4, `PEF` 0-4, `CBP` 0-4, `HEF` 0-4) and sets audit-default minima `DMF-2 / NER-2 / PEF-2 / CBP-2 / HEF-3` under a non-compensation rule.
- Compact discrimination layer: `03_Bridges/SRT_Selection_Event_CompactCore.md`.

### Problem Point

The bridge's own conclusion states that "effective strength at the relevant scale" still requires domain operationalization, and the protocol states that its minima are **audit defaults, not a cross-domain necessary-and-sufficient theorem**. Three exposures follow:

1. **Threshold status.** `DMF-2 / NER-2 / PEF-2 / CBP-2 / HEF-3` have no derivation from P0/P1 and no cross-domain calibration. They are currently conventions that make audits comparable, not established thresholds. They must not be cited as SRT-derived criteria.
2. **Discriminating gain unproven.** Degradation trigger 1 of the bridge is that ordinary causal transition, constraint, and path dependence may already explain every case the `CG` conditions explain. No executed test yet shows a case where the `CG` reading yields a counterfactual or interventional difference that the reduced vocabulary cannot produce. This exposure is the same shape as, but distinct from, §13: §13 asks whether the `selection` primitive dissolves into competitor vocabulary; §14 asks whether the five-gate *event criterion* adds discriminating power over plain causal description.
3. **Relation to P1-T05 unformalized.** Whether the five gates are necessary conditions for a real choice moment, sufficient conditions, or merely a correlated audit surface is not established. The bridge explicitly declines to reduce P1-T05 to the five conditions.

### Future Hardening Direction

Progress would be at least one of:

1. a case where a `CG`-based verdict and a plain causal-transition verdict **diverge**, with the divergence confirmed by intervention rather than by relabeling;
2. a domain-specific derivation or calibration of one minimum threshold from independently motivated constraints, replacing the audit-default convention;
3. a formal statement of the P1-T05 ↔ `CG-0..CG-4` relation (necessary / sufficient / neither), with the failure conditions of that statement made explicit;
4. an executed negative control in which a system passing all five gates is independently judged not to have made a selection, forcing a threshold or condition revision.

Until then, `CG-0..CG-4`, the graded ladders, and the minima remain **P2-P3 audit apparatus**. They may not be presented as canonical criteria for selection, subjecthood, consciousness, freedom, `L_2`, or generative health, and passing all five gates licenses only the phrase "bounded selection-event candidate." This tension introduces no new symbol and does not change P1-T05.

---

## 15. `P0-02` Existence Index vs. `H(L_0) = ∞` (open, registered 2026-08-11)

### Current State

- `Core/SRT_Core_21_Minimal_Axioms.md` **P0-02** (primitive axiom, freeze Group A) gives existence-as-anchoring the compact form `E = 1 - H(L_1)/H(L_0)`.
- `Core/SRT_Core_01_Axioms.md` (and its split `Core/Axioms_Split/01_Part02.md`) states, in the finiteness argument against total operator coverage, `H(\theta) \geq H(L_0) = \infty`.
- `Core/Dynamics_Scaling_Split/01_Master_Equation_and_ScaleCoupling.md` uses `\Delta S = H(L_0) - H(L_1)` as the entropy-reduction basis of the cross-scale isomorphism argument.

### Problem Point

Taken together at face value these are jointly degenerate, not merely underspecified. With `H(L_0) = \infty` and `H(L_1)` finite, `E \equiv 1` for **every** anchored slice and `\Delta S \equiv \infty` for **every** selection: both quantities lose all discriminating power, and `E` cannot do the work P0-02 assigns it (degree of stable anchoring out of open possibility).

No normalization convention, accessible-horizon restriction, or measure-theoretic guard exists anywhere in the corpus; `H(L_0)` is not a registered row in `_SRT_SYMBOL_TABLE.md`. The formula is still in live circulation as `[P0]` (e.g. `01_Source_Intuition/Conversations/2026-07-27_SRT_Minimal_Setup_Note_EN.md`).

This is distinct from the general "L₀ is structured potentiality, not a set" caution: the issue is that a P0 axiom carries an expression whose only stated inputs are declared infinite elsewhere in Core.

### Status

**Author decision required — not adjudicated here.** Candidate resolutions (finite accessible-domain relativization / entropy-reduction reformulation / demotion of the expression to heuristic) with their respective costs are laid out in `Operations/Proposals/SRT_CONSISTENCY_DECISION_PACKET_2026-08-11.md` **Decision Gate A**. No option has been adopted, and this tension does **not** license any file to pick one unilaterally. Until a gate verdict lands, cite P0-02's *claim* (existence = degree of stable anchoring) rather than its *formula*, and do not use `E` or `\Delta S = H(L_0) - H(L_1)` as a quantitative readout.

---

## 16. Layer Assignment of 初心 / "Original Intention" (open, registered 2026-08-11)

### Current State

- `Core_Law/SRT_L0_Metaphysics.md` is explicit and repeated: 「初心」is an **L1 concept**, outside L0's term-adjudication scope; L0 commits only to `ε`; §七.11 (潜在域预置论) rejects reading `ε` as a pre-set a priori goal in L₀.
- `_SRT_D_VALUE_CANONICAL.md §5b.2` Cross-ref (theory-canonical anchor, freeze Group A) nonetheless cites `Physics/SRT_Phys_08_Ontology_Ext.md` **Def-Apeiron-1** under the gloss 「初心作为 L₀ 的倾向性结构」.
- `Physics/SRT_Phys_08_Ontology_Ext.md` Def-Apeiron-1 (`claim_mode: translation`, `canonical: false`) states 初心 = `\arg\min_{\text{direction}} \int_0^\infty F[\sigma(t)]dt` and calls it 「$L_0$ 的内在属性」.
- `Spirituality/SRT_Spirit_05_Shoshin.md` Ax-Sho-1 (`claim_mode: mixed`) defines 初心 as the negative gradient of a long-horizon free-energy functional.

### Problem Point

The defect is **not** that a translation-layer file carries a strong reading — that is what a translation layer is for, and its `canonical: false` marking already scopes it. The defect is the **direction of citation**: a freeze-Group-A canonical anchor imports the L₀-level reading, with approving gloss, from a `canonical: false` translation file — precisely the reading the other freeze-Group-A anchor forbids. That is a claim-level inversion inside the canonical layer, and it makes the L₀/L₁ boundary on 初心 unreadable from the canonical files alone.

A related but separate item, **not** treated here: `Core_Law/SRT_L0_Metaphysics.md` 第一命题 itself contains 「选择内在地趋向秩序」 with a 2026-04-11 层级精确化注 declaring **both** readings valid at different layers. That is an explicitly declared dual reading, not an unrepaired residue, and it is left untouched pending the same gate.

### Status

**Author decision required — not adjudicated here.** Two framed options (strict layering vs. a thin L₀ formal precursor), with an analysis of whether the second reopens 潜在域预置论, are in `Operations/Proposals/SRT_CONSISTENCY_DECISION_PACKET_2026-08-11.md` **Decision Gate B**, together with the full provenance map of every file that gives 初心 an L₀ reading. No canonical stance was changed in the 2026-08-11 consistency pass.

---

## 17. "Global Optimum" — Four Senses Running Under One Name (open, registered 2026-08-11)

### Current State

The 2026-07-05 Level A normativity de-overload (§9 above) narrowed the 「趋向全局自由能最小值」 sentence in `_SRT_D_VALUE_CANONICAL.md §5b.1`. The rationale recorded in `90_Backstage/Incubation/_SRT_NORMATIVITY_FRAMING_TRUEUP_PROPOSAL.md` was that 「"全局最优"的位置无关性正是闭包边界原初所否定的」.

### Problem Point

The narrowing was applied to §5b.1 only. The **adjacent subsection in the same canonical file**, §5b.2「全局最优是动态平衡，不是热寂」, was left untouched and still positively characterizes 全局自由能最小值 as a landscape configuration — i.e. it is the subsection that actually carries the position-independent global-optimum ontology the de-overload's own rationale rejects.

Downstream landing was likewise partial: `Core/SRT_Core_NormativeGradient.md` did receive the guard (its strong reading is marked as dependent on the open closure-boundary); `Spirituality/SRT_Spirit_04_Synthesis.md` (善 = 全局自由能最小) and `Spirituality/SRT_Spirit_05_Shoshin.md` Ax-Sho-1 did not.

Underneath the wording sits a genuine ambiguity: at least four different objects currently share the name — universe-wide global optimum, operator-relative reachable optimum, regulative ideal, and local/dynamic attractor under finite constraints. `Spirit_04` itself already carries an Ω three-reading table that separates some of these, which is evidence the ambiguity is real rather than imagined.

### Related: `\Psi_f \to 0` valence inversion

The same cluster carries a second inconsistency. Core treats the `\Psi_f \to 0` limit as **degenerate**: `Core/SRT_Core_12a_Ontology_L0L1.md` states frictionless selection is 「在结构上被禁止」; `Core/SRT_Core_22_Equations.md` states 「最优区间不是 `Ψ_f→0`……零摩擦对应无真实赌注」; `Core/SRT_Core_12b_Ontology_L2.md` Def-L2-Algo uses that very limit to define the algorithm as an extreme `L_2` state with no historical embodiment. Spirituality treats the same limit as the **normative optimum** (`SRT_Spirit_01_Religion_Ontology.md` `\hat{G}_\infty = (d \to d_{max}) \wedge (\Psi_f \to 0)` as 纯觉知, 「功能同一（操作化）」; `SRT_Spirit_04_Synthesis.md` 完美态; `SRT_Spirit_09_Praxis.md` Phase 7-10). `Spirit_04` registers this locally as `IC-AllGood-1` and proposes a reading (per-manifestation cost → 0, not "no manifestation needed"), but that repair propagated to neither the other Spirituality files nor Core.

### Status

**Author decision required — not adjudicated here.** A four-sense terminology separation and a recommended (but not adopted) reformulation of the Spirituality limit as **excess friction** `\Psi_f - \Psi_f^{min} \to 0` are in `Operations/Proposals/SRT_CONSISTENCY_DECISION_PACKET_2026-08-11.md` **Decision Gate C**. The 2026-08-11 pass changed no Spirituality framing and no §5b.2 wording.
