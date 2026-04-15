---
id: SRT-CORE-12A-SPLIT-PLAN
type: framework
tags: [Refactor, Ontology, AtomicMap]
status: planning_v1
layer: meta
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-CORE-12A]
---

# SRT_Core_12a 拆分候选计划（Atomicization）

## 目标
缓解 `SRT_Core_12a_Ontology_L0L1.md` 过载，将高异质主题拆分为可维护原子文件。

## 拆分候选
1. `SRT_Core_12a_Gauge_Ruliad.md`（规范场论 + Ruliad）
2. `SRT_Core_12a_InfoBandwidth.md`（认识论带宽 + hard problem）
3. `SRT_Core_12a_Identity_Decomposition.md`（主体同一性与解组合）
4. `SRT_Core_12a_Phenomenology_Binding.md`（统一性与多模态绑定）

## 保留在 12a 主文件的内容
- L0/L1 的最小定义
- 核心公理与跨文件依赖锚点
- 索引与摘要导航

## 验收
- 12a 主文件长度下降（目标：减少 30% 以上）
- 新文件均有 frontmatter 与双向链接
- `run_srt_checks.sh` 通过
