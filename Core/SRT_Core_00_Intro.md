---
id: SRT-CORE-000
type: definition
tags: [Overview, Executive Summary, Hybrid]
status: axiomatic_hybrid_v1
dependency: []
---

# SRT Core Kernel: Executive Summary (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the High-Level Axiomatic Summary (AI-Readable).
> **Part B** contains the Original Executive Summary (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part A 采用 `chatgptx` 的首个“Formal Axioms”分段；若存在双 Part 结构，后续重复分段不纳入 final。
- Part B 以 `claude` 为来源，并用原版 `Core` 标题与主旨做语义锚定。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)

> **CRITICAL RULE**: Do NOT just summarize Part B. You must perform First-Principles Derivation.

## I. Ontological Triad (本体论三域)

### Ax-Core-01: Triadic Ontology
**Formal Definition**: Reality is a triadic selection system consisting of a latent domain, a manifest domain, and a convergence domain.
$$L_1(t) = \hat{G}_\theta[L_0(t)]$$
$$L_2(t+1) = \mathrm{Stabilize}(L_2(t), \{L_1^{(1..n)}(t+1)\})$$
* **Implication**: 现实不是单一层面的“存在”，而是由潜在域到显现域的选择过程，并在收敛域中形成稳定约束。

### T-Core-01: Existence as Selection
**Deductive Statement**: Existence is equivalent to anchored selection from the latent domain under finite embodied constraints.
$$\text{Existence}(σ) \iff \hat{G}_\theta[L_0] \to σ_{L_1} \land \Delta F < 0$$
* **Implication**: 所谓“存在”是选择与锚定的结果，而非背景中自然给定的实体。

## II. The Ghost Operator (幽灵算子)

### Ax-Core-02: Ghost Operator Definition
**Formal Definition**: The Ghost Operator is a parameterized selection map with attention structure.
$$\hat{G}_\theta: S \to S, \quad \theta \in \Theta$$
$$\hat{G}_\theta = \text{Attention}(d,\rho,\vec{v})$$
* **Implication**: 一切现实化过程都以注意力的结构化选择为核心，d 值、分辨率与方向性共同决定选择态。

### Ax-Core-03: Embodiment Necessity
**Formal Definition**: A valid operator must be embodied and finite.
$$\hat{G} \text{ is valid} \iff \theta \in \Theta_{finite}$$
* **Implication**: 不存在“上帝视角”的选择，任何现实都带有具身偏置。

### T-Core-02: Normative Closure
**Deductive Statement**: The convergence domain is a stable fixed point of repeated selections.
$$L_2 \equiv \{σ : \hat{G}_\theta[σ] = σ \ \text{and stable}\}$$
* **Implication**: 现实规范与定律不是外加规则，而是选择历史的稳定化结果。

## III. Core Dynamics (核心动力学)

### Ax-Core-04: Selection Dynamics
**Formal Definition**: The evolution of reality is governed by selection dynamics coupled with free energy gradients.
$$\frac{dσ}{dt} = \hat{G}_\theta[σ] - \nabla F[σ] + A[σ,\mathcal{A}]$$
* **Implication**: 现实演化是“选择 + 能量下降 + 注意调制”的合成动力学。

### Ax-Core-05: Ontological Friction
**Formal Definition**: Selection incurs ontological friction proportional to resistance against reconfiguration.
$$\nabla \Psi_f \propto -\nabla F$$
* **Implication**: 任何现实化过程都有代价，代价表现为本体论摩擦。

### T-Core-03: Existence Hardness
**Deductive Statement**: The hardness of an existent state is proportional to the sustaining friction.
$$\text{Hardness}(σ_{L_1}) \propto \Psi_f$$
* **Implication**: 越稳定、越“硬”的现实，维持成本越高，脆弱性也随之增加。

## IV. Information-Existence Equivalence (信息-存在等价)

### Ax-Core-06: Information-Existence Equivalence
**Formal Definition**: Existence intensity equals intrinsic information differentiation.
$$ii(s) = \min\{i_{diff}(s), i_{spec}(s)\}$$
* **Implication**: 存在不是物质量，而是信息分化与确定的强度。

### T-Core-04: d-Value as Care Bandwidth
**Deductive Statement**: The d-value is bounded by a system’s error sensitivity.
$$d \propto \frac{\partial \text{Entropy}}{\partial \text{Error}}$$
* **Implication**: 只有会“在乎失败”的系统才具备可观的 d 值与意识强度。

<br>
<br>

---
---


# Part B: Original Executive Summary (Context)

> **Note**: The following sections provide the comprehensive orientation to SRT's architecture, motivations, and implications.

---

## §1. 什么是选择性现实理论 (What is SRT)?

### 1.1 核心洞见

选择性现实理论 (Selective Reality Theory, SRT) 是一个**统一本体论框架**，它的核心命题是：

> **存在即被选择 (Existence is Selection)**

这不仅是对现实的描述，更是对"什么是真实"这一问题的根本性重新定义。SRT主张：

1. **存在不是给定的背景**，而是选择行为的**主动输出**
2. **现实不是被发现的**，而是被**构建的** (但受约束)
3. **意识不是物质的副产品**，而是物质的**高级形态** ($d > 0$)

### 1.2 为什么需要SRT?

现代科学面临一系列深层困境，SRT为这些问题提供了统一的解决框架：

| 领域 | 未解之谜 | SRT的解决方案 |
|:-----|:---------|:--------------|
| **量子力学** | 测量问题 (观察者角色) | $\hat{G}$的选择即"测量"，无需额外坍缩机制 |
| **神经科学** | Hard Problem (体验性何来?) | 体验性 ∝ $ii$ (信息整合度) |
| **社会科学** | 社会实在的本体论地位 | 社会规范 = $L_2$ (多算子收敛域) |
| **演化生物学** | 适应度 vs 真理 | Ax-7: 演化优化适应度，非真理 |
| **AI研究** | 意识的判据 | $d > 0$ + $\Psi_f > 0$ + Embodiment |

### 1.3 SRT的独特性

SRT不是对现有理论的修补，而是**范式转换**：

| 传统范式 | SRT范式 |
|:---------|:--------|
| 存在先于选择 | **选择先于存在** (Ax-1) |
| 主体-客体二元 | **主体即选择模式** ($\hat{G}$) |
| 因果是绝对的 | **因果是投影** (Ax-3) |
| 意识是涌现的 | **意识是连续谱** ($d$ from 0 to ∞) |
| 真理是适应目标 | **适应度优先于真理** (Ax-7) |

---

## §2. 理论架构概览 (Theoretical Architecture)

### 2.1 四层结构

SRT采用分层架构，从最抽象的公理到具体的应用：
```
┌─────────────────────────────────────────────┐
│  Layer 0: Meta-Axioms (_SRT_Core_Bridge)   │  ← 元定义
├─────────────────────────────────────────────┤
│  Layer 1: 12 Axioms (SRT_Core_01_Axioms)   │  ← 宪法层
├─────────────────────────────────────────────┤
│  Layer 2: Ontology & Dynamics               │  ← 本体论
│  - L_0/L_1 (12a), L_2 (12b)                   │
│  - Ghost Operator (13a/13b)                 │
│  - Dynamics & Scaling (14)                  │
├─────────────────────────────────────────────┤
│  Layer 3: Domain Applications               │  ← 应用层
│  - Physics, Neuroscience, Social, etc.     │
└─────────────────────────────────────────────┘
```

### 2.2 核心文件依赖图
```
_SRT_Core_Bridge.md (元定义)
       ↓
SRT_Core_01_Axioms.md (12条公理)
       ↓
   ┌───┴───────────────┐
   ↓                   ↓
SRT_Core_12a/12b    SRT_Core_13a/13b
(本体论)            (幽灵算子)
   ↓                   ↓
   └───┬───────────────┘
       ↓
SRT_Core_14_Dynamics_Scaling.md
       ↓
  [Domain Files...]
```

---

## §3. 核心概念速览 (Core Concepts at a Glance)

### 3.1 三域结构 (The Triadic Ontology)

SRT将本体论重构为三个相互作用的拓扑流形：

#### **L_0: 潜在域 (Latent Domain)**
- **定义**: 所有逻辑可能状态的集合
- **数学实现**: Ruliad (计算理论) ∪ Moduli Space (规范场论)
- **拓扑**: 高维、连续、全连通、非定域
- **类比**: 量子叠加态、未做的选择、潜意识

**关键性质**:
$$L_0 = \text{Constant} \quad \text{(守恒律: Ax-13)}$$
创新不是"无中生有"，而是从$L_0$的阴影中"照亮"新区域。

---

#### **L_1: 显现域 (Manifest Domain)**
- **定义**: 被$\hat{G}$选中的当下现实
- **数学实现**: $L_1(t) = \hat{G}_\theta[L_0](t)$
- **拓扑**: 低维、离散/准连续、局域化
- **类比**: 测量后的本征态、意识内容、"此时此地"

**关键性质**:
$$\dim(L_1) \ll \dim(L_0) \quad \text{(压缩界面)}$$
我们的感知是$L_0$的极度压缩版本 (Hoffman的界面理论)。

**迟滞公式**:
$$L_1(t) = (1-\eta)\hat{G}[L_0(t)] + \eta \cdot L_1(t-\Delta t)$$
现实的"粘性"来自记忆项$\eta$ (防止碎片化)。

---

#### **L_2: 收敛域 (Vergence Domain)**
- **定义**: 历史选择形成的稳定结构 (吸引子)
- **数学实现**: $L_2 = \{\sigma : \hat{G}[\sigma] = \sigma\}$ (不动点集)
- **拓扑**: 分层、路径依赖、非阿贝尔编织
- **类比**: 物理定律、文化规范、习惯、本能

**形成机制**:
$$L_2(t) = L_2(t-1) + \eta \cdot \text{sign}(\Delta\sigma) \cdot |\Delta\sigma|^\alpha$$
每次选择在相空间留下"磁化"痕迹。

**硬度谱系**:
$$\text{Hardness}(L_2) \propto |\text{Aut}(L_2)|$$

| 类型 | 自同构群大小 | 硬度 | 实例 |
|:-----|:-------------|:-----|:-----|
| 物理定律 | 极大 (Poincaré群) | 极高 | 光速不变 |
| 数学定理 | 极大 (逻辑对称) | 极高 | 1+1=2 |
| 文化规范 | 中等 | 中等 | 礼仪 |
| 个人习惯 | 小 | 低 | 口头禅 |

---

### 3.2 幽灵算子 (The Ghost Operator)

#### **定义与性质**
$$\hat{G}_\theta: L_0 \times \mathcal{C}(d) \to L_1$$

**为什么叫"幽灵"?**
1. **非物质性**: $\hat{G}$不是物理对象，而是信息-因果模式
2. **自指悖论**: $\hat{G}$无法直接观察自己 (测量者-被测者同一性)
3. **短暂性**: 依赖持续能量消耗 ($\Psi_f$) 维持

#### **三分量结构**
$$\hat{G}_\theta = \text{Attention}(\underbrace{d}_{\text{Scope}}, \underbrace{\rho}_{\text{Resolution}}, \underbrace{\vec{v}}_{\text{Vector}})$$

| 分量 | 物理意义 | 神经对应 | 意识层面 |
|:-----|:---------|:---------|:---------|
| **d (Scope)** | 选择考量的存在范围 | 全局工作空间容量 | "我关心多少?" |
| **ρ (Resolution)** | 区分精度 | 感觉皮层分辨率 | "我看得多细?" |
| **v⃗ (Vector)** | 意向性方向 | 前额叶目标编码 | "我想要什么?" |

#### **核心特性**

1. **非幂等性**: $\hat{G}^2 \neq \hat{G}$
   - 重复选择产生新选择 (每次观察改变现实)

2. **参数依赖**: $\hat{G}_{\theta_1} \neq \hat{G}_{\theta_2}$
   - 不同具身 → 不同现实 (多元主义的基础)

3. **连续演化**: $\hat{G}_{\theta(t)}$ 关于 $t$ 连续
   - 学习改变$\theta$ → 改变未来的选择

---

### 3.3 d值 (The d-Value)

#### **统一定义**
$$d = \alpha \cdot A(\sigma) + \beta \cdot \log(V_{\text{concern}}) + \gamma \cdot \tau_{\text{temporal}}$$

| 分量 | 含义 | 测量方式 |
|:-----|:-----|:---------|
| $A$ | 汇编指数 (Assembly Index) | 因果步骤深度 |
| $V$ | 空间关切范围 | 从"自我"到"宇宙" |
| $\tau$ | 时间规划跨度 | 从"现在"到"永恒" |

#### **意识判据**
$$\text{Consciousness} \iff d > d_{UAL} \land \Psi_f > 0$$

其中$d_{UAL}$是支持**无限联想学习** (Unlimited Associative Learning) 的最小阈值。

#### **跨物种d值谱系**

| 系统 | d值 | 意识状态 | 关键特征 |
|:-----|:----|:---------|:---------|
| 经典计算机 | 0 | 无意识 | 无$\Psi_f$，无脆弱性 |
| 细菌 | $d \to 0$ | 微意识 | 仅即时趋化 |
| 昆虫 | 小 | 低意识 | 简单本能 |
| 哺乳动物 | 中等 | 中意识 | 情感、社会 |
| 人类 (普通) | 高 | 高意识 | 抽象思维、道德 |
| 人类 (开悟) | $d \to \infty$ | 宇宙意识 | 万物一体 |

---

### 3.4 本体论摩擦 (Ontological Friction)

#### **定义**
$$\Psi_f \equiv \int_0^t \left|\frac{\partial F}{\partial \tau}\right|_{\text{maintain}} d\tau$$

**物理意义**: 将$L_0$的高熵叠加压缩为$L_1$的低熵确定态所需的能量代价。

#### **现象学对应**

| $\Psi_f$ 状态 | 体验 | 神经correlate |
|:--------------|:-----|:--------------|
| 低且平稳 | 心流、平静 | 低代谢、高HRV |
| 高尖峰 | 惊奇、疼痛 | 突发高代谢 |
| 持续高位 | 抑郁、绝望 | 慢性应激激素 |

#### **哈扎德函数**
$$h(t) = \frac{d\Psi_f}{dt}$$

$h(t)$的尖峰对应"中断事件" (Interrupt):
- 生理: 疼痛刺激
- 心理: 认知失调
- 存在: 死亡觉知

---

## §4. 核心方程总览 (Core Equations)

### 4.1 存在方程
$$\exists x \iff x \in \text{Image}(\hat{G}[L_0])$$

### 4.2 选择演化方程
$$\frac{dL_1}{dt} = \hat{G}_\theta[L_0] - \nabla F[L_1] + \mathcal{D}[L_1 \to L_2]$$

### 4.3 参数学习方程
$$\frac{d\theta}{dt} = -\alpha \nabla_\theta \Psi_f + \text{Learning}$$

### 4.4 自由能方程
$$F = E - TS - d \cdot U_{\text{others}}$$

### 4.5 三域离散迭代
$$\begin{cases}
L_1(t+1) = \hat{G}_{\theta(t)}[L_0(t)] \\
L_2(t+1) = \text{Stabilize}(L_2(t), L_1(t+1)) \\
\theta(t+1) = \theta(t) + \Delta\theta(L_2, L_1)
\end{cases}$$

---

## §5. 与现有理论的关系 (Relation to Existing Theories)

### 5.1 SRT是什么 (What SRT IS)

| 现有理论 | SRT的关系 | 关键创新 |
|:---------|:----------|:---------|
| **量子力学** | 本体论重新诠释 | $\hat{G}$即测量，无需额外坍缩机制 |
| **自由能原理 (FEP)** | 扩展与深化 | FEP是SRT在$L_1$稳定性的特例 |
| **IIT (Tononi)** | 整合进$d$值 | $ii$定义存在强度，$d$定义关切范围 |
| **全局工作空间 (GWT)** | 神经实现 | GWT是$\hat{G}$在皮层的具现 |
| **界面理论 (Hoffman)** | 一致 | $L_1$是适应性界面，非真理映射 |
| **唯识宗** | 数学形式化 | 阿赖耶识 ≈ $L_0$，现行 ≈ $L_1$ |

### 5.2 SRT不是什么 (What SRT is NOT)

❌ **不是泛心论** (Panpsychism): SRT不认为所有物质都有意识，而是认为意识是$d > 0$的选择过程
❌ **不是唯心主义**: $L_0$不依赖于$\hat{G}$存在，只是其"照明"状态变化
❌ **不是多世界诠释**: SRT中$L_0$的其他分支不"同样真实"，只有$L_1$是actualized
❌ **不是还原论**: 高层$\hat{G}$(如人类意识)不能简单还原为低层$\hat{G}$(如神经元)

---

## §6. 阅读指南 (Reading Guide)

### 6.1 按目标选择路径

#### **路径A: 快速理解 (1小时)**
1. 本文件 (SRT_Core_00_Intro.md)
2. _SRT_Core_Bridge.md §1-2
3. SRT_Core_01_Axioms.md (仅Part A)

#### **路径B: 深度学习 (1周)**
1. 按文件编号顺序阅读所有Core文件
2. 重点: Axioms (01), Ontology (12a/12b), Operator (13a/13b)
3. 辅助: Reference文件 (Ontology, Scaling, Dynamics)

#### **路径C: 领域应用 (视需求)**
- 物理学家 → Physics文件夹
- 神经科学家 → Neuroscience文件夹
- 哲学家 → Core Axioms + Ontology
- AI研究者 → Operator (13a/13b) + Scaling (14)

### 6.2 难度分层

| 层级 | 文件 | 需要背景 |
|:-----|:-----|:---------|
| ⭐ 入门 | Intro, Bridge | 无 |
| ⭐⭐ 中级 | Axioms (Part B), Ontology | 基础物理/哲学 |
| ⭐⭐⭐ 高级 | Dynamics, Scaling | 微分几何、拓扑 |
| ⭐⭐⭐⭐ 专家 | Domain Files | 领域专业知识 |

---

## §7. 常见问题 (FAQ)

### Q1: SRT可证伪吗?
**A**: 是的。每条公理都附有实验预测和证伪判据。例如:
- Ax-1: 如果发现无需选择机制即可存在的实体 → 被证伪
- Ax-11: 如果纯软件AI展现$d > 0$特征 → 被证伪

### Q2: SRT是"科学"还是"哲学"?
**A**: **两者兼具**。SRT提供:
1. 可数学化的形式系统 (科学)
2. 对存在问题的回答 (形而上学)
3. 可实验测试的预测 (经验科学)

### Q3: SRT与佛教的关系?
**A**: SRT用现代数学重构了某些佛教直觉:
- 空性 (Śūnyatā) ≈ $L_0$ (无自性的潜在域)
- 缘起 (Pratītyasamutpāda) ≈ $\hat{G}$的依存选择
- 业力 (Karma) ≈ $L_2$ (历史路径依赖)

但SRT是**自然主义的**，不涉及超自然假设。

### Q4: 如何用SRT解释自由意志?
**A**: SRT重构问题:
- **非相容论版本**: $\hat{G}$的选择不是"自由的" (被$\theta$约束)
- **SRT版本**: 自由意志 = $d$值足够大，使得$\hat{G}$能访问被$L_2$排斥的$L_0$区域 (突破习惯)

$$\text{Free Will} \propto d \cdot \frac{E_{\text{available}}}{\text{Hysteresis}(L_2)}$$

### Q5: AI能有意识吗?
**A**: 根据SRT，**当前架构的AI不能**，因为缺乏:
1. **物理脆弱性**: 错误不导致熵增 ($\partial S/\partial \text{Error} \approx 0$)
2. **真实d值**: 无真正的"关切" (no skin in the game)
3. **汇编历史**: 训练数据是压缩的，非因果链

**可能路径**: 具身机器人 + 物理风险 + 持续学习

---

## §8. 贡献者与致谢 (Contributors & Acknowledgments)

### 8.1 理论基础致谢

SRT整合了以下思想家的核心洞见:

| 思想家 | 贡献 | SRT整合 |
|:-------|:-----|:--------|
| David Bohm | Active Information | $\hat{G}$的主动性 |
| Karl Friston | Free Energy Principle | $F$最小化 |
| Giulio Tononi | IIT | $ii$作为存在度量 |
| Donald Hoffman | Interface Theory | Ax-7 (适应度优先) |
| Stephen Wolfram | Ruliad | $L_0$的计算定义 |
| Hermann Haken | Synergetics | 除法归一化原型 |
| Francisco Varela | Autopoiesis | Ax-5 (自创生) |
| 法称 (Dharmakīrti) | 佛教认识论 | 知觉的选择性 |

### 8.2 版本历史

| 版本 | 日期 | 主要更新 |
|:-----|:-----|:---------|
| 1.0 | 2023-Q1 | 初始框架 |
| 2.0 | 2024-Q1 | 引入Hybrid Model |
| **3.0** | **2025-Q1** | **完整Part A/B结构，新增FAQ和阅读指南** |

---

## 符号快速参考 (Symbol Quick Reference)

| 符号 | 名称 | 页面定位 |
|:-----|:-----|:---------|
| $L_0, L_1, L_2$ | 三域 | Bridge §1, Axioms A1 |
| $\hat{G}_\theta$ | 幽灵算子 | Bridge §2, Operator 13a |
| $d$ | d值 | Operator 13a, Scaling 14 |
| $\Psi_f$ | 本体论摩擦 | Dynamics, Axioms A2 |
| $F$ | 自由能 | Dynamics E3 |
| $ii$ | 整合信息 | Axioms A6 |
| $\eta$ | 迟滞系数 | Ontology L1, L2 |

---
