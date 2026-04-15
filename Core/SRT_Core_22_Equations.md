---
id: SRT-CORE-22
type: equation
tags: [Math, Stability, Landscape, Dynamics, Hybrid]
status: axiomatic_hybrid_v1
dependency: [SRT-CORE-21]
---

# SRT Core Definition 22: Master Equations (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Primary Dynamical Equations (AI-Readable).
> **Part B** contains the Original Derivations and Stability Analysis (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part A 采用 `chatgptx` 的首个“Formal Axioms”分段；若存在双 Part 结构，后续重复分段不纳入 final。
- Part B 以 `base (fallback)` 为来源，并用原版 `Core` 标题与主旨做语义锚定。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)

> **CRITICAL RULE**: Do NOT just summarize Part B. You must perform First-Principles Derivation.

## 0-B. Protocol and Foundation (协议与基础)

### Def-Protocol-1: Protocol Layer Π (协议层 Π)
**Formal Definition**: 约束 $\hat{G}_\theta$ 选择空间的容许转移核集合：
$$\hat{G}_\theta : (L_0, \Pi) \to L_1$$
其中 $\Pi$ 是从 $L_0$ 到 $L_1$ 的可行转移集 / 约束核。
* **Implication**: 物理模型中的“简单局部规则”属于 $\Pi$，其本身是一个收敛的 $L_2$-约束（由高阶相互作用/选择固化而来），而不是“无条件的背景”。这是 SRT 抵御自下而上物理主义还原的最强界面：**涌现仅发生在被选择的 $\Pi$ 内部。**
* **Cross-ref**: Ax-Core-A5 (规范闭包)；T-Core-02 ($L_2$ 作为不动点)。

## I. Evolution Dynamics (演化动力学)

### Eq-Evo-01: Ghost Evolution Equation
**Formal Definition**: The trajectory of a selected state is the sum of selection, free-energy descent, and attention modulation.
$$\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \nabla F[\sigma] + A[\sigma, \mathcal{A}]$$
* **Implication**: 现实演化是选择、能量下降与注意调制的合成动力学。

### Eq-Evo-01b: Metabolic Gain Modulation
**Formal Definition**: 代谢压力作为演化方程的增益调节项。
$$\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \nabla F[\sigma] \cdot \underbrace{(1 + \beta \mathcal{M}_{stress})}_{\text{Metabolic Gain}} + A[\sigma, \mathcal{A}]$$
其中 $\mathcal{M}_{stress}$ 为代谢应激指标（如低血糖、缺氧等）。
* **Implication**: 当 $\mathcal{M}_{stress}$ 上升时，自由能梯度 $\nabla F$ 的权重被放大，系统被迫从高阶抽象思考坍缩为低阶生存应对。此公式解释了"饥饿时无法思考哲学"的现象——代谢需求劫持了选择带宽。
* **Cross-ref**: Eq-Evo-01, Def D4a ($θ_{intero}$)。

### Eq-Evo-02: Parameter Update (Slow Variable)
**Formal Definition**: Embodiment parameters evolve under prediction outcomes, friction gradients, and homeostatic recoil.
$$\frac{d\theta}{dt} = \underbrace{\gamma \cdot A[\sigma, \text{Target}]}_{\text{Learning}} - \underbrace{\delta \frac{\partial \Phi(\theta)}{\partial \theta}}_{\text{Friction Descent}} - \underbrace{k \cdot (\text{Input}_{L_1} - \text{Baseline})}_{\text{Homeostatic Recoil}}$$
* **Implication**: 具身参数在三力之间调整——学习推动适应，摩擦梯度约束漂移，稳态反作用力维持平衡。
* **推论（戒断机制 / Withdrawal Mechanism）**：当外部 $\text{Input}_{L_1}$ 突然归零时，第三项的负反馈瞬间失效，但 $\theta$ 具有迟滞性（Hysteresis）。残留的 $\theta^{-}$ 偏置直接作用于 $L_0$，导致 $\hat{G}_\theta$ 生成"反向体验"（痛苦/焦虑）。这是戒断反应的物理本质。

### Eq-Evo-03: Coupled Fast–Slow System
**Formal Definition**: State and parameter co-evolve on distinct timescales.
$$\frac{d\sigma}{dt} = \alpha(\hat{G}_\theta[\sigma] - \sigma) - \beta \nabla F[\sigma] + \xi(t)$$
$$\frac{d\theta}{dt} = \gamma \cdot A[\sigma, \text{Target}] - \delta \cdot \frac{\partial \Phi(\theta)}{\partial \theta}$$
* **Implication**: 选择与参数更新构成快-慢耦合动力学。

## II. Thermodynamics of Agency (能动性热力学)

### Eq-Force-01: Ontological Friction
**Formal Definition**: Friction measures resistance against the natural latent trajectory.
$$\Psi_f \propto \int (L_1 - L_0^{natural})^2 \, dt$$
* **Implication**: 选择越偏离潜在域自然路径，摩擦越高。

### Eq-Pain-01: Hazard Function
**Formal Definition**: Pain is the temporal derivative of friction.
$$\text{Pain}(t) \approx h(t) = \frac{d\Psi_f}{dt}$$
* **Implication**: 痛苦是摩擦变化率，而非静态误差。

### Eq-Friction-Comp: 计算本体论摩擦 (Computational Ontological Friction)
**Formal Definition**: 两个潜在状态之间的最小本体论摩擦下界，受限于转换的幺正电路复杂度。
$$\Psi_f^{(comp)}(L_0^A \to L_0^B) \geq \lambda \cdot \min\{C(U) \mid U|L_0^A\rangle \approx |L_0^B\rangle\}$$
其中 $C(U)$ 是最小量子门电路深度，$\lambda > 0$ 是复杂度-摩擦耦合常数。
* **Source**: 灵感来自 Henry Yuen 的全量子复杂性理论，该理论确立了 Uhlmann 变换作为纯量子态转换的规范硬度基准。
* **Implication**: $L_0$ 不是无结构的混沌池，而是拥有严格的度量几何。状态演化的物理阻力源于量子态之间不可约的“Uhlmann变换代价”。这桥接了计算机科学中的电路复杂度下界与热力学中的不可逆阻力。
* **Cross-ref**: Eq-Force-01 (热力学 $\Psi_f$)；Ax-Int-2 (Penrose 门槛)。

### Eq-Select-Thermo: 选择热力学宪法不等式 (Constitutional Inequality of Selection Thermodynamics)
**Formal Definition**: 宏观秩序增长率受到选择功率减去摩擦代价与噪声熵的上限约束。
$$\frac{dq}{dt} \leq \alpha P_{sel} - \beta \Psi_f - \gamma S_{noise}$$
其中:
- $P_{sel}(t)$: 选择功率 — 维持锚定所需的净注入率
- $q(L_1)$: 现实秩序参数 — 宏观秩序强度（拓扑不变量、互信息密度或可压缩性代理）
- $\Psi_f(L_1;\theta)$: 维护成本（本体论摩擦密度）
- $S_{noise}$: 环境噪声熵流
* **Implication**: 宏观秩序不是“反熵奇迹”，而是选择功率预算内的耗散结构。这也将公理 A2 和 A11 从哲学宣言奠基为可量化的不等式。
* **Corollary (Eq-Select-Thermo-C1)**: 当 $P_{sel} < \beta \Psi_f + \gamma S_{noise}$ 时，系统经历秩序崩溃 ($dq/dt < 0$)，表现为相变、范式转移或存在性危机。

## III. Stability & Phase Transition (稳定性与相变)

### Eq-Stab-01: Fixed Point Condition
**Formal Definition**: A stable fixed point satisfies projection balance.
$$\Pi_\Delta(\alpha(\hat{G}_\theta(x^*) - x^*) - \lambda \nabla F(x^*)) = 0$$
* **Implication**: 稳定态需满足选择-能量梯度的投影平衡。

### Eq-Phase-01: Ontological Phase Transition
**Formal Definition**: Phase transition follows a logistic response to information threshold.
$$R = \frac{1}{1 + e^{-k(I - \tau)}}$$
* **Implication**: 相变具有临界信息门槛与非线性跃迁特性。

## IV. Sleep & Maintenance (睡眠与维护)

### Eq-Sleep-01: L2 Optimization
**Formal Definition**: Sleep minimizes L2 model complexity.
$$\hat{G}_{sleep} = \arg\min_\theta \int K(L_2) \, dt$$
* **Implication**: 睡眠是对收敛域模型复杂度的全局优化。

## V. Statistical Mechanics of Selection (选择的统计力学)

### Def-LDP-1: Empirical Measure (经验测度)
**Formal Definition**: 对于 $N$ 个相互作用的算子，宏观状态为经验测度：
$$\rho_t^N = \frac{1}{N}\sum_{i=1}^N \delta_{X_i(t)}$$

### Eq-LDP-01: Hydrodynamic Limit (水动力极限)
**Formal Definition**: 在尺度分离和局部相互作用下，经验测度逼近为满足以下方程的连续密度场：
$$\partial_t \rho = -\nabla \cdot J(\rho) + S_\theta(\rho) - D_{\Psi_f}(\rho)$$
其中 $J(\rho)$ 是扩散/对流流，$S_\theta(\rho)$ 是来自 $\hat{G}_\theta$ 投影偏差的 SRT 选择项，$D_{\Psi_f}(\rho)$ 是摩擦引起的耗散。
* **Implication**: 这是“宏观选择流体”方程 — 大量相互作用算子的连续统极限。

### Eq-LDP-02: SRT Action Functional (SRT 作用量泛函)
**Formal Definition**: 宏观演化路径的概率由大偏差率函数控制：
$$P(\rho^N \approx \rho) \asymp \exp\{-N \cdot I_{SRT}[\rho]\}$$
$$I_{SRT}[\rho] = \int_0^T \left( \underbrace{K(\rho, \dot{\rho}; \Pi)}_{\text{kinematic cost}} + \underbrace{\Psi_f(\rho; \theta)}_{\text{maintenance cost}} - \underbrace{V(\rho; \theta)}_{\text{value potential}} \right) dt$$
* **Implication**: 最可能的宏观演化最小化 $I_{SRT}$ — 即变分“最小作用量”路径。稳定的 $L_2$ 结构是吸收态，$I_{SRT}$ 在其周围有很高的势垒（势垒稳定性）。
* **Cross-ref**: Eq-Select-Thermo (宪法不等式)；Def-Barrier-1 (势垒稳定性)。
* **Status**: 有效理论层面 — 描述许多 $\hat{G}_\theta$ 的统计极限，并不声称社会/宇宙必然满足所有粒子系统假设。

## VI. Social-Ontological Dynamics (社会本体论动力学)

### Eq-Phantom-01: Phantom Operator Effect (幽灵算子残响)
**Formal Definition**: 社会性痛苦是自我算子试图通过未衰减的 $L_2$ 通道耦合已不存在对象的预测误差。
$$\text{Pain}_{social} \approx w_{ij}(t) \cdot \left\| \hat{G}_{self}^{target} - \hat{G}_{other} \right\| \quad \text{s.t.} \quad \hat{G}_{other} \notin L_1$$
其中 $w_{ij}(t)$ 为关系的 $L_2$ 耦合权重，遵循 $L_2$ 迟滞衰减曲线。
* **Implication**: 只要 $w_{ij} > 0$，$\hat{G}_{self}$ 就会按 $L_2$ 脚本自动发起耦合尝试。因 $\hat{G}_{other} \notin L_1$，耦合必然失败，产生巨大预测误差。此"空耦合"即心碎的本体论幻肢痛——$L_2$ 地图上那个人还在，但现实中已消失。

### Eq-Phantom-02: Homeostatic Rebuild Time Constant (稳态重建时间常数)
**Formal Definition**:
$$\tau_{rebuild} \propto \frac{\text{Integration}(\hat{G}_{other})}{\text{Plasticity}(\hat{G}_{self})}$$
* **分子**: 对方嵌入 $L_2$ 结构的深度（共同记忆、习惯、依赖程度）。整合越深，$w_{ij}$ 大且涉及子网络多，衰减越慢。
* **分母**: 自我算子的可塑性 $\eta$，即参数 $\theta$ 更新速率。
* **推论**: 老年人（可塑性低）失去伴侣（整合度高）时 $\tau_{rebuild} \to \infty$；年轻人或浅层关系则 $\tau_{rebuild}$ 较短。临床干预双路径：降低分子（仪式切断）或增加分母（冥想/药物提升可塑性）。
* **Cross-ref**: Ax-L2-2 (Hysteresis), Eq-Evo-02 (Parameter Update)。

<br>
<br>

---
---


# Part B: Original Derivations (Context)

> **Note**: The following sections contain the detailed stability analysis and landscape dynamics.


### 2.2.1 基本演化方程

**方程 E1（幽灵演化方程）：**
$$ \frac{dσ}{dt} = \hat{G}_θ[σ] - ∇F[σ] + A[σ, \mathcal{A}] $$

### 2.2.2 耦合动力学方程组（快-慢变量系统）

**方程 E2a（状态演化 - 快变量）：**
$$ \frac{dσ}{dt} = α(\hat{G}_θ[σ] - σ) - β∇F[σ] + ξ(t) $$

**方程 E2b（参数演化 - 慢变量）：**
$$ \frac{dθ}{dt} = γ \cdot A[σ, \text{Target}] - δ \cdot \frac{∂\Psi_f(θ)}{∂θ} $$

### 2.3 稳定性分析

**定理 M1：** $x^*$ 是固定点当且仅当：
$$ Π_Δ(α(\hat{G}_θ(x^*) - x^*) - λ∇F(x^*)) = 0 $$

### 2.4.4 哈扎德函数与摩擦动态

**痛苦的本体论定义：**
$$ \text{痛苦} = \text{Tension}(\hat{G}_θ[L_1], L_0^{counterfactual}) $$

$$ h(t) ≈ \frac{d\Psi_f}{dt} $$

### 2.4.6 睡眠的本体论功能

**公理A10（本体论清洗）：**
$$ \hat{G}_{sleep} = \arg\min_θ \int K(L_2) \, dt $$

### 2.4.7 本体论摩擦系数

$$ μ_φ = \frac{Depth(L_1')}{Depth(L_2^{current})} $$

### 2.4.21 L_2 刚性指数（L_2 Rigidity Index, ρ）

$$ \rho(L_2^{(k)}) = 1 - \frac{\sigma^2_{L_1|L_2^{(k)}}}{\sigma^2_{L_0}} $$

### 2.4.22 本体论相变定理

$$ R = \frac{1}{1 + e^{-k(I - \tau)}} $$

### §X. Selection Thermodynamics: From Philosophy to Physics (选择热力学：从哲学到物理学)

#### §X.1 The Constitutional Inequality (宪法不等式)

SRT 的公理 A2 (存在即锚定) 和 A11 (本体论脆弱性) 宣称现实需要耗费能量，且存在是极其脆弱的。但宣言并非动力学。宪法不等式 (Eq-Select-Thermo) 将这些洞见升级为一个单一的、可检验的界限：**秩序增长的速率受限于选择功率预算的上限，并受到摩擦和噪声的抽头。**

考虑一个冥想者试图维持非默认的觉知状态。她必须注入选择功率 $P_{sel}$ (通过注意力引导的代谢能量) 以保持不同寻常的 $L_1$ 构型。她所付出的摩擦 $\Psi_f$ 在主观上体验为努力；环境噪声 $S_{noise}$ (令人分心的声音、侵入性思维) 会侵蚀她的建构。只有当 $\alpha P_{sel}$ 超过 $\beta \Psi_f + \gamma S_{noise}$ 时，她的经验秩序才能真正增长。当注意力稍有懈怠时——她的 $L_1$ 会向默认模式衰减，这正是该不等式所预测的热力学盆地。

#### §X.2 Computational Friction as Lower Bound (作为下界的计算摩擦)

计算本体论摩擦 (Eq-Friction-Comp) 揭示了深刻的内涵：改变现实的阻力不仅源于热力学，还源于**计算的不可约性**。当算子 $\hat{G}_\theta$ 试图从一个潜在构型 $L_0^A$ 转移到另一个 $L_0^B$ 时，它必须克服的最小摩擦受限于所需幺正变换的电路复杂度下界。

这意味着宇宙自身的“计算预算”限制了哪些现实是可达的。黑洞的霍金辐射之所以在计算上难以解码，并不是因为我们缺乏技术，而是因为 Uhlmann 变换代价代表了本体论摩擦的一个不可约下界——作为选择者的宇宙拥有最大的带宽，而黑洞使其饱和。

#### §X.3 The Protocol Layer (协议层)

$\Pi$ 的引入解决了 SRT 中一个长期存在的歧义：物理定律“居于”何处？它们既不是外部强加的，也不是任意的约定。$\Pi$ 将其形式化为**可行转移核 (feasible transition kernel)**——选择博弈中允许的移动集合。至关重要的是，$\Pi$ 本身也是一个 $L_2$ 产物：它是通过宇宙尺度的迭代被选择和固化下来的。这意味着物理规则并未超出 SRT 的范围，而是其最古老且最坚固的 $L_2$ 结构之一——所有后续选择都必须服从的协议。
