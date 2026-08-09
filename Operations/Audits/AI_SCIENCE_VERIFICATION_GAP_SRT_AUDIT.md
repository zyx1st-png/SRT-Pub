---
id: SRT-AI-SCIENCE-VERIFICATION-GAP-AUDIT-20260809
type: audit_protocol
status: active
layer: meta
epistemic_layer: os
claim_mode: governance
claim_level: P3-P4_governance
canonical: false
ai_do_not_use_for_definition: true
created: 2026-08-09
tags: [AI, Science, Verification, Provenance, ChoiceTrace, Audit, Reproducibility, Responsibility, SelectionBias]
dependency:
  - Operations/_SRT_CHOICE_TRACE_LOG.md
  - Operations/SRT_CHOICE_TRACE_AUTHOR_DECISIONS_2026-08-04.md
  - Governance/SRT_GOV_SUB01_Subtractive_Audit_Protocol_v0_1.md
  - papers/stake_future_selectability/01_mvp_spec_lock.md
  - papers/stake_future_selectability/03_mvp_decision.md
pilot_target:
  repository: zyx1st-png/SRT-Pub
  pull_request: 746
  title: "Stake–Future Selectability MVP: complete locked P4 experiment"
---

# AI Science Verification Gap × SRT Audit

> **Purpose**: test whether an SRT-style scientific choice trace detects verification risks that ordinary provenance does not.
>
> **Hard boundary**: this protocol does not assume that SRT choice-trace fields add value. Its first task is to try to delete them. If ordinary provenance plus standard preregistration / reproducibility records detect the same risks, the SRT-specific layer must be classified as redundant or target-relative dispensable.

---

## 0. The question

AI-assisted science increasingly leaves abundant execution evidence:

```text
prompt / instruction
→ tool calls
→ code
→ config
→ random seeds
→ commits
→ artifacts
→ final result
```

That record can still omit a different class of information:

```text
what alternatives were live?
which alternatives were rejected?
why did they die?
when did a criterion become binding?
who was allowed to override it?
where did a failure cost land?
did a negative result close, redirect, or merely rename the path?
```

The SRT-facing hypothesis is therefore deliberately narrow:

> **H-VG**: for some AI-assisted scientific workflows, a selection-aware trace may reveal risk in candidate suppression, post-hoc path rewriting, criterion drift, or responsibility relocation that a standard execution provenance log can leave underdetermined.

`H-VG` is a P4 governance / audit hypothesis. It is not a theorem about science, AI, agency, consciousness, `d`, `Ψ_f`, or SRT ontology.

---

## 1. Why existing choice-trace cannot simply be reused

`Operations/_SRT_CHOICE_TRACE_LOG.md` records the author's **convergence function** in writing and decision workflows. Its high-value fields include the option set, chosen branch, skipped mode, reason, closure boundary, and pruned / reclaimed branches.

That is useful lineage, but scientific verification requires a different target.

The new target is not:

```text
author taste
```

It is:

```text
claim validity under a constrained evidence-generating process
```

Therefore this audit borrows field logic from choice-trace but does **not** append scientific runs into the article choice-trace ledger by default.

---

## 2. Two records to compare

### 2.1 Record A — Standard scientific provenance

Minimum fields:

| Field | Meaning |
|---|---|
| `task_or_hypothesis` | declared scientific question |
| `instructions` | human / model instructions relevant to execution |
| `code_state` | commit / tree hash |
| `environment` | runtime, packages, hardware |
| `data_and_inputs` | datasets, seeds, input manifests |
| `configuration` | frozen parameters / config files |
| `tool_calls` | commands / programs / services used when available |
| `artifacts` | outputs, checkpoints, tables, figures |
| `analysis_code` | code that produces reported statistics |
| `preregistration_or_lock` | frozen analysis / decision rules |
| `final_claim` | final reported conclusion |

This is the baseline. A result counts against SRT if Record A alone already supports the same audit decisions.

### 2.2 Record B — Selection-aware scientific trace

Record B contains all Record A fields plus:

| SRT-facing field | Operational meaning | Verification risk it targets |
|---|---|---|
| `candidate_set_at_decision` | alternatives genuinely live at a decision point | hidden result / hypothesis selection |
| `rejected_candidates` | branches killed, with timestamp / stage | silent suppression of failed paths |
| `rejection_rule` | reason or frozen criterion used to reject | criterion drift / post-hoc rationalization |
| `criterion_state` | whether a rule was pre-locked, newly introduced, or revised | evaluator drift |
| `human_override_point` | where a person accepted / rejected model advice | responsibility attribution |
| `model_override_point` | where model / automation changed the path | automation-induced path dependence |
| `bearer_of_consequence` | who/what absorbs the cost of a wrong selection | responsibility relocation |
| `path_writeback` | what future options became unavailable / newly available | history-dependent research narrowing |
| `failed_branch_retention` | whether failed runs remain inspectable | publication / workflow selection bias |
| `counterfactual_reopen_rule` | what evidence would reopen a rejected branch | falsifiability / premature closure |

These are **audit fields**, not canonical SRT variables.

---

## 3. SRT-specific risk classes

The audit tests whether Record B detects any of the following beyond Record A.

### VG-1 — Hidden result selection

A reported result survives because competing runs, seeds, metrics, model blocks, or analyses disappeared from the visible record.

Required discriminator:

```text
execution reproducible
but candidate history incomplete
```

### VG-2 — Failed-path suppression

A negative or invalid branch is removed instead of retained as part of the scientific state.

Key question:

> Can an independent auditor tell that this path was tried, why it failed, and whether its failure constrains future work?

### VG-3 — Post-hoc hypothesis rewriting

The final claim is technically compatible with the data, but differs from the question / threshold that governed the run before outcomes were visible.

### VG-4 — Evaluator drift

The success criterion changes after observing results, including substitution of a favorable secondary metric for a failed preregistered primary gate.

### VG-5 — Responsibility relocation

The visible workflow says “the model decided”, “the code selected”, or “the protocol required it”, but the consequential choice was actually made by a human—or the inverse.

The audit records the location of authority rather than treating the final artifact as agentless.

### VG-6 — Future-path laundering

A failed result is verbally described as a “promising signal” and therefore continues to shape subsequent work without the failure constraint being carried forward.

This is a history-writeback problem:

```text
failure happened
but the future research state behaves as if it did not
```

---

## 4. Pilot target: PR #746

The first pilot is repository PR **#746**, `Stake–Future Selectability MVP: complete locked P4 experiment`.

Why it is a strong test case:

1. it is a real AI-assisted / Codex-executed scientific workflow;
2. it has smoke, pilot, formal lock, 12 master seeds × 6 branches, tests and processed artifacts;
3. pre-C features were hash-locked before C;
4. it contains a preregistered validity gate;
5. the formal result is unfavorable;
6. the top-level decision preserves the failure instead of upgrading a favorable secondary signal.

The frozen decision is:

```text
UNINTERPRETABLE PROTOCOL
```

because T/S Reach20 failed in 8/48 coupled cells. Even setting that gate aside, the primary predictive tests were unfavorable: `dV_CF_pre` did not improve grouped out-of-sample prediction beyond M3, and M4 worsened LOSO CV R² / NRMSE.

This makes #746 unusually useful for a verification-gap audit: the central question is not whether the result is positive, but whether a third party can reconstruct **why favorable-looking evidence was not allowed to rescue the study**.

---

## 5. PR #746 reconstruction map

### 5.1 What standard provenance can already recover

Record A should be able to recover at least:

- formal config and seeds;
- code state and manifest hashes;
- phase order A→B→C;
- X / T / S condition definitions;
- pre-C lock and leakage tests;
- primary `Q_C` outcome;
- M0–M4 model blocks;
- Reach20 / Emp5 controls;
- GO / NARROW / NO-GO style decision thresholds;
- exact formal outputs;
- final `UNINTERPRETABLE PROTOCOL` decision.

Relevant repository evidence includes:

```text
Experiments/stake_future_selectability_mvp/configs/formal_locked.yaml
Experiments/stake_future_selectability_mvp/manifests/formal_manifest.json
Experiments/stake_future_selectability_mvp/outputs/formal/processed/
papers/stake_future_selectability/01_mvp_spec_lock.md
papers/stake_future_selectability/02_analysis_plan.md
papers/stake_future_selectability/03_mvp_decision.md
```

### 5.2 What Record B must add or it fails

The SRT layer earns retention only if it makes one or more of these easier to verify:

1. **why Reach20, not Emp5, remained binding** after Emp5 stayed positive in all T/S cells;
2. **why the favorable S−X `dV_CF_pre` separation did not rescue the bridge**;
3. **why the pilot did not trigger proxy / threshold / seed changes** despite lacking a favorable S-over-X pattern;
4. **which pre-lock bugs were repaired and why those repairs did not count as post-hoc scientific changes**;
5. **who had authority to keep or reject a metric / rerun / branch after the lock**;
6. **how the failed gate changes what future experiments are permitted to claim or redesign**.

If the ordinary preregistration and decision files already make all six points equally clear, then the SRT choice-trace layer has no demonstrated incremental value in this pilot.

---

## 6. Minimal pilot annotation for #746

This section fixes the initial decision nodes to annotate. It is **not yet the completed empirical audit**.

| Node | Candidate set | Observed selection | Risk tested |
|---|---|---|---|
| `D1 probe bug` | keep smoke / fix integrity-only probe / redesign construct | fix probe before pilot/formal; preserve obsolete smoke tree outside active output | VG-2, VG-3 |
| `D2 training summary bug` | accept reward_sum=0 / fix accounting / alter reward definition | fix accounting + regression test; scientific reward definition unchanged | VG-3 |
| `D3 pilot interpretation` | tune proxy / tune thresholds / change seeds / freeze unchanged | freeze unchanged | VG-3, VG-4 |
| `D4 formal Reach20 gate failure` | use Reach20 gate / replace with favorable Emp5 / average both / relax threshold | keep frozen Reach20 gate; verdict becomes uninterpretable | VG-4 |
| `D5 positive S−X dV separation` | treat as support / treat as secondary / rescue primary bridge | retain as secondary; no rescue | VG-1, VG-4 |
| `D6 negative M4 increment` | report / suppress / reframe around within-sample coefficient | report negative incremental prediction and interval-crossing coefficient | VG-1, VG-2 |
| `D7 future continuation` | declare SRT falsified / declare support / preserve narrow open question | preserve only the unvalidated better-manipulation question | VG-6 |

For each node, the completed pilot must record:

```yaml
node_id:
when:
candidate_set_at_decision: []
evidence_available_at_decision: []
criterion_state: prelocked | unlocked | repaired_prelock | postlock
selected:
rejected_candidates: []
rejection_rule:
human_override_point:
model_override_point:
bearer_of_consequence:
path_writeback:
failed_branch_retention:
counterfactual_reopen_rule:
provenance_only_verdict:
selection_trace_increment:
```

---

## 7. Evaluation design

### 7.1 Blind two-pass audit

Prefer two independent auditors or two isolated agent sessions.

**Pass A — provenance only**

Give access to Record A fields but hide explicit selection annotations.

Ask the auditor to identify:

- all invalidating failures;
- all post-lock scientific changes, if any;
- all places where a favorable secondary result could have improperly rescued the primary claim;
- who had decision authority at each critical step;
- what future claims remain allowed.

**Pass B — provenance + selection trace**

Repeat with Record B.

### 7.2 Frozen scoring dimensions

Before the audit, freeze:

| Metric | Question |
|---|---|
| `R_detection` | how many planted / known scientific risks are detected? |
| `R_false` | how many false risks are invented? |
| `authority_accuracy` | is the real decision-maker correctly located? |
| `criterion_drift_detection` | are post-hoc substitutions correctly identified / rejected? |
| `failed_path_recall` | are scientifically constraining failures preserved? |
| `future_claim_boundary` | does the auditor correctly state what remains claimable? |
| `audit_time_or_reads` | does Record B reduce verification cost? |

Do not let “more detailed explanation” count as value unless one of these dimensions improves.

---

## 8. Subtractive audit: delete the SRT-specific fields

Use `GOV-SUB01` with:

```text
M  = full verification record
x  = SRT-specific selection fields
Y  = correct identification of scientific verification risk
C  = AI-assisted research PR with frozen scientific criteria
H  = full PR lifecycle through final claim and immediate future-work boundary
K  = standard provenance may include preregistration, code hashes, seeds, failed results and comments
```

This `K` is intentionally generous. SRT does not get credit by comparing itself to a weak provenance straw man.

### 8.1 Negative result for the SRT application

If removing the SRT-specific fields leaves:

```text
risk detection unchanged
false-positive rate unchanged
authority attribution unchanged
criterion-drift detection unchanged
future-claim boundary unchanged
```

then classify this application as:

```text
R1 proxy redundancy
or
R3 target-relative dispensable
```

Do **not** market scientific choice trace as an SRT-specific verification advantage.

### 8.2 Positive but bounded result

If the added fields repeatedly improve one or more frozen verification metrics—especially hidden candidate suppression, criterion drift, responsibility relocation, or future-path laundering—classify at most:

```text
N1 current target-relative indispensable candidate
```

This supports a workflow / audit method, not SRT ontology.

### 8.3 Stronger evidence requirement

Do not move beyond N1 from one repository case. Require:

- multiple AI-assisted research workflows;
- at least one positive-result case and one negative-result case;
- at least one workflow not authored under SRT governance;
- independent auditor agreement;
- a preregistered comparison against strong provenance baselines.

---

## 9. Distinguish provenance, choice trace, and explanation

A recurring failure mode is to conflate three things:

### Provenance

```text
What happened, with what code / data / config?
```

### Choice trace

```text
What could have happened, what was killed, by which rule and authority, and how did that change the future research state?
```

### Narrative explanation

```text
Why does the final author say this was reasonable?
```

Only the first two are audit objects here. Narrative explanation is evidence only when it is anchored to contemporaneous records rather than reconstructed after the outcome.

---

## 10. Anti-gaming rules

1. **No hindsight candidate inflation**: do not invent alternatives that were never genuinely live.
2. **No reason laundering**: post-hoc prose cannot replace the rule available at decision time.
3. **No field-count scoring**: more metadata is not automatically better verification.
4. **No SRT vocabulary bonus**: using `selection`, `bearer`, `writeback`, or `future selectability` earns zero points by itself.
5. **No weak provenance baseline**: Record A may include modern preregistration, failed-run retention, hashes, seeds and explicit decision criteria.
6. **No author omniscience assumption**: absence of a recorded candidate may reflect unknown state; mark `unknown`, do not reconstruct certainty.
7. **No AI agency inflation**: tool output or autonomous execution does not automatically relocate scientific responsibility from the human approval boundary.
8. **No successful-result privilege**: the protocol must work on invalid, negative, null and positive studies.

---

## 11. Pilot completion criteria

This protocol is **designed but not yet validated**.

The #746 pilot counts as complete only when:

- Record A is reconstructed independently;
- Record B is annotated at D1–D7;
- Pass A and Pass B are run under frozen questions;
- each risk class receives a detection / false-positive judgment;
- the incremental value of Record B is explicitly scored;
- the SRT-specific field block is deleted and the audit rerun;
- the result receives one of `R1/R2/R3/R4/N1`, not a rhetorical success label.

---

## 12. Current verdict

```text
Scientific verification gap: plausible and worth testing
Standard provenance baseline: must be strong
SRT-specific incremental value: NOT ESTABLISHED
Pilot target: PR #746
Pilot state: protocol designed; comparative audit not yet run
Canonical impact: none
Book / paper claim impact: none until validation
```

The intended standard is simple:

> **If deleting the SRT-specific choice fields changes nothing an auditor can correctly detect, the fields should not be retained merely because they fit SRT vocabulary.**
