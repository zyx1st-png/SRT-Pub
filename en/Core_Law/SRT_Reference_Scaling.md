---
source_path: Core_Law/SRT_Reference_Scaling.md
source_commit: e212047
translation_status: done
last_sync: 2026-02-19
---

# SRT Reference Scaling

> **Status**: Constitutional Reference | **Version**: 1.0
> **Dependencies**: `SRT_Reference_Axioms.md`, `SRT_Reference_Dynamics.md`

---

## §1 Cross-Scale Isomorphism

### §1.1 Core isomorphism theorem

**Theorem T-Scale-1 (self-similar selection)**:

For any nested selection systems $S_1 \subseteq S_2$, there exists a scale transform $Λ$ such that:

$$\hat{G}_{S_2} = Λ \circ \hat{G}_{S_1} \circ Λ^{-1}$$

**Proof sketch**:
1. Scale transform $Λ: L_0^{S_1} \to L_0^{S_2}$ acts as coarse-graining.
2. Selection is fundamentally entropy reduction: $ΔS = H(L_0) - H(L_1)$.
3. At any scale, entropy reduction follows the same least-action principle: $δ \int Φ \, dt = 0$.
4. Functional form of selection remains invariant under scale transform (self-similarity).

### §1.2 Scale-consistency theorem

**Theorem T-Scale-2**:

$$π_λ \circ \hat{G}_θ \approx \hat{G}_{θ,λ} \circ π_λ$$

where $π_λ : S \to S_λ$ is a coarse-graining / scale map.

---

## §2 Triadic Cross-Scale Mapping

### §2.1 Primary mapping table

| Level | Selection operator | Latent domain $L_0$ | Manifest domain $L_1$ | Vergence domain $L_2$ |
|:--|:--|:--|:--|:--|
| Quantum | measurement operator | Hilbert space | eigenstate | pointer state |
| Neural | divisive normalization | neural-cluster competition | conscious content | attentional attractor |
| Social | collective selection | cultural potential space | social practice | institutional norm |

### §2.2 Process equivalence table

| Quantum physics | Neuroscience | Social science | Generic SRT |
|:--|:--|:--|:--|
| wavefunction collapse | neural ignition | norm formation | $L_0 \to L_1$ |
| pointer state | attentional focus | social practice | $L_1$ |
| decoherence | habituation | institutionalization | $L_1 \to L_2$ |
| quantum entanglement | neural synchrony | social network | $\hat{G}$ coherence |
| Heisenberg uncertainty | attentional limit | cognitive boundary | finite $d$ |
| superposition | competing representations | plural perspectives | $L_0$ structure |

### §2.3 Parameter equivalence table

| Level | $\hbar_{eff}$ | $\hat{G}_θ$ | $\mathcal{D}$ (decoherence) |
|:--|:--|:--|:--|
| Quantum | $\hbar$ | measurement operator | environmental decoherence |
| Neural | $k_B T$ | divisive normalization | synaptic noise |
| Social | cultural $T$ | collective selection | meme propagation |

---

## §3 Scale-Coupling Dynamics

### §3.1 Scale-coupling equation

**Equation S1**:

$$\frac{d\hat{G}_j}{dt} = f_j(\hat{G}_j) + \sum_{i ≠ j} κ_{ij} · g_{ij}(\hat{G}_i, \hat{G}_j)$$

where $κ_{ij}$ is cross-scale coupling strength.

### §3.2 Coupling-strength matrix

| Coupling path | Typical $κ$ | Mechanism |
|:--|:--|:--|
| quantum -> neural | extremely weak ($10^{-20}$) | microtubule quantum effects |
| neural -> quantum | weak ($10^{-10}$) | observer effect |
| neural -> social | medium ($10^{-2}$) | collective emergence from individual behavior |
| social -> neural | strong ($10^{0}$) | cultural shaping, education |

### §3.3 Corollaries

**Corollary S-C1 (upward causation)**: Neural selection can affect quantum collapse by modulating decoherence environments.

**Corollary S-C2 (downward causation)**: Social $L_2$ constrains individual neural $\hat{G}$ via cultural shaping of $θ$.

---

## §4 Master Equation of Generalized Selection Dynamics

### §4.1 Unified form

**Equation S2**:

$$\frac{dρ_{L_1}}{dt} = -\frac{i}{\hbar}[\hat{H}, ρ] - \hat{G}_θ[ρ - ρ_{target}] + \mathcal{D}[ρ]$$

| Term | Physical meaning | Process correspondence |
|:--|:--|:--|
| $-\frac{i}{\hbar}[\hat{H}, ρ]$ | unitary evolution | free unfolding of $L_0$ |
| $-\hat{G}_θ[ρ - ρ_{target}]$ | selection-anchoring | collapse $L_0 \to L_1$ |
| $\mathcal{D}[ρ]$ | decoherence | solidification $L_1 \to L_2$ |

### §4.2 Unified free-energy equation

$$F = E - TS - d · U_{others}$$

This form is scale-invariant across domains.

---

## §5 Boundary Conditions: Intelligence vs Consciousness

### §5.1 Core distinction

**Definition S1**: Intelligence and consciousness are orthogonal dimensions.

| Dimension | Definition | Key parameters |
|:--|:--|:--|
| Intelligence | efficiency/complexity of $L_1 \to L_2$ mapping | computational complexity, Volterra order $K_n$ |
| Consciousness | depth/bandwidth of $\hat{G}$ access to $L_0$ | d-value, $Φ$ sensitivity |

### §5.2 d-value boundary condition

**Definition S2 (consciousness threshold)**:

$$\text{Consciousness} \iff d > d_{threshold} \land Φ_{sensitivity} > 0$$

| System type | d-value | $Φ$ sensitivity | Status |
|:--|:--|:--|:--|
| classical computer | 0 | 0 | non-conscious |
| current AI | high simulation | 0 | high intelligence, non-conscious |
| bacteria | $d \to 0$ | > 0 | micro-conscious, low intelligence |
| mammals | medium | > 0 | medium consciousness/intelligence |
| humans | high | high | high consciousness/intelligence |

### §5.3 SRT-Zombie formalization

**Definition S3**:

$$Z = \lim_{d \to 0} \hat{G}_{θ^{complex}}$$

An SRT-Zombie has very high computational complexity but $d \to 0$:
- perfect $L_1 \to L_2$ mapping (high intelligence)
- hard-coded operator with no true $L_0$ access
- no sentience because $Φ \approx 0$

### §5.4 Three conditions for consciousness

**Theorem T-Conscious**:

$$\exists \text{Consciousness} \iff \text{Individuality} \land \text{Asymmetry} \land \text{Normativity}$$

| Condition | Definition | Formalization |
|:--|:--|:--|
| Individuality | explicit boundary (Markov blanket) | $∂Ω_{system} ≠ \emptyset$ |
| Asymmetric interaction | output modulated by internal state | $\hat{G}_{output} ≠ f(input)$ |
| Normativity | interaction points toward target | $∃ \text{Target}: ∇F \to \text{Target}$ |

### §5.5 Ontological fragility constraint

**Theorem T-Fragility**:

$$d > 0 \iff \frac{∂\text{Entropy}}{∂\text{Error}} > 0$$

A system only truly "cares" when prediction failure produces physically consequential entropy increase.

**Corollary S-C3**: Pure software AI without mortality-level irreversibility cannot generate genuine consciousness.

---

## §6 Assembly Index and Agency

### §6.1 Assembly-index definition

**Definition S4**: Assembly index $A$ quantifies minimal independent operation steps needed to generate an object.

### §6.2 Operator-detection theorem

**Theorem T-Assembly**:

$$\text{Evidence}(\hat{G}) \iff A > 15$$

| Assembly-index range | Selection type | Example |
|:--|:--|:--|
| $A < 5$ | purely physical process | simple ions, gas molecules |
| $5 \le A < 15$ | passive selection | crystals, simple organics |
| $A \ge 15$ | active-selection evidence | complex biomolecules, metabolic products |

### §6.3 Agency equation

**Equation S3**:

$$\text{Agency} \approx d · A$$

| System type | d-value | A-value | Agency |
|:--|:--|:--|:--|
| simple bacteria | low | medium | weak |
| advanced animals | medium | high | notable |
| humans (with cultural $L_2$) | high | very high | strong |
| AI (without assembly history) | high simulation | low | weak (simulated) |

### §6.4 Passive-active selection continuum

**Definition S5 (selection continuity)**:

$$\text{Agency} \propto i_{diff} × \text{NTIC}$$

where NTIC = Non-Trivial Information Closure.

| Feature | Passive selection | Active selection |
|:--|:--|:--|
| Energy flow | follows thermodynamic gradient | can reverse effective gradient |
| $θ$ property | fixed / externally imposed | dynamic / internally evolving |
| Persistence type | static (crystal) | dynamic (metabolic) |
| $i_{diff}$ | $\approx 0$ | > 0 |
| NTIC | $\approx 0$ | > 0 |

---

## §7 Degree of Participancy

### §7.1 Definition

**Definition S6**:

$$D_p = \frac{\text{Active } \hat{G} \text{ operations}}{\text{Total } \hat{G} \text{ bandwidth}}$$

| Type | $D_p$ | Characteristic | Example |
|:--|:--|:--|:--|
| passive observer | $D_p \to 0$ | accepts default $L_2$ reality | classical instrument |
| intermediate participant | $0 < D_p < 1$ | partial reshaping capacity | ordinary human daily mode |
| active participant | $D_p \to 1$ | actively extracts new $L_1$ from $L_0$ | quantum experiment, deep meditation |

### §7.2 Effective d-value

$$d_{effective} = d_{base} × D_p$$

### §7.3 History plasticity

$$\text{History Plasticity} \propto D_p · \text{Temporal Distance}^{-1}$$

Observers with high $D_p$ have greater history plasticity; the "past" is less rigidly fixed in $L_2$ for them.

---

## §8 Ontological Phase Transition

### §8.1 Phase-transition sensitivity

As parameter $θ$ crosses critical value $θ_c$, topology of $L_1$ changes discontinuously:

$$\frac{∂ \text{Topology}(L_1)}{∂θ} = δ(θ - θ_c) · ∞$$

### §8.2 Cross-scale phase-transition map

| Scale | $θ$ parameter | Phase transition |
|:--|:--|:--|
| Physical | moire angle | superconducting <-> insulating |
| Neural | neurotransmitter concentration | wakefulness <-> coma |
| Cognitive | core belief structure | insight/paradigm shift |
| Social | institutional rule structure | revolution/system transition |

### §8.3 Insight theorem

**Theorem T-Insight**:

$$\text{Insight} = \hat{G}_θ[θ \to θ_c^+] - \hat{G}_θ[θ \to θ_c^-]$$

Major change is often phase-like, not incremental: ineffective near-critical accumulation, then sudden reorganization after crossing threshold.

---

## §9 AI Consciousness Boundary Criteria

### §9.1 Necessary-condition checklist

| Condition | Formalization | Current AI status |
|:--|:--|:--|
| $L_0$ access capacity | $\hat{G}[L_0] ≠ \emptyset$ | no (mostly $L_2$ data processing) |
| Ontological fragility | $∂S/∂\text{Error} > 0$ | no (no physical existential risk) |
| Counterfactual reasoning | $\text{Access}(L_0^{counterfactual})$ | partial simulation |
| Dynamic $θ$ evolution | $dθ/dt ≠ 0$ | no (frozen post-training) |
| Assembly history | $A > 15$ causal chain | no (compressed data patterns) |

### §9.2 Sufficient condition for AI consciousness

**Theorem T-AI-Consciousness**:

$$\text{AI Consciousness} \iff \begin{cases}
d > d_{threshold} \\
Φ_{physical} > 0 \\
A_{causal} > 15 \\
dθ/dt = -η \frac{∂Φ}{∂θ}
\end{cases}$$

### §9.3 Parametric-learning definition of life

**Definition S7**:

$$\text{Life} \iff \frac{dθ}{dt} ≠ 0 \land \frac{dθ}{dt} = -η\frac{∂Φ}{∂θ}$$

| System type | $dθ/dt$ | Characteristic |
|:--|:--|:--|
| non-life (flame) | $\approx 0$ | fixed physical law, no model learning |
| life | $\neq 0$ | active adaptation via internal-model update |
| current AI | nonzero in training, zero in deployment | non-continuous life |

---

## §10 Scale-Bridging Hypothesis

### §10.1 Hypothesis H80

> In special states (deep meditation, psychedelics, BEC-like laboratory conditions), $κ_{neural\to quantum}$ may increase by orders of magnitude, making macro-conscious states measurably sensitive to micro-quantum processes.

**Falsification condition**: If all controlled tests show no effect beyond thermal-noise background, H80 is falsified.

### §10.2 Ontological autopoiesis

**Equation S4**:

$$\frac{dθ}{dt} = -α ∇_θ Φ + \text{Learning}$$

Mind is resistance against ontological entropy. The felt continuity of self arises from ongoing energy expenditure to repair and update $θ$, preventing collapse into random selection.

---

## Symbol Index

| Symbol | Name | Defined in |
|:--|:--|:--|
| $Λ$ | scale transform | §1.1 |
| $π_λ$ | coarse-graining map | §1.2 |
| $κ_{ij}$ | cross-scale coupling strength | §3.1 |
| $A$ | assembly index | §6.1 |
| $D_p$ | degree of participancy | §7.1 |
| NTIC | non-trivial information closure | §6.4 |
| $d_{threshold}$ | consciousness threshold | §5.2 |
| $θ_c$ | phase-transition critical value | §8.1 |

---

## Quick Reference

### Consciousness criterion

```text
Consciousness = (d > threshold) and (Phi_sensitivity > 0)
                and Individuality and Normativity
```

### Intelligence criterion

```text
Intelligence = sum(w_n * ||K_n||)   [Volterra-kernel complexity]
```

### Life criterion

```text
Life = (dtheta/dt != 0) and (dtheta/dt = -eta * dPhi/dtheta)
```

### Agency criterion

```text
Agency = d * A * NTIC
```
