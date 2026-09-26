---
id: SRT-PR1066-PREOBJECT-FIELD-GATE-TYPED-INDEPENDENT-CONTENT-REVIEW-20260926
type: audit
status: active
date: 2026-09-26
layer: governance
epistemic_layer: operations
claim_mode: independent_review
canonical: false
research_mode: U
dependency:
  - Operations/Proposals/SRT_PREOBJECT_GENERATIVE_ORIENTATION_COGNITION_RESEARCH_PROGRAM_2026-09-26.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_L0_FACING_ATTRACTOR_FIELD_FORMATION_CORRECTION_2026-09-26.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CONSCIOUSNESS_MULTILEVEL_GATING_ACTION_FIELD_2026-09-26.md
  - 01_Source_Intuition/SRT_AUTHOR_INTUITION_GATE_BRIDGE_PROPERTY_OBJECT_FORMATION_2026-09-26.md
  - Operations/Audits/SRT_GATE_TYPED_OPERATOR_MINIMAL_FORMALIZATION_2026-09-26.md
  - Operations/Proposals/SRT_GATE_TYPED_TOY_SIMULATION_DESIGN_2026-09-26.md
tags: [IndependentReview, PR1066, PreObjectCognition, L0Facing, WholeField, Gate, TypedFormalization, ToySimulation, ConceptInflation]
---

# PR #1066 独立内容评审 — pre-object 认知 / L0-facing 整体场 / 类型化 Gate / 玩具模拟

> **角色**：对**未合并**的 draft PR #1066 的 pre-merge 独立内容评审。只读：本记录不修改 #1066 的任何文件、STATUS、路由面或 canonical owner，也不替作者关闭任何 OPEN。
>
> **评审者独立性**：独立 session，没有参与 #1066 的对话或写作。本 session 此前评审过 HP-B 包（#1059、#1063），其中提出的邻居债务（Plessner、O'Regan & Noë、Piaget）在 F4 中被再次引用，特此披露。
>
> **评审局限**：原始对话不在仓库中，A0-Q 逐字性无法核验。PR 共 19 个文件、约 1.07 万行。本评审**完整阅读**了 3 份作者原始文件、类型化形式化、玩具模拟设计和研究程序 §14–§16，其余 13 份机器审计按“结论节 + 关键词核对”的方式抽读，并在各发现中注明。

## 0. 评审对象

```text
PR:    #1066 (OPEN, draft) “Research: refocus cognition on L0-facing whole-field formation”
head:  9c4af318c06a90e963b30aadb702eab73100b3d1   base: 68920877 (= current main)
time:  2026-09-26 13:06 → 17:11 (+0800), 41 commits, 19 files, +10703 / −43

author sources (3):
  A1 = 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_L0_FACING_ATTRACTOR_FIELD_FORMATION_CORRECTION_2026-09-26.md (347)
  A2 = 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CONSCIOUSNESS_MULTILEVEL_GATING_ACTION_FIELD_2026-09-26.md (415)
  A3 = 01_Source_Intuition/SRT_AUTHOR_INTUITION_GATE_BRIDGE_PROPERTY_OBJECT_FORMATION_2026-09-26.md (525)
machine audits (13), proposals (3; programme PG modified), incl.:
  TF = Operations/Audits/SRT_GATE_TYPED_OPERATOR_MINIMAL_FORMALIZATION_2026-09-26.md (653)
  TS = Operations/Proposals/SRT_GATE_TYPED_TOY_SIMULATION_DESIGN_2026-09-26.md (515)
  DD = Operations/Audits/SRT_ACTIVE_GATE_BRIDGE_FORMATION_DRIVE_DECOMPOSITION_2026-09-26.md (525)
  XB = Operations/Audits/SRT_GATE_BRIDGE_PROPERTY_OBJECT_FORMATION_CROSSWALK_2026-09-26.md (534)
  PG = Operations/Proposals/SRT_PREOBJECT_GENERATIVE_ORIENTATION_COGNITION_RESEARCH_PROGRAM_2026-09-26.md (1118)
  MG = Operations/Audits/SRT_CONSCIOUSNESS_MULTILEVEL_GATING_ACTION_FIELD_CROSSWALK_2026-09-26.md (600)
  AC = Operations/Audits/SRT_CONSCIOUS_TARGET_TO_MULTILEVEL_CONTROL_CONSTRAINT_BRIDGE_2026-09-26.md (715)
  WF = Operations/Audits/SRT_WHOLE_FIELD_COMPOSITION_FROM_TRANSPARENT_CLOSURES_2026-09-26.md (513)
```

控制 owner / source（在 68920877 上读取）：`STATUS.md`（l.58 HP-B FROZEN；l.111 与 l.896 两条 CURRENT NEXT）；`SRT_AI_START.md §1.1`（Selection 护栏 l.37–43）；`_SRT_SYMBOL_TABLE.md` l.34（Ĝ：“Never use plain `G` for this.”）；`Glossary/SRT_Live_Term_Router.md`（new-term gate l.35；`gating (organization-level)` l.130；`gate geometry` l.131）；#1055 二次裁决 D-1（gating = 实现 Ĝ 型 Selection 角色的已形成组织）；`01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GATE_GEOMETRY_PR1058_REVIEW_SECOND_ADJUDICATION_2026-09-25.md` A-3.3（foreground 三分：manifest_OF / foreground_obj / foreground_phen）；HP-B 冻结记录 `Operations/Audits/SRT_PR1063_B1_B5_CORRECTIVE_FINAL_CONSISTENCY_REVIEW_2026-09-26.md` §5；`01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GENERATIVE_EXPECTATION_TYPING_2026-09-20.md`（C0 / C1）。

## 1. Verdict

```text
MECHANICAL / FRONTMATTER + CI (governance-preflight on 9c4af318)   = PASS
CANONICAL IMPACT (file edits)                                       = NONE
MATURE-NEIGHBOR PAYMENT (control / GNW / PFC-BG / EVC / metastability /
  SI / autonomy / closure / active inference / object files)        = STRONG
RE-ENTRY OF PRIOR WORK (Cycle-2 Pass 4/5, Simondon, NEURAL34, PH-AG02) = GOOD
ANTI-UNIFICATION (Gate as predicate over typed Form/Close/Compose)  = GOOD
ZERO-GAIN RULES (TS Z1–Z6; PG S1–S6)                                 = GOOD

CONCEPT-SET STABILITY / PACE                                        = FAIL (F1)
RELATION TO FROZEN HP-B VOCABULARY                                  = REVISE (F2)
NEW-TERM GATE (Glossary) FOR GATE FAMILY / FIELD / CLOSURE          = FAIL (F3)
BRIDGE → PROPERTY → OBJECT NEIGHBOR LINEAGE                         = PARTIAL (F4)
SIMULATION BASELINE STRENGTH                                        = REVISE (F5)
SELECTION / EXPECTATION TYPING                                      = REVISE (F6, F7)
SINGLE-NEXT (STATUS vs owner; multiple nexts in PG §14)            = FAIL (F8)
NOTATION (“G” used four ways + Ĝ rule)                              = REVISE (F9)

MERGE #1066 AS-IS                                                   = NO
OVERALL                                                             = VALUABLE RESEARCH TRAIL; FREEZE THE CONCEPT SET,
                                                                      REGISTER A MINIMAL TERM SET, FIX NEXT, THEN RUN TS
AUTHOR DECISIONS NEEDED                                             = YES (D-1 … D-4, §4)
```

一句话：#1066 的研究质量在很多方面高于前几轮：
- 成熟邻居支付强；
- 主动回收了 09-09/09-10 的 Cycle-2 与 NEURAL34 结果；
- 把 H1/H2/H3 从竞争对手改为层级；
- 把 Gate 从“一个方程”降为“对三个类型化变换的谓词”；
- 以带强基线与零增益规则的玩具模拟收尾。

问题主要不在单个论证，而在于：HP-B 包刚因“停止加概念”而冻结，不到一小时 `main` 就重设了 CURRENT NEXT，随后四小时内本 PR 又引入了约二十组新的命名构造与标签，而且大多没有经过术语登记，也没有与冻结词汇对齐。

## 2. 通过项（保留）

- **作者更正被忠实表达**（PR 描述复核点 1）：A1 §0 保留原话「重点不是先后，而是整体吸引子场如何形成」，§1 明确 `L0-facing != earliest time slice != hidden warehouse != independent substance != completed possibility inventory`；“attractor”被降为可能的动力学性质（PG；PR 描述 “Current best machine synthesis”）。
- **不创造 L0 实体**（复核点 5，大体通过）：A1 §5 与 WF 把整体场写成“各部分共同维持的差异化未来可达性组织，不是额外对象”；后来的关系式定义 “field = current organization of mutual Gate-possibility” 进一步去实体化。例外见 F6。
- **邻居支付**：XB、MG 与 AC 三份审计，分别以分层运动控制、affordance competition、基底节门控、分层主动推断、GNW、Miller-Cohen PFC、O'Reilly-Frank PFC-BG、EVC、快速指令学习等为对手，并明确“不从任何单一成分主张新颖性”。
- **反过载**：access / control / ownership 的拆分避免把 Bearer / Concern 塞进最小控制机制，与冻结的 B-2（Bearer 只对 “experience proper” 必需）相容。
- **反统一检验**：XB §10 给出成败条件；TF §6 结论为“共同 Gate 核先是一个谓词而非一个方程”，并逐项排除泛相关、任意约束、静态标签、不可逆锁定（TF §7）。
- **预注册方向正确**：TS 设了强世界模型 B1 与 object-file / slot 基线 B2、active vs yoked 对照、禁止学习器侧对象 ID，Z1–Z6 零增益规则（TS §15），执行前冻结清单（TS §19）。
- **诚实的证据边界**：局部关系几何变化 = 合理的 P3 bridge；Bearer / One 索引的整体认知场重建 = NOT ESTABLISHED；NEURAL34 深井 Case B 已关闭，数据访问 NO-GO。

## 3. Findings（按严重度排序）

### F1 — 高：概念集不稳定，速度与规模重演了刚被冻结的模式

**证据。**
- HP-B 包于 2026-09-26 12:02 冻结，冻结理由正是停止继续加概念（`..._FINAL_CONSISTENCY_REVIEW` §5；STATUS l.58）。
- 12:32 与 12:48 `main` 两次重设 CURRENT NEXT（preformal coherence → pre-object generative orientation）。
- #1066 在 13:06–17:11 之间，CURRENT NEXT 在 PG 中依次变为：
  1. CN-1 / CN-2；
  2. 整体场形成；
  3. H1–H3 + G2–G4；
  4. MG-1 / MG-2；
  5. GK-1；
  6. Gate genesis；
  7. property genesis；
  8. typed formalization；
  9. simulation freeze。
- 新增的命名构造 / 标签（不完全列举）：
  - H1–H3；G1–G4 证据梯；W1–W4；
  - MG-1 / MG-2；C / C1 / C2；target vs gate objectification；
  - access / maintenance / admission / structuring bias / execution / writeback 六角色；
  - G-pass / G-bind / G-coarse；K1–K4；AF-1–AF-3；
  - I-thin / rich object closure；Gate transparency；
  - Form（F-K1–K5）/ Close（C-K1–K6）/ Compose（M-K1–K5）；G-K1–K6；U1–U5；
  - `A_t(q)`；B0 / B1 / B2 / G 臂；S1–S4；T1–T4；Z1–Z6；
  - “Selection-facing actualisation”；“field = current organization of mutual Gate-possibility”。
- 作者接受事件有：「认同继续」（A1 §0.1）；「认同C，继续」（A2 §0，**显式选项接受**）；「认同，继续」×3（A2 §12；A3 §17、§18）。除 C 以外，都只构成 package-level directional acceptance（`CONTINUE_DIRECTIONAL_ACCEPTANCE`）。

**风险。** 与 HP-B 相同：机制表述在一天内多次重写。后续 session 很难知道哪一层是控制性的。多数构造以 M 强度进入研究程序的 CURRENT NEXT 体系。

**修复。** [D-1] 作者裁决：是否对 cognition / Gate 包采取与 HP-B 相同的冻结，即“概念集冻结，只允许执行 TS”。评审推荐**冻结**：
- 以 TF 的 Form / Close / Compose + G-K1–K6 + TS 作为唯一保留的新概念层；
- 其余标签（MG、C1/C2、W1–W4、AF 等）标为 provenance / working label；
- 在 TS 返回结果之前不再新增构造。

### F2 — 中高：意识线在 HP-B 冻结后重新进入，没有声明与冻结的关系，也没有使用冻结的 foreground 分型

**证据。**
- A2 的核心 C：“conscious intention itself is a foregrounded high-level gate / objectification”（§0–§1）。A2 §6 与 09-25 gate-objectification 路线相连，而后者属于已冻结的 HP-B 谱系（S25 A-12：ontological / generative foregrounding vs cognitive / interventional foregrounding）。
- 在 A2 与其交叉比对中检索 “HP-B / frozen” 为 0 处。只有 object givenness 审计 §12 有一句“是否现象性，需另行的 HP-B / qualia bridge”。
- “foreground” 在 A2 中出现 16 次、MG 交叉比对 13 次、PG 8 次，全部没有使用作者已采纳的 A-3.3 三分（manifest_OF / foreground_obj / foreground_phen）。
- 新增的 target objectification（“我要 X”成为前景的粗目标）不属于 A-12 的任一级别，实际上是冻结的两级分型之外的第三型，但没有与 A-12 对照。
- AC 的 ACCESS（“target is consciously / globally available”）与冻结的 HP-B 最小核中 `broadcast / wider access != generative mediation` 同名不同义，没有交叉说明。

**判断。** 内容本身属于控制 / 能动（HP-A、PH-AG 线），不属于 HP-B 现象性，所以**可以**不受冻结约束，但必须声明这一点。

**修复（机械，并入 D-1 确认）。**
- A2 / MG / AC / PG 加一段：“本线处理意识内容的控制作用（HP-A / PH-AG），不处理 phenomenal admission；HP-B 冻结不受影响。”
- 所有 “foreground” 按 A-3.3 标型（本线主要是 foreground_obj 或 cognitive / interventional），并注明与 HP-B 核中 access 用法的区别。
- target objectification 注明是 A-12.2 的扩展子型还是 A-12 之外的控制概念。

### F3 — 中高：Gate 家族、整体场、闭合等新构造没有经过 new-term gate；Gate 的外延被悄悄扩大

**证据。**
- 术语登记（Live Term Router）的门槛 l.35：术语出现在文件标题、作为可复用命名构造的节标题或命名机制 / 算子字段中，即须登记。#1066 的文件标题含 ACTIVE_GATE_BRIDGE、GATE_TYPED_OPERATOR、GATE_TRANSPARENCY、WHOLE_FIELD_COMPOSITION、OBJECT_CLOSURE 等，但 PR 没有改动 Glossary。
- 现行登记：l.130 `gating (organization-level)` = 实现 / 承载 Ĝ 型 Selection 角色的**已形成组织**（#1055 D-1）；l.131 `gate geometry` = 已形成 gating 的等价 / 边界 / 邻域 / 迁移-可达解释。
- 新用法：A3 §12–§13、XB §16、TF §3 让 “Gate” 同时覆盖**形成过程**（Form：主动形成 / 修订桥）、闭合（Close）、组合（Compose）和使用（pass / suppress）。“Gate genesis” 已不是 D-1 意义上的“已形成组织”。
- A3 的作者原话「这种桥梁连接是一种主动形成的」支持“形成是主动的”，但并未裁决“Gate 一词应包含形成过程本身”。

**修复。** [D-2] 作者裁决 “Gate” 的外延：
- (a) 保持 D-1，Gate = 已形成组织，形成过程另名（如 “bridge formation”）（评审推荐）；
- (b) 扩大 Gate，包含 Form / Close / Compose，并修订 l.130。

机械部分：Live Term Router 登记最小集合，逐项标 PARTIAL_OVERLAP / WORKING_LABEL，例如 bridge formation、thin index / rich closure、Gate transparency、whole field（关系式定义）、Form / Close / Compose。

### F4 — 中：桥 → 属性 → 对象这条线最直接的历史邻居缺席，其中两项是已接受的邻居债务

**证据。**
- 在 19 个文件中检索，von Foerster、eigen（eigenbehavior / eigenform）、Piaget、Poincaré、Cassirer、O'Regan、Plessner 均为 0 处；“affordance” 出现在 17 个文件，但没有提到 Gibson。
- XB §4–§6 的三个形式家族（变换下的不变量、等价 / 商、对象作为稳定变换轨道 / 关系闭合）恰是以下经典路线：
  - Poincaré 的“补偿运动群”与 Cassirer（1944）“The concept of group and the theory of perception”；
  - Piaget 的对象建构（对象 = 位移群下的不变量；感觉运动图式的同化 / 顺应）；
  - von Foerster（1976）“Objects: tokens for (eigen-)behaviors”：对象作为递归感觉运动闭合的稳定本征行为，几乎就是 “rich object closure = reciprocal stabilization”。
- 主动桥形成与 graspability：O'Regan & Noë（2001）的感觉运动相依性。PG 与 XB §14 只泛称 “sensorimotor-contingency work”。
- Plessner、O'Regan & Noë、Piaget 已列入 B-1…B-5 修正清单第 9 项的邻居债务。#1066 正处在这些债务所对应的领域，却没有支付。

**修复（机械）。** XB §14 / A3 §9 补上上述谱系，并说明 SRT 版本相对 von Foerster eigen-object 与 Piaget 对象建构的**增量**；若没有增量，就标为 reorganization。

### F5 — 中：玩具模拟的基线在 Close / Compose 两级上不够强，调参预算也未对齐

**证据。**
- TS §6 的 B1 是整体隐状态世界模型，§7 的 B2 是 slot + 动作转移。TS §14 T4 用 “independent closure policies” 作为 Compose 的对照。
- 缺少最自然的强基线：**以对象为中心的关系型世界模型**（slot + 图网络 / 交互网络转移，例如 Contrastive Structured World Models，Kipf et al. 2020；Interaction Networks，Battaglia et al. 2016）。它同时覆盖 Close（slot 与关系的双向支持）与 Compose（slot 间关系动力学），是 S2 / S4 最可能的吸收者。以独立闭合策略作为 Compose 的对照过弱。
- TS §19 冻结清单列了 “baseline capacities”，但没有列**调参 / 搜索预算对齐**与**计算预算对齐**。G 与环境由同一方设计（TS §1–§3），有环境按 G 的归纳偏置剪裁的风险。

**修复（机械）。** TS 增加 B3（对象中心关系型世界模型），T4 改以 B3 为对照；§19 增加“同等调参与计算预算”和“至少一个不由 G 设计者设计的环境族，或在实现 G 之前冻结环境生成器”。

### F6 — 中低：“原始 Selection” 被写成与已形成因子并列的乘项（复核点 5 的残余）

**证据。**
- A1 §4 与 PG §13 写作 `primitive generativity / Selection × retained vertical organization × formed Bearer × structural Expectation × body-world coupling × support / glue → whole L0-facing generative field`。
- 按 L0 与 Spine，现实**就是**非平、非预闭模式下的 Selection。原始 Selection 不是与历史、Bearer、期望并列的一个可分因子，而是这些因子本身得以发生的方式。把它写成乘项，容易读成“底物 + 调制它的 Selection”这一二元结构。#1055 评审 F2 已在另一处遇到同型问题。
- A1 §3 自己的分型说明（“It is not a cognitive object, explicit predictor, chooser, or already formed gate”）是对的，但公式没有跟上。

**修复（机械）。** 公式改写为 “all listed contributors are Selection-realized; primitive Selection is the mode, not a multiplicand”，或者把 Selection 行移出乘积，作为整个循环的前提注记。

### F7 — 中低：“structural Expectation / current goal” 被合并；Selection 的形成层措辞接近“从菜单中选”

**证据。**
- DD l.389 与 l.480 写作 `structural Expectation / current goal`。09-20 typing 中结构期望（C0 具身 / C1 模型介导，均不蕴含显式目标）与显式当前目标是两回事；同一 PR 的 AC 审计也把 “target” 单独列为可进入意识的内容。这是复核点 3 要防的“压平”。
- DD l.243：“Selection marks the actual commitment / realization of a provisional coupling **among non-equivalent possibilities**”。它否定了“Selection chooses which bridge”的循环用法，这一点正确；但替代措辞仍预设了一个可能性集合，并用了 “commitment / provisional … tried” 这类试选语义。`SRT_AI_START §1.1`（l.37–43）规定 Selection 不预设完成的备选集。在形成层（Ĝ 型实现）讨论主动试探可以接受，但须标明层级。

**修复（机械）。** DD 把 “structural Expectation” 与 “current goal / target” 分成两行；l.243 改为“形成层的 Selection-facing actualisation（Ĝ 型实现；不预设完成的备选集）”。

### F8 — 中：单一 next 被破坏；合并后 STATUS 与 owner 文件会互相矛盾

**证据。**
- `main` 的 STATUS 已有两条 CURRENT NEXT：l.111 `CN-1 root construct/neighbor map + CN-2 object-first vs orientation-first discriminator map`，l.896 `pre-object generative orientation … programme`（owner = PG）。这是 68920877 引入的，本 PR 之前就存在。
- 本 PR 明确“不改 STATUS”，但 PG §14 “Immediate CURRENT NEXT” 下并列了 CN-1、CN-2、GK-1a–f、MG-1、MG-2、CN-3（HOLD）、CN-4、CN-5；§16 又压缩为 “GK-1 … GK-1f freeze toy simulation”。
- 合并后，STATUS l.111 仍描述已被本 PR 否定的“对象先 vs 定向先”框架，owner 文件却说冻结模拟包。一条 next 过时，owner 文件内部又有多条并列 next。

**修复（机械，内容待 D-3）。** 合并前把 STATUS l.111 与 l.896 合为一条，指向 PG §16；PG §14 标明哪些子项已完成、已 HOLD 或作为 provenance，只留一个 active next。

### F9 — 低：“G” 在同一 PR 中有四种用法，并触及 Ĝ 规则

- XB §7：G1 = pass / suppress，G2 = bind，G3 = coarse-grain / objectify。
- G2–G4 设计：G1–G4 = 场证据梯（G2 = predictive shared geometry）。
- TF §6：G-K1–K6 = Gate 谓词。
- TS §8：G = 模拟臂。

“G2” 在同一 PR 里同时指 “bind” 和 “predictive shared geometry”。另外，Symbol Table l.34 对 Ĝ 规定 “Never use plain `G` for this”，而 gating 按 D-1 正是 Ĝ 型角色的实现，用 plain G 命名 Gate 家族会招致混淆。

**修复（机械）。** 证据梯改名（如 FG1–FG4），Gate 角色改名（GR-pass / GR-bind / GR-coarse），模拟臂改名（如 T-Gate）。

## 4. 需要作者裁决的事项

```text
D-1  cognition / Gate 包是否按 HP-B 先例冻结概念集，只执行 TS（F1；评审推荐：是）；
     并确认意识 / 目标对象化线属于 HP-A / PH-AG 控制线，不重开 HP-B（F2）
D-2  “Gate” 的外延（F3）：(a) 保持 D-1“已形成组织”，形成过程另名（评审推荐） | (b) 扩大为 Form / Close / Compose 并修订 Glossary l.130
D-3  单一 CURRENT NEXT 的内容（F8）：TS 冻结执行 | MG-2 access→control | 其他
D-4  C1 / C2 分叉（A2；PR 描述已标为未裁决）：意识内容**就是**高层 gate（C1），还是**前景化 / 对象化**一个 gate 或高阶约束（C2）
```

## 5. 机械后续（D-1 / D-2 / D-3 回答后，建议合为一次 bounded 修正）

```text
F2  A2 / MG / AC / PG 声明本线属于 HP-A / PH-AG；foreground 按 A-3.3 标型；target objectification 对照 A-12
F3  Live Term Router 登记最小术语集（按 D-2）
F4  XB §14 / A3 §9 补 von Foerster / Piaget / Poincaré-Cassirer / O'Regan & Noë / Gibson；写出增量或标 reorganization
F5  TS 加 B3（对象中心关系型世界模型）；T4 以 B3 为对照；§19 加调参与计算预算对齐及环境独立性
F6  A1 §4 / PG §13 公式：Selection 为模式，不是乘项
F7  DD 拆分 structural Expectation 与 current goal；l.243 标明形成层且不预设备选集
F8  STATUS 合并两条 CURRENT NEXT；PG §14 只留一个 active next
F9  G 标签改名
```

## 6. 保持 OPEN

- 整体场是否可以由 H1 / H2 还原（H3 增量）；
- 共同 Gate 代数（TF U1–U5）；
- Bearer 索引的整体场重建；
- C1 / C2；
- TS 的结果本身（包括 Z1–Z6 零增益结局）；
- scientific distinctiveness = NOT ESTABLISHED；HP-B = FROZEN；canonical Gate 定义 / 符号 = HOLD；人类 G2–G4 实验 = HOLD。
