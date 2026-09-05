---
id: SRT-OPERATIONS-README
type: index
tags: [Operations, Pipeline, Workflow]
status: active
layer: meta
epistemic_layer: os
claim_mode: navigation
canonical: false
dependency: [SRT-STATUS]
updated: 2026-09-05
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

- 用它追溯执行节奏、日志、队列、流程状态与结构治理记录；
- 不用它替代理论主文、canonical 定义或符号规范；
- 若与 `CANONICAL_REGISTRY.md` 或 canonical 文件冲突，以后者为准；
- 当前 reconstruction 执行顺序以 `AGENTS.md` + 2026-09-05 author-reentry amendment + 具名 active plan 为准；
- Operations 文件不能把 AI synthesis、historical SRT 或 local pilot result 静默写成作者当前 ontology。

raw session / dialogue compilation / residual archives 已下沉到：

- `Archive/raw_sessions/`

## Current Research Programme — 2026-09-05

当前第一优先工作线是 **SRT Author Re-entry + Ontology Reconstruction**，Constitution v1 与 Domain Reconstruction Layer 保留，但重新定位：

1. `../01_Source_Intuition/SRT_AUTHOR_REENTRY_CORRECTION_2026-09-05.md` — 最新作者纠偏：节奏过快；bearer 不是全部 ontology。
2. `../Governance/SRT_GOV_AUTHOR_REENTRY_ONTOLOGY_RECONSTRUCTION_AMENDMENT_2026-09-05.md` — 当前 scope / pace / sequencing 控制。
3. `Proposals/SRT_CONSTITUTION_DOMAIN_ARCHITECTURE_V2_2026-09-04.md` — Domain Reconstruction Layer 保留，按 2026-09-05 amendment 收紧解释。
4. `Proposals/SRT_CONSTITUTION_DOMAIN_RECONSTRUCTION_BLUEPRINT_2026-08-29.md` — 历史/补充蓝图，不再以 bearer-totalizing shorthand 单独定义当前 programme。
5. `Proposals/SRT_CONSTITUTION_DOMAIN_EXECUTION_PLAN_2026-08-29.md` — 原 execution plan，受 Architecture v2 + 2026-09-05 amendment 修正。
6. `../Governance/SRT_GOV_CONSTITUTION_DOMAIN_RECONSTRUCTION_2026-08-29.md` — base governance。
7. `Templates/SRT_DOMAIN_RECONSTRUCTION_FRAMEWORK_TEMPLATE.md` — v2 模板，已把 author provenance / mature-neighbor adaptation / common-problem extraction 前置。
8. `Proposals/SRT_CONSTITUTION_SOURCE_RECOVERY_MAP_2026-08-29.md` — source-intuition recovery route。
9. `../01_Source_Intuition/SRT_CONSTITUTION_IDENTITY_AUTHOR_TRACE_2026-08-29.md` — earlier author identity/method trace；非 canonical。

当前核心工作纪律：

```text
current author question / intuition
-> source recovery
-> AI divergence
-> bounded mature-neighbor awareness
-> author provisional convergence
-> internal red-team
-> fuller neighbor adaptation / pressure
-> common-problem extraction
-> author second adjudication
-> only then ontology/interface hardening
-> only then domain-specific discrimination / Case A-B-C when warranted
```

Constitution v1 保持 active/canonical reader-interface prototype，但：

```text
six reader operations
!= complete SRT ontology
```

Bearer / position / participation 保留为重要结构，但：

```text
bearer problem
!= whole SRT ontology
```

当前开放 ontology problem field 可包含 multiplicity / unity / Selection / manifestation / persistence / history-writeback / relation-constraint / bearer-position / future selectability / order-convergence / objectification 等问题，但这些不是新 primitive list、层级或已裁决关系。

### Current deep-well hold

现有两口井保留其历史局部结果：

- Neuroscience：Case B / translation-only / access NO-GO 等继续有效；
- Epistemology：high Case-B pressure / archive NO-GO / evidence infrastructure 等继续有效。

但二者统一按 **early calibration pilots** 解释，不外推为 mature whole-SRT ontology verdict。

在 author re-entry 至少完成一轮并由作者明确放行之前：

```text
third main deep well = HOLD
broad cross-domain synthesis = HOLD
forced Case A/B/C as ontology-formation engine = PROHIBITED
```

有 bounded stop condition 的 archive / evidence infrastructure 可继续。

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
11. `_SRT_CHOICE_TRACE_LOG.md`（收敛轨迹台账：发散→收敛配对留痕，作者收敛函数的 revealed-stake 记录；append-only；Constitution / ontology 对话优先复用此纪律）
12. `.agents/skills/srt-humanization-pipeline/SKILL.md`（公共文本三阶段真人化执行层：`shuorenhua → humanizer-zh → stop-slop → protected-spans 核验`；语言通过不等于发布批准）

## Author-reentry workflow reuse

本轮不另造一套“AI—作者”工作流。优先复用现有 ChoiceMap / Choice Trace 的核心分工：

- AI 可以记录发散选项；
- 作者选择、跳过项、理由、closure boundary 不由 AI 代填；
- `intuition_mining` / `decision` 可用独立 trace + pointer 模式；
- substantive ontology / Constitution write 发生在 author convergence 之后。

新增要求：

- machine review 按角色分工而不是用模型共识代替裁决；
- strong neighbor 必须先用其自身语言表达；
- neighbor pressure 可以改变 / 缩小 SRT；
- 在提出 SRT solution 前先做 common-problem extraction；
- 只有 bounded、author-owned SRT response 存在时才要求 D-track / Case A-B-C。

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

在当前 author-reentry programme 下，O-track 更强调：source-native fact / mature-neighbor resonance-contrast-pressure-realization / common-problem relevance / domain mechanism or constraint。没有 D-track 独有增量不自动等于材料价值低；但外部结果不能因被纳入 SRT 结构就写成“证明 Constitution / ontology”。只有当作者已形成具体 bounded SRT response，并声称额外预测、不可还原或经验优越时，才进入 D-track 与 bounded rival comparison。

`Operations/_SRT_MATERIAL_LOG.md` 仍是正式状态台账；任何 patch、hook 或 index 的状态若与台账冲突，以台账为准。

## Structure Governance Stop Rule

不要在没有新 pre-audit / adjudication 的情况下继续 opportunistic extraction。

当前已经关闭：

- `AI Annex Round 1`
- `Physics P1 frontmatter normalization`
- `Physics P2 interface work`

当前安全工作优先级改为：

1. **author re-entry**：围绕开放 ontology 问题进行作者对话与 source recovery；
2. **mature-neighbor adaptation**：多个强邻居、强反例、source-native problem framing；
3. **machine red-team refinement**：内部一致性、strong-neighbor advocate、counterexample、relabeling、hidden commitment、author-intent drift；
4. **common-problem extraction**：先在非 SRT 语言中识别传统视野的重复困难；
5. **author second adjudication**：决定是否形成 bounded SRT response；
6. index / link / bootstrap hygiene；
7. 后续 Core/Core_Law role-reclassification audit；
8. bounded archive / evidence infrastructure 只在有明确 stop condition 时继续。

当前不应直接开始：

- 在 Constitution 层移动/创造公式、scalar、threshold；
- 批量重写 frozen owner；
- 开启第三个 domain main deep well；
- broad cross-domain synthesis；
- 把 bearer/objectification 当成全部 ontology；
- 因“邻近理论已有”而阻止 author intuition 形成；
- 因“SRT 视角好用”而跳过 mature-neighbor adaptation；
- 在没有 author-owned SRT response 时强迫 Case A/B/C；
- 因两个 pilot 都有 Case-B pressure 就把 SRT 总体收缩成 methodology。
