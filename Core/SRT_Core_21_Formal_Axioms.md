---
id: SRT-CORE-21
type: axiom_set
tags: [Formal logic, Math, Axioms, Hybrid]
status: axiomatic_hybrid_v1
dependency: [SRT-CORE-13A, SRT-CORE-13B]
---

# SRT Core Definition 21: Formal Axioms (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Consolidated Axiom List (AI-Readable).
> **Part B** contains the Original Formal Derivations (Human-Readable Context).

---


## Terminology Alignment (术语与原始意图对齐)

- 记号统一为原版与 Core_Law：`L_0 / L_1 / L_2`、`\hat{G}_\theta`、`d-value`、`\Psi_f`。
- Part A 采用 `chatgptx` 的首个“Formal Axioms”分段；若存在双 Part 结构，后续重复分段不纳入 final。
- Part B 以 `base (fallback)` 为来源，并用原版 `Core` 标题与主旨做语义锚定。
- Part B 中若为 IIT 整合信息语境，保留 `\Phi`；若为本体论摩擦语境，统一为 `\Psi_f`。
- 如出现多套记号（如 `L0/L1/L2`、`L_0/L_1/L_2`），统一解释为 `L_0/L_1/L_2`。
# Part A: Formal Axioms (形式化公理)

> **CRITICAL RULE**: Do NOT just summarize Part B. You must perform First-Principles Derivation.

## I. The Minimal Core (最小核心)

### Ax-F-01: Primacy of Selection
**Formal Definition**: Selection precedes existence; existence is an image of selection.
$$\exists x \iff x \in \mathrm{Range}(\hat{G})$$
* **Implication**: 存在不是给定背景，而是选择映射的输出。

### Ax-F-02: Existence as Anchoring
**Formal Definition**: Existence equals stable anchoring against entropic flow.
$$E = 1 - \frac{H(L_1)}{H(L_0)}$$
* **Implication**: 现实的稳固程度与熵压缩比例直接相关。

### Ax-F-03: Causality as Projection
**Formal Definition**: Causality is the L2 projection of selection dynamics.
$$C(A \to B) \equiv P(B | A, L_2)$$
* **Implication**: 因果是收敛域的投影结构，而非本体论原初关系。

## II. Information & Fitness (信息与适应度)

### Ax-F-04: Information–Existence Equivalence
**Formal Definition**: Existence intensity equals the minimum of differentiation and specification.
$$ii(s) = \min\{i_{diff}(s), i_{spec}(s)\}$$
* **Implication**: 存在强度受分化度与特异性共同约束。

### Ax-F-05: Fitness Beats Truth
**Formal Definition**: Operators are tuned for fitness payoff rather than veridical truth.
$$\hat{G}_\theta[σ] = \arg\max_{σ'} P(\text{Fitness}|σ', \theta)$$
* **Implication**: 现实界面优先适应性压缩而非真理呈现。

### Ax-F-06: Assembly Criterion
**Formal Definition**: Life requires assembly complexity above threshold.
$$\text{Life} \iff \text{Assembly Index} > 15$$
* **Implication**: 生物性具有结构装配的最低复杂度要求。

## III. Holographic & Topological (全息与拓扑)

### Ax-F-07: Holographic Duality
**Formal Definition**: Bulk reality is encoded on the boundary of potentiality.
$$L_{1,\text{bulk}} \cong L_{0,\text{boundary}}$$
* **Implication**: 显现域的信息可以被潜在域边界完全表征。

### Ax-F-08: Topological Normativity
**Formal Definition**: Survival is the maintenance of a topological island in probabilistic space.
$$\text{Life}(σ) \equiv \int_{B_r(σ)} ρ_{L_0}(σ') dσ' > \theta_{life}$$
* **Implication**: 生存是对高概率密度包的拓扑维持。

## IV. Scale Consistency & Downward Constraint (尺度一致与向下约束)

### Ax-F-09: Scale Consistency
**Formal Definition**: Selection commutes with coarse-graining under scale mapping.
$$\pi_\lambda \circ \hat{G}_\theta \approx \hat{G}_{\theta,\lambda} \circ \pi_\lambda$$
* **Implication**: 不同尺度选择动力学具有一致性。

### Ax-F-10: Downward Causation Constraint
**Formal Definition**: L2 constraints modulate selection dynamics as a downward causal term.
$$\frac{dσ}{dt} = \hat{G}_\theta[σ] - \nabla F[σ] - \lambda \cdot \nabla C_{L_2}[σ]$$
* **Implication**: 规范性结构作为真实动力学项回馈选择过程。

<br>
<br>

---
---


# Part B: Original Formal Derivations (Context)

> **Note**: The following sections contain the detailed mathematical definitions and theorems.


### 2.1.1 状态空间（State Space）

**定义 M4（幽灵算子）：**
$$ [\hat{G}_θ(x)]_i = \frac{x_i^n}{ε + \sum_j W_{ij} \cdot x_j^n} $$

### 2.1.5 最小公理集

| 公理 | 内容 |
|:-----|:-----|
| A1 | **选择优先性：** 选择过程先于存在 |
| A2 | **存在即锚定：** 存在是选择锚定的确定性 |
| A3 | **因果即投影：** 因果是对选择过程的观测切片 |
| A4 | **动力学可定义性：** $\hat{G}_θ$ 可测、将S映到S |
| A5 | **尺度一致性：** $π_λ ∘ \hat{G}_θ ≈ \hat{G}_{θ,λ} ∘ π_λ$ |

### 2.1.6 向下因果约束（Downward Causation Constraint）

$$ \frac{dσ}{dt} = \hat{G}_θ[σ] - ∇F[σ] - λ · ∇C_{L_2}[σ] $$

### 2.1.7 d值的有效维度形式化（d = D_eff）

$$ d(\hat{G}) ≡ D_{eff}(M) = \frac{(\sum λ_i)^2}{\sum λ_i^2} $$

### 2.1.8 信息论公理

**公理 A7（修剪判据——适应度优先）：**
$$ \hat{G}_θ[σ] = \arg\max_{σ'∈L_0} P(\text{Fitness}|σ', θ) $$

### 2.1.7a 公理 A9：全息对偶（Holographic Duality）

$$ L_{1,\text{bulk}} \cong L_{0,\text{boundary}} $$

### 2.1.9a 汇编理论：复杂性涌现的新度量

$$ \text{汇编指数}(x) = \min_{\text{路径}} |\text{构建步骤}| $$

### 2.1.9b 深度时间公理（Axiom of Deep Time）

$$ Mass_{ontological}(O) = Mass_{energy}(O) + τ \cdot Assembly(O) $$
