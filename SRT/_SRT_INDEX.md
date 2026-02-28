---
id: SRT-INDEX
type: framework
tags: [Index, Registry, Navigation]
status: axiomatic_hybrid_v1
dependency: [_SRT_MANIFEST, SRT-GLOSSARY]
---

# 选择性现实理论（SRT）完整索引

---
**维护说明：** 此索引当前为手工维护。

**单一数据源约定：**
- **文档统计信息** → 本文件为权威来源（其他索引文件仅提供概要并链接到此处）
- **概念完整定义** → 请参考 [SRT_Glossary.md](SRT_Glossary.md)
- **阅读路径规划** → 请参考 [SRT_Navigation_Map.md](SRT_Navigation_Map.md)
- **机器可读清单** → 请参考 [_SRT_MANIFEST.yaml](_SRT_MANIFEST.yaml)
- **文档工程规范** → 请参考 [_SRT_DOC_ENGINEERING_GUIDE.md](_SRT_DOC_ENGINEERING_GUIDE.md)

**未来自动化建议：**
1. 在各文档中添加 YAML frontmatter（词数、难度、依赖关系）
2. 使用脚本从 frontmatter 自动生成统计表
3. 建立交叉引用验证脚本
4. 依赖字段统一使用 canonical id（如 `SRT-AI-01`）或 `Core_Law/...` 路径

---

<!-- AUTO:ENTRYPOINTS:START -->
## 🧭 Canonical Domain Entrypoints (Auto-Synced)

> 本区块由 `scripts/srt_sync_entrypoints.py` 从 `_SRT_MANIFEST.yaml` 自动生成，请勿手工编辑。
> Last sync: 2026-02-28

| Domain | Bridge | Entrypoints |
| :--- | :--- | :--- |
| Core | [`Core/_SRT_Core_Bridge.md`](Core/_SRT_Core_Bridge.md) (`SRT-CORE-BRIDGE`) | [`SRT_1H_Onboarding.md`](SRT_1H_Onboarding.md) (`SRT-CORE-ONBOARDING`)<br>[`Core/SRT_Core_00_Intro.md`](Core/SRT_Core_00_Intro.md) (`SRT-CORE-000`)<br>[`Core/SRT_Core_01_Axioms.md`](Core/SRT_Core_01_Axioms.md) (`SRT-CORE-001`)<br>[`Core/SRT_Core_21_Formal_Axioms.md`](Core/SRT_Core_21_Formal_Axioms.md) (`SRT-CORE-21`)<br>[`Core/SRT_Core_22_Equations.md`](Core/SRT_Core_22_Equations.md) (`SRT-CORE-22`) |
| Physics | [`Physics/_SRT_Phys_Bridge.md`](Physics/_SRT_Phys_Bridge.md) (`SRT-PHYS-BRIDGE`) | [`Physics/SRT_Quant_00_Intro.md`](Physics/SRT_Quant_00_Intro.md) (`SRT-QUANT-00`)<br>[`Physics/SRT_Phys_10_Integration.md`](Physics/SRT_Phys_10_Integration.md) (`SRT-PHYS-10`) |
| Neuroscience | [`Neuroscience/_SRT_Neuro_Axioms.md`](Neuroscience/_SRT_Neuro_Axioms.md) (`SRT-NEURO-AXIOMS-001`) | [`Neuroscience/SRT_Neural_Mechanisms.md`](Neuroscience/SRT_Neural_Mechanisms.md) (`SRT-NEURO-MECH-001`)<br>[`Neuroscience/SRT_Consciousness_Mechanisms.md`](Neuroscience/SRT_Consciousness_Mechanisms.md) (`SRT-NEURO-MECH-B`)<br>[`Neuroscience/SRT_Neuro_Experiments.md`](Neuroscience/SRT_Neuro_Experiments.md) (`SRT-NEURO-EXP`) |
| Philosophy | [`Philosophy/_SRT_Phil_Axioms.md`](Philosophy/_SRT_Phil_Axioms.md) (`SRT-PHIL-AXIOMS`) | [`SRT_FAQ_CRITICAL.md`](SRT_FAQ_CRITICAL.md) (`SRT-PHIL-FAQ`)<br>[`Philosophy/SRT_Philosophy_Foundations.md`](Philosophy/SRT_Philosophy_Foundations.md) (`SRT-PHIL-FOUNDATIONS`)<br>[`Philosophy/SRT_Philosophy_Ethics.md`](Philosophy/SRT_Philosophy_Ethics.md) (`SRT-PHIL-ETHICS`)<br>[`Philosophy/SRT_Social_Economics.md`](Philosophy/SRT_Social_Economics.md) (`SRT-SOC-ECONOMICS`) |
| Spirituality | [`Spirituality/_SRT_Spirit_Axioms.md`](Spirituality/_SRT_Spirit_Axioms.md) (`SRT-SPIRIT-AXIOMS`) | [`Spirituality/SRT_Spirit_01_Religion_Ontology.md`](Spirituality/SRT_Spirit_01_Religion_Ontology.md) (`SRT-SPIRIT-01`)<br>[`Spirituality/SRT_Spirit_04_Synthesis.md`](Spirituality/SRT_Spirit_04_Synthesis.md) (`SRT-SPIRIT-04`)<br>[`Spirituality/SRT_Spirit_09_Praxis.md`](Spirituality/SRT_Spirit_09_Praxis.md) (`SRT-SPIRIT-09`) |
| AI | [`AI/_SRT_AI_Bridge.md`](AI/_SRT_AI_Bridge.md) (`SRT-AI-BRIDGE-001`) | [`AI/SRT_AI_00_Crisis.md`](AI/SRT_AI_00_Crisis.md) (`SRT-AI-00`)<br>[`AI/SRT_AI_01_Ontology.md`](AI/SRT_AI_01_Ontology.md) (`SRT-AI-01`)<br>[`AI/SRT_AI_02_Mortality_Wisdom.md`](AI/SRT_AI_02_Mortality_Wisdom.md) (`SRT-AI-02`)<br>[`AI/SRT_AI_03_Consciousness_Framework.md`](AI/SRT_AI_03_Consciousness_Framework.md) (`SRT-AI-03`)<br>[`AI/SRT_AI_Architecture.md`](AI/SRT_AI_Architecture.md) (`SRT-AI-ARCH`) |
| Experiment | - | [`SRT_EXP_PRIORITY_MATRIX.md`](SRT_EXP_PRIORITY_MATRIX.md) (`SRT-EXP-PRIORITY`)<br>[`SRT_EXP_TEMPLATE.md`](SRT_EXP_TEMPLATE.md) (`SRT-EXP-TEMPLATE`)<br>[`SRT_EXP_MEASURE_MAP.md`](SRT_EXP_MEASURE_MAP.md) (`SRT-EXP-MEASUREMAP`) |
| Project | - | [`SRT_OPTIMIZATION_BACKLOG.md`](SRT_OPTIMIZATION_BACKLOG.md) (`SRT-BACKLOG`) |
<!-- AUTO:ENTRYPOINTS:END -->


> 最新更新：2026-01-31（draft_*.md 七文档融合完成）| 上次索引优化：2026-01-31

## 📜 历史增量与版本记录

- 历史理论增量（含批次合并记录）已迁移至：[`_SRT_CHANGELOG_2026.md`](_SRT_CHANGELOG_2026.md)
- 主索引仅保留导航/入口/注册信息，以提升可维护性与 AI 检索稳定性。

## 🧰 Documentation Governance Hub（治理入口）

### 规划与流程
- 总体优化计划：[`SRT_INTERNAL_OPTIMIZATION_PLAN_2026Q1.md`](SRT_INTERNAL_OPTIMIZATION_PLAN_2026Q1.md)
- 解释协议（Definition→Mechanism→Falsification）：[`_SRT_EXPLANATION_PROTOCOL.md`](_SRT_EXPLANATION_PROTOCOL.md)
- 方程-假设映射：[`_SRT_EQ_HYP_MAP.md`](_SRT_EQ_HYP_MAP.md)
- 领域文档模板：[`_SRT_DOMAIN_TEMPLATE.md`](_SRT_DOMAIN_TEMPLATE.md)
- diff 管线规范：[`_SRT_DIFF_PIPELINE_GUIDE.md`](_SRT_DIFF_PIPELINE_GUIDE.md)

### 质量与发布
- Frontmatter 审计：[`_SRT_FRONTMATTER_AUDIT.md`](_SRT_FRONTMATTER_AUDIT.md)
- 质量评分卡：[`_SRT_QUALITY_SCORECARD.md`](_SRT_QUALITY_SCORECARD.md)
- 自动指标快照：[`_SRT_QUALITY_METRICS.md`](_SRT_QUALITY_METRICS.md)
- 解释链审计：[`_SRT_EXPLAINABILITY_AUDIT.md`](_SRT_EXPLAINABILITY_AUDIT.md)
- Release 模板：[`_SRT_RELEASE_NOTE_TEMPLATE.md`](_SRT_RELEASE_NOTE_TEMPLATE.md)
- 最新发布快照：[`_SRT_RELEASE_2026-02.md`](_SRT_RELEASE_2026-02.md)
- 减肥变更日志：[`_SRT_SLIMMING_CHANGELOG_2026-02.md`](_SRT_SLIMMING_CHANGELOG_2026-02.md)
- 执行总控：[`_SRT_EXECUTION_PLAN.md`](_SRT_EXECUTION_PLAN.md)
- 论文流水线：[`_SRT_PAPER_PIPELINE.md`](_SRT_PAPER_PIPELINE.md)
- 情报流水线：[`_SRT_SIGNAL_PIPELINE.md`](_SRT_SIGNAL_PIPELINE.md)
- 治理流水线：[`_SRT_GOVERNANCE_PIPELINE.md`](_SRT_GOVERNANCE_PIPELINE.md)
- 媒体流水线：[`_SRT_MEDIA_PIPELINE.md`](_SRT_MEDIA_PIPELINE.md)
- 运行节奏：[`_SRT_OPERATIONS_SCHEDULE.md`](_SRT_OPERATIONS_SCHEDULE.md)
