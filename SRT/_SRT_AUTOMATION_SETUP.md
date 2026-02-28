---
id: SRT-AUTOMATION-SETUP
type: framework
tags: [Automation, Schedule, Ops]
status: active_v1
dependency: [_SRT_OPERATIONS_SCHEDULE, _SRT_MEDIA_PIPELINE]
---

# SRT 自动化执行设置

## 目标
稳定执行“每日 08:00 自动生成 1 个媒体策划主题（不成文、不外发）”。

## 方案 A：Cron（推荐，时间最稳定）

### 示例（macOS/Linux）
```bash
# 编辑 crontab
crontab -e
```
添加：
```cron
0 8 * * * cd /Users/zhangyuxin/.openclaw/workspace && python3 scripts/srt_media_topic_daily.py >> /tmp/srt_media_topic_daily.log 2>&1
```

说明：
- 每天 08:00 执行。
- 仅向 `SRT/_SRT_MEDIA_QUEUE.md` 追加策划条目。

## 方案 B：Heartbeat（上下文感知更强）

在 heartbeat 回合中触发脚本：
```bash
python3 scripts/srt_media_topic_daily.py
```

建议增加防重复门：
- 若当天已生成过主题（检查队列中的日期标记），则跳过。

## 运行后验收

1. 检查队列是否新增当天条目：
- `SRT/_SRT_MEDIA_QUEUE.md`
2. 运行质量检查：
```bash
./scripts/run_srt_checks.sh
```

## 故障处理

- 脚本执行失败：查看 `/tmp/srt_media_topic_daily.log`
- 队列写入冲突：先备份队列再重跑
- 若内容重复：人工删除重复项并记录到变更日志
