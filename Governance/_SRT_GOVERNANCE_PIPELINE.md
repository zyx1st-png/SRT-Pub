---
id: SRT-GOVERNANCE-PIPELINE
type: framework
tags: [Governance, Maintenance, Readability, TheoryReview]
status: active
version: v4
layer: meta
epistemic_layer: os
claim_mode: governance
dependency: [SRT-QUALITY-SCORECARD, SRT-WEEKLY-THEORY-REVIEW, SRT-REVIEW-QUEUE, SRT-EQ-HYP-MAP]
updated: 2026-08-05
---

# SRT 内部治理流水线（Pipeline 4）

> **变更（2026-08-05）**：周评读取 review queue 时，必须区分作者裁决、触发式延期和自动扫描待分类，不再引用已删除的 Pending 区。

---

## 目标

1. **文档质量**：持续提升结构清晰度、可读性与文档密度，控制冗余回流；
2. **理论方向**：每周评审 SRT 理论状态，给出下周值得推进的工作项；
3. **队列治理**：防止自动扫描、作者裁决与停驻任务混成同一优先级。

---

## 触发方式

**自动提醒（HEARTBEAT，每周一）**：
- 检查本周是否已完成 Pipeline 4；
- 未完成则提醒；
- 用户确认后执行，因 Pipeline 4 可能涉及语义判断，不完全自动化。

**手动触发**：
- 用户发送 `周评` → 执行文档质量审查 + 理论方向评审。

---

## Part A：文档质量审查

1. 从 workspace 根目录运行：`uv run python scripts/governance_preflight.py`；
2. 只审查时可使用：`uv run python scripts/governance_preflight.py --skip-write-report`；
3. 审阅 large-file audit、split freshness、registry consistency、frontmatter baseline；
4. baseline 旧债修复后必须删除对应条目；新真实错误优先修文件；
5. 清理重复段落、边界声明、标题和旧计划入口；
6. 只有本周实际编辑 Core / Core_Law / canonical-facing bridge 时，才执行 `_SRT_CORE_LAW_CORE_SYNC.md`；
7. 更新 `_SRT_QUALITY_SCORECARD.md`，必要时追加 release note 或 weekly review。

约束：

- `Core_Law/` 只做谨慎结构优化；
- Operations / Governance 文件不得宣布 canonical owner 废止；
- 重大语义变更需独立 PR 和 release 标注；
- 不把自动脚本副产物与理论编辑混在同一提交。

---

## Part B：理论方向评审

周评追加到 `Governance/_SRT_WEEKLY_THEORY_REVIEW.md`，使用以下结构：

```markdown
## YYYY-WXX（YYYY-MM-DD）

### 1. 当前理论前沿
...

### 2. 作者裁决项
（_SRT_REVIEW_QUEUE.md §A）
| Item | 本周状态变化 | 是否阻塞 |
|---|---|---|

### 3. 自动扫描待分类
（_SRT_REVIEW_QUEUE.md §C）
| Finding | 分类结果 | 后续去向 |
|---|---|---|

### 4. 张力监控
- 新检测：...
- 已消解：...

### 5. 实验接口状态
- gap / partial / ready 的真实变化：...

### 6. 理论方向建议
P1（本周内可推进）：...
P2（本月内）：...
```

### 评审信息来源

| 评审项 | 数据来源 |
|---|---|
| 当前理论前沿 | `Operations/_SRT_SIGNAL_LOG.md` |
| 作者裁决 | `Operations/_SRT_REVIEW_QUEUE.md §A` |
| 触发式延期 | `Operations/_SRT_REVIEW_QUEUE.md §B` |
| 自动扫描待分类 | `Operations/_SRT_REVIEW_QUEUE.md §C` |
| 张力监控 | `Operations/_SRT_MATERIAL_LOG.md` + `Operations/_SRT_DAILY_REVIEW_LOG.md` |
| 实验接口 | `_SRT_EQ_HYP_MAP.md` |
| 方向建议 | 以上来源 + 上次 P1/P2 的完成情况 + 当前作者排期 |

周评不得把 §B 的停驻项自动提升为 P1/P2，也不得把 §C 的原始扫描直接写成理论结论。

---

## 输出产物

- `Operations/Archive_Records/Large_File_Audit_2026-05-09.md`（需要写入大文件报告时）；
- `Governance/Frontmatter_Warning_Baseline.txt`（只承认仍存在的已知债）；
- `Governance/_SRT_QUALITY_SCORECARD.md`；
- `Governance/_SRT_WEEKLY_THEORY_REVIEW.md`；
- `Governance/_SRT_CORE_LAW_CORE_SYNC.md §五`（确有 canonical-facing 变更时）；
- 建议提交：`docs(governance): weekly review YYYY-WXX`。
