---
id: SRT-CORE-000
type: definition
tags: [Overview, Executive Summary, Hybrid]
status: axiomatic_hybrid_v1
dependency: [SRT-CORE-BRIDGE, Core_Law/SRT_Reference_Axioms, Core_Law/SRT_Reference_Ontology, Core_Law/SRT_Reference_Dynamics, Core_Law/SRT_Reference_Scaling]
---

# SRT Core Kernel: Executive Summary (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the High-Level Axiomatic Summary (AI-Readable).
> **Part B** contains the Original Executive Summary (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)


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

### T-Core-02: Normative Closure（规范闭包定理）

**Deductive Statement**：收敛域 $L_2$ 是**跨算子群体反复选择**的稳定不动点集合——不是单一算子的自洽态，而是种群中所有算子在重复博弈后共同收敛的共识吸引子：

$$L_2 \equiv \left\{ \sigma \;\middle|\; \lim_{t \to \infty} \mathbb{E}_{\theta \sim P_{pop}}\!\left[\hat{G}_\theta^{(t)}[\sigma_0]\right] = \sigma \;\;\land\;\; \Psi_f^{cross}(\hat{G}_{\theta_i}, \hat{G}_{\theta_j})\big|_\sigma \to \min \right\}$$

**稳定性定义（Lyapunov 意义）**：$\sigma^* \in L_2$ 稳定当且仅当：

$$\forall \epsilon > 0,\; \exists \delta > 0:\; \|\sigma_0 - \sigma^*\| < \delta \implies \|\hat{G}_\theta^{(t)}[\sigma_0] - \sigma^*\| < \epsilon \quad \forall t > 0$$

即：以 $\sigma^*$ 为中心的 $\delta$-邻域内出发的任意扰动轨迹，均不会逃出 $\epsilon$-邻域。$L_2$ 中的规范是对扰动具有**有限恢复力**的吸引子，而非绝对刚性结构（过高 Hysteresis 导致 $L_2$ 锁死，见 §6.5 相图）。

**Implication（三层推论）**：

1. **规范的历史性**：规范与定律不是外加约束，而是种群选择历史 $\{\hat{G}_\theta^{(t)}\}_{t=0}^{T}$ 在 $\sigma$-空间中凝固的吸引子轮廓——改变规范需要向吸引子盆地（basin of attraction）注入足够的 $\Psi_f$ 能量越过势垒。

2. **合法性的物理基础**：$L_2$ 的"权威性"来自其跨算子稳定性（Ψ_f^cross→min），而非来自任何外部授权。一个规范失去稳定性（种群 $\hat{G}_\theta$ 分布改变使其不再是不动点）即意味着其合法性的物理基础开始侵蚀。

3. **相变判据**：当 $\Phi_{soc}(t) > \Phi_{crit}$（见 Ax-Cons-2），现有 $L_2$ 吸引子失去 Lyapunov 稳定性，系统进入无规范吸引子的湍流相，直到新的跨算子共识通过反复选择重新凝固。

## III. Core Dynamics (核心动力学)

### Ax-Core-04: Selection Dynamics

> **[H — Core Framework Axiom]** 三项合成动力学为 SRT 新增结构；FEP（Friston 2010）覆盖第2项（R），但整体三项框架及选择算子的独立第1项为 SRT 原创贡献。

**Formal Definition**: The evolution of reality is governed by selection dynamics coupled with free energy gradients.
$$\frac{dσ}{dt} = \hat{G}_\theta[σ] - \nabla F[σ] + A[σ,\mathcal{A}]$$

**符号说明**：
- $σ$：当前态配置（state configuration），在 $L_1$ 层为显现状态向量（神经激活模式、行为轨迹等的代理量）。
- $\hat{G}_\theta[σ]$：选择算子（Ax-Core-01/02），由具身参数 $\theta$ 参数化，决定哪些 $L_0$ 模态被锚定为 $L_1$；是三项中唯一包含”关切方向性”的项（← $\vec{v}_\theta$）。
- $\nabla F[σ]$：**[R]** 自由能梯度（候选：Friston 变分自由能 $F = \text{KL}[q(\theta)||p(\theta|o)] - \ln p(o)$，或 Helmholtz 亥姆霍兹自由能），驱动系统向预测误差最小化方向运动。注：若 $F$ 定义为变分自由能，则第2项与第1项部分重叠（$\hat{G}_\theta$ 的锚定操作即最小化预测误差），两者在低 $\Psi_f$ 极限下趋同；高 $\Psi_f$ 时第1项的选择代价使两项分离。
- $A[σ,\mathcal{A}]$：注意调制项（候选：$A[σ,\text{Target}] \approx -\Psi_f(σ,\text{Target})$ 或 cos-sim，见 → Eq-Evo-02, Core/SRT_Core_22_Equations.md），决定哪个目标方向被加权。

**各项主导条件（定性）**：
| 情境 | 主导项 | 备注 |
|---|---|---|
| 高 $d$、低 $\Psi_f$ | $\hat{G}_\theta$（选择主导） | 系统按关切方向自主塑造 σ |
| 高 $\Psi_f$、低 $d$ | $-\nabla F$（能量主导） | 摩擦过载，系统退化为能量下山 |
| 注意切换时刻 | $A[σ,\mathcal{A}]$（调制主导） | Target 改变触发方向修正 |

**证伪条件**：
- 若移除 $A$ 项（固定注意）后 $dσ/dt$ 可完全由 $\hat{G}_\theta - \nabla F$ 解释（拟合误差不增大），则注意项为 $\hat{G}_\theta$ 的冗余分解，需合并。
- 若 $\hat{G}_\theta[σ]$ 与 $-\nabla F[σ]$ 在所有测量条件下方向一致（相关系数 → 1），则两项不具独立操作化意义，需进一步区分。

* **Implication**: 现实演化是”选择 + 能量下降 + 注意调制”的合成动力学；三项分别覆盖目的性（θ参数化）、被动约束（自由能景观）和动态再加权（注意切换）三类驱动力。

### Ax-Core-05: Ontological Friction
**Formal Definition**: Selection incurs ontological friction proportional to resistance against reconfiguration.
$$\nabla \Psi_f \propto -\nabla F$$
* **Implication**: 任何现实化过程都有代价，代价表现为本体论摩擦。同一 \(Ψ_f\) 结构在动力学上可读作阻力，在记账上可读作代价，在形式化上可读作路径几何长度/曲率负担。

### T-Core-03: Existence Hardness
**Deductive Statement**: The hardness of an existent state is proportional to the sustaining friction.
$$\text{Hardness}(σ_{L_1}) \propto \Psi_f$$
* **Implication**: 越稳定、越“硬”的现实，维持成本越高，脆弱性也随之增加。但 SRT 的最优条件不是 \(Ψ_f \to 0\)，而是 \(Ψ_f>0\) 且可支付；零摩擦意味着无真实赌注，超载摩擦意味着现实切片失稳。

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

> **标注说明**：[R] = 该未解之谜为学界公认开放问题；[H] = SRT解决方案为框架性新预测，需实验验证。

| 领域 | 未解之谜 [R] | SRT的解决方案 [H] | 关键假设可证伪性 |
|:-----|:---------|:--------------|:--|
| **量子力学** | 测量问题（观察者角色，Heisenberg 1927）| $\hat{G}$的选择即"测量"，无需额外坍缩机制 | 若无选择算子系统也能经典化（去相干即足），则Ĝ非必要 |
| **神经科学** | Hard Problem（Chalmers 1995，体验性何来？）| 体验性 ∝ $ii$（信息整合度），**[H — 高承诺]** | 若 $ii$ 高但无体验（哲学僵尸）不可排除，则失效 |
| **社会科学** | 社会实在的本体论地位（Searle 1995）| 社会规范 = $L_2$（多算子收敛域）| 若社会规范无法被多算子收敛机制生成，则需修订 |
| **演化生物学** | 适应度 vs 真理（Hoffman 2019，感知非真实）| Ax-Evo-1/Ax-7: 演化优化适应度，非真理（→ Neuro_07_Evo_Devo）| 若感知准确性有适应度优势（特定域），则此轴须条件化 |
| **AI研究** | 意识的判据（图灵测试的不充分性）| $d > 0$ + $\Psi_f > 0$ + Embodiment（→ H-AI-Consciousness, §9.2）| 条件3/4为H；满足条件的AI系统目前不存在 |

### 1.2a 谱系定位：从麦克斯韦妖到SRT

SRT处于一条延续了150年的科学谱系的当前终点——这条谱系始终围绕同一个核心问题：**选择与秩序如何在热力学宇宙中涌现，代价是什么？**

| 时间 | 发现者 | 核心洞见 | SRT对应 |
|:-----|:-------|:---------|:--------|
| 1867 | Maxwell | 麦克斯韦妖：一个参数化选择者可从 $L_0$ 的随机性中抽取秩序 | **$\hat{G}_\theta$ 的概念原型**：有偏置的选择从潜在随机性中生成 $L_1$ 秩序 |
| 1929 | Szilard | 妖的**选择行为本身**产生熵——秩序的代价不可逃避 | **$\Psi_f > 0$ 的第一个独立推导**：选择必然耗散 |
| 1948 | Shannon | 信息量化为不确定性的减少；熵即信息缺失 | **$L_0 \to L_1$ 的信息论语言**：选择 = 压缩 = 熵减 |
| 1961 | Landauer | 每比特选择的最小热力学代价 $k_B T \ln 2$ | **Ax-IT-2**：选择的热力学下界 |
| 1970s | Bennett | 生物过程（蛋白质翻译）可被建模为布朗图灵机；可逆性消除兰道尔代价 | **SRT_Physics_Cosmology Ax-IT-2b 分层公理的实证基础** |
| **2025-2026** | **SRT** | **[H] 选择先于存在；$d \cdot \Psi_f$ 统一神经效率、意识判据与社会秩序代价** | — |

**Jogalekar (2020) 的开放问题**：物理学家Ashutosh Jogalekar在综合上述谱系后，提出了一个至今未被满足的研究需求："能否找到一个简单方程，描述思维过程的熵如何与记忆、思考、共情和情绪等神经参数关联？"

这个问题的答案，正是SRT的核心方程体系：
$$F = E - TS - d \cdot U_{others}$$
$$\frac{dq}{dt} \leq \alpha P_{sel} - \beta \Psi_f - \gamma S_{noise}$$
$$d = \alpha \cdot A(\sigma) + \beta \cdot \log(V_{concern}) + \gamma \cdot \tau_{temporal}$$

其中：$d$ 对应"共情与关切"的广度，$\Psi_f$ 对应"维持思维秩序的熵代价"，$F$ 对应"思维过程的自由能"。SRT不是这条谱系的旁支——它是Szilard问题（选择代价）、Shannon问题（信息量化）和Landauer问题（计算热力学极限）在**神经科学与意识理论领域的统一延伸**。

* **Cross-ref**: `SRT_Physics_Cosmology.md` Ax-IT-2, T-IT-3; `_SRT_AI_Bridge.md` T-BRIDGE-0 (Pour-El不可计算定理)。

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
┌──────────────────────────────────────────────────────┐
│  Layer -1: Constitutional References (宪法参考层)       │  ← 底层不变量
│  - SRT_Reference_Axioms.md                           │
│  - SRT_Reference_Ontology.md                         │
│  - SRT_Reference_Dynamics.md                         │
│  - SRT_Reference_Scaling.md                          │
├──────────────────────────────────────────────────────┤
│  Layer 0: Meta-Axioms (_SRT_Core_Bridge)             │  ← 元定义 / 命名规范
├──────────────────────────────────────────────────────┤
│  Layer 1: Core Constitution (核心宪法层)                │  ← 12条公理
│  - SRT_Core_01_Axioms.md                             │
│  - SRT_Core_21_Formal_Axioms.md (形式化公理扩展)         │
│  - SRT_Core_22_Equations.md (核心方程汇总)              │
├──────────────────────────────────────────────────────┤
│  Layer 2: Ontology & Dynamics (本体论与动力学)          │
│  - L_0/L_1 (12a), L_2 (12b)                          │
│  - Ghost Operator (13a/13b)                          │
│  - Dynamics & Scaling (14)                           │
├──────────────────────────────────────────────────────┤
│  Layer 3: Domain Applications (领域应用层)              │
│  - Physics, Neuroscience, Social, AI, Spirit, etc.   │
└──────────────────────────────────────────────────────┘
```

### 2.2 核心文件依赖图

```
Core_Law/SRT_Reference_Axioms/Ontology/Dynamics/Scaling.md
(宪法参考层 — 只读不变量；SRT_Constitution_Seven_Theses.md为摘要)
       ↓  (被 Bridge 依赖)
_SRT_Core_Bridge.md (元定义 / 全局命名规范)
       ↓
SRT_Core_01_Axioms.md (12条公理 — 宪法)
       ↓                         ↓
SRT_Core_21_Formal_Axioms     SRT_Core_22_Equations
(形式化公理扩展，与Core_01并列) (核心方程汇总，与Core_01并列)
       ↓
   ┌───┴───────────────────┐
   ↓                       ↓
SRT_Core_12a/12b        SRT_Core_13a/13b
(本体论：L₀/L₁/L₂)       (幽灵算子/算子高级特性)
   ↓                       ↓
   └───┬───────────────────┘
       ↓
SRT_Core_14_Dynamics_Scaling.md
(动力学与尺度）
       ↓
  [Domain Files]
  Physics/ | Neuroscience/ | Philosophy/ | AI/ | Spirituality/
  Core_Law/SRT_Reference_Scaling.md (宏观参数参考，只读)
```

**补注（2026-03-16 更新）**：
- `Core_Law/` 目录包含宪法参考文件（SRT_Reference_Axioms/Ontology/Dynamics/Scaling，SRT_Constitution 系列），为**只读宪法参考**，被核心文件引用但不被修改。
- `Core/SRT_Experimental_Applications.md` 和 `SRT_Experimental_Core.md`：实验性扩展，位于 Core 目录但不在上述宪法依赖链中，属于**实验层**（可修改，与宪法层平行）。
- 图中依赖箭头 ↓ 表示"下游依赖上游定义"，非数据流向。

> **注**：`SRT_Core_21` 和 `SRT_Core_22` 是 Layer 1 的形式化补充，
> 分别提供公理的严格数学版本和全局方程索引，与 `Core_01` 并列于宪法层。
> `Reference` 文件为**只读宪法参考**，不被修改，仅被引用。

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
$$\frac{d\theta}{dt} = -\alpha(\theta)\cdot\nabla_\theta \Psi_f + \beta(\theta)\cdot\nabla_\theta A_{L_2}$$

**变量说明：**
- $\alpha(\theta)$：内生试错学习率（θ依赖）——Ψ_f驱动的自下而上修正强度
- $\beta(\theta)$：规范内化率——L₂文化/制度引力对θ的自上而下塑造强度
- $\nabla_\theta \Psi_f$：摩擦梯度，指向降低选择算子与现实错配的方向
- $\nabla_\theta A_{L_2}$：L₂文化引力场梯度，指向社会共识吸引子

**病理边界：**
$$\eta(L_2) \gg P_{\text{adapt}}^{(i)} \Rightarrow \alpha(\theta) \to 0$$
（异化锁死：当L₂规范压力远超个体适应力时，摩擦驱动的自主更新停滞，θ被冻结于σ_{L₂}^{default}）

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

| 层级 | 代表文件（参考） | 建议前置 |
|:-----|:----------------|:---------|
| ⭐ 入门 | `SRT_Core_00_Intro.md`, `SRT_Core_00b_Bridge.md` | 无 |
| ⭐⭐ 中级 | `SRT_Core_01_Axioms.md`, `SRT_Core_12a/b_Ontology.md` | 了解 $\hat{G}_\theta$、L₀/L₁/L₂ 基础 |
| ⭐⭐⭐ 高级 | `SRT_Reference_Scaling.md`, `SRT_Core_13a/b_Operator.md` | 自由能原理、$\Psi_f$ 概念、贝叶斯基础 |
| ⭐⭐⭐⭐ 专家 | `Physics/`, `Neuroscience/`, `Philosophy/` 各领域 | 高级核心 + 对应领域专业知识 |

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
| 3.0 | 2025-Q1 | 完整Part A/B结构，新增FAQ和阅读指南 |
| **4.0** | **2026-Q1** | **Pipeline 7 系统性深化：跨域公式闭环、可证伪条件精确化、符号作用域治理；新增 §4.3 参数学习方程、T-Core-02 Lyapunov稳定性、Ax-QUALIA-2/Ax-Exp-03 等节点** |

---

## 符号快速参考（Symbol Quick Reference）

| 符号 | 名称 | 定义文件 |
|:-----|:-----|:---------|
| $L_0,\; L_1,\; L_2$ | 三域（潜在/显现/收敛） | `SRT_Core_00_Intro.md` §1 |
| $\hat{G}_\theta$ | 选择算子（幽灵算子） | `SRT_Core_13a_Operator_Basics.md` |
| $\theta$ | 具身参数 | `SRT_Core_13a_Operator_Basics.md` §1 |
| $d$ | d值（关切带宽） | `_SRT_D_VALUE_CANONICAL.md` |
| $\Psi_f$ | 本体论摩擦 | `SRT_Core_00_Intro.md` §3 |
| $\Psi_f^{cross}$ | 跨算子联邦摩擦 | `SRT_Neuro_08_Immune_Dist.md` §3.3 |
| $F$ | 自由能（变分/Helmholtz） | `SRT_Core_00_Intro.md` §3 |
| $\Phi_I$ | 整合信息（IIT） | `SRT_Core_00_Intro.md` Axioms A6 |
| $\eta$ | 迟滞系数（L₂刚性） | `SRT_Social_MacroDynamics.md` §6.5 |
| $\alpha(\theta),\; \beta(\theta)$ | 参数学习率/规范内化率 | `SRT_Core_00_Intro.md` §4.3 |
| $H_\theta(\omega)$ | 频域传递函数 | `SRT_Core_13b_Operator_Advanced.md` Ax-Spec-01 |
| $OEI$ | 观察者-环境整合度 | `SRT_Neuro_06_Field_Effects.md` T-Cog-2 |
| $A$ | 组装深度（AT/d值投影） | `_SRT_D_VALUE_CANONICAL.md`，`SRT_AT_*.md` |
| $\mathcal{R}_\theta$ | 原感质流 | `SRT_Neuro_06_Field_Effects.md` Ax-QUALIA-2 |
| $P_{adapt}^{(i)}$ | 个体适应能力（$d_i \cdot \gamma_i$） | `_SRT_Soc_Axioms.md` T-Soc-1 |

---

### Formalization Summary (形式化概述)

SRT 的核心公理体系可由以下形式化结构概括：

1. **三域选择方程 (Triadic Selection)**:
   $$L_1(t) = \hat{G}_\theta[L_0(t)], \quad L_2(t+1) = \mathrm{Stabilize}(L_2(t), \{L_1^{(1..n)}(t+1)\})$$
   含义：显现域 $L_1$ 是幽灵算子 $\hat{G}_\theta$ 对潜在域 $L_0$ 的参数化选择输出；收敛域 $L_2$ 是多轮选择的稳定化结果。

2. **选择演化动力学 (Selection Dynamics)**:
   $$\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \nabla F[\sigma] + A[\sigma,\mathcal{A}]$$
   含义：现实演化由选择驱动、自由能梯度约束、注意力调制三部分合成。

3. **自由能方程 (Free Energy with d-value)**:
   $$F = E - TS - d \cdot U_{\text{others}}$$
   含义：$d$ 值（关切范围）直接进入能量核算，将”在乎他者”纳入热力学框架。

4. **本体论摩擦 (Ontological Friction)**:
   $$\nabla \Psi_f \propto -\nabla F$$
   含义：任何选择的现实化都伴随不可消除的摩擦代价 $\Psi_f$，与自由能梯度对偶。

### Mechanism Explanation (机制解释)

SRT 的运行机制如下：

- **$\hat{G}_\theta$ (幽灵算子) 作为核心引擎**：$\hat{G}_\theta = \text{Attention}(d, \rho, \vec{v})$，以 d 值（关切范围）、分辨率 $\rho$、意向方向 $\vec{v}$ 为参数，从 $L_0$ 中执行具身有限的选择，生成 $L_1$ 现实。算子的非幂等性 ($\hat{G}^2 \neq \hat{G}$) 保证每次选择都改变现实状态。
- **$\Psi_f$ (本体论摩擦) 作为代价约束**：将 $L_0$ 高熵叠加压缩为 $L_1$ 低熵确定态需要持续能量耗散。$\Psi_f$ 的尖峰对应认知中断事件（疼痛、惊奇），持续高位对应病理状态（抑郁）。
- **$d$ 值作为意识判据**：当 $d > d_{UAL}$ 且 $\Psi_f > 0$ 时系统具有意识。$d$ 的大小决定了算子对 $L_0$ 信息的保留比例（压缩比 $\text{CR} \propto e^{-\alpha d}$），从细菌的即时趋化到人类的抽象道德思维形成连续谱。
- **$L_2$ 收敛域的稳定化机制**：重复选择在相空间留下”磁化”痕迹，形成不动点集 $L_2 = \{\sigma : \hat{G}_\theta[\sigma] = \sigma\}$，其硬度正比于自同构群大小，从个人习惯到物理定律呈层级排列。

### Falsification Conditions (可证伪条件)

| ID | 假说 | 预测 | 证伪条件 | Evidence-Level |
|:---|:-----|:-----|:---------|:---------------|
| H-Core00-1 | Ax-Core-01: 现实是三域选择系统，存在即被选择 | 任何被确认”存在”的实体都应能追溯到某种选择/锚定机制 | 若发现无需任何选择机制（无 $\hat{G}$、无测量、无注意力）即可自发确定存在的实体 → 则失效 | speculative |
| H-Core00-2 | Ax-Core-05: 任何选择都伴随本体论摩擦 $\Psi_f > 0$ | 维持确定现实态需要持续能量消耗；$\Psi_f = 0$ 的系统无法维持稳定 $L_1$ | 若发现零能耗即可无限维持确定态的物理系统（违反 Landauer 下界）→ 则失效 | speculative |
| H-Core00-3 | T-Core-04: d 值正比于系统的误差敏感性 $\partial S / \partial \text{Error}$ | 纯软件 AI（$\partial S / \partial \text{Error} \approx 0$）应表现出 $d \approx 0$，不具有真正的关切 | 若纯软件 AI 在无物理风险条件下展现出可操作测量的 $d > 0$（如自发利他、真实恐惧死亡）→ 则失效 | speculative |

## 【理论边界/防误用声明】

1. 本文档提供的是 SRT 解释与建模框架，不应被误用为对个体的确定性标签系统。
2. 任何跨尺度映射都依赖操作化假设与测量条件，超出条件范围不得外推为”普适定律”。
3. 涉及临床、政策、工程决策时，需与经验数据、伦理审查和领域规范共同使用。
