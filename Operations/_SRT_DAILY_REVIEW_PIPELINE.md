---
id: SRT-DAILY-REVIEW-PIPELINE
type: framework
tags: [DailyReview, AutoFix, QualityGate, Pipeline6]
status: active_v1
layer: meta
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-EXECUTION-PLAN, SRT-REVIEW-QUEUE, SRT-D-VALUE-CANONICAL, SRT-EQ-HYP-MAP]
---

# SRT 每日自动内部审查流水线（Pipeline 6）

> **目标**：每日自动扫描 SRT KB，将发现的问题按严重程度分流——小问题自动修复并提交，大问题写入待审队列等待人工决策。
>
> **触发方式**：HEARTBEAT 自动触发（距上次运行 ≥ 22 小时）或手动触发（用户发送 `内审`）

---

## §1 自动修复范围（直接执行，无需人工确认）

以下问题由 agent 自动修复后直接 `git commit`：

### 1.1 Frontmatter 规范
- 缺少 `status` 字段 → 补填 `status: draft`
- 缺少 `tags` 字段 → 补填空数组 `tags: []`
- `id` 字段缺失 → 根据文件名生成标准 ID（`SRT-DOMAIN-BASENAME`）

### 1.2 符号一致性
基于 `_SRT_SYMBOL_TABLE.md` 的权威表，修复以下已记录的不一致：
- `Ĝθ` → `Ĝ_θ`（缺下划线）
- `Ψf` → `Ψ_f`（缺下划线）
- `L0 / L1 / L2` → `L₀ / L₁ / L₂`（补下标）
- `d-value` 的单数/复数混用 → 统一为 `d-value`

### 1.3 结构冗余
- 同一文件中完全相同的段落标题（相邻出现）→ 删除重复项
- 连续空行超过 3 行 → 压缩为 2 行

### 1.4 引用完整性
- `dependency:` 字段中列出的文件不存在于 `_SRT_MANIFEST.yaml` → 追加注册

---

## §2 标记并写入 `Operations/_SRT_REVIEW_QUEUE.md` 的范围

以下问题**不自动修复**，仅标记记录：

### 2.1 实验映射缺口
- `_SRT_EQ_HYP_MAP.md` 中 `status: gap` 的条目（每次检查是否有新增或状态变化）

### 2.2 占位内容检测
搜索以下模式，定位文件和行号：
- `[待填写]`、`[TODO]`、`[待补充]`、`[占位]`、`TBD`

### 2.3 d-value 定义偏离
- 包含 `d ≡`、`d =`、`d-value 定义` 的段落
- 检查是否引用了 `_SRT_D_VALUE_CANONICAL.md`
- 未引用则标记为 Medium 优先级

### 2.4 跨文件语义不一致（关键词比对）
以下概念在不同文件中的描述如果出现方向性矛盾（一个说"A意味着B"，另一个说"A意味着非B"）：
- `L₂` 的定义方式
- `Ψ_f` 的方向性（摩擦/成本的正负）
- 意识涌现的条件（三条件 vs 其他）

### 2.5 Part B 完整性
- 检查 `Core/SRT_Core_01_Axioms.md` 各公理的 Part B 段落是否包含 5 节结构（历史/数学/实验/对话/边界）
- 缺少任一节 → 标记为 Low 优先级（已有内容但结构不完整）

---

## §3 执行流程

```
1. 读取 heartbeat-state.json → 检查 pipeline6_last
2. 若距上次 < 22h → 跳过，输出 "PIPELINE6_SKIP"
3. 若距上次 ≥ 22h 或手动触发：
   a. 运行 §1 检查项 → 收集修复列表
   b. 运行 §2 检查项 → 收集待审列表
   c. 执行 §1 修复（直接编辑文件）
   d. 追加 §2 待审项到 Operations/_SRT_REVIEW_QUEUE.md
   e. 追加本次运行摘要到 Operations/_SRT_DAILY_REVIEW_LOG.md
   f. git commit（若有修复）
   g. 更新 heartbeat-state.json 的 pipeline6_last
```

---

## §4 输出规范

### git commit 格式
```
fix(daily-review): auto-fix YYYY-MM-DD [N items]
```

### `Operations/_SRT_DAILY_REVIEW_LOG.md` 追加格式
```
## YYYY-MM-DD HH:mm
自动修复：N 项（frontmatter: A, 符号: B, 冗余: C, 引用: D）
写入队列：M 项（实验映射: A, 占位: B, d-value: C, 语义: D, PartB: E）
```

---

## §5 自动修复阈值（不修改的边界）

以下情况即使检测到问题也**不自动修复**，仅记录：
- 语义变更（任何改变命题含义的修改）
- 删除 20 字以上的段落内容
- 跨文件的内容迁移
- 涉及 `Core_Law/` 目录下文件的任何修改

---

## 【边界声明】
1. Pipeline 6 的自动修复仅覆盖格式层，不修改理论内容。
2. `Operations/_SRT_REVIEW_QUEUE.md` 中的标记是建议性的，人工处理时可以判断为误报并标注 `[FALSE_POSITIVE]`。
3. 每日审查不替代 Pipeline 4（每周治理），二者互补：前者侧重自动化格式，后者侧重人工理论方向判断。
