# Selective Reality Theory (SRT) - Public Repository

> Bilingual README / 双语说明文档  
> This repository is a theory corpus (Markdown-first), not an executable software package.

- [中文版](#中文版)
- [English Version](#english-version)

## 中文版

### 1. 项目简介
**Selective Reality Theory (SRT，选择性现实理论)** 是一个跨学科统一本体论框架，核心命题为：

> **存在即选择（Existence = Selection）**

该仓库收录 SRT 公开理论文档（当前以 Markdown 为主），覆盖核心公理体系及多领域扩展，包括物理、神经科学、AI、哲学与灵性研究。

### 2. 核心理论关键词
- **三域本体论**：`L_0`（潜在域）、`L_1`（显现域）、`L_2`（收敛域）
- **幽灵算子**：`\hat{G}_\theta`（具身、有限参数的选择算子）
- **存在代价**：自由能、`Ψ_f`（本体论摩擦）、稳定性与脆弱性
- **意识判据**：`d-value`、信息分化/整合、错误敏感性
- **跨尺度同构**：量子-神经-社会结构可在统一选择动力学下映射

### 3. 仓库结构

| 目录 | 作用 | 入口文件（建议） |
|:---|:---|:---|
| `Core_Law/` | 宪法层参考文件，定义最高解释权公理与符号规范 | `Core_Law/SRT_Reference_Axioms.md` |
| `Core/` | 核心理论内核、12公理、动力学与主方程、实验假设 | `Core/SRT_Core_00_Intro.md` |
| `Physics/` | 量子测量诠释、热力学、时间与宇宙学扩展 | `Physics/_SRT_Phys_Bridge.md` |
| `Neuroscience/` | 神经机制、意识阈值、病理参数漂移、实验设计 | `Neuroscience/_SRT_Neuro_Axioms.md` |
| `AI/` | AI 本体论危机、智能-意识正交性、架构桥接 | `AI/_SRT_AI_Bridge.md` |
| `Philosophy/` | 现象学/认识论/社会理论的 SRT 形式化映射 | `Philosophy/_SRT_Phil_Axioms.md` |
| `Spirituality/` | 比较宗教本体论、修行动力学、实践路径 | `Spirituality/_SRT_Spirit_Axioms.md` |

### 4. 文档组织规范（全仓库通用）
- 多数文件采用 **Hybrid 双分部结构**：  
  `Part A`（形式化公理，AI-readable） + `Part B`（扩展论述，Human-readable）
- 文件头部常含 front matter 元信息：`id`、`type`、`tags`、`status`、`dependency`
- 各域文档普遍包含术语对齐，统一符号为 `L_0/L_1/L_2`、`\hat{G}_\theta`、`d-value`、`Ψ_f`

### 5. 推荐阅读路径

#### 路径 A：快速总览（首次阅读）
1. `Core_Law/SRT_Reference_Axioms.md`
2. `Core/_SRT_Core_Bridge.md`
3. `Core/SRT_Core_00_Intro.md`
4. `Core/SRT_Core_01_Axioms.md`

#### 路径 B：核心理论深读（研究向）
1. `Core/SRT_Core_12a_Ontology_L0L1.md`
2. `Core/SRT_Core_12b_Ontology_L2.md`
3. `Core/SRT_Core_13a_Operator_Basics.md`
4. `Core/SRT_Core_13b_Operator_Advanced.md`
5. `Core/SRT_Core_14_Dynamics_Scaling.md`
6. `Core/SRT_Core_21_Formal_Axioms.md`
7. `Core/SRT_Core_22_Equations.md`
8. `Core/SRT_Experimental_Core.md`
9. `Core/SRT_Experimental_Applications.md`

#### 路径 C：按领域进入
- **Physics**: `_SRT_Phys_Bridge` -> `SRT_Quant_00_Intro` -> `SRT_Quant_01_Selection` -> `SRT_Quant_02_Cosmology` -> `SRT_Physics_Cosmology`
- **Neuroscience**: `_SRT_Neuro_Axioms` -> `SRT_Neural_Mechanisms` -> `SRT_Consciousness_Mechanisms` -> 临床与实验扩展
- **AI**: `_SRT_AI_Bridge` -> `SRT_AI_00_Crisis` -> `SRT_AI_01_Ontology` -> `SRT_AI_Architecture`
- **Philosophy**: `_SRT_Phil_Axioms` -> `SRT_Philosophy_Foundations` -> 伦理与社会理论分支
- **Spirituality**: `_SRT_Spirit_Axioms` -> `SRT_Spirit_01_Religion_Ontology` -> `SRT_Spirit_09_Praxis`

### 6. 如何使用本仓库
- 这是理论文本仓库，不包含构建脚本或运行入口
- 建议使用支持 LaTeX 公式渲染的 Markdown 阅读器
- 阅读时优先检查每篇文档的 `dependency` 字段，按依赖回溯核心定义
- 跨领域引用时，优先以 `Core_Law/` 与 `Core/` 作为符号与公理基准

### 7. 贡献建议（文档增修）
- 保持符号一致：`L_0/L_1/L_2`、`\hat{G}_\theta`、`d-value`、`Ψ_f`
- 新增文档建议沿用 Hybrid 结构（Part A / Part B）
- 明确写出依赖链（`dependency`）与版本状态（`status`）
- 任何领域扩展不应与 `Core_Law/` 宪法层公理冲突

### 8. 引用与许可
- 许可协议：**Creative Commons Attribution 4.0 International (CC BY 4.0)**
- 详见：`LICENSE` 或 <http://creativecommons.org/licenses/by/4.0/>

---

## English Version

### 1. Overview
**Selective Reality Theory (SRT)** is a transdisciplinary unified ontological framework built around the thesis:

> **Existence = Selection**

This repository is the public theory corpus of SRT, organized as Markdown documents spanning core axioms and domain-specific extensions.

### 2. Core Concepts
- **Triadic Ontology**: `L_0` (latent), `L_1` (manifest), `L_2` (vergence)
- **Ghost Operator**: `\hat{G}_\theta` as embodied finite selection operator
- **Cost of Existence**: free energy, ontological friction (`Ψ_f`), stability/fragility
- **Consciousness Criteria**: `d-value`, integration-differentiation, error sensitivity
- **Cross-Scale Isomorphism**: unified mappings across quantum, neural, and social scales

### 3. Repository Layout

| Directory | Role | Suggested Entry |
|:---|:---|:---|
| `Core_Law/` | Constitutional references and highest-priority axiomatic constraints | `Core_Law/SRT_Reference_Axioms.md` |
| `Core/` | Kernel architecture, 12 axioms, operator dynamics, master equations | `Core/SRT_Core_00_Intro.md` |
| `Physics/` | Selection-based interpretation of QM, thermodynamics, cosmology | `Physics/_SRT_Phys_Bridge.md` |
| `Neuroscience/` | Neural mechanisms, consciousness thresholds, pathology as parameter drift | `Neuroscience/_SRT_Neuro_Axioms.md` |
| `AI/` | AI ontology, alignment limits, intelligence-consciousness split | `AI/_SRT_AI_Bridge.md` |
| `Philosophy/` | Epistemology, phenomenology, social theory mappings | `Philosophy/_SRT_Phil_Axioms.md` |
| `Spirituality/` | Comparative religious ontology and praxis dynamics | `Spirituality/_SRT_Spirit_Axioms.md` |

### 4. Document Pattern
- Most documents follow a **Hybrid** format:  
  `Part A` (formal axioms, AI-readable) + `Part B` (expanded discourse, human-readable)
- Front matter commonly includes: `id`, `type`, `tags`, `status`, `dependency`
- Notation is generally normalized to `L_0/L_1/L_2`, `\hat{G}_\theta`, `d-value`, `Ψ_f`

### 5. Recommended Reading Paths

#### Path A: Quick Orientation
1. `Core_Law/SRT_Reference_Axioms.md`
2. `Core/_SRT_Core_Bridge.md`
3. `Core/SRT_Core_00_Intro.md`
4. `Core/SRT_Core_01_Axioms.md`

#### Path B: Core Deep-Dive
1. `Core/SRT_Core_12a_Ontology_L0L1.md`
2. `Core/SRT_Core_12b_Ontology_L2.md`
3. `Core/SRT_Core_13a_Operator_Basics.md`
4. `Core/SRT_Core_13b_Operator_Advanced.md`
5. `Core/SRT_Core_14_Dynamics_Scaling.md`
6. `Core/SRT_Core_21_Formal_Axioms.md`
7. `Core/SRT_Core_22_Equations.md`
8. `Core/SRT_Experimental_Core.md`
9. `Core/SRT_Experimental_Applications.md`

#### Path C: Domain Entry
- **Physics**: `_SRT_Phys_Bridge` -> `SRT_Quant_00_Intro` -> `SRT_Quant_01_Selection` -> `SRT_Quant_02_Cosmology` -> `SRT_Physics_Cosmology`
- **Neuroscience**: `_SRT_Neuro_Axioms` -> `SRT_Neural_Mechanisms` -> `SRT_Consciousness_Mechanisms` -> clinical/experimental modules
- **AI**: `_SRT_AI_Bridge` -> `SRT_AI_00_Crisis` -> `SRT_AI_01_Ontology` -> `SRT_AI_Architecture`
- **Philosophy**: `_SRT_Phil_Axioms` -> `SRT_Philosophy_Foundations` -> ethics/social branches
- **Spirituality**: `_SRT_Spirit_Axioms` -> `SRT_Spirit_01_Religion_Ontology` -> `SRT_Spirit_09_Praxis`

### 6. How to Use This Repository
- This is a documentation-first theory repository (no runtime/build pipeline)
- Use a Markdown reader with LaTeX math rendering
- Follow `dependency` fields to reconstruct derivation chains
- Use `Core_Law/` and `Core/` as canonical references for notation and constraints

### 7. Contribution Notes
- Keep notation aligned: `L_0/L_1/L_2`, `\hat{G}_\theta`, `d-value`, `Ψ_f`
- Prefer the Hybrid structure for new modules
- Include explicit `dependency` and `status` metadata
- Domain extensions should remain consistent with `Core_Law/` constitutional axioms

### 8. License
- **Creative Commons Attribution 4.0 International (CC BY 4.0)**
- See `LICENSE` or <http://creativecommons.org/licenses/by/4.0/>
