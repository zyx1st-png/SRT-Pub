---
id: SRT-AUTOMATION-SETUP
type: framework
tags: [Automation, Schedule, Ops]
status: active_v1
layer: meta
epistemic_layer: os
claim_mode: canonical
dependency: [_SRT_OPERATIONS_SCHEDULE, _SRT_MEDIA_PIPELINE]
---

# SRT 自动化执行设置

## 治理预检

从仓库根目录运行：

```bash
uv run python scripts/refresh_split_metadata.py --check
uv run python scripts/governance_preflight.py --skip-write-report --strict-split-metadata
```

用途：

- 检查长文 split registry 是否完整；
- 检查 split README 中的 owner bytes / SHA-256 是否落后于源文件；
- 检查主书大纲拆分是否仍保持连接器安全；
- 检查 frontmatter 与辅助层 canonical 泄漏；
- 检查 staged 文件中是否混入 `.DS_Store`、`.claude/`、`__pycache__/` 等本地噪音。

`Governance_Preflight_GitHub_Actions_Template.yml` 提供同一组命令的 GitHub Actions 模板。启用时需由具备 GitHub `workflow` 权限的凭证复制到 `.github/workflows/governance-preflight.yml`。当前不默认开启全局 `--strict`，因为历史 frontmatter 债务仍按 warning 管理；等 frontmatter 基线收口后再升级。

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
0 8 * * * cd /Users/zhangyuxin/.openclaw/workspace/SRT && uv run python ../scripts/srt_media_topic_daily.py >> /tmp/srt_media_topic_daily.log 2>&1
```

说明：
- 每天 08:00 执行。
- 仅向 `SRT/Operations/_SRT_MEDIA_QUEUE.md` 追加策划条目。

## 方案 B：Heartbeat（上下文感知更强）

在 heartbeat 回合中触发脚本：
```bash
uv run python ../scripts/srt_media_topic_daily.py
```

建议增加防重复门：
- 若当天已生成过主题（检查队列中的日期标记），则跳过。

## 运行后验收

1. 检查队列是否新增当天条目：
- `SRT/Operations/_SRT_MEDIA_QUEUE.md`
2. 运行质量检查：
```bash
# 必须从 workspace 根目录运行（wrapper 内部依赖 scripts/... 相对路径）
./scripts/run_srt_checks.sh

# 若当前在 SRT/ 目录
(cd .. && ./scripts/run_srt_checks.sh)
```

## 故障处理

- 脚本执行失败：查看 `/tmp/srt_media_topic_daily.log`
- 队列写入冲突：先备份队列再重跑
- 若内容重复：人工删除重复项并记录到变更日志
