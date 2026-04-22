---
id: SRT-CANONICAL-REGISTRY
type: index
tags: [Canonical, Registry, Definitions, Equations]
status: active_v1
layer: meta
claim_mode: canonical
epistemic_layer: os
dependency: [SRT-INDEX, SRT-CLAIM-LADDER, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-CORE-22]
---

# SRT Canonical Registry

本页用于固定 SRT 当前应优先引用的 **canonical 主干层**。
原则：
- canonical 文件优先短、稳、少歧义
- 长文负责展开、推导、接口批次与历史沉积
- split 文件负责导航，不替代 canonical 定义

## 0. 定位说明（Epistemic Note）

- `canonical` 在本仓库内表示“当前内部优先引用的稳定锚点”，**不自动等于**“外部已证实的自然定律”。
- 自 `2026-03-17` 起，SRT 默认按 `OS / Bridge / Lab` 三层理解；详见 `Governance/SRT_POSITIONING.md`。
- 自 `2026-04-20` 起，SRT 额外按命题级硬度 `P0-P5` 管理；详见 `Governance/SRT_CLAIM_LADDER.md`。
- 本注册表中的大多数条目默认属于 **OS** 或 **Bridge**，用于收口词汇、语法与高阶接口；真正的硬赌点应优先沉淀到实验与假说文件，而不是混在 canonical 锚点里。

## A. 核心定义层（Definitions）

### 1. d-value
- 主锚点：`_SRT_D_VALUE_CANONICAL.md`
- 说明：统一 d-value 的第一性定义、域内投影、误用边界
- 引用规则：首次出现 d-value 时优先回链本文件

### 2. Ψ_f（本体论摩擦）
- 主锚点：`_SRT_PSI_F_CANONICAL.md`
- 说明：统一 `Ψ_f` 的第一性定义、几何主表达、可支付性条件与引力实现地位
- 引用规则：首次出现 `Ψ_f`、本体论摩擦、可支付性条件或“引力是否只是类比”时优先回链本文件

### 3. T_dir（方向透明度）与价值遮蔽
- 主锚点：`_SRT_T_DIR_CANONICAL.md`
- 说明（Part I §1-§10）：T_dir 是系统对自身选择秩序方向的可读性；统一价值遮蔽命题、Ψ_f_actual/Ψ_f_felt 分裂、致命 L₂ 机制的 canonical 表述
- 说明（Part II §11-§16）：扩展至价值动力学底层机制——L₂ 磁带/DNA 类比（§11）、三层价值结构（§12）、价值归纳 vs 理性归纳（§13）、时空对称性感知机制（§14）、价值作为暂时吸引子而非守恒结构（§15）、吸引子上升/退化动力学（§16）
- 引用规则：涉及方向透明度、意义感/虚无感的 SRT 机制解释、致命 L₂、价值遮蔽、三层价值结构、价值归纳、吸引子动力学时优先回链本文件
- 与 d-value 的关系：d 是 T_dir 的必要条件；两者独立，不互相替代

### 4. Core Axioms
- 主锚点：`Core/SRT_Core_21_Formal_Axioms.md`
- 分层正文：
  - P0 minimal axioms → `Core/SRT_Core_21_Minimal_Axioms.md`
  - P1 constitutive theorems → `Core/SRT_Core_21b_Constitutive_Theorems.md`
  - P2/P3/P4 bridge hypotheses → `Core/SRT_Core_21c_Bridge_Hypotheses.md`
- 说明：`Core_21_Formal_Axioms.md` 现在是形式公理索引，不再承载混层正文
- 引用规则：涉及核心公理编号时，先回链索引，再按命题硬度引用对应分层文件

### 4b. Core Equations
- 主锚点：`Core/SRT_Core_22_Equations.md`
- 说明：主动力学方程、热力学与稳定性方程主入口
- 引用规则：涉及主方程、选择热力学、稳定性条件时优先回链本文件

### 4c. Core Open Tensions
- 主文件：`Core/SRT_OPEN_TENSIONS.md`
- 说明：记录当前未完全封口的 core pressure points
- 引用规则：凡涉及其中 tension，不得包装成已完成 P0/P1

## B. 规范辅助层（Canonical Support）

### 5. 七命题宪法摘要层
- 文件：`Core_Law/SRT_Constitution_Seven_Theses.md`
- 角色：为 SRT 提供最短的元理论宪法摘要，用于对外解释、框架比较与自我收口
- 注意：它是顶层摘要，不替代 `Core_Law/SRT_Reference_Axioms.md`、`Core_Law/SRT_Reference_Ontology.md`、canonical 定义文件或主方程文件

### 5b. Claim Ladder
- 文件：`Governance/SRT_CLAIM_LADDER.md`
- 角色：定义 P0-P5 命题级硬度，防止 bridge / lab / companion 命题伪装成 primitive axiom 或 constitutive theorem
- 注意：它是治理机制，不新增理论命题

### 6. d-value 跨尺度展开
- 辅助文件：`Core/SRT_Core_14_Dynamics_Scaling.md`
- 角色：把 canonical d-value 映射到跨尺度动力学与带宽表述
- 注意：它是展开层，不替代 `_SRT_D_VALUE_CANONICAL.md` 的规范地位

### 7. Ψ_f 跨尺度展开
- 辅助文件：`Core_Law/SRT_Reference_Dynamics.md`、`_SRT_VERTICAL_INTEGRATION.md`
- 角色：把 canonical `Ψ_f` 映射到选择热力学、多算子耦合、跨尺度可支付性与实验代理
- 注意：展开层负责方程与场景化，不替代 `_SRT_PSI_F_CANONICAL.md` 的规范地位

### 8. Core Dynamics & Scaling 主轴
- compact core：`Core/SRT_Core_14_Dynamics_Scaling_CompactCore.md`
- 全量展开：`Core/SRT_Core_14_Dynamics_Scaling.md`
- 角色：compact core 固定跨尺度同构、d-bandwidth、主动力学、边界成本函数与反泛心论边界
- 注意：原文继续保留长篇机制解释、接口批次与 annex 沉积

### 9. Philosophy 主轴
- Foundations：`Philosophy/SRT_Philosophy_Foundations_CompactCore.md` / `Philosophy/SRT_Philosophy_Foundations.md`
- Social Economics：`Philosophy/SRT_Social_Economics_CompactCore.md` / `Philosophy/SRT_Social_Economics.md`
- Political Philosophy：`Philosophy/SRT_Political_Philosophy.md`（`SRT-POLITICAL-PHILOSOPHY`）
- Political Rights：`Philosophy/SRT_Political_Rights.md`（`SRT-POLITICAL-RIGHTS`）
- 角色：形成 Philosophy 板块从三域本体论与选择一元论，到社会现实、制度、权利、合法性与政治病理的 compact/main 主线
- 注意：原文继续保留接口批次、案例扩展、社会科学经典映射与 split 导航

### 9a. SRT 政治哲学
- 主文件：`Philosophy/SRT_Political_Philosophy.md`
- id：`SRT-POLITICAL-PHILOSOPHY`
- layer：L1 / epistemic：bridge / status：axiomatic_hybrid_v1
- 说明：把国家、权利、合法性、民主、结构性不公、危机决断与政治病理统一重写为多主体共同现实选择的生成—沉积—封闭—再打开过程；以 P2/P3 为主，并将制度判准与紧急状态边界显式标记为 P4
- 与 `SRT-SOC-ECONOMICS` / `SRT-POLITICAL-RIGHTS` 的关系：前者提供社会现实、制度与结构性不公接口；后者提供权利、授权与投票后验验证的子接口；本文件负责收口为完整政治哲学主文
- 重要追加：政治合法性被重写为可持续共同选择；反支配被重写为反现实定义权垄断；危机政治以 `minimum necessary interruption` 为护栏

### 9b. SRT 政治权利理论
- 主文件：`Philosophy/SRT_Political_Rights.md`
- id：`SRT-POLITICAL-RIGHTS`
- layer：L1 / epistemic：bridge / status：draft_v1
- 说明：从SRT第一性原理推导权利的本体论定义；建立以决策d值为核心的授权合法性框架；分析投票作为d倾向后验验证的机制；提出三层制度结构（公检法/监督机构/授权主体）
- 与SRT-SOC-ECONOMICS的关系：兄弟关系，后者处理市场与经济不平等，本文件处理政治权利与制度授权
- 重要追加：d值范畴澄清（决策属性非主体属性）已同步写入 `_SRT_D_VALUE_CANONICAL.md §范畴边界`
- 开放问题：监督机构自身d验证完整机制、d倾向准入窗口规格（见文件§10）

### 10. AI 主轴
- 定位说明：`AI/AI_POSITIONING_NOTE.md`
- Ontology：`AI/SRT_AI_01_Ontology_CompactCore.md` / `AI/SRT_AI_01_Ontology.md`
- Architecture：`AI/SRT_AI_Architecture_CompactCore.md` / `AI/SRT_AI_Architecture.md`
- Consciousness Framework：`AI/SRT_AI_03_Consciousness_Framework_CompactCore.md` / `AI/SRT_AI_03_Consciousness_Framework.md`
- 角色：形成 AI 板块从本体门槛、结构限制到正向意识路径的 compact core 主线
- 注意：AI 是压力测试场 / 边界测试场，不是 core 定义发动机；AI 语境中的所有 d-value 与意识判据仍服从 `_SRT_D_VALUE_CANONICAL.md`，所有 `Ψ_f` stake / non-binding / payability 语句仍服从 `_SRT_PSI_F_CANONICAL.md`

### 11. Neuroscience 主轴
- Neuro registry：`Neuroscience/NEUROSCIENCE_COMPACT_REGISTRY.md`
- Neuro Axioms / Bridge：`Neuroscience/_SRT_Neuro_Axioms.md`
- Neural Mechanisms：`Neuroscience/SRT_Neural_Mechanisms_CompactCore.md` / `Neuroscience/SRT_Neural_Mechanisms.md`
- Consciousness Mechanisms：`Neuroscience/SRT_Consciousness_Mechanisms_CompactCore.md` / `Neuroscience/SRT_Consciousness_Mechanisms.md`
- 角色：形成 Neuroscience 板块从桥接公理、神经选择动力学到意识机制的主入口层
- 注意：Neuroscience 已具备 bridge + compact core + registry 的入口骨架，但仍少于 Physics 的覆盖深度

### 12. Physics 主轴
- Quant Intro：`Physics/SRT_Quant_00_Intro_CompactCore.md` / `Physics/SRT_Quant_00_Intro.md`
- Quant Selection：`Physics/SRT_Quant_01_Selection_CompactCore.md` / `Physics/SRT_Quant_01_Selection.md`
- Quant Cosmology：`Physics/SRT_Quant_02_Cosmology_CompactCore.md` / `Physics/SRT_Quant_02_Cosmology.md`
- Physics Cosmology：`Physics/SRT_Physics_Cosmology_CompactCore.md` / `Physics/SRT_Physics_Cosmology.md`
- Formalism Ext：`Physics/SRT_Phys_09_Formalism_Ext_CompactCore.md` / `Physics/SRT_Phys_09_Formalism_Ext.md`
- Integration：`Physics/SRT_Phys_10_Integration_CompactCore.md` / `Physics/SRT_Phys_10_Integration.md`
- Complex Systems：`Physics/SRT_Phys_07_Complex_Systems_CompactCore.md` / `Physics/SRT_Phys_07_Complex_Systems.md`
- Ontology Ext：`Physics/SRT_Phys_08_Ontology_Ext_CompactCore.md` / `Physics/SRT_Phys_08_Ontology_Ext.md`
- 角色：Physics 板块已形成从量子入口、宇宙学/形式化主干，到复杂性/深本体扩展的完整 compact core 入口层
- 注意：Physics 的具体阅读顺序由 `Physics/PHYSICS_COMPACT_REGISTRY.md` 统一管理；其中“引力是 `Ψ_f` 的物理规范实现”这一口径以 `_SRT_PSI_F_CANONICAL.md` 为优先锚点

### 13. Spirituality 主轴
- Spirit registry：`Spirituality/SPIRITUALITY_COMPACT_REGISTRY.md`
- Spirit Bridge：`Spirituality/_SRT_Spirit_Axioms.md`
- Praxis：`Spirituality/SRT_Spirit_09_Praxis_CompactCore.md` / `Spirituality/SRT_Spirit_09_Praxis.md`
- 角色：形成 Spirituality 板块从桥接公理到实践演化主线的最小 compact core 入口层
- 注意：Spirituality 现已具备 bridge + compact core + registry 的入口骨架，但覆盖深度仍少于 Physics

## C. 当前 canonical 引用优先级

当同一概念同时出现在多个文件时，默认优先级如下：

1. `CANONICAL_REGISTRY.md`（找入口）
2. `Governance/SRT_CLAIM_LADDER.md`（判断命题硬度）
3. `_SRT_D_VALUE_CANONICAL.md` / `_SRT_PSI_F_CANONICAL.md` / `_SRT_T_DIR_CANONICAL.md` / `Core/SRT_Core_21_Formal_Axioms.md` / `Core/SRT_Core_22_Equations.md`（找规范定义）
4. `Core/SRT_Core_21_Minimal_Axioms.md` / `Core/SRT_Core_21b_Constitutive_Theorems.md` / `Core/SRT_Core_21c_Bridge_Hypotheses.md`（按 P-level 找 Core_21 正文）
5. `Core/SRT_Core_14_Dynamics_Scaling.md` / `Core_Law/SRT_Reference_Dynamics.md` / `AI/SRT_AI_01_Ontology.md`（找展开与跨域解释）
6. `Core/SRT_OPEN_TENSIONS.md`（确认未封口问题）
7. 各 split 目录（找导航与局部阅读）
8. 原始长文（找历史展开与全量语境）

## D. 当前收口结论

本轮 canonical 抽离 v1 暂定以下四者为主干：
- `d-value` → `_SRT_D_VALUE_CANONICAL.md`
- `Ψ_f` → `_SRT_PSI_F_CANONICAL.md`
- `Core formal axioms` → `Core/SRT_Core_21_Formal_Axioms.md`
- `Core master equations` → `Core/SRT_Core_22_Equations.md`
- `Claim hardness` → `Governance/SRT_CLAIM_LADDER.md`
- `Open tensions` → `Core/SRT_OPEN_TENSIONS.md`

这意味着：
- `AI/SRT_AI_01_Ontology.md` 不再单独承担 d-value 的最终规范权
- `AI/SRT_AI_01_Ontology.md` 不再单独承担 `Ψ_f` 的最终规范权
- `Core/SRT_Core_14_Dynamics_Scaling.md` 不再单独承担 d-value 的最终规范权
- `Core_Law/SRT_Reference_Dynamics.md` 不再单独承担 `Ψ_f` 的最终规范权
- 上述文件保留为高价值展开层
