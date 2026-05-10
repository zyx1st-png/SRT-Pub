---
id: SRT-INDEX
type: framework
tags: [Index, Registry, Navigation]
status: active_v2
layer: meta
claim_mode: canonical
epistemic_layer: os
dependency: [_SRT_MANIFEST, SRT-GLOSSARY]
---

# SRT Machine Index

本文件只做三件事：

1. 固定入口面分工
2. 固定权威层级与注册表关系
3. 提供最短机器可读路径表

它不是：

- 完整历史日志
- 人类阅读地图
- 运行协议主文件

## Entry Surfaces

| Surface | Role |
|:--|:--|
| `README.md` | 公开入口 |
| `AGENTS.md` | 运行协议主入口 |
| `CLAUDE.md` | Claude 兼容包装层 |
| `SRT_AI_START.md` | AI 最小首读入口 |
| `STATUS.md` | 当前状态面板 |
| `SRT_Navigation_Map.md` | 人类阅读地图 |
| `_SRT_INDEX.md` | 机器索引 |
| `_SRT_SYMBOL_TABLE.md` | 符号规范锚点 |
| `_SRT_AGENT_RETRIEVAL_PROFILE.md` | Agent 检索扩展协议：区分 authority 与 retrieval value |
| `_SRT_CONTEXT_ROUTER.md` | 深层问题上下文抓取路由 |
| `_SRT_DEEP_THEORY_MAP.md` | 深层理论节点地图 |
| `_SRT_HIGH_PRIORITY_CORE_COVERAGE_INDEX.md` | 高优先级 Core/Core_Law 覆盖索引 |
| `_SRT_MEDIUM_AI_NEURO_COVERAGE_INDEX.md` | 中优先级 AI/Neuroscience 覆盖索引 |
| `_SRT_MEDIUM_PHILOSOPHY_COVERAGE_INDEX.md` | 中优先级 Philosophy 覆盖索引 |
| `_SRT_MEDIUM_PHYSICS_COVERAGE_INDEX.md` | 中优先级 Physics 覆盖索引 |
| `_SRT_MEDIUM_SPIRITUALITY_COVERAGE_INDEX.md` | 中优先级 Spirituality 覆盖索引 |
| `_SRT_MEDIUM_PAPERS_PUBLICATION_COVERAGE_INDEX.md` | 中优先级 Papers/Publication 覆盖索引 |
| `_SRT_MEDIUM_ROOT_TOPIC_FAQ_COVERAGE_INDEX.md` | 中优先级 Root Topic/FAQ 覆盖索引 |
| `Manifesto/SRT_MANIFESTO.md` | 公开宣言（`claim_mode: manifesto`，非 canonical 主源） |

## Default Read Order

### AI / Agent

1. `AGENTS.md`
2. `SRT_AI_START.md`
3. `STATUS.md`
4. `_SRT_INDEX.md`
5. `_SRT_SYMBOL_TABLE.md`
6. `_SRT_AGENT_RETRIEVAL_PROFILE.md`（non-trivial theory / book / domain / public / governance tasks）
7. `_SRT_CONTEXT_ROUTER.md`（any non-simple SRT question; required for deep questions）
8. `_SRT_DEEP_THEORY_MAP.md`（cross-domain theory questions）
9. `_SRT_HIGH_PRIORITY_CORE_COVERAGE_INDEX.md`（coverage-audit follow-up / missed core context）
10. `_SRT_MEDIUM_AI_NEURO_COVERAGE_INDEX.md`（AI / neuroscience coverage-audit follow-up）
11. `_SRT_MEDIUM_PHILOSOPHY_COVERAGE_INDEX.md`（philosophy coverage-audit follow-up）
12. `_SRT_MEDIUM_PHYSICS_COVERAGE_INDEX.md`（physics coverage-audit follow-up）
13. `_SRT_MEDIUM_SPIRITUALITY_COVERAGE_INDEX.md`（spirituality coverage-audit follow-up）
14. `_SRT_MEDIUM_PAPERS_PUBLICATION_COVERAGE_INDEX.md`（papers / publication coverage-audit follow-up）
15. `_SRT_MEDIUM_ROOT_TOPIC_FAQ_COVERAGE_INDEX.md`（root topic / FAQ coverage-audit follow-up）
16. `Philosophy/00_READ_FIRST_Philosophy_Hardening_Soft_Spots.md`（philosophy deep-hardening / objection-led edits）

### Human / Public

1. `README.md`
2. `Manifesto/SRT_MANIFESTO.md`（worldview-level center sentence；`claim_mode: manifesto`，不替代 canonical core）
3. `SRT_Quick_Start.md`
4. `SRT_1H_Onboarding.md`
5. `SRT_Navigation_Map.md`
6. `Philosophy/00_READ_FIRST_Philosophy_Hardening_Soft_Spots.md`（when reading or editing the Philosophy folder）

## Authority Order

默认权威顺序：

1. `CANONICAL_REGISTRY.md`
2. `Governance/SRT_CLAIM_LADDER.md`
3. `Governance/SRT_CLAIM_MODE_AUDIT.md`
4. `Core_Law/SRT_L0_Metaphysics.md`
5. `_SRT_D_VALUE_CANONICAL.md`
6. `_SRT_PSI_F_CANONICAL.md`
7. `_SRT_T_DIR_CANONICAL.md`
8. `_SRT_CROSS_DOMAIN_MATRIX.md`
9. `_SRT_SYMBOL_TABLE.md`
10. `Core/SRT_Core_21_Formal_Axioms.md`
11. `Core/SRT_Core_22_Equations.md`

以下层默认不承担最终定义权：

- bridge
- split / annex 导航层
- context router / deep theory map
- coverage indexes
- `Operations/` 日志
- `memory/`

Important retrieval note: "not final definition authority" is not the same as "low retrieval value." For agent context loading, use `_SRT_AGENT_RETRIEVAL_PROFILE.md`.

## Registry Layer

- canonical registry → `CANONICAL_REGISTRY.md`
- annex registry → `ANNEX_REGISTRY.md`
- longform split registry → `LONGFORM_SPLITS.md`
- agent retrieval profile → `_SRT_AGENT_RETRIEVAL_PROFILE.md`
- glossary → `SRT_Glossary.md`
- structural governance glossary → `SRT_Glossary_Structural_Governance_Terms.md`
- manifest → `_SRT_MANIFEST.yaml`

## Canonical Theory Anchors

- L0 → `Core_Law/SRT_L0_Metaphysics.md`
- Chinese core text candidate → `Core_Law/SRT_Core_Text_CN_Euclid.md`
- claim ladder → `Governance/SRT_CLAIM_LADDER.md`
- claim-mode audit → `Governance/SRT_CLAIM_MODE_AUDIT.md`
- d-value → `_SRT_D_VALUE_CANONICAL.md`
- `Ψ_f` → `_SRT_PSI_F_CANONICAL.md`
- `T_dir` → `_SRT_T_DIR_CANONICAL.md`
- cross-domain usage matrix → `_SRT_CROSS_DOMAIN_MATRIX.md`
- formal axioms → `Core/SRT_Core_21_Formal_Axioms.md`
- minimal axioms → `Core/SRT_Core_21_Minimal_Axioms.md`
- constitutive theorems → `Core/SRT_Core_21b_Constitutive_Theorems.md`
- individuation / ISP entry / self-consciousness condensate → `Core_Law/SRT_Individuation.md`
- occlusion dynamics / A-B phases / d_c / intervention window / vacuum period / structural evil → `Core_Law/SRT_Occlusion_Dynamics.md`
- suffering / pain vs suffering / signal-vs-structural / four phenomenological types / anti-minimization / collective externalization → `Core_Law/SRT_Suffering.md`
- L1 formalism / σ dynamics / d_c drift / T_dir ODE (relaxation + real-reselection pump + Ψ_f-gap deduction + S_str erosion + L_2 scaffolding) / S coupled equations / pathological attractor / healthy working region / lethal L_2 equation-level criterion / **T-CHI-1 χ jump-function family universality (H8, §2.5)** / **T-CHANNEL-1 channel-indicator family universality (H9, §4.5)** / **T-PROJ-1 main-equation projection theorem (H5, §6)** → `Core_Law/SRT_L1_Formalism.md`
- collective selection / multi-ISP shared L_2 / consequence return matrix M(t) / aggregation-dominance-collapsed / collective ε / co-selection reality criterion / collective four-variable coupled ODE (σ^coll, d_c^coll, T_dir^coll, S^coll) / collective lethal L_2 criterion / individual-collective bidirectional coupling / **T-PROJ-1^{coll} collective projection theorem (H6, §4.7)** / minimal canonical collective-selection surface through §4.7. Tower/nested hardening H10-H16 has been extracted to `Core_Law/SRT_Collective_Tower_Hardening_Notes.md` → `Core_Law/SRT_Collective_Selection.md`
- L1 hardening notes (σ_sr namespace / Δ_avail three-component / **T-DELTA-1 operator-level theorem (H7, §2)** / M(t) MOC / FEP→S_sig bridge) → `Core_Law/SRT_L1_Hardening_Notes.md`
- irreversibility / learning asymmetry / termination as absorbing boundary / P1-T07 precision / `\nu_{block}` operator-level constitution (T-IRR-3.5, H4) / thermodynamic bridge guardrail → `Core_Law/SRT_Irreversibility.md`
- bridge hypotheses → `Core/SRT_Core_21c_Bridge_Hypotheses.md`
- equations → `Core/SRT_Core_22_Equations.md`
- open tensions → `Core/SRT_OPEN_TENSIONS.md`

## Secondary Hardening Notes

- collective tower/nested hardening H10-H16 / late-stage hardening only / P1-candidate under strong closure assumptions / not a primary canonical anchor → `Core_Law/SRT_Collective_Tower_Hardening_Notes.md`
- floor replacement / object-first ontology critique / purpose-value-morality-framework dynamics / non-reductive validation / Ψ_f-d-L2 operational projections / reviewer-risk guardrails → `Core/SRT_Core_24_Floor_Normativity_Verification.md`
- retrieval index for Core 24 floor replacement and non-reductive verification note → `Core/SRT_Core_24_Index.md`
- philosophy soft spots / selection realism / layered realism / anti-idealism / anti-relativism / Psi_f layering / d-value philosophy / normativity generation / social ontology / consciousness threshold / non-reductive validation → `Philosophy/00_READ_FIRST_Philosophy_Hardening_Soft_Spots.md`

## Domain Entrypoints

### Core

- `Core/_SRT_Core_Bridge.md`
- `Core/SRT_Core_21_Formal_Axioms.md`
- `Core/SRT_Core_21_Minimal_Axioms.md`
- `Core/SRT_Core_21b_Constitutive_Theorems.md`
- `Core/SRT_Core_21c_Bridge_Hypotheses.md`
- `Core/SRT_Core_22_Equations.md`
- `Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md`（bridge hardening entry; not a canonical core source）
- `Core/SRT_Core_24_Floor_Normativity_Verification.md`（bridge-hardening note for floor replacement, normativity, and non-reductive verification; not a canonical replacement）
- `Core/SRT_Core_24_Index.md`（navigation index for Core 24）
- `Core/SRT_OPEN_TENSIONS.md`
- `Core/Axioms_Split/README.md`、`Core/Ontology_L0L1_Split/README.md`、`Core/Ontology_L2_Split/README.md`、`Core/Operator_Basics_Split/README.md`、`Core/Dynamics_Scaling_Split/README.md`、`Core/Equations_Split/README.md`（longform split reading aids; not independent authority layers）

### Meta Navigation

- `_SRT_CONTEXT_ROUTER.md`（query-type retrieval router; not a canonical source）
- `_SRT_DEEP_THEORY_MAP.md`（deep theory node map; not a canonical source）
- `_SRT_HIGH_PRIORITY_CORE_COVERAGE_INDEX.md`（coverage-audit follow-up for Core/Core_Law high-priority files; not a canonical source）
- `_SRT_MEDIUM_AI_NEURO_COVERAGE_INDEX.md`（coverage-audit follow-up for AI/Neuroscience medium-priority files; not a canonical source）
- `_SRT_MEDIUM_PHILOSOPHY_COVERAGE_INDEX.md`（philosophy coverage-audit follow-up only; not a canonical source）
- `_SRT_MEDIUM_PHYSICS_COVERAGE_INDEX.md`（physics coverage-audit follow-up only; not a canonical source）
- `_SRT_MEDIUM_SPIRITUALITY_COVERAGE_INDEX.md`（spirituality coverage-audit follow-up only; not a canonical source）
- `_SRT_MEDIUM_PAPERS_PUBLICATION_COVERAGE_INDEX.md`（papers / publication coverage-audit follow-up only; not a canonical source）
- `_SRT_MEDIUM_ROOT_TOPIC_FAQ_COVERAGE_INDEX.md`（root topic / FAQ coverage-audit follow-up only; not a canonical source）

### Bridge / Interface

- `Bridge/SRT_Adjacent_Theory_Interface_Index.md`（navigation index for adjacent-theory interfaces; not a canonical core source）

### AI

- `AI/README.md`（directory entry; separates positioning, bridge, compact summaries, operational rubrics, split reading aids, and annex/interface material）
- `AI/SRT_AI_Claim_Status.md`（claim-status audit for AI-domain claims; prevents `d_AI`, AI suffering, subjecthood, and architecture-state claims from being over-read）
- `AI/AI_POSITIONING_NOTE.md`
- `AI/_SRT_AI_Bridge.md`
- `AI/SRT_AI_01_Ontology_CompactCore.md`
- `AI/SRT_AI_03_Consciousness_Framework_CompactCore.md`
- `AI/SRT_AI_Consciousness_Evaluation_Rubric.md`（operational rubric; not a canonical consciousness definition source）
- `AI/SRT_AI_Agency_Responsibility_Note.md`（operational agency / responsibility note）
- `AI/Ontology_Annex/README.md`（historical AI ontology interface batches; claim status governed by AI claim-status + positioning note）
- `AI/Architecture_Annex/README.md`（AI architecture interface/comparison annex; claim_mode: translation; canonical: false）
- `AI/Consciousness_Annex/README.md`（AI consciousness interface/comparison annex; claim_mode: translation; canonical: false）
- `AI/Ontology_Split/README.md`、`AI/Consciousness_Framework_Split/README.md`、`AI/Architecture_Split/README.md`（longform split reading aids; not independent authority layers）
- `AI/Ontology_Annex/General_Boundary_Block_Split/README.md`（annex longform split reading aid; not an independent authority layer）

### Neuroscience

- `Neuroscience/README.md`（directory entry; separates canonical-facing material from bridge/lab hardening drafts）
- `Neuroscience/_SRT_Neuro_Axioms.md`
- `Neuroscience/SRT_Neuro_Axioms_Claim_Status.md`（claim-status audit for the neuro axiom bridge; not a replacement for the axiom file）
- `Neuroscience/SRT_Neural_Mechanisms_CompactCore.md`
- `Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md`
- `Neuroscience/_SRT_Neuroscience_Hardening_Index.md`（domain index for hardening drafts and Pipeline 1 neuroscience material patches; not a canonical source）
- `Neuroscience/SRT_Neuroscience_Hardening_N1_N9_v0_1.md`（bridge/lab working draft; not a canonical source）
- `Neuroscience_Annex/README.md`（bridge/interface annex index for extracted neuroscience comparison material; `canonical: false`, not a Core definition source）
- `Neuroscience/Neural_Mechanisms_Split/README.md`、`Neuroscience/Immune_Dist_Split/README.md`（longform split reading aids; not independent authority layers）

### Physics

- `Physics/README.md`（directory entry; separates canonical-facing material, bridge files, compact summaries, claim-status audit, and annex/interface material）
- `Physics/_SRT_Phys_Bridge.md`
- `Physics/PHYSICS_COMPACT_REGISTRY.md`
- `Physics/SRT_Physics_Cosmology_CompactCore.md`
- `Physics/SRT_Physics_Claim_Status.md`（claim-status audit for Physics-domain claims; prevents quantum, cosmology, and bridge claims from being over-read as P0/P1）
- `Physics/QBox_Annex/README.md`（QBox / hyperdecoherence interface annex; claim_mode: translation; canonical: false）
- `Physics/Earth_Accretion_Annex/README.md`（Earth accretion / reservoir-selection interface annex; claim_mode: translation; canonical: false）
- `Physics/Cosmology_Split/README.md`、`Physics/Formalism_Ext_Split/README.md`、`Physics/Selection_Split/README.md`、`Physics/Quant_02_Cosmology_Split/README.md`（longform split reading aids; not independent authority layers）

### Philosophy

- `Philosophy/00_READ_FIRST_Philosophy_Hardening_Soft_Spots.md`（read-first philosophy soft-point map; not a canonical definition source）
- `Philosophy/_SRT_Phil_Axioms.md`
- `Philosophy/SRT_Philosophy_Foundations_CompactCore.md`
- `Philosophy/SRT_Social_Cognition.md`
- `Philosophy/SRT_Social_Economics_CompactCore.md`
- `Philosophy/SRT_Political_Philosophy_CompactCore.md`
- `Philosophy/SRT_Political_Philosophy.md`
- `Philosophy/SRT_Political_Rights.md`
- `Philosophy/Foundations_Split/README.md`、`Philosophy/Ethics_Split/README.md`、`Philosophy/Ethics_Agency_Split/README.md`、`Philosophy/Social_Cognition_Split/README.md`、`Philosophy/Social_Economics_Split/README.md`、`Philosophy/Political_Philosophy_Split/README.md`、`Philosophy/Language_Eco_Split/README.md`、`Philosophy/L2_Dynamics_Split/README.md`（longform split reading aids; not independent authority layers）

### Spirituality

- `Spirituality/_SRT_Spirit_Axioms.md`
- `Spirituality/SPIRITUALITY_COMPACT_REGISTRY.md`
- `Spirituality/SRT_Spirit_09_Praxis_CompactCore.md`
- `Spirituality/SRT_Spirituality_Selection_Pathology_and_Return.md`
- `Spirituality/SRT_Spirituality_How_We_Lose_Ourselves_and_Return.md`
- `Spirituality/SRT_Spirituality_Community_and_Sangha.md`

## Governance / Runtime

- governance hub → `Governance/README.md`
- operations hub → `Operations/README.md`
- schedule → `Operations/_SRT_OPERATIONS_SCHEDULE.md`
- deep navigation TODO → `Operations/_SRT_DEEP_NAV_TODO.md`
- freeze policy → `Governance/SRT_CANONICAL_FREEZE.md`
- edit protocol → `Governance/SRT_EDIT_PROTOCOL.md`
- claim ladder → `Governance/SRT_CLAIM_LADDER.md`
- claim-mode audit → `Governance/SRT_CLAIM_MODE_AUDIT.md`
- harness tests → `Governance/SRT_HARNESS_TESTS.md`
- 2026 changelog split index → `Governance/_SRT_CHANGELOG_2026_Split/README.md`
- material log split index → `Operations/Material_Log/README.md`
- status history split index → `Operations/Status_History/README.md`
- current status split index → `STATUS_Split/README.md`
- large-file connector audit → `Operations/Large_File_Audit_2026-05-09.md`
- AI split / annex pre-audit → `Operations/AI_Split_Annex_PreAudit_2026-04-29.md`
- operations closure index → `Operations/Closure_Index_2026-04-29.md`
- structural governance rollup → `Operations/Structural_Governance_Rollup_2026-04-29.md`

## Archives

- raw sessions → `Archive/raw_sessions/`
- status history → `Operations/_SRT_STATUS_HISTORY.md`（connector-safe dated parts in `Operations/Status_History/README.md`）

## Machine Notes

- `_SRT_MANIFEST.yaml` 是机器清单，不是 canonical 理论主文
- `SRT_Navigation_Map.md` 是人类阅读地图，不是 registry 摘要
- `STATUS.md` 现在只保留当前状态，不再承载长历史
- `Core/SRT_Core_21_Formal_Axioms.md` 现在是 Core_21 claim-layer index，不再是混层公理正文
- `_SRT_CONTEXT_ROUTER.md` 是深层问题的上下文抓取路由，不新增定义权
- `_SRT_DEEP_THEORY_MAP.md` 是深层理论节点地图，不替代 canonical 文件
- `_SRT_HIGH_PRIORITY_CORE_COVERAGE_INDEX.md` 是 coverage audit 后续索引，只处理 Core/Core_Law 高优先级候选，不提升 canonical 权限
- `_SRT_MEDIUM_AI_NEURO_COVERAGE_INDEX.md` 是 coverage audit 后续索引，只处理 AI/Neuroscience 中优先级候选，不提升 canonical 权限
- `_SRT_MEDIUM_PHILOSOPHY_COVERAGE_INDEX.md` 是 coverage audit 后续索引，只处理 Philosophy 中优先级候选，不提升 canonical 权限
- `_SRT_MEDIUM_PHYSICS_COVERAGE_INDEX.md` 是 coverage audit 后续索引，只处理 Physics 中优先级候选，不提升 canonical 权限
- `_SRT_MEDIUM_SPIRITUALITY_COVERAGE_INDEX.md` 是 coverage audit 后续索引，只处理 Spirituality 中优先级候选，不提升 canonical 权限
- `_SRT_MEDIUM_PAPERS_PUBLICATION_COVERAGE_INDEX.md` 是 coverage audit 后续索引，只处理 papers / publication 中优先级候选，不提升 canonical 权限
- `_SRT_MEDIUM_ROOT_TOPIC_FAQ_COVERAGE_INDEX.md` 是 coverage audit 后续索引，只处理 root topic / FAQ 候选，不提升 canonical 权限
- `Bridge/SRT_Adjacent_Theory_Interface_Index.md` 是相邻理论接口导航，不新增 P0/P1，不替代 FEP/IIT/GNW/量子/社会现实等既有正文
- `Core/SRT_Core_24_Floor_Normativity_Verification.md` is a bridge-hardening supplement for floor replacement, dynamic normativity, and non-reductive verification; it does not outrank canonical anchors until promoted through claim governance.
- `Core/SRT_Core_24_Index.md` is a retrieval index for Core 24 and does not define theory.
- `Philosophy/00_READ_FIRST_Philosophy_Hardening_Soft_Spots.md` is the read-first Philosophy hardening map for soft points and additions; it is machine-readable and human-readable but does not define P0/P1 canonical terms.
- `Operations/_SRT_DEEP_NAV_TODO.md` 是持续维护计划，不是理论主文
- `AI/README.md` 是 AI 目录入口，不定义 AI 意识、d-value 或 `Psi_f`
- `AI/SRT_AI_Claim_Status.md` 是 AI 领域 claim-status 审计与 guardrail；它不替代 `_SRT_AI_Bridge.md` 或 canonical anchors，但用于防止整类 AI claim 被过度读成 P0/P1 定义
- `AI/*_Split/`、`AI/Ontology_Annex/*_Split/`、`Core/*_Split/`、`Core_Law/*_Split/`、`Philosophy/*_Split/`、`Neuroscience/*_Split/`、`Physics/*_Split/`、`STATUS_Split/` 是 longform reading aids，不新增权威层；总表见 `LONGFORM_SPLITS.md`
- `AI/Ontology_Annex/` 与未来可能的 `AI_Annex/` 是 interface / comparison 层，默认 `canonical: false`
- `Neuroscience/SRT_Neuro_Axioms_Claim_Status.md` 是 `_SRT_Neuro_Axioms.md` 的 claim-status 审计与 guardrail；它不替代 axiom file，但用于防止整文件 canonical 误读
- `Neuroscience/SRT_Neuroscience_Hardening_N1_N9_v0_1.md` 是 neuroscience bridge/lab hardening 草稿；它不替代 `_SRT_Neuro_Axioms.md`，也不提升 canonical 权限
- Spirituality 板块现采用”旧主轴 + 新双线 + community companion”并行：旧主轴负责 axioms / praxis compact core；新双线负责主体位丢失、现代生活反思与回返路径；community companion 负责共同体如何托住回返而不重新变成地板
- `ANNEX_REGISTRY.md` 是各 annex 批次的注册总表，不定义 canonical 术语，不提升 annex 内容权限
- `SRT_Glossary_Structural_Governance_Terms.md` 是治理/结构操作层术语补充词汇表；`canonical: false`，不替代 `SRT_Glossary.md` 主体
- `Operations/Closure_Index_2026-04-29.md` 是 2026-04-29 各 annex / Physics / AI 批次的 closure 汇总索引；`canonical: false`，仅运行层留痕
- `Operations/Structural_Governance_Rollup_2026-04-29.md` 是结构治理 rollup 报告；`canonical: false`，仅运行层留痕
- `AI/Architecture_Annex/README.md` 是 AI 架构接口/对比 annex 的批次索引；`canonical: false`，claim status 受 `AI/SRT_AI_Claim_Status.md` 和 `AI/AI_POSITIONING_NOTE.md` 管控
- `AI/Consciousness_Annex/README.md` 是 AI 意识接口/对比 annex 的批次索引；`canonical: false`，claim status 受 `AI/SRT_AI_Claim_Status.md` 和 `AI/AI_POSITIONING_NOTE.md` 管控
- `Physics/README.md` 是 Physics 目录入口，分离 canonical-facing 材料、bridge、compact summaries、claim-status audit 和 annex 层，不定义 P0/P1 物理命题
- `Physics/SRT_Physics_Claim_Status.md` 是 Physics 领域 claim-status 审计与 guardrail；防止量子、宇宙学和 bridge 命题被过度读成 P0/P1
- `Physics/QBox_Annex/README.md` 是 QBox / hyperdecoherence 接口 annex 的批次索引；`canonical: false`，claim_mode: translation
- `Physics/Earth_Accretion_Annex/README.md` 是地球吸积 / reservoir-selection 接口 annex 的批次索引；`canonical: false`，claim_mode: translation
- `Manifesto/SRT_MANIFESTO.md` 是公开宣言（worldview-level front-edge）；`claim_mode: manifesto`，非 canonical 主源；遵循 `Governance/SRT_CLAIM_LADDER.md §2A`；human-first，不进 AI session bootstrap
