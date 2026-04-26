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
| `_SRT_CONTEXT_ROUTER.md` | 深层问题上下文抓取路由 |
| `_SRT_DEEP_THEORY_MAP.md` | 深层理论节点地图 |
| `_SRT_HIGH_PRIORITY_CORE_COVERAGE_INDEX.md` | 高优先级 Core/Core_Law 覆盖索引 |
| `_SRT_MEDIUM_AI_NEURO_COVERAGE_INDEX.md` | 中优先级 AI/Neuroscience 覆盖索引 |
| `_SRT_MEDIUM_PHILOSOPHY_COVERAGE_INDEX.md` | 中优先级 Philosophy 覆盖索引 |
| `_SRT_MEDIUM_PHYSICS_COVERAGE_INDEX.md` | 中优先级 Physics 覆盖索引 |
| `_SRT_MEDIUM_SPIRITUALITY_COVERAGE_INDEX.md` | 中优先级 Spirituality 覆盖索引 |
| `_SRT_MEDIUM_PAPERS_PUBLICATION_COVERAGE_INDEX.md` | 中优先级 Papers/Publication 覆盖索引 |
| `_SRT_MEDIUM_ROOT_TOPIC_FAQ_COVERAGE_INDEX.md` | 中优先级 Root Topic/FAQ 覆盖索引 |

## Default Read Order

### AI / Agent

1. `AGENTS.md`
2. `SRT_AI_START.md`
3. `STATUS.md`
4. `_SRT_INDEX.md`
5. `_SRT_SYMBOL_TABLE.md`
6. `_SRT_CONTEXT_ROUTER.md`（deep questions only）
7. `_SRT_DEEP_THEORY_MAP.md`（cross-domain theory questions only）
8. `_SRT_HIGH_PRIORITY_CORE_COVERAGE_INDEX.md`（coverage-audit follow-up only）
9. `_SRT_MEDIUM_AI_NEURO_COVERAGE_INDEX.md`（AI / neuroscience coverage-audit follow-up only）
10. `_SRT_MEDIUM_PHILOSOPHY_COVERAGE_INDEX.md`（philosophy coverage-audit follow-up only）
11. `_SRT_MEDIUM_PHYSICS_COVERAGE_INDEX.md`（physics coverage-audit follow-up only）
12. `_SRT_MEDIUM_SPIRITUALITY_COVERAGE_INDEX.md`（spirituality coverage-audit follow-up only）
13. `_SRT_MEDIUM_PAPERS_PUBLICATION_COVERAGE_INDEX.md`（papers / publication coverage-audit follow-up only）
14. `_SRT_MEDIUM_ROOT_TOPIC_FAQ_COVERAGE_INDEX.md`（root topic / FAQ coverage-audit follow-up only）

### Human / Public

1. `README.md`
2. `SRT_Quick_Start.md`
3. `SRT_1H_Onboarding.md`
4. `SRT_Navigation_Map.md`

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

## Registry Layer

- canonical registry → `CANONICAL_REGISTRY.md`
- annex registry → `ANNEX_REGISTRY.md`
- longform split registry → `LONGFORM_SPLITS.md`
- glossary → `SRT_Glossary.md`
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
- collective selection / multi-ISP shared L_2 / consequence return matrix M(t) / aggregation-dominance-collapsed / collective ε / co-selection reality criterion / collective four-variable coupled ODE (σ^coll, d_c^coll, T_dir^coll, S^coll) / collective lethal L_2 criterion / individual-collective bidirectional coupling / **T-PROJ-1^{coll} collective projection theorem (H6, §4.7)** / **T-PROJ-1^{coll,nested} nested-ISP recursive projection (H10, §4.8)** / **T-FAMILY-1^{coll} collective extension of T-CHI-1/T-CHANNEL-1/T-DELTA-1 (H11, §4.9)** / **T-FAMILY-1^{coll,nested} tower-level recursion of family-universality trio (H12, §4.10)** / **T-TOWER-STAB-1 self-referential closure spectral stability (H13, §4.11)** / **T-LAYER-SKIP-1 layer-skip + multiple closure unified spectral criterion (H14, §4.12)** / **T-FAMILY-1^{layer-skip} triple Cartesian product (H15, §4.13)** / **T-LYAPUNOV-1 global nonlinear tower stability (H16, §4.14)** → `Core_Law/SRT_Collective_Selection.md`
- L1 hardening notes (σ_sr namespace / Δ_avail three-component / **T-DELTA-1 operator-level theorem (H7, §2)** / M(t) MOC / FEP→S_sig bridge) → `Core_Law/SRT_L1_Hardening_Notes.md`
- irreversibility / learning asymmetry / termination as absorbing boundary / P1-T07 precision / `\nu_{block}` operator-level constitution (T-IRR-3.5, H4) / thermodynamic bridge guardrail → `Core_Law/SRT_Irreversibility.md`
- bridge hypotheses → `Core/SRT_Core_21c_Bridge_Hypotheses.md`
- equations → `Core/SRT_Core_22_Equations.md`
- open tensions → `Core/SRT_OPEN_TENSIONS.md`

## Domain Entrypoints

### Core

- `Core/_SRT_Core_Bridge.md`
- `Core/SRT_Core_21_Formal_Axioms.md`
- `Core/SRT_Core_21_Minimal_Axioms.md`
- `Core/SRT_Core_21b_Constitutive_Theorems.md`
- `Core/SRT_Core_21c_Bridge_Hypotheses.md`
- `Core/SRT_Core_22_Equations.md`
- `Core/SRT_Core_23_IG_Complexity_Neuro_Hardening.md`（bridge hardening entry; not a canonical core source）
- `Core/SRT_OPEN_TENSIONS.md`

### Meta Navigation

- `_SRT_CONTEXT_ROUTER.md`（query-type retrieval router; not a canonical source）
- `_SRT_DEEP_THEORY_MAP.md`（deep theory node map; not a canonical source）
- `_SRT_HIGH_PRIORITY_CORE_COVERAGE_INDEX.md`（coverage-audit follow-up for Core/Core_Law high-priority files; not a canonical source）
- `_SRT_MEDIUM_AI_NEURO_COVERAGE_INDEX.md`（coverage-audit follow-up for AI/Neuroscience medium-priority files; not a canonical source）
- `_SRT_MEDIUM_PHILOSOPHY_COVERAGE_INDEX.md`（coverage-audit follow-up for Philosophy medium-priority files; not a canonical source）
- `_SRT_MEDIUM_PHYSICS_COVERAGE_INDEX.md`（coverage-audit follow-up for Physics medium-priority files; not a canonical source）
- `_SRT_MEDIUM_SPIRITUALITY_COVERAGE_INDEX.md`（coverage-audit follow-up for Spirituality medium-priority files; not a canonical source）
- `_SRT_MEDIUM_PAPERS_PUBLICATION_COVERAGE_INDEX.md`（coverage-audit follow-up for papers / publication medium-priority files; not a canonical source）
- `_SRT_MEDIUM_ROOT_TOPIC_FAQ_COVERAGE_INDEX.md`（coverage-audit follow-up for root topic / FAQ medium-priority files; not a canonical source）

### Bridge / Interface

- `Bridge/SRT_Adjacent_Theory_Interface_Index.md`（navigation index for adjacent-theory interfaces; not a canonical core source）

### AI

- `AI/_SRT_AI_Bridge.md`
- `AI/AI_POSITIONING_NOTE.md`
- `AI/SRT_AI_01_Ontology_CompactCore.md`
- `AI/SRT_AI_03_Consciousness_Framework_CompactCore.md`

### Neuroscience

- `Neuroscience/_SRT_Neuro_Axioms.md`
- `Neuroscience/SRT_Neural_Mechanisms_CompactCore.md`
- `Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md`

### Physics

- `Physics/_SRT_Phys_Bridge.md`
- `Physics/PHYSICS_COMPACT_REGISTRY.md`
- `Physics/SRT_Physics_Cosmology_CompactCore.md`

### Philosophy

- `Philosophy/_SRT_Phil_Axioms.md`
- `Philosophy/SRT_Philosophy_Foundations_CompactCore.md`
- `Philosophy/SRT_Social_Economics_CompactCore.md`
- `Philosophy/SRT_Political_Philosophy_CompactCore.md`
- `Philosophy/SRT_Political_Philosophy.md`
- `Philosophy/SRT_Political_Rights.md`

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

## Archives

- raw sessions → `Archive/raw_sessions/`
- status history → `Operations/_SRT_STATUS_HISTORY.md`

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
- `_SRT_MEDIUM_ROOT_TOPIC_FAQ_COVERAGE_INDEX.md` 是 coverage audit 后续索引，只处理 root topic / FAQ 中优先级候选，不提升 canonical 权限
- `Bridge/SRT_Adjacent_Theory_Interface_Index.md` 是相邻理论接口导航，不新增 P0/P1，不替代 FEP/IIT/GNW/量子/社会现实等既有正文
- `Operations/_SRT_DEEP_NAV_TODO.md` 是持续维护计划，不是理论主文
- Spirituality 板块现采用“旧主轴 + 新双线 + community companion”并行：旧主轴负责 axioms / praxis compact core；新双线负责主体位丢失、现代生活反思与回返路径；community companion 负责共同体如何托住回返而不重新变成地板
