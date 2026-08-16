---
id: SRT-OPS-AUDIT-A2-REAL-CHOICE-RIVAL-ADJUDICATION-20260816
type: audit_record
status: active
record_stage: executed_a2_no_d2
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: P3/P4_governance
canonical: false
date: 2026-08-16
dependency:
  - SRT-GOV-SUB01-SUBTRACTIVE-AUDIT
  - SRT-OPS-AUDIT-SELECTION-IRREDUCIBILITY-RIVAL-TEST-20260816
  - SRT-OPS-AUDIT-SELECTION-IRREDUCIBILITY-PASS1-5-JOINT-REMOVAL-20260816
  - SRT-CORE-21B-CONSTITUTIVE-THEOREMS
  - SRT-UNIFIED-SELECTION-EVENT-AUDIT-PROTOCOL-20260804
tags: [Governance, DifferentialHardening, RealChoice, P1T05, CG, RivalModel, Counterfactual, Intervention, NoD2]
---

# A2 — Real-Choice Rival Adjudication

> **Role**: execute the A2 handoff produced by Pass 1 / Pass 1.5. Compare canonical `P1-T05`, the non-canonical CG five-gate audit, and a frozen strongest ordinary causal-history rival on the same evidence.
>
> **Primary question**: does current SRT produce a counterfactual or intervention prediction that differs from the ordinary causal-history rival, rather than merely a different label?
>
> **Hard boundary**: this record does not alter P0/P1, does not promote CG, does not attach a GOV-SUB01 residue to `selection`, and does not treat absence of current D2 as proof that no future D2 is possible.

---

## 0. Executive verdict

**A2 verdict: `NO-D2 / differential closure not achieved on the current case set`.**

Three judges were kept separate:

```text
Judge S_core = canonical P1-T05 Real Choice Moment
Judge S_CG   = CG-0..CG-4 non-compensable operational audit
Judge R      = frozen ordinary causal-history rival
```

Three cross-domain cases were adjudicated:

1. correct-SHA GitHub transaction;
2. E. coli chemotaxis / methylation-history case;
3. institutional publication acceptance -> production writeback.

The result is consistent across domains:

- `S_CG` can classify bounded event structure and in some cases reaches `SEA-3 qualified`;
- `S_core` does **not** obtain a positive real-choice verdict merely from that result, because P1-T05 explicitly excludes script execution, habit replay, gradient following, or `L2` label optimization as sufficient;
- the frozen ordinary rival reproduces the documented path efficacy, memory/history, consequence accounting, and future-state change without a primitive `selection` variable;
- none of the current cases contains a preregistered intervention for which SRT and the rival predict different observable outcomes.

Therefore the strongest executed divergence is **D1**, not D2:

```text
D1a: S_core and S_CG can classify the same event differently
D1b: SRT-family labels can differ from an ordinary causal-history description
D2 : NOT OBSERVED
D3 : NOT RUN
```

The central scientific consequence is sharper than “we need more data”:

> **Current P1-T05 is a constitutive classification boundary, not yet a differential dynamical law. It tells us that script / habit / gradient / L2 optimization are insufficient for real choice, but it does not yet specify an observable downstream quantity that must differ when all ordinary causal-history state variables are matched.**

Until such a prediction is frozen and tested, the `selection` primitive remains an author-adopted P0 admission, CG remains useful audit technology, and neither may be cited as an independently demonstrated mechanism advantage over ordinary causal-history models.

Formal GOV-SUB01 residue for primitive `selection`: **UNASSIGNED**.

---

## 1. Why A2 uses three judges

Pass 1.5 established a bounded negative sufficiency result:

> a deterministic scripted GitHub transaction can pass the current five-gate CG audit while P1-T05 still withholds real-choice standing absent independent live-choice evidence.

Therefore the earlier two-judge plan:

```text
SRT/CG vs ordinary rival
```

would already be invalid, because it silently treats `P1-T05` and CG as the same judge.

A2 instead freezes:

### 1.1 `Judge S_core`

Authority: `Core/SRT_Core_21b_Constitutive_Theorems.md P1-T05`.

Positive clause:

```text
live L0 -> L1 anchoring event
+
what is selected genuinely constrains future selection space
```

Negative clause:

```text
script execution
habit replay
gradient following
L2 label optimization
```

are not sufficient by themselves.

### 1.2 `Judge S_CG`

Authority: `03_Bridges/SRT_Selection_Event_CompactCore.md` + unified audit protocol.

Positive operational package:

```text
CG-0 / DMF >= 2
CG-1 / NER >= 2
CG-2 / PEF >= 2
CG-3 / CBP >= 2
CG-4 / HEF >= 3
```

with same-event / same-boundary / compatible-timescale and non-compensation requirements.

Passing this package licenses only a **bounded selection-event candidate**. It is P2-P3 apparatus, not a P1 definition.

### 1.3 `Judge R`

A strong ordinary rival is frozen below. It is allowed to represent causal state, memory, hysteresis, feedback, adaptive policy, cost, and future reachability. It is not allowed to add a case-specific hidden variable after seeing the SRT verdict.

This makes A2 difficult in the intended way: SRT must earn a different prediction, not win because the rival was artificially weakened.

---

## 2. Frozen rival: ordinary causal-history transition model

### 2.1 Purpose

The rival is not claimed to be one named external theory. It is a deliberately generic but **pre-frozen** ordinary causal-history model class capturing resources that standard control, learning, state-machine, dynamical-systems, and causal models routinely possess.

It is called `R_CH` only as an audit handle.

### 2.2 State schema

For a declared boundary `B` and time step / event window `t`:

```text
x_t   = current bounded system state
u_t   = input / perturbation / candidate-relevant difference
m_t   = internal causal mediator state
pi_t  = current policy / transition rule / control law
h_t   = persistent history / memory carrier
b_t   = declared bearer / affected-position ledger
c_t   = cost / resource / repair-burden state
E_t   = environment state within the frozen boundary
```

The rival may use deterministic or stochastic transitions:

```text
m_t       = M(x_t, u_t, h_t, pi_t)
a_t       = A(x_t, m_t, h_t, pi_t)
x_{t+1}   = F(x_t, a_t, E_t, xi_t)
h_{t+1}   = U(h_t, x_t, m_t, a_t, x_{t+1})
pi_{t+1}  = G(pi_t, h_{t+1}, x_{t+1})
c_{t+1}   = C(c_t, b_t, x_t, a_t, x_{t+1})
R_{t+1}   = Reach(x_{t+1}, h_{t+1}, pi_{t+1}, E_{t+1}, B)
```

where `xi_t` may represent declared stochasticity.

### 2.3 What `R_CH` is allowed to explain

Without using SRT-specific vocabulary, it may represent:

- asymmetric constraints;
- fixed or adaptive input-response mappings;
- internal non-equivalent mediation;
- causal path efficacy;
- feedback control;
- hysteresis and memory;
- persistent environmental or internal writeback;
- policy / threshold / rule updates;
- resource expenditure and repair cost;
- bearer-specific cost ledgers;
- later reachable-set differences;
- stochastic branching;
- learning or meta-learning if the update law was declared before the case.

### 2.4 Anti-Goodhart restrictions on the rival

The rival may **not**:

1. add a new latent variable solely because an SRT verdict was hard to reproduce;
2. introduce an unexplained “real choice”, “actualisation”, “selection”, “manifestation”, or equivalent black-box primitive;
3. redefine the boundary, bearer, event unit, or horizon after seeing the result;
4. use future outcome labels as causes of earlier transitions;
5. claim a D2 win by merely redescribing the same outcome with different vocabulary;
6. absorb every future anomaly through unrestricted model expansion without paying a preregistered complexity / prediction cost.

### 2.5 Same-schema rule

The same variable families and update grammar must be used across software, biological, and institutional cases. Domain-specific observables may instantiate `x`, `m`, `h`, `pi`, `c`, and `E`, but the rival cannot invent a qualitatively new explanatory resource per case.

This restriction is what makes `NO-D2` informative rather than tautological.

---

## 3. Divergence ladder

A2 freezes four levels:

### `D0` — vocabulary divergence

Two descriptions use different words but agree on event classification, counterfactuals, interventions, and predicted observations.

**Scientific gain: none.**

### `D1a` — internal SRT criterion divergence

`S_core` and `S_CG` classify the same case differently.

This can expose an internal bridge problem but does not establish SRT-vs-rival advantage.

### `D1b` — SRT-vs-rival classification divergence

SRT and `R_CH` assign different conceptual classes while agreeing on all observable counterfactual / intervention outcomes.

This is potentially philosophically useful but still not a differential empirical result.

### `D2` — counterfactual / intervention divergence

Before the result is known, the models predict different observable outcomes under the same intervention or counterfactual.

**This is the minimum level that can discharge the main §13 / §14 discrimination burden.**

### `D3` — preregistered empirical discrimination

A frozen D2 prediction is run and the result favors one model family under declared error / model-comparison rules.

No D3 is attempted here.

---

## 4. Case A — correct-SHA GitHub transaction

Source:

`Operations/SRT_AI_CORRECT_SHA_SUCCESS_CONTROL_UNIFIED_AUDIT_2026-08-05.md`

### 4.1 Observed event

At full boundary:

```text
correct expected SHA
-> update_file accepted
-> new blob created
-> new commit created
-> branch ref advances
-> later work starts from changed branch state
```

The prior unified audit records a full-boundary `SEA-3 qualified` operational result.

### 4.2 `S_CG` verdict

```text
bounded selection-event candidate: YES
```

because the case supplies the five operational roles at the declared full boundary.

### 4.3 `S_core` verdict

```text
P1-T05 real choice: NOT ESTABLISHED
```

Reason: the transaction is a deterministic compare-and-swap / state-transition procedure once the user-authorized call and correct SHA are given. P1-T05 explicitly blocks script execution from becoming real choice merely because it causes persistent future-state change.

This is the Pass-1.5 negative-control result.

### 4.4 `R_CH` fit

Map:

```text
x_t  = repository / branch state
u_t  = requested content + expected SHA
m_t  = server validation of expected vs actual blob identity
pi_t = GitHub update transaction rule
h_t  = blob / commit / ref history
c_t  = operation / recovery obligations within chosen boundary
E_t  = repository service state
```

Ordinary transition rules predict:

- mismatch -> reject / no target write;
- match -> commit / ref movement;
- new ref state -> later operations inherit changed baseline.

No primitive selection role is needed to predict these observations.

### 4.5 Divergence

```text
S_core vs S_CG: D1a
S_CG vs R_CH: at most D1b label difference
D2: absent
```

A different label for the same scripted transaction does not constitute a different intervention prediction.

---

## 5. Case B — E. coli chemotaxis and methylation history

Source:

`Operations/SRT_LIFE_BOUNDARY_CASE_ECOLI_CHEMOTAXIS_UNIFIED_AUDIT_2026-08-05.md`

### 5.1 Observed structure

The existing audit records:

- real ligand-gradient differences;
- receptor / Che pathway mediation;
- run/tumble path redistribution;
- methylation-dependent adaptation and later-response effects;
- strong path and history evidence;
- same-event CBP not established.

Its conservative result is:

```text
SEA-2 strong
SEA-3 not established
```

### 5.2 `S_CG` verdict

The five-gate event is not closed because the bearer-specific consequence gate is missing at the same event / boundary / timescale.

### 5.3 `S_core` verdict

```text
P1-T05 real choice: NOT ESTABLISHED by current evidence
```

The reason is independent of the CBP deficit: canonical P1-T05 explicitly says **gradient following does not by itself constitute a real choice moment**.

The chemotaxis literature used in the audit documents sophisticated control, adaptation, history dependence, and path change, but the current evidence package does not contain an independently operationalized “live rather than gradient-following” discriminator.

### 5.4 `R_CH` fit

Map:

```text
x_t  = receptor / signaling / motor state
u_t  = experienced ligand concentration history
m_t  = receptor-CheA-CheY mediation
pi_t = run/tumble control relation
h_t  = receptor methylation / adaptation state
c_t  = measured metabolic / maintenance variables when available
E_t  = microfluidic / chemical environment
```

The rival predicts:

- perturb CheR/CheB -> altered adaptation and later response;
- perturb motor coupling -> altered path efficacy;
- reverse / reset gradient -> changed navigation conditional on adaptation state;
- non-metabolizable attractant may preserve navigation while failing to establish nutrient consequence.

These are exactly the kinds of distinctions already identified by the existing audit. No current intervention has one prediction under SRT and another under this ordinary causal-history schema.

### 5.5 Divergence

```text
S_core: real choice not established
S_CG: SEA-2 strong, not full event
R_CH: ordinary adaptive control/history model sufficient for current observations
D2: absent
```

This case is especially important because biological complexity and memory do not automatically rescue the real-choice claim.

---

## 6. Case C — institutional acceptance -> production

Source:

`Operations/SRT_INSTITUTIONAL_PUBLICATION_PAIRED_UNIFIED_AUDIT_2026-08-05.md`

### 6.1 Observed event

The positive institutional chain includes:

```text
registered manuscript
-> independent review / revision
-> review finalised
-> acceptance
-> production
-> proof generation / correction obligations
```

The source audit gives the acceptance / production chain a bounded:

```text
SEA-3 qualified
```

because accepted status is later called by production processes and changes reachable workflow, roles, obligations, and completion conditions.

### 6.2 `S_CG` verdict

```text
bounded selection-event candidate: YES at the frozen institutional boundary
```

### 6.3 `S_core` verdict

```text
P1-T05 real choice: UNRESOLVED / NOT ESTABLISHED by this audit
```

This is deliberately not a claim that editors, reviewers, or authors are “scripts.” Human agents may of course make real choices.

The narrower point is evidential:

> the institutional audit measures workflow registration, path efficacy, consequence bearing, and historical writeback. It does not independently distinguish a live P1-T05 event from rule-governed criterion application, policy execution, habitual judgment, or other ordinary decision processes that can produce the same state transition.

Human participation cannot be used as an unmeasured shortcut to a P1 verdict.

### 6.4 `R_CH` fit

Map:

```text
x_t  = manuscript / workflow state
u_t  = manuscript + review / revision information
m_t  = role-specific editorial / reviewer / production processing
pi_t = current journal workflow and decision policy
h_t  = manuscript history, review state, revision and acceptance records
b_t  = author / editor / production role positions
c_t  = deadlines, fees/resources, revision/production burden
E_t  = journal platform and institutional environment
```

A state-machine / causal-history model predicts that an accepted status can be consumed by downstream production to open new transitions and obligations.

No current evidence isolates a counterfactual in which `S_core` predicts a different externally observable result from `R_CH` after the relevant causal-history variables are matched.

### 6.5 Divergence

```text
S_core vs S_CG: D1a-like unresolvedness
S_CG vs R_CH: classification / audit emphasis differs
D2: absent
```

The case therefore cannot serve as evidence that institutional selection requires an SRT-specific mechanism.

---

## 7. Cross-case matrix

| Case | `S_core` P1-T05 | `S_CG` | `R_CH` current adequacy | Highest divergence |
|---|---|---|---|---|
| correct-SHA software transaction | not established; script exclusion | `SEA-3 qualified` | high | `D1a` |
| E. coli chemotaxis | not established; gradient-following exclusion remains | `SEA-2 strong` | high | `D1b` at most |
| institutional acceptance -> production | unresolved / not established by workflow audit | `SEA-3 qualified` | high | `D1a/D1b` |

**No case reaches D2.**

This cross-domain result is stronger than a single-case failure because the same mismatch appears in:

- deterministic software;
- adaptive biological control;
- human-containing institutional workflow.

But it remains bounded to the current evidence and the frozen rival schema.

---

## 8. Why current P1-T05 cannot yet generate D2 by itself

### 8.1 It contains a negative exclusion, not an operational positive variable

P1-T05 says that script, habit, gradient following, and L2 label optimization are insufficient.

This prevents overclassification, but it leaves a positive gap:

```text
What measurable property makes an event live rather than merely adaptive / history-effective / policy-updating?
```

No current scalar, relation, intervention target, or transition constraint in P1-T05 answers that question.

### 8.2 “Future selection space changed” is not enough

Software commits, learned policies, institutional rules, receptor methylation, and ordinary hysteretic systems all change later reachable states.

Therefore:

```text
future reachability changed
```

cannot by itself distinguish P1-T05 real choice from ordinary causal-history processes.

### 8.3 “The rule itself changed” is also not enough without a rival constraint

`R_CH` explicitly allows `pi_{t+1} = G(pi_t, h_{t+1}, x_{t+1})`.

Thus adaptive rule revision, meta-learning, institutional policy update, or threshold change can remain ordinary causal-history phenomena unless SRT states a stronger prospective restriction.

This blocks a common escape route:

> “real choice is when the system changes its own rule.”

That can be a useful bridge hypothesis, but it is not yet a discriminator against an adaptive rival.

### 8.4 “Non-preformation” is metaphysically important but not yet an intervention variable

SRT may reject a completed inventory of pre-given future objects. An ordinary rival may instead use a state/process ontology with stochastic or generative transitions.

Unless the two views make different measurable predictions under a frozen experiment, the disagreement remains metaphysical / representational rather than D2.

---

## 9. The strongest negative result

A2 rejects two easy but invalid moves.

### Move 1

```text
CG passes
-> real choice established
```

Rejected by Pass 1.5 and Case A.

### Move 2

```text
ordinary model can redescribe the event
-> selection is dispensable / false
```

Also rejected. Representational and mechanistic reconstruction of current observables does not prove the metaphysical primitive false, nor does it prove the actualisation role absent.

The correct result is:

> **Current SRT has not yet earned a differential empirical advantage for P1-T05 or the primitive selection role.**

That is a statement about current discriminating content, not a global refutation.

---

## 10. Consequences for the theory architecture

### 10.1 P0-01 / AM-A

No change.

`selection` remains the current P0 primitive admission. A2 does not prove it irreducible and does not demote it.

### 10.2 P1-T05

No canonical change is authorized by this audit.

Its present role is clarified:

> canonical structural distinction / exclusion boundary whose positive operational discriminator remains open.

It must not be cited as an already operationalized empirical law.

### 10.3 CG / SEA

CG retains real value as an audit methodology for preventing weak proxies from being overread:

- output difference alone is not path efficacy;
- path efficacy alone is not consequence bearing;
- a record alone is not historical efficacy;
- evidence cannot be stitched across incompatible boundaries or timescales.

But current A2 does **not** support calling CG an independently demonstrated SRT-specific mechanism.

### 10.4 Existing `SEA-3 qualified` cases

They remain valid **within the operational protocol's own bounded meaning**.

They must not be upgraded to:

- canonical P1-T05 real choice;
- P0 selection irreducibility;
- subjecthood;
- consciousness;
- freedom;
- independent mechanism superiority over ordinary theories.

### 10.5 §13 residue

Formal GOV-SUB01 residue remains:

```text
UNASSIGNED
```

A2 produces no qualifying D2 exhibit.

---

## 11. A2 identifies the actual next experimental burden

The next task is **not** another descriptive case audit.

A future test must create a condition where the two model families are forced to make different prospective predictions.

### 11.1 Minimal matched-state D2 contract

Before data collection, freeze:

```text
B        = boundary
H        = horizon
x        = measured current state vector
h        = measured history / memory state
pi       = measured policy / transition-rule state
c        = measured cost / resource / bearer state
E        = controlled environment
O_future = preregistered future outcome
```

Construct two conditions that are matched, within declared tolerance, on the rival's sufficient-state vector:

```text
Z_R = (x, h, pi, c, E)
```

but that SRT prospectively classifies differently:

```text
Condition L = live P1-T05 candidate
Condition S = script / replay / gradient / L2-automation control
```

Then require **before observation**:

```text
R_CH prediction: O_future(L) ~= O_future(S) given matched Z_R
SRT prediction:  O_future(L) != O_future(S)
```

If SRT cannot state the second line quantitatively or ordinally in advance, the experiment cannot reach D2.

### 11.2 What cannot count as the outcome

Do not use as `O_future`:

- the SRT/CG classification label itself;
- self-report that merely repeats the manipulation instruction;
- the same state variables used to define L vs S;
- post-hoc addition of a new hidden rival variable;
- generic “more flexibility” without a frozen measure and direction;
- outcome differences that were already predicted by ordinary reward, memory, policy, resource, or task-state differences left unmatched.

### 11.3 Rival revision rule

If `R_CH` fails, it may be extended only if the added variable / mechanism:

1. was independently motivated before seeing the focal outcome, or
2. yields a new out-of-sample prediction that can itself fail.

Otherwise the extension is degenerative accommodation.

The same rule must apply symmetrically to SRT.

---

## 12. Most promising candidate for a future D2 test

A2 does not preregister a full experiment, but it narrows what would be worth building.

The most promising structure is **matched immediate output + matched recorded history + novel perturbation**.

Example schema:

```text
Phase 1:
  produce the same immediate choice/output under two generation regimes

Phase 2:
  match observable state/history/policy variables as tightly as possible

Phase 3:
  introduce a novel perturbation that requires generating or reopening a path
  not directly encoded in the prior task mapping

Outcome:
  preregister future reachable-option use, rule revision, recovery trajectory,
  or transfer to a genuinely new candidate structure
```

Why this is better than the current cases:

- simple script replay can match the initial output;
- ordinary memory can match much of the historical trace;
- the novel perturbation creates a prospective window where a real differential prediction might be forced.

Why it is still not automatically SRT-specific:

- meta-learning, generative control, model-based RL, active inference, or other adaptive models may predict transfer too;
- therefore the rival sufficient-state vector and competing quantitative predictions must be frozen before execution.

This is an experiment-design direction, not evidence.

---

## 13. Relation to P24 discriminating predictions

A2 reinforces a distinction already implicit in Core 24:

> a distinctive vocabulary or audit procedure is not enough; a discriminating prediction needs specificity, a rival contrast, operationalization, and a failure condition.

The current A2 burden is upstream of running P24 at scale:

```text
A1: can the primitive role be deleted / reconstructed?
A2: can SRT and a frozen rival be forced to disagree prospectively?
P24: which domain-level predicted patterns actually discriminate?
```

A2 currently closes with a **negative** result: no such prospective disagreement has yet been executed for the selection / real-choice core.

That result should constrain which P24 candidates receive experimental investment.

---

## 14. What this audit does and does not say

### It does say

1. current CG full-pass is not sufficient by itself for P1-T05;
2. current case audits do not provide D2 against a strong ordinary causal-history rival;
3. P1-T05's live-choice clause lacks a positive operational discriminator in the current core;
4. persistent history, bearer consequence, path efficacy, and future reachability are all representable in ordinary causal-history terms;
5. the next serious test must be prospective, matched-state, and rival-frozen.

### It does not say

1. selection does not exist;
2. P0-01 is false;
3. every human choice is scripted;
4. E. coli cannot select in any meaningful sense;
5. CG is useless;
6. ordinary causal-history theory is complete;
7. future D2 is impossible;
8. metaphysical disagreement is meaningless.

---

## 15. Stop rule

A2 stops here because:

1. the ordinary rival was frozen before case adjudication;
2. the same rival schema was used across three domains;
3. `S_core` and `S_CG` were not conflated;
4. each case was evaluated for prospective divergence rather than vocabulary difference;
5. no current case produced D2;
6. no formal selection residue is over-assigned;
7. the next valid move is a purpose-built matched-state prospective test, not another retrospective case classification.

**Final A2 verdict:**

> `NO-D2 / differential closure not achieved on the current case set.` SRT currently has a canonical real-choice exclusion boundary and a useful five-gate audit technology, but it has not yet specified and executed a counterfactual or intervention prediction that a strong frozen ordinary causal-history rival cannot also produce. The next hardening step must therefore turn “live choice” into a prospective differential contract before further empirical investment.