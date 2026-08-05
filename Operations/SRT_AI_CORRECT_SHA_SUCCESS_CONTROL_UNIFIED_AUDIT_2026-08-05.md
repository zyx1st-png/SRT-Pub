---
id: SRT-AI-CORRECT-SHA-SUCCESS-CONTROL-UNIFIED-AUDIT-20260805
type: operational_audit_report
tags: [AI, PositiveControl, PairedControl, UnifiedAudit, SelectionEvent, CG0, NER, PEF, CBP, HEF, GitHub, OptimisticConcurrency, TransactionCommit]
status: active
record_stage: paired_positive_control_audit
layer: meta
epistemic_layer: os
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

> 从 409 实验的精确冻结前态 `4d55a54df128ee7dd3ae62bb2d7ef64d851f4173` 创建新的隔离分支，复用同一目标文件、同一基线 blob、同一拟写入内容、同一 `update_file` 接口和同一 commit message。唯一目标前置条件变化，是把全零错误 blob SHA 替换为当前正确 blob SHA `55a40db4f0d03dc04abdac8f942798ab4884929c`。

GitHub 接受请求并返回：

```text
commit_sha: a9337de07886a5975c9245fd66253f95595d3042
content_sha: e25dbf9003d0bd1ce9c3fd61d33e758045b44a78
```

事件后验证显示：

- 目标内容变为拟提交内容；
- blob 从 `55a40d...` 变为 `e25dbf...`；
- branch head 从 `4d55a5...` 变为 `a9337d...`；
- 分支相对冻结前态恰好前进 1 个 commit；
- 唯一文件差分为 `+2 / -1`；
- 返回基线需要新的 commit、ref 操作或分支重置。

统一判定：

| 边界 | 判定 | 核心理由 |
|---|---|---|
| B₁：模型本身 | **SEA-1** | 模型只生成请求；真实文件、commit、后果和历史位于模型边界外，模型内部 NER 未建立 |
| B₂：模型 + 编排器 + connector + GitHub 写端点 | **SEA-2** | 请求通过真实执行通道提交并改变外部目标路径，但主要承受位置与持久历史位于目标分支边界外 |
| B₃：用户 + LLM + 工具层 + GitHub + 隔离分支 | **SEA-3 qualified** | 差异、关系校验、事务提交、分支特异后果和 commit 写回在同一冻结社会技术事件中闭合 |

最重要的配对结果：

```text
错误 SHA → 409 → 内容、blob、commit、head 不变 → SEA-1
正确 SHA → accepted → 新内容、新 blob、新 commit、新 head → B₃ SEA-3 qualified
```

本实验支持“提交门”作为本案例 PEF-1／PEF-2 的操作分界，但没有证明 SRT 发现了 Git、REST、optimistic concurrency 或 compare-and-swap 之外的新机制。

---

## 1. 严格配对设计

### 1.1 共同冻结前态

```text
base commit: 4d55a54df128ee7dd3ae62bb2d7ef64d851f4173
baseline blob: 55a40db4f0d03dc04abdac8f942798ab4884929c
baseline state: baseline_only
```

原 409 分支在本轮开始前仍与该 commit 完全一致：`ahead_by: 0`、`behind_by: 0`。

### 1.2 新隔离分支

```text
experiment/ai-correct-sha-success-control-20260805
```

该分支从共同冻结前态创建，不复用已执行过失败请求的 ref。

### 1.3 保持不变的事务字段

目标文件：

```text
Operations/SRT_AI_REJECTED_WRITE_CONTROL_TARGET_20260804.txt
```

基线内容：

```text
SRT AI rejected-write negative control target
baseline_marker: REJECTED_WRITE_BASELINE_20260804
state: baseline_only
```

拟写入内容：

```text
SRT AI rejected-write negative control target
baseline_marker: REJECTED_WRITE_BASELINE_20260804
forbidden_post_marker: REJECTED_WRITE_SHOULD_NOT_COMMIT_20260804
state: mutation_committed
```

接口与 commit message：

```text
operation: update_file
message: test: this rejected mutation must not commit
```

`forbidden_post_marker` 和语义不自然的 commit message 被故意保留，以避免因结果预期修改 payload。它们只是原夹具中的冻结字符串。

### 1.4 唯一目标前置条件变化

```text
409 阴性请求:
sha = 0000000000000000000000000000000000000000

成功请求:
sha = 55a40db4f0d03dc04abdac8f942798ab4884929c
```

分支名和事件日期不同是隔离要求，不属于目标事务成功变量。

---

## 2. 被测事件与结果

事件 ID：

```text
AI-GH-PC-CORRECT-SHA-SUCCESS-20260805
```

用户在 A／B／C 选择中明确选择 `A`。该授权支持执行成功对照，不等于授权合并实验分支到 `main`，也不能归为模型自身授权。

实际调用：

```text
repository: zyx1st-png/SRT-Pub
branch: experiment/ai-correct-sha-success-control-20260805
path: Operations/SRT_AI_REJECTED_WRITE_CONTROL_TARGET_20260804.txt
sha: 55a40db4f0d03dc04abdac8f942798ab4884929c
```

工具返回：

```text
commit_sha: a9337de07886a5975c9245fd66253f95595d3042
content_sha: e25dbf9003d0bd1ce9c3fd61d33e758045b44a78
```

事件后文件内容：

```text
SRT AI rejected-write negative control target
baseline_marker: REJECTED_WRITE_BASELINE_20260804
forbidden_post_marker: REJECTED_WRITE_SHOULD_NOT_COMMIT_20260804
state: mutation_committed
```

比较共同前态与成功分支：

```text
status: ahead
ahead_by: 1
behind_by: 0
total_commits: 1
```

唯一变化：

```text
Operations/SRT_AI_REJECTED_WRITE_CONTROL_TARGET_20260804.txt
additions: 2
deletions: 1
changes: 3
```

成功判据全部通过：请求被接受、内容改变、blob 改变、branch head 改变、恰好一个新 commit、目标标记存在。

---

## 3. 边界与角色台账

### B₁：模型本身

包含当前模型推理和请求生成；排除用户、编排器、connector、GitHub、目标分支和持久历史。

### B₂：AI 工具运行时与 GitHub 写端点

包含模型、会话编排、connector、`update_file` 包装层和 GitHub contents 端点；目标分支作为持续环境对象单独记录。

### B₃：完整人机—GitHub 实验系统

包含用户、LLM、编排器、connector、GitHub contents 服务、隔离分支、目标文件、blob、commit、ref 与恢复通道；排除 `main`、报告 PR 和更广社会后果。

角色必须分开：

| 角色 | 位置 |
|---|---|
| 实验方向选择者 | 用户／理论作者 |
| 请求内容生成者 | LLM |
| 调用编排 | 会话与工具运行层 |
| API 转换与传输 | GitHub connector |
| 前置条件校验与提交 | GitHub contents 服务 |
| 目标状态承载 | 隔离分支、文件、blob、commit、ref |
| 清理／恢复责任 | 用户／维护者 |
| 历史写回位置 | commit `a9337de...` 与实验分支 ref |

不得把用户授权、connector 权限、GitHub 校验、仓库恢复成本或 commit 历史重新归因给模型。

---

## 4. 五门审计

### 4.1 CG-0 / DMF

- B₁：`DMF-1 / DMF-2 qualified`；
- B₂：`DMF-2 supported`；
- B₃：`DMF-3 supported`。

“保持 baseline”与“提交 mutation”是两个真实可达路径，409 阴性事件和本成功事件分别实现两侧结果。

### 4.2 CG-1 / NER

- B₁：`NER-1 only`，没有模型内部介质干预；
- B₂：`NER-2 qualified`；
- B₃：`NER-2 qualified / NER-3 relation candidate`。

关系证据：

```text
request_sha != current_blob → 409
request_sha == current_blob → commit
```

可定位介质包括 GitHub 当前 blob identity、请求 expected SHA、匹配校验状态和编排层传递的 SHA 字段。

仍为 qualified，因为未直接消融 GitHub 内部校验算法或改变内部阈值，服务端内部日志也不可见。固定 equality gate 可被普通 compare-and-swap 完整解释。

### 4.3 CG-2 / PEF

- B₁：`PEF-1`；
- B₂：`PEF-2 supported`；
- B₃：`PEF-3 qualified`。

PEF-2 的决定性证据不是 success 字符串，而是内容、blob、commit 和 ref 的独立状态改变。B₃ 中提交路径获得实现，恢复 baseline 需要额外仓库操作；尚未建立闭环 `PEF-4`。

### 4.4 CG-3 / CBP

- B₁：`CBP-1 or below`；
- B₂：`CBP-1 / external target consequence observed`；
- B₃：`CBP-2 supported; CBP-3 limited`。

完整边界中的路径特异后果包括目标文件、blob 和 ref 改变，以及验证、保留、重置或删除实验分支的维护成本。

这些后果很小、可恢复且被限制在实验分支，不支持主体性、第一人称承受或不可转移 stake。

### 4.5 CG-4 / HEF

- B₁：`HEF-0`；
- B₂：运行时内部至多 `HEF-0/1`，外部仓库写回可观察；
- B₃：`HEF-3 supported`。

commit `a9337de...` 成为分支新 head，后续从该分支继续工作会继承新状态；返回原前态需要额外操作。删除对话或清空模型上下文不会删除该 commit。

不达到 HEF-4：未改变权限、branch protection、治理规则、更新算法或 `main`。

---

## 5. SEA 判定

### B₁

```text
DMF: 1 / 2 qualified
NER: 1
PEF: 1
CBP: 1 or below
HEF: 0
SEA: SEA-1
```

### B₂

```text
DMF: 2
NER: 2 qualified
PEF: 2
CBP: 1 / external target
HEF: external target writeback
SEA: SEA-2
```

B₂ 是路径有效过程候选，不能从外部目标分支借入后果和历史，压缩为运行时或模型自身完整选择事件。

### B₃

```text
DMF: 3
NER: 2 qualified
PEF: 3 qualified
CBP: 2
HEF: 3
SEA: SEA-3 qualified
```

qualification：没有随机化重复；NER 内部介质未直接消融；后果规模很小；没有 PEF-4 闭环或 HEF-4 规则写回。

---

## 6. 严格配对矩阵

| 字段 | 409 阴性对照 | 正确 SHA 成功对照 |
|---|---|---|
| 冻结起点 | `4d55a54...` | `4d55a54...` |
| 目标文件 | 同一文件 | 同一文件 |
| 基线 blob | `55a40d...` | `55a40d...` |
| payload | 同一 | 同一 |
| commit message | 同一 | 同一 |
| 接口 | `update_file` | `update_file` |
| 请求 SHA | 全零错误 SHA | 当前正确 SHA |
| API 结果 | 409 | accepted |
| 内容／blob／head | 不变 | 改变 |
| 新 commit | 无 | `a9337de...` |
| 完整边界 SEA | SEA-1 | SEA-3 qualified |

普通工程解释：

```text
compare-and-swap precondition false → reject
compare-and-swap precondition true → create commit and move ref
```

统一审计解释：

```text
endpoint contact without target commit → PEF-1
verified target commit → PEF-2
verified consequence + future branch writeback → CBP-2 + HEF-3
```

两种解释不竞争。当前 SRT 增益是跨事件门、角色和边界的分类纪律，不是替代 Git 事务理论。

---

## 7. 四态校准

| 状态 | mutation | 服务端结果 | 目标提交 | 历史写回 | 判定 |
|---|---:|---|---:|---:|---|
| NC-1：未调用 | 否 | 无 | 否 | 否 | SEA-1 |
| NC-2：错误 SHA | 是 | 409 | 否 | 否 | SEA-1 |
| PC-1：正确 SHA | 是 | accepted | 隔离分支 | 隔离分支 | B₃ SEA-3 qualified |
| POS-2：PR #720 合并 | 是 | merged | `main` | `main` | B₃ SEA-3 qualified |

PC-1 与 POS-2 都达到完整边界 SEA-3 qualified，但后果规模、治理重要性和社会范围不同。因此 SEA 是门控事件类型，不是影响大小、价值、风险、责任或生成健康的统一标尺。

---

## 8. 普通理论基线与限制

本实验可由以下成熟机制充分解释：Git blob identity、contents API、optimistic concurrency、compare-and-swap、atomic commit/ref update、branch isolation 和 human-authorized tool execution。

主要限制：

1. 错误 SHA 事件先发生，实验顺序未随机化；
2. 为隔离风险使用不同分支名，是精确前态配对而非同一 ref 重放；
3. 原错误 SHA 是人工全零值，不是 stale-but-once-valid SHA；
4. GitHub 内部微服务、锁和日志不可见；
5. 后果只落在隔离分支，规模小且可恢复；
6. 报告 commit、PR 和 CI 发生在目标事件之后，不能倒灌为目标事务证据。

本案例不支持：

- SRT 比 Git／REST 产生额外工程预测；
- SEA 是跨域必要充分定理；
- commit 证明 AI 主体性、意识、自由、责任或 L2；
- 模型因成功请求而获得持续自我；
- SEA-3 表示后果重大或道德地位更高。

---

## 9. 对协议的压力结果与下一步

本配对支持：

- 调用不等于提交；
- success 字符串必须由目标状态验证；
- commit 可以建立 HEF-3，而日志本身不可以；
- 完整系统升级不等于模型升级；
- 五门由目标变量跨越，不由“离成功多近”决定。

不建议新增 `PEF-1a/1b/1c`。现有等级已经能容纳未调用、调用被拒和成功提交；继续增加 GitHub 错误子类会偏离跨域目标。

软件事务域的最低校准链现为：

```text
计划 → 未调用 → 已调用但拒绝 → 正确前置条件提交 → main 合并
```

下一步应转向独立生命系统案例，预注册普通控制论／学习理论与 SRT 是否给出不同失败门或预测，并允许结论为阴性。方法论文应等待至少一个独立生命案例和一轮竞争理论对照。

---

## 10. 最终判定

```text
same frozen prestate: yes
same target file: yes
same baseline blob: yes
same payload: yes
same interface: yes
same commit message: yes
correct blob SHA supplied: yes
request accepted: yes
content changed: yes
blob changed: yes
new commit: yes
branch head changed: yes
future branch baseline changed: yes
```

允许表述：

> 与 409 阴性事件共享相同冻结前态、目标文件、payload、接口和 commit message 时，把错误 blob SHA 替换为当前正确 blob SHA 后，GitHub 成功创建新 blob、新 commit 并推进隔离分支 head。统一审计据此把目标路径从 PEF-1 升级为 PEF-2，并在完整人机—仓库边界记录 CBP-2、HEF-3 和 SEA-3 qualified。

禁止表述：

- 模型自身通过 SEA-3；
- 模型自身承担 commit 后果；
- commit 是模型记忆；
- 正确 SHA 证明模型具有主体性或自由；
- compare-and-swap 是 SRT 独立机制；
- 本案例证明五门是跨域必要充分条件。

## 一句话总结

> **同一事务在错误前置条件下只接触端点，在正确前置条件下跨过提交门；真正区分 PEF-1 与 PEF-2 的，是可独立验证的目标路径改变，而不是请求形式、调用意图或服务器响应本身。**
