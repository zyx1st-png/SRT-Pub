---
id: SRT-PR1058-GATE-GEOMETRY-QUALIA-INDEPENDENT-CONTENT-REVIEW-20260925
type: audit
status: active
date: 2026-09-25
layer: governance
epistemic_layer: operations
claim_mode: independent_review
canonical: false
research_mode: U
dependency:
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GATE_GEOMETRY_BEARER_FRICTION_QUALIA_L0_FREEDOM_2026-09-25.md
  - 01_Source_Intuition/SRT_DIALOGUE_DERIVATION_TRACE_GATE_GEOMETRY_QUALIA_CONSCIOUSNESS_2026-09-25.md
  - Operations/Proposals/SRT_GATE_GEOMETRY_QUALIA_SHORT_TERM_ROUTING_PATCH_2026-09-25.md
tags: [IndependentReview, PR1058, GateGeometry, Qualia, Bearer, Friction, PsiF, HPB, L0Freedom, GRG, Provenance, SingleNext]
---

# PR #1058 独立内容评审 — gate geometry / qualia / Bearer-relative friction / L0-facing freedom

> **角色**：对**未合并** PR #1058 的 pre-merge 独立内容评审记录。只读：本记录**不修改** #1058 的任何文件，也不修改 `main` 上 40b22d9 落地的同主题文件、STATUS、路由面或任何 canonical owner，不替作者关闭任何 OPEN。
>
> **评审者独立性**：独立 session / model context，没有参与 2026-09-25 的对话，也没有参与 #1058 或 40b22d9 的写作。评审依据是在 `main`（40b22d9）上重新读取 owner / source / OPEN guards，没有复述 #1058 的自我结论。
>
> **评审局限**：原始对话不在仓库里。A0-Q 引文是否逐字、作者接受事件是否发生，本评审**无法核验**，只能核对内部一致性、与现有 owner 的相容性、provenance 标注是否符合仓库规则，以及它与 `main` 现状能否共存。

## 0. 评审对象

```text
PR:          #1058 (OPEN; not draft)
title:       Source: gate geometry, qualia, and L0-facing freedom reconciliation
head:        theory/gate-geometry-bearer-qualia-reconciliation-20260925 @ 82c3bda6b65a8b442fc323d5a527d0ef4bdd7fdf
PR base:     b0f64dc5b2696fe337143a7db61a0ed8352dbce7
files (6):
  S  = 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GATE_GEOMETRY_BEARER_FRICTION_QUALIA_L0_FREEDOM_2026-09-25.md   (617 lines, #1058 version)
  T  = 01_Source_Intuition/SRT_DIALOGUE_DERIVATION_TRACE_GATE_GEOMETRY_CONSCIOUSNESS_2026-09-25.md                 (565 lines)
  P  = Operations/Proposals/SRT_GATE_GEOMETRY_QUALIA_SHORT_TERM_RECONCILIATION_PATCH_2026-09-25.md                 (254 lines)
  G  = Glossary/SRT_Live_Term_Router.md (+1 row, l.131)
  R  = _SRT_CONTEXT_ROUTER.md (+§5a, l.173–208)
  ST = STATUS.md (+5 ledger lines, l.58–62; updated: 2026-09-25)

current main: 40b22d9c85f4aee5d09a9dfc43bb4d9b886d8e9a
  = direct push, parent b0f64dc, 2026-09-25 22:26:10 +0800 (≈1 min after #1058 was opened)
  = parallel landing of the SAME dialogue under different companion filenames:
  S' = same path as S, different content (724 lines)
  T' = 01_Source_Intuition/SRT_DIALOGUE_DERIVATION_TRACE_GATE_GEOMETRY_QUALIA_CONSCIOUSNESS_2026-09-25.md (717 lines)
  P' = Operations/Proposals/SRT_GATE_GEOMETRY_QUALIA_SHORT_TERM_ROUTING_PATCH_2026-09-25.md (480 lines)
  + STATUS / _SRT_CONTEXT_ROUTER / Philosophy Hardening Index pointers
```

控制 owner / source（都在 40b22d9 上重新读取）：

- `Core_Law/SRT_One_Formation.md`（Def-OF-1 l.56–74：Selection-relative manifest / relative background；Def-OF-2 l.78–）
- `Core_Law/SRT_Generative_Ontology_Spine.md`（§8 Bearer l.348–382；§9 Agency l.386–405，含 `Selection-totality -/> pan-consciousness` l.403）
- `_SRT_SYMBOL_TABLE.md`（L0/L1/L2 aspect boundary l.27）
- `_SRT_PSI_F_CANONICAL.md`（Def-Ψ-1 l.66–72；Def-Ψ-2 l.44 / l.90–）
- `Philosophy/patches/SRT_Philosophy_PH_CONSC03_...Bearer_Concern_v0_1.md`（Concern Domain l.98；bearer ≠ concern boundary l.110–128）
- `Philosophy/patches/SRT_Philosophy_PH_CONSC04_...Zombie_Deletion_Test_v0_1.md`（Z6 l.273；definitional-substitution guard l.389）
- `Philosophy/patches/SRT_Philosophy_PH_CONSC05_...Functionalization_Residual_v0_1.md`（F2 bearer-constitutive For-P l.154；`strong For-P != For-me proved` l.173）
- `Philosophy/patches/SRT_Philosophy_PH_QUAL01_Reselective_Qualia_Geometry_v0_2.md`（§7.3 intensity l.501–521；§8 valence × reselectability l.566–579）
- `Philosophy/hooks/PH_QUAL_Bearing_Indexed_Phenomenal_Compression_Hook_2026-08-23.md`（working hypothesis l.111–119；PC-H1 l.321–327；automation prediction l.439–446）
- `_SRT_D_VALUE_CANONICAL.md` §2a（micro-valence，l.205–）
- `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GENERATIVE_EXPECTATION_TYPING_2026-09-20.md`（B + C0/C1）
- `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GRG_CROSS_OBJECTIFICATION_METHOD_2026-09-23.md`（§1.2 A0-Q「深层的语法」l.56–60）
- `Operations/Proposals/SRT_GRG_FOUNDATIONAL_PROTO_GRAMMAR_V0_3_2026-09-21.md`（“NOT … a completed universal grammar” l.77；`universal GRG = NOT ESTABLISHED` l.1011）
- `Operations/Audits/SRT_GRG_CASE2_ENGAGEMENT_VERTICAL_DECOMPOSITION_RESULT_2026-09-24.md` §16（l.838–）及 no-GRG ablation control（l.274）
- `Glossary/SRT_Live_Term_Router.md` §4（objectification l.103；re-objectification l.104；generative equivalence l.115；supported equivalence l.116；friction l.118；Ψ_f^maint l.119；gating l.130）
- `Governance/SRT_CLAIM_LADDER.md`（P3 = bridge mapping，l.117）
- `AGENTS.md`（Merged-handoff / single-next rule；Constitution / Ontology Dialogue Hard Guard；new-term rule）
- 先例：`Operations/Audits/SRT_PR1055_PREOBJECT_VERTICAL_GATING_INDEPENDENT_CONTENT_REVIEW_2026-09-24.md`（F3 provenance、F6 GRG stop-loss、F11 neighbor 的判据）

## 1. Verdict

```text
MECHANICAL / FRONTMATTER (check_frontmatter_changed vs b0f64dc)  = PASS (errors=0 warnings=0)
CI governance-preflight on 82c3bda                               = PASS
CANONICAL IMPACT                                                 = NONE (no Freeze-A owner file changed)
MERGEABILITY AGAINST CURRENT main (40b22d9)                      = FAIL
  add/add conflict on S; content conflict on STATUS.md;
  _SRT_CONTEXT_ROUTER.md auto-merges into contradictory routing
SINGLE-NEXT CONSISTENCY WITH main                                = FAIL (opposite STATUS reading of the same author instruction)
GUARD INVENTORY (HP-B OPEN / Ψ_f firewall / One≠Bearer≠Experiencer /
  no fusion reopening / no v0.4 / terminal Selection)            = PASS
S — SOURCE FIDELITY + PROVENANCE TYPING                          = REVISE
S — INTERNAL CONSISTENCY (foreground / manifestation / for-me)   = REVISE
S — CANONICAL-COMPATIBILITY FLAGGING (Bearer / Ψ_f / Concern)    = PARTIAL
G — TERM ROUTING (new-term rule entered)                         = PARTIAL (overlap under-reported)
P — AS BOUNDED RECONCILIATION PLAN                               = PARTIAL (direction right; key collisions missing)
NEIGHBOR PACKAGE                                                 = FAIL (no external neighbor named; unlabeled comparative sentence)

MERGE #1058 AS-IS                                                = NO
OVERALL                                                          = SUPERSEDED-IN-PART BY 40b22d9;
                                                                   SALVAGE UNIQUE CONTENT INTO A main-BASED FOLLOW-UP;
                                                                   CONTENT FINDINGS APPLY TO WHICHEVER VERSION CONTROLS
AUTHOR DECISIONS NEEDED                                          = YES (A-1 … A-5, §4)
```

一句话：#1058 的主体防线是健全的。它没有碰 Freeze-A，HP-B 保持 OPEN，Ψ_f / 物理能量 / 预测误差 / 痛苦都有显式防火墙，One ≠ Bearer ≠ Experiencer 得到保留，fusion lane 没有被重开，还按 new-term rule 进入了 Live Term Router（`main` 版反而缺这一步）。但它现在不能合并：`main` 已被同一对话的另一版本直接落地，两版在 STATUS 上给出相反的单一 next 读法。§3 的实质问题（F2–F9）大多同样存在于 `main` 版。所以无论最后哪一版起控制作用，都需要处理这些问题。

## 2. 通过项（保留）

- **防线清单完整**：S §16 的 hard guards 与 P §4 / §6 的 FAIL 条件方向正确，尤其是 `qualia != friction`、`Psi_f = felt intensity` 被列为 FAIL，以及 `GRG universal grammar = already retired canonically` 被列为 FAIL。
- **Selection 语义未漂移**：S §1 “Terminal Selection remains genuine”，S §16 `primitive Selection != gating of a pregiven option menu`，与 `SRT_AI_START.md §1.1` 以及 #1055 二次裁决 D-1 一致。
- **L0/L1/L2 aspect 读法正确**：S §1 “not three substances or mandatory temporal stages” 与 Symbol Table l.27 一致。
- **One 的转述与 Def-OF-2 相容**：T §15 “recurrent relatively separable process-unity” 没有越出 Def-OF-2。
- **HP-B 诚实保持 OPEN**：S §10 / T §17 把新的 Z6 前件写得更强，同时明确 `logical / constitutive necessity NOT established`，并主动点出 “foreground / manifest / for-this-bearer” 可能偷运现象内容。这正是 PH-CONSC04 的正确用法（但 S 自身其他节没有贯彻，见 F3）。
- **红 / 蓝压力例**：S §6.2 用低 friction 的中性感受质反驳 “qualia = friction”，推理有效。
- **自传假设处理得当**：S §14 / T §19 只把它作为自传性假设保留，并给出对称反例（failure 也可能沉积 fear / shame）和个案检验条件。
- **new-term rule 已执行**：G 为 “gate geometry” 登记了 WORKING_LABEL_ONLY / PARTIAL_OVERLAP 行，并写明合并条件。`main` 版 40b22d9 没有这一行。
- **机械检查**：frontmatter 变更检查 0 error / 0 warning；CI governance-preflight 通过。

## 3. Findings（按严重度排序）

### F1 — 高（阻断合并）：#1058 已被 `main` 上的平行直推 40b22d9 部分取代；合并会冲突，并制造双 owner / 双 next

**证据。**
- 40b22d9 以 b0f64dc 为父提交直接推到 `main`，与 #1058 同一基点、同一对话、同一 author-source 路径（S），但内容不同（724 行 vs 617 行），companion 文件名也不同（T' / P' vs T / P）。
- 以 40b22d9 为目标试合并 #1058：`CONFLICT (add/add)` 发生在 S，`CONFLICT (content)` 发生在 STATUS.md，`_SRT_CONTEXT_ROUTER.md` 则**自动合并成功**。
- 自动合并后的 router 同时包含两句话：`main` l.234 称 P' 为 “current bounded patch owner”；#1058 §5a l.175 称本路线是 “HIGH companion route … does **not** create a second CURRENT NEXT”，并指向 P。两个 patch owner，两种相反的地位说明。
- STATUS 读法相反：
  - `main` l.56–57：`CURRENT NEXT = high-priority gate-geometry / qualia bounded routing patch`，owner = P'；原 GRG next 被并入 P' 的 Route H（§0.3a、§2 “Current single next” 都已同步）。
  - #1058 l.58–62：`CURRENT NEXT UNCHANGED`，本包只是 companion，服务 post-stop-loss GRG review。
- 两版都是同一作者指令（`main` S' 的 A0-Q5：「……提高这份文件的优先级，虽然暂时不改Canonical，但是作为patch短期任务尽量路由过一下这个文件」）的不同实现。这句话本身没有说明是否取代现行 CURRENT NEXT，所以这是作者裁决事项，不是机械冲突。
- #1058 PR 描述中 “main...head: ahead 6 / behind 0” 已过时。

**风险。** 按冲突手工解决后，仓库会同时存在 T / T'、P / P' 两对 companion，各自声称不同的 STATUS 地位。这违反 `AGENTS.md` 的 merged-handoff / single-next 规则（“A handoff must not create a second CURRENT NEXT”）。

**修复。** [A-1 / A-2] 作者先定哪一版控制、STATUS 取哪种读法。评审推荐：**不合并 #1058；以 `main` 现状为基底**，把 #1058 独有、且经 §3 修订后仍成立的内容（见 §7 对照表：G 行、两条 “earlier” 作者引文、S §6.2 / §9 等段落）作为 `main` 上的 bounded follow-up 落地，然后关闭 #1058。不保留第二对 T / P 文件；需要的话，把 T 的独有推导段并入 T' 作为附录。

### F2 — 高：作者 A0-Q1 的“成为对象”被 machine 改型为“现象前景化 ≠ 对象化（= 反思）”，属于实质语义变更，没有记录作者二次裁决

**证据。**
- A0-Q1（S l.37）：「感受质是，通过friction的积累使L0视角下的门控从背景进入前景**成为对象**……」
- 同一记录保存的作者话语（S l.47）：「……**门控对象化这块我非常认同**。」
- S §6 的 “bounded form”（l.231–243）删掉了“成为对象”，只剩 “foreground manifestation”。S §12（l.470–490）把 “part of the gate / deformation becomes an explicit object” 定义为 **reflection**，并规定 `phenomenality != reflection`。
- T §13（l.325–349）承认这是一次修正：“The dialogue initially risked collapsing phenomenality into gate-objectification. Correction: …”。但它没有记录是谁提出的修正，也没有这一修正的作者接受事件。
- 结果是：按 S 自己的分型，作者字面的 qualia 定义（gate 成为对象）落在了 “reflection” 一侧，而不是 qualia 一侧。

**风险。** 这是本包的核心命题。机器分型可能是对的（它保住了非反思意识候选），但 `AGENTS.md` Hard Guard 要求：“substantive changes of meaning/direction” 须交作者二次裁决后才能硬化。现在的写法会让后续 session 把 “qualia ≠ gate 对象化” 当作作者方向引用。

**修复。** [A-3] 交作者裁决，至少三种读法并列：
- (a) machine 改型：“成为对象”读作非反思的前景化；对象化 / 反思是第二步。
- (b) 作者字面：qualia 本身就是 gate 的（前反思）对象化；reflection 是更高阶的**显式**对象化，需要另行区分 “前反思对象化 / 显式对象化” 两级。
- (c) 分级读法，把 “object” 的强度写成参数。

裁决前，S §6 / §12 与 T §13 应标注 “machine re-typing of A0-Q1 ‘成为对象’ — pending author adjudication”。

### F3 — 高/中：“foreground / manifestation / for-me” 与 canonical 同名重载；S §12 用 “=” 下了现象性定义，与 S §10 自己的 Z6 警告冲突

**证据。**
- Def-OF-1（One Formation l.56–74）：**每一个** Selection 事件都有 manifest + relative background 两个结构读法。Spine §9 l.403 另有 `Selection-totality -/> pan-consciousness`。
- S §12 l.476：`felt / phenomenal deformation = gate mismatch or deformation becomes part of current bearer-relative manifestation`。S §9 l.386 也用 “becomes part of the current bearer-relative manifest reality” 替代 inner observer。
- S §6 l.241：“background gate becomes phenomenally foregrounded”；S §3：“foreground / background asymmetry -> re-identifiable object”。同一文件里的 “foreground” 至少有三义：本体（Def-OF-1）、对象化切分、现象。
- S §6.1 l.268：`for-me-ness <- bearer-indexed constitutive involvement`。PH-CONSC05 F2（l.154）正好把 “bearer-constitutive For-P” 列为最强结构形式，并规定 `strong For-P != For-me proved`（l.173）。PH-CONSC04 l.389 要求 “survive the Z6 test rather than rely on definitional substitution”。
- S §10 自己写着：“which terms such as ‘manifest’, ‘foreground’, ‘internal’ or ‘for-this-bearer’ were silently carrying phenomenal content?”

**风险。** §12 的 “=” 只有两种读法。若 “manifestation” 取 canonical 义，则每个 bearer-relative Selection 都“被感受”，与 pan-consciousness 护栏及 HP-B OPEN 冲突。若取现象义，则定义里已含现象性，Z6 变成循环。S §6.1 把现象词 “for-me-ness” 挂到结构项上，正是 PH-CONSC05 所拦的推断。

**修复（机械，无需作者裁决）。**
- 在 S 中显式分型：`manifest_OF`（Def-OF-1）/ `foreground_obj`（对象化切分）/ `foreground_phen`（现象候选）。
- S §12 的 “=” 改为 “candidate:” 并加 `manifest_OF != phenomenal`。
- S §6.1 的轴名改为 “bearer-constitutive For-P (PH-CONSC05 F2) — phenomenal For-me NOT licensed”，并把 PH-CONSC05 加进 S / P 的 dependency 与 P4 目标。

### F4 — 中高：provenance——两条“earlier controlling”引文在仓库中首次出现；第三条与同日另一记录不一致；优先级指令缺引文；接受事件整体化

**证据。**
- S l.43–47 把两条引文标为 “Earlier controlling author direction from the same reconstruction line remains active”：「其实目前看来，L0、 L1、 L2并不是某种空间，而是某种视角……」和「另外GRG可能不应该去找一种通用的语法……门控对象化这块我非常认同……」。在 40b22d9 全仓库检索，这两句**只出现在 #1058**，其他任何作者记录（包括 09-24 Spine minimal-kernel 与 pre-object 记录）都没有。“remains active” 暗示它们已有在案记录，事实并非如此。
- S l.41：「认同你的分析，按你的方向继续。另外所以我的失败成功的避免了L2视角选择的过度积累。」`main` S' 把后半句单独记为 A0-Q3，另记 A0-Q4「认同你的分析，下一步尽量开始收敛，方便写入仓库。」同日两份记录对同一对话给出了不同的“逐字”引文，而且都没有标注轮次。
- #1058 全文声称 “high priority / short-term”（S 头注、§15；P §1；G；R；ST），却没有保存授权这一优先级的作者原话（`main` S' 的 A0-Q5）。
- 接受事件整体化：S l.49 “The author repeatedly accepted …”；T l.45 / l.231 “Author accepted …”；T l.510 “The author explicitly requested convergence …”。都没有引文或轮次。先例 #1055 F3 及 Phase-3 provenance map D1 要求：没有逐条作者措辞或接受事件的 machine 措辞按 **M** 处理，record-level directional acceptance 可以注明，但不能升级逐条 provenance（亦见 `CONTINUE_DIRECTIONAL_ACCEPTANCE` §5）。

**正面价值。** 如果这两条 “earlier” 引文属实，它们是仓库里**唯一**记录作者本人 GRG 修正措辞（「不应该去找一种通用的语法，而是恢复一个对象应有的L0.L1.L2视野」）和 “L0/L1/L2 是视角” 措辞的地方。`main` S' §14 只写了 “The author accepts a major reframing”，没有引文。这是 #1058 最值得保留的内容。

**修复。** [A-5] 作者确认这两条引文的轮次 / 日期，以及第三条引文的准确形式。确认后，把它们以 A0-Q 形式补进控制版 S'，标注轮次，并删去 “remains active”。S / T 的节级 provenance 按 A0-Q / A1 / M 逐节标注（机械，待 A-5 回答后填）。

### F5 — 中高：「位置、攸关、预期」→ “Bearer / Concern / Expectation” 的映射与 canonical Bearer 不对齐

**证据。**
- Spine §8（l.350–380）：`formed One / Selection-position + P + E -> Bearer`，其中 P = prospective self-indexing，E = same-One prospective **exposure**。这是**前瞻性**自我暴露。另有 `Bearer -/> Concern automatically`。
- S §5 l.198：`Bearer -> where consequence is non-trivially carried`。S §8 l.355–356：`Bearer -> consequence-return / own-history burden`。T §15 l.393：`consequences become own-history`。这是 PH-CONSC03 / PH-QUAL01 的 bridge 级 “structural bearing”（same-bearer consequence return + history writeback），偏**回顾性**，不是 Spine §8 的 canonical Bearer。S 没有说明用的是哪一个。
- 作者说的是「bearer**提供的**位置、攸关和预期」。按 canonical 顺序，Selection-position 是 Bearer 的**上游输入**（One Formation l.50、Spine §8），不是 Bearer 提供的。Concern 也不是 Bearer 自动提供的。S §5 把三者拆成独立行，方向是对的，但把“位置”直接吸收进了 “Bearer”，也没有标出作者字面与 canonical 的张力。
- PH-CONSC03 l.110–128：bearer boundary ≠ concern boundary，concern domain 可以越出 bearer（例如为他者承担风险）。S §5 把 Concern 限为 “what differences genuinely matter to that continuing position”，S §8 的统一判据又要求 “consequences close on the same continuing Bearer”。越出 bearer 的 concern 所产生的 friction 该归谁，没有说明。
- Expectation：S §5 说明 “need not be explicit, propositional or conscious”，方向正确，但没有接 09-20 的 B + C0/C1 typing，也没有接 `structural / operative expectation != E_G` 护栏（G l.121–122）。另须注意 Spine §8 的 `E` 指 exposure，不是 expectation，后续形式化时容易撞名。

**修复（机械）。** 在 S §5 加对照：`位置 -> Selection-position（上游，One Formation）`；`攸关 -> Concern Domain（PH-CONSC03；Bearer -/> Concern automatically）`；`预期 -> structural generative expectation（09-20 B+C0/C1；≠ E_G；≠ Spine §8 E）`；`Bearer -> Spine §8 canonical（prospective P+E）；PH-CONSC03 structural bearing 仅作 bridge 读法`。另在 S §8 注明 concern-beyond-bearer 为 OPEN 压力例。

### F6 — 中：friction 与 gate geometry 本身都贴近 canonical Ψ_f，#1058 只防了前者；作者所说的“friction”指什么本身是待裁决事项

**证据。**
- `_SRT_PSI_F_CANONICAL.md` 的标题是 “Ontological Friction”。Def-Ψ-1（l.66–72）：Ψ_f := 在已声明的 Ĝθ 形成态 / 模型载体把开放可能性表示为**可维持、可行动、可协调的 L1 现实切片**时必须承担的本体论阻抗。Def-Ψ-2（l.44）：Fisher–Rao 信息几何投影。换句话说，canonical Ψ_f 已经是“把开放可能性粗粒化为稳定切片的代价”，并且已有一个信息几何读法。
- 所以 gate geometry（稳定的粗粒化几何）与 Def-Ψ-1 / Def-Ψ-2 的重叠，并不小于 friction 与 Ψ_f 的重叠。G 行的重叠清单没有 Ψ_f。
- S §4 的 toy case（“old gate treats x1 ~ x2 … maintaining the old equivalence becomes costly”）几乎逐字对应 G l.119 的 `maintenance-friction interface`：historical `Psi_f^maint` ≈ reach §V “cost of maintaining current equivalence”，状态是 **UNRESOLVED COLLISION**。G l.118 已有 `friction` 族行（OVERLOADED_SAME_NAME）。#1058 引入了第三个 “friction” 义（bearer-relative gate reconstruction burden），却没有接这两行。
- 在 SRT 语境中，作者用的 “friction” 很可能就是指自己理论里的 ontological friction。S §4 把“保留的能量”改写为 “retained load / retained tension”，并规定当前不得读作 Ψ_f。这是保守防火墙，但也可能预先否定了作者的本意。
- S §6.1 把 `phenomenal intensity / urgency <- … friction contribution`。PH-QUAL01 §7.3（l.501–521）要求 intensity 模型说明它预测的是 felt / registered burden、actual burden，还是二者的背离；并规定 intensity ≠ Ψ_f。S 没有作这一区分。在 friction 与 Ψ_f^maint 的碰撞未解之前，这条映射有借道等同的风险。

**修复。** [A-4] 请作者裁决 “friction” 所指：(i) canonical Ψ_f 的一个读法（→ 走 P6 crosswalk，关注 Def-Ψ-1 的“可维持 L1 切片”）；(ii) 更宽的 bearer-relative 重构负担族（→ 在 G 中与 l.118 / l.119 分型）；(iii) OPEN，待 P6。
机械部分：G 行的碰撞注记补上 `_SRT_PSI_F_CANONICAL.md` Def-Ψ-1 / Def-Ψ-2 与 G l.118 / l.119；S §6.1 intensity 行补 “felt vs actual vs divergence — per PH-QUAL01 §7.3”。

### F7 — 中：对既有 owner 的重叠报告不足，使 “gate geometry / L0-facing freedom / phenomenal compression” 看起来比实际更新

| #1058 负担 | 已由谁承载（未被 #1058 引用） |
|---|---|
| S §11 L0-facing freedom：“participating in reconstruction of the gate geometry that helps determine what later alternatives … become formable” | Spine §9 Agency（l.392–397）：“participating in the rewriting of conditions of its own and/or relational future Selection”；G l.104 `re-objectification / recutting`：“reopening and changing the operative cut when consequence/friction requires it” |
| S §2 “which differences may currently be treated as equivalent … under a declared range of perturbation” | G l.115 `generative equivalence`（intervention-relative）；G l.116 `supported / subsidized equivalence`（其持续有效依赖支持条件） |
| S §7 “high-dimensional … deformation -> low-dimensional selection-active quale” | 08-23 hook working hypothesis（l.111–119）与 PC-H1（l.321–327）：“high-dimensional unresolved constraints -> qualitative compression Q” |
| P §5 test 7（skilled automation） | 08-23 hook l.439–446 的 automation 预测 |
| S §11 / T §3 addiction as L2 capture | PH-QUAL01 §8 l.579：“addiction / habit capture: positive reward can stabilize narrowing and repeated lock-in” |
| S §6.1 valence 轴 | `_SRT_D_VALUE_CANONICAL.md §2a` micro-valence（hook l.97 / l.239 明确保留，不得重定义）；PH-QUAL01 §8 `Valence != Reselectability` |
| S §6 “qualitative character <- local gate geometry” | PH-QUAL01 的 `Q_L1 = (E, Delta_ij)` 与 `RDef_B(q)` reselective deformation profile |

S §7 写了 “extends the existing phenomenal-compression hook”，S §6.2 写了 “preserves PH-QUAL01”，但都没有给出增量说明。

**修复（机械）。** 在 P（或控制版 P'）的 P4 / P5 前加一张 **delta 表**：每一行写明“既有 owner 已承载什么 / 09-25 新增什么 / 新增是否仅为重述”。L0-facing freedom 的候选增量看来只有 (i) continuity 条款和 (ii) L1 vs L0 对照，应以 Spine §9 为锚写成对它的**限定**，而不是新定义。G 行碰撞注记补上 l.104 / l.115 / l.116。

### F8 — 中：GRG 修正的对手定位不准；它与 09-23「深层的语法」的关系未声明；也没有回应 stop-loss 的证据

**证据。**
- v0.3 从未主张 universal grammar：l.77 “It is NOT currently: a completed universal grammar”；l.1011 `universal GRG = NOT ESTABLISHED`。P §1 担心后续 session 会 “continue treating GRG’s goal as universal grammar extraction”，R 的 boundary 也说 “not as proof that a universal grammar has already been canonically retired”。两处针对的都是一个 owner 并未持有的立场。
- 真正需要处理的张力，在 09-23 作者 A0-Q（cross-objectification §1.2 l.60）：「……而是要理解各名称和形式化内容背后所想表明的**深层的语法**。然后将其他领域的各种概念和形式化内容去重新整理。」09-25 的「不应该去找一种通用的语法，而是恢复一个对象应有的L0.L1.L2视野」是对这一句的收窄、修正，还是并存？S §13 与 T §18 都没有说明。
- S §13 的 8 问方法（equivalence / boundary / support / history / friction / hidden differences / X as gate / reopen），与两次得出 `SOURCE_OWNED_DECOMPOSITION_NO_GRG_GAIN` 的那类分解高度同构。no-GRG ablation（l.274）的结论是 “ordinary causal / systems analysis” 足以恢复主要接缝。先例 #1055 F6 对同一模式已要求补 LLM 先验控制。
- S §13 称 “directly supports the existing STATUS post-stop-loss GRG method contraction”，但对 case2 result §16（l.878 起）为该路线列出的四个问题一个都没有回答：哪些 cut 作为内部 SRT / 哲学组织仍有用；哪些只是通用因果 / 系统分析；保留什么作为治理纪律；哪些跨域科学独特性主张要撤回、收窄或留 OPEN。

**修复（机械 + 待 A-5）。**
- S §13 首句改为针对 09-23「深层的语法」的定位（待作者确认后标 narrowing / supersession）。
- 补一条非主张：“the 8-question reconstruction does not by itself exceed ordinary causal / systems analysis — see case2 no-GRG ablation”。
- P 的 P3 问题清单直接采用 case2 §16 的四问，把现 Q5（“Does this reframing explain why two fusion cases were no-gain?”）改成须带 same-model no-GRG control 的检验。

### F9 — 中：U-mode 下完全没有外部邻居；且有一句未标注的比较主张

**证据。**
- S / T / P 的 frontmatter 都是 `comparative_claim: none`，但 T l.400 写：“This gave a **more precise route than** treating Stable ISP or integration alone as consciousness.” `AGENTS.md`：“Novelty, irreducibility, superiority … claims trigger the relevant scoped audit even when unlabeled.”
- 路由器 §8 已有 IIT / PCI / GNW 路线，#1058 的 P4 目标清单只列 SRT 内部 owner。

| #1058 负担 | 直接邻居（评审 M，供 P4 / P5 的 light neighbor awareness） |
|---|---|
| S §8 共同重构面：“cannot be independently resolved without changing one another’s available resolutions” | IIT 的 integration / exclusion（不可分解性；对 split-brain 预测两个 complex）；GNW 的 global ignition / availability；Bayne（2010）*The Unity of Consciousness* |
| T §16 “perceptual unity may split while broader bearer unity remains partly shared” | Pinto et al.（2017, *Brain*）“Split brain: divided perception but undivided consciousness”（有争议的经验结果，恰好是现成压力例） |
| S §9 no homunculus | Dennett（1991）对 Cartesian theater 的批评 / multiple drafts |
| S §7 低维现象压缩界面 | Graziano 的 Attention Schema Theory；Seth 的 interoceptive inference；Damasio 的 homeostatic feelings |
| S §6.2 质的邻域由几何约束 | quality-space theory（Austen Clark；Rosenthal）（PH-QUAL01 / Annex 06 可能已部分支付） |
| S §2 稳定粗粒化几何 | coarse-graining / lumpability；causal emergence（Hoel, Albantakis & Tononi 2013） |
| S §11 L0-facing freedom = continuity + revisability | Frankfurt（1971）second-order volition；Fischer & Ravizza（1998）reasons-responsiveness；Dennett（1984）*Elbow Room* |
| addiction as L2 capture | incentive-sensitization（Robinson & Berridge 1993）；habit 转移（Everitt & Robbins 2005） |
| P §5 tests 1–2（anesthesia：局部处理保留而共同重构改变） | PCI（Casali et al. 2013）与 IIT 的既有预测；仓库已有 `Neuroscience/SRT_Clin_00_IIT_PCI.md` |

**修复（机械）。** T l.400 改为非比较措辞，或把它标为 comparative claim 并命名比较对象（IIT integration）。P 的 P4 / §5 按上表标注 neighbor-paid，并说明 SRT 版本若要有区分力，须作出与 IIT / GNW / PCI **不同**的预测。本评审不主张 #1058 被这些邻居完全吸收，只要求在下一步作这项检查。

### F10 — 中低：作者的 L2 / L0 对照被 machine 换轴为 L1 / L0，没有标注

- 作者原话（S l.47）：「成瘾这些应该属于**L2视野**下的选择，我们需要的自由很可能是**L0视野**下的自由。」
- S §11 l.439 与 T §3 l.97 改成了 `L1-facing freedom`（在已形成选项中选）vs `L0-facing freedom`。
- 两者可以相容（成瘾表现为被 L2 约束的 L1 选项），但作者的对照项是 L2 而不是 L1，这一换轴属于 machine 分析。
- **修复（机械）**：S §11 保留作者的 L2 / L0 对照为主轴，把 L1 / L0 标为 machine 补充。

### F11 — 低：STATUS / G / 等级标签的若干小问题

- **ST 落点**：5 行插在 STATUS §0 “Landing ledger — 已落地事实”里，但写于合并之前，也没有像其他 ledger 行那样写 `#NNNN = MERGED / sha`。
- **ST 遗留**：base 的 STATUS 在 l.689 另有一个过时的 “Current single next: LATENT RECONSTRUCTIVE REACH …”。#1058 没有处理它，P §6 的验收项 “STATUS preserves exactly one CURRENT NEXT” 因此并未真正满足（`main` 40b22d9 已同步该块）。
- **G 状态列**：`**SHORT-TERM HIGH-PRIORITY WORKING CONSTRUCT**` 放进了 “Status / maturity” 列。优先级属于 STATUS，不属于术语路由表（#1043 “keep router table descriptive rather than adding admission labels”）。建议改为 `working label; priority per STATUS`。
- **G 路由列**：“One/stability owners” 过于含糊，应写出具体文件。
- **S §17**：`QUALIA MECHANISM = STRONG P3-STYLE CANDIDATE`。Claim Ladder 的 P3 是 bridge mapping（l.117），“STRONG” 没有依据。建议与 hook / PH-QUAL01 一致，写 `P3/P4 bridge hypothesis candidate`。

## 4. 需要作者裁决的事项

```text
A-1  #1058 与 main 40b22d9 的关系（F1）：
     (a) 不合并 #1058；以 main 为基底，把 #1058 独有内容作为 follow-up 落地，然后关闭 #1058（评审推荐）
     (b) 以 #1058 为准替换 40b22d9 的对应文件
     (c) 两版合并为一版（须同时回答 A-2）
A-2  STATUS 单一 next 口径（F1）：
     (a) gate-geometry patch 即 CURRENT NEXT，GRG post-stop-loss review 并入其 Route H（main 现状）
     (b) CURRENT NEXT 不变，gate-geometry 包只是 companion（#1058）
A-3  A0-Q1「成为对象」（F2）：
     (a) machine 改型：现象前景化 ≠ 对象化 / 反思
     (b) 作者字面：qualia = 前反思的 gate 对象化；reflection = 显式对象化
     (c) 分级读法
A-4  作者所说的 “friction”（F6）：(i) canonical Ψ_f 的一个读法 | (ii) 更宽的 bearer-relative 重构负担族 | (iii) OPEN 待 P6
A-5  provenance（F4 / F8）：两条 “earlier” 引文的轮次 / 日期；第三条引文的准确形式；
     09-25 GRG 修正对 09-23「深层的语法」是 narrowing、supersession 还是并存
```

## 5. 无需作者裁决的机械后续（在 A-1 裁定的控制版上执行，建议合成一个 bounded follow-up PR）

```text
F3  foreground / manifestation 三义分型；S §12 “=” -> candidate；for-me-ness 轴改名为 bearer-constitutive For-P；接 PH-CONSC05
F5  位置 / 攸关 / 预期 -> Selection-position / Concern Domain / 09-20 expectation 对照；Bearer 取 Spine §8 canonical；concern-beyond-bearer 列为 OPEN
F6  G 行碰撞注记补 Ψ_f Def-Ψ-1 / Def-Ψ-2 与 G l.118 / l.119；intensity 行补 felt / actual / divergence
F7  P4 / P5 前加 delta 表；L0-facing freedom 以 Spine §9 为锚写成对它的限定；G 补 l.104 / l.115 / l.116
F8  S §13 非主张（不超出 ordinary causal / systems analysis）；P3 采用 case2 §16 四问 + same-model no-GRG control
F9  T l.400 去比较或标注；P4 / §5 neighbor-paid 标注
F10 S §11 恢复作者 L2 / L0 主轴
F11 STATUS 落点 / 遗留 next 块；G 状态列与路由列；S §17 等级标签
F4  节级 provenance 表（A-5 回答后填）
```

## 6. 保持 OPEN（本评审刻意不关闭）

- `B_s -> B_p ?` / HP-B phenomenal necessity；
- common bearer-relative reconfiguration → phenomenality；
- friction / Ψ_f / Ψ_f^maint 的关系；
- gate geometry 是否有超出既有 owner 的独立负担（G 行的保留条件）；
- phenomenal surface 的 split / merge 条件；
- L0-facing freedom 的充要判据；
- genuine actualised Selection vs merely descriptive / modelled change；
- scientific distinctiveness = NOT ESTABLISHED；fusion lane PAUSED；third fusion domain = NO；BCTB T2 = HOLD；GRG v0.4 = NOT AUTOMATIC；further owner cleanup = PAUSED BY DEFAULT。

## 7. #1058 与 40b22d9 的内容对照（供 A-1 使用）

| 内容 | #1058 | main 40b22d9 | 评审建议 |
|---|---|---|---|
| Live Term Router “gate geometry” 行（new-term rule） | 有（G l.131） | **无** | 按 F6 / F7 / F11 修订后移入 main |
| 作者引文「L0、L1、L2并不是某种空间，而是某种视角……」 | 有（S l.45） | 无 | A-5 确认后作为 A0-Q 补入 S' |
| 作者引文「GRG可能不应该去找一种通用的语法……门控对象化这块我非常认同……」 | 有（S l.47） | 无（S' §14 只有 “The author accepts a major reframing”） | 同上；这是 GRG 修正唯一的作者措辞 |
| A0-Q4「……方便写入仓库」/ A0-Q5 优先级指令 | 无 | 有（S' l.72 / l.76） | 保留 main |
| 红 / 蓝中性感受质压力例 | S §6.2 | S' §7.3–7.4 | 等价，保留 main |
| no-homunculus；constitutive deformation；split-brain 压力例 | S §9；T §10 / §16 | T' §4–5 / §8 | 以 main 为基，T 的 §10 / §16 可并入 T' 作附录 |
| 独立 context-router 路线 | R §5a（新 route） | 在 §5 / §8 / §8a 插条目 + boundary | 保留 main 的插入式；不再新开 §5a，避免双路由 |
| Philosophy Hardening Index 条目 | 无 | 有 | 保留 main |
| D1–D5 交付物 + stop condition | P §3 P1–P6（无显式 stop） | P' §5 / §7 | 保留 main |
| STATUS 口径 | companion / next 不变 | 取代 CURRENT NEXT，GRG 并入 Route H | 由 A-2 决定 |

说明：§3 的 F2、F3、F5–F9 在 `main` 版 S' / T' / P' 中基本同样存在（例如 S' §8 同样把 phenomenal foregrounding 与 reflective gate-objectification 分开，S' §7.2 同样有 for-me 轴）。本评审只核对了 #1058。若 A-1 选 (a)，§5 的机械修复应作用于 S' / T' / P'，并须针对 main 版的具体行号另行复核。
