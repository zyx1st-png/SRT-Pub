---
id: SRT-OPERATIONS-SCHEDULE
type: framework
tags: [Schedule, Cadence, Ops]
status: active_v2
layer: meta
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-EXECUTION-PLAN, SRT-HEARTBEAT]
---

# SRT 运行节奏（Cadence）

> **版本 v2.3（2026-04-10）**：保留 6 条 Pipeline 节奏；恢复原 Pipeline 1，并新增独立的“材料第二轮结构裁决工作流”作为辅助流程；A 类材料回写默认追加一轮“去材料化改写”，正文目标为原生章节而非材料补丁口吻。

---

## 每日任务（Daily）

| Pipeline | 任务 | 触发方式 | 交付物 |
|---------|------|---------|-------|
| Pipeline 1 | 材料融合（双向增益版：等待用户提交，提交后立即审查并双向整合；A 类默认原生化回写） | 用户指令或文件提交 | `Operations/_SRT_MATERIAL_LOG.md` 新记录 |
| Pipeline 3 | 网络信号采集与审核 | HEARTBEAT（≥22h 自动触发）或 `信号采集` | `Operations/_SRT_SIGNAL_LOG.md` 新记录 |
| Pipeline 5 | 双路线媒体选题（大众+精英各 1 条） | Cron 08:00 / HEARTBEAT / `选题` | `Operations/_SRT_MEDIA_QUEUE.md` 新增 2 条 |
| Pipeline 6 | 每日自动内部审查 | HEARTBEAT（≥22h 自动触发）或 `内审` | 自动修复 + `Operations/_SRT_REVIEW_QUEUE.md` + `Operations/_SRT_DAILY_REVIEW_LOG.md` |

---

## 每周任务（Weekly，建议周一执行）

| Pipeline | 任务 | 触发方式 | 交付物 |
|---------|------|---------|-------|
| Pipeline 2 | 论文候选池更新 + 期刊匹配评分 | HEARTBEAT 提醒 / `论文候选` | `Operations/_SRT_PAPER_CANDIDATES.md` 更新 |
| Pipeline 4 | 文档治理审查 + 理论方向评审 | HEARTBEAT 提醒 / `周评` | `Governance/_SRT_QUALITY_SCORECARD.md` + `Governance/_SRT_WEEKLY_THEORY_REVIEW.md` 新增条目 |

---

## 每两周任务（Biweekly）

| 任务 | 触发方式 | 交付物 |
|-----|---------|-------|
| Release Note 更新与质量回顾 | Pipeline 4 扩展 | `Governance/_SRT_CHANGELOG_2026.md` 新增条目 |
| 论文主稿迭代就绪评估 | Pipeline 2 扩展 | `Operations/_SRT_PAPER_SUBMISSION_CHECKLIST.md` 更新 |

---

## Heartbeat 状态跟踪

所有自动触发任务通过 `memory/heartbeat-state.json` 防止重复执行：

```json
{
  "pipeline3_last": 0,
  "pipeline4_last": 0,
  "pipeline5_last": 0,
  "pipeline6_last": 0,
  "paper_pipeline_week": ""
}
```

---

## 手动触发词汇表

| 触发词 | 对应 Pipeline | 动作 |
|--------|-------------|------|
| `材料 <内容/URL/文件>` | Pipeline 1 | 审查并双向整合外部材料 |
| `信号采集` | Pipeline 3 | 立即执行网络信号采集 |
| `内审` | Pipeline 6 | 立即执行每日内部审查 |
| `选题` | Pipeline 5 | 生成当日双路线选题 |
| `论文候选` | Pipeline 2 | 更新候选池与期刊匹配 |
| `周评` | Pipeline 4 | 执行文档治理 + 理论方向评审 |
| `对话` | 对话工作流 | 启动自我修补对齐模式 |
| `学者对话` | 学者对话工作流 | 启动学者批判模式 |

## 辅助工作流（On Demand）

| 工作流 | 任务 | 触发方式 | 交付物 |
|------|------|---------|-------|
| 材料第二轮结构裁决 | 审查第一轮扩建输出，压成最小可承重命题，并给出 A/B/C 建议、文件落点与去材料化主句 | `材料裁决 <内容/URL/文件>` / `二轮裁决 <内容/URL/文件>` | `Operations/_SRT_MATERIAL_ADJUDICATION_WORKFLOW.md` 规定的裁决输出；必要时再回注 Pipeline 1 |
