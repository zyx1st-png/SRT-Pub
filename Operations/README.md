---
id: SRT-OPERATIONS-README
type: index
tags: [Operations, Pipeline, Workflow]
status: active_v1
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
dependency: [SRT-STATUS]
---

# SRT Operations Hub

这里集中放置 SRT 的运行层文档：

- 每日内审 pipeline 与日志
- 信号采集 pipeline 与日志
- 媒体选题 pipeline 与队列
- 论文 pipeline、候选池、活跃草稿、投稿清单
- 材料台账、待审队列、自动化配置
- 结构治理、annex / split 审计、closure 报告

## Authority Boundary

`Operations/` 是 **runtime / workflow layer**，不是 canonical theory layer。

使用原则：

- 用它追溯执行节奏、日志、队列、流程状态与结构治理记录
- 不用它替代理论主文、canonical 定义或符号规范
- 若与 `CANONICAL_REGISTRY.md` 或 canonical 文件冲突，以后者为准

raw session / dialogue compilation / residual archives 已下沉到：

- `Archive/raw_sessions/`

## Recommended Read Order

### Current structure governance

1. `Closure_Index_2026-04-29.md`
2. `Structural_Governance_Rollup_2026-04-29.md`
3. `AI_Annex_Round1_Closure_Report.md`
4. `Physics_P1_Frontmatter_Normalization_Closure_Report.md`
5. `Physics_P2_Interface_Closure_Report.md`

### Runtime pipelines

1. `_SRT_OPERATIONS_SCHEDULE.md`
2. `_SRT_DAILY_REVIEW_PIPELINE.md`
3. `_SRT_SIGNAL_PIPELINE.md`
4. `_SRT_PAPER_PIPELINE.md`
5. `_SRT_MEDIA_PIPELINE.md`
6. `_SRT_KNOWLEDGE_REVIEW_PIPELINE.md`（Pipeline 7：知识点抽查与回写）
7. `_SRT_MATERIAL_PIPELINE.md`（Pipeline 1：材料融合 v2 结构化写入版）
8. `_SRT_MATERIAL_LOG.md`（Pipeline 1 正式材料融入台账；长记录读取从 `Material_Log/README.md` 进入）
9. `_SRT_MATERIAL_ADJUDICATION_WORKFLOW.md`（材料第二轮结构裁决；辅助工作流，不属于 6 条主流水线）

### Connector / large-file safety

1. `../_SRT_AGENT_RETRIEVAL_PROFILE.md`
2. `Agent_Context_Retrieval_Audit_2026-05-10.md`
3. `Large_File_Audit_2026-05-09.md`
4. `Material_Log/README.md`
5. `Status_History/README.md`
6. `../STATUS_Split/README.md`

### Automation / preflight

1. `_SRT_AUTOMATION_SETUP.md`
2. `Governance_Preflight_GitHub_Actions_Template.yml`
3. `../scripts/governance_preflight.py`
4. `../scripts/refresh_split_metadata.py`

## Pipeline 1 Authority

`Operations/_SRT_MATERIAL_PIPELINE.md` 是材料进入仓库的主流程说明。`SourceCard / PatchNote / Registry / IntegrationHook` 都是 Pipeline 1 的结构化产物，不是平行工作流。

`Operations/_SRT_MATERIAL_LOG.md` 仍是正式状态台账；任何 patch、hook 或 index 的状态若与台账冲突，以台账为准。

## Structure Governance Stop Rule

不要在没有新 pre-audit / adjudication 的情况下继续 opportunistic extraction。

当前已经关闭：

- `AI Annex Round 1`
- `Physics P1 frontmatter normalization`
- `Physics P2 interface work`

后续安全工作优先级：

1. index / link hygiene;
2. broken frontmatter 修复;
3. 新领域 pre-audit;
4. 特定高风险主题 read-only adjudication。

不应直接开始：

- 移动公式；
- 移动阈值；
- 移动 AI subjecthood / consciousness claim；
- 移动 Physics gravity / constants / collapse / MWI / discrete-time claim。
