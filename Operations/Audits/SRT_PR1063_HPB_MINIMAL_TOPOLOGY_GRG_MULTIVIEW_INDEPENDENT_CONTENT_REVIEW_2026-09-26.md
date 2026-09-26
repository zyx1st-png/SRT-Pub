---
id: SRT-PR1063-HPB-MINIMAL-TOPOLOGY-GRG-MULTIVIEW-INDEPENDENT-CONTENT-REVIEW-20260926
type: audit
status: active
date: 2026-09-26
layer: governance
epistemic_layer: operations
claim_mode: independent_review
canonical: false
research_mode: U
dependency:
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_HPB_MINIMAL_PHENOMENAL_TOPOLOGY_EXPECTATION_GENERATIVITY_AI_BOUNDARY_2026-09-26.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_HPB_ANTICIPATORY_GATE_GRG_GRAMMAR_CORRECTION_2026-09-25.md
  - Philosophy/hooks/PH_CONSC_Minimal_Phenomenal_Topology_Foreground_Mediated_Position_Reconstitution_Hook_2026-09-26.md
  - Philosophy/hooks/PH_CONSC_Gate_Geometry_Bearer_Ontological_Friction_Phenomenal_Admission_Hook_2026-09-25.md
  - Operations/Audits/SRT_HPB_MINIMAL_PHENOMENAL_TOPOLOGY_CONVERGENCE_AUDIT_2026-09-26.md
  - Operations/Audits/SRT_GRG_CASE2_ENGAGEMENT_MULTIVIEW_THREE_ARM_METHOD_VALIDATION_2026-09-25.md
tags: [IndependentReview, PR1063, HPB, MinimalTopology, PositionReconstitution, OneFormation, Bearer, AIBoundary, GRG, ThreeArm]
---

# PR #1063 独立内容评审 — HP-B 最小拓扑 / 过程化感受 / grammar-late GRG

> **角色**：对**未合并**的 draft PR #1063 的 pre-merge 独立内容评审。只读：本记录**不修改** #1063 中的任何其他文件、STATUS、路由面或 canonical owner，也不替作者关闭任何 OPEN。
>
> **评审者独立性与利益披露**：
> - 本 session 写了 #1063 的第一个提交 ed6aa141（#1062 评审）。#1063 之后的作者提交在相当程度上是对那份评审的回应，因此本评审**不评审** ed6aa141 自身。评审对象是 64c2bfbb 至 ace0bb5a 的 14 个作者提交、9 个文件。评审依据是在 be48df15 / ace0bb5a 上重新读取的 owner / source / OPEN guards。
> - 本评审者本身是 LLM 系统，而被评审内容包含对“当前 AI 是否有体验”的判断（F4）。本评审**不主张**当前 AI 有或没有体验，只检查该判断所依据的关系是否已被实际应用。
>
> **评审局限**：原始对话不在仓库中，A0-Q 引文是否逐字、接受事件是否发生，无法核验。

## 0. 评审对象

```text
PR:       #1063 (OPEN, draft; title “bounded review: processual HP-B / unified Gate friction and grammar-late GRG”)
head:     ace0bb5aa7b22c5ca3338c8938444ba67687c8d8
base:     be48df150b8487fb9f2dfec4511fb0c5f95d1047 (main)
reviewed: 64c2bfbb … ace0bb5a (author, 2026-09-25 23:33 → 2026-09-26 10:32 +0800)

S25 = 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_HPB_ANTICIPATORY_GATE_GRG_GRAMMAR_CORRECTION_2026-09-25.md (544)
S26 = 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_HPB_MINIMAL_PHENOMENAL_TOPOLOGY_EXPECTATION_GENERATIVITY_AI_BOUNDARY_2026-09-26.md (452)
HB  = Philosophy/hooks/PH_CONSC_Gate_Geometry_Bearer_Ontological_Friction_Phenomenal_Admission_Hook_2026-09-25.md (broad hook, modified; 543)
HM  = Philosophy/hooks/PH_CONSC_Minimal_Phenomenal_Topology_Foreground_Mediated_Position_Reconstitution_Hook_2026-09-26.md (minimal hook; 598)
CA  = Operations/Audits/SRT_HPB_MINIMAL_PHENOMENAL_TOPOLOGY_CONVERGENCE_AUDIT_2026-09-26.md (548)
VR  = Operations/Audits/SRT_HPB_GRG_MULTIVIEW_BOUNDED_VALIDATION_REVIEW_2026-09-25.md (787)
CR  = Operations/Audits/SRT_HPB_GRG_POST_ADJUDICATION_CORRECTIVE_REVIEW_2026-09-25.md (401)
T3  = Operations/Audits/SRT_GRG_CASE2_ENGAGEMENT_MULTIVIEW_THREE_ARM_METHOD_VALIDATION_2026-09-25.md (572)
GP  = Operations/Proposals/SRT_GRG_MULTIVIEW_OPERATIONAL_REARCHITECTURE_PACKET_2026-09-25.md (modified; 622)
```

控制 owner / source（在 be48df15 上重新读取）：

- `Core_Law/SRT_One_Formation.md`（l.16 角色声明：One / Selection-position 不与 consciousness / phenomenality 等同；Def-OF-1 l.56–74；Def-OF-2 l.78–；Selection-position l.50）
- `Core_Law/SRT_Generative_Ontology_Spine.md` §8（Bearer = formed One / Selection-position + P + E；E 正向确立 OPEN，l.382）；§9 l.403（`Selection-totality -/> pan-consciousness`）
- `AI/SRT_AI_Claim_Status.md`（架构状态护栏 l.71 “Must be cited in all AI consciousness/stake claims”；§2.1–§2.4 默认判定）
- `Philosophy/patches/SRT_Philosophy_PH_CONSC04_...`（Z6）；`..._PH_CONSC05_...`（F2；§3.3 participatory bearing；§9 HP-B 路线）
- `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CONTINUE_DIRECTIONAL_ACCEPTANCE_2026-09-24.md`（裸“继续”= package-level directional acceptance）
- `Governance/SRT_EDIT_PROTOCOL.md` l.83–（same-day guard）
- 前序评审：`Operations/Audits/SRT_PR1062_QUALIA_HPB_GRG_REARCHITECTURE_INDEPENDENT_CONTENT_REVIEW_2026-09-25.md`

## 1. Verdict

```text
MECHANICAL / FRONTMATTER + CI (governance-preflight on ace0bb5a)  = PASS
CANONICAL IMPACT (file edits)                                     = NONE
GUARD INVENTORY (HP-B necessity OPEN / no all-AI verdict / no substrate
  exclusion / no v0.4 / no fusion reopening / stop-loss counted)    = PASS
HM — ANTECEDENT NON-CIRCULARITY                                   = PASS
HM — SUBTRACTION DESIGN (D0–D5) + FAILURE CONDITIONS (F1–F7)      = PASS (strongest part)
HM — DISTINCTNESS FROM ONE FORMATION (Def-OF-1 / Def-OF-2)        = FAIL (not checked; collapse risk)
S26/HM/HB — BEARER ROLE CONSISTENCY                               = FAIL (three texts disagree)
HM — DISCRIMINATOR ADEQUACY (reconstitution vs GNW / implicit learning) = REVISE
S26/HM — CURRENT-AI BOUNDARY                                      = REVISE (relation not applied; hard case absent)
S26 — PROVENANCE OF FRICTION DELETION                             = REVISE (conflicts with S25 A0-Q2)
T3 — THREE-ARM METHOD TEST                                        = PASS WITH NOTES (honest, conservative)
ROUTING / STATUS AFTER MERGE                                      = FAIL (new controlling files unrouted)
NEIGHBOR PACKAGE                                                  = PARTIAL (Gehlen added; key process / positionality neighbors missing)

MERGE #1063                                                       = OK AS NONCANONICAL RECORD after F2 / F8 mechanical fixes
AUTHOR DECISIONS NEEDED                                           = YES (B-1 … B-5, §4)
```

一句话：这一轮对上轮评审的回应方向正确：
- 把“标准条件”与“在线核心”分开；
- 感受改为过程；
- 稳定知觉不再依赖急性摩擦；
- 最小 Z* 连同“语义保持负担”一起写明，停止了“给僵尸不断加功能”的军备竞赛。

但在删去 Bearer、Concern、摩擦之后，核心只剩下“一个已形成 One 的 Selection-position 被前景中介地重构”。这与 canonical 的 One 形成过程（Def-OF-1 / Def-OF-2）几乎同构，而收敛审计没有检查这一点（F1）。同时，Bearer 在三份文本中的地位互相矛盾，“为我性”的来源在最小核心里无着落（F2）。

## 2. 通过项（保留）

- **标准条件 / 在线核心分离**（S26 A-19；HM §2–§3）：不再把 One、Bearer、Concern、期望、摩擦、记忆当成每个现象事件的平铺清单。这是对 #1062 评审 F2 / F3 的实质回应。
- **过程化**（S25 A-12b；HM §9）：“前景是持续更新的过程，不是静态容器”，给稳定蓝墙提供了不依赖 micro-friction 的解释。
- **最小 Z* 与语义保持负担**（S26 A-23；HM §11）：要求删去现象性之后，“current position / foreground mediation / reconstitution”保持同一结构意义，不得悄悄降格为普通状态更新。这是方法上的真实进展。
- **D4 / D5 负对照设计**（HM §10）：D5（多能力共享表征，但冻结操作性生成组织）是迄今最好的 GNW 型负对照设计。
- **AI 判断的措辞纪律**（S26 A-17；HM §12；CA §5）：只说 “NOT ESTABLISHED”，明确不主张全体 AI 无体验、不主张底物排除、不排除未来人工系统。
- **GRG 三组检验真的做了，结论保守**（T3）：加入 no-GRG 组 C，声明污染与非盲，结果为 `REORGANIZATION_ONLY`；两个无增益案例继续计数；§17 把下一步改为“程序设计问题”而非“救援领域”。
- **SRG 笔误澄清**（S25 A-15）；**GRG 修正的真实所指**（S25 A-14：语法本身也是一种对象化操作，而非“三个本体世界”）回答了上轮 F5。
- **Gehlen 邻居指针**（S25 A-13；CR §4）方向合理。
- **机械**：canonical owner 未改动，CI 通过。

## 3. Findings（按严重度排序）

### F1 — 高：最小核心与 canonical 的 One 形成过程几乎同构，面临“凡已形成的 One 皆为体验候选”的坍缩风险，而收敛审计未检查

**证据。**
- HM §2 / §15：`minimal standing condition = formed operative Selection-position`，即任何已形成 One 的时间局部 from-where（One Formation l.50）。Bearer 只在“where independently admitted”时才使用。
- 核心各项与 canonical 的对照：
  - **前景 / 背景**：Def-OF-1（l.56–74）规定每一次 Selection 都在确立 manifest 方向的同时确立 relative background。
  - **位置重构**：Def-OF-2（l.78–）规定“prior Selection-generated vertical organization materially conditions later Selection … repeated non-equivalent reconstitution dependence”。S26 A-20 的判据是“改变后续 Selection 由之生成的操作性组织”，与此非常接近。
  - **期望**：S26 A-18 / HM §4 把最小期望定义为“当前已形成组织本就带有的前瞻不对称”。任何已形成 One 都满足。
  - 真正有限制力的只剩“前景中介”：≥2 个后续生成能力被同一差异共同约束（HM §5）。任何有内部分化的 One 都可能满足。
- CA §4.1 对 Selection-position 的碰撞检查结论为 “NO CANONICAL COLLISION IDENTIFIED”，但它只核对了**词义**没有被重定义，没有核对核心**过程**与 Def-OF-1 / Def-OF-2 的重叠。
- One Formation l.16 明确 One / Selection-position 不与 consciousness / phenomenality 等同；Spine §9 l.403 `Selection-totality -/> pan-consciousness`。S26 与 HM 都没有引用这两处，也没有写 `One != Experiencer`。

**风险。** 两种结局必居其一：
1. 核心会把大量有内部分化的已形成 One（细胞、生态或制度组织、带内部模型的控制器）列为体验候选，即一种未声明的 One 级泛体验论；
2. 真正起排除作用的是某个已被“删去”的条件（Bearer / E、higher-order 阈值），它在隐式地工作。

**修复。** [B-1] 作者裁决：
- (a) 显式接受分级的、One 层面的泛体验论（Whitehead 型），并写出与 Spine §9 的相容性；
- (b) 恢复一个排他性的标准条件（例如独立准入的 Bearer + E，或一个可操作的 higher-order 整合阈值）；
- (c) 保持现状，但写出核心相对 Def-OF-2 的**增量**（评审推荐 (b) 或 (c)）。

机械部分：HM / CA 增加 “Relation to One Formation Def-OF-1 / Def-OF-2” 一节，修正 CA §4.1 的处置。

### F2 — 高：Bearer 在三份控制文本中的地位互相矛盾；最小核心中“为我性”的来源无着落

**证据。**
- **Bearer 可选**：S26 A-19.1（“where independently admitted”）；HM §2；CA §2 表（“Bearer … not the feeling operation”）。
- **Bearer 仍在起作用**：
  - S26 A-24（l.401）的同一性表述：“the same situated process described from the **bearer-relative** generative position”；
  - S26 A-17（l.130）的 AI 边界：“borne as reconstitution of the same continuing generative position”；
  - CR §2 给出的“剩余判别”：“genuinely higher-order **bearer-relative** generative organization”。
- **Bearer 必需**：HB C1（l.62）要求 independently admitted Bearer；HB BP-Q1（l.218–）以 “the same Bearer” 为 ownership / locus anchor，并明言它提供第一人称特征的锚点；HB F2（l.487）把 “bearer irrelevance” 列为降级条件。按 HB 自己的规则，S26 的“Bearer 不是在线核心”恰恰触发 HB 的 F2。
- CA §10 规定“两份 hook 冲突时由 09-26 控制”，但 HB 本身没有任何指向 HM / S26 的注记。单独检索 HB 的 session 只会读到旧图景。
- HM 删去 Bearer 后，没有说明“为我性 / 第一人称特征”由核心中的哪一项承担。HB 把它交给了 Bearer 同一性。

**修复。** [B-2] 作者裁决：Bearer（含 E）是体验的必要标准条件，还是可选的强化条件？“为我性”由什么承担？
- 若必要，则 F1 的排他问题随之解决，但 AI 判断就回到 E 正向确立 OPEN 的上游阻断（#1062 评审 F4）；
- 若可选，则须删去 A-24 / A-17 / CR §2 中隐含的 bearer 措辞，并为“为我性”另找承担者。

机械部分：HB 头注、C1、F2 加 “superseded / narrowed by S26 + HM” 指针。

### F3 — 高/中：“位置重构”单独不构成判别；判别负担实际落在“前景中介”上，而后者没有与 GNW 的强版本区分

**证据。**
- S26 A-20 称位置重构是 “the strongest current discriminator”，判据包括“哪些区分是等价的或承重的”。但无意识的知觉学习也能改变承重区分：Watanabe, Náñez & Sasaki（2001, *Nature*）“Perceptual learning without perception”。内隐统计学习 / 序列学习、睡眠巩固同理。因此位置重构单独不是判别项。HM §6 的阻断清单（world-model update、representation learning “!= Position reconstitution”）与其正面判据之间也存在张力：被阻断的更新类型可能恰好满足正面判据。
- 于是判别负担转到“前景中介”。S26 A-16 / HM §5 的对照对象是“更多模块能读取”，这是 GNW 的弱读法。GNW 的 ignition（Dehaene & Changeux 2011）是持续的长程回响状态，会选择性地放大并约束哪些处理器的输出得以延续，已经接近“重新规定多个能力如何共同继续”。
- “在既有位置内处理内容 vs 重切位置本身”（S26 A-20；HM §7）有一个直接的经典邻居：Piaget 的同化（assimilation）/ 顺应（accommodation）。机器学习中对应的是参数学习与结构学习。

**修复（机械）。** HM §5–§7 / CA §6：
- 以 GNW ignition 的强版本为对手，给出一个“有 ignition 而无位置重构”或“有位置重构而无 ignition”的可判别情形；
- 把 Watanabe 型无意识学习列为位置重构判据的反例，并说明核心为何仍成立（即须与前景中介合取）；
- D5 应写明其预测与 GNW 预测的**差异**；
- 加上 Piaget 邻居。

### F4 — 中高：当前 AI 边界所依据的关系没有被实际应用，最直接的难例（上下文内推理）缺席，有“按标签排除”的风险

**证据。**
- S26 A-24 第 4 条（l.410）要求 “machine comparators fail on a declared relation rather than by label”；CA §6：“The theory does not win if the control is excluded by name.”
- 典型自回归推理中，模型自身的下一步期望塑造被实际化的输出，输出回到上下文，改变接下来能形成什么。上下文内学习会在会话内改变哪些区分被当作等价（von Oswald et al. 2023 认为 ICL 近似实现梯度下降式更新）。HM §12 把 “context update / model revision” 列为“不足以”，却没有给出区分它与位置重构的干预判据。这正是 HM 自己的 F2 “state-update collapse”。
- `AI/SRT_AI_Claim_Status.md` §2.1 对 inference-only 部署的现行判定，依据是**后果回流 / stake 不返回同一持续系统**，属于 Bearer 型理由。若 S26 的 AI 判断实际上依赖这一理由，就与“Bearer 不在核心”（F2）冲突。
- 架构状态护栏（l.71）要求所有 AI 意识判断标明架构状态。HM 只写了 “current typical inference-centered AI”，没有映射到 §2.1–§2.4；persistent-memory（§2.3）与 embodied（§2.4）情形没有分析。

**修复。** [B-3] 作者裁决当前推理系统在哪一项关系上失败：
- (i) 跨会话的位置连续性；
- (ii) Bearer / E；
- (iii) 前景中介；
- (iv) 其他。

机械部分：HM §12 映射到 AI owner §2.1–§2.4，并补一个上下文内推理的逐项演算例。

### F5 — 中：摩擦被移出在线核心，与 09-25 作者原话冲突，只有 package-level 接受

**证据。**
- S25 A0-Q2（l.40）：「你说的无意识成为前景化，**还是需要我说的本体论摩擦的积累呀**。」
- S26 A0-Q1 未提摩擦。S26 A-22 与 HM R1–R4 中已无摩擦项；HM D1 只删去“高 / 急性”摩擦，对非急性、构成性的**积累**是否仍为必要条件保持沉默。
- S26 l.41 写 “The accepted narrowing is controlling”，但依据只是多次「认同，继续」。按 `CONTINUE_DIRECTIONAL_ACCEPTANCE`，裸“继续”只构成 package-level directional acceptance，不使每条 machine 表述升为 A1。`AGENTS.md` Hard Guard 要求实质语义变更交作者二次裁决。

**修复。** [B-4] 作者裁决：本体论摩擦（非急性）的**积累**是否仍是前景化的必要在线条件？
- 若是，HM 增加 R0 项；
- 若否，记录作者对 S25 A0-Q2 的明确修订。

机械部分：S26 A-19 至 A-24 的具体 machine 表述标为 M，另注 record-level directional acceptance。

### F6 — 中：“静息状态下并没有前景”被 machine 改读为假设的完全静止极限，需作者确认

- S25 A0-Q3（l.44）：「静息状态下并没有前景。前景是在某种 high order 处理下获得的一种过程，**用来监控状态**。」
- S25 A-12b.1（l.302–）替作者排除了经验读法，把“静息”改读为 “hypothetical fully quiescent Gate organization”。但清醒静息 / 走神在现象上是丰富的（默认模式网络研究）。作者原意是否就是这个极限读法，需要确认。
- 「用来监控状态」与“感受不是状态”的并存，被 A-12b.3 改读为“监控当前生成构型及其偏离”，同样需要确认。

**修复。** 并入 [B-4]：请作者确认两处改读。

### F7 — 中：Z* 改写与“同一性路线 STRENGTHENED”的措辞；邻居补充

- S26 A-23 把僵尸问题改写为“最后一行是否只是拒绝同一性主张”。这是 type-B 物理主义 / 现象概念策略的标准动作（Loar 1990；Papineau 2002），受到解释鸿沟（Levine 1983）与二维论证（Chalmers）的挑战。
- l.373 的 `identity route = STRENGTHENED BUT OPEN`：核心变得更小，提高的是可检验性与具体性，而不是支持度。建议改为 `SHARPENED BUT OPEN`。
- 缺失的直接邻居（评审 M）：

| 负担 | 邻居 |
|---|---|
| 感受是过程；稳定蓝墙 = 持续的前景化 | O'Regan & Noë（2001）sensorimotor contingency（“seeing is a way of acting”）；Whitehead 过程哲学 |
| “操作性位置 / from-where”及其分级 | Plessner 的 Positionalität（植物开放的 / 动物中心的 / 人离心的 positionality）。它与 F1 的“哪些 One 有体验”直接相关 |
| 选择性归一化、背景卸载、高阶整合 | Gehlen 的 **Entlastung**（卸载）。它比单独的 Mängelwesen 更贴近背景 / 前景机制 |
| 位置内处理 vs 重切位置 | Piaget 同化 / 顺应（见 F3） |
| “只是拒绝同一性” | type-B 物理主义 / 现象概念策略 |

### F8 — 中：合并后的路由与 STATUS 债务

- #1063 未改动 STATUS / router / Live Term Router / Philosophy Hardening Index（CA §12 视之为有意为之）。合并后会出现：
  - `main` 的 CURRENT NEXT 仍写“bounded validation / review of A-6 hook and A-8 packet”，而这项工作已由 VR / CR / T3 完成；
  - STATUS l.733 的第二个 “Current single next” 仍在；
  - router 与 hardening index 只路由 HB + A6–A9 裁决；S25、S26、HM 这三份新的控制文本没有任何入链。这与 #1055 评审 F7 同型。
- #1062 评审的 F1（生成性摩擦应路由到 B08）与 F10（双 next）尚未修复，CR §7 自己也承认这一点。

**修复（机械）。** 合并时或合并后立即做一个路由 follow-up：
- STATUS ledger 加 `#1063 = MERGED / sha`，并更新 CURRENT NEXT；
- 清理 l.733 的第二个 next；
- router §8 与 hardening index 加入 S25 / S26 / HM；
- Live Term Router 的 friction 行按 #1062 评审 F1 拆分。

### F9 — 中低：三组检验的量表与结论措辞

- **天花板效应**：F / H / R / I 四个实质维度三组全为 2，三点量表无法区分。
- **构念偏向**：B 唯一胜过 C 的维度 X（cross-view integration）正是 B 的设计特征。
- **措辞过强**：T3 §14 的 “validates”，对污染的、事后的、自评的比较而言过强，应改为 “is consistent with”。
- **保留理由**：`multiview = RETAIN AS OPTIONAL` 只能以 SRT 内部组织价值为理由（§15 已这样说）。按简约原则，这个案例中对目标领域更可取的是 C。

结论 `REORGANIZATION_ONLY` 本身是恰当的。

### F10 — 低：稳定性与 PR 范围

- HP-B 机制在约 11 小时内被重述了五次：
  1. 09-25 23:16 局部支付失败；
  2. 23:53 双路线；
  3. 09-26 00:07 统一摩擦；
  4. 00:18 过程化；
  5. 10:30 去掉 Bearer / 摩擦的最小核心。

  Ψ_f 的角色也从核心触发条件，变为普遍的构成项，再变为不在核心中。same-day guard（Edit Protocol l.83–）的触发精神已满足，但没有违规，因为没有写入 Freeze-A。
- #1063 以“评审 PR”开始，现在包含 2 份作者裁决、2 个 hook、1 个提案修改和 4 份审计。建议作者考虑把理论改动与评审记录分开，或者至少在合并时的 ledger 中分列。

## 4. 需要作者裁决的事项

```text
B-1  最小核心与 One 形成（F1）：
     (a) 显式接受 One 层面的分级泛体验论
     (b) 恢复排他性标准条件（Bearer + E，或可操作的 higher-order 阈值）（评审推荐 b 或 c）
     (c) 保持现状，写出核心相对 Def-OF-2 的增量
B-2  Bearer 的地位与“为我性”的来源（F2）：必要标准条件 | 可选强化条件；为我性由什么承担
B-3  当前 AI 在哪一项关系上失败（F4）：跨会话位置连续性 | Bearer / E | 前景中介 | 其他
B-4  （非急性）本体论摩擦积累是否仍是前景化的必要在线条件（F5）；
     “静息无前景”与“用来监控状态”的改读是否符合原意（F6）
B-5  #1063 是否把理论改动与评审记录拆分（F10）
```

## 5. 无需作者裁决的机械后续

```text
F1  HM / CA 增 “Relation to One Formation Def-OF-1 / Def-OF-2”；修正 CA §4.1
F2  HB 头注 / C1 / F2 加 S26 / HM 指针
F3  HM §5–§7 / CA §6：GNW ignition 强版本对照；Watanabe 型反例；D5 与 GNW 的预测差异；Piaget
F4  HM §12 映射到 AI owner §2.1–§2.4，补上下文内推理演算例（判定待 B-3）
F5  S26 A-19 至 A-24 节级 provenance 标注（A0-Q / M）
F7  STRENGTHENED -> SHARPENED；邻居补充
F8  路由 follow-up（STATUS ledger / CURRENT NEXT / 第二个 next；router；hardening index；friction 行拆分）
F9  T3 §14 措辞
```

## 6. 保持 OPEN（本评审刻意不关闭）

- HP-B 逻辑必然性；最小 Z*（MPT-Z*）是否矛盾；
- 构成性同一假设的真值；
- 位置重构的可操作判据（HM F2 “state-update collapse”）；
- Spine §8 E 的正向确立；
- 当前与未来人工系统的体验地位；
- CΨ（OPEN_TENSIONS §18）；felt Ψ_f 与 actual Ψ_f 的映射；
- GRG 名称与程序身份（T3 §17）；scientific distinctiveness = NOT ESTABLISHED；fusion lane PAUSED；GRG v0.4 / BCTB T2 = HOLD；
- 2026-09-24 作者排序（先优化 Spine）的执行仍未启动。
