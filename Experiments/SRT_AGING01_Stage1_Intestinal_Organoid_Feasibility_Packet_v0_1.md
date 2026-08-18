---
id: SRT-AGING01-STAGE1-INTESTINAL-ORGANOID-FEASIBILITY-PACKET
type: experiment_feasibility_packet
status: draft
record_stage: pre_pilot_design
version: v0_1
layer: empirical_bridge
epistemic_layer: experimental
claim_mode: feasibility
claim_level: P4-P5
canonical: false
domain: intestinal_organoid_regeneration_repeated_challenge
created: 2026-08-18
dependency:
  - Experiments/SRT_AGING01_Recovered_Present_Restored_Future_Protocol_v0_1.md
  - Operations/Audits/SRT_AGING01_P4_MODEL_SELECTION_FEASIBILITY_AUDIT_2026-08-18.md
  - Core/SRT_Validation_Template.md
  - 03_Bridges/SRT_Aging_Selective_Maintenance_Bridge_2026-08-17.md
source_anchors:
  - DOI:10.1038/s41586-019-1154-y
  - DOI:10.1038/s41422-020-00453-x
  - DOI:10.1038/s41467-024-47124-8
  - DOI:10.1038/s41586-026-10258-4
tags:
  - aging
  - organoid
  - intestinal-regeneration
  - revival-stem-cell
  - repeated-challenge
  - feasibility
  - route-switching
  - matched-state
---

# AGING01 Stage-1 Packet v0.1 — Intestinal Organoid Feasibility

> **Role**: engineering pilot for the `Recovered Present / Restored Future` protocol.  
> **Non-role**: not an organismal aging experiment, not evidence for SRT, not proof of policy memory, not a rejuvenation study.  
> **Primary objective**: determine whether a controlled epithelial system can implement the full experimental grammar `different route history -> overlapping present endpoint -> common rechallenge -> route-specific future readout -> route blockade -> rival comparison`.

---

## 0. Why this model is being considered

Primary studies already establish the technical building blocks separately:

```text
injury-induced Clu+ revival stem-cell state;
reconstitution of Lgr5+ homeostatic stem-cell compartment;
intestinal organoid injury / regenerative-state culture;
p53-dependent control of revival-stem-cell induction after radiation;
lineage tracing of Clu-derived regenerated crypts;
cell-intrinsic persistence of inflammatory epigenetic history in colonic stem-cell-derived organoids.
```

The Stage-1 question is **not** whether these findings prove history-conditioned future selectability. They do not.

The question is whether they can be assembled into a clean prospective pilot in which current-state and route-history explanations are measured rather than rhetorically inferred.

---

## 1. Pilot claim lock

The only claim this packet is allowed to test is:

> Two intestinal organoid populations that experienced different early regenerative-route conditions may, after recovery into an overlapping declared T1 state, respond differently to a later common epithelial challenge in route recruitment or switching.

Even if observed:

```text
history effect
!= SRT Selection
!= L2
!= Psi_f
!= generative reselectability by definition
!= organismal aging
```

The strongest Stage-1 result is **protocol feasibility plus a local biological history effect**.

---

## 2. Preferred formation-history family

### Preferred structure

Use the **same broad injury class** in both histories and transiently alter early regenerative-route recruitment.

Working family:

```text
common epithelial injury P1

H_A:
  endogenous / intact p53-associated revival-stem-cell recruitment window

H_B:
  same P1
  + transient early perturbation that measurably alters revival-route recruitment
  + complete washout before T1
```

The literature-supported candidate handle is transient p53-pathway modulation during the post-injury regenerative window because primary work shows that p53 activity is required for induction / proper reprogramming of Clu+ revival stem cells after irradiation.

### Critical boundary

This packet does **not** freeze:

```text
compound;
dose;
duration;
radiation dose;
recovery duration.
```

Those parameters require a separate methods / toxicity / dose-finding review.

The formation manipulation is acceptable only if it changes route recruitment without producing an irreversible gross viability difference that makes T1 overlap impossible.

---

## 3. Backup formation-history families

If no transient p53-modulation window yields both route divergence and T1 overlap, do **not** force the design.

Backup families may be evaluated in this order:

### Backup A — same injury, different regenerative culture support

```text
same P1 injury
-> transient ENR-like vs regenerative-support condition
-> return both groups to common medium
-> T1 overlap audit
```

This is technically tractable but carries a larger ordinary culture-state confound.

### Backup B — different upstream injury histories converging on common endpoint

Examples:

```text
radiation injury
vs
homeostatic-stem-cell depletion / alternative injury
```

This is weaker for causal isolation because upstream damage differs. Use only as feasibility plumbing, not as the preferred discriminating history contrast.

### Backup C — colitis-memory-derived organoids

Inflammation-history organoids provide a strong positive control for durable cell-intrinsic history, but the published phenotype is already well described as epigenetic memory and tumour-promoting regenerative bias.

Use them only to verify that the analysis pipeline can correctly conclude:

```text
history effect exists
BUT
rich current epigenetic state may exhaust the causal explanation
```

---

## 4. Required T1 recovery window

T1 is the decisive feasibility bottleneck.

The two histories need not be identical, but they must enter a preregistered overlapping window on a declared set of current measurements **before P2 is inspected**.

### T1-A — gross viability / morphology

Minimum:

```text
organoid survival;
size distribution;
bud / crypt-like structure count;
growth rate over a defined pre-P2 interval.
```

### T1-B — current injury burden

Preferred panel:

```text
DNA-damage / damage-response readout;
apoptosis / cell-death readout;
proliferation readout;
major unresolved stress response.
```

Exact assay family remains implementation-specific.

### T1-C — stem / regenerative composition

At minimum quantify:

```text
Lgr5+ homeostatic stem-cell compartment;
Clu+ / revival-state compartment;
major epithelial lineage composition;
relevant fetal-like / injury-associated regenerative-state readout.
```

### T1-D — reserve / functional capacity rival

At least one independent measure such as:

```text
organoid-forming efficiency;
clonogenic re-plating;
serial-passage survival;
recovery growth after standardized passaging.
```

### T1-E — optional rich-state layer

If resources allow, use a predeclared transcriptomic / epigenetic panel or single-cell assay to estimate how much of the later response is already readable from current state.

This layer belongs first to the **rival model**, not to the history model.

---

## 5. T1 GO / NO-GO gate

### GO

Proceed to confirmatory P2 only if:

```text
H_A and H_B show a reproducible difference in P1 route recruitment
AND
both groups survive through recovery
AND
there is a non-trivial overlapping T1 window on the predeclared gross-state panel
AND
P2 can be delivered at the same protocol-defined dose / condition.
```

### CONDITIONAL GO

Proceed only as exploratory if gross T1 overlap exists but major current-state differences remain in route composition or damage.

Interpretation:

```text
future difference may simply be current-state difference;
no N1 attempt allowed.
```

### NO-GO

Stop this formation family if:

```text
route manipulation necessarily causes persistent viability collapse;
T1 groups do not overlap;
route recruitment cannot be measured independently;
washout does not remove the direct acute pharmacological effect;
P2 cannot be standardized.
```

Do not rescue a NO-GO by weakening the T1 definition after seeing P2.

---

## 6. Standardized P2 challenge

Preferred first P2 family:

```text
common, predefined epithelial injury of the same general class used in the validated organoid system.
```

Radiation is a strong candidate because primary intestinal-organoid studies already support controlled injury, p53-dependent regenerative-state induction and lineage tracing.

But the final P2 dose remains **unfrozen** until a methods review establishes:

```text
sufficient route recruitment;
non-saturating survival;
room for alternative-route use;
reasonable between-batch reproducibility.
```

A P2 so severe that all cultures collapse, or so mild that no route switch is required, is non-informative.

---

## 7. Primary route definition

The pilot needs at least two biologically separable routes.

### Route R_homeo

Working definition:

```text
recovery dominated by persistence / re-expansion of the homeostatic Lgr5-associated stem-cell route
```

### Route R_revival

Working definition:

```text
injury-induced Clu-associated revival / fetal-like route
-> contribution to regenerated Lgr5+ crypt / stem-cell compartment
```

### Primary route endpoint

Best current candidate, because it is close to a published lineage-tracing readout:

```text
fraction / probability of regenerated Lgr5+ crypt-like structures
that derive from the predeclared Clu-lineage route after P2
```

The exact lineage-tracing implementation must follow the available model system and cannot be inferred from marker co-expression alone.

---

## 8. Secondary future endpoints

Predeclare a small vector rather than one “health score”:

```text
P2 survival;
time to regain growth;
bud / crypt recovery;
Lgr5 compartment restoration;
Clu-route recruitment;
clonogenic recovery;
serial-passage success after P2;
cell-loss burden;
current-route concentration vs mixed-route recovery.
```

Do not collapse these into a scalar `generative reselectability` score.

---

## 9. Route-blockade / switching arm

The blockade arm is what distinguishes this pilot from a generic injury-recovery study.

### Preferred logic

After confirming that both routes can be measured:

```text
block / deplete / strongly suppress one predeclared route during P2
-> ask whether H_A and H_B differ in recruitment of the alternative route
```

A literature-compatible candidate is suppression / depletion of the Lgr5-associated homeostatic route **if technically validated in the chosen organoid line**, forcing greater dependence on revival-like regeneration.

Alternative blockade may target the revival route, but this risks circularity if the same pathway was used to create H_A/H_B.

### Primary blockade endpoint

```text
Delta_switch = additional loss / latency / failure / alternative-route recruitment
under blockade relative to unblocked P2
```

The key model term is:

```text
history x blockade
```

Switching cost remains ordinary experimental language and is not identified with `Psi_f`.

---

## 10. Match-2 rival set for this pilot

The base rival should receive the strongest available current information.

Minimum pre-P2 variables:

```text
gross morphology / growth;
current damage-response burden;
cell-death state;
Lgr5 fraction;
Clu / injury-associated regenerative-state fraction;
major epithelial lineage composition;
clonogenic / serial-passage reserve proxy;
predeclared current transcriptional state if measured.
```

Optional richer rival:

```text
current chromatin / epigenetic state;
cell-state transition composition;
other validated injury-memory programs.
```

The history model may add only:

```text
H_A vs H_B label;
predeclared P1 route-use features;
predeclared bearer / lineage consequences.
```

If the current-state rival fully predicts P2, the protocol should say so.

---

## 11. Confirmatory model comparison

For the route endpoint:

```text
M_X:
Y_route_P2 ~ current_damage + current_Lgr5 + current_Clu + lineage_state + reserve + batch

M_H:
Y_route_P2 ~ M_X + H

M_B:
Y_route_P2 ~ M_X + H + blockade + H*blockade
```

Primary question:

```text
does H or H*blockade improve prospective held-out prediction
beyond M_X under a frozen information budget?
```

This is a model-selection question, not a significance-test-only question.

---

## 12. Experimental unit / replication lock

Do not treat every organoid as an independent biological replicate if they arise from one source preparation.

The execution packet must predeclare the hierarchy, for example:

```text
biological source / donor or mouse
-> independent culture preparation
-> well
-> organoid
```

Primary inferential units should respect the independent biological preparation level.

A later confirmatory phase should use:

```text
independent preparation / donor / mouse batch
```

rather than merely more organoids from the calibration batch.

---

## 13. Evidence ladder

### F0 — plumbing only

```text
P1 route manipulation works;
T1 overlap feasible;
P2 route readout measurable.
```

No biology claim beyond feasibility.

### F1 — current-state dissociation

```text
T1 gross overlap
+ different H
-> different P2 route use
```

Still readily explained by hidden current state.

### F2 — rich-rival residual

```text
pre-frozen M_X
+ H improves held-out prediction
```

Local history-conditioned response evidence; still not SRT-specific.

### F3 — switching differential

```text
H*blockade robustly predicts alternative-route recruitment / failure
```

Strongest Stage-1 result.

### F4 — carrier equalization

If a later targeted intervention normalizes a candidate present carrier and abolishes the H effect:

```text
history efficacy is localized to that carrier for the tested target.
```

This is scientifically valuable even though it removes any residual “history beyond current state”.

---

## 14. Direct NO-GO / falsification rules

Stop or downgrade if:

1. no formation manipulation can alter route recruitment while permitting T1 overlap;
2. apparent T1 overlap disappears with basic damage / composition measurement;
3. P2 outcome is dominated only by gross viability;
4. the Clu / Lgr5 route distinction cannot be lineage-validated;
5. blockade kills all cultures and therefore does not measure switching;
6. batch effects exceed the history effect and cannot be stabilized;
7. current-state model fully absorbs H in held-out data;
8. H effect is present only in the calibration batch;
9. result requires post-hoc endpoint redefinition;
10. a successful “recovery” is only marker normalization without repeated-challenge function.

Rule:

```text
Stage-1 NO-GO
-> do not jump directly to mice to rescue the idea.
```

---

## 15. Novelty / competitor boundary

Existing intestinal regeneration literature already establishes:

```text
injury-responsive stem-cell states;
revival-stem-cell recruitment;
p53-dependent regenerative reprogramming;
epigenetic inflammatory memory;
state-dependent future behaviour.
```

Therefore the Stage-1 packet does **not** claim novelty for any of those facts.

The only new SRT-programmatic contribution is the experimental grammar:

```text
explicit T1 recovery declaration
+ same-information-budget rival
+ common P2
+ route identity
+ blockade / switching
+ symmetric null disposition.
```

If this grammar adds no useful experimental discrimination, keep AGING01 as a conceptual organizer and stop.

---

## 16. Methods not yet frozen

The following are intentionally unresolved:

```text
exact organoid genotype / source;
exact radiation protocol;
exact p53-pathway manipulation;
exact lineage-tracing construct;
T1 recovery duration;
assay panel;
sample size / power;
primary held-out metric;
blockade implementation;
blinding / randomization details;
ethical / animal-source review;
cost / personnel / equipment.
```

This file must not be treated as an executable laboratory SOP.

---

## 17. Pre-pilot readiness checklist

Move from `pre_pilot_design` to `pilot-ready` only after all are answered:

1. Which published organoid genotype / line enables the required route tracing?
2. Which transient P1 route manipulation is reversible and survives washout?
3. What dose range produces route divergence without terminal collapse?
4. What exact T1 panel defines overlap?
5. What route endpoint is primary?
6. What blockade is technically independent of the formation manipulation?
7. What is the biological replicate?
8. What is the held-out replication unit?
9. What rich current-state rival model is frozen?
10. What is the formal GO / NO-GO threshold?
11. What methods / safety / ethics review applies?
12. Is the pilot cheaper and more informative than moving directly to HSC xenografts?

Until then:

```text
execution_status = NOT READY
```

---

## 18. Source boundaries

Primary literature anchors support the following pieces only:

- Ayyaz et al. 2019: Clu+ revival stem cells are injury-induced and can regenerate the intestinal stem-cell compartment.
- Liu et al. 2021: injury-associated regenerative intestinal organoid states can be maintained / modeled in culture.
- Moyer et al. 2024: p53 is required for appropriate Clu+ revival-stem-cell induction / regenerative reprogramming after severe radiation injury; organoid lineage-tracing and p53-pathway manipulation are feasible in that context.
- Castillo et al. 2026: colonic stem cells can retain cell-intrinsic epigenetic memory of prior colitis after disease resolution and organoid isolation.

None of these papers tests the full AGING01 repeated-challenge / matched-present / route-switching protocol proposed here.

---

## 19. Current disposition

```text
Stage-1 model family: SELECTED FOR METHODS REVIEW ONLY
pilot-ready: NO
experimental execution: NO
theory upgrade: NO
roadmap priority landing: STILL PENDING
```

Next required action:

> **Methods feasibility close-read of the exact organoid genotypes / route perturbation and a bounded novelty review against ordinary epithelial memory / regeneration designs.**
