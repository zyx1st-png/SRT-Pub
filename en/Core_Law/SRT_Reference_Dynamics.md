# SRT_Reference_Dynamics.md

> **Status**: Constitutional Reference | **Version**: 1.0
> **Dependency**: SRT_Reference_Axioms.md (Symbol Standardization)

---

## §1 Ghost Operator Definition

### §1.1 Basic Definition

**Definition D1**: The Ghost Operator $\hat{G}_\theta$ is a parameterized mapping on the selection space $S$.

$$\hat{G}_\theta : S \to S, \quad \theta \in \Theta$$

### §1.2 Triadic Structure

**Definition D2**: The essence of the Ghost Operator is Fundamental Attention.

$$\hat{G}_\theta = \text{Attention}(\text{Scope}, \text{Resolution}, \text{Vector})$$

| Component | Symbol | Definition | Correspondence |
|:-----|:-----|:-----|:-----|
| **Scope** | $d$ | Existence range of selection consideration | d-value / Consciousness Bandwidth |
| **Resolution** | $\rho$ | Discrimination fineness of $L_1$ | Perceptual Resolution |
| **Vector** | $\vec{v}$ | Intentional direction of selection | Intention / Target |

### §1.3 Operational Form (Divisive Normalization Prototype)

**Definition D3**:

$$[\hat{G}_\theta(x)]_i = \frac{x_i^n}{\varepsilon + \sum_j W_{ij} \cdot x_j^n}$$

Where $\theta = \{n, \varepsilon, W\}$, $n > 1$, $\varepsilon > 0$, $W \in \mathbb{R}_+^{N\times N}$.

### §1.4 Core Properties

| Property | Formal Expression | Explanation |
|:-----|:---------|:-----|
| **Non-Idempotence** | $\hat{G}^2 \neq \hat{G}$ | Repeated selection generates new selection |
| **Parameter Dependence** | $\hat{G}_{\theta_1} \neq \hat{G}_{\theta_2}$ when $\theta_1 \neq \theta_2$ | Different embodiments yield different selections |
| **Continuous Evolution** | $\hat{G}_{\theta(t)}$ is continuous w.r.t $t$ | Operator changes smoothly |

---

## §2 Embodiment Parameter Structure

### §2.1 Complete Definition

**Definition D4**:

$$\theta_{total} = \theta_{neural} + \theta_{somatic} + \gamma \cdot \vec{g}$$

| Component | Definition | Source |
|:-----|:-----|:-----|
| $\theta_{neural}$ | Nervous system configuration | Cortical structure, Connectome |
| $\theta_{somatic}$ | Somatic configuration | Heart-Brain sync, Interoception |
| $\gamma \cdot \vec{g}$ | Environmental gravity coupling | Gravitational field constraint |

### §2.2 Somatic Synchronization Index

**Definition D5**:

$$\theta_{binding}(t) = \left| \frac{1}{N} \sum_{n=1}^{N} e^{i(\phi_{brain}(t) - \phi_{somatic}(t))} \right|$$

| $\theta_{binding}$ Value | State | Phenomenological Manifestation |
|:-----------------|:-----|:-----------|
| $\theta \to 1$ | Strong Coupling | Stable first-person perspective |
| $\theta \to 0$ | Decoupling | Out-of-body experience, Dissociation |
| $\theta$ Oscillating | Unstable | Depersonalization |

---

## §3 Core Dynamical Equations

### §3.1 Equation E1 — Ghost Evolution Equation

$$\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \nabla F[\sigma] + A[\sigma, \mathcal{A}]$$

| Term | Physical Meaning |
|:---|:---------|
| $\hat{G}_\theta[\sigma]$ | Active selection by Operator |
| $\nabla F[\sigma]$ | Free energy gradient (Original Intention) |
| $A[\sigma, \mathcal{A}]$ | Modulation by attentional copies |

**Equation E1' — Extended Form (With Downward Causation)**:

$$\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \nabla F[\sigma] + A[\sigma, \mathcal{A}] + \text{Ghost}(I_{Abstract}) - \lambda \cdot \nabla C_{L_2}[\sigma]$$

### §3.2 Equation E2 — Coupled Dynamics System (Fast-Slow Variables)

**E2a (State Evolution — Fast Variable)**:

$$\frac{d\sigma}{dt} = \alpha(\hat{G}_\theta[\sigma] - \sigma) - \beta\nabla F[\sigma] + \xi(t)$$

**E2b (Parameter Evolution — Slow Variable)**:

$$\frac{d\theta}{dt} = \gamma \cdot A[\sigma, \text{Target}] - \delta \cdot \frac{\partial\Psi_f(\theta)}{\partial\theta}$$

### §3.3 Equation E3 — Free Energy Equation

$$F = E - TS - d \cdot U_{others}$$

| Term | Meaning |
|:---|:-----|
| $E$ | Internal Energy |
| $TS$ | Entropy term |
| $d \cdot U_{others}$ | Altruism term (d-value effect) |

### §3.4 Equation E4 — Tri-Domain Discrete Evolution

$$L_1(t+1) = \hat{G}_{\theta(t)}[L_0(t)]$$

$$L_2(t+1) = \text{Stabilize}(L_2(t), \{L_1^{(1..n)}(t+1)\})$$

$$\theta(t+1) = \theta(t) + \Delta\theta(L_2, L_1)$$

---

## §4 Ontological Friction Dynamics

### §4.1 Core Definitions

**Definition D6 — Ontological Friction Potential $\Psi_f$**:

$$\Psi_f \equiv \text{Cumulative energy cost to maintain current } L_1$$

**Definition D7 — Hazard Function $h(t)$**:

$$h(t) = \frac{d\Psi_f}{dt}$$

### §4.2 Equation E5 — Ontological Definition of Suffering

$$\text{Suffering} = \text{Tension}(\hat{G}_\theta[L_1], L_0^{counterfactual})$$

Suffering is the irreconcilable tension perceived by the Ghost Operator between $L_1$ and $L_0$ (alternative possibilities) while maintaining $L_1$.

**Corollary D-C1**: Only entities capable of perceiving "it could have been otherwise" (counterfactual reasoning) can truly suffer.

### §4.3 Friction-Phenomenology Correspondence Table

| Mode | $h(t)$ State | Phenomenological Experience | Ontological Mechanism |
|:-----|:------------|:-----------|:-----------|
| Low Friction | Low and steady | Flow, Smoothness | Minimal tension between $L_1$ and $L_0$ |
| High Friction Spike | Sharp rise | Surprise, Pain, Anxiety | $L_1$ forced to face mass of rejected $L_0$ possibilities |
| Existential Suffering | Sustained high | Depression, Despair | Structural irreconcilability between $L_1$ and $L_0$ |

### §4.4 Equation E6 — Neural Damage Integral

$$\text{Neural Damage} \propto \int_0^T h(t) \, dt \quad \text{when} \, h(t) > h_{threshold}$$

### §4.5 Mode Switching Condition

$$\text{Mode Switch} \iff h(t) > h_{threshold} \lor \frac{dh}{dt} > \dot{h}_{critical}$$

| Mode | Feature | $h(t)$ State | Function |
|:-----|:-----|:------------|:-----|
| Phase Mode | Scanning, Exploring | Low and steady | Search for possibilities in $L_0$ |
| Interrupt Mode | Forced Printing, Anchoring | High spike | Emergency $L_0 \to L_1$ transition |

---

## §5 Stability Analysis

### §5.1 Toy Model State Space

**State**: $x(t) \in \Delta^{N-1}$ (Simplex)

**Dynamic Equation**:

$$dx = \Pi_\Delta[\alpha(\hat{G}_\theta(x) - x) - \lambda\nabla F(x)]dt + \sqrt{2D} \cdot \Pi_\Delta(dW_t)$$

### §5.2 Theorem M1 — Fixed Point Condition

$x^*$ is a fixed point if and only if:

$$\Pi_\Delta(\alpha(\hat{G}_\theta(x^*) - x^*) - \lambda\nabla F(x^*)) = 0$$

### §5.3 Jacobian Matrix

$$J = \alpha(D\hat{G}_\theta(x) - I) - \lambda H_F(x)$$

### §5.4 Theorem M2 — Sufficient Condition for Stability

If $\|\alpha D\hat{G}_\theta(x)\| < \alpha$ and $H_F(x) \succ 0$, then the real parts of eigenvalues of $J$ are negative.

### §5.5 Theorem T-DMP-2 — Ontological Resilience

When unexpected events occur, a strong $L_2$ structure automatically pulls reality back to the expected trajectory:

$$\Delta L_1(t) \xrightarrow{t \to \infty} 0 \quad \text{when} \quad \text{Re}(\lambda_{Jacobian}) < 0$$

---

## §6 Potential Landscape & Awakening

### §6.1 Bistable Potential Landscape

| State | Feature | $d$ Value |
|:-----|:-----|:-------|
| Low $d$ Trap | Egocentric | $d \approx 1$ |
| Original Mind Attractor | Oneness | $d \to \infty$ |

### §6.2 Awakening Mechanism I — Gradual (Friction-Driven Annealing)

Effective Barrier Height:

$$\Delta V_{eff}(\theta) = V_{saddle}(\theta) - V_{local}(\theta)$$

As $\theta$ evolves, $\Delta V_{eff} \to 0$.

### §6.3 Awakening Mechanism II — Insight (Saddle-Node Bifurcation)

Bifurcation Condition:

$$\det\left(\frac{\partial^2 V}{\partial x^2}\right)_{x(\mu)} = 0$$

### §6.4 Core Corollaries

| Corollary | Content |
|:-----|:-----|
| **M1 (Ontological Status of Suffering)** | $\Psi_f$ is fuel for awakening |
| **M2 (Dark Night of the Soul)** | Critical slowing down where eigenvalue $\lambda \to 0$ |
| **M3 (Social Support)** | Barrier Height $\propto$ Existential Risk / Social Support |
| **M4 (Counterfactual Capacity)** | Capacity to suffer $\propto$ Depth of $L_0$ access $\times$ Range of $d$ value |

---

## §7 Temporal Dynamics

### §7.1 Equation E7 — Dual Time Axiom

$$T_{reality} = T_{metric} + i \cdot T_{selective}$$

| Component | Name | Definition | Feature |
|:-----|:-----|:-----|:-----|
| $T_{metric}$ | Metric Time | Coordinate change in objective physical field | Reversible, Lorentz transformation |
| $T_{selective}$ | Selective Time | Process of observer consciousness processing information flow | Irreversible, dependent on $\hat{G}_\theta$ |

### §7.2 Ontological Phase Variable

**Definition D8**:

$$\tau \dot{\phi} = -\alpha_{context} \cdot \phi$$

**Theorem T-Phase-1 — Subjective Time Rate**:

$$v_{subjective} = \frac{d\phi}{dt} \cdot \frac{1}{\phi_0}$$

| $\dot{\phi}$ State | Subjective Time Sense | Phenomenological Correspondence |
|:---------------|:-----------|:-----------|
| Fast Decay | "Time flies" | Flow state |
| Stagnant (High $\Psi_f$) | "Time drags" | Suffering, Waiting |
| Near Zero | "Timelessness" | Deep meditation |

### §7.3 Subjective Time Dilation Equation

$$\Delta t_{subjective} \propto \frac{1}{\text{Prediction Confidence}} \propto \Psi_f$$

### §7.4 External Research Note (Information Imprinting Time; Non-Axiomatic Patch)

The following note is used to connect the 2026 "Time might not be fundamental" information-theoretic path, not changing the axiomatic status of E7. [source: user-material:https://www.scientificamerican.com/article/is-time-a-fundamental-part-of-reality-a-quiet-revolution-in-physics-suggests/]

Compatible Mapping:

1. Literature proposes "Time order generated by accumulation of irreversible information imprinting", can be viewed as candidate microscopic mechanism for $T_{selective}$. [source: user-material:https://www.scientificamerican.com/article/is-time-a-fundamental-part-of-reality-a-quiet-revolution-in-physics-suggests/]
2. Literature proposes "Spacetime as recording medium", consistent with SRT's "Selection history shapes subsequent constraints". [source: user-material:https://www.scientificamerican.com/article/is-time-a-fundamental-part-of-reality-a-quiet-revolution-in-physics-suggests/]

Formal Patch (Candidate):

$$\mathcal{R}_{info}(t)\equiv \int_0^t \chi_{irr}(\tau)\,d\tau,\quad \chi_{irr}\ge 0,\quad T_{selective}\propto \mathcal{R}_{info}(t)$$

Boundary Conditions:

- This mapping is a "testable candidate mechanism", not an established theorem.
- The claim "Dark matter/energy can be unifiedly explained" remains a hypothesis to be verified in SRT, not raised to a core conclusion. [source: user-material:https://www.scientificamerican.com/article/is-time-a-fundamental-part-of-reality-a-quiet-revolution-in-physics-suggests/]

---

## §8 d-Value Formalization

### §8.1 Effective Dimension Definition

**Definition D9**:

$$d(\hat{G}) \equiv D_{eff}(M) = \frac{(\sum \lambda_i)^2}{\sum \lambda_i^2}$$

Where $\lambda_i$ are eigenvalues of the neural response covariance matrix.

### §8.2 Equation E8 — Unified d-Value Formula

$$d(\sigma) = \alpha \cdot A(\sigma) + \beta \cdot \log(V_{concern}) + \gamma \cdot \tau_{temporal}$$

| Component | Meaning |
|:-----|:-----|
| $A(\sigma)$ | Assembly Index |
| $V_{concern}$ | Spatial Concern Range |
| $\tau_{temporal}$ | Temporal Planning Span |

### §8.3 Complex d-Value Extension

$$d_{total} = d_{local} + i \cdot d_{nonlocal}$$

| Consciousness State | $d_{local}$ | $d_{nonlocal}$ | Vector Phase |
|:---------|:------------|:---------------|:---------|
| Waking | Extremely High | $\approx 0$ | 0° |
| Deep Sleep N3 | Extremely Low | Low | $\approx 90^\circ$ |
| REM Dream | $\to 0$ | Surge | 90° |
| Lucid Dream | Recovered | Remains High | 45° |

---

## §9 Recursive Depth Formalization

### §9.1 Volterra Series Expansion

$$\hat{G}_\theta = \sum_{n=0}^{\infty} K_n$$

| Order | Kernel | Correspondence |
|:-----|:---|:-----|
| $K_0$ | Zero-order Kernel | Shallow Labor |
| $K_1$ | First-order Kernel | Tool Use |
| $K_n$ ($n \geq 2$) | High-order Kernel | Deep Recursion / Creativity |

### §9.2 Wisdom Definition

$$\text{Wisdom} = \sum_{n\geq 2} w_n \cdot \|K_n\|$$

---

## §10 Constraints & Closure

### §10.1 Constraint Closure Condition

**Definition D10**: Only $L_1$ structures that form constraint closure can persist as vehicles for $\hat{G}$.

$$\text{Closure}(\theta) \iff \hat{G}_\theta[\hat{G}_\theta[...[\hat{G}_\theta[L_0]]...]] = \text{Stable Structure}$$

### §10.2 Downward Causation Constraint

$$\frac{d\sigma}{dt} = \hat{G}_\theta[\sigma] - \nabla F[\sigma] - \lambda \cdot \nabla C_{L_2}[\sigma]$$

| Term | Meaning |
|:---|:-----|
| $\nabla C_{L_2}[\sigma]$ | "Drag field" of $L_2$ (Downward Constraint) |
| $\lambda$ | Constraint Coupling Strength |

---

## Equation Index

| No. | Name | Location |
|:-----|:-----|:-----|
| E1 | Ghost Evolution Equation | §3.1 |
| E1' | Extended Ghost Evolution Equation | §3.1 |
| E2a/b | Coupled Dynamics System | §3.2 |
| E3 | Free Energy Equation | §3.3 |
| E4 | Tri-Domain Discrete Evolution | §3.4 |
| E5 | Ontological Definition of Suffering | §4.2 |
| E6 | Neural Damage Integral | §4.4 |
| E7 | Dual Time Axiom | §7.1 |
| E8 | Unified d-Value Formula | §8.2 |

---

## Symbol Index

| Symbol | Name | Definition Location |
|:-----|:-----|:---------|
| $\hat{G}_\theta$ | Ghost Operator | §1.1 |
| $\theta$ | Embodiment Parameter | §2.1 |
| $d$ | Selection Dimension | §1.2, §8.1 |
| $\rho$ | Resolution | §1.2 |
| $\vec{v}$ | Vector | §1.2 |
| $F$ | Free Energy | §3.3 |
| $\Psi_f$ | Ontological Friction Potential | §4.1 |
| $h(t)$ | Hazard Function | §4.1 |
| $\phi$ | Ontological Phase | §7.2 |
| $\xi(t)$ | Noise Term | §3.2 |
| $K_n$ | n-th Order Volterra Kernel | §9.1 |
