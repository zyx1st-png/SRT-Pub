---
id: SRT-GOVERNANCE-README
type: index
tags: [Governance, Documentation, Quality, Archive]
status: active
version: v2
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
dependency: [SRT-INDEX, SRT-AGENTS]
updated: 2026-08-17
---

# SRT Governance Hub

本目录保存 SRT 仓库的治理、编辑边界、claim 分级、文档工程与质量检查材料。

## Proportionality Principles（治理比例原则 · 2026-07-20）

治理减负轮确立的四条元原则，优先于逐条堆积的具体规则。目的：让治理强度随工作面收缩，而不是单向增长。

1. **治理强度跟着活跃度走**。活跃工作线（书稿、papers、canonical 锚点）保持硬护栏；休眠层（域层、coverage 快照、archive）降为"带冻结戳的图书馆"——只读、可检索、零维护义务，按 `_SRT_DOC_ENGINEERING_GUIDE.md` 的 touch-based repair 处理。
2. **任何过滤器必须自带回流路径**。下沉（降级、B 类裁决、种子停驻、annex 化）必须在 `_SRT_PARKED_INDEX.md` 登记一条**具名复活触发条件**（绑工作线事件，不绑日历）。没有回流路径的下沉等于删除，不允许。
3. **状态只有一个面**。描述"当前状态"的文件唯一（`STATUS.md`，§Fast Status 兼任 compact 入口）；镜像要么自动生成，要么删除。历史进 `Operations/Status_History/`。
4. **导航一进一出**。新增任何 index / router / coverage 文件，必须同时合并或废除一个旧的。router 路由折进主 router，不再生 `_*_EXTENSION.md` 侧车文件。

可观测指标看板见 `_SRT_QUALITY_METRICS.md §Governance Load Indicators`；本轮执行记录见 `Governance/Governance_Load_Reduction_2026-07-20.md`。

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
3. `SRT_GOV_SYN01_Ontological_Synthesis_and_Empirical_Discrimination_Protocol_v0_1.md`
4. `SRT_GOV_SUB01_Subtractive_Audit_Protocol_v0_1.md`

`SRT_CLAIM_MODE_AUDIT.md` 是 claim-mode 降级台账，不是完整当前状态表；引用时应说明它的历史批次边界。

`SRT_GOV_SYN01_Ontological_Synthesis_and_Empirical_Discrimination_Protocol_v0_1.md` 把理论贡献拆成两条不能互相替代的轨道：**O-track 本体论整合**与 **D-track 经验/判别增量**。SRT 可以忠实吸收成熟外部理论已经建立的局部机制来构建共同本体论语法；“没有独有经验增量”不自动等于低价值或 bridge 失败。但外部结果只支持其原生事实，作为 SRT 结构实例不等于证明 SRT 本体论。只有当 SRT 声称超越、替代、不可还原或新增预测时，才必须进入 D-track 与 bounded rival comparison。

`SRT_GOV_SUB01_Subtractive_Audit_Protocol_v0_1.md` 用于 primitive、symbol、layer、bridge 与竞争理论的受控删除审计。其输出始终是目标/尺度/时间窗相对的可删除性或当前不可删除性，不把“删除无损”写成不存在，也不把“暂不可删除”写成本体基础。对材料/bridge 的价值判断还必须结合 `GOV-SYN01`：D-track 上可替代，不等于 O-track 上没有整合价值。

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
4. `Governance_Anti_Blocking_Gate.md`
5. `_SRT_QUALITY_SCORECARD.md`
6. `_SRT_WEEKLY_THEORY_REVIEW.md`
7. `_SRT_RELEASE_NOTE_TEMPLATE.md`
8. `_SRT_CHANGELOG_2026.md`

`Governance_Anti_Blocking_Gate.md` 定义 PR-local、base-main 与完整仓库三范围检查、失败归因、baseline 单调性和 main-health incident 模式。

`_SRT_EXECUTION_PLAN.md` is retained as a legacy compatibility bridge for old dependencies. Prefer the Operations schedule for current cadence.

### Tooling Baselines

1. `Frontmatter_Warning_Baseline.txt`
2. `../Operations/Archive_Records/Large_File_Audit_2026-05-09.md`
3. `../LONGFORM_SPLITS.md`

Baselines record known debt. They are not quality scores and must not grow in ordinary PRs.

## Archive

Historical governance files moved on 2026-06-05:

- `Archive_2026-06-05/`

Use archived files only for provenance, not as active policy.