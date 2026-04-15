---
source_path: Physics/SRT_Quant_01_Selection.md
source_commit: f708b2e
translation_status: in_progress
last_sync: 2026-02-19
---

# SRT Quantum Mechanics: Selection and Measurement (Hybrid Edition) - English v1

> Version 2.0 (Hybrid)
> Part A gives formal operator-level definitions and theorems.
> Part B provides mechanism-level interpretation and criticism response.

---

## Terminology Alignment

- Canonical notation: `L_0/L_1/L_2`, `\hat{G}_\theta`, `d-value`, `\Psi_f`.
- This module extends `SRT_Quant_00_Intro` with deeper formal measurement mechanics.

# Part A: Formal Selection Axioms

## I. Operator Formalization

### Def-Sel-1: Quantum Selection Operator

$$
\hat{G}_\theta:\mathcal{H}\to\mathcal{P}(\mathcal{H}),\quad
|\Psi\rangle\mapsto\hat{\Pi}_k|\Psi\rangle
$$

with parameter bundle `\theta={\theta_{basis},\theta_{cut},\theta_{H_{int}}}`.

Instrument form:

$$
p_k=\mathrm{Tr}(M_k\rho M_k^{\dagger}),\quad
\rho_k=\frac{M_k\rho M_k^{\dagger}}{p_k}
$$

and path-evaluation linkage:

$$
p_k=\int_{R_k}\Omega_{L_0},\quad
\rho_k\equiv\oint_{\gamma\in R_k}\omega_{L_0}
$$

### Def-Sel-2: Measurement Event Criterion

$$
\mathrm{Measurement}\iff
\begin{cases}
\Delta S_{\mathrm{entanglement}}>0\\
\Delta I_{\mathrm{classical}}>0\\
\tau_{\mathrm{decoherence}}<\tau_{\mathrm{readout}}
\end{cases}
$$

### Def-Sel-3: Proxy Observer
A proxy observer is any physical system satisfying Def-Sel-2; no consciousness premise is required.

## II. Core Theorems

### T-Sel-1: Objective Measurement Theorem

$$
\tau_{\mathrm{decoherence}}<\tau_{\mathrm{readout}}
\Rightarrow
S\ \mathrm{acts\ as}\ \hat{G}_{\mathrm{proxy}}
$$

### T-Sel-2: Bit Generation Theorem

$$
\mathrm{RealityContent}(\Omega)=\int_{t_0}^{t}H(\hat{G}_\theta[\Psi])\,dt
$$

### T-Sel-3: Probabilistic Bias Theorem

$$
P_{\mathrm{obs}}(x)=P_{\mathrm{Born}}(x)+\delta_\theta(x,d),\quad
\int\delta_\theta\,dx=0
$$

### T-Sel-4: Entanglement Unity Theorem

$$
\mathrm{Entanglement}(A,B)
\iff
\hat{G}_\theta\ \mathrm{fails\ to\ factorize}\ L_0(A\cup B)
$$

### T-Sel-5: Macroscopic Suppression Theorem

$$
\mathrm{Influence}_\theta\propto e^{-N/N_{\mathrm{coherence}}}
$$

### T-Sel-6: Bias Energy Cost Theorem

$$
W_{\mathrm{bias}}\ge k_B T\,D_{KL}(P_{\mathrm{Born}}+\delta\,\|\,P_{\mathrm{Born}})
$$

## III. Temporal Quantization

### Def-Sel-4: Planck Consciousness Time

$$
t_\Psi\approx\frac{1}{\nu_{\mathrm{neural}}}\approx 10^{-1}\sim10^{-2}\,\mathrm{s}
$$

### T-Sel-7: Sub-Threshold Inaccessibility

$$
\Delta t<t_\Psi\Rightarrow\mathrm{Event}\in L_0
$$

Corollary (time averaging):

$$
L_1^{\mathrm{observed}}=\frac{1}{t_\Psi}\int_0^{t_\Psi}L_0(t)\,dt
$$

## IV. Interpretation and Geometry

### T-Sel-8: QBism-RQM Unification
Born-like statistics are treated as adaptive strategy constraints under observer-parameterized projection.

### Ax-Sel-1: Contextuality as Ontology

$$
\theta_A\ne\theta_B\Rightarrow\mathrm{Ontology}(A)\ne\mathrm{Ontology}(B)
$$

### Ax-Sel-2: Dynamic Heisenberg Cut

$$
\mathrm{CutPosition}=f(d_{\mathrm{observer}},F_{\mathrm{minimization}})
$$

### Def-Sel-5: Configuration Space as L0 Realization

$$
L_0^{\mathrm{quantum}}\cong\mathbb{R}^{3N},\quad
\hat{G}_\theta:\mathbb{R}^{3N}\to\mathbb{R}^3
$$

### T-Sel-9: Dimensional Projection Theorem
Observed locality is a low-dimensional projection effect.

### T-Sel-10: Fact Relativity Theorem

$$
\mathrm{ObjectiveReality}=\bigcap_{\theta\in\mathrm{Observers}}L_1^{\theta}
$$

<br>
<br>

---
---

# Part B: Expanded Context (English)

## 1. Mechanism: measurement as L0 to L1 conversion

This module operationalizes measurement as a constrained transformation, replacing observer-vague phrasing with measurable inequalities.

## 2. Response to mind-over-matter criticism

SRT does not claim free energy creation. It claims bounded probability-flow bias under conservation constraints, with rapidly shrinking effect at macroscopic `N`.

## 3. Interpretation synthesis

- QBism contributes observer-parameter dependence.
- RQM contributes relation-relative facts.
- Decoherence contributes environment stabilization.
- SRT adds unified ontological mapping with explicit transition criteria.

## 4. Configuration-space perspective

What appears as nonlocal correlation in `L_1` is treated as projection from a shared high-dimensional latent structure.

## 5. Experimental directions

- High-coherence systems should be more sensitive to bounded bias terms.
- Context changes should alter outcome profiles through parameter shifts.
- Temporal sampling limits should constrain direct access to fast latent dynamics.

## Symbol Index

| Symbol | Meaning |
|:--|:--|
| `\delta_\theta` | bounded intentional bias term |
| `t_\Psi` | subjective/operational temporal sampling threshold |
| `D_{KL}` | distribution-deviation cost term |
| `N_{\mathrm{coherence}}` | coherence-scale constant |

