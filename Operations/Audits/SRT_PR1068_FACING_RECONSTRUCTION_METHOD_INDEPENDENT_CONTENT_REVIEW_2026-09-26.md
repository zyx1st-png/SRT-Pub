---
id: SRT-PR1068-FACING-RECONSTRUCTION-METHOD-INDEPENDENT-CONTENT-REVIEW-20260926
type: audit
status: active
date: 2026-09-26
layer: governance
epistemic_layer: operations
claim_mode: independent_review
canonical: false
research_mode: U
dependency:
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_FACING_GENERATIVE_CONTINUITY_POSITION_METHOD_2026-09-26.md
  - 01_Source_Intuition/SRT_DIALOGUE_DERIVATION_TRACE_FACING_GENERATIVITY_POSITION_METHOD_2026-09-26.md
  - Operations/Proposals/SRT_FACING_RECONSTRUCTION_SIMPLIFICATION_METHOD_V0_1_2026-09-26.md
tags: [IndependentReview, PR1068, Facing, L0Facing, Position, One, Orientation, GenerativeContinuity, NonObjectification, ReconstructionMethod, PreflightCorrection]
---

# PR #1068 独立内容评审 — Facing 分离 / Position 与 L0-facing 连续性 / 重构简化方法 v0.1

> **角色**：对**已合并**的 PR #1068 做合并后独立内容评审。#1068 把仓库唯一的 CURRENT NEXT 改成了一次 Facing 重构 / 简化 pass，所以本评审的主要作用是**在这次 pass 执行之前**校正方法本身。只读：本记录不修改 #1068 的任何文件、STATUS、路由面或 canonical owner，也不替作者关闭任何 OPEN。
>
> **评审者独立性**：独立 session，没有参与 #1068 的对话或写作。本 session 评审过 #1066（#1067），当时的 F1 批评了概念膨胀，而 #1068 的简化方向正是对这一点的回应。评审者因此可能倾向于赞同这次改向，特此披露。
>
> **评审局限**：原始对话不在仓库中，A0-Q 的逐字性和逐项“作者接受”无法核验。三份新增文件**全部通读**，STATUS 与研究程序的 diff 全部核对；canonical owner 与既有邻居审计只读了相关节，并在各发现中注明行号。

## 0. 评审对象

```text
PR:    #1068 (MERGED 2026-09-26 12:56Z by author) “Facing reconstruction method + source trace”
head:  a72dca20   base: b5ceac42 (= #1066 merge)   merge: de12cd41
time:  commits 20:35 → 20:42 (+0800); PR opened 12:42Z, merged 12:56Z; 5 commits, 5 files, +2612 / −24

AJ = 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_FACING_GENERATIVE_CONTINUITY_POSITION_METHOD_2026-09-26.md (550)
TR = 01_Source_Intuition/SRT_DIALOGUE_DERIVATION_TRACE_FACING_GENERATIVITY_POSITION_METHOD_2026-09-26.md (1304)
MT = Operations/Proposals/SRT_FACING_RECONSTRUCTION_SIMPLIFICATION_METHOD_V0_1_2026-09-26.md (699)
PG = cognition research programme (routing update only, +41 / −7)
ST = STATUS.md (CURRENT NEXT routing, l.111 / l.896–923; +18 / −17)
```

控制 owner / source（在 de12cd41 上读取）：

- `_SRT_SYMBOL_TABLE.md` l.27（Aspect boundary）、l.31（L₀ = Selection's open / non-preclosed aspect）；
- `Core_Law/SRT_L0_Metaphysics.md` l.283；
- `Core_Law/SRT_Generative_Ontology_Spine.md`：
  - §2.1 l.119–127：`Selection occurrence != retained historical efficacy != sedimentation != generative inheritance`；
  - §2 l.138：O0；
  - §5 l.243–274：One 的最低条件；`ordinary path dependence != One`；branch / merge OPEN；
  - §6.1–6.3 l.280–320：finite positionality、formed Selection-position、anticipation 护栏；
  - §8：Bearer 与 P / E；
- `Glossary/SRT_Live_Term_Router.md`：l.31–38 hardening gate、l.90 Selection-position、l.113 generative reconstructibility、l.118 Ψ_f / A-9；
- `_SRT_PSI_F_CANONICAL.md`：Def-Ψ-1 l.66–88、§3.2 l.252–；
- `Governance/SRT_EDIT_PROTOCOL.md` l.83–（same-day rapid author-dialogue guard）；
- STATUS l.358–359（A0-Q / A0-P schema）；
- `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_SPINE_MINIMAL_KERNEL_L0L1L2_REFLEXIVE_FACETS_2026-09-24.md`（下称 K24）；
- `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GENERATIVE_EXPECTATION_TYPING_2026-09-20.md`（下称 E20）；
- HP-B 冻结记录 `Operations/Audits/SRT_PR1063_B1_B5_CORRECTIVE_FINAL_CONSISTENCY_REVIEW_2026-09-26.md` §5；
- 既有邻居审计：
  - Whitehead：`…CYCLE3_CREATIVE_PRIMITIVE_PRESSURE_PASS1_2026-09-06.md` §3.2；
  - Barad：`…PREOBJECT_FOREGROUND_OBSERVABILITY_BARAD_STRONGEST_NEIGHBOR_PASS13_2026-09-10.md` §10；
  - Simondon：`…SELECTION_ARTICULATION_EXTERNAL_NOVELTY_AUDIT_2026-08-28.md` l.202；
  - `…L0_FACING_FIELD_H1_H2_H3_LEVEL_RECLASSIFICATION_2026-09-26.md` l.26、l.534。

## 1. Verdict

```text
CANONICAL IMPACT (file edits)                                  = NONE (no Freeze-A owner touched)
SAME-DAY RAPID-DIALOGUE GUARD                                  = FOLLOWED (source -> bounded map -> later landing)
STATUS SINGLE CURRENT NEXT (l.111 = l.896)                     = CONSISTENT (resolves #1066 review F8)
DIRECTION (simplify before simulating)                          = SOUND; answers #1066 review F1
METHOD SKELETON (reverse + forward, stop rules, fail criteria)  = GOOD
HARD GUARDS (AJ §16)                                            = GOOD

CENTRAL CANDIDATE “L0-facing continuity”                        = MIXES FACINGS; likely reducible to existing K (F1)
“Facing separation” novelty / citation                          = EXISTING CANONICAL ASPECT RULE, NOT CITED; “L0” used in 3 senses (F2)
FORWARD TEST / EMPIRICAL FOOTHOLD                               = DILEMMA UNSTATED; signatures already judged neighbor-paid; baseline gap (F3)
One / Position / Orientation (H1, H2, AJ §14)                  = One/Position half already K; H2 + merger criterion circular (F4)
Expectation (H3)                                                = CONFLICTS WITH E20 B/C ASYMMETRY + Spine §6.3 unless typed (F5)
Friction retyping                                               = NARROWER THAN Def-Ψ-1 / A-9; touches frozen HP-B (F6)
Mature neighbors                                                = ALREADY IN REPO BUT NOT ROUTED + 4 unpaid (F7)
Provenance schema (MT §5)                                       = REDEFINES A0-P; label collisions (F8)
Pass scope                                                      = QUALITATIVELY BOUNDED, QUANTITATIVELY OPEN (F9)
Routing surfaces                                                = STATUS block / ledger / routers missing (F10, mechanical)

REVERT NEEDED                                                   = NO
BLOCKER FOR MERGED STATE                                        = NO
BLOCKER FOR EXECUTING THE PASS AS WRITTEN                       = YES for F1, F3, F8 (fix MT first; small edits)
RECOMMENDATION = patch MT (v0.1 -> v0.2 pre-flight) with F1/F3/F8 corrections + D-1…D-4, then run the pass
```

## 2. 优点

- **没有写 canonical。** 三份文件都声明 `canonical: false`，Freeze-A owner 一处未动。流程上严格走了 edit protocol l.83 的 `dialogue -> source record -> bounded conflict / OPEN map -> only then Freeze-A`。MT §15 的 O1–O4 正对应其中的 “bounded conflict / OPEN map”。
- **改向本身合理。** #1066 的主要问题是概念膨胀（#1067 F1）。先做一次简化 pass，再用模拟去论证理论结构，这个顺序是对的。MT §17 的理由也成立：如果 Gate / field / Orientation 的解释在重构中被改写，现在跑模拟得到的结果会对不上靶。模拟设计被保留而不是删除，处理得当。
- **“非对象化 ≠ 零对象化”（AJ §9，MT §9）** 是这次最稳的一步。它把一个容易滑向不可研究的口号，变成了可以检查的纪律：声明切分、保留来源、保留重切权、保留重构路径。
- **双向结构（AJ §10，MT §6–7）** 并且明确写出 “reverse reconstruction alone can always invent a post-hoc L0 story”。这是这类方法最常见的失败方式，作者提前堵住了。
- **失败判据是自指的。** MT §18–19 写明 “the pass creates more ontology nouns than it removes” 即失败，也写明 “cannot distinguish a genuine L0-facing burden from a richer L2 model” 时停止。这是本仓库近期提案里最好的失败判据。
- **TR 保留了纠错轨迹。** “condensed Orientation” 被撤回（TR l.249–253），“为了”的目的论护栏被作者纠正（TR §5）。这使 A1 与 M 的边界可以追溯。
- **与既有裁决一致的部分：**
  - Gate 重类型（TR §29）与 #1066 D-2、#1055 D-1 一致；
  - Stable ISP 重类型（TR §27）与既有 `stable ISP != generatively healthy ISP` 一致；
  - Bearer 重类型（AJ §13）与 Spine §8、HP-B 的 “Bearer REQUIRED” 不冲突；
  - whole-field 仍是 “not an L0 substance”（router l.137），与 AJ §8 一致。

## 3. 发现

### F1（高）中心候选 “L0-facing continuity” 本身混合了 facing，而且很可能可以还原为现有 K

AJ §4 和 TR §10–12 的候选是：

```text
L0-facing continuity
= (1) generative inheritance: next Position genuinely generated from current formed Position
+ (2) renewed nonclosure: next Position not exhausted by formed L1/L2 structure
```

AJ §3 又说它的来源是原初选择（A0-Q「我感觉这种L0 Facing的连续性的来源就是原初选择」）。

用 MT 自己的三 facing 工作表检查这个候选：

- **(1) 是 L2 侧。** Spine §2.1（l.123–126）和 `SRT_AI_START.md` l.43/49 把 `generative inheritance` 与 retained historical efficacy、sedimentation 并列，明确写为 **≠ Selection occurrence**，并写明 “Where prior Selection remains materially effective later, that stronger burden belongs to retained historical efficacy / L2-side history”。K24 §4.2 进一步把跨 Selection 的继承写成 vertical generative reconstitution，也就是 One 的形成条件。
- **(2) 是 O0。** Spine l.138 定义 O0 = “Selection reality is not exhausted by completed determinate actuality and is not fully preclosed”。TR §12 的 “no actuality exhausts generativity” 与此一字之差。

由此得到一个两难：

```text
(a) 如果 L0-facing continuity 是某个 One 特有的，
    那么让它成为“这一个 One 的”连续性的，是 (1) 继承 / vertical reconstitution，
    这属于 L2 / One 侧；原初选择不是它的来源，否则违反 Spine §2.1。
(b) 如果它的来源是原初选择，
    那么它就是 (2)：每次 Selection 都成立的 O0 非预闭合。
    这对 terminal Selection 和非 One 的 Selection 同样成立，并不是连续性，也不特属于某个 One。
```

作者的直觉可以完整保留，只要把“来源”落在正确的分量上。AJ §6 其实已经写出了这个解法：

> primitive Selection = source of genuine generativity; Position / One = formed localization / historical conditioning of that generativity.

也就是说，原初选择是**被更新的生成性**的来源，历史 / One 是使这种更新**属于这个 One** 的载体。AJ §3 的标题句 “primitive Selection = ontological source of L0-facing generative continuity” 把两个分量合在一起，归到了原初选择名下。

**对 pass 的后果：** “L0-facing continuity” 是 H1–H8 之前最该先跑的目标。最可能的处置是 `MERGE_CANDIDATE / SOURCE_ABSORBED(K)`：

```text
O0 (Spine §2)  +  vertical reconstitution / One (Spine §5, K24 §4.2)  +  Selection-position_t (Spine §6.2)
```

如果这个还原成立，pass 一开始就删掉一个候选名词，正好是 MT §19 要的结果。若还原失败，剩下的残差才是真正的 OPEN。

**建议修正：**

- 把 AJ §3 / §17 的 “source of L0-facing continuity” 改写为 “source of the generativity renewed in L0-facing continuity”；
- 在 MT §13 前加 H0：“L0-facing continuity = O0 + vertical reconstitution + Selection-position?”

### F2（高）“Facing 分离”就是现有 canonical 的 aspect 规则，但没有引用；“L0” 在三种意义下使用

AJ §0 把 Facing 分离作为“controlling author correction”，TR §20 说它是“emerges”。但仓库早已写明：

- `_SRT_SYMBOL_TABLE.md` l.27：“`L_0 / L_1 / L_2` are analytic / model-facing aspects of the one Selection ontology, not three ontic substances or a compulsory three-stage product pipeline.”
- `Core_Law/SRT_L0_Metaphysics.md` l.283：“L0 / L1 / L2 = analysis / model-facing distinctions of one Selection reality”。
- K24 l.295 已经在用 “later Selection-totality with a changed **L0-facing burden landscape**”。
- `_SRT_CONTEXT_ROUTER.md` l.163 记录了 2026-09-25 的作者方向 “L0/L1/L2 are analytic views”。

AJ、TR、MT 的 dependency 都没有列这四处。

这不削弱作者的诊断，反而使它更精确：**以前打转，不是因为理论缺少 facing 概念，而是研究文件（09-25 Gate geometry、09-26 cognition）没有执行 canonical 已有的 aspect 规则。** 这是执行上的缺口，便宜的修法是一张检查表（MT §4 工作表即可），挂到 router 的 hardening gate 上：新构造被 harden 之前必须先填三 facing 表。它不需要一个新的 “Facing discipline” 名词。

更实质的问题是，三份文件里的 “L0” 有**三种**用法：

| 用法 | 位置 | 内容 | 与 canonical 的关系 |
| --- | --- | --- | --- |
| L0 aspect | MT §3、AJ §0 “analytic-view usage” | 任一 Selection 的开放 / 非预闭合面 | = Symbol Table l.31 |
| bare L0 | TR §2 l.146–149、TR §30 l.1121–1126 | non-flat generativity **+ genuine (actualising) Selection + finite positionality** | **越界**：finite-position-indexed actualisation 是 S0 面，canonical 放在 L₁（Spine l.142–145；Symbol Table L₁ 行）。“bare L0” 实际指的是原初选择整体（O0 + S0），不是 L0 aspect |
| 某个 formed Position 的 L0-facing | AJ §8 “the unexhausted generative face of a **current formed Position**” | 相对于已形成的 One / Position | 比 L0 aspect 窄：pre-One 与 terminal Selection 没有这种 L0-facing |

TR §2 的 bare L0 被标为 “Machine compression accepted by the author”，所以是 A1 覆盖了 K。这正是 MT §5 自己禁止的情况（“Do not let an A1/M compression silently replace K”）。

另外，K24 l.119 的 L0 机器表述（“relational organization of difference, **constraint, localization** …”，标注为 “for later canonical review”）比 #1068 的“薄 L0”厚，而 constraint 在 Symbol Table 中是 L₂ 的内容。两者需要在 pass 中对齐。

**建议：**

- router 登记 `L0/L1/L2-facing` = canonical L0/L1/L2 aspect 的别名，不作为新术语；
- AJ §8 的相对意义另写，例如 “Position-relative L0-facing”；
- TR §2/§30 的 “bare L0” 改为 “primitive Selection (O0 + S0)”。

### F3（高，方法）前向检验的两难没有写明；“生成不完备性”的信号已被判为邻居已付；基线缺结构学习

**两难。** AJ §10 与 MT §7 要求 “candidate L0-facing account → predict discriminable L1 formation / recut”。但 L0-facing 的定义就是“不被任何已形成的确定结构穷尽”，于是：

```text
一个 L0 候选若能预测“具体哪一个新切分”，它本身就是一个已形成模型（L2）；
一个 L0 候选若不能预测任何具体内容，前向检验就无法证伪它。
```

唯一可行的是**二阶预测**：不预测“切出什么”，而预测“在哪里、何时、以什么频率、在什么负荷 / 摩擦条件下发生重切”，以及重切之后的沉积形态。MT 需要把这一点写成允许的预测类型。否则 MT §18 的停止条件 “cannot distinguish a genuine L0-facing burden from a richer L2 model” 对每个目标都会触发，pass 会以全部 OPEN 结束。

**信号已付。** AJ §11 和 MT §8 把 “new distinction emerges / old equivalence breaks / dimension changes / similarity recuts / transition-space changes” 列为经验立足点。但同一天早上 #1066 的 reclassification 已经判定：

- l.26：“mature structure learning, representation learning, conceptual reorganization and manifold learning already pay functional field-reconstitution roles”；
- l.534：“PRE-OBJECT FIELD RECONSTITUTION = author-confirmed meaning but **NOT scientific distinctiveness**”。

#1068 没有引用这一结论。

**基线缺口。** MT §7 的基线清单（richer latent-state、non-Markov、hierarchical SSM、object-file / relational、dynamical manifold、predictive / generative）缺少**假设空间会增长**的结构学习模型，而它们原生地产生上面每一种信号：

- Dirichlet-process / CRP 混合与 latent-cause inference（Gershman, Blei & Niv 2010）：新类别的产生概率由预测误差和集中度参数决定；
- 形式发现（Kemp & Tenenbaum 2008）；
- 无限 HMM / 非参数状态空间。

这一类同时也是二阶预测最强的对手，因为它们也预测“何时新建类别”。**建议**把它们加入 MT §7，并在 MT §8 的信号清单前写明 l.534 的已付结论。

### F4（中）H1 的 One/Position 一半已经是 K；H2 和 AJ §14 的合并判据是循环的

**H1。** AJ §5 的 “One = diachronic reading, Position = current operative from-where reading” 与现有 K 几乎相同：

- Spine §6.2 l.297：“For an already formed One, `Selection-position_t` is the time-local operative `from-where` …”；
- router l.90：“time-local operative aspect of an already formed One”。

TR §6 自己也注明 “This aligns with the current canonical owner”。所以 H1 真正新的只有 Orientation 的位置（见 F5）。AJ §17 把它记为 “AUTHOR ACCEPTED FOR RECONSTRUCTION”，应补注“One/Position 部分 = K 重述”。

**H2 循环。** H2 / AJ §5 的判据是 “history participates in forming the later operative **from-where**”。但 from-where（= Selection-position）按 Spine §6.2 只对 **already formed One** 定义；Spine §6.1 又明确 finite positionality ≠ formed locality。所以：

```text
用 “参与形成后来的 from-where” 来判定 One 是否形成
= 用预设已形成 One 的概念来定义 One 的形成
```

有两条出路：

- 按 canonical §5 的写法表述：“renewed organization can again carry the relevant conditioning role”（l.250–256，K24 §4.2）；
- 或者先给出一个 pre-One 的 proto-from-where，但 canonical 目前没有这个概念，引入它需要作者裁决。

此外，H2 与 K24 §4.2 的 vertical generative reconstitution 基本同义。K24 l.433 已写明 “generative re-entry may be strong operational evidence but is not by itself a sufficient canonical One criterion”，H2 需要说明自己比它多了什么。

**AJ §14 同样循环。** “Two previously separable generative from-wheres form a stronger higher-order One only when they participate in the formation of a **new operative from-where**”。在没有独立个体化 from-where 的判据时，这只是把 Spine l.274 的 OPEN（“branch / merge attribution remain OPEN”）从 “same One?” 挪到了 “one from-where?”，并没有推进。可对照的成熟邻居见 F7：evolutionary transitions in individuality。

### F5（中）H3 与 E20 的 B/C 不对称以及 Spine §6.3 冲突，除非明确类型

H3（MT §13，TR §28）提出：“older basal ‘structural expectation’ partly collapses into Position / Orientation”。但：

- E20 l.55–72：**B**（structural generative expectation）属于“an actually formed generative relation”，并且 “**B does not require C** in order to exist”；**C** 才 “presupposes enough formed organization to make anticipation operative **from somewhere**”。
- Position / Orientation 按 Spine §6.2 只存在于已形成的 One。

所以把 B 收进 Position / Orientation，要么丢掉 B 在没有 formed locus 的关系上的适用范围，要么要把 Position 扩展到 pre-locus。按 E20 的结构，Position / Orientation 更接近 **C** 一侧，而不是 B。

Spine §6.3 l.314 也给出护栏：“Selection affecting later selectability != formed-position anticipation automatically”。如果 “Orientation = future-facing expression of Position” 随 Position 自动存在，它必须落在“影响后来可选性”这一层，不能等于 formed-position anticipation。否则 §6.3 的门控就被绕过了。

**建议：** H3 改写为“B / C 中哪一部分被 Position / Orientation 吸收？”，并要求 Orientation 在 Spine §6.3 的两层之间明确定位。另外，AJ §5 与 TR §22 中的裸写 “Orientation” 应一律写 “formed Orientation”。Spine l.158 已把 `Oriented Openness` 作为 O0 的 routing label，裸写容易与之混淆。

### F6（中）摩擦重类型比 Def-Ψ-1 / A-9 窄，并且触及冻结的 HP-B

AJ §13 与 TR §19 写：“Friction → diagnostic strain where formed L1/L2 organization and continued generation **mismatch**”。MT H7 写：“diagnostic of mismatch … rather than a source of generation”。

- 后半句（“不是生成源”）与 `_SRT_PSI_F_CANONICAL.md` §3.2（generative-friction 属 P2/P3-B08）一致，没有问题。
- 前半句把摩擦限定为**失配时**的应变。Def-Ψ-1（l.66–80）定义的是 “选择发生时不可消除的结构性阻抗”：只要把开放可能性压成可维持的 L1 切片就存在，不以失配为条件。
- router l.118 的 A-9 规定理论性摩擦 = canonical Ψ_f 概念族，“do not create a second friction variable”。“失配应变”作为 Ψ_f 的一种读数或代理（Def-Ψ-Obs-1、Ψ_f_felt）是合法的，作为 Friction 的重类型则构成第二个摩擦变量。
- HP-B B-4 已冻结 “constitutive Ψ_f REQUIRED; high / acute friction not required”。“只在失配时”的读法与“构成性”相冲突。

更一般地，MT §10 的第 12 项（Bearer）、第 14 项（friction）、第 19 项（consciousness / foregrounding）都落在冻结的 HP-B 词汇上。但 MT 通篇没有提到 HP-B 冻结（grep 为零）。

**建议：** 在 MT §18 加一条：这些项在本 pass 中对 HP-B 只读；任何改变 HP-B kernel 条件的处置，都必须按冻结记录 §5 点名 reopen trigger。

### F7（中）成熟邻居：仓库里已有却没接上的 3 个，尚未支付的 4 个

MT §11 要求 “already-retrieved first”。仓库里恰好已有针对 #1068 两个中心主张的判决，但三份文件都没有引用：

| 主张 | 已有判决 | 位置 |
| --- | --- | --- |
| L0-facing continuity（每个新现实被先前现实条件化但不被穷尽，生成持续前进） | Whitehead creativity + concrescence + transition；“Do not claim novelty for: … each new actuality contributes to future becoming” | Cycle-3 Pass 1 §3.2 l.217– |
| 非对象化方法（切分是被施行的，客观性 = 对切分负责） | Barad agential cut；“PO-1 weak constitutive-observation claim: STRONGLY NEIGHBOR-PAID” | Pass 13 §10 l.389 |
| 被形成者携带未穷尽的前个体潜能 | Simondon；“novelty burden is on the typed dependency ladder, not on pre-individuality itself” | novelty audit l.202 |

尚未支付、与 #1068 直接相关的邻居：

- **Husserl：sedimentation / reactivation**（《几何学的起源》）。沉积的意义可以沿原初构成被“重新激活”，这几乎就是 AJ §12 的 reconstructibility = “retained reopening path”，也是 L2 → L1 → L0 反推路线的现象学原型。仓库里只在 `Philosophy/SRT_Philosophy_Tradition_Comparison_PH_SS.md` 出现过。
- **功能的组织论解释**（Mossio, Saborido & Moreno 2009；Montévil & Mossio 2015），以及 **Kant《判断力批判》§64–65 的 Naturzweck**。它们给出了非外在目的论的“为了”：一个约束的“功能”就是它对维持自身所在组织的贡献。这正是 AJ §1 对作者“为了”的读法（constitutive generative role, not external final cause），而且是成熟的现成解释。
- **Evolutionary transitions in individuality**（Michod 2007；Queller & Strassmann 2009；Godfrey-Smith 2009）。它研究两个单元何时合成一个更高层个体（合作 + 冲突抑制 + 新的选择层级），是 AJ §14 合并判据最直接的对手。
- **Parfit：Relation R 与 fission**。它讨论的正是 TR §26 的“L2 历史连续性、L1 同一性、生成性来源可以分离”。Parfit 在仓库里已有，但没有接到这里。

**建议：** pass B 从上表 3 条既有判决和这 4 个邻居开始，而不是从 MT §11 的 30 个概念开始。

### F8（中，治理）MT §5 重新定义了 A0-P，标签有冲突，英文粗体引文没有 provenance

- **A0-P 被改义。** 现有 schema（STATUS l.358–359；Phase-3 provenance map l.58）规定 A0-P = “faithful paraphrase of an **author-originated** move”，并写明 “record-level directional acceptance does not by itself upgrade machine wording into author authority”（l.88）。MT §5 改为 “A0-P = direct author choice / **accepted direction**”。按新定义，作者接受的机器方向会被标成 A0-P，也就是作者权威，与 A1 混同。MT 是本次 pass 给所有目标陈述做类型标注的 owner，这一处必须在执行前改回。
- **标签冲突：**
  - MT §5 用 `E` 表示 external，而 Spine §8 的 `E` 是 same-One prospective exposure；pass 第 12 项 Bearer 同时要用后者。
  - MT §15 的输出 `O1–O4` 与 canonical `O0`（同文 §10 第 2 项）并列，读起来像 O0 的后继；HP-B 冻结记录还有 `O-1…O-3`。
  - MT §13 的 `H1–H8` 与 #1066 当天的 `H1/H2/H3`（认知层级，仍保留在 PG）并存。
  - MT §4 的 `F0/F1/F2` 与 HP-B minimal hook 的 F1–F7 失败条件冲突。
- **英文粗体引文。** AJ §5、§6、§8、§9、§12 的英文粗体块引用与 A0-Q（「」中文引文）排版相同，但它们是机器表述。TR 开头说明了边界，AJ 本身没有。建议逐条标 A1 / M。

### F9（中低，范围与过程）

- **数量上没有边界。** MT 在质的方面有边界（不开深井、不写 canonical），但 pass A 有 20 个目标、pass B 约 30 个，每个 8 个字段。建议：
  - pass A 只跑 H0–H8 真正落到的约 8 个目标；
  - pass B 按 F7 的 7 个邻居封顶；
  - 写出完成判据，例如 O1–O4 各一份，并给出篇幅或时间上限。
- **名词账的基线。** MT §19 的“名词净减少”判据应把 #1068 自己新增的构造计入基线：
  - L0/L1/L2-facing continuity；
  - generative inheritance（新义）/ renewed nonclosure；
  - bare L0 与 cognitive L0-facing；
  - formed Orientation（作为 reading）；
  - structured generative incompleteness；
  - anonymous actualisation / historically positioned generation；
  - recut rights。
- **CURRENT NEXT 更替。** 这是当天第三次改写 CURRENT NEXT。#1066 D-3 在 17:57 设定模拟为 CURRENT NEXT，2 小时 40 分钟后被取代，模拟没有执行。这次改向本身有充分理由（见 §2），只记录这一模式。
- **合并过程。** PR 从创建到作者自合并 14 分钟，没有独立评审。按 edit protocol，独立复审要求针对 canonical semantic edit，本 PR 不涉及，所以不违规。

### F10（机械）路由面

- **STATUS。** 两处 CURRENT NEXT 一致（✓）。但：
  - l.111 的新 CURRENT NEXT 位于 §0.3c “Pre-object generative orientation / cognition research” 块内，该块链接的仍是认知程序的 source / owner，没有 Facing 路线自己的 §0.3d 块；
  - ledger 中没有 `#1066 = MERGED / role` 与 `#1068 = MERGED / role` 两行。
- **`_SRT_CONTEXT_ROUTER.md` 与 `_SRT_AGENT_RETRIEVAL_PROFILE.md`** 没有登记新的 CURRENT NEXT owner（MT）和 source（AJ）。
- **`Glossary/SRT_Live_Term_Router.md`。** “Facing” 出现在 3 个文件标题和 frontmatter tag 中，符合 l.31–38 的 hardening 条件，但没有登记。建议登记为 canonical aspect 的别名（F2），另把 “L0-facing continuity”“formed Orientation” 登记为 working label。
- **reconstructibility 需要标明意义。** MT §9 的“每个模型可重构”是研究模型层面的可恢复性，而 router l.113 把 `generative reconstructibility` 限定为 “theory-side ability … **not repository / data / dialogue recoverability**”。AJ §12 的系统能力义与 MT §9 的方法义应分开写。

## 4. 需要作者决定的事项

```text
D-1  L0-facing continuity：
     (a) 接受 F1 的分解，让 pass 以 H0 “= O0 + vertical reconstitution + Selection-position?” 开头 [推荐]；
     (b) 保留为独立候选构造，但须写明它比这三项多出的内容。

D-2  “Facing” 的地位：
     (a) 登记为 canonical L0/L1/L2 aspect 的别名；AJ §8 的相对义另名（如 Position-relative L0-facing）；
         把三 facing 工作表挂到 router hardening gate，作为执行规则 [推荐]；
     (b) 作为新术语登记（需说明与 Symbol Table l.27 的区别）。

D-3  前向检验允许的预测类型：
     (a) 只允许二阶预测（重切的位置、时机、频率、负荷依赖、沉积形态），
         并以非参数结构学习 / latent-cause 模型为必备基线 [推荐]；
     (b) 允许一阶内容预测（则须说明为什么该候选不是 L2 模型）。

D-4  pass 的边界：
     (a) pass A ≤ 8 个目标（H0–H8 所及），pass B ≤ 7 个邻居（F7）；
         Bearer / friction / consciousness 三项对 HP-B 只读 [推荐]；
     (b) 按 MT §10–11 全量执行，另定停止时间。
```

## 5. 执行 pass 前的小修清单（不涉及理论）

```text
MT §5      A0-P 恢复为 “faithful paraphrase of an author-originated move”；E 改名（如 X / EXT）
MT §15     O1–O4 改名（如 OUT-1…4）；§13 H1–H8 改名或加前缀（如 FH-1…8），避免与 #1066 H1–H3 冲突
MT §7      加入非参数 / 结构学习基线（F3）；§8 前写明 #1066 reclassification l.534 已付结论
MT §18     加 HP-B 只读条款（F6）
MT §13     加 H0（F1）；H2 按 Spine §5 / K24 §4.2 措辞重写或标注循环（F4）；H3 按 E20 B/C 与 Spine §6.3 重写（F5）
AJ §3/§17  “source of L0-facing continuity” -> “source of the generativity renewed in …”（F1）
AJ §5/§6/§8/§9/§12  英文粗体块标 A1 / M（F8）
TR §2/§30  “bare L0” -> “primitive Selection (O0 + S0)”（F2）
STATUS     §0.3d Facing 路线块 + #1066 / #1068 ledger 行（F10）
routers    context router / retrieval profile 登记 MT、AJ；Live Term Router 登记 facing 别名与 working labels（F10）
```

以上均为作者可选的修正；本评审不代为执行。
