---
id: SRT-PR1055-PREOBJECT-VERTICAL-GATING-INDEPENDENT-CONTENT-REVIEW-20260924
type: audit
status: active
date: 2026-09-24
layer: governance
epistemic_layer: operations
claim_mode: independent_review
canonical: false
research_mode: U
dependency:
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_PREOBJECT_VERTICAL_GATING_GLUE_GENERATIVE_DIVINITY_2026-09-24.md
  - Operations/Proposals/SRT_PREOBJECT_VERTICAL_GENERATION_CANONICAL_RECONCILIATION_PLAN_2026-09-24.md
tags: [IndependentReview, PR1055, Verticality, PreObject, Gating, Glue, Divinity, Provenance, CClassContract]
---

# PR #1055 独立内容评审 — pre-object vertical gating / glue / generative divinity

> **角色**：对已合并 PR #1055 的 post-merge 独立内容评审记录。只读评审：本记录**不修改**被评审的两个文件、STATUS 或任何 canonical owner，也不替作者关闭任何 OPEN。
>
> **评审者独立性**：独立 session / model context，未参与 #1055 的对话或写作；评审依据是 `main` 上的 owner / source / OPEN guards 重新读取，而非复述 #1055 的自我结论。
>
> **评审局限**：原始对话不在仓库中。A0-Q 引文是否逐字、作者接受事件是否发生，本评审**无法核验**；只能核对内部一致性、与现有 owner / source 的相容性、provenance 标注是否符合仓库规则。

## 0. 评审对象

```text
PR:            #1055 (MERGED 2026-09-24)
merge commit:  01faf40bfb903a1f2c9d378939f5452d36d7cad9
base:          d02c8520a5a5a7a0416701f311aad18b597ead95
PR head:       146b4fd88fe9d1b1aaefd21c8e1a9ddb70d5440c
files:
  S = 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_PREOBJECT_VERTICAL_GATING_GLUE_GENERATIVE_DIVINITY_2026-09-24.md  (785 lines)
  P = Operations/Proposals/SRT_PREOBJECT_VERTICAL_GENERATION_CANONICAL_RECONCILIATION_PLAN_2026-09-24.md            (532 lines)
```

控制 owner / source（均在 01faf40 上重新读取）：

- `Core_Law/SRT_L0_Metaphysics.md`（核心主张 l.28；无选择者 l.110–122；S0 l.174–180；风险清单 l.422–424）
- `Core_Law/SRT_Generative_Ontology_Spine.md`（event-level verticality l.165–174；Ĝ 边界 l.196–203）
- `Core_Law/SRT_One_Formation.md`（Def-OF-1 l.56–74；One l.80–82）
- `_SRT_SYMBOL_TABLE.md`（L0/L1/L2 aspect boundary l.27；Ĝ 行 l.34；Ĝ† 行 l.35）
- `Core/SRT_Core_21_Minimal_Axioms.md`（Ĝ ≠ primitive Selection l.246–256）
- `Operations/Audits/SRT_GENERATIVE_ONTOLOGY_SPINE_SEMANTIC_THINNING_AUDIT_2026-09-24.md`（§14.0 / §14 landing order）
- `Operations/Audits/SRT_REPOSITORY_SELF_RECONSTRUCTION_PHASE3_PROVENANCE_VOCABULARY_MAP_2026-09-23.md`（四类 provenance；D1 / D3；§9）
- `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_CONTINUE_DIRECTIONAL_ACCEPTANCE_2026-09-24.md`
- `Operations/Proposals/SRT_GRG_FOUNDATIONAL_PROTO_GRAMMAR_V0_3_2026-09-21.md`（§4 horizontal / vertical research；§4.3 no-unrepresentability）
- `Operations/Audits/SRT_GRG_CASE2_ENGAGEMENT_VERTICAL_DECOMPOSITION_RESULT_2026-09-24.md` §16，及 `..._NO_GRG_ABLATION_CONTROL_2026-09-24.md` §6–§7
- `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_SELECTION_GENERATIVE_VERTICAL_DYNAMICS_2026-09-22.md` §B / §C / §D / §F
- `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GENERATIVE_EXPECTATION_TYPING_2026-09-20.md` §2–§5
- `01_Source_Intuition/SRT_AUTHOR_REENTRY_CROSS_DIMENSIONAL_SELECTABILITY_AND_WHOLE_SURPLUS_2026-09-10.md` §2 / §7
- `Glossary/SRT_Live_Term_Router.md`；`Governance/SRT_EDIT_PROTOCOL.md`（C 类复审；same-day guard）；`STATUS.md` §0–§2

## 1. Verdict

```text
MECHANICAL / FRONTMATTER (check_frontmatter_changed vs base)  = PASS (errors=0 warnings=0)
CANONICAL IMPACT                                               = NONE (no owner file changed)
GUARD INVENTORY (no Freeze-A edit / no 2nd CURRENT NEXT /
  HOLDs kept / distinctiveness NOT ESTABLISHED / U-mode)        = PASS
S — SOURCE FIDELITY + PROVENANCE TYPING                        = REVISE
S — INTERNAL CONSISTENCY (gating level; object sense)           = REVISE
S — CANONICAL-COMPATIBILITY FLAGGING                            = PARTIAL
P — AS FUTURE C-CLASS CONTRACT                                  = REVISE (do not execute as-is)
NEIGHBOR PACKAGE                                                = PARTIAL
ROUTEABILITY                                                    = FAIL (no inbound reference on main)

REVERT #1055                                                    = NO
OVERALL                                                         = KEEP; BOUNDED FOLLOW-UP REQUIRED
AUTHOR SECOND ADJUDICATION NEEDED                               = YES (A-1 … A-4, §4)
```

#1055 作为 **noncanonical source record + future contract** 的主体防线是健全的：没有碰 Freeze-A owner，没有制造第二个 CURRENT NEXT，保留了所有 HOLD，`primitive Selection != prior chooser`、`L0 != warehouse`、`occurrence != persistence != One` 均被显式保留，§9 的 L0 A/B/C/D 四选项也没有被静默选定。它不需要回滚。

但它有两类问题需要后续处理：(i) 源记录把若干 machine consolidation 以“作者已接受”的强度写入，却没有保存接受事件，且在“gating 属于哪一层”“object 是认识切分还是世界侧组织”上内部不一致；(ii) 调和计划与**已在 STATUS §2 中处于控制地位**的 Spine restoration 契约在同一组 Freeze-A owner 上给出了相反的落地顺序与冲突的阶段编号。在修订前，P 不应被当作 C 类执行契约使用。

## 2. 通过项（保留）

- **防线清单完整**：S §21 非主张清单与 S §22 landing status 准确；P §7 A–H 验收测试方向正确（尤其 A no-chooser、B no-warehouse、C occurrence boundary、H 独立复审）。
- **Ĝ / L0 基本护栏正确**：S §7 与 L0 l.117–119、l.422–424、Spine l.200–203、Core21 l.254–256 一致。
- **L0 “改变”未被静默选定**：S §9 把 “altered L0” 拆成 A/B/C/D 四种读法并留 OPEN，符合 `CONTINUE_DIRECTIONAL_ACCEPTANCE` 例外 2（未选择的互斥分支）。
- **词源更正正确**：information < *informare*（*forma*），inflammation < *inflammare*（*flamma*），二者无词源同一性；S §13 的更正准确。
- **emergence 批评有度**：S §15 只主张“贴标签不付 formation 负担”，没有主张 emergence 为假。
- **first Selection 诚实留 OPEN**：S §17 没有用 chooser / 神意 / 完备 L0 填洞。
- **隐私处理得当**：自传 / 心理自我分析被明确排除。

## 3. Findings（按严重度排序）

### F1 — 高：P 的落地顺序与现行 Spine restoration 契约相反，且阶段编号三重冲突

**证据。**
- 现行契约 `SPINE_SEMANTIC_THINNING_AUDIT` §14.0（l.804–842）/ §14（l.848–860）：**local-owner-first**——Phase **C1** = `SRT_L0_Metaphysics.md` + `_SRT_SYMBOL_TABLE.md`，Phase **C2** = Spine；并要求“no half-landed canonical main state”。STATUS §2 把该审计列为 ontology / canonical 编辑的控制路由第 2 项。
- P §5（l.348–417）：Stage **C1 = Spine 先行**，理由为“must decide … before local owners are edited”；Stage **C2 = L0**。顺序与理由都与现行契约相反。
- P 内部又用 C1–C8 命名 §3 的冲突项（l.115–263），与 §5 的 Stage C0–C5 同名；加上 Spine 审计的 Phase C1/C2，“C1”在三处指三件不同的事。
- P 把 Spine 审计列为 dependency，却没有写两份契约如何组合（先后？合并为一个包？谁优先？）。

**风险。** 两份未来 C 类契约覆盖同一组 Freeze-A owner（Spine、L0，且都会触及 Symbol Table），执行者可能按 P 的顺序先改 Spine，直接违反控制契约的 local-owner-first 与 no-half-landed 条件。

**修复。** [A-3] 作者裁决 P 与 Spine 审计的关系；评审建议：P 明确**从属于** Spine restoration 契约（其负担作为该包的附加 OPEN / 冲突项并入，或在该包完成后再开），采用 local-owner-first；机械上把 P 的冲突项改名（如 `PV-K1…K8`）、阶段改名（如 `PV-S0…S5`），消除与 Spine 审计 C1/C2 的碰撞。

### F2 — 高：“Selection = gate act”在 primitive 层与 L0 / Spine 冲突，且 Maxwell 妖类比按物理读法反而支持 formed-level gating

**证据（内部不一致）。**
- S §6（l.195–245）标题与结论：“Selection is the gate act”“Selection is closer to the actual opening / closing of generative passage”，不加层级限定。
- S §14 kernel（l.496–523）：`generative openness -> Selection / gating -> …`，把 gating 放在 primitive 位置。
- 但 S §8（l.276–312）与 S §17（l.590–622）给出两阶段：primitive Selection 不需要 prior expectation；gating 是 `structural expectation -> expectation-mediated gating of later Selection`。作者 A0-Q 3 本身也说 operator “通过**预期**改变对象可以形成的 l0”——即 gating 由带预期的已形成 operator 执行。

**证据（与 canonical 的张力）。**
- 类比链条 `ongoing dynamics -> a gate is opened / closed -> differential passage` 预设了：(a) 独立于 Selection 的既有流动；(b) 既有的隔板与通道；(c) 隐含的分拣判据（快 / 慢）。
- L0 核心主张（l.28）：reality **is** Selection under a non-flat, non-preclosed mode；determinate actuality 不是外在于它的产物。若 Selection 是对既有动力学的“开关”，就重新引入了“底物动力学 + 调制它的 Selection”这种二元结构。
- L0 S0（l.174–180）：primitive 层不得预先给出 A/B 菜单、权重、概率、目标或 chooser——(b)(c) 正是预给的 A/B 分区与目标。
- Spine（l.165–174）：actualising Selection event = determinate manifestation = relative backgrounding = event-level verticality，是同一事件的诸读法，而非对既有流的调节。

**证据（物理读法）。**
- 在 Maxwell 的原始思想实验里，门的开合**以对单个分子的测量为条件**：通过门来实现的恰恰就是对分子的分拣。Szilard / Landauer / Bennett 以来，热力学上起决定作用的是信息获取与记忆擦除，而门本身被理想化为无成本。
- 没有信息耦合的被动门（Smoluchowski trapdoor、Feynman ratchet）在平衡态下**不能**产生冷热分离。

所以按准确读法，这个类比支持的是 **formed、带测量 / 预期耦合的 gating**——即 09-20 typing 的 C0/C1 层，以及 Live Term Router l.117 已把 gating 列为 “support” 别名的那一层——而不是 primitive Selection。S §6 的 hard guard `!= observing demon required for primitive Selection` 承认了其中一部分，但仍把“开关门”称为 decisive action。

**修复。** [A-1] 作者二次裁决 gating 的层级。
- **G1（评审推荐）**：gating = formed / recurrent / expectation-mediated 的 Selection 组织（Ĝ 型 realization、C0/C1），primitive Selection 不是对既有流的 gating。改写 S §6 标题 / 结论与 S §14 kernel 的 primitive 槽位。
- **G2**：保留 primitive gating，但必须给出“在没有预给流、隔板和判据的情况下，被 gate 的是什么”的说明，并对 L0 l.28 / l.180 付清兼容性负担。

评审补充（M，仅供参考）：Smoluchowski 教训可以被建设性地读成“单靠门本身产生不了不对称；不对称需要背景已经是非平的”——这与 L0 的 non-flat 主张同向，也许比“Selection = 门”更贴近作者要的东西。P 的 C1（l.115–143）问对了问题，但应补上 (a)(b)(c) 预设与测量判据两点。

### F3 — 高/中：provenance 强度被抬高——“作者已接受”没有保存接受事件，也没有逐条 A0-Q / A0-P / A1 / M 标注

**证据。**
- S l.51：“The author subsequently explicitly accepted the machine-side analysis that refined these intuitions …”——整体断言，没有引文。
- 分节强断言：S §1 l.57 `AUTHOR-ACCEPTED direction`；S §5 l.187 “The author accepts the stronger reading”；S §16 l.571 “author-accepted machine consolidations”；S §19 l.677 “The author accepts the post-case2 contraction”。
- Phase 3 map D1（l.312）是作者裁决：没有保存逐条作者措辞或明确接受事件的 machine 措辞 = **M**；record-level directional acceptance 可以注明，但不升级逐条 provenance。§9（l.327）建议未来的作者裁决记录逐条标注，且 A1 必须有记录在案的接受事件。
- `CONTINUE_DIRECTIONAL_ACCEPTANCE` §5：即便是裸“继续”，也只构成 package-level directional acceptance，`!= every prior sentence becomes A1`。
- 同日的兄弟文件 `SRT_AUTHOR_ROUTING_GRG_CROSS_OBJECTIFICATION_ROOT_RETURN_2026-09-24.md` §1–§2 展示了正确做法：保存了“认同，继续”原文，并标注 `[A1 — explicit acceptance …]`。
- S §8 “The stronger reading is retained” 继承自 09-22 §F，而 Phase 3 map（l.134）已把它定为 **M**。

**风险。** 后续 session 会把 S §5 的更强读法、S §16 的神性 consolidation、S §19 的收缩当作 A1 强度的作者裁决来引用。

**修复。** [A-4] 如果接受事件存在，补上接受原文（A0-Q）并逐节标 A1；否则逐节改标 M，并注明 record-level directional acceptance。加一张逐节 provenance 表（机械工作，但需要作者确认哪些接受事件真实存在）。

### F4 — 中高：神性 consolidation 可能置换了作者原意——把“维持”换成“不可穷尽”

**证据。**
- 作者 A0-Q 7：「……在所有selection中一直持续的一种**使我们维持并持续维持的力量**。」其核心是维持 / 持续。
- 作者 A0-Q 4：「存在比切片对象多出来的是这种稳定性，这种粘性glue……而这是传统科学所忽略的，**神学神秘化的东西**。」作者在这里把 glue / 稳定性与“神学所神秘化的东西”连在一起。
- S §16 的“safe stronger reading”改成了 `No determinate formation exhausts the generative reality`，以及「神性不是使万物不死的力量，而是任何已成之物都不能垄断生成的能力」——重心从**维持**移到了**不可穷尽 / 非封闭**。
- P C8（l.263–286）自己也在问这是否已被 L0 non-preclosure（L0 l.28）完全承载；果真如此，这条 consolidation 就把作者的直觉压缩成了一句现有 canonical 语句，同时丢掉了“维持”那一半，并切断了作者自己建立的 glue ↔ 神性联系（glue 落在 S §10，神性落在 S §16，两节互不引用）。

**另一种符合护栏的读法（评审 M 建议）。** 维持不是惯性：凡是得以延续的，都经由持续的 Selection 被重新实际化。这种读法不涉及生存驱力或延续偏好，因此与 S §16 的全部 hard guards 相容，并直接连到 One Formation 的 vertical reconstitution（l.80–82）。邻居：Descartes 的 conservation = continual creation（*Meditation III*）；occasionalism 的逐刻再造；Whitehead 的 perpetual perishing / concrescence。

**修复。** [A-2] 在 S §16 把两种读法并列保留 OPEN——D-maint（维持即持续再生成；路由到 P C4/C6 与 glue）和 D-inex（不可穷尽；路由到 P C8 与 L0）——交作者二次裁决，而不是只保留 D-inex 为“safe reading”。

### F5 — 中：“object”在认识切分与世界侧组织之间滑动；“horizontal causality”同样滑动

**证据。**
- S §3（l.110–142）继承 09-22 §B：`object = a cognitive / research binding of relations`（认识侧）。
- S §10 l.387：“an object is a local organization that has acquired enough recurrent generative coherence to remain an effective unit across change”；S §20：“Objects are downstream stabilized organizations”（世界侧）。
- S §2 l.95 粗体 “Horizontal causality is downstream of object formation”，而同节标题称之为 “effective discretization”（描述侧）。
- `SRT_AI_START.md` §8 明确要求 `world-side formation / manifestation / persistence != epistemic-public objectification / representation`。
- S §15 自己也区分了 cut（认识）与“使 cut 追踪到稳定之物的世界侧组织”，但全文没有把这一区分贯彻为术语。

**修复（机械，无需作者裁决）。** 在 S 中显式区分 `object-cut`（认识 / 研究切分）与 `formed unit`（世界侧稳定组织，是否等同于 One 仍 OPEN）；把 “horizontal” 标为已对象化的描述体制（description regime），而不是与纵向 Selection 并列的另一种世界侧因果。

### F6 — 中：与 GRG v0.3 §4.3 和 stop-loss 教训之间的张力未被标出

**证据。**
- 作者 A0-Q 1「……而不是通过切片或是涌现这种半成本来解释」、A0-Q 4「这是传统科学所忽略的」，逼近一种“horizontal 表示付不起”的主张。
- v0.3 §4.3（l.196–212）：“A sufficiently rich horizontal model may encode every variable used in a vertical analysis … Verticality is therefore not a variable ontology.”
- S §3 却称 `given -> reopen` 只是“methodological entry move, not the full vertical ontology”，把 verticality 从 v0.3 的问题相对研究关系推向世界侧本体。S §21 的非主张清单覆盖了“mature science ignored …”，但**没有**覆盖 unrepresentability。
- case2 no-GRG ablation §6–§7：`ordinary causal / systems analysis: sufficient to recover the major seams`；GRG 幸存的价值是 checklist / governance / vocabulary。
- S §19 的 8 步方法中第 3–6 步，正是两次得出 `SOURCE_OWNED_DECOMPOSITION_NO_GRG_GAIN` 的那种分解；S §19 称其为收缩，同时把目标加深为“object-formation grammar = deeper target”。
- case2 result §16（l.875–888）给 CURRENT NEXT 列了四个问题（哪些 cut 作为内部 SRT / 哲学组织仍有用；哪些只是通用因果 / 系统分析；保留什么作为治理纪律；撤回 / 收窄 / 留 OPEN 哪些跨域科学独特性主张），S §19 一个都没有回答。

**修复（机械）。** S §21 加一条非主张：“no unrepresentability claim beyond GRG v0.3 §4.3”；S §19 按 case2 §16 的选项给收缩后的 GRG 定型（内部 SRT / 哲学研究组织，vs 科学主张），并写明本记录**服务但不执行** CURRENT NEXT；第 8 步补上 case2 §15 的 LLM 先验控制（same-model no-GRG control、作者先冻结预测、私有目标）。

### F7 — 中：不可路由（orphan）

**证据。** 在 01faf40 上 grep 两个新文件名，除它们互相引用外，没有任何入链（STATUS、`_SRT_CONTEXT_ROUTER.md`、Live Term Router、Context Bundles 都没有）。STATUS §0 landing ledger 和 §0.4 均未提及。先例：#1047（同类：noncanonical direction + future C-class contract）在 STATUS ledger 中有 role 行，并进入了 §2 控制路由。`_SRT_AGENT_RETRIEVAL_PROFILE.md` §0.1 要求被接受的分析 `must remain routeable`；`AGENTS.md` 的 merged-handoff 规则要求 fresh session 能从 `main` + STATUS 推出执行交接。

**修复（机械）。** 在 STATUS §0 ledger 加一行 `#1055 = MERGED / 01faf40… ; role = NONCANONICAL SOURCE + FUTURE C-CLASS CONTRACT; serves (does not execute) CURRENT NEXT; owner-cleanup pause unchanged`；在 Live Term Router 登记 working labels（见 F8）。仅在 F1 裁决后才考虑把 P 放进 STATUS §2。

### F8 — 中：术语碰撞与未路由的既有负担

1. **gating**：Live Term Router l.117 已把 `gating` 列为 `support` 的别名（OVERLOADED_SAME_NAME）；S §6 把它用作 Selection 本身——新增一种同名异义。
2. **vertical**：已有的含义至少包括 One Formation Def-OF-1（l.56–74，Selection 生成的非平 foreground / background；event-level verticalization）、Spine l.172 `event-level verticality as structural reading`、09-22 §C–§D（稍后形成的闭环 vertical structure）、v0.3 §4（vertical research）。S §1 又新增“under the object cut / pre-object”一义。S 与 P 都**没有引用 Def-OF-1**。
3. **glue**：与 09-22 §D（`vertical structure = proxy + support + stability through friction / homeostatic reconstitution`）、§H friction、§I support、One Formation 的 vertical reconstitution 大面积重叠；也没有接上 09-10 §2 作者自有的稳定性轴（`more stable Selection = cross-time / space / position / subject selectability`）——该文件被列为 dependency，但其稳定性定义没有被使用。此外，“glia”源自希腊语 γλία（胶），Virchow 称之为 *Nervenkitt*；神经科学后来抛弃的正是这个被动胶水图景，而 “glue” 一词会把这种被动含义带回来，与作者要的“主动维持”相反。
4. **plain `G`**：S §7 标题与 l.261 “G names a formed / formal / domain-level realization of selective gating”。Symbol Table l.34：`Ĝ` 是 “role-carrier for a declared Selection realization … **Never use plain `G` for this**”。S 既用了 plain G，又把 Ĝ 收窄为 “selective gating” 的载体。（作者 A0-Q 中的「选择算子G」属于引文，保留原样即可。）
5. **structural expectation**：Phase 3 D3 要求 expectation 对齐 09-20 的 B + C0/C1 typing，并区别于 `E_G`（STATUS guard `structural / operative generative expectation != E_G automatically`）。S §8 与 P C5 都没有接这两处路由。

**修复。** 1、2、3、5 按 `AGENTS.md` 的 new-term rule 分类（alias / overloaded / partial overlap / distinct），写进 P §6；机械修复：4 把 machine prose 中的 plain G 改为 `Ĝ` 或 “formed gating organization”，并撤回“Ĝ = gating 载体”这一收窄。

### F9 — 中低：整体盈余的“更强读法”悄悄收窄了 09-10 的 OPEN

S §5 l.187–190：“the Whole is partly constituted by that stabilized organization”（作者接受，但无事件证据，见 F3）。09-10 §7 把 `whether whole-level surplus is ontological, causal, modal, explanatory, or several of these` 列为 OPEN / REQUIRES AUDIT；S §5 实际上选了“构成性 / 本体论”一支，却没有声明这是在收窄该 OPEN，也没有把 “Whole” 映射到 One / collective One。

**修复。** 注明这是对 09-10 §7 OPEN 的收窄候选（provenance 按 F3 处理），并把 Whole ↔ One / T-COLL-1 的关系加入 P C7。

### F10 — 中低：S §12–§13 的神经免疫段落有“后门开领域”的风险，且问题已被邻居支付

- S §13 l.479 把 “The stronger GRG/SRT question: when does inflammatory information processing … rewrite the future conditions …” 写成 GRG/SRT 问题。这恰好就是 trained immunity、endotoxin tolerance、metaplasticity 正在研究的问题（P §4 自己也列了 metaplasticity / trained immunity）。在 fusion lane 暂停期间用 GRG 词汇重述它，重复的是 case1/case2 的模式。
- S §12 l.437 的前提（“不应假设只有 spike 才有认知价值”）在今天的神经科学里是主流（tripartite synapse；microglia 介导的突触修剪），S §21 的非主张清单没有专门覆盖这一点。

**修复（机械）。** 在 S §12–§13 加 guard：不开神经科学 / 免疫学 case 或 deep well（fusion lane PAUSED、third domain NO；Neuroscience pilot well 的既有结果保留）；并把这些问题标为 neighbor-paid。

### F11 — 低中：邻居包缺少若干直接对口的邻居

S §18 / P §4 已有的清单方向正确，但针对 #1055 的具体新负担，至少缺以下几项：

| 新负担 | 缺失的直接邻居 |
|---|---|
| S §4 组织不是又一个部分 | Aristotle *Metaphysics* Z.17 音节论证（BA ≠ B + A；形式若是又一元素则无穷后退）；Bradley 关系后退 |
| S §16 “生成永远大于已经生成之物” | Spinoza *natura naturans / natura naturata*（S 只在 conatus 处引 Spinoza）；Stuart Kauffman *Reinventing the Sacred*（God as creativity） |
| gating + glue + whole surplus | Deacon *Incomplete Nature*（constraint / absential / teleodynamics）；Juarrero enabling constraints；Pattee（constraint vs dynamics，正对 F2 的二元问题） |
| expectation 塑造边界维持 | Friston FEP / Markov blankets（expectation + 边界维持 + object 边界；评审认为这是最强的遗漏） |
| altered reachability / L0 选项 A | Kauffman adjacent possible |
| Maxwell 妖类比 | Szilard / Landauer / Bennett；Smoluchowski trapdoor / Feynman ratchet（见 F2） |
| D-maint 读法 | continuous creation / occasionalism / Whitehead perpetual perishing（见 F4） |

### F12 — 低：kernel 的箭头把 L0 读成先行阶段

S §14 `generative openness -> Selection / gating -> …`。Symbol Table l.27：L0/L1/L2 是 analytic / model-facing aspects，“not … a compulsory three-stage product pipeline”；Spine：“readings of the same event, not successive universal operations”。**修复（机械）**：在 kernel 下加一行 aspect guard（09-20 §2 已有同类说明：箭头是依赖 / 重构箭头，不是时间序列）。

### F13 — 低：“first Selection”预设了时间起点

S §17 l.594 的问法默认存在时间上的第一次 Selection。在 Selection-totality 下，依赖箭头不是时间箭头（09-20 §2 l.80）。**修复**：把 grounding 问题（为什么有非平的实际性）与 temporal-first 问题分开；后者在当前本体下可能是不适定的，应作为 OPEN 的一部分注明。

### F14 — 低：P 的其他遗漏与小误

- 按 C 类交叉检查（Edit Protocol l.63–67）应纳入的 owner 缺三个：`_SRT_SYMBOL_TABLE.md`（Ĝ、Ĝ†、L0 行）、`CANONICAL_REGISTRY.md` 回链、`Core_Law/SRT_Irreversibility.md`（retained historical efficacy 的 owner，直接关系到 C4）。C4 也没有考虑 `Ĝ†` gated writeback。
- §7 验收测试缺 “no half-landed main” 合并条件（见 F1）。
- P §1 l.66 说“前两步已由 S 与本计划开始”，而 P §5 Stage C0 又说 conflict / OPEN map 尚待建立——两处自相矛盾。
- P §1 l.55 把 “author second adjudication -> independent review” 归到 same-day guard 名下；Edit Protocol l.83–102 的 same-day guard 只规定 `record -> bounded conflict / OPEN map -> only then consider landing`，另外两步分别来自 `AGENTS.md` 的 Constitution / Ontology Dialogue Hard Guard 与 C 类 pre-merge 独立复审（l.69–79）。实质无害，但引用应更正。

## 4. 需要作者二次裁决的事项

```text
A-1  gating 层级（F2）：G1 formed / recurrent / expectation-mediated only（评审推荐） | G2 primitive gating + 兼容性负担
A-2  神性读法（F4）：D-maint 与 D-inex 并列 OPEN | 选定其一 | 二者关系另议
A-3  P 与 Spine restoration 契约的关系（F1）：从属 / 合并为一个包（评审推荐 local-owner-first） | 反序并给出理由
A-4  S §1 / §5 / §16 / §19 的接受事件（F3）：提供原文 -> A1 | 无 -> M + record-level directional acceptance
```

## 5. 无需作者裁决的机械后续（建议合成一个 bounded follow-up PR）

```text
F3  逐节 provenance 表（A-4 回答后再填）
F5  object-cut / formed unit 术语区分；horizontal = description regime
F6  S §21 加 no-unrepresentability 非主张；S §19 定型 + “服务但不执行 CURRENT NEXT” + LLM 先验控制
F7  STATUS §0 ledger 行 + Live Term Router working-label 条目
F8  plain G -> Ĝ / formed gating organization；gating / vertical / glue / expectation 按 new-term rule 分类并写入 P §6
F10 S §12–§13 no-domain-opening guard + neighbor-paid 标注
F12 kernel aspect guard
F14 P owner 清单补 Symbol Table / Registry / Irreversibility；§7 加 no-half-landed；§1 自相矛盾与 guard 归属更正
F1  P 冲突项 / 阶段改名（顺序本身待 A-3）
```

## 6. 保持 OPEN（本评审刻意不关闭）

- genuine actualised Selection 与 merely descriptive / modelled change 的判据（anti-tautology）；
- “altered L0” 的 A/B/C/D；
- glue 是否构成独立负担，还是既有 vertical reconstitution / support / friction 家族的别名；
- structural expectation 在 One 之前、之时还是之后；
- whole-level surplus 的本体地位；
- 神性的两种读法；
- scientific distinctiveness = NOT ESTABLISHED；
- BCTB T2 = HOLD；third fusion domain = NO；GRG v0.4 = NOT AUTOMATIC；further owner cleanup = PAUSED BY DEFAULT。

（§6 中“whole-level surplus 的本体地位”与“神性的两种读法”两项已被 §7 的作者裁决部分收窄 / 选定。）

## 7. 作者二次裁决后的处置（2026-09-24）

作者对 §4 的四项作出了回答，原文与处置见 `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_PR1055_REVIEW_SECOND_ADJUDICATION_2026-09-24.md`：

```text
A-1 「组织，作为选择算子的actualize」
    -> D-1：gating = formed organization，作为 Ĝ 角色的 actualization；primitive Selection != 对预给流的 gating
    -> 与评审推荐的 G1 同向；F2 在 source 层 RESOLVED
A-2 「……我觉得生成性更合适一点」
    -> D-2：生成性读法获作者明确认可（A1）；“维持”仅作来源 provenance
    -> 评审提出的 D-maint 替代读法被作者选择关闭；F4 RESOLVED
A-3 「先优化Spine，然后优化Canonical。这次对话作为canonical 优化的重要材料」
    -> D-3：Spine 先行，其次其他 canonical owner；#1055 是 canonical-owner 阶段的材料
    -> 评审关于 local-owner-first 的推荐未被采纳（作者裁决优先）；no-contradiction 合并条件作为 guard 保留
    -> F1 RESOLVED（顺序由作者裁决确定；标签碰撞已通过 PV-K / PV-S 改名消除）
A-4 「有」
    -> D-4：S §1 / §5 / §16 / §19 = A1（证据为作者追认）；其余节按 S §0.1 表
    -> F3 RESOLVED；F9 随之定性为作者接受的 OPEN 收窄
```

同一 follow-up 中已落地的机械修复（这些修改由后续 commit 执行，本评审正文本身仍然只读）：

```text
S：§0.1 逐节 provenance 表（F3）；§1 vertical 术语路由（F8）；§2 horizontal = description regime + no-unrepresentability（F5 / F6）；
   §5 D-4 注记（F9）；§6 标题与 D-1 层级 typing + 物理注记（F2）；§7 plain G -> Ĝ，且不把 Ĝ 收窄为 gating（F8）；
   §8 09-20 B+C0/C1 路由与 E_G guard（F8）；§10 object-cut / formed unit + glue 重叠与 Nervenkitt 注记（F5 / F8）；
   §12–§13 no-domain-opening guard（F10）；§14 保留原 kernel 并补 D-1 修订版 + aspect guard（F2 / F12）；
   §16 D-2 注记；§17 grounding vs temporal-first（F13）；§19 服务但不执行 CURRENT NEXT + stop-loss 证据 + LLM 先验控制（F6）；
   §20 / §21 相应补句与非主张
P：D-3 顺序说明；PV-K / PV-S 改名（F1）；§1 guard 归属与自相矛盾更正（F14）；PV-K1 / K4 / K5 / K7 / K8 处置注记；
   §4 邻居补充（F11）；PV-S1 改为“Spine 阶段后核验”，不另行重写 Spine；PV-S2 补 Symbol Table / Registry（F14）；
   §6 术语初步分诊；§7 测试 A 补 D-1、新增 I（no contradictory main）与 J（C 类交叉检查）；§9 处置更新
STATUS：§0 ledger 增 #1055 与作者顺序行；§2 增 author sequencing 块（F7）
Spine restoration audit §14.0：顺序被作者裁决取代的指针（保留 no-half-landed guard）
Live Term Router §4：gating / pre-object vertical inquiry / glue / generative divinity 四行（F7 / F8）
```

更新后的 verdict：

```text
S — SOURCE FIDELITY + PROVENANCE TYPING      = PASS (after follow-up)
S — INTERNAL CONSISTENCY                     = PASS (after follow-up)
P — AS FUTURE CANONICAL-OWNER-STAGE CONTRACT = PASS FOR SEQUENCING; exact owner wording still pending PV-S0 + C-class review
ROUTEABILITY                                 = PASS (STATUS + router)
CANONICAL IMPACT                             = NONE (no Freeze-A owner edited)
EXECUTION                                    = NOT STARTED; requires explicit author instruction
```
