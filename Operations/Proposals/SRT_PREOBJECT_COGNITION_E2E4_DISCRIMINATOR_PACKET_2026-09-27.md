---
id: SRT-PREOBJECT-COGNITION-E2E4-DISCRIMINATOR-PACKET-20260927
type: proposal
status: active
canonical: false
layer: operations
epistemic_layer: research_program
claim_mode: preregistration_preparation
created: 2026-09-27
updated: 2026-09-27
priority: current_next
research_mode: U
dependency:
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_PRIMITIVE_SELECTION_ANTI_TAUTOLOGY_STOP_AND_NEXT_ROUTING_2026-09-27.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_PREOBJECT_GENERATIVE_ORIENTATION_COGNITION_2026-09-26.md
  - Operations/Proposals/SRT_PREOBJECT_GENERATIVE_ORIENTATION_COGNITION_RESEARCH_PROGRAM_2026-09-26.md
  - Operations/Audits/SRT_L0_FACING_FIELD_H1_H2_H3_LEVEL_RECLASSIFICATION_2026-09-26.md
tags: [Cognition, NeuralGeometry, Learning, PreObjectOrientation, E2, E3, E4, Discriminator, Wójcik]
---

# Pre-object cognition CURRENT NEXT — E2/E3/E4 discriminator packet

> **Role:** first bounded execution packet after the 2026-09-27 primitive anti-tautology STOP.
>
> **Boundary:** neutral cognition science first. This packet does not test primitive Selection, O0, L0 ontology, HP-B or SRT metaphysical distinctiveness.

## 0. Current question

The active programme asks whether a whole-system orientation / geometry description adds any independent scientific value beyond:

- local implementation / tuning changes;
- latent-state / representation models;
- generic learning dynamics.

The first execution therefore must not ask:

> “Can we see neural geometry changing?”

That is already mature-neighbor paid.

It asks:

> **Can one shared geometry-level organization predict multiple held-out local recutting / generalization effects better, or more compactly, than strong local-update and latent-state baselines?**

This is an E2 question.

## 1. First dataset lock — COG-E2-1

### Dataset / paper

Wójcik et al. (2026), *Learning shapes neural geometry in the primate prefrontal cortex*, Nature Neuroscience 29:1966–1975.

DOI: `10.1038/s41593-026-02333-w`

Open data:

`https://doi.org/10.5061/dryad.c2fqz61kb`

Open code:

`https://github.com/m-j-wojcik/pfc_learning`

### Why selected

The public package provides:

- longitudinal PFC recordings during learning;
- two macaques;
- multiple sessions over the learning trajectory;
- trial-level neural activity and condition metadata;
- Experiment 1: learning a nonlinear XOR rule;
- Experiment 2: rule generalization to a novel stimulus set;
- published analyses of decoding, shattering dimensionality, selectivity and cross-generalization;
- 32.11 GB total Dryad data;
- public Python analysis code.

The published result already shows a progression from high-dimensional / mixed representations toward lower-dimensional rule-selective geometry, with further abstract stimulus-invariant geometry during generalization.

Therefore this dataset is **not** used to rediscover “geometry changes with learning.”

It is used to ask whether a geometry-level model earns **held-out predictive/compression gain** beyond fair baselines.

## 2. Evidence ladder

### E1 — descriptive geometry

Already source-paid.

Examples:

- dimensionality changes;
- factorization / abstraction changes;
- RDM / manifold structure changes;
- cross-generalization improves.

No new SRT or programme credit for reproducing E1.

### E2 — predictive geometry — CURRENT TARGET

Required:

> A geometry-level summary/operator inferred from training conditions/sessions predicts held-out local relations or generalization better than strong H1/H2 baselines.

### E3 — causal geometry — HOLD

Requires an intervention that changes the candidate geometry while controlling lower-level alternatives.

The Wójcik dataset alone does not provide this.

No E3 claim may be made from retrospective geometry/behavior association.

### E4 — recursive field reconstitution — HOLD / DESIGN AFTER E2

Requires:

~~~text
consequence / history
-> geometry change
-> geometry predicts later recutting / generalization
-> new consequences
-> further geometry change
~~~

Longitudinal structure may support a preliminary lagged analysis, but causal E4 requires stronger evidence than this first packet.

## 3. Analysis unit

Primary unit:

~~~text
session-level condition geometry
at declared task-relevant time windows
~~~

Reason:

- recorded neurons differ across sessions;
- geometry based on condition relations can be compared across sessions without pretending neuron identity is stable;
- the programme target is organization across local probes, not a claim of one literal field variable.

Primary objects:

- condition centroids / cross-validated condition distances;
- representational dissimilarity structure;
- geometry statistics tied to factorization, dimensionality and abstraction;
- held-out cross-condition / cross-stimulus generalization.

## 4. Three fair model families

### H1 — LOCAL / IMPLEMENTATION baseline

Allow:

- condition-specific tuning changes;
- feature-wise decoder strength changes;
- neuron/selectivity changes;
- session and learning-stage effects;
- independent local predictors for each probe.

H1 may fit local effects flexibly.

It fails only if a shared geometry model predicts held-out relations that independent local fits do not capture under matched regularization / information budget.

### H2 — LATENT-STATE / REPRESENTATION baseline

This must be strong.

Allow a regularized low-rank latent representation learned from the same neural data, with:

- session-dependent latent state;
- nonlinear task-variable interactions where needed;
- cross-validated dimensionality;
- learned mappings from latent state to local readouts;
- no requirement that latent axes preserve SRT vocabulary.

Candidate implementations for preregistration comparison:

- factor-analysis / reduced-rank regression family;
- supervised low-rank task representation;
- optionally a flexible neural latent baseline if parameter matching is explicit.

H2 is allowed to reproduce geometry.

If H2 reconstructs the H3 geometry and predicts held-out probes equally well with equal/lower complexity, then:

~~~text
H3 scientific increment = ZERO.
~~~

### H3 — WHOLE-GEOMETRY model

H3 is **not** a separate mechanism by definition.

It is a candidate organizational description.

Fit one shared geometry-level structure per learning stage/session family from a training subset, then test whether it predicts held-out condition relations / generalization.

Candidate representation:

~~~text
G_s
= cross-validated condition-by-condition geometry
  for session/stage s
~~~

Candidate transformation:

~~~text
T_s:
G_s -> G_(s+1) / abstracted geometry family
~~~

The operator is descriptive until it earns E2.

No new SRT symbol is created.

## 5. The first nontrivial prediction

### E2-P1 — held-out relation prediction

Split task relations into training and held-out sets.

Fit H1 / H2 / H3 without access to the held-out relation.

Ask whether H3 predicts:

- **primary:** held-out context cross-stimulus-set generalisation where ordinary context decoding is stable across learning;
- secondary shape cross-set generalisation;
- the contrasting XOR pattern where cross-set generalisation is already high early;
- held-out irrelevant-feature normalization / width control;
- later novel-stimulus-set abstraction.

A valid H3 result requires prediction of structure that was not directly used to fit the geometry.

### E2-P2 — cross-probe compression

A single H3 fit should jointly account for at least three probe families, for example:

1. context cross-set alignment;
2. shape relational generalisation;
3. XOR early-aligned positive control;
4. width-irrelevance / normalization.

If a separate geometry parameterization is fitted for every probe, compression credit is lost.

### E2-P3 — prospective session prediction

Exploratory unless sample structure supports preregistration:

~~~text
G_s
-> held-out behavioral / cross-generalization improvement at s+1
controlling current performance and H1/H2 state.
~~~

This is stronger than concurrent correlation.

It remains predictive, not causal.

## 6. Complexity / fairness rules

All models must use:

- identical train/test splits;
- same session inclusion;
- same declared time windows;
- nested cross-validation for hyperparameters;
- comparable effective complexity reporting;
- no condition leakage;
- no tuning on Experiment-2 transfer labels before the transfer test.

Report at minimum:

- held-out prediction error / likelihood;
- cross-generalization accuracy;
- parameter/effective-rank cost;
- out-of-sample compression metric.

No victory by raw in-sample fit.

## 7. Strong failure conditions

Record **NO WHOLE-GEOMETRY INCREMENT** if any holds:

1. H2 reproduces H3 held-out predictions at equal/lower complexity;
2. H3 only redescribes decoder accuracy already available to H1/H2;
3. H3 gains disappear under cross-session / cross-stimulus holdout;
4. H3 requires separate probe-specific fits;
5. apparent geometry gain depends on a leakage-prone condition definition;
6. the result is only “dimensionality changed with learning.”

A null/no-gain result is preferred to weakening the baselines.

## 8. What would count as a bounded E2 PASS

Only:

~~~text
one shared geometry-level organization
-> predicts multiple held-out local recutting/generalization relations
-> survives strong H1/H2 baselines
-> offers lower-burden or genuinely additional out-of-sample prediction.
~~~

Even then:

~~~text
E2 PASS
!= field ontology;
!= SRT-specific mechanism;
!= primitive Selection evidence;
!= E3 causal geometry;
!= E4 recursive field reconstitution.
~~~

## 9. Candidate E3 route after E2 only

If E2 passes, next ask for a perturbation paradigm where:

- local stimulus statistics are matched;
- latent context / explicit rule knowledge is controlled;
- a global/context manipulation shifts geometry;
- several local objectification/choice/grouping probes move coherently.

Possible families:

- context-switch decision geometry;
- category recutting after consequence changes;
- task-set or rule remapping;
- causal perturbation of PFC / frontoparietal coordination.

No E3 execution is authorized in this packet.

## 10. Candidate E4 route after E2 only

Nogueira et al. (2026 preprint), *The geometry of context-dependent biased decisions during learning*, is a strong E4-shaped future comparator because:

- reward context switches;
- geometry shifts across contexts;
- learning makes context transitions faster;
- behavioral generalization co-evolves with manifold shifts.

But its neural dataset is not yet publicly deposited as of the 2026-09-27 check; code is public.

Therefore:

~~~text
Nogueira 2026
= E4 design reference / future candidate;
!= first execution dataset.
~~~

## 11. Contemporary theory baseline

Wakhloo, Slatton & Chung (2026), *Neural population geometry and optimal coding of tasks with shared latent structure*, provides an explicit mature geometry account in which dimensionality, factorization and correlation statistics determine generalization.

Therefore H3 cannot claim novelty merely for linking geometry to generalization.

The present programme must ask whether a **shared geometry transformation across learning / recutting** adds predictive/compression value over latent-state and local models.

## 12. Execution staging

### Stage A — source/code audit

- freeze sessions and task windows;
- reproduce one published E1 result;
- verify metadata / condition coding;
- record compute/storage burden;
- do not inspect held-out target results while finalizing E2 split.

### Stage B — preregister E2

Freeze:

- H1/H2/H3 implementations;
- train/test splits;
- primary metric;
- E2-P1 / P2;
- no-gain gates.

### Stage C — execute E2

No E3/E4 interpretation.

### Stage D — disposition

Outcomes:

~~~text
E2 PASS
-> design E3 perturbation / E4 recursion;

E2 PARTIAL
-> keep geometry as descriptive/compression layer only;

E2 NO-GAIN
-> whole-field scientific increment not established in this case;
   do not rescue with SRT vocabulary.
~~~

## 13. Current route

~~~text
CURRENT NEXT
= COG-E2-1 source/code audit
  -> preregistered held-out predictive geometry duel;

dataset
= Wójcik et al. 2026 open PFC learning dataset;

canonical edit
= NO;

SRT primitive evidence
= NO;

toy simulation
= HOLD;

HP-B
= READ-ONLY / FROZEN.
~~~


## 14. 2026-09-27 primary-target refinement

Experiment 2 contains a particularly clean geometry-vs-information dissociation:

- context ordinary decoding remains stable across learning;
- context cross-set generalisation increases significantly;
- shape shows a similar but secondary pattern;
- XOR cross-set generalisation is already high early and does not significantly increase.

Therefore the first E2 duel now prioritizes **context cross-set generalisation**, not XOR.

Scientific reason:

> the model must predict a change in representational relation / alignment while not simply predicting more decodable context information.

This is a stronger E2 discriminator between local information gain and geometry-level reorganization.
