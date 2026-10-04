---
id: SRT-PR1099-PREOBJECT-UNFINISHEDNESS-SACRED-SPIRITUALITY-INDEPENDENT-CONTENT-REVIEW-20261004
type: audit
status: active
date: 2026-10-04
layer: governance
epistemic_layer: operations
claim_mode: independent_review
canonical: false
research_mode: U
comparative_claim: none (review only)
named_comparator: "see §3 F7 table"
n_mode_triggered: false
dependency:
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_PREOBJECT_UNFINISHEDNESS_SACRED_SPIRITUALITY_2026-10-04.md
  - Operations/Proposals/SRT_PREOBJECT_UNFINISHEDNESS_SACRED_SPIRITUALITY_BOUNDED_RESEARCH_ROUTE_2026-10-04.md
  - Philosophy/hooks/PH_CONSC_Gate_Geometry_Bearer_Ontological_Friction_Phenomenal_Admission_Hook_2026-09-25.md
  - Philosophy/hooks/PH_CONSC_Minimal_Phenomenal_Topology_Foreground_Mediated_Position_Reconstitution_Hook_2026-09-26.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_MUSIC_CHANGE_PHENOMENAL_VERTICAL_GENERATION_2026-09-29.md
  - Neuroscience/patches/SRT_Neuro_NEURAL35_Psychedelic_Reopening_Reanchoring_v0_1.md
  - Operations/Audits/SRT_DREAM_PSYCHEDELIC_MATURE_NEIGHBOR_CONTINUATION_AUDIT_2026-10-04.md
tags: [IndependentReview, PR1099, PreObject, ProspectiveMemory, Unfinishedness, CoarseGraining, HPB, Bearer, Sacredness, Spirituality, EgoDissolution, CrossDomain, CPsi]
---

# PR #1099 独立内容评审 — 未完成方向 / 统一粗粒化 / 神圣与灵性 bounded route

> **角色**：对**未合并（draft）**的 PR #1099 做合并前独立内容评审。只读：本记录不修改 #1099 的任何文件、STATUS、路由面、HP-B 冻结包或 canonical owner，也不替作者关闭任何 OPEN。
>
> **评审者独立性**：独立 session，没有参与 #1099 的作者对话或写作。
>
> **评审局限**：原始对话不在仓库中，A0-Q 的逐字性和逐项“Author ruling”的接受事件无法核验。两份新增文件**全部通读**；canonical / domain owner 与既有审计只读相关节，并在各发现中注明行号（行号均以 base `30ba40e0` 为准）。外部文献按评审者知识引用；其中 Ghibellini & Meier (2025) 与 Metcalfe & Wiebe (1987) 两项在本 session 经检索核对，其余为该领域标准文献，未逐条复核。外部文献只作为邻居压力，不作为 SRT 证据。

## 0. 评审对象

```text
PR:    #1099 (OPEN, draft) “research: unfinished direction, unified coarse-graining and sacred/spiritual route”
head:  3f0996a9   base: 30ba40e0 (= #1098 merge)
commits: 75a7ce9 (source record) -> 3f0996a (bounded route); 2 files, +838 / −0
CI:    governance-preflight = success

AJ = 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_PREOBJECT_UNFINISHEDNESS_SACRED_SPIRITUALITY_2026-10-04.md (406)
RT = Operations/Proposals/SRT_PREOBJECT_UNFINISHEDNESS_SACRED_SPIRITUALITY_BOUNDED_RESEARCH_ROUTE_2026-10-04.md (432)
```

控制 owner / source（只读相关节）：

- `AGENTS.md` l.33（new term / working-label rule）、l.55（Hard Guard：先回收既有 source intuition）、l.58（U/N-mode 记录字段）、l.61–63（local no-gain / same-target / claim-state 三条）；
- `STATUS.md`：l.93（A-9）、l.135（`pre-object != pre-sensory or contentless`）、l.260（cognition result 不得作 O0 证明）、l.334–435（HP-B 冻结，l.404–410 冻结期允许 / 禁止事项）、l.564–571（A0-Q / A0-P / A1 / M）、l.581（`constitutive / boundary friction != Psi_f automatically`）、§6 l.753、§7 l.778–795、§8 l.797–830；
- `Core_Law/SRT_L0_Metaphysics.md` l.29；`Core_Law/SRT_Generative_Ontology_Spine.md` l.138；
- HP-B 冻结 hook：gate-geometry hook §2 C1–C7（l.59–210）、F1（l.484）、Still OPEN（l.524–531）；minimal-topology hook l.171、l.198、l.479；
- `Glossary/SRT_Live_Term_Router.md` l.107（objectification）、l.136（gate geometry）；
- 音乐包：`…MUSIC_CHANGE_PHENOMENAL_VERTICAL_GENERATION_2026-09-29.md` A7（l.254–）、A11（l.356–410）；修正案 `Governance/SRT_GOV_AUTHOR_REENTRY_ONTOLOGY_RECONSTRUCTION_AMENDMENT_2026-09-05.md` §10.2（l.673）；
- 认知程序 `Operations/Proposals/SRT_PREOBJECT_GENERATIVE_ORIENTATION_COGNITION_RESEARCH_PROGRAM_2026-09-26.md`：l.80–90（Facing v0.3 promotion gate）、l.122（冻结的 consequence-feedback discriminator）、CN-5 l.1274、S4 l.1296；
- Spirituality domain（P3/P5，非 canonical，`SRT_Spirituality_Claim_Status.md` l.18）：Spirit_01 l.62–72、l.347–353；`_SRT_Spirit_Axioms.md` §5 l.294–、§6.1 l.329–；Spirit_02 l.57–67；Spirit_03 l.49–70；Spirit_04 l.97–101、l.495；`SRT_Spirituality_Selection_Pathology_and_Return.md` l.48–52；
- `Neuroscience/patches/SRT_Neuro_NEURAL35_Psychedelic_Reopening_Reanchoring_v0_1.md` l.49、§4 l.217、§6 l.274–295、§7 l.300–；
- 同日已合并：`Operations/Audits/SRT_DREAM_PSYCHEDELIC_MATURE_NEIGHBOR_CONTINUATION_AUDIT_2026-10-04.md` §9 l.453–467；`01_Source_Intuition/SRT_AUTHOR_ROOT_RETURN_POWER_CROSS_POSITION_GENERATIVITY_2026-10-04.md` l.103；
- CΨ：`Core/SRT_OPEN_TENSIONS.md` l.48 / §18；`Operations/_SRT_REVIEW_QUEUE.md` l.33（RQ-2026-08-A05）；
- 既有评审：`Operations/Audits/SRT_PR1058_GATE_GEOMETRY_QUALIA_INDEPENDENT_CONTENT_REVIEW_2026-09-25.md` l.240（coarse-graining 邻居映射）。

## 1. Verdict

```text
CI governance-preflight                                   = PASS
CANONICAL IMPACT (file edits)                             = NONE
STATUS / CURRENT NEXT                                     = UNCHANGED ✓
HP-B FILES                                                = UNTOUCHED ✓
METAPHYSICAL OVERREACH GUARDS (AJ §15 / RT §18)           = GOOD
NECESSITY vs SUFFICIENCY SEPARATION (AJ §3)               = EXPLICIT ✓

INTERNAL SOURCE RECOVERY (sacred / ego / reopening)       = NOT DONE; parallel and partly conflicting accounts (F1)
“unified bearer-relative selective coarse-graining”       = RE-EXPRESSES FROZEN HP-B C1–C6 + a unity condition;
                                                            quarantine is formal only (F2)
CONSCIOUSNESS-NECESSITY CLAIM                             = NO FALSIFIER IN ROUTE; report-confounded; IIT exclusion unpaid (F3)
BEARER TYPING                                             = CONFLICTS WITH STATUS §6–§8 GUARDS (F4)
PRE-OBJECT / O0 TYPING                                    = CONFLICTS WITH STATUS l.135; felt direction lacks O0 guard (F5)
CROSS-DOMAIN GRAMMAR                                      = RE-RUNS A11 POST-HOC INVARIANT WITHOUT A11 / §15.5 / §10.2 GUARDS (F6)
MATURE-NEIGHBOR SUBTRACTION                               = SEVERAL JOBS SOURCE-OWNED; two candidate discriminators survive (F7)
“energy potential” / Ψ_f / CΨ                             = TYPING LEFT OPEN IMPLICITLY; existing CΨ author gate bypassed (F8)
ITEM-LEVEL PROVENANCE                                     = MISSING (F9)
ROUTING / FRONTMATTER                                     = ORPHAN FILES; U/N-mode fields incomplete (F10)

RECOMMENDATION                                            = REVISE BEFORE MERGE (content level)
```

本 PR 不含 C 类 canonical semantic edit，edit protocol 的独立复审门不强制适用；REVISE 是内容建议，不是合并阻断规则。

## 2. 优点

- **治理反射正确**：两份文件都不碰 canonical、STATUS、HP-B，也不新开 CURRENT NEXT；RT §14 明确自己是认知 CURRENT NEXT 的 companion。
- **AJ §3 把必要性与充分性分开写**，并主动指出 integration / broadcast / AI gating 不能单独推出意识。
- **局部闭合 ≠ 全局闭合**（AJ §7）这个区分是对的，“住院费”例子清楚。
- **“exclusion ≠ deletion”**（AJ §4）与 HP-B C3/C4、router l.107（objectification “not automatically an error”）一致。
- **“反思 = 再对象化，不是透明回放”**（AJ §6）是正确的默认立场。
- **硬护栏清单**（AJ §15、RT §18）覆盖了主要形而上学越界路径：awe/神秘体验证明 SRT、神圣性证明超自然实体、主观强度 = Ψ_f、局部闭合 = 全局 `Ψ_f→0`。
- **RT §13 采用 `NO LOCAL COMPARATIVE INCREMENT` 措辞**，符合 AGENTS l.61。
- **RT §17 失败条件具体**；RT §10 的反向模式（特殊状态强度上升而关怀变窄、可修正性下降）是真正的不利判据。
- **RT §4 的真 / 假候选对照**是整包最有希望的判别实验（条件见 F7）。
- **入口现象选得好**：前瞻记忆中“知道有事 / 不知道是什么”的分离成本低、自然、可以有 ground truth。

## 3. 发现

### F1（高）没有回收既有 SRT 内部来源：神圣、自我消融、重开三块已有 owner，且部分冲突

AGENTS l.55 要求先回收既有 source intuition 再提出方案。AJ / RT 的 dependency 只列了 `Selection_Pathology_and_Return`，以下既有内容都没有引用：

| PR 条目 | 既有 owner（行号） | 关系 |
|---|---|---|
| AJ §9 神圣 = 非中立性超出当前局部对象化所能吸收的范围 | Spirit_01 Def-Spirit-2 l.62–66（Sacred = L₀ overflow 饱和 L₁ 概念边界，`S_φ ≫ 1`）；Axioms §5.1 l.294–308（Otto tremendum / fascinans = L₀ 饱和）；Spirit_03 Ax-Awe-1 l.49–64（震悚 = 约束崩解时的潜能过载） | 同一解释任务。PR 把机制从“溢出 / 饱和”换成“选择性统一”，两者对 coherence 的预测方向不同。**CONFLICT，需要类型化** |
| AJ §10 对象只是更大关系的局部切片 | Spirit_01 Def-Spirit-3 l.68–72、Axioms §5.2 l.310–（偶像 = 不透明 L₁ 接口，圣像 = 透明窗口） | **INHERIT / RETYPE** |
| AJ §11 自我消融 ≠ Bearer 消融 | NEURAL35 §6 l.274–295（`ego dissolution ≠ subject dissolution ≠ bearer dissolution`，并写明“not a claim that subjecthood necessarily persists”“retrospective reports alone cannot establish literal subject absence”）；Axioms §6.1 l.329–（合一的非融合性）；Spirit_02 Ax-Trad-4 l.57–61（Fana = `Center(d) → ∅`） | NEURAL35 已拥有这一区分，应 **INHERIT**，包括它的不对称谨慎；Fana 读法须登记为 **CONFLICT** |
| AJ §12 / RT §10 灵性 = 重开能力 | Selection Pathology l.48（“recovery of direction beyond local `L_2` basins”）与 §2 ready-made floors；Spirit_05 Shoshin；NEURAL35 l.49、§4、§7（`reopening ≠ reselectability`；opening × re-anchoring；以 `M1: Outcome ~ AcuteIntensity` 为对手模型）；同日梦 / 迷幻审计 §9 l.453–467（REBUS source-owns relaxation；“should not infer freedom, truth or Selection from entropy / flexibility”）；同日 power root-return l.103（`new "reopening elasticity" term-of-art = NO`） | 大体 **INHERIT**。PR 真正新增的是“纵向能力而非单一状态”这一框定，应明说 |
| AJ §13 不可言说与后续再对象化 | Spirit_02 T-Trad-2 l.63–67（apophatic bound）；Spirit_04 l.479、l.495（Katz 构建主义，开放立场） | INHERIT，另见 F7 内部张力 |
| AJ §15 “spirituality = one privileged altered state / high d” | Spirit_01 l.347–353（`Ĝ_∞` 极限，已降为探索性类比）；Selection Pathology l.52（`Spirit ≡ ∇d`）；CΨ | 触及未决作者门，见 F8 |

后果：

1. 既有内容被当作新的作者裁决重新提出。
2. 仓库会同时存在两套部分冲突的叙述：饱和 vs 统一；`Center(d) → ∅` vs Bearer 持续；`Ĝ_∞` 单一极限态 vs “非单一特殊状态”。
3. RT §8 的神圣分解丢掉了 Spirit_03 Ax-Awe-2（l.66–70，敬畏 / 恐惧二元）和 Otto *tremendum* 已经承载的**威胁 / 恐惧维度**，在这一维度上比既有 domain 退步。

这些 domain 文件是 P3/P5、非 canonical（Claim Status l.18），所以问题在检索一致性，不在定义权威。**建议**：把 RT §16 扩成内部 crosswalk，按上表逐项标 INHERIT / RETYPE / CONFLICT，并把 CONFLICT 项登记为待作者处理，不在本 PR 内裁决。

### F2（高）“unified bearer-relative selective coarse-graining” 是冻结 HP-B gate-geometry 词汇的重述，隔离只是形式上的

冻结的 gate-geometry hook 已经写有：

- C1 l.63：independently admitted Bearer；
- C2 l.73：formed gate geometry = “a formed coarse-graining organization”，决定等价、边界、可达转移、扰动吸收和背景化关系；
- C3 l.85：“selective exclusion / backgrounding”；
- C4 l.124：“selective normalization / coarse-graining … some differences become generatively equivalent, some remain consequential”；
- C5 l.150：higher-order generative integration；
- C6 l.166：foregrounding process。

minimal-topology hook 也已写有：

- l.171：“Foreground is treated as a **generative role**, not as an internal display”，即 AJ §8 的“consciousness is not a read-only display”；
- l.198：position reconstitution 是必需合取项；
- l.479：`phenomenal necessity = OPEN`。

gate-geometry hook 的 Still OPEN（l.524–531）中：

- Q1：单个 gate 能否在没有跨 gate 共同重组时有意识；
- Q4：现象统一是分级、嵌套还是可离散分裂。

`Glossary/SRT_Live_Term_Router.md` l.136 已把 “coarse-graining geometry” 登记为 `gate geometry` 的别名（WORKING_LABEL_ONLY，“keep only if Route A/C/E subtraction leaves explanatory gain”）；l.107 已登记 coarse-graining 与 objectification 部分重叠。

因此：

- **AJ §3 的必要性判断，实质上是作者对 HP-B `phenomenal necessity = OPEN` 以及 OPEN Q1/Q4 的答案方向**；真正新增的只有“统一”条件，“bearer-relative”就是 C1。
- RT §6 的 burden 清单在冻结包外重建了 HP-B 自己的 burden：
  - 第 1 项（不用现象词汇）就是 hook §2 的标题要求；
  - 第 2–3、6 项（区分无意识整合控制、负控制、比较 IIT / GNW / RPT）就是 hook F1 access absorption（l.484）和 F4。
- STATUS l.407–410 规定冻结期不允许“new HP-B terms / kernel conditions / hooks”。把一个“意识的必要条件”连同自己的 burden 清单放进 active author adjudication，文件层面绕开了冻结，功能上却是一个 kernel condition。后续 session 可能把 AJ §3 当作意识判据引用，从而绕过 HP-B 治理。

**建议**：

1. 把 AJ §3 重写为“作者对 HP-B gate-geometry 组织（C2/C4/C5）附加统一要求的必要性判断”，不另立新构造。
2. 保留的标签在 router 中登记为 `gate geometry` 的别名。
3. 在 HP-B 冻结 owner 或 hook 的 OPEN Q1/Q4 旁加一条 routing-only 指针（冻结期允许，STATUS l.404–406），指向 AJ §3，作为“pending author input for reopen”。
4. 写明相对 HP-B 的实际增量：只有统一条件。

### F3（高，逻辑 / 方法）必要性主张在路线中没有证伪口；报告范式会让它自动成立

- **逻辑不匹配**：`C → U` 只能被 `C ∧ ¬U` 证伪。
  - AJ §3 的 “negative controls”（无意识控制、整合、压缩、broadcast、AI gating）、RT §6 第 2–3 项和 RT §17 第 4 条，都是 `U-ish ∧ ¬C` 的情形。它们检验的是充分性或构造可区分性，而作者并没有主张充分性。
  - RT §17 中没有任何一条能让必要性主张失败。
- **报告混淆**：AJ §3 链条的终点是 “explicit object / report”。如果用报告识别意识，而报告本身要求一个稳定、统一、可报告的前景，必要性就由测量方式保证成立。需要 no-report 范式（Tsuchiya et al. 2015）或不依赖报告的指标，并写明 U 中哪一部分可以独立于被报告对象测量。
- **应预先声明的 `C ∧ ¬U` 压力案例**：
  1. 现象不统一：split-brain、Bayne (2010)、Schechter (2018)。这正是 HP-B OPEN Q4。
  2. Overflow（Block 2011）：AJ §4 说被排除者只是背景化、不是删除，那么必须说明背景化内容能否是现象性的。如果能，现象性就大于被统一选择的部分，“selective”就成了 access 条件。
  3. Minimal phenomenal experience / “pure awareness” / PCE（Forman 1990；Metzinger 2020）。这类案例**就在本 PR 自己纳入的神秘体验范围内**：被报告为无对象、无边界、常常“无内容”的状态，对一个由差异保留、等价形成、边界形成来定义的构造是最直接的反例候选。要么证明它们实现了 U 的某种全局 / 退化形式，要么把它们列为候选反例。
  4. 梦与碎片化状态（同日梦审计材料可用）。
- **最近邻没有支付**：
  - IIT 的 intrinsicality + integration + exclusion，包括唯一时空粒度的选择（Oizumi, Albantakis & Tononi 2014；Albantakis et al. 2023），以及 causal-emergence 意义上的 coarse-graining（Hoel, Albantakis & Tononi 2013，PR1058 评审 l.240 已映射）。“统一 + bearer-relative（≈ intrinsic）+ 带 exclusion 的选择性粗粒化”与 IIT 公设非常接近。
  - 可能的判别差异：作者只主张必要性；作者的 exclusion 是分级、宽义的（背景化、可达性重组），IIT 的 exclusion 是带确定边界的唯一极大。应写明这一点；否则在这个解释任务上是 `NO LOCAL COMPARATIVE INCREMENT`。
- **逐字性**：AJ §3 的 A0-Q 是“直到在方向上会获得一致性，一种统一粗粒化门控，**从而**获得意识”。“从而获得意识”读起来偏向充分性。“只是必要条件”这一限定（PR 描述写成 “necessary for consciousness, but not sufficient”）在文件中没有保存作者原话。如果它来自机器收窄、经作者接受，应标 A1；如果来自作者，应保存 A0-Q。这一点决定了哪一组证伪案例才相关。

### F4（高）Bearer 类型与 STATUS 硬护栏冲突

**(a) RT §9 的 Bearer 延续代理与 canonical gate 不对应。**

- canonical gate（STATUS §8 l.797–830）：formed One / Selection-position + **P** prospective self-indexing + **E** same-One prospective exposure。
- 护栏：`history-bearing != Bearer`、`own-history writeback != bearing`（l.823）、`being affected != bearing`、`feedback != bearing`、`Bearer != experiencer`。
- RT §9 列出的代理是 coherent consequence-bearing、temporal continuity、structured direction、later writeback、“what changes for this continuing locus”。一个没有 Bearer 的 One / Selection-position 就能满足这些，它们都不对应 P 或 E。
- 所以“自我被削弱而这些仍在”最多说明 One / Selection-position 延续，说明不了 Bearer 延续。
- 更要紧的是：自我消融文献报告的正是自我参照加工减弱，这恰好落在 **P（prospective self-indexing）**上。“Bearer 持续”真正的经验风险在 P，而 RT §9 没有探测 P。

**(b) AJ §11 的必要性清单与护栏冲突。** AJ §11 说 Bearer “may remain necessary for meaningful difference, unity, felt consequence and later writeback”：

- “necessary for later writeback” 与 l.823 和 STATUS §4 冲突：SED-B writeback 发生在 One 层，不需要 Bearer。
- “necessary for unity” 是 HP-B 中没有的新 Bearer–统一关联。

**(c) AJ §2 的两层类型跳过了 canonical 的中间层。** AJ §2 只有“原初非中立”与“Bearer-relative meaning”两层，跳过了：

- One-level perspective（STATUS §6 l.753–776）：谱系条件化的组织在后续显现中承担负荷，不需要 Bearer；
- A2 formed-position anticipation（§7 l.778–795）；l.780 写明“Anticipation must not be moved entirely downstream to Bearer”。

AJ §2 的 “difference … consequential for this continuing formed position” 是 One-level / A2 的语言；Bearer 层是 A3（“what this position itself will undergo / preserve / lose / enable”）。除非把 “meaningful” 明确定义在 A3 层，AJ §2 就把 consequentiality 整体下移给了 Bearer。

**(d) 不可证伪。**

- 如果任何有意义、统一、有感受、能写回的状态都必须有 Bearer，那么任何可报告的状态（包括“我消融了”这种报告）都蕴含 Bearer，Bearer 消融在构造上就观察不到。
- NEURAL35 §6 已经给出安全的不对称形式，应继承。
- 成熟邻居：Zahavi（minimal self / for-me-ness 持续）vs Metzinger、Millière (2017)、Letheby & Gerrans (2017)（完全的自我消融可以取消 minimal self）。AJ §11 站在 Zahavi 一边。
- 除非证明 Bearer（P + E 的结构）不同于 minimal self / for-me-ness，这个解释任务应标为 `SOURCE-OWNED AT THIS EXPLANATORY JOB`。

### F5（高）“pre-object”被等同于“contentless”；原初 Selection 被等同于 O0；感受方向缺 O0 护栏

- AJ §2 写 “primitive Selection / pre-object non-neutrality = contentless non-maximal indifference / non-equivalence”。
  - 这与 STATUS l.135 的 strong guard `pre-object != pre-sensory or contentless` 直接冲突：认知程序里的 pre-object 不是无内容的。
  - 前瞻记忆里的方向（重要性、紧迫性、类别）带有内容。把 pre-object 等同于原初无内容，会把认知构造塌缩到 O0 上。
- 原初 Selection 不只是 O0：L0_Metaphysics l.29 写明 “O0 non-maximal indifference and S0 actualising differentiation are co-primitive analytic faces of primitive Selection”（Spine l.138 同）。应写成 “O0 face of primitive Selection” 或 “primitive Selection (O0 + S0)”。
- A0-Q「这种方向感指向了原初选择」作为作者 source intuition 保留没有问题，但 AJ §15 缺一条护栏：**感受到的方向不是 O0 的现象读出，也不是 O0 的证据**。依据：
  - STATUS l.260：`primitive Selection / O0 proof from cognition result = PROHIBITED`；
  - anti-tautology STOP 的重开条件；
  - AJ §6 自身：既然反思不能透明读取生成，“这种方向感指向原初选择”只能是本体论解释，不能是现象学发现。
- **建议**：在 AJ §15 加 `felt direction / importance ≠ phenomenal access to, or evidence for, primitive Selection / O0`，并把 §2 的“指向”标为解释性。
- AJ §2 把语义 / 价值方向放在下游，符合 Gate 0（OPEN_TENSIONS l.52，class C 不得作 L₀ 原初）✓。

### F6（中高）跨域 grammar 重跑了 A11 的 post-hoc invariant，却没有带上 A11 / §15.5 / §10.2 的护栏

音乐包 A11（l.356–410）规定：

- 该关系是 post-hoc label，音乐是 discovery case；
- “must not earn cross-domain convergence credit merely because language, action or Aha can later be redescribed with the same four outcome verbs”；
- 升级需要**在检视下一个 domain 之前**选定一个独立在先的关系；
- `next-domain prospective freeze = NOT YET AUTHORIZED`；
- 受修正案 §10.2 broad-synthesis HOLD（l.673）约束。

本 PR 的做法：

- AJ §14 列了 5 个 domain（前瞻记忆、音乐、理论直觉 ≈ Aha、语言 ≈ TOT、神圣），并提出一条在同一次对话中、看过前瞻记忆之后才造出的 8 步链。
- RT §11 用这条链填了 6 行矩阵。
- RT §0 “one bounded question” 的后半句（同一架构能否从前瞻记忆扩展到神圣 / 灵性）本身就是 broad-synthesis 问题。

两份文件都没有：

- 引用 A11、§15.5 或 §10.2；
- 写出 discovery-domain confirming count = 0；
- 给出任何禁止的转移（A11 admissibility 第 2 条）。

矩阵每行都是 “yes candidate”，所以这个 scaffold 能把任何结果都归类进去。“candidate / scaffold” 标注是好的，但按 AGENTS l.63 还不够。

还应点名的强跨域比较者：

- **Lewin 场论 / tension systems**：Zeigarnik 与 Ovsiankina 的实验正出自 Lewin 实验室，检验的就是“意图产生准需要张力系统，持续到释放为止”。Lewin 也使用场、valence、vector 的语言，是“重要性 = 势差、闭合 = 抹平”的直接先行者。
- predictive processing / active inference；
- goal-systems theory；
- event segmentation。

**建议**：

1. 从 RT §0 删去跨域半句，或明确放到 §10.2 HOLD 下。
2. AJ §14 标为 §15.5 working label；前瞻记忆、音乐的 discovery 确认计数记为 0。
3. 照录 A11 的 6 条 admissibility 条件。

### F7（中高）成熟邻居：若干 assay 已有现成结果，有的对 PR 不利

| PR 条目 | 邻居 | 后果 |
|---|---|---|
| AJ §1 / §7；RT §12 列出的 Zeigarnik | Lewin 1935；Zeigarnik 1927；Ovsiankina 1928；**Ghibellini & Meier 2025** 元分析：未完成任务的记忆优势不可靠（37 项研究的未完成 / 已完成回忆比 ≈ 0.99），恢复中断任务的倾向稳健（约 67%） | “未完成”应通过恢复、持续、侵入来操作化，不能用回忆优势；RT §12 列了 Zeigarnik 却没有注明其重复状况 |
| AJ §7 局部释放 ≠ 全局闭合（住院费） | Masicampo & Baumeister 2011（为未完成目标制定计划，即可在目标未达成时消除其侵入性认知效应）；Förster, Liberman & Higgins 2005（目标相关可及性持续到完成，完成后被抑制） | 在这个解释任务上 **SOURCE-OWNED**，最多继承 |
| RT §2 回忆前的方向结构 | Einstein & McDaniel 的 prospective / retrospective component（“that” vs “what”，正是 AJ §0 的分离）；TOT 部分信息（Brown & McNeill 1966；Vigliocco et al. 1997 语法性别）；Koriat 1993 accessibility model | 高于机会的部分结构是**预期结果**。只有 RT §2 的 “strongest version”（一致性在熟悉度 / 信心之外预测**哪个**目标随后被找回）可能有判别力。机会水平必须用被试本人待办类别的基率，不能用均匀分布（认知程序 S4 l.1296：response bias / fluency）；探针本身是提取线索，需要无探针对照；只有实验诱导的意图才有 ground truth，自然样本受“已回忆成功”的选择偏差影响 |
| AJ §5 / RT §3 突然显现 vs 过程 | **Metcalfe & Wiebe 1987** warmth ratings（非顿悟题逐渐上升，顿悟题平坦后突然跳升）；Kounios & Beeman 2014（顿悟前的内隐 / 神经前兆）；GNW ignition（Sergent & Dehaene 2004） | AJ §16 Q2 必须写明测的是主观还是内隐一致性：对顿悟型解答，“回忆前主观一致性上升”已有已知的阴性模式。R1–R3 必须对照 GNW ignition（连续累积 + 非线性进入意识）来写 |
| AJ §6 / RT §7 反思 | Nisbett & Wilson 1977；Johansson et al. 2005（choice blindness） | 在这个解释任务上 SOURCE-OWNED |
| RT §4 假候选 | Koriat（信心跟随可及性而非正确性）；goal systems（释放跟随**自认为的**完成）；Reason & Lucas 1984（“ugly sister” 阻断） | SRT 唯一可能区别于邻居的版本：在**信心与自认完成都匹配**时，仍残留未完成感，用内隐目标可及性、自发恢复、侵入来测。若自认正确的假候选同样释放，结果归邻居所有，并计为不利证据。应把这一条写成 matched-control 条件 |
| RT §8 神圣 / awe | Keltner & Haidt 2003（vastness + need for accommodation ≈ “更大关系 + 局部切分不足”）；Piff et al. 2015（small self）；Yaden et al. 2017（self-transcendent experience）；Gordon et al. 2017（threat-based awe）；Otto 1917；sacred values（Tetlock 2003；Atran & Ginges 2012：不可替换 / 禁忌权衡） | RT §8 的候选结构 ≈ Keltner–Haidt + small self，区别内容需写明。sacred values 文献给出了非现象学的操作化（拒绝权衡），也是真正通过对象 / 价值定义神圣的传统；AJ §9 偏离它，应明说 |
| AJ §13 不可言说 | Stace 1960 vs Katz 1978 vs Forman 1990 | AJ §13 是 Stace 式两阶段（先于概念的显现 → 后续再对象化），Katz 否认这一点。AJ §8（前景必然写回）本身也意味着先前的文化 / 语言对象化会塑造后续生成组织，即中介发生在**生成阶段**，不只在事后贴标签。这是内部张力；Spirit_04 l.495 已持开放立场。建议改写 AJ §13：文化 / 修行史可以经由写回塑造生成 |
| AJ §12 / RT §10 灵性 = 重开 | Batson 的 Quest orientation（Batson & Schoenrade 1991：不简化复杂性地面对存在问题、把怀疑视为积极、保持试探性）；need for closure（Kruglanski）作为反向；spiritual bypassing（Welwood）对应 RT §10 失败模式；REBUS（`Materials/2026/SRC_2026_10_04_Psychedelic_CarhartHarris_Friston_REBUS.md`，已在 main） | RT §10 的维度大体就是 Quest 量表。增量需写明，例如 NEURAL35 §7 式的 consequence-bearing × re-anchoring 联合判据 |
| RT §9 自我消融 | Millière 2017 分类（≈ RT §9 列表）；Letheby & Gerrans 2017；EDI（Nour et al. 2016） | 继承分类；另见 F4 |

### F8（中）“能量势差 / burden”的类型悬空；灵性部分绕开了既有 CΨ 作者门

**类型悬空。**

- AJ §1 写“≠ canonical `Psi_f` by stipulation”，而 AJ §15 / RT §18 又防止“local closure = global `Psi_f -> 0`”。后一条护栏预设了二者相邻。
- A-9（STATUS l.93）：theoretical friction = Ontological Friction = canonical Ψ_f concept family / contextual readings only。
- HP-B C3/C4 用 “burden” 指 constitutive Ontological Friction，并写 “mismatch … redistribute / amplify … that same friction”。AJ §7 的 “objectification is local resolution / redistribution of burden” 几乎就是 C3 原句。
- STATUS l.581：`constitutive / boundary friction != Psi_f automatically`。
- **建议**：明确写成 typing OPEN，列出候选，本 PR 不选：
  1. A-9 / HP-B C3–C4 下 Ψ_f 家族的 contextual reading；
  2. T_dir 一侧的方向量；
  3. 在 router 登记的独立 working label。

**绕开 CΨ。**

- OPEN_TENSIONS §18（l.48）与 RQ-2026-08-A05（review queue l.33，“Awaiting author”）问的是：Spirituality 的绝对 `Ψ_f→0` 完美 / 解脱映射应保留、改写还是撤回。
- AJ §12（不是单一特殊状态）、AJ §15（阻断 “spirituality = one privileged altered state / high d”）、RT §16（Spirit-as-gradient 的“future owner review”）都直接触及 CΨ，但两份文件都没有引用它。
- RT §16 另立了一个“future owner review”，而不是指向已有的作者门。
- **建议**：RT §16 改为指向 CΨ / RQ-2026-08-A05，并把 AJ §12 记为该门的作者输入，本 PR 不裁决。

**登记对立预测。** Spirituality 内部已有三种对神圣状态的预测：

- Spirit_04 Cor-Synth-H1 l.97–101：神圣体验 ↦ 预测误差 / 自由能可测下降；
- Def-Spirit-2：溢出 / 过载；
- AJ §9：选择性统一。

三者对 coherence / error 的预测方向不同，RT §8 应把它们登记为内部对立预测。

### F9（中，provenance）作者归属没有逐条标注

- 现行 schema 只有四类（STATUS l.564–571）。Phase-3 provenance map l.88：“record-level directional acceptance does not by itself upgrade machine wording into author authority”。
- AJ 中 §1、§2、§3、§5、§7 的「」中文引文可以算 A0-Q。以下各处都没有标类型：
  - §4（“Author ruling: … not in a narrow deletion sense”，英文转述）；
  - §6、§8、§10–§12 的英文 “Author ruling”，其中部分是块引用，排版与原话引文相同；
  - §7 的 “Refinement accepted in dialogue”；
  - §9 的 “Accepted direction”；
  - §14 的 “accepts the possibility”。
- 需要特别标注的三处：
  - AJ §3 的“只是必要条件”限定（F3）；
  - 作者原话“统一粗粒化门控”被加上了 “bearer-relative”“selective”（F2）；
  - AJ §14 的 domain 列表。
- 没有 derivation trace；音乐包和 #1068 都有。PR1068 评审 F8 指出过同类问题。
- **建议**：逐条标 A0-Q / A0-P / A1 / M；需要时补一份简短的对话推导记录。

### F10（低–中，机械 / 路由）

- **frontmatter**：有 `research_mode: U` ✓，但缺 `comparative_claim / named_comparator / n_mode_triggered`（AGENTS l.58；音乐路线 frontmatter l.12–14 有这三项）。`root_question` 只出现在 RT §0 正文。
- **没有入链**：仓库中没有任何文件引用这两个新路径。音乐 companion 有 STATUS §0.3f 记录和检索档案认知条目第 7 项。建议加一条 STATUS 簿记行（不改 CURRENT NEXT），并在检索档案 / 认知程序 companion 处加指针；否则违反 AGENTS 对 accepted analysis 可路由的要求。
- **Glossary router**：“unified (bearer-relative selective) coarse-graining”“local discharge”“objectification insufficiency”“reopening capacity”都作为承重标签使用，但没有记录 router 检查（AGENTS l.33）。router l.136 / l.107 已覆盖 coarse-graining；power root-return l.103 已写 “reopening elasticity” term-of-art = NO。
- **认知程序**：CN-5 l.1274 写明“author naturalistic case later — do not make it the first empirical target”。RT §19 的 “prospective-memory natural assay = HIGH VALUE CANDIDATE” 应注明 CN-5，并注明冻结的 consequence-feedback discriminator（程序 l.122）不受影响。
- **Facing v0.3**：认知程序 l.80–90 规定，中性结果晋升为 SRT / GRG 重切、跨域或新对象化主张时，需要 FR-AUTH + FR-ADV。RT §14 / §18 没有提及。
- **same-target 规则只写了一半**：RT §13 写了 “not rescue by moving the claim upstream”，没有写 AGENTS l.62 的反方向：downstream equivalence 不得升级为 upstream subtraction。两个方向都应写。
- **标签冲突**：RT §3 的 R1–R3 与 STATUS 账本的 R2-A / R2-B / R2-C 冲突；RT §1 的 N0–N6 与 “N-mode” 冲突。建议加前缀，例如 RT-R1…、NS0…NS6。

## 4. 对 PR “Review focus” 七问的直接回答

```text
1  Bearer-relative meaning 是否干净保留了无主体的原初非中立？
   部分。原初 / Bearer 的二分是干净的；但跳过了 One-level / A2 层（F4c），
   并把 pre-object 等同于 contentless（F5）。-> REVISE

2  意识必要性措辞与冻结 HP-B 的隔离是否恰当？
   形式上恰当，实质上不恰当：内容就是 HP-B C1–C6 + 统一条件（F2），
   且没有证伪口（F3）。应作为 HP-B 的 pending input 用指针路由。

3  “selective unified coarse-graining” 是否强到足以区别于一般 integration / broadcast？
   还没有。最近邻是 IIT exclusion / grain + causal emergence，以及 HP-B C2/C4 本身；
   目前只有“分级的宽义 exclusion”是候选差异（F2、F3）。

4  local discharge 是否避开了 Ψ_f→0 冲突？
   局部 / 全局的区分是好的；但“势”是否属于 Ψ_f 家族没有类型化（F8），
   而且这个解释任务已由 goal-systems 文献拥有（F7）。

5  神圣 / 灵性的分解是否避免了形而上学越界？
   形而上学护栏是好的。问题在别处：与既有 domain 重复 / 冲突（F1）、
   绕开 CΨ（F8）、与 Quest / awe 文献重叠、丢掉了 tremendum（F7）。

6  自我消融与 Bearer 消融的区分是否避免了循环论证？
   没有。代理指标只到 One 层（F4a）；“报告即需要 Bearer”使消融不可观察（F4d）。
   应继承 NEURAL35 的不对称谨慎，并探测 P。

7  跨域 grammar 在成熟邻居相减之后是否还有研究杠杆？
   目前没有挣得，也无法从这些 discovery domain 挣得（F6 / A11）。
   只有 RT §4 假候选（匹配自认完成）与 RT §2 strongest version 是候选判别器（F7）。
```

## 5. 需要作者决定的事项

```text
D-1  AJ §3 必要性主张的地位：
     (a) 记为“作者对 HP-B gate-geometry 组织（C2/C4/C5）+ 统一要求的必要性判断”，
         作为 HP-B OPEN Q1/Q4 与 phenomenal necessity 的 pending input，
         用 routing-only 指针连接，不另立新构造 [推荐]；
     (b) 保留为独立构造，但须写明相对 HP-B C2/C4/C5 与 IIT exclusion 的增量，
         并在 RT §17 加入 C ∧ ¬U 证伪条件。

D-2  “necessary, not sufficient” 的来源：
     作者原话（补 A0-Q）还是机器收窄后经作者接受（标 A1）？

D-3  跨域 grammar：
     (a) 只作为 §15.5 working label 保留在 §10.2 HOLD 下；
         前瞻记忆 / 音乐的 discovery 确认计数 = 0；从 RT §0 删去跨域半句 [推荐]；
     (b) 按 A11 先选定并冻结一个独立在先的关系，再检视下一个 domain（需另作作者决定）。

D-4  神圣 / 灵性与既有 domain 的关系：
     (a) 把 AJ §9–§13 作为既有 Spirituality owner 与 CΨ（RQ-2026-08-A05）的
         retyping 输入，逐项登记 INHERIT / RETYPE / CONFLICT [推荐]；
     (b) 作为独立新线（则须说明与 Def-Spirit-2、Fana、Ĝ_∞、NEURAL35 §6 的关系）。

D-5  AJ §2 “meaningful difference” 的层级：
     (a) 明确定义在 Bearer / A3 层，并承认 One-level / A2 的 consequentiality 不需要 Bearer [推荐]；
     (b) 维持原文（则与 STATUS §6 / §7 冲突）。

D-6  “能量势差 / burden” 的类型：
     (a) 写明 OPEN，列出 Ψ_f-family contextual reading / T_dir 一侧方向量 / 独立 working label 三个候选 [推荐]；
     (b) 现在就声明为 A-9 下的 Ψ_f contextual reading。
```

## 6. 合并前小修清单（不涉及理论）

```text
AJ §2      “pre-object non-neutrality = contentless …” 拆开：pre-object（认知层，带内容）
           与 O0 face of primitive Selection（无内容）分写（F5）
AJ §11     删去或限定 “necessary for … later writeback”（F4b）；引用 NEURAL35 §6
AJ §13     加入“文化 / 修行史可经写回塑造生成阶段”（F7 Katz）
AJ §14     标为 §15.5 working label；引 A11；discovery count = 0（F6）
AJ §15     加 felt direction ≠ O0 读出 / 证据（F5）
AJ 全文    逐条标 A0-Q / A0-P / A1 / M（F9）
RT §0      跨域半句删除或放入 §10.2 HOLD（F6）
RT §2      机会水平 = 个人基率；加无探针对照；实验诱导意图作 ground truth（F7）
RT §3      R1–R3 改名并加 GNW ignition / Metcalfe & Wiebe 对照；写明主观 vs 内隐（F7、F10）
RT §4      匹配信心与自认完成；用内隐可及性 / 恢复 / 侵入测释放；写明不利结果（F7）
RT §6      改为 HP-B pending input 的指针说明；加 C ∧ ¬U 案例与 no-report 要求（F2、F3）
RT §8      加 tremendum / threat-awe 维度；登记 Spirit_01/03/04 的三种对立预测（F1、F8）
RT §9      Bearer 代理改为对应 P / E；加 P（prospective self-indexing）探测（F4）
RT §12     Zeigarnik 注明 Ghibellini & Meier 2025；补 Lewin、Masicampo & Baumeister、Förster et al.、
           Koriat、Einstein & McDaniel、Batson Quest、Millière、Metzinger MPE、IIT exclusion / Hoel（F6、F7）
RT §13     补 AGENTS l.62 的反方向规则（F10）
RT §16     内部 crosswalk 表；指向 CΨ / RQ-2026-08-A05（F1、F8）
RT §17     加必要性证伪条件（F3）
RT §19     注明 CN-5 与冻结的 consequence-feedback discriminator；注明 Facing v0.3 晋升门（F10）
frontmatter 两文件补 comparative_claim / named_comparator / n_mode_triggered（F10）
routing    STATUS 簿记行（CURRENT NEXT 不变）+ 检索档案 / 认知程序 companion 指针；
           Live Term Router 登记或归并标签；HP-B 冻结 owner 加 routing-only 指针（F2、F10）
```

以上均为作者可选的修正；本评审不代为执行。
