---
id: SRT-GOVERNANCE-README
type: index
tags: [Governance, Documentation, Quality, Archive]
status: active
version: v3
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
dependency: [SRT-INDEX, SRT-AGENTS]
updated: 2026-08-29
---

# SRT Governance Hub

本目录保存 SRT 仓库的治理、编辑边界、claim 分级、文档工程与质量检查材料。

## Proportionality Principles（治理比例原则 · 2026-07-20）

治理减负轮确立的四条元原则继续有效：

1. **治理强度跟着活跃度走**。活跃工作线保持硬护栏；休眠层降为带冻结戳的图书馆。
2. **任何过滤器必须自带回流路径**。下沉必须有具名复活触发条件。
3. **状态只有一个面**。当前状态唯一入口为 `STATUS.md`；历史进 `Operations/Status_History/`。
4. **导航一进一出**。新增 index/router 时应合并、废除或 repurpose 一个旧入口。

本轮 Constitution reconstruction 额外强调：不要把“治理减负”换成“哲学文档增殖”。一个 active identity blueprint、一个 execution plan、一个 governance protocol 足够。

## Authority Boundary

`Governance/` 是治理层，不是书稿正文、理论主文或当前状态本身。

使用原则：

- 用它判断编辑风险、claim 硬度、元数据规范、流程入口和历史留痕；
- 不用它替代 author Constitution、当前书稿、canonical definition；
- 不用旧治理计划覆盖 `AGENTS.md` 的 fresh-session read order；
- 与当前书稿、canonical 锚点或 Material Log 冲突时，治理旧文降为历史记录。

## Current Programme Control — 2026-08-29

### GOV-CONST01 — Constitution + Domain Reconstruction

`SRT_GOV_CONSTITUTION_DOMAIN_RECONSTRUCTION_2026-08-29.md` 是当前 programme 的 identity/workflow governance。

它新增的不是 theory claim，而是执行边界：

- Constitution + Domain identity freeze；
- AI divergence / author convergence 分工；
- no-write-before-convergence；
- Constitution non-formalization guard；
- reflexivity / no God-view exemption；
- ontology situatedness 与 participatory methodology 分离；
- reader-entry operation gate；
- Neighbor Map after convergence, not novelty permission gate；
- domain increment gate；
- Bearer–Objectification Declaration；
- sigma worked-example overclaim guard；
- one-deep-well-before-breadth；
- existing-manuscript carve-out。

如果旧 programme 文件仍把 `unified ontology -> local formalization -> D2` 写成当前执行顺序，以 2026-08-29 blueprint/plan 为当前 programme 路由；这不自动改变 canonical theory authority。

## Current Active Control Surface

### Edit Safety

1. `SRT_CANONICAL_FREEZE.md`
2. `SRT_EDIT_PROTOCOL.md`
3. `SRT_HARNESS_TESTS.md`
4. `SRT_GOV_CONSTITUTION_DOMAIN_RECONSTRUCTION_2026-08-29.md`

### Claim Discipline

1. `SRT_CLAIM_LADDER.md`
2. `SRT_CLAIM_MODE_AUDIT.md`
3. `SRT_GOV_SYN01_Ontological_Synthesis_and_Empirical_Discrimination_Protocol_v0_1.md`
4. `SRT_GOV_SUB01_Subtractive_Audit_Protocol_v0_1.md`

`SRT_CLAIM_MODE_AUDIT.md` 是 claim-mode 降级台账，不是完整当前状态表。

`GOV-SYN01` 的 O-track / D-track 区分继续有效，但在新 programme 下不要把 O-track 当作 Constitution 的外部“证明”。材料可作为 source-native fact、resonance、contrast、pressure、mechanism example 或 domain constraint。

`GOV-SUB01`、A0、bounded-rival 等 subtraction 工具继续有效，但默认从 idea permission gate 移到：

```text
Constitution internal pressure / anti-overclaim
+
Domain increment claim gate
+
repository owner consistency
```

### Layer / Metadata

1. `SRT_POSITIONING.md`
2. `SRT_COORDINATE_SYSTEM.md`
3. `SRT_Layer_Guard.md`
4. `SRT_L1_Interface_Spec.md`
5. `_SRT_DOC_ENGINEERING_GUIDE.md`
6. `_SRT_DOMAIN_TEMPLATE.md`
7. `_SRT_EXPLANATION_PROTOCOL.md`

现有 layer/claim metadata 暂时保留为仓库工程与历史 authority map；本轮不把它们静默升格为新 Constitution 的本体结构。

### Runtime Governance

1. `../Operations/README.md`
2. `../Operations/Proposals/SRT_CONSTITUTION_DOMAIN_RECONSTRUCTION_BLUEPRINT_2026-08-29.md`
3. `../Operations/Proposals/SRT_CONSTITUTION_DOMAIN_EXECUTION_PLAN_2026-08-29.md`
4. `../Operations/_SRT_OPERATIONS_SCHEDULE.md`
5. `_SRT_GOVERNANCE_PIPELINE.md`
6. `Governance_Anti_Blocking_Gate.md`
7. `_SRT_QUALITY_SCORECARD.md`
8. `_SRT_WEEKLY_THEORY_REVIEW.md`
9. `_SRT_RELEASE_NOTE_TEMPLATE.md`
10. `_SRT_CHANGELOG_2026.md`

`Governance_Anti_Blocking_Gate.md` 继续定义 PR-local、base-main 与完整仓库三范围检查、失败归因、baseline 单调性和 main-health incident 模式。

`_SRT_EXECUTION_PLAN.md` 继续作为 legacy compatibility bridge；当前 programme 以 Constitution execution plan 为准。

### Tooling Baselines

1. `Frontmatter_Warning_Baseline.txt`
2. `../Operations/Archive_Records/Large_File_Audit_2026-05-09.md`
3. `../LONGFORM_SPLITS.md`

Baselines record known debt. They are not quality scores and must not grow in ordinary PRs.

## Constitution-specific governance summary

### Constitution-level prohibited shortcuts

- formal equation as constitutional proof;
- state space / unit / boundary smuggled in before author clarification;
- AI agreement counted as author convergence;
- novelty search used to block a live author intuition;
- `knowledge is situated` treated as sufficient SRT content without showing what bearer participation changes about individuation/objectification;
- special access converted into universal epistemic privilege;
- sigma failures generalized into “mathematics cannot model indexicality”.

### Domain-level required discipline

- declare objectification assumptions when an SRT-sensitive claim depends on them;
- use the domain’s strongest existing baseline before claiming SRT increment;
- allow domain to conclude “SRT adds no increment here”;
- keep formalization, evidence and proof domain-local until independent cross-domain support exists.

## Archive

Historical governance files moved on 2026-06-05:

- `Archive_2026-06-05/`

Use archived files only for provenance, not as active policy.
