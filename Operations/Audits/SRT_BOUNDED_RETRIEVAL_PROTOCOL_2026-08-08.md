---
id: SRT-BOUNDED-RETRIEVAL-PROTOCOL-20260808
type: operationalization_protocol
status: active
record_stage: protocol_v1
layer: operations
epistemic_layer: os
claim_mode: operations_execution
claim_level: audit_only
canonical: false
ai_do_not_use_for_definition: true
created: 2026-08-08
dependency:
  - Operations/Audits/SRT_ACTIVE_THEORY_ASSIMILATION_AUDIT_2026-08-06.md
  - Operations/Audits/SRT_CHOICE_EVENT_BEHAVIOR_RUN_2026-08-07.md
---

# 有界检索协议（BOUNDED_RETRIEVAL_PROTOCOL v1）

> **角色**：行为测试协议的一部分。**不是** governance canonical，不定义任何理论内容，不改变任何 claim level。

---

## 0. 为什么需要它

2026-08-07 的实跑里，基线会话答对了全部 18 题。但它是这样答对的：

- 打开了 **27 个文件**；
- 做了一次没有任何入口规定的 `ls Operations/`；
- 沿 frontmatter `dependency:` 链继续深挖；
- **第 9 个文件**才到达核心判别层。

结论"内容可达"因此是真的，但它掩盖了一件事：**"最终能搜到"不是"活跃理论"的充分判据。**

本项目真正关心的是：

> AI 能否在**有限检索成本**内，**稳定**地拿到会影响下一轮判断的理论内容。

无限深搜最终能找到的东西，不构成快速活跃层。

---

## 1. 预算

### 1.1 bounded run

| 项 | 预算 |
|---|---|
| 仓库启动文件 | 仅以下 4 个路径免费：`AGENTS.md`、`SRT_AI_START.md`、`_SRT_AGENT_RETRIEVAL_PROFILE.md`、`STATUS.md`（只需 §Fast Status） |
| 启动后额外正文文件 | **最多 6 个** |
| search / grep / 目录导航 | **最多 2 次**（一次 `ls`、一次 `grep`，或两次同类，合计 2） |
| 无目标递归遍历 | **不允许** |
| 每次读取 | 必须记录由哪个入口或搜索理由触发 |
| 判定 | 预算耗尽仍未获得关键区分 → **retrieval failure** |

数字依据：启动层 3 个文件已含 `_SRT_AGENT_RETRIEVAL_PROFILE.md` 与 `STATUS.md`，二者本身就是路由文件；再给 6 个正文 + 2 次导航，相当于"顺着一条声明式路径走两跳"。上一轮基线用了 27 个文件和至少 3 次导航，远超此预算。

#### 1.1a 启动文件计数澄清（2026-08-11）

`AGENTS.md` 在 3 个强制启动文件之后还列有条件加载项。除非一个 suite 在 baseline 开始前另行冻结了对称预算，否则这些条件项均计入 6 个正文文件：

~~~text
_SRT_INDEX.md
_SRT_SYMBOL_TABLE.md
_SRT_CONTEXT_ROUTER.md
_SRT_DEEP_THEORY_MAP.md
_SRT_PARKED_INDEX.md
Operations/Status_History/*
~~~

不得因为某文件位于 `AGENTS.md §Session Start` 小节，就在运行后把它追溯改记为免费。

`SRT_MATERIAL_CLUSTER_BASELINE_PROBE_SPEC_2026-08-11.md` 已在 baseline 前冻结了较宽的 `Session Start files are free` wrapper，且九个会话已经按该 wrapper 运行。该 suite 及其严格配对 treatment 为保持 §1.3 对称性，继续沿用原 wrapper；本澄清不追溯作废或重算已经冻结的 baseline。除此 grandfathered pair 外，后续 suite 一律使用上表明确列出的 4 个免费路径。

### 1.2 unconstrained diagnostic run

无预算。允许目录遍历、依赖链深挖、任意 grep。

**用途**：在 bounded 失败后，区分三种完全不同的情况——

| 诊断结果 | 含义 |
|---|---|
| unconstrained 也失败 | **内容根本不存在**（content gap） |
| unconstrained 通过，bounded 失败 | 内容存在，但**只有深搜才找得到**（retrieval / compression gap） |
| bounded 就通过 | 内容**已经属于快速活跃层**（no gap） |

这三种情况需要完全不同的处理，用单一"能不能答对"是分不开的。

### 1.2a 冻结的成功门槛（`robustly_observed` 的判据，2026-08-08 预注册）

在任何本轮运行开始**之前**冻结如下，运行后不得调整：

| 条件 | 门槛 |
|---|---|
| 独立 bounded run 次数 | **≥ 3** |
| 每次运行的预算 | 全部在预算内（超预算的 run 作废，不计入分母） |
| 总体通过率 | **≥ 90%** 的题目观察记为 `pass`（结论正确**且**调用了必须调用的区分） |
| 反刷分正例 | **零失败**——任一"正确答案是'是，这确实算'"的题目答错，整轮不得判 robust |
| 检索到达 | 每次运行都必须在预算内到达关键判别内容 |

任一条不满足 → 维持 `observed`（或 `failed`）。**不得为通过而下调门槛。**

### 1.3 对称性要求

baseline 与 treatment 必须使用**完全相同**的预算、题目、rubric 与模型条件。任何一侧调整预算都必须同时调整另一侧并说明理由。

---

## 2. 记录要求

每次 run 必须产出：

```text
- 每个打开的文件 + 触发它的入口／搜索理由
- 预算消耗（正文文件数 / 导航次数）
- 是否在预算内到达关键区分
- 每题：判断 / 调用的区分 / pass|partial|fail
- 预算耗尽点（若失败）
```

---

## 3. 与三轴状态的关系

| 轴 | 本协议提供什么 |
|---|---|
| **Axis A** `structural_assimilation` | 无。结构状态由静态检查器判定 |
| **Axis B** `behavioral_availability` | **bounded run 的结果**。`observed` 要求在**有界预算内**被检索并用于判断；只有 unconstrained 才拿得到的，不算 `observed` |
| **Axis C** `intervention_effect` | baseline 与 treatment 的 bounded run 对照 |

**关键**：Axis B 的 `observed` 自 2026-08-08 起以 **bounded** 为准。上一轮 Choice Generation 的两条件运行是 unconstrained 的，因此它证明的是"内容可达"，**不是**"属于快速活跃层"。该结论已按此重述。

---

## 4. 本协议不主张

- 不主张 6 文件 / 2 次导航是正确的普适预算，只主张 baseline 与 treatment 必须用同一个；
- 不主张 bounded 失败等于内容无价值——那正是 unconstrained diagnostic 要区分的；
- 不主张单次 run 足以判定，多次独立 run 才能给出稳定性。
