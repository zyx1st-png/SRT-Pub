---
id: SRT-MEDIA-PIPELINE
type: framework
tags: [Media, Publishing, Outreach]
status: active_v1
dependency: [_SRT_EXECUTION_PLAN, _SRT_MEDIA_QUEUE]
---

# SRT 自媒体选题与发布准备流水线（Pipeline 5）

## 目标
仅提供发布前的“内容准备资产”，不直接成文：
- 选题
- 传播方向
- 选题原因
- 内部关联内容整理（SRT 文档与证据锚点）

## 平台
- 知乎
- 微信公众号
- 头条
- Twitter/X
- Substack
- Medium

## 流程（仅策划，不代写成文）
1. 选题（来自论文孵化线与情报线）
2. 方向定义（大众向/学术向）
3. 原因阐明（时效性、争议点、可证伪价值）
4. 内部关联整理（相关文档、章节、方程、实验接口）
5. 发布准备清单（推荐平台、时窗、风险提示）

## 自动节奏（已启用目标）
- 频率：每日 1 个主题
- 生成时间：每天早 8:00（Asia/Shanghai）
- 产物落点：`_SRT_MEDIA_QUEUE.md` 新增一条 Active Item（策划项）
- 约束：仅生成策划，不生成成文稿，不执行外发
- 模板与脚本：`_SRT_MEDIA_TOPIC_TEMPLATE.md` + `scripts/srt_media_topic_daily.py`

## 外部动作安全规则
- 默认不生成成文稿，不自动发布
- 如需成文或外发，必须由用户单独明确下达指令