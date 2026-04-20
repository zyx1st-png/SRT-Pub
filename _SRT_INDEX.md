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

## Default Read Order

### AI / Agent

1. `AGENTS.md`
2. `SRT_AI_START.md`
3. `STATUS.md`
4. `_SRT_INDEX.md`
5. `_SRT_SYMBOL_TABLE.md`

### Human / Public

1. `README.md`
2. `SRT_Quick_Start.md`
3. `SRT_1H_Onboarding.md`
4. `SRT_Navigation_Map.md`

## Authority Order

默认权威顺序：

1. `CANONICAL_REGISTRY.md`
2. `Governance/SRT_CLAIM_LADDER.md`
3. `Core_Law/SRT_L0_Metaphysics.md`
4. `_SRT_D_VALUE_CANONICAL.md`
5. `_SRT_PSI_F_CANONICAL.md`
6. `_SRT_T_DIR_CANONICAL.md`
7. `_SRT_SYMBOL_TABLE.md`
8. `Core/SRT_Core_21_Formal_Axioms.md`
9. `Core/SRT_Core_22_Equations.md`

以下层默认不承担最终定义权：

- bridge
- split / annex 导航层
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
- d-value → `_SRT_D_VALUE_CANONICAL.md`
- `Ψ_f` → `_SRT_PSI_F_CANONICAL.md`
- `T_dir` → `_SRT_T_DIR_CANONICAL.md`
- formal axioms → `Core/SRT_Core_21_Formal_Axioms.md`
- minimal axioms → `Core/SRT_Core_21_Minimal_Axioms.md`
- constitutive theorems → `Core/SRT_Core_21b_Constitutive_Theorems.md`
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
- `Core/SRT_OPEN_TENSIONS.md`

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

### Spirituality

- `Spirituality/_SRT_Spirit_Axioms.md`
- `Spirituality/SPIRITUALITY_COMPACT_REGISTRY.md`
- `Spirituality/SRT_Spirit_09_Praxis_CompactCore.md`
- `Spirituality/SRT_Spirituality_Selection_Pathology_and_Return.md`
- `Spirituality/SRT_Spirituality_How_We_Lose_Ourselves_and_Return.md`

## Governance / Runtime

- governance hub → `Governance/README.md`
- operations hub → `Operations/README.md`
- schedule → `Operations/_SRT_OPERATIONS_SCHEDULE.md`
- freeze policy → `Governance/SRT_CANONICAL_FREEZE.md`
- edit protocol → `Governance/SRT_EDIT_PROTOCOL.md`
- claim ladder → `Governance/SRT_CLAIM_LADDER.md`
- harness tests → `Governance/SRT_HARNESS_TESTS.md`

## Archives

- raw sessions → `Archive/raw_sessions/`
- status history → `Operations/_SRT_STATUS_HISTORY.md`

## Machine Notes

- `_SRT_MANIFEST.yaml` 是机器清单，不是 canonical 理论主文
- `SRT_Navigation_Map.md` 是人类阅读地图，不是 registry 摘要
- `STATUS.md` 现在只保留当前状态，不再承载长历史
- `Core/SRT_Core_21_Formal_Axioms.md` 现在是 Core_21 claim-layer index，不再是混层公理正文
- Spirituality 板块现采用“旧主轴 + 新双线展开”并行：旧主轴负责 axioms / praxis compact core；新双线负责主体位丢失、现代生活反思与回返路径的独立 spiritual 组织
