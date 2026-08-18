---
id: SRT-PAPER-ONTOFRICTION-POSTPUB-CONVERGENCE-20260818
type: post_publication_convergence_note
status: active
layer: L1-L2-bridge
epistemic_layer: bridge-lab
claim_mode: synthesis
claim_level: P3-P4
canonical: false
date: 2026-08-18
dependency:
  - SRT-CORE-21B-CONSTITUTIVE-THEOREMS
  - SRT-CORE-21C-BRIDGE-HYPOTHESES
  - SRT-AGENCY-AUTOMATION-GUARD-20260817
  - SRT-FISHER-FEP-LANDSCAPE-INTERFACE
  - SRT-CORE-12B
  - SRT-INTEROCEPTIVE-PRECISION-BRIDGE-2026-08-08
tags: [Executive Friction, Psi_f, Reachability, Accessibility, Effective Candidacy, Attractor Dynamics, Depression, Generative Reselectability, Post-publication Convergence]
---

# Post-publication convergence: executive friction, transition landscapes, and history-dependent reachability

> **Use rule**: post-publication P3/P4 bridge only. This file does **not** amend the published Frontiers article, add a P0/P1 theorem, identify a clinical mechanism, or authorize neuroscience-owner synthesis.
>
> **Layer guard**: neural states, task/policy states, and SRT candidates are not assumed to be the same state variable. Source-derived neural findings, the published executive-friction claims, and the cross-domain bridge proposed here must remain distinguishable.

## 0. Executive verdict

The useful joint decomposition is:

```text
structural reachability
!= functional accessibility / candidate admission
!= transition friction / payability
!= currently effective candidacy
!= generative reselectability
```

The 2024–2026 neural-dynamics literature is compatible with the published Frontiers framework, but it does not prove `attractor = L2`, `NCT energy = Psi_f`, `persistent neural state = Stable ISP`, or `automation = no Selection`.

For depression, the new evidence does **not** overturn the published agent/policy-level claim that inaction can minimize acute executive friction. It blocks only an overstrong neural gloss that would identify that policy-level low-friction state with one static, long-dwell neural basin. A behaviorally persistent policy can coexist with frequent neural-state transitions and a narrowed transition repertoire.

No canonical edit follows from this note.

---

## 1. Source cluster and evidence roles

### 1.1 Published anchor — Zhang 2026

**Yuxin Zhang.** *A translational cross-modal control-cost framework for executive breakdown.* *Frontiers in Neuroscience* 20 (2026), 1837760. DOI `10.3389/fnins.2026.1837760`. Published 2026-08-06. Article type: Hypothesis and Theory.

Relevant published structure:

- `Psi_f` is operationally treated as a cross-modal latent control/execution-cost factor;
- candidate mechanism families include accumulated control effort and departure from a habitual/default policy; they are not universal identities;
- `P_sel` is an available control-budget proxy;
- the knowing-doing gap can arise when implementation burden exceeds remaining control capacity despite intact representation of the appropriate action;
- slow constraints such as habits, priors, hyperpriors and trait-like limits shape later behavior.

**Boundary**: the paper does not provide a complete theory of candidate accessibility, and represented-but-unexecuted does not automatically mean currently action-guiding.

### 1.2 Vinograd et al. 2024

**Vinograd et al.** *Causal evidence of a line attractor encoding an affective state.* *Nature* 634 (2024): 910–918. DOI `10.1038/s41586-024-07915-x`.

Role: causal implementation-level evidence that affect-related neural population activity can exhibit line-attractor dynamics. On-manifold perturbation can be integrated; off-manifold perturbation relaxes toward the attractor.

```text
causal neural attractor dynamics exist
!= attractor is L2 / Selection / subjecthood
```

### 1.3 Kauvar et al. 2025

**Kauvar et al.** *Conserved brain-wide emergence of emotional response from sensory experience in humans and mice.* *Science* 388(6750) (2025): eadt3971. DOI `10.1126/science.adt3971`.

Role: separates fast sensory broadcast from a slower persistent distributed affect-related pattern; pharmacological perturbation can attenuate the persistent component while largely preserving the fast broadcast.

```text
sensory event detected / broadcast
!= persistent affective context formed
```

Persistent context is an implementation-level result, not by itself `L2`, Stable ISP, or consciousness.

### 1.4 Kilic et al. 2026

**Kilic et al.** *Spatiotemporal asymmetries on brain energy landscape uncover system entrapment related to depression severity.* *Nature Communications* 17 (2026): 5662. DOI `10.1038/s41467-026-71961-4`.

Source-derived findings relevant here:

- 38 MDD / 38 healthy-control participants with 7T resting-state fMRI;
- DWI subset: 26 MDD / 27 healthy controls;
- one CAP state shows elevated entry/exit probability and fractional occupancy despite shorter dwell time;
- State 3 <-> State 2 transitions increase while State 4 <-> State 1 transitions decrease;
- empirical CAP transitions are compared with Network Control Theory transition-energy estimates;
- critically, the paper reports preference for modeled higher-control-energy trajectories despite structurally facilitated alternatives.

Therefore:

```text
high transition activity != high transition repertoire / flexibility
```

and the preference-versus-structural-energy dissociation is **already source-derived within the neural domain**. This note must not relabel that observation as an SRT prediction.

### 1.5 Rust 2025 commentary

**Nicole Rust.** *Neuroscience needs a new paradigm: The brain is not a machine.* IAI, 2025-08-12. Source: `https://iai.tv/articles/neuroscience-needs-a-new-paradigm-the-brain-is-not-a-machine-auid-3287`.

Role: conceptual framing of feedback-rich complex dynamics, not primary evidence.

---

## 2. What the Frontiers framework already supplies

Minimal published reading:

```text
candidate policy space
+ slow constraints theta_t
+ finite control budget P_sel
-> active implementation
```

Two relevant mechanism families remain separate:

```text
Psi_f^effort ~ accumulated control input required to resist drift

Psi_f^dev ~ accumulated departure from a baseline / habitual policy
```

The new neural materials expose a neighboring construct that should not be silently folded into `Psi_f`: whether a represented option is recruited into present action-guiding competition **before** execution burden is paid.

---

## 3. Construct separation

### 3.1 Structural reachability

```text
R_struct(j | i) > 0
```

means the declared physical/computational architecture permits a route from `i` to `j`. It does not mean the bearer currently recruits that route.

### 3.2 Functional accessibility — candidate admission, not realized transition

Do **not** define accessibility as the realized one-step transition probability; that quantity is downstream of both admission and execution/payability and mechanically confounds the constructs.

Use instead:

```text
A_eff(j,t)
~ P(j enters the current action-guiding candidate set
    | S_t, h_t, theta_t, physiology/context,
      before the target transition is executed)
```

Possible readouts include a preregistered consideration-set / policy-probability admission threshold, a low-burden action-set probe, or evidence that the target becomes selectable when execution burden is experimentally minimized.

Thus:

```text
R_struct(j | i) > 0
but
A_eff(j,t) ~ 0
```

is coherent.

### 3.3 Transition friction — conditional on admission

A useful research extension is:

```text
Psi_f(i -> j | theta_t, h_t, j admitted)
```

meaning the control/execution burden of implementing an already recruited target. This is not a retroactive redefinition of the published estimand.

Experimental split:

```text
accessibility probe
-> does j enter operative competition under minimal execution burden?

friction probe
-> conditional on admission, what extra control/time/physiological burden
   is required to implement i -> j?
```

### 3.4 Currently effective candidacy

Bridge-level hierarchy:

```text
C_effective(t)
subseteq C_functionally_accessible(t)
subseteq C_structurally_reachable
```

`currently effective` inherits RC-A / P1-T06 descriptive scope language and does not create a new `live selection` object.

### 3.5 Generative reselectability

Generative reselectability is the stronger P2/P3 question of whether consequence-sensitive mismatch can revise comparison rules, candidate boundaries, or candidate-generation / reopening conditions. It is not required for every Stable ISP and is not the definition of Selection.

---

## 4. Five-stage joint model

```text
1. structural landscape
   which transitions are physically/computationally possible?

2. history-conditioned accessibility
   which routes enter action-guiding competition now?

3. executive friction
   conditional on admission, what burden is required to maintain/switch?

4. payability / execution
   can residual P_sel pay the burden?

5. historical write-back / reopening
   how do consequences reshape later admission and burden,
   and can mismatch revise the repertoire itself?
```

This is a bridge decomposition, not an anatomical serial model.

---

## 5. Depression: preserve the policy-level claim, retire only the cross-level neural gloss

The published paper's depression example is at the agent/policy level: a stable low-energy attractor in which **inaction** minimizes acute distress/friction while longer-term burden accumulates.

It does not entail:

```text
one neural CAP state -> long dwell -> low neural transition count
```

Kilic therefore pressures only that added neural interpretation. Safer joint reading:

```text
agent/policy level:
locally low acute executive friction can stabilize inaction / habitual avoidance

neural implementation level:
imbalanced transition asymmetry
+ restricted repertoire
+ recurrent state subspaces
+ state-dependent structural control burden
```

Hence:

```text
behavioral persistence != neural long dwell
transition activity != generative health
state lability != repertoire reopening
```

The direct RC-A guard is `03_Bridges/SRT_Agency_Automation_Guard_2026-08-17.md`: script / habit / gradient / `L2` automation is insufficient for stronger agency, but does **not** imply a selection-free process.

---

## 6. NCT energy != Psi_f; cross-domain comparison needs a state map

Use separate vocabularies:

```text
E_struct(n_i -> n_j)
= structural control-burden estimate over neural CAP states

Psi_f_effective(p_a -> p_b | h_t, theta_t)
= executive paid-burden construct / mechanism-family estimate over task-policy transitions
```

Do not write `E_NCT = Psi_f` or identify NCT control energy with metabolic energy actually paid by the brain.

Kilic has already observed a within-neural preference-versus-structural-energy dissociation. A **cross-domain** ordinal test becomes executable only after a preregistered mapping such as:

```text
M_state: neural CAP transition -> task/policy transition label
```

or a common task-defined event vocabulary indexing both quantities.

The mapping must declare one-to-one / many-to-one / probabilistic structure, time window, mapping uncertainty or held-out classification error, ambiguous-transition exclusion rules, and whether only ordinal or calibrated comparison is claimed.

Without this shared indexing layer, neural `E_struct` and behavioral `Psi_f` may be discussed as neighboring constructs but may not be rank-compared on nominally identical `(i,j)` labels.

P4 cross-domain hypothesis:

> after a preregistered state map, structural facilitation and independently measured executive burden may dissociate in direction, while history-conditioned candidate admission may explain held-out variance beyond structural burden alone.

---

## 7. Two kinds of knowing-doing gap

### Type I — payability failure

```text
A in C_effective(t)
Psi_f(A | admitted) > residual P_sel
```

Target remains readily recruitable when acute execution burden is lowered, but implementation fails under high burden.

### Type II — accessibility contraction

```text
A in C_represented
A notin C_effective(t)
```

The target remains reportable/represented but fails to enter operative competition; time or acute load reduction alone may be insufficient, and restoration may require reframing, relearning or a history-sensitive intervention.

This is a P4 experimental separation, not an established clinical subtype.

---

## 8. Accessibility × friction design

The factors must be manipulated/read at different stages:

| | low friction conditional on admission | high friction conditional on admission |
|---|---|---|
| high accessibility/admission | easy execution | classic payability-failure candidate |
| low accessibility/admission | suppressed option, easy once externally admitted | severe lock-in candidate |

Primary readouts:

1. target-admission probability;
2. implementation latency **conditional on admission**;
3. recovery after acute load reduction;
4. post-probe hysteresis;
5. transfer to a novel structurally analogous option;
6. future arrival-distribution / reachable-policy change.

A valid design must verify that the accessibility manipulation affects admission more than conditional execution cost, and that the friction manipulation affects conditional execution burden more than admission. Failure of this orthogonality check makes the 2×2 uninterpretable.

---

## 9. Activity is not repertoire

Theory-neutral readout:

```text
H_T(i) = - sum_j p_ij log p_ij
R_eff(i) = exp(H_T(i))
```

Use rule:

```text
R_eff = descriptive transition-repertoire proxy
!= d-value
!= Stable ISP
!= Selection count
!= generative reselectability
```

---

## 10. State change != landscape change != generative revision

```text
Level A: state displacement
external perturbation -> current state changes

Level B: landscape / repertoire change
intervention -> admission / transition probabilities change persistently

Level C: generative reselectability candidate
new mismatch -> same history-bearing process revises comparison/reopening conditions
```

NEURAL35 already supplies the neighboring guard `reopening != reselectability`.

---

## 11. Rival-theory requirement

Feedback, attractors, persistent states, history dependence, hysteresis, restricted repertoire, precision dominance and transition-cost asymmetry are not unique SRT evidence.

At minimum compare:

```text
M0 ordinary dynamical / transition model
M1 history-aware recurrent RL / metaplastic model
M2 richer active-inference / predictive-processing model
   (learned transitions, temporal depth, precision, priors, history)
M3 SRT bridge model adding explicit same-bearer consequence return
   and future-effective-candidate loss / reopening
```

Required negative result:

```text
if M2 explains the held-out history, hysteresis, recovery,
candidate suppression and reopening effects under matched complexity/refit budgets,
and M3 adds no predictive or intervention gain,
-> SRT-specific bridge contribution is dispensable for this target
```

Do not relabel a successful rival mechanism as `Psi_f`, `L2` or reselectability after the fact.

---

## 12. Relation to `history_dependent_reachability`

`papers/history_dependent_reachability/` already supplies a designed-system identification battery:

```text
exact present-state matching
+ master-yoked control
+ external-action sham
+ selection-specific write-back
+ calibration -> freeze -> fresh-seed discipline
```

Its scope is binding: results are constructive demonstrations in designed models, **not facts about natural systems**. The retained prediction-error NO-GO — where a yoked agent reproduces the future effect — is especially relevant because generic history dependence is not selection-specific write-back.

Human/neural translation therefore additionally requires:

1. preregistered neural-state ↔ task/policy-state mapping when cross-domain comparison is attempted;
2. independently measured candidate-admission readout;
3. perturbational or quasi-experimental separation of own action→consequence coupling from generic exposure history;
4. longitudinal evidence that any history-dependent remainder changes later reachability after the observable present is matched as far as feasible.

The neuroscience cluster should feed this identification program rather than create a parallel construct family.

---

## 13. Matched-present / different-history extension

Compare histories with matched immediate loss but different same-bearer future consequences:

```text
History A:
failure -> immediate loss -> full reset

History B:
failure -> same immediate loss
        -> persistent change to later sensing/action/recovery/reachable policies
```

At test, match current environment, fast policy, reward structure and acute sensory noise as far as feasible, then introduce a novel mismatch and measure candidate admission/reopening latency, repertoire, hysteresis, future arrival distribution and transfer to novel goals.

The question is not whether this proves SRT, but whether same-bearer consequence history leaves a future-effective remainder after ordinary present-state variables are matched.

---

## 14. SAME vs COPY — copy-completeness audit only

A deterministic digital system copied completely — including every future-relevant state variable, identical environment coupling and identical RNG stream — should satisfy `SAME = COPY` by construction. If the copy is incomplete, `SAME != COPY` may be explained trivially by omitted state.

Therefore predeclare a copy inventory:

```text
copied:
- fast policy/value state
- slow memory/latent state
- optimizer/adaptation state
- replay/episodic buffer
- RNG state or seed policy

held fixed:
- environment state
- observation stream
- reward/task specification

intentionally not copied, if any:
- continuous body/environment coupling
- accumulated wear/resource state outside the controller vector
- declared relational state constitutive of the bearer model
```

A difference caused by a declared non-copied coupling identifies that coupling as causally relevant; it does not establish subjecthood or a metaphysically non-copyable residue.

---

## 15. Clinical and treatment guard

```text
symptom reduction
!= state displacement
!= landscape change
!= repertoire reopening
!= generative reselectability
```

A treatment may lower friction for an already accessible action without reopening suppressed candidates; conversely, a perturbation may broaden accessibility while weakening stable re-anchoring. Clinical claims require longitudinal evidence, nuisance controls and the neuroscience claim-status guardrail.

---

## 16. RC-A / P1 inheritance

Direct guard:

```text
script / habit / gradient / L2 automation
is not sufficient for stronger agency
and does not imply a selection-free process
```

Higher-level separation:

```text
Selection != Agency
```

P1-T06 retains the Stable ISP minimum — same perspective/history-bearing process, recurrent currently effective non-equivalent candidates, write-back and continued selectability. Generative reselectability remains P2/P3.

Neural transition count is not a Selection count.

---

## 17. Landing map and non-actions

Relevant existing files:

- `papers/ontological_friction/paper_ontological_friction.md`
- `papers/history_dependent_reachability/manuscript/MANUSCRIPT.md`
- `Core/SRT_Core_21b_Constitutive_Theorems.md`
- `Core/SRT_Core_21c_Bridge_Hypotheses.md`
- `03_Bridges/SRT_Agency_Automation_Guard_2026-08-17.md`
- `Core/SRT_Core_12b_Ontology_L2.md`
- `SRT_Fisher_FEP_Landscape_Interface.md`
- `Neuroscience/INTEROCEPTIVE_PRECISION_SRT_BRIDGE.md`
- `Neuroscience/hooks/NEURAL35_Psychedelic_Reopening_Reanchoring_Integration_Hook.md`

Explicit non-actions:

```text
no P0/P1 edit
no neuroscience compact-core synthesis
no published Frontiers rewrite
no clinical treatment-mechanism promotion
```

---

## 18. Candidate next-paper direction

> **From Executive Friction to Effective Choice Landscapes: Distinguishing Transition Cost, Accessibility, and History-Dependent Reachability**

Useful contribution:

```text
structural reachability
functional candidate admission / accessibility
transition friction / payability
```

plus the longitudinal question:

```text
does mismatch merely change the current state,
or change which alternatives can become effective candidates next?
```

The line must be allowed to fail if standard recurrent / active-inference rivals explain the complete result under matched complexity and held-out testing.

---

## 19. Retained conclusions

1. The published Frontiers paper remains compatible with recent neural-dynamics evidence.
2. Do not retire its agent-level depression claim; retire only the overstrong neural long-dwell gloss.
3. Kilic already provides a within-neural preference-versus-structural-energy dissociation.
4. NCT energy is not `Psi_f`.
5. Cross-domain rank comparison requires an explicit neural ↔ task/policy state map.
6. Accessibility is pre-execution candidate admission, not realized transition probability.
7. Represented option != effective candidate; payability failure and accessibility contraction are experimentally separable candidates.
8. High transition activity != high repertoire.
9. State escape != landscape revision != generative reselectability.
10. HDR is a designed-system identification framework, not natural-system evidence.
11. SAME/COPY is interpretable only after a copy-boundary inventory.
12. Unique SRT value is not established; richer dynamical, RL, predictive-processing and active-inference rivals must be allowed to absorb the result.

**Disposition**: retain as post-publication convergence / experiment-design bridge. No P0/P1 promotion.
