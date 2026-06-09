---
id: SRT-PAPER-BEFORE-OBJECTS-SELECTION-REALISM
title: "对象之前：选择实在论与确定性的奠基"
title_en: "Before Objects: Selection Realism and the Grounding of Determinacy"
status: working_draft_v0_5
canonical: false
layer: philosophy_bridge
epistemic_layer: bridge
claim_mode: paper_draft
date: 2026-06-09
revision: v0_5
dependency:
  - Philosophy/SRT_Philosophy_Foundations_CompactCore.md
  - Philosophy/SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md
  - Philosophy/SRT_Philosophy_Tradition_Comparison_PH_SS.md
  - Philosophy/SRT_Philosophy_Hardening_TODO.md
  - 01_Source_Intuition/BOOK/BOOK_ARCHITECTURE_MAP_2026-06-03.md
  - 01_Source_Intuition/BOOK/BOOK_CORE_PROPOSITIONS_2026-05-30.md
machine_summary: >
  Working draft (v0.2) of the first academic-entry philosophy paper for SRT. It defends
  selection realism as a self-limiting alternative to object-first ontology. v0.2 responds
  to an R&R-level review: (1) determinacy is split into levels D1-D5 and the target is
  locked to object-style determinacy (D1+D2+D4); (2) the regress (stage A) is downgraded
  from a deductive defeat of naturalness realism to an explanatory-debt argument, while the
  bold thesis "determinacy is not fundamental" is retained as the defeasible output of the
  stage-B abduction; (3) L0 is given a single primary model (comparative-topological:
  non-uniformity over cut-space), with a terrain-gradient analogy and a contrastive
  complex-plane foil; (4) selection is given minimal conditions S1-S4 and a unified
  definition; (5) manifestational priority is anchored as constitutive dependence (primary)
  with grounding as optional strengthening; (6) Sider/Lewis engaged via the weaker critique
  (dispersed vs unified explanation), Hirsch/Carnap via a dedicated "anchoring cost is not
  merely pragmatic" subsection, Barad via one strongest difference; (7) reality-strength is
  recast as four dimensions with E1-E4 as typical combinations, handling unobserved facts,
  stable ideology, scientific revolution, and mathematics; (8) the worked example adds
  disease classification alongside the cup. Every strong claim carries a withdrawal
  condition. v0.2.1 refinement pass adds a semi-formal L0 model (cut-space C with R/S/H
  profiles, guardrailed so C is not a determinate domain), a D5-vs-reality-strength
  disambiguation, and stage-B abduction gating on "misplaces foundation" claims.
  Not canonical; does not modify canonical files.
changelog_v0_5: >
  vs v0.4 (literature pass, third-review priority 5): added author-date citations for the
  positions actually engaged — Sider 2011 and Lewis 1983 (§2.4), Hirsch 2011 and Carnap 1950
  (§2.5), Barad 2007 with page anchors for phenomena (33, 139), apparatus (140-148), agential
  cut (140) and agential separability (175) (§5.1), Boyd 1991/1999, Khalidi 2013, Haslanger
  2012 (§6.2), and the two micro-case sources Marshall & Warren 1984 / Nobel 2005 and APA 2013
  (DSM-5) (§6.2); added a selected References section. Citations were web-verified, not
  fabricated; final pinpoint page-proofing of Barad remains a copy-edit task.
changelog_v0_4: >
  vs v0.3 (third-round review, verdict "moderate revision then submittable"): fixed the
  same-type-determinate definition to use role-applicability, explicitly disambiguated from
  D3, preventing D3 reflux into stage A (§3.1); rebuilt the §3.3 comparative table into five
  rows (givenness, scale-relativity, intervention-collapse, inheritance-lag, cross-operator
  divergence) with a failure-condition column, and concretized the co-variation prediction
  into the high-R3 vs low-R3 revision pattern; added the one-sentence formal definition of
  counterfactual-differential objectivity plus the relata/truthmaker reply (c/c' are
  operational differential paths, truthmaker is L0 non-neutrality) (§3.6); added the
  non-circularity / explanatory-interlock clarification for possible intervention (§4.3);
  committed to the weak (constitutive-explanation) route on grounding, with grounding only as
  an optional footnote articulation (§3.5); added two concrete disease micro-cases (peptic
  ulcer / H. pylori as high-R3; Asperger's -> ASD/DSM-5 as low-R3) instantiating the
  co-variation prediction (§6.2). Specific page-level citations and the five-section
  submission version remain TODO.
changelog_v0_3: >
  vs v0.2.1 (second-round review): added §2.4 theoretical-virtue criteria C1-C6; defined
  "same-type determinate item" (3.1 2''); added a comparative argument table in §3.3 (SRT
  vs naturalness vs deflationism per phenomenon) with the "unification is a virtue only when
  it yields differential predictions (C2->C4)" argument; added §3.6 L0 objection battery
  (determinization / vacuity / modal-base) with the counterfactual-differential-objectivity
  formula; split resistance into three types and added the operator-transcendent middle
  formula (§4.2); specified the modal basis of "possible intervention" as the counterfactual
  operational space relative to L0/L2 (§4.3) and softened reality-strength wording; added a
  D3-status clarification (§2.0); promoted disease classification to the primary worked
  example with position-level contrasts to HPC/Khalidi/Haslanger/medical-pragmatism and
  explicit failure conditions (§6.2); deepened Barad to position-level text engagement (§5.1).
  Specific page citations remain TODO.
changelog_v0_2: >
  vs v0.1: added determinacy levels (D1-D5) and target lock; rewrote §3.1 as explanatory
  debt; selected comparative-topological model for L0 + terrain analogy + complex-plane foil;
  added selection minimal conditions S1-S4; swapped manifestational priority to
  constitutive-dependence-primary; weaker-critique-primary for Sider; new §4.4 (anchoring
  cost not merely pragmatic); multidimensional reality-strength + 4 boundary cases; disease
  classification worked example; softened "mainstream default", restricted the truth claim,
  reality-strength != degrees of being; expanded TODO.
---

# 对象之前：选择实在论与确定性的奠基

**Before Objects: Selection Realism and the Grounding of Determinacy**

> **状态**：working draft v0.5。SRT 的第一篇学院入口论文草稿，非定稿、非 canonical，不替代 Core / Core_Law / Philosophy 护栏文件的定义。核心术语（`L_0/L_1/L_2`、`G_hat_theta`、`Psi_f`、`d-value`）的权威定义仍在 canonical 文件中；本文以散文方式使用其哲学读法。投稿版（去 frontmatter、压成五节、统一语言）将另出，见文末 TODO。

---

## 摘要

本文为对象优先本体论（object-first ontology）提出一个自限的替代入口：**选择实在论（selection realism）**。其核心主张是，确定性（determinacy）不是本体论地板，而是受约束选择——切割（cutting）、锚定（anchoring）、稳定（stabilization）——之条件的被奠基结果；选择条件相对于确定存在具有**显现优先性（manifestational priority）**，本文将其主读法安置为**构成性依赖（constitutive dependence）**，grounding 作为可选的强化读法。

为降低论证负担，本文先把"确定性"分层（边界 D1、同一性 D2、适用 D3、实践承重 D4、本体强度 D5），并把核心靶心锁定为**对象式确定性（D1+D2+D4 的结合）**。论证分两阶段：阶段 A 是一个弱超验后退论证，得到的是较弱但稳固的结论——对象优先本体论欠一笔关于确定性条件的**解释债**；阶段 B 是一个最佳解释推断（可废止），论证奠基条件最好被理解为受约束的可选择性，而非 Sider/Lewis 式唯一自然关节，也非 Hirsch/Carnap 式框架内约定。由此 SRT 被定位为唯一关节实在论与紧缩论之间**有纪律的中道**。为避免唯心论与相对主义，本文把现实强度刻画为四个维度（显现稳定、跨 operator 对齐、干预抵抗、继承硬化），E1–E4 作为典型组合而非线性阶梯，其中干预抵抗取倾向性判据。本文将 SRT 与 Barad 的 agential realism、结构实在论、过程哲学与康德区分，并为每个强主张附以撤回条件与经验风险刻画（杯子与疾病分类两个 worked example）。结论不主张 SRT 整体成立，而主张它标识出一个先于对象优先本体论的真问题，并提供了一个有纪律的 selection-first 解答。

**关键词**：选择实在论；层级实在论；对象优先本体论；显现优先性；构成性依赖；确定性；现实强度；非还原验证；反相对主义

## Abstract

This paper proposes a self-limiting alternative to object-first ontology: *selection realism*. Its core claim is that determinacy is not the ontological floor but a grounded result of conditions of constrained selection—cutting, anchoring, stabilization. Selection conditions are *manifestationally prior* to determinate existence; this paper anchors that priority primarily as *constitutive dependence*, with metaphysical grounding retained as an optional strengthening. To lower the argumentative burden, determinacy is split into levels (boundary D1, identity D2, applicability D3, practical load-bearing D4, ontological strength D5), and the target is locked to *object-style determinacy* (the combination D1+D2+D4). The argument has two stages: (A) a weak transcendental regress that yields the modest but secure conclusion that object-first ontology owes an *explanatory debt* concerning the conditions of determinacy; and (B) a defeasible inference to the best explanation that these conditions are best understood as constrained selectability rather than unique natural joints (Sider/Lewis) or framework-internal convention (Hirsch/Carnap). SRT is thereby located as the disciplined middle of a Sider / deflationism / SRT triangle. To avoid idealism and relativism, reality-strength is recast as four dimensions (manifestational stability, cross-operator alignment, intervention-resistance, inheritance/hardening), with E1–E4 as typical combinations rather than a linear ladder, and intervention-resistance read dispositionally. Selection realism is distinguished from Barad's agential realism, ontic structural realism, process philosophy, and Kant. Every strong claim is paired with a withdrawal condition and an account of empirical risk (the cup and disease-classification worked examples). The paper does not claim that the framework is established; it claims to identify a genuine problem prior to object-first ontology and to offer a disciplined selection-first answer.

**Keywords**: selection realism; layered realism; object-first ontology; manifestational priority; constitutive dependence; determinacy; reality-strength; non-reductive validation; anti-relativism

---

## §1　引言：为什么要在对象之前开始

你伸手拿起桌上的杯子。但"杯子"并不只是一团裸物理刺激：它已经带有边界、可抓取性、用途、语言上的稳定性与重复识别的条件——它已经是一个**确定项**。世界几乎总是这样到来：像是已经在那里，由一件件已经完成、已经分好界限的东西组成，我们随后才进入其中去感知、命名、评价、行动。这种"已经在那里"的给定感如此稳固，以至于哲学的多数追问都从它之后开始：世界是否真实？主体是否自由？价值是否客观？制度是否正当？

但这些问题都来得**太晚**。它们各自预设：对象、主体、价值、秩序已经稳定地在那里，剩下的只是判定其性质。一个更早的、被默认跳过的问题是：**某物究竟如何成为确定的、对象般的、有边界的，从而可供随后的感知与选择去把握？** 在追问"对象是什么"之前，应先追问"个体化（individuation）如何被奠基"。

本文围绕一个主张展开，并刻意把它收窄到可被独立评估的尺度。为避免承重词含混，本文先把"确定性"分层（§2.0），再把靶心锁定为**对象式确定性**。在此前提下，本文的主张是：

> **对象式确定性不应被对象优先本体论无解释地预设为本体论起点；它更适合被理解为受约束选择——切割、锚定、稳定——之条件的被奠基结果。**

这一主张，我们称之为**选择实在论（selection realism）**。它的承重词是：**选择条件相对于确定存在具有显现优先性（manifestational priority）**——不是时间在先（没有任何选择者先于世界把世界选出来），也不仅是认识在先（不只是"我们得借选择来解释对象"），而是**构成性依赖意义上的在先**（§3.5 给出安置，并保留 grounding 作为可选强化）。

本文也保留一个更强的版本——**确定性一般地不是本体论地板**——但明确把它作为阶段 B 溯因推断的**可废止输出**，而非阶段 A 的演绎定理（§3）。

需要立刻划清四条边界，因为本主张极易被误读：

- 其一，**这不是主观唯心论**。SRT 不说"心灵创造世界"。可被建构的只是解释性的切分；不可被免除的是锚定的代价——一个无法在干预、重复与跨 operator 对齐下存活的切分，至多是局部显现。Construction has cost。
- 其二，**这不是相对主义**。现实有**层级强度**（§4.3）：梦与幻觉、习惯与记忆、公共制度、物理律，并不同样真实。就确定对象性而言，客观性表现为阻力与跨 operator 校正下的稳定对齐。
- 其三，**这不预设隐藏世界**。承担奠基功能的前对象条件域（本文记作 `L_0`）不是躲在现象背后的对象库，也不是康德式不可知的 noumenon，而只是 cut-space 上的非中立性（§3.2）。
- 其四，**这不声称解释一切**。本文不处理价值、主体、意识、AI、政治；它们只在结论作为该地板**打开**的方向出现。本文为自身的每个强主张附上撤回条件（§6）。

对象优先仍是许多理论与日常本体论的默认入口（尽管当代形而上学内部已有事件本体论、事实本体论、结构实在论、过程哲学、trope 理论、bundle theory 等反对象基础性路线）。本文将先与已有的反对象基础性火力线并肩（§2），再指出真正最深的预设并不在"对象是否基础"，而在"确定性是否被给定"。

**全文结构**。§2 分层界定确定性、精确界定对象优先本体论及其真正靶心，并处理来自自然性实在论与紧缩论的两个相反方向的反吸收，形成三角定位。§3 给出两段式奠基论证（阶段 A 解释债 + 阶段 B 溯因），固定 `L_0` 的主模型，并回应"选择需要选择者"。§4 正面刻画奠基层——选择的最小条件与三相位、反唯心论的过滤—阻力二象与实在论内核、多维现实强度、以及"锚定代价为何不只是 pragmatic cost"。§5 把 SRT 与最近邻——Barad、OSR、过程哲学、康德——逐一切割。§6 把撤回条件确立为方法论纪律，给出经验风险与两个 worked example，并收束于"对象之前的问题"。

---

## §2　确定性、对象优先本体论及其真正靶心

### §2.0　确定性的分层与本文靶心

"确定性"在不同语境承担多种含义，混用会让读者不清楚论文到底针对 metaphysical determinacy、individuation、objecthood、semantic determinacy、phenomenological givenness 还是 practical stability。本文先分层：

- **D1 边界确定性**：某物与非某物之间有可操作区分。
- **D2 同一性确定性**：某物可在变化中被追踪为同一项。
- **D3 适用确定性**：某概念、谓词或分类可稳定适用。
- **D4 实践确定性**：某项能在行动、干预、修复、预测中稳定承重。
- **D5 本体确定性**：某项具有足够现实强度，可作为后续选择的条件。

**本文核心论证针对"对象式确定性"，即 D1+D2+D4 的结合**——边界、同一性与实践承重性的合取。这是对象优先本体论无解释地设为地板的东西。更强的"一切确定性（含 D3/D5）皆非基础"的版本不作为主论证前提，只在阶段 B 的溯因结论与 §6.3 中作为受支撑的延伸出现。如此可显著降低论证负担：本文不必一开始就击败一切关于基础确定项的立场，只需表明对象式确定性需要解释，且 SRT 的解释更好。

须特别强调以防一个混淆：**D5（本体确定性）不是本文主靶心，只是后续扩展层（§6.4）；本文主论证只处理 D1+D2+D4**。因此本文是**用现实强度（§4.3 的 R1–R4）解释对象式确定性，而非用确定性定义现实强度**——reality-strength 刻画的是 determinate anchoring 的强度，D5 的本体确定性留作扩展、不参与主论证。两者不在同一解释方向上循环。

**D3（适用确定性）的地位**：D3 也不进入主论证的奠基前提，但它在案例中频繁出现（语言标签、诊断谓词的适用与修订）。原因是 **D3 是 D1+D2+D4 稳定后的常见表达层，并作为 `L_2` 继承的反馈机制回流**——谓词的稳定适用既是对象式确定性稳定的结果，又反过来预裁剪后续切割。故 §6.2 案例依赖 D3 不与"主靶心是 D1+D2+D4"冲突：D3 在此是表达与反馈层，不是奠基前提。

### §2.1　对象优先本体论的定义

**对象优先本体论（Object-First Ontology）** =df 主张实在的基本家具是确定个体（对象）之论域、且满足：(O1) 对象基础性——确定对象本体论上基本，事件／过程／事实／视角都用对象作 relata 分析；(O2) 个体化的给定性——对象预先地、独立于任何选择／视角／操作，就已带有边界与同一性条件；(O3) 主体后入——主体、知觉、价值、语言、框架在对象之后进入，作用于已被个体化的论域。

### §2.2　对 (O1) 的批判：与已有火力线并肩

(O1) 至今是许多理论与日常本体论的默认入口（量化逻辑把论域设为对象集，新亚里士多德实体论以实体为先），但已被三条独立压力线围攻，SRT 接入之：

1. **组合与个体化的不确定性**。特殊组合问题（van Inwagen, *Material Beings*）与"多的问题"（Unger）显示：哪些对象存在、一个对象到哪为止，无法被非任意地固定。
2. **无关系之 relata 的可疑性**（OSR）。Ladyman & French：物理学交付的是结构，"承载内在本性的对象"在认识上闲置、在形而上学上可疑。
3. **个体化的尺度／概念相对性**。Putnam 的概念相对性与 Hirsch 的 quantifier variance：算作"一个对象"依赖于所采的切分方案。

SRT 的自有增量：即便让步承认对象，(O1) 也无法解释**给定感的产生**——除了 reification 或 reduction，它没有第三条路。这是从 (O1)-批判通向 (O2)-批判的桥。

### §2.3　反 (O1) 阵营的两组与真正的靶心

反对 (O1) 的当代立场分两组。**第一组**（OSR、trope 理论、Putnam/Hirsch 式概念相对性）削弱对象基础性，却仍让某个确定项在新层级承担地板功能——结构事实、trope、或框架内对象被当作预先确定的，故实际保留 (O2)。**第二组**（Barad、部分过程哲学）更进一步，也否认确定性是给定的，但未充分说明切割如何受约束、被排序与纠错、并沉积为可继承的现实厚度。

> **战略定位**：SRT 的真正靶心由此从"什么是基础"推进到"**对象式确定性如何被奠基**"。"对象优先"作入口标签，"Before Objects" 在正文兑现为 "before determinate individuation"。但这一推进面对两个相反方向的反吸收，必须正面处理。

### §2.4　自然性反吸收（Sider / Lewis）

最强的反吸收来自自然性实在论。Sider（2011，*Writing the Book of the World*）主张实在具有一个被特别标举的**结构**（structure），并把它设为一个原始的、跨范畴的概念——是 Lewis（1983，"New Work for a Theory of Universals"，*AJP* 61: 343–377）"perfectly natural properties"在关节处切分世界（carving at the joints）之观念的跨范畴推广。须先做一处区分：**自然性关于基础结构的唯一性，不直接等于普通对象切分的唯一性**——Sider 的 privileged structure 不直接给出唯一的普通对象论域，Lewis 的 perfectly natural properties 也不必推出唯一的日常对象切分。

因此本文主打**较弱批评**：自然性实在论可以承认高层／普通／社会／功能对象的尺度相对性，把它们交给派生结构、reference magnetism、语义或实践——但这恰恰意味着关于对象式确定性的解释被**分散到物理、语义、心理、实践多层**；SRT 提供的是**统一的 selection-stabilization 账目**。这是一个理论选择标准上的比较（统一性、原始负担、解释范围），而非独断的反驳：SRT does not refute naturalness realism by demanding an explanation it refuses to give; rather, it offers an alternative with a lower primitive burden and greater explanatory reach regarding scale-relative individuation, givenness, stabilization, and inheritance.

**较强批评**（自然性即便加派生层也无法解释 determinacy 作为 determinacy 的生成，因为总要在某处预设已确定 joints）更有锋芒但更难证，**留作未来工作**，不作本文承重。

**本文采用的理论选择准则（供 §3.3 的 IBE 使用）**。为使"统一优于分散"不沦为审美偏好，本文预先固定六条比较准则，并在 §3.3 逐项落地：(C1) **原始负担**——预设多少未经解释的基础项；(C2) **解释统一性**——是否用同一机制覆盖多现象，且统一带来新的可检验后承；(C3) **解释范围**——覆盖给定感、尺度相对性、稳定、继承多少；(C4) **反事实/差分预测**——是否预测可观察的差异（而非事后追认）；(C5) **路径依赖处理**——能否解释滞后与历史沉积；(C6) **跨 operator 校正处理**——能否解释多 operator 间的对齐与分歧模式。关键原则：**统一性只有在它产生差分预测（C2→C4）时才算理论德性，而非仅凭简洁**——§3.3 据此论证 SRT 的统一不是省事，而是因为这些现象共享同一结构（cut–anchor–stabilize–inherit–pre-trim）并因此被同一组反事实绑定。

### §2.5　紧缩论反吸收（Hirsch / Carnap）

相反方向的反吸收来自紧缩论。Hirsch（2011，*Quantifier Variance and Realism*）的 quantifier variance 与 Carnap（1950，"Empiricism, Semantics, and Ontology"，*Revue Internationale de Philosophie* 4: 20–40）的内/外问题区分会说：没有关于"the 切分"的深层事实，选定语言框架、框架内成立即可，于是"确定性如何被奠基"是伪问题。

SRT 的回应须避免把紧缩论读成"否认一切事实差异"。SRT does not deny that deflationary frameworks can state internal truths. Its objection is that the cost of adopting, maintaining, shifting, repairing, or abandoning a cut is not itself exhausted by framework-internal truth conditions.（SRT 不否认紧缩框架能陈述其内部真值；它反对的是：一个切分被**采用、维持、转移、修复或放弃的代价**，不能被框架内部真值条件穷尽。）这一回应的关键预设——锚定代价不只是外在 pragmatic cost，而是确定项成立的构成条件——将在 §4.4 专门论证。

### §2.6　三角定位

由此 SRT 在形而上学地图上占据一个确定坐标：

- **Sider / Lewis**：存在唯一的、操作者无关的自然切分（关于基础结构）。
- **Hirsch / Carnap**：切分之争是框架/语言问题，无深层事实。
- **SRT**：无唯一预给的真切分，但切分的**阻力、稳定性与现实强度有事实**。

SRT 是二者之间**有纪律的中道**：对紧缩论而言它是实质的（切分差异是事实），对唯一关节实在论而言它是多元且 operator 相对的（无唯一真切分）。

---

## §3　对象式确定性的奠基：两段式论证

### §3.0　两个阶段及其不同力度

论证分两阶段，力度不同，刻意分开。**阶段 A**（弱超验/后退）只得到一个较弱但稳固的结论：对象优先本体论欠一笔关于确定性条件的**解释债（explanatory debt）**。**阶段 B**（最佳解释推断，可废止）论证这些条件最好被理解为受约束的可选择性。SRT 的本体论锋芒由阶段 B 挣得，而非伪装成阶段 A 的定理——这正是"付费而非降调"：大胆主张保留，但其支撑明确标为溯因且可废止。

### §3.1　阶段 A：后退论证（得到"解释债"，不演绎击败自然性）

- **(1)** 任一对象式确定项 *x* 之为确定（具 D1 边界 + D2 同一性 + D4 实践承重），需要个体化条件：可分辨边界、同一性条件、以及一个使"这一个/非这一个"被固定的尺度—视角。
- **(2)** 对于任何**非原始、非自明**的确定项 *x*，其确定性不能仅由另一个**同型的**已确定项 *y* 来解释；否则解释只是把确定性从 *x* 转移到 *y*，而未偿付被解释项本身。
- **(2′)** 这一点是**范畴不变的**：把 *y* 改述为关系、结构、性质或 trope 并不改变情形，因为这些项同样只有具备可区分性与适用边界才是确定的。故压力针对的是**确定性本身**，而非对象性。
- **(2″)** "同型确定项"的界定：任一其**解释角色本身已预设争议中的那种个体化、边界、同一性与（角色层的）可适用条件**的 explanans，即为同型（*a same-type determinate item is any explanans whose explanatory role already presupposes the individuated boundary, identity, and role-applicability conditions of the sort at issue*）。**澄清以防 D3 回流**：此处的 applicability **不是**作为主靶心被排除的 D3 语义适用确定性，而仅是"一个解释项要能承担其解释角色所需的最低可适用性（role-applicability）"；它不把 D3 纳入阶段 A 的奠基前提。故对手不能靠把 explanans 改称"结构/性质/关系/trope"脱身——只要其承担解释所凭借的确定性正是被解释项所需的那种，它就是同型，解释债未偿。一个真正异型的 explanans 必须**不**预设此种确定性——这正是 §3.2 的 `L_0` 所要充当的角色。
- **(3)** 因此，对象优先本体论若把对象式确定性设为无须解释的起点，就**欠缺一个关于确定性条件的解释**。这就是**解释债**。

> 重要限定：阶段 A **不**演绎地推出"确定性不是基础的"。一个自然性实在论者可以主张存在**基础的、原始的、自带个体化条件的**确定项（自然关节、基础实体或本质、确定结构事实），从而声称在某处偿清解释债。阶段 A 不以"否则后退"直接驳倒此立场——那会乞题。阶段 A 只确立：**要么承认基础原始确定项（并承担其代价），要么解释债悬空。** 哪一条更可取，交给阶段 B 的解释力比较。
>
> 脚注（读法）：本段的依赖关系主读为**构成性依赖**；grounding 作为可选强化（见 §3.5）。

### §3.2　后退的终止与 `L_0` 的主模型：比较拓扑（comparative-topological）

若不诉诸基础原始确定项，后退终止于何处？本文为 `L_0` 选定一个**主解释模型并不再滑动**：**比较拓扑模型**。`L_0` 不包含任何确定项（对象/性质/结构/关系），只包含 **cut-space 中的非均匀性**——某些切割比另一些更可稳定、更低阻力、更可继承。非中立性因此不是一个被个体化的性质，而是**可能切割之上的一个比较序（a comparative order over possible cuts）**：它使不同切割并非等价，却不预先划定任何确定区域。须区分两个谓词：**"确定的"** = 具个体化边界 + 同一性条件；**"非中立的"** = 具足以使切割非等价的比较不均匀性。`L_0` 非中立而未被个体化（sub-determinate but not null）。

两难的拆解：`L_0` 既非完全确定（不含确定项，后退不重启），亦非完全空无（含非平凡比较序，有物可供约束）。"比较序本身是否已经确定？"——被排序的是可能切割，而排序所依赖的不均匀性是**功能性的**：它只在"使某些切割更易稳定"这一可显现的差别中存在，而不作为独立确定结构存在；它的确定化恰恰是切割—锚定—稳定的成就（§4）。

**类比与其限度**。一个会**误导**的类比是复平面：虚轴上的量不在实轴上，却影响后续变换与投影。它的误导恰在于——复平面是一个**完全确定的结构**（`i` 有精确同一性条件），而 `L_0` 不是；按此类比，`L_0` 会被读成"现象背后的第二条确定维度"，即 §5.4 拒绝的隐藏世界/noumenon。更贴切（同样仅启发性）的类比来自本文的**地形**语汇：一片尚未被分出流域的**坡度场**——坡度使某些分水方式更稳定、代价更低，但坡度本身不是一组已划定的流域；流域（确定对象）不是被给定的，是坡度（非中立性）使某些划分成为低阻力的成就。地形类比的限度在于：真实地形已是确定的物理结构，而 `L_0` 不是——它只是"使切割非等价"的比较不均匀性本身。

**一个半形式的展示（representational device, not a determinate-domain claim）**。为使 `L_0` 更可审查，给出一个最小半形式模型（仅作展示，不主张 C 是已确定集合）：

- cut-space **C**：可能差异化的空间（the space of possible differentiations），不预设为已个体化的对象集；
- 候选切割 *c₁, c₂, c₃, … ∈ C*；
- 阻力剖面 **R(c)**：切割 *c* 在干预/重复/跨 operator 对齐下遭遇的抵抗；
- 稳定倾向 **S(c)**：*c* 被锚定并退入背景的倾向；
- 继承倾向 **H(c)**：*c* 沉积为后续约束、预裁剪未来切割的倾向。

则 **`L_0` 不是 C 中的某个子集（不是对象集合），而是 R、S、H 在 C 上的非均匀性/比较剖面**——即 R/S/H 并非跨切割恒定，而这种不恒定使某些切割并非等价。两点护栏须随形式**一起**声明，否则记号会偷偷预设确定性：**(i)** C 不被主张为已确定的论域——它是可能差异化的空间，其元素 *c* 的确定性是锚定—稳定的成就，而非给定；半形式记号只是把"非均匀性"显示出来的表征手段，不是对一个预先确定域施加度量。**(ii)** R/S/H 是功能性差分而非已确定结构——它们只在"某些切割更易稳定"这一可显现差别中存在；把它们读成 C 上的确定函数是一种表征理想化，其本体承诺仅为"比较序非平凡（the comparative order is non-trivial）"。

**撤回条件**：若"非中立的比较序而不含确定项"被证不自洽，则 SRT 退至 operator-relative-all-the-way 的较弱（较 Kant 的）立场。

### §3.3　阶段 B：溯因到受约束的可选择性

阶段 A 留下解释债与一个开放问题：偿付确定性条件的最佳方式是什么？三个在场候选：(i) Sider/Lewis 的唯一操作者无关自然关节；(ii) Hirsch/Carnap 的框架内约定；(iii) SRT 的受约束可选择性——operator 相对的、支付阻力、被稳定与继承的切割。

主张 (iii) 是**最佳解释**，**可废止**，依据是 (i)、(ii) 无法无余地承担的解释工作：

1. **给定感**：世界为何总像"已经对象化"地到来。唯一关节不解释显现与通达（把它分散给认知/语义）；约定论消解之，却无法解释为何某些切分昂贵、不稳。
2. **个体化的尺度/视角相对性**（杯/分子/餐具组合）：单一自然关节须判其余为派生并为其余另欠说明（解释分散）；可选择性原生地容纳这一相对性（统一解释）。
3. **切割—锚定—稳定的不对称**：为何某些切分持存、另一些消散。差异性稳定是**事实**（反约定论），却无须唯一真切分（反唯一关节）。
4. **现实强度的多维分级 + 继承**（§4.3）：分级的、路径依赖的稳定可被观察；唯一关节与约定论都不预测这种**多维组合 + 滞后**。

下表按 §2.4 的准则把**五项**解释工作逐项对比（非穷尽，旨在显示 SRT 的统一是 C2→C4 意义上的，而非审美）。每行附**失败条件**，使比较可被外审检验：

| 现象 | 自然性实在论（Sider/Lewis） | 紧缩论（Hirsch/Carnap） | SRT | SRT 的差分预测（C4） | SRT 的失败条件 |
|---|---|---|---|---|---|
| 给定感 | 外包给认知科学/语义磁性 | 消解为框架习惯 | cut 后的锚定退入背景 | 给定感强度随 `L_2` 沉积史可测变化（标签滞后于可供性） | 给定感与沉积史无相关 |
| 尺度/视角相对性 | 判为派生，另欠派生层说明 | 框架选择，无深层事实 | 多 operator 切割原生相对 | 切分分歧呈 R1–R4 依赖的模式 | 分歧模式与 R1–R4 无关、纯随机 |
| 干预崩解（差异稳定） | 诉诸因果/自然结构 | 诉诸实践便利 | 阻力 `Psi_f` 支付差异稳定 | 崩解模式可测且**框架无关** | 崩解随框架重命名而变 |
| 继承滞后（路径依赖） | 单一关节不预测滞后 | 约定不预测滞后 | `L_2` 硬化 | 修订留下**路径依赖**的代价重分配与滞后签名 | 修订无滞后、可自由重置 |
| 跨 operator 分歧/对齐 | 唯一关节预测趋同 | 框架内无跨框架事实 | R2 对齐 + R3 锚 | 对齐/分歧依 R3 强弱分层（高 R3 趋同，低 R3 制度相对） | 对齐/分歧与 R3 无关 |

**为何统一在此是德性而非审美**：对手当然可以接受"解释分散"，且分散本身并不丑陋。SRT 的论点更尖：这五项现象**经验上共变**——同一 cut 的给定感强度、尺度分歧模式、干预崩解、继承滞后与跨 operator 对齐是相互绑定、随同一 `L_2` 史共同移动的。**共变的可检验形式**（与 §6.2 对接）：当一个 cut 的 R3 高时，其分歧应随干预证据收敛、修订主要表现为**边界重绘与病例重判**；当 R3 低而 R2/R4 高时，同一 cut 的稳定主要由制度/继承承担，修订主要表现为**制度资格、身份叙事、标签与治疗路径的滞后重分配**。分层分工解释把这些现象指派给互不通约的解释域（认知科学、语义学、社会实践、因果结构），因而**不预测它们随 R3/`L_2` 共同移动**；SRT 用单一 cut–anchor–stabilize–inherit 结构**预测此共变**。统一性在此兑现为 C2→C4 的差分后承，故是理论德性而非简洁偏好。**撤回条件**：若该共变被证伪（诸项可相互独立变动、与 R3/`L_2` 无依赖），则统一论点失败，SRT 收窄。

故奠基条件最好被理解为受约束的可选择性。**撤回条件**：若自然性或约定能以同等或更低的原始负担、无余地复原给定感、尺度相对性、差异性稳定与继承，则 SRT 收窄。由此，更强版本"对象式确定性不是基础的（乃至确定性一般非基础）"作为本阶段的**可废止输出**成立，而非阶段 A 的演绎定理。

### §3.4　"选择需要选择者"反对

> 反对：若 *x* 的确定性奠基于"选择"，而选择需要一个进行切割的 operator，且 operator 是确定对象，则后退被偷偷重启。

回应三步：**(R1)** operator 不必是基础确定对象，而是一个约束剖面（constraint profile）；切割之"被操作"不蕴含预先给定的"切割者"。**(R2)** operators 本身被奠基：任何稳定 operator（主体、仪器）都是沉积的选择历史（`L_2`），故以 operator 解释 determinacy 非恶性循环，而是**自举（bootstrapping）**。**(R3)** 后退终止于 §3.2 的 cut-space 非中立性，而非第一对象，亦非隐藏世界（护栏 O-Phil-11）。"选择"在此为术语，其非施事刻画与最小条件见 §4.1。

### §3.5　输出命题与显现优先性的安置

> **(A 解释债)** 对象式确定性需要解释：它不能仅由同型确定项偿付。**(B 溯因)** 偿付它的最佳方式是受约束的可选择性。合起来：**选择条件相对于确定存在具有显现优先性**（*Selection conditions are manifestationally prior to determinate existence*）。**若阶段 B 溯因成立（if the stage-B abduction succeeds）**，对象/确定性优先本体论就把一个被奠基的成果错置为基础；若溯因被废止，则本主张收窄为 §6.3 的防御版（对象式确定性至少欠一笔解释债）。这是有意的语气纪律：凡"错置基础"一类强句皆挂在溯因前件之下，不作无条件断言。

**显现优先性的安置（弱化路线）**：本文的真正贡献在 selection-first determinacy，不在 grounding theory 本身；为降低篇幅与审稿风险，本文采取**弱化路线**——把 manifestational priority 主张为**构成性解释（constitutive explanation）**：确定项之所以能作为确定项出现并承重，依赖于选择条件的切割、锚定与稳定。本文**不使用强 grounding 语言、不承诺**其形式特征（非对称性、传递性、非循环性、partial/full ground 之分）。这一克制是有理由的：`L_2` 稳定、历史沉积与自举模型含反馈与滞后结构，可能与标准 grounding 的非循环/非对称要求张力。**脚注（可选强化读法）**：若读者接受 grounding，本文的构成性解释可被视为一种 grounding-friendly 的表述，其与 Fine / Schaffer / Rosen / Audi / Correia 的完整对接列为**可选的**未来工作，而非本文承重。

### §3.6　`L_0` 反对意见集束（objection battery）

`L_0` 是全文最深的哲学风险，集中处理三类反对。

**(O-a) 确定化反对**：比较序若能排序，岂非已是确定结构，后退重启？回应：须区分**对象式确定性**（个体化边界 + 同一性条件）与**反事实差分客观性**（counterfactual-differential objectivity）。`L_0` 不具前者：它不含任何可被追踪、可被再识别为同一项的个体。它只具后者：存在反事实差别——若切割 *c* 而非 *c′*，则后续稳定/继承代价不同。排序不预设被排序项已被个体化，正如一片坡度场的"更陡/更缓"不预设流域已被划出。故 `L_0` **不是结构，而是结构化可能性的非均匀性**；它的客观性是反事实差分的，不是对象式的——这正是它不重启后退的原因。**形式化一句**：一个亚确定条件具有**反事实差分客观性**，当且仅当不同的可允许操作会生成不等价的稳定与继承剖面，即便在基底层尚无确定 relata 被个体化（*a sub-determinate condition has counterfactual-differential objectivity iff different admissible operations would generate non-equivalent stabilization and inheritance profiles, even though no determinate relata are yet individuated at the base level*）。**relata 与 truthmaker 反对**：在 cut 被确定前，"若切割 *c* 而非 *c′*"的 relata 如何指定？回应：*c*、*c′* **不是对象式项**，而是**操作性差分路径**（operational differential paths）；该反事实不是关于两个已确定对象的比较，而是关于两种操作剖面的稳定代价比较。其 truthmaker 不是一对已个体化的 relata，而是 `L_0` 的非中立性本身——它使两条操作路径的稳定/继承代价不等。若坚持反事实必须有对象式 relata 作 truthmaker，则 `L_0` 退为解释工具而非本体条件、SRT 收窄为 interface 读法（§6.1）；本文主张操作剖面足以充当 truthmaker，故不必收窄。

**(O-b) 空洞性反对**：若比较序不是确定结构，它如何能**约束**任何东西？回应：约束不需要约束者是确定对象。`L_0` 通过使某些切割的锚定/继承代价系统性更低来约束——这种约束在"某些 cut 在干预下崩解、某些持存"的可显现差别中兑现（§4.4）。一个无任何非均匀性的 cut-space 将使一切切割等代价，于是不会有差异稳定、不会有给定感、不会有现实强度分级；我们恰恰观察到这些，故 `L_0` 非空洞。空洞性反对与确定化反对形成钳形：本文立场恰在二者之间——足以约束（非空洞），不足以个体化（非确定）。

**(O-c) 模态基底反对**：可能切割空间 C 的"可能性"由什么给出？若由自然律给出，则回到物理主义/自然性基底；若由 operator 能力给出，则失去 operator 独立性。回应：本文把 C 的模态读为**相对于 `L_0` 非中立性与已沉积 `L_2` 的反事实操作空间**，而非（i）当前 operator 的实际技术能力，亦非（ii）纯逻辑可想象性，亦非（iii）完整自然律的先行给定。这与 §4.3 对"可能干预"的刻画同源：模态基底是 `L_0` 的非均匀性本身——它已足以使某些切割反事实地更可稳定，而无须先有一部完成的自然律之书。**代价与撤回**：这要求 `L_0` 承担一个最小模态角色（支撑反事实差别）；若可证该模态角色必须由一个完整的确定律结构提供，则 SRT 退回承认一个自然性模态基底、相应收窄为 interface 读法（§6.1）。

---

## §4　选择实在论：奠基层的最小刻画

§3 留下解释债与一个方向：对象式确定性最好被理解为受约束可选择性的成果。本节把正面刻画补足到四件事所需的程度——给"选择"以最小条件与定义、堵住唯心论、给现实强度以多维刻画、并论证锚定代价的构成性。机制始终系于奠基主张：以下过程是确定性*据以成立*的构成性条件，而非已确定之物的因果史。

### §4.1　选择的定义、最小条件与三相位

选择在此不指主体面对菜单的挑选。**本文所谓"选择"指约束下的差异实现（differential actualization under constraint），而非一个已被个体化的主体的意向性挑选**（Selection here means differential actualization under constraint, not intentional choosing by an already individuated agent）。统一定义：

> **Selection = constrained differential actualization whose phases are cut, anchor, and stabilize.**（选择 = 受约束的差异实现，其相位为切割、锚定、稳定。）

为防止"选择"过宽（否则任何因果筛选、信息压缩、演化、分类、制度沉积都成为选择，解释力反而下降），本文给出 SRT 意义上 selection 的**最小条件**。一个过程要算作 selection，至少需：

- **(S1)** 存在多个可实现但不等价的显现路径；
- **(S2)** 某些路径因阻力、代价、约束而更易稳定；
- **(S3)** 被实现的路径产生**可继承的**后续条件；
- **(S4)** 该后续条件反过来**预裁剪**未来的选择空间。

仅当 S1–S4 同时成立，过程才是"差异实现—锚定—继承—预裁剪"的结构，而非"仅仅发生了某种差异"。由此 selection 在 SRT 中是广布的，但**不是普遍的**——这避免了把一切发生都称为选择的泛化（与反泛心论一致）。

三相位：**切割（cut）**使"这一个"与"非这一个"分开并赋予可辨识的操作格式，同时是排除——被排除者作为后续摩擦改变未来代价分配。**锚定（anchor）**使一次显现获得地形位置：出现不等于留下，唯当它成为后续选择必须面对的条件时才获得现实重量。**稳定（stabilize）**使反复锚定退入背景，沉积为习惯、语言、规范、制度与模型。三者之间的非琐碎环节：锚定带来**不可逆性**（撤回可取消表面结果，不能取消已改变的地形），不可逆累积成**现实厚度**，厚度退入背景成为**秩序**，秩序又**预裁剪**后续选择。正是这条链使 selection-first 能说明对象式确定性如何实际生成并自我约束。

三层记号（散文使用）：**`L_0`** 是 cut-space 上的非中立比较序（§3.2）；**`L_1`** 是选择后的显现/锚定事件（非第二实体）；**`L_2`** 是稳定下来的选择历史（非自动正当）。

### §4.2　过滤—阻力二象与实在论内核

"确定性被奠基于选择"最危险的滑坡是被读成"心灵投射世界"。堵住它的是代价。operator（记作 `theta`，约束剖面）**过滤**；显现要**支付阻力**（记作 `Psi_f`）：可被建构的只是解释性切分，不可被免除的是锚定代价。`Psi_f` 在本文只取一种含义并标明层级——候选选择在预测、干预、重复与跨 operator 对齐下持续遭遇的抵抗（本体/信息几何层，不展开四层全表）。

实在论内核须精确声明：**SRT is realist about minimal non-neutrality and resistance in the sense that they are not created by, nor exhausted by, any given operator's projection. What is operator-relative is the determinate cut.**（SRT 对最低非中立性与阻力持实在论立场——它们既非由某个 operator 创造，亦不被某个 operator 的投射穷尽；operator 相对的是确定切分。）这比"operator-independent"更稳：不声称非中立性/阻力是脱离一切 operator 的现成结构（那会滑回 object-first），只声称无任何单个 operator 能创造或耗尽它们。

**三类阻力须分开，否则 `Psi_f` 过宽**：(i) 物理/干预阻力（破杯不能再饮）；(ii) 社会/制度阻力（制度对重新分类的抵抗）；(iii) 语义/实践阻力（概念修订的代价）。三者都是 resistance，但承担反相对主义功能的主要是 (i) 型 R3——唯有它的反事实约束不能由任何 operator 群体的协议自由重置。由此给出比"operator-independent"更精确、比"不被单个 operator 穷尽"更硬的中间公式：**Resistance is not operator-independent as a ready-made structure, but it is operator-transcendent in the limited sense that no actual or possible operator-profile can freely reset its comparative constraints.**（阻力不是作为现成结构而 operator 无关，但它是 operator 超越的——在这一有限意义上：没有任何现实或可能的 operator 剖面能自由重置其比较约束。）这堵住强社会建构论的回应（"由集体实践创造"）：集体 `L_2` 可以**移动**代价分配，却不能**自由重置** (i) 型 R3 的反事实约束；社会现实强度（R1/R2/R4 高）与物理阻力（R3）由此可分（§4.3、§6.2）。

故一族护栏：**construction has cost; stabilization requires resistance; alignment is not optional.** `Psi_f` 是反主观唯心论的核心护栏之一。

### §4.3　现实强度：四维刻画，E1–E4 作为典型组合

若被选择者皆真实，梦、幻觉、制度与物理律岂非同样真实？回应：**就确定对象性而言，现实强度表现为锚定稳定性的差异**（不是一般存在论上"存在有程度"）——并须把它刻画为**四个维度**，而非单一线性等级：

- **(R1) 显现稳定（manifestational stability）**：显现是否反复出现。
- **(R2) 跨 operator 对齐（operator alignment）**：是否可在多 operator、仪器、语境间对齐。
- **(R3) 干预抵抗（intervention-resistance）**：是否在干预下保持。
- **(R4) 继承硬化（inheritance/hardening）**：是否沉积为后续约束（路径依赖、滞后）。

E1–E4 是这些维度的**典型组合**，而非严格阶梯：E1 局部显现（仅 R1 低度，如梦/幻觉）；E2 稳定现实（R1 + 部分 R4，如习惯）；E3 跨 operator 现实（R1+R2+R4，如制度/公共事实）；E4 典范物理现实（四维皆高，且 R3 在可能干预下稳健，如物理律）。

须强调：**现实强度不是 being 的程度，而是 determinate anchoring 的强度**——避免触发"存在有程度"的争议。其中 R3 取**倾向性判据**：指结构在**可能的**干预、重复、测量与跨 operator 校正下的抵抗倾向，而非当前共识量；阻力本身真实而非建构（反唯心论锚），而把阻力切成某个确定结构仍是选择—稳定的成就；其倾向基底不是确定范畴结构，而是 `L_0` 的非中立性（这与 §3.2 一致）。E4 = dispositional robustness under possible intervention, not current consensus。

**"可能干预"的模态基础**。R3 取倾向性判据，必须说明其模态空间由什么给出，否则 R3 失去本体承重。本文的 possible intervention **不是**当前技术能力（否则无人观测事实失去独立 R3），**不是**纯逻辑可想象性（否则太弱、流于空泛可想象性），**也不是**对完整自然律的先行还原（否则 R3 坍回自然性基底）；而是**相对于 `L_0` 非中立性与已沉积 `L_2` 条件的反事实操作空间**（the counterfactual space of operations relative to `L_0` non-neutrality and sedimented `L_2`）。即：一个切分有高 R3，当且仅当在这一反事实操作空间内它稳健地抵抗。如此，R3 的模态既不还原为自然律、不还原为主体能力、也不空洞——它锚在 §3.6(O-c) 所辩护的 `L_0` 最小模态角色上。**避免循环的说明**：R3 依赖 possible intervention，possible intervention 依赖 `L_0`/`L_2`，而 `L_0` 的非中立性又通过不同操作的稳定代价显现——这不是恶性循环，而是**显式自举（explanatory interlock / 协同约束）**：possible intervention 不由实际 operator、亦不由纯逻辑可想象性定义，而是**由亚确定非中立性与已继承的稳定剖面共同约束的可允许反事实操作**（admissible counterfactual operations constrained jointly by sub-determinate non-neutrality and inherited stabilization profiles）。"jointly constrained" 不等于循环定义：它把模态空间**限制在可显现差分上**——R3 与 `L_0` 不是相互定义，而是在"可显现的稳定代价差别"这一**共同测度**上协同确定。若该协同被证只能化约为单向的自然律决定，则 R3 坍回自然性基底、SRT 收窄（§6.1）。

**四个边界案例**：(a) **无人观测的事实**——可有高 R3（可能干预下稳健），即便当前 R2 为零；"可能干预"不由当前 operator 的实际能力定义。(b) **稳定意识形态/神话**——可有高 R1/R2/R4（社会现实强度），但其"关于物理世界的真值声称"不因此为真：须区分社会现实强度与物理真值（§4.4、§6.2）。(c) **科学革命**——旧理论曾有高 R1/R2/R4 的**描述地位**（E3/E4 描述），但其试图切中的阻力结构（R3）可能并未真正达到；区分"理论稳定性"与"被切中的阻力稳定性"。(d) **数学/逻辑对象**——R2/R4 高而 R3（物理干预抵抗）不直接适用；E1–E4 的物理读法不直接套用于数学，其现实强度须另作刻画，列为范围限制。

于是，**就确定对象性而言**，客观性表现为在阻力与跨 operator 校正下的稳定对齐——本文不在此重定义真理一般，只主张确定对象性的客观性如此表现。不同 operator 可有不同切分，但并非同等有效；一个分类要获得更强客观性，须提升其 R1–R4。

### §4.4　锚定代价为何不只是 pragmatic cost

紧缩论者会承认锚定代价是事实，却把它归为心理/社会/实践/语义事实，与框架内真值并存而无须 selection realism。SRT 的反驳须证明：一个 cut 的稳定、继承与阻力，不只是"我们采用某语言框架时的外部代价"，而是"该 cut 能否成为确定现实项的**构成条件**"。

论证：若把锚定代价完全外部化为 pragmatic cost，则无法解释三件事——其一，为何某些 cut 在干预下崩解（破杯不能再饮），而这与我们如何称呼它无关；其二，为何代价分配呈现**路径依赖**（修补史改变后续同一性判断），而非随框架自由重置；其三，为何 R3 抵抗**独立于任何单个框架的选择**。这些不是"选用框架的不便"，而是"该 cut 作为确定项能否持续承重"的条件——即对象式确定性的构成条件，而非其外在伴随。故锚定代价进入本体论账目，而非仅 pragmatics。这正是 SRT 对 Carnap/Hirsch 的真正分歧所在。

---

## §5　定位：与最近邻的切割

本节不做综述，只切最近邻，回应"SRT 只是换名复述"。差异化压在 SRT 为切割提供的约束、稳定与继承账目上。

### §5.1　Barad 的 agential realism

Barad（*Meeting the Universe Halfway*）主张确定性由 **agential cut** 在 intra-action 中产生、现象（phenomena）是基本本体单位——表面上几乎是选择实在论的同义改写。本文**接受**其核心方向：确定性经切割而成立，边界并非预先给定。本文**重写**：把 agential cut 重述为支付 `Psi_f` 的受约束选择。

为避免不公并保持锋利，本文只保留**一条最强差异**：*Barad gives an ontology of cut-dependent phenomena; SRT adds a general account of how cuts acquire comparative resistance, cross-operator rankability, and inheritable reality-thickness.* Barad 的 cut 由具体物质装置（apparatus）施行，本已受约束；SRT 所加的不是"约束"本身，而是一个**跨装置、可排序的一般阻力度量 `Psi_f`** 及其沉积为可继承现实厚度（`L_2` 硬化）与多维现实强度的机制。方法路径亦不同：Barad 从量子物理诠释、测量实践与 onto-epistemology 出发；SRT 在不绑定任何特定物理诠释的前提下，把"确定性依赖切割"重构为一般性的构成性解释。

**三点正面交手**（页码依 Barad 2007，Duke 版）：**(1) 核心定义**——*phenomena* 是 intra-action 中诸 intra-acting agencies 的本体不可分性，为基本本体单位（Barad 2007: 33, 139）；*apparatus* 是物质—话语的边界生成实践（boundary-making practices，2007: 140–148）；*agential cut* 在现象内施行对固有本体不确定性的**偶然/局部消解**（a contingent resolution of the ontological indeterminacy within the phenomenon，2007: 140）；客观性则系于 *agential separability*——"现象内被施行的本体可分性 / exteriority-within-phenomena"（2007: 175）。**(2) 客观性的差别**——Barad 的客观性是**装置相对的**（apparatus-specific）：确定性对给定物质装置成立；SRT 增加的是**跨 operator 可排序性**（cross-operator rankability）与**可继承现实厚度**，即不同装置/operator 之间，切割的阻力可被比较与排序、并沉积为 `L_2` 硬化。Barad 给出"切割在装置内产生确定性"，SRT 给出"切割如何跨装置获得可比较的阻力与历史厚度"。**(3) `Psi_f` 是否可被 Barad 吸收**——本文判断不能无损吸收：`Psi_f` 要求一个跨装置、可排序的一般阻力度量，而 Barad 刻意把客观性绑定在具体装置内（这是其 onto-epistemology 的核心承诺）；引入跨装置可排序的 `Psi_f` 会改变其本体论结构（从装置相对客观性转向比较—继承客观性）。故 SRT 不是 agential realism 的换名，而是对其"装置相对"承诺的一处实质修改。

> 页码依 Barad 2007（Duke 版）；终稿校样时再核对 agential cut（140）与 phenomena（33, 139）的确切页位。

### §5.2　Ontic Structural Realism（Ladyman & Ross）

本文**接受** OSR 对对象基础性的削弱（结构优先）。**重写**：结构本身是稳定下来的选择成果（`L_2`），而非无须奠基的地板。OSR 仍保留 (O2)——把结构事实当作预先确定的；而 §3.1 的 (2′) 表明，即便把基础换成关系或结构，确定性问题也未消失。**增加**：结构如何变得确定、如何被个体化。分歧清晰：OSR 让结构在新层级承担地板功能，SRT 则连结构的确定性也奠基于受约束的可选择性。

### §5.3　过程哲学（Whitehead / Seibt）

**接受**：生成先于实体。**重写**：把 concrescence 式生成重述为带阈值与代价的受约束选择。**增加**：operator、`Psi_f`、撤回条件与可操作代理逻辑，把过程形而上学约束为可问责结构。与 §2.3 一致：部分过程哲学也否认 given determinacy，故分歧不在 (O2)，而在其常缺的阻力—代价纪律与解释形式。

### §5.4　康德

**接受**：经验有条件。**重写**：把固定先验范畴替换为动态 `theta` 约束，且 `theta` 本身是可修正、具身、历史地沉积的选择历史。**增加**：`Psi_f` 阻力使依赖成为构成性的；operator 自身也被奠基（R2）。最关键切割：`L_0` 与 noumenon 的区别——康德的物自体是被否定性刻画的现象背后之物或域（仍是某种对象/领域），而 `L_0` 不是对象，是 cut-space 的非中立性。SRT 没有不可知的 X 躲在现象之后，只有需支付代价的可选择性条件（护栏 O-Phil-11）。

> **脚注 H**：海德格尔的上手状态（Zuhandenheit）已挑战"孤立、现成对象优先"；但本文不分析此在的世界性或用具结构，而是追问确定性本身如何由受约束可选择性与稳定化奠基。
>
> **脚注 E**：Enactivism 与 Gibson 的 affordance 理论是重要近邻，同样拒绝被动的对象接收；但本文把问题从知觉—行动一般化到本体、社会与科学领域中的选择、锚定、稳定与现实强度。（若杯子案例留在正文，此两者须从脚注升入正文交手，见 TODO。）

---

## §6　自限的纪律 · 经验风险 · 结论

### §6.1　撤回条件作为方法论美德（self-limiting metaphysics）

SRT 为每个大胆句附上层级、代价、阈值、失败模式与撤回条件。这是论证纪律：一个无法说出"什么会让它收窄"的形而上学主张，不值得被当作主张对待。**主撤回条件**：若某种物理主义或自然性账目能**无余地**解释 manifestation、anchoring、first-person access、update-cost、给定感与差异性稳定，则 SRT 应从 meta-ontology 收窄为 interface / compression 框架。两点限定：其一，**This would be a narrowing of scope rather than a total refutation**（这构成适用范围的收窄，而非整体失败）；其二，"无余地"是理想极限，实践上以**可检验的中间里程碑**逼近（自然性账目能否在不引入 operator 相对性下复原个体化的尺度相对性？能否预测 `L_2` 硬化的滞后签名？），而非一次性二元判决。

### §6.2　非空洞性与两个 worked example

SRT 通过 proxy 操作化、结构性收敛与差分预测承担风险；三者皆缺则某主张被归为形而上学纲领或桥接假设，而非经验理论。

**入门直观例：杯子（warm-up）**。同一区域可被切为杯（功能）、陶瓷分子集合（微结构）、碎片堆（破损后）、餐具组合（社会—实践）。四条可操作预测：(i) 破损后语言标签"杯子"的保留慢于实践可供性的崩解（标签滞后于可供性）；(ii) 修补杯与微观结构近似的新制复制品在 `L_2` 历史上产生不同的同一性判断；(iii) 不同 operator 群体在"是否仍是同一个杯"上出现可测分歧，模式依使用史、修复史、情感锚定与制度背景而变；(iv) 当实践可供性、语言标签、物理连续性、社会承认相互**脱钩**时，SRT 预测**锚定代价的重新分配**，而自然性实在论与紧缩论只能分别将其还原或语义化。

**主 worked example：疾病分类**。杯子适合入门，但疾病分类更能承重，因为它**同时**涉及自然阻力（R3）、分类实践、跨 operator 稳定、历史继承与干预效果。同一组体征/病理可被切为不同诊断类别。SRT 预测：诊断类别在 R1–R4 上有可追踪差异——某些切分有强 R3（在治疗/干预下稳健，如有明确病原与药物反应），某些 R3 弱而 R1/R2/R4 强（社会—制度稳定但干预不稳，如部分症候群式诊断）。**关键差分**：当一个诊断类别被修订（某综合征被拆分或合并），SRT 预测不是纯词汇更替，而是**有模式的锚定代价重分配**——诊断实践迟疑、既往病例重判、治疗路径改变、患者身份与制度资格变动——且重分配模式依 R1–R4 的具体组合而异。

**两个具体微型案例（R3 高 vs R3 低）**。为使"疾病分类"不流于泛谈，给出两个方向相反的真实分类修订（具体史实与文献引用见 TODO，此处作结构示例）：

- **高 R3：消化性溃疡 → 幽门螺杆菌（H. pylori）感染性重分类。** 在 Marshall & Warren（1984，*The Lancet*；2005 年诺贝尔生理学或医学奖）之后，消化性溃疡从"应激/胃酸"框架重切为以细菌感染为主因的类别。SRT 读法：此切分有**强 R3**——抗生素根除疗法在干预下稳健有效，治愈模式**框架无关**。预测的锚定代价重分配以**边界重绘 + 病例重判 + 治疗路径切换**（抑酸→根除）为主导，而非主要由制度资格驱动；R2 对齐随干预证据快速趋同。对手对照：HPC 可诉诸因果稳态机制，但 SRT 额外预测**修订时代价重分配的具体形态由 R3 主导**（治疗反应先行，而非制度协商先行）。
- **低 R3 / 高 R2·R4：Asperger 综合征 → 并入孤独症谱系障碍（APA 2013，DSM-5）。** 该修订把一个独立标签并入谱系。SRT 读法：此切分 **R3 较弱**（无单一干预—稳健的自然关节），而 **R2/R4 高**（制度与继承承重）。预测的代价重分配以**制度资格变动、身份叙事（"Aspie"认同）、服务/教育资格、研究队列重定义、标签与治疗路径滞后**为主导，而非由干预证据驱动的病例重判。对手对照：医学实用主义会说这只是目标驱动的实践调整，但 SRT 预测重分配呈 **R1–R4 依赖的结构化形态**（身份与制度滞后签名），而非自由的目标设定。

两案对照即 §3.3 共变预测的落地：**同为"分类修订"，高 R3 与低 R3 的代价重分配形态系统不同**——这是 SRT 相对 HPC、Khalidi、Haslanger、医学实用主义的**差分收益**，也给出可证伪点（若两案重分配形态无 R3 依赖差异，则四维模型对该域失效）。

**与自然种类/社会种类立场的差别**（立场层对照，具体文本引用见 TODO）：

- **Homeostatic Property Cluster（Boyd 1991, 1999）**：HPC 用因果稳态机制解释类别投射性。SRT 不否认稳态机制，但追问它为何在**多个不等价切分**中使**这一**聚类被锚定承重；差分在于 SRT 预测分类修订时的**代价重分配模式**，而纯 HPC 只预测聚类的存废。
- **Khalidi（2013）式分级/关系自然种类**：二者都接受种类分级与相对性，但 Khalidi 仍把节点当作世界给定；SRT 把"哪些关系节点被切出并稳定"也纳入选择—继承账目。
- **Haslanger（2012）式社会建构实在论**：二者都承认制度性分类真实，但 Haslanger 不分社会现实强度与物理 R3；SRT 用 R1–R4 分维明确区分。
- **医学实用主义/工具主义**：诊断修订不只是治疗目标驱动的实践调整——SRT 预测修订带来**有结构的**锚定代价重分配，其模式由 R1–R4 组合决定，而非自由目标设定。

**失败条件（使经验风险真正可测）**：

- 杯子：若破损后语言标签、可供性、同一性判断、修复史**完全同步**变化、无滞后或路径依赖，则 `L_2` 滞后预测变弱。
- 杯子：若修补杯与新制复制品在所有 operator 群体中无身份判断差异，则历史硬化预测变弱。
- 疾病：若分类修订只产生词汇替换、而不伴随病例重判/治疗路径改变/制度资格变动，则锚定代价重分配预测变弱。
- 疾病：若高 R3 与低 R3 诊断在修订时表现出**相同**的代价重分配模式（R3 维度不做功），则四维模型对该域失效。

差分预测的方向落在 **operator-constrained anchoring 与 path-dependent `L_2` hardening**，不引入 `d-value` 或 concern。

### §6.3　结论：对象之前的问题

本文未证明 SRT 整体成立，也未声称它解释一切。它主张两件可被独立评估的事：**(防御版)** 对象式确定性不应被对象优先本体论无解释地预设；SRT 提供了一个更统一的构成性解释。**(延伸版，受阶段 B 溯因支撑、可废止)** 若该解释成立，它支持更强的 selection-first 形而上学——对象式确定性乃至确定性一般，不是本体论地板。

收束句：

> 若对象不是哲学的第一事实，哲学就不应从追问"什么作为已完成之物而存在"开始；它应追问：在何种选择、锚定、摩擦与稳定的条件下，某物才成为确定的、可承重的、可被继承为现实的。

### §6.4　后续研究（仅方向，不在本文论证）

价值作为关切宽度（`d-value`，仅书稿 Q15 意义）；主体与意识作为阈值化选择而非地板；社会事实作为 collective `L_2`；AI 作为共同地形的改写者。这些是 selection-first 地板**打开**的问题，不是它在此处**已回答**的问题。

---

## 参考文献（选）· References (selected)

> 本草稿阶段直接交手的核心文献；投稿版将补全并统一 author–date 格式。Barad 页码依 2007 Duke 版，终稿校样复核。

- American Psychiatric Association (2013). *Diagnostic and Statistical Manual of Mental Disorders* (5th ed., DSM-5). Arlington, VA: APA.
- Barad, K. (2007). *Meeting the Universe Halfway: Quantum Physics and the Entanglement of Matter and Meaning*. Durham, NC: Duke University Press.
- Boyd, R. (1991). "Realism, Anti-Foundationalism and the Enthusiasm for Natural Kinds." *Philosophical Studies* 61: 127–148.
- Boyd, R. (1999). "Homeostasis, Species, and Higher Taxa." In R. A. Wilson (ed.), *Species: New Interdisciplinary Essays*, 141–185. Cambridge, MA: MIT Press.
- Carnap, R. (1950). "Empiricism, Semantics, and Ontology." *Revue Internationale de Philosophie* 4: 20–40.
- Haslanger, S. (2012). *Resisting Reality: Social Construction and Social Critique*. Oxford: Oxford University Press.
- Hirsch, E. (2011). *Quantifier Variance and Realism: Essays in Metaontology*. Oxford: Oxford University Press.
- Khalidi, M. A. (2013). *Natural Categories and Human Kinds: Classification in the Natural and Social Sciences*. Cambridge: Cambridge University Press.
- Ladyman, J., & Ross, D. (2007). *Every Thing Must Go: Metaphysics Naturalized*. Oxford: Oxford University Press.
- Lewis, D. (1983). "New Work for a Theory of Universals." *Australasian Journal of Philosophy* 61: 343–377.
- Marshall, B. J., & Warren, J. R. (1984). "Unidentified Curved Bacilli in the Stomach of Patients with Gastritis and Peptic Ulceration." *The Lancet* 323(8390): 1311–1315.
- Sider, T. (2011). *Writing the Book of the World*. Oxford: Oxford University Press.
- Unger, P. (1980). "The Problem of the Many." *Midwest Studies in Philosophy* 5: 411–467.
- van Inwagen, P. (1990). *Material Beings*. Ithaca, NY: Cornell University Press.

---

## TODO before submission

> 投稿前必须完成的硬化与编辑任务，不影响当前 working draft 的论证主脊。

**文献交手（v0.5 已加核心引用；剩终稿校样级）**
- v0.5 已为 Sider/Lewis、Hirsch/Carnap、Barad、HPC（Boyd）/Khalidi/Haslanger、两个疾病微案例（Marshall & Warren 1984；APA 2013 DSM-5）加入 author–date 引用，并新增"参考文献（选）"。剩余为**终稿校样**：核对 Barad 2007 的 agential cut（140）/ phenomena（33, 139）确切页位；为每条交手补 pinpoint 页码。
- **Grounding / fundamentality**：v0.4 已定**弱化路线**（§3.5 主张构成性解释、不承诺 grounding 形式特征）；若改走强化路线再接 Fine / Schaffer / Rosen / Audi / Correia。当前为可选项，不阻塞投稿。
- **Hirsch / Carnap**：把 §2.5、§4.4 接到 quantifier variance 与内/外问题具体文本。
- **Barad**：§5.1 已做立场层三点交手（phenomena/apparatus 定义、装置相对客观性 vs 跨 operator 可排序性、`Psi_f` 不可无损吸收）；仍须落到 intra-action、agential separability、phenomena 客观性的**具体段落页码**。
- **Metaphysical indeterminacy / vagueness**：说明本文 determinacy 问题与 ontic vagueness、semantic vagueness、epistemicism 的关系。
- **Objecthood / composition**：van Inwagen、Unger 之外补 ordinary objects、mereology、composition as identity。
- **Natural kinds / classification**（疾病分类主案例所需）：§6.2 已给 HPC（Boyd）/Khalidi/Haslanger/医学实用主义的**立场层**对照；仍须落到具体文本与页码，并补 social kinds 文献。
- **Affordance / enactivism / pragmatism**：若杯子案例留正文，Gibson/enactivism 须从脚注升入正文交手。

**结构与编辑**
- **投稿版另出**：去 frontmatter 与内部标记（"护栏 O-Phil-11"、本 TODO 等），按 GPT 建议压成五节（问题与靶心 / 确定性为何需解释 / SRT 正面模型 / 三角对抗 / 现实强度与经验风险）。
- **语言策略**：本草稿暂维持中英双语；投稿版按目标期刊决定全英文化或中文主体 + 术语表；统一术语对照（selection realism / manifestational priority / reality-strength / sub-determinate 等）。
- **符号**：决定正文是否保留 `L_0/L_1/L_2`、`G_hat_theta`、`Psi_f`、`theta`，抑或散文化 + 术语表脚注。
- **参考文献**：建立完整 bibliography，统一 author–date 引用格式。
- **长度**：压到目标期刊约 8000–12000 词。

**论证细化**
- §6.2 至少一个 proxy 细化为可设计的操作化测度与通过/失败判据（建议优先疾病分类的 R3/R4 分离测度）。
- 复核与 `SRT_Philosophy_Foundations_CompactCore.md`、`SRT_Philosophy_Objection_Ledger_PH_SS_Extension.md`、`SRT_Philosophy_Tradition_Comparison_PH_SS.md` 的术语一致，无 canonical 漂移。
