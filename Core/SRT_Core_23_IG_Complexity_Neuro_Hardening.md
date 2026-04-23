---
id: SRT-CORE-23-IG-COMPLEXITY-NEURO-HARDENING
type: framework
tags: [Information Geometry, Complexity, Neural Computation, Psi_f, d-value, Ghost Operator, L0, L1, L2]
status: draft_v1
layer: L1
epistemic_layer: bridge
claim_mode: bridge
dependency: [SRT-PSIF-CANONICAL, SRT-D-VALUE-CANONICAL, SRT-CORE-21, SRT-CORE-22, SRT-FISHER-FEP-LANDSCAPE-INTERFACE]
---

# SRT Core 23: Information Geometry / Complexity / Neural-Computational Hardening

> **Purpose**: This file hardens the conceptual core of SRT by mapping `Ψ_f`, `d-value`, `Ĝ`, and `L0-L1-L2` onto three scientific interface languages: information geometry, complex systems, and neural computation.  
> **Boundary**: This is a bridge / hardening document. It does **not** add a new P0/P1 theorem. All uses of `Ψ_f` and `d-value` remain subordinate to `_SRT_PSI_F_CANONICAL.md` and `_SRT_D_VALUE_CANONICAL.md`.

---

## 0. Three Scientific Interfaces

SRT's core triad can be made more precise by assigning three scientific languages to three different tasks:

| Interface | SRT role | Primary concepts |
|---|---|---|
| **Information geometry** | Local cost, distinguishability, and update geometry at the `L0 -> L1` frontier | `Ψ_f`, `d-value`, local Fisher projection |
| **Complex systems** | Stabilization, attractor formation, hysteresis, and sedimentation from `L1 -> L2` | `L2`, path dependence, order parameters |
| **Neural computation** | Implementation-level approximation of embodied selection in biological systems | `Ĝ`, normalization, inhibition, global availability |

Compressed rule:

> **Information geometry hardens the selection frontier; complex systems harden stabilization; neural computation hardens the implementation interface.**

---

## 1. Dynamical Domain Definitions

### 1.1 `L0`: Structured Latent Possibility Space

`L0` is not nothingness. It is the structured field of candidates not yet actualized by the current operator.

A minimal representation is:

\[
L_0 := \mathcal{X}_{possible}
\]

When probabilistic modeling is available:

\[
L_0 := \{p(x\mid\theta)\}_{\theta\in\Theta}
\]

where:

- `x` denotes a candidate state, event, representation, or action;
- `θ` denotes embodied parameters, model state, context, history, and constraints;
- `Θ` is the parameter space available to the selecting system.

**Hard reading**:

> `L0` is the current system's structured latent possibility space. When it can be probabilized, it becomes a parameterized family of candidate distributions; when it can be geometrized, it forms a statistical or effective state manifold.

### 1.2 `L1`: Actualized Slice

`L1` is the selected actualization of a candidate from `L0` under `Ĝθ` and the current constraints.

\[
L_1(t) := \hat{G}_\theta[L_0](t)
\]

or, in probabilistic terms:

\[
x_t \sim \pi_\theta(x\mid L_0,L_2)
\]

**Hard reading**:

> `L1` is not an independently self-grounded object. It is the currently actualized slice produced by an embodied selection operator under historical and environmental constraint.

### 1.3 `L2`: Historical Sedimentation / Constraint Domain

`L2` is the stable constraint domain produced by repeated or overlapping `L1` actualizations.

\[
L_2(t) := \mathcal{A}_{stable}\left(\{L_1(\tau)\}_{\tau<t}\right)
\]

A complex-systems representation is:

\[
L_2(t) := \{\rho_k(t), A_k(t), B_k(t)\}_{k\in K}
\]

where:

- `ρ_k` = path-trace density / sedimented usage weight;
- `A_k` = attractor structure;
- `B_k` = basin boundary or constraint boundary;
- `K` = set of stabilized patterns, habits, norms, schemas, or institutional pathways.

**Hard reading**:

> `L2` is not merely memory or rule storage. It is the attractor landscape / order-parameter field / hysteresis structure through which past selections bias future actualizations.

---

## 2. `Ĝθ` as Selection-Normalization-Anchor Operator

### 2.1 Abstract Definition

\[
\hat{G}_\theta: L_0 \to L_1
\]

This abstract definition must be supplemented by an operational structure.

### 2.2 Candidate Activation

Each latent candidate `x_i` receives an activation value:

\[
a_i = f(x_i,\theta,L_2)
\]

where activation depends on:

- candidate content `x_i`;
- embodied parameters `θ`;
- sedimented constraints `L2`;
- current noise, goals, bodily state, and context.

### 2.3 Competitive Normalization

A minimal implementation-level proxy for `Ĝθ` is a divisive-normalization form:

\[
[\hat{G}_\theta(x)]_i
=
\frac{a_i(\theta,L_2)^n}{\sigma^n+\sum_j w_{ij}a_j(\theta,L_2)^n}
\]

where:

- `a_i` = candidate activation;
- `w_ij` = competitive / inhibitory coupling;
- `σ` = baseline damping, noise floor, or regularizer;
- `n` = gain / sharpness parameter.

### 2.4 Anchoring

The selected candidate becomes `L1` through thresholding, winner selection, sampling, or global availability:

\[
L_1 = \operatorname{Anchor}\left(\operatorname{argmax}_i[\hat{G}_\theta(x)]_i\right)
\]

or, when stochastic selection is required:

\[
L_1 \sim \pi_\theta(x_i) \propto [\hat{G}_\theta(x)]_i
\]

### 2.5 Mechanistic Reading

`Ĝθ` should be read as a structured operation with five stages:

1. **candidate activation** — latent candidates become differentially available;
2. **competition** — candidates suppress or constrain one another;
3. **normalization** — the system compresses many candidates into a usable selection distribution;
4. **thresholding / sampling** — one or a small set of candidates becomes operative;
5. **anchoring** — the selected candidate becomes a stable `L1` slice.

Boundary:

> Divisive normalization is an implementation-level proxy for `Ĝθ`, not the whole Ghost Operator. `Ĝθ` remains the abstract SRT selection operator; neural normalization is one biological realization pattern.

---

## 3. `Ψ_f` as Fisher-Induced Local Cost + Payability Burden

### 3.1 Canonical Reading

`Ψ_f` is the information-theoretic / organizational payability burden required to compress open possibility into a maintainable, actionable, and coordinable `L1` slice.

Do **not** write:

\[
\Psi_f \equiv g_F
\]

as a literal scalar-tensor identity.

### 3.2 Fisher–Rao Local Projection

When the local selection space admits a smooth statistical-manifold representation:

\[
p(x\mid\theta)
\]

Fisher–Rao metric is:

\[
g^F_{ij}(\theta)
=
\mathbb{E}_{p(x\mid\theta)}
\left[
\partial_i\log p(x\mid\theta)\,\partial_j\log p(x\mid\theta)
\right]
\]

The local KL expansion gives:

\[
D_{KL}\left(p_\theta\parallel p_{\theta+d\theta}\right)
=
\frac12 d\theta^\top g_F(\theta)d\theta
+O(\|d\theta\|^3)
\]

Therefore the local information-geometric projection of `Ψ_f` is:

\[
\boxed{
\delta\Psi_f^{geom}
=
\frac12 d\theta^\top g_F(\theta)d\theta
+O(\|d\theta\|^3)
}
\]

### 3.3 Path Functional

For a finite update path `γ`:

\[
\boxed{
\Psi_f^{geom}[\gamma]
=
\int_\gamma
\sqrt{g^F_{ij}(\theta)\dot\theta^i\dot\theta^j}\,dt
}
\]

If an energy/action-style accumulation is needed:

\[
\mathcal{E}_{\Psi}^{geom}[\gamma]
=
\frac12\int_\gamma
\dot\theta^\top g_F(\theta)\dot\theta\,dt
\]

### 3.4 Payability Gate

Geometry gives local cost; SRT additionally requires payability:

\[
\mathrm{Payable}(X,\Delta t)
\iff
\alpha P_{sel}^{X}(\Delta t)
\ge
\beta\Psi_f^{X}(\Delta t)+\gamma S_{noise}^{X}(\Delta t)
\]

Hard reading:

> Fisher geometry tells us how costly a local update is in information space. SRT asks the additional question: can the system pay that cost while preserving closure, identity continuity, and future selection capacity?

### 3.5 Projection Conditions

The Fisher projection is valid only when:

1. a meaningful parameter space `θ` or distribution family `p(x|θ)` is available;
2. the local differentiable approximation is not broken by singularity, phase transition, model redundancy, or strong nonlinearity;
3. Fisher-distinguishable directions correspond to real selection burdens rather than coordinate artifacts;
4. cross-scale comparison uses role equivalence, not unit identity.

---

## 4. `d-value` as Stake-Gated Effective Dimension

### 4.1 Canonical Risk-Gradient Reading

The canonical risk-gradient form is:

\[
d(x)=\left\|\frac{\partial\mathcal{U}}{\partial\mathcal{S}}\right\|
\]

where:

- `𝒰` = utility / viability / closure / future-selection functional;
- `𝒮` = selection space;
- `d` = sensitivity to irreversible risk in selection.

Hard reading:

> `d-value` is not mere preference, reward, or information integration. It is the degree to which selection directions are coupled to irreversible consequences for closure, identity continuity, and future selection capacity.

### 4.2 Fisher Spectrum as Capacity Proxy

Let the Fisher spectrum be:

\[
\lambda_1,\lambda_2,\ldots,\lambda_n
\]

The ordinary effective dimension proxy is:

\[
D_{eff}(g_F)
=
\frac{(\sum_i\lambda_i)^2}{\sum_i\lambda_i^2}
\]

This is a capacity proxy, not canonical `d`.

### 4.3 Stake Gate

Introduce a stake coupling for each eigendirection:

\[
s_i\in[0,1]
\]

where `s_i` measures whether direction `i` is genuinely coupled to irreversible risk, closure maintenance, or future selection capacity.

Stake-gated eigenvalues:

\[
\tilde\lambda_i=s_i\lambda_i
\]

Stake-gated effective dimension:

\[
\boxed{
d_{stake}
=
\frac{(\sum_i s_i\lambda_i)^2}{\sum_i(s_i\lambda_i)^2}
}
\]

### 4.4 Payability-Gated d

A stronger operational proxy can include payability:

\[
d_{actual}
=
D_{eff}(g_F)\cdot\chi_{stake}\cdot\chi_{payable}
\]

where:

- `D_eff(g_F)` = distinguishable direction capacity;
- `χ_stake` = whether directions are risk-bearing;
- `χ_payable` = whether the system can carry the required `Ψ_f` without collapse.

Boundary:

> High information integration does not imply high `d-value`; high Fisher rank does not imply real care; high pain does not imply high `d`. Only stake-coupled and payable dimensions count toward SRT `d-value`.

---

## 5. `L2` as Complex-Systems Stabilization

### 5.1 L2 as Attractor Landscape / Order-Parameter Field

Repeated `L1` actualizations modify the future selection landscape. A minimal path-trace model is:

\[
\dot\rho_k
=
\alpha\phi_k(L_1)-\beta\rho_k+\eta R_k
\]

where:

- `ρ_k` = path-trace density for pathway `k`;
- `φ_k(L1)` = activation of pathway `k` by current actualization;
- `β` = decay / forgetting / loosening;
- `R_k` = repetition, reinforcement, or social validation term;
- `η` = stabilization rate.

Then:

\[
L_2(t)=\{\rho_k(t),A_k(t),B_k(t)\}_{k\in K}
\]

### 5.2 L2 Feedback into Future Selection

`L2` modifies later selection by changing activation, coupling, priors, or thresholds:

\[
a_i(t+1)=f(x_i,\theta,L_2(t))
\]

\[
w_{ij}(t+1)=w_{ij}(t)+\Delta w_{ij}(L_1,L_2)
\]

Thus `L2` is not a passive record. It is a constraint field that reshapes future `Ĝθ` operations.

### 5.3 Complex-Systems Reading

| Complex-systems concept | SRT reading |
|---|---|
| Attractor | Stabilized future-selection tendency |
| Attractor basin | Range of states pulled into a similar `L1` pattern |
| Order parameter | Low-dimensional variable summarizing stabilized selection regimes |
| Hysteresis | Past selections continue to bias current selection even after inputs change |
| Metastability | Temporary but non-final stabilization of `L2` |
| Phase transition | Regime shift in available or dominant selection patterns |

Boundary:

> `L2` is thicker than any single energy landscape. A landscape is an effective projection of `L2`, not the whole convergence domain.

---

## 6. Neural-Computational Implementation Interfaces

### 6.1 Divisive Normalization as Candidate Competition

Neural computation can approximate the `Ĝθ` selection step through normalization:

\[
R_i
=
\frac{L_i^n}{\sigma^n+\sum_jw_{ij}L_j^n}
\]

SRT mapping:

| Neural computation | SRT role |
|---|---|
| Candidate activation | Latent possibility becomes locally available |
| Inhibitory pool | Competing possibilities suppress one another |
| Gain modulation | `θ` changes the selectivity and threshold of `Ĝ` |
| Normalized response | Many candidates are compressed into an actionable distribution |
| Threshold / winner | `L1` anchoring begins |

### 6.2 Global Availability as L1 Stabilization

A selected neural representation becomes robust `L1` only when it becomes usable across memory, report, planning, action, or integration systems.

SRT reading:

\[
L_1^{neural}
\approx
\text{globally available selected content}
\]

Boundary:

> Global availability is an implementation-level criterion for neural `L1`, not a universal definition of `L1` across all scales.

### 6.3 Plasticity as L2 Writeback

Neural `L2` may be approximated by:

- synaptic weights;
- habit circuits;
- predictive templates;
- emotional priors;
- categorical schemas;
- sensorimotor coordinations.

The writeback loop is:

\[
L_1^{neural}\to \Delta W \to L_2^{neural}\to \hat G_{\theta'}\to L_1'
\]

---

## 7. Minimal Closed-Loop Model

The hard core of the bridge can be summarized as:

### 7.1 Candidate Space

\[
L_0=\{p(x\mid\theta)\}
\]

### 7.2 Selection Operator

\[
\pi_\theta(x_i)
=
\frac{a_i(\theta,L_2)^n}{\sigma^n+\sum_jw_{ij}a_j(\theta,L_2)^n}
\]

\[
L_1(t)=\operatorname{Anchor}\left(\operatorname{sample/argmax}_{x_i}\pi_\theta(x_i)\right)
\]

### 7.3 Selection Friction

\[
\delta\Psi_f^{geom}
=
\frac12d\theta^\top g_F(\theta)d\theta
+O(\|d\theta\|^3)
\]

### 7.4 Stake-Gated d-value

\[
d_{stake}
=
\frac{(\sum_i s_i\lambda_i)^2}{\sum_i(s_i\lambda_i)^2}
\]

### 7.5 L2 Writeback

\[
\dot\rho_k
=
\alpha\phi_k(L_1)-\beta\rho_k+\eta R_k
\]

### 7.6 Full Loop

\[
L_0\xrightarrow{\hat G_\theta}L_1\xrightarrow{writeback}L_2\xrightarrow{constraint}\hat G_{\theta'}\xrightarrow{}L_1'
\]

Interpretation:

1. `L0 -> L1`: information geometry hardens local cost and distinguishability.
2. `L1 -> L2`: complex systems harden sedimentation and stabilization.
3. `L2 -> L1`: neural / cognitive / social constraints harden recursive selection.

---

## 8. Boundary Conditions and Non-Claims

### 8.1 Fisher Metric Boundary

Fisher metric is local and projection-dependent. It does not define the whole of `Ψ_f`.

Correct:

\[
\delta\Psi_f^{geom}=\frac12d\theta^\top g_Fd\theta+O(\|d\theta\|^3)
\]

Incorrect:

\[
\Psi_f\equiv g_F
\]

if read as a strict scalar-tensor identity.

### 8.2 Landscape Boundary

`L2` is not identical to any one landscape function. A landscape is a compressed effective projection of the broader convergence domain.

### 8.3 Neural Boundary

Divisive normalization, global availability, and plasticity are neural implementation proxies. They do not exhaust `Ĝ`, `L1`, or `L2` in non-neural domains.

### 8.4 d-value Boundary

`d-value` is not information integration alone, not preference strength alone, and not subjective importance alone. It requires stake-coupling and payability.

### 8.5 Ψ_f Boundary

`Ψ_f` is not subjective pain, generic metabolic cost, arbitrary free energy, or Fisher metric itself. Pain, energy, free energy, and Fisher geometry are domain-specific readings or proxies.

---

## 9. Short Canonical Paragraph for Reuse

> SRT can be hardened by distributing its core concepts across three scientific interfaces. Information geometry formalizes the `L0 -> L1` selection frontier: when a local statistical-manifold projection exists, `Ψ_f` has a Fisher-induced second-order cost form `δΨ_f^{geom}=1/2 dθ^T g_F dθ+O(||dθ||^3)`, while `d-value` can be approximated as a stake-gated effective dimension of the Fisher spectrum. Complex systems theory formalizes `L1 -> L2` stabilization: repeated actualizations sediment into attractor basins, order parameters, and hysteresis structures. Neural computation provides implementation-level proxies for `Ĝθ`: candidate activation, competitive inhibition, divisive normalization, thresholding, global availability, and plastic writeback. This bridge does not replace SRT's canonical definitions; it supplies modeling interfaces that make them mechanistically and empirically tractable.

---

## 10. Editing Rule

This file is for content hardening and cross-domain mechanism bridging. It does not add a P0/P1 core theorem. All `Ψ_f` and `d-value` usages must continue to route through the canonical files:

- `_SRT_PSI_F_CANONICAL.md`
- `_SRT_D_VALUE_CANONICAL.md`
- `SRT_Fisher_FEP_Landscape_Interface.md`
