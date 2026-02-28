---
id: SRT-GOVERNANCE-PIPELINE
type: framework
tags: [Governance, Maintenance, Readability]
status: active_v1
dependency: [_SRT_QUALITY_SCORECARD, _SRT_SLIMMING_CHANGELOG_2026-02]
---

# SRT 内部治理流水线（Pipeline 4）

## 目标
持续提升结构清晰度、可读性（人类/AI）与文档密度，控制冗余回流。

## 固定动作（每周）
1. 运行检查：`./scripts/run_srt_checks.sh`
2. 质量快照：`python3 scripts/srt_quality_metrics.py`
3. 解释审计：`python3 scripts/srt_explainability_audit.py`
4. 去冗余：重复段落/重复边界/重复标题清理
5. 更新 scorecard 与 release 注记

## 约束
- Core_Law 仅做谨慎结构优化，避免语义漂移
- 重大语义变更需单独 commit + release 标注
