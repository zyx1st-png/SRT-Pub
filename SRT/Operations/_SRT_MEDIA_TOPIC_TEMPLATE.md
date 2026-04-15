---
id: SRT-MEDIA-TOPIC-TEMPLATE
type: framework
tags: [Media, Topic, Template]
status: active_v1
layer: meta
epistemic_layer: os
claim_mode: canonical
dependency: [_SRT_MEDIA_PIPELINE, _SRT_MEDIA_QUEUE]
---

# SRT 每日主题生成模板（08:00）

## 目标
保证每天自动生成的双路线策划主题质量稳定、字段完整、可直接入队。

## 必填字段
- Topic
- Direction (大众向/学术向/双向)
- Why Now (时效/争议/价值)
- Internal Mapping
  - Core Docs
  - Equation/Axiom Anchors
  - Experiment/Falsification Hooks
- Platforms (recommended)
- Risk Notes
- Publish Window

## 评分规则（100分）
- SRT 相关性（30）
- 增量性（20）
- 可证伪价值（20）
- 传播潜力（15）
- 风险可控性（15）

> 建议入队阈值：>= 70 分。

## 生成顺序
1. 先从最近 7 天 signal log 取候选方向
2. 再从 paper candidates 补理论主线方向
3. 再用 review queue / weekly theory review 补当前治理主线
4. 避免与前 3 天同一路线主题重复
5. 生成 2 条并写入 `Operations/_SRT_MEDIA_QUEUE.md`：
   - 1 条大众路线
   - 1 条精英路线
