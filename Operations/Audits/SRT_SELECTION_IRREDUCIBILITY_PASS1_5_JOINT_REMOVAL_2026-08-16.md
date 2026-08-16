---
id: SRT-OPS-AUDIT-SELECTION-IRREDUCIBILITY-PASS1-5-JOINT-REMOVAL-20260816
type: audit_record
status: active
record_stage: executed_pass1_5
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: P3/P4_governance
canonical: false
date: 2026-08-16
dependency:
  - SRT-GOV-SUB01-SUBTRACTIVE-AUDIT
  - SRT-OPS-AUDIT-SELECTION-IRREDUCIBILITY-RIVAL-TEST-20260816
  - SRT-CORE-21B-CONSTITUTIVE-THEOREMS
  - SRT-UNIFIED-SELECTION-EVENT-AUDIT-PROTOCOL-20260804
  - SRT-AI-CORRECT-SHA-SUCCESS-CONTROL-UNIFIED-AUDIT-20260805
  - SRT-OPEN-TENSIONS
tags: [Governance, SubtractiveAudit, Selection, JointRemoval, Writeback, ConsequenceReturn, RealChoice, CG, DifferentialHardening]
---

# Selection Irreducibility Pass 1.5 — Joint Removal Audit

> **Role**: execute the lowest-cost Step-5 test frozen by `SRT_SELECTION_IRREDUCIBILITY_RIVAL_TEST_2026-08-16.md`.
>
> **Frozen operation**: remove `irreversible writeback` + `bearer-specific consequence return`, then retest the `Y3 real-choice discrimination` target under a fixed boundary and horizon.
>
> **Hard boundary**: this pass does not modify `P0-01`, `P1-T05`, the CG protocol, or any canonical definition. It does not assign a formal GOV-SUB01 residue to `selection`.

---

## 0. Executive result

**Pass 1.5 result: the frozen joint-removal test is informative, but not in the way a simple “both are necessary” verdict would suggest.**

The key result is a target split that was hidden inside Pass 1's `Y3` wording:

```text
Y3a = P1-T05 constitutive target:
      a live event genuinely constrains future selection space

Y3b = CG operational target:
      a bounded selection-event candidate passes CG-0..CG-4
```

Under the fixed software-transaction case used here:

- removing **bearer-specific consequence return only** does **not by itself destroy Y3a** so long as a persistent historical carrier still changes future reachable state;
- the same removal **does destroy Y3b**, because CG-3 is non-compensable by protocol;
- removing **irreversible writeback / persistent historical carrier** destroys **Y3a**, because the event no longer demonstrably constrains a later selection space rather than only changing the immediate path;
- joint removal therefore collapses the case to at most a path-effective transition unless writeback is covertly reintroduced through `history`, `reachable-set transformation`, or another renamed state carrier.

The strongest new conclusion is therefore:

> **P1-T05 and the five-gate CG audit are not currently equivalent criteria. CG is a stricter operational package than the wording of P1-T05 in at least one dimension: bearer-specific consequence is required by CG-3 but is not yet shown necessary for the minimal P1-T05 future-selection-space clause.**

This is a hardening result, not a demotion of either object. It identifies a relation that §14 had left explicitly unformalized.

Formal GOV-SUB01 residue for `selection`: **UNASSIGNED**.

---

## 1. Frozen target and case

### 1.1 Why split `Y3`

Pass 1 defined:

> `Y3 Real-choice discrimination`: distinguish a live event that changes future reachability from script replay / habit / gradient following without merely renaming the distinction.

That sentence mixed two authorities:

1. canonical `P1-T05`, whose positive load is future selection-space constraint;
2. non-canonical CG operations, whose five gates additionally require consequence bearing as a non-compensable condition.

A Step-5 interaction test cannot be interpreted cleanly until these two targets are separated.

### 1.2 Fixed case

Primary bounded case:

`Operations/SRT_AI_CORRECT_SHA_SUCCESS_CONTROL_UNIFIED_AUDIT_2026-08-05.md`

Frozen full boundary `B3`:

```text
user + LLM + orchestration + connector + GitHub contents service
+ isolated branch + target file + blob + commit + ref + recovery channel
```

Frozen event:

```text
correct expected blob SHA
-> accepted update_file transaction
-> target content changes
-> new blob
-> new commit
-> branch head advances
-> later work from the branch inherits the changed state
```

The paired wrong-SHA 409 case remains a calibration control for “endpoint contact without target commit.”

### 1.3 Why this case is adequate for Pass 1.5

This case does **not** establish a special SRT mechanism; its own report says ordinary compare-and-swap / Git transaction theory explains the engineering process. That is useful here because Pass 1.5 is testing role dependence, not claiming mechanism novelty.

The case has separately identified:

- path efficacy;
- consequence location;
- historical carrier;
- future baseline change;
- fixed system boundary;
- matched negative control.

That makes it sufficient for a bounded Step-5 decomposition without running a new live mutation.

---

## 2. Removal variables

Let:

- `W` = irreversible writeback / persistent historical carrier that preserves the event into later state;
- `C` = bearer-specific consequence return / identified position to which path-specific loss, obligation, repair cost, or future-option burden returns.

The frozen joint-removal operation is:

```text
M^{-W,-C}
```

### 2.1 Anti-laundering rule for `W`

After deleting `W`, the rival may not preserve the same role by saying only:

- “history remembers it”;
- “the reachable set is now different”;
- “the state contains the result”;
- “a transition kernel is conditioned on the event”;

unless an independently specified persistent carrier explains how the earlier event remains causally available later.

If the later reachable set depends on an event only because a state variable, memory, environment modification, commit, parameter, threshold, or equivalent carrier persists, that carrier **is the writeback role for this audit** even if not called `writeback`.

### 2.2 Anti-laundering rule for `C`

After deleting `C`, the rival may retain ordinary state change and path-specific effects, but may not count generic aggregate change as bearer-specific consequence merely by renaming the affected state “the bearer.”

The affected position must be independently fixed before the result.

---

## 3. Four-cell Step-5 matrix

| Cell | `W` | `C` | `Y3a` P1-T05 target | `Y3b` CG target | Main diagnosis |
|---|---:|---:|---|---|---|
| A | 1 | 1 | preserved as bounded candidate | preserved as `SEA-3 qualified` in the source case | reference |
| B | 1 | 0 | **can remain preserved** if persistent writeback still changes later reachable state | **fails** because CG-3 / CBP minimum is removed | separates P1-T05 from CG |
| C | 0 | 1 | **fails** unless writeback is smuggled back through history/reachability | fails because CG-4 / HEF minimum is removed | writeback carries future-space clause |
| D | 0 | 0 | **fails**; at most immediate path efficacy remains | fails CG-3 and CG-4 | joint removal collapses event standing |

---

## 4. Cell A — reference

In the correct-SHA source audit, the full `B3` boundary records:

```text
PEF >= 2
CBP = 2
HEF = 3
SEA = 3 qualified
```

The new commit and branch-head movement persist after the immediate request and alter the baseline from which later branch operations proceed.

For this pass:

- `Y3a`: preserved as a bounded P1-T05-compatible candidate because later reachable operations are conditioned by the new branch state;
- `Y3b`: preserved because the source audit passes the five gates at the declared qualified level.

No stronger claim is imported from the source audit.

---

## 5. Cell B — remove bearer-specific consequence return only

### 5.1 Operation

Keep:

- correct-SHA path efficacy;
- commit creation;
- branch-head update;
- persistent historical state;
- future reachable-state change.

Delete from the model:

- attribution of repair burden, loss, obligation, risk, or future-option cost to a separately identified bearer position.

### 5.2 Result for `Y3a`

The event can still satisfy the literal future-space part of P1-T05:

```text
pre-event branch state != post-event branch state
and
later admissible / available branch operations inherit the post-event state
```

Nothing in the minimal wording of P1-T05, by itself, requires a separately identified bearer-specific consequence position.

Therefore:

> `C` is **not shown necessary for Y3a** by current P1-T05 wording.

This is not a formal `R3` verdict for `C` across SRT. It is a bounded candidate reading relative to this target and case.

### 5.3 Result for `Y3b`

The CG protocol is explicitly non-compensatory. Removing the bearer-specific consequence role removes the positive basis for CG-3 / CBP.

Therefore:

```text
CG-0/1/2 may still pass
CG-4 may still pass
CG-3 fails
-> no bounded selection-event candidate under the five-gate protocol
```

This loss is **protocol-structural**. It does not yet prove that nature requires bearer-specific consequence for every real choice moment.

### 5.4 Cell-B interpretation

Cell B is the decisive separation result:

> **CG-3 carries additional operational load beyond what is explicitly stated in the minimal P1-T05 future-selection-space criterion.**

---

## 6. Cell C — remove irreversible writeback only

### 6.1 Operation

Keep:

- immediate request validation;
- immediate path efficacy;
- an identified consequence position for the immediate event.

Delete:

- commit/ref persistence as a historical carrier;
- any equivalent persistent state that makes the event causally available to later transitions.

### 6.2 Result for `Y3a`

Without a persistent carrier, the model can still describe:

```text
input difference -> different immediate transition -> immediate consequence
```

But it cannot establish:

```text
this event genuinely constrains the future selection space
```

unless a later state, memory, modified environment, parameter, branch head, threshold, or equivalent historical carrier preserves the earlier event.

If such a carrier is reintroduced under `history dependence` or `reachable-set transformation`, the deleted `W` role has been hidden rather than removed.

Therefore:

> within this bounded case, a persistent writeback/history-carrier role is a current indispensability **candidate** for `Y3a`.

No cross-context `N1/N2` residue is assigned because the perturbation sweep is not complete.

### 6.3 Result for `Y3b`

CG-4 requires HEF-3 by the frozen protocol. With no persistent carrier capable of changing future reachability, transition probability, return cost, threshold, or rule:

```text
CG-4 fails
-> bounded selection-event candidate fails
```

Again, this is a protocol result plus a bounded structural dependency, not a universal metaphysical theorem.

---

## 7. Cell D — joint removal `W + C`

With both roles deleted, the strongest remaining description is approximately:

```text
candidate difference
-> internal/non-equivalent processing
-> path-effective immediate transition
```

This can still distinguish:

- no call vs call;
- rejected request vs accepted immediate execution;
- one immediate path from another.

It cannot, without smuggling deleted roles back in, establish either:

1. that the event changes a later selection space (`Y3a`); or
2. that all five non-compensable CG gates close (`Y3b`).

In the source domain, the event therefore collapses from the full-boundary `SEA-3 qualified` pattern toward at most the path-effective process class carried by PEF/SEA-2-like structure.

This is exactly the distinction already visible in the source report between endpoint contact / path effect and persistent target commit.

---

## 8. Interaction result

### 8.1 The two deletions are asymmetric

The important Step-5 result is **not** simply:

```text
W necessary + C necessary
```

Instead:

```text
for Y3a / P1-T05:
W carries a load that C does not currently carry

for Y3b / CG:
W and C are both mandatory because CG-3 and CG-4 are separately non-compensable
```

So the apparent pairwise necessity depends on which target was meant.

### 8.2 Overloaded target detected

Pass 1's single `Y3` target hid this distinction. The Step-5 audit therefore discovers a **target-definition interaction** rather than a clean component-synergy theorem.

This matters methodologically:

> if deleting `C` “fails Y3” only because Y3 silently means “pass the five-gate protocol,” then using that result to prove `C` is necessary for canonical real choice would be target laundering in reverse.

### 8.3 No selection-residue consequence

The joint-removal result does not show that the primitive `selection` role is irreducible. A non-selection causal-history model can still carry `W` through persistent state and can carry `C` through an explicit bearer ledger.

Therefore formal residue for `selection` remains:

```text
UNASSIGNED
```

---

## 9. Candidate classifications — explicitly non-formal

| Component / relation | Target | Candidate reading | Why not formal |
|---|---|---|---|
| persistent writeback/history carrier `W` | `Y3a` | `N1-like current target-relative indispensability candidate` | one bounded domain/case; no full perturbation sweep |
| bearer consequence `C` | `Y3a` | `R3-like target-relative dispensability candidate` | only minimal P1-T05 wording tested; other targets may need C |
| `W` | `Y3b` | protocol-mandatory | CG-4 defines the audit gate; not independent empirical necessity |
| `C` | `Y3b` | protocol-mandatory | CG-3 defines the audit gate; not independent empirical necessity |
| primitive `selection` | §13 overall | **no classification change** | no qualifying `E_cf/E_int` exhibit |

Do not quote the `N1-like` or `R3-like` rows as attached GOV-SUB01 residues.

---

## 10. Consequence for §14

Pass 1.5 materially sharpens the open relation between P1-T05 and `CG-0..CG-4`.

The current evidence supports at least:

```text
CG full pass -> a stricter operational package than the literal minimum stated in P1-T05
```

It does **not** yet support:

```text
CG full pass <-> P1-T05 real choice moment
```

or:

```text
CG-3 bearer consequence is a necessary condition of every P1-T05 real choice moment
```

The next A2 test must therefore avoid treating “Judge S” and “Judge CG” as automatically identical. At minimum it should separate:

- **Judge S_core**: P1-T05 minimum;
- **Judge S_CG**: five-gate bounded audit;
- **Judge R**: strongest ordinary causal-history rival.

This turns A2 from a two-judge vocabulary comparison into a three-way adjudication capable of detecting whether disagreement comes from SRT's canonical criterion, from its stricter audit apparatus, or from the ordinary rival.

---

## 11. A2 handoff contract

Freeze the next test as:

```text
Judge S_core = P1-T05 only
Judge S_CG   = CG-0..CG-4 non-compensable audit
Judge R      = strongest ordinary causal-history rival
```

Use the same event unit, boundary, history, bearer, horizon and evidence.

Record divergence:

- `D0`: wording only;
- `D1a`: S_core vs S_CG classification difference;
- `D1b`: SRT-family vs rival classification difference;
- `D2`: counterfactual/intervention prediction differs;
- `D3`: preregistered empirical outcome discriminates.

Only `D2+` can discharge the main §13 discrimination burden.

A `D1a` result is nevertheless theoretically useful because it exposes internal criterion mismatch and can force clarification of whether CG conditions are necessary, sufficient, or intentionally stronger audit guards.

---

## 12. Stop rule

Pass 1.5 stops because:

1. the frozen pairwise joint-removal operation has been executed;
2. the fixed case, boundary and horizon are explicit;
3. anti-laundering rules for `W` and `C` are explicit;
4. the four-cell matrix has been evaluated;
5. the overloaded `Y3` target has been split into `Y3a` and `Y3b`;
6. no formal residue is over-assigned;
7. the next discriminating task is now A2 three-way rival adjudication, not further vocabulary deletion.

**Final Pass-1.5 verdict:**

> The joint deletion does not establish primitive selection irreducibility. It establishes that persistent writeback is load-bearing for the minimal P1-T05 future-selection-space clause in the bounded case, while bearer-specific consequence is load-bearing for the stricter CG audit but is not yet shown necessary for P1-T05 itself. The main new pressure therefore lands on the unformalized P1-T05 ↔ CG relation and should be carried into A2 as a three-judge comparison.