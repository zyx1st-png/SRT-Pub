# HEARTBEAT.md
# SRT Openclaw 心跳任务清单
#
# 每次心跳时按以下顺序检查，读取 memory/heartbeat-state.json 确认是否需要运行。
# 若所有任务均已在今日执行，输出 HEARTBEAT_OK。

## 每日检查（Daily）

读取 memory/heartbeat-state.json，检查以下字段：

### Pipeline 6 — 每日内部审查
- 条件：`pipeline6_last` 距当前 ≥ 22 小时
- 动作：执行 SRT/每日自动内审（见 SRT/_SRT_DAILY_REVIEW_PIPELINE.md）
- 完成后：更新 `pipeline6_last` 为当前时间戳

### Pipeline 3 — 网络信号采集
- 条件：`pipeline3_last` 距当前 ≥ 22 小时
- 动作：采集 Scholar/Reddit/Twitter/X 信号并按 6 项审核门分类
- 完成后：更新 `pipeline3_last` 为当前时间戳，写入 `_SRT_SIGNAL_LOG.md`

### Pipeline 5 — 双路线媒体选题
- 条件：`pipeline5_last` 距当前 ≥ 22 小时（或当日 `_SRT_MEDIA_QUEUE.md` 无新条目）
- 动作：生成大众路线 + 精英路线各 1 条选题
- 完成后：更新 `pipeline5_last` 为当前时间戳，写入 `_SRT_MEDIA_QUEUE.md`

---

## 每周检查（Weekly，周一 or 首次心跳）

读取 memory/heartbeat-state.json，检查 `paper_pipeline_week` 是否为本周 ISO 周号：

### Pipeline 4 — 文档治理 + 理论方向评审
- 条件：本周未执行（`pipeline4_last` 在本周之前）
- 动作：提醒用户本周 Pipeline 4 待执行（需用户确认后执行，不自动完成）
- 说明：有语义变更风险，不完全自动化

### Pipeline 2 — 论文候选更新
- 条件：`paper_pipeline_week` 不是当前 ISO 周号
- 动作：提醒用户本周论文候选池待更新（需用户确认后执行）
- 说明：等待用户发送 `论文候选` 触发

---

## 状态跟踪文件路径

`/Users/zhangyuxin/.openclaw/workspace/memory/heartbeat-state.json`

初始结构：
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

## 时间要求

- 日常心跳任务（Pipeline 3/5/6）：容忍时间漂移（22h 窗口），不需精确时间
- 精确时间任务（Pipeline 5 每日 08:00 生成）：建议同时配置 Cron：
  `0 8 * * * cd /Users/zhangyuxin/.openclaw/workspace/SRT && uv run python scripts/srt_media_topic_daily.py`

---

## 安静时段

- 23:00–08:00（Asia/Shanghai）：仅在有紧急事项时打扰，其余保持 HEARTBEAT_OK
