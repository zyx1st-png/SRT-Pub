---
id: SRT-OPS-AUDIT-A3-LIVE-CHOICE-POSITIVE-DISCRIMINATOR-GATE-20260816
type: audit_record
status: active
record_stage: executed_a3_design_gate_no_go
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: P3/P4_governance
canonical: false
date: 2026-08-16
dependency:
  - SRT-OPS-AUDIT-A2-REAL-CHOICE-RIVAL-ADJUDICATION-20260816
  - SRT-CORE-21B-CONSTITUTIVE-THEOREMS
  - SRT-T-DIR-CANONICAL
  - SRT-CLAIM-LADDER
tags: [Governance, DifferentialHardening, RealChoice, ExperimentalDesign, Preregistration, RivalModel, NoGo]
---

# A3 — Live-Choice Positive Discriminator Design Gate

> **Role**: decide whether SRT is ready to preregister a `live choice vs script / replay / gradient` D2 experiment after A2 returned `NO-D2`.
>
> **Question**: do we currently possess a positive, outcome-independent manipulation or measurement of `live P1-T05 choice` that (a) does not simply restate the P1 label, and (b) is not already freely representable inside the frozen ordinary causal-history rival?
>
> **Hard boundary**: this is a design-readiness audit. It does not modify P1-T05, does not define a new canonical variable, and does not claim that a future discriminator is impossible.

---

## 0. Verdict

**A3 verdict: `NO-GO FOR EMPIRICAL EXECUTION AT THE CORE REAL-CHOICE LEVEL`.**

A2 correctly identified the next abstract contract:

```text
match ordinary causal-history state Z_R
classify one condition as live and one as script/replay/gradient
predict a future outcome difference under SRT
predict invariance under the rival
```

But the current repository cannot yet instantiate the middle line without circularity.

There is no existing P1/P2/P3 object that simultaneously satisfies all of the following:

1. **positive** — says what is present in a live event, not only what is excluded;
2. **prospective** — can be measured or manipulated before the downstream outcome;
3. **outcome-independent** — is not defined by later flexibility / success / option expansion;
4. **non-tautological** — does not simply say “this is a real choice because P1-T05 says so”;
5. **rival-discriminating** — is not already representable as memory, policy update, stochasticity, meta-learning, generative planning, bearer cost, or internal monitoring in `R_CH`;
6. **failure-bearing** — could be present while SRT's predicted downstream difference fails.

Therefore an immediate experiment would either:

- manipulate an ordinary causal-history variable and rediscover an ordinary causal-history effect; or
- define “live” from the downstream result and become circular; or
- rely on a construct whose own formalization is still open.

The correct next step is **not data collection**. It is a bounded P3 discriminator-design task.

---

## 1. Admission gate for any future D2 experiment

A future experiment may enter execution only if it freezes all six items below **before outcome data are inspected**.

### G1 — positive live-candidate variable

There must be a named, non-canonical operational candidate `L*` with an independent measurement/manipulation rule.

Forbidden definition:

```text
L* = whatever later shows more flexibility / novelty / reselectability
```

### G2 — rival sufficient-state vector

Freeze the rival state:

```text
Z_R = (x, h, pi, c, E)
```

or a stricter domain-specific replacement, with explicit matching tolerances.

### G3 — same-bearer continuity

If bearer continuity matters to the hypothesis, freeze identity / continuity rules before the manipulation. Do not infer continuity from behavioral similarity after the fact.

### G4 — prospective SRT prediction

State, before observation:

```text
O_future(L*) - O_future(control)
```

including sign / ordering / threshold or a distributional prediction.

“Should differ somehow” is insufficient.

### G5 — prospective rival prediction

State what the frozen ordinary rival predicts under matched `Z_R`.

A D2 test requires actual disagreement. If both predict the same direction, the design is not discriminating even if the experiment is interesting.

### G6 — symmetric failure rule

Specify what result pressures SRT and what result pressures the rival. Post-hoc variable addition is not allowed unless it creates a new independently testable prediction.

Until G1-G6 all close, **do not run the experiment as a test of P1-T05 or primitive selection**.

---

## 2. Candidate family C1 — “the system changes its own rule”

### Proposal

Treat online revision of the current mapping / policy as evidence of live choice.

### Why it initially looks promising

It distinguishes fixed script replay from a process that revises how it maps situations to actions.

### Rival absorption test

A2 froze:

```text
pi_{t+1} = G(pi_t, h_{t+1}, x_{t+1})
```

Ordinary adaptive control, reinforcement learning, meta-learning, online system identification, and institutional policy revision can all update a rule through ordinary causal history.

### Verdict

```text
C1 -> NO-GO as a D2 discriminator by itself
```

Rule revision can be a useful P2/P3 marker of generative reselectability, but it does not uniquely operationalize P1-T05 real choice.

---

## 3. Candidate family C2 — “a genuinely new option is generated”

### Proposal

Treat generation of a candidate not present in the earlier explicit option set as the positive live-choice variable.

### Why it initially looks promising

It speaks directly to SRT's non-preformation / candidate-generation intuitions and appears stronger than choosing from a fixed menu.

### Rival absorption test

An ordinary rival may contain:

- a generative model;
- stochastic search;
- compositional planning;
- program synthesis;
- mutation / exploration;
- latent continuous action spaces;
- hierarchical policy expansion.

A candidate can be “new to the explicit menu” while still being inside the support of a predeclared generative process.

### Hidden problem

If “genuinely new” is defined as:

```text
not generated by the rival
```

then the manipulation becomes model-relative and risks defining SRT success by rival failure after the fact.

### Verdict

```text
C2 -> NO-GO in its naive form
```

A narrowed support-expansion test remains a **possible P3 bridge direction**, but only after the rival model class and its pre-event support are frozen quantitatively.

---

## 4. Candidate family C3 — bearer-specific irreversible consequence

### Proposal

Treat non-transferable consequence returning to the same continuing bearer as the positive live-choice variable.

### Why it initially looks promising

This is central to several SRT bridges and to stake / payability reasoning. It also blocks purely external logging from being mistaken for endogenous commitment.

### Rival absorption test

`R_CH` already contains:

```text
b_t = affected / bearer position
c_t = cost / resource / repair-burden state
```

Standard control, homeostasis, viability, active inference, embodied RL, and resource-bounded agent models can all represent same-unit consequence and future resource loss.

### Additional conceptual problem

P1-T05 itself does not currently state bearer-specific consequence as a necessary positive condition. Pass 1.5 showed that importing CG-3 into P1-T05 without a separate argument would be reverse target laundering.

### Verdict

```text
C3 -> NO-GO as a standalone P1-T05 discriminator
```

It remains a strong bridge/stake variable, not an established live-choice primitive.

---

## 5. Candidate family C4 — `T_dir` / self-readability and reorientation

### Proposal

Use self-readability of current direction plus behavioral reorientation as evidence that the event is live rather than scripted.

### Why it initially looks promising

It is closer to the system's own access to direction than external output classification and could, in principle, distinguish internal self-reorientation from fixed execution.

### Current formal burden

The repository already marks `T_dir` as a v0 operational proxy rather than a completed formal object. Its role terms `R_self` and `A_reorient` remain only partly specified, and the independent ODE layer still needs operator-level hardening.

### Rival absorption test

Ordinary models can represent:

- self-monitoring;
- uncertainty estimates;
- confidence / error monitoring;
- internal model update;
- controller switching;
- metacognitive access;
- re-planning.

Without a sharper `T_dir`-specific prediction, increased self-readability does not force D2.

### Verdict

```text
C4 -> NO-GO for a core real-choice D2 test now
```

This candidate should not be experimentally loaded with more proof burden before its own formal audit is closed.

---

## 6. Candidate family C5 — phenomenality / felt authorship

### Proposal

Treat reported or inferred phenomenal authorship as the missing positive live-choice mark.

### Immediate block

HP-B-B has already separated structural bearing from phenomenal bearing. Current SRT does not have a closed theorem that structural bearerhood, stable ISP, or same-bearer consequence implies phenomenal necessity.

Self-report also introduces familiar reportability, demand-characteristic, and metacognitive confounds.

### Verdict

```text
C5 -> HARD NO-GO for P1-T05 discrimination
```

Phenomenality cannot be used to patch the real-choice discriminator while phenomenal necessity itself remains open.

---

## 7. Candidate family C6 — matched output, different generation history

### Proposal

Hold the immediate output fixed while arranging two different generation histories, then test transfer under a novel perturbation.

Example:

```text
Condition S: fixed script / cached response yields action A
Condition L: online process also yields action A

then introduce novel perturbation P_new
and compare future adaptation / candidate reopening
```

### Why this is the strongest current design shape

It prevents immediate task success from being the discriminator and forces attention onto later dynamics.

### Why it still does not yet reach D2

If the two histories differ in:

- memory state;
- policy parameters;
- uncertainty;
- latent model state;
- resource state;
- training history;
- representational support;

then an ordinary causal-history rival already predicts different transfer.

Matching only the visible output is not enough.

### Verdict

```text
C6 -> PROMISING DESIGN SHELL, NOT YET EXECUTABLE D2
```

It becomes admissible only after G1-G6 close and the rival sufficient-state matching is made credible.

---

## 8. The only candidate direction worth carrying forward now

Among C1-C6, only a narrowed version of C2+C6 deserves a new design pass:

> **frozen-support expansion under matched causal-history state**.

This is not a new SRT definition. It is a P3 discriminator candidate.

### 8.1 Core idea

Before the focal perturbation, freeze a rival model class `R_frozen` and its supported continuation set:

```text
Supp_R(Z_R)
```

Then construct a later event where:

1. visible immediate performance is matched;
2. measured `Z_R` is matched within declared tolerances;
3. no external code/rule/candidate is inserted during the focal window;
4. the system produces and successfully uses a continuation outside the frozen rival support or outside its preregistered probability floor;
5. the same continuing bearer carries the resulting history into a later novel probe.

### 8.2 Why this could become D2

A frozen rival can make a real prediction:

```text
P_R(out-of-support continuation | Z_R) <= epsilon_R
```

A future SRT bridge would have to predict, before observation, a higher probability or a structurally specified support-expansion event under a declared “live” condition.

### 8.3 Why this is not yet a win for SRT

A flexible generative model may simply have wider support than expected. If the rival support was underestimated, the result pressures rival specification, not automatically the metaphysics.

Therefore the test must include:

- independent rival calibration;
- held-out tasks;
- complexity penalty / preregistered model family;
- no post-hoc support expansion;
- explicit SRT failure condition.

### 8.4 What this candidate is actually testing

At best, initially:

```text
Does the SRT-motivated live-condition variable predict support expansion
beyond a frozen ordinary model class?
```

It does **not** directly test:

```text
Is selection the ontological ultimate?
```

The claim ladder must remain intact.

---

## 9. Required theory work before A4 / experiment execution

The next bounded work package should produce a non-canonical **Live-Choice Discriminator Candidate** with exactly five outputs:

1. `L*` — positive operational variable / relation;
2. `I_L` — intervention or manipulation changing `L*` without defining it by outcome;
3. `R_frozen` — explicit rival model class and calibration protocol;
4. `O_future` — preregistered downstream outcome and direction;
5. `F_SRT` — failure condition under which the SRT bridge is downgraded or withdrawn.

No sixth conceptual axis should be added until these five are complete.

---

## 10. Governance consequence

### Allowed now

- keep P1-T05 as the canonical exclusion / structural boundary;
- keep CG as bounded audit apparatus;
- use A2/A3 to design a P3 discriminator;
- treat frozen-support expansion as a candidate research direction only.

### Not allowed now

- launch a P4 experiment claiming to test P1-T05 directly;
- treat online rule revision, novelty, stake, `T_dir`, or phenomenality as the missing live-choice variable by fiat;
- define “live” from successful transfer after the fact;
- call a future out-of-support event proof of P0 selection irreducibility;
- weaken `R_CH` until SRT wins by construction.

---

## 11. Why this NO-GO is progress

A2 showed that current retrospective cases stop at D1.

A3 now explains why simply collecting a new dataset would likely reproduce the same problem:

```text
no independent positive live variable
-> no clean manipulation
-> no prospective model disagreement
-> no D2
```

The design debt is therefore no longer “we need better evidence.” It is specifically:

> **SRT needs one positive, outcome-independent, rival-constrained operational bridge for live choice.**

That is a much smaller and more actionable burden than trying to prove the whole selection-first metaphysics at once.

---

## 12. Stop rule

A3 stops because:

1. the six most obvious positive-discriminator families have been audited;
2. C1/C3/C4/C5 fail as current D2 discriminators;
3. naive C2 fails through generative-rival absorption;
4. C6 survives only as a design shell;
5. the narrowed C2+C6 support-expansion route is the only retained P3 design candidate;
6. no empirical execution is authorized until G1-G6 and the five-output package in §9 are complete.

**Final A3 verdict:**

> `NO-GO FOR EMPIRICAL EXECUTION AT THE CORE REAL-CHOICE LEVEL.` The current theory is ready to design a positive discriminator, not yet to claim a decisive live-vs-script experiment. The next valid move is a P3 frozen-support / matched-state discriminator specification with an explicit SRT failure condition.