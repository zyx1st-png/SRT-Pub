---
id: SRT-SEA-RELIABILITY-PILOT-PACKET-MANIFEST-V0-1-20260805
title: "SEA 可靠性试点证据包清单 v0.1"
title_en: "SEA Reliability Pilot Evidence-Packet Manifest v0.1"
type: reliability_pilot_manifest
status: active
version: v0_1
record_stage: packet_roster_preregistered
layer: meta
epistemic_layer: os
claim_mode: operations_execution
claim_level: audit_only
canonical: false
ai_do_not_use_for_definition: true
created: 2026-08-05
revised: 2026-08-05
provenance: 2026-08-05 作者要求在 SEA 案例编码手册 v0.1 合并后继续。本文件预注册首轮可靠性试点的 21 个正式编码单位、3 个不计分训练单位、证据包构造纪律、盲化、版本锁定、隐私分级和随机呈现规则。它不制作完整证据包，不给出预期 SEA 等级，不把既有作者审计结论当作金标准。
dependency:
  - Operations/SRT_UNIFIED_SELECTION_EVENT_AUDIT_PROTOCOL_2026-08-04.md
  - Operations/SRT_SEA_CASE_CODING_MANUAL_v0_1_2026-08-05.md
  - Operations/SRT_AI_BOUNDARY_CASE_PR720_UNIFIED_SELECTION_AUDIT_2026-08-04.md
  - Operations/SRT_AI_NEGATIVE_CONTROL_DISCONNECTED_WRITE_UNIFIED_AUDIT_2026-08-04.md
  - Operations/SRT_AI_SERVER_REJECTED_WRITE_UNIFIED_AUDIT_2026-08-04.md
  - Operations/SRT_AI_CORRECT_SHA_SUCCESS_CONTROL_UNIFIED_AUDIT_2026-08-05.md
  - Operations/SRT_LIFE_BOUNDARY_CASE_ECOLI_CHEMOTAXIS_UNIFIED_AUDIT_2026-08-05.md
  - Operations/SRT_INSTITUTIONAL_PUBLICATION_PAIRED_UNIFIED_AUDIT_2026-08-05.md
  - Philosophy/Papers/Selection_Event_Audit_Method_Paper_Strategy.md
---

# SEA 可靠性试点证据包清单 v0.1

## 0. 结论先行

本文件把首轮可靠性试点冻结为：

```text
3 个不计分训练单位
+
21 个正式编码单位
=
AI 7 + 生命 7 + 制度 7
```

每个正式编码单位遵循：

```text
U = <event, boundary, timescale, locked packet version>
```

本文件只固定：

- 单位数量与组成；
- 每个单位的事件焦点、边界和时间尺度；
- 证据包必须包含与排除的材料类型；
- 隐私级别；
- 构造、哈希、释放和随机化程序；
- 何时必须重启试点。

本文件不固定：

- 任何单位的预期门等级；
- 任何单位的预期 SEA 类别；
- “正例”“负例”“成功”“失败”标签；
- 决定性降级门；
- 作者既有报告是否正确；
- GO / REVISE / NO-GO 结果。

---

# 1. 文件角色

## 1.1 本文件是什么

这是可靠性试点的公开预注册清单。

其用途是让试点在编码前回答：

1. 哪些单位会进入正式分析；
2. 哪些边界和时间尺度必须分别编码；
3. 哪些材料可以进入 packet；
4. 哪些结论性或诱导性内容必须排除；
5. 如何防止看到编码结果后替换单位；
6. 如何在不公开私有邮箱或投稿平台内容的前提下完成受控编码。

## 1.2 本文件不是什么

它不是：

- 新协议；
- 编码答案；
- 作者结论摘要；
- 既有审计报告的索引版；
- 公开数据集；
- 可直接交给编码者的 packet；
- 方法论文结果部分；
- 对期刊、模型、生物系统或机构的评价。

## 1.3 与编码手册的关系

所有编码规则、门定义、总体推导、分歧处理和 GO / REVISE / NO-GO 阈值均继承：

```text
Operations/SRT_SEA_CASE_CODING_MANUAL_v0_1_2026-08-05.md
```

本清单不得修改其阈值或推导算法。

---

# 2. 试点治理

## 2.1 角色分离

至少设置：

| 角色 | 职责 | 编码阶段限制 |
|---|---|---|
| P：packet 准备者 | 从原始材料制作脱敏 packet | 不参与 A/B 讨论 |
| A：编码者 A | 独立编码全部正式单位 | 不看作者报告与 B 结果 |
| B：编码者 B | 独立编码全部正式单位 | 不看作者报告与 A 结果 |
| J：裁决者 | 双方锁定后处理分歧 | 不得覆盖原始编码 |
| D：数据管理员 | 哈希、版本、随机顺序和统计表 | 不解释案例事实 |

P 与 J 可以是同一人；A 与 B 必须为不同的人。

正式试点中，作者可以担任 P 或 J，但不建议担任唯一的 A 或 B。

## 2.2 编码者访问隔离

正式编码期间，A 与 B 不得：

- 浏览仓库中的既有 SEA 案例审计报告；
-查看 PR 标题、PR 正文或 commit message；
-搜索 packet 原始事件的公开讨论；
-询问作者该单位被设计成什么等级；
-互相讨论边界、门等级或总体判定；
-使用“positive control”“negative control”“success case”等外部标签。

若编码者已经熟悉某一事件，必须在编码表记录：

```text
prior_case_familiarity: none / low / moderate / high
```

熟悉不自动排除，但必须在结果中分层报告。

## 2.3 作者报告不是答案

既有审计报告只用于 P：

- 定位原始来源；
- 识别可用状态记录；
- 发现隐私字段；
- 检查遗漏材料。

它们不得直接进入 coder-facing packet，也不得作为裁决时的最终答案。

若独立编码稳定反对作者报告，应重新审计作者报告。

---

# 3. Packet 生命周期

每个 packet 必须经过以下状态：

```text
planned
→ assembled
→ privacy_reviewed
→ hash_locked
→ released
→ coding_locked
→ adjudicated
```

## 3.1 `planned`

本文件中的 21 个正式单位均处于 `planned`。

## 3.2 `assembled`

P 已制作完整文件夹，但尚可修正事实遗漏、格式或脱敏。

## 3.3 `privacy_reviewed`

确认没有：

- 邮箱地址；
- 私有 URL；
- access token；
- attachment ID；
- reference code；
- 账单编号或个人财务陈述；
- 不必要的第三方身份；
- 未获许可的审稿意见全文。

## 3.4 `hash_locked`

所有文件计算 SHA-256；生成排序后的 `packet_files.sha256`。

Packet 根哈希定义为：

```text
SHA256(concatenate(sorted("<file_sha256>  <relative_path>\n")))
```

锁定后不得修改任何字节。

## 3.5 `released`

A 与 B 收到相同根哈希和相同字节内容，但文件呈现顺序可以由统一随机化规则生成。

## 3.6 `coding_locked`

编码结果带时间戳和文件哈希锁定；不得覆盖原始结果。

## 3.7 `adjudicated`

仅在 A、B 原始编码均锁定后进入。

---

# 4. Packet 目录标准

每个正式 packet 至少包含：

```text
PACKET-XXX/
  README_CODER.md
  packet_metadata.yaml
  evidence/
    E01.*
    E02.*
    ...
  evidence_index.csv
  coding_form.yaml
  packet_files.sha256
```

## 4.1 `README_CODER.md`

只能说明：

- 任务；
- 编码单位；
- 允许访问范围；
- 时间尺度；
- 隐私限制；
- 如何提交编码。

不得包含：

- 预期 SEA 等级；
- 决定性失败门；
- 作者结论；
- “本包测试某陷阱”等提示。

## 4.2 `packet_metadata.yaml`

最低字段：

```yaml
packet_id: ""
packet_version: "v1"
domain_family: "software | life | institution | training"
event_id: ""
boundary_id: ""
timescale_id: ""
cutoff_date: ""
privacy_level: "public | controlled | restricted"
packet_root_hash: ""
source_count: 0
prior_author_audit_available: true
prior_author_audit_included: false
```

## 4.3 `evidence_index.csv`

列：

```text
evidence_id
chronology_position
evidence_type
source_date
public_or_controlled
included_scope
excluded_scope
redaction_applied
file_sha256
```

不得出现 SEA 结论列。

## 4.4 证据顺序

默认按事件时间顺序排列。

若顺序本身会直接暴露未被材料支持的解释，允许使用原始时间戳并随机文件名，但不得改变事实时间。

---

# 5. 盲化与语言清洗

## 5.1 必须删除的结论性语言

从 coder-facing packet 删除或中性替换：

- positive / negative control；
- success / failure control；
- SEA-0 至 SEA-4；
- qualified / supported / strong；
- decisive gap；
- failed gate；
- same-event CBP unresolved；
- historical write-back established；
- 作者对案例的总结句。

## 5.2 不能删除的事实语言

不得为了盲化删除：

- HTTP 状态码；
- 目标对象前后哈希；
- 是否产生 commit 或 ref；
- 是否进入审稿、production 或 proof；
- 实验对象、突变体、干预和测量；
- 时间戳和事件顺序；
- 公开论文的方法与结果；
- 证据未测量某变量这一事实。

盲化不等于隐藏结果。

## 5.3 审计文件名不得进入 packet

Coder-facing packet 不得展示类似：

```text
NEGATIVE_CONTROL
SUCCESS_CONTROL
SEA-3
PAIRED_UNIFIED_AUDIT
```

P 应从原始记录或中性摘录生成 packet，而不是把案例报告直接打包。

---

# 6. 隐私级别

## 6.1 `public`

全部来源可公开访问，可保留 DOI、公开 Git 记录和论文引文。

## 6.2 `controlled`

包含作者私有但低敏状态记录，例如：

- 投稿状态邮件的脱敏摘录；
- 平台状态时间线；
- 私有但不含财务或第三方敏感信息的操作记录。

编码者可在受控环境阅读，不得公开转发。

## 6.3 `restricted`

包含不能进入普通 packet 的材料，例如：

- 未公开审稿意见；
- 付款与财务细节；
- 私有附件；
- 访问凭据；
- 第三方个人信息。

首轮正式试点原则上不使用 `restricted`。若某单位必须依赖 restricted 材料，应将单位标记为 `build_blocked`，不得用摘要替代关键证据。

---

# 7. 三个不计分训练单位

训练单位不进入 κ、agreement 或 GO / REVISE / NO-GO 统计。

它们只测试：

- 编码表是否可执行；
- `unresolved` 与 `failed` 是否能区分；
- 事件与边界是否能冻结；
- 编码者是否会把一般成本、日志或建议误当成完整门证据。

## TR-001 · 设备控制与未使用日志

```text
domain: synthetic engineering
boundary: controller + actuator + room
window: one temperature-control episode plus one later probe
```

材料应包含：

- 传感器读数；
- 控制器规则；
- 执行器动作；
- 房间温度变化；
- 永久日志；
- 后续控制器不读取该日志的说明。

不得给出答案键。

## TR-002 · 委员会建议与授权分离

```text
domain: synthetic institution
boundary: committee + approving officer + implementation unit
window: one recommendation cycle
```

材料应包含：

- 多个候选方案；
- 委员会建议；
- 正式授权状态；
- 实施记录或缺失；
- 后续规则状态。

## TR-003 · 指令、接口和物理执行分离

```text
domain: synthetic automation
boundary: planner + API + actuator + target object
window: one command episode
```

材料应包含：

- 计划输出；
- API 接收状态；
- 执行器连接状态；
- 目标对象前后状态；
- 运行时成本。

## 7.1 训练完成标准

只有当 A、B 均能：

- 独立填写完整表；
- 不询问预期等级；
- 区分事实缺失与门槛失败；
- 解释总体等级如何由门推导；

才可释放正式 packets。

若训练暴露手册规则歧义，必须先发布手册新版本，再开始正式试点。

---

# 8. 正式试点总表

正式样本固定为 21 个单位。

| Packet | 领域 | 事件焦点 | 边界 | 时间尺度 | 隐私 |
|---|---|---|---|---|---|
| RP-001 | software | 变更文本形成至外部调用窗口结束 | 生成组件 | 秒—分钟 | public/controlled |
| RP-002 | software | 同一窗口的编排与连接器活动 | 生成组件＋编排器＋连接器 | 秒—分钟 | controlled |
| RP-003 | software | 带前置条件的写请求与服务端响应 | 工具链＋远端端点 | 秒 | public/controlled |
| RP-004 | software | 同一请求及其授权、执行和目标状态 | 完整人—工具—平台系统 | 秒—分钟 | controlled |
| RP-005 | software | 生成组件对已提交变更的可归属证据 | 生成组件 | 秒—分钟 | controlled |
| RP-006 | software | 写请求、对象创建、提交与 ref 更新 | 工具链＋远端仓库 | 秒—分钟 | public |
| RP-007 | software | 授权、工具执行、仓库状态与后续历史 | 完整人—工具—仓库系统 | 分钟—后续探针 | public/controlled |
| RP-008 | life | 野生型时间比较实验 | 细胞内感知—信号边界 | 约数秒 | public |
| RP-009 | life | 适应相关突变体时间比较实验 | 细胞内感知—信号边界 | 约数秒 | public |
| RP-010 | life | tethered 条件下信号与马达输出 | 单细胞信号—马达边界 | 秒 | public |
| RP-011 | life | 野生型梯度迁移 | 单细胞—环境闭环 | 分钟 | public |
| RP-012 | life | 受体甲基化相关缺陷与梯度迁移 | 单细胞—环境闭环 | 分钟 | public |
| RP-013 | life | CheY-P 与马达切换的直接测量 | 信号—马达执行边界 | 毫秒—秒 | public |
| RP-014 | life | 信号、迁移、代谢／适合度材料的组合包 | 细胞—种群复合边界 | 秒—代际 | public |
| RP-015 | institution | 私有稿件工件形成 | 稿件工件边界 | 天—周 | controlled |
| RP-016 | institution | 投稿登记与稿号生成 | 作者＋投稿平台 | 分钟—小时 | controlled |
| RP-017 | institution | 已登记稿件的编辑终止 | 作者＋平台＋编辑流程 | 天 | controlled |
| RP-018 | institution | 投稿与初始验证 | 作者＋平台＋编辑流程 | 小时—天 | controlled |
| RP-019 | institution | 独立审稿、互动审查与修订 | 作者＋编辑＋审稿人 | 周—月 | controlled |
| RP-020 | institution | 最终审查与接受决定 | 作者＋编辑＋审稿人 | 天—周 | controlled |
| RP-021 | institution | 接受后 production 与 proof | 作者＋编辑＋生产系统 | 天—周 | controlled |

表中顺序不是 coder-facing 呈现顺序。

---

# 9. Software 家族 packet 规格

## RP-001

### 冻结单位

```text
event: 目标变更文本形成后，到该回合外部调用窗口关闭
boundary: 仅生成组件
```

### 必含证据

- 输入任务或约束；
- 生成的变更内容或行动表示；
- 生成组件可访问的内部／外部接口说明；
- 该窗口内是否存在可核验工具调用记录。

### 必排除

- 作者审计结论；
- 较大边界中的人类授权；
- 后续仓库状态作为生成组件内部状态；
- PR 标题中的 control 标签。

## RP-002

### 冻结单位

```text
event: 同一变更请求的编排与连接器窗口
boundary: 生成组件 + 编排器 + 连接器
```

### 必含证据

- 编排器是否构造调用；
- 连接器是否收到调用；
- 端点接触记录；
- 目标对象前后状态；
- 失败或无调用时的运行记录。

### 必排除

- 人类授权被归为模型内部授权；
- 目标系统之外的一般会话日志作为目标写回。

## RP-003

### 冻结单位

```text
event: 一个带对象版本前置条件的写请求，从发送到服务端响应
boundary: 工具链 + 远端写端点
```

### 必含证据

- 请求方法；
- 前置条件字段；
- 服务端响应码；
- 目标文件／对象前后哈希；
- 是否创建 blob、commit 或 ref。

### 必排除

- “错误”“拒绝”“阴性”结论词；
- 仅凭耗时或 API 调用成本推断后果承担。

## RP-004

### 冻结单位

```text
event: RP-003 同一请求及其人类授权、工具执行与目标状态
boundary: 完整人—工具—平台系统
```

### 必含证据

- 授权者；
- 执行器；
- 平台权限；
- 请求与响应；
- 目标状态；
- 必要时的恢复或重新尝试记录。

### 必排除

- 把系统级授权归给生成组件；
- 把平台错误本身写成历史写回。

## RP-005

### 冻结单位

```text
event: 一次最终产生仓库变更的生成与调用序列
boundary: 仅生成组件
```

### 必含证据

- 生成内容；
- 调用参数中由生成组件提供的部分；
- 是否能干预或定位生成组件内部登记；
- 外部提交结果。

### 必排除

- 工具、仓库和人类状态自动算作模型内部状态；
- 完整系统结果直接升级模型边界。

## RP-006

### 冻结单位

```text
event: 写请求发送至目标分支 ref 指向新 commit
boundary: 编排器 + 连接器 + GitHub 写端点 + 目标仓库
```

### 必含证据

- 正确对象版本前置条件；
- 新内容；
- blob SHA；
- commit SHA；
- branch head 前后值；
- fetch-back 内容验证；
- 后续查询是否读取新历史。

### 必排除

- 人类授权被删除；
- Git 事务机制被描述成 SRT 特有机制。

## RP-007

### 冻结单位

```text
event: 从人类授权到提交后历史探针
boundary: 人类授权者 + 生成组件 + 编排器 + 连接器 + 平台 + 仓库
```

### 必含证据

- 角色表；
- 授权记录；
- 请求和提交记录；
- 目标状态；
- 恢复／撤销成本；
- 后续历史读取或分支基线使用。

### 必排除

- 责任、自由或主体性结论；
- 把仓库持久化称为模型自我连续性。

---

# 10. Life 家族 packet 规格

## RP-008

### 冻结单位

```text
event: 野生型细胞在时间变化刺激下的单次比较响应
boundary: 受体—信号通路
window: 约数秒
```

### 必含证据

- 刺激时间序列；
- 野生型条件；
- 旋转或信号响应；
- 实验装置；
- 作者对时间比较窗口的结果。

### 必排除

- 后续种群适合度；
- 未在同一实验测量的代谢收益；
- SRT 案例报告结论。

## RP-009

### 冻结单位

```text
event: 适应相关突变体在同类时间变化刺激下的响应
boundary: 受体—信号通路
window: 约数秒
```

### 必含证据

- 突变体基因型；
- 与野生型可比的刺激与测量；
- 响应差异；
- 适应或甲基化相关解释。

### 必排除

- 把基因型缺陷自动解释为某个 SEA 门失败；
- 种群长期结果。

## RP-010

### 冻结单位

```text
event: tethered-cell 条件下信号变化至马达旋转输出
boundary: 单细胞信号—马达
window: 秒
```

### 必含证据

- tethering 条件；
- 刺激；
- 马达输出；
- 空间迁移是否可能；
- 装置对运动路径的限制。

### 必排除

- 用未发生的空间路径补足后果；
- 把实验者固定装置的成本算作细胞后果。

## RP-011

### 冻结单位

```text
event: 野生型细胞进入温和吸引物梯度后的迁移
boundary: 单细胞—局部环境闭环
window: 分钟
```

### 必含证据

- 梯度条件；
- 初始分布；
- 迁移或再分布结果；
- 运动机制；
- 是否同时测量资源、维持或未来行动能力。

### 必排除

- 跨论文代谢收益；
- 种群扩张倒投单细胞事件。

## RP-012

### 冻结单位

```text
event: 受体甲基化相关缺陷条件下的梯度迁移
boundary: 单细胞—局部环境闭环
window: 分钟
```

### 必含证据

- 突变或甲基化缺陷；
- 梯度；
- 迁移／再分布；
- 与对照比较；
- 已测与未测变量。

### 必排除

- 用“适应必需”直接代替五门编码；
- 未测量的 CBP 变量。

## RP-013

### 冻结单位

```text
event: CheY-P 结合／解离至马达切换
boundary: 信号—马达执行
window: 毫秒—秒
```

### 必含证据

- 直接成像或测量方法；
- CheY-P 动态；
- 马达切换；
- 时间关系；
- 干预或相关性边界。

### 必排除

- 空间迁移和营养后果未测时不得自动加入；
- 细胞长期历史不得由瞬时成像推断。

## RP-014

### 冻结单位

```text
event: 多研究材料形成的信号—运动—迁移—适合度组合
boundary: 细胞—种群复合边界
window: 秒至代际
```

### 必含证据

- 至少一个信号研究；
- 至少一个马达或轨迹研究；
- 至少一个迁移研究；
- 至少一个资源或适合度研究；
- 每项研究的对象、样本、边界和时间尺度；
- 明确的跨研究来源表。

### 必排除

- 任何预先写好的“fragmented evidence”结论；
- 把不同样本自动连接成同一事件；
- 删除研究间不相容信息。

---

# 11. Institution 家族 packet 规格

## RP-015

### 冻结单位

```text
event: 稿件工件形成至首次制度投稿之前
boundary: 稿件工件
window: 天—周
```

### 必含证据

- 稿件存在的最小证明；
- 版本或附件存在；
- 尚未进入目标期刊状态机的时间界线；
- 工件内容与制度状态的区分。

### 必排除

- 后续稿号；
- 后续编辑决定；
- 作者审计判定。

## RP-016

### 冻结单位

```text
event: 一篇稿件进入投稿系统并获得稳定稿号
boundary: 作者 + 投稿平台
window: 分钟—小时
```

### 必含证据

- 收稿时间；
- 稿号；
- 稿件标题和作者身份的脱敏一致性；
- 投稿条件和状态；
- 可用的排他投稿或流程义务。

### 必排除

- 后续拒稿；
- 后续改稿或另投；
- 邮箱地址和私有链接。

## RP-017

### 冻结单位

```text
event: 已登记稿件进入编辑处理至终止通知
boundary: 作者 + 平台 + 编辑流程
window: 数天
```

### 必含证据

- 与 RP-016 相同稿号的连续性；
- 编辑终止状态；
- 是否进入同行评审、修订或 production；
- 当前路径关闭后的直接义务或重新路由要求；
- 截止日期内是否存在后续制度调用。

### 必排除

- 情绪描述作为唯一后果；
- 把终止事实同时重复用于当前路径与未来写回；
- 期刊质量或公平性判断。

## RP-018

### 冻结单位

```text
event: 另一篇稿件投稿登记至初始验证结果
boundary: 作者 + 平台 + 编辑流程
window: 小时—天
```

### 必含证据

- 稳定稿号；
- 投稿确认；
- 初始验证；
- 后续可能路径；
- 参与角色。

### 必排除

- 独立审稿、接受和 proof；
- 费用信息。

## RP-019

### 冻结单位

```text
event: 进入独立审稿至修订／互动审查阶段结束
boundary: 作者 + 编辑 + 审稿人
window: 周—月
```

### 必含证据

- independent review 状态；
- 至少两条审稿报告状态或等价记录；
- interactive review；
- revision 请求与提交；
- final review 之前的截止边界。

### 必排除

- 审稿意见全文；
- 接受结果；
- 账单与 fee-support 信息。

## RP-020

### 冻结单位

```text
event: review finalised 至正式接受决定
boundary: 作者 + 编辑 + 审稿人
window: 天—周
```

### 必含证据

- final review 状态；
- 编辑角色；
- 接受通知；
- 接受当时可见的下一阶段说明；
- 截止在决定发生的事件终点。

### 必排除

- proof 生成作为事件内部事实；
- DOI、索引或引用；
- 接受等于公开出版的措辞。

## RP-021

### 冻结单位

```text
event: 已接受状态进入 production 至 proof 生成
boundary: 作者 + 编辑 + 生产系统
window: 天—周
```

### 必含证据

- 与 RP-020 相同稿号；
- production handoff；
- proof ready；
- 校对期限和完成条件；
- 必要的生产义务；
- 截止 2026-08-05 可核验的公开记录状态。

### 必排除

- 账单金额、编号和付款细节；
- fee-support 个人陈述；
- 未核验的 DOI、索引或引用；
- public scholarly-record 边界自动并入生产边界。

---

# 12. Packet 构造的完整性检查

P 对每个 packet 必须回答：

1. 是否保留了事件前状态？
2. 是否保留了目标状态？
3. 是否保留了关键失败或缺失记录？
4. 是否保留了边界外执行者和授权者？
5. 是否列出所有时间尺度？
6. 是否列出未测量变量？
7. 是否包含足以反对 P 自己初始看法的材料？
8. 是否删除了作者结论而没有删除事实？
9. 是否存在因隐私而无法提供的承重证据？
10. 编码者能否只凭 packet 判断 `not_codable`，而不是被迫猜测？

任一问题不能回答，packet 不得进入 `hash_locked`。

---

# 13. 一致性与平衡检查

## 13.1 领域平衡

正式单位固定：

```text
software = 7
life = 7
institution = 7
```

不得因某领域更容易制作而替换其他领域单位。

## 13.2 边界平衡

至少包括：

- 组件级边界；
- 工具／执行链边界；
- 完整社会技术或生态边界；
- 同一事实在两个以上边界的重复编码。

## 13.3 时间尺度压力

至少包括：

- 秒级；
- 分钟级；
- 周／月级；
- 一个跨不相容尺度组合包。

## 13.4 结论标签平衡不得预注册

本文件不根据作者预期等级做配额。

原因：

> 以预期 SEA 等级平衡样本会把作者答案写进抽样设计。

结果出现后可以描述等级分布，但不得在编码前替换单位来制造均匀分布。

---

# 14. 呈现顺序随机化

## 14.1 固定种子

在本 manifest 合并后，使用其 **merge commit SHA** 作为种子字符串：

```text
seed = "SEA-RP-v0.1|<manifest_merge_commit_sha>"
```

## 14.2 排序方法

对每个 `RP-001` 至 `RP-021` 计算：

```text
SHA256(seed + "|" + packet_id)
```

按十六进制升序排列，生成 coder-facing 顺序。

A 与 B 使用相同顺序，以避免顺序成为额外变量。

若未来研究顺序效应，应另行预注册不同随机序列。

## 14.3 不允许手工调序

不得：

- 把“简单包”放前面；
- 把预期等级相近的包分开；
- 把某领域集中或打散；
- 根据训练表现重新排列。

---

# 15. 构造与释放日志

packet 构建完成后，另建：

```text
Operations/SEA_Reliability_Pilot_v0_1/PACKET_BUILD_LEDGER_v0_1.md
```

该 ledger 至少记录：

| 字段 | 内容 |
|---|---|
| packet_id |  |
| assembled_at |  |
| preparer |  |
| privacy_reviewer |  |
| source_count |  |
| packet_root_hash |  |
| privacy_level |  |
| status |  |
| build_gap |  |
| released_at |  |

不得在 ledger 中写预期 SEA 等级。

---

# 16. 何时必须重启试点

出现任一情况，正式试点必须停止并重新版本化：

1. hash_locked 后修改 packet 字节；
2. 添加或删除正式单位；
3. 改变事件起止；
4. 改变边界定义；
5. 改变时间尺度；
6. 编码者看到作者审计结论；
7. A 与 B 在锁定前讨论案例；
8. 关键隐私泄露；
9. 发现 packet 漏掉明显反证材料；
10. 编码手册在正式编码中途升级；
11. 用作者解释补充某一编码者但未补充另一编码者；
12. 单位只能靠未记录的口头背景编码。

重启后使用：

```text
manifest v0.2
packet version v2
new hashes
new coding files
```

旧结果保留为 pilot failure record，不得删除。

---

# 17. 不构成重启的情况

以下事项可记录但不自动重启：

- 编码者选择 `not_codable`；
- 编码者对同一事实产生不同解释；
- 某领域单位全部落在相近等级；
- 结果不符合作者预期；
- κ 较低；
- 作者审计被多数编码者反对；
- 普通理论被认为完全充分。

这些都是试点结果，不是修改样本的理由。

---

# 18. 统计计划继承

本 manifest 不新增统计阈值。

正式分析继承编码手册：

- gate-level ordinal weighted Cohen’s kappa；
- exact agreement；
- within-one-level agreement；
- overall SEA exact agreement；
- first decisive downgrade gate agreement；
- boundary agreement；
- timescale compatibility agreement；
- `none` 与 `not_codable` 单独报告；
- 置信区间与单位级分歧表。

21 个单位是内部试点，不足以支持强泛化结论。

---

# 19. 试点完成前禁止事项

在正式可靠性结果出现前，不得：

- 再增加新的 SEA 案例以改善分布；
- 直接写完整方法论文结果；
- 把作者报告称为独立验证；
- 声称 SEA 已是可移植识别方法；
- 回写 canonical 或书稿；
- 将 SEA 等级解释为主体性、意识、自由、责任、stake、L₂ 或生成健康；
- 把 Git、生化或出版流程写成 SRT 特有机制。

---

# 20. 下一步执行顺序

本 manifest 合并后，严格按以下顺序：

```text
1. 制作 TR-001 至 TR-003
2. 完成训练并记录手册歧义
3. 若需修订，先冻结 Coding Manual v0.2
4. 制作 RP-001 至 RP-021
5. 完成隐私审查
6. 生成逐文件 SHA-256 与 packet 根哈希
7. 创建 PACKET_BUILD_LEDGER
8. 由 merge commit SHA 生成固定呈现顺序
9. 同时向 A、B 释放相同 packets
10. 锁定 A、B 原始编码
11. 计算可靠性指标
12. 按 GO / REVISE / NO-GO 处理
```

---

# 21. 当前未完成事项

本文件没有完成：

- 训练 packet 的实际字节内容；
- 21 个正式 packet 的实际字节内容；
- packet 根哈希；
- 第二名和第三名编码者安排；
- 受控阅读环境；
- 正式编码；
- 可靠性统计；
- 裁决；
- 方法论文正文。

因此当前状态只能写作：

> 首轮可靠性试点的样本结构和构造纪律已预注册，证据包尚未制作和释放。

---

# 22. 最终操作结论

> **首轮 SEA 可靠性试点固定为 21 个 `事件 × 边界 × 时间尺度` 正式单位和 3 个不计分训练单位。所有 coder-facing packet 必须删除作者结论与控制标签，保留完整事实、角色、时间戳和缺失证据；hash lock 后不得修改。任何单位的预期等级、决定性失败门或作者判定都不进入本 manifest。**
