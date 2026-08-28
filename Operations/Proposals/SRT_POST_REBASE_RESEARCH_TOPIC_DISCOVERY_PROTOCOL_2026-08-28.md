---
id: SRT-OPS-PROPOSAL-POST-REBASE-RESEARCH-TOPIC-DISCOVERY-PROTOCOL-20260828
type: proposal
status: active_planning
date: 2026-08-28
layer: meta
epistemic_layer: os
claim_mode: governance
canonical: false
dependency:
  - Operations/Proposals/SRT_SELECTION_FIRST_ARCHITECTURE_REBASE_MASTER_PLAN_2026-08-28.md
  - Operations/Audits/SRT_SELECTION_FIRST_REBASE_OWNER_MATRIX_2026-08-28.md
  - Governance/SRT_CLAIM_LADDER.md
  - Core/SRT_Core_24_Discriminating_Predictions.md
  - Core/SRT_OPEN_TENSIONS.md
tags: [ResearchProgramme, TopicDiscovery, Novelty, Subtraction, D2, Publication, VenueFit]
---

# Post-Rebase Research Topic Discovery Protocol — 2026-08-28

> **Boundary:** non-canonical research-program governance. This protocol is activated only after the relevant rebase owners have stabilized enough to support comparison. It does not select a paper topic, does not promote any novelty claim, and does not treat publication fit as evidence for theory quality.

---

## 0. Purpose

Replace the workflow:

```text
venue / call appears
-> find an SRT angle
-> search for novelty around that angle
-> patch theory to fit
```

with:

```text
landed SRT architecture
-> recover candidate intuitions
-> subtract current SRT owners
-> subtract neighboring theories
-> derive residual consequences
-> rank research questions
-> select paper form
-> select venue
```

The protocol is intentionally venue-last.

---

## 1. Candidate intake

A candidate research question may enter the pool from:

1. source-intuition recovery;
2. owner-level open tensions;
3. failed or partial D2 worklines;
4. comparative architecture gaps;
5. external evidence that creates pressure, not merely support;
6. formal inconsistencies exposed by the rebase;
7. cross-domain cases that force two SRT roles apart.

Do not admit a candidate whose only basis is:

```text
interesting phrase
popular current topic
journal special issue
new vocabulary
weak analogy to SRT
```

---

## 2. Candidate card

Every candidate gets one card with the following fields.

```text
ID
one-sentence research question
source intuition / trigger
current SRT owner(s)
claim level ceiling
minimal SRT dependency chain
nearest neighboring theories
already-owned / prior-art portion
residual claim after subtraction
strongest rival
prospective failure case
possible empirical / logical / comparative discriminator
publication mode candidate
status
```

Allowed status:

```text
RAW
OWNER-SUBTRACTED
EXTERNALLY-SUBTRACTED
DERIVATION-READY
D2-READY
PHILOSOPHICAL-SURPLUS-READY
PAPER-A
PAPER-B
PAPER-C
NO-GO
```

---

## 3. Gate 1 — owner subtraction

Question:

> Is the apparent novelty actually already present somewhere else in SRT?

Mandatory checks:

- canonical owner;
- compact core;
- current bridge / patch owners;
- integration hooks;
- open tensions;
- recent decision packets;
- book/source intuition;
- material registry where the candidate originated from external reading.

Failure condition:

```text
candidate = duplicate owner wording
```

Disposition:

```text
NO NEW TOPIC
route to synchronization / exposition only
```

---

## 4. Gate 2 — neighboring-theory subtraction

Do not compare slogans. Compare roles and dependencies.

For every candidate, build the smallest role-matched rival package able to reproduce the target.

At minimum ask:

```text
Does the rival have an equivalent primitive role?
Does it generate the same individuation?
Does it already contain history / memory / autonomy / viability?
Does it already contain the relevant boundary criterion?
Does it already distinguish the same unity / ownership relation?
Does it make the same negative non-jump claim?
```

If yes, score the candidate as convergence unless an additional downstream consequence remains.

### Fairness rule

Never score as SRT surplus a premise that is simply withheld from the rival.

If the candidate wins only because:

```text
SRT is allowed history but rival is frozen memoryless
SRT is allowed a boundary but rival is denied one
SRT receives a target-bearing definition the rival does not
SRT includes phenomenality while rival is asked only for function
```

classify:

```text
INVALID SURPLUS / ROLE MISMATCH
```

---

## 5. Gate 3 — derivability

After subtraction, ask:

> Does the residual claim actually follow from current SRT owners?

Use three outcomes.

### D-A — derivable

The claim follows from landed SRT premises plus declared bridge assumptions.

### D-B — candidate extension

The claim requires a new P2/P3 construct but is independently motivated and has failure conditions.

### D-C — novelty by invention

The claim becomes novel only after adding a bespoke construct introduced to win the comparison.

Disposition:

```text
D-C -> NO-GO for current paper
```

A future theory-development project may still investigate it, but it cannot be advertised as an existing SRT consequence.

---

## 6. Gate 4A — scientific discriminator

For scientific candidates, apply Core 24 D2 discipline.

Require prospectively frozen:

1. bounded rival family;
2. common intervention / observation protocol;
3. `O_SRT`;
4. `O_R` with `O_SRT != O_R`;
5. symmetric failure conditions;
6. no post-outcome widening.

### Strong-rival rule

The rival receives all generic mechanisms reasonably available in the neighboring literature.

Examples:

```text
history candidate -> rival may receive latent persistent history
bearer candidate -> rival may receive autonomy, viability, consequence return
object candidate -> rival may receive process identity / dynamical boundary
neural-unity candidate -> IIT may receive its exclusion / complex criterion
access candidate -> workspace rival may receive memory / planning / report broadcast
```

The SRT increment must survive after these are granted.

### Stop rule

If no prospective disagreement can be derived before simulation / data inspection:

```text
SPEC-STAGE NO-GO
```

Do not run the experiment merely to create a result.

---

## 7. Gate 4B — philosophical / theoretical surplus

Not every worthwhile paper requires D2.

A philosophical topic may survive if it provides at least one of:

```text
new dependency ordering
new incompatibility result
new non-equivalence between established constructs
new typed decomposition that dissolves a false dilemma
new explanatory burden that materially changes how rival theories are compared
new impossibility / circularity result
```

But it must be stronger than:

```text
renaming
analogy
literature synthesis
"SRT can also explain this"
```

Required failure question:

> What would make the proposed dependency distinction collapse into an existing theory's vocabulary without loss?

---

## 8. Gate 5 — research-value score

Score 0-3 on each axis.

| Axis | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| Novelty after subtraction | role-isomorphic | mostly known | residual difference | strong residual architecture |
| SRT derivability | bespoke add-on | weak bridge | supported P2/P3 | direct landed dependency |
| Failure clarity | none | vague | explicit | symmetric / decisive |
| Empirical/theoretical leverage | no new consequence | re-description | useful discriminator | high-value D2 / theorem |
| Owner maturity | unstable | partial | mostly stable | fully routed |
| Cross-domain reach | none | local | 2 domains | multiple domains without scope inflation |
| Venue independence | call-driven | venue-shaped | topic-first | clearly valuable without venue |

Maximum = 21.

Suggested disposition:

```text
17-21 -> PAPER-A
13-16 -> PAPER-B
9-12  -> PAPER-C / bridge synthesis
0-8   -> NO-GO / archive
```

This score does not override a hard failure in novelty, fairness or derivability.

---

## 9. Comparative architecture matrix requirement

Before a PAPER-A topic is approved, its relevant comparison row must be entered into a maintained architecture matrix.

Columns should include:

```text
framework
primitive floor
actualisation / becoming
individuation rule
boundary rule
history role
object identity
autonomy / viability
bearer / ownership
perspective
subject
phenomenality
normativity
empirical burden
```

The candidate's claimed novelty must point to a **specific unmatched dependency**, not merely an empty cell caused by incomplete reading.

---

## 10. Source-intuition mining discipline

Priority is not `find quotable sentences`.

For each source-intuition chapter / note, extract:

```text
intuition
-> structural claim
-> minimal dependency
-> current owner
-> prior-art pressure
-> residual question
```

High-priority first-pass chapters after the architecture rebase:

```text
Q01-Q10
Q16
Q25
Q26
Q27
Q28
```

Possible high-value shapes to look for include, without assuming novelty:

- primitive differentiation before object individuation;
- exclusion whose residual effect depends on what was excluded;
- anchoring versus mere occurrence;
- reality thickness as graded historical efficacy;
- backgrounding / scaffold formation;
- object history versus bearer history;
- consequence ownership versus generic feedback;
- selector-position as historically constituted constraint;
- open transition from `from here` to `for me`;
- theory self-application / self-revision conditions.

---

## 11. Current consciousness / bearer line under this protocol

Current provisional card:

```text
Question:
When a neural theory identifies a whole, what kind of unity has it identified?

Known prior art / subtraction:
IIT -> causal / exclusion unity
GNWT -> access / broadcast unity
enactivism -> autonomous / viability unity
Damasio -> organismic / interoceptive subjectivity
unity literature -> multiple unity taxonomies

Residual SRT candidate:
bearer unity as same-unit consequence ownership / non-outsourcing

Current status:
PAPER-B / unresolved

Reason:
role-matched active-inference / persistent-history rival has not yet been defeated;
D2-IIT current V0-V4 design is not a clean primary duel.
```

Do not promote this topic to PAPER-A until bearer residual survives the rebase and subtraction.

---

## 12. Venue selection rule

Venue comes after topic rank.

For each PAPER-A / PAPER-B candidate, choose venue by the actual contribution:

```text
ontology / metaphysics -> philosophy venue
consciousness taxonomy / explanatory burden -> consciousness / psychology theory venue
computational discriminator -> complex systems / theoretical neuroscience / AI venue
organism / autonomy / individuation -> theoretical biology / cognitive science
formal result -> mathematics / information / systems venue as appropriate
```

A special collection deadline may influence scheduling but must not change the candidate's dependency structure or rival freeze.

---

## 13. Final anti-overfitting rule

> **A publishable topic should be what remains after SRT is forced to give away everything its strongest neighbors already explain.**

If nothing remains for a candidate, record that result. A clean NO-GO is research progress because it prevents the repository from building future papers on duplicated territory.
