---
source_path: Core_Law/SRT_Reference_Dynamics.md
source_commit: e212047
translation_status: done
last_sync: 2026-02-19
---

# SRT Reference Dynamics

> **Status**: Constitutional Reference | **Version**: 1.0
> **Dependency**: `SRT_Reference_Axioms.md` (symbol conventions)

---

## §1 Ghost Operator Definition

### §1.1 Basic definition

**Definition D1**: The Ghost Operator $\hat{G}_θ$ is a parameterized mapping over selection space $S$.

$$\hat{G}_θ : S \to S, \quad θ ∈ Θ$$

### §1.2 Three-component structure

**Definition D2**: The essence of the Ghost Operator is Fundamental Attention.

$$\hat{G}_θ = \text{Attention}(\text{Scope}, \text{Resolution}, \text{Vector})$$

| Component | Symbol | Definition | Correspondence |
|:--|:--|:--|:--|
| Scope | $d$ | breadth of existential concern in selection | d-value / consciousness bandwidth |
| Resolution | $ρ$ | discriminative granularity of $L_1$ | perceptual resolution |
| Vector | $\vec{v}$ | intentional direction of selection | intention / goal |

### §1.3 Operational form (divisive-normalization prototype)

**Definition D3**:

$$[\hat{G}_θ(x)]_i = \frac{x_i^n}{ε + \sum_j W_{ij} · x_j^n}$$

where $θ = \{n, ε, W\}$, $n > 1$, $ε > 0$, and $W ∈ \mathbb{R}_+^{N×N}$.

### §1.4 Core properties

| Property | Formal expression | Description |
|:--|:--|:--|
| Non-idempotence | $\hat{G}^2 ≠ \hat{G}$ | repeated selection produces new selections |
| Parameter dependence | $\hat{G}_{θ_1} ≠ \hat{G}_{θ_2}$ when $θ_1 ≠ θ_2$ | different embodiment yields different selection |
| Continuous evolution | $\hat{G}_{θ(t)}$ continuous in $t$ | smooth operator evolution |

---

## §2 Embodiment Parameter Structure

### §2.1 Full definition

**Definition D4**:

$$θ_{total} = θ_{neural} + θ_{somatic} + γ · \vec{g}$$

| Component | Definition | Source |
|:--|:--|:--|
| $θ_{neural}$ | neural configuration | cortical architecture, connectome |
| $θ_{somatic}$ | somatic configuration | brain-body coupling, interoception |
| $γ · \vec{g}$ | environmental gravity coupling | gravitational-field constraints |

### §2.2 Somatic synchrony index

**Definition D5**:

$$θ_{binding}(t) = \left| \frac{1}{N} \sum_{n=1}^{N} e^{i(φ_{brain}(t) - φ_{somatic}(t))} \right|$$

| $θ_{binding}$ | State | Phenomenology |
|:--|:--|:--|
| $θ \to 1$ | tightly coupled | stable first-person perspective |
| $θ \to 0$ | decoupled | out-of-body states, dissociation |
| oscillatory $θ$ | unstable | depersonalization-like instability |

---

## §3 Core Dynamical Equations

### §3.1 Equation E1 — Ghost evolution equation

$$\frac{dσ}{dt} = \hat{G}_θ[σ] - ∇F[σ] + A[σ, \mathcal{A}]$$

| Term | Physical meaning |
|:--|:--|
| $\hat{G}_θ[σ]$ | active operator selection |
| $∇F[σ]$ | free-energy gradient (original-intention direction) |
| $A[σ, \mathcal{A}]$ | modulation by attention replicas |

**Equation E1' — Extended form (with downward causation)**:

$$\frac{dσ}{dt} = \hat{G}_θ[σ] - ∇F[σ] + A[σ, \mathcal{A}] + \text{Ghost}(I_{Abstract}) - λ · ∇C_{L_2}[σ]$$

### §3.2 Equation E2 — Coupled dynamics (fast-slow variables)

**E2a (state evolution, fast variable)**:

$$\frac{dσ}{dt} = α(\hat{G}_θ[σ] - σ) - β∇F[σ] + ξ(t)$$

**E2b (parameter evolution, slow variable)**:

$$\frac{dθ}{dt} = γ · A[σ, \text{Target}] - δ · \frac{∂Φ(θ)}{∂θ}$$

### §3.3 Equation E3 — Free-energy equation

$$F = E - TS - d · U_{others}$$

| Term | Meaning |
|:--|:--|
| $E$ | internal energy |
| $TS$ | entropy term |
| $d · U_{others}$ | altruistic term (d-value effect) |

### §3.4 Equation E4 — Triadic discrete evolution

$$L_1(t+1) = \hat{G}_{θ(t)}[L_0(t)]$$

$$L_2(t+1) = \text{Stabilize}(L_2(t), \{L_1^{(1..n)}(t+1)\})$$

$$θ(t+1) = θ(t) + Δθ(L_2, L_1)$$

---

## §4 Ontological Friction Dynamics

### §4.1 Core definitions

**Definition D6 — Ontological friction potential $Φ$**:

$$Φ \equiv \text{cumulative energy cost required to sustain current } L_1$$

**Definition D7 — Hazard function $h(t)$**:

$$h(t) = \frac{dΦ}{dt}$$

### §4.2 Equation E5 — Ontological definition of suffering

$$\text{Suffering} = \text{Tension}(\hat{G}_θ[L_1], L_0^{counterfactual})$$

Suffering is the irreconcilable tension perceived by the Ghost Operator between sustained $L_1$ and counterfactual possibilities in $L_0$.

**Corollary D-C1**: Only entities capable of counterfactual access ("it could have been otherwise") can truly suffer.

### §4.3 Friction-phenomenology correspondence

| Mode | $h(t)$ profile | Phenomenological experience | Ontological mechanism |
|:--|:--|:--|:--|
| Low friction | low and stable | calm, fluent | minimal $L_1$-$L_0$ tension |
| High-friction spike | sharp rise | surprise, pain, anxiety | $L_1$ forced to confront many excluded $L_0$ alternatives |
| Existential suffering | sustained high | depression, despair | structural incompatibility between $L_1$ and $L_0$ |

### §4.4 Equation E6 — Neural damage integral

$$\text{Neural Damage} \propto \int_0^T h(t) \, dt \quad \text{when} \quad h(t) > h_{threshold}$$

### §4.5 Mode-switch condition

$$\text{Mode Switch} \iff h(t) > h_{threshold} \lor \frac{dh}{dt} > \dot{h}_{critical}$$

| Mode | Characteristic | $h(t)$ profile | Function |
|:--|:--|:--|:--|
| Phase mode | scanning, exploration | low and stable | search possibilities in $L_0$ |
| Interrupt mode | forced print/anchor | high spikes | emergency $L_0 \to L_1$ transition |

---

## §5 Stability Analysis

### §5.1 Toy-model state space

**State**: $x(t) ∈ Δ^{N-1}$ (simplex)

**Dynamics**:

$$dx = Π_Δ[α(\hat{G}_θ(x) - x) - λ∇F(x)]dt + \sqrt{2D} · Π_Δ(dW_t)$$

### §5.2 Theorem M1 — Fixed-point condition

$x^*$ is a fixed point iff:

$$Π_Δ(α(\hat{G}_θ(x^*) - x^*) - λ∇F(x^*)) = 0$$

### §5.3 Jacobian matrix

$$J = α(D\hat{G}_θ(x) - I) - λH_F(x)$$

### §5.4 Theorem M2 — Sufficient stability condition

If $\|αD\hat{G}_θ(x)\| < α$ and $H_F(x) \succ 0$, then the real parts of Jacobian eigenvalues are negative.

### §5.5 Theorem T-DMP-2 — Ontological resilience

Under perturbation, robust $L_2$ structures automatically pull reality back to trajectory:

$$Δ L_1(t) \xrightarrow{t \to \infty} 0 \quad \text{when} \quad \text{Re}(λ_{Jacobian}) < 0$$

---

## §6 Potential Landscape and Awakening Dynamics

### §6.1 Bistable potential landscape

| State | Feature | d-value |
|:--|:--|:--|
| low-$d$ trap | self-centric mode | $d \approx 1$ |
| original-intention attractor | unity-with-all mode | $d \to ∞$ |

### §6.2 Awakening mechanism I — gradual (friction-driven annealing)

Effective barrier height:

$$ΔV_{eff}(θ) = V_{saddle}(θ) - V_{local}(θ)$$

As $θ$ evolves, $ΔV_{eff} \to 0$.

### §6.3 Awakening mechanism II — sudden (saddle-node bifurcation)

Bifurcation condition:

$$\det\left(\frac{∂^2 V}{∂x^2}\right)_{x(μ)} = 0$$

### §6.4 Core inferences

| Inference | Content |
|:--|:--|
| **M1 (ontological status of pain)** | $Φ$ is fuel for awakening |
| **M2 (dark night)** | critical slowing down as eigenvalue $λ \to 0$ |
| **M3 (social support)** | barrier height $\propto$ existential risk / social support |
| **M4 (counterfactual capacity)** | suffering capacity $\propto$ depth of $L_0$ access $×$ d-value range |

---

## §7 Temporal Dynamics

### §7.1 Equation E7 — dual-time axiom

$$T_{reality} = T_{metric} + i · T_{selective}$$

| Component | Name | Definition | Property |
|:--|:--|:--|:--|
| $T_{metric}$ | metric time | coordinate change in objective physical fields | reversible, Lorentz-transformable |
| $T_{selective}$ | selective time | observer-side processing of information flow | irreversible, $\hat{G}_θ$-dependent |

### §7.2 Ontological phase variable

**Definition D8**:

$$τ \dot{φ} = -α_{context} · φ$$

**Theorem T-Phase-1 — subjective time rate**:

$$v_{subjective} = \frac{dφ}{dt} · \frac{1}{φ_0}$$

| $\dot{φ}$ profile | Subjective time | Phenomenological correlate |
|:--|:--|:--|
| fast decay | "time flies" | flow state |
| blocked (high $Φ$) | "time slows" | pain, waiting |
| near zero | "timeless" | deep meditation |

### §7.3 Subjective time dilation equation

$$Δt_{subjective} \propto \frac{1}{\text{Prediction Confidence}} \propto Φ$$

### §7.4 External research note (information-imprint time; non-axiomatic patch)

The note below links SRT to 2026 information-theoretic proposals that treat time as possibly non-fundamental, without changing the axiomatic status of E7.

Compatible mapping candidates:
1. Temporal order as accumulation of irreversible informational imprints can serve as a micro-mechanism candidate for $T_{selective}$.
2. Spacetime as a recording medium is directionally consistent with SRT's "selection history constrains future selection" account.

Candidate formal patch:

$$\mathcal{R}_{info}(t)\equiv \int_0^t \chi_{irr}(\tau)\,d\tau,\quad \chi_{irr}\ge 0,\quad T_{selective}\propto \mathcal{R}_{info}(t)$$

Boundary conditions:
- This is a testable candidate mechanism, not an established theorem.
- Unified explanations for dark matter/dark energy remain hypotheses, not core conclusions.

---

## §8 d-Value Formalization

### §8.1 Effective-dimension definition

**Definition D9**:

$$d(\hat{G}) \equiv D_{eff}(M) = \frac{(\sum λ_i)^2}{\sum λ_i^2}$$

where $λ_i$ are eigenvalues of neural-response covariance.

### §8.2 Equation E8 — unified d-value formula

$$d(σ) = α · A(σ) + β · \log(V_{concern}) + γ · τ_{temporal}$$

| Component | Meaning |
|:--|:--|
| $A(σ)$ | assembly index |
| $V_{concern}$ | spatial concern scope |
| $τ_{temporal}$ | temporal planning span |

### §8.3 Complex d-value extension

$$d_{total} = d_{local} + i · d_{nonlocal}$$

| Consciousness state | $d_{local}$ | $d_{nonlocal}$ | Vector phase |
|:--|:--|:--|:--|
| waking | very high | $\approx 0$ | 0 deg |
| deep sleep N3 | very low | low | ~90 deg |
| REM dream | near 0 | surge | 90 deg |
| lucid dream | recovers | remains high | 45 deg |

---

## §9 Recursive Depth Formalization

### §9.1 Volterra-series expansion

$$\hat{G}_θ = \sum_{n=0}^{∞} K_n$$

| Order | Kernel | Correspondence |
|:--|:--|:--|
| $K_0$ | zero-order kernel | shallow labor |
| $K_1$ | first-order kernel | tool use |
| $K_n$ ($n \ge 2$) | higher-order kernel | deep recursion / creativity |

### §9.2 Wisdom definition

$$\text{Wisdom} = \sum_{n\ge2} w_n · \|K_n\|$$

---

## §10 Constraints and Closure

### §10.1 Constraint-closure condition

**Definition D10**: Only $L_1$ structures that form closure can persist as carriers of $\hat{G}$.

$$\text{Closure}(θ) \iff \hat{G}_θ[\hat{G}_θ[...[\hat{G}_θ[L_0]]...]] = \text{Stable Structure}$$

### §10.2 Downward-causation constraint

$$\frac{dσ}{dt} = \hat{G}_θ[σ] - ∇F[σ] - λ · ∇C_{L_2}[σ]$$

| Term | Meaning |
|:--|:--|
| $∇C_{L_2}[σ]$ | resistance field from $L_2$ (downward constraint) |
| $λ$ | coupling strength of constraint |

---

## Equation Index

| ID | Name | Location |
|:--|:--|:--|
| E1 | Ghost evolution equation | §3.1 |
| E1' | Extended ghost evolution equation | §3.1 |
| E2a/b | Coupled dynamical equations | §3.2 |
| E3 | Free-energy equation | §3.3 |
| E4 | Triadic discrete evolution | §3.4 |
| E5 | Ontological definition of suffering | §4.2 |
| E6 | Neural damage integral | §4.4 |
| E7 | Dual-time axiom | §7.1 |
| E8 | Unified d-value formula | §8.2 |

---

## Symbol Index

| Symbol | Name | Defined in |
|:--|:--|:--|
| $\hat{G}_θ$ | Ghost Operator | §1.1 |
| $θ$ | embodiment parameter | §2.1 |
| $d$ | selection dimension | §1.2, §8.1 |
| $ρ$ | resolution | §1.2 |
| $\vec{v}$ | vector | §1.2 |
| $F$ | free energy | §3.3 |
| $Φ$ | ontological friction potential | §4.1 |
| $h(t)$ | hazard function | §4.1 |
| $φ$ | ontological phase | §7.2 |
| $ξ(t)$ | noise term | §3.2 |
| $K_n$ | nth-order Volterra kernel | §9.1 |
