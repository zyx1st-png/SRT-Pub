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

## I. Evolution Dynamics (演化动力学)

### Eq-Evo-01: Ghost Evolution Equation
**Formal Definition**: The trajectory of a selected state is the sum of selection, free-energy descent, and attention modulation.
$$\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \nabla F[\sigma] + A[\sigma, \mathcal{A}]$$
* **Implication**: 现实演化是选择、能量下降与注意调制的合成动力学。

### Eq-Evo-02: Parameter Update (Slow Variable)
**Formal Definition**: Embodiment parameters evolve under prediction outcomes and friction gradients.
$$\frac{d\theta}{dt} = \gamma \cdot (\text{outcome} - \text{target}) - \delta \nabla_\theta \Psi_f$$
* **Implication**: 具身参数在成功-失败反馈与摩擦梯度之间调整。

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
