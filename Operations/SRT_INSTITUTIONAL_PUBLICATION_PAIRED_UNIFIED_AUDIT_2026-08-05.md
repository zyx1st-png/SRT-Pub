---
id: SRT-INSTITUTIONAL-PUBLICATION-PAIRED-UNIFIED-AUDIT-20260805
type: operational_audit_report
tags: [Institutions, ScholarlyPublishing, Submission, PeerReview, EditorialDecision, Production, UnifiedAudit, SelectionEvent, CG0, NER, PEF, CBP, HEF, PairedCalibration, NegativeControl, PositiveControl]
status: active
record_stage: institutional_paired_calibration_v1
layer: meta
epistemic_layer: os
claim_mode: operations_execution
claim_level: audit_only
canonical: false
ai_do_not_use_for_definition: true
created: 2026-08-05
revised: 2026-08-05
provenance: 2026-08-05 作者要求在统一选择事件方法论文策略合并后继续执行制度三态案例。本报告以作者邮箱中的两条真实学术出版流程为私有一手证据：Entropy 稿件登记后终止处理，以及 Frontiers in Neuroscience 稿件经独立审稿、修订、最终审查、接受、production 与 proof 阶段的阳性链。报告只提交隐私安全的事件摘要，不提交邮件正文、地址、私有链接、附件、账单细节、折扣申请或平台访问凭据。
dependency:
  - Operations/SRT_UNIFIED_SELECTION_EVENT_AUDIT_PROTOCOL_2026-08-04.md
  - Operations/SRT_INTERNAL_NON_EQUIVALENT_REGISTRATION_OPERATIONAL_TEST_2026-08-04.md
  - Operations/SRT_PATH_EFFICACY_OPERATIONAL_TEST_2026-08-04.md
  - Operations/SRT_CONSEQUENCE_BEARING_POSITION_OPERATIONAL_TEST_2026-08-04.md
  - Operations/SRT_HISTORICAL_EFFICACY_OPERATIONAL_TEST_2026-08-04.md
  - Operations/SRT_AI_NEGATIVE_CONTROL_DISCONNECTED_WRITE_UNIFIED_AUDIT_2026-08-04.md
  - Operations/SRT_AI_SERVER_REJECTED_WRITE_UNIFIED_AUDIT_2026-08-04.md
  - Operations/SRT_AI_CORRECT_SHA_SUCCESS_CONTROL_UNIFIED_AUDIT_2026-08-05.md
  - Operations/SRT_LIFE_BOUNDARY_CASE_ECOLI_CHEMOTAXIS_UNIFIED_AUDIT_2026-08-05.md
  - Philosophy/Papers/Selection_Event_Audit_Method_Paper_Strategy.md
---

# 制度系统配对校准：学术投稿终止与接受后生产写回

## 0. 结论先行

本报告完成统一选择事件审计的第一组真实制度系统配对案例。

两个案例均来自作者本人、均有稳定稿号与制度状态记录，但不是同一篇稿件、同一期刊或严格随机对照，因此它们只能作为**结构性校准对**，不能用于估计“什么因素导致接受或拒绝”。

### 阴性链：Entropy

- 稿件：*Selection Cost as a Fisher Information Metric: A Riemannian Geometry of Embodied Updating*
- 稿号：`entropy-4202982`
- 2026-02-28：投稿系统确认接收并分配稿号；
- 2026-03-02：编辑部明确不再继续处理；
- 私有证据包中没有同行评审、修订、接受、production、proof、DOI 或公开出版记录。

保守判定：

```text
manuscript artifact alone → SEA-1 upper bound
registered submission → SEA-2 qualified
editorial termination at author–platform–editorial boundary → SEA-2 strong
public scholarly-record boundary → unresolved / not established
```

决定性限制不是“没有任何制度后果”。该链确实产生登记、排他投稿义务、等待、路径终止和重新路由压力。

决定性限制是：

> 当前路径终止不能同时充当历史写回证据；私有状态记录尚未被一个后续过程以可干预方式调用，从而改变未来候选可达性、转换门槛或适用规则。因此 `HEF-3` 未建立。

### 阳性链：Frontiers in Neuroscience

- 稿件：*A Translational Cross-Modal Control-Cost Framework for Executive Breakdown*
- 稿号：`1837760`
- 2026-03-24：投稿登记并进入初始验证；
- 2026-05-04：进入 independent review；
- 2026-05 至 2026-07：审稿报告、interactive review、修订与复审；
- 2026-07-15：进入 review finalised；
- 2026-07-17：正式接受并进入 production；
- 2026-07-28：proof 已生成并要求作者校对；
- 另有接受后费用与生产义务记录，但隐私细节不进入仓库。

保守判定：

```text
manuscript artifact alone → SEA-1 upper bound
submitted / independent-review workflow → SEA-2 strong
acceptance decision, author–editor–reviewer–production boundary → SEA-3 qualified
public publication / DOI / indexing / citation boundary → unresolved as of 2026-08-05
```

`SEA-3 qualified` 的负载点不是“期刊说 accepted”，而是：

> 接受状态被后续 production 流程实际调用，生成校样、校对期限与费用／生产义务，从而改变后续可达路径、参与角色、返回成本和完成条件。

### 配对增量

这组制度案例为现有校准序列增加了新的门槛区分：

```text
AI wrong-SHA / 409 → PEF gate fails
E. coli standard chemotaxis → same-event CBP remains unresolved
Entropy registered then declined → real PEF and CBP, but HEF-3 not established
Frontiers accepted then proof generated → B3 HEF-3 and SEA-3 qualified
```

五门不能相互补偿：

- 强烈拒稿后果不能替代历史写回；
- 接受通知本身不能替代 production 的后续调用；
- 费用、等待和情绪影响不能自动建立 CBP；
- 邮件、日志和稿号不能自动建立 HEF；
- public DOI 或 citation 不能在尚未核验时倒灌进当前事件。

---

# 1. 文件性质与隐私纪律

本文件是内部 Operations 审计报告，不是投稿证据附件，不是期刊申诉，不是出版状态证明，也不是对任何期刊质量、编辑动机或公平性的评价。

## 1.1 私有一手证据

审计读取了作者已连接邮箱中的以下事件类型：

### Entropy 链

1. 同日较早的外部学术联络邮件，附有 `manuscript_v9.pdf`；
2. `Submission Received`；
3. `Declined for Publication`。

### Frontiers 链

1. `Your manuscript is submitted`；
2. `Progress: Independent review stage`；
3. reviewer report / interactive review / revision 通知；
4. `Your manuscript has moved to final review`；
5. `your article has been accepted`；
6. 接受后费用／生产通知；
7. `your proof is ready`。

## 1.2 不进入仓库的内容

本文件不复制：

- 发件或收件邮箱地址；
- 邮件正文全文；
- 私有 tracking、review 或 production URL；
- attachment ID；
- 访问码、平台 reference code 或 endorsement code；
- 账单编号、金额、付款信息；
- fee-support 申请中的个人财务陈述；
- 审稿意见正文；
- 未公开的稿件附件。

## 1.3 外部可复核性限制

当前证据属于作者私有一手档案。

它可以支持：

- 仓库内部方法校准；
- 事件冻结；
- 边界和角色审计；
- 后续制作隐私安全的编码包。

它暂时不能支持：

- 外部读者独立复核所有邮件；
- 对期刊制度的一般统计推断；
- 对审稿质量、编辑公平性或决定理由的强判断；
- 公开论文中的无附件可验证事实主张。

若未来用于方法论文，需要另行制作：

- 经作者批准的脱敏时间线；
- 公开可访问的期刊状态页或 DOI；
- 文件哈希与版本映射；
- 最小必要邮件摘录或机构导出；
- 独立编码者可访问但不公开扩散的受控证据包。

---

# 2. 审计问题

本轮不问：

> 期刊接受是否“本质上”比拒稿更像选择？

本轮问：

> 在真实出版流程中，稿件差异何时进入制度有效通道、被内部非等价登记、改变现实路径、把路径特异后果落到可识别位置，并通过状态载体重塑后续可达流程？

进一步问：

> 登记后终止与接受后进入 production 的差异，是否会在相同五门审计中产生稳定降级，而不是由研究者依据“成功／失败”事后贴标签？

---

# 3. 事件与状态冻结

## 3.1 不采用单一“投稿生命周期大事件”

若把从写稿、投稿、审稿、接受、校样、出版、引用、职业影响全部合并，就会制造：

- 事件窗口无限扩张；
- 作者内部决定与制度状态混合；
- 期刊流程与公共知识系统混合；
- 当前路径改变与后续历史写回重复计数；
- 月级审稿与年级引用直接拼接。

因此本报告拆为四个事件单元。

## 3.2 `E-N1`：Entropy 投稿登记

开始：稿件与元数据进入 Entropy 投稿系统。

结束：系统发出 `Submission Received`，分配 `entropy-4202982` 并登记稿件标题、类型、作者、收稿日期和栏目。

不属于事件内部：

- 稿件形成的全部前史；
- 同日较早的 arXiv endorsement 邮件；
- 后续拒稿决定；
- 任何之后的改稿或另投。

## 3.3 `E-N2`：Entropy 编辑终止

开始：已登记稿件进入编辑处理窗口。

结束：2026-03-02 编辑部通知“不再进一步处理该投稿”。

事件后探针：

- 是否进入同行评审；
- 是否产生 revision；
- 是否进入 acceptance / production；
- 是否形成 DOI 或公开出版；
- 是否有持久状态被后续制度程序调用。

当前私有证据包只支持流程终止，不支持以上后续写回。

## 3.4 `E-P1`：Frontiers 投稿与独立审稿

开始：2026-03-24 稿件 `1837760` 被系统登记。

结束：稿件进入 independent review，并出现审稿报告、interactive review 与修订循环。

该事件用于判定真实制度登记和路径效力，不把最终接受倒灌进本事件。

## 3.5 `E-P2`：Frontiers 接受决定

开始：稿件进入 `review finalised`，associate editor 评估审稿报告与最新稿件。

结束：2026-07-17 发出正式接受通知。

事件后探针：

- accepted 状态是否被后续系统调用；
- 是否进入 production；
- 是否产生校样与校对义务；
- 是否产生路径特异费用或资源义务；
- 是否形成公开出版、DOI、索引和引用。

截至 2026-08-05：

- production：已建立；
- proof：已生成；
- 费用／生产义务：存在私有记录；
- public publication / DOI / indexing / citation：未在本轮证据中核验。

---

# 4. 三态／分叉状态机

本轮制度校准不是简单线性三态，而是一个带终止分支与生产分支的状态机：

```text
S0  私有稿件／投稿准备
       |
       v
S1  稿件被制度系统登记
       |
       +-----------------------------+
       |                             |
       v                             v
S2-N  编辑终止                    S2-R  独立审稿／修订
                                     |
                                     v
                                  S3-A  接受
                                     |
                                     v
                                  S4-P  production / proof
                                     |
                                     v
                                  S5-U  public publication / DOI
                                        [本轮未核验]
```

## 4.1 `S0` 的证据限制

同日较早的学术联络邮件证明：

- 一个与 Fisher spectral analysis 相关的稿件附件已经存在；
- 作者正在开展外部传播或预印本准备。

但没有附件 hash 或版本比对，不能证明该 PDF 与 Entropy 提交文件逐字相同。

因此：

- `S0` 只作为背景；
- 不用于建立同一稿件连续性；
- 不用于评价 Entropy 系统内 NER；
- 不把作者发送邮件自动称为制度选择事件。

## 4.2 `S1 → S2-N` 的连续性

Entropy 的接收与终止邮件具有：

- 相同稿号；
- 相同稿件标题；
- 相同稿件类型；
- 相同作者；
- 相同收稿日期；
- 相同栏目。

这足以把 `E-N1` 和 `E-N2` 视为同一制度对象的连续状态，但仍不证明提交附件的位级身份。

## 4.3 `S1 → S2-R → S3-A → S4-P` 的连续性

Frontiers 链具有：

- 稳定稿号 `1837760`；
- 稳定稿件标题；
- 稳定作者与期刊栏目；
- 投稿、初审、独立审稿、interactive review、final review、acceptance、production 和 proof 的连续状态通知。

该链足以支持一个制度对象从登记到接受后生产的连续审计。

---

# 5. 边界台账

## 5.1 `B0`：稿件文本／PDF

包含：

- 稿件文件；
- 标题、正文、图表和引用。

不包含：

- 作者内部状态；
- 投稿平台；
- 编辑；
- 审稿人；
- production；
- 费用承担；
- 公共索引。

最高允许等级：`SEA-1 upper bound`。

稿件可以包含候选、论证和决定文本，但文件本身不执行投稿、不承担制度后果，也不自动调用自己的历史。

## 5.2 `B1`：作者＋稿件

包含：

- 作者授权投稿、修订和校样；
- 作者的时间、排他投稿义务、修改劳动和费用风险；
- 稿件文件。

不包含：

- 期刊状态机；
- 编辑权限；
- reviewer assignment；
- production 系统。

本轮没有测量作者内部比较介质、候选竞争或匹配状态，因此不得把作者边界直接升级为 NER-2 或 SEA-3。

## 5.3 `B2`：投稿平台＋编辑流程

包含：

- 稿号与状态；
- 初始验证；
- 栏目路由；
- 编辑处理；
- 审稿流程状态；
- 接受／终止状态。

不包含：

- 作者资源与身体；
- 审稿人完整内部推理；
- production 后续；
- 公共出版与索引。

该边界可支持 NER 和 PEF，但若不纳入承受位置与后续调用，通常不能单独达到 SEA-3。

## 5.4 `B3`：作者＋平台＋编辑＋审稿＋production

包含：

- 投稿和修订授权；
- 编辑与 reviewer 状态；
- 截止期限；
- 接受／终止决定；
- 费用与校样义务；
- production 状态；
- proof 文件与校对接口。

这是本轮 Frontiers `SEA-3 qualified` 的边界。

注意：

- 该结果属于完整制度流程；
- 不属于稿件文本；
- 不属于任何自动邮件程序；
- 不归因于单独的编辑、单独的审稿人或任何 AI 工具；
- 作者、期刊与平台角色不能互相替代。

## 5.5 `B4`：公共学术记录系统

可能包含：

- 正式 published article；
- DOI；
- landing page；
- Crossref metadata；
- 数据库索引；
- 引用；
- 勘误、撤回和版本历史。

截至冻结时间，本轮没有核验这些对象。

判定：`unresolved`。

不能因为文章已经 accepted 或 proof ready，就提前声称：

- 已经公开发表；
- 已有 DOI；
- 已进入索引；
- 已形成领域知识写回；
- 已改变引用网络。

---

# 6. 普通制度理论基线

本案例首先由普通出版工作流解释：

- 文档管理；
- 状态机；
- access control；
- editorial triage；
- peer review；
- revision workflow；
- acceptance authorization；
- production handoff；
- invoicing；
- proof correction；
- records management。

SEA 不提出新的出版机制。

SEA 的候选增量只在于：

> 不把稿号、拒稿、接受、费用、日志和公开 DOI 混成一个“制度选择”；逐门检查这些事实是否在同一事件和边界内形成登记、执行、承受与未来写回。

若普通状态机与审计日志已经完整表达全部区分，SEA 应降级为跨域审计模板，而不是独立制度理论。

---

# 7. Entropy 阴性链逐门审计

## 7.1 `E-N1`：投稿登记

### DMF

证据：稿件和元数据进入投稿系统，系统发出正式接收确认并分配稿号。

判定：`DMF-2 supported`。

允许表述：

> 稿件差异进入制度有效通道。

不允许：

> 系统已经比较并选择该稿件。

### NER

证据：

- 稳定稿号；
- 栏目、类型、标题、作者、日期登记；
- 后续终止通知调用同一稿号与元数据。

限制：

- 无内部 editorial note；
- 无状态字段导出；
- 无稿号／栏目交换干预；
- 无内部阈值干预；
- 无竞争稿件集合证据。

判定：

```text
NER-1 supported
NER-2 qualified / intervention evidence incomplete
NER-3 not established
```

统一门槛不能把自动生成的接收邮件单独当作强内部比较证据。

### PEF

证据：

- 稿件进入真实处理路径；
- 作者确认排他投稿条件；
- 后续编辑终止只能发生在该制度路径已经建立之后。

判定：`PEF-2 qualified`。

提交不是建议或草稿；它改变了稿件在该期刊的现实状态。

### CBP

证据：

- 作者承担排他投稿义务；
- 存在等待与行政资源占用；
- 若接受，存在预先说明的许可与费用条件。

限制：

- 费用为条件性，不是已支付后果；
- 没有量化等待机会成本；
- 没有保护／转移干预；
- 平台自身承受位置未解析。

判定：

```text
CBP-1 supported
CBP-2 qualified at author–institution boundary
CBP-3 not established
```

### HEF

接收邮件与投稿记录是历史痕迹，但没有事件后证据证明该接收状态本身改变了另一个后续制度程序的可达性或规则。

判定：

```text
HEF-0 supported
HEF-1/2 possible but not tested
HEF-3 not established
```

### `E-N1` 总判定

```text
B0 manuscript → SEA-1
B2 platform/editorial process → SEA-2 qualified
B3 full author–institution boundary → SEA-2 qualified
```

---

## 7.2 `E-N2`：编辑终止

### DMF

已登记稿件进入编辑评价通道，终止通知明确引用同一制度对象。

判定：`DMF-2 supported`。

### NER

终止决定不是单纯输出字符串：它是机构对该稿件后续处理状态的非等价登记。

证据：

- 决定明确停止进一步处理；
- 通知列出 discipline、novelty 和 general significance 等选择维度；
- 同一稿号从“received”进入终止状态。

限制：

- 不知道各维度如何加权；
- 没有 reviewer assignment；
- 没有内部 decision field 导出；
- 没有阈值或候选集合干预。

判定：

```text
NER-2 qualified
NER-3 not established
```

不得推断：

- 一定由某位编辑个人决定；
- 一定由自动系统决定；
- 一定代表稿件质量低；
- 一定经过外部同行评审。

### PEF

终止状态真实改变制度路径：

- Entropy 路径不再继续；
- peer review、revision、acceptance 与 production 在该稿号下停止可达；
- 作者需要保留、修改、另投或停止。

判定：`PEF-3 qualified`。

这比接触端点、收到建议或状态显示更强，因为当前制度路径确实关闭。

### CBP

路径特异后果落到：

- 作者：等待、另投、版本调整与重新进入其他制度路径；
- 期刊：停止继续投入该稿件流程；
- 稿件对象：在该稿号下失去继续处理路径。

限制：

- 没有量化作者恢复成本；
- 没有验证稿件实际如何修改或另投；
- 不能把情绪反应作为未测量的承受证据；
- 不能把作者后果反投给投稿平台。

判定：`CBP-2 qualified`。

### HEF

拒稿通知和 terminal status 是可读取记录。

但以下证据缺失：

- 该记录被另一个投稿系统读取；
- 它改变未来期刊的可接受性或门槛；
- 它改变 Entropy 的一般规则；
- 它形成可调用的制度先例；
- 移除／遮蔽记录会改变后续路径；
- 匹配当前稿件状态后，不同拒稿历史产生不同未来可达性。

最重要的重复计数禁令：

> “该稿号停止处理”已经用于 PEF。若没有新的事件后 probe，不能把同一事实再次记为 HEF-3。

判定：

```text
HEF-0 supported
HEF-2 not established
HEF-3 failed for current evidence package
```

### `E-N2` 总判定

```text
B0 manuscript → SEA-1
B2 platform/editorial process → SEA-2 strong
B3 author–platform–editorial boundary → SEA-2 strong
B4 public scholarly record → unresolved
```

本案例是**制度历史效力阴性校准**，但不是完美单门隔离：NER-2 与 CBP-2 仍为 qualified，而非实验级 fully supported。

---

# 8. Frontiers 阳性链逐门审计

## 8.1 `E-P1`：投稿与独立审稿

### DMF

稿件进入初始验证，随后明确进入 independent review。

判定：`DMF-3 qualified`。

理由：

- 稿件不是只到达接口；
- 多条现实制度路径存在：验证失败、编辑终止、送审、修订、接受或拒绝；
- 后续状态证明至少多个路径阶段实际可进入。

### NER

证据链：

- 初始验证状态；
- independent review 状态；
- 两名 reviewer 报告；
- interactive review；
- 修订截止与延期；
- reviewer 新评论；
- final review。

这表明稿件状态不是固定单步映射，而是由编辑、审稿意见、修订稿与作者回应共同中介。

判定：

```text
NER-2 supported
NER-3 qualified
```

NER-3 仍为 qualified，因为：

- 审稿意见正文未进入仓库；
- 没有候选集合或决策权重导出；
- 没有交换 reviewer／revision 的实验干预。

### PEF

审稿状态实际改变现实路径：

- 产生 revision 义务；
- reviewer comments 触发作者响应；
- deadline 与 extension 影响继续资格；
- final review 取决于最新版本和审稿报告。

判定：`PEF-3 supported`。

替代路径被真实重分配，而不是只显示标签。

### CBP

可识别承受位置：

- 作者承担修订、回复、截止期限与继续参与条件；
- reviewer 承担评审工作；
- 编辑承担流程与判断；
- 期刊投入工作流资源。

限制：

- reviewer 与编辑成本未量化；
- 未解析全部工作外包链；
- 不从行政劳动推出道德或体验结论。

判定：

```text
CBP-2 supported
CBP-3 qualified
```

### HEF

在 `E-P1` 内，修订后的最新稿件与 reviewer record 被 final review 调用。

这提供主动历史携带：

- 过去 reviewer comments 改变当前修订要求；
- 最新版本取代旧版本进入下一阶段；
- final review 明确依赖审稿报告和最新稿件。

判定：

```text
HEF-2 supported
HEF-3 qualified
```

`HEF-3` 之所以仍为 qualified，是因为当前私有时间线未提供文件 hash、matched-present 比较或历史载体删除干预。

### `E-P1` 总判定

```text
B2 submission/review workflow → SEA-2 strong
B3 author–editor–reviewer system → SEA-3 qualified only if E-P1 includes revision write-back
```

为避免事件窗口扩张，本文把主要 SEA-3 判定负载放在更清楚的 `E-P2` 接受后 probe，而不是依赖本段的 qualified HEF。

---

## 8.2 `E-P2`：接受决定与接受后 probe

### DMF

`review finalised` 明确保留至少两个现实继续路径：

- editor 提出进一步问题／评论；
- editor 满意并 provisional acceptance。

随后实际发生 acceptance。

判定：`DMF-3 supported`。

### NER

接受决定调用：

- review reports；
- latest submitted manuscript；
- associate editor assessment；
- institutionally authorized acceptance state。

判定：

```text
NER-2 supported
NER-3 qualified
```

本报告不把自动通知程序当作做决定的位置。

### PEF

接受状态产生可核验的路径重分配：

```text
review / revision path closes
production path opens
proof-correction path opens
billing / funding path activates
publication-completion conditions change
```

判定：`PEF-3 supported`。

### CBP

接受后产生路径特异后果：

- 作者获得进入 production 的机会；
- 作者承担校样核验与短期限；
- 作者进入费用／资助处理路径；
- production office 承担排版与 copyediting；
- 错过 proof query 会延迟 publication；
- 角色与义务相对拒稿路径发生非对称变化。

费用证据纪律：

- 私有邮箱确认接受后产生 APC invoice 与 fee-support 流程；
- 本文件不记录金额或个人财务说明；
- invoice 证明实际义务接口，不证明已付款；
- 费用不是 SEA-3 的唯一或充分理由。

判定：

```text
CBP-2 supported
CBP-3 qualified
CBP-4 not established
```

### HEF

接受决定的历史载体至少包括：

- manuscript status = accepted；
- 稿号与 production handoff；
- accepted version；
- production record；
- proof object 与 query 状态。

事件后 probe 显示：

1. acceptance 后稿件进入 production；
2. production 生成 proof；
3. proof 状态向作者施加校对期限和完成条件；
4. 接受前的 review 状态不再是当前可执行路径；
5. 若校样 query 未解决，publication 会延迟。

这不是被动日志。accepted 状态被另一个后续流程实际调用，并改变：

- 可进入的制度路径；
- 作者下一步行动；
- 资源与角色配置；
- 完成门槛；
- 返回 review 路径的成本与权限。

判定：`HEF-3 supported`。

不升级为 `HEF-4`：

- 没有证据表明这次接受改变 Frontiers 的一般规则；
- 没有证据形成可约束其他稿件的制度先例；
- 没有公共 DOI、索引或引用网络证据；
- 没有规则／边界继承到其他实例的证明。

### `E-P2` 总判定

```text
B0 manuscript → SEA-1
B2 editorial status machine → SEA-2 strong
B3 author–editor–reviewer–production system → SEA-3 qualified
B4 public scholarly-record system → unresolved
```

`qualified` 的理由：

- 私有邮件证据而非公开数据包；
- 无随机化或严格 matched control；
- 内部 editor/reviewer decision variables 不完整；
- CBP 分配链未完全解析；
- public publication 尚未核验。

---

# 9. 为什么接受通知本身仍然不够

若只有一封 `accepted` 邮件，本报告最多会给：

- NER-2 qualified；
- PEF-2/3 qualified；
- CBP-1/2 qualified；
- HEF-0。

真正允许 HEF 升级的是**后续独立流程调用**：

```text
accepted status
→ production handoff
→ proof generated
→ author correction interface and deadline
```

因此：

> “被接受”作为标签，不等于历史写回；被接受状态实际改变后续流程，才构成 HEF-3 候选。

这与 GitHub 正确 SHA 案例相似：

- success 字符串不够；
- 必须验证 commit、blob、branch head 与后续 history。

但两个机制仍完全普通：

- GitHub 是内容寻址、compare-and-swap 和 ref update；
- 出版流程是状态机、授权、review、production handoff 和 records management。

不主张 SRT 特有机制。

---

# 10. 为什么拒稿的强烈后果仍然不等于 HEF

拒稿可能造成：

- 时间损失；
- 心理压力；
- 修改成本；
- 另投；
- 职业路径影响。

但本轮只记录有一手证据的制度事实。

没有测量：

- 心理状态；
- 实际修改量；
- 再投稿成本；
- 后续期刊决定；
- 引用或职业结果。

即使这些后果很强，也不能用来补偿 HEF：

> CBP 问“后果落到哪里”；HEF 问“过去结果通过什么载体改变后续可达路径”。两者不是同一事实。

---

# 11. 边界扰动测试

本案例同时提供方法策略要求的初步 boundary-perturbation pressure。

## 11.1 缩小到稿件文本

结果：`SEA-1`。

原因：

- 稿件不自主投稿；
- 不读取审稿状态；
- 不承担 invoice 或 proof deadline；
- 不把 acceptance 写入未来流程。

## 11.2 扩大到投稿平台

结果：`SEA-2`。

原因：

- 平台登记并路由；
- 状态改变实际流程；
- 但平台自身 CBP 和 HEF 不能由作者后果补足。

## 11.3 扩大到作者—编辑—reviewer—production

Frontiers `E-P2`：`SEA-3 qualified`。

原因：

- 角色、执行、承受与写回闭合；
- acceptance 被 production 实际调用。

## 11.4 继续扩大到公共学术系统

结果：`unresolved`，不能自动保持 SEA-3。

原因：

- 尚未核验 DOI、publication、indexing 或 citation；
- 更大边界引入新的承受位置与时间尺度；
- 局部 acceptance 不能自动证明领域知识结构已改变。

### 边界结论

```text
扩大边界不会单调增加证据等级。
```

边界扩大可能：

- 纳入缺失的承受位置；
- 也可能引入尚未测量的接口；
- 使时间尺度不再相容；
- 使原有证据无法覆盖新边界。

这阻止“把整个社会纳入系统即可制造 SEA-3”。

---

# 12. 时间尺度审计

## 12.1 Entropy

- 登记：分钟／小时；
- 编辑终止：约两天；
- 另投或修改：未测量；
- 公共出版与引用：未发生或未核验。

不能把数月后另一篇稿件的成功当作该 Entropy 稿件拒稿的 HEF。

## 12.2 Frontiers

- 投稿：2026-03-24；
- independent review：2026-05-04；
- review / revision：5 月至 7 月；
- final review：2026-07-15；
- acceptance：2026-07-17；
- proof：2026-07-28。

这些阶段通过同一稿号、同一标题与连续状态机因果连接，时间尺度相容。

但以下尺度仍未纳入：

- publication date；
- DOI registration；
- indexing；
- citation；
- correction / retraction；
- 职业与领域影响。

因此 B4 不能由 B3 的证据补足。

---

# 13. 配对校准表

| 维度 | Entropy termination | Frontiers acceptance → proof |
|---|---|---|
| 同一稿件链连续性 | 稳定稿号、标题、日期 | 稳定稿号、标题、连续状态 |
| 进入制度系统 | 是 | 是 |
| 独立同行评审证据 | 无 | 有 |
| revision loop | 无 | 有 |
| authorized terminal decision | decline | acceptance |
| 当前路径改变 | 终止处理 | 关闭 review，开启 production |
| 作者路径特异后果 | qualified | supported |
| production handoff | 无 | 有 |
| proof object | 无 | 有 |
| 后续流程调用 terminal state | 未建立 | 已建立 |
| HEF-3 | 未建立 | supported |
| B3 SEA | SEA-2 strong | SEA-3 qualified |
| public DOI / indexing | 未建立 | 未核验 |

## 13.1 不能作因果比较

两列存在大量混杂：

- 不同稿件；
- 不同期刊；
- 不同学科；
- 不同日期；
- 不同审稿制度；
- 不同稿件质量与契合度；
- 不同编辑和 reviewer；
- 不同作者版本与响应。

因此不能说：

- 某一特征导致接受；
- 某一期刊流程更好；
- SEA 预测了决定；
- 接受链证明 SRT 理论正确。

配对目的仅是：

> 检查相同审计是否能区分“登记后终止”与“接受状态被后续生产流程调用”。

---

# 14. 跨域门失败矩阵

| 案例 | 最高结果 | 决定性降级点 |
|---|---|---|
| AI mutation 未调用 | SEA-1 | PEF 未进入真实写入 |
| AI wrong SHA / 409 | SEA-1 | endpoint contact 未形成提交 |
| AI correct SHA | B3 SEA-3 qualified | commit/ref 写回验证成立 |
| E. coli 标准趋化 | SEA-2 strong | same-event CBP 未建立 |
| Entropy termination | SEA-2 strong | HEF-3 未建立；NER/CBP 仍 qualified |
| Frontiers acceptance → proof | B3 SEA-3 qualified | B4 public write-back 尚未核验 |

这张表开始显示非补偿式审计的跨域价值：

- 软件负例停在执行门；
- 生命负例停在承受门；
- 制度负例停在历史效力门；
- 软件与制度阳性在较大完整边界中达到 SEA-3 qualified；
- 任一较大边界结果都不能反投给局部模型、细胞信号、稿件文本或自动邮件程序。

---

# 15. 反事实与降级测试

## 15.1 只保留接收邮件

若删除后续终止／审稿／接受／production 记录：

- DMF 保留；
- NER 降级；
- PEF 只到入队；
- CBP 主要是一般程序成本；
- HEF 只到历史痕迹。

## 15.2 只保留 accepted 邮件

若删除 production 与 proof 记录：

- accepted 是制度状态；
- PEF 可 qualified；
- HEF-3 不允许；
- SEA-3 应撤回。

## 15.3 接受后没有 production

预注册反例：

- 接受邮件误发、撤销或系统故障；
- 没有 typesetting、proof 或后续状态；
- 不能因 accepted 标签升级 HEF。

## 15.4 proof 存在但不是该稿件

若 Article ID、标题或作者不匹配：

- 同事件链断裂；
- 不能把 proof 用作接受事件的 HEF。

当前 Frontiers proof 与同一 Article ID 对应，因此连续性成立；本报告仍建议未来获取 proof 文件 hash。

## 15.5 DOI 出现但未进入后续过程

仅有 DOI 仍最多是 HEF-0/2 候选。

要主张公共知识写回，需要额外证明：

- DOI metadata 被索引；
- 页面公开可达；
- correction/version 机制有效；
- 记录实际约束后续引用或检索。

---

# 16. 编码手册的直接输入

本案例为下一步 `SEA_CASE_CODING_MANUAL_v0_1` 提供以下字段。

## 16.1 事件身份字段

- case_id；
- manuscript_id；
- title；
- institution；
- start event；
- end event；
- post-event probe；
- continuity keys；
- missing hash / version evidence。

## 16.2 边界字段

- artifact-only；
- author-plus-artifact；
- platform/editorial；
- author/editor/reviewer/production；
- public scholarly record。

## 16.3 门槛字段

每一门分别编码：

- `supported`；
- `qualified`；
- `unresolved`；
- `failed`；
- evidence carrier；
- intervention evidence；
- counterfactual；
- privacy restriction；
- duplicate-count risk。

## 16.4 特殊编码规则

1. acceptance 与 production 必须分开；
2. current path closure 与 future write-back 必须分开；
3. invoice 不等于 payment；
4. proof 不等于 publication；
5. DOI 不等于 citation；
6. reviewer report existence 不等于 report quality；
7. automated email 不等于 automated decision；
8. author consequence 不归给平台或 AI；
9. 较大制度边界等级不归给稿件文本；
10. 私有邮件存在不等于公开可复核。

---

# 17. 对方法论文策略门槛的影响

## 17.1 已推进

策略文件要求的“一个制度或组织案例”现在获得第一轮满足：

- 一个真实制度负例；
- 一个真实制度阳性；
- 同一审计产生不同等级；
- 明确 boundary perturbation；
- 明确 current path 与 historical write-back 区分。

## 17.2 尚未完成

方法论文仍不 ready，至少还缺：

1. 独立编码者；
2. inter-rater reliability；
3. 脱敏可复核证据包；
4. 系统性近邻协议搜索；
5. ordinary-theory-only vs ordinary-theory-plus-SEA 对比；
6. Frontiers public publication / DOI 后续核验；
7. 自然系统 same-event CBP + HEF 数据，或正式保留失败；
8. 边界扰动在更多案例中的重复。

## 17.3 最重要的新方法压力

本案例显示：

> 制度状态机天然拥有日志、角色、权限和持续记录，因此最容易产生“所有门都已满足”的错觉。

SEA 必须特别阻止：

- status label 冒充 NER；
- decision email 冒充 PEF；
- APC 冒充 CBP；
- archive / DOI 冒充 HEF；
- accepted 冒充 published；
- published 冒充领域知识结构改变。

---

# 18. 限制

1. 两个案例不是同一稿件的严格正负配对；
2. 没有公开附上邮件；
3. 没有平台状态导出或 API 日志；
4. 没有提交文件 hash；
5. Entropy 内部编辑状态不可见；
6. Frontiers reviewer 与 editor 判断介质不完整；
7. 没有量化作者时间、风险或恢复成本；
8. 费用证据只证明义务接口，不证明最终支付；
9. proof ready 不等于 published；
10. 没有 DOI、Crossref、索引或 citation 核验；
11. 无独立编码者；
12. 所有等级都是方法校准结论，不是制度本体论结论。

---

# 19. 非主张

本报告不证明：

- 学术期刊是主体；
- 稿件具有主体性或意识；
- 编辑决定具有自由意志；
- reviewer 承担第一人称 stake；
- 自动邮件系统作出了接受或拒绝决定；
- AI reviewer assistant 获得授权、责任或历史；
- 拒稿不公平或接受正确；
- Frontiers 或 Entropy 的总体质量；
- 接受稿件的科学结论为真；
- 拒稿稿件的科学结论为假；
- SEA 解释了决定原因；
- SEA 优于普通 workflow、records management 或 causal process tracing；
- 五门是制度选择的必要充分条件；
- SEA-3 等同 L2、意识、道德责任或生成健康；
- accepted 等于 published；
- proof 等于 DOI；
- DOI 等于领域影响。

---

# 20. 最终判定

## 20.1 Entropy

```text
E-N1 registration:
DMF-2 supported
NER-1 supported / NER-2 qualified
PEF-2 qualified
CBP-2 qualified at expanded boundary
HEF-0 supported
→ SEA-2 qualified

E-N2 termination:
DMF-2 supported
NER-2 qualified
PEF-3 qualified
CBP-2 qualified
HEF-3 not established
→ SEA-2 strong
```

## 20.2 Frontiers

```text
E-P1 review workflow:
DMF-3 qualified
NER-2 supported / NER-3 qualified
PEF-3 supported
CBP-2 supported / CBP-3 qualified
HEF-2 supported / HEF-3 qualified
→ SEA-2 strong; B3 SEA-3 only qualified

E-P2 acceptance with production probe:
DMF-3 supported
NER-2 supported / NER-3 qualified
PEF-3 supported
CBP-2 supported / CBP-3 qualified
HEF-3 supported
→ B3 SEA-3 qualified
```

## 20.3 Public scholarly record

```text
publication / DOI / indexing / citation:
unresolved as of 2026-08-05
```

## 20.4 校准序列

```text
private manuscript artifact
→ SEA-1

registered submission with real workflow effects
→ SEA-2

registered submission terminated without demonstrated future write-back
→ SEA-2 strong

accepted state called by production and proof workflow
→ B3 SEA-3 qualified

public knowledge-system write-back
→ not yet established
```

---

# 21. 下一步

按已冻结方法论文路线，下一步不再新增案例，而是创建：

```text
SEA_CASE_CODING_MANUAL_v0_1
```

编码手册应以以下六个案例作为训练集：

1. AI mutation 未调用；
2. AI wrong SHA / 409；
3. AI correct SHA commit；
4. E. coli chemotaxis；
5. Entropy termination；
6. Frontiers acceptance → proof。

随后：

- 生成脱敏 case packet；
- 邀请至少一名不知道预期答案的编码者；
- 计算逐门一致性；
- 检查分歧是否集中在 NER、CBP、HEF 或边界选择；
- 一致性不足时修订手册，不修改案例结果以追求一致。

---

# 22. 一句话结论

> 学术制度中的登记、拒绝、接受、费用和档案都不能自动构成完整选择事件；在本轮私有证据中，Entropy 的登记后终止停在 `SEA-2 strong`，而 Frontiers 的接受状态因被后续 production 与 proof 流程实际调用，在作者—编辑—审稿—生产的完整边界达到 `SEA-3 qualified`，但公共出版与知识系统写回仍未建立。
