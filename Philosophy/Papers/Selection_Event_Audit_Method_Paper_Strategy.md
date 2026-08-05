---
id: SRT-STRATEGY-SELECTION-EVENT-AUDIT-METHOD-PAPER-20260805
title: "统一选择事件审计：方法论文定位、证据门槛与投稿前策略"
title_en: "Auditing Selection Events Across Domains: Positioning, Evidence Gates, and Pre-Submission Strategy"
type: strategy_note
status: active
version: v0_1
canonical: false
layer: philosophy_bridge
epistemic_layer: bridge
claim_mode: mixed
primary_claim_level: P2/P3
date: 2026-08-05
strategy_state: evidence_building_before_manuscript
proposed_paper_title_strong: "Auditing Selection Events Across Domains: A Non-Compensatory Identification Framework"
proposed_paper_title_weak: "When Does an Output Become a Selection Event? An Audit Framework for Registration, Efficacy, Consequence, and Write-Back"
provisional_target_journals:
  - Philosophy of Science
  - Adaptive Behavior
  - Biology & Philosophy
claim_governance:
  methodological_contribution: candidate only; requires calibration and comparator audit
  srt_ontology: not claimed by this paper
  five_gate_necessity: not established
  five_gate_sufficiency: not established
  cross_domain_scale: not established
  ai_agency: not inferred from tool use or repository effects
  biological_agency: not inferred from chemotaxis, metabolism, adaptation, or memory alone
  novelty: protocol-level novelty search incomplete
machine_summary: >
  This strategy note positions the unified selection-event audit as a candidate
  identification and audit method rather than a new causal, control, learning, or
  biochemical mechanism. The candidate contribution is the conjunction of event
  freezing, boundary indexing, compatible timescales, five non-compensatory gates,
  downgrade rules, and paired positive/negative controls. It separates the method
  paper from the existing history-dependent reachability manuscript, maps the method
  against causal inference, control and reachability, reinforcement-learning credit
  assignment, empowerment, active inference, trace-based AI assurance, and institutional
  path dependence, and defines explicit falsifiers. The present evidence base is not
  submission-ready: the AI transaction triad is a strong calibration set, while the
  E. coli chemotaxis audit is a useful bounded negative result, but an institutional
  case, boundary-perturbation study, independent coding reliability test, and a natural
  same-event consequence/write-back dataset are still required before a full manuscript.
dependency:
  - Operations/SRT_UNIFIED_SELECTION_EVENT_AUDIT_PROTOCOL_2026-08-04.md
  - Operations/SRT_AI_NEGATIVE_CONTROL_DISCONNECTED_WRITE_UNIFIED_AUDIT_2026-08-04.md
  - Operations/SRT_AI_SERVER_REJECTED_WRITE_UNIFIED_AUDIT_2026-08-04.md
  - Operations/SRT_AI_CORRECT_SHA_SUCCESS_CONTROL_UNIFIED_AUDIT_2026-08-05.md
  - Operations/SRT_LIFE_BOUNDARY_CASE_ECOLI_CHEMOTAXIS_UNIFIED_AUDIT_2026-08-05.md
  - Operations/SRT_INTERNAL_NON_EQUIVALENT_REGISTRATION_OPERATIONAL_TEST_2026-08-04.md
  - Operations/SRT_PATH_EFFICACY_OPERATIONAL_TEST_2026-08-04.md
  - Operations/SRT_CONSEQUENCE_BEARING_POSITION_OPERATIONAL_TEST_2026-08-04.md
  - Operations/SRT_HISTORICAL_EFFICACY_OPERATIONAL_TEST_2026-08-04.md
  - papers/history_dependent_reachability/manuscript/MANUSCRIPT.md
---

# 统一选择事件审计：方法论文定位、证据门槛与投稿前策略

## 文件性质

这是内部论文策略文件，不是投稿正文，不修改统一协议，也不建立新的 canonical 定义。

本文件只回答五个问题：

1. 这篇方法论文究竟研究什么；
2. 它与现有控制论、因果推断、强化学习、主动推断和路径依赖理论有什么关系；
3. 它与仓库中的 history-dependent reachability 论文如何分工；
4. 现有证据是否足够投稿；
5. 什么结果会迫使项目停止、降级或改写。

---

# 0. 结论先行

## 0.1 当前判断

统一选择事件审计已经形成一个值得继续检验的方法候选，但**尚未达到完整论文投稿条件**。

最强允许定位不是：

> SRT 发现了世界中一种新的因果机制。

而是：

> 不同学科已经分别拥有干预、控制、可达性、信用分配、适应、记忆、路径依赖和制度反馈等工具；但在跨域讨论“选择”时，研究者经常把这些局部证据拼接成一个未经识别的整体事件。统一选择事件审计提出一套非补偿式识别程序，要求差异、内部登记、现实路径效力、路径特异后果和未来可达路径写回在同一个冻结事件、同一个明示边界和相容时间尺度内闭合。

这是一项**识别与审计贡献候选**，不是机制发现。

## 0.2 候选方法贡献

候选贡献由六个组件组成：

1. **event freezing**：先冻结被审计事件，不允许把准备、失败后的报告或后续治理倒灌进目标事件；
2. **boundary indexing**：每个等级都必须说明属于模型、工具链、完整人机系统、细胞、种群还是制度；
3. **compatible timescales**：五门证据必须处于可因果拼接的时间尺度，而不是从毫秒信号、小时代谢和多年进化中各取一项；
4. **five non-compensatory gates**：DMF、NER、PEF、CBP、HEF 不能相加补偿；
5. **downgrade rules**：工具调用、耗能、奖励、记忆、日志、适应和持久化都拥有明确的非充分性规则；
6. **paired calibration**：通过未调用、真实拒绝、真实提交等结构化正负对照检验方法是否产生单调区分。

单独看，六项都不是新的。论文能否成立取决于：

> 它们的组合是否产生现有框架没有明确给出的额外可检验区分，并且这些区分能在跨域案例中稳定复现。

## 0.3 当前证据状态

| 证据包 | 当前作用 | 允许结论 | 不允许结论 |
|---|---|---|---|
| AI 未调用 mutation | 弱阴性对照 | 计划与输出不等于路径效力 | 证明 AI 没有任何因果作用 |
| AI 错误 SHA / 409 | 强阴性对照 | 接触真实端点仍可保持 PEF-1 / SEA-1 | 409 是新的选择机制 |
| AI 正确 SHA 成功提交 | 配对阳性对照 | 实际 commit 和 ref 写回允许完整边界升级 | 模型本身 SEA-3 |
| E. coli 趋化 | 生命系统受限阴性结果 | NER、PEF、HEF 强证据不能补偿同事件 CBP 缺失 | 细菌已被证明具有高阶主体性 |
| history-dependent reachability 设计模型 | HEF / 选择特异写回识别工具 | 历史可改变匹配当前后的未来可达性 | 自然系统已经满足该机制 |

## 0.4 投稿前最低缺口

在形成完整 manuscript 之前，至少还缺：

1. 一个制度或组织案例；
2. 一个显式改变审计边界的稳健性测试；
3. 两名以上独立编码者的判定一致性测试；
4. 一个自然系统中的同事件 CBP + HEF 数据包，或明确保留为未完成强检验；
5. 系统性的 protocol-level novelty search；
6. 至少一个“普通理论判为成功、SEA 必须降级”的预注册案例；
7. 至少一个“普通描述看似相同、SEA 因边界或历史不同而区分”的配对案例。

在这些条件完成前，最合理产物是：

> 方法策略、案例审计和证据档案，而不是直接投稿正文。

---

# 1. 论文对象：不是“选择是什么”，而是“如何识别一个选择事件”

## 1.1 中心识别问题

论文不回答形而上学的全部问题：

> 世界是否由选择构成？

它回答更窄的问题：

> 当研究者已经观察到差异、响应、动作、成本、记忆或制度变化时，什么证据允许把这些事实归属于同一个选择事件？

## 1.2 被审计对象

被审计对象不是系统的一般属性，而是带索引的事件：

```text
E = <target transition, boundary, start condition, end condition, timescale, alternatives>
```

一个系统可以：

- 在某个事件中达到 SEA-1；
- 在另一个事件中达到 SEA-2；
- 在更大边界中达到 SEA-3 qualified；
- 同时不能把较大边界结果反投给较小组成部分。

## 1.3 论文必须避免的本质化

以下说法全部超出方法论文：

- 某类生命天然属于 SEA-3；
- 具备记忆的系统天然是主体；
- 能调用工具的模型天然是 agent；
- 具有奖励函数的系统天然承担后果；
- 路径依赖天然等于选择写回；
- 五门是所有可能世界中的必要充分条件。

方法论文的对象是**证据纪律**，不是存在等级表。

---

# 2. 与 history-dependent reachability 论文的严格分工

## 2.1 现有论文解决的问题

`Identifying History-Dependent Reachability` 的核心问题是：

> 在当前可观察状态与快速策略被匹配后，历史形成的慢变量是否仍能改变未来行为可达性，并且这种改变是否来自系统自身的选择—后果耦合，而不是一般暴露历史？

它已经建立：

- matched-present 设计；
- master-yoked control；
- external-action sham；
- 选择特异写回与一般持久化／一般规则变化的分离；
- 保留的负结果；
- 设计模型中的可达分布改变。

## 2.2 新方法论文解决的问题

SEA 方法论文问的是：

> 在任意跨域案例中，如何判断差异、内部介质、外部执行、路径特异后果和未来写回是否属于同一个选择事件？

因此：

| 维度 | History-dependent reachability | SEA 方法论文 |
|---|---|---|
| 核心对象 | 选择特异历史写回 | 完整选择事件识别 |
| 主门槛 | matched present 后未来可达性仍不同 | 五门同事件闭合 |
| 主要方法 | 设计模型、yoked/sham、holdout | 冻结事件、边界索引、降级、正负校准 |
| 主要结果 | 写回是否选择特异 | 一个事件最高可判到哪里 |
| HEF 地位 | 中心对象 | 五门之一 |
| CBP 地位 | 通过代价与行为结果间接出现 | 必须单独识别，不能由成本或奖励替代 |
| 跨域目标 | 不主张自然系统事实 | 明确压力测试跨域可移植性 |

## 2.3 不允许的重复投稿结构

新论文不得重复：

- double-well 模型完整结果；
- S2 prediction-error NO-GO 的主结果；
- S3/S4 action-attributable predictive information 机制；
- matched-present 方法作为主要新贡献；
- 相同图表和相同结果数字。

允许的引用方式是：

> history-dependent reachability 提供 HEF 和 selection-specific write-back 的一个候选识别模块；SEA 检验该模块是否与其他事件门在同一边界和时间尺度内闭合。

## 2.4 投稿顺序

默认顺序：

1. history-dependent reachability 独立投稿；
2. SEA 继续积累跨域校准；
3. SEA 正文只简要引用前者的方法和负结果；
4. 不把 SEA 用作前一论文尚未发表时的外部权威来源。

---

# 3. 五门在方法论文中的最小角色

## 3.1 CG-0 / DMF：差异进入真实候选空间

最低问题：

> 是否存在对目标事件有意义的非等价候选，而不是观察者事后贴标签？

DMF 不证明：

- 内部比较；
- 执行；
- 后果；
- 记忆。

## 3.2 CG-1 / NER：内部非等价登记

最低问题：

> 是否存在可定位的内部介质，使候选差异以非等价方式改变后续响应？

仅有不同输出、分类标签或外部校验不足。

## 3.3 CG-2 / PEF：现实路径效力

最低问题：

> 目标事件是否跨过执行门，改变了预注册的外部路径变量？

请求、建议、意图、API 接触和错误返回不能替代目标提交。

## 3.4 CG-3 / CBP：路径特异后果承载位置

最低问题：

> 哪个边界因该路径而获得、损失、维持、受损、承担恢复成本或改变未来行动能力？

一般耗能、运行时间和信息处理成本不是自动的 CBP。

## 3.5 CG-4 / HEF：未来可达路径写回

最低问题：

> 事件结果是否改变了后续可达路径、进入成本、返回成本或响应分布？

日志、缓存、瞬时状态和可读取记录不自动达到 HEF-3。

## 3.6 非补偿原则

论文的核心方法主张候选是：

```text
high NER + high PEF + high HEF
cannot compensate for failed CBP
```

以及：

```text
real cost + persistent record
cannot compensate for failed PEF
```

如果审计最终允许通过加权总分跨越失败门，方法将退化为一般指标表，失去主要区分力。

---

# 4. 与普通理论的关系：组件重叠，识别任务不同

## 4.1 因果推断与结构因果模型

Pearl 的干预语义和 do-calculus 解决：

- 观察与干预的区分；
- 因果效应识别；
- 反事实和直接／间接效应。

SEA 必须使用这些工具，而不是替代它们。

SEA 额外询问：

- 被识别的因果效应是否属于目标系统的实际执行路径；
- 后果由哪个边界承担；
- 历史写回是否发生；
- 五项证据是否属于同一个事件。

如果结构因果模型已经明确编码这些变量，SEA 可能只是一份审计清单。论文必须承认这种可能，并通过案例证明组合纪律产生额外降级结果。

## 4.2 控制理论、可达性与 viability

控制与可达性理论能够描述：

- 系统能否到达目标状态；
- 在扰动下哪些状态可维持；
- 控制成本、可行域、viability kernel 和 backward reachable set。

这与 PEF、CBP 和 HEF 高度重叠。

SEA 不得声称重新发现 reachability。

潜在差异在于：

- potential controllability 不等于 actual event execution；
- 外部控制器维持的状态不自动属于目标系统自身路径效力；
- 可达集合本身不要求内部非等价登记；
- 安全或可行约束不自动确定后果承担边界；
- 单次到达不自动形成历史写回。

## 4.3 Empowerment 与信息论控制

Empowerment 将 agent 的行动通道容量作为控制潜能指标。

它可以支持：

- 候选路径可区分度；
- 行动对未来感知状态的潜在影响；
- agency phenotype 的计算指标。

但 empowerment 通常测量的是**潜在通道容量**，不保证：

- 目标事件实际执行；
- 某条路径产生了边界特异后果；
- 事件写回未来路径；
- 结果属于模型本身而不是完整系统。

因此 SEA 与 empowerment 的关系应写成：

> empowerment 可作为 DMF/PEF 的候选测量，不是 SEA 总等级的代理变量。

## 4.4 强化学习与信用分配

强化学习的 credit assignment 研究区分：

- 行动影响与环境运气；
- 当前行动与延迟奖励；
- 多行动／多智能体的贡献分配。

这与 NER、PEF 和选择—后果归因直接相关。

但 RL 中：

- reward 可以由设计者外部指定；
- 高 return 不等于系统边界承担现实后果；
- 参数更新不一定是路径特异写回；
- 训练历史与部署事件可能不是同一个事件；
- credit assignment 成功不自动证明 CBP。

SEA 的新增压力是：

> 信用被算法正确分配给行动，仍不等于该行动在所声明边界内构成完整选择事件。

## 4.5 主动推断与自由能框架

主动推断把行动、推断、偏好和生成模型放入统一规范框架。

2026 年出现的 AI agency phenotyping 工作进一步尝试以 intentionality、rationality、explainability 和 empowerment 区分不同 agency phenotype。

SEA 不应与其竞争完整 agency 理论，而应提出更窄的审计问题：

- 内部模型结构是否真的被干预并验证；
- 行动是否跨越外部执行门；
- 后果属于哪个边界；
- 事件是否改变未来可达路径；
- 结构性 agency phenotype 是否在真实失败／成功对照中保持。

可能的差异是：

> 主动推断框架可从生成模型结构刻画 agentic action chain；SEA 要求事件级外部验证，并允许一个结构上高度 agentic 的系统在某次事件中停留于 SEA-1。

## 4.6 Agentic AI trace assurance

2026 年 trace-based assurance 框架已经把：

- message-action traces；
- step / trace contracts；
- deterministic replay；
- fault injection；
- external side effects；
- governance mediation

纳入 agentic AI 运行审计。

这对 SEA 构成强近邻压力。

SEA 不得声称首次区分文本输出与外部副作用。

可能保留的差异只有：

- SEA 同时要求 consequence-bearing position；
- SEA 把未来可达路径写回与一般 trace persistence 分离；
- SEA 明确禁止跨边界反投；
- SEA 试图跨 AI、生命和制度域保持同一审计语法。

如果 trace assurance 加上 stake 和 history-dependent reachability 后可以完全覆盖 SEA，方法论文的新颖性必须降级为综合性应用框架。

## 4.7 制度路径依赖与历史制度主义

路径依赖研究已经强调：

- 时间和顺序重要；
- 小事件可能产生大后果；
- increasing returns；
- 逆转成本上升；
- critical juncture 和 policy feedback。

这与 HEF 和 CBP 高度重叠。

SEA 不得把“历史改变未来”当作新发现。

潜在差异在于：

- 路径依赖常从长期结果反推关键节点；
- SEA 要求冻结目标事件和替代路径；
- SEA 要求明确内部登记介质；
- SEA 区分一般制度惯性与路径特异后果承载；
- SEA 不允许把多年累积效应自动归给单次决策。

制度案例将是方法论文的关键压力测试，因为它最容易暴露：

> “同一事件”和“同一边界”在分布式社会系统中是否过度理想化。

---

# 5. 当前最强经验校准：AI 事务三态

## 5.1 三态结构

```text
NC-1: mutation 未调用
NC-2: mutation 调用，但错误 SHA 导致 409
POS: 正确 SHA，产生新 blob、commit 和 branch head
```

## 5.2 方法价值

三态案例证明统一审计至少能稳定区分：

- 计划；
- 真实端点接触；
- 服务端处理；
- 事务提交；
- 目标状态改变；
- commit / ref 历史写回。

## 5.3 仍然薄弱之处

该校准具有以下局限：

- 环境为人工构造的隔离分支；
- CBP 主要是恢复成本和分支状态承担；
- 事件风险低；
- Git 事务机制完全可由普通工程理论解释；
- 对模型内部 NER 没有干预证据；
- 只证明方法在一个结构清晰的软件事件中可工作。

因此 AI 三态应在论文中作为：

> calibration vignette，而不是中心自然科学发现。

---

# 6. 首个生命压力测试：E. coli 趋化的受限阴性结果

## 6.1 为什么重要

趋化系统包含：

- 受体差异；
- CheA / CheY 信号；
- CheR / CheB 适应；
- 鞭毛马达执行；
- 空间迁移；
- 短时历史效应。

它看起来几乎天然满足完整选择事件。

## 6.2 审计结果

现有实验可分别支持：

- NER；
- PEF；
- HEF。

但通常没有在同一细胞、同一事件和相容时间尺度内同时测量：

- 营养收益；
- ATP / PMF；
- 损伤；
- 恢复成本；
- 生长；
- 后续行动能力。

因此：

```text
standard chemotaxis case != established SEA-3
```

## 6.3 对方法论文的价值

这比一个轻易通过的生命案例更有价值，因为它表明：

> 方法不会因为对象是生命、会运动、会适应、会耗能、有记忆，就自动升级。

## 6.4 仍需完成的实验压力

最关键设计是同细胞微流控联测：

```text
ligand history
→ receptor / CheY state
→ trajectory
→ resource / maintenance consequence
→ matched-history future probe
```

并加入：

- non-metabolizable attractant；
- cheR cheB；
- motor coupling interruption；
- matched current state；
- history reset。

这可以直接检验：

```text
high NER + high PEF
without CBP
must remain below SEA-3
```

---

# 7. 方法论文的新颖性必须通过的六项测试

## 7.1 组合不可约测试

问题：

> 五门组合是否只是把现有术语并排放置？

通过条件：

- 至少两个案例中，单一邻近理论会给出相同描述，而 SEA 因门失败给出不同判定；
- 差异可由预注册观测决定，而不是解释者印象。

失败后果：

> 降级为综合性审计清单，不主张新方法。

## 7.2 单调校准测试

问题：

> 从未调用、真实拒绝到真实提交，等级是否按预期单调变化？

通过条件：

- 独立编码者不看预期标签时仍恢复顺序；
- 不允许因 409 产生真实成本而把阴性对照升级。

## 7.3 边界稳健性测试

问题：

> 更换边界是否可以任意制造 SEA-3？

设计：

- 同一事实分别在模型、工具链、完整社会技术系统中编码；
- 要求每次升级指出新增的可观测门闭合；
- 禁止只因边界变大而升级。

失败后果：

> 若边界可随意扩张并总能闭合五门，SEA 不具有判别力。

## 7.4 时间尺度稳健性测试

问题：

> 是否能从不同时间尺度各取一项证据拼出完整事件？

设计：

- 制造毫秒 NER、小时 CBP、长期 HEF 的不兼容证据包；
- 预期判定为“无统一等级”。

失败后果：

> 若仍给 SEA-3，兼容时间尺度规则失效。

## 7.5 编码一致性测试

至少两名不了解案例预期的编码者，对冻结材料独立判定：

- 事件窗口；
- 边界；
- 各门等级；
- 决定性失败门；
- 允许和禁止表述。

预注册指标：

- ordinal weighted kappa；
- gate-level agreement；
- boundary agreement；
- downgrade-trigger agreement。

若关键门一致性低于预注册阈值，不能声称方法可移植。

## 7.6 近邻覆盖测试

对每个案例建立：

```text
ordinary-theory-only analysis
vs
ordinary theory + SEA audit
```

如果后者没有新增：

- 可检验变量；
- 阴性对照；
- 降级条件；
- 边界归属；
- 未来实验设计；

则案例不能计入方法论文的新颖性证据。

---

# 8. 明确的证伪与停止规则

出现任一情况，必须停止强方法论文路线：

1. 五门在大多数案例中无法独立编码；
2. CBP 始终退化为一般成本或效用；
3. HEF 无法与普通记忆／持久化稳定区分；
4. 边界改变能够无新证据地任意升级；
5. 独立编码一致性低；
6. 近邻框架已明确给出同样的同事件、同边界、非补偿式五门结构；
7. 正负对照不能产生稳定单调顺序；
8. 所有 SEA 判定都可以由“是否成功完成任务”替代；
9. 制度案例必须依赖事后叙事才能确定事件；
10. 生命案例只能通过跨论文、跨尺度拼接达到 SEA-3。

停止后保留的最低成果可以是：

> 一套跨域研究设计清单，用于防止把输出、执行、成本、记忆和路径依赖混为一谈。

---

# 9. 下一项必须完成的案例：制度决策事件

## 9.1 案例要求

制度案例必须具有：

- 明确候选方案；
- 可定位的内部登记载体，例如会议记录、表决、审批状态或组织规则；
- 真实执行门；
- 明确承担后果的组织或群体边界；
- 后续规则、预算、权限或可达路径写回；
- 至少一个“决定形成但未执行”的阴性对照；
- 至少一个“执行但未制度化”的中间对照。

## 9.2 推荐三态设计

```text
I-1: 形成建议／会议共识，但无正式授权
I-2: 正式授权并执行一次，但无规则或预算写回
I-3: 正式执行，并改变后续权限、预算、默认项或逆转成本
```

预期：

```text
I-1 → PEF-1 / SEA-1
I-2 → PEF-2, HEF below 3 / SEA-2
I-3 → SEA-3 qualified, only if CBP is explicit
```

## 9.3 案例选择纪律

不得选择：

- 只有成功故事、没有失败记录的案例；
- 结果已知后才构造候选路径的案例；
- 无法区分执行与制度化的案例；
- 仅凭媒体叙事推断内部登记的案例；
- 后果承担者与事件边界完全不清楚的案例。

---

# 10. 建议论文结构

## 10.1 目标长度

完整稿目标：

```text
8,000–10,000 English words
```

不含补充材料。

## 10.2 主文结构

### Section 1 — The identification problem

从常见混淆开始：

- output vs action；
- action vs committed effect；
- cost vs consequence bearing；
- persistence vs historical write-back；
- system-level result vs component attribution。

### Section 2 — Existing tools and the remaining event-unity gap

覆盖：

- causal inference；
- control and reachability；
- RL credit assignment；
- empowerment；
- active inference；
- path dependence；
- trace-based assurance。

必须以“组合识别缺口”而非“前人都没研究选择”来写。

### Section 3 — The audit protocol

只呈现最小方法：

- event tuple；
- boundary tuple；
- five gates；
- non-compensation；
- downgrade rules；
- evidence table；
- uncertainty labels。

不扩展 SRT 宏大本体论。

### Section 4 — Calibration in a software transaction

呈现三态：

- disconnected；
- rejected；
- committed。

把普通 Git / REST 机制放在首位。

### Section 5 — Biological stress test and retained negative result

呈现 E. coli：

- 强 NER / PEF / HEF；
- 同事件 CBP 缺失；
- 为什么不能拼接 SEA-3；
- 集成实验设计。

### Section 6 — Institutional calibration

必须在正文开始前完成。

### Section 7 — Reliability, boundary sensitivity, and failure analysis

报告：

- independent coding；
- boundary perturbation；
- time-scale incompatibility；
- near-neighbor coverage；
- failed cases。

### Section 8 — What the framework does not establish

必须集中声明：

- 不建立主体性；
- 不建立意识；
- 不建立道德地位；
- 不取代领域机制；
- 不证明五门必要充分；
- 不证明自然尺度统一。

## 10.3 补充材料

建议包含：

- 完整编码手册；
- 每个案例的冻结证据包；
- 独立编码结果；
- 判定分歧记录；
- 普通理论对照分析；
- 所有降级触发；
- 未纳入案例及排除理由。

---

# 11. 图表计划

## Figure 1 — Event and boundary decomposition

展示：

```text
candidate difference
→ internal registration
→ execution channel
→ target path change
→ consequence-bearing boundary
→ future reachability write-back
```

并在图中分开：

- model；
- orchestration；
- external system；
- human / organization。

## Figure 2 — Non-compensatory gate structure

不要画加权雷达图。

应画成串联门：

```text
failed gate → downgrade
```

## Figure 3 — AI three-state calibration

```text
not invoked | rejected | committed
```

对应外部状态变量。

## Figure 4 — E. coli evidence map

用不同颜色区分：

- 已在同事件测量；
- 仅跨研究支持；
- 尚未测量；
- 不能拼接。

## Table 1 — Comparison with neighboring frameworks

列：

- intervention；
- internal registration；
- actual execution；
- consequence boundary；
- historical reachability；
- event unity；
- non-compensation；
- negative controls。

必须避免把邻近理论粗暴写成“没有”。应使用：

```text
central / available / optional / not required by default
```

## Table 2 — Case verdicts and decisive failed gates

只列冻结案例，不列推测性例子。

---

# 12. 投稿路线与期刊适配

## 12.1 Philosophy of Science

适配条件：

- 中心贡献必须是科学识别方法；
- 与干预、模型、跨域测量和操作化文献充分对话；
- 提供真正的新论证或方法结果；
- 不能主要依赖 SRT 内部术语。

只有在 reliability 和 institutional case 完成后才建议首投。

## 12.2 Adaptive Behavior

适配条件：

- 强调生物系统与自主人工系统的共同审计问题；
- E. coli 与 AI 对照成为主案例；
- 最好包含可复现编码或实验设计；
- 文章更偏 operational framework，而非纯哲学论证。

在现阶段，这是比 Philosophy of Science 更现实的应用型候选。

## 12.3 Biology & Philosophy

适配条件：

- 文章重点转向生命 agency、适应、后果承载和历史写回；
- E. coli 不能只是一个文献审计，需更强自然系统证据；
- AI 只能作为边界对照，不能占据主线。

## 12.4 暂不选择的路线

暂不建议：

- 直接投一般 AI benchmark 会议：当前没有大规模 benchmark；
- 直接投控制理论期刊：没有新的控制算法或定理；
- 直接投生物实验期刊：没有新实验数据；
- 直接投宏大意识期刊：方法不识别意识。

---

# 13. 论文的主张阶梯

## Level 0 — 审计便利性

> 五门表格有助于整理跨域材料。

价值有限，但安全。

## Level 1 — 稳定区分力

> 在预注册正负对照中，五门产生普通任务成败标签无法完全替代的稳定降级结果。

这是最低可投稿主张。

## Level 2 — 可移植识别方法

> 经过独立编码、边界扰动和多域校准，方法在 AI、生命和制度案例中保持可解释一致性。

这是目标主张。

## Level 3 — SRT 独立理论增量

> 五门结构揭示现有理论无法表达的新自然规律。

当前完全没有建立，不进入本论文。

---

# 14. 允许与禁止的写作语言

## 14.1 允许

- candidate identification framework；
- audit discipline；
- non-compensatory gates；
- boundary-indexed verdict；
- retained negative result；
- calibration sequence；
- protocol-level comparison；
- ordinary-theory baseline；
- qualified；
- not established。

## 14.2 禁止

- universal law of selection；
- mathematical proof of agency；
- objective scale of consciousness；
- AI has stakes because it used tools；
- bacteria choose because they chemotax；
- all causation is selection；
- SEA replaces causal inference；
- SEA unifies all sciences；
- five gates are necessary and sufficient；
- first framework ever to audit agentic side effects。

---

# 15. 参考文献与近邻压力清单（非完整文献综述）

以下只作为下一轮系统检索的起点：

1. Pearl, J. (1995). A Causal Calculus for Statistical Research.
2. Pearl, J. (2010). Causal Inference.
3. Aubin, J.-P. (2009). Viability Theory.
4. Mitchell, I. M., Bayen, A. M., & Tomlin, C. J. (2005). A Time-Dependent Hamilton–Jacobi Formulation of Reachable Sets for Continuous Dynamic Games.
5. Klyubin, A. S., Polani, D., & Nehaniv, C. L. (2005). Empowerment: A Universal Agent-Centric Measure of Control.
6. Friston, K., Samothrakis, S., & Montague, R. (2012). Active Inference and Agency: Optimal Control without Cost Functions.
7. Everitt, T., Carey, R., Langlois, E., Ortega, P. A., & Legg, S. (2021). Agent Incentives: A Causal Perspective.
8. Mesnard, T. et al. (2021). Counterfactual Credit Assignment in Model-Free Reinforcement Learning.
9. Mesnard, T. et al. (2023). Quantile Credit Assignment.
10. Pierson, P. (2000). Increasing Returns, Path Dependence, and the Study of Politics.
11. Bednar, J., & Page, S. E. (2018). When Order Affects Performance: Culture, Behavioral Spillovers, and Institutional Path Dependence.
12. Wilson, P. et al. (2026). Active Inference: A Method for Phenotyping Agency in AI Systems?
13. Paduraru, C., Bouruc, P.-L., & Stefanescu, A. (2026). A Trace-Based Assurance Framework for Agentic AI Orchestration.

系统检索必须继续查找：

- 直接把 event identity、stake、write-back 和 boundary attribution 联合操作化的工作；
- 生物 agency 的干预式评估框架；
- process tracing 与机制证据标准；
- 软件 side-effect assurance 与 transaction semantics；
- organizational decision implementation 与 policy feedback；
- cross-domain coding reliability 方法。

在检索完成前，不允许写：

> no prior framework combines these elements。

只能写：

> no close protocol-level precedent has yet been established in the current search。

---

# 16. 执行路线

## Phase C1 — 制度三态案例

产物：

- 一个冻结事件包；
- 未授权／一次执行／制度写回三态；
- 普通制度理论基线；
- SEA 判定；
- 阴性结果保留。

## Phase C2 — 编码手册 v0.1

产物：

- 事件冻结表；
- 边界表；
- 门级证据模板；
- 降级触发表；
- 不确定性标签；
- 冲突解决规则。

## Phase C3 — 独立编码试验

至少：

- 2 名编码者；
- 6 个冻结案例；
- 3 个领域；
- 盲化预期等级；
- 记录全部分歧。

## Phase C4 — 近邻框架覆盖审计

逐项回答：

- causal inference 能否完整覆盖；
- reachability 能否完整覆盖；
- RL credit assignment 能否完整覆盖；
- active inference phenotyping 能否完整覆盖；
- trace assurance 能否完整覆盖；
- path dependence 能否完整覆盖。

## Phase C5 — Go / No-Go

Go 条件：

- 至少三个领域；
- 至少两项强阴性结果；
- 至少一项严格配对阳性结果；
- 边界扰动通过；
- 编码可靠性达到预注册阈值；
- 近邻覆盖后仍有明确方法增量。

No-Go 条件：

- 只能形成术语对照表；
- 判定依赖作者直觉；
- CBP 无法独立；
- 跨域后门槛含义漂移；
- 近邻框架完全覆盖。

---

# 17. 最终策略判断

当前不应立即撰写完整英文 manuscript。

应该继续的不是增加更多宏大概念，而是完成：

```text
制度三态案例
→ 编码手册
→ 独立一致性测试
→ 边界／时间尺度扰动
→ 近邻覆盖审计
→ Go / No-Go
```

若这些测试通过，论文的最强可守主张是：

> 统一选择事件审计是一种跨域、边界索引、非补偿式的事件识别方法。它不替代领域因果机制，而是检验差异、内部登记、路径执行、后果承担和历史写回能否被合法归属于同一个选择事件。

若测试失败，项目仍保留一个更弱但实用的成果：

> 一套防止把输出、执行、成本、记忆、适应和路径依赖混为一谈的跨域审计清单。
