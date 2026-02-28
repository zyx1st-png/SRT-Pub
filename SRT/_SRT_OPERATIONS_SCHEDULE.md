---
id: SRT-OPERATIONS-SCHEDULE
type: framework
tags: [Schedule, Cadence, Ops]
status: active_v1
dependency: [_SRT_EXECUTION_PLAN]
---

# SRT 运行节奏（Cadence）

- Daily:
  - Pipeline 1 材料融合（先审后入正文）
- Every 3 days:
  - Pipeline 3 情报采集与审核
- Weekly:
  - Pipeline 2 论文候选池与主稿迭代
  - Pipeline 4 文档治理巡检
- Daily at 08:00 (Asia/Shanghai):
  - Pipeline 5 自动生成 1 个策划主题（仅选题/方向/原因/内部关联整理）并写入媒体队列
- Biweekly:
  - Release Note 更新与质量回顾
