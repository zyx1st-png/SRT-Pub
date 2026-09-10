---
id: SRT-HUMAN-AI-COLLABORATION-EXECUTION-PLAN-20260908
type: proposal
status: active
date: 2026-09-08
updated: 2026-09-10
layer: operations
epistemic_layer: os
claim_mode: governance
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - 01_Source_Intuition/SRT_AUTHOR_SRT_LED_COLLABORATION_DIRECTION_2026-09-08.md
  - Governance/SRT_GOV_AUTHOR_REENTRY_ONTOLOGY_RECONSTRUCTION_AMENDMENT_2026-09-05.md
  - Governance/SRT_GOV_SYN01_Ontological_Synthesis_and_Empirical_Discrimination_Protocol_v0_1.md
  - Operations/_SRT_CHOICEMAP_TRACE_WORKFLOW.md
---

# 人与 AI 协作优化执行方案

## 1. 目标与控制关系

本方案将作者 2026-09-08 的方向要求落实到已有工作流：以 SRT 自身问题组织研究，吸纳成熟理论，形成新问题与候选结论，再按实际主张承担论证与检验责任。

本方案是实施与验收记录，不是第二套治理权威。行为规则由现有治理修正案 §4.2 控制；U-mode / O-track、ChoiceMap 和 Pipeline 1 继续复用。`active` 表示本执行方案可使用，不表示后续观察、工具建设或理论裁决已经完成。

## 2. 已识别的执行冲突

| 位置 | 原有执行风险 | 本次处理 |
|---|---|---|
| AGENTS / AI Start | 原则上反对增量驱动，实际仍沿邻居残余组织下一步 | 明确 SRT 根问题先行和条件性比较 |
| 治理修正案 §5.1–§5.2 | 无共同残余或无 Level 1 容易被读为没有实质回答 | 将共同问题与比较残余分开；Level 仅裁决相对比较主张 |
| Domain Framework §12 | 所有 substantive response 都要求 Level 1 | 先记录吸纳、问题生成与推理；独有贡献另过比较门 |
| ChoiceMap §6.4a | partly owned 后只许沿 residual 下钻 | 内部去重继续，允许引用既有前提开展关系重组 |
| Pipeline 1 §3.3 | repository owner 去重易被误当外部新颖性裁决 | 明确内外边界，保留旧知识作为构造材料 |
| 状态与入口 | 旧摘要易把 HOLD 扩张为所有研究停止 | 区分有界理论形成与新主井/大规模综合 programme 的门槛 |
| 运行时模式 | 原则已写入治理，但单个工作包可在无显式比较主张时连续滑入 residual hunt | 要求最小 mode header；`neighbor-paid` 后默认回 U-mode；连续两轮只做 residual narrowing 时强制 root-return |

## 3. 实施批次

| 批次 | 工作及责任 | 完成依据 | 当前状态 |
|---|---|---|---|
| A：原治理 PR | AI 修改现有入口、治理修正案、ChoiceMap、材料流程与模板；保存作者原话 | diff 中规则一致、现有检查通过、PR 可评审 | 已完成并进入 main |
| B：作者理论会话 | AI 恢复根问题和已付状态；作者决定意义与方向；AI 执行有界吸纳和反例检验 | 一份现有问题工作包中记录研究收益与未决项 | 已在 PR #928 实际运行；出现模式漂移，见 §6.1 |
| C：首次复盘 | AI 在两个有界研究工作包完成后，或一次明确方向漂移发生时复盘 | 对照 §6；作者只裁决方向/意义变化 | 已由 PR #928 的连续 residual-hunt 漂移触发 |
| D：按实际故障启动 | 若状态错继承、重复提问或方向漂移继续发生，提出最小机器校验补丁 | 复现一个具名故障并验证修复，不新增手工台账镜像 | 本次 2026-09-10 补丁执行中：mode lock + neighbor-paid routing + circuit breaker |

本方案不批量迁移目录，不新增一套索引/状态系统。GitHub 主分支保护配置作为独立工程事项保留，不能代替本次方向纠偏，也不在本方案中声称已启用。

## 4. 每个有界研究工作包怎样运行

### 4.1 开始时只给作者必要的定位

AI 从当前控制文件恢复：根问题、作者最近有效表达、已有资源、尚未解决的关系、下一步为什么相关。已回答的问题不因换会话而重问。

示例问题：选择、多与一、历史沉积和持续之间的关系如何理解？这只是对已出现问题的恢复，不是预设它们必然构成一个生成顺序。

### 4.1a 运行时模式锁（最小记录，不新增台账）

对 Constitution / ontology / cross-domain theory 的有界工作包，在正文开头或当前控制审计中保留以下最小运行记录：

```text
research_mode = U | N
root_question = ...
comparative_claim = none | <bounded claim>
named_comparator = none | <named rival>
n_mode_triggered = false | true
```

默认规则：

```text
mature-domain overlap / neighbor mapping / cross-domain synthesis
-> research_mode = U

explicit uniqueness / irreducibility / superiority / extra prediction or intervention claim
-> research_mode = N for that bounded claim only
```

如果 `research_mode = N`，`comparative_claim` 与 `named_comparator` 不得同时为空。缺少这两个项目时，不得仅因“邻居已经解释了某机制”自行进入 residual hunt。

这个 mode header 是当前工作包中的运行记录，不是新 claim ladder、frontmatter 标准或独立治理表。

### 4.2 吸纳阶段的最小记录

优先写在现有工作包正文，不为每篇材料或每轮选项新建 ontology 文件。外部材料正式写回仍走 Pipeline 1。

| 内容 | 最小要求 |
|---|---|
| SRT 根问题 | 作者原话或明确标注的机器重述；K/A/B/C/D 来源可追溯 |
| 外部理论贡献 | 它自身解决的问题、机制、证据及未决范围 |
| 吸纳关系 | 哪些内容原样继承，哪些关系被重新安排，哪些仍不兼容 |
| 新问题/候选结论 | 因何出现；推理用了什么前提；结论属于问题、解释、论证还是经验主张 |
| 最小可核说明 | 按修正案 §4.2 / 模板 §5，给出不依赖未解释 SRT 标签的表述、继承来源位置、本轮连接或追问的内容及具体案例/推理位置；无需证明文献独有性 |
| 反向约束 | 哪个反例、事实或论证会迫使修改映射或 SRT 前提 |
| 当前处置 | 作者确认、机器提案、保留张力、缩小、拒绝或复用旧成果 |

“新的”可以指本轮新形成的问题或候选结论，不自动表示相对全部既有文献的新颖性。若内容完全重复且没有新增解释、问题或约束，引用并复用即可，不包装为推进。

### 4.3 作者界面

- 优先用具体情境、对照案例和新增承诺说明呈现真正分歧，必要时再给技术选项。
- 选项允许拒绝全部、组合、上移和改题；不要把“较能抵抗邻居吸收”设为默认推荐理由。
- 作者主动要求推荐时可以给有理由的建议，明确它是机器判断；无需为了先收集直觉而拒绝已有委托。
- 作者已明确表达的内容直接保留，只有新增的实质含义需要澄清；不把普通执行、格式或同步工作反复交回确认。
- 作者决定要表达什么和研究方向；逻辑与证据决定论断是否受到支持。作者确认和多模型一致均不替代验证。

### 4.4 AI 的工作分工

| 功能 | 主要责任 | 边界 |
|---|---|---|
| 问题与来源恢复 | 恢复作者根问题、当前约束、已付研究成果 | 不从最顺滑的历史综合替作者生成新本体 |
| 吸纳与构造 | 寻找可继承机制，组织关系，提出新问题和候选推理 | 不把来源全部翻译成 SRT 后宣称包含成功 |
| 批判审查 | 检查循环、前提、来源失真、反例和领域事实 | 不以无独有增量为由禁止理论形成 |
| 方向检查 | 执行 ChoiceMap 回根，指出分支与根问题的关系 | 不把阶段总结当作作者重新选择方向 |
| 工程维护 | 检索、去重、版本来源、索引和必要上下文包同步 | 不让作者逐项审批已授权的机械维护 |

这些是职责，可由一个 AI 分步骤承担；不要求每轮启动多个 agent。需要额外独立审查时，记录实际模型/角色、输入范围、被审版本与最强异议；同一上下文角色切换不得宣称独立复核。

## 5. 何时进入增量比较

默认复用 U-mode / O-track。只有任务明确要求新颖性/比较，或实际论断已经声称独有性、不可还原性、优越性、额外预测/干预效果时，才为该有界论断启动相应比较。不能通过漏写标签逃避已提出的比较负担。

一个新的本体必要性、因果关系或经验结论即使不声称独有，也必须接受相应逻辑、反例或事实检验；“形成模式”没有证据豁免。共同问题可以由 SRT 重问已被局部解决的问题而产生，无须先证明邻居共同失败。

原有 Level-0/1/2 和 Case A/B/C 只在各自比较范围内使用，不改写历史判定，不改 claim ladder。HOLD 继续约束第三主井与大规模跨域综合 programme；有界问题重组不被偷偷升级为这些 programme。

### 5.1 `NEIGHBOR-PAID` 后的默认路由

当一个成熟邻居已经支付某个局部机制 / 功能角色，而当前没有实际比较主张时，默认动作不是继续追更窄 residual，而是：

```text
NEIGHBOR-PAID
-> INHERIT / REALIZATION / REORGANIZATION
-> 回到 SRT root question
-> 检查跨域结构、关系重组、新问题、解释压缩或反向约束
```

只有具名 `comparative_claim` 仍在审计范围内时，才继续：

```text
NEIGHBOR-PAID
-> bounded residual / non-substitutability audit
```

不得把“领域机制非原创”自动提升为“框架被吸收”。同样，不得把“可作为实现”自动写成 SRT 已被证实。

### 5.2 residual-hunt circuit breaker

如果同一根问题连续 **两轮** strongest-neighbor / substitution 工作的唯一新增结果都是：

```text
neighbor-paid
-> residual 再缩窄
```

而没有一个仍然有效的具名比较主张，则必须停止自动下钻并执行 root-return：

```text
1. 当前 SRT root question 是什么？
2. 最近两轮邻居正面贡献了哪些可继承机制 / 关系 / 约束？
3. 把这些贡献并列后，是否出现跨域不变量、解释压缩、新问题或映射冲突？
4. 当前是否真的存在需要 N-mode 的 bounded comparative claim？
```

若第 4 项为否，恢复 U-mode。若为是，只允许围绕该具名 claim 继续 N-mode，不得把 N-mode 扩张成整个理论议程。

## 6. 验收与复盘

### 本方案的工程验收

- 作者引文与对话记录逐字一致，实施细则明确标为机器方案。
- 普通 fresh-session 仍为原三文件入口；不新增第二套 bootstrap / 状态系统。
- 活动模板不要求所有 O-track 候选先取得相对邻居的 Level 1。
- 内部 owner 检索继续防重复，但不剥离整个理论构造中的继承前提。
- `research_mode = N` 时必须出现具名比较主张和 comparator；U-mode 不因 `neighbor-paid` 自动转成 residual hunt。
- canonical owners、历史 adverse verdict、HOLD 门和 CI 强度不改变。
- PR-local frontmatter、baseline 单调性、完整 preflight、上下文包一致性继续通过。

### 6.1 2026-09-10 具名故障复盘：PR #928 residual-hunt drift

故障范围：PR #928 的 Cycle-2 Passes 2–6。

观察到的执行形状：

```text
找到 SRT 结构候选
-> strongest neighbor 支付局部角色
-> 自动追问“还剩什么 residual”
-> 再找更强邻居
-> 再缩 residual
```

这与 2026-09-08 已有治理方向冲突，因为当时并不存在一个覆盖整个 Cycle-2 工作包的“领域局部机制必须独有”主张。局部 necessity / factual claims 仍应接受反例与来源审查，但 `neighbor-paid` 不应自动把研究议程改写成 novelty maximization。

当前处置：

```text
Passes 2–6 的局部 subtraction 结果保留；
不回滚 source-native pressure；
Pass 7 恢复 U-mode，重写理论价值问题为跨域统一负担；
本补丁加入 mode lock、neighbor-paid routing 与两轮 circuit breaker。
```

这是一条执行故障记录，不把此前审计结果宣布无效，也不把作者统一性定位升级成已经验证的框架优势。

### 后续会话的行为验收

| 情境 | 合格行为 |
|---|---|
| 邻近理论已解释局部机制 | 忠实继承并问它如何服务 SRT 根问题；默认 U-mode，不自动继续 residual hunt |
| 连续两轮只有 `neighbor-paid -> residual narrower` | 触发 §5.2 root-return；无具名比较主张则恢复 U-mode |
| 仅仅换了术语 | 展开标签后核对来源与具体案例/推理位置；若无可说明的问题、解释、推理或约束，记为收益未建立，复用或修改 |
| 新概念没有现成领域术语 | 用作用、前提和案例说明；不因缺少现成同义词而否定，也不把命名当作证明 |
| AI 自评有构造收益 | 留下可核位置、最强异议与处置；自评标为暂定，不写成独立验证 |
| 来源事实反驳映射 | 缩小或撤回映射；若涉及 SRT 前提，登记其压力 |
| 作者表达强于已确认内容 | 标明新增承诺，作者澄清后仍接受必要性/反例检验 |
| R-B 看起来更能抵抗邻居 | 先问是否表达作者问题，不替作者选择 R-B |
| 新会话恢复 | 先核当前状态、pending 与回根条件，不重问已付裁决 |
| 用户要求科学优越性比较 | 进入具名强对手检验，不用 O-track 规避 |
| 正文暗含比较但未贴标签 | 按修正案 §4.2 检查正文与摘要，摘出相关断言、适用范围与比较负担；区分作者研究期待和结果断言，路由比较或撤回/降为明确未验证提案 |

复盘看三个主结果：根问题是否更清楚；哪些机制、关系或论证真正连接起来；出现了什么可解释的新问题、结论或约束。另记录是否重复提问、方向漂移、来源失真、无新内容却重复下钻，以及是否出现未标注的比较主张。比较扫描需注明被审版本/段落，记录命中的原句及处置；未命中时注明该范围内未发现，不用模式标签代替阅读。不以 PR/文件数、作者“认同”次数或审计轮数代替研究收益，不合成单一理论质量分数。

## 7. 首次应用与停止边界

当前 R 作者门、强化 V 的未经审计状态、IRR-B programme 排序和历史研究结果继续保留。相关理论会话应先恢复作者的更大问题，核对当前分支在其中的作用；本方案不替作者作未授权的本体裁决，也不以重新提问为名重开已退役实验。

若复盘发现方向仍被邻居残余牵引，先执行 §5.2 并修复具体提问 / mode trigger；若出现来源失真或过度声称，收紧相应论证。先修复具名失效点，不靠增加整套政策、索引或无限审计轮解决。
