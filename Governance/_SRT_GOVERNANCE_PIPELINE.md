---
id: SRT-GOVERNANCE-PIPELINE
type: framework
tags: [Governance, Maintenance, Readability, TheoryReview]
status: active_v2
layer: meta
epistemic_layer: os
claim_mode: canonical
dependency: [SRT-QUALITY-SCORECARD, SRT-WEEKLY-THEORY-REVIEW, SRT-REVIEW-QUEUE, SRT-EQ-HYP-MAP]
---

# SRT 内部治理流水线（Pipeline 4）

> **变更（2026-03-02）**：在每周文档质量审查后，新增"理论方向评审"环节，产出写入 `Governance/_SRT_WEEKLY_THEORY_REVIEW.md`。

---

## 目标

1. **文档质量**：持续提升结构清晰度、可读性与文档密度，控制冗余回流
2. **理论方向**（新增）：每周评审 SRT 理论状态，给出下周最值得推进的工作项

---

## 触发方式

**自动提醒（HEARTBEAT，每周一）**：
- 检查本周是否已完成 Pipeline 4 → 未完成则提醒
- 用户确认后执行（Pipeline 4 有语义变更风险，不完全自动化）

**手动触发**：
- 用户发送 `周评` → 立即执行文档质量审查 + 理论方向评审

---

## Part A：文档质量审查（每周固定动作）

1. 在 workspace 根目录运行检查：`./scripts/run_srt_checks.sh`
2. 在 `SRT/` 目录生成质量快照：`uv run python ../scripts/srt_quality_metrics.py`
3. 在 `SRT/` 目录生成解释审计：`uv run python ../scripts/srt_explainability_audit.py`
4. 审阅根目录自动快照 `_SRT_QUALITY_METRICS.md` 与 `_SRT_EXPLAINABILITY_AUDIT.md`；若 split / compact / governance / operations 扫描扩容导致口径漂移，需在评分卡中显式标注
5. 去冗余：重复段落 / 重复边界声明 / 重复标题清理
6. **跨层一致性扫描**：执行 `Governance/_SRT_CORE_LAW_CORE_SYNC.md §三` 完整检查步骤（定位映射 → 一致性判断 → 处理结论）；若发现张力，在本步骤内触发 `/srt-harden` 或标注「暂定锚 + 接口预留」，不推迟到下周
7. 更新 `Governance/_SRT_QUALITY_SCORECARD.md` 与 release 注记

**约束（不变）**：
- `Core_Law/` 目录仅做谨慎结构优化，避免语义漂移
- 重大语义变更需单独 commit + release 标注
- 每轮动作后 git commit

---

## Part B：理论方向评审（新增，每周固定，追加到 `Governance/_SRT_WEEKLY_THEORY_REVIEW.md`）

在完成 Part A 后，生成本周 SRT 理论状态报告，使用固定模板：

### 评审模板（5 项）

```markdown
## YYYY-WXX（YYYY-MM-DD）

### 1. 当前理论前沿
（本周 Pipeline 3 信号采集中哪些材料触及了 SRT 的核心问题？若本周无信号，则总结内部工作进展）

### 2. 未解 Gap 状态
（Operations/_SRT_REVIEW_QUEUE.md 中 High 优先级条目进展）
| Gap | 优先级 | 本周状态变化 |
|-----|--------|------------|

### 3. 张力监控
（本周材料融入或内审中是否出现新的破坏性张力？）
- 新检测：...
- 已消解：...

### 4. 实验接口状态
（_SRT_EQ_HYP_MAP.md 中实验钩覆盖率变化）
- 上周：N 个 gap / M 个 ready
- 本周：N' 个 gap / M' 个 ready
- 变化：...

### 5. 理论方向建议
P1（本周内可推进）：...（附理由）
P2（本月内）：...（附理由）
```

### 评审信息来源

| 评审项 | 数据来源 |
|--------|---------|
| 当前理论前沿 | `Operations/_SRT_SIGNAL_LOG.md`（本周记录） |
| 未解 Gap | `Operations/_SRT_REVIEW_QUEUE.md`（Pending 区） |
| 张力监控 | `Operations/_SRT_MATERIAL_LOG.md` + `Operations/_SRT_DAILY_REVIEW_LOG.md` |
| 实验接口 | `_SRT_EQ_HYP_MAP.md` |
| 方向建议 | 综合以上 + 上次评审的 P1/P2 完成情况 |

---

## 输出产物

- `_SRT_QUALITY_METRICS.md`（root-level 自动快照）
- `_SRT_EXPLAINABILITY_AUDIT.md`（root-level 自动快照）
- `Governance/_SRT_QUALITY_SCORECARD.md`（更新）
- `Governance/_SRT_WEEKLY_THEORY_REVIEW.md`（追加本周区块）
- `Governance/_SRT_CORE_LAW_CORE_SYNC.md §五`（暂定锚登记表更新，如有消解或新增）
- git commit：`docs(governance): weekly review YYYY-WXX`
