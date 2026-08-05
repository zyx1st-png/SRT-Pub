---
id: SRT-DAILY-REVIEW-PIPELINE
type: framework
status: active
claim_mode: governance
updated: 2026-08-05
version: v2
layer: meta
epistemic_layer: os
dependency: [SRT-EXECUTION-PLAN, SRT-REVIEW-QUEUE, SRT-D-VALUE-CANONICAL, SRT-EQ-HYP-MAP]
---

# SRT 每日自动内部审查流水线（Pipeline 6）

> **目标**：每日扫描 SRT KB，将格式层小问题自动修复，将语义／理论层发现写入“自动扫描待分类”，等待人工分类；自动扫描不得直接生成作者裁决或 canonical 废止结论。
>
> **触发方式**：HEARTBEAT 自动触发（距上次运行 ≥ 22 小时）或手动触发（用户发送 `内审`）。

---

## §1 自动修复范围

以下问题可自动修复后提交：

### 1.1 Frontmatter 最小字段

- 新建或本次实质修改文件缺 `status` → 补 `status: draft`；
- 缺 `id`、`claim_mode` 或 `updated` → 仅在能从当前 owner / workflow 明确判断时补；
- 不自动扩展 `type`、`status`、`claim_mode` 枚举。

### 1.2 符号与格式

- 只修 `_SRT_SYMBOL_TABLE.md` 已明确规定、且不改变语义的拼写／格式偏差；
- 连续空行、相邻重复标题等纯格式问题可修；
- 不自动重写理论术语或跨文件迁移内容。

### 1.3 引用与路径

- 仅修可验证的断链、移动路径和明显导航错误；
- 不因 dependency 未注册而自动修改 manifest 或 registry；该类发现进入待分类区。

---

## §2 仅扫描、不自动裁决的范围

- `_SRT_EQ_HYP_MAP.md` 中 gap / partial 状态变化；
- 占位模式与可能误报；
- d-value 定义段是否缺 canonical 引用；
- 跨文件语义冲突；
- `Core/SRT_Core_01_Axioms.md` Part B 结构完整性；
- owner、入口、claim level、canonical 状态或 supersession 问题；
- 需要作者选择的符号、变量、理论落点和论文方向。

这些发现只能进入 `Operations/_SRT_REVIEW_QUEUE.md §C 自动扫描待分类`。

---

## §3 自动扫描写入格式

```markdown
| 扫描日期 | 来源文件 | 原始发现 | 检查类别 | 建议严重度 | 分类状态 |
|---|---|---|---|---|---|
| YYYY-MM-DD | `path` | 只描述观察到的事实，不给作者结论 | frontmatter / path / mapping / semantic / PartB / owner | Low / Med / High-suggested | Unclassified |
```

规则：

- 不直接写入作者裁决区；
- 不使用 `Resolved`、`Superseded`、`canonical` 等结论词，除非有明确上游裁决可引用；
- 建议严重度不是正式优先级；
- 人工分类后才移动到作者裁决、触发式延期或已处理区。

---

## §4 执行流程

```text
1. 读取 heartbeat-state.json，检查 pipeline6_last；
2. 若距上次 < 22h，输出 PIPELINE6_SKIP；
3. 运行自动修复检查与语义扫描；
4. 对 §1 纯格式项执行修复；
5. 将 §2 原始发现追加到 _SRT_REVIEW_QUEUE.md §C；
6. 将运行摘要追加到 _SRT_DAILY_REVIEW_LOG.md；
7. 只有存在实际文件修复或新扫描记录时才提交；
8. 更新 pipeline6_last。
```

---

## §5 输出规范

### commit

```text
fix(daily-review): auto-fix YYYY-MM-DD [N items]
```

### 日志

```text
## YYYY-MM-DD HH:mm
自动修复：N 项
自动扫描待分类：M 项（按类别汇总）
未执行语义裁决：K 项
```

---

## §6 不自动修改的边界

- 任何命题含义变化；
- 删除或迁移实质正文；
- `Core_Law/`、canonical registry、symbol table 的语义修改；
- owner 废止、入口升格、claim-level 变化；
- 作者裁决项；
- 论文主张、书稿正文和实验结论。

## 边界声明

1. Pipeline 6 是扫描与格式修复工具，不是理论评审者；
2. 自动扫描发现必须经过人工分类；
3. 每日审查不替代 Pipeline 4 周评；
4. 误报可在人工分类时标记并转入已处理区。
