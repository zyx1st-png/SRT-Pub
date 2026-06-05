---
id: SRT-GOVERNANCE-README
type: index
tags: [Governance, Documentation, Quality, Archive]
status: active_v2
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
dependency: [SRT-INDEX, SRT-AGENTS]
updated: 2026-06-05
---

# SRT Governance Hub

本目录保存 SRT 仓库的治理、编辑边界、claim 分级、文档工程与质量检查材料。

## Authority Boundary

`Governance/` 是治理层，不是书稿正文、理论主文或当前状态本身。

使用原则：

- 用它判断编辑风险、claim 硬度、元数据规范、流程入口和历史留痕。
- 不用它评审全书质量，不用它替代当前书稿正文。
- 不用旧治理计划覆盖 `AGENTS.md` 的 fresh-session read order。
- 与当前书稿、canonical 锚点或 `Operations/_SRT_MATERIAL_LOG.md` 冲突时，治理旧文降为历史记录。

## Current Active Control Surface

### Edit Safety

1. `SRT_CANONICAL_FREEZE.md`
2. `SRT_EDIT_PROTOCOL.md`
3. `SRT_HARNESS_TESTS.md`

### Claim Discipline

1. `SRT_CLAIM_LADDER.md`
2. `SRT_CLAIM_MODE_AUDIT.md`

`SRT_CLAIM_MODE_AUDIT.md` 是 claim-mode 降级台账，不是完整当前状态表；引用时应说明它的历史批次边界。

### Layer / Metadata

1. `SRT_POSITIONING.md`
2. `SRT_COORDINATE_SYSTEM.md`
3. `SRT_Layer_Guard.md`
4. `SRT_L1_Interface_Spec.md`
5. `_SRT_DOC_ENGINEERING_GUIDE.md`
6. `_SRT_DOMAIN_TEMPLATE.md`
7. `_SRT_EXPLANATION_PROTOCOL.md`

### Runtime Governance

1. `../Operations/README.md`
2. `../Operations/_SRT_OPERATIONS_SCHEDULE.md`
3. `_SRT_GOVERNANCE_PIPELINE.md`
4. `_SRT_QUALITY_SCORECARD.md`
5. `_SRT_WEEKLY_THEORY_REVIEW.md`
6. `_SRT_RELEASE_NOTE_TEMPLATE.md`
7. `_SRT_CHANGELOG_2026.md`

`_SRT_EXECUTION_PLAN.md` is retained as a legacy compatibility bridge for old dependencies. Prefer the Operations schedule for current cadence.

### Tooling Baselines

1. `Frontmatter_Warning_Baseline.txt`
2. `../Operations/Large_File_Audit_2026-05-09.md`
3. `../LONGFORM_SPLITS.md`

Baselines record known debt. They are not quality scores.

## Archive

Historical governance files moved on 2026-06-05:

- `Archive_2026-06-05/`

Use archived files only for provenance, not as active policy.
