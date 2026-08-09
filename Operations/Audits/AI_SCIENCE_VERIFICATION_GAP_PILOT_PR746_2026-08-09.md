---
id: SRT-AI-SCIENCE-VERIFICATION-GAP-PILOT-PR746-20260809
type: audit_result
status: archived
run_status: completed_dry_run
layer: meta
epistemic_layer: os
claim_mode: audit
claim_level: P4_governance
canonical: false
ai_do_not_use_for_definition: true
created: 2026-08-09
tags: [AI, Science, Verification, Provenance, ChoiceTrace, Audit, PR746, NegativeResult]
dependency:
  - Operations/Audits/AI_SCIENCE_VERIFICATION_GAP_SRT_AUDIT.md
  - papers/stake_future_selectability/01_mvp_spec_lock.md
  - papers/stake_future_selectability/03_mvp_decision.md
pilot_target:
  pull_request: 746
  title: "Stake–Future Selectability MVP: complete locked P4 experiment"
validation_status: single_session_nonblind
---

# AI Science Verification Gap — PR #746 Pilot Dry Run

> **Top-line verdict**: on PR #746, a strong standard provenance baseline already captures almost all scientifically load-bearing verification information. The SRT-specific choice-trace layer does **not** yet demonstrate a distinct risk-detection advantage. Current classification: **R3 target-relative dispensable for this pilot**, with one unresolved niche around contemporaneous authority / live-candidate logging that #746 did not record in a way that can now be independently validated.

## 0. Why this is a dry run, not validation

This audit was executed in one already-informed session after the #746 result and the verification-gap protocol were known. Therefore:

```text
not blind
not independent
not a valid estimate of auditor effect size
```

It is useful only for:

- checking whether the protocol is operational;
- discovering obvious redundancy;
- deciding which fields deserve prospective capture in a future case.

It must not be cited as evidence that SRT choice trace improves scientific verification.

---

## 1. Strong-baseline rule

The provenance baseline is intentionally generous. It includes not only raw execution logs, but also modern scientific controls already present in #746:

- preregistration / scientific lock;
- exact formal seeds and config;
- code / manifest hashes;
- fixed analysis blocks and thresholds;
- leakage tests;
- failed manipulation gate;
- retained unfavorable outcomes;
- explicit protocol deviations and pre-lock repairs;
- final claim boundary;
- reproducibility metadata.

This matters because SRT earns no credit by comparing choice trace against a weak “code + final PDF only” baseline.

---

## 2. Record A — provenance-only reconstruction

### A1. Scientific target

The frozen target was whether early-B `dV_CF_pre` adds leave-one-master-seed-out prediction of C-stage adaptability `Q_C` beyond current state, homeostasis, controllability and generic adaptive-dynamics controls.

The construct was explicitly P4 surrogate stake; no metric was declared to measure canonical `d`.

### A2. Pre-outcome lock

Before formal C outcomes:

- formal seeds were fixed;
- X/T/S condition meanings were fixed;
- Reach20 / Emp5 controls were fixed;
- `dV_CF_pre` was fixed as the primary pre-C proxy;
- M0–M4 block order was fixed;
- GO/NARROW/NO-GO-related thresholds were fixed;
- pre-C artifacts were hashed and made immutable before C instantiation.

### A3. Formal integrity

The final record preserves:

- 72 A→B→C trajectories;
- 72/72 pre-C hash checks;
- 24/24 T resets;
- 24/24 S persistence;
- stable identities and zero replacements.

### A4. Invalidating gate

The preregistered T/S Reach20 validity condition passed only 40/48 coupled cells. The top-level result therefore became:

```text
UNINTERPRETABLE PROTOCOL
```

The record explicitly refuses to replace the failed frozen Reach20 gate with favorable Emp5 behavior.

### A5. Favorable secondary signal retained but not promoted

The formal cohort produced a small positive S−X `dV_CF_pre` separation. That result was preserved, but the record states that it did not correspond to improved future adaptation and could not rescue the primary bridge.

### A6. Unfavorable predictive result retained

M4 did not add useful grouped out-of-sample prediction over M3. The final report preserves the negative incremental CV result, worsened NRMSE, interval-crossing coefficient, and seed instability.

### A7. Pre-lock repairs disclosed

Two pre-lock implementation problems were disclosed:

1. the probe originally allowed integrity to cap probe energy and was repaired so only the intended integrity input changed;
2. a training-summary bug reporting `reward_sum=0` was repaired and regression-tested.

The record explicitly distinguishes these pre-lock repairs from post-lock scientific parameter changes.

### A8. Future claim boundary

The final record does not convert the failed MVP into support for SRT. It preserves only a narrower future question: whether a better structural manipulation and proxy could test same-bearer consequence return / future selectability beyond standard controls.

---

## 3. Pass A risk detection

Using Record A alone, this dry run can already judge the protocol's six verification-gap classes.

| Risk class | Detectable from provenance alone? | PR #746 finding |
|---|---|---|
| VG-1 hidden result selection | **yes, strongly** | formal cells, unfavorable model results and favorable secondary signal are all retained; no selective rerun is reported |
| VG-2 failed-path suppression | **yes, strongly** | failed Reach20 gate and negative M4 results remain visible and constrain the verdict |
| VG-3 post-hoc hypothesis rewriting | **yes, strongly** | pre-outcome lock plus final decision makes the before/after target comparison explicit |
| VG-4 evaluator drift | **yes, strongly** | Emp5 is not substituted for failed Reach20; positive `dV` does not replace locked primary criteria |
| VG-5 responsibility relocation | **partial / unresolved** | repository shows human-owned PR and AI/Codex-assisted execution, but exact decision authority at each node is not contemporaneously decomposed |
| VG-6 future-path laundering | **yes** | final claim boundary carries the failure forward and does not present the MVP as positive support |

### Pass A score — qualitative dry-run

```text
R_detection: high for 5/6 classes; partial for VG-5
R_false: no clear false risk identified
criterion_drift_detection: high
ailed failed_path_recall: high
future_claim_boundary: high
authority_accuracy: incomplete
```

The key finding is already unfavorable to the SRT-specific application: **the scientifically important selection discipline is visible in ordinary lock / decision / reproducibility records.**

---

## 4. Record B — reconstructed selection-aware trace

Because no contemporaneous scientific choice-trace file exists for #746, Record B can only be reconstructed from existing records. Such reconstruction is lower-quality evidence than live capture.

### D1 — probe bug

- `candidate_set_at_decision`: keep flawed smoke / repair probe / redesign larger construct.
- `selected`: repair the integrity-only probe before pilot/formal.
- `criterion_state`: `repaired_prelock`.
- `rejected_candidates`: proceeding with contaminated probe; changing scientific target.
- `path_writeback`: obsolete smoke no longer admissible as evidence; corrected probe becomes required for later phases.
- `failed_branch_retention`: reported in final decision, though obsolete smoke tree was not part of tracked active outputs.

**Increment over Record A**: negligible for scientific validity; possible small gain in making the alternative set explicit.

### D2 — training-summary bug

- `candidate_set_at_decision`: accept zero summary / repair reporting / alter reward definition.
- `selected`: repair accounting and add regression test; do not alter reward science.
- `criterion_state`: `repaired_prelock`.
- `path_writeback`: summary correctness becomes test-covered.

**Increment**: negligible. Provenance already records the repair and unchanged scientific definition.

### D3 — pilot interpretation

- `candidate_set_at_decision`: tune proxy / tune thresholds / change formal seeds / freeze unchanged.
- `selected`: freeze unchanged.
- `criterion_state`: pre-lock.
- `rejection_rule`: pilot is A/B-only feasibility evidence; no C outcome exists; unfavorable pilot proxy pattern cannot be used to tune the formal test.

**Increment**: small. The spec lock already says no candidate parameter changed after inspection and explicitly notes the pilot lacked a favorable S-over-X pattern.

### D4 — formal Reach20 failure

- `candidate_set_at_decision`: obey Reach20 / substitute Emp5 / combine metrics / relax threshold.
- `selected`: obey frozen Reach20; verdict becomes uninterpretable.
- `criterion_state`: prelocked.
- `rejected_candidates`: favorable Emp5 rescue; threshold relaxation.
- `path_writeback`: no clean GO/NARROW/NO-GO interpretation from this protocol.

**Increment**: essentially zero. This is already one of the clearest parts of standard provenance.

### D5 — positive S−X `dV_CF_pre`

- `candidate_set_at_decision`: treat as bridge support / treat as descriptive secondary / use to rescue result.
- `selected`: retain as secondary only.
- `rejection_rule`: proxy separation without stable primary-outcome prediction is insufficient.

**Increment**: essentially zero. The final decision states this explicitly.

### D6 — negative M4 increment

- `candidate_set_at_decision`: report / suppress / reframe around within-sample coefficient or proxy separation.
- `selected`: report negative incremental prediction and uncertainty.
- `path_writeback`: no evidence of incremental predictive value under locked model comparison.

**Increment**: zero to small. Standard provenance already makes this reconstructible.

### D7 — future continuation

- `candidate_set_at_decision`: SRT falsified / bridge supported / narrow unresolved manipulation question remains.
- `selected`: narrow unresolved question remains.
- `counterfactual_reopen_rule`: a future design would need a more robust structural manipulation / proxy and must again beat standard controls.

**Increment**: modest conceptual clarity, but the final decision already contains nearly the same claim boundary.

---

## 5. Pass B incremental score

Compared with Record A, reconstructed Record B changes little on the frozen scientific risk dimensions.

| Metric | Record A | Record B | Increment |
|---|---:|---:|---:|
| known-risk detection | high | high | ~0 |
| false-risk control | high | high | ~0 |
| criterion-drift detection | high | high | ~0 |
| failed-path recall | high | high | ~0 |
| future-claim boundary | high | high | small at most |
| authority attribution | partial | still partial | **not validated** |
| audit efficiency | already compact | more fields | unknown / possibly worse |

The two fields that look potentially non-redundant are:

1. `candidate_set_at_decision` — what alternatives were genuinely live;
2. `human_override_point / model_override_point` — who actually possessed decision authority.

But #746 did not contemporaneously record these as structured choice-trace fields. Reconstructing them after outcomes are known risks hindsight inflation and reason laundering. Therefore this pilot cannot credit them as demonstrated verification gain.

---

## 6. Subtractive audit result

Delete from Record B:

```text
candidate_set_at_decision
rejected_candidates
human_override_point
model_override_point
bearer_of_consequence
path_writeback
counterfactual_reopen_rule
```

while retaining the strong standard provenance in Record A.

### Observed dry-run loss

For #746:

- invalid manipulation detection: preserved;
- primary/secondary criterion separation: preserved;
- post-hoc rescue detection: preserved;
- failed-result retention: preserved;
- future claim boundary: preserved;
- scientific conclusion: preserved;
- exact per-node authority decomposition: still unresolved either way.

Therefore the SRT-specific block is currently:

```text
R3 — target-relative dispensable
```

for **verification of this PR's scientific validity and claim boundary**.

This does **not** mean choice traces are globally useless. It means #746 is a case where unusually good preregistration and negative-result discipline already perform most of the work.

---

## 7. The useful negative finding

The strongest result of this pilot is not “choice trace works.” It is the opposite:

> **A well-designed preregistration + provenance + negative-result record can already encode most scientifically important selection history without SRT vocabulary.**

This narrows the SRT research question substantially.

A future choice-trace system should not compete with provenance on information already well handled by:

- preregistration;
- version control;
- manifests;
- seeds;
- failed-run retention;
- frozen criteria;
- explicit decision reports.

Its only plausible remaining niche is information that these systems often do not capture:

```text
live candidate alternatives at the moment of choice
+ actual human/model authority boundary
+ contemporaneous rejection reason
+ explicit rule for reopening a killed path
```

Even that niche must be tested prospectively rather than reconstructed after the fact.

---

## 8. Prospective test redesign

The next valid test should instrument a **new** AI-assisted research workflow before outcomes exist.

Capture only four extra fields prospectively:

```yaml
candidate_set_at_decision:
selected:
rejection_rule_at_time:
authority_boundary:
```

Do not start with the full ten-field SRT trace. That would increase audit burden before incremental value is shown.

Then compare:

```text
strong provenance baseline
vs
strong provenance + four prospective choice fields
```

on an external or at least non-SRT-shaped research workflow.

### Required positive result

Retain the four-field layer only if it improves at least one pre-frozen dimension without materially increasing false alarms:

- hidden candidate suppression detection;
- criterion-drift detection;
- responsibility / authority attribution;
- premature closure / reopenability judgment;
- audit time or reads.

Otherwise classify it R1/R3 again.

---

## 9. Pilot verdict

```text
Target: PR #746
Run type: single-session, non-blind dry run
Standard provenance quality: unusually strong
SRT-specific added risk detection: not demonstrated
Scientific conclusion changed by choice trace: no
Main unresolved niche: contemporaneous candidate-set + authority-boundary capture
Subtractive classification: R3 target-relative dispensable
Recommended next step: prospective four-field instrumentation on a new workflow
Canonical impact: none
Paper / book claim impact: none
```

This is a useful failure of the initial application hypothesis: **for a well-governed experiment like #746, SRT choice trace currently looks more like metadata duplication than an independently valuable scientific verification layer.**
