---
id: SRT-OPS-PROPOSAL-PH-IND04-OWNER-HARDENING-2026-08-15
type: proposal
status: active
date: 2026-08-15
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: P3_governance
canonical: false
dependency:
  - PATCH-PHIL-PH-IND04-OBJECT-BEARER-SELECTOR-SUBJECT-EXPERIENCER-NONJUMP-LADDER
  - PATCH-PHIL-PH-CONSC04-PHENOMENAL-NECESSITY-ZOMBIE-DELETION
  - SRT-INDIVIDUATION
  - SRT-CORE-13A
  - SRT-CORE-14
  - SRT-PHIL-EPISTEMOLOGY-01
tags: [Governance, OwnerHardening, Individuation, Selector, Subjecthood, Phenomenality, Scaling]
---

# SRT PH-IND04 Owner Hardening — Decision Packet (2026-08-15)

> **Status:** non-canonical governance packet. It records a bounded owner audit triggered by the Levin–Wen negative control and PH-IND04. It does not itself rewrite any canonical owner. Three items are low-risk scope hardenings; one item is an author-level phenomenality decision and must not be smuggled in as a wording cleanup.

---

## 0. Executive result

The close read generated one non-jump ladder:

```text
Object
!-> Bearer
!-> Selector
!-> Subject
!-> Experiencer
```

Audit of the four intended owners produced the following disposition:

| Gate | Owner | Finding | Disposition |
|---|---|---|---|
| H1 | `Core_Law/SRT_Individuation.md` | `sigma_sr` risks carrying more subjecthood burden than its formula warrants | low-risk scope hardening |
| H2 | `Core/SRT_Core_13a_Operator_Basics.md` | generic Ghost Operator is mixed with cognitive attention/interoception realization | low-risk scope hardening |
| H3 | `Core/SRT_Core_14_Dynamics_Scaling.md` | `T-Scale-07` universalizes `D_topo` beyond the domains where topology is clearly identity-relevant | low-risk abstraction hardening |
| H4 | `Philosophy/SRT_HardProblem_Epistemology.md §3.2` | owner currently asserts a constitutive bearing→first-person relation strongly enough to dissolve zombies, while PH-CONSC04 keeps phenomenal necessity open | **author-level decision gate** |

No canonical owner is modified by this packet.

---

## 1. H1 — `sigma_sr`: historical self-conditioning is not a subjecthood scalar

### Current owner structure

`Core_Law/SRT_Individuation.md` defines:

```text
theta_t = theta_t^trace + theta_t^ext

sigma_sr(P,t)
= ||theta_t^trace|| / (||theta_t^trace|| + ||theta_t^ext||)
```

and uses `sigma_sr` as a one-dimensional order-parameter candidate for the transition into a subject-position.

The owner already contains an important guard: `sigma_sr` does not replace P1-T06's four conditions and `sigma_sr < 1` does not prove continued or generative reselectability.

### Hardening pressure

The formula directly measures only a narrower relation:

```text
how strongly the pattern's own prior trace contributes to current operator state
```

Historical self-conditioning can also occur in:

```text
adaptive controllers
learning systems
immune memory
path-dependent materials / processes
```

without independently establishing:

```text
same-bearer non-outsourcable stake
subject-position
phenomenality
```

Therefore the safest interpretation is:

```text
sigma_sr
= candidate order parameter for historical self-conditioning / trace contribution

sigma_sr
!= subjecthood scalar
```

### Recommended owner insertion

Add after `Def-IND-1` / the paragraph explaining why sigma is used:

```text
#### Scope hardening — sigma_sr does not by itself individuate a subject

The self-reference ratio directly tracks the contribution of the pattern's own retained trace to its current operator state. This quantity can become non-zero in historical adaptive systems that are not thereby established as stake-bearing subjects. Therefore sigma_sr is an order-parameter candidate for the transition architecture only when read jointly with the bearer, consequence-return, stake and continued-selectability conditions below. In particular:

historical self-conditioning != subjecthood
sigma_sr threshold crossing != subjecthood by scalar fiat

The first transition should therefore be read as a coupled admission event rather than a one-variable definition: sigma_sr supplies a trace/self-conditioning coordinate, while same-bearer consequence return and non-outsourcable stake do separate work.
```

### Required preservation

Do not change:

```text
P1-T06
three-phase architecture
second-order condensate reading of self-consciousness
sigma_sr symbol namespace
```

Do not introduce a new canonical threshold.

---

## 2. H1b — selector-position and subject-position should be separated analytically

The current owner goes from subjectless selection to subject-position entry. PH-IND04 shows a useful intermediate distinction:

```text
historical operator
-> bearer
-> selector-position
-> subject-position
```

This should **not** become a mandatory universal evolutionary sequence. Its purpose is diagnostic.

### Recommended native paragraph

```text
A history-conditioned selector-position and a stake-bearing subject-position should be distinguished analytically even where they coincide empirically. A continuing bearer may allow its own history to alter later path realization without yet satisfying the full subjecthood burden. Subject-position admission additionally requires that some consequences close on that same bearer as non-outsourcable stakes affecting its continued selectability.
```

Compact guard:

```text
history-bearing control != subjecthood
selector-position != subject-position
```

---

## 3. H1c — stake sensitivity and stake readability should not be collapsed

Current `T-IND-2` includes local directional readability as part of subject-position entry. This may be too cognitively thick if minimal subjecthood is intended to precede reflective self-access.

Keep three levels distinct:

```text
D0  dynamical bias
D1  bearer-stake-coupled bias
D2  self-readable direction
```

with:

```text
D0 != D1 != D2
```

### Recommendation

Do **not** delete the current `epsilon` / directional clause in this pass. Instead add an explicit open-pressure note:

> Does minimal subject-position entry require D2 self-readable direction, or is D1 stake-sensitive path organization sufficient while D2 is a later thickening? Until adjudicated, `T_dir`-like readability must not be inferred from objective stake coupling alone.

This is a boundary question, not a settled correction.

---

## 4. H2 — Core 13A: split generic operator role from cognitive realization

### Current owner wording

Core 13A contains, immediately after the generic parameterized selection map:

```text
Ax-Op-02: Attention Decomposition
G_hat_theta = Attention(d, rho, v)
```

and:

```text
Ax-Op-02b: Dual-Stream Coupling
G_hat_theta = T^intent tensor T^embody * kappa_body
```

with the implication:

```text
attention decides "what is seen"
interoception decides "who is looking"
```

It then gives a broad Embodied Anchoring Necessity Theorem.

### Finding

This sits uneasily beside the same owner’s 2026-08-11 AM-A guard:

```text
G_hat_theta is not a prior entity
and is not the cause of primitive actualisation
```

If `G_hat_theta` is also used in non-cognitive / pre-neural / abstract selection grammar, defining the generic operator as attention plus interoception makes the formal role too cognitively thick and risks reintroducing a tacit prior observer.

### Recommended scope correction

Reclassify the current attention/interoception equations as **cognitive/embodied realization interfaces**, not universal definitions of the generic operator.

Suggested owner wording:

```text
#### Scope note — generic operator versus cognitive realization

Ax-Op-01 supplies the generic formal role of the parameterized selection map. The attention and interoceptive decompositions below are realization hypotheses for cognitive / embodied systems; they do not define the operator at every scale and do not imply that primitive actualisation requires a pre-existing observer, attention system or interoceptive self-model.

Generic operator role
!= cognitive attention realization
!= phenomenal subject
```

### Specific wording downgrade

Replace the universal reading of:

```text
attention decides "what"
interoception decides "who"
```

with:

```text
In the declared cognitive realization, attention can contribute to content gating while interoceptive coupling can contribute to bearer/self anchoring. Neither contribution alone establishes a universal selector origin or phenomenality.
```

### T-Op-EAN boundary

The Embodied Anchoring Necessity Theorem should be read as a biological/cognitive bridge hypothesis unless a substrate-neutral definition of embodiment is independently supplied.

Do not infer:

```text
kappa_body = 0 -> metaphysically no L1 actualisation
current AI is an "actual zombie" by theorem
interoception is required for every SRT selector
```

without separate promotion.

---

## 5. H3 — Core 14: `D_topo` is too specific for a universal identity criterion

### Current owner

`T-Scale-07` currently states:

```text
I_Delta_t(X)
= 1[ D_topo(X_t, pi_Delta_t(X_(t+Delta t))) < epsilon_theta ]
```

and says object identity is defined by a topological gluing condition.

### Finding

This is natural for topological phases / string-net excitations and may be useful for some dynamical objects. It is not obviously the correct invariant for:

```text
organisms
persons
institutions
concepts
```

The cross-scale owner already uses a safer principle in P3-Scale-01: declared maps, retained observables, norms and tolerances, without mechanism or consciousness identity.

### Recommended abstraction

Introduce a domain/regime-indexed invariant family:

```text
J_B(X) = identity-relevant invariant family for X under declared regime B
```

and a domain-appropriate discrepancy:

```text
D_{J_B}(X_t, pi_Delta_t(X_(t+Delta t)))
```

Then rewrite the general persistence candidate as:

```text
I_Delta_t^B(X)
= 1[ D_{J_B}(X_t, pi_Delta_t(X_(t+Delta t))) < epsilon_B ]
```

with `D_topo` retained as an important special realization:

```text
D_topo = one physical instance of D_{J_B}
```

### Boundary

This does **not** imply that identity is arbitrary or observer-created. `J_B` must be declared and independently justified by the domain’s persistence / re-identification practice and consequences.

Do not infer:

```text
same invariant grammar = same mechanism
same identity grammar = same bearer
same persistence = same subject
```

---

## 6. H4 — Hard Problem §3.2 is an author-level decision gate

### Current owner commitment

`Philosophy/SRT_HardProblem_Epistemology.md §3.2` is titled:

```text
承担即第一人称读数（反哲学僵尸）
```

and asserts, in substance:

```text
bearing and subject presence are constitutively related
felt presence is the internal structure of bearing
an otherwise complete bearer without phenomenal presence is not a coherent SRT possibility
```

### Later hardening pressure

PH-CONSC03 and PH-CONSC04 deliberately separate:

```text
Selector != Bearer != Concern Domain != Experiencer
```

and:

```text
B_s = structural bearing candidate
B_p = phenomenal bearing candidate
B_s -> B_p is not yet a proven theorem
```

PH-CONSC04’s Z6 asks whether a system can satisfy all current subject-position conditions while phenomenality is explicitly deleted.

This is not a mere terminological mismatch. It is a substantive choice about the hard problem.

### Decision Gate HP-B

Choose one of two coherent positions.

#### HP-B-A — retain constitutive identity as a foundational commitment

Keep the strong §3.2 stance, but make its status explicit:

```text
Structural bearing and phenomenal presence are postulated / defended
as two access modes of the same situated event.
```

Consequences:

- Z6 is rejected as conceptually incoherent by SRT.
- SRT owes a non-circular constitutive argument explaining why `B_s + no PH` is contradictory.
- The claim must be labeled philosophical / constitutive, not empirical neuroscience.
- PH-CONSC04 becomes a challenge that the owner answers rather than an open guard.

#### HP-B-B — downgrade phenomenal necessity and keep Z6 open

Change §3.2 from a solved anti-zombie claim to a constitutive bridge hypothesis:

Suggested title:

```text
3.2 承担与第一人称在场：构成性候选，而非已闭合定理
```

Suggested core:

```text
SRT has a structural account of where consequences close and how they rewrite the future of a continuing bearer. A stronger constitutive hypothesis proposes that phenomenal first-person presence is the internal mode of such fully situated bearing. This hypothesis is not yet established by bearer formation alone. Until the SRT-zombie deletion test is closed non-circularly, structural bearing and phenomenal bearing remain analytically distinct.
```

Then use the three-arrow burden:

```text
Structural Bearing
->? Indexical For-P
->? Phenomenal For-me
->? Qualitative Character
```

Consequences:

- HP-A perspective-center individuation remains a major SRT strength.
- HP-B phenomenal necessity remains open.
- The theory avoids circularly defining bearing as experience.
- Qualitative-character derivation remains separately open.

### Recommendation

**Recommend HP-B-B.**

Reason: it preserves all of SRT’s current positive work on bearer formation, stake, consequence return and reselectability while removing the single largest overclaim in the consciousness architecture. It also keeps the theory falsifiable / criticizable rather than solving Z6 by definition.

This recommendation is an author-level theory choice. It should not be landed into the foundational owner as a deterministic consistency repair without explicit adoption.

---

## 7. Cross-owner synthesis if H1–H3 and HP-B-B are adopted

The resulting architecture would read:

```text
primitive actualisation
-> objectification
-> historical operator
-> continuing bearer
-> selector-position
-> stake-bearing subject-position
-> reflective self-model
-> phenomenality ?
```

with:

```text
historical self-conditioning != subjecthood
attention realization != generic selector definition
object persistence != bearer persistence
bearer persistence != phenomenality
```

and the remaining consciousness burden:

```text
Structural Bearing
->? Indexical For-P
->? Phenomenal For-me
->? Qualitative Character
```

---

## 8. No-jump acceptance tests

Any future owner integration should pass all of the following:

```text
T1  A stable quasiparticle can pass object identity without becoming a bearer.
T2  A historical adaptive controller can have trace-conditioned behavior without becoming a subject by sigma_sr alone.
T3  A persistent AI can have memory/self-model without subjecthood being inferred before same-bearer stake audit.
T4  A subject-position candidate can exist without reflective self-identification.
T5  Stable ISP does not automatically prove phenomenality unless HP-B-A is explicitly adopted and defended.
T6  D_topo is not silently used as the identity metric for every domain.
T7  Attention/interoception equations are not cited as the universal origin of G_hat_theta.
T8  Cross-scale structural correspondence does not imply unit/mechanism/subject/consciousness identity.
```

---

## 9. Proposed execution order

If adopted:

```text
1. Core_Law/SRT_Individuation.md
   -> sigma scope note + selector/subject distinction

2. Core/SRT_Core_13a_Operator_Basics.md
   -> generic-vs-cognitive scope note

3. Core/SRT_Core_14_Dynamics_Scaling.md
   -> domain-relative identity invariant abstraction

4. Philosophy/SRT_HardProblem_Epistemology.md
   -> execute HP-B author decision

5. Core/SRT_OPEN_TENSIONS.md
   -> retain only unresolved D1/D2 and For-P/For-me questions

6. Re-run governance / claim-mode / symbol consistency checks
```

No new canonical symbol is required by this packet.
