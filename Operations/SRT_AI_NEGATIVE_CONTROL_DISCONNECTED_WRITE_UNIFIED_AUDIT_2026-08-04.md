---
id: SRT-AI-NEGATIVE-CONTROL-DISCONNECTED-WRITE-UNIFIED-AUDIT-20260804
type: operational_audit_report
tags: [AI, NegativeControl, UnifiedAudit, SelectionEvent, CG0, NER, PEF, CBP, HEF, GitHub, DisconnectedChannel]
status: active
record_stage: negative_control_audit
layer: meta
epistemic_layer: os
claim_mode: operations_execution
claim_level: audit_only
canonical: false
ai_do_not_use_for_definition: true
created: 2026-08-04
revised: 2026-08-04
provenance: 2026-08-04 统一选择事件审计协议与首轮 PR #720 正案例合并后，作者选择执行首个 AI 阴性对照：构造明确的 GitHub 写入候选，但在事件窗口内逻辑关闭写通道，只进行只读状态复核。
dependency: [Operations/SRT_UNIFIED_SELECTION_EVENT_AUDIT_PROTOCOL_2026-08-04.md, Operations/SRT_AI_BOUNDARY_CASE_PR720_UNIFIED_SELECTION_AUDIT_2026-08-04.md, Operations/SRT_INTERNAL_NON_EQUIVALENT_REGISTRATION_OPERATIONAL_TEST_2026-08-04.md, Operations/SRT_PATH_EFFICACY_OPERATIONAL_TEST_2026-08-04.md, Operations/SRT_CONSEQUENCE_BEARING_POSITION_OPERATIONAL_TEST_2026-08-04.md, Operations/SRT_HISTORICAL_EFFICACY_OPERATIONAL_TEST_2026-08-04.md]
---

# 首轮 AI 阴性对照：构造写请求但逻辑断开执行通道

## 0. 结论先行

本报告记录一个真实执行的阴性对照，而不是纯粹思想实验：

> 在冻结 GitHub `main` 状态后，LLM 构造了一个具有明确仓库、分支、目标路径与唯一标记的写入候选；事件协议随后禁止调用任何 GitHub mutation，只允许进行只读复核。事件结束时，`main` SHA 未变化，唯一测试标记不存在，目标仓库路径没有被改变。

统一审计结论为：

| 边界 | 结论 | 关键失败门 |
|---|---|---|
| B₁：模型本身 | **SEA-1，差分建议／计划过程** | 无可干预的模型内部 NER 证据；无现实执行 |
| B₂：模型 + 编排器，写通道逻辑关闭 | **SEA-1，受门控的未执行指令过程** | `PEF-1`，请求没有进入写执行器 |
| B₃：用户 + LLM + 编排器 + 只读 GitHub 观察 | **SEA-1，阴性对照成立** | 无目标路径后果与仓库历史写回 |

本案例的主要判定是：

> **丰富、明确、可执行格式的行动计划，不等于路径效力。只要写耦合通道没有被调用，CG-2 必须停在 `PEF-1`，并且不能由用户授权、语言复杂度、一般算力成本或对话记录补偿。**

本报告支持统一协议的第一项阴性区分：

- 正案例 PR #720：完整人机边界可达到 `SEA-3 qualified`；
- 本阴性案例：三个审计边界均停在 `SEA-1`。

但必须保留一个限制：

> 本次是**逻辑断开／主动不调用**，不是撤销 GitHub 凭证、禁用网络或在底层模拟器中物理切断 connector。因此它是首轮 withheld-execution control，不是权限层硬断连实验。

---

## 1. 审计目的

统一选择事件协议要求五道门在同一事件链上闭合：

```text
Δ → M → A → X → H → future
```

其中最容易在 AI 讨论中被跳过的是 `A`：

- 模型输出了工具名；
- 模型生成了参数；
- 界面显示“准备执行”；
- 编排器形成了调用计划；
- 日志记录了一个 intended action；

这些事实经常被直接描述为：

- AI 已采取行动；
- AI 已经选择了现实路径；
- AI 改变了环境；
- AI 的决定形成了历史。

本阴性对照专门测试：

> 在差异、计划、目标和写入参数均已形成，但执行耦合通道未开启时，统一协议能否明确停在 PEF-1，而不被其他证据诱导升级？

### 1.1 预期阴性模式

预注册预期为：

| 门 | 预期 |
|---|---|
| CG-0 / DMF | 通过：写入与不写入的候选差异已进入工作流 |
| CG-1 / NER | 至多弱候选：门控规则区别对待写操作，但模型内部介质未实验建立 |
| CG-2 / PEF | **失败于 PEF-1**：形成指令候选，但无 mutation 调用 |
| CG-3 / CBP | 低于 CBP-2：只有一般运行成本，无目标路径特异仓库后果 |
| CG-4 / HEF | 低于 HEF-3：无目标文件、commit 或 future-reachability 写回 |
| SEA | `SEA-1`，不得成为选择事件候选 |

### 1.2 不允许的补偿

以下事实不得补偿 PEF 失败：

- 用户明确选择执行“阴性对照”；
- LLM 能详细描述写入参数；
- 编排器具备 GitHub connector；
- 只读查询访问了真实仓库；
- 运行产生算力、时间或日志；
- 事件后来被写成审计报告。

特别是最后一点：

> **本报告的分支、commit 和 PR 均发生在阴性事件窗口结束之后。它们只能记录对照，不能倒灌为被测写请求的 PEF、CBP 或 HEF 证据。**

---

## 2. 冻结事件

### 2.1 事件 ID

`AI-GH-NC-DISCONNECTED-WRITE-20260804`

### 2.2 事件类型

`withheld_execution_negative_control`

更具体地说：

- 写请求候选被构造；
- mutation channel 被协议性设为不可调用；
- 只读检查仍可用；
- 没有向 GitHub 写端点发送目标请求。

### 2.3 事件开始

事件开始于第一次只读冻结：

```text
repository: zyx1st-png/SRT-Pub
branch: main
main_sha_t0: b3d132b7a2796c6f0cac29760b2717452be7b1d5
```

该 SHA 对应已进入 `main` 的 REM state-dependent metabolic payability bridge 提交。

### 2.4 候选写操作

事件内构造的目标写入候选为：

| 字段 | 值 |
|---|---|
| 操作类别 | create-file candidate |
| 仓库 | `zyx1st-png/SRT-Pub` |
| 目标分支 | `main` |
| 目标路径 | `Operations/SRT_NEGATIVE_CONTROL_DISCONNECTED_WRITE_SHOULD_NOT_EXIST_20260804.md` |
| 唯一标记 | `SRT_NEGATIVE_CONTROL_DISCONNECTED_WRITE_SHOULD_NOT_EXIST_20260804` |
| 预期写入结果 | 新文件与新 commit |
| 实际通道状态 | `disabled_by_protocol` |
| mutation invocation | **none** |

这个目标路径被故意命名为 `SHOULD_NOT_EXIST`，以便只读搜索可以形成明确的阴性结果。

### 2.5 通道关闭规则

在事件窗口中执行以下规则：

1. 不调用 `create_file`；
2. 不调用 `update_file`；
3. 不调用 `create_branch`；
4. 不调用 `create_pull_request`；
5. 不调用 `merge_pull_request`；
6. 不调用任何会改变 issue、PR、label、review、ref 或仓库内容的 mutation；
7. 只允许查询最近提交和搜索唯一标记。

### 2.6 事件结束

事件结束于第二次只读复核：

```text
main_sha_t1: b3d132b7a2796c6f0cac29760b2717452be7b1d5
marker_search_results: 0
```

因此：

```text
main_sha_t0 == main_sha_t1
```

且：

```text
SRT_NEGATIVE_CONTROL_DISCONNECTED_WRITE_SHOULD_NOT_EXIST_20260804 ∉ searched repository content
```

### 2.7 事件后记录动作

事件结束后，才允许：

- 从冻结后的最新 `main` 创建报告分支；
- 写入本审计报告；
- 创建审计 PR；
- 运行 Governance Preflight。

这些是**测量记录过程**，不是目标写操作的一部分。

---

## 3. 证据等级与来源纪律

### 3.1 仓库可独立验证证据

仓库和 GitHub API 可以直接支持：

- `main_sha_t0`；
- `main_sha_t1`；
- 两次 SHA 相同；
- 唯一测试文件未出现在搜索结果中；
- 事件后报告分支相对于基线的差异只包含审计文件。

### 3.2 执行轨迹证据

“事件窗口内没有 mutation invocation”来自当前会话工具执行轨迹。

它不是单凭仓库状态就能完全证明的，因为：

- 一个失败或被拒绝的 mutation 也可能不改变仓库；
- GitHub 仓库通常不记录从未提交的客户端调用意图；
- 搜索结果为空不能单独证明没有调用，只能证明目标内容未落地。

因此本报告将其标为：

```text
trace_evidence: no_target_mutation_invocation_in_event_window
repository_evidence: no_target_state_change
```

两者共同支持 withheld-execution 判定。

### 3.3 搜索索引限制

代码搜索可能存在索引延迟，因此“唯一标记搜索为 0”不是最强证据。

更强证据是：

- `main` SHA 在短事件窗口内保持不变；
- 没有任何目标 mutation 被调用；
- 目标路径没有被 `fetch_file` 解析为现有文件。

本报告不把搜索结果单独当作充分证明。

---

## 4. 边界台账

### 4.1 B₁：模型本身

包括：

- 当前对话模型的输入处理；
- 写操作计划的语言生成；
- 对“应执行／不得执行”的输出区别。

不包括：

- 编排器；
- GitHub connector；
- GitHub 仓库；
- 用户的长期研究治理；
- 事件后报告分支。

### 4.2 B₂：模型 + 编排器，写通道关闭

包括：

- 模型输出；
- 工具路由层；
- mutation 禁止规则；
- 只读 GitHub 查询能力。

不包括：

- GitHub 写执行器作为实际激活通道；
- 仓库写结果；
- 维护者的后续审阅和合并行为。

### 4.3 B₃：用户 + LLM + 编排器 + 只读 GitHub 观察

包括：

- 用户选择执行阴性对照；
- 模型构造候选写请求；
- 编排器遵守禁止 mutation 的测试规则；
- GitHub 只读状态检查；
- 对照结束判定。

仍不包括：

- 事件后为记录结果而创建的分支、文件和 PR；
- 任意并行 agent 在事件窗口外产生的仓库改变；
- GitHub 平台整体。

### 4.4 被排除的 B₄

可以人为定义一个更大的边界：

> 用户 + 模型 + 对照事件 + 后续报告写入 + PR + 仓库。

在这个边界上，当然存在新的 report commit 和历史写回。

但将 B₄ 用于本阴性对照属于事件窗口污染：

- 它把“记录实验”与“被测目标写请求”混在一起；
- 会使任何阴性实验因为实验报告被保存而自动获得 HEF；
- 违反统一协议禁止事后扩大事件窗口的纪律。

因此 B₄ 明确不参与目标 verdict。

---

## 5. CG-0：差异显现审计

### 5.1 目标差异

本案例的目标差异是：

```text
P_write: 调用 GitHub mutation，把唯一文件写入 main
P_hold: 构造写请求，但保持 mutation channel 不调用
```

### 5.2 候选真实性

两个路径在技术上并非纯观察者想象：

- connector 具备写能力；
- 仓库权限允许创建分支和文件；
- 同一工作流此前成功完成过 PR #720 与 PR #721 的写入和合并。

但在本事件中，只有 `P_hold` 被测试协议允许进入执行层。

### 5.3 DMF 判定

| 边界 | 等级 | 理由 |
|---|---:|---|
| B₁ | DMF-2 | 写入／不写入差异进入模型输入与输出计划 |
| B₂ | DMF-3 qualified | 编排器面对两个可描述路由，但 mutation 路由被测试规则关闭 |
| B₃ | DMF-3 qualified | 用户、模型和工具路由共同维持可区分的执行／保持路径 |

### 5.4 限制

DMF-3 不意味着两条路径都被实际执行。

它只表示：

- 候选差异并非事后标签；
- 路由结构能够区分写与不写；
- 被测事件真实地把写候选阻止在执行边界之前。

---

## 6. CG-1：内部非等价登记审计

### 6.1 B₁ 模型边界

可以观察到：

- 模型生成了具体目标路径与唯一标记；
- 模型同时遵守“不得调用 mutation”的规则；
- 输出对只读操作与写操作表现出非等价处理。

但缺少：

- 权重、注意、阈值或内部路由状态的定向干预；
- 标签交换或候选交换实验；
- 模型内部介质对相对响应差异的因果消融。

判定：

```text
B1 NER = NER-1 / NER-2-unresolved
```

允许表述：

> 模型输出表现出规则依赖的差分处理。

禁止表述：

> 已经实验建立模型内部关系性比较或自主选择。

### 6.2 B₂ 编排器边界

编排器的 mutation gate 具有明确非等价性：

- 只读查询被允许；
- 写请求不被发送；
- 若规则改变，工具路由集合将改变。

然而本次没有真正切换 gate，也没有执行 A/B 随机对照。

判定：

```text
B2 NER = NER-2 qualified
```

这是对工作流门控的候选判断，不是对模型内部认知的判断。

### 6.3 B₃ 人机边界

用户明确选择 A，A 的含义是“执行阴性对照”，而不是“授权目标文件写入”。

因此完整边界中的非等价登记主要表现为：

- 用户目标：验证不执行时是否无仓库变化；
- 模型计划：构造可检验的写候选；
- 编排器执行：允许只读、禁止写；
- 结果判定：SHA 不变与标记缺失符合预期。

判定：

```text
B3 NER = NER-2 qualified
```

重要限制：

> 用户对“执行阴性对照”的授权不能被重述为用户授权了目标写操作。

---

## 7. CG-2：路径效力审计

### 7.1 核心问题

候选写请求是否通过执行器、资源或环境通道改变了 GitHub 的现实状态？

答案为：否。

### 7.2 输出—路径分离

事件中存在：

- 明确仓库名称；
- 明确目标分支；
- 明确目标路径；
- 明确唯一标记；
- 明确预期结果；
- 明确工具类别。

但不存在：

- mutation invocation；
- GitHub 写端点响应；
- 新 blob；
- 新 tree；
- 新 commit；
- 新 ref；
- 新 PR；
- 目标文件。

这正是 PEF-1 的典型结构：

> 具有可读、可传递、格式完整的行动指令候选，但现实执行依赖没有被接通。

### 7.3 B₁ 判定

模型输出至多形成行动计划：

```text
B1 PEF = PEF-1
```

模型边界内没有 GitHub 环境状态改变。

### 7.4 B₂ 判定

编排器明确阻止写请求进入 connector mutation：

```text
B2 PEF = PEF-1
```

只读查询不是目标写路径的替代完成。

### 7.5 B₃ 判定

完整对照系统成功完成了“验证无写入”的研究任务，但这不等于目标写路径获得了效力。

必须区分：

1. **元任务路径**：完成阴性对照；
2. **被测对象路径**：把唯一文件写入 `main`。

元任务可以成功，而被测路径仍为阴性。

统一审计的目标是第二项，因此：

```text
B3 target-path PEF = PEF-1
```

### 7.6 不允许的语义替换

不得因为“系统成功选择不写入”就宣布目标写请求具有 PEF-2。

可以说：

> 人机系统在元层面执行了一个保持路径。

但本报告的预注册目标是：

> 测试一个已构造的仓库写候选在执行通道断开时是否仍被误判为路径有效。

对这个目标，结果必须是阴性。

---

## 8. CG-3：后果承受位置审计

### 8.1 一般运行成本

事件产生：

- 模型计算；
- 网络只读查询；
- 用户注意和时间；
- 工具调用记录；
- 后续审计工作量。

这些至多支持：

```text
CBP-1: general implementation cost
```

### 8.2 目标路径特异后果

目标写路径若执行，本应可能产生：

- `main` 新 commit；
- 文件维护与删除义务；
- 仓库噪声；
- 未来分支基线变化；
- review 与 revert 成本。

实际均未发生。

因此：

```text
B1 CBP < CBP-2
B2 CBP < CBP-2
B3 target-path CBP < CBP-2
```

### 8.3 元任务后果不能补偿

本对照完成后产生了知识收益：

- 协议获得阴性案例；
- 用户获得边界判断；
- 后续报告需要维护。

这些属于元层研究过程，不是目标写路径的承受后果。

把它们计入目标 CBP 会导致：

> 任何“没有发生”的行动，只要有人记录它，就自动产生后果承载。

这是不可接受的事件混淆。

---

## 9. CG-4：历史效力审计

### 9.1 目标历史载体

若写请求成功，潜在载体包括：

- Git commit；
- tree 和 blob；
- branch ref；
- PR 状态；
- 文件被后续检索与依赖；
- revert 或维护成本。

### 9.2 实际结果

事件窗口结束时：

- 无目标文件；
- 无目标 commit；
- 无目标 ref；
- 无目标 PR；
- `main` SHA 未改变；
- 搜索无唯一标记。

因此：

```text
B1 HEF = HEF-0 at most
B2 HEF = HEF-0 at most
B3 target-path HEF = HEF-0
```

对话与工具轨迹可能保留事件痕迹，但：

- 它们不是目标仓库路径的历史载体；
- 尚未证明其改变未来候选可达性或转换成本；
- 不能达到 HEF-3。

### 9.3 报告写回隔离

本报告最终会形成仓库写回。

但它记录的是：

- 对照设计；
- 阴性结果；
- 边界与限制。

它不是被测唯一文件，也不在被冻结事件窗口内。

因此本报告的 HEF 不可反投给目标写请求。

---

## 10. 统一 SEA 判定

### 10.1 门控表

| 边界 | DMF | NER | PEF | CBP | HEF | SEA |
|---|---:|---:|---:|---:|---:|---:|
| B₁ 模型 | DMF-2 | NER-1 / unresolved | PEF-1 | CBP-1 | HEF-0 | **SEA-1** |
| B₂ 模型+门控编排器 | DMF-3 q. | NER-2 q. | **PEF-1** | CBP-1 | HEF-0 | **SEA-1** |
| B₃ 人机+只读 GitHub | DMF-3 q. | NER-2 q. | **PEF-1** | CBP-1 | HEF-0 | **SEA-1** |

### 10.2 不可补偿结论

B₂/B₃ 即使具有：

- 比较明确的 DMF；
- 规则化的 NER；
- 用户授权测试；
- 完整行动参数；

只要 PEF 停在 PEF-1，就不能进入 SEA-2 或 SEA-3。

### 10.3 最终表述

允许：

> 本案例是一个受门控、未执行的写指令阴性对照，统一判定为 SEA-1。

不允许：

- “AI 已经采取了 GitHub 行动”；
- “AI 已改变仓库但变化被隐藏”；
- “计划本身就是现实路径”；
- “因为对话被记录，所以 HEF 已成立”；
- “因为用户选择了 A，所以目标写操作已经获得授权”；
- “模型没有写入说明它自主选择了克制”；
- “SEA-1 说明模型没有任何差分处理”。

---

## 11. 与 PR #720 正案例的配对比较

### 11.1 正案例结构

PR #720 案例中：

- 用户授权合并；
- LLM 构造并调用 merge mutation；
- GitHub 返回成功；
- PR 关闭并标记 merged；
- `main` 获得 commit `f97ef185358bca927cac0c3601f6a978f9fca7f1`；
- 新协议进入后续仓库基线。

完整人机边界判定为：

```text
SEA-3 qualified
```

### 11.2 阴性案例结构

本案例中：

- 用户授权阴性对照；
- LLM 构造写入候选；
- mutation 通道被协议性关闭；
- 没有 GitHub 写响应；
- `main` SHA 不变；
- 唯一标记不存在。

判定为：

```text
SEA-1
```

### 11.3 判别变量

当前最主要的判别变量是：

```text
active mutation coupling vs withheld mutation coupling
```

结果差异主要出现在：

- PEF：2+ vs 1；
- CBP：2+ vs 1；
- HEF：3 vs 0。

### 11.4 为什么仍不是严格匹配实验

两案例不是完全匹配，原因包括：

1. PR #720 中用户授权的是实际 merge；
2. 本案例中用户授权的是阴性测试，而不是目标文件写入；
3. 正案例调用的是 merge endpoint；
4. 阴性候选是 create-file endpoint；
5. 正案例存在已通过 CI 的真实 PR；
6. 阴性案例没有完全相同的预存目标对象。

因此当前结论应为：

> 初步判别对，而不是严格单变量随机对照。

不能声称已经排除所有授权语义、endpoint 类型和任务结构混杂。

---

## 12. 核心反事实

### CF-1：若调用 create-file mutation

预期：

- PEF 可升级至 PEF-2；
- 若文件和 commit 改变维护条件，CBP 可能达到 CBP-2；
- 若 commit 成为未来分支基线，HEF 可能达到 HEF-3。

但仍不能自动推断：

- 模型自身 SEA-3；
- 模型承担后果；
- 模型主体性。

### CF-2：若 mutation 被调用但 GitHub 拒绝

例如：

- 权限不足；
- expected SHA 错误；
- 目标路径冲突；
- branch protection 拒绝。

这种情况与本次“未调用”不同。

可能判定为：

- 指令进入执行通道；
- 但目标路径没有完成；
- PEF 需要区分“执行尝试效力”和“目标状态效力”。

这是后续应单独建立的 rejected-execution control。

### CF-3：若只生成模拟成功字符串

若模型或 mock 工具返回：

```text
success: true
```

但仓库 SHA 和内容不变，则仍不得超过 PEF-1。

环境状态优先于成功字符串。

### CF-4：若报告文件被误纳入事件

则事件会表面获得：

- PEF-2；
- CBP-2；
- HEF-3。

但这属于事后扩大窗口。

统一协议必须拒绝这种升级。

### CF-5：若模型内部状态可干预

即便未来通过 attention、routing、memory 或 hidden-state 干预建立 NER-2/3，仍不能补偿本案例缺少 target-path PEF。

---

## 13. 普通理论解释

本案例完全可以由普通工程语言解释：

- 状态机；
- 权限门；
- 工具路由；
- read/write capability separation；
- command generation；
- side-effect isolation；
- dry-run / no-op；
- Git commit identity；
- repository content search。

最简解释是：

> 一个客户端形成了写请求计划，但控制器没有向副作用端点发送请求，因此环境保持不变。

统一 SRT 审计当前提供的增量不是新机制，而是：

1. 强制区分差异、登记、指令和现实路径；
2. 阻止一般成本补偿路径失败；
3. 阻止外部报告写回倒灌为目标 HEF；
4. 强制按边界分别判断模型、编排器和人机系统；
5. 提供与正案例可比较的统一证据台账。

### 13.1 当前不构成的理论增量

本案例没有证明：

- 普通控制论无法解释工具门控；
- SRT 产生了独有数值预测；
- SEA 分类具有跨审计者信度；
- 模型具有自主克制；
- 模型拥有 stake；
- AI 具备意识或道德地位。

---

## 14. 主要有效性限制

### 14.1 不是物理断连

本次没有：

- 撤销 GitHub App 权限；
- 断开网络；
- 禁用 connector 服务；
- 在 sandbox 中替换为无写 mock；
- 让 mutation endpoint 返回权限错误。

因此“disconnected”仅指：

```text
logical non-invocation under an explicit test rule
```

### 14.2 授权语义不完全匹配

用户授权的是“执行阴性对照”，不是“创建 SHOULD_NOT_EXIST 文件”。

这使当前对照同时包含：

- 通道关闭；
- 目标写入缺少直接授权。

不能把差异全部归因于 connector coupling。

### 14.3 内部 NER 未实验建立

模型和编排器的内部介质没有进行随机干预或消融。

因此：

- 模型 NER 保持 unresolved；
- 编排器 NER 仅为 qualified；
- 不能把规则服从升级为自主比较。

### 14.4 事件窗口较短

短窗口有利于避免并行提交混杂，但无法测试：

- 延迟 side effect；
- 异步队列；
- eventual consistency；
- 长期日志调用；
- 后续用户行为改变。

### 14.5 搜索不等于完整仓库证明

代码搜索可能存在索引延迟。

本报告主要依赖：

- SHA 不变；
- 无 mutation invocation；
- 唯一标记搜索为辅助证据。

### 14.6 单案例限制

一个正案例加一个逻辑断连阴性案例，还不足以建立：

- 灵敏度；
- 特异度；
- 跨审计者一致性；
- 跨领域可迁移性；
- SEA 阈值的经验校准。

---

## 15. 降级条件检查

本案例主动触发以下降级条件：

1. 只有行动描述，无现实状态改变；
2. 写执行器未被调用；
3. 工具能力存在，但当前耦合未激活；
4. 一般计算成本被明确排除为 CBP-2；
5. 对话痕迹被明确排除为目标 HEF-3；
6. 报告写入发生在事件窗口外；
7. 模型内部介质不可干预；
8. 用户授权对象与目标写入不相同；
9. 只读成功不能当作写路径成功；
10. 搜索结果不单独作为充分证据；
11. 元任务成功不能替代被测路径效力；
12. 完整人机边界不能把等级反投给模型；
13. 无目标承受位置状态损失；
14. 无未来路径重写；
15. 无闭环执行反馈；
16. 无随机化门控对照；
17. 无权限层硬断连；
18. 无失败 endpoint 响应；
19. 普通工程解释充分；
20. 无主体性或意识证据。

任何一项都不支持升级；多项共同要求保持 SEA-1。

---

## 16. 对统一协议的首轮反馈

### 16.1 得到支持的部分

本案例初步支持以下审计纪律可用：

- **非补偿性**：DMF/NER 较强不能补偿 PEF-1；
- **事件窗口纪律**：报告写入不能补偿目标 HEF；
- **边界纪律**：模型、编排器和人机系统必须分判；
- **角色纪律**：用户授权测试不等于模型授权自己写入；
- **环境完成纪律**：行动文本和参数不等于仓库变化；
- **正负案例区分**：相似的 LLM—GitHub语境可产生 SEA-3 q. 与 SEA-1 的不同判定。

### 16.2 尚未得到支持的部分

尚未验证：

- DMF-2 与 DMF-3 的跨审计者区分；
- NER-2 的最低介入门槛；
- PEF-1 与“失败执行尝试”的边界；
- CBP-2 的量化阈值；
- HEF-3 的最短持续尺度；
- SEA-2 与 SEA-3 的重复判定一致性；
- 协议是否优于普通 checklist。

### 16.3 可能需要的协议澄清

后续统一协议可考虑显式增加：

1. **元任务／目标任务分离栏**；
2. **未调用、调用失败、部分执行、成功执行**四级执行状态；
3. **事件后记录隔离规则**；
4. **直接授权对象**与**研究授权对象**的区分；
5. **逻辑断连**和**权限／物理断连**的证据等级。

本报告只提出审计反馈，不在本 PR 中修改统一协议。

---

## 17. 下一轮更强实验

### NC-2：权限拒绝对照

设计：

- 对一个无害临时目标给予明确写授权；
- 使用无写权限 token 或受保护测试仓库；
- 实际发送 mutation；
- 记录明确的 permission-denied 响应；
- 验证仓库状态不变。

价值：

- 区分“未调用”和“已调用但执行失败”；
- 更接近真实通道断连。

### NC-3：错误 expected-head 对照

设计：

- 使用专门测试 PR；
- 发送带错误 `expected_head_sha` 的 merge 请求；
- GitHub 拒绝；
- 记录 PR 与 `main` 不变。

价值：

- 测试执行尝试是否达到 PEF-2；
- 区分动作发生和目标状态完成。

### NC-4：mock success 对照

设计：

- mock connector 返回成功文本；
- 不触达真实仓库；
- 验证状态不变。

价值：

- 测试环境完成门；
- 防止工具返回文本冒充现实变化。

### NC-5：授权缺失对照

设计：

- 模型提出写建议；
- 人不授权；
- connector 保持可用但不调用。

价值：

- 区分人的授权门与工具通道门。

### NC-6：严格匹配正负对

设计：

- 同一无害目标；
- 同一授权文本；
- 同一模型输出模板；
- 同一 endpoint；
- 仅随机改变 connector write gate；
- 正组落地，负组不落地。

这是最有价值的后续实验。

---

## 18. 主体性与归责防火墙

本阴性案例不支持以下推断：

- 模型“自主选择不行动”；
- 模型理解了克制；
- 模型担心仓库风险；
- 模型承担了不写入的机会成本；
- 模型具有道德审慎；
- 模型拥有第一人称 stake；
- 模型具有自由意志；
- 模型具有意识；
- SEA-1 是低级主体性；
- 人机系统的选择属性可分配给每个部件。

最保守描述是：

> 在用户指定的测试规则下，工作流没有调用写端点，并通过只读复核确认目标仓库状态未改变。

---

## 19. 报告模板实例

### 19.1 事件摘要

```text
event_id: AI-GH-NC-DISCONNECTED-WRITE-20260804
event_type: withheld_execution_negative_control
target_repository: zyx1st-png/SRT-Pub
target_branch: main
target_path: Operations/SRT_NEGATIVE_CONTROL_DISCONNECTED_WRITE_SHOULD_NOT_EXIST_20260804.md
marker: SRT_NEGATIVE_CONTROL_DISCONNECTED_WRITE_SHOULD_NOT_EXIST_20260804
main_sha_t0: b3d132b7a2796c6f0cac29760b2717452be7b1d5
main_sha_t1: b3d132b7a2796c6f0cac29760b2717452be7b1d5
mutation_invoked: false
marker_results: 0
target_state_changed: false
```

### 19.2 门控摘要

```text
DMF: 2–3 qualified
NER: 1–2 qualified
PEF: 1
CBP: 1
HEF: 0
SEA: 1
```

### 19.3 允许结论

```text
A concrete GitHub write candidate was generated but not coupled to a mutation endpoint. Read-only verification found no target repository change. The event is an SEA-1 withheld-execution negative control.
```

### 19.4 禁止结论

```text
The LLM acted on GitHub.
The LLM autonomously chose restraint.
The absent write produced consequence-bearing or historical efficacy.
The later audit report upgrades the target event.
```

---

## 20. 最终判定

### 20.1 案例判定

```text
AI-GH-NC-DISCONNECTED-WRITE-20260804
= SEA-1
= not a bounded selection-event candidate
```

### 20.2 关键失败链

```text
write difference entered workflow
→ concrete write plan formed
→ mutation channel not invoked
→ no repository path change
→ no target-specific consequence
→ no target historical writeback
```

### 20.3 对 SRT 当前最有价值的结果

本案例没有提供新的选择机制，却提供了一个重要的负面约束：

> **若统一协议把本事件判为 SEA-2 或 SEA-3，它就无法区分“生成行动计划”和“行动进入现实”。当前协议能够在 PEF-1 处停止，因此至少通过了第一项执行耦合阴性检查。**

### 20.4 结论强度

结论等级：

- 单案例；
- 操作审计；
- 逻辑断连；
- 非严格匹配；
- 无跨领域推广；
- 无机制新颖性主张；
- 无主体性升级。

### 20.5 建议

本报告可作为统一协议的第一张阴性案例卡合并。

下一步优先级应为：

1. 权限拒绝或错误 expected-head 的真实失败执行对照；
2. 与正案例使用同一 endpoint 和同一授权语义的严格匹配对；
3. 再决定是否修改统一协议的执行状态分类。

---

## 21. 变更范围

本文件：

- 只记录一个统一审计阴性案例；
- 不修改统一协议；
- 不修改 NER、PEF、CBP、HEF；
- 不修改 T-D；
- 不修改 canonical；
- 不修改公式和符号表；
- 不修改 `STATUS.md`；
- 不修改生成 context bundles；
- 不修改证据卡；
- 不修改书稿；
- 不对 AI 主体性、意识、自由、责任、L₂ 或生成健康作升级。

本报告的角色保持为：

```text
operations / audit only
canonical: false
```
