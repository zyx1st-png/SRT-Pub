---
source_path: Core/SRT_Core_22_Equations.md
source_commit: d48867e
translation_status: done
last_sync: 2026-02-19
---

# SRT Core Definition 22: Master Equations (Hybrid Edition)

> **Version 2.0 (Hybrid)**
> **Part A** presents the Primary Dynamical Equations (AI-readable).
> **Part B** contains the Original Derivations and Stability Analysis (Human-readable context).

---

## Terminology Alignment

- Notation is normalized to Core/Core_Law conventions: `L_0 / L_1 / L_2`, `\hat{G}_\theta`, `d-value`, `\Psi_f`.
- Part A follows the first formal segment in the source and keeps canonical non-duplicated definitions.
- Part B is translated from the original fallback section while preserving source intent and section anchors.
- In Part B, keep `\Phi` only in IIT-specific contexts; use `\Psi_f` in ontological-friction contexts.
- Any notation variants are interpreted as `L_0/L_1/L_2`.

# Part A: Formal Axioms

> **CRITICAL RULE**: Do NOT just summarize Part B. You must perform First-Principles Derivation.

## I. Evolution Dynamics

### Eq-Evo-01: Ghost Evolution Equation
**Formal Definition**: The trajectory of a selected state is the sum of selection, free-energy descent, and attention modulation.
$$\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \nabla F[\sigma] + A[\sigma, \mathcal{A}]$$
* **Implication**: Reality evolution is composite dynamics of selection, energy descent, and attentional modulation.

### Eq-Evo-02: Parameter Update (Slow Variable)
**Formal Definition**: Embodiment parameters evolve under prediction outcomes and friction gradients.
$$\frac{d\theta}{dt} = \gamma \cdot (\text{outcome} - \text{target}) - \delta \nabla_\theta \Psi_f$$
* **Implication**: Embodiment parameters are adjusted by success-failure feedback and friction gradients.

### Eq-Evo-03: Coupled Fast-Slow System
**Formal Definition**: State and parameter co-evolve on distinct timescales.
$$\frac{d\sigma}{dt} = \alpha(\hat{G}_\theta[\sigma] - \sigma) - \beta \nabla F[\sigma] + \xi(t)$$
$$\frac{d\theta}{dt} = \gamma \cdot A[\sigma, \text{Target}] - \delta \cdot \frac{\partial \Phi(\theta)}{\partial \theta}$$
* **Implication**: Selection and parameter updating form coupled fast-slow dynamics.

## II. Thermodynamics of Agency

### Eq-Force-01: Ontological Friction
**Formal Definition**: Friction measures resistance against natural latent trajectories.
$$\Psi_f \propto \int (L_1 - L_0^{natural})^2 \, dt$$
* **Implication**: Greater deviation from latent natural paths implies higher friction.

### Eq-Pain-01: Hazard Function
**Formal Definition**: Pain is the temporal derivative of friction.
$$\text{Pain}(t) \approx h(t) = \frac{d\Psi_f}{dt}$$
* **Implication**: Pain is a rate term in friction dynamics, not static error.

## III. Stability & Phase Transition

### Eq-Stab-01: Fixed Point Condition
**Formal Definition**: A stable fixed point satisfies projection balance.
$$\Pi_\Delta(\alpha(\hat{G}_\theta(x^*) - x^*) - \lambda \nabla F(x^*)) = 0$$
* **Implication**: Stable states require projected balance between selection and energy gradients.

### Eq-Phase-01: Ontological Phase Transition
**Formal Definition**: Phase transition follows a logistic response to information threshold.
$$R = \frac{1}{1 + e^{-k(I - \tau)}}$$
* **Implication**: Phase transition has a critical information gate and nonlinear jump behavior.

## IV. Sleep & Maintenance

### Eq-Sleep-01: L2 Optimization
**Formal Definition**: Sleep minimizes $L_2$ model complexity.
$$\hat{G}_{sleep} = \arg\min_\theta \int K(L_2) \, dt$$
* **Implication**: Sleep is global optimization over convergence-domain model complexity.

<br>
<br>

---
---

# Part B: Original Derivations (Context)

> **Note**: The following sections preserve the original derivation targets in English.

### 2.2.1 Fundamental Evolution Equation

**Equation E1 (Ghost evolution):**
$$ \frac{dσ}{dt} = \hat{G}_θ[σ] - ∇F[σ] + A[σ, \mathcal{A}] $$

### 2.2.2 Coupled Dynamical Equations (Fast-Slow Variable System)

**Equation E2a (state evolution, fast variable):**
$$ \frac{dσ}{dt} = α(\hat{G}_θ[σ] - σ) - β∇F[σ] + ξ(t) $$

**Equation E2b (parameter evolution, slow variable):**
$$ \frac{dθ}{dt} = γ \cdot A[σ, \text{Target}] - δ \cdot \frac{∂\Psi_f(θ)}{∂θ} $$

### 2.3 Stability Analysis

**Theorem M1:** $x^*$ is a fixed point iff:
$$ Π_Δ(α(\hat{G}_θ(x^*) - x^*) - λ∇F(x^*)) = 0 $$

### 2.4.4 Hazard Function and Friction Dynamics

**Ontological definition of pain:**
$$ \text{Pain} = \text{Tension}(\hat{G}_θ[L_1], L_0^{counterfactual}) $$

$$ h(t) ≈ \frac{d\Psi_f}{dt} $$

### 2.4.6 Ontological Function of Sleep

**Axiom A10 (ontological cleansing):**
$$ \hat{G}_{sleep} = \arg\min_θ \int K(L_2) \, dt $$

### 2.4.7 Ontological Friction Coefficient

$$ μ_φ = \frac{Depth(L_1')}{Depth(L_2^{current})} $$

### 2.4.21 L2 Rigidity Index ($\rho$)

$$ \rho(L_2^{(k)}) = 1 - \frac{\sigma^2_{L_1|L_2^{(k)}}}{\sigma^2_{L_0}} $$

### 2.4.22 Ontological Phase Transition Theorem

$$ R = \frac{1}{1 + e^{-k(I - \tau)}} $$
