---
id: SRT-SYMBOL-TABLE
type: definition
tags: [Symbols, Registry, Canonical]
status: axiomatic_hybrid_v1
layer: meta
epistemic_layer: os
claim_mode: canonical
dependency:
  - SRT-REF-AXIOMS
  - SRT-REF-DYNAMICS
  - SRT-D-VALUE-CANONICAL
  - SRT-PSIF-CANONICAL
  - SRT-SUFFERING
  - SRT-GLOSSARY-STRUCTURAL-GOVERNANCE-TERMS
  - SRT-ANNEX-REGISTRY
  - SRT-OPS-CLOSURE-INDEX-2026-04-29
---

# SRT Symbol Table & Definition Registry

> **Purpose**: Canonical symbol registry for cross-domain writing and AI parsing.
>
> **Governance boundary**: Terms such as `interface_annex`, `copy-to-annex`, `owner-bound`, `claim_mode`, and `canonical:false` are structural governance vocabulary (see `SRT_Glossary_Structural_Governance_Terms.md`); they are not canonical mathematical symbols and do not appear in this table's symbol rows. Non-canonical annexes and Operations records may reference symbols defined here but must not redefine them.
> **Proxy boundary**: This table records canonical symbol usage plus governed projections. It does not license domain formulas to redefine `d`, `Ψ_f`, suffering/pain, Fisher, Landauer, or AI consciousness; use `_SRT_D_VALUE_CANONICAL.md`, `_SRT_PSI_F_CANONICAL.md`, `Core_Law/SRT_Suffering.md`, and the relevant claim-status file when a row points to a proxy.

| Symbol | LaTeX | Name | Atomic Definition | Dimensions/Units | Scope / Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **L₀** | `L_0` | Latent Domain | Set of all unselected possibilities (structured potentiality, not nothingness). | Thin: structural potentiality space (measure/cardinality unfixed at core level) | Core, universal. **Domain projection**: the `∞-dim Hilbert space` reading is a physics / statistics bridge realization, **not** the universal atomic definition — see `Physics/_SRT_Phys_Bridge.md`, `Physics/SRT_Quant_00_Intro.md`; thin structural home `Core_Law/SRT_L0_Metaphysics.md`. |
| **L₁** | `L_1` | Manifest Domain | Selected slice of reality produced by operator dynamics. | Thin: manifest reality slice (domain-dependent realization) | Core, universal. **Domain projection**: the `4D spacetime + qualia` reading is a physics (spacetime) + phenomenology (qualia) bridge realization, **not** the universal atomic definition — see `Core/SRT_Core_12a_Ontology_L0L1.md` (spacetime emergence), `Philosophy/SRT_HardProblem_Epistemology.md` (qualia); thin structural home `Core_Law/SRT_L0_Metaphysics.md`. |
| **L₂** | `L_2` | Convergence Domain | Stable consensus constraints from repeated/overlapping selections. | Topological manifold | Core, universal |
| **Ĝ** | `\hat{G}` | Ghost Operator | Selection operator mapping $L_0 \to L_1$. | Operator | Never use plain `G` for this |
| **θ** | `\theta` | Embodiment Parameters | Finite configuration parameters of $\hat{G}$ (biology/model state/context). | Tensor / parameter set | Core, universal |
| **d** | `d` | d-value (Depth of Care) | Governance-canonical default is a scalar summary of stake-coupled concern / irreversible-risk sensitivity; geometric, Fisher, vector, and gate readings require explicit marking. | Scalar summary by default; proxies are projections | Core, universal; canonical source `_SRT_D_VALUE_CANONICAL.md`; `Def-d-canonical` is the core-facing anchor, while scalar default / vector / gate rules are governance-canonical usage controls; do not mix scalar `d`, `D_eff`, Fisher proxy, `d-vector`, and `d-gate` in one claim without notation |
| **Ψf** | `\Psi_f` | Ontological Friction | Ontological impedance / information-theoretic payability burden required to compress open possibility into a maintainable reality slice. | Cross-scale readout; units vary by domain | Core, universal; canonical source `_SRT_PSI_F_CANONICAL.md`; v1 governance-canonical main reading is information-theoretic/payability cost; Fisher geometry may induce local second-order proxy `δΨ_f^{geom}=1/2 dθ^T g_F dθ+O(||dθ||^3)` and path functionals, but `Ψ_f ≡ g_F` is never a literal scalar-tensor identity; metabolic readings are budget/load projections only under stated conditions; domain projections do not become theory-canonical by reuse |
| **T_dir** | `T_{dir}` | Direction Transparency | v0 operational proxy / constrained readability-reorientation functional for a system's own current selection direction. | Proxy / accessibility index | Governance-canonical working proxy `_SRT_T_DIR_CANONICAL.md`; not a completed ontological foundation and not semantic valence, reward, coherence, or confidence |
| **Ω** | `\Omega` | Ontological Consistency | Internal coherence of an $L_1/L_2$ structure. | Probability (0-1) | Canonical `\Omega` in Core_Law context |
| **Ω_mis** | `\Omega_{\text{mis}}` | Ontological Mismatch Index | Distance between inherited $\theta$ and current-environment optimal $\theta$. | Scalar | Legacy docs may call this `Ω` |
| **ω_sub** | `\omega_{sub}` | Subjective Frequency | Refresh rate of selection cycles. | Hz | Neuro/phenomenology |
| **η** | `\eta` | Operator Viscosity | Transition resistance of $\hat{G}$ states. | Scalar ($0 \to \infty$) | Low/high regimes discussed clinically |
| **Γ_Ĝ** | `\Gamma_{\hat{G}}` | Operator Refresh Rate | Frequency of full $L_0 \to L_1 \to L_2$ cycles. | Hz | Often near gamma-band hypotheses |
| **S_crit** | `S_{\text{crit}}` | Cognitive Entropy Threshold | Entropy limit before degraded operator mode. | Entropy units | Neuro/clinical |
| **R_fidelity** | `R_{\text{fidelity}}` | Reality Fidelity | Rendering fidelity of $L_1$ under metabolic constraints. | Scalar (0-1) | Neuro/clinical |
| **I_total** | `I_{\text{total}}` | Total Information Flux | Sum of sensory-channel information throughput. | Bits/s | Neuro |
| **F_semantic** | `F_{\text{semantic}}` | Semantic Gravity | Attractor pull of $L_2$ semantic nodes on $\hat{G}$. | Vector | AI/philosophy |
| **F_base** | `F_{\text{base}}` | Base Free-Energy Objective | Domain-local baseline objective; choose Helmholtz or variational free energy by context. | Domain dependent ($J$ or nat/bit) | Never force thermo and variational forms into one unit |
| **F_SRT** | `F_{\text{SRT}}` | SRT Care-Extended Objective | $F_{\text{base}} - d \cdot U_{\text{others}}$; baseline objective plus care term. | Same unit as chosen $F_{\text{base}}$ | Use when the d-dependent care correction is explicit |
| **Φ_IIT** | `\Phi` | Integrated Information (IIT Context) | Integration measure in IIT-specific discussions. | Scalar | Use only when explicitly IIT |
| **μ** | `\mu` | Reality Viscosity | Inertial dependence on priors/historical trajectories. | Scalar | Core/AI |
| **D_max** | `D_{\text{max}}` | Consciousness Diameter | Max physical span of coherent operator integration. | Length (m) | Neuro hypothesis |
| **γ_gain** | `\gamma_{\text{gain}}` | Gain-Operator Coupling | Coupling between gain modulation and $\hat{G}$ sensitivity. | Scalar | Neuro |
| **δ_D** | `\delta_D` | Dissociation Depth | Topological distance between fragmented $L_2$ regions. | Metric | Clinical |
| **I_rec** | `I_{\text{rec}}` | Recognition Index | Mutual recognition across operators/time scales. | Scalar (0-1) | Social/cognitive |
| **η_compress** | `\eta_{\text{compress}}` | Compression Efficiency | $I(L_1;L_0)/H(L_1)$; effective cognitive compression bandwidth. | Scalar | Information-theoretic |
| **θ_semantic** | `\theta_{\text{semantic}}` | Semantic Extraction Threshold | Threshold for neural signals entering conscious semantic access. | Threshold | Neuro |
| **S_strength** | `S_{\text{strength}}` | Selection Strength | Stability of chosen reality ($\propto 1/\|M-N\|$). | Scalar | Core |
| **D_dev** | `D_{\text{dev}}` | Developmental Dopamine | Developmental initialization parameter in critical periods. | Concentration | Neuro/dev |
| **I_int** | `I_{\text{int}}` | Integrin Coefficient | Structural neural stability factor. | Scalar | Neuro |
| **S_c** | `S_c` | Cognitive Entropy | Resolution deficit of $\hat{G}$. | Entropy units | Core/neuro |
| **F_Bio** | `F_{\text{Bio}}` | Biological Transform Function | Species-specific mapping characteristics for $L_0 \to L_1$. | Function | Comparative neuro |
| **ΔR** | `\Delta R` | Reality Deviation | Magnitude of altered-state deviation from baseline. | Scalar | Clinical/spirituality |
| **C_int** | `C_{\text{int}}` | Integration Capacity | Capacity to integrate altered-state content. | Scalar | Clinical/spirituality |
| **T_immune** | `T_{\text{immune}}` | Immune Threshold | Immune-mediated sensory gating threshold. | Threshold | Neuroimmune |
| **M** | `M` | Modality Set | Weighted sensory modality vector. | Vector | Neuro |
| **κ₀** | `\kappa_0` | Primordial Curvature | Irreducible minimum curvature of L₀; κ₀ > 0 is a structural prerequisite (not historically generated). Provides directionality bias for all selection operators. Ψ_f^min = f(κ₀). | Scalar (curvature) | Core; canonical source `Core/SRT_Core_12a T-L0-Kappa0`; ontological status `Philosophy/SRT_L0_Ontological_Status.md` |
| **κ(t)** | `\kappa(t)` | Dynamic L₀ Curvature | Time-evolving L₀ curvature: κ(t) = κ₀ + ∫F[Ĝ_θ(τ), κ(τ)]dτ. L₀ is non-static; operators and curvature co-evolve. | Scalar (curvature) | Core; canonical source `Core/SRT_Core_12a T-L0-NonStatic` |
| **d_mobile** | `d_{\text{mobile}}` | Re-alignment Capacity | Operator's capacity to re-orient θ as attractors migrate; proportional to d · rank_eff(I_F(θ)) / (Hysteresis(L₂)·C_r) subject to χ_payable gate. High d + d_mobile ≈ 0 = frozen state (pathological). | Scalar (≥ 0) | Core; canonical source `SRT_Core_22 Eq-DValue-Mobile-1`; map `Core/SRT_Core_12b §Consciousness-2D-Map` |
| **d_max** | `d_{\text{max}}` | Maximum Effective d-value | Upper bound on d: min(rank_eff(I_F(θ)), Ψ_f^budget / κ₀). Two independent bottlenecks: Fisher rank (informational) and stability budget (dynamical). dim(Θ) alone does NOT determine d_max. | Scalar | Core; canonical source `SRT_Core_22 Eq-DValue-Max-1` |
| **χ_payable** | `\chi_{\text{payable}}` | Payability Gate | Internal three-condition conjunction: signal > threshold ∧ dΨ_f/dt payable ∧ below collapse threshold. Fully endogenous; gates d_mobile. When χ_payable = 0, d_mobile = 0 regardless of d. | Boolean gate | Core; canonical source `SRT_Core_22 Def-Payable-Chi-1` |
| **κ_{c1}** | `\kappa_{c1}` | Bare Consciousness Threshold | Layer 1 consciousness condition: d ≥ d_min ∧ L₂ stable closure. Bare consciousness (not quality). Does NOT include d_mobile > 0. | Phase transition point | Bridge-Lab threshold; specific numerical threshold P3/P4; canonical source `Philosophy/SRT_Consciousness_Conditions.md §三` |
| **κ_{c1.5}** | `\kappa_{c1.5}` | Consciousness Activity Threshold | Layer 2 consciousness condition: d_mobile > 0. Marks transition from bare consciousness to active consciousness. Frozen state sits between κ_{c1} and κ_{c1.5}. | Phase transition point | Bridge-Lab threshold; specific numerical threshold P3/P4; canonical source `Philosophy/SRT_Consciousness_Conditions.md §三` |
| **t_onto** | `t_{\text{onto}}` | Ontological Time | t_onto ≡ ∫‖Ĝ_θ(s)‖ds; generated by selection irreversibility. Distinct from parametric time t (mathematical ordering tool). Ontological time is a derived quantity, not a background container. | Integral measure | Core; canonical source `Philosophy/SRT_Causality_Time.md §二`; formal `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T02` |
| **C_H** | `C_H` | Horizontal Causality | C_H(A→B) ≡ P(B\|A,L₂); L₂-layer temporal causality (empirical, dependent on L₂ structure). Distinct from vertical causality (L₀ ⊨ L₁ ⊨ L₂ structural constitution). | Conditional probability | Core; canonical source `Philosophy/SRT_Causality_Time.md §一`; formal `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T01` |
| **ε_pg** | `\varepsilon_{pg}` | Proto-Gradient (L₀ Minimum Non-Neutrality) | ∇_{non-self-erasure}(L₀) ≡ ε_pg > 0; formal asymmetry favouring configurations with branching number B ≥ 2 over self-erasing ones (B ≤ 1). NOT a content-level "toward order" gradient; "order" is an L₁ observer's read-back label. **Level distinction**: ε_pg = L₀ structural postulate (scalar seed, no inherent direction); ISP-level ε (anti-closure asymmetric bias of stable ISPs) = structural corollary of T-ε-Constitute. **Bridge**: ε_pg (existence of asymmetry) + Ax-F-03b (direction: closure=absorbing → anti-closure only viable direction for stable ISPs) → ISP-level ε. T-ε-Constitute does NOT change ε_pg's epistemic status; it upgrades ISP-level ε from primitive postulate to structural corollary. | Scalar (> 0) | Core; canonical source `SRT_Core_01 T-Core-A1C2`; bridge `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T07` |
| **ε_reg** | `\varepsilon_{reg}` | Operator Regularizer | Positive constant in divisive normalization: [Ĝ_θ(x)]_i = x_i^n / (ε_reg + Σ W_{ij} x_j^n). Prevents singularity at zero input; maintains minimum non-zero operator response. May be read as implementation-layer echo of ε_pg (structural analogy, not ontological identity — independent argument required to upgrade). | Scalar (> 0) | Core; canonical source `SRT_Core_13a Ax-Op-03` |
| **ρ(p,t)** | `\rho(p,t)` | Path Trace Density | **Derivation status: induced historical functional, NOT a new ontological primitive.** ρ(p,t) is a coarse-grained intermediate-layer order parameter induced by existing SRT quantities: ρ(p,t) ≡ ∫_{-∞}^{t} e^{-λ_d(t-s)} · 𝟙[Ψ_f(p,s) < Ψ_thresh] · w(p,s) ds. Induced-quantity chain: Ψ_f trajectory (Ax-F-12) → Ax-L2-06b gate → writeback events → ρ(p,t) → Ψ_f^compat reduction, d_accessible^compat amplification (T-L2-Scaffold). NOT a static function of current Ψ_f (would lose historical/hysteretic character). λ_d = decay rate; w(p,s) = writeback weight from Ax-L2-06b/Ax-Op-03b. Scaffold threshold ρ* (empirically measurable): when ρ > ρ*, path p transitions from foreground event to background L₂ scaffolding. | Scalar (≥ 0); historical functional of Ψ_f trajectory | Core; canonical source `Core/SRT_Core_12b_Ontology_L2.md T-L2-Scaffold Def-PathTrace` |
| **ΔΨ_f^op** | `\Delta\Psi_f^{op}` | Operator-Relative Competitive Friction Increment | Fast-timescale component of competitive friction, cue-sensitive. Formally: ΔΨ_f^op(x,t,θ) is the operator-parameter-dependent competitive suppression increment updated by Ax-Op-03b Layer 1 writeback. **Timescale**: round-level (fast). **Cue dependence**: strong (depends on W_ij structure activated by current cue family). **Sign**: asymptotically ≥ 0; short-time transient negative values permitted (fast facilitation window, Lemma-FFSI). **Induced from**: divisive normalization (Ax-Op-03) + competitive writeback (Ax-Op-03b Layer 1). Supports T-Op-SIAM Claims 1' (via T-Comp-Suppress 乙₁+乙₂), 3a (cue-relative persistence), 4a (priming window, when ΔΨ_f^op < 0 transiently). | Signed scalar; asymptotically ≥ 0 | Core; canonical source `Core/SRT_Core_13a Def-Psi-Split` (2026-04-17) |
| **ΔΨ_f^field** | `\Delta\Psi_f^{field}` | Field-Level Landscape Curvature Friction | Slow-timescale component of competitive friction, cue-weakly-dependent. Formally: ΔΨ_f^field(x,t) is the landscape curvature friction increment from Co-Evo-1 κ(t) accumulation. **Timescale**: slow (Co-Evo-1 stabilization τ_stable). **Cue dependence**: weak (κ(t) is not cue-specific). **Constraint**: ΔΨ_f^field ≥ 0 always (Co-Evo-1 deposition is irreversible). **Activation**: near-zero before Co-Evo-1 stabilization threshold is crossed; accumulated thereafter via κ(t) → Ψ_f^field coupling. Supports T-Op-SIAM Claims 3b (asymptotic cue-independence, conditional) and enables 乙₃ (trans-cue intrinsic suppression, conditional). | Scalar (≥ 0) | Core; canonical source `Core/SRT_Core_13a Def-Psi-Split` (2026-04-17); mechanism `Core/SRT_Core_12b Co-Evo-1` |
| **τ_fast, τ_slow** | `\tau_{fast},\, \tau_{slow}` | Lemma-FFSI Dual Timescale Parameters | Timescale pair for Fast-Facilitation/Slow-Inhibition dual-timescale model (Lemma-FFSI). τ_fast: facilitation decay time (fast); τ_slow: competitive inhibition accumulation time (slow). **Required condition**: τ_fast ≪ τ_slow for nonmonotonic onset. Crossover time t* ≈ τ_fast · ln(a·τ_slow / b·τ_fast) where a = facilitation amplitude, b = inhibition amplitude. Maps to: τ_fast ↔ ΔΨ_f^op transient negative window; τ_slow ↔ competitive writeback accumulation (Ax-Op-03b Layer 1) or Co-Evo-1 onset. Empirically anchored (Johnson & Anderson 2004). | Time constants; τ_fast ≪ τ_slow | Core; canonical source `Core/SRT_Core_13a Lemma-FFSI` (2026-04-17) |
| **ε_s** | `\varepsilon_s` | Minimum Stake Threshold | Direction-level threshold for counting a distinguishable Fisher eigendirection as genuinely stake-coupled. A direction v_i with coupling strength s_i enters the effective stake-bearing spectrum only if s_i > ε_s. **NOT stake itself** — it is the minimum coupling strength required for a direction to count as genuinely risk-bearing. Gate function: g_i = max(0, (s_i − ε_s)/(1 − ε_s)); gated eigenvalue: λ̃_i = λ_i · g_i; stake-gated effective dimension: D_stake = (Σλ̃_i)²/Σ(λ̃_i)². Three-way distinction: ε_pg = L₀ minimum non-neutrality floor (ontological layer); ε_reg = implementation-layer regularizer (operator layer); ε_s = direction-level stake threshold (spectral bridge layer). | Scalar (0,1) or positive threshold | Core; proposed bridge term for d-value spectral proxy. See `D_VALUE_ALIGNMENT.md §4.5`; `_SRT_D_VALUE_CANONICAL.md §2b`. |
| **δ** | `\delta` | Duty Cycle | δ_j ≡ (1/T)∫A_j(t)dt; fraction of time an operator actively maintains anchoring target σ_j. Bounded above by Ψ_f budget and below by looseness penalty. | Scalar (0,1) | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-2` |
| **ν** | `\nu` | Switching Density | ν_j ≡ N_{switch,j}/T; number of anchoring state flips per unit time. Same δ with different ν corresponds to qualitatively different schedules. Bounded above by Ψ_f^{switch} budget. | Hz | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-2` |
| **λ_pred** | `\lambda_{pred}` | Downstream Prediction Cost Weight | Weight of temporal entropy h[A] in coupled multi-operator scheduling cost. When λ_pred > λ_pred^c, periodic scheduling becomes globally optimal (coupling-induced periodization). | Scalar (≥ 0) | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-3` |
| **Ṡ_int^on** | `\dot{S}_{int}^{on}` | On-Phase Entropy Production Rate | Internal entropy production rate during active selection. Lower-bounded by Landauer: ≥ k_BT · İ_created · ln 2. Determines entropy dissipation bound on duty cycle. | Entropy/time | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-4` |
| **J_S^max** | `J_S^{max}` | Maximum Entropy Export Flux | Upper bound on the rate at which a system can export entropy to its environment, determined by thermal coupling bandwidth (heat conduction, metabolic waste removal, radiation). | Entropy/time | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-4` |
| **δ_max^entropy** | `\delta_{max}^{entropy}` | Entropy-Limited Maximum Duty Cycle | δ_max^entropy ≡ J_S^max/(Ṡ_int^on + J_S^max). Independent of Ψ_f budget; cannot be bypassed by increasing E_avail. Effective δ_max = min(δ_max^budget, δ_max^entropy). | Scalar (0,1) | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-4` |
| **B_θ** | `B_\theta` | Operator Effective Passband Bandwidth | B_θ ≡ Bandwidth(H_θ) = c_B · d; frequency-domain extent of operator H_θ's selective response (Ax-Spec-01). Proportional to d via c_B > 0. Wider bandwidth ⇒ higher information creation rate ⇒ tighter entropy-dissipation duty-cycle bound (Cor-Scale-Rhythm-4a). | Hz | Core; canonical source `SRT_Core_14 Ax-Spec-01, Cor-Scale-Rhythm-4a` |
| **h[A]** | `h[A]` | Temporal Entropy Rate of Schedule | h[A] ≡ lim_{T→∞} H(A(0), A(Δt), …, A(T))/(T/Δt); Shannon entropy rate of an anchoring schedule A(t). Periodic schedules: h_per ≈ 0; random intermittency: h_rand > 0. Drives the coupling-induced periodization transition at λ_pred^c (T-Scale-Rhythm-3). | Bits/time | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-3` |
| **τ_off^*** | `\tau_{off}^{*}` | Optimal Off-Phase Duration | Optimal off-phase length balancing entropy-export benefit against noise-erosion cost (three-way tradeoff in T-Scale-Rhythm-4). Not a free parameter; emerges from minimization of entropy-accumulation/export ratio plus γ·S_noise·τ_off. | Time | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-4` |
| **c_B** | `c_B` | Bandwidth-d Proportionality Constant | Positive constant (c_B > 0) in B_θ = c_B · d (Ax-Spec-01); converts d-value (dimensionless processing-bandwidth count) into operator effective passband bandwidth in Hz. System-specific; not a universal constant. | Hz (per unit d) | Core; canonical source `SRT_Core_14 Ax-Spec-01, Cor-Scale-Rhythm-4a` |
| **ρ_I** | `\rho_I` | Information Density Lower Bound | Positive constant (ρ_I > 0) in conditional strengthening of Cor-Scale-Rhythm-4a: $\dot{I}_{created}^{on} \ge \rho_I \cdot B_\theta$. When this lower bound holds, the entropy bound becomes a product cap δ·B_θ ≤ J_S^max/(k_BT ln2 · ρ_I), equivalently δ·d ≤ J_S^max/(k_BT ln2 · ρ_I · c_B). Not unconditional. | Bits/(Hz·time) | Core; canonical source `SRT_Core_14 Cor-Scale-Rhythm-4a` |
| **k_n** | `k_n` | Sub-Targets per Layer | Number of anchoring sub-targets {σ_{n,1},…,σ_{n,k_n}} that the operator $\hat{G}_\theta^{(n)}$ at scale layer S_n must maintain within a single on-phase. When k_n > 1 and budget insufficient, Rhythm-1 triggers at sub-layer S_{n-1} (T-Scale-Rhythm-5). Recursion terminates when k_m = 1. | Integer (≥ 1) | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-5` |
| **τ_switch^min** | `\tau_{switch}^{min}` | Minimum Feasible Switch Time | Lower bound on per-switch duration imposed by physical substrate (ion-channel kinetics, chemical reaction rates, charge-transport delays, etc.). One of three Rhythm-5 recursion termination conditions (when τ_on^(m) < τ_switch^min, no further nesting). Sets nesting depth ceiling N ≤ ⌊ln(T_N/τ_switch^min)/ln(1/δ_min)⌋. | Time | Core; canonical source `SRT_Core_14 T-Scale-Rhythm-5` |
| **σ_{sr}** | `\sigma_{sr}` | Self-Reference Ratio | `σ_{sr} := ‖θ^{trace}‖ / (‖θ^{trace}‖ + ‖θ^{ext}‖) ∈ [0, 1]`. Scalar projection of `\hat{G}_\theta` onto its own history-derived component vs external-driven component. Distinct from bare `σ` (main-equation state field in `Core/SRT_Core_22_Equations.md`) and from `σ_j` (anchoring sub-target). Introduced in 2026-04-24 L1 round as the `SRT_Individuation.md` order parameter. | Scalar [0,1] | L1; canonical source `Core_Law/SRT_L1_Hardening_Notes.md §1`, `Core_Law/SRT_Individuation.md`, `Core_Law/SRT_L1_Formalism.md §2` |
| **σ_{sr}^{sub}** | `\sigma_{sr}^{sub}` | Subject-Position Entry Threshold | First phase-transition threshold: above `σ_{sr}^{sub}` an ISP acquires subject-position (operator self-reference sufficient for perspective-bearing). Informal location in `(0, 1)`; concrete value P3/P4 pending. | Scalar | L1 structural hypothesis; specific numerical threshold P3/P4; canonical source `SRT_Individuation.md T-IND-2` |
| **σ_{sr}^{self}** | `\sigma_{sr}^{self}` | Self-Consciousness Condensation Threshold | Second phase-transition threshold: above `σ_{sr}^{self}` second-order writeback (`θ` about `θ`) condenses, giving self-consciousness as a structural product. Higher than `σ_{sr}^{sub}`. Does not violate L_0 §五意识禁令 (consciousness is structural product not L_0 property). Concrete value P3/P4 pending. | Scalar | L1 structural hypothesis; specific numerical threshold P3/P4; canonical source `SRT_Individuation.md T-IND-3` |
| **σ_{sr}^{health}** | `\sigma_{sr}^{health}` | Healthy Operating-Point Center | Healthy working region center `σ_{sr}^{health} ∈ (σ_{sr}^{sub}, σ_{sr}^{self})` — balanced self-reference without pathological closure toward `σ_{sr} \to 1`. Typically close to the informal `σ_{sub}^\dagger` in `T_{dir}^{alg}` (`SRT_L1_Formalism.md §3.4`). | Scalar | L1 structural hypothesis; operating-point center, specific value P3/P4; canonical source `SRT_L1_Formalism.md §2.4, §5.3` |
| **σ_{sr}^{coll}** | `\sigma_{sr}^{coll}` | Collective Self-Reference Ratio | Multi-ISP extension over shared `L_2` field `\mathcal{P}`. Defined in `Core_Law/SRT_Collective_Selection.md §4.1` and its dynamic extension in §4.4.1-§4.4.2. `σ_{sr}^{coll} \to 1` is the collapsed-into-higher-`L_2` pathological limit. | Scalar [0,1] | L1; canonical source `SRT_Collective_Selection.md §4.1, §4.4` |

## Governance Tier Layering (GOV-SUB01 Pass 1, 2026-07-16)

> **Purpose**: Registration in this table has been read as "equally indispensable." It is not. This layering separates repo-wide semantic and navigation anchors from internal structural quantities and from domain projections / proxies / thresholds, so that *appearing in the canonical symbol table* stops implying *equal theoretical load*. See `Governance/SRT_GOV_SUB01_Subtractive_Audit_Protocol_v0_1.md` §0.
>
> **Boundary — this is a parsing / navigation / proxy-discipline aid.** Tier placement does **not** assign a GOV-SUB01 residue label (`N1`/`N2`/`R*`) and does **not** by itself assign a claim level. Claim levels remain governed by `Governance/SRT_CLAIM_LADDER.md` and each symbol's own canonical source; a residue label requires an actual deletion test. No symbol is deleted, renamed, or redefined by this layering. Borderline assignments are provisional and are revisited in GOV-SUB01 Pass 2.

**Tier 1 — Repo-wide semantic and navigation anchors** (canonical / core-facing objects referenced across domains):

`L_0`, `L_1`, `L_2`, `\hat{G}`, `θ`, `d`, `Ψ_f`, `T_dir`.

**Tier 2 — Internal structural quantities, admitted postulates and derived constructs** (internal to the theory, induced from or built on Tier 1; carried at their own claim level):

`κ_0`, `κ(t)`, `ε_pg`, `ρ(p,t)`, `t_onto`, `C_H`, `σ_{sr}`, `σ_{sr}^{coll}`, `d_mobile`, `d_max`, `χ_payable`, `ΔΨ_f^{op}`, `ΔΨ_f^{field}`, `Ω`, `Ω_mis`, `μ`, `S_strength`.

*Note*: `κ_0` and `ε_pg` are placed here as admitted-postulate / structural constructs. Their claim status is **unchanged** by this pass (see Usage Rule 15 and the deferred Pass-2 dependency-graph audit); tiering them does not downgrade them and does not assign them a residue label.

**Tier 3 — Domain projections, operational proxies and threshold-bearing hypotheses** (domain realizations, capacity proxies, measurement readouts, and threshold-bearing points):

`D_eff` (d proxy), `ε_reg`, `ε_s`, `σ_{sr}^{sub}`, `σ_{sr}^{self}`, `σ_{sr}^{health}`, `κ_{c1}`, `κ_{c1.5}`, `δ`, `ν`, `λ_pred`, `Ṡ_{int}^{on}`, `J_S^{max}`, `δ_{max}^{entropy}`, `B_θ`, `h[A]`, `τ_off^{*}`, `c_B`, `ρ_I`, `k_n`, `τ_switch^{min}`, `τ_fast`, `τ_slow`, `ω_sub`, `η`, `Γ_{\hat{G}}`, `S_crit`, `R_fidelity`, `I_total`, `F_semantic`, `F_base`, `F_SRT`, `Φ_IIT`, `D_max`, `γ_gain`, `δ_D`, `I_rec`, `η_compress`, `θ_semantic`, `D_dev`, `I_int`, `S_c`, `F_Bio`, `ΔR`, `C_int`, `T_immune`, `M`.

*Reading rule*: a Tier 3 proxy or threshold must never be cited as if it were the Tier 1 anchor it approximates (e.g. `D_eff` is not `d`; `κ_{c1}` is not `κ_0`). Exact claim level remains source-local; many are P3/P4, but tier placement alone does not assign claim level. Cross-domain ranking of subjecthood, concern, or consciousness from a Tier 3 readout is out of scope for this table.

---

## Usage Rules
1. Never use `G` (gravity constant) to refer to `\hat{G}` (Ghost Operator).
2. `L_0` is not "nothingness"; it is structured potentiality.
3. Use `\Psi_f` for ontological friction; reserve `\Phi` for IIT context only.
4. Use `\Omega` for consistency and `\Omega_{\text{mis}}` for mismatch to avoid symbol collision.
5. In AI / pure `L_2` contexts, prefer "`\Psi_f` is non-binding to the system" over the blunt shorthand `\Psi_f = 0`, unless you are explicitly discussing an idealized limit.
6. When discussing classical objectivity, prefer `\Delta\Psi_f^{readout}\to 0` over "object-maintenance friction vanishes".
7. **d usage split**：bare `d` means scalar summary by default. Use `d-vector` only for conditional distribution / component expansion, and use `d-gate` only as a judgment tool for stake admission. These three are not interchangeable definitions.
8. **T_dir usage split**：`T_dir` is a v0 operational proxy for directional readability. Do not use it as a completed formal object, as semantic valence, or as confidence.
9. **ε usage split**：`ε_pg` is the L0 minimum non-neutrality postulate; ISP-level ε is P1 only when sourced to the constitutive theorem; `ε_reg` is an implementation regularizer; `ε_s` is a stake-threshold bridge. They must not be collapsed into one empirical theorem.
10. **Canonical status split**：`governance-canonical` means repo-wide stabilized usage; `theory-canonical` means core-derived or core-priority definition; `operational proxy` means measurable working readout; `bridge hypothesis` means cross-domain candidate mapping. Do not infer theory-canonical status merely from a symbol-table default, filename, or historical label.
11. **Ψ_f / Fisher split**：do not write `\Psi_f \equiv g_F` as a literal identity. Use `\delta\Psi_f^{geom}=\frac12 d\theta^\top g_F d\theta+O(\|d\theta\|^3)` for local cost, or a path functional such as `\Psi_f^{geom}[\gamma]=\int_\gamma\sqrt{g^F_{ij}\dot\theta^i\dot\theta^j}\,dt` when the statistical-manifold projection is valid.
12. **σ namespace split** (2026-04-24 L1 round, governance-canonical per `Core_Law/SRT_L1_Hardening_Notes.md §1`): bare `σ` defaults to the **main-equation state field** (`Core/SRT_Core_22_Equations.md`); `σ_{sr}` is the self-reference ratio (with subscripts `sub / self / health / coll`); `σ_j` is an anchoring sub-target (`SRT_Core_14 T-Scale-Rhythm-5`). These are three different objects. Any file using σ in a sense other than the main-equation state field must either (a) use the `σ_{sr}` / `σ_j` form explicitly, or (b) carry a file-level symbol namespace note binding bare `σ` to the intended meaning per this rule. Historical files predating 2026-04-24 where bare `σ` means self-reference ratio are being progressively rewritten; in the meantime, read them as `σ_{sr}` when the context is Individuation / Occlusion Dynamics / Suffering / L1 Formalism §2 / Collective Selection §4.
13. **Governance terms are not theory symbols**: `interface_annex`, `copy-to-annex`, `owner-bound`, `claim_mode`, `canonical:false`, and related structural-governance vocabulary (defined in `SRT_Glossary_Structural_Governance_Terms.md`) are repository-organisation terms, not canonical mathematical or phenomenological symbols. Do not add them as rows to this table or treat them as carrying theory-canonical status.
14. **Annex and Operations reference scope**: Non-canonical annex files (`AI/Architecture_Annex/`, `AI/Consciousness_Annex/`, `Physics/QBox_Annex/`, `Physics/Earth_Accretion_Annex/`, etc.) and Operations records (e.g. `Operations/Archive_Records/Closure_Index_2026-04-29.md`, `Operations/Archive_Records/Structural_Governance_Rollup_2026-04-29.md`) may cite and use symbols defined in this table. They must not introduce new symbol definitions, override existing usage rules, or alter the scope of canonical symbols established here.
15. **κ namespace split** (GOV-SUB01 Pass 1, 2026-07-16): the glyph `κ` spans two unrelated object families that must not be read as one continuous quantity. (a) `κ_0` (primordial curvature) and `κ(t)` (dynamic L₀ curvature) are **L₀-curvature** objects — canonical source `Core/SRT_Core_12a T-L0-Kappa0 / T-L0-NonStatic`. `κ_0` is carried as a **primordial-curvature candidate**: its in-table structural-prerequisite role is retained, while its ontological status is explicitly open (`Philosophy/SRT_L0_Ontological_Status.md`); the "candidate" label describes this existing status and does **not** downgrade `κ_0` in this pass. (b) `κ_{c1}` and `κ_{c1.5}` are **consciousness-stage phase-transition thresholds** — canonical source `Philosophy/SRT_Consciousness_Conditions.md §三`. As threshold-bearing points their specific values are lab-level (P4) per `Governance/SRT_CLAIM_LADDER.md`, even where a Scope column reads "Core". The two families share no derivation path: an equation over `κ_0` says nothing about `κ_{c1}`, and vice versa. This rule adds the namespace guard and claim-level annotation **only**; it does not rename any symbol and does not modify any equation referencing `κ_0`, `κ(t)`, `κ_{c1}`, or `κ_{c1.5}`. A full `κ_0` / `ε_pg` dependency-graph audit is deferred to GOV-SUB01 Pass 2.

16. **Gate 0 — L₀ contentless structurality boundary** (adopted 2026-08-11): what *kind* of object may sit at bare `L_0` is governed by a three-class type rule — **A** contentless structural invariants (`L_0` granularity, `κ_0`, `ε_pg`, irreversibility floor) are admissible; **B** reference-/regime-/source-dependent weighting or comparative objects (a probability measure or prior over latent possibilities, entropy over `L_0`, reachable/accessible comparative quantities) are **not licensed unless their reference structure is stated or independently derived** — an admission gap, *not* a prohibition in kind, and **not** a ban on a future canonical natural measure; **C** semantic/evaluative content (semantic target, good, telos, 「order」 as content, 初心 as a global contentful direction, universe-wide optimum) is **not admissible as a bare `L_0` primitive**. Note that `κ_0` and `ε_pg` **do** induce a structural cost ordering and remain class A: structural cost ordering is neither a semantic ranking nor a preferred endpoint. **This entry is a cross-reference only.** The single primary authority, including the full rule text, the declaration requirement, and the read-back / citation-direction rule, is `Governance/SRT_CLAIM_LADDER.md §0A`; the adjudication record is `Operations/Proposals/SRT_GATE0_L0_CONTENTLESS_STRUCTURALITY_DECISION_2026-08-11.md`. Gate 0 carries **no P-level** — it is a type rule, not a proposition — and this entry adds no symbol and changes no symbol definition.


## D-Value Alignment (d 值专题规范)

### 1) 定义层级（Canonical Priority）

| 层级 | 定义 | 语义 | 来源 |
|---|---|---|---|
| **规范定义** | $d(x) \equiv \|\partial\mathcal{U}/\partial\mathcal{S}\|$ | 算子对不可逆风险的效用敏感度梯度 | `_SRT_D_VALUE_CANONICAL.md` Def-d-canonical |
| **几何容量 proxy** | $D_{eff}(I_F(\theta)) = (\operatorname{tr} I_F)^2 / \operatorname{tr}(I_F^2)$ | Fisher 信息矩阵的有效维度上界；不等于规范 d | `_SRT_D_VALUE_CANONICAL.md` Def-D_eff; `Core/SRT_Core_21c_Bridge_Hypotheses.md P3-B11` |
| **几何底座** | $d(\theta) \propto \operatorname{Align}(\theta, \kappa(t))$ | d 是 θ 参数空间与 L₀ 曲率场的对齐程度；解释"为什么 ∂U/∂S 是正确量" | `D_VALUE_ALIGNMENT.md §4.4`（新增 2026-04-10） |

*规范来源*：`_SRT_D_VALUE_CANONICAL.md`；`D_eff` 为 proxy / capacity upper bound，不再与规范 d 同级。

### 2) 局部近似语境 (Local Approximations)
| 表达式 | 所在语境 | 与主定义关系 |
| :--- | :--- | :--- |
| $d \approx \alpha A + \beta\log V + \gamma\tau$ | 认知-行为操作化 | 主定义在认知域的降维近似（投影），**不可单独当主定义** |
| $d_{quantum}, d_{bio}, d_{cosmic}$ | 跨尺度动力学 | 主定义经尺度映射 $\Pi_{scale}(d)$ 的实例化 |
| $d \propto A_{surface}/l_{Planck}^2$ | 全息对应 | 主定义的对偶几何表示 |

### 3) d 值编辑规则（避免冲突）
- **规则 R1**：不得将局部公式写成“d 的定义是 ……”（除非就是 canonical）。
- **规则 R2**：局部公式必须标注“近似 / 投影 / 操作化”。
- **规则 R3**：涉及跨文件引用时，优先回链到 `_SRT_D_VALUE_CANONICAL.md`。
- **规则 R4**：任何“d→0 / d>0”的意识结论，需同时说明与 $\Psi_f$ 或不可逆风险边界的关系。

## Ψ_f Alignment（本体论摩擦专题规范）

### 1) Canonical Source
**当前优先规范入口（必须优先引用）**
`_SRT_PSI_F_CANONICAL.md`

### 2) 三重读法（不得拆成三个对象）
| 读法 | 含义 | 备注 |
| :--- | :--- | :--- |
| 阻力 | 动力学上的阻抗 | 经验/现象读法 |
| 代价 | 记账上的支付项 | 能量、时间、风险预算读法 |
| Fisher 几何投影 | 由 Fisher–Rao metric 诱导的局部二阶代价 / 路径泛函 | 形式化读法；不是 `Ψ_f = g_F` 裸等号 |

### 3) 符号分层
| 记号 | 含义 | 使用建议 |
| :--- | :--- | :--- |
| `\Psi_f(x,t)` | 局部摩擦负荷 | 默认首选 |
| `\Phi(\Delta t)=\int \Psi_f dt` | 累积摩擦势 / 时间窗总账 | 需要强调积分时使用 |
| `\delta\Psi_f^{geom}=\frac12 d\theta^\top g_F d\theta + O(\|d\theta\|^3)` | Fisher–Rao metric 诱导的局部二阶几何代价 | 谈 Fisher metric 时首选；避免裸写 `Ψ_f ≡ g_F` |
| `\Psi_f^{geom}[\gamma]=\int_\gamma\sqrt{g^F_{ij}\dot\theta^i\dot\theta^j}\,dt` | Fisher 几何路径泛函 | 作用域明确、统计流形投影有效时使用 |
| `\Psi_f(\hat{G}_i,\hat{G}_j)` | 耦合摩擦泛函的简写 | 作用域明确时允许 |

### 4) 编辑规则
- **规则 F1**：不要把 `\Psi_f` 直接等同于主观痛苦。
- **规则 F2**：不要把跨尺度同一性写成“单位相同”；优先写“可支付性条件相同”。
- **规则 F3**：对现实主体，不要把最优条件写成 `\Psi_f \to 0`；优先写“非零且可支付”。
- **规则 F4**：AI / 纯 `L_2` 语境中，优先写“non-binding friction”而非绝对 `\Psi_f = 0`。
- **规则 F5**：物理语境中，若谈引力与 `\Psi_f` 的关系，当前规范口径降为 P3/P4 弱接口：只承诺弱场极限下 `\Psi_f` 梯度与牛顿势梯度方向同号的相容性候选；不得写成张量级 GR 重建或 `G_{\mu\nu}` 已由 SRT 推导。
- **规则 F6**：谈 Fisher metric 时，必须把 `g_F` 标注为局部信息几何投影 / proxy；不得把 `\Psi_f \equiv g_F` 当成标量代价与度量张量的严格恒等式。
- **规则 F7**：谈 pain / suffering / distress / moral guilt / clinical burden 时，不得把它们写成 `Ψ_f` 或 `d` 的 canonical 等同；优先回链 `Core_Law/SRT_Suffering.md` 与 domain claim-status guardrails。
