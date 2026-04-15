---
id: SRT-INDEX
type: framework
tags: [Index, Registry, Navigation]
status: axiomatic_hybrid_v1
layer: meta
claim_mode: canonical
epistemic_layer: os
dependency: [_SRT_MANIFEST, SRT-GLOSSARY]
---

# 选择性现实理论（SRT）完整索引

---
**维护说明：** 此索引当前为手工维护。

**单一数据源约定：**
- **文档统计信息** → 本文件为权威来源（其他索引文件仅提供概要并链接到此处）
- **概念完整定义** → 请参考 [SRT_Glossary.md](SRT_Glossary.md)
- **术语拆分导航** → 请参考 [Glossary/README.md](Glossary/README.md)
- **长文拆分导航** → 请参考 [Philosophy/Foundations_Split/README.md](Philosophy/Foundations_Split/README.md)、[Philosophy/Social_Economics_Split/README.md](Philosophy/Social_Economics_Split/README.md)、[AI/Ontology_Split/README.md](AI/Ontology_Split/README.md)、[AI/Architecture_Split/README.md](AI/Architecture_Split/README.md)、[AI/Consciousness_Framework_Split/README.md](AI/Consciousness_Framework_Split/README.md)、[Core/Dynamics_Scaling_Split/README.md](Core/Dynamics_Scaling_Split/README.md)、[Physics/Cosmology_Split/README.md](Physics/Cosmology_Split/README.md)、[Physics/Formalism_Ext_Split/README.md](Physics/Formalism_Ext_Split/README.md)、[Spirituality/Praxis_Split/README.md](Spirituality/Praxis_Split/README.md)
- **阅读路径规划** → 请参考 [SRT_Navigation_Map.md](SRT_Navigation_Map.md)
- **定位与层级治理** → 请参考 [Governance/SRT_POSITIONING.md](Governance/SRT_POSITIONING.md)
- **二维坐标治理** → 请参考 [Governance/SRT_COORDINATE_SYSTEM.md](Governance/SRT_COORDINATE_SYSTEM.md)
- **Lab 硬赌点总表** → 请参考 [Governance/SRT_LAB_HYPOTHESES.md](Governance/SRT_LAB_HYPOTHESES.md)
- **专题入口（自由意志）** → [SRT_TOPIC_FREE_WILL_INDEX.md](SRT_TOPIC_FREE_WILL_INDEX.md)
- **专题入口（意识×能动性）** → [SRT_TOPIC_CONSCIOUSNESS_AGENCY_INDEX.md](SRT_TOPIC_CONSCIOUSNESS_AGENCY_INDEX.md)
- **专题入口（文章写作）** → [SRT_TOPIC_ARTICLE_INDEX.md](SRT_TOPIC_ARTICLE_INDEX.md)
- **机器可读清单** → 请参考 [_SRT_MANIFEST.yaml](_SRT_MANIFEST.yaml)
- **文档工程规范** → 请参考 [Governance/_SRT_DOC_ENGINEERING_GUIDE.md](Governance/_SRT_DOC_ENGINEERING_GUIDE.md)
- **长文拆分总注册表** → 请参考 [LONGFORM_SPLITS.md](LONGFORM_SPLITS.md)
- **canonical 总注册表** → 请参考 [CANONICAL_REGISTRY.md](CANONICAL_REGISTRY.md)
- **annex 总注册表** → 请参考 [ANNEX_REGISTRY.md](ANNEX_REGISTRY.md)

**未来自动化建议：**
1. 在各文档中添加 YAML frontmatter（词数、难度、依赖关系）
2. 使用脚本从 frontmatter 自动生成统计表
3. 建立交叉引用验证脚本
4. 依赖字段统一使用 canonical id（如 `SRT-AI-01`）或 `Core_Law/...` 路径

---

<!-- AUTO:ENTRYPOINTS:START -->
## 🧭 Canonical Domain Entrypoints (Manifest-Maintained)

> 本区块当前按 `_SRT_MANIFEST.yaml` 人工维护。
> 仓库中未包含 `srt_sync_entrypoints.py` 自动同步脚本；如入口发生变更，请同步更新本区块与 `SRT_Quick_Start.md`。
> Last manual sync: 2026-02-28

| Domain | Bridge | Entrypoints |
| :--- | :--- | :--- |
| Core | [`Core/_SRT_Core_Bridge.md`](Core/_SRT_Core_Bridge.md) (`SRT-CORE-BRIDGE`) | [`SRT_1H_Onboarding.md`](SRT_1H_Onboarding.md) (`SRT-CORE-ONBOARDING`)<br>[`Core/SRT_Core_00_Intro.md`](Core/SRT_Core_00_Intro.md) (`SRT-CORE-000`)<br>[`Core/SRT_Core_01_Axioms.md`](Core/SRT_Core_01_Axioms.md) (`SRT-CORE-001`)<br>[`Core/SRT_Core_21_Formal_Axioms.md`](Core/SRT_Core_21_Formal_Axioms.md) (`SRT-CORE-21`)<br>[`Core/SRT_Core_22_Equations.md`](Core/SRT_Core_22_Equations.md) (`SRT-CORE-22`) |
| Physics | [`Physics/_SRT_Phys_Bridge.md`](Physics/_SRT_Phys_Bridge.md) (`SRT-PHYS-BRIDGE`) | [`Physics/SRT_Quant_00_Intro.md`](Physics/SRT_Quant_00_Intro.md) (`SRT-QUANT-00`)<br>[`Physics/SRT_Phys_10_Integration.md`](Physics/SRT_Phys_10_Integration.md) (`SRT-PHYS-10`) |
| Neuroscience | [`Neuroscience/_SRT_Neuro_Axioms.md`](Neuroscience/_SRT_Neuro_Axioms.md) (`SRT-NEURO-AXIOMS-001`) | [`Neuroscience/SRT_Neural_Mechanisms.md`](Neuroscience/SRT_Neural_Mechanisms.md) (`SRT-NEURO-MECH-001`)<br>[`Neuroscience/SRT_Consciousness_Mechanisms.md`](Neuroscience/SRT_Consciousness_Mechanisms.md) (`SRT-NEURO-MECH-B`)<br>[`Neuroscience/SRT_Neuro_Experiments.md`](Neuroscience/SRT_Neuro_Experiments.md) (`SRT-NEURO-EXP`) |
| Philosophy | [`Philosophy/_SRT_Phil_Axioms.md`](Philosophy/_SRT_Phil_Axioms.md) (`SRT-PHIL-AXIOMS`) | [`SRT_FAQ_CRITICAL.md`](SRT_FAQ_CRITICAL.md) (`SRT-PHIL-FAQ`)<br>[`Philosophy/SRT_Philosophy_Foundations.md`](Philosophy/SRT_Philosophy_Foundations.md) (`SRT-PHIL-FOUNDATIONS`)<br>[`Philosophy/SRT_Philosophy_Ethics.md`](Philosophy/SRT_Philosophy_Ethics.md) (`SRT-PHIL-ETHICS`)<br>[`Philosophy/SRT_Social_Economics.md`](Philosophy/SRT_Social_Economics.md) (`SRT-SOC-ECONOMICS`)<br>[`Philosophy/SRT_Political_Rights.md`](Philosophy/SRT_Political_Rights.md) (`SRT-POLITICAL-RIGHTS`) |
| Spirituality | [`Spirituality/_SRT_Spirit_Axioms.md`](Spirituality/_SRT_Spirit_Axioms.md) (`SRT-SPIRIT-AXIOMS`) | [`Spirituality/SRT_Spirit_01_Religion_Ontology.md`](Spirituality/SRT_Spirit_01_Religion_Ontology.md) (`SRT-SPIRIT-01`)<br>[`Spirituality/SRT_Spirit_04_Synthesis.md`](Spirituality/SRT_Spirit_04_Synthesis.md) (`SRT-SPIRIT-04`)<br>[`Spirituality/SRT_Spirit_09_Praxis.md`](Spirituality/SRT_Spirit_09_Praxis.md) (`SRT-SPIRIT-09`) |
| AI | [`AI/_SRT_AI_Bridge.md`](AI/_SRT_AI_Bridge.md) (`SRT-AI-BRIDGE-001`) | [`AI/SRT_AI_00_Crisis.md`](AI/SRT_AI_00_Crisis.md) (`SRT-AI-00`)<br>[`AI/SRT_AI_01_Ontology.md`](AI/SRT_AI_01_Ontology.md) (`SRT-AI-01`)<br>[`AI/SRT_AI_02_Mortality_Wisdom.md`](AI/SRT_AI_02_Mortality_Wisdom.md) (`SRT-AI-02`)<br>[`AI/SRT_AI_03_Consciousness_Framework.md`](AI/SRT_AI_03_Consciousness_Framework.md) (`SRT-AI-03`)<br>[`AI/SRT_AI_Architecture.md`](AI/SRT_AI_Architecture.md) (`SRT-AI-ARCH`) |
| Experiment | - | [`SRT_EXP_PRIORITY_MATRIX.md`](SRT_EXP_PRIORITY_MATRIX.md) (`SRT-EXP-PRIORITY`)<br>[`SRT_EXP_TEMPLATE.md`](SRT_EXP_TEMPLATE.md) (`SRT-EXP-TEMPLATE`)<br>[`SRT_EXP_MEASURE_MAP.md`](SRT_EXP_MEASURE_MAP.md) (`SRT-EXP-MEASUREMAP`) |
| Project | - | [`SRT_OPTIMIZATION_BACKLOG.md`](SRT_OPTIMIZATION_BACKLOG.md) (`SRT-BACKLOG`) |
<!-- AUTO:ENTRYPOINTS:END -->


> 最新更新：2026-04-15（ε → 通用智能 & 统一道德拓扑：`Philosophy/SRT_Philosophy_Ethics.md §V`（Ax-Eth-11~13 + Lemma-Eth-MNI）、`AI/SRT_AI_01_Ontology.md §VII`（Def-ONT-UI、Def-ONT-FI、T-ONT-Convergence）；词汇表新增 $C_{FBC}$、道德计量单元、构成地板、扩展支架、通用智能、完全智能、最小必要阻断）| 上次更新：2026-04-10（新增 Annex 13：社会delegation、d值判断系统、多G协调机制；Annex 12 升至 v2.1——§6 全面扩充引导性delegation正向机制）

### 🆕 2026-04-08 核心新增文件

| 文件 | 层级 | 内容 |
|---|---|---|
| `Core/Dynamics_Scaling_Annex/07_SelectionBarrier_L0L1_PriorSystem.md` | Annex | 选择壁垒的层级机制与L0/L1先验系统 |
| `Core/Dynamics_Scaling_Annex/08_MoralPredictionError_MultiG_System.md` | Annex | 道德预测误差与多G先验系统 |
| `Core/Dynamics_Scaling_Annex/09_ErrorAccumulation_L2Reconstruction.md` | Annex | 错误积累与L2重建动力学 |
| `Core/Dynamics_Scaling_Annex/10_ROS_Apoptosis_ErrorDose.md` | Annex | 错误积累的剂量动力学 |
| `Core/Dynamics_Scaling_Annex/11_G_CrossScale_PhaseState.md` | Annex | G的跨尺度结构与高阶相态条件 |
| `Core/Dynamics_Scaling_Annex/12_ProxyModel_OcclusionPhases_Intervention.md` | Annex | 代理模型、遮蔽两相结构与三层介入（v2.1：引导性delegation正向机制完整描述）|
| `Core/Dynamics_Scaling_Annex/13_SocialDelegation_DJudgment_Coordination.md` | Annex | 社会delegation方向性、d值判断系统（殖民检测）、多G协调机制 |
| `Core/SRT_Core_PhaseState_TripleCondition.md` | **Core** | 高阶相态三条件规范定义（历史闭合、规范梯度、自写回强度）|
| `Core/SRT_Core_NormativeGradient.md` | **Core** | 规范梯度规范定义（自指势差读数）|

**同期 Core 层修正**（就地更新，非新文件）：
- `Core/SRT_Core_01_Axioms.md`：新增 T-Core-A1C3（G跨尺度连续性；G选择=遮蔽修正）
- `Core/SRT_Core_12a_Ontology_L0L1.md`：新增 T-L0-ProtoG（L₀中的原型G选择形式；三相态条件）
- `Core/SRT_Core_13a_Operator_Basics.md`：Ax-Op-01 补充遮蔽定义与代理结构
- `_SRT_D_VALUE_CANONICAL.md`：新增 §10（d值多场景显现：整合半径、张力窗口、校准带宽）

## 📜 历史增量与版本记录

- 历史理论增量（含批次合并记录）已迁移至：[`Governance/_SRT_CHANGELOG_2026.md`](Governance/_SRT_CHANGELOG_2026.md)
- 主索引仅保留导航/入口/注册信息，以提升可维护性与 AI 检索稳定性。

## 🗂️ Structure Layers（结构分层）

> **层级说明（L0 / L1 / L2）**：
> - **L0（形而上学核心）**：`Core_Law/SRT_L0_Metaphysics.md` ← 唯一命题锚点，四命题 + 选择边界
> - **L0 哲学接口**：`Core_Law/SRT_L0_Philosophy_Bridge.md` ← (L0, bridge)，哲学传统定位，不构成 L0 证据
> - **L1（接口层）**：`Core_Law/` 其余文件、各领域 Bridge 文件、Physics/Neuroscience/Philosophy/AI 文件
> - **L2（验证层）**：`SRT_EXP_*.md`、`Governance/SRT_LAB_HYPOTHESES.md`
>
> 所有新内容写作前先问：这属于哪层？L0 内容只进 `SRT_L0_Metaphysics.md`，不散落到其他文件。
>
> **水平覆盖层（OS / Bridge / Lab）**：
> - `OS` = 概念语法 / 内部稳定锚点
> - `Bridge` = 与外部理论和领域现实的互译接口
> - `Lab` = 愿意下注的实验与证伪界面
>
> 这两套不是竞争层级，而是正交坐标。任何文件都应按 `(layer, epistemic_layer)` 来理解；详见 `Governance/SRT_COORDINATE_SYSTEM.md`。

- **L0 锚点**：`Core_Law/SRT_L0_Metaphysics.md`（选择的形而上学，四命题，无公式无引用）
- **Entry**：`STATUS.md`、`SRT_Quick_Start.md`、`SRT_1H_Onboarding.md`、`SRT_Navigation_Map.md`
- **Canonical / Registry**：`CANONICAL_REGISTRY.md`、`ANNEX_REGISTRY.md`、`LONGFORM_SPLITS.md`
- **Positioning Overlay**：`Governance/SRT_POSITIONING.md`（`OS / Bridge / Lab` 作为水平认识论覆盖层）
- **Coordinate Spec**：`Governance/SRT_COORDINATE_SYSTEM.md`（`layer × epistemic_layer × claim_mode` 的统一说明）
- **Lab Portfolio**：`Governance/SRT_LAB_HYPOTHESES.md`（全局硬赌点与最小实验下注口）
- **Theory**：`Core/`、`Core_Law/`、`Physics/`、`Neuroscience/`、`Philosophy/`、`Spirituality/`、`AI/`
- **Compact Core**：各板块新增的 compact core 文件，用于提供最短稳定主线
- **Governance**：`Governance/` 下的规范、发布、质量、审计、周评文件
- **Operations**：`Operations/` 下的流水线、台账、队列、运行日志
- **Glossary Split**：`Glossary/` 下的术语拆分导航文件（保留总表，不删内容）

## 🧭 Current Registry & Compact-Core Entrypoints（当前入口骨架）

### Global
- 会话入口：`STATUS.md`
- 导航总图：`SRT_Navigation_Map.md`
- 定位宪章：`Governance/SRT_POSITIONING.md`
- Lab 假说包：`Governance/SRT_LAB_HYPOTHESES.md`
- canonical 总注册表：`CANONICAL_REGISTRY.md`
- annex 总注册表：`ANNEX_REGISTRY.md`
- 长文拆分总注册表：`LONGFORM_SPLITS.md`
- d-value 规范：`_SRT_D_VALUE_CANONICAL.md`
- Ψ_f 规范：`_SRT_PSI_F_CANONICAL.md`
- T_dir 规范（方向透明度 / 价值遮蔽 / 致命 L₂）：`_SRT_T_DIR_CANONICAL.md`

### Chinese Core Text Family
- L0 锚点：`Core_Law/SRT_L0_Metaphysics.md`
- 中文主论证候选：`Core_Law/SRT_Core_Text_CN_Euclid.md`
- 原版中文自足论证（历史主文 / 读者入口）：`Core_Law/SRT_Core_Text_CN.md`
- 哲学辩护文：`Core_Law/SRT_Selection_Argument.md`

### Core
- `Core/SRT_Core_21_Formal_Axioms.md`
- `Core/SRT_Core_22_Equations.md`
- `Core/SRT_Core_14_Dynamics_Scaling_CompactCore.md`

### Philosophy
- `Philosophy/SRT_Philosophy_Foundations_CompactCore.md`
- `Philosophy/Foundations_Split/README.md`
- `Philosophy/Social_Economics_Split/README.md`

### AI
- `AI/SRT_AI_01_Ontology_CompactCore.md`
- `AI/SRT_AI_Architecture_CompactCore.md`
- `AI/SRT_AI_03_Consciousness_Framework_CompactCore.md`

### Neuroscience
- `Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md`
- `Neuroscience/_SRT_Neuro_Axioms.md`
- `Neuroscience/SRT_Neural_Mechanisms_CompactCore.md`
- `Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md`

### Physics
- `Physics/PHYSICS_COMPACT_REGISTRY.md`
- `Physics/SRT_Quant_00_Intro_CompactCore.md`
- `Physics/SRT_Quant_01_Selection_CompactCore.md`
- `Physics/SRT_Quant_02_Cosmology_CompactCore.md`
- `Physics/SRT_Physics_Cosmology_CompactCore.md`
- `Physics/SRT_Phys_09_Formalism_Ext_CompactCore.md`
- `Physics/SRT_Phys_10_Integration_CompactCore.md`
- `Physics/SRT_Phys_07_Complex_Systems_CompactCore.md`
- `Physics/SRT_Phys_08_Ontology_Ext_CompactCore.md`

### Spirituality
- `Spirituality/SPIRITUALITY_COMPACT_REGISTRY.md`
- `Spirituality/_SRT_Spirit_Axioms.md`
- `Spirituality/SRT_Spirit_09_Praxis_CompactCore.md`

## 🧰 Documentation Governance Hub（治理入口）

### 规划与流程
- 定位与分层治理：[`Governance/SRT_POSITIONING.md`](Governance/SRT_POSITIONING.md)
- 全局 Lab 假说包：[`Governance/SRT_LAB_HYPOTHESES.md`](Governance/SRT_LAB_HYPOTHESES.md)
- 总体优化计划：[`Governance/SRT_INTERNAL_OPTIMIZATION_PLAN_2026Q1.md`](Governance/SRT_INTERNAL_OPTIMIZATION_PLAN_2026Q1.md)
- 解释协议（Definition→Mechanism→Falsification）：[`Governance/_SRT_EXPLANATION_PROTOCOL.md`](Governance/_SRT_EXPLANATION_PROTOCOL.md)
- 方程-假设映射：[`_SRT_EQ_HYP_MAP.md`](_SRT_EQ_HYP_MAP.md)
- 领域文档模板：[`Governance/_SRT_DOMAIN_TEMPLATE.md`](Governance/_SRT_DOMAIN_TEMPLATE.md)
- diff 管线规范：[`Governance/_SRT_DIFF_PIPELINE_GUIDE.md`](Governance/_SRT_DIFF_PIPELINE_GUIDE.md)

### 质量与发布
- Frontmatter 审计：[`Governance/_SRT_FRONTMATTER_AUDIT.md`](Governance/_SRT_FRONTMATTER_AUDIT.md)
- 质量评分卡：[`Governance/_SRT_QUALITY_SCORECARD.md`](Governance/_SRT_QUALITY_SCORECARD.md)
- 自动指标快照：[`Governance/_SRT_QUALITY_METRICS.md`](Governance/_SRT_QUALITY_METRICS.md)
- 解释链审计：[`Governance/_SRT_EXPLAINABILITY_AUDIT.md`](Governance/_SRT_EXPLAINABILITY_AUDIT.md)
- Release 模板：[`Governance/_SRT_RELEASE_NOTE_TEMPLATE.md`](Governance/_SRT_RELEASE_NOTE_TEMPLATE.md)
- 最新发布快照：[`Governance/_SRT_RELEASE_2026-02.md`](Governance/_SRT_RELEASE_2026-02.md)
- 减肥变更日志：[`Governance/_SRT_SLIMMING_CHANGELOG_2026-02.md`](Governance/_SRT_SLIMMING_CHANGELOG_2026-02.md)
- 执行总控：[`Governance/_SRT_EXECUTION_PLAN.md`](Governance/_SRT_EXECUTION_PLAN.md)
- 论文流水线：[`Operations/_SRT_PAPER_PIPELINE.md`](Operations/_SRT_PAPER_PIPELINE.md)
- 情报流水线：[`Operations/_SRT_SIGNAL_PIPELINE.md`](Operations/_SRT_SIGNAL_PIPELINE.md)
- 治理流水线：[`Governance/_SRT_GOVERNANCE_PIPELINE.md`](Governance/_SRT_GOVERNANCE_PIPELINE.md)
- 媒体流水线：[`Operations/_SRT_MEDIA_PIPELINE.md`](Operations/_SRT_MEDIA_PIPELINE.md)
- 运行节奏：[`Operations/_SRT_OPERATIONS_SCHEDULE.md`](Operations/_SRT_OPERATIONS_SCHEDULE.md)
- 自动化设置：[`Operations/_SRT_AUTOMATION_SETUP.md`](Operations/_SRT_AUTOMATION_SETUP.md)
