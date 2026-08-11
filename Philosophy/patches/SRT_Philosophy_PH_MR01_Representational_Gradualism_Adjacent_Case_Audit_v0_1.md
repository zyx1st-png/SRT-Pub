---
patch_id: PATCH-PHIL-PH-MR01-REPRESENTATIONAL-GRADUALISM-ADJACENT-CASE-AUDIT
id: PATCH-PHIL-PH-MR01-REPRESENTATIONAL-GRADUALISM-ADJACENT-CASE-AUDIT
source_ids:
  - SRC-2026-08-11-PHIL-SCHULTE-RADICAL-GRADUALISM-REPRESENTATION
domain: philosophy_of_mind_representation_cognition_demarcation
claim_level: P3
canonical_status: non_canonical
status: active
target_future_doc:
  - Philosophy/Foundations_Annex/10_MentalRepresentation_Interface_Batch.md
  - Philosophy/SRT_Subjecthood_Threshold_Interface.md
related_claims:
  - representation_evidence_ladder
  - sensitivity_vs_representation
  - producer_consumer_functionality
  - adjacent_case_audit
  - classification_threshold_vs_ontological_boundary
  - history_writeback
  - bearer_formation
tags:
  - representation
  - gradualism
  - adjacent_cases
  - threshold_audit
  - information_processing_complexity
  - history_bearing_state
  - bearer
layer: operations
epistemic_layer: bridge
claim_mode: hardening
canonical: false
type: theory_hardening_patch
---

# SRT Philosophy Patch PH-MR01: Representational Gradualism / Adjacent-Case Audit v0.1

> **Status:** P3 philosophy-of-mind / mental-representation hardening patch.  
> **Canonical caution:** this patch does not redefine representation, `d`, `Psi_f`, `L0/L1/L2`, Stable ISP, bearer, subjecthood, phenomenality or the Real Choice Moment. It imports an audit method and records one SRT-side research hypothesis.

## 0. Source anchor

Peter Schulte's 2026 *Erkenntnis* paper argues that traditional necessary-and-sufficient boundaries between mere sensitivity and genuine representation face a `problem of adjacent cases`.

Source-level route:

```text
representational status should track genuine representational explanatory value
-> a proposed threshold C should correspond to an explanatory tipping point
-> compare the strongest C-negative case with the weakest C-positive case
-> if explanatory practice shows no discontinuity there,
   C is under pressure as a natural boundary
-> scientific practice instead appears to move gradually toward representational modeling
-> representationality may itself be graded.
```

Schulte then proposes sensory information-processing complexity as a broad parameter of degree, while explicitly acknowledging that complexity alone is unlikely to be sufficient and leaving memory, learning and multisensory integration for future work.

## 1. Existing SRT position that must be preserved

Current SRT Mental Representation work already separates evidence dimensions such as:

```text
Sensitivity
-> Specificity
-> Invariance
-> Downstream functionality
```

and rejects:

```text
Decode(X | R) > 0
!=
StrongRep(R, X).
```

PH-MR01 adds a second issue:

```text
E_rep = evidence strength for a representation attribution
```

must be distinguished from:

```text
R_deg = hypothesized degree of representational organization.
```

The first is epistemic; the second is ontological/mechanistic.

## 2. PH-MR01-A — adjacent-case audit

Whenever an SRT bridge proposes a binary threshold `C` for representation-like organization, bearer admission, agency or another thickened status, pressure-test the threshold with adjacent cases before treating it as a natural boundary.

Minimal audit:

```text
choose condition C
-> identify S_minus: maximally developed relevant case with C = 0
-> identify S_plus: minimally developed relevant case with C = 1
-> match neighboring dimensions as closely as possible
-> compare the relevant explanatory / causal / behavioral / historical change
-> ask whether crossing C produces the discontinuity the theory claims.
```

Compact diagnostic:

```text
C(S_minus) = 0
C(S_plus)  = 1

Delta E = E_target(S_plus) - E_target(S_minus)
```

If a well-matched comparison yields no corresponding discontinuity in `E_target`, then `C` is under pressure as a **fundamental natural boundary**.

This is a methodological audit, not a theorem that all natural thresholds are impossible.

## 3. PH-MR01-B — classification cutoff != ontological phase boundary

SRT should preserve:

```text
practical classification threshold
!=
fundamental ontological phase boundary.
```

A research protocol may define:

```text
R_deg > R_c -> call the system representational for task T
```

or:

```text
B_strength > B_c -> bearer candidate for protocol P
```

without asserting a metaphysical discontinuity exactly at the cutoff.

This is especially relevant to subjecthood work: operational admission rules can coexist with graded precursor organization.

### Guard

Do not infer:

```text
graded structural formation
-> graded actuality of every event.
```

Keep:

```text
graded formation / strength of an organization
!=
graded actuality of a particular history-producing event.
```

No weakening of the Real Choice Moment follows.

## 4. PH-MR01-C — information-processing complexity is not representation by definition

Schulte's positive proposal is useful as an external pressure model, but SRT should not adopt:

```text
more information-bearing state families
+ more systematic causal relations
=
more representation
```

as a definition.

The modified-rifle case is the key negative control:

```text
trigger state
+ safety state
-> logical conjunction
-> firing.
```

The mechanism is structurally richer than a one-input trigger, but semantic content attribution does not obviously become more explanatorily necessary merely because one extra causal dependency is present.

SRT should therefore preserve existing requirements such as:

```text
specificity
+ invariance where relevant
+ downstream consumer use
+ task-relative explanatory gain.
```

Information-processing complexity may correlate with representational organization, but PH-MR01 does not admit it as a sufficient condition or scalar definition.

## 5. Mapping to the existing Mental Representation interface

| Existing SRT item | Schulte pressure | PH-MR01 hardening |
|---|---|---|
| `Sens` | mere sensitivity is insufficient | preserve as low-level evidence only |
| `Spec` | richer internal structure may support more determinate content | do not infer representation from relation-count alone |
| `Inv` | perceptual constancy is one route to distal invariance | constancy is not a unique representation threshold |
| `Func` | representation should earn explanatory keep | strengthen task-relative downstream-use requirement |
| producer -> representation -> consumer | alternative to sensory-system gate | compatible with Schulte's own complexity caveat |
| task underdetermination / offline need | Burge privileges one underdetermination pattern | treat underdetermination as one pressure, not a universal border |
| evidence ladder | evidence is already graded | keep epistemic grading separate from ontological gradualism |

## 6. PH-MR01-D — history-bearing recursive state as P3 candidate refinement

This claim is **SRT-side**, generated from comparison of Schulte's cases; it is not attributed to Schulte.

The desert-ant home-vector example exposes a distinction between:

```text
static multi-input integration
```

and:

```text
history-bearing recursive updating.
```

Compare:

```text
modified rifle:
Y_t = F(X_t)
```

with:

```text
H_(t+1) = G(H_t, X_(t+1)).
```

The second architecture contains a state `H_t` that compresses prior interaction history and becomes an input to later processing.

Candidate SRT route:

```text
past selective / interaction history
-> retained relational state H_t
-> H_t changes weighting / interpretation of present differences
-> current consequence rewrites H_t
-> future accessibility / selectability changes.
```

Research hypothesis:

> Representational explanatory necessity may increase not merely with the number of internal relations, but when a reusable internal relation becomes historically recursive and counterfactually relevant to later processing.

### Strong caution

Do not promote:

```text
history-bearing state = representation
memory = representation
recursive state = L2
```

without the existing specificity/functionality/consumer-use gates. Schulte himself only lists memory as future work.

## 7. PH-MR01-E — representation axis != bearer axis != phenomenality axis

Schulte brackets phenomenal consciousness. SRT should preserve an even stricter decomposition:

```text
representation-bearing organization
!= bearer
!= experiencer.
```

A system may have:

```text
stable distal content
+ cross-context reuse
+ recursive historical updating
```

without thereby establishing:

```text
same-unit consequence return
+ stake ownership
+ maintained bearer boundary
+ phenomenal for-me-ness.
```

Crosswalk:

```text
representation axis:
specificity / invariance / consumer use / reusable content / possible historical recursion

bearer axis:
consequence return / same-unit writeback / future-selectability change / maintained boundary

phenomenality axis:
open necessity problem.
```

The axes may covary but are not identified.

## 8. Formal adjacent-case template

For a candidate threshold `C`:

```text
S_minus = nearest relevant system with C = 0
S_plus  = nearest relevant system with C = 1
```

Match as far as possible:

```text
M = <task, environment, output demand, available cues,
     history depth, consumer structure, control authority>
```

and compare:

```text
Q = <representational explanatory gain,
     causal-use gain,
     behavioral generalization gain,
     historical efficacy gain>.
```

A threshold is under pressure when:

```text
C changes discretely
but
Q does not show the corresponding discontinuity
under sufficiently matched M.
```

This plural template intentionally avoids replacing one unearned scalar boundary with another.

## 9. Operational consequences

### 9.1 Constancy versus cue integration

Compare systems matched for task performance where one uses perceptual constancy and another reliability-weighted cue integration.

Question:

```text
Does representational attribution become more explanatorily indispensable exactly at constancy?
```

Schulte predicts no unique tipping point.

### 9.2 Static integration versus historical recursion

Construct matched systems:

```text
A: current multi-cue integration only
B: same current cues + retained recursively updated state
```

Test whether historical recursion adds independent value for:

- cross-context generalization;
- downstream consumer prediction;
- behavior under current-cue ambiguity;
- counterfactual dependence on past interaction history.

If no independent increment survives current-state controls, PH-MR01-D should be weakened.

### 9.3 Near-threshold bearer tests

For future operational bearer cutoffs, compare adjacent systems on:

```text
same-unit consequence return
history writeback
future-selectability change
boundary continuity.
```

If these vary smoothly across a cutoff, treat the cutoff as operational unless an independent phase-transition argument exists.

## 10. Boundary cautions

Do not infer from Schulte:

```text
1. representation is numerically measurable by one established scalar;
2. information-processing complexity is sufficient for representation;
3. every complex machine is a representational system simpliciter;
4. path integration proves SRT;
5. home vector = L2;
6. recursive state = bearer;
7. graded representation = graded consciousness;
8. graded bearer formation = graded choice actuality;
9. absence of one representation threshold proves absence of all natural cognitive thresholds.
```

Also preserve:

```text
source-level radical gradualism about representation
!=
SRT-side radical gradualism about every ontological category.
```

## 11. Integration hook

Primary future targets:

```text
Philosophy/Foundations_Annex/10_MentalRepresentation_Interface_Batch.md
Philosophy/SRT_Subjecthood_Threshold_Interface.md
```

Recommended future actions:

1. add an `Adjacent-Case Threshold Audit` after the representation evidence ladder;
2. separate epistemic evidence degree from ontological representational degree;
3. add `information-processing complexity != representation by definition` as a negative control;
4. add history-bearing recursion only as a P3 research hypothesis;
5. add `representation axis != bearer axis != phenomenality axis` to the subjecthood threshold interface.

No canonical Core rewrite is recommended from this source alone.

## 12. Abstract

Schulte's radical gradualism is most useful to SRT as a threshold-audit method rather than as a ready-made scalar theory. His adjacent-case argument asks whether a proposed necessary-and-sufficient boundary actually coincides with a discontinuity in scientific explanatory practice; perceptual constancy, desert-ant path integration and auditory cue integration suggest that representational modeling becomes useful gradually rather than at one privileged mechanism. PH-MR01 imports that audit while keeping the existing SRT representation-evidence ladder intact, separates epistemic evidence strength from ontological degree, rejects information-processing complexity as a sufficient definition, and records a narrower P3 hypothesis that historically recursive reusable states may explain part of the gap between static causal integration and strongly representational organization. Representation, bearer status and phenomenality remain separate axes.
