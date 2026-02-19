---
source_path: Neuroscience/SRT_Clin_00_IIT_PCI.md
source_commit: 1469775
translation_status: in_progress
last_sync: 2026-02-19
---

# SRT Neuroscience I: Consciousness Metrics (Hybrid Edition) - English v1

> Version 2.0 (Hybrid)
> Part A formalizes IIT/PCI metrics under SRT.
> Part B provides clinical interpretation and falsifiable predictions.

---

## Terminology Alignment

- Canonical notation: `\Phi`, `d`, `\hat{G}_\theta`, `L_0/L_1/L_2`, `\Psi_f`.
- `\Phi` is treated as structural irreducibility; `d` as concern/selection depth.

# Part A: Formal Axioms

## I. IIT as Selection Capacity

### Ax-IIT-1: Irreducibility-Selection

$$
\Phi(\hat{G}_\theta)\equiv\min_{\mathrm{cut}}\Delta\mathcal{I}(\hat{G}_\theta)
$$

### Ax-IIT-2: Maximum-Phi Anchoring

$$
\sigma\in L_1\iff\sigma=\arg\max_{\sigma'}\Phi(\hat{G}_\theta[\sigma'])
$$

### Ax-IIT-3: Complementarity

$$
\Phi\cdot d > C_{\mathrm{critical}}
$$

## II. Clinical Metrics as Operator Probes

### Ax-CLIN-1: Blindsight Dissociation

$$
I(\mathrm{Input};\mathrm{Output})>0\ \land\ \hat{G}_\theta[L_1]=\varnothing
$$

### Ax-CLIN-2: PCI as Capacity Probe

$$
\mathrm{PCI}\propto\int_\Omega\mathcal{D}(\sigma)\,\mathcal{I}(\sigma)\,d\sigma
$$

### Ax-CLIN-3: L6b Resampling

$$
\hat{R}_{L6b}:L_0^{\mathrm{neural}}\to L_0^{\mathrm{neural}},\quad d(t)\uparrow
$$

## III. Theorems

### T-CLIN-1: PCI-d Coupling

$$
\Delta d>0\Rightarrow\Delta\mathrm{PCI}>0
$$

### T-CLIN-2: Non-report Theorem
Low anchoring yields intact partial processing with absent reportable foreground.

### C-CLIN-1: PCI Threshold Corollary

$$
\mathrm{PCI}<\tau_{\mathrm{clin}}\Rightarrow\hat{G}_\theta\ \mathrm{fragmented}
$$

<br>
<br>

---
---

# Part B: Expanded Context (English)

## 1. Three-way metric dilemma

The source frames consciousness metrics as a tri-constraint problem: theoretical rigor (`\Phi`), clinical practicality (PCI), and process-level validity (dynamic selection).

## 2. Main synthesis

PCI is interpreted as real-time selection-capacity proxy; IIT-like measures capture structural capacity. Neither is sufficient alone.

## 3. Clinical implications

The framework differentiates coma, UWS/VS, MCS, and covert consciousness through operator capacity and stability rather than behavior alone.

## 4. Test directions

- Task-induced `d` changes should co-modulate PCI.
- Small-system computable `\Phi` should track flexibility but not perfectly.
- Combined PCI + personalized stimulation should improve CMD detection.

## Symbol Index

| Symbol | Meaning |
|:--|:--|
| `\Phi` | irreducibility/structure metric |
| `\mathrm{PCI}` | perturbational complexity index |
| `\hat{R}_{L6b}` | layer-6b resampling operator |

