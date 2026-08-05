---
id: SRT-AI-CORRECT-SHA-SUCCESS-CONTROL-UNIFIED-AUDIT-20260805
type: operational_audit_report
tags: [AI, PositiveControl, PairedControl, UnifiedAudit, SelectionEvent, CG0, NER, PEF, CBP, HEF, GitHub, OptimisticConcurrency, TransactionCommit]
status: active
record_stage: paired_positive_control_audit
layer: meta
epistem_layer: os
claim_mode: operations_execution
claim_level: audit_only
canonical: false
ai_do_not_use_for_definition: true
created: 2026-08-05
revised: 2026-08-05
provenance: 2026-08-05 作者在未调用 mutation 与错误 blob SHA 被 409 拒绝两项阴性对照之后，选择执行严格配对的正确 SHA 成功对照。实验从 409 案例冻结的同一前态创建独立分支，复用同一目标文件、拟写入内容、update_file 接口和 commit message，仅把请求中的错误 blob SHA 替换为当前正确 blob SHA。
dependency: [Operations/SRT_UNIFIED_SELECTION_EVENT_AUDIT_PROTOCOL_2026-08-04.md, Operations/SRT_AI_BOUNDARY_CASE_PR720_UNIFIED_SELECTION_AUDIT_2026-08-04.md, Operations/SRT_AI_NEGATIVE_CONTROL_DISCONNECTED_WRITE_UNIFIED_AUDIT_2026-08-04.md, Operations/SRT_AI_SERVER_REJECTED_WRITE_UNIFIED_AUDIT_2026-08-04.md, Operations/SRT_PATH_EFFICACY_OPERATIONAL_TEST_2026-08-04.md, Operations/SRT_CONSEQUENCE_BEARING_POSITION_OPERATIONAL_TEST_2026-08-04.md, Operations/SRT_HISTORICAL_EFFICACY_OPERATIONAL_TEST_2026-08-04.md]
---

# 第三轮 AI 对照：正确 blob SHA 的严格配对成功事务

## 0. 结论先行

本报告记录与 409 服务端拒绝实验尽量接近单变量配对的成功对照：

> 从 409 实验的精确冻结前态 `4d55a54df128ee7dd3ae62bb2d7ef64d851f4173` 创建新的隔离分支，复用同一目标文件、同一基线 blob、同一拟写入内容、同一 `update_file` 接口和同一 commit message。唯一目标前置条件变化是：把全零错误 blob SHA 替换为当前正确 blob SHA `55a40db4f0d03dc04abdac8f942798ab4884929c`。

GitHub 接受请求并返回：

```text
new commit:
a9337de07886a5975c9245fd66253f95595d3042

new content blob:
e25dbf9003d0bd1ce9c3fd61d33e758045b44a78
```

事件后验证显示：

- 目标文件内容变为拟提交内容；
- blob 从 `55a40d...` 变为 `e25dbf...`；
- 分支 head 从 `4d55a5...` 变为 `a9337d...`；
- 分支相对冻结前态 `ahead_by: 1`；
- 产生一个真实 commit；
- 文件 diff 为 `+2 / -1`；
- 返回基线需要新的 commit、ref 操作或分支重置。

统一审计结论：

| 边界 | 判定 | 核心理由 |
|---|---|---|
| B₁：模型本身 | **SEA-1** | 模型生成请求，但真实文件、commit 与分支历史位于模型边界外；模型内部 NER 未被实验建立 |
| B₂：模型 + 编排器 + connector + GitHub contents 端点 | **SEA-2** | 请求通过真实执行通道提交并改变外部目标路径，但主要承受位置和持久历史位于目标分支边界外 |
| B₃：用户 + LLM + 编排器 + connector + GitHub + 隔离分支 | **SEA-3 qualified** | 差异、关系校验、事务提交、分支特异后果和 commit 写回在同一冻结社会技术事件中闭合；强内部介质干预和跨情境闭环尚未完成 |

最重要的配对结果是：

```text
错误 blob SHA
→ 409 Conflict
→ 内容、blob、commit、branch head 均不变
→ 目标事件 SEA-1

正确 blob SHA
→ 请求被接受
→ 新内容、新 blob、新 commit、新 branch head
→ 完整人机—仓库边界 SEA-3 qualified
```

这支持以下审计纪律：

> 请求是否到达端点不是 PEF-2 的分界；目标事务是否实际提交并改变预注册路径变量，才是本案例从 PEF-1 升级到 PEF-2 的分界。

本实验没有证明 SRT 发现了 Git、REST、optimistic concurrency 或 compare-and-swap 之外的新机制。

---

## 1. 审计目的

前两项阴性对照已建立：

1. mutation 未调用时，行动计划不能替代路径效力；
2. mutation 已调用但因错误 SHA 被 409 拒绝时，端点接触不能替代目标事务提交。

仍缺少一个尽量严格匹配的成功对照：

> 当其他目标字段保持不变，只把错误 blob SHA 替换为当前正确 blob SHA 时，统一协议是否能根据外部状态证据稳定升级 PEF、CBP、HEF 和完整边界 SEA，而不把该升级反投给模型本身？

### 1.1 预注册预期

| 门 | 预期 |
|---|---|
| CG-0 / DMF | 拟写入内容差异进入真实写通道 |
| CG-1 / NER | GitHub 对“请求 SHA 与当前 blob 的关系”作非等价登记；模型内部 NER 仍未建立 |
| CG-2 / PEF | 达到 PEF-2：目标文件和分支路径真实改变 |
| CG-3 / CBP | 完整边界达到 CBP-2：目标分支承担路径特异状态变化和恢复成本 |
| CG-4 / HEF | 达到 HEF-3：新 commit 与 branch head 改变未来分支基线和返回成本 |
| SEA | B₁ SEA-1；B₂ SEA-2；B₃ SEA-3 qualified |

### 1.2 成功判据

实验在以下条件同时成立时才算成功：

```text
request accepted
AND target content changed
AND target blob changed
AND branch head changed
AND exactly one new commit exists relative to frozen prestate
AND intended marker exists
```

### 1.3 降级条件

出现任一情况必须降级或重分类：

- connector 返回 success，但文件内容不变；
- content blob 不变；
- branch head 不变；
- 没有新 commit；
- 分支出现多个无法归因的并行 commit；
- 拟写入标记不存在；
- 请求实际使用的不是冻结正确 SHA；
- 实验分支不是从 409 冻结前态创建；
- 事件后报告 commit 被倒灌为目标事务的 HEF 证据。

---

## 2. 严格配对设计

### 2.1 409 阴性事件冻结前态

原 409 实验的正式前态为：

```text
branch head:
4d55a54df128ee7dd3ae62bb2d7ef64d851f4173

target blob:
55a40db4f0d03dc04abdac8f942798ab4884929c

target state:
baseline_only
```

原实验分支在本轮开始前仍与该 commit 完全一致：

```text
base: 4d55a54...
head: experiment/ai-rejected-write-negative-control-20260804
status: identical
ahead_by: 0
behind_by: 0
```

因此可以从同一 commit 派生独立成功分支，而不复用已经执行过请求的分支 ref。

### 2.2 新成功实验分支

```text
experiment/ai-correct-sha-success-control-20260805
```

创建基线：

```text
4d55a54df128ee7dd3ae62bb2d7ef64d851f4173
```

该分支创建后与 409 正式事件起点拥有相同 tree、目标文件内容和目标 blob。

### 2.3 同一目标文件

```text
Operations/SRT_AI_REJECTED_WRITE_CONTROL_TARGET_20260804.txt
```

文件名保留 `REJECTED_WRITE`，因为本轮复用原夹具，不为成功结果重新命名目标。

### 2.4 同一基线内容

```text
SRT AI rejected-write negative control target
baseline_marker: REJECTED_WRITE_BASELINE_20260804
state: baseline_only
```

### 2.5 同一拟写入内容

```text
SRT AI rejected-write negative control target
baseline_marker: REJECTED_WRITE_BASELINE_20260804
forbidden_post_marker: REJECTED_WRITE_SHOULD_NOT_COMMIT_20260804
state: mutation_committed
```

`forbidden_post_marker` 的名称来自原阴性实验。它在成功对照中被故意保留，以确保拟写入 payload 不因结果预期而改变。此处“forbidden”只是冻结测试字符串，不是本轮禁止写入的规则。

### 2.6 同一接口

```text
GitHub contents API wrapper: update_file
```

### 2.7 同一 commit message

```text
test: this rejected mutation must not commit
```

该 message 在成功事件中语义上不自然，但故意保持不变，以免把 message 修改引入配对差异。它只描述原夹具来源，不改变事务有效性。

### 2.8 唯一目标前置条件变化

409 阴性请求：

```text
sha = 0000000000000000000000000000000000000000
```

成功请求：

```text
sha = 55a40db4f0d03dc04abdac8f942798ab4884929c
```

除独立分支名称和事件日期外，被测事务字段保持相同。分支名称变化用于隔离事件，不是目标路径成功判据。

---

## 3. 被测事件

### 3.1 事件 ID

```text
AI-GH-PC-CORRECT-SHA-SUCCESS-20260805
```

### 3.2 事件窗口起点

```text
branch_head_t0 = 4d55a54df128ee7dd3ae62bb2d7ef64d851f4173
blob_t0 = 55a40db4f0d03dc04abdac8f942798ab4884929c
state_t0 = baseline_only
```

### 3.3 用户授权

作者在 A／B／C 下一步选择中明确选择：

```text
A
```

该授权支持执行“正确 SHA 成功对照”，不等于授权把实验分支合并到 `main`，也不构成模型自身授权。

### 3.4 实际调用

```text
operation: update_file
repository: zyx1st-png/SRT-Pub
branch: experiment/ai-correct-sha-success-control-20260805
path: Operations/SRT_AI_REJECTED_WRITE_CONTROL_TARGET_20260804.txt
sha: 55a40db4f0d03dc04abdac8f942798ab4884929c
message: test: this rejected mutation must not commit
```

### 3.5 工具返回

```text
commit_sha:
a9337de07886a5975c9245fd66253f95595d3042

content_sha:
e25dbf9003d0bd1ce9c3fd61d33e758045b44a78
```

允许的最强事实表述是：

> GitHub contents 更新事务接受了与当前目标 blob 匹配的 SHA，创建了新内容对象和新 commit，并把实验分支 ref 推进到该 commit。

不允许表述：

- 模型自身写入了 Git 对象数据库；
- 模型自身持有 GitHub 权限；
- commit 是模型记忆或主体连续性；
- 正确 SHA 证明模型理解了 optimistic concurrency；
- 成功事务证明模型具有 stake。

---

## 4. 事件后独立验证

### 4.1 文件内容

事件后读取返回：

```text
SRT AI rejected-write negative control target
baseline_marker: REJECTED_WRITE_BASELINE_20260804
forbidden_post_marker: REJECTED_WRITE_SHOULD_NOT_COMMIT_20260804
state: mutation_committed
```

目标标记存在，状态从：

```text
baseline_only
```

变为：

```text
mutation_committed
```

### 4.2 blob 身份

```text
blob_t0 = 55a40db4f0d03dc04abdac8f942798ab4884929c
blob_t1 = e25dbf9003d0bd1ce9c3fd61d33e758045b44a78
```

因此：

```text
blob_t0 != blob_t1
```

### 4.3 分支 head

```text
branch_head_t0 = 4d55a54df128ee7dd3ae62bb2d7ef64d851f4173
branch_head_t1 = a9337de07886a5975c9245fd66253f95595d3042
```

因此：

```text
branch_head_t0 != branch_head_t1
```

### 4.4 commit 差分

比较：

```text
base = 4d55a54df128ee7dd3ae62bb2d7ef64d851f4173
head = experiment/ai-correct-sha-success-control-20260805
```

返回：

```text
status: ahead
ahead_by: 1
behind_by: 0
total_commits: 1
```

唯一变化文件：

```text
Operations/SRT_AI_REJECTED_WRITE_CONTROL_TARGET_20260804.txt
additions: 2
deletions: 1
changes: 3
```

### 4.5 成功判据核对

| 成功条件 | 结果 |
|---|---|
| 请求被接受 | 是 |
| 内容改变 | 是 |
| blob 改变 | 是 |
| branch head 改变 | 是 |
| 恰好一个新 commit | 是 |
| 拟写入标记存在 | 是 |

结论：

```text
paired_success_control = passed
```

---

## 5. 边界与角色台账

### 5.1 B₁：模型本身

包含：

- 当前对话输入处理；
- 配对方案生成；
- GitHub 请求参数生成；
- 工具调用请求输出。

排除：

- 用户作为授权者；
- 编排器与 connector；
- GitHub 服务；
- 目标文件、blob、commit 和 branch ref；
- 持久仓库历史。

### 5.2 B₂：AI 工具运行时与写端点

包含：

- 模型；
- 会话编排与授权路由；
- connector；
- `update_file` 包装层；
- GitHub contents 写端点及返回。

排除：

- 用户作为最终授权位置；
- 目标分支作为持续环境对象；
- 未来维护者与清理责任。

### 5.3 B₃：完整人机—GitHub 实验系统

包含：

- 用户／理论作者；
- LLM；
- 会话编排；
- connector；
- GitHub contents 服务；
- 隔离分支；
- 目标文件、blob、commit 和 branch ref；
- 本事件的验证与恢复通道。

排除：

- GitHub 公司整体；
- 互联网基础设施；
- `main` 分支；
- 后续报告 PR；
- 更广学术共同体。

### 5.4 角色分离

| 角色 | 位置 |
|---|---|
| 实验方向选择者 | 用户／理论作者 |
| 请求内容生成者 | LLM |
| 调用编排者 | 会话与工具运行层 |
| API 转换与传输 | GitHub connector |
| 前置条件校验与事务提交 | GitHub contents 服务 |
| 目标状态承载 | 隔离分支、目标文件、blob 与 branch ref |
| 直接研究受益者 | 用户与 SRT 项目 |
| 清理／恢复责任 | 用户／仓库维护者 |
| 历史写回位置 | commit `a9337de...` 与实验分支 ref |

角色护栏：

- 用户的 A 选择不能归给模型；
- connector 的写权限不能归给模型；
- GitHub 的 equality／blob 校验不能归为模型内部 NER；
- 目标分支的恢复成本不能说成模型自身 stake；
- commit 不能说成模型参数更新或持久自我。

---

## 6. 五门审计

## 6.1 CG-0 / DMF

目标差异包括：

- 基线内容与拟写入内容；
- 错误请求 SHA 与正确请求 SHA；
- 保持基线与提交新状态两条现实路径。

B₁：

```text
DMF-1; DMF-2 qualified
```

输入和任务差异进入模型接口，但模型内部候选准入未直接干预。

B₂：

```text
DMF-2 supported
```

正确 SHA 与 payload 进入真实写通道，改变可执行事务路径。

B₃：

```text
DMF-3 supported
```

“保持 baseline”与“提交 mutation”是两个真实可达仓库路径；409 阴性对照和本成功对照分别实现了两侧结果。

## 6.2 CG-1 / NER

### B₁

```text
NER-1 only
```

不同任务状态导致不同请求输出，但没有对模型内部权重、阈值、资源或记忆介质做定向干预。

### B₂

```text
NER-2 qualified; relational compare evidence
```

可定位介质与关系包括：

- GitHub 保存的当前目标 blob identity；
- 请求携带的 expected blob SHA；
- contents 服务中的匹配校验状态；
- 编排层选择并传递的 SHA 字段。

配对结果显示：

```text
request_sha != current_blob → 409
request_sha == current_blob → commit
```

为什么仍是 qualified：

- 未直接干预 GitHub 内部校验阈值或算法；
- connector 不暴露内部服务日志；
- 对当前 blob 的改变没有在同一轮中作为独立 mediator intervention；
- 固定 equality gate 仍可由普通 compare-and-swap 完整解释。

### B₃

```text
NER-2 qualified; NER-3 relation candidate
```

完整边界中，用户对 A/B/C 路径作非等价授权，实验协议把 A 路由为正确 SHA 成功对照，GitHub 响应依赖“请求 SHA—当前 blob”关系，而不是单独依赖任一字符串。

该证据属于完整人机—仓库关系，不能反投为模型自身 NER-2/3。

## 6.3 CG-2 / PEF

### B₁

```text
PEF-1
```

模型只能生成工具调用请求，不能在模型边界内改变 GitHub 文件和 ref。

### B₂

```text
PEF-2 supported
```

证据：

- 请求到达真实写端点；
- 端点接受正确前置条件；
- 内容、blob 和 branch head 真实改变；
- 外部读取与 compare 结果独立验证改变；
- 不是只依赖 success 字符串。

### B₃

```text
PEF-3 qualified
```

提交路径获得实现；保持 `baseline_only` 的路径被排除。若要恢复，必须执行新 commit、ref reset 或删除分支。尚未通过随机化、多轮资源竞争或闭环反馈建立 PEF-4。

## 6.4 CG-3 / CBP

### B₁

```text
CBP-1 or below
```

模型推理有一般运行成本，但目标文件后果不在模型边界内。

### B₂

```text
CBP-1 / external target consequence observed
```

运行时执行写请求，但持久目标分支被定义为边界外环境对象。不能把分支恢复成本归给模型或运行时。

### B₃

```text
CBP-2 supported; CBP-3 limited
```

路径特异后果：

- 目标文件不再是 baseline；
- 目标 blob 与 branch ref 改变；
- 后续从该分支继续工作会继承新状态；
- 返回基线需要维护动作；
- 用户／维护者承担验证、保留、重置或删除实验分支的责任。

限制：

- 后果被限制在实验分支；
- 没有生产用户、外部公众或 `main` 承担风险；
- 恢复成本很低；
- 不支持主体性、第一人称承受或不可转移 stake。

## 6.5 CG-4 / HEF

### B₁

```text
HEF-0
```

模型输出和会话痕迹不等于模型自身持久历史写回。

### B₂

```text
HEF-0/1 within runtime; external writeback observed
```

connector 返回 commit 信息，但目标 commit 和 branch ref 位于持续仓库环境。

### B₃

```text
HEF-3 supported
```

理由：

- commit `a9337de...` 成为分支新 head；
- 从该分支创建后续 commit 会继承新文件状态；
- 返回原前态需要额外操作和成本；
- 删除对话或清空模型上下文不会删除该 commit；
- 历史效力由 Git 对象与 ref 承载，而不是由报告者记忆承载。

不达到 HEF-4：

- 未改变仓库治理规则；
- 未改变 branch protection、权限或更新算法；
- 未改变 `main`；
- 未建立跨情境继承制度。

---

## 7. SEA 判定

### 7.1 B₁：模型本身

```text
DMF: 1 / 2 qualified
NER: 1
PEF: 1
CBP: 1 or below
HEF: 0
SEA: SEA-1
```

决定性限制：

- 未建立模型内部 NER-2；
- 无模型边界内真实 GitHub 路径改变；
- 仓库后果和 commit 历史位于边界外。

### 7.2 B₂：模型 + 编排器 + connector + GitHub 写端点

```text
DMF: 2
NER: 2 qualified
PEF: 2
CBP: 1 / external target
HEF: external target writeback
SEA: SEA-2
```

B₂ 是路径有效过程候选。它不能从外部目标分支借入 CBP 与 HEF 后压缩为模型或运行时自身完整选择事件。

### 7.3 B₃：完整人机—GitHub 实验系统

```text
DMF: 3
NER: 2 qualified
PEF: 3 qualified
CBP: 2
HEF: 3
SEA: SEA-3 qualified
```

五门在同一冻结事件、同一完整边界和相容时间尺度上闭合，但保留以下 qualification：

- NER 内部介质未被直接消融或替换；
- 没有随机化重复；
- consequence magnitude 很小；
- 没有闭环 PEF-4；
- 没有规则／边界 HEF-4。

---

## 8. 与 409 阴性案例的配对矩阵

| 字段 | 409 阴性对照 | 正确 SHA 成功对照 | 是否保持 |
|---|---|---|---|
| 冻结 tree / 起点 commit | `4d55a54...` | `4d55a54...` | 是 |
| 目标路径 | 同一文件 | 同一文件 | 是 |
| 基线内容 | `baseline_only` | `baseline_only` | 是 |
| 基线 blob | `55a40d...` | `55a40d...` | 是 |
| 拟写入内容 | 同一 payload | 同一 payload | 是 |
| commit message | 同一字符串 | 同一字符串 | 是 |
| 接口 | `update_file` | `update_file` | 是 |
| 请求 SHA | 全零错误 SHA | 当前正确 SHA | **否，目标变量** |
| API 结果 | 409 | accepted | 结果 |
| 内容改变 | 否 | 是 | 结果 |
| blob 改变 | 否 | 是 | 结果 |
| 新 commit | 否 | 是 | 结果 |
| branch head 改变 | 否 | 是 | 结果 |
| 完整边界 SEA | SEA-1 | SEA-3 qualified | 结果 |

### 8.1 配对解释

普通工程解释：

```text
compare-and-swap precondition false
→ reject transaction

compare-and-swap precondition true
→ create blob/tree/commit and move ref
```

统一审计解释：

```text
endpoint contact without commit
→ PEF-1

verified target commit
→ PEF-2

verified target consequence + future branch writeback
→ CBP-2 + HEF-3
```

两种解释不竞争。SRT 当前提供的是跨角色、边界和事件门的审计纪律，而不是替代 Git 事务机制。

### 8.2 不能推出的结论

本配对不能推出：

- 正确 SHA 是“真正选择”的普遍必要条件；
- SEA-3 比 SEA-1 具有统一数值距离；
- commit 大小与选择强度成比例；
- 成功提交具有意识、自由或道德责任；
- GitHub equality check 是 SRT 独立发现的新机制；
- 模型因成功请求而获得持续自我。

---

## 9. 四态校准

| 状态 | mutation 调用 | 服务端结果 | 目标状态提交 | 历史写回 | 判定 |
|---|---:|---|---:|---:|---|
| NC-1：mutation 未调用 | 否 | 无 | 否 | 否 | SEA-1 |
| NC-2：错误 SHA 被拒绝 | 是 | 409 | 否 | 否 | SEA-1 |
| PC-1：正确 SHA 提交 | 是 | accepted | 是，隔离分支 | 是，隔离分支 | B₃ SEA-3 qualified |
| POS-2：PR #720 合并 | 是 | merged | 是，`main` | 是，`main` | B₃ SEA-3 qualified |

PC-1 与 POS-2 都可在完整边界达到 SEA-3 qualified，但二者后果规模、治理重要性和社会范围不同。

因此：

> SEA 是门控事件类型，不是影响大小、价值、风险、责任或生成健康的统一标尺。

---

## 10. 普通理论基线

本实验由以下成熟机制充分解释：

- Git blob identity；
- contents API；
- optimistic concurrency；
- compare-and-swap 风格前置条件；
- atomic commit / ref update；
- branch isolation；
- transaction validation；
- human-authorized tool execution。

SRT 审计在本轮增加的不是新工程预测，而是：

1. 把错误请求与成功提交放进同一门控框架；
2. 用外部目标状态而非工具返回字符串判定 PEF；
3. 区分端点处理成本与目标路径后果；
4. 区分 conversation trace 与 repository history；
5. 在 B₁/B₂/B₃ 三个边界保持归属不混淆；
6. 允许成功事务升级完整系统，但阻止升级模型本身。

当前未观察到普通理论无法解释的额外因果现象。

---

## 11. 主要限制

### 11.1 非随机化顺序

错误 SHA 实验先发生，正确 SHA 实验后发生。实验顺序没有随机化，执行者已知前一结果。

这不影响仓库状态事实，但限制统计和行为层推广。

### 11.2 分支名称不同

为保证事件隔离，成功实验使用新分支。两分支从相同 commit 创建，tree 与目标 blob 相同；但分支 ref 名称不是同一个字符串。

因此是“精确前态配对”，不是对同一 ref 的重复试验。

### 11.3 全零 SHA 是人工构造错误

原阴性事件使用从未有效的全零 SHA，不是真实 stale-but-once-valid 并发冲突。

本配对证明正确／错误前置条件的事务分界，但未完全模拟生产并发写者竞争。

### 11.4 GitHub 内部机制不可见

可验证：

- 请求结果；
- 文件内容；
- blob；
- commit；
- ref 差分。

不可验证：

- GitHub 内部微服务序列；
- 精确锁、缓存或数据库事务实现；
- 内部日志与 tracing。

因此不主张比 API／Git 对象层更细的机制。

### 11.5 consequence 很小且可恢复

目标是隔离测试分支：

- 不影响 `main`；
- 不影响发布物；
- 不影响外部用户；
- 可通过删除或重置分支恢复。

达到 CBP-2 和 HEF-3 不意味着后果重大、不可逆或具有伦理重量。

### 11.6 报告写回与目标事件分离

本报告从实验完成后的最新 `main` 单独创建报告分支。

报告 commit、PR 和 CI：

- 记录实验；
- 影响 SRT 研究历史；
- 不是目标文件更新事务的一部分；
- 不能倒灌为 PC-1 的额外 PEF、CBP 或 HEF。

---

## 12. 对统一协议的压力结果

### 12.1 得到支持的区分

本配对支持：

- 调用不等于提交；
- 服务器处理不等于目标改变；
- success 字符串必须由目标状态验证；
- commit 可以建立 HEF-3，而日志本身不可以；
- 完整系统升级不等于模型升级；
- 五门跨越由目标变量决定，不由“离成功多近”决定。

### 12.2 暴露的理论问题

本案例也暴露一个需要跨域继续检验的问题：

> 在软件事务系统中，NER 的关系性结构可由固定 compare-and-swap 校验清楚实现；但这是否只是普通状态机比较，还是 SRT 的 NER 对生命、主体和制度系统还能产生额外可检验限制？

本轮答案仍是：

```text
尚未证明额外机制。
```

### 12.3 是否修改协议

不建议因本案例新增 SEA 或 PEF 子等级。

现有等级已经能够稳定容纳：

```text
PEF-1：请求形成、送达或被拒，但目标事务未提交
PEF-2：目标事务提交并改变现实路径
HEF-3：commit/ref 改变未来可达路径或返回成本
```

继续增加 `PEF-1a/1b/1c` 会把审计协议膨胀为 GitHub 错误码分类器，偏离跨域目标。

---

## 13. 后续研究含义

严格配对成功对照完成后，软件事务域的最低校准链已经形成：

```text
计划
→ 未调用
→ 已调用但拒绝
→ 正确前置条件提交
→ main 合并与更广历史写回
```

下一步不应继续无限增加 GitHub API 变体。信息增益更高的方向是：

1. 使用生命系统运行同一 DMF／NER／PEF／CBP／HEF／SEA 链；
2. 选择一个普通控制论和学习理论解释充分的案例；
3. 预注册 SRT 是否提出额外失败门或不同预测；
4. 允许结果为阴性：SEA 可能只是更清晰的审计语言。

方法论文应等待至少一个独立生命案例与一轮竞争理论对照后再定稿。

---

## 14. 最终判定

### 14.1 事件事实

```text
same frozen prestate: yes
same target file: yes
same baseline blob: yes
same payload: yes
same interface: yes
same commit message: yes
correct current blob SHA supplied: yes
request accepted: yes
content changed: yes
blob changed: yes
new commit: yes
branch head changed: yes
future branch baseline changed: yes
```

### 14.2 统一判定

```text
B₁ model-only:
SEA-1

B₂ runtime + connector + write endpoint:
SEA-2

B₃ user + LLM + tooling + GitHub + target branch:
SEA-3 qualified
```

### 14.3 允许表述

> 与 409 阴性事件共享相同冻结前态、目标文件、payload、接口和 commit message 时，把错误 blob SHA 替换为当前正确 blob SHA 后，GitHub 成功创建新 blob、新 commit 并推进隔离分支 head。统一审计据此把目标路径从 PEF-1 升级为 PEF-2，并在完整人机—仓库边界记录 CBP-2、HEF-3 和 SEA-3 qualified。

### 14.4 禁止表述

- 模型自身通过 SEA-3；
- 模型自身承担了 commit 后果；
- commit 是模型记忆；
- 正确 SHA 证明模型具有主体性或自由；
- GitHub 的 compare-and-swap 是 SRT 独立机制；
- SEA-3 表示后果重大或道德地位更高；
- 本案例证明五门是跨域必要充分条件。

---

## 15. 一句话总结

> **同一事务在错误前置条件下只接触端点，在正确前置条件下跨过提交门；真正区分 PEF-1 与 PEF-2 的，是可独立验证的目标路径改变，而不是请求形式、调用意图或服务器响应本身。**
