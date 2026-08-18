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
tags:
  - Executive Friction
  - Psi_f
  - Reachability
  - Accessibility
  - Effective Candidacy
  - Attractor Dynamics
  - Depression
  - Generative Reselectability
  - Post-publication Convergence
---

# Post-publication convergence: executive friction, transition landscapes, and history-dependent reachability

> **Status / use rule**: This is a post-publication research and bridge note. It does **not** amend the published Frontiers article, add a new P0/P1 theorem, or establish a clinical mechanism. It records how several 2024–2026 neural-dynamics results can be jointly analyzed with the published executive-friction framework and with the repository's current RC-A / ST-A semantics.

## 0. Executive verdict

The published Frontiers framework and the recent attractor / state-transition literature are compatible, but they answer different questions.

```text
neural dynamics / attractor work
-> which states and transition patterns are dynamically supported?

executive friction (Psi_f)
-> how costly is it to maintain or execute a transition relative to current defaults and resources?

history-dependent reachability / SRT bridge
-> how does the same history-bearing process acquire a different future effective candidate set,
   and can mismatch later reopen or revise that set?
```

The principal post-publication refinement is therefore **not**:

```text
attractor = L2
NCT energy = Psi_f
persistent state = Stable ISP
rigid / automated process = no Selection
```

The useful distinction is:

```text
Structural Reachability
!= Functional Accessibility
!= Transition Friction
!= Currently Effective Candidacy
!= Generative Reselectability
```

The strongest immediate implication for the published depression example is that MDD should not be modeled only as occupancy of one static "low-energy attractor." A more general and empirically safer reading is an **imbalanced, history-conditioned transition landscape** in which abundant state transitions can coexist with a narrowed effective transition repertoire.

No canonical edit is required by this note.

---

## 1. Source cluster and evidence roles

### 1.1 Published anchor: Zhang 2026, Frontiers in Neuroscience

**Yuxin Zhang.** *A translational cross-modal control-cost framework for executive breakdown.* Frontiers in Neuroscience 20 (2026). DOI: `10.3389/fnins.2026.1837760`.

Publication date: 2026-08-06. Article type: Hypothesis and Theory. No new empirical dataset is reported.

Load-bearing published claims relevant here:

1. `Psi_f` is operationally estimated as a cross-modal latent control/execution-cost factor.
2. Candidate mechanistic models include accumulated control effort and departure from a habitual/default policy; these are rival/related mechanisms rather than universal identities.
3. `P_sel` is the available control budget proxy.
4. The knowing-doing gap appears when implementation cost exceeds remaining control capacity despite an intact representation of the appropriate action.
5. Slow constraints — habits, priors, hyperpriors, trait-like limits — shape future selections.
6. Slow embodiment parameters may change through learning, friction-landscape change, and homeostatic recoil.

**Boundary**: The paper does not claim that `Psi_f` is a complete theory of candidate accessibility, nor that every unexecuted represented action is still an effective candidate in the same operational sense.

### 1.2 Vinograd et al. 2024, Nature

**Vinograd et al.** *Causal evidence of a line attractor encoding an affective state.* Nature (2024). DOI: `10.1038/s41586-024-07915-x`.

Empirical role:

- provides causal perturbational evidence that an affect-related neural population can exhibit line-attractor dynamics;
- on-manifold stimulation can be integrated along the attractor;
- off-manifold perturbation relaxes back toward the attractor.

SRT / friction use:

```text
causal neural-state persistence / attraction exists
-> implementation-level support for state-landscape reasoning
!= evidence that attractor = L2 / Selection / subjecthood
```

### 1.3 Kauvar et al. 2025, Science

**Kauvar et al.** *Conserved brain-wide emergence of emotional response from sensory experience in humans and mice.* Science 388(6750) (2025): eadt3971. DOI: `10.1126/science.adt3971`.

Empirical role:

- emotionally salient sensory signals show a fast brain-wide broadcast followed by a slower persistent distributed pattern;
- pharmacological manipulations can selectively attenuate the persistent component while largely preserving the fast sensory broadcast and reducing the corresponding emotional response.

Useful separation:

```text
sensory event detected / broadcast
!= persistent affective context formed
```

This is an implementation-level temporal-stage result. Persistent neural context is not by itself an SRT `L2`, Stable ISP, or consciousness criterion.

### 1.4 Kilic et al. 2026, Nature Communications

**Kilic et al.** *Spatiotemporal asymmetries on brain energy landscape uncover system entrapment related to depression severity.* Nature Communications (2026). DOI: `10.1038/s41467-026-71961-4`.

Empirical role:

- 7T resting-state fMRI was analyzed in 38 MDD and 38 healthy-control participants;
- a DWI subset contained 26 MDD and 27 healthy-control participants;
- MDD participants showed higher entry/exit probabilities for one state and elevated fractional occupancy despite shorter dwell time;
- some transitions (e.g. State 3 <-> State 2) were increased while others (State 4 <-> State 1) were reduced;
- the study combines empirical co-activation-pattern transitions with Network Control Theory (NCT) transition-energy estimates and describes depression-related system-entrapment signatures.

Key implication for this note:

```text
high transition count
!= high transition repertoire / flexibility
```

The result supports replacing a simplistic single-static-basin picture with an **imbalanced transition-field** picture.

### 1.5 Nicole Rust 2025, IAI commentary

**Nicole Rust.** *Neuroscience needs a new paradigm: The brain is not a machine.* IAI, 2025-08-12.

Role: conceptual commentary / synthesis, not primary empirical evidence.

Useful framing:

```text
brain -> mood / motivation / decisions
-> experience / learning
-> changed brain
```

The commentary is valuable as an entry point to the complex-systems framing, but the primary evidential weight in this cluster should remain with the peer-reviewed studies above.

---

## 2. What the published Frontiers paper already provides

The Frontiers framework defines a resource-bounded mapping from a candidate policy space into an active state under slow constraints and finite embodiment parameters.

A minimal reading is:

```text
candidate policy space Pi(t)
+ slow constraints theta_t
+ finite control budget P_sel
-> selected / active implementation
```

Executive friction is then the cost of maintaining or reconfiguring that active state relative to default drift or habitual policy.

Two mechanism families are deliberately separated:

### 2.1 Control-effort family

Conceptually:

```text
Psi_f^effort ~ accumulated control input required to resist uncontrolled drift
```

### 2.2 Default-deviation family

Conceptually:

```text
Psi_f^dev ~ accumulated divergence from a baseline / habitual policy
```

with a local Fisher approximation permitted only under the declared regularity conditions.

The published paper's knowing-doing gap can therefore be summarized as:

```text
appropriate action is represented
+
implementation / switching friction is high
+
remaining P_sel is insufficient
-> execution fails
```

The new materials do not invalidate this mechanism. They expose a neighboring construct that should not be silently folded into `Psi_f`: **whether the represented action is currently functionally accessible enough to enter operative competition at all.**

---

## 3. Post-publication construct separation

### 3.1 Structural reachability

A state or policy is structurally reachable when the physical / computational architecture permits a path to it.

Conceptual readout:

```text
R_struct(j | i) > 0
```

Examples include graph-theoretic reachability and NCT-based structural transition models.

Structural reachability answers:

> Is there a physically/model-supported route from current state `i` to state `j`?

It does not answer whether the current bearer can readily recruit that route now.

### 3.2 Functional accessibility

Functional accessibility is history- and state-conditioned ease of entering a structurally available state:

```text
A_eff(j,t)
~ P(S_{t+1}=j | S_t, h_t, theta_t, current physiology/context)
```

A state may therefore be structurally reachable while functionally suppressed:

```text
R_struct(j | i) > 0
but
A_eff(j,t) ~ 0
```

### 3.3 Transition friction

For the published framework, a useful post-publication notation is:

```text
Psi_f(i -> j | theta_t, h_t)
```

meaning the effective control / execution burden of actually traversing from current active state `i` toward `j`, conditional on the current embodiment and history.

This notation is a **research extension**, not a retroactive redefinition of the published estimand.

### 3.4 Currently effective candidacy

A represented option should not automatically be treated as a currently effective candidate.

Bridge-level distinction:

```text
C_effective(t)
subseteq C_functionally_accessible(t)
subseteq C_structurally_reachable
```

`currently effective` is inherited as descriptive scope language from RC-A / P1-T06. It does **not** create a new `live selection` object.

An option may be:

```text
represented / verbally reportable
but
not sufficiently accessible to enter present action-guiding competition
```

This distinction provides a new way to subdivide the knowing-doing gap.

### 3.5 Generative reselectability

Generative reselectability is the stronger P2/P3 question of whether consequence-sensitive mismatch can revise the process's own comparison rules, candidate boundaries, or candidate-generation / reopening conditions.

It is **not** required for every Stable ISP and must not be promoted into the definition of Selection.

---

## 4. A revised five-stage joint model

The combined framework can be expressed as:

```text
1. Structural landscape
   Which transitions are physically / computationally possible?

2. History-conditioned accessibility
   Which of those routes are presently recruitable under h_t and theta_t?

3. Executive friction
   For an accessible target, what burden must be paid to maintain / switch into it?

4. Effective candidacy and execution
   Which routes enter current operative competition, and can P_sel pay the selected transition?

5. Historical write-back / reopening
   How do consequences reshape future accessibility and transition burden,
   and can later mismatch revise the repertoire itself?
```

Compact form:

```text
structure
-> accessibility
-> friction / payability
-> execution
-> history write-back
-> changed future accessibility
```

This is a bridge decomposition. No claim is made that these stages are anatomically serial modules.

---

## 5. Depression: from a single low-energy attractor to an imbalanced transition field

The original Frontiers discussion used a stable low-energy attractor intuition for depression. The Kilic 2026 results motivate a more general formulation.

### 5.1 What should be retired as the default reading

Avoid treating the clinical picture as necessarily:

```text
one deep state
-> long dwell
-> low movement
```

### 5.2 Safer updated reading

Use:

```text
history-conditioned transition asymmetry
+
restricted effective repertoire
+
locally recurrent state subspaces
+
state-dependent transition burdens
```

A system may show:

```text
many transitions
+
frequent exits and re-entries
+
strong pathology
```

while still having:

```text
low effective transition diversity
```

Therefore:

```text
transition activity != generative health
state lability != repertoire reopening
```

This also blocks the inference:

```text
habit / recurrent loop / L2 automation
-> no Selection
```

RC-A explicitly preserves the separation `Selection != Agency`.

---

## 6. NCT transition energy must not be identified with Psi_f

The Kilic paper's Network Control Theory quantity is a modeled control input required to drive a structural-network system between states under the chosen linear control assumptions.

Do **not** write:

```text
E_NCT = Psi_f
```

or:

```text
NCT control energy = metabolic energy actually paid by the brain
```

The useful comparison is instead:

```text
E_struct(i -> j)
= domain-specific structural control-burden estimate

Psi_f_effective(i -> j | h_t, theta_t)
= cross-modal / executive paid-burden construct or mechanism-family estimate
```

A particularly informative empirical possibility is a dissociation:

```text
E_struct(i -> C) < E_struct(i -> B)
while
Psi_f_effective(i -> C | h_t) > Psi_f_effective(i -> B | h_t)
```

Interpretation:

> a route can be structurally cheaper yet functionally / historically harder for the present bearer to recruit.

This is exactly the kind of dissociation that can give the history-dependent layer empirical content without redefining anatomy or control theory as SRT primitives.

---

## 7. Two kinds of knowing-doing gap

### Type I — Payability failure

The target remains a currently effective candidate:

```text
A in C_effective(t)
```

but:

```text
Psi_f(A) > residual P_sel
```

Predicted signature:

- target action remains rapidly recruitable when immediate burden is lowered;
- reducing concurrent load or noise, increasing recovery, or simplifying switching demands should restore performance comparatively quickly;
- no prolonged retraining is required merely to make the option operative again.

This is the cleanest continuation of the published executive-friction model.

### Type II — Accessibility contraction

The target remains represented:

```text
A in C_represented
```

but is weak or absent from current operative competition:

```text
A notin C_effective(t)
```

Predicted signature:

- simply increasing time or lowering immediate load may be insufficient;
- contextual reframing, relearning, prolonged intervention, or history-sensitive perturbation may be required to restore access;
- recovery should show stronger hysteresis and transfer dependence.

### Boundary

`Type II` is not yet an established clinical subtype. It is a P4 experimental separation to test whether executive friction and candidate accessibility can be empirically dissociated.

---

## 8. A minimal 2 x 2 experimental separation

Freeze two factors independently:

| | Low transition friction | High transition friction |
|---|---|---|
| **High functional accessibility** | ordinary easy execution | classic knowing-doing / payability failure candidate |
| **Low functional accessibility** | candidate suppression / automatic exclusion candidate | severe lock-in candidate |

Primary readouts should include:

1. switch latency;
2. probability that the target option enters the action set;
3. recovery after acute load reduction;
4. post-probe hysteresis;
5. transfer to a novel but structurally analogous option;
6. future reachable-policy / arrival-distribution change.

Do not infer `d-value`, consciousness, agency, or moral standing from any cell of this design.

---

## 9. Repertoire metrics: activity is not flexibility

A simple empirical readout for transition diversity can be kept theory-neutral.

For transition probabilities `p_ij` from current state `i`:

```text
H_T(i) = - sum_j p_ij log p_ij
```

and an optional effective repertoire count:

```text
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

This captures an important Kilic-compatible pattern:

```text
high number of transitions
+
low transition entropy
-> active but narrow loop
```

---

## 10. State change, landscape change, and generative revision

Therapeutic or experimental perturbations should be separated into at least three levels.

### Level A — State displacement

```text
external perturbation
-> current state changes
```

If the perturbation is removed and the system returns immediately to the old loop, this is not evidence of landscape revision.

### Level B — Landscape / repertoire change

```text
intervention
-> transition probabilities / accessibility change persistently
```

Previously suppressed alternatives become more accessible after the intervention.

### Level C — Generative reselectability candidate

```text
new mismatch
-> same history-bearing process can revise comparison / reopening conditions
-> adaptive alternatives become effective without replaying a fixed externally supplied script
```

Hard guard:

```text
state escape
!= landscape revision
!= generative reselectability
```

This is consistent with `Core/SRT_Core_21c_Bridge_Hypotheses.md P2/P3-B13` and with the NEURAL35 reopening / re-anchoring guard.

---

## 11. Rival-theory requirement

None of the following, by itself, establishes unique SRT explanatory value:

```text
feedback
attractors
persistent neural states
history dependence
hysteresis
restricted state repertoire
precision dominance
transition-cost asymmetry
```

These can be modeled by ordinary dynamical systems, recurrent reinforcement learning, control theory, predictive processing, and richer active-inference models.

The correct model-comparison stack is at least:

```text
M0: ordinary dynamical / transition model
M1: history-aware recurrent RL / metaplastic model
M2: richer active-inference / predictive-processing model
    (learned transitions, temporal depth, precision, priors, history)
M3: SRT bridge model adding explicit same-bearer consequence return
    and future-effective-candidate loss / reopening
```

### Negative result that SRT must accept

If `M2` predicts the relevant history, hysteresis, recovery, candidate suppression, and reopening effects under frozen complexity / refit budgets, while `M3` adds no held-out predictive or intervention gain, then record:

```text
SRT-specific bridge contribution dispensable for this target
```

Do not relabel the rival mechanism as `Psi_f`, `L2`, or reselectability after the fact.

---

## 12. Direct bridge to `history_dependent_reachability`

The repository already contains:

```text
papers/history_dependent_reachability/
```

whose manuscript asks whether two systems matched in their observable present can nevertheless differ in future behavioral reachability because a slow history-formed memory survives the matching boundary.

That work already provides the more rigorous identification battery needed here:

```text
exact present-state matching
+
master-yoked controls
+
external-action sham
+
selection-specific write-back
+
fresh-seed / frozen-threshold discipline
```

This post-publication neuroscience cluster should therefore **feed that identification program rather than create a parallel construct family**.

Recommended translation:

```text
Frontiers Psi_f
-> transition-burden / payability axis

Kilic / Vinograd / Kauvar
-> empirical neural-dynamics existence and dissociation cases

history_dependent_reachability
-> causal-identification framework for whether history changes future reachability

RC-A / ST-A / B13
-> semantic guards separating Selection, Stable ISP, agency and generative reselectability
```

---

## 13. Stronger matched-present / different-history test

A useful next experiment is to match the present while varying the consequence structure of the history.

### History A — resettable consequence

```text
failure
-> immediate loss
-> complete reset
-> no persistent loss of future sensing / action / recovery capacity
```

### History B — same-bearer persistent consequence

Match immediate reward magnitude, but let failure alter the same agent's later capacity:

```text
failure
-> sensor fidelity down
and/or action options down
and/or recovery capacity down
and/or later reachable policies down
```

At the test point, match as much current state as possible:

```text
same observable environment state
same fast values / initial policy distribution
same current reward structure
same acute sensory noise
```

Then introduce a novel mismatch and measure:

```text
candidate reopening latency
transition repertoire
post-mismatch hysteresis
future arrival distribution
transfer to novel goals
```

The purpose is not to prove SRT. It is to ask whether **same-bearer consequence history leaves a future-effective remainder after ordinary present-state variables are matched**.

---

## 14. Same-bearer vs copied-state control

A harder identity / continuity control can be added in artificial systems.

```text
SAME:
history-bearing process P_t continues into P_(t+1)

COPY:
all explicitly copyable internal state is transferred to a fresh bearer P'_(t+1)
```

If:

```text
SAME = COPY
```

for all future-reachability readouts, the alleged bearer-continuity effect is likely reducible to ordinary copyable state variables in that model.

If:

```text
SAME != COPY
```

under well-controlled state matching, the next task is not to declare subjecthood, but to identify the residual continuous consequence structure and test whether it survives alternative mechanistic explanations.

This is a P4 identification strategy only.

---

## 15. Treatment interpretation guard

For depression and other clinical applications, distinguish:

```text
symptom reduction
!= state displacement
!= basin / transition-landscape change
!= effective repertoire reopening
!= generative reselectability
```

A successful treatment may lower `Psi_f` for an already accessible action without reopening previously suppressed candidates.

Conversely, a perturbation may broaden accessibility while weakening stable action-guiding re-anchoring. NEURAL35 already guards:

```text
reopening != reselectability
```

Clinical claims require longitudinal evidence, nuisance controls, ethics / clinical collaboration, and the folder-level neuroscience claim-status guardrail.

---

## 16. Relation to RC-A and current P1 boundaries

This note inherits the 2026-08-17 RC-A decision:

```text
Selection != Agency
script / habit / gradient / L2 automation
!= selection-free by inference
```

Therefore an MDD-related recurrent loop may contain abundant transitions and abundant Selection while remaining poor evidence for stronger agency / generative revision standing.

P1-T06 retains only the Stable ISP minimum:

```text
same perspective-bearing, history-bearing process
+
recurrent currently effective non-equivalent candidates
+
write-back
+
continued selectability
```

Generative reselectability remains P2/P3 and must not be retrofitted as a necessary condition for every Stable ISP.

---

## 17. Repository landing map

### Directly relevant existing files

- `papers/ontological_friction/paper_ontological_friction.md` — repository manuscript lineage for the published executive-friction work.
- `papers/history_dependent_reachability/manuscript/MANUSCRIPT.md` — matched-present / different-future identification framework.
- `Core/SRT_Core_21b_Constitutive_Theorems.md` — RC-A P1 boundaries, especially former P1-T05 and current P1-T06.
- `Core/SRT_Core_21c_Bridge_Hypotheses.md` — ST-A / generative reselectability at P2/P3-B13.
- `03_Bridges/SRT_Agency_Automation_Guard_2026-08-17.md` — automation is not sufficient for stronger agency, but does not imply no Selection.
- `Core/SRT_Core_12b_Ontology_L2.md` — path dependence, hysteresis, scaffold formation, and L2 hardening guardrails.
- `SRT_Fisher_FEP_Landscape_Interface.md` — landscape / Fisher / FEP non-identity guard.
- `Neuroscience/INTEROCEPTIVE_PRECISION_SRT_BRIDGE.md` — rival-model and subtractive-audit discipline against richer active inference.
- `Neuroscience/hooks/NEURAL35_Psychedelic_Reopening_Reanchoring_Integration_Hook.md` — reopening versus reselectability / re-anchoring guard.

### Explicit non-actions

This note does **not** authorize immediate edits to:

```text
P0/P1 canonical core
Neuroscience compact-core owners
clinical treatment claims
published Frontiers text
```

The neuroscience owner remains subject to the repository's synthesis-target freeze. If a later reactivation gate fires, this note may be used as a source for a governed synthesis pass.

---

## 18. Candidate next-paper framing

A possible future paper line is:

> **From Executive Friction to Effective Choice Landscapes: Distinguishing Transition Cost, Accessibility, and History-Dependent Reachability**

The academically useful contribution would not be to restate SRT ontology. It would be to separate and experimentally identify three often-confounded constructs:

```text
structural reachability
functional accessibility
effective transition friction / payability
```

and then ask a stronger longitudinal question:

```text
does mismatch merely change the current state,
or does it change which alternatives can become effective candidates next?
```

The paper should be allowed to fail if standard recurrent / active-inference models explain the full result under matched complexity and held-out testing.

---

## 19. Minimal retained conclusions

1. **The Frontiers paper remains compatible with recent neural-dynamics evidence.** Its main construct is a transition / execution burden under finite control resources, not a complete candidate-accessibility theory.
2. **The depression example should be generalized.** Prefer an imbalanced, history-conditioned transition landscape over a mandatory single low-energy attractor.
3. **NCT energy is not `Psi_f`.** Structural control-energy estimates are domain-specific proxies / comparators, not cross-modal executive friction or actual metabolic payment.
4. **Represented option != effective candidate.** This creates a testable split between payability failure and accessibility contraction.
5. **High transition activity != high repertoire.** A system can change frequently while remaining trapped in a narrow subspace.
6. **State escape != landscape revision != generative reselectability.** The latter remains a stronger P2/P3 criterion.
7. **The strongest repository route is through the existing history-dependent-reachability identification program, not through new canonical primitives.**
8. **Unique SRT value is not yet established.** Rich dynamical, RL, predictive-processing, and active-inference rivals must be frozen and allowed to absorb the result.

**Disposition**: retain as post-publication convergence / experiment-design bridge. No P0/P1 promotion. No clinical mechanism claim. No immediate neuroscience-owner synthesis.
