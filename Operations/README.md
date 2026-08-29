---
id: SRT-OPERATIONS-README
type: index
tags: [Operations, Pipeline, Workflow]
status: active
record_stage: active_v3
epistemic_layer: os
layer: meta
epistem_layer: os
claim_mode: navigation
canonical: false
dependency: [SRT-STATUS]
updated: 2026-08-29
---

# SRT Operations Hub

这里集中放置 SRT 的运行层文档：

- 当前研究 programme / execution plan
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
- 若与 `CANONICAL_REGISTRY.md` 或 canonical 文件冲突，以后者为准；当前 programme 的执行顺序以 `STATUS.md` + 具名 active plan 为准

raw session / dialogue compilation / residual archives 已下沉到：

- `Archive/raw_sessions/`

## Current Research Programme — 2026-08-29

当前第一优先工作线是 **SRT Constitution + Domain Reconstruction**：

1. `Proposals/SRT_CONSTITUTION_DOMAIN_RECONSTRUCTION_BLUEPRINT_2026-08-29.md` — 当前身份级蓝图：Constitution = bearer-involved perspective；Domain = formalization/evidence/testing layer。
2. `Proposals/SRT_CONSTITUTION_DOMAIN_EXECUTION_PLAN_2026-08-29.md` — 当前唯一 programme execution plan。
3. `../Governance/SRT_GOV_CONSTITUTION_DOMAIN_RECONSTRUCTION_2026-08-29.md` — identity freeze、author convergence、reflexivity、Neighbor Map、domain increment 等治理。
4. `Proposals/SRT_CONSTITUTION_SOURCE_RECOVERY_MAP_2026-08-29.md` — 基于原仓库/书稿/材料卡/审计恢复 source intuition 的路由。
5. `../01_Source_Intuition/SRT_CONSTITUTION_IDENTITY_AUTHOR_TRACE_2026-08-29.md` — 本轮作者身份与方法直觉源记录；非 canonical。

核心工作纪律：

```text
existing source recovery
-> AI divergence
-> author convergence
-> internal red-team
-> Neighbor Map
-> Constitution v1 freeze
-> Core/Core_Law role audit
-> one domain deep well
-> productive-adequacy review
```

在作者收敛前不为每个分支生成理论文件。Constitution 不把 equations/scalars/state-space formalism 作为 authority；domain 侧形式化继续允许。

### Superseded active-plan note

`SRT_CROSS_SCALE_GENERATIVE_EMERGENCE_WRITEBACK_PLAN_2026-07-12.md` 保留为其原工作线的历史/专项施工入口，但**不再是全仓当前第一优先 active execution plan**。若未来重开该工作线，应由 `STATUS.md` / 当前 programme 显式授权。

## Historical structure governance records

已完成的一次性审计 / adjudication / extraction / closure 记录统一存放于 [`Archive_Records/`](Archive_Records/README.md)（2026-07-20 治理减负轮迁入），从其 README 进入。这些记录是历史留痕，不产生维护义务。总入口：

1. `Archive_Records/Closure_Index_2026-04-29.md`
2. `Archive_Records/Structural_Governance_Rollup_2026-04-29.md`

## Runtime pipelines

1. `_SRT_OPERATIONS_SCHEDULE.md`
2. `_SRT_DAILY_REVIEW_PIPELINE.md`
3. `_SRT_SIGNAL_PIPELINE.md`
4. `_SRT_PAPER_PIPELINE.md`
5. `_SRT_MEDIA_PIPELINE.md`
6. `_SRT_KNOWLEDGE_REVIEW_PIPELINE.md`（Pipeline 7：知识点抽查与回写）
7. `_SRT_MATERIAL_PIPELINE.md`（Pipeline 1：材料融合 v2 结构化写入版；贡献判定遵守 `../Governance/SRT_GOV_SYN01_Ontological_Synthesis_and_Empirical_Discrimination_Protocol_v0_1.md`）
8. `_SRT_MATERIAL_LOG.md`（Pipeline 1 正式材料融入台账；长记录读取从 `Material_Log/README.md` 进入）
9. `_SRT_MATERIAL_ADJUDICATION_WORKFLOW.md`（材料第二轮结构裁决；辅助工作流，不属于 6 条主流水线；同样执行 O-track / D-track 双轨判定）
10. `_SRT_ARTICLE_WORKFLOW.md`（文章写作工作流：LLM 发散 / 作者收敛 / 记录轨迹；`2026-07-02` 战略重心转向社媒文章后新增，Pipeline 5 主模式改由此文件定义）
11. `_SRT_CHOICE_TRACE_LOG.md`（收敛轨迹台账：发散→收敛配对留痕，作者收敛函数的 revealed-stake 记录；append-only；Constitution 对话优先复用此纪律）
12. `.agents/skills/srt-humanization-pipeline/SKILL.md`（公共文本三阶段真人化执行层：`shuorenhua → humanizer-zh → stop-slop → protected-spans 核验`；语言通过不等于发布批准）

## Constitution reconstruction workflow reuse

本轮不另造一套“AI—作者”工作流。优先复用现有 ChoiceMap / Choice Trace 的核心分工：

- AI 可以记录发散选项；
- 作者选择、跳过项、理由、closure boundary 不由 AI 代填；
- `intuition_mining` / `decision` 可用独立 trace + pointer 模式；
- Constitution substantive write 发生在 author convergence 之后。

新增加的要求是：Constitution convergence 后必须做 reflexivity/internal red-team 与 bounded Neighbor Map，再由作者二次裁决。

## Connector / large-file safety

1. `../_SRT_AGENT_RETRIEVAL_PROFILE.md`
2. `Archive_Records/Agent_Context_Retrieval_Audit_2026-05-10.md`
3. `Archive_Records/Large_File_Audit_2026-05-09.md`
4. `Material_Log/README.md`
5. `Status_History/README.md`

## Automation / preflight

1. `_SRT_AUTOMATION_SETUP.md`
2. `Governance_Preflight_GitHub_Actions_Template.yml`
3. `../scripts/governance_preflight.py`
4. `../scripts/refresh_split_metadata.py`

## Pipeline 1 Authority

`Operations/_SRT_MATERIAL_PIPELINE.md` 是材料进入仓库的主流程说明。`SourceCard / PatchNote / Registry / IntegrationHook` 都是 Pipeline 1 的结构化产物，不是平行工作流。

Pipeline 1 的材料价值判定必须同时遵守 `Governance/SRT_GOV_SYN01_Ontological_Synthesis_and_Empirical_Discrimination_Protocol_v0_1.md`：

```text
O-track = ontological synthesis
D-track = discriminating / empirical increment
```

在当前 Constitution programme 下，O-track 的读取进一步细分为：source-native fact / Constitution resonance-contrast-pressure / domain mechanism or constraint。没有 D-track 独有增量不自动等于材料价值低；但外部结果不能因被纳入 SRT 结构就写成“证明 Constitution”。只有当 SRT 在具体 domain 声称额外预测、不可还原或经验优越时，才进入 D-track 与 bounded rival comparison。

`Operations/_SRT_MATERIAL_LOG.md` 仍是正式状态台账；任何 patch、hook 或 index 的状态若与台账冲突，以台账为准。

## Structure Governance Stop Rule

不要在没有新 pre-audit / adjudication 的情况下继续 opportunistic extraction。

当前已经关闭：

- `AI Annex Round 1`
- `Physics P1 frontmatter normalization`
- `Physics P2 interface work`

当前安全工作优先级改为：

1. Constitution source recovery / author convergence；
2. index / link / bootstrap hygiene；
3. bounded red-team / Neighbor Map；
4. 后续 Core/Core_Law role-reclassification audit；
5. 首个 domain deep well 前的 scoped pre-audit。

不应直接开始：

- 在 Constitution 层移动/创造公式、scalar、threshold；
- 批量重写 frozen owner；
- 同时开启多个 domain deep-well programme；
- 因“邻近理论已有”而阻止 author perspective 形成；
- 因“SRT 视角好用”而跳过 domain strongest-baseline comparison。
