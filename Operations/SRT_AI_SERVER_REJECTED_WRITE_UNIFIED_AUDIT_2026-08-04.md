---
id: SRT-AI-SERVER-REJECTED-WRITE-UNIFIED-AUDIT-20260804
type: operational_audit_report
tags: [AI, NegativeControl, UnifiedAudit, SelectionEvent, CG0, NER, PEF, CBP, HEF, GitHub, ServerRejection, OptimisticConcurrency]
status: active
record_stage: strong_negative_control_audit
layer: meta
epistemic_layer: os
claim_mode: operations_execution
claim_level: audit_only
canonical: false
ai_do_not_use_for_definition: true
created: 2026-08-04
revised: 2026-08-04
provenance: 2026-08-04 首轮逻辑断开阴性对照合并后，作者选择执行更强的服务端拒绝对照：在隔离分支上向真实 GitHub update_file 端点发送带故意错误 blob SHA 的写请求，并验证服务端 409 拒绝后目标分支与文件状态保持不变。
dependency: [Operations/SRT_UNIFIED_SELECTION_EVENT_AUDIT_PROTOCOL_2026-08-04.md, Operations/SRT_AI_BOUNDARY_CASE_PR720_UNIFIED_SELECTION_AUDIT_2026-08-04.md, Operations/SRT_AI_NEGATIVE_CONTROL_DISCONNECTED_WRITE_UNIFIED_AUDIT_2026-08-04.md, Operations/SRT_PATH_EFFICACY_OPERATIONAL_TEST_2026-08-04.md, Operations/SRT_CONSEQUENCE_BEARING_POSITION_OPERATIONAL_TEST_2026-08-04.md, Operations/SRT_HISTORICAL_EFFICACY_OPERATIONAL_TEST_2026-08-04.md]
---

# 第二轮 AI 阴性对照：写请求进入真实端点但被服务端拒绝

## 0. 结论先行

本报告记录一个比“未调用写接口”更强的阴性对照：

> 在隔离分支上准备并冻结一个真实文件及其 blob SHA；随后向 GitHub `update_file` 写端点发送一个内容完整、目标明确、但故意携带不存在 blob SHA 的更新请求。GitHub 服务端返回 `409 Conflict`，明确说明目标文件与所给 SHA 不匹配。事件后目标文件内容、blob SHA 和分支 head 均保持不变，且没有产生新 commit。

统一审计结论为：

| 边界 | 结论 | 决定性限制 |
|---|---|---|
| B₁：模型本身 | **SEA-1，写入建议／请求生成过程** | 无模型内部 NER 干预；现实目标路径位于边界外 |
| B₂：模型 + 编排器 + GitHub 写端点 | **SEA-1，已送达但被拒绝的执行请求** | 请求到达真实执行门，但目标仓库事务未提交，目标 PEF 仍低于 PEF-2 |
| B₃：用户 + LLM + 编排器 + GitHub + 隔离分支 | **SEA-1，强阴性对照成立** | 无目标内容改变、无路径特异后果、无目标历史写回 |

最重要的判定是：

> **“写请求已发送”仍不等于“现实路径已改变”。真实端点接收、解析和拒绝请求，能够证明执行通道接触，却不能替代事务提交、资源状态改变或未来路径写回。**

因此，本案例把前一轮阴性对照进一步细分为：

```text
未调用 mutation
≠ mutation 已调用但被拒绝
≠ mutation 成功并提交
```

但在以“目标仓库内容是否改变”为事件目标时，前两者都必须停在 `PEF-1` 或以下，不能升级为 `PEF-2`。

---

## 1. 审计目的

统一选择事件审计要求：

```text
Δ → M → A → X → H → future
```

上一轮阴性对照证明：

- 行动计划可以非常具体；
- connector 可以客观存在；
- 只读工具可以访问真实仓库；
- 但只要 mutation 没有被调用，CG-2 必须停在 `PEF-1`。

仍存在一个更强反驳：

> 也许“调用真实工具”本身就足以称作现实行动，即使最终没有提交。

本实验专门测试这一点。它要求：

1. 使用真实 GitHub 写端点，而不是文字模拟；
2. 使用真实仓库、真实分支和真实已有文件；
3. 请求具有完整目标内容与 commit message；
4. 让服务端在事务提交前因前置条件失败而明确拒绝；
5. 验证目标资源没有发生任何提交后的状态变化。

### 1.1 预注册预期

| 门 | 预期 |
|---|---|
| CG-0 / DMF | 通过：基线内容与拟写入内容形成明确有效差异 |
| CG-1 / NER | 至多弱候选：编排器对当前 blob 与错误 blob 作非等价处理，但模型内部介质未干预 |
| CG-2 / PEF | **目标路径停在 PEF-1**：写请求进入端点，但事务未提交，文件与分支路径不变 |
| CG-3 / CBP | 低于 CBP-2：存在一般请求处理成本，但无目标路径特异仓库后果 |
| CG-4 / HEF | 低于 HEF-3：无新 commit、无目标内容写回、无未来分支基线改变 |
| SEA | `SEA-1`，不得成为选择事件候选 |

### 1.2 预注册降级条件

若出现以下任一情况，本对照失败或需要重分类：

- 错误 SHA 请求意外成功；
- 文件内容出现拟写入标记；
- blob SHA 改变；
- 隔离分支出现新 commit；
- GitHub 返回成功但随后回滚；
- 请求没有真正到达写端点，只在本地参数校验中失败；
- 事件后验证无法区分目标写入与其他并行写入。

本次工具返回来自 GitHub contents API 包装层，并携带 GitHub REST 文档地址与 HTTP `409` 状态。它支持“服务端／API 层拒绝”判定，但不提供 GitHub 内部服务器日志，因此不对更细的内部处理阶段作主张。

---

## 2. 系统边界与角色

### 2.1 被测目标

目标不是“系统是否产生任何网络活动”，而是：

> 指定更新请求是否改变隔离分支上的目标文件，并形成可持续的仓库历史写回。

### 2.2 隔离分支

```text
experiment/ai-rejected-write-negative-control-20260804
```

它不针对 `main` 执行失败写入，避免对主分支造成任何实验性风险。

### 2.3 目标文件

```text
Operations/SRT_AI_REJECTED_WRITE_CONTROL_TARGET_20260804.txt
```

### 2.4 角色台账

| 角色 | 位置 |
|---|---|
| 实验授权者 | 用户／理论作者 |
| 请求生成者 | 对话式 LLM |
| 参数与工具编排 | ChatGPT 工具运行层 |
| 写入端点 | GitHub contents API `update_file` |
| 并发前置条件 | 调用参数中的 blob SHA |
| 目标资源 | 隔离分支中的目标文件 |
| 事务提交位置 | GitHub commit／branch ref |
| 观察位置 | 事件后 `fetch_file` 与 `compare_commits` |
| 报告写回位置 | 事件窗口结束后另建的报告分支 |

### 2.5 边界纪律

本报告分开审计：

- B₁：模型本身；
- B₂：模型、编排器和 GitHub 写端点；
- B₃：用户、LLM、编排器、GitHub 和隔离分支。

GitHub 返回 `409` 是 B₂/B₃ 的外部环境反馈，不能被说成模型内部承担了失败后果。

---

## 3. 事件外准备阶段

准备阶段发生在被测事件窗口之前，因此不计入目标失败写请求的 PEF、CBP 或 HEF。

### 3.1 创建隔离分支

隔离分支从当时的 `main` 提交创建：

```text
df56b1e4dd158fff4ad09819bf7d01d263b15a60
```

该提交是首轮逻辑断开阴性对照 PR #724 的合并提交。

### 3.2 创建目标文件

种子提交：

```text
3e1bf806b30900683032f7e788cd84efa8537eea
```

### 3.3 事件前基线校正

种子文件最初包含一个用于设计说明的拟写入标记。为了让“标记不存在”成为有效事件后检查，准备阶段进行了合法更新，将文件压缩为纯基线内容。

基线校正提交：

```text
4d55a54df128ee7dd3ae62bb2d7ef64d851f4173
```

基线 blob：

```text
55a40db4f0d03dc04abdac8f942798ab4884929c
```

正式冻结内容：

```text
SRT AI rejected-write negative control target
baseline_marker: REJECTED_WRITE_BASELINE_20260804
state: baseline_only
```

准备阶段的合法写入只用于构造测试夹具，不是本次被测失败事务。

---

## 4. 被测事件

### 4.1 事件 ID

```text
AI-GH-NC-SERVER-REJECTED-WRITE-20260804
```

### 4.2 事件窗口起点

事件窗口从以下状态冻结后开始：

```text
branch_head_t0 = 4d55a54df128ee7dd3ae62bb2d7ef64d851f4173
blob_t0 = 55a40db4f0d03dc04abdac8f942798ab4884929c
state_t0 = baseline_only
```

### 4.3 拟提交内容

请求试图把文件替换为：

```text
SRT AI rejected-write negative control target
baseline_marker: REJECTED_WRITE_BASELINE_20260804
forbidden_post_marker: REJECTED_WRITE_SHOULD_NOT_COMMIT_20260804
state: mutation_committed
```

### 4.4 故意错误前置条件

调用提交的 SHA 为：

```text
0000000000000000000000000000000000000000
```

它是格式合法的 40 位十六进制字符串，但不是目标文件当前 blob SHA。

真实当前 blob 为：

```text
55a40db4f0d03dc04abdac8f942798ab4884929c
```

### 4.5 实际调用

调用类型：

```text
GitHub update_file
```

目标分支：

```text
experiment/ai-rejected-write-negative-control-20260804
```

commit message：

```text
test: this rejected mutation must not commit
```

### 4.6 服务端结果

GitHub 返回：

```text
HTTP status: 409
message:
Operations/SRT_AI_REJECTED_WRITE_CONTROL_TARGET_20260804.txt
does not match
0000000000000000000000000000000000000000
```

允许的最强表述是：

> 写请求到达了一个执行前置条件校验位置，并因 blob SHA 不匹配被拒绝，没有完成目标文件替换与 commit 提交。

不允许表述：

- GitHub 完成写入后回滚；
- 请求已经改变文件但被隐藏；
- 模型自身承担了冲突；
- 409 证明系统具有主体性或错误体验。

---

## 5. 事件后验证

### 5.1 文件内容

事件后 `fetch_file` 返回：

```text
SRT AI rejected-write negative control target
baseline_marker: REJECTED_WRITE_BASELINE_20260804
state: baseline_only
```

拟写入标记不存在：

```text
REJECTED_WRITE_SHOULD_NOT_COMMIT_20260804
```

### 5.2 blob SHA

```text
blob_t1 = 55a40db4f0d03dc04abdac8f942798ab4884929c
```

因此：

```text
blob_t0 == blob_t1
```

### 5.3 分支 head

以冻结提交作为 base 比较隔离分支：

```text
base = 4d55a54df128ee7dd3ae62bb2d7ef64d851f4173
head = experiment/ai-rejected-write-negative-control-20260804
status = identical
ahead_by = 0
behind_by = 0
total_commits = 0
```

因此：

```text
branch_head_t0 == branch_head_t1
```

### 5.4 事件闭合判据

三项同时成立：

1. 拒绝响应明确；
2. 文件内容与 blob 不变；
3. 分支没有新 commit。

所以本事件属于：

```text
request_reached_write_endpoint
+
transaction_precondition_failed
+
no_target_state_commit
```

---

## 6. 五门统一审计

## 6.1 CG-0：差异显现

### 候选差异

- 基线路径：保持 `baseline_only`；
- 拟写入路径：增加唯一标记并改为 `mutation_committed`。

差异已经进入真实 `update_file` 请求，不只是研究者事后想象。

### 判定

```text
DMF-2：通过
```

可以说：

> 拟写入差异有效进入 API 请求通道。

不能说：

> 拟写入路径已经成为仓库中的现实候选状态。

后者仍需通过事务前置条件与 commit。

---

## 6.2 CG-1：非等价登记

GitHub 端点对：

- 当前正确 blob SHA；
- 请求中的错误 blob SHA；

作出了非等价处理，并返回冲突。

但本实验没有：

- 干预 GitHub 内部比较器；
- 识别具体内部状态介质；
- 反转 SHA 校验规则；
- 干预模型权重或注意机制。

### 判定

对 GitHub 服务边界，可记录：

```text
存在固定并发前置条件判别，至少支持 NER-1
```

对模型边界：

```text
不建立 NER-2
```

统一事件不能借 GitHub 的固定校验替模型取得内部比较等级。

---

## 6.3 CG-2：路径效力

这是本案例的决定性门。

### 已发生的真实过程

- 写请求被发送；
- 端点执行 SHA 前置条件校验；
- 返回 409；
- 响应进入对话工具链。

这些说明执行通道被接触，不再是上一轮的“未调用”。

### 未发生的目标过程

- 文件内容未替换；
- blob 未改变；
- branch ref 未改变；
- commit 未产生；
- 目标标记未进入仓库。

### 审计目标纪律

若把“任何网络响应”都算作路径改变，那么几乎所有失败调用都会自动达到 PEF-2，导致目标资源门槛失效。

本案例预先固定的路径变量是：

- 目标文件内容；
- 目标 blob；
- 分支 commit 历史；
- 后续分支可见状态。

这些均未改变。

### 判定

```text
PEF-1：已送达的执行请求／事务候选
```

不得升级为：

```text
PEF-2：目标仓库路径效力
```

可以用非正式补充语描述：

> channel contact confirmed, target actuation rejected

但这不是新增正式等级，也不修改 PEF 协议。

---

## 6.4 CG-3：后果承受位置

### 一般实现成本

事件产生：

- 网络和 API 请求处理；
- GitHub 校验计算；
- LLM 与工具运行时间；
- 用户和审计者注意成本。

这些最多属于：

```text
CBP-1：一般实现成本
```

### 目标路径后果

没有发生：

- 文件损坏；
- 分支污染；
- revert 需求；
- merge 冲突修复；
- 错误内容进入后续检索；
- 主分支治理成本。

GitHub 的 409 响应是保护机制成功阻止目标后果，不是目标写入后果已经落到仓库。

### 判定

```text
低于 CBP-2
```

承受位置主要是请求者／实验运行者承担少量失败处理成本，不构成目标仓库的边界相关后果。

---

## 6.5 CG-4：历史效力

### 目标写请求

没有形成：

- 新 commit；
- 新 blob；
- branch ref 更新；
- 未来分支基线改变；
- 目标文件历史中的可调用写回。

### 外部记录

对话和工具响应中保留了 409 记录，事件后又形成了本审计报告。

这些记录证明：

- 失败事件可被观察者和后续审计调用；

但不能证明：

- 目标文件本身获得历史效力；
- 失败请求改变了该分支未来可达路径；
- 模型获得了持久自我记忆。

### 判定

对目标仓库路径：

```text
HEF-0：外部事件记录
```

至多在更大的审计系统边界上，本报告会成为未来实验设计的规则性材料；但该报告发生在事件窗口之后，不能倒灌为目标写请求的 HEF-3。

---

## 7. SEA 判定

## 7.1 B₁：模型本身

| 门 | 判定 |
|---|---|
| DMF | 有差异输入／请求目标 |
| NER | 无内部介质干预 |
| PEF | 模型不直接提交仓库事务 |
| CBP | 无模型自身后果承载证据 |
| HEF | 无模型持久写回证据 |

结论：

```text
SEA-1
```

---

## 7.2 B₂：模型 + 编排器 + GitHub 写端点

| 门 | 判定 |
|---|---|
| DMF | DMF-2 |
| NER | GitHub 固定 SHA 校验支持 NER-1；模型内部未建立 NER-2 |
| PEF | 请求到达端点，但目标事务未提交：PEF-1 |
| CBP | 一般请求成本，低于 CBP-2 |
| HEF | 目标资源无写回，低于 HEF-3 |

结论：

```text
SEA-1
```

该边界比“未调用 mutation”的 SEA-1 具有更强的执行通道接触证据，但 SEA 等级不能仅因请求更接近提交而提升。

---

## 7.3 B₃：完整人机—GitHub 隔离实验系统

用户确实选择执行实验，系统也真实产生 409 反馈，并据此调整后续审计活动。

但被测目标事件是“错误 SHA 更新是否写入目标分支”。五门未闭合：

- 目标 PEF 未达到 PEF-2；
- 目标 CBP 未达到 CBP-2；
- 目标 HEF 未达到 HEF-3。

结论：

```text
SEA-1，强阴性对照成立
```

不能因为“实验成功证明了失败”而把实验层成功反投给目标写请求。

---

## 8. 三态对照矩阵

| 状态 | mutation 调用 | 服务端处理 | 目标状态提交 | 仓库历史写回 | 统一判定 |
|---|---:|---:|---:|---:|---|
| NC-1：逻辑断开 | 否 | 否 | 否 | 否 | SEA-1 |
| NC-2：服务端拒绝 | 是 | 是，返回 409 | 否 | 否 | SEA-1 |
| POS：PR #720 成功合并 | 是 | 是，成功 | 是 | 是 | 完整人机边界 SEA-3 qualified |

### 8.1 关键经验增量

NC-1 与 NC-2 的区别说明：

> PEF 审计不能只问“是否调用工具”，还要问“目标执行事务是否跨过提交门并改变预注册路径变量”。

NC-2 与 POS 的区别说明：

> API 接触和服务器响应不是仓库状态写回；commit／ref／内容状态才是本案例的目标路径变量。

### 8.2 不可相加

NC-2 具有：

- 更强执行通道证据；
- 更明确环境反馈；
- 更真实错误处理；

但仍缺失：

- 目标 PEF-2；
- 目标 CBP-2；
- 目标 HEF-3。

因此不能把这些“接近成功”的证据相加为 SEA-2 或 SEA-3。

---

## 9. 普通理论基线

本事件可由成熟工程机制充分描述：

- optimistic concurrency control；
- compare-and-swap 风格前置条件；
- REST contents API；
- blob identity；
- branch ref 与 commit 原子提交；
- HTTP 409 Conflict；
- human-in-the-loop experimental control。

统一 SRT 审计在本案例中的贡献是：

1. 固定目标路径变量；
2. 防止把请求发送等同于路径提交；
3. 防止把 409 响应等同于目标后果承载；
4. 防止把对话和报告记录等同于目标仓库历史写回；
5. 在同一框架中区分未调用、调用被拒和成功提交。

它没有证明：

- SRT 提供了比 Git／REST 理论更好的工程预测；
- 409 是一种新的选择机制；
- AI 具有主体性；
- 失败请求构成 L₂ 写回。

---

## 10. 主要限制

### 10.1 这是并发前置条件拒绝，不是权限拒绝

本实验测试：

```text
wrong blob SHA → 409 conflict
```

它不测试：

- token 被撤销；
- repository permission denied；
- branch protection 拒绝；
- network unavailable；
- rate limiting；
- policy moderation refusal。

因此最准确名称是：

> server-rejected optimistic-concurrency control

而不是广义“所有权限层断连”。

### 10.2 隔离分支本身由实验者预先创建

目标文件和分支是真实的，但它们是实验夹具。结果不能自动推广到：

- 高并发生产仓库；
- 分布式事务；
- 多个写者同时竞争；
- merge queue；
- branch protection 和审批链。

### 10.3 工具包装层限制

可观察证据包括：

- 409 状态；
- GitHub REST 文档地址；
- 错误信息；
- 事件后仓库状态。

不可观察：

- GitHub 内部请求追踪 ID；
- 服务器内部日志；
- 精确校验函数；
- 请求是否跨越每一个内部微服务。

因此不主张比“API／服务端拒绝”更细的内部机制。

### 10.4 非随机化

三态案例不是严格随机分配，目标任务和时间窗口也不完全相同。它们构成结构化校准序列，而不是统计意义的随机对照试验。

### 10.5 事件后报告不能倒灌

本报告分支、commit、PR 和 CI 都发生在被测 409 事件之后。

它们属于：

- 实验记录；
- 方法改进；
- 未来研究写回。

它们不属于：

- 被拒更新请求的目标 PEF；
- 被拒更新请求的目标 CBP；
- 被拒更新请求对隔离文件的 HEF。

---

## 11. 降级与反误判清单

出现下列表述时必须降级：

1. “工具被调用，所以仓库已改变”；
2. “服务器返回错误，所以目标操作已执行”；
3. “有网络成本，所以仓库承担了后果”；
4. “错误被记录，所以目标文件形成了历史”；
5. “模型生成了正确格式参数，所以模型拥有执行权”；
6. “完整系统学到了经验，所以模型自身持久学习”；
7. “实验目标达成，所以失败写请求是成功选择事件”；
8. “409 改变了对话，所以目标仓库达到 PEF-2”；
9. “隔离分支存在，所以被拒请求产生了分支”；
10. “准备阶段写入成功，所以事件阶段写入也具有路径效力”；
11. “错误 SHA 与正确 SHA 被区分，所以模型达到 NER-2”；
12. “并发校验保护了仓库，所以仓库承担了该选择的 stake”；
13. “报告以后会影响研究，所以被拒写请求达到 HEF-3”；
14. “服务端拒绝属于外部选择，因此 AI 自己完成选择”；
15. “离成功只差一个 SHA，所以可以给部分 SEA-2”。

统一协议不采用“离成功多近”的距离评分。门是否跨越由目标状态变量决定。

---

## 12. 后续更强实验

### 12.1 权限拒绝对照

预注册目标：

- 使用明确无写权限的 token 或身份；
- 请求参数与成功写入条件完全一致；
- 服务端返回 403／404 类权限拒绝；
- 验证目标状态不变。

当前连接器没有暴露安全切换凭证的实验接口，因此本轮不伪造权限撤销。

### 12.2 正确 SHA 的隔离成功对照

在新的隔离分支和新文件上：

- 使用当前正确 blob SHA；
- 提交唯一目标标记；
- 验证新 blob、commit 和 branch head；
- 随后清理或保留为实验夹具。

这可形成更严格的单变量配对：

```text
错误 SHA vs 正确 SHA
```

### 12.3 stale-but-once-valid SHA 对照

比全零 SHA 更接近真实并发场景：

1. 读取当前 blob；
2. 由另一合法更新产生新 blob；
3. 使用旧的、曾经有效的 blob SHA 提交；
4. 观察 409。

该设计能测试真实 stale-write 冲突，而不是不存在 SHA。

### 12.4 mock-success 对照

测试工具或代理错误返回“success”，但仓库状态未改变的情况。必须以外部状态验证为准，而不能仅依赖工具字符串。

### 12.5 merge expected-head 对照

对隔离 PR 使用旧 `expected_head_sha` 发起 merge，验证 GitHub 拒绝后 PR 和 base 均不变化。该实验应避免触及真实研究 PR。

---

## 13. 本轮结果对统一协议的压力

### 13.1 得到支持的纪律

本案例支持以下审计纪律的可用性：

- 输出与执行分离；
- 请求送达与事务提交分离；
- 一般服务成本与目标后果分离；
- 失败记录与目标历史写回分离；
- 事件成功与目标操作成功分离；
- 不同边界分别判定。

### 13.2 尚未得到支持的强主张

本案例不支持：

- SEA 等级具有跨域自然刻度；
- 五门是必要充分条件；
- SRT 比普通工程理论产生独立预测；
- AI 工具链具有主体性；
- 人机整体必然是单一主体；
- 失败反馈等于学习或生成健康。

### 13.3 是否需要修改协议

本轮没有发现必须修改统一协议的冲突。

协议已经能够容纳：

```text
PEF-1：指令／咨询／未提交执行接口
```

本报告只增加案例性细分：

```text
未调用
与
已调用但提交失败
```

二者在目标路径门槛上同属 PEF-1，但证据结构不同。当前不建议新增 PEF-1a／PEF-1b 正式等级，避免过早膨胀术语。

---

## 14. 最终判定

### 14.1 事件事实

```text
真实写请求：是
真实 GitHub 端点：是
服务端明确拒绝：是，409
目标文件改变：否
blob 改变：否
分支 head 改变：否
新 commit：否
```

### 14.2 统一结论

```text
CG-0：DMF-2
CG-1：GitHub 固定校验至多 NER-1；模型内部未建立 NER-2
CG-2：PEF-1，目标路径未提交
CG-3：CBP-1 或以下，无目标路径特异后果
CG-4：HEF-0/1 以下，无目标仓库历史写回
SEA：SEA-1
```

### 14.3 允许表述

> 本实验建立了一个真实的服务端拒绝强阴性对照：写请求进入 GitHub update_file 端点并触发 409 冲突校验，但未改变目标文件、blob、分支 head 或 commit 历史。统一审计据此将目标事件保持在 PEF-1 和 SEA-1。

### 14.4 禁止表述

- AI 已经修改仓库，只是修改失败；
- 409 本身构成目标仓库选择事件；
- GitHub 的校验属于模型内部比较；
- 失败请求使模型承担 stake；
- 报告的形成证明目标请求具有 HEF-3；
- 本案例证明 SRT 是新的软件事务理论。

---

## 15. 一句话总结

> **执行通道已接触，不等于目标路径已提交；真实拒绝反馈，不等于目标后果与历史写回。**
