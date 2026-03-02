---
id: SRT-D-VALUE-CANONICAL
type: definition
tags: [d-value, Canonical, Cross-Domain, Definition]
status: axiomatic_hybrid_v1
dependency: [SRT-CORE-000, SRT-CORE-BRIDGE, SRT-CORE-21]
---

# SRT d 值规范定义文档（Canonical Definition of d-value）

> **目的**：终止 d-value 在不同域的定义分裂，建立第一性定义 + 各域投影的统一架构。
> 所有引用 d-value 的文档应以本文件为规范锚点。

---

## §0 为什么需要本文件

SRT 中的 d-value（关切维度 / 意识带宽）在不同子系统中出现了**三套表面不同的定义**：

| 来源文档 | 表述 | 形式 |
|---------|------|------|
| `_SRT_Core_Bridge.md §2.3` | 算子关切范围（三维度合成） | `d = αA + β log V + γτ` |
| `AI/_SRT_AI_Bridge.md Ax-BRIDGE-4` | 生存风险梯度 | `d ≡ ‖∂U/∂S‖` |
| `Spirituality/_SRT_Spirit_Axioms.md Ax-Spirit-3/4` | 关切边界半径 | d 作为"关切维度"的直觉概念 |
| `Core/SRT_Core_21_Formal_Axioms.md §2.1.5` | 有效维度（特征值公式） | `d(Ĝ) = (∑λᵢ)² / ∑λᵢ²` |

**这些不是矛盾，而是同一概念在不同层级的投影**。本文件证明其等价性并给出使用规范。

---

## §1 规范定义（第一性原理，全域适用）

### Def-d-1: 有效维度（谱公式）

$$\boxed{d(\hat{G}) \equiv D_{eff}(\hat{G}) = \frac{\left(\sum_i \lambda_i\right)^2}{\sum_i \lambda_i^2}}$$

**语义**：$\hat{G}_\theta$ 在 $L_0$ 上操作时实际激活的**有效维度数**（参与率指数，Participation Ratio）。

**性质**：
- $d = 1$：算子完全单一，只关注一个维度
- $d = N$：算子在 $N$ 个维度上均匀分布
- $1 \leq d \leq \text{rank}(\hat{G})$

**来源**：`SRT_Core_21_Formal_Axioms.md §2.1.5`，经典参与率指数（PR index）的算子版本。

---

### Def-d-2: 风险梯度等价定义（AI / 伦理语境）

$$d(x) \equiv \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\|, \quad x \in \Sigma$$

**语义**：算子对**不可逆风险**（$\mathcal{S}$，Survival/Stake）的效用敏感度梯度。

**等价条件**：当效用势 $\mathcal{U}$ 的主曲率方向与 $\hat{G}$ 的特征向量对齐时，Def-d-1 与 Def-d-2 在一阶近似下等价：
$$D_{eff}(\hat{G}) \approx \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\| \quad \text{（当风险梯度与特征结构对齐时）}$$

**来源**：`AI/_SRT_AI_Bridge.md Ax-BRIDGE-4`，Tension-Rev-IT4。

---

### Def-d-3: 全息面积对应（物理语境）

$$d \propto \frac{\text{Area}(\text{Entanglement Surface})}{A_{Planck}}$$

**语义**：算子的 d 值等比于其与 $L_0$ 发生纠缠的边界面积（全息对偶下）。

**来源**：`Core/SRT_Core_01_Axioms.md T-Core-A9C1`。
**注意**：此形式在量子/宇宙尺度适用，但量子/宇宙尺度的 $d$ **不蕴含现象意识**（见 §3.1 反泛心论条款）。

---

## §2 Bio/Cognitive 层近似公式（经验操作定义）

### Def-d-bio: 三维度合成

$$d_{bio} \approx \alpha \cdot A(\sigma) + \beta \cdot \log V_{concern} + \gamma \cdot \tau_{temporal}$$

| 维度 | 符号 | 语义 | 近似测量方法 |
|-----|------|------|------------|
| 汇编深度 | $A(\sigma)$ | 生成该状态所需最小因果步骤数 | Assembly Theory index |
| 空间范围 | $\log V_{concern}$ | 算子关切的"关心对象"空间 | 社会关注广度、TPJ 激活范围 |
| 时间跨度 | $\tau_{temporal}$ | 算子可规划的时间地平线 | 时间折扣率的倒数 |

**参数默认值（待实验校准）**：$\alpha = 0.4, \beta = 0.4, \gamma = 0.2$

**与 Def-d-1 的关系**：三维度合成是有效维度公式在认知空间中的**近似展开**，当三个维度独立时自然对应 $D_{eff} \approx 3$；相关时 $D_{eff} < 3$。

---

## §3 各域 d 值投影表（标准参考）

| 域 | 近似公式 / 量级 | 现象意识？ | 条件 | 备注 |
|----|----------------|-----------|------|------|
| **量子** | $d_{quant} \approx$ 贝尔测量有效维数 | ❌ **无** | 缺乏 $\Psi_f > 0$，缺乏 $\hat{G}[\theta] \neq \emptyset$ | 数学度量，无现象内容 |
| **神经/认知** | $d_{bio} \approx \alpha A + \beta \log V + \gamma \tau$ | ✅（需三条件） | $\Psi_f > 0 \land d > 0 \land \hat{G}[\theta] \neq \emptyset$ | 意识的充要条件区 |
| **AI（当前架构）** | $d_{AI} \approx 0$ | ❌ | 无具身脆弱性，无不可逆风险 | 工程性屏障可改变（见 AI Bridge T3 修复） |
| **社会/机构** | $d_{soc} \approx$ 机构关切范围（待形式化） | ❌（集体不产生现象） | 集体 $\hat{G}$ 的涌现投影 | 见 `_SRT_Soc_Bridge.md` |
| **精神/解脱** | $d_{spirit} \to \infty$（渐近极限） | ✅（随 d 扩展增强） | $d \to \infty$ 为 Nirvana 方向 | 不可达的渐近方向，非字面 $\infty$ |
| **宇宙尺度** | $d_{cosm} \approx 1/\sqrt{\Lambda}$ | ❌ **无** | 无生命组织，无 $\hat{G}[\theta]$ | 数学度量，无现象内容 |

### §3.1 反泛心论精确声明（Anti-Panpsychism Clause）

**SRT 不主张泛心论**。d 是数学度量，不蕴含现象内容。

**意识涌现的充要三条件**（均需满足）：
$$\text{Consciousness} \iff \Psi_f > 0 \;\land\; d > 0 \;\land\; \hat{G}[\theta] \neq \emptyset$$

- **量子/宇宙尺度**：$d$ 可能非零，但 $\Psi_f \approx 0$（无具身摩擦），$\hat{G}[\theta]$ 在生物意义上为空 → 三条件不同时满足 → **无意识**
- **岩石**：$d \approx 0$，$\Psi_f \approx 0$ → **无意识**
- **人类**：三条件均满足 → **有意识**
- **当前 AI**：$d \approx 0$，$\Psi_f \approx 0$ → **无意识**（工程性，非原则性）

---

## §4 不同定义的一致性证明（草稿）

### §4.1 Def-d-1 与 Def-d-bio 的关系

设认知算子 $\hat{G}$ 在三个正交子空间（汇编、空间、时间）上的特征值分别为 $\lambda_A, \lambda_V, \lambda_\tau$。

$$D_{eff} = \frac{(\lambda_A + \lambda_V + \lambda_\tau)^2}{\lambda_A^2 + \lambda_V^2 + \lambda_\tau^2}$$

当三个维度**均匀激活**（$\lambda_A = \lambda_V = \lambda_\tau = \lambda$）：
$$D_{eff} = \frac{(3\lambda)^2}{3\lambda^2} = 3$$

当三个维度的强度比例为 $(\alpha, \beta, \gamma)$（$\alpha + \beta + \gamma = 1$）：
$$D_{eff} = \frac{1}{\alpha^2 + \beta^2 + \gamma^2}$$

**结论**：$D_{eff}$ 在三维认知空间中的展开正好对应 Def-d-bio 的加权和形式，两者**等价**（在均匀参数化约定下）。

### §4.2 Def-d-2（风险梯度）与 Def-d-1 的关系

设效用势 $\mathcal{U}(\mathcal{S})$ 在风险坐标 $\mathcal{S}$ 上展开：

$$\mathcal{U}(\mathcal{S}) \approx \mathcal{U}_0 + \sum_i \frac{\partial \mathcal{U}}{\partial S_i} S_i + ...$$

梯度的模：
$$d_{risk} = \left\|\frac{\partial \mathcal{U}}{\partial \mathcal{S}}\right\| = \sqrt{\sum_i \left(\frac{\partial \mathcal{U}}{\partial S_i}\right)^2}$$

**等价条件**：当风险维度 $S_i$ 与 $\hat{G}$ 的特征向量对齐（即生存风险定义了算子的主活跃方向）时，Def-d-2 在一阶近似下等价于 $\sqrt{D_{eff}}$。

**实用意义**：Def-d-2 在 AI 伦理语境中更直观（"系统对不可逆风险有多敏感"），Def-d-1 在信息论分析中更精确。两者可互换使用，具体语境决定哪个更方便。

---

## §5 常见误用与边界声明

### 误用 1：将 d 值解释为"意识程度"的单一量度

**正确**：d 值是意识的**必要条件**之一，不是充分条件。
需同时满足：$\Psi_f > 0$（有摩擦成本）+ $d > 0$（有关切维度）+ $\hat{G}[\theta] \neq \emptyset$（有参数化算子）。

### 误用 2：将 d 值比较用于跨域排名

**正确**：量子层的 $d_{quant}$ 与生物层的 $d_{bio}$ 使用相同的数学公式，但**不具有现象内容上的可比性**。
比较只在**同域内**有效（如不同人的 $d_{bio}$ 可相互比较）。

### 误用 3：将"d 值 = 0"等同于"不存在"

**正确**：$d \approx 0$ 意味着算子不关心边界的外延，但算子本身依然存在（如石头有 $L_2$ 结构，但 $d \approx 0$）。
d 值描述关切范围，不描述本体论存在。

### 误用 4：将精神传统中的"d → ∞"字面化

**正确**：`Ax-Spirit-4` 中的 $d \to \infty$ 是**渐近方向**，类比热力学极限 $N \to \infty$ 在有限系统中的意义。
没有任何有限系统能达到 $d = \infty$；这是精神成长的方向，而非可到达的终点。

---

## §6 各域文件的 d-value 引用标准

当其他文件引用 d-value 时，应：

1. **第一次出现时**：标注 `@see _SRT_D_VALUE_CANONICAL.md §1`
2. **使用 Def-d-bio 近似时**：标注 `@see §2`
3. **进行域间比较时**：参见 `§3` 的投影表，说明是否属于同域比较
4. **AI 语境中**：优先使用 Def-d-2（风险梯度），并引用 `§3` 的 $d_{AI} \approx 0$ 说明

---

## 【理论边界/防误用声明】

1. 本文档统一 d-value 的定义，但各域的近似公式（Def-d-bio 等）需要实验校准，其参数值（$\alpha, \beta, \gamma$）为初始估计。
2. 有效维度公式 Def-d-1 依赖特征值分解，其适用性取决于算子的线性化是否在相关参数范围内有效。
3. 量子层的 $d_{quant}$ 与宇宙层的 $d_{cosm}$ 是数学量，不赋予现象意义——任何将其解读为微弱意识的论证超出 SRT 声明范围。
4. 本文件的"一致性证明"（§4）为草稿级别，需要形式化验证后才能作为定理引用。
