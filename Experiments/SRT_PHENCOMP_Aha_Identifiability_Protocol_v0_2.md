---
id: SRT-PHENCOMP-AHA-IDENTIFIABILITY-PROTOCOL-V0-2
type: experimental_protocol
status: draft
record_stage: parked_pre_pilot_v0_2
layer: empirical_bridge
epistemic_layer: experimental
claim_mode: protocol
claim_level: P4
canonical: false
created: 2026-08-23
supersedes: Experiments/SRT_PHENCOMP_Aha_Same_Terminal_Content_Protocol_v0_1.md
execution_authorized: false
validation_level: formal_V4_pre_V5_identifiability_redesign
owner_hook: Philosophy/hooks/PH_QUAL_Bearing_Indexed_Phenomenal_Compression_Hook_2026-08-23.md
dependency:
  - Core/SRT_Validation_Template.md
  - Experiments/SRT_Experimental_Roadmap_v1.md
  - _SRT_D_VALUE_CANONICAL.md
  - _SRT_PSI_F_CANONICAL.md
  - 03_Bridges/SRT_Agency_Automation_Guard_2026-08-17.md
  - Philosophy/hooks/PH_CONSC04_Phenomenal_Necessity_Zombie_Deletion_Integration_Hook.md
  - Philosophy/hooks/PH_MR01_Representational_Gradualism_Integration_Hook.md
  - Philosophy/hooks/PH_QUAL_Bearing_Indexed_Phenomenal_Compression_Hook_2026-08-23.md
  - Neuroscience/hooks/SRT_Aha_Representational_Reconstitution_Hook_2026-08-23.md
  - Materials/2026/SRC_2026_08_23_Neuro_Becker_Aha_Representational_Reconstitution.md
tags:
  - aha
  - insight
  - phenomenal-compression
  - candidate-space
  - identifiability
  - predictive-estimand
  - terminal-state-equivalence
  - lived-directional-non-neutrality
  - P4
  - falsification
---

# Phenomenal Compression P4 Protocol v0.2 — Identifiability Before Execution

> **Decision first:** this protocol is **PARKED / PRE-PILOT**. It is not an active execution item, not a preregistration and not authorization to recruit participants.
>
> The protocol tests a bounded **predictive-discrimination claim**, not a causal or constitutive claim: under a terminal-state equivalence gate and fair rival feature access, does content-sensitive candidate-space change add held-out predictive information about Aha suddenness?

---

## 0. What v0.2 is allowed to claim

The design preserves four useful ideas from v0.1:

```text
matched terminal object identity
different formation paths
PRE / TRANSITION / POST separation
ordinary-rival comparison
```

but hardens the identification boundary:

```text
same object label != same terminal representational state
predictive increment != causal effect
weak Aha != phenomenal emptiness
confidence dynamics != candidate-space deformation
```

The central question is therefore narrower than the owner hook:

> Among B/C trials that pass a measured terminal-state equivalence gate, does a preregistered content-sensitive PRE→POST candidate-space endpoint improve held-out prediction of Aha suddenness beyond equally rich ordinary rivals?

This protocol does **not** estimate:

```text
deformation causes Aha
formation path causes phenomenality
deformation is constitutively sufficient for qualia
absence of Aha implies absence of phenomenality
pressure trajectory = Psi_f
```

---

## 1. Predictive estimand and interpretation boundary

### 1.1 Primary estimand

Freeze one held-out predictive metric at Stage 0A / Stage 1 before confirmatory execution.

Generic test-local form:

```text
DeltaPred = held_out_loss(RM1) - held_out_loss(RM2)
```

where larger positive `DeltaPred` means the candidate-space endpoint adds predictive information beyond the ordinary-rival model.

The final implementation may use a metric appropriate to the frozen model family, e.g. held-out log loss, RMSE reduction, cross-validated R2 increment or ELPD difference. The metric must be selected before Stage 2.

`DeltaPred` is a protocol-local estimand. It is not an SRT primitive or mechanism variable.

### 1.2 No causal conversion

A positive `DeltaPred` licenses only:

> candidate-space information contributes incremental held-out prediction of suddenness under the frozen design.

It does not license:

```text
candidate-space deformation -> suddenness
candidate-space deformation -> phenomenality
candidate-space deformation is sufficient / necessary for qualia
```

The owner hook may treat a robust predictive result as bounded HP-C evidence, but not as a causal or phenomenal-necessity theorem.

### 1.3 Minimal temporal-role graph

Stage 0A must maintain an explicit temporal-role graph at least as rich as:

```text
participant/item latent factors
          |\
          | \________________________
          v                          v
formation condition B/C       report/metacognitive traits
          |                          |
          v                          v
cue exposure / search process   phenomenology report quality
          |
          +--> RT / time-to-recognition
          |
          +--> PRE candidate state
          |         |
          |         v
          |    PRE->POST D_PRIMARY
          |         |
          v         v
transition / recognition --> suddenness report
          |
          v
terminal-state measures
```

This is not a causal-identification claim. Its purpose is to prevent post-treatment or outcome-adjacent variables from being described later as if ordinary predictive conditioning had identified a causal effect.

---

## 2. Experimental logic

### 2.1 Core comparison: B vs C

Primary analysis uses:

```text
B — gradual externally supported disambiguation
C — unhinted self-generated recognition
```

Both contain an unresolved interval before recognition in which a content-sensitive PRE candidate field can in principle be sampled.

### 2.2 Benchmark only: A

```text
A — direct verbal/category reveal
```

A is a low-search benchmark only. It does **not** enter the primary PRE→POST deformation regression because it has no assumed measurement-equivalent unresolved PRE field.

A may contribute to:

- terminal-state benchmarking;
- transition-phenomenology benchmarking;
- descriptive comparison of low-search versus search-heavy resolution.

It must not be used to manufacture a three-point PRE ordering.

### 2.3 No clear-image reveal before primary endpoints

Before transition and terminal-state measures are complete, A should use a preregistered verbal/category cue while the ambiguous visual stimulus remains physically unchanged as far as practicable.

Do not use:

```text
clear canonical image -> ambiguous image
```

before primary endpoints, because clear-image exposure introduces visual priming / target-template exposure / one-shot perceptual learning in the same representational direction used by the Becker RC result.

---

## 3. Formation conditions

### A — direct verbal reveal benchmark

Example:

```text
ambiguous image remains on screen
+
brief preregistered object/category label
```

A remains outside the core PRE-deformation model.

### B — gradual externally supported disambiguation

Use a fixed, item-specific, preregistered cue schedule.

Rules:

- cue content and timing fixed before collection;
- no adaptive branching based on participant guesses;
- recognition may terminate the cue sequence;
- cumulative cue dose at recognition is recorded;
- cue dose is an ordinary explanatory / sensitivity variable, not deformation.

Because cue dose is partly downstream of recognition timing, it cannot be treated as a clean exogenous control.

### C — unhinted self-generated recognition

Present the ambiguous image without solution cues until recognition or timeout.

Condition membership does not define Aha. Suddenness is measured continuously.

### 3.1 Anti-carryover

Each participant-item pair appears in only one formation condition before the primary endpoint. Across participants, items are counterbalanced across conditions.

---

## 4. Terminal state: equivalence is a gate, not a covariate rescue

### 4.1 Replace label identity with measured terminal state

Do not infer:

```text
same DOG label -> same terminal representation
```

Use:

```text
same intended object identity
+
common terminal-state battery
-> empirical equivalence test
```

Becker-style evidence motivates the concern: post-solution representational strength can vary with insight.

### 4.2 Common terminal-state battery

Administer the same battery across A/B/C after recognition and before any contaminating clear-image exposure.

Candidate components:

1. near-neighbor forced choice — target vs plausible lure classes;
2. generalization probe — preregistered transformed / degraded derivative not previously shown;
3. target-lure similarity profile — only after primary transition measures;
4. recognition stability / latency on a held-out variant.

Stage 0A selects a bounded battery; Stage 0B tests reliability and discriminability.

### 4.3 Primary D-track GO rule

Freeze local terminal equivalence bounds:

```text
TERM_SESOI_k
```

Primary confirmatory D-track entry requires equivalence within the frozen bounds on the selected terminal-state measures.

If terminal equivalence fails:

```text
PRIMARY D-TRACK STOP
```

A predeclared conditional model using measured terminal-state features may still be reported as a **secondary predictive analysis**, but it cannot restore the matched-terminal-state claim and cannot be used to strengthen the owner hook as if the gate had passed.

Correct labels alone never satisfy this gate.

---

## 5. PRE candidate field: content-sensitive and claim-preserving

### 5.1 Scope

Confirmatory PRE candidate-field inference is restricted to B/C.

### 5.2 Primary temporal anchor

PRE probes must be externally scheduled / stimulus-onset locked. They must not be back-locked to the participant's reported Aha time.

Recognition time is modeled separately as RT / event-time information.

Transition-locked plots are secondary descriptive analyses only.

### 5.3 RT belongs to rivals

```text
RT / search duration -> ordinary-rival block
```

RT is not part of `D_PRIMARY`.

### 5.4 PM-A — preferred content-sensitive staggered single-probe design

Preferred low-reactivity architecture:

```text
each probed trial:
exactly one PRE content-sensitive candidate probe
at an externally randomized / balanced onset time
+
one common POST candidate probe after recognition
```

Across trials, PRE probe times are staggered across preregistered onset windows.

The PRE probe must preserve information about **which interpretations are live**, not merely confidence.

Possible content formats:

- independently normed candidate/lure set + `other / none`;
- sparse open-ended report with blinded semantic coding;
- probability / allocation across a bounded candidate set if Stage 0B shows acceptable reactivity.

### 5.5 What PM-A can and cannot estimate

The primary confirmatory construct is a **PRE→POST structural change**, not a continuous within-trial trajectory.

Permissible candidate components include:

```text
live-candidate count change
candidate-distribution concentration change
target-vs-strongest-alternative dominance change
strongest-alternative suppression
```

Cross-trial estimates of candidate structure as a function of randomized probe time may be used as secondary temporal profiles.

Do not claim that staggered single probes directly recover each trial's continuous compression trajectory.

### 5.6 PM-B — confidence-like diagnostic fallback

A confidence / candidate-presence trajectory may be collected for feasibility and rival modeling, but:

```text
confidence-only PRE != candidate-space deformation evidence
```

If only PM-B survives reliability/reactivity engineering, the allowed claim downgrades to something like:

> confidence dynamics predicts Aha suddenness beyond confidence level.

Forbidden rescue:

> rename confidence dynamics candidate-space deformation and keep the D-track.

PRE proxy selection is claim-altering.

---

## 6. Probe reactivity

### 6.1 Mean effects

A no-probe benchmark can test whether probing changes:

- recognition/Aha incidence;
- recognition timing;
- mean suddenness.

### 6.2 Slope effects

Stage 0B must also compare at least two probed densities or schedules targeting the same construct, e.g. low-density sparse probe vs higher-density diagnostic probe.

Test whether:

```text
beta(D_PRIMARY or candidate-state measure -> suddenness)
```

changes materially with probe density/schedule.

If the relation is probe-dependent beyond a frozen tolerance:

```text
REDESIGN
```

Probe-density manipulation is a preferred low-cost test, not the only logically possible reactivity test.

---

## 7. Transition phenomenology

### 7.1 Single primary outcome

```text
PRIMARY = suddenness
```

### 7.2 Confirmatory secondary outcomes

```text
rightness / obviousness
relief
```

Use a preregistered multiplicity correction, e.g. Holm across the secondary family.

### 7.3 Rival/control/exploratory outcomes

```text
pleasantness
confidence / certainty
arousal
urgency / pull
```

These cannot be promoted post hoc to rescue a failed primary endpoint.

### 7.4 Positive-control definition

Stage 0B must norm an independent subset of items / trials expected to produce a high rate of clearly endorsed Aha-like transitions under the chosen report scale.

A report instrument is considered sensitive only if it discriminates this positive-control subset from a low-Aha comparison subset with acceptable reliability.

Positive controls validate **Aha-report sensitivity**, not consciousness detection.

### 7.5 PH_MR01 guard

```text
subjective suddenness
!= demonstrated neural discontinuity
!= ontological phase transition
```

---

## 8. D_PRIMARY: one confirmatory deformation endpoint

Stage 0A must freeze one primary content-sensitive PRE→POST endpoint or one fully prespecified multivariate summary.

Working family:

```text
D_PRIMARY = preregistered content-sensitive PRE->POST candidate-field change
```

The preferred first-pass design should choose one simple endpoint, such as target-vs-strongest-alternative dominance change, if reliability/norming support it.

`D_PRIMARY` is protocol-local and is not `RDef_B`, `Psi_f`, `d`, valence or consciousness.

### 8.1 Confirmatory versus secondary deformation measures

Confirmatory model:

```text
RM2 = RM1 + D_PRIMARY
```

Secondary construct-validity / robustness measures may include:

- alternative suppression;
- ambiguity recoverability;
- switching cost;
- attention to diagnostic features;
- transfer/generalization.

A failed `D_PRIMARY` cannot be rescued by selecting another deformation feature after seeing confirmatory data.

---

## 9. Rival-model fairness

### 9.1 Naming

```text
PM-* = PRE measurement methods
RM-* = predictive model families
```

### 9.2 Core predictive model family

The exact final specification is frozen after Stage 0 / Stage 1, but the roles are:

```text
RM0:
participant/item structure
+ condition B/C
+ item difficulty
+ RT / time-to-recognition
+ preregistered B cue-dose sensitivity terms where applicable

RM1:
RM0
+ confidence / certainty
+ arousal / pleasantness
+ attention / salience proxies
+ available mismatch / prediction-error-style proxies

RM2:
RM1
+ D_PRIMARY
```

Terminal-state variables are **not** used to rescue a failed terminal-equivalence gate. If the gate fails, the primary D-track stops; any terminal-conditioned analysis is secondary only.

### 9.3 Feature-form parity follows the actual measurement design

Do not pre-assume slopes / curvature that PM-A cannot produce.

If `D_PRIMARY` is a PRE→POST level/change endpoint, rival signals that have comparable PRE/POST measurements should receive the same function class where applicable, e.g.:

```text
PRE->POST confidence change
PRE->POST arousal change
PRE->POST attention-proxy change
```

If a later authorized design gives RM2 a temporal transform such as slope, variance, switching rate or curvature, RM1 must receive the same transform class on rival signals where measurable.

Never compare a rich deformation representation against a deliberately impoverished scalar rival and call the increment SRT-specific.

### 9.4 Equal modeling opportunity

Where flexible models are used:

- same train/test partitions;
- same tuning / regularization budget;
- same leakage rules;
- participant/item-aware splits where appropriate;
- held-out performance with uncertainty intervals.

---

## 10. Effect-size / equivalence discipline

v0.2 remains formal V4 / pre-V5.

Before confirmatory GO, independent literature / norming / feasibility data must support frozen local decision scales:

```text
TERM_SESOI  terminal-state equivalence bound(s)
DEF_SESOI   smallest meaningful D_PRIMARY difference / negligible range
PRED_SESOI  smallest held-out DeltaPred worth retaining D-track
```

These are protocol-local placeholders, not theory symbols.

### 10.1 Positive criterion

A confirmatory positive result requires:

1. terminal-state gate passes;
2. `DeltaPred` meets or exceeds the frozen `PRED_SESOI` under the frozen held-out metric;
3. uncertainty is compatible with the strengthening claim;
4. the B/C source-sensitivity result is interpreted according to Section 11.

### 10.2 Null / narrowing criterion

Use an equivalence / ROPE / TOST-style branch appropriate to the frozen metric so a practically negligible effect can be affirmatively identified rather than described only as nonsignificant.

---

## 11. B/C source-sensitivity is part of the primary interpretation

B and C differ not only in graduality but in the source of information:

```text
B: externally cue-assisted narrowing
C: unhinted self-generated narrowing
```

Therefore the design must pre-register condition moderation of the `D_PRIMARY`–suddenness relationship.

Test-local interpretive discriminator:

```text
D_PRIMARY × condition(B/C)
```

Before Stage 2, freeze an equivalence / meaningful-difference rule for the B/C slopes.

### Case 1 — B/C slopes materially equivalent

Admissible strengthening:

> the predictive relation between content-sensitive candidate-field change and suddenness is relatively robust to whether resolution was externally supported or self-generated.

### Case 2 — C-only relation

If the relation is meaningful in C but negligible in B:

> narrow the claim to self-generated restructuring / recognition contexts.

Do not generalize to cue-driven resolution.

### Case 3 — B-only relation

If the relation is meaningful in B but negligible in C:

> the self-generated phenomenal-compression reading is under pressure; retain only a cue-assisted closure result unless another preregistered explanation survives.

### Case 4 — neither arm

```text
D-track narrow / STOP
```

Condition interaction is not a post-hoc nuisance check; it is part of the main interpretation.

---

## 12. Falsification / narrowing conditions

### F1 — vivid Aha-specific phenomenology with negligible D_PRIMARY

If high suddenness repeatedly occurs while `D_PRIMARY` is equivalent to the preregistered negligible range, the compression interpretation weakens.

### F2 — strong measured deformation with weak Aha-specific phenomenology

If large `D_PRIMARY` co-occurs with weak / absent Aha-specific phenomenology under a sensitive report instrument, this weakens any claim of a tight or reliable deformation–Aha coupling.

It does **not** establish:

```text
deformation is causally insufficient for phenomenality
absence of phenomenality
PH-CONSC04 zombie evidence
```

Human participants may remain richly conscious while lacking a strong Aha transition.

### F3 — ordinary-rival absorption

If `DeltaPred` is equivalent to less than `PRED_SESOI` under feature-parity RM1/RM2, the SRT-specific D-track fails / narrows.

### F4 — terminal nonequivalence

If B/C fail the frozen terminal-state equivalence gate:

```text
PRIMARY D-TRACK STOP
```

A secondary terminal-conditioned prediction analysis cannot rescue the primary claim.

### F5 — measurement reactivity

If PRE probing materially alters mean Aha/recognition outcomes or the candidate-space–suddenness relation beyond frozen tolerances, redesign the measurement.

### F6 — claim-preserving proxy failure

If no reliable nonreactive content-sensitive PRE proxy survives and only confidence-like PM-B survives, candidate-space D-track is downgraded / parked rather than relabeled.

### F7 — source-instability

If B/C moderation shows that the predictive relation reverses or exists only in a formation source incompatible with the stated interpretation, narrow the claim according to Section 11 rather than averaging the arms into a misleading pooled effect.

---

## 13. Stage 0 is an identifiability program

### Stage 0A — desk identifiability audit

No participant recruitment.

Must freeze / specify:

1. terminal-state battery candidate and measurement order;
2. B/C core analysis and A benchmark role;
3. onset-locked / externally randomized staggered PRE timing architecture;
4. PM-A content-sensitive candidate representation and common POST representation;
5. one confirmatory `D_PRIMARY` candidate and secondary deformation family;
6. rival feature-form parity rules matched to the actual PM-A design;
7. single primary phenomenology outcome and secondary multiplicity rule;
8. external basis / procedure for `TERM_SESOI`, `DEF_SESOI`, `PRED_SESOI`;
9. exclusion / missingness handling for recognition before scheduled PRE probe;
10. B cue-dose / RT sensitivity strategy;
11. **predictive estimand and temporal-role audit** — freeze `DeltaPred`, explicitly classify the protocol as predictive rather than causal/constitutive, maintain the minimal temporal-role graph, and forbid post-treatment conditioning from rescuing a failed terminal-equivalence gate;
12. **measurement-feature compatibility audit** — verify that the frozen PM-A scheme can actually generate the proposed `D_PRIMARY`; default to staggered single PRE probe + common POST probe and do not claim unavailable within-trial trajectory features;
13. **B/C source-sensitivity rule** — freeze the `D_PRIMARY × condition` analysis and the scope-narrowing decisions for equivalent, C-only, B-only and null relations.

Output:

```text
DESK-GO -> eligible for separately authorized Stage 0B
REDESIGN -> revise protocol
STOP -> park D-track
```

No DESK-GO may be issued while items 11–13 remain unresolved.

### Stage 0B — micro-feasibility / norming

Requires separate later authorization.

Goals:

- terminal-battery reliability / discriminability;
- candidate/lure norming for PM-A;
- randomized staggered probe-time feasibility;
- probe-density mean- and slope-reactivity test;
- B/C recognition density and timing;
- cue-dose behavior;
- Aha positive-control item norming and report-scale sensitivity;
- preliminary variance needed to freeze decision bounds.

Stage 0B is measurement engineering, not evidence for phenomenality.

### Stage 1 — behavioral pipeline pilot

Only after Stage 0A/0B gates pass.

Stage 1 may be used to debug leakage, terminal balance, proxy collapse, model implementation and precision planning.

**Stage 1 data used to choose or modify endpoints, SESOI, transforms, exclusions, model family or analysis rules must not be reused as Stage 2 confirmatory evidence.**

If a frozen subset is ever proposed for reuse, that exception must be prospectively justified before Stage 1 inspection; default is no reuse.

### Stage 2 — confirmatory behavioral replication

Only after Stage 1 freezes:

- sample-size / precision logic;
- terminal-state gate;
- `D_PRIMARY`;
- `TERM_SESOI`, `DEF_SESOI`, `PRED_SESOI`;
- primary suddenness endpoint + secondary correction;
- PM-A implementation;
- RM0/RM1/RM2 feature sets;
- `DeltaPred` metric / held-out evaluation scheme;
- B/C source-sensitivity rule;
- failure / narrowing rules.

### Stage 3 — optional neural / physiological extension

Only if the behavioral D-track survives.

Neural measurement does not repair a failed behavioral identification strategy.

---

## 14. Interpretation matrix

| Result | Admissible interpretation | Forbidden interpretation |
|---|---|---|
| terminal gate passes; `DeltaPred >= PRED_SESOI`; B/C rule satisfied | bounded predictive support that content-sensitive candidate-field change adds information about Aha suddenness | deformation causes Aha / consciousness |
| `DeltaPred` equivalent to negligible | D-track narrows toward ordinary rivals | SRT secretly explains it anyway |
| large D_PRIMARY + weak Aha | weakens tight/reliable predictive coupling | causal insufficiency for phenomenality / zombie evidence |
| high suddenness + negligible D_PRIMARY | compression account weakens | redefine D_PRIMARY post hoc |
| terminal gate fails | primary formation-path D-track not identified | covariate-adjust terminal state and claim the same inference |
| only confidence-like PRE survives | downgrade to confidence-dynamics result | relabel confidence as candidate-space deformation |
| C-only relation | narrow to self-generated restructuring | generalize across formation sources |
| B-only relation | pressure on self-generated reading | average B/C and hide moderation |

---

## 15. Relation to the owner hook

This protocol tests only:

```text
content-sensitive candidate-field change
<-> predictive structure of Aha suddenness
```

It does not test the owner hook's phenomenal-necessity bridge:

```text
bearing-indexed directional non-neutrality
-> ?
lived directional non-neutrality
```

Nor does it empirically instantiate PH-CONSC04 deletion.

A successful result supports only a bounded HP-C statement:

> after terminal-state equivalence and fair rival access are satisfied, a content-sensitive candidate-space endpoint carries incremental predictive information about Aha suddenness.

---

## 16. Canonical / terminology guards

```text
Aha != Selection definition
Selection != Agency
representation change != phenomenality
attractor / deformation != consciousness
bearing != experiencer
repo micro-valence != epsilon_pg
lived directional non-neutrality is not repo micro-valence
lived directional non-neutrality != d
task-level pressure trajectory != Psi_f
subjective relief != demonstrated Psi_f decrease
prediction error != Psi_f
confidence / attention / emotion != d
memory != L2
immediate relief != truth
immediate relief != generative health
subjective suddenness != neural discontinuity
absence of Aha-specific phenomenology != phenomenal emptiness
predictive increment != causal effect
predictive increment != constitutive sufficiency
```

---

## 17. Current disposition

**PARKED PRE-PILOT / IDENTIFIABILITY REDESIGN.**

The next allowed action after merge is **Stage 0A desk identifiability audit only**.

Do not recruit participants, run Stage 0B, freeze a power calculation, add neural modalities or promote the owner hook on the basis of this protocol without later explicit authorization.

The protocol becomes V5-candidate only after Stage 0 identification debts are resolved and the predictive estimand, terminal-state gate, PM-A measurement architecture, `D_PRIMARY`, rival parity rules, B/C source-sensitivity rule and SESOI/equivalence decisions are frozen.
