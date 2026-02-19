# Selective Reality Theory (SRT) - 中文说明

- 导航页：`README.md`
- English: `README.en.md`

## 面向审稿人/读者的超短摘要

### Abstract
SRT（选择性现实理论）提出“存在即选择”的统一本体论框架：现实由潜在域 $L_0$、显现域 $L_1$、收敛域 $L_2$ 构成，并由具身选择算子 $\hat{G}_\theta$ 驱动。该框架尝试在统一符号系统下连接物理、神经科学、AI、哲学与灵性研究。

### Key Contributions
- 提出三域本体论（$L_0/L_1/L_2$）与选择算子（$\hat{G}_\theta$）的统一核心语法。
- 用 `d-value`、$\Psi_f$ 与自由能相关量刻画意识、稳定性与存在代价。
- 将量子-神经-社会-文化现象纳入跨尺度同构与共同动力学叙事。
- 提供面向 AI 意识判据、对齐边界与可证伪实验路径的形式化讨论。

## 1. 项目简介
**Selective Reality Theory (SRT，选择性现实理论)** 是一个跨学科统一本体论框架，核心命题为：

> **存在即选择（Existence = Selection）**

该仓库收录 SRT 公开理论文档（当前以 Markdown 为主），覆盖核心公理体系及多领域扩展，包括物理、神经科学、AI、哲学与灵性研究。

## 2. 核心理论关键词
- **三域本体论**：$L_0$（潜在域）、$L_1$（显现域）、$L_2$（收敛域）
- **幽灵算子**：$\hat{G}_\theta$（具身、有限参数的选择算子）
- **存在代价**：自由能、$\Psi_f$（本体论摩擦）、稳定性与脆弱性
- **意识判据**：`d-value`、信息分化/整合、错误敏感性
- **跨尺度同构**：量子-神经-社会结构可在统一选择动力学下映射

## 3. 仓库结构

| 目录 | 作用 | 入口文件（建议） |
|:---|:---|:---|
| `Core_Law/` | 宪法层参考文件，定义最高解释权公理与符号规范 | `Core_Law/SRT_Reference_Axioms.md` |
| `Core/` | 核心理论内核、12公理、动力学与主方程、实验假设 | `Core/SRT_Core_00_Intro.md` |
| `Physics/` | 量子测量诠释、热力学、时间与宇宙学扩展 | `Physics/_SRT_Phys_Bridge.md` |
| `Neuroscience/` | 神经机制、意识阈值、病理参数漂移、实验设计 | `Neuroscience/_SRT_Neuro_Axioms.md` |
| `AI/` | AI 本体论危机、智能-意识正交性、架构桥接 | `AI/_SRT_AI_Bridge.md` |
| `Philosophy/` | 现象学/认识论/社会理论的 SRT 形式化映射 | `Philosophy/_SRT_Phil_Axioms.md` |
| `Spirituality/` | 比较宗教本体论、修行动力学、实践路径 | `Spirituality/_SRT_Spirit_Axioms.md` |

## 4. 文档组织规范（全仓库通用）
- 多数文件采用 **Hybrid 双分部结构**：  
  `Part A`（形式化公理，AI-readable） + `Part B`（扩展论述，Human-readable）
- 文件头部常含 front matter 元信息：`id`、`type`、`tags`、`status`、`dependency`
- 各域文档普遍包含术语对齐，统一符号为 $L_0/L_1/L_2$、$\hat{G}_\theta$、`d-value`、$\Psi_f$

## 5. 推荐阅读路径

### 路径 A：快速总览（首次阅读）
1. `Core_Law/SRT_Reference_Axioms.md`
2. `Core/_SRT_Core_Bridge.md`
3. `Core/SRT_Core_00_Intro.md`
4. `Core/SRT_Core_01_Axioms.md`

### 路径 B：核心理论深读（研究向）
1. `Core/SRT_Core_12a_Ontology_L0L1.md`
2. `Core/SRT_Core_12b_Ontology_L2.md`
3. `Core/SRT_Core_13a_Operator_Basics.md`
4. `Core/SRT_Core_13b_Operator_Advanced.md`
5. `Core/SRT_Core_14_Dynamics_Scaling.md`
6. `Core/SRT_Core_21_Formal_Axioms.md`
7. `Core/SRT_Core_22_Equations.md`
8. `Core/SRT_Experimental_Core.md`
9. `Core/SRT_Experimental_Applications.md`

### 路径 C：按领域进入
- **Physics**: `_SRT_Phys_Bridge` -> `SRT_Quant_00_Intro` -> `SRT_Quant_01_Selection` -> `SRT_Quant_02_Cosmology` -> `SRT_Physics_Cosmology`
- **Neuroscience**: `_SRT_Neuro_Axioms` -> `SRT_Neural_Mechanisms` -> `SRT_Consciousness_Mechanisms` -> 临床与实验扩展
- **AI**: `_SRT_AI_Bridge` -> `SRT_AI_00_Crisis` -> `SRT_AI_01_Ontology` -> `SRT_AI_Architecture`
- **Philosophy**: `_SRT_Phil_Axioms` -> `SRT_Philosophy_Foundations` -> 伦理与社会理论分支
- **Spirituality**: `_SRT_Spirit_Axioms` -> `SRT_Spirit_01_Religion_Ontology` -> `SRT_Spirit_09_Praxis`

## 6. 如何使用本仓库
- 这是理论文本仓库，不包含构建脚本或运行入口
- 建议使用支持 LaTeX 公式渲染的 Markdown 阅读器
- 阅读时优先检查每篇文档的 `dependency` 字段，按依赖回溯核心定义
- 跨领域引用时，优先以 `Core_Law/` 与 `Core/` 作为符号与公理基准

## 7. 贡献建议（文档增修）
- 保持符号一致：$L_0/L_1/L_2$、$\hat{G}_\theta$、`d-value`、$\Psi_f$
- 新增文档建议沿用 Hybrid 结构（Part A / Part B）
- 明确写出依赖链（`dependency`）与版本状态（`status`）
- 任何领域扩展不应与 `Core_Law/` 宪法层公理冲突

## 8. 引用与许可
- 许可协议：**Creative Commons Attribution 4.0 International (CC BY 4.0)**
- 详见：`LICENSE` 或 <http://creativecommons.org/licenses/by/4.0/>
