---
patch_id: PATCH-PHIL-PH-IND05-OCCURRENCE-TRACE-L2-BEARER-EXPERIENCER-DISCRIMINATION
source_ids:
  - SRC-2026-08-16-PHIL-NILSSON-REALM-OF-MIND
domain: philosophy_of_time_individuation_subjecthood_consciousness
claim_level: P3_bridge_hardening
canonical_status: non_canonical
status: active
target_future_doc:
  - Core/SRT_Core_21_Minimal_Axioms.md
  - Core/SRT_Core_21b_Constitutive_Theorems.md
  - Core/SRT_Core_12b_Ontology_L2.md
  - Philosophy/SRT_Causality_Time.md
  - Core_Law/SRT_Individuation.md
  - Philosophy/SRT_Subjecthood_Threshold_Interface.md
  - Philosophy/SRT_HardProblem_Epistemology.md
  - Core/SRT_OPEN_TENSIONS.md
related_claims:
  - primitive_actualisation
  - occurrence_irreversibility
  - anchoring_persistence
  - L2_sedimentation
  - historical_facticity
  - historical_efficacy
  - bearer_individuation
  - continuation_relation
  - subject_position
  - experiencer_open_problem
  - spatial_localization_guard
tags:
  - occurrence
  - trace
  - L2
  - time
  - bearer
  - individuation
  - personal_identity
  - consciousness
  - spatial_localization
  - hard_problem
layer: operations
epistemic_layer: bridge
claim_mode: hardening
canonical: false
type: theory_hardening_patch
id: PATCH-PHIL-PH-IND05-OCCURRENCE-TRACE-L2-BEARER-EXPERIENCER-DISCRIMINATION
---

# SRT Philosophy Patch PH-IND05: Occurrence / Trace / L2 / Bearer / Experiencer Discrimination v0.1

> **Status:** P3 philosophy-of-time / individuation / consciousness hardening patch.  
> **Canonical caution:** this file does not redefine P0 actualisation, P0-02 persistence, P0-03 irreversibility, `L_2`, ontological time, bearer, Stable ISP, subjecthood, consciousness, or personal identity. It records discrimination rules and pressure tests opened by the Nilsson close read together with existing SRT owner language. No bridge statement here may be cited as a new P0/P1 theorem.

---

## 0. Why this patch exists

Nilsson's essay supplies three unusually clean thought experiments:

```text
A. perfect duplicate
B. perfect restoration / time loop
C. total-erasure / Big Crunch
```

The essay uses them to motivate a non-spatial "realm of mind." SRT need not accept that conclusion. Their stronger value is diagnostic: they expose several roles that can be collapsed when `history`, `time`, `location`, `identity`, and `experience` are discussed too quickly.

The main hardening target is therefore:

```text
actual occurrence
!= persistent trace
!= L2 sedimentation
!= bearer-indexed history
!= phenomenal experiencer
```

This patch also extends PH-IND04's non-jump architecture:

```text
Object
!-> Bearer
!-> Selector
!-> Subject
!-> Experiencer
```

by adding a pre-bearer history discrimination surface.

---

## 1. Claim PH-IND05-A — occurrence is not persistence

Current SRT already distinguishes event-level actuality from anchoring persistence. This patch makes the consequence explicit:

```text
Occurred(E)
!=
PersistentTrace(E, t)
```

Loss of a trace does not license:

```text
Occurred(E) -> NeverOccurred(E)
```

A compact pressure-test notation may be used locally:

```text
Actual(E) !-> NeverOccurred(E)
```

where `!->` means that ordinary downstream state change, erasure, forgetting, compensation, restoration, or trace decay does not constitute cancellation of the earlier occurrence.

### Guard

This does **not** require a permanent cosmic record, hidden memory substrate, eternal archive, universal witness, or mental realm.

```text
occurrence irreversibility
!= permanent trace persistence
```

The stronger metaphysical status of past facts remains an open philosophical burden beyond this discrimination.

---

## 2. Claim PH-IND05-B — historical facticity is not historical efficacy

A useful distinction is:

```text
historical facticity:
what became actual

historical efficacy:
how prior selection still changes later selection conditions
```

Then:

```text
historical facticity
!= historical efficacy
```

A past event may be factive without retaining detectable causal efficacy at a later audit point.

By contrast, `L_2` is strongest when read as sedimented historical efficacy: a path-history that remains stable, inheritable, re-enterable, hysteretic, or constraining for future selection.

### L2 guard

```text
L2
!= cosmic archive of every occurrence
```

and:

```text
trace loss
!-> occurrence cancellation
```

This patch therefore pressures any wording that makes ontological time depend on the indefinite survival of every event-level trace.

---

## 3. Claim PH-IND05-C — a four-stage history ladder

Use the following P3 discrimination ladder:

```text
H0 actual occurrence
H1 persistent trace / anchoring
H2 L2-grade sedimentation / scaffold
H3 bearer-indexed history
```

### H0 — actual occurrence

Question:

```text
Did a determinate difference actually occur?
```

This is nearest to P0-01 / EX-A and does not require stable objecthood or a subject.

### H1 — persistent trace

Question:

```text
Does the occurrence leave a continuing record, maintenance condition,
parameter change, environmental change, or other detectable persistence?
```

H1 may decay to zero without rewriting H0 as never having occurred.

### H2 — L2-grade sedimentation

Question:

```text
Does history continue to alter later accessibility, friction,
transition structure, hysteresis, inheritance, or scaffold conditions?
```

Not every H1 trace is L2-grade.

### H3 — bearer-indexed history

Question:

```text
Did the consequence return to the same continuing bearer,
write into that bearer's history,
and alter that bearer's future selectability?
```

Not every L2 scaffold is the history of a phenomenal or even subject-like bearer.

### Guard

```text
H0 !-> H1 !-> H2 !-> H3
```

Each transition requires new evidence and may fail.

---

## 4. Claim PH-IND05-D — state identity is not historical identity

Nilsson's restoration thought experiment is a clean negative control against:

```text
same state
=
same history
```

SRT-side guard:

```text
State(X_t0) = State(X_t2)
!->
HistoricalIdentity(X_t0, X_t2)
```

A restoration is itself a new occurrence under P0-03-style irreversibility. Therefore:

```text
configuration identity
!= trajectory identity
```

and:

```text
perfect restoration
!= erasure of having-restored
```

This does not decide all metaphysical questions about recurrence or eternalism. It only blocks state equality from doing the work of historical identity.

---

## 5. Claim PH-IND05-E — spatial separation is neither sufficient nor obviously necessary for bearer individuation

Nilsson is useful in pressuring the naive rule:

```text
x_B1 != x_B2
->
B1 and B2 are distinct subjects
```

SRT should instead audit the closure relation.

Spatial separation is often a strong empirical proxy because physically separated organisms typically have partially independent:

```text
resource closure
injury closure
sensory closure
history writeback
future action space
```

But the constitutive bearer question is different:

```text
where do consequences close?
```

Therefore retain:

```text
spatial separation
!= bearer individuation criterion
```

and also:

```text
distributed physical realization
!-> multiple bearers
```

A physically distributed process could remain one bearer candidate if the relevant consequence/history closure is genuinely common at the declared scale.

---

## 6. Claim PH-IND05-F — counterfactual consequence separability as a bearer-branching diagnostic

For two candidate continuations `B1` and `B2`, define only as a test-local P3 diagnostic:

```text
counterfactual consequence separability
```

The diagnostic asks whether there exists an admissible event/intervention `E` such that:

```text
E changes Omega_B1
while the same consequence does not close on B2
```

and, symmetrically, an admissible event can change `Omega_B2` without the same consequence closing on `B1`.

Here `Omega_B(t)` denotes the bearer-relative reachable future state/action/choice space already used in adjacent SRT bearer hardening work.

Stronger bearer-branching evidence is:

```text
independently closable consequences
+ independently writable histories
+ independently alterable future selectability
+ maintained boundary / closure continuity
-> stronger evidence for B1 != B2
```

### Boundary

This is not a necessary-and-sufficient theorem. It may fail for tightly coupled systems, partial fission, shared-control systems, collective bearers, split-brain edge cases, or ambiguous unit boundaries.

Most importantly:

```text
two bearers
!-> proven two experiencers
```

PH-IND04 remains controlling on the final phenomenality jump.

---

## 7. Claim PH-IND05-G — qualitative identity does not establish numerical identity

The duplicate case must distinguish:

```text
qualitative identity
```

from:

```text
numerical identity
```

Even if two candidate systems instantiate matching:

```text
state
memory report
behavior
phenomenal-character description
```

that does not by itself license:

```text
experience-token(B1) = experience-token(B2)
```

Safe SRT statement:

```text
qualitatively identical phenomenal character
!-> numerically identical experience-token
```

This is an anti-overreach guard, not a theorem that two experiencers have already been established.

---

## 8. Claim PH-IND05-H — continuation may branch without strict identity branching

Perfect copying pressures personal-identity language.

Let pre-branch process `P` have history `H_P`, then split into `B1` and `B2`:

```text
        H_P
         |
      branch
      /    \
    B1      B2
```

Both may inherit the pre-branch history in a meaningful continuation relation:

```text
Continuation(B1, P)
Continuation(B2, P)
```

while:

```text
B1 != B2
```

Therefore SRT should not equate:

```text
shared memory
state similarity
historical inheritance
continuation relation
```

with strict same-bearer numerical identity.

### Open burden

SRT currently has stronger resources for tracking one continuing Stable ISP than for characterizing legitimate fission / branching continuation. This remains a P3 individuation pressure point rather than a resolved personal-identity theory.

---

## 9. Claim PH-IND05-I — Where-question typing

The question "where is mind / experience / the past?" is under-typed. Use the following discrimination surface:

```text
WHERE-P  physical realization
WHERE-C  causal propagation
WHERE-B  consequence-return and history-writeback closure
WHERE-S  subject-relative / indexical perspective position
WHERE-E  phenomenal locus / for-me-ness
```

### Core guards

```text
WHERE-P != WHERE-B != WHERE-E
```

and:

```text
physical localization
!-> bearer individuation
!-> phenomenal localization
```

A question about where a neural process is implemented is not yet a question about which bearer owns its consequences, and neither automatically answers for whom there is phenomenality.

---

## 10. Claim PH-IND05-J — experienced space, subject position, and physical spacetime must remain separated

Nilsson's strongest sentence is effectively:

```text
experience does not require space
but space requires experience
```

SRT should split three levels:

```text
phenomenological / experienced space
representational / embodied spatial model
physical spacetime
```

Safe bridge:

```text
bearer-relative perspective
may structure here/there, near/far, reachable/unreachable experience
```

But block:

```text
experienced space is constructed
-> physical spacetime is constructed by experience
```

and:

```text
spacetime is emergent
-> spacetime emerges from consciousness
```

SRT Physics remains bridge-governed and does not require a conscious observer for physical realization-event candidates.

---

## 11. Relation to ontological time

Current SRT distinguishes parametric time from ontological time and links ontological time to irreversible selection history.

PH-IND05 recommends a narrower hierarchy:

```text
occurrence asymmetry
-> minimum historical direction

persistent / sedimented history
-> L2 temporal structure and reconstructable historical constraint
```

This prevents the stronger reading:

```text
ontological time exists only while a durable trace of every event survives
```

Candidate guard:

```text
ontological arrow
!= memory
!= clock time
!= subjective duration
```

### Canonical caution

This patch does not rewrite P1-T02. It opens an owner-level audit: whether phrases such as "memory horizon," "historical record," or "L2 accumulation" are being used for both occurrence asymmetry and surviving historical efficacy.

---

## 12. Relation to L2

Future L2 hardening should preserve the owner's strongest sentence:

```text
L2 is not an archive
```

and sharpen it with:

```text
Occurrence asks what became actual.
L2 asks what prior selection continues to do.
```

Candidate discrimination:

```text
L2-grade history
requires continuing structural efficacy
not merely the proposition that an event once occurred
```

No new L2 primitive is created here.

---

## 13. Relation to PH-IND04 and PH-CONSC03

PH-IND05 extends, but does not replace, the existing role ladder:

```text
Object
!-> Bearer
!-> Selector
!-> Subject
!-> Experiencer
```

The combined pressure surface is:

```text
Occurrence
!-> Persistent trace
!-> L2-grade sedimentation
!-> Bearer-indexed history
!-> Subject-position
!-> Experiencer
```

The main anti-idealism and anti-materialism virtue is symmetrical:

```text
neural location
!-> experiencer

non-spatial facticity
!-> mind-substance / realm of mind
```

SRT should not solve one illicit jump by replacing it with another.

---

## 14. Failure cases / pressure tests

### Test A — total trace erasure

Suppose:

```text
Occurred(E) = true
PersistentTrace(E,t*) = 0
```

Question:

```text
Does the theory preserve occurrence without inventing a hidden archive?
```

Failure mode: defining facticity as current record availability.

### Test B — exact state restoration

Suppose:

```text
State(t0) = State(t2)
```

after a non-trivial path.

Question:

```text
Does the theory preserve trajectory difference without smuggling it into current-state variables?
```

Failure mode: state identity silently becoming history identity.

### Test C — perfect duplicate

Suppose two candidates have matched current state and matched pre-branch history.

Question:

```text
Can bearer individuation be audited through consequence closure
without using spatial distance as the definition?
```

Failure mode 1: spatial counting by fiat.  
Failure mode 2: qualitative identity treated as numerical identity.  
Failure mode 3: two bearers treated as proof of two experiencers.

### Test D — distributed common closure

Suppose a system is realized across spatially distant nodes but consequences and history genuinely close on one continuing organization.

Question:

```text
Does the theory avoid multiplying bearers merely because physical support is distributed?
```

### Test E — branching continuation

Suppose one stable history-bearing process fissions into two independently continuing closures.

Question:

```text
Can the theory distinguish shared historical inheritance from strict same-bearer identity?
```

---

## 15. Non-negotiable guards

```text
non-spatial != mental
space non-fundamental != space consciousness-dependent
past facticity != mental storage
occurrence != persistence
persistent trace != L2-grade history
L2 != permanent world archive
state identity != historical identity
spatial separation != bearer individuation criterion
qualitative identity !-> numerical identity
shared history != same future bearer
bearer != experiencer
physical localization != phenomenal localization
```

---

## 16. Final synthesis payload

Retain this compact package for future owner hardening:

```text
What occurred?
What persists?
What still constrains?
Whose history is it?
For whom, if anyone, is it experienced?
```

These are five different questions.

And:

```text
Occurrence
!-> Persistent trace
!-> L2 sedimentation
!-> Bearer-indexed history
!-> Experiencer
```

The Nilsson source is useful because it makes the collapse of these questions visible. It does not license SRT to adopt a "realm of mind" ontology.
