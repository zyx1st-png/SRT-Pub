---
id: SRT-OPERATIONS-README
type: index
tags: [Operations, Pipeline, Workflow]
status: active_v1
layer: meta
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-STATUS]
---

# SRT Operations Hub

这里集中放置 SRT 的运行层文档：

- 每日内审 pipeline 与日志
- 信号采集 pipeline 与日志
- 媒体选题 pipeline 与队列
- 论文 pipeline、候选池、活跃草稿、投稿清单
- 材料台账、待审队列、自动化配置

## Authority Boundary

`Operations/` 是 **runtime layer**，不是 canonical theory layer。

使用原则：

- 用它追溯执行节奏、日志、队列与流程状态
- 不用它替代理论主文、canonical 定义或符号规范
- 若与 `CANONICAL_REGISTRY.md` 或 canonical 文件冲突，以后者为准

raw session / dialogue compilation / residual archives 已下沉到：

- `Archive/raw_sessions/`

推荐阅读顺序：
1. `_SRT_OPERATIONS_SCHEDULE.md`
2. `_SRT_DAILY_REVIEW_PIPELINE.md`
3. `_SRT_SIGNAL_PIPELINE.md`
4. `_SRT_PAPER_PIPELINE.md`
5. `_SRT_MEDIA_PIPELINE.md`
6. `_SRT_KNOWLEDGE_REVIEW_PIPELINE.md`（Pipeline 7：知识点抽查与回写）
7. `_SRT_MATERIAL_ADJUDICATION_WORKFLOW.md`（材料第二轮结构裁决；辅助工作流，不属于 6 条主流水线）
