---
id: SRT-CANONICAL-FREEZE
type: framework
tags: [Governance, Canonical, Freeze, EditSafety]
status: active_v2
layer: meta
epistemic_layer: os
claim_mode: governance
canonical: false
dependency: [SRT-CANONICAL-REGISTRY, SRT-SYMBOL-TABLE]
updated: 2026-06-05
---

# SRT Canonical Freeze

> 2026-06-05 scope note: this file is an edit-safety policy. It does not define SRT terms and does not replace `CANONICAL_REGISTRY.md`, `_SRT_SYMBOL_TABLE.md`, or current manuscript files.

本文件用于明确：

- 哪些文件当前属于 **不可直接改写的 canonical 锚点**
- 哪些文件可改但必须 cross-check
- 哪些文件属于运行/导航层，可调整但不得偷渡新理论口径

## A. 不可直接改写的 canonical 锚点

以下文件默认不做无明确授权的正文重写：

- `Core_Law/SRT_L0_Metaphysics.md`
- `_SRT_D_VALUE_CANONICAL.md`
- `_SRT_PSI_F_CANONICAL.md`
- `_SRT_T_DIR_CANONICAL.md`
- `_SRT_SYMBOL_TABLE.md`
- `Core/SRT_Core_21_Formal_Axioms.md`
- `Core/SRT_Core_21_Minimal_Axioms.md`
- `Core/SRT_Core_21b_Constitutive_Theorems.md`
- `Core/SRT_Core_21c_Bridge_Hypotheses.md`
- `Core/SRT_Core_22_Equations.md`

默认规则：

- 允许修 typo、断链、格式错误
- 不允许静默改定义、改判据、改 canonical 优先级
- 若必须改正文，需明确标注为高风险编辑

## B. 可改但必须 cross-check 的核心主文

以下文件允许收紧口径、补 Quick Reference、补回链、补边界说明，但不得与 canonical 锚点冲突：

- `Core_Law/SRT_Core_Text_CN_Euclid.md`
- `Core_Law/SRT_Core_Text_CN.md`
- `Core_Law/SRT_Selection_Argument.md`
- `Core/SRT_Core_14_Dynamics_Scaling.md`
- `AI/SRT_AI_01_Ontology.md`
- `AI/SRT_AI_03_Consciousness_Framework.md`
- `Philosophy/SRT_Philosophy_Foundations.md`
- `Neuroscience/SRT_Neural_Mechanisms.md`
- `Neuroscience/SRT_Consciousness_Mechanisms.md`
- `Physics/SRT_Physics_Cosmology.md`

最小要求：

- 先核 `_SRT_SYMBOL_TABLE.md`
- 先核对应 canonical 文件
- 再核本文件在主入口层中的角色

## C. 运行 / 导航 / 状态文件

以下文件允许按仓库工程目标持续调整：

- `README.md`
- `AGENTS.md`
- `CLAUDE.md`
- `SRT_AI_START.md`
- `STATUS.md`
- `_SRT_INDEX.md`
- `_SRT_AGENT_RETRIEVAL_PROFILE.md`
- `_SRT_SYMBOL_QUICK_GUARD.md`
- `SRT_Navigation_Map.md`
- `_SRT_MANIFEST.yaml`
- `Operations/README.md`
- `Governance/README.md`
- `memory/README.md`

但这些文件必须遵守：

- 不引入与 canonical 冲突的新理论口径
- 不把 bridge / split / ops log 升格成定义源
- 不替 canonical 文件重新定义核心术语

## D. 当前 round 明确不做

本轮仓库优化不做：

- 大规模正文删改
- canonical 数学定义重写
- 大批量文件重命名
- 大规模目录搬迁
- 让 README 承担运行协议职责
- 再造第二套 AI harness

## E. 判定原则

若一个改动同时影响：

- 术语定义
- canonical 优先级
- 核心方程/公理
- 主论证关键链条

则默认为高风险改动，先按 [SRT_EDIT_PROTOCOL.md](SRT_EDIT_PROTOCOL.md) 处理。
