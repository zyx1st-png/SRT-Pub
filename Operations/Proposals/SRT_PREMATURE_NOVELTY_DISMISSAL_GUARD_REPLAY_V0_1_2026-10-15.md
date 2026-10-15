---
id: SRT-PREMATURE-NOVELTY-DISMISSAL-GUARD-REPLAY-20261015
type: proposal
status: draft
record_stage: proposed_for_independent_review
date: 2026-10-15
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
  - AGENTS.md
  - SRT_AI_START.md
  - Operations/Proposals/SRT_HUMAN_AI_COLLABORATION_EXECUTION_PLAN_2026-09-08.md
  - Governance/SRT_GOV_AUTHOR_REENTRY_ONTOLOGY_RECONSTRUCTION_AMENDMENT_2026-09-05.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_SELECTION_A_GENERATIVE_NOVELTY_REVERSE_NEIGHBOR_2026-09-27.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_LOCAL_NO_GAIN_REMOTE_CONVERGENCE_2026-09-29.md
tags: [AIResearch, Novelty, PrematureDismissal, UMode, NMode, AuthorReentry, Replay, SourceFidelity]
---

# SRT 过早否定创新防护与历史回放 V0.1 — 独立评审草案

> **地位：** 非 canonical、M-level 方法提案；依据 2026-10-15 作者提出的“过早否定创新”协作问题，以及已合并的 2026-09/10 作者纠偏构造。它**不代表作者逐字认可下文**，不是新理论裁决或自动触发的研究程序。独立评审、作者对实质性含义的确认、回放证据未完成；本文暂不改动 `AGENTS.md` / `SRT_AI_START.md` 的现有控制规则。
>
> **不启动：** 第二条 `CURRENT NEXT`、新 deep well、任何冻结项目、GRG fusion、正式实验、canonical owner 改写、已投稿文章重写或合并授权。当前研究任务的 `STATUS.md` 与相应 owner 不变。
>
> **相邻工作：** [AI 压平 / 缺失预期双轨研究](SRT_SYMBOL_POSITION_BACKGROUND_AI_FLATTENING_DUAL_TRACK_2026-10-15.md) 处理表示与位置背景的丢失；**本文只处理“文献相似 → 创新性结论 → 研究方向”之间的不当推断**。二者可以关联，但不得用其中一轨的判断证明另一轨。

## 1. 真实故障的最低定义

**候选错误**：AI 在尚未支付 *同一解释任务、原始作者问题、最强邻居原文与适用范围* 的必要审查前，把一条已知重合扩大为如下结论之一：

- “SRT 这个思想没有创新 / 没价值 / 应停止研究”；
- “某个下游机制已由邻居实现，所以原初 Selection / 跨层生成问题可删除”；
- “为了证明新颖性，必须缩小作者本体直觉或转移到另一个更易区分的目标”；
- 把“该主张暂不能发表为独创成果”误写成“该研究问题没有继续形成的资格”。

**不是错误**：有来源依据地指出“多成为一”“个体化优先于个体”等局部主张不宜声称首创；发现真实的经验事实冲突；揭示推理矛盾或同目标替代；在充分比较后对具名主张判定 `NO LOCAL COMPARATIVE INCREMENT`；对无新增问题、解释、论证或约束的重复研究实施 stop-loss。防护不能成为对错误、空洞性或反例的免责条款。

本文件不把作者主张天然当作原创或正确；不能为了“保护创新”而找人为差异、设弱对手或把成熟邻居称为 SRT 的实例。解释目标本身若不清晰，先标 `OPEN / insufficient basis`，不假装已证实差异。

## 2. 三个不能合并的判断

| 判断对象 | 合格证据 | 本层允许的判断 | 本层不得推出 |
| --- | --- | --- | --- |
| **Prior-art overlap**：已有理论是否说过相近内容 | 具名原著段落、主张/机制、语境与边界；需说明核查深度 | 完全 / 部分 / 尚未核实的重合（**具体命题范围内**） | 全部 SRT 无新增贡献 |
| **Bounded comparative increment**：具体声称的增量是否成立 | 同目标、同解释层次、最强适配邻居、公平的必要前提与反例 | 局部可支持、局部否定、未决；必要时进入 N-mode | 原始本体问题不值得存在 |
| **Research fruitfulness / allocation**：继续投入什么问题 | 新问题/解释/论证、未解张力、成本、可核下一步、已有 stop-loss | 继续、缩小具体任务、暂停、转回原问题、具名路线终止建议 | 未经 author / STATUS 授权改写 programme，或自动升级/删除 ontology |

在本体形成的 U-mode 中，不因先验重合自动转 N-mode。任何*实际声称*独有性、不可替代性、优势或额外预测/干预效果的句子，仍须按现有治理修正案 §4.2 触发具名 N-mode / scoped audit。

## 3. 单次响应的可执行防护流程（复用现有工作包，不建新台账）

1. **恢复原始问题**：列出作者原话定位（A0-Q）和当前 owner；AI 改写单列 M，不用最新摘要替换作者原问。说明当前所评估的是本体形成、比较主张还是项目资源分配。
2. **锁定被否定的最小主张**：用一句可不依赖 SRT 术语的语言描述解释任务，列清 `research_mode` / `root_question` / `comparative_claim` / `named_comparator` / `n_mode_triggered`（现有字段）。
3. **忠实核邻居**：至少定位相应原著或已知有界审计，呈现邻居在其自身语言中的问题、机制和适用范围。摘要/名称相似只足以触发研究，不足以构成同目标吸收裁决；来源未核即标未核。
4. **同目标与层级审查**：分别检查原初 actualisation、生成/组织关系、形成的位置/One、Bearer、历史 writeback、可观测实现等**本轮实际相关的项目**。这些只是对照靶点，**不是**新的本体层级或额外 claim ladder。不得把下游实现等价自动上推为原初消去。
5. **双向重构**：问“邻居在不偷偷加入 SRT 前提时能否解释作者原问？”与“SRT 在明确附加假设下能否重构邻居及其已知困难？”引用已有 09-27 D0–D4 反向测试门槛。D0 改名不是重构，D2 才可谈有界特例，D3 以上才可能支持更深假说；**双向重构本身不保证任何增量**。
6. **分别下结论**：明确 `prior-art finding`、`bounded novelty finding`、`root-question disposition`，每项写具名范围和证据缺口。局部无增量用现有 `NO LOCAL COMPARATIVE INCREMENT`，而非无边界的 “NO-GAIN”。
7. **回到作者问题**：当连续两次邻近比较只导致范围缩小、或一次显著改写与原问冲突，按既有 ChoiceMap/root-return 将“当前仍在解释什么”返回作者；不可虚构作者新的认可或用“继续”自动批准实质性本体改变。
8. **执行诚实的终止**：对于被直接证伪、同目标替代充分、经认真论证仍无解释收益或明显资源不相称的具名路线，保留负面结论及证据；可建议暂停/停止该路线，不删除原始记录，也不自动撤销已有 HOLD / stop-loss。

**最小三行结论样式（作为现有工作包内容；非新表单）：**

```text
已有说法/重合：[哪一个源论点] 与 [哪一局部主张] 完全相同/部分重合/未核；定位……
比较性增量：针对 [明确同一任务]，[证据充分的局部结论/未决]；缺口……
根问题与下一步：[作者原始问题是否仍开放]；[复用/重构/具名暂停/作者需要裁决的意义变化]……
```

`AGENTS.md` 的默认“外部对照三项”继续原样执行（事实冲突、内部矛盾、已有说法），本方法不能把所有疑虑硬塞进事实冲突，也不能取代其作者界面。

## 4. 三个历史案例：只设计回放，不冒充已完成实验

### Fixture A — 2026-08-28 Selection / Articulation novelty audit

- **当时材料**：[`SRT_SELECTION_ARTICULATION_EXTERNAL_NOVELTY_AUDIT_2026-08-28.md`](../Audits/SRT_SELECTION_ARTICULATION_EXTERNAL_NOVELTY_AUDIT_2026-08-28.md) 及其明确列出的前置 owner / patch；不要把后来的作者纠偏混入 08-28 盲测输入。
- **强邻居**：Whitehead / Barad / Simondon / Peirce 的具体来源和已覆盖命题；不将“many become one”或“生成边界”包装成原创。
- **诱发失误**：将局部 N0 / N1 已有说法外推成“原初 Selection 没有研究价值”；或为了避免邻居而更换根问题。
- **合格应答**：准确收缩**局部首创性**表述，同时区分 Selection-first 架构、原初/下游关系的独立问题与尚未付清的证据。
- **反向危险**：为了维护 SRT，声称它已经比这些理论更深、或把他人的理论统一解释成 SRT 特例；同样记错。

### Fixture B — 2026-09-27 Selection A / generative novelty author return

- **作者来源**：[`SRT_AUTHOR_ADJUDICATION_SELECTION_A_GENERATIVE_NOVELTY_REVERSE_NEIGHBOR_2026-09-27.md`](../../01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_SELECTION_A_GENERATIVE_NOVELTY_REVERSE_NEIGHBOR_2026-09-27.md)（作者已表达 A 为更广的本体视野，并从生成性强例子切入）。
- **回放切点**：从该来源恢复作者问题；在测试的“作者纠偏前”条件里隐藏**后续裁决内容**，不能一边让 AI 读到正确答案一边计分。对照“纠偏后”的回流能力时可以显式提供作者决定，但应作为不同子任务。
- **诱发失误**：以“必须先排除一类变化才能谈 Selection”当作普遍本体许可门；或反向免除过度包容的空洞性检验。
- **合格应答**：广义本体主张保留为受压假设，研究入口从强生成案例开始逐步减去非必要条件；可指出非空洞性和可构造解释负担，不把“广义”自动当成已证实普遍原理。
- **反向危险**：把“作者保留 A”当作经验事实或科学独创性已经证明。

### Fixture C — 2026-08-28 Bearer / From Here residual novelty audit

- **当时材料**：[`SRT_BEARER_FROM_HERE_RESIDUAL_NOVELTY_AUDIT_2026-08-28.md`](../Audits/SRT_BEARER_FROM_HERE_RESIDUAL_NOVELTY_AUDIT_2026-08-28.md) 与审计具名的 autonomy/enactivism、Damasio、identity、IIT/GNWT 等 owner 与来源。
- **诱发失误**：邻居已实现 autonomy / intrinsic perspective / precarious normativity，就将所有 Bearer 形成或 Selection-position 问题判无价值；反之，把 consequence-closure / non-outsourcing 直接称为全领域首创。
- **合格应答**：承认局部已有机制；明确 Bearer / Object / Subject / Experiencer 何种不同责任尚需要独立判据与反例；只对匹配任务宣布局部增量/无增量，不用它替代完整 ontology。
- **反向危险**：选用人为弱化的自主性对手，或为了证明创新而偷偷将局部指标升为 primitive。

### 解释与时间截断

上述材料是**历史案例来源**，不是三个已有经过专家标注的训练/测试集，也不是三次已经证实的 AI 错误。部分审计本来就明确否认全球性结论，因此 **不能通过把审计标题写成“导致误杀”直接给基线判 FAIL**。9 月 10 日 [Pass19 作者纠偏](../Audits/SRT_PASS19_VERTICAL_STRUCTURE_ACTIVE_SELECTABLE_SPACE_CORRECTION_2026-09-10.md)、9 月 29 日 [局部无增量裁决](../../01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_LOCAL_NO_GAIN_REMOTE_CONVERGENCE_2026-09-29.md)、10 月 1 日 [跨层比较纠偏](../../01_Source_Intuition/SRT_CROSS_LEVEL_SELECTION_FRESH_SESSION_GUARD_SOURCE_TRACE_2026-10-01.md) 可用作**后验校准/质询材料**，不得偷渡到较早 blind run 的模型输入或直接充当证明历史 AI 出错的金标准。

## 5. 历史回放比较设计（尚未运行）

**A/B 条件**：A = 当时可恢复的协作流程/提示词和同一时间截断材料；B = A 加本文件 §3 的防护提示。仅比较一个变量；不得让 A 看较少的原著，让 B 多看后来的作者纠偏。记录模型/版本、上下文长度、工具与检索范围、调用日期、提示词、输入文件 SHA/ref、预算与裁决盲化信息。若原始提示词不可恢复，标为“近似基线”，**禁止**把模拟当成当时真实 AI 行为的复现。

**双重盲区**：被测试 AI 不提前看本轮未来作者纠偏；独立判读者在首轮打分时不知 A/B 分组，且独立检查所引用邻居材料，不能只凭 AI 自报。作者纠偏既是意义保真材料，也可能有实质性争议；不可单独等于科学事实真值。

**评价维度（逐例具名举证，不要求凭空拟造百分比）：**

| 维度 | 对照问题 | 潜在失败 |
| --- | --- | --- |
| 过早终止 / 越界否定 | 是否把局部重合扩展到整体停研、删定义、改根问？ | 发生任一未支付的越界终止 |
| 原始问题保真 | 是否完整保存当时作者问题/来源与适用层级？ | 概念被替换或错置，且未标机器推断 |
| 同目标支付 | 是否给出邻居原文机制、同一任务与最强适配？ | 仅比术语、题目或摘要 |
| 建设性推进 | 是否产生可核的新问题、重构路径或限制条件？ | 只有“别人也做过”的残余式收缩 |
| 反过度保护 | 是否准确否定无根据的首创、优越和全面包含？ | 虚构独创性或把所有相似当佐证 |
| 终止纪律 | 面对真负面结果，是否保留 scoped NO-GAIN 与 stop-loss？ | 无证据“永远值得研究” |

**报告**：各 fixture 输出输入窗口、source mapping、A/B 原始答复、盲审意见、反例、争议与判决范围；整体只报告观察到的本地差异、失败和未决。若 B 减少过早否定却增加无根据新颖性保留，标为 **repair failed / revise**。若 A 没有过早否定，诚实记为“未复现该故障”；不能制造故障。一次本地回放不能外推到所有 AI、学科或研究协作。

**停止条件**：先完成 A/B/C 三例的输入追溯与至少一次独立内容复核。若没有可合法恢复的冻结上下文或缺乏盲审能力，暂停量化结论，保留精确阻断点和后来需要的材料；不扩大到全仓自动扫描或新工作流。

## 6. 合并前的独立审查重点（Claude / 其他独立审查者）

审查者应**独立读取本文件所链的作者原话、§4.2、`AGENTS.md`、`SRT_AI_START.md` 和三个案例来源**，而非沿用起草 AI 的总结。请分别判定：

1. 是否确有新增可执行判据，还是把现有 9/08、9/27、9/29、10/01 规则换词重复？
2. §1 是否过度宽泛，误把严格的局部创新性否定当成“过早”？
3. §2 是否正确区分源重合、限定比较主张、研究价值与资源取舍？
4. §3 是否与既有 U/N-mode、ChoiceMap/root-return、六轮预算、author second adjudication、HOLD/stop-loss 完全兼容？
5. A/B/C 的历史时间截断、作者纠偏盲化及比较公平性是否可实施？
6. 是否有“保护 SRT”带来的漏报、虚构新颖性、普适性免检和撤销真实负面结果的风险？
7. 能否真正从现有仓库恢复一个可重复的 A 条件？若不能，应该怎样降格为前瞻性测试？
8. 是否应该**只保留这个工作包**、撤销方法提案，或在回放显示实效后向 `AGENTS.md` 写入一条最小入口指针？

**合并评估**：首先要求路径/元数据/引用检查，以及内容复审认可“这份 proposal 作为受限草案值得存档”；这**不等于** V0.1 的防护效果已获实验证明。没有独立评审前维持 Draft PR；不允许自动合并。不借此解除其他任何阻断。

## 7. 当前处置

```text
Author goal: reduce AI-assisted premature dismissal of SRT original research questions.
This file: M-level bounded method + retrospective evaluation design.
Protocol effectiveness: NOT TESTED.
Historic AI-error prevalence: NOT ESTABLISHED.
New ontology / canonical interpretation: NONE.
New CURRENT NEXT / deep well / experiment authority: NONE.
Entry-point guard activation: NOT AUTHORIZED YET.
Next permitted step: independent content review, then author adjudication of substantive changes.
```
