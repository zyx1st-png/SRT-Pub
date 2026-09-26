---
id: SRT-PR1062-QUALIA-HPB-GRG-REARCHITECTURE-INDEPENDENT-CONTENT-REVIEW-20260925
type: audit
status: active
date: 2026-09-25
layer: governance
epistemic_layer: operations
claim_mode: independent_review
canonical: false
research_mode: U
dependency:
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_QUALIA_HPB_GRG_REARCHITECTURE_ONTOLOGICAL_FRICTION_2026-09-25.md
  - Philosophy/hooks/PH_CONSC_Gate_Geometry_Bearer_Ontological_Friction_Phenomenal_Admission_Hook_2026-09-25.md
  - Operations/Proposals/SRT_GRG_MULTIVIEW_OPERATIONAL_REARCHITECTURE_PACKET_2026-09-25.md
tags: [IndependentReview, PR1062, HPB, PhenomenalAdmission, Bearer, OntologicalFriction, PsiF, GRG, Rearchitecture, SameDayGuard]
---

# PR #1062 独立内容评审 — HP-B 机制重开 / 共同重构 hook / GRG 多视角重构 / 本体论摩擦统一

> **角色**：对**已合并** PR #1062 的 post-merge 独立内容评审记录（#1062 从创建到合并用时 53 秒，合并前没有评审窗口）。本记录只读：**不修改** #1062 的任何文件、STATUS、路由面或 canonical owner，也不替作者关闭任何 OPEN。
>
> **评审者独立性**：独立 session / model context，没有参与 A-6…A-9 的对话，也没有参与 #1062 的写作。本 session 此前写过 #1058 的评审（#1059），D1–D5 审计不是本 session 所写。评审依据是在 `main`（be48df15）上重新读取的 owner / source / OPEN guards。
>
> **评审局限**：原始对话不在仓库里，A0-Q 引文是否逐字无法核验。本评审**不对**作者的方向性裁决本身（例如 A-9 “两者指称同一概念”）作真假判定，只检查：它在仓库里的落地是否与现有 owner 相容，claim 强度是否与证据相称，以及 hook / packet 自己声明的负担是否已付。

## 0. 评审对象

```text
PR:          #1062 (MERGED 2026-09-25 15:16:12Z; created 15:15:19Z)
squash:      be48df150b8487fb9f2dfec4511fb0c5f95d1047
base:        05791027634800691fb9669e9178d56d7d81ebb4
PR head:     a5d703211c46b4ef829ab054bfa8c441dc6b9558 (9 commits, 23:11–23:15 +0800)
files (9):
  S  = 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_QUALIA_HPB_GRG_REARCHITECTURE_ONTOLOGICAL_FRICTION_2026-09-25.md (653 lines)
  H  = Philosophy/hooks/PH_CONSC_Gate_Geometry_Bearer_Ontological_Friction_Phenomenal_Admission_Hook_2026-09-25.md (428 lines)
  P  = Operations/Proposals/SRT_GRG_MULTIVIEW_OPERATIONAL_REARCHITECTURE_PACKET_2026-09-25.md (586 lines)
  G  = Glossary/SRT_Live_Term_Router.md (friction rows → l.118–119)
  ST = STATUS.md; R = _SRT_CONTEXT_ROUTER.md; PHI = Philosophy/_SRT_Philosophy_Hardening_Index.md
  D  = D1–D5 audit post-note; RP = gate-geometry routing patch §6.0
```

控制 owner / source（均在 be48df15 上重新读取）：

- `_SRT_PSI_F_CANONICAL.md`（Def-Ψ-1 l.66–72；Def-Ψ-3 payability l.182–；`Ψ_f > 0 and payable` l.318–330；Def-Ψ-Obs-1 l.340–349；**canonical 管辖边界 §(一) l.254–262**）
- `Core/SRT_Core_21c_Bridge_Hypotheses.md` P2/P3-B08（`Ψ_f` as Generative Principle，l.196）
- `Core/SRT_OPEN_TENSIONS.md` §2（Ψ_f 三读法边界）；§18（CΨ `Ψ_f → 0` valence conflict，OPEN）
- `Core_Law/SRT_Generative_Ontology_Spine.md` §8（Bearer = formed One / Selection-position + P + E；“Positive independently applicable E establishment remains OPEN” l.382）
- `Philosophy/SRT_HardProblem_Epistemology.md` §3.2（已有的构成性候选：phenomenal first-person presence 是 fully situated bearing 的内部方式；`B_s -> B_p ?`）
- `Philosophy/patches/SRT_Philosophy_PH_CONSC05_...Functionalization_Residual_v0_1.md`（F2 l.154–175；§3 四个不充分桥 l.178–232，含 §3.3 participatory bearing；§5 permutation；§6 Copy–Branch；§9 HP-B 三条路线 l.418–469；§10 Phenomenal Admission Gate）
- `Philosophy/patches/SRT_Philosophy_PH_CONSC04_...Zombie_Deletion_Test_v0_1.md`（Z6）
- `Operations/Audits/SRT_GATE_GEOMETRY_QUALIA_D1_D5_BOUNDED_ROUTING_AUDIT_2026-09-25.md`（D4.1–D4.4；P1–P12；D5.2）
- `Operations/Proposals/SRT_GRG_FOUNDATIONAL_PROTO_GRAMMAR_V0_3_2026-09-21.md`（§4.3 l.196–212；§22 l.945–953）；`..._CROSS_OBJECTIFICATION_GENERATIVE_ARCHITECTURE_V0_1_2026-09-23.md`
- `_SRT_SYMBOL_TABLE.md` l.27（L0/L1/L2 aspect boundary，引入于 71d3b604 / 2026-09-15）
- `Operations/Audits/SRT_GRG_CASE2_ENGAGEMENT_VERTICAL_DECOMPOSITION_RESULT_2026-09-24.md`（no-GRG ablation l.274；§15 LLM-prior limitation l.798–；control list l.832–）
- `Governance/SRT_EDIT_PROTOCOL.md` l.83–（same-day rapid author-dialogue guard）；`Governance/SRT_CLAIM_LADDER.md` l.117–118

## 1. Verdict

```text
MECHANICAL / FRONTMATTER (check_frontmatter_changed vs 05791027)   = PASS (errors=0 warnings=0)
CANONICAL IMPACT (file edits)                                      = NONE (no Freeze-A owner file changed)
CANONICAL IMPACT (routing)                                         = REVISE — G routes P2/P3 generative-friction readings
                                                                     to the canonical Ψ_f owner against its own §(一)
GUARD INVENTORY (HP-B necessity OPEN / no v0.4 / no fusion reopening /
  no Ψ_f subtype / One≠Bearer≠Experiencer / gate≠Ψ_f)              = PASS
H — NON-CIRCULAR ANTECEDENT (C1–C7)                                = PASS (D4.1 circularity repaired)
H — FAILURE CONDITIONS (F1–F6)                                     = PASS (concrete; best part of the package)
H — HP-B ROUTE TYPING vs PH-CONSC05                                = REVISE (route undeclared; §3.3 / F2 not engaged)
H — SCOPE (steady low-conflict perception)                         = REVISE (C4 fits affect, not ordinary presence)
H — P4 PATH                                                        = BLOCKED UPSTREAM (Bearer E-establishment OPEN)
P — REARCHITECTURE RATIONALE                                       = REVISE (v0.3 was not layer-based)
P — VALIDATION DESIGN                                              = REVISE (no no-GRG arm; no freeze; LLM prior)
NEIGHBOR PACKAGE                                                   = FAIL (closest functional neighbors unnamed)
STATUS SINGLE-NEXT CONSISTENCY                                     = FAIL (two “next” blocks again; stale guard l.208)
SAME-DAY STABILITY                                                 = CAUTION (guard trigger condition met; no violation)

REVERT #1062                                                       = NO
OVERALL                                                            = KEEP; BOUNDED FOLLOW-UP REQUIRED
AUTHOR DECISIONS NEEDED                                            = YES (B-1 … B-5, §4)
```

一句话：#1062 做对了最难的一件事。它把 HP-B 候选的前件改写成不含现象词汇的 C1–C7，并给出了六条可以失败的条件。这让 SRT 第一次有了一个“可以被检验失败”的正向意识机制假说，而不只是“结构承担不证明感受”。

但有三处需要处理：
1. **命题部分**：BP-Q1 的“第一人称来源”恰好落在 PH-CONSC05 已判为不充分的那一侧；它的适用范围按 C4 只覆盖情感 / 显著性体验，却被表述为“为什么会有感觉”的一般解释。
2. **路由部分**：A-9 的术语统一绕过了 canonical Ψ_f 自己划定的 P2/P3 边界。
3. **GRG 部分**：重构的理由与 v0.3 的实际形态不符，验证设计缺少 stop-loss 所依据的那个对照。

## 2. 通过项（保留）

- **循环已修复**：H §2 明确禁止在前件中使用 felt / phenomenal / experience / qualia / for-me，C6 写明“report / language / metacognition / self-model optional”。D4.1 指出的“phenomenal objectification 进入 HP-B 前件即循环”在 H 中已经解决。
- **失败条件可检验**：H §10 F1–F6 分别对应 access 吸收、bearer 无关、friction 无关、共同重构无独立预测、循环回流、gate-geometry 冗余。这正是 PH-CONSC05 §9 Route B 所要求的“produce discriminating predictions”的前置形态。
- **用对了 D1–D5**：H 以 D4.4 给出的“最强非循环压力线”（same-bearer mutual resolution dependence + non-outsourcable consequence closure + structural foregrounding + future-selectability rewrite）为骨架，没有另起炉灶。
- **在无意识承担与有感承担之间划出了有原则的切分**：H §4（局部可支付则可保持无意识）是 HardProblem §3.2 所缺的。§3.2 只说 “fully situated bearing 的内部方式”，没有说哪些承担是有感的。BP-Q1 给出了切分条件。这是实质进步。
- **与 canonical 可支付性相容**：“局部支付失败 → bearer 级升级”保持了全局 payability（Def-Ψ-3；`Ψ_f > 0 and payable` l.318–330）。H §6 Q2 的 `Psi_f_actual != Psi_f_felt` 与 Def-Ψ-Obs-1（痛苦 / 焦虑 / 惊讶不是 Ψ_f 本身，而是尖峰 / 变化率 / 逼近不可支付边界的报警，l.342）方向一致。
- **A-9 与 canonical 的自我理解一致**：canonical Ψ_f §0 本来就把各领域读法写成“同一结构在不同描述层上的投影”。作者的术语规则（理论侧一律写“本体论摩擦 / Ontological Friction”，物理摩擦须显式限定）干净，也没有引入 Ψ_f 子类型符号。
- **GRG 的 stop-loss 纪律**：P §13 显式封堵“旧方法无增益 → 改名 → 换领域 → 重置证据时钟”；P §12 要求用既有案例、不开新领域，结果状态包含 `NO_GAIN` / `REORGANIZATION_ONLY`；遵守 architecture first / name second；gate geometry 标为可选。
- **机械检查**：frontmatter 变更检查 0 error / 0 warning。

## 3. Findings（按严重度排序）

### F1 — 高：A-9 的术语路由把 P2/P3 的“生成性摩擦”读法指向了 canonical Ψ_f owner，违反 canonical 文件自己的管辖边界

**证据。**
- `_SRT_PSI_F_CANONICAL.md` §(一)（l.258–262）：canonical 管辖范围只是 payability 主读（Def-Ψ-1）、条件投影（Def-Ψ-2）与可支付性判据（Def-Ψ-3）。“摩擦是所有动力学的生成性来源”**不在**本文件管辖范围，其落点是 `Core_21c P2/P3-B08`。“演化 / 学习 / 文化变迁 / 免疫应答可建模为算子间摩擦”必须引用 B08 并按 P2/P3 标注，“不得回引本文件为其升格背书”；“若某个域内推导只有在「摩擦即生成」成立时才成立，该推导继承 P2/P3 等级”。
- G l.118 新行把 friction、maintenance cost、**transformation pressure**、boundary friction、constitutive friction、bearer-relative reconstruction burden 全部登记为 `ALIAS_TO_CANONICAL_PSI_F / CONTEXTUAL_READING`。owner 列只写 `_SRT_PSI_F_CANONICAL.md` + A6–A9 源 + GRG provenance，**没有 B08**。
- S A-9.2 列出 formation / maintenance / reconstruction / consciousness / agency 五种“contextual emphasis”，全部挂到 canonical Ψ_f。其中 reconstruction（改写 gate geometry）、agency（recut 的可支付性）以及 GRG 旧用法中的 transformation / friction conversion，属于或依赖“摩擦生成动力学”的 B08 型主张。
- S l.524 称 “No canonical semantic rewrite is required merely to recognize this identity”。只有当路由尊重 §(一) 时这句话才成立；否则就是通过非 canonical 路由面，事实上扩大了 canonical owner 的背书范围。
- 残留冲突护栏：STATUS l.208 仍写 `constitutive / boundary friction != Psi_f automatically;`；trace T' l.702 仍写 `friction PARTIAL_OVERLAP Psi_f … identity not established`。两处都没有指向 A-9 的 supersession 注记（RP l.661 位于已被 §6.0 覆盖的历史节，可接受）。
- 另：H Q3（valence）与 S A-9.2 的 consciousness 读法，都会碰到 OPEN 的 CΨ（OPEN_TENSIONS §18：`Ψ_f → 0` 在 Core 中是退化 / 无 stake 极限，在 Spirituality 中却被映射为圆满）。BP-Q1 意味着 `Ψ_f` 可局部支付时体验退回背景。它对 CΨ 两种读法的含义没有交代。

**风险。** 后续 session 会以 “canonical Ψ_f” 为据，为 GRG 案例中的生成性摩擦主张或意识生成主张背书，把 P2/P3 或 P3/P4 的推导抬到 canonical 强度。这正是 §(一) 设立的目的所要防止的。

**修复。** [B-3] 保留作者的“同一概念”裁决，但在 G 中拆分路由：
- formation / maintenance / payability 读法 → canonical Def-Ψ-1 / Def-Ψ-3；
- generative / transformation / reconstruction / agency-recut 读法 → **B08（P2/P3）**，并注明“不得回引 canonical 升格”；
- consciousness / felt 读法 → Def-Ψ-Obs-1 观察规则 + H（P3/P4）。

机械部分：STATUS l.208 与 T' l.702 加 “superseded by A-9 at concept level; routing per G” 指针；H / S 各加一句说明 BP-Q1 对 CΨ（§18）两种读法的含义留 OPEN。

### F2 — 高：BP-Q1 的第一人称来源落在 PH-CONSC05 已判为不充分的一侧；H 没有声明自己走的是哪条 HP-B 路线

**证据。**
- H §3 l.169：“This identity of affected unit and continuing selection-locus is the **candidate source of first-person character**.” S A-6.3：“for-me character … arises because the deformation … becomes constitutive of the current from-where”。
- PH-CONSC05 §3.3（participatory bearing）：“P does not merely represent event e; e participates in constituting P_(t+1) … constitutive state update can occur in non-phenomenal candidate systems → `participation !-> phenomenality`”。F2（l.154–175）的 bearer-constitutive For-P 同样被标为 `strong For-P != For-me proved`。H 把 PH-CONSC05 列为 dependency，正文却没有引用 §3.3 / F2 / §9。
- PH-CONSC05 §9 给出 HP-B 的三条路线：A 构成性同一（负担：非循环地证明 Z* 矛盾）；B “structural bearer package + X”（负担：独立定义 X、给出区分性预测、说明 X 为何不只是又一个功能相关项）；C 消解形而上推导要求、保留 admission 问题。
- 由此形成一个钳形：
  - 使 BP-Q1 **区别于** GNW 的成分是 C1 / C7（同一 Bearer、当前 Selection-position 被重构）。但它们正是 §3.3 / F2 已判为**不充分**的那部分。
  - 使 BP-Q1 **可能充分**的新增成分是 C4–C6（局部支付失败、相互 resolution 依赖、共享的 selection-active 前景压缩态）。但它们在功能轮廓上正是全局工作空间类理论的核心：无意识专门处理器无法局部解决时，招募全局广播 / 共享内容。
- S A-6.1 的目标句（l.76）问的是 “why would a formed Bearer need a felt / first-person mode at all”。H §5 给出的是**结构侧**的功能理由：低维共享前景使高维 bearer 级形变可协调。Z6-GG（H §9 自认 “not yet shown contradictory”）说明这个结构功能可以在没有感受的情况下成立。所以“需要”论证解释的是为何需要结构前景化；“它被感受到”这一步只由 BP-Q1 的 “is the first-person mode of” 断定。
- HardProblem §3.2 本已承载一个构成性候选（phenomenal presence 是 fully situated bearing 的内部方式）。BP-Q1 实际上是在它之上加了 X = C4–C6，属于**收窄后的 Route A**，或者说 **Route B（X = C4–C6）**，而不是从 HOLD 状态“重开”一条全新路线。

**风险。** “HP-B mechanistic explanation candidate / why feeling arises” 的措辞会被读作已经提供了从结构到感受的解释。实际上 H 提供的是：(i) 一个桥原则（同一性）假设；(ii) 结构侧的功能说明；(iii) 一个可检验的“何时有感”划界。三者都有价值，但不是同一种东西。

**修复。** [B-1] 作者裁决 BP-Q1 的路线归属（评审推荐：**Route B，X = C4–C6，同时继承 §3.2 的 Route A 取向**）。机械部分：
- H 增一节 “Relation to PH-CONSC05 §3.3 / F2 / §9”，承认 bearer 成分单独不充分，写明 X 须付的三项 Route B 负担；
- S A-6.4 / H §5 的 “why feeling / useful” 改写为 “why a common structural foreground is needed; its being felt is the BP-Q1 posit”；
- 措辞从 “mechanistic explanation” 调为 “bridge-principle hypothesis with a functional account of the structural side and a testable admission boundary”。

### F3 — 高：C4 使 BP-Q1 适配情感 / 显著性体验，但不适配稳定、低冲突的日常知觉；H 把这个范围问题推迟为“非阻断项”

**证据。**
- C4（H l.89–）要求：相关负担无法在局部背景 gate 内被吸收。H §4：局部可支付则无意识调节可以维持。
- D1–D5 P1：“neutral sensory quale — low acute friction can still be phenomenally vivid”。静看一面稳定的蓝墙、听一个持续的纯音，都是鲜明的现象在场，却很难说是“局部支付失败”。
- H §5 的例子里有 “many sensory relations → stable qualitative color / pitch / texture object”（l.222）。“稳定”知觉被放进了一个以“局部支付失败”为触发条件的机制里。
- H §11 Q3（“low-friction mature sensory qualia require ongoing micro-friction or can be sustained mainly by already-stabilized gate geometry”）被标为 “not blockers”。但它决定 BP-Q1 是一般的现象在场理论，还是情感 / 显著性体验理论：
  - 如果稳定知觉可由已稳定的几何维持，则 C4 不是现象在场的必要条件，“为什么会有感觉”只对一部分体验成立；
  - 如果答案是处处存在 micro-friction，则 C4 趋于平凡，接近 H 自己的 F4（无独立预测）。
- canonical Def-Ψ-Obs-1 把**痛苦 / 焦虑 / 惊讶**（情感类）读为逼近不可支付边界的报警，这恰好支持把 C4 用于情感维度，而不是用于全部在场。
- 梦（D1–D5 P5）：C3 写的是 “**World-side** actualisation imposes … Ψ_f”，外部输入弱而体验鲜明的情形需要说明内部 actualisation 是否算数。

**修复。** [B-2] 作者裁决 BP-Q1 的范围：
- (a) 限定为情感 / 显著性在场，稳定知觉的在场另由（或留 OPEN 给）已稳定 gate geometry 路线承担，形成双路线结构（评审推荐）；
- (b) 承诺处处存在 micro-friction，并给出区别于 F4 平凡化的判据；
- (c) 把 C4 改写为 “cannot be handled without a common foreground”，不再是 “payment failure”。

机械部分：H §11 Q3 升为范围决定项；C3 注明内部 actualisation 的处理。

### F4 — 中高：C1 依赖的 Bearer 正向确立在 canonical 中仍 OPEN，P4 路径在上游被阻断

**证据。**
- H C1：“A Bearer must already be independently admitted under the current repository route.” Spine §8 l.382：“Positive independently applicable E establishment remains OPEN”；non-outsourcing 反事实只是一致性 / 排除测试，不是完整的正向准入程序。
- H §8 要求 “vary or dissociate: same-Bearer consequence closure; … non-outsourcable history writeback”。可仓库目前没有可操作的判据来判定被操纵的变量（Bearer 身份 / E）何时成立。
- PH-CONSC05 §5（permutation / bearer-isomorphism）与 §6（Copy–Branch Test）正是为 “same-bearer / non-outsourcing” 设计的思想实验，H §8 的 “digital / AI systems with copied or outsourced consequence architectures” 却没有接到这两节。
- H frontmatter `claim_level: P3_P4`，而 S A-7.3 自己说 “what remains missing for stronger P4 standing is a matched-control design”。

**修复（机械）。** H §8 注明：P4 强化以 Spine §8 的 E 正向确立（或一个声明性的操作化 Bearer 判据）为前置；把 AI / copy 情形接到 PH-CONSC05 §5–§6；frontmatter 在区分设计出现前改为 `P3`（目标 P4）。

### F5 — 中高：A-8 的重构理由与 GRG 的实际形态不符——v0.3 并不是按 L0/L1/L2 分层构建的

**证据。**
- S A-8.1（l.308）：“old working picture: L0 / L1 / L2 were often operationalized as layered / stratified surfaces”。P §1 l.36：“A large part of its prior architecture was compatible with a layered reading”；l.63：“This is a root-method change.”
- GRG v0.3 全文只在 §22（l.950–953）两次提到 L2，而且原文是 “objectified measurement slice of an L2 / history aspect … **Do not treat ‘L2-facing’ as a canonical type**”。v0.3 §4.3（l.196–212）：verticality “is not a variable ontology. It is a research relation among question / objectification / …”。l.1175：`new Level = NO`。09-23 cross-objectification architecture 全文没有使用 L0/L1/L2。
- “aspects, not three ontic substances or a compulsory three-stage product pipeline” 早在 2026-09-15 已进入 `_SRT_SYMBOL_TABLE.md` l.27（71d3b604），早于 v0.3（09-21）。
- P §13 的 stop-loss 规则：“change method only if **author ontology changed**”。按上述证据，“视角而非层”不是一次足以迫使 GRG 重构的本体变化。v0.3 本来就不依赖分层。

**风险。** 重构的真实性质是一项**新的设计提议**：以 L0/L1/L2 视角作为 GRG 的操作框架，并以 gate geometry 为可选脚手架。它出现在两个无增益案例之后。如果把它说成“本体修正所迫”，恰好满足 P §13 想要封堵的那种证据时钟重置叙事。

**修复。** [B-4] 作者确认重构是新设计选择，而非对“分层 v0.3”的修正。机械部分：P §1 / S A-8.1 改写理由（引 v0.3 §4.3 / §22、Symbol Table l.27）；P §13 的条件改为 “change method only if a stated design hypothesis predicts gain over both old method and no-GRG baseline”。

### F6 — 中：P §12 验证设计缺少 no-GRG 对照组，也没有冻结与 LLM 先验控制

**证据。**
- P §12 只比较 A（09-23 协议）与 B（multiview），由 “same model / analyst” 在 “an already understood case” 上执行。
- 两个无增益结论都是**相对于普通因果 / 系统分析**得出的：case2 no-GRG ablation l.274；D1–D5 D5.2 `eight-question gate reconstruction != GRG gain by itself`。只比 A 与 B，可能得到 B > A、而两者都不优于 C 的结果，无法回答 stop-loss 真正的问题。
- case2 §15（l.798–）已记录 LLM 先验污染在主检验中未受控；l.832– 列出后续 LLM 执行检验应加的控制（same-model no-GRG control 等）。P §12 使用“已理解的案例”，同一模型已经看过该案例的分解结果，污染更重。
- 度量项（hidden-assumption exposure、explanatory compression、failure clarity 等）没有操作定义、评分者或事先冻结的评分规则。
- A-8.3 / P §3 的诊断（“其他领域多有局部视角，缺乏完备性与整体性”）没有设负对照。evo-devo 明确整合了发育潜能 / 形态空间约束（L0 型）、形态发生（L1 型）与进化历史 / 调控网络（L2 型），是检验 “completeness gain” 的天然负对照。

**修复（机械）。** P §12 增加：
- C 组：same-model no-GRG / 普通多尺度因果分析；
- 执行前冻结预测、度量定义与评分规则；
- 盲评或跨模型评分；
- 一个多视角整合已成熟的负对照领域（仍用既有材料，不开新 fusion 域）。

### F7 — 中：邻居包缺少与 BP-Q1 功能部分最直接重叠的理论

H §8 只列了 GNW / IIT / generic integration / arousal / report。二次裁决 B-4 要求 “light neighbor awareness before any claim of distinctiveness”，A-6 却在未补邻居的情况下把 HP-B 升为 ACTIVE。

| #1062 负担 | 直接邻居（评审 M，供 H §8 / P §3 使用） |
|---|---|
| C4–C5：局部无法解决 → 多个本可分离的系统互相约束 → 需要有意识状态 | Morsella 的 Supramodular Interaction Theory（*Psychological Review* 2005）与 Passive Frame Theory（*BBS* 2016）：现象状态的功能是整合相互冲突的行动系统 |
| S A-6.1 / H §5：“为什么 Bearer 需要感受”——稳态需要无法自动满足时，感受作为优先化接口 | Solms & Friston（*JCS* 2018）；Solms（2021，*The Hidden Spring*）：情感在稳态需要无法自动满足、须在多需要间排序时被感受 |
| C6：共享的 selection-active 前景压缩态 | Baars 的 GWT（新颖 / 冲突情境招募意识）；GNW 的 ignition |
| BP-Q1 “is the first-person mode of” | dual-aspect / Russellian monism（同一事件的结构面与第一人称面） |
| C7：被对象改变的机体本身成为体验的“从何处” | Damasio 的 core consciousness |
| P §3 / A-8.3 多视角的完备与整合 | integrative pluralism（Mitchell 2003）；perspectival realism（Massimi 2022）；mechanistic multilevel integration（Craver 2007）；evo-devo（见 F6） |

**修复（机械）。** H §8 把 Morsella / Solms / GWT 列为匹配对照必须击败的对手：若 “冲突整合 / 稳态优先化” 已能预测全部差异，则按 F1 / F3 处理。P §3 补上方法论邻居。本评审不主张 BP-Q1 被这些邻居吸收，只要求在称其为 SRT 特有机制之前完成比对。

### F8 — 中：同日稳定性——same-day guard 的触发条件已经满足（没有违规）

- 2026-09-25（+0800）时间线：22:26 源落地（40b22d9）→ 22:42 #1059 评审 → 22:50 二次裁决 → 22:57 D1–D5（1213 行）→ 23:16 #1062。50 分钟内五次基础层落地。
- 同一概念的状态翻转：
  - friction 与 Ψ_f 的关系三次翻转：22:26 `not automatically Ψ_f` → 22:50 `PARTIAL_OVERLAP; identity NOT ESTABLISHED; separation also not assumed` → 23:16 `same concept`；
  - HP-B 机制：22:57 建议 HOLD → 23:16 ACTIVE。
- #1062 从创建到合并用时 53 秒。
- `SRT_EDIT_PROTOCOL.md` l.83– 的 same-day guard 针对的正是“同一天的 author dialogue 仍在快速生成、修正或相互覆盖 foundation-level 概念”。本包没有写入 Freeze-A，**没有违规**。但 A-6 / A-9 目前应视为尚未稳定：在冷却期和一次独立复核之前，不宜作为任何 Freeze-A 落地的输入。本评审可以充当这次复核的第一轮。

### F9 — 中低：provenance——方向是作者的，细节是机器的

- S 的 A0-Q（l.36）给出了 A-6…A-9 的方向，例如「我感觉目前的材料已经可以去解释为什么会有感觉了呀」。但 BP-Q1 的具体措辞（S l.115 “Working machine formulation accepted for testing”）、C1–C7、Q1–Q4、A-8.4 的 engine 以及 A-9.2 的五种读法，都没有逐条接受事件。frontmatter 写的是 `author_status: explicit_A6_A9_adjudication`。按 Phase-3 provenance map D1，这些细节应标为 **M**，另注 record-level directional acceptance。
- A-8 原话中的 “SRG”（S l.39–40 已保留原样并注明无 owner）很可能是 “SRT” 的笔误。[B-5] 请作者确认。

### F10 — 低：STATUS / frontmatter 杂项

- **双 next**：STATUS §0 l.58–59 的 `CURRENT NEXT = bounded validation / review of A-6 HP-B mechanism hook and A-8 GRG multiview …`，与 “Immediate routing” l.733–739 的 `Current single next: HIGH-PRIORITY GATE-GEOMETRY / QUALIA BOUNDED ROUTING PATCH`（owner 为已完成的 RP）并存。这与 #1059 评审 F11 指出的是同一类问题。
- l.72 `A-6..A-9 AUTHOR ADJUDICATION = COMPLETE / current branch package pending merge`，合并后已过时。
- §0 ledger 没有 `#1062 = MERGED / be48df15` 行（#1059 已有同类行）。
- STATUS l.208 旧护栏见 F1。
- H frontmatter `claim_level: P3_P4` 见 F4。

## 4. 需要作者裁决的事项

```text
B-1  BP-Q1 的 HP-B 路线（F2）：
     (a) PH-CONSC05 Route B，X = C4–C6，继承 HardProblem §3.2 的 Route A 取向（评审推荐）
     (b) 纯 Route A：须承担“非循环地证明 Z* / Z6-GG 矛盾”的负担
     (c) 其他
B-2  BP-Q1 的范围（F3）：
     (a) 情感 / 显著性在场；稳定知觉另由已稳定 gate geometry 路线承担或留 OPEN（评审推荐）
     (b) 处处 micro-friction，并给出防止平凡化的判据
     (c) 把 C4 改写为 “needs a common foreground”
B-3  A-9 的路由拆分（F1）：同一概念不变；generative / transformation / reconstruction /
     agency-recut 读法按 canonical §(一) 路由到 B08（P2/P3）（评审推荐） | 其他安排（须同时修改 canonical §(一)，属 C 类）
B-4  A-8 的性质（F5 / F6）：确认 multiview 是新设计选择而非对“分层 v0.3”的修正；
     验证是否纳入 no-GRG 对照组与冻结规则
B-5  A-8 原话中 “SRG” 的所指（F9）
```

## 5. 无需作者裁决的机械后续（建议合成一个 bounded follow-up PR）

```text
F1  STATUS l.208、T' l.702 加 A-9 supersession 指针；H / S 注明 CΨ（§18）含义 OPEN；G 行的拆分待 B-3
F2  H 增 “Relation to PH-CONSC05 §3.3 / F2 / §9” 节；A-6.4 / H §5 的功能论证措辞收窄
F3  H §11 Q3 升为范围决定项；C3 注明内部 actualisation
F4  H §8 注明 Bearer E 前置；接 PH-CONSC05 §5–§6；claim_level 暂标 P3（目标 P4）
F5  P §1 / S A-8.1 理由改写；P §13 条件改写（待 B-4）
F6  P §12 增 C 组、冻结、盲评或跨模型评分、负对照领域
F7  H §8 / P §3 邻居补充
F9  S 节级 provenance 标注（A0-Q / M）
F10 STATUS 双 next、过时行、ledger 行
```

## 6. 保持 OPEN（本评审刻意不关闭）

- HP-B 逻辑必然性（`B_s -> B_p ?`）；Z6-GG 不矛盾的现状；
- BP-Q1 作为桥原则的真值；其范围（B-2）；
- Spine §8 E 的正向确立；
- CΨ（`Ψ_f → 0` valence conflict）；
- felt Ψ_f 与 actual Ψ_f 的映射；concern-beyond-bearer；
- GRG 新架构及其名称；gate geometry 能否成为优先操作语言；
- scientific distinctiveness = NOT ESTABLISHED；fusion lane PAUSED；third fusion domain = NO；BCTB T2 = HOLD；GRG v0.4 = NOT AUTOMATIC；further owner cleanup = PAUSED BY DEFAULT；
- 2026-09-24 作者排序（先优化 Spine，再处理其他 canonical owner）的执行仍未启动。
