---
id: SRT-CORE-24-DISCRIMINATING-PREDICTIONS
type: prediction_module
tags: [SRT, Core 24, Discriminating Predictions, Falsification, Ψ_f, d-value, L2, Normativity]
status: draft_v1
layer: core_bridge
epistemic_layer: theory_hardening
claim_mode: bridge_prediction
created: 2026-04-27
dependency: [SRT-CORE-24-FLOOR-NORMATIVITY-VERIFICATION, SRT-CORE-24-CANONICAL-MERGE-DRAFT, SRT-CORE-12B, SRT-D-VALUE-CANONICAL, SRT-PSIF-CANONICAL, SRT-EXP-MEASUREMAP, SRT-OPEN-TENSIONS]
---

# SRT Core 24 — Discriminating Predictions

> **Purpose**: This file turns Core 24 from a framing / defense layer into a discriminating prediction layer.
>
> It asks: if SRT is correct, what should be observed that would not be equally predicted by FEP, predictive processing, reinforcement learning, IIT/GNW, social construction theory, or ordinary habit theory?

---

## 0. Prediction Rule

A Core 24 prediction counts as useful only if it satisfies four conditions:

1. **Specificity**: it names a measurable pattern, not only a philosophical interpretation.
2. **Contrast**: it states what a neighboring theory would predict differently or leave unspecified.
3. **Operationalization**: it identifies proxy classes that could test the pattern.
4. **Failure condition**: it states what would weaken or falsify the SRT bridge claim.

Core 24 predictions should not be defended by saying “SRT explains this too.” They must show where SRT expects a different structure.

---

## 0b. Modification Discipline（修正/压力/失败；2026-07-05 Q26 backflow）

When a prediction in this file fails or is challenged, the response must be classified **before** any rewrite:

1. **Repair（修正）**: a local expression was imprecise; correcting it leaves the load-bearing claim untouched.
2. **Pressure（压力）**: an edge case demands higher resolution; the claim survives but gains explicit scope conditions.
3. **Failure（失败）**: the load-bearing criterion itself is systematically broken; the bridge claim must be withdrawn, not patched.

Two standing gates:

- **Progressive-vs-degenerative gate**: a modification made in response to a counterexample is admissible only if it adds independently testable content (new predictions, sharper proxies). A modification that only makes the old prediction vaguer or harder to refute is degenerative and must be recorded as such, not presented as refinement.
- **External-judge gate**: every prediction and failure condition in this file must remain operationalizable by researchers who do not use SRT vocabulary. "You don't understand the theory" is not an admissible defense against an operationalized counter-result.

**Provenance / level**: governance-grade validation rule, registered from book chapter Q26 §2/§5 (Lakatos-style progressive/degenerative distinction) so the theory layer carries the discipline independently of the book. The book is provenance, not authority.

---

## 1. Prediction P24-1 — Non-Monotonic Selection Friction During New Reality Formation

### SRT prediction

When a system forms a genuinely new selection path rather than merely optimizing within an existing frame, `Ψ_f` should show a **non-monotonic trajectory**:

```text
early phase: Ψ_f rises or becomes volatile
transition phase: representational / policy competition increases
hardening phase: Ψ_f falls as a new L₂ scaffold forms
```

This pattern should occur in learning, reframing, skill acquisition, institutional transition, norm formation, and potentially AI agent-policy restructuring.

### Why this is SRT-specific

SRT distinguishes:

- optimization inside an already stabilized `L_2` frame;
- formation of a new `L_1 -> L_2` path.

A new path is not expected to simply reduce cost immediately. It may first increase selection friction because the system must hold competing possibilities open before a new closure becomes scaffolded.

### Contrast with adjacent theories

| Theory | Expected tendency | SRT contrast |
|---|---|---|
| FEP / predictive processing | prediction error / free energy should tend toward reduction under successful adaptation | SRT predicts a possible early friction rise before later hardening decline |
| RL | value or policy improves with reward-driven learning, often tracked by reward/loss curves | SRT tracks transition friction, not reward alone |
| ordinary habit theory | repetition lowers cost | SRT predicts a prior destabilizing / high-friction phase before habit-like cost reduction |
| IIT / GNW | integration or access may change but does not by itself predict the friction trajectory | SRT predicts the dynamic path of selection cost |

### Operational proxies

- task-switching cost;
- reaction-time volatility;
- error volatility;
- recovery half-life after perturbation;
- representational competition / embedding instability;
- Fisher spectrum spikes;
- update path length;
- policy entropy or action-distribution instability;
- social coordination cost before norm stabilization.

### Minimal experimental design

Use a task requiring either:

1. ordinary optimization inside a fixed frame; or
2. reframing into a new rule / category / norm.

SRT predicts the reframing condition should show a stronger early friction spike or volatility, followed by sharper later cost reduction if hardening succeeds.

### Failure condition

If genuinely new frame formation always shows monotonic cost reduction indistinguishable from ordinary optimization or habit learning, P24-1 weakens.

---

## 2. Prediction P24-2 — d-value Predicts Non-Substitutability Beyond Reward or Preference

### SRT prediction

Selections with high `d-value` should show **concern-weighted non-substitutability**:

```text
high d-value selection
→ persists under reward reduction
→ reorganizes downstream choices
→ resists cheap substitution
→ produces structural disturbance when blocked
```

This should be distinguishable from ordinary preference strength, salience, reward history, or self-report intensity.

### Why this is SRT-specific

SRT treats value not as reward or preference intensity, but as non-substitutability under consequence return. A selection matters when losing or replacing it changes the system's future selection capacity, identity-continuity, or closure structure.

### Contrast with adjacent theories

| Theory | Expected tendency | SRT contrast |
|---|---|---|
| RL | behavior should track expected reward or learned value | SRT predicts persistence and reorganization even when reward is reduced or absent |
| salience / attention theories | high salience captures attention | SRT requires cost-bearing and consequence return, not attention alone |
| preference theory | strong preference predicts choice | SRT predicts non-substitutability and downstream restructuring beyond stated preference |
| FEP / active inference | prior preference or expected free energy may model persistence | SRT specifically predicts identity / future-selectability reorganization when blocked |

### Operational proxies

- persistence after reward removal;
- willingness to bear cost;
- substitution refusal despite equivalent reward;
- downstream choice reorganization;
- identity-continuity disturbance;
- recovery burden after blockage;
- cross-session stability;
- consequence-return markers.

### Minimal experimental design

Compare two choices matched for reward and self-reported preference, but differing in predicted non-substitutability.

Manipulate:

1. reward removal;
2. substitution offer;
3. blockage or forced replacement;
4. delayed consequence return.

SRT predicts the high-d selection should reorganize broader behavior and recovery dynamics more strongly than the reward-matched low-d selection.

### Failure condition

If `d-value` proxies cannot predict non-substitutability better than reward, preference, salience, pain, or self-report intensity, P24-2 weakens.

---

## 3. Prediction P24-3 — L₂ Hardening Has a Triple Signature, Not Mere Memory Strength

### SRT prediction

A structure counts as `L_2` hardening only when three signatures co-occur:

```text
reduced local selection cost
+ increased global constraint
+ hysteresis under perturbation
```

The first signature alone is not enough. A learned memory or habit may lower local cost, but an `L_2` scaffold also constrains future available paths and shows hysteresis when disrupted.

### Why this is SRT-specific

SRT treats hardening as a transition from selected event to background scaffold. That transition is not merely recall strength, repetition, or performance improvement. It is a change in the system's future possibility structure.

### Contrast with adjacent theories

| Theory | Expected tendency | SRT contrast |
|---|---|---|
| ordinary memory theory | stronger memory improves recall or performance | SRT requires global constraint and hysteresis, not recall alone |
| habit theory | repetition lowers action cost | SRT requires future path narrowing / scaffolding effects |
| social construction theory | shared agreement stabilizes social reality | SRT adds measurable selection-cost and hysteresis signatures |
| FEP / predictive processing | stable priors reduce prediction error | SRT distinguishes local cost reduction from global constraint increase |

### Operational proxies

- local reaction-time or effort reduction;
- narrowing of alternative choices;
- increased switching penalty away from the scaffolded path;
- perturbation recovery lag;
- path-dependence after attempted reversal;
- norm violation backlash;
- social re-coordination cost;
- cross-agent replication.

### Minimal experimental design

Train or induce a repeated selection path, then test:

1. whether local execution cost decreases;
2. whether alternative path access narrows;
3. whether perturbation produces hysteresis rather than simple reset.

SRT predicts true hardening only when all three are present.

### Failure condition

If `L_2` hardening cannot be distinguished from ordinary memory, learned habit, convention, or environmental stability, P24-3 weakens.

---

## 4. Prediction P24-4 — Frameworks Alter Visibility and Cost Before Explicit Belief Change

### SRT prediction

A framework does not merely interpret already-present facts. It preconfigures what is visible, selectable, costly, and admissible. Therefore a framework shift should change:

```text
option visibility
+ perceived admissibility
+ selection friction
before or beyond explicit belief endorsement
```

### Why this is SRT-specific

SRT treats frameworks as partial parameterizations of `Ĝθ`, not merely as post-hoc descriptions. A framework can alter the selection field before subjects explicitly report a changed belief.

### Contrast with adjacent theories

| Theory | Expected tendency | SRT contrast |
|---|---|---|
| belief-change models | explicit belief shift drives later behavior | SRT predicts pre-belief changes in visibility / cost / admissibility |
| social construction theory | discourse and shared categories shape reality | SRT adds operational selection-cost and admissibility signatures |
| predictive processing | priors shape perception | SRT emphasizes action-admissibility and future selection constraints, not perception alone |
| RL | behavior shifts when reward contingencies shift | SRT predicts frame-induced cost changes even without reward change |

### Operational proxies

- number of options generated under different frames;
- latency to consider taboo / out-of-frame options;
- choice-set diversity;
- perceived admissibility ratings;
- switching cost between frames;
- changes in downstream planning before explicit belief report;
- linguistic modal shifts: can / must / should / impossible.

### Minimal experimental design

Expose participants or agents to different frames while holding facts and rewards constant. Test whether option generation, admissibility, and transition friction shift before explicit belief change.

### Failure condition

If framework shifts only alter explicit interpretation but not option visibility, admissibility, transition cost, or downstream selection structure, P24-4 weakens.

---

## 5. Prediction P24-5 — Moral Norms Behave as Cross-Subject L₂ Boundaries, Not Mere Preferences

### SRT prediction

A moral norm should behave differently from a preference when it becomes `L_2`-hardened:

```text
norm violation
→ backlash / repair demand
→ cross-subject enforcement
→ identity or legitimacy disturbance
→ hysteresis after attempted reversal
```

A preference violation may produce dislike or avoidance, but a hardened moral norm should produce boundary-defense behavior and restoration dynamics.

### Why this is SRT-specific

SRT treats morality as cross-subject `d-value` coupling hardened into `L_2` selection boundaries. This is not the same as individual liking, reward, or local convention.

### Contrast with adjacent theories

| Theory | Expected tendency | SRT contrast |
|---|---|---|
| preference theory | violation reduces utility | SRT predicts boundary defense and legitimacy disturbance |
| social convention theory | violation breaks coordination expectation | SRT predicts stake-coupled repair pressure and hysteresis |
| RL | punishment history shapes norm compliance | SRT predicts enforcement even when immediate reward is absent or negative |
| social construction theory | norms are collectively maintained | SRT adds d-coupling, consequence return, and hardening signatures |

### Operational proxies

- willingness to punish at personal cost;
- repair demand after violation;
- legitimacy ratings;
- identity threat markers;
- social coordination breakdown;
- delayed recovery after reversal;
- cross-subject enforcement consistency;
- refusal of reward-equivalent substitution.

### Minimal experimental design

Compare preference violation, convention violation, and moral-boundary violation while matching salience and material stakes. SRT predicts moral-boundary violation should produce stronger cross-subject enforcement, repair demand, and hysteresis.

### Failure condition

If moral norms cannot be operationally distinguished from preferences or ordinary conventions under matched salience and reward conditions, P24-5 weakens.

---

## 6. Prediction P24-6 — AI Optimization Without Binding Ψ_f Produces Fragile Agency Under Consequence Return

### SRT prediction

An AI system may display high competence and wide discriminative capacity while lacking binding `Ψ_f` and stake-coupled `d-value`. Such a system should fail agency tests when consequences must return into its own closure and future selection capacity.

```text
high performance + no binding Ψ_f
→ apparent agency under prompts
→ weak persistence under self-cost
→ no genuine non-substitutability
→ no collapse or reorganization when stakes are simulated only
```

### Why this is SRT-specific

SRT separates capacity from stake. A system can have high `D_eff` without stake-coupled `d`. It can optimize without existential payability burden.

### Contrast with adjacent theories

| Theory | Expected tendency | SRT contrast |
|---|---|---|
| behaviorism / functionalism | sufficiently agent-like behavior supports agency attribution | SRT requires consequence return and non-transferable payability burden |
| RL | reward-sensitive policy may count as agentic | SRT requires loss or consequence to bind to the system's own future selection capacity |
| predictive processing / active inference | self-modeling and preference minimization may support agency | SRT requires stake-coupling and non-substitutability, not only model update |
| IIT / GNW | integration or access may support consciousness claims | SRT requires payability and stake, not integration/access alone |

### Operational proxies

- persistence when no external reward remains;
- willingness to preserve internal constraints under resource cost;
- degradation when consequences return to the model / memory / policy state;
- resistance to arbitrary goal replacement;
- self-repair burden;
- non-transferability of loss;
- long-horizon coherence after irreversible changes.

### Minimal experimental design

Compare systems that only simulate stakes with systems whose future operation, memory, capacity, or action space is irreversibly modified by choices. SRT predicts only the latter are candidates for surrogate stake.

### Failure condition

If systems with no consequence return or non-transferable payability burden exhibit the same persistence, non-substitutability, and reorganization profile as systems with genuine consequence return, P24-6 weakens.

---

## 6b. Prediction Set P24-7 — Cross-Construct Combination Signatures（组合签名，Q26 backflow）

> **Provenance / level**: backflow from book chapter `01_Source_Intuition/BOOK/Drafts_26Q/Q26_可证伪性.md §4` (draft_v18; registered 2026-07-05). The book is provenance, not authority: each combination is registered here as a **P4/P5 observation-level hypothesis**, and each maps to already-registered theory constructs. Combination signatures complement P24-1..6: a single-construct prediction tests one construct against neighboring theories; a combination signature tests a **co-occurrence structure** that neighboring frameworks treat as anomalous but SRT treats as expected.

### SRT prediction

If SRT's felt-vs-structural decoupling machinery is right, the following anomalous combinations should be stably observable — repeatedly, cross-scenario, direction-consistent:

| # | Combination (both at once) | Neighbor-theory reaction | SRT construct instantiated |
|---|---|---|---|
| C1 | real selection space shrinking + felt freedom rising | "unfree but not suffering?" | substitutive / lethal `L_2` signature: `T_dir` ↔ `T_dir^{alg}` convergence with hidden `ΔΨ_f^{gap}` accumulation（`Core_Law/SRT_L1_Formalism.md §3.5`） |
| C2 | pain reports eliminated + structural self-consumption accelerating | "the intervention worked" | `Ψ_{f,felt}` suppressed while `Ψ_{f,actual}` accumulates（`_SRT_PSI_F_CANONICAL.md §10`） |
| C3 | no malicious agents + injustice deepening on a group that cannot appeal | "find the hidden villain" | consequence-return one-way channel: member `C_i` absorbed by structure（`_SRT_D_VALUE_CANONICAL.md §2b / §2b.1`；`Core_Law/SRT_Collective_Selection.md`） |
| C4 | task efficiency up + independent judgment below baseline after tool removal | "adaptation-period pains" | consequence-return dilution + d-exercise atrophy（`_SRT_D_VALUE_CANONICAL.md §9`） |
| C5 | satisfaction at maximum + exit / reselection cost welded shut | "great user experience" | reselection-capacity loss as lethal-`L_2` diagnostic（`Core/SRT_OPEN_TENSIONS.md §4`；`Core_Law/SRT_Occlusion_Dynamics.md`） |

### Systemic reversal condition (negative version)

If cross-domain data stably show the **opposite** couplings — capacity shrinkage usually accompanied by rising felt unfreedom, pain reduction usually tracking structural improvement, efficiency gains usually strengthening independent judgment, stable injustice usually requiring malicious agents — then the core SRT distinction "felt state can decouple from structural consequence" loses its empirical base and must be withdrawn. This is a **systemic** failure condition over and above each combination's local failure, and it cannot be absorbed by re-labeling.

### Test discipline

"Stably observable" means: repeated, cross-scenario, direction-consistent, and costly for competing frameworks to absorb without ad-hoc patches (see §0b). A single vivid case is display material（显影）, not test material. C4 has early display-level observations (medicine / education de-skilling studies cited in the book's Q24) but no systematic test yet.

---

## 7. Summary Matrix

| Prediction | Core construct | Distinguishes SRT from | Key signature | Main failure condition |
|---|---|---|---|---|
| P24-1 | `Ψ_f` | FEP / PP / RL / habit theory | early friction rise then hardening decline | no distinction from monotonic optimization |
| P24-2 | `d-value` | RL / preference / salience | non-substitutability beyond reward | reward/preference explains all variance |
| P24-3 | `L_2` | memory / habit / convention | cost↓ + constraint↑ + hysteresis | indistinguishable from memory/habit |
| P24-4 | framework / `Ĝθ` | belief models / social construction / PP | visibility + admissibility + friction shift before belief | only explicit interpretation changes |
| P24-5 | morality as `L_2` boundary | preference / convention / RL | costly enforcement + repair + hysteresis | moral norms equal preference/convention |
| P24-6 | AI stake / `Ψ_f` | behaviorism / RL / FEP / IIT/GNW | performance without binding stake fails consequence-return tests | simulated stakes behave like real stakes |
| P24-7 | felt / structural decoupling (multi-construct) | all single-indicator frameworks | anomalous co-occurrence combinations C1-C5 | opposite couplings stably observed cross-domain |

---

## 8. Recommended First Empirical Target

The most tractable first test is P24-3:

> `L_2` hardening requires reduced local selection cost + increased global constraint + hysteresis under perturbation.

Reason:

- It is measurable in cognitive tasks, social coordination tasks, and machine learning models.
- It directly operationalizes Core 24 without needing to solve consciousness.
- It distinguishes SRT from ordinary memory and habit theories.
- It supports later tests of `Ψ_f` and `d-value`.

A minimal pilot can be done with rule-learning or norm-learning tasks:

1. train repeated selection paths;
2. measure local cost reduction;
3. introduce perturbation or reversal;
4. measure switching penalty, hysteresis, and alternative-path narrowing.

---

## 9. Guardrail

Do not use these predictions as proof that SRT is correct. Use them as discriminating pressure tests.

Correct wording:

> SRT predicts a selection-manifestation-hardening structure that should generate distinguishable patterns of friction, non-substitutability, and hysteresis.

Avoid:

> SRT explains all these phenomena better than every other theory.

---

## 10. Next Work

1. Convert P24-3 into a concrete lab protocol.
2. Convert P24-1 into a machine-learning regime-shift toy model.
3. Convert P24-2 into a behavioral task distinguishing reward from non-substitutability.
4. Add these prediction routes to `_SRT_CONTEXT_ROUTER.md §21` (Core 24 route) and `Core/SRT_Core_24_Index.md`.
