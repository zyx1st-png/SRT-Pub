---
id: SRT-OPS-AUDIT-SELECTION-IRREDUCIBILITY-PASS1-5-JOINT-REMOVAL-20260816
type: audit_record
status: active
record_stage: executed_pass1_5_corrected
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
> **Frozen operation**: remove `irreversible writeback` + `bearer-specific consequence return`, then retest the `Y3 real-choice discrimination` pressure under a fixed boundary and horizon.
>
> **Hard boundary**: this pass does not modify `P0-01`, `P1-T05`, the CG protocol, or any canonical definition. It does not assign a formal GOV-SUB01 residue to `selection`.
>
> **Post-PD-A read-back (2026-08-17)**: PD-A separates P0 admission from downstream D2 and retires the former extra §13 D2/exhibit gate. This historical pass is **not** retroactively upgraded: it did not execute the full declared perturbation sweep or a post-PD-A residue re-adjudication. Its no-formal-residue disposition therefore remains in force until the current `Core/SRT_OPEN_TENSIONS.md §13` re-adjudication rule is satisfied.

---

## 0. Corrected executive result

**Pass 1.5 exposes a target mismatch rather than proving that the two deleted roles are jointly necessary for canonical real choice.**

The frozen source case—the correct-SHA GitHub transaction—was previously audited as a full-boundary `SEA-3 qualified` event under CG. But its own ordinary explanation is a deterministic compare-and-swap / transaction script. `P1-T05` explicitly says that **script execution does not by itself constitute a real choice moment**.

Therefore the source case is admissible for the operational CG target but **not** as an independently established positive instance of `P1-T05`.

The correct target split is:

```text
Y3a = P1-T05 constitutive target:
      a live L0 -> L1 anchoring event in which what is selected
      genuinely constrains future selection space,
      with script/habit/gradient/L2-label execution insufficient by itself

Y3b = CG operational target:
      a bounded selection-event candidate passes CG-0..CG-4
      under the non-compensation rule
```

Pass-1.5 outcome:

1. the `W + C` deletion can be validly evaluated against **Y3b / CG**;
2. the same case is **UNINTERPRETABLE as a positive Y3a / P1-T05 test**, because the anti-script gate is not satisfied independently of the CG verdict;
3. a stronger and more important result follows: **CG full-pass is not sufficient, by itself, to establish P1-T05**, because a scripted transaction can pass the operational five-gate audit while still lacking the extra evidence required by P1-T05's live-choice exclusion;
4. the reverse implication is also unproved: P1-T05 does not explicitly require the full bearer-specific CG-3 package;
5. therefore the current P1-T05 ↔ CG relation is **non-equivalent and not yet nested in either direction**.

Formal GOV-SUB01 residue for primitive `selection`: **UNASSIGNED**.

---

## 1. Frozen case and authority split

### 1.1 Primary bounded case

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

The paired wrong-SHA 409 case remains the negative calibration for endpoint contact without target commit.

### 1.2 What the source case actually establishes

The source report establishes, at full boundary:

- difference manifestation;
- internal relation checking at the transaction interface;
- path efficacy;
- bounded consequence attribution;
- persistent historical writeback;
- future branch-baseline change;
- `SEA-3 qualified` under the five-gate operational protocol.

It also explicitly states that ordinary Git blob identity, optimistic concurrency, compare-and-swap, atomic commit/ref update, branch isolation, and human-authorized tool execution sufficiently explain the engineering process.

### 1.3 What the source case does **not** establish

It does not establish that the transaction is a `P1-T05` real choice moment.

Why:

```text
correct SHA condition
-> deterministic transaction precondition passes
-> scripted update commits
```

That is exactly the kind of case for which P1-T05's exclusion matters: **future-state change alone is insufficient if the process is merely script execution**.

So the original temptation to read the source case as “P1-T05-compatible because future reachability changed” is rejected as incomplete.

---

## 2. Removal variables

Let:

- `W` = irreversible writeback / persistent historical carrier that preserves the event into later state;
- `C` = bearer-specific consequence return / identified position to which path-specific loss, obligation, repair cost, or future-option burden returns.

Frozen Step-5 operation:

```text
M^{-W,-C}
```

### 2.1 Anti-laundering rule for `W`

After deleting `W`, the model may not preserve the same role by saying only:

- “history remembers it”;
- “the reachable set is now different”;
- “the state contains the result”;
- “the transition kernel is conditioned on the event.”

A persistent state variable, memory, environment modification, commit, parameter, threshold, or equivalent carrier that makes the earlier event causally available later **is the writeback role for this audit**, whatever it is called.

### 2.2 Anti-laundering rule for `C`

After deleting `C`, the model may retain generic state change and path-specific effects, but may not count aggregate change as bearer-specific consequence merely by renaming the affected state “the bearer.”

The bearer / consequence position must be independently fixed before the result.

---

## 3. Four-cell Step-5 matrix

| Cell | `W` | `C` | `Y3a` P1-T05 | `Y3b` CG audit | Main diagnosis |
|---|---:|---:|---|---|---|
| A | 1 | 1 | **not established by this case**; script exclusion remains live | preserved as source `SEA-3 qualified` | CG-positive / P1-T05-insufficient control |
| B | 1 | 0 | not adjudicable positively from this case | **fails CG-3** | bearer consequence is protocol-load-bearing for CG |
| C | 0 | 1 | not adjudicable positively; future-space evidence also disappears | **fails CG-4** | writeback is protocol-load-bearing for CG and supports future-effect evidence |
| D | 0 | 0 | not adjudicable positively; only immediate path efficacy remains | fails CG-3 and CG-4 | joint removal collapses CG event standing |

The matrix therefore licenses a result about the **CG apparatus** and a negative sufficiency result about the **CG → P1-T05 relation**. It does not license a positive P1-T05 indispensability verdict from this scripted case.

---

## 4. Cell A — reference case

The source audit records at `B3`:

```text
DMF = 3
NER = 2 qualified
PEF = 3 qualified
CBP = 2
HEF = 3
SEA = SEA-3 qualified
```

This is sufficient for `Y3b` under the operational protocol.

But the ordinary event remains a deterministic transaction whose success condition is the expected-SHA equality gate. No independent evidence in the source audit establishes a live `L0 -> L1` anchoring event rather than script execution.

Therefore:

```text
Y3b: positive operational case
Y3a: not established
```

This prevents operational event standing from silently promoting itself into canonical real-choice standing.

---

## 5. Cell B — remove bearer-specific consequence return only

Keep:

- correct-SHA path efficacy;
- commit creation;
- branch-head update;
- persistent historical state;
- future branch-baseline change.

Delete:

- attribution of path-specific burden, repair obligation, risk, loss, or future-option cost to a separately identified bearer position.

### 5.1 Result for Y3b / CG

CG is non-compensatory. Removing `C` removes the positive basis for CG-3 / CBP.

```text
CG-0 may pass
CG-1 may pass
CG-2 may pass
CG-3 fails
CG-4 may pass
-> no five-gate bounded selection-event candidate
```

Thus `C` is protocol-load-bearing for the current CG event class.

### 5.2 Result for Y3a / P1-T05

No positive conclusion is licensed from this case because Cell A already failed to establish P1-T05 independently of the script exclusion.

The only safe statement is:

> current P1-T05 wording does not explicitly state the CG-3 bearer-specific consequence condition, so this audit cannot infer `C` as a P1-T05 necessary condition merely from CG failure.

That remains an open relation question.

---

## 6. Cell C — remove irreversible writeback only

Keep:

- immediate transaction validation;
- immediate path efficacy;
- an identified consequence position for the immediate event.

Delete:

- commit/ref persistence as the historical carrier;
- any equivalent persistent state that makes the event causally available to later transitions.

### 6.1 Result for Y3b / CG

Without an independently specified persistent carrier capable of changing future reachability, transition probability, return cost, threshold, or rule:

```text
CG-4 / HEF fails
-> no five-gate bounded selection-event candidate
```

If “history” or “reachable-set change” is retained by adding a persistent state elsewhere, `W` has been hidden rather than removed.

### 6.2 Result for Y3a / P1-T05

Removing the only evidence of later state dependence also removes the case's evidence for the “future selection space is genuinely constrained” clause.

But this does **not** turn the scripted transaction into a valid P1-T05 positive test in the reference condition. It only shows:

> an independently specified persistence / future-effect carrier is required to *evidence* the future-space clause in this domain, while the separate live-vs-script requirement remains unresolved.

This is a support relation, not an attached `N1` residue.

---

## 7. Cell D — joint removal `W + C`

With both roles deleted, the strongest remaining description is:

```text
candidate difference
-> internal relation check
-> path-effective immediate transition
```

This can still distinguish:

- no call vs call;
- rejected request vs accepted immediate execution;
- one immediate path from another.

It cannot establish the five-gate CG event because CG-3 and CG-4 are both absent.

It also cannot establish P1-T05, but importantly **P1-T05 was not established in the reference cell either**. The joint deletion therefore cannot be interpreted as “P1-T05 was present and was destroyed.”

That distinction is the main correction to the naive Pass-1.5 reading.

---

## 8. Relation result: CG and P1-T05 are not the same test

### 8.1 `CG -> P1-T05` is not licensed

The correct-SHA transaction passes the operational five-gate audit at full boundary but remains fully explainable as deterministic transaction/script execution.

P1-T05 explicitly says script execution does not by itself constitute a real choice moment.

Therefore:

> **Passing CG-0..CG-4 is not sufficient, by itself, to establish P1-T05.**

This is the strongest result of Pass 1.5.

It does not prove that no CG-positive event could ever also satisfy P1-T05. It proves only that the CG verdict alone does not discharge the live-choice / anti-script burden.

### 8.2 `P1-T05 -> CG` is also not licensed

P1-T05's minimal statement focuses on a live anchoring event whose selected result genuinely constrains future selection space and excludes script/habit/gradient/L2-label execution as sufficient substitutes.

It does not explicitly state all five CG gates, especially a separately identified bearer-specific consequence requirement at the CG-3 level.

Therefore the reverse implication is unproved.

### 8.3 Current relation

The safe current relation is:

```text
CG full pass  = operational bounded-event package
P1-T05        = constitutive real-choice distinction

CG != P1-T05
CG -> P1-T05  [not sufficient as currently shown]
P1-T05 -> CG  [unproved]
```

The two criteria are neither identical nor currently established as nested subsets.

---

## 9. GOV-SUB01 Step-5 result

### 9.1 What the joint deletion really shows

For the declared CG target:

- `C` is load-bearing because CG-3 is non-compensable;
- `W` is load-bearing because CG-4 is non-compensable;
- deleting both collapses the full event class to a lower path-effective process description.

This is partly **protocol-structural**: the audit was designed so the gates cannot compensate for each other.

Therefore it cannot be cited as independent empirical proof that `W` and `C` are metaphysically necessary for every real choice event.

### 9.2 Selection residue consequence

Nothing in this pass establishes a differential `E_cf` or `E_int` that ordinary causal-history vocabulary cannot reproduce.

Formal residue for primitive `selection` remains:

```text
UNASSIGNED
```

No `R* / N* / P` label is attached to `selection`.

---

## 10. Candidate readings — explicitly non-formal

| Object | Target | Candidate reading | Limitation |
|---|---|---|---|
| `C` bearer consequence | CG / Y3b | protocol-load-bearing | follows from CG-3 non-compensation; not independent P1-T05 necessity |
| `W` writeback/history carrier | CG / Y3b | protocol-load-bearing | follows from CG-4 non-compensation |
| `W` persistence role | future-space evidence | structurally supportive | reference case is scripted and not a P1-T05 positive case |
| CG full pass | P1-T05 | **insufficient by itself** | anti-script/live-choice burden remains |
| primitive `selection` | §13 overall | no classification change | no qualifying rival differential exhibit |

---

## 11. Consequence for §14

Pass 1.5 materially sharpens the previously open P1-T05 ↔ CG relation.

The relation is no longer merely “unformalized.” There is now a bounded negative sufficiency result:

> **The current five-gate CG verdict cannot be used as a sufficient proxy for P1-T05, because a deterministic scripted transaction can satisfy the five-gate audit while P1-T05 still withholds real-choice standing absent additional live-choice evidence.**

This does not settle necessity or sufficiency in the other direction.

The strongest next question is therefore not “does the rival pass the same five gates?” It is:

> what independent observation or intervention distinguishes a live P1-T05 event from a history-effective scripted process that also passes CG?

That is exactly the place where A2 can become discriminating rather than terminological.

---

## 12. A2 handoff contract

A2 must use **three judges**:

```text
Judge S_core = P1-T05 only
Judge S_CG   = CG-0..CG-4 non-compensable operational audit
Judge R      = strongest ordinary causal-history rival
```

Use the same event unit, boundary, history, bearer, horizon and evidence.

Record divergence:

- `D0`: wording only;
- `D1a`: `S_core` vs `S_CG` classification difference;
- `D1b`: SRT-family vs rival classification difference;
- `D2`: counterfactual / intervention prediction differs;
- `D3`: preregistered empirical outcome discriminates.

The correct-SHA software case is already a useful **D1a calibration case**:

```text
S_CG: bounded event candidate
S_core: real choice not established because scripted execution remains sufficient ordinary explanation
```

But this is not yet a D2 result.

Only `D2+` can discharge the main §13 discrimination burden.

---

## 13. Stop rule

Pass 1.5 stops because:

1. the frozen `W + C` joint-removal operation has been executed against a valid CG-positive bounded case;
2. the source case has been rejected as an unjustified P1-T05 positive proxy;
3. CG-3 and CG-4 load-bearing roles are separated without overclaiming metaphysical necessity;
4. the current `CG -> P1-T05` sufficiency inference is blocked by the script exclusion;
5. formal selection residue remains `UNASSIGNED`;
6. the next task is A2 three-judge rival adjudication focused on producing or failing to produce D2.

**Final Pass-1.5 verdict:**

> The joint deletion shows that bearer consequence and irreversible writeback are load-bearing for the current non-compensable CG event class, but it does not show they jointly constitute canonical real choice. More importantly, the scripted correct-SHA case passes CG while still failing to establish the extra live-choice condition of P1-T05. The immediate theoretical burden therefore moves from “are the CG gates all present?” to “what observable or intervention distinguishes a live P1-T05 event from a history-effective scripted process that passes those gates?”