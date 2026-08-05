---
id: SRT-SEA-CASE-CODING-MANUAL-V0-1-20260805
title: "SEA 案例编码手册 v0.1：独立判定、降级与一致性测试"
title_en: "SEA Case Coding Manual v0.1: Independent Classification, Downgrade Rules, and Reliability Testing"
type: coding_manual
status: active
version: v0_1
record_stage: reliability_pilot_ready
layer: meta
epistemic_layer: os
claim_mode: operations_execution
claim_level: audit_only
canonical: false
ai_do_not_use_for_definition: true
created: 2026-08-05
revised: 2026-08-05
provenance: 2026-08-05 作者要求在制度系统配对校准合并后继续推进统一选择事件审计方法路线。本手册把现有统一协议压缩为可由不了解预期结论的独立编码者执行的冻结、编码、降级、分歧记录和一致性测试流程；不修改协议定义，不预先认定现有案例结论正确。
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
  - Operations/SRT_INSTITUTIONAL_PUBLICATION_PAIRED_UNIFIED_AUDIT_2026-08-05.md
  - Philosophy/Papers/Selection_Event_Audit_Method_Paper_Strategy.md
---

# SEA 案例编码手册 v0.1

## 0. 文件角色

本文件是统一选择事件审计的**案例编码手册**，服务于下一阶段的独立编码一致性测试。

它不是：

- 新的选择定义；
- canonical 文件；
- 对统一协议的修订；
- 五门必要充分性的证明；
- 主体性、意识、自由、责任、L₂ 或生成健康判据；
- 对既有 AI、生命或制度案例结论的自动确认；
- 用总分替代逐门审计的评分表。

本手册只解决一个操作问题：

> 当两名或更多编码者只获得冻结证据包、不了解预期结论时，如何以同一规则独立确定事件、边界、时间尺度、五门等级、链路状态、决定性降级点和最高允许 SEA 类别？

手册的成功标准不是“编码者都同意作者”，而是：

1. 编码单位能够稳定冻结；
2. 五门能够分开编码；
3. 不同失败门能够被独立恢复；
4. 边界改变不会无证据地自动升级；
5. 时间尺度不相容会阻止统一等级；
6. 分歧可以被定位到具体规则，而不是靠印象协商；
7. 可靠性不足时，方法路线能够停止或降级。

---

# 1. 核心纪律

## 1.1 编码单位不是“一个系统”

最小编码单位为：

```text
U = <event, boundary, timescale, evidence packet version>
```

即：

> **一个冻结事件 × 一个明确边界 × 一组相容时间尺度 × 一个锁定证据包版本。**

同一个系统可以产生多个编码单位：

- 同一 AI 事务分别在模型边界、工具链边界和完整社会技术边界编码；
- 同一细菌过程分别在细胞内信号边界、细胞—环境闭环边界编码；
- 同一出版流程分别在稿件、投稿平台、作者—编辑—审稿—生产系统和公共学术记录边界编码。

不得给“AI”“细菌”“期刊”“机构”整体赋予一个脱离事件的固定 SEA 等级。

## 1.2 五门不可加权补偿

编码者必须分别给出：

- DMF；
- NER；
- PEF；
- CBP；
- HEF。

禁止：

- 求和；
- 求平均；
- 使用雷达图面积；
- 因某一门特别强而补偿另一门失败；
- 因案例“看起来复杂”而提高总体等级；
- 因结果成功、重要、昂贵或有社会影响而提高总体等级。

总体 SEA 类别只能由本手册 §11 的规则推导。

## 1.3 证据不足与门槛失败必须分开

以下两种情况不能混同：

### `unresolved`

证据包不足以判断最低门槛是否满足。

### `failed`

冻结证据或预注册阴性结果显示最低门槛没有满足。

例如：

- 没有测量后果变量：CBP 可能是 `unresolved`；
- 已测量且路径干预不改变任何边界相关后果：CBP 可以是 `failed`；
- 没有检查日志是否被后续调用：HEF 为 `unresolved`；
- 删除日志不改变未来路径，且没有其他载体：该日志的 HEF 主张为 `failed`。

`unresolved` 不能被当作“可能成立”用于升级。

## 1.4 领域机制优先

编码者应首先用领域内普通机制描述事实，例如：

- Git compare-and-swap、提交和 ref 更新；
- 细菌受体适应、CheY-P 和鞭毛马达；
- 编辑状态机、同行评审、生产与校样流程；
- 权限、预算、执行器、资源路由和持久记录。

SEA 只编码事件识别结构，不替代领域机制。

即使一个案例达到 SEA-3，也不得据此写成：

> SRT 提供了该系统的独立因果机制。

## 1.5 角色不得洗白

编码时必须分开：

- 差异生成者；
- 登记者；
- 授权者；
- 执行者；
- 受益者；
- 承受者；
- 修复者；
- 记录或写回位置。

尤其禁止：

- 把人的授权归给模型；
- 把工具执行归给纯文本输出；
- 把用户后果说成 AI 自身承受；
- 把组织后果说成某个单独组件的后果；
- 把公共影响倒投给尚未公开的稿件；
- 把种群长期收益倒投给某一次单细胞事件。

---

# 2. 编码团队与盲化

## 2.1 最低角色

可靠性试验至少包含：

1. **证据包准备者 P**：制作脱敏、版本锁定的材料包；
2. **编码者 A**：独立编码；
3. **编码者 B**：独立编码；
4. **裁决者 J**：在两名编码者锁定结果后处理分歧。

P、A、B、J 可以由三人承担，其中 P 与 J 可为同一人；但 A 与 B 不能是同一人，且编码阶段不得讨论案例。

## 2.2 编码者不应看到的内容

测试编码者不得看到：

- 既有审计报告的最终 SEA 等级；
- “positive control”“negative control”“成功案例”“失败案例”等预期标签；
- PR 标题或摘要中包含的结论；
- 作者对决定性失败门的说明；
- 其他编码者的表格、批注或置信判断；
- 裁决规则之外的临场提示。

若证据包材料本身不可避免地包含“accepted”“rejected”“commit succeeded”等事实，可以保留事实，但不得告诉编码者这些结果应对应何种 SEA 等级。

## 2.3 允许编码者看到的内容

每名编码者必须获得完全相同的：

- 本手册锁定版本；
- 统一协议和四个门协议；
- 冻结证据包；
- 证据包目录与文件哈希；
- 字段定义；
- 空白编码表；
- 普通理论基线说明；
- 隐私与非主张要求。

## 2.4 独立性

在提交锁定编码前，A 与 B 不得：

- 讨论具体案例；
- 共享搜索结果；
- 交换边界图；
- 询问对方的等级；
- 根据对方的理由修改结果；
- 查看作者预期答案。

编码完成时间不同不构成问题；关键是各自结果在首次提交时被保存并带有时间戳与文件哈希。

## 2.5 训练包与测试包分离

允许使用不计入可靠性统计的训练包。

训练包用于：

- 熟悉字段；
- 检查手册歧义；
- 练习区分 `unresolved` 与 `failed`；
- 练习边界分离和角色归属。

测试开始后：

- 不得依据测试分歧修改手册并继续沿用旧编码；
- 若规则发生实质修改，受影响测试单位必须重新盲化并重新编码；
- 训练包不得与正式测试单位完全相同。

---

# 3. 证据包标准

## 3.1 每个证据包的最小目录

```text
PACKET_<opaque_id>/
  00_MANIFEST.md
  01_EVENT_TIMELINE.md
  02_BOUNDARY_LEDGER.md
  03_ROLE_LEDGER.md
  04_VARIABLE_MAP.md
  05_PRIMARY_TRACES/
  06_BASELINES_AND_CONTROLS.md
  07_MISSING_EVIDENCE.md
  08_PRIVACY_AND_REDACTION.md
  09_HASHES.txt
```

测试时使用不携带预期结论的 opaque ID，例如：

```text
PACKET-R07
PACKET-K12
PACKET-M03
```

不得使用：

```text
AI_POSITIVE
ENTROPY_NEGATIVE
ECOLI_FAILED_CBP
```

## 3.2 `00_MANIFEST.md`

必须列出：

- packet ID；
- packet version；
- 准备日期；
- 文件清单；
- 来源类型；
- 是否脱敏；
- 是否包含私有材料；
- 是否允许编码者访问原始来源；
- 排除的材料；
- 所有文件哈希。

不得包含预期 SEA 结论。

## 3.3 `01_EVENT_TIMELINE.md`

只记录可证实状态变化：

- 时间；
- 可观测状态；
- 触发条件；
- 执行或拒绝结果；
- 后续状态；
- 来源。

不得把解释写进时间线，例如：

```text
错误：此处发生真正选择。
正确：服务端返回 409；目标分支 head 未改变。
```

## 3.4 `02_BOUNDARY_LEDGER.md`

至少提供两个候选边界，复杂社会技术案例通常提供三个：

| 边界 | 包含 | 排除 | 输入通道 | 执行通道 | 后果位置 | 历史载体 |
|---|---|---|---|---|---|---|
| B1 |  |  |  |  |  |  |
| B2 |  |  |  |  |  |  |
| B3 |  |  |  |  |  |  |

边界由证据包准备者提出，但编码者可以：

- 接受；
- 收紧；
- 拆分；
- 判定不可编码。

编码者不得为了补足某一门而临时把任意外部对象纳入边界。

## 3.5 `03_ROLE_LEDGER.md`

至少区分：

| 角色 | 候选位置 | 证据 | 是否在当前边界内 |
|---|---|---|---|
| 差异提供 |  |  |  |
| 内部登记 |  |  |  |
| 授权 |  |  |  |
| 执行 |  |  |  |
| 受益 |  |  |  |
| 承受 |  |  |  |
| 修复 |  |  |  |
| 写回 |  |  |  |

## 3.6 `04_VARIABLE_MAP.md`

使用统一报告占位符：

```text
Δ = 目标差异
M = 登记介质
A = 路径通道
X = 后果承受位置
H = 历史载体
```

这些只是报告字段，不是 canonical 符号。

必须注明：

- 每个变量的直接证据；
- 可能混杂；
- 可用干预；
- 未测量项；
- 哪些变量来自不同实验或不同时间尺度。

## 3.7 `05_PRIMARY_TRACES/`

优先级从高到低：

1. 目标对象的直接前后状态；
2. 带时间戳的执行、拒绝、提交或状态转移记录；
3. 实验原始数据或原始测量；
4. 一手制度通知或正式记录；
5. 论文中的方法与结果；
6. 二手摘要；
7. 研究者事后叙述。

低优先级材料可以用于背景，不能在缺少直接证据时自动承担高等级门槛。

## 3.8 `06_BASELINES_AND_CONTROLS.md`

至少列出一个最强普通解释：

- 固定映射；
- 预设脚本；
- 单路径反射；
- 共同外部驱动；
- 一般控制回路；
- 一般成本；
- 缓存或普通迟滞；
- 普通权限和事务机制；
- 普通制度状态机；
- 观察者事后分类。

并列出：

- 无差异基线；
- 无执行基线；
- 拒绝或断连基线；
- 无后果或保护基线；
- 历史重置或未调用基线；
- 已执行但未写回的中间态，如存在。

## 3.9 `07_MISSING_EVIDENCE.md`

准备者必须主动列出缺失项，而不是让编码者误以为未提供即不存在。

示例：

- 没有内部状态干预；
- 没有同细胞代谢测量；
- 没有正式 DOI；
- 没有证据表明日志被后续过程调用；
- 没有比较替代路径；
- 没有文件哈希连接两个版本；
- 没有公共可访问验证。

## 3.10 证据包版本锁

任何材料变化都必须：

1. 增加 packet version；
2. 更新 manifest；
3. 更新哈希；
4. 说明新增、删除和修改；
5. 判断是否影响既有编码。

如果新增材料触及事件、边界、门等级或链路，原编码不得继续作为同一可靠性样本使用。

---

# 4. 证据充分性字段

门等级与证据充分性分开记录。

## 4.1 `evidence_status`

每个门和链路使用以下一种状态：

### `supported`

冻结证据直接满足该等级的负载条件，且没有未解决的决定性冲突。

### `qualified`

最低门槛可以成立，但至少存在一个明确限制，例如：

- 干预是自然实验而非直接操纵；
- 证据只在特定边界成立；
- 因果链存在合理但非唯一解释；
- 一手材料可读但不能公开复核；
- 测量代理与目标变量之间仍有有限缺口。

### `unresolved`

证据不足以确定是否达到最低门槛。

### `failed`

有直接反证、阴性干预或状态验证表明最低门槛没有达到。

### `not_codable`

事件、边界、时间尺度或证据包严重不完整，无法进行有效编码。

`not_codable` 不是 SEA-0。它表示编码任务本身无效。

## 4.2 `confidence`

编码者另外记录：

- `high`；
- `medium`；
- `low`。

置信度不能改变门等级。

低置信的高等级仍须按高等级进入一致性统计；裁决时再检查理由。

## 4.3 允许的总体后缀

新编码使用两个字段，不把形容词混入 SEA 数字：

```text
sea_category: SEA-2
sea_evidence_status: qualified
```

允许的总体状态：

- `supported`；
- `qualified`；
- `upper_bound`；
- `unresolved`；
- `not_codable`。

### `upper_bound`

只能证明案例不超过某等级，但不足以完整建立该等级时使用。

例如：

```text
sea_category_upper_bound: SEA-2
sea_evidence_status: upper_bound
```

既有报告中的 `SEA-2 strong`、`SEA-2 upper bound` 等遗留写法不在本手册中自动改写；正式重编码时映射到以上双字段格式。

---

# 5. Phase 0：编码资格检查

编码者首先回答以下问题。

## 5.1 资格表

| 字段 | 允许值 |
|---|---|
| event_start 可定位 | yes / no / disputed |
| event_end 可定位 | yes / no / disputed |
| target transition 明确 | yes / no / disputed |
| boundary 明确 | yes / no / disputed |
| timescale 可说明 | yes / no / disputed |
| 至少一个替代路径真实可达 | yes / no / unresolved |
| evidence packet 完整且哈希匹配 | yes / no |
| 隐私权限允许编码 | yes / no |

## 5.2 停止条件

出现以下任一情况，编码单位标记为 `not_codable`：

- packet 哈希不匹配；
- 编码者获得的材料版本不同；
- 事件起止完全无法定位；
- 系统边界无法说明包含与排除；
- 材料混入预期答案且无法重新盲化；
- 私有材料权限不清楚；
- 证据包在编码期间实质改变。

如果事件可冻结，但差异没有进入系统，则继续编码并可能得到 SEA-0；不要用 `not_codable` 代替阴性结果。

---

# 6. Phase 1：事件冻结

## 6.1 事件字段

每个编码单位必须填写：

| 字段 | 内容 |
|---|---|
| event_id | 唯一编号 |
| event_start | 最早属于目标事件的状态或差异进入 |
| event_end | 目标路径结果或写回完成点 |
| prehistory | 只作为背景的前史 |
| posthistory | 不属于事件的后续结果 |
| target_transition | 被审计状态迁移 |
| candidate_alternatives | 当时现实可达的替代路径 |
| exclusion_rule | 哪些事实不得倒灌进本事件 |

## 6.2 禁止事后扩窗

以下做法必须触发降级或 `not_codable`：

- 当前事件没有 HEF，于是把数月后的无关适应纳入；
- 当前细胞事件没有 CBP，于是加入群体长期增长；
- acceptance 尚未公开，于是加入假设的未来 DOI 与引用；
- API 请求被拒绝，于是把错误处理日志当作目标提交结果；
- 会议决定未执行，于是把后来另一团队的行动计入。

## 6.3 相邻事件必须拆分

若一个流程包含多个制度或技术状态，优先拆分：

```text
登记事件
执行或拒绝事件
接受或终止事件
生产写回事件
公共发布事件
```

只有存在明确因果连续性、统一边界和相容时间尺度时，才允许再建立较大复合事件。

---

# 7. Phase 2：边界与时间尺度

## 7.1 每个边界单独编码

编码表不得使用：

```text
B1/B2/B3 combined best score
```

必须为每个边界建立独立行：

```text
U-01-B1
U-01-B2
U-01-B3
```

## 7.2 边界升级检查

从较小边界升级到较大边界时，编码者必须列出新增证据：

| 新增项目 | 必须回答 |
|---|---|
| 新内部介质 | 哪个状态现在位于边界内并中介差异？ |
| 新执行通道 | 哪个执行器或资源路由现在属于系统？ |
| 新承受位置 | 谁或什么在新边界内承担路径特异后果？ |
| 新历史载体 | 什么载体改变未来可达性或规则？ |
| 新普通解释 | 更大系统是否可由组织或控制理论充分解释？ |

如果只有“边界变大”，没有新增门证据，不得升级。

## 7.3 时间尺度台账

至少分别记录：

| 窗口 | 时间尺度 |
|---|---|
| Δ 进入 |  |
| M 登记 |  |
| A 执行 |  |
| X 后果显现 |  |
| H 写回 |  |
| H 影响 future |  |
| 自然恢复／缓存清空 |  |

## 7.4 时间尺度兼容性

编码者对每一相邻环节给出：

- `compatible`；
- `qualified_compatible`；
- `incompatible`；
- `unresolved`。

以下不允许直接拼接：

- 毫秒级 NER + 数小时后未连接的代谢变化 + 多代进化 HEF；
- 一次工具输出 + 数周后由人独立完成的仓库修改；
- 一次编辑决定 + 数年后无法追踪来源的引用；
- 一个细胞轨迹 + 种群层平均增长，缺少跨尺度归因。

任一负载链路时间尺度为 `incompatible`，不得给统一 SEA-3/4。

---

# 8. Phase 3：五门编码

# 8.1 CG-0 / DMF

## 问题

> 目标差异是否越过固定边界，进入能够改变内部状态或现实候选路径的有效通道？

## 等级

| 等级 | 编码条件 |
|---:|---|
| 0 | 只有观察者枚举或事后标签 |
| 1 | 差异到达接口，但有效性未建立 |
| 2 | 屏蔽、交换或改变差异会改变系统可用内部状态或候选通道 |
| 3 | 差异对应多个现实可进入的继续路径或连续分岔场 |
| 4 | 历史、反馈或资源状态改变哪些差异能够成为活候选 |

## 最低负载证据

- 目标差异定义；
- 差异屏蔽或交换；
- 输入通道；
- 候选路径现实可达性；
- 排除纯标签解释。

## 常见降级

- 研究者能描述两个选项，但系统只有一条现实路径；
- UI 显示两个按钮，但其中一个不可执行；
- 两种输入物理不同，却没有证据进入系统作用通道；
- 结果发生后才把轨迹命名为不同候选。

# 8.2 CG-1 / NER

## 问题

> 固定边界内是否存在因果中介，使候选差异产生内部非等价登记？

## 等级

| 等级 | 编码条件 |
|---:|---|
| 0 | 只有外部可区分输出 |
| 1 | 固定差分转导、硬编码阈值或稳定映射 |
| 2 | 内部权重、阈值、资源或状态中介相对不等价；干预可改变不等价 |
| 3 | 对候选 A 的登记依赖候选 B、候选集合、共享资源或关系背景 |
| 4 | 登记结果进入后续阈值、资源、路径或历史写回接口 |

## 最低负载证据

- 指认 M；
- M 位于当前边界内；
- M 接受 Δ 的影响；
- 干预 M 改变相对响应，而非只改变总体幅度；
- 排除固定独立通道足以解释全部差异。

## 常见降级

- 只有最终输出不同；
- 只有编辑者或观察者的分类；
- 模型内部状态不可访问且没有替代因果证据；
- 固定受体差异被直接称为当前比较；
- 候选关系从未改变内部响应。

# 8.3 CG-2 / PEF

## 问题

> 登记或控制信号是否通过可干预通道改变现实路径？

## 等级

| 等级 | 编码条件 |
|---:|---|
| 0 | 标签、分数、排序、建议或观察差异 |
| 1 | 指令或咨询接口存在，但真实执行未建立 |
| 2 | 信号通过执行器、资源路由或环境接口改变实际路径 |
| 3 | 一条路径被实现或稳定，替代路径的概率、资源、延迟或成本相对改变 |
| 4 | 结果反馈到系统并在扰动下持续重组路径 |

## 最低负载证据

- 指认 A；
- 目标信号进入 A；
- A 的切断、替换或路由干预改变实际状态；
- 目标对象前后状态；
- 区分请求、服务端处理、提交和环境完成；
- 区分制度决定、授权、执行和制度化。

## 常见降级

- 输出命令但执行器禁用；
- API 被调用但目标事务失败；
- 返回成功字符串但目标状态未改变；
- 委员会形成意见但无权限或资源变化；
- 外部人看到建议后独立行动，耦合未解析；
- 行动只是固定脚本的下一步。

# 8.4 CG-3 / CBP

## 问题

> 目标路径相对于匹配基线是否产生落到可识别位置、影响维持或未来路径的边界相关后果？

## 等级

| 等级 | 编码条件 |
|---:|---|
| 0 | 只有外部影响痕迹 |
| 1 | 一般能量、时间、算力、工时或材料成本 |
| 2 | 路径特异后果改变边界内维持、恢复、风险、资源或未来可达路径 |
| 3 | 后果在候选位置间非对称分配；保护、交换或转移干预改变承担位置 |
| 4 | 授权、执行、受益、承受、修复和写回链得到解析 |

## 最低负载证据

- 指认 X；
- 目标路径与匹配基线；
- 路径特异后果变量；
- 后果影响维持、恢复、风险或未来行动能力；
- 保护、缓冲、路由或位置交换证据；
- 区分一般实现成本与路径后果。

## 常见降级

- 一切计算都耗电；
- 一切制度程序都耗时；
- 拒绝让人不愉快，但没有可编码状态或路径变量；
- 系统产生环境影响，但承受位置不清楚；
- 群体平均收益被倒投给单个事件；
- 用户承担后果，却被说成模型自身 stake。

# 8.5 CG-4 / HEF

## 问题

> 事件结果是否通过可定位、可干预载体改变未来候选可达性、转换概率、返回成本、门槛或规则？

## 等级

| 等级 | 编码条件 |
|---:|---|
| 0 | 外部日志、记录或痕迹可读取，但未进入后续过程 |
| 1 | 被动持续状态、缓存、疲劳或自然恢复前残留 |
| 2 | 历史载体被后续过程主动调用，改变当前响应或资源配置 |
| 3 | 先前路径改变未来候选可达性、转换概率、返回成本、门槛或候选生成 |
| 4 | 更新规则、制度约束、系统边界、权限或继承结构被写回 |

## 最低负载证据

- 指认 H；
- H 与目标事件结果连接；
- H 被后续过程调用；
- 重置、迁移、替换或消融 H 改变 future；
- future 指标是可达性、门槛、转换成本、候选生成或规则；
- 效力超出自然恢复、缓存或瞬时残留窗口。

## 常见降级

- 有日志但运行系统从不读取；
- 参数改变但未来行为未改变；
- 结果留下记录但没有后续调用；
- 当前路径终止被重复计为历史写回；
- acceptance 通知存在，但没有 production 或后续流程调用；
- 历史相关性存在，但 matched-present 或载体干预缺失。

---

# 9. Phase 4：链路编码

五个变量存在不等于事件链成立。

## 9.1 必编码链路

| 链路 | 最低问题 |
|---|---|
| `Δ → M` | 改变差异是否改变相对内部登记？ |
| `M → A` | 改变介质或耦合是否改变现实路径？ |
| `A → X` | 改变目标路径是否改变边界相关后果？ |
| `X → H` | 目标后果或结果是否进入历史载体？ |
| `H → future` | 改变载体是否改变未来可达性或成本？ |

## 9.2 链路状态

每条链路编码为：

- `pass`；
- `qualified_pass`；
- `partial`；
- `failed`；
- `unresolved`；
- `incompatible_timescale`；
- `boundary_mismatch`。

## 9.3 `partial` 不能用于完整事件

`partial` 表示存在相关或间接连接，但没有达到最低因果负载。

例如：

- M 与 A 同时变化，但共同驱动未排除；
- A 后出现 X，但没有路径干预；
- X 与 H 同时记录，但没有证明 X 写入 H；
- H 与 future 相关，但没有载体干预。

任何负载链路为 `partial`、`failed`、`unresolved`、`incompatible_timescale` 或 `boundary_mismatch`，不得给 SEA-3/4。

---

# 10. Phase 5：普通理论对照

## 10.1 字段

每个编码单位填写：

```text
ordinary_frameworks_considered:
ordinary_explanation_status:
sea_added_distinctions:
```

## 10.2 `ordinary_explanation_status`

允许值：

- `fully_sufficient`；
- `partially_sufficient`；
- `insufficient_for_recorded_distinction`；
- `not_assessed`。

## 10.3 与 SEA 等级的关系

普通理论是否充分，不直接改变 SEA 事件类别。

例如：

- Git 事务可完全由普通工程理论解释，但仍可作为 SEA 校准；
- 趋化可由普通生化与控制机制解释，但 SEA 可记录同事件 CBP 缺口；
- 编辑状态机可由普通制度理论解释，但 SEA 可检查执行与历史写回是否被混同。

若普通理论完全覆盖所有区分，则方法论文的新颖性降级；但不得因此伪造门失败。

---

# 11. 总体 SEA 类别推导

## 11.1 推导顺序

编码者先完成事实与门编码，再使用以下规则。不得先选 SEA 类别再回填门等级。

## 11.2 `not_codable`

若 Phase 0 失败：

```text
sea_evidence_status = not_codable
```

不赋 SEA-0 至 SEA-4。

## 11.3 SEA-0

满足任一：

- 事件与边界可编码，但 DMF < 2；
- 差异只在观察者侧；
- 候选路径并非现实可达；
- 差异没有进入有效通道。

结论：

> 未建立可审计的有效差异过程。

## 11.4 SEA-1

需要：

- DMF ≥ 2；

且出现任一：

- NER < 2；
- PEF < 2；
- `Δ → M` 未通过；
- `M → A` 未通过；
- 只有建议、命令、咨询接口或固定差分响应。

结论：

> 存在有效差异响应或行动接口，但不是完整路径有效过程候选。

## 11.5 SEA-2

最低需要：

- DMF ≥ 2；
- NER ≥ 2；
- PEF ≥ 2；
- `Δ → M` 至少 `qualified_pass`；
- `M → A` 至少 `qualified_pass`；
- 事件、边界和执行窗口相容。

且出现任一：

- CBP < 2；
- HEF < 3；
- `A → X` 未通过；
- `X → H` 未通过；
- `H → future` 未通过；
- 后果或历史证据来自不相容尺度；
- 较大边界的证据无法归属于当前边界。

结论：

> 存在内部登记并改变现实路径，但尚未建立完整后果与历史写回链。

## 11.6 SEA-3

必须同时满足：

- DMF ≥ 2；
- NER ≥ 2；
- PEF ≥ 2；
- CBP ≥ 2；
- HEF ≥ 3；
- 五条链路全部为 `pass` 或 `qualified_pass`；
- 事件起止冻结；
- 边界角色一致；
- 时间尺度相容；
- 最强普通解释已记录；
- 没有跨事件或跨边界补证。

结论必须写成：

> 在边界 B、事件窗口 τ 和匹配基线 K 下，该过程支持有界选择事件候选。

必须保留“有界”和“候选”。

## 11.7 SEA-4

只有在 SEA-3 已成立后才考虑。

还需：

- 至少一个经干预验证的跨门反馈回路；
- 后果或历史写回改变下一轮差异显现、登记或路径组织；
- 较强的活候选、关系性比较、替代路径重分配、位置分配或规则写回证据；
- 反馈不是普通缓存、恢复或固定循环。

不要求五门都达到 4，但必须说明哪些较强结构承担升级。

SEA-4 仍不是主体性、意识、自由、L₂ 或生成健康判定。

## 11.8 无统一等级

若五门分别有较强证据，但来自：

- 不同事件；
- 不同不可对齐边界；
- 不相容时间尺度；
- 不同对象或不同样本；
- 无法连接的论文或数据集；

则输出：

```text
unified_sea_grade: none
reason: fragmented_evidence
```

不得机械降为 SEA-2，也不得拼成 SEA-3。

## 11.9 决定性降级门

每个单位必须指定一个或多个：

- `DMF`；
- `NER`；
- `PEF`；
- `CBP`；
- `HEF`；
- `EVENT_UNITY`；
- `BOUNDARY`；
- `TIMESCALE`；
- `ROLE_ATTRIBUTION`；
- `EVIDENCE_PACKET`。

若有多个，按最早阻断推导链的门排序。

---

# 12. 常见降级触发器

编码者从以下多选，并可补充。

## 12.1 事件触发器

- `POST_HOC_EVENT_EXPANSION`
- `PREHISTORY_MIXED_WITH_EVENT`
- `POSTHISTORY_BACKFILLED`
- `ALTERNATIVES_NOT_REAL`
- `TARGET_TRANSITION_UNCLEAR`

## 12.2 边界触发器

- `BOUNDARY_DRIFT`
- `B3_ATTRIBUTED_TO_B1`
- `EXTERNAL_EXECUTOR_HIDDEN`
- `EXTERNAL_BEARER_ABSORBED`
- `WRITEBACK_OUTSIDE_BOUNDARY`

## 12.3 时间尺度触发器

- `INCOMPATIBLE_TIMESCALES`
- `RECOVERY_WINDOW_NOT_EXCEEDED`
- `CROSS_GENERATION_BACKFILL`
- `INSTANT_SIGNAL_LONG_TERM_OUTCOME_GAP`

## 12.4 NER 触发器

- `OUTPUT_DIFFERENCE_ONLY`
- `FIXED_MAPPING_ONLY`
- `INTERNAL_MEDIUM_NOT_IDENTIFIED`
- `MEDIUM_INTERVENTION_MISSING`
- `RELATION_DEPENDENCE_NOT_SHOWN`

## 12.5 PEF 触发器

- `ADVICE_ONLY`
- `COMMAND_ONLY`
- `ENDPOINT_CONTACT_ONLY`
- `SUCCESS_STRING_ONLY`
- `EXECUTION_REJECTED`
- `TARGET_STATE_UNCHANGED`
- `FIXED_SCRIPT_ONLY`
- `HUMAN_ACTION_UNRESOLVED`

## 12.6 CBP 触发器

- `GENERAL_COST_ONLY`
- `PATH_ATTRIBUTION_MISSING`
- `BEARING_POSITION_UNCLEAR`
- `MAINTENANCE_RELEVANCE_MISSING`
- `BURDEN_EXTERNALIZED`
- `GROUP_OUTCOME_BACKFILLED_TO_EVENT`
- `AFFECT_CONFUSED_WITH_STAKE`

## 12.7 HEF 触发器

- `LOG_ONLY`
- `CACHE_ONLY`
- `PASSIVE_PERSISTENCE_ONLY`
- `FUTURE_INVOCATION_MISSING`
- `CARRIER_INTERVENTION_MISSING`
- `CURRENT_TERMINATION_DOUBLE_COUNTED`
- `PUBLICATION_OR_DOI_NOT_VERIFIED`
- `HISTORY_CORRELATION_ONLY`

## 12.8 结果偏见触发器

- `SUCCESS_EQUALS_HIGH_GRADE`
- `FAILURE_EQUALS_LOW_GRADE`
- `LIFE_EQUALS_AGENCY`
- `COMPLEXITY_EQUALS_SELECTION`
- `HIGH_COST_EQUALS_CBP`
- `PERSISTENCE_EQUALS_HEF`

---

# 13. 编码表

## 13.1 单位元数据

| 字段 | 内容 |
|---|---|
| coder_id |  |
| manual_version |  |
| packet_id |  |
| packet_version |  |
| packet_hash |  |
| coding_started_at |  |
| coding_locked_at |  |
| unit_id |  |
| event_id |  |
| boundary_id |  |
| timescale_id |  |

## 13.2 冻结字段

| 字段 | 内容 |
|---|---|
| event_start |  |
| event_end |  |
| target_transition |  |
| prehistory_excluded |  |
| posthistory_excluded |  |
| alternatives |  |
| boundary_includes |  |
| boundary_excludes |  |
| timescale_summary |  |
| strongest_baseline |  |

## 13.3 变量与角色

| 字段 | 内容 |
|---|---|
| Δ |  |
| M |  |
| A |  |
| X |  |
| H |  |
| authorizer |  |
| executor |  |
| beneficiary |  |
| bearer |  |
| repairer |  |
| writeback_location |  |

## 13.4 门结果

| 门 | 等级 0–4 | evidence_status | confidence | 负载证据 | 关键缺口 |
|---|---:|---|---|---|---|
| DMF |  |  |  |  |  |
| NER |  |  |  |  |  |
| PEF |  |  |  |  |  |
| CBP |  |  |  |  |  |
| HEF |  |  |  |  |  |

## 13.5 链路结果

| 链路 | 状态 | confidence | 证据 | 缺口 |
|---|---|---|---|---|
| Δ → M |  |  |  |  |
| M → A |  |  |  |  |
| A → X |  |  |  |  |
| X → H |  |  |  |  |
| H → future |  |  |  |  |

## 13.6 总体结果

| 字段 | 内容 |
|---|---|
| unified_sea_grade | SEA-0 / SEA-1 / SEA-2 / SEA-3 / SEA-4 / none |
| sea_evidence_status | supported / qualified / upper_bound / unresolved / not_codable |
| decisive_downgrade_gate |  |
| downgrade_triggers |  |
| ordinary_explanation_status |  |
| allowed_statement |  |
| forbidden_attributions |  |
| unresolved_experiments |  |

---

# 14. 机器可读模板

```yaml
coding_record:
  coder_id: ""
  manual_version: "v0_1"
  packet_id: ""
  packet_version: ""
  packet_hash: ""
  coding_started_at: ""
  coding_locked_at: ""

unit:
  unit_id: ""
  event_id: ""
  boundary_id: ""
  timescale_id: ""
  codable: true
  not_codable_reason: null

freeze:
  event_start: ""
  event_end: ""
  target_transition: ""
  prehistory_excluded: []
  posthistory_excluded: []
  candidate_alternatives: []
  boundary_includes: []
  boundary_excludes: []
  timescale_summary: ""
  strongest_baseline: ""

variables:
  delta: ""
  registration_medium: ""
  action_channel: ""
  consequence_location: ""
  history_carrier: ""

roles:
  authorizer: ""
  executor: ""
  beneficiary: ""
  bearer: ""
  repairer: ""
  writeback_location: ""

gates:
  dmf:
    level: null
    evidence_status: ""
    confidence: ""
    evidence: []
    gap: ""
  ner:
    level: null
    evidence_status: ""
    confidence: ""
    evidence: []
    gap: ""
  pef:
    level: null
    evidence_status: ""
    confidence: ""
    evidence: []
    gap: ""
  cbp:
    level: null
    evidence_status: ""
    confidence: ""
    evidence: []
    gap: ""
  hef:
    level: null
    evidence_status: ""
    confidence: ""
    evidence: []
    gap: ""

links:
  delta_to_m:
    status: ""
    confidence: ""
    evidence: []
  m_to_a:
    status: ""
    confidence: ""
    evidence: []
  a_to_x:
    status: ""
    confidence: ""
    evidence: []
  x_to_h:
    status: ""
    confidence: ""
    evidence: []
  h_to_future:
    status: ""
    confidence: ""
    evidence: []

timescale_compatibility:
  delta_to_m: ""
  m_to_a: ""
  a_to_x: ""
  x_to_h: ""
  h_to_future: ""

overall:
  unified_sea_grade: ""
  sea_evidence_status: ""
  sea_category_upper_bound: null
  decisive_downgrade_gate: []
  downgrade_triggers: []
  ordinary_frameworks_considered: []
  ordinary_explanation_status: ""
  sea_added_distinctions: []
  allowed_statement: ""
  forbidden_attributions: []
  unresolved_experiments: []

coder_note:
  strongest_reason_against_own_verdict: ""
  alternative_plausible_verdict: ""
  evidence_that_would_change_verdict: []
```

---

# 15. 强制反方检查

每名编码者在锁定前必须填写三项。

## 15.1 反对自身结论的最强理由

```text
strongest_reason_against_own_verdict
```

不能写“无”。至少指出一个：

- 边界选择争议；
- 干预不足；
- 普通解释；
- 时间尺度问题；
- 代理变量缺口；
- 角色归属问题。

## 15.2 最接近的替代判定

```text
alternative_plausible_verdict
```

例如：

```text
SEA-2 qualified rather than SEA-3 qualified
```

并说明决定差异的具体证据。

## 15.3 什么证据会改变结论

必须列出可执行或可检索的证据，而不是抽象要求。

例如：

- 目标对象前后状态哈希；
- 内部介质消融；
- 后果保护干预；
- 历史载体重置；
- 同细胞代谢联测；
- 正式 production 调用记录；
- 公共 DOI 页面；
- 替代路径资源记录。

---

# 16. 分歧分类与裁决

## 16.1 分歧代码

| 代码 | 含义 |
|---|---|
| D-EVENT | 事件起止或目标迁移不同 |
| D-BOUNDARY | 边界包含／排除不同 |
| D-TIME | 时间尺度兼容性不同 |
| D-ALTERNATIVE | 候选路径现实性不同 |
| D-SOURCE | 对来源强度或事实读取不同 |
| D-DMF | DMF 等级不同 |
| D-NER | NER 等级不同 |
| D-PEF | PEF 等级不同 |
| D-CBP | CBP 等级不同 |
| D-HEF | HEF 等级不同 |
| D-LINK | 链路状态不同 |
| D-ROLE | 授权、执行、承受或写回归属不同 |
| D-BASELINE | 最强普通解释不同 |
| D-DERIVATION | 门等级相同但总体等级推导不同 |
| D-PRIVACY | 对可用证据权限理解不同 |
| D-OTHER | 其他，必须说明 |

## 16.2 裁决顺序

裁决者必须按以下顺序处理：

1. 材料版本是否相同；
2. 事实读取是否相同；
3. 事件是否相同；
4. 边界是否相同；
5. 时间尺度是否相同；
6. 候选路径是否相同；
7. 五门等级；
8. 链路状态；
9. 总体规则推导。

不得一开始讨论“这个案例究竟是不是选择”。

## 16.3 禁止平均裁决

如果 A 给 NER-1，B 给 NER-3，不得取 NER-2。

裁决必须选择：

- A 的理由更符合规则；
- B 的理由更符合规则；
- 证据不足，改为 unresolved；
- 事件或边界需拆分；
- 手册规则歧义，需要版本修订并重新编码。

## 16.4 裁决记录

每个分歧必须保留：

- A 原始编码；
- B 原始编码；
- 分歧代码；
- 裁决结果；
- 裁决依据；
- 是否触发手册修改；
- 是否需要重编码其他单位。

不得覆盖原始文件。

---

# 17. 可靠性指标

## 17.1 主要指标

### 门等级

对 DMF、NER、PEF、CBP、HEF 的 0–4 有序等级计算：

- ordinal weighted Cohen’s kappa；
- exact agreement；
- within-one-level agreement。

### 总体 SEA 类别

对 SEA-0 至 SEA-4 计算：

- ordinal weighted Cohen’s kappa；
- exact agreement。

`none` 和 `not_codable` 单独报告，不强行放入有序序列。

### 决定性降级门

报告：

- exact agreement；
- multi-label overlap；
- 第一决定性失败门 agreement。

### 边界与事件

报告：

- event-start agreement；
- event-end agreement；
- boundary inclusion agreement；
- timescale compatibility agreement；
- `not_codable` agreement。

## 17.2 三名以上编码者

若编码者超过两名或存在缺失编码，可补充：

- ordinal Krippendorff’s alpha；
- nominal alpha for downgrade triggers。

本手册不把某一统计量当作方法有效性的唯一判据。

## 17.3 不能只报告总体平均

必须按门报告。

如果总体 κ 较高，但 CBP 或 HEF 一致性很低，方法仍不能声称可移植，因为最关键的降级门可能不稳定。

---

# 18. v0.1 预注册验收阈值

以下阈值是内部试点规则，不是通用方法学定律。

## 18.1 `GO`：进入扩大可靠性测试

同时满足：

- 五门合并 ordinal weighted κ ≥ 0.70；
- 每个关键门 DMF/NER/PEF/CBP/HEF 的 κ ≥ 0.60；
- 总体 SEA exact agreement ≥ 0.75；
- 第一决定性降级门 agreement ≥ 0.75；
- 边界是否可升级的 agreement ≥ 0.75；
- 时间尺度兼容性 agreement ≥ 0.75；
- 没有系统性把 B3 结果倒投给 B1；
- 没有通过平均或成功标签恢复结果。

达到 GO 只允许：

> 手册进入更大样本或外部编码者测试。

不等于方法论文已完成。

## 18.2 `REVISE`：修改手册后重测

出现任一：

- 五门合并 κ 为 0.50–0.69；
- 任一关键门 κ < 0.60；
- 总体 SEA exact agreement 为 0.60–0.74；
- 分歧主要集中在可定位的单一术语或规则；
- 编码者频繁混淆 `unresolved` 与 `failed`；
- 同一事实在不同边界上的编码格式不一致。

处理：

1. 分类分歧；
2. 修订手册；
3. 增加独立训练包；
4. 冻结新版本；
5. 对受影响测试单位重新盲化编码。

## 18.3 `NO-GO`：停止强方法主张

出现任一：

- 五门合并 κ < 0.50；
- 总体 SEA exact agreement < 0.60；
- 编码者主要依据“成功／失败”而非门规则判定；
- 边界可由编码者任意扩张并总能制造 SEA-3；
- CBP 持续退化为一般成本；
- HEF 持续退化为日志或持久化；
- 大量单位只能靠作者解释才能冻结事件；
- 关键分歧无法通过明确证据或规则解决；
- 正负对照的预期顺序无法由盲化编码恢复。

NO-GO 后可保留：

> 跨域研究设计与反混淆清单。

不得继续声称 SEA 是稳定、可移植的识别方法。

---

# 19. 首轮试点样本设计

## 19.1 单位数量

建议首轮不是按“案例数”，而是按编码单位计数：

```text
18–24 个 event × boundary × timescale 单位
```

至少覆盖：

- AI 软件事务；
- 生命趋化；
- 学术出版制度流程。

## 19.2 盲化 packet 构造

证据包准备者从现有材料制作 opaque packets，但不把既有审计报告提供给编码者。

### AI 家族

可使用：

- 未调用的目标变更；
- 被服务端拒绝的事务；
- 已提交并产生目标状态变化的事务；
- 模型、工具链和完整人机系统边界。

### 生命家族

可使用：

- tethered-cell 时间比较；
- 梯度迁移；
- 适应缺陷条件；
- 代谢型与非代谢型吸引物；
- 单细胞与种群边界；
- 同事件测量与跨研究拼接版本。

### 制度家族

可使用：

- 稿件工件；
- 投稿登记；
- 编辑终止；
- 独立审稿与修订；
- 接受；
- production 调用；
- proof；
- 公共学术记录边界。

## 19.3 必含压力包

至少加入：

1. **边界诱导包**：同一事实分别给 B1/B2/B3；
2. **时间尺度陷阱包**：五门材料来自不相容尺度；
3. **一般成本陷阱包**：有高成本但无路径特异承受；
4. **日志陷阱包**：有永久记录但未被后续调用；
5. **成功标签陷阱包**：任务成功但某门失败；
6. **失败标签陷阱包**：目标路径终止但 PEF/CBP 真实成立；
7. **跨研究拼接包**：每门分别有证据但没有统一事件。

## 19.4 不把现有报告当金标准

既有报告只能作为：

- packet 来源目录；
- 作者首次编码；
- 后续比较对象。

它们不是不可修改的 gold labels。

若独立编码稳定反对既有报告，必须重新审计报告，而不是把独立编码者判为错误。

---

# 20. 隐私与受控材料

## 20.1 私有制度材料

使用邮箱、投稿平台或账单状态时：

- 只提供最小必要状态；
- 删除邮箱地址；
- 删除私有 URL；
- 删除 access token、reference code 和 attachment ID；
- 删除个人财务陈述；
- 删除无关第三方信息；
- 不复制审稿意见全文，除非该意见本身是编码对象且已获许可。

## 20.2 编码者访问范围

编码者必须知道：

- 材料是否公开；
- 是否只可在受控环境读取；
- 是否允许保存本地副本；
- 是否允许引用原文；
- 编码完成后是否必须删除副本。

## 20.3 可靠性不要求公开泄露

内部一致性测试可以使用受控材料，但方法论文若要引用案例事实，需要另行准备：

- 脱敏时间线；
- 可公开状态页；
- DOI 或正式记录；
- 文件哈希；
- 最小摘录；
- 伦理与隐私说明。

---

# 21. 允许与禁止的结论语言

## 21.1 允许

```text
在边界 B、事件窗口 τ 和基线 K 下，编码者将该过程判为 SEA-2 qualified；决定性缺口为 HEF-3 未建立。
```

```text
该证据包支持内部登记和现实路径效力，但 CBP 证据来自不同尺度，因此没有统一 SEA-3 等级。
```

```text
扩大到完整社会技术边界后出现新的执行、承受和写回证据；该升级不能归属于模型边界。
```

## 21.2 禁止

```text
该系统本质上是 SEA-3。
```

```text
SEA-3 证明系统有意识或有真正 stake。
```

```text
因为任务成功，所以是选择事件。
```

```text
因为付出了很多成本，所以 CBP 成立。
```

```text
因为留下永久日志，所以 HEF-3 成立。
```

```text
因为是生命系统，所以自动高于软件系统。
```

```text
因为期刊接受，所以知识已写回公共学术系统。
```

---

# 22. 手册修订治理

## 22.1 何时升级版本

以下变化至少升级 patch 或 minor version：

- 修改门等级定义；
- 修改总体推导规则；
- 新增或删除 evidence_status；
- 修改可靠性阈值；
- 修改编码单位；
- 修改 `unresolved` 与 `failed` 的区分；
- 修改边界或时间尺度规则；
- 修改降级触发器。

## 22.2 不允许静默修订

每个版本必须保留：

- 变更摘要；
- 变更原因；
- 受影响编码单位；
- 是否需要重编码；
- 旧版可靠性统计是否仍有效。

## 22.3 数据与手册分离

手册文件不保存私有证据正文。

编码结果、packet manifest 和裁决记录应分别存放，以避免：

- 修改规则时误改原始编码；
- 公开仓库泄露私有材料；
- 既有结论污染盲化包。

---

# 23. 本手册的验收与下一步

## 23.1 v0.1 完成条件

本文件完成的是：

- 编码单位定义；
- 证据包标准；
- 独立与盲化规则；
- 五门等级压缩；
- 链路编码；
- 总体推导算法；
- 分歧代码；
- 裁决流程；
- 可靠性指标；
- GO / REVISE / NO-GO 阈值；
- 首轮 18–24 单位试点设计；
- 隐私纪律。

## 23.2 尚未完成

本手册本身没有完成：

- 第二名独立编码者招募；
- 脱敏 evidence packets；
- 训练包；
- 正式盲化测试；
- κ 或 alpha 计算；
- 外部复核；
- 近邻理论系统覆盖审计；
- 方法论文正文。

## 23.3 下一步顺序

```text
1. 合并本手册
2. 制作不含预期结论的 packet manifests
3. 制作 2–3 个不计分训练单位
4. 冻结 18–24 个测试单位
5. 两名编码者独立编码
6. 锁定原始结果
7. 计算门级与总体一致性
8. 按 GO / REVISE / NO-GO 决定方法路线
```

在可靠性结果出现前：

- 不继续扩充新案例；
- 不直接写完整投稿正文；
- 不把现有作者判定称为已独立验证；
- 不回写 canonical 或书稿；
- 不声称 SEA 已达到 Level 2 可移植识别方法。

---

# 24. 最终操作结论

> **SEA 案例编码必须以“事件 × 边界 × 时间尺度 × 锁定证据包”为单位，分别记录五门等级、证据充分性和链路状态，再由非补偿规则推导总体类别。独立编码者若不能稳定恢复决定性降级门，方法路线必须修订或停止，而不是通过平均、扩边界或作者解释挽救。**
