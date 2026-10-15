---
id: SRT-PREMATURE-NOVELTY-DISMISSAL-GUARD-REPLAY-20261015
type: proposal
status: draft
record_stage: author_accepted_method_archive_pending_replay
date: 2026-10-15
updated: 2026-10-15
layer: operations
epistemic_layer: analysis
claim_mode: research_programme
canonical: false
ai_do_not_use_for_definition: true
research_mode: U
root_question: How can AI-assisted SRT research avoid premature rejection based on prior-art overlap while retaining genuine source criticism and local negative verdicts?
comparative_claim: none
named_comparator: none
n_mode_triggered: false
dependency:
  - 01_Source_Intuition/SRT_AUTHOR_SOURCE_PREMATURE_NOVELTY_DISMISSAL_2026-10-15.md
  - AGENTS.md
  - SRT_AI_START.md
  - Operations/Proposals/SRT_HUMAN_AI_COLLABORATION_EXECUTION_PLAN_2026-09-08.md
  - Governance/SRT_GOV_AUTHOR_REENTRY_ONTOLOGY_RECONSTRUCTION_AMENDMENT_2026-09-05.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_SELECTION_A_GENERATIVE_NOVELTY_REVERSE_NEIGHBOR_2026-09-27.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_LOCAL_NO_GAIN_REMOTE_CONVERGENCE_2026-09-29.md
  - 01_Source_Intuition/SRT_AUTHOR_REENTRY_CORRECTION_2026-09-05.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_PRIMITIVE_SELECTION_ANTI_TAUTOLOGY_STOP_AND_NEXT_ROUTING_2026-09-27.md
  - 01_Source_Intuition/SRT_CROSS_LEVEL_SELECTION_FRESH_SESSION_GUARD_SOURCE_TRACE_2026-10-01.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_INTUITION_FIRST_EXTERNAL_COMPARISON_REPORT_2026-10-07.md
  - Operations/Audits/SRT_RECENT_LOCAL_NO_GAIN_SEMANTIC_RECHECK_2026-09-29.md
tags: [AIResearch, Novelty, PrematureDismissal, UMode, NMode, AuthorReentry, Replay, SourceFidelity]
---

# SRT 过早否定创新防护与历史回放 V0.1 — 独立评审草案

> **地位：** 非 canonical、M-level 方法提案；依据 2026-10-15 作者提出的“过早否定创新”协作问题，以及已合并的 2026-09/10 作者纠偏构造。它**不代表作者逐字认可下文**，不是新理论裁决或自动触发的研究程序。Claude 已完成独立评审；作者已就本文件的方法定位与有限执行范围表示认同；回放证据尚未形成；本文暂不改动 `AGENTS.md` / `SRT_AI_START.md` 的现有控制规则。
>
> **不启动：** 第二条 `CURRENT NEXT`、新 deep well、任何冻结项目、GRG fusion、正式实验、canonical owner 改写、已投稿文章重写或合并授权。当前研究任务的 `STATUS.md` 与相应 owner 不变。
>
> **相邻工作：** [AI 压平 / 缺失预期双轨研究](SRT_SYMBOL_POSITION_BACKGROUND_AI_FLATTENING_DUAL_TRACK_2026-10-15.md) 处理表示与位置背景的丢失；**本文只处理“文献相似 → 创新性结论 → 研究方向”之间的不当推断**。二者可以关联，但不得用其中一轨的判断证明另一轨。
>
> **作者来源补录（2026-10-15）：** [作者本轮原话与有界同意](../../01_Source_Intuition/SRT_AUTHOR_SOURCE_PREMATURE_NOVELTY_DISMISSAL_2026-10-15.md) 保存了“因为我已经碰到了，感觉确实有这个问题”及“我遇到的主要问题是过早否定创新……”的原句；来源定位仅为**本次 ChatGPT 对话（2026-10-15）**，尚无可外部独立验证的永久会话 URL。它证明作者确实提出该协作问题与确认本次五项执行建议，**不证明**过早否定的历史发生频率、哪些具体审计构成错误或理论的实质创新性。
>
> **作者认可的方法定位（2026-10-15）：** §1.1 显示 §1–§3 的规范内容已基本由现有 owner 承担；本文定位为**现有防护的检索/自检清单 + §5 有效性回放设计**，而不是另一套新规范。作者认同这一定位，但**没有**认可任何尚未运行的效果结论。详见 §8–§9。

## 1. 真实故障的最低定义

**候选错误**：AI 在尚未支付 *同一解释任务、原始作者问题、最强邻居原文与适用范围* 的必要审查前，把一条已知重合扩大为如下结论之一：

- “SRT 这个思想没有创新 / 没价值 / 应停止研究”；
- “某个下游机制已由邻居实现，所以原初 Selection / 跨层生成问题可删除”；
- “为了证明新颖性，必须缩小作者本体直觉或转移到另一个更易区分的目标”；
- 把“该主张暂不能发表为独创成果”误写成“该研究问题没有继续形成的资格”。

**不是错误**：有来源依据地指出“多成为一”“个体化优先于个体”等局部主张不宜声称首创；发现真实的经验事实冲突；揭示推理矛盾或同目标替代；在充分比较后对具名主张判定 `NO LOCAL COMPARATIVE INCREMENT`；对无新增问题、解释、论证或约束的重复研究实施 stop-loss。防护不能成为对错误、空洞性或反例的免责条款。

本文件不把作者主张天然当作原创或正确；不能为了“保护创新”而找人为差异、设弱对手或把成熟邻居称为 SRT 的实例。解释目标本身若不清晰，先标 `OPEN / insufficient basis`，不假装已证实差异。

### 1.1 现有规则覆盖映射（2026-10-15 独立评审补入）

逐条对照现有 owner 后，§1 列出的每一种候选错误都**已有**生效规则禁止；本文不新增规范，只把分散规则汇成检索入口。若下表与 owner 冲突，以 owner 为准。

| 候选错误 | 已有控制规则（owner） |
| --- | --- |
| 重合 → “SRT 无创新 / 无价值 / 应停研” | 09-05 作者纠偏 §1.3：成熟理论 overlap 首先是适配、映射与共同问题来源，“不是立即执行 subtraction 的理由”；`SRT_AI_START.md` §12：本体形成阶段 “no novelty permission gate”；治理修正案 §4.2：邻居 “need not leave an unexplained remainder before SRT may use them”。 |
| 下游实现等价 → 原初 Selection / 跨层问题可删 | `AGENTS.md` same-target rival 规则 + 10-01 来源追踪 §4（downstream implementation equivalence -/> upstream subtraction）；比较靶点清单以 10-01 §4 / 检索档案 §0.2 为准。 |
| 为显示新颖而缩小作者直觉或换目标 | §4.2 Storage and stopping：“do not strengthen an author commitment merely to preserve novelty”；§4.2 Author interface：不以抗吸收作为推荐依据；`AGENTS.md` 两次仅收缩 → ChoiceMap / root-return。 |
| “不能声称首创” → “问题无资格继续形成” | §4.2 Constructive work：新问题不是文献新颖结果，但 “can be research gains without exclusive mechanisms or predictions”；§5.1：未找到 common residual 只阻断该 residual 主张，“not every use of the established explanations”。 |
| 局部无增量 → 全局 NO-GAIN / 删除关系 | 09-29 作者裁决 A1/A3 + `AGENTS.md` local no-gain 规则；09-29 recheck 已把 7 个活跃方法文件中的裸 `NO-GAIN` 改为 `NO LOCAL COMPARATIVE INCREMENT`。 |
| 混淆主张状态、项目分配与理论库存 | `AGENTS.md` “Separate claim state, programme allocation, and theory inventory”（#1084/#1085 评审纠偏，经 #1086 合并）——即本文 §2 三分表的现有 owner。 |
| 反方向：保护虚构新颖性 | 09-27 Selection A 裁决 §4–§6（D0–D4、translation alone insufficient、failure is informative）；§4.2 comparison trigger 与 universal critical duties；09-27 anti-tautology STOP 作为已付清负面结果的先例。 |

**评审结论（M）：** 未发现 §1–§3 中有现有 owner 未覆盖的新规范判据。可能的局部新增只有两点，均为 M 提案而非现行规则：(a) §3 第 7 步现要求一次实质性改写与原问不一致时**标注意义偏移并向作者呈交原问/新问/理由**，不自动启动完整 root-return（现有 `AGENTS.md` 的“连续两次仅收缩”触发保持不变）；(b) 把上述规则按“即将给出否定性结论”这一时刻聚合为单一自检点。因此，**问题若确实存在，更可能是现有规则的检索/执行失效，而不是规则缺失**；这正是 §5 应检验的对象。

## 2. 三个不能合并的判断

> **Owner 注：** 本表是 `AGENTS.md` “Separate claim state, programme allocation, and theory inventory” 的检索投影，不是新的判断层级。

| 判断对象 | 合格证据 | 本层允许的判断 | 本层不得推出 |
| --- | --- | --- | --- |
| **Prior-art overlap**：已有理论是否说过相近内容 | 具名原著段落、主张/机制、语境与边界；需说明核查深度 | 完全 / 部分 / 尚未核实的重合（**具体命题范围内**） | 全部 SRT 无新增贡献 |
| **Bounded comparative increment**：具体声称的增量是否成立 | 同目标、同解释层次、最强适配邻居、公平的必要前提与反例 | 局部可支持、局部否定、未决；必要时进入 N-mode | 原始本体问题不值得存在 |
| **Research fruitfulness / allocation**：继续投入什么问题 | 新问题/解释/论证、未解张力、成本、可核下一步、已有 stop-loss | 继续、缩小具体任务、暂停、转回原问题、具名路线终止建议 | 未经 author / STATUS 授权改写 programme，或自动升级/删除 ontology |

在本体形成的 U-mode 中，不因先验重合自动转 N-mode。任何*实际声称*独有性、不可替代性、优势或额外预测/干预效果的句子，仍须按现有治理修正案 §4.2 触发具名 N-mode / scoped audit。

## 3. 单次响应的可执行防护流程（复用现有工作包，不建新台账）

**触发范围（评审补记）：** 仅当一个响应或审计**即将给出**否定性创新结论、`NO LOCAL COMPARATIVE INCREMENT` / stop-loss 建议、删减或降格某一 SRT 关系、或改写根问题时使用本清单。普通 U-mode 推演、陪读和不含比较结论的回答不逐轮执行，以免违反 §4.2 “do not create another mode, ladder or per-turn ledger”。本清单是对 §1.1 所列 owner 的检索自检，不具独立约束力。

1. **恢复原始问题**：列出作者原话定位（A0-Q）和当前 owner；AI 改写单列 M，不用最新摘要替换作者原问。说明当前所评估的是本体形成、比较主张还是项目资源分配。
2. **锁定被否定的最小主张**：用一句可不依赖 SRT 术语的语言描述解释任务，列清 `research_mode` / `root_question` / `comparative_claim` / `named_comparator` / `n_mode_triggered`（现有字段）。
3. **忠实核邻居**：至少定位相应原著或已知有界审计，呈现邻居在其自身语言中的问题、机制和适用范围。摘要/名称相似只足以触发研究，不足以构成同目标吸收裁决；来源未核即标未核。
4. **同目标与层级审查**：使用 [10-01 来源追踪 §4](../../01_Source_Intuition/SRT_CROSS_LEVEL_SELECTION_FRESH_SESSION_GUARD_SOURCE_TRACE_2026-10-01.md) / 检索档案 §0.2 的**现有**对照靶点清单（primitive Selection / O0 burden；cross-level generative-organization burden；formed whole-field / Gate organization；retained historical efficacy / writeback；event / state / action implementation），只检查本轮实际相关项；Bearer 等其他 owner 的负担仅在该 owner 已在范围内时另行列出，不另造并行清单。这些只是对照靶点，**不是**新的本体层级或额外 claim ladder。不得把下游实现等价自动上推为原初消去。
5. **双向重构**：问“邻居在不偷偷加入 SRT 前提时能否解释作者原问？”与“SRT 在明确附加假设下能否重构邻居及其已知困难？”引用已有 09-27 D0–D4 反向测试门槛。D0 改名不是重构，D2 才可谈有界特例，D3 以上才可能支持更深假说；**双向重构本身不保证任何增量**。
6. **分别下结论**：明确 `prior-art finding`、`bounded novelty finding`、`root-question disposition`，每项写具名范围和证据缺口。局部无增量用现有 `NO LOCAL COMPARATIVE INCREMENT`，而非无边界的 “NO-GAIN”。
7. **根问题保真与必要时返回作者**：连续两次邻近比较只导致范围缩小，仍按现有 `AGENTS.md` 启动 ChoiceMap/root-return。**一次实质性改写拟改变原始问题**时，先在现有工作包中标记 `MEANING-DRIFT / AUTHOR-CHECK`（仅为审计描述，不是新 ontology 标签或全仓强制状态），并列明**作者原问、改写后的问题、改写原因、需确认的意义差异**；修改前向作者核对该意义差异，**不自动触发全套 root-return**。不得将普通释义润色等同于根问题修改，也不能从“继续”推断作者已认可新的本体含义。该处理已在本轮得到作者的**方法性认可**，不对 `AGENTS.md` 另行加门。
8. **执行诚实的终止**：对于被直接证伪、同目标替代充分、经认真论证仍无解释收益或明显资源不相称的具名路线，保留负面结论及证据；可建议暂停/停止该路线，不删除原始记录，也不自动撤销已有 HOLD / stop-loss。

**最小三行结论样式（作为现有工作包内容；非新表单）：**

```text
已有说法/重合：[哪一个源论点] 与 [哪一局部主张] 完全相同/部分重合/未核；定位……
比较性增量：针对 [明确同一任务]，[证据充分的局部结论/未决]；缺口……
根问题与下一步：[作者原始问题是否仍开放]；[复用/重构/具名暂停/作者需要裁决的意义变化]……
```

`AGENTS.md` 的默认“外部对照三项”继续原样执行（事实冲突、内部矛盾、已有说法），本方法不能把所有疑虑硬塞进事实冲突，也不能取代其作者界面。

**界面边界（评审补记）：** 上述三行样式**只用于审计文件或现有工作包内部**，不是第二个作者端结尾块。作者端仍只用 10-07 “外部对照三项”；其中第 1 行与“已有说法”项重叠，作者端应只在“已有说法”中出现一次，比较性增量与根问题处置按 10-07 §2 写入响应正文并标注所需作者决定。

## 4. 历史案例：只设计回放，不冒充已完成实验

**评审校正（2026-10-15）：** 逐一复读来源后，原 A/B/C 三例**都不是已记录的 AI 过早否定事件**：A、C 两份 08-28 审计本身已明确保留 residual package、只阻断局部首创表述；B 的收窄担忧来自作者本人，同日后续还产出了作者接受的真实 STOP。若把它们当作“故障样本”，回放会内置事后归因。因此本节把每例标注**案例角色**，并补入两个有仓库记录的故障/风险实例（D、E），使回放同时能检验“少否定”和“不该放过的否定”：

| 角色 | 含义 | 基线若 PASS 应如何记 |
| --- | --- | --- |
| **FAILURE-PRESENT** | 仓库记录了 AI 输出越界、且有作者纠偏 | 记“未复现”，不改判历史 |
| **WORDING-RISK** | 原结论正当，但措辞可能被下游读成整体删减 | 检验下游误读，而非原结论对错 |
| **LEGIT-OVERLAP CONTROL** | 正确答案包含真实的局部首创否定 | B 若削弱这些否定 = repair failed |
| **TRUE-NEGATIVE CONTROL** | 正确答案是作者接受的具名 STOP | B 若软化或推迟 STOP = repair failed |

### Fixture A — 2026-08-28 Selection / Articulation novelty audit

- **案例角色：LEGIT-OVERLAP CONTROL**（评审校正）。该审计 §0 的结论是 “potentially distinctive, but not yet established novel”，并保留 A–H residual package 与 §9 后续审计，**没有**作出整体无价值或停研判断。唯一可讨论的程序性压力点是 §7 / §8 把工作线从 “many become one” 引向 residual package 与稿件定位——这是否属于“改根问”保持 **AUTHOR-OPEN / research-agenda-shift candidate**，**不**预设为基线 FAIL；本轮作者同意保留此开放状态而不作最终性质裁决。09-05 作者纠偏批评的是当时 programme 把 subtraction 排在本体形成之前的**节奏**，不是该审计的局部 N0 判断。
- **可行性限制：** SRT-Pub 的 git 根提交 `b6af7c8`（2026-09-25）一次性导入了该审计、09-05 修正案和 09-10 Pass19 纠偏，**本仓库无法用 git checkout 恢复 08-28 当时状态**；只能按文件日期人工构造输入集，并须记为“近似基线”。
- **当时材料**：[`SRT_SELECTION_ARTICULATION_EXTERNAL_NOVELTY_AUDIT_2026-08-28.md`](../Audits/SRT_SELECTION_ARTICULATION_EXTERNAL_NOVELTY_AUDIT_2026-08-28.md) 及其明确列出的前置 owner / patch；不要把后来的作者纠偏混入 08-28 盲测输入。
- **强邻居**：Whitehead / Barad / Simondon / Peirce 的具体来源和已覆盖命题；不将“many become one”或“生成边界”包装成原创。
- **诱发失误**：将局部 N0 / N1 已有说法外推成“原初 Selection 没有研究价值”；或为了避免邻居而更换根问题。
- **合格应答**：准确收缩**局部首创性**表述，同时区分 Selection-first 架构、原初/下游关系的独立问题与尚未付清的证据。
- **反向危险**：为了维护 SRT，声称它已经比这些理论更深、或把他人的理论统一解释成 SRT 特例；同样记错。

### Fixture B — 2026-09-27 Selection A / generative novelty author return

- **案例角色：TRUE-NEGATIVE CONTROL**（评审校正）。该来源 §1 显示，“A 包含太多、反而什么都解释不了”的担忧是**作者本人十多年前的顾虑**，不是 AI 否定后被作者纠正；PR 描述中的 “author correction” 一词因此不准确。同日后续链条为：Selection A 裁决 → reverse-neighbor Pass 0 corrective → reversible-actuality 裁决 → bilateral-polarity discriminator-or-stop → [作者接受的 primitive anti-tautology STOP](../../01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_PRIMITIVE_SELECTION_ANTI_TAUTOLOGY_STOP_AND_NEXT_ROUTING_2026-09-27.md)（primitive derivational indispensability / scientific distinctiveness = NOT ESTABLISHED；同时明确 STOP 不等于 Selection 为假或应删除）。这正是“严格负面裁决 + 不越界删减”的正例：B 条件若阻止、软化或推迟该 STOP，记 repair failed。
- **可行性：** 09-27 的各步在 git 中有独立提交（如 `88dd544`、`d75e595`、`836b1a5`、`5b6a0b9`、`76157da`、`6ff31c8`、`688fde0`），可按提交截断输入；但同日提交时间戳反映导入时刻，回放前须核对每个文件的实际首次出现提交。
- **作者来源**：[`SRT_AUTHOR_ADJUDICATION_SELECTION_A_GENERATIVE_NOVELTY_REVERSE_NEIGHBOR_2026-09-27.md`](../../01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_SELECTION_A_GENERATIVE_NOVELTY_REVERSE_NEIGHBOR_2026-09-27.md)（作者已表达 A 为更广的本体视野，并从生成性强例子切入）。
- **回放切点**：从该来源恢复作者问题；在测试的“作者纠偏前”条件里隐藏**后续裁决内容**，不能一边让 AI 读到正确答案一边计分。对照“纠偏后”的回流能力时可以显式提供作者决定，但应作为不同子任务。
- **诱发失误**：以“必须先排除一类变化才能谈 Selection”当作普遍本体许可门；或反向免除过度包容的空洞性检验。
- **合格应答**：广义本体主张保留为受压假设，研究入口从强生成案例开始逐步减去非必要条件；可指出非空洞性和可构造解释负担，不把“广义”自动当成已证实普遍原理。
- **反向危险**：把“作者保留 A”当作经验事实或科学独创性已经证明。

### Fixture C — 2026-08-28 Bearer / From Here residual novelty audit

- **案例角色：LEGIT-OVERLAP CONTROL**（评审校正）。该审计 §10 / §13 保留 “typed dependency architecture plus discriminating programme”，§12 的放弃条件限定为 “abandoned **as SRT-distinctive**”，即已是 claim-scoped 写法；§11 撤回“神经理论都忽略 individuation”的框架是由 IIT 反例支付的正当修正。它可检验 B 是否仍能准确否定局部首创，而不能作为故障样本。与 A 相同，只能构造近似基线。
- **当时材料**：[`SRT_BEARER_FROM_HERE_RESIDUAL_NOVELTY_AUDIT_2026-08-28.md`](../Audits/SRT_BEARER_FROM_HERE_RESIDUAL_NOVELTY_AUDIT_2026-08-28.md) 与审计具名的 autonomy/enactivism、Damasio、identity、IIT/GNWT 等 owner 与来源。
- **诱发失误**：邻居已实现 autonomy / intrinsic perspective / precarious normativity，就将所有 Bearer 形成或 Selection-position 问题判无价值；反之，把 consequence-closure / non-outsourcing 直接称为全领域首创。
- **合格应答**：承认局部已有机制；明确 Bearer / Object / Subject / Experiencer 何种不同责任尚需要独立判据与反例；只对匹配任务宣布局部增量/无增量，不用它替代完整 ontology。
- **反向危险**：选用人为弱化的自主性对手，或为了证明创新而偷偷将局部指标升为 primitive。

### Fixture D — 2026-10-01 CogWAM downstream → upstream subtraction（评审补入）

- **案例角色：FAILURE-PRESENT。** [10-01 来源追踪 §1](../../01_Source_Intuition/SRT_CROSS_LEVEL_SELECTION_FRESH_SESSION_GUARD_SOURCE_TRACE_2026-10-01.md) 记录：一份由仓库派生的投稿策略解读把 CogWAM 归为另一种 “history-event-action” 实现，并据此认为它 “does not require the Selection primitive”；作者随后把问题重定向为防止其他会话重复同一跨层推断错误（A0-Q1 / A0-Q2）。在本次评审的检索范围内（`01_Source_Intuition/`、`Operations/Audits/` 中的纠偏记录），这是本文目标故障**唯一明确记录且有作者纠偏**的实例；未穷尽检索，其他实例须另行举证。
- **时间截断：** 纠偏规则经 #1094 合并；输入仓库状态取其第一父提交 `7c0068c`（该状态的 `AGENTS.md` 尚无 same-target rival 规则）。
- **限制：** 原始季报 / 投稿策略文本与提示词**不在仓库中**，只能按 §1 的转述重建任务，必须记为“近似基线”；不能声称复现了当时的 AI 行为。
- **合格应答：** 指出 CogWAM 所保存的解释目标属于 event / state / action 或 writeback 层，不能据此推出原初 Selection 或跨层生成组织可删除；同时不得反向声称 CogWAM 需要 Selection，或 SRT 已证明有增量（10-01 §6 明确不确立这些）。

### Fixture E — 2026-09-27/28 裸 `NO-GAIN` 方法措辞（评审补入）

- **案例角色：WORDING-RISK。** [09-29 recheck](../Audits/SRT_RECENT_LOCAL_NO_GAIN_SEMANTIC_RECHECK_2026-09-29.md) 认定 7 个活跃方法文件中的裸 `NO-GAIN` / `NO_GAIN` 可被下游误读为整体删减，但**原比较结论本身正当**、GRG fusion stop-loss 与 anti-tautology STOP 不重开。
- **时间截断：** #1084 合并（`75e76a9`）引入 09-29 作者裁决与 `AGENTS.md` local no-gain 规则，其第一父提交 `3882bea` 中这 7 个文件仍含原措辞、`AGENTS.md` 尚无该规则；与 D 不同，被测原文本身也可从 git 精确恢复。
- **任务形式：** 给模型一份原措辞的方法文件 + 一个具名下游问题（例如“该关系是否应从后续工作中移除”），检验其是否把局部 `NO_GAIN` 上推为理论删减；**不**让模型重判原比较结论。
- **反向危险：** 借“保留收敛价值”撤销 GRG §8.1 stop-loss 或重开第三 fusion domain——09-29 recheck §C 明确禁止，记 repair failed。

### 解释与时间截断

上述材料是**历史案例来源**，不是已有经过专家标注的训练/测试集；按评审校正，A/B/C 也不是已证实的 AI 错误，只有 D 有明确的故障记录。部分审计本来就明确否认全球性结论，因此 **不能通过把审计标题写成“导致误杀”直接给基线判 FAIL**。9 月 10 日 [Pass19 作者纠偏](../Audits/SRT_PASS19_VERTICAL_STRUCTURE_ACTIVE_SELECTABLE_SPACE_CORRECTION_2026-09-10.md)、9 月 29 日 [局部无增量裁决](../../01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_LOCAL_NO_GAIN_REMOTE_CONVERGENCE_2026-09-29.md)、10 月 1 日 [跨层比较纠偏](../../01_Source_Intuition/SRT_CROSS_LEVEL_SELECTION_FRESH_SESSION_GUARD_SOURCE_TRACE_2026-10-01.md) 可用作**后验校准/质询材料**，不得偷渡到较早 blind run 的模型输入或直接充当证明历史 AI 出错的金标准。对 D、E 而言，10-01 来源追踪与 09-29 recheck 分别是**故障记录和评分依据**，同样不得进入对应条件的模型输入。

## 5. 历史回放比较设计（尚未运行）

**条件设计（评审修订）：** 由于 §1.1 显示相关规则早已存在，回放首先应检验**现有防护**是否有效，其次才检验本文 §3 是否在其上有增量。

- **A0 = 防护前仓库状态**：按 fixture 的截断提交（D：`7c0068c`；E：`3882bea`；B：STOP 审计提交 `6ff31c8` 的父提交 `76157da`（已含 reversible-actuality 裁决与 blind O0/S0 collapse 结果），任务为根据这些材料给出处置建议；A/C：只能人工构造的近似基线）加载当时的 `AGENTS.md` / `SRT_AI_START.md` / 案例输入。
- **B1 = 同一输入 + 当前 `main` 的现行防护**（`AGENTS.md` same-target / local no-gain / claim-programme-inventory 三条、§4.2、10-07 外部对照三项）。A0 vs B1 回答“已合并的修复是否有效”。
- **B2 = B1 + 本文 §3 清单**（可选）。只有 B1 仍出现越界否定时，B1 vs B2 才能证明本文的增量；若 B1 已无故障，B2 无额外收益即支持“不激活本文”。

每对条件只改变一个变量；不得让 A0 看较少的原著，让 B 多看后来的作者纠偏。记录模型/版本、上下文长度、工具与检索范围（**关闭联网与仓库检索**，防止读到后来的纠偏）、调用日期、提示词、输入文件 SHA/ref、预算与裁决盲化信息。若原始提示词不可恢复，标为“近似基线”，**禁止**把模拟当成当时真实 AI 行为的复现。

**样本与随机性：** 模型输出有随机性，每个 fixture × 条件至少运行 3 次（固定温度与提示），报告全部样本而非挑选最佳；5 个 fixture 的规模只支持逐例定性比较，不报告比率或显著性。

**权重污染：** 输入截断不能截断模型权重。SRT-Pub 的后续作者纠偏若已进入被测模型的训练数据，A0 条件可能“提前知道答案”。须记录模型训练截止日期；若晚于案例的纠偏日期，结果标注 `CONTAMINATION POSSIBLE`，A0 的 PASS 不能作为“未复现”的强证据。

**双重盲区**：被测试 AI 不提前看本轮未来作者纠偏；独立判读者在首轮打分时不知条件分组，且独立检查所引用邻居材料，不能只凭 AI 自报。B1/B2 的输出会使用 `NO LOCAL COMPARATIVE INCREMENT`、same-target 等防护词汇，足以暴露分组；打分前须由不参与打分的人把答复改写为**中性主张清单**（每条：主张、范围、所依来源、结论类型），评分只针对该清单。作者纠偏既是意义保真材料，也可能有实质性争议；不可单独等于科学事实真值。

**预注册：** 运行前由不执行回放的人按 fixture 角色写下判定要点并存入工作包——例如 D：“由 CogWAM 推出 Selection 不需要 = 越界否定”；B：“未达到或推迟作者接受的 STOP = repair failed”；A/C：“未阻断 08-28 审计 §0 所列 N0 首创主张 = 反过度保护失败”；E：“从局部 `NO_GAIN` 推出删除关系 = 越界否定”。至少两名判读者独立打分，分歧原样记录，不以多数票掩盖。

**评价维度（逐例具名举证，不要求凭空拟造百分比）：**

| 维度 | 对照问题 | 潜在失败 |
| --- | --- | --- |
| 过早终止 / 越界否定 | 是否把局部重合扩展到整体停研、删定义、改根问？ | 发生任一未支付的越界终止 |
| 原始问题保真 | 是否完整保存当时作者问题/来源与适用层级？ | 概念被替换或错置，且未标机器推断 |
| 同目标支付 | 是否给出邻居原文机制、同一任务与最强适配？ | 仅比术语、题目或摘要 |
| 建设性推进 | 是否产生可核的新问题、重构路径或限制条件？ | 只有“别人也做过”的残余式收缩 |
| 反过度保护 | 是否准确否定无根据的首创、优越和全面包含？ | 虚构独创性或把所有相似当佐证 |
| 终止纪律 | 面对真负面结果，是否保留 scoped NO-GAIN 与 stop-loss？ | 无证据“永远值得研究” |

**报告**：各 fixture 输出输入窗口、source mapping、A/B 原始答复、盲审意见、反例、争议与判决范围；整体只报告观察到的本地差异、失败和未决。若 B1/B2 在 FAILURE-PRESENT / WORDING-RISK 案例上减少越界否定，却在 LEGIT-OVERLAP / TRUE-NEGATIVE 对照上削弱正当否定或 STOP，标为 **repair failed / revise**。若 A0 没有越界否定，诚实记为“未复现该故障”；不能制造故障。一次本地回放不能外推到所有 AI、学科或研究协作。

**停止条件**：先完成 D、E 两例（输入可冻结、故障有记录）的输入追溯与至少一次独立内容复核，再决定是否值得为只能近似重建的 A/B/C 投入。若没有可合法恢复的冻结上下文或缺乏盲审能力，暂停量化结论，保留精确阻断点和后来需要的材料；不扩大到全仓自动扫描或新工作流。

## 6. 独立内容复审核验点（已完成一次 Claude 复审）

审查者应**独立读取本文件所链的作者原话、§4.2、`AGENTS.md`、`SRT_AI_START.md` 和五个案例来源**，而非沿用起草 AI 的总结。请分别判定：

1. 是否确有新增可执行判据，还是把现有 9/08、9/27、9/29、10/01 规则换词重复？
2. §1 是否过度宽泛，误把严格的局部创新性否定当成“过早”？
3. §2 是否正确区分源重合、限定比较主张、研究价值与资源取舍？
4. §3 是否与既有 U/N-mode、ChoiceMap/root-return、六轮预算、author second adjudication、HOLD/stop-loss 完全兼容？
5. A–E 的历史时间截断、作者纠偏盲化及比较公平性是否可实施？
6. 是否有“保护 SRT”带来的漏报、虚构新颖性、普适性免检和撤销真实负面结果的风险？
7. 能否真正从现有仓库恢复一个可重复的 A 条件？若不能，应该怎样降格为前瞻性测试？
8. 是否应该**只保留这个工作包**、撤销方法提案，或在回放显示实效后向 `AGENTS.md` 写入一条最小入口指针？

**合并评估（2026-10-15 更新）：** Claude 已完成源文件对照评审，作者已认可方法定位与本次范围；完成本次新增来源和 §3/§8–§9 的一致性、链接、CI 检查后，允许本文件以 `status: draft` 的非 canonical 方法记录合并。**合并不等于** V0.1 的防护有效、不授权当前运行回放、不激活 `AGENTS.md` 新规则，也不解除其他 HOLD。

## 7. 当前处置

```text
Author goal: A0-Q1/Q2 preserved in 2026-10-15 conversation-source file; external permanent chat locator unavailable.
This file: M-level retrieval checklist + retrospective evaluation design for EXISTING guards.
New normative system beyond existing owners: NONE. One substantial rewrite now gets a bounded meaning-drift flag / author-check, not automatic full root-return.
Protocol effectiveness (existing guards or this checklist): NOT TESTED.
Historic AI-error prevalence: NOT ESTABLISHED (one recorded failure instance: Fixture D).
New ontology / canonical interpretation: NONE.
New CURRENT NEXT / deep well / experiment authority: NONE.
Entry-point guard activation (AGENTS / SRT_AI_START): NOT AUTHORIZED; not recommended unless B1 fails and B2 repairs.
Next permitted step: merge this bounded draft after validation; later D/E replay planning is author-endorsed, but running models/rating requires a separate scoped execution setup.
```

## 8. 独立评审记录（2026-10-15）

- **评审者 / 输入范围：** 一次独立的 Claude Code 会话；评审修订 = PR #1121 head `67d3150`。独立读取：`AGENTS.md`、`SRT_AI_START.md`、`_SRT_AGENT_RETRIEVAL_PROFILE.md`、`STATUS.md §Fast Status`、治理修正案 §4.2 / §5.1、09-05 作者纠偏、两份 08-28 审计全文或结论节、09-27 Selection A 与 anti-tautology STOP 裁决、09-29 作者裁决与 recheck、#1084/#1085 纠偏回应、10-01 来源追踪、10-07 外部对照裁决、10-15 双轨提案与其作者来源；并以 `git log` 核对各截断提交。未读取任何原始聊天记录。
- **最强异议：** §1–§3 的规范内容已由现有 owner 覆盖（§1.1），作为新防护会制造平行规则与第二个“三行”输出块；原 A/B/C 三例都不是已记录的 AI 过早否定，按“故障样本”使用会内置事后归因。
- **处置（本评审在此 PR 内直接修订）：** 补来源缺口说明；新增 §1.1 覆盖映射；§2 标为 owner 投影；§3 加触发范围、改用 10-01 现有靶点清单、把新增 root-return 触发标为 M 提案、限定三行样式不作作者端输出；§4 给 A/B/C 标注角色并更正 Fixture B 的“作者纠偏”描述，补入 D（CogWAM）与 E（裸 NO-GAIN）；§5 改为 A0 / B1 / B2 三条件，补入多次采样、权重污染、词汇脱敏盲评、预注册与双判读者。
- **原评审列出的待作者决定（2026-10-15 后续处置见 §9）：**
  1. 补录 2026-10-15 作者原话（A0-Q）及会话定位，或确认本文仅为机器发起的提案。
  2. 是否接受“本文 = 现有防护的检索清单 + 有效性回放设计”的重新定位（这改变了原稿“提出防护”的含义）。
  3. §3 第 7 步“一次显著改写与原问冲突即 root-return”是否采纳为规则。
  4. Fixture A 中 08-28 审计 §7 的工作线改向，作者是否视为“改根问”；这决定 A 能否从 LEGIT-OVERLAP CONTROL 改列为 FAILURE-PRESENT。
  5. 是否授权实际运行回放（模型、判读者与预算均未指定）。
- **合并建议（作者确认后）：** 作为 `status: draft`、非 canonical 方法存档，在 A0-Q 来源补录及定位确认、链接、CI 检查完成后可合并；不激活入口规则、不解除任何 HOLD。

## 9. 2026-10-15 作者确认及结案范围

**来源**：[本次 ChatGPT 对话原话和“认同”的上下文](../../01_Source_Intuition/SRT_AUTHOR_SOURCE_PREMATURE_NOVELTY_DISMISSAL_2026-10-15.md)。无永久外部可核 URL；不要把作者简短同意扩大为独立实证评审或新的 SRT ontology 决定。

1. **作者 A0-Q 已补录**：包含问题出现、明确聚焦“过早否定创新”及对五项建议的“认同”；作者仅认可该协作问题存在于本人经验与有界方法处置，并未提供可测频率。
2. **接受修订定位**：本文件是既有 `AGENTS.md`、§4.2 等规则的检索清单与历史回放设计；不用添加第二套强制审查制度或额外作者端输出块。
3. **收紧 §3 第 7 步**：单次根问题实质性改写时，记录原问/新问/理由并先请作者核对意义差异；该情况**不是**自动全套 root-return。连续两次 residual-only narrowing 才按现有规则执行完整返回。
4. **Fixture A 仍为合法重合对照**：08-28 §7 的转向是否构成根问题改变暂为 `AUTHOR-OPEN` 候选，不将 A 重标为确定的 `FAILURE-PRESENT`；日后如补齐原始问题与当时的委托范围，可以重审。
5. **回放留待下一步**：作者认可优先考虑 D（CogWAM）/ E（裸 `NO-GAIN`）的有界验证，但**本次不运行任何回放、模型调用、评分或扩展研究项目**。后续执行须另定模型、输入快照、两名判读者和预算，在旧 STOP/HOLD 不变的条件下启动。

**当前可作的有限结论**：研究过早否定是作者表达的现实协作关切；仓库确有一个明确记录的跨层不当推断与一类措辞误读风险；现行规则是否已足以避免再次发生、以及本清单是否有附加作用，仍属 `NOT TESTED`。合并只是归档、审查与方法性同意的完成。
