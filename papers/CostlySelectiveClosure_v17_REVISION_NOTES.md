---
id: CSC-V17-REVISION-NOTES
type: revision_memo
status: draft
version: v17
target_venue: Artificial Life
derived_from: papers/CostlySelectiveClosure_v16.md
---

# Costly Selective Closure v17 — Post-Rejection Revision Notes

## 1. Trigger

Adaptive Behavior manuscript `AB-26-0280`, *Costly Selective Closure: A Comparative Heuristic for Life-Likeness in Artificial Systems*, received an editor-in-chief desk rejection dated 2026-09-04 on journal-appropriateness grounds and did not enter associate-editor or peer review.

Repository adjudication for this revision treats that outcome as:

```text
VENUE-LEVEL REJECTION
!= scientific adverse evidence
!= experimental failure
!= requirement to rewrite current SRT ontology into the manuscript
```

The historical v16 manuscript and `CostlySelectiveClosure_AdaptiveBehavior_submission.tex` remain unchanged as submission records.

## 2. v17 target and scope

Primary next-venue candidate:

```text
Artificial Life (MIT Press)
article route
```

The v17 goal is **conceptual decontamination + methodological sharpening**, not a new SRT theory cycle.

Explicit non-actions:

- no canonical SRT owner edits;
- no #976 dependency or backflow;
- no rewrite of `CostlySelectiveClosure_v16.md`;
- no rewrite of the historical Adaptive Behavior export;
- no experiment-code or result-file changes in this landing;
- no claim that the four-dimensional heuristic has been jointly validated.

## 3. P0 changes implemented

### P0-01 — remove SRT-symbol collision

v16 used:

```text
d = selective bandwidth = D_eff(...)
Psi_f = maintenance cost
eta = hysteretic memory
V = irreversible vulnerability
```

Current SRT canonical usage no longer permits bare `d` to mean effective rank/selective breadth. v17 therefore uses manuscript-local dimensions:

```text
B = selective breadth
M = maintenance burden
H = historical retention
V = irreversible vulnerability
```

The manuscript now stands independently of SRT canonical symbol ownership.

### P0-02 — remove weak formalism

Removed from v17:

- `x_(t+1) = (1-eta) Ghat_theta[Omega_t] + eta x_t`;
- `d = D_eff(Ghat)` as a universal definition;
- `d_cog` weighted proxy equation;
- the viability bookkeeping inequality involving `q`, `P_sel`, `Psi_f`, `N`, and `kappa_i`.

Reason:

```text
no direct role in the causal experiment
+ no cross-substrate calibration
+ unnecessary symbol collision / pseudo-precision risk
```

### P0-03 — remove unsupported numeric profile rankings

v16 assigned approximate numerical values such as:

- Lenia `d ~ 1-3`;
- autopoietic/evolved agents `d ~ 5-20`;
- organisms `d ~ 10^2-10^4`.

v17 replaces those with qualitative, explicitly non-calibrated profiles.

### P0-04 — narrow causal language

v17 no longer treats the experiment as direct validation of “life-likeness.”

Primary supported statement:

> Within this survival-coupled reinforcement-learning architecture, changing depletion from terminate to restore causally changes the learned policy and strongly suppresses the persistence of costly cooperation under cheap restoration.

CSC then **interprets** terminate-versus-restore as one operational probe of vulnerability.

### P0-05 — move organizational levels before interpretation

v17 makes the following distinction explicit before the experiment is interpreted:

```text
episode-token
!= controller-lineage
!= training process
```

This prevents the phrase “real stake” from implying that the learned controller itself is physically destroyed on token termination.

## 4. P1 changes implemented

### P1-01 — fairer strongest-neighbor framing

v16 section `Why Existing Criteria Stop Too Early` is replaced by a comparative-gap framing.

Current posture:

```text
autopoiesis / autonomy / enactivism / active inference / evolutionary theory
already explain substantial parts of the problem;
CSC contribution = explicit cross-system profiling + manipulable recovery-regime variable
```

No superiority or whole-theory non-substitutability claim is made.

### P1-02 — profile declaration rule

A CSC profile is well formed only after declaring:

1. organizational unit;
2. boundary;
3. timescale;
4. recovery regime.

This rule is intended to stabilize claims about who bears maintenance burden and what counts as irreversible failure.

### P1-03 — profile is not a scalar score

v17 states explicitly:

- B/M/H/V are not assumed orthogonal;
- there is no universal life-likeness scalar;
- profiles are diagnostic rather than calibrated rankings.

### P1-04 — borderline cases become diagnostic rather than verdictive

v17 no longer ranks prion versus virus or assigns maximal/minimal dimension values as if measured.

Borderline examples now illustrate:

- level dependence;
- burden externalization;
- phase dependence;
- separation of inherited organization from active maintenance.

### P1-05 — conceptual Figure 1 retired from v17

The historical v16 `figure1_framework.*` retains the old symbols and is not used by v17.

v17 uses only the existing experimental figures:

- design;
- main results / robustness;
- common-state probe.

The historical generator and figure remain unchanged for provenance.

## 5. Empirical assets retained unchanged

The v17 manuscript preserves the following reported results:

- post-withdrawal cooperation: real `0.55` vs resettable `0.04` across 30 paired seeds;
- paired sign-flip permutation `p < 0.0001`;
- zero-penalty ablation: `0.50` vs `0.05`;
- lives-gradient dose-response and blocked-by-seed Spearman test;
- payoff sweep: real > resettable in all 6 cells;
- common-state frozen-policy probe: `0.485` vs `0.030` at end-of-withdrawal;
- common-state paired difference `0.454`, 95% CI `[0.346, 0.557]`, `p < 0.0001`.

No result JSON, algorithm, seed plan, or statistical procedure is changed by this revision.

## 6. New explicit limitation

The strongest next experiment is identified but **not required for current resubmission**:

```text
matched episode length
+ irreversible non-terminal capacity loss
vs
matched transient damage with full recovery
```

Purpose: separate broader irreversibility from return-stream termination.

Current status:

```text
OPTIONAL STRENGTHENING
NOT SUBMISSION BLOCKER
```

## 7. Reference / venue cleanup

- Baltieri & Suzuki updated from the stale v16 `2025 / in press` form to `2026 / to appear` based on the authors' current publication listing.
- v17 uses 6 keywords, matching current Artificial Life author guidance.
- v17 is framed as a regular Article candidate rather than a review or fast-track letter.

## 8. Current gate

```text
SCIENTIFIC CORE = KEEP
ADAPTIVE BEHAVIOR REJECTION = VENUE-LEVEL ONLY
CURRENT SRT ONTOLOGY BACKFLOW = NO
OLD SRT SYMBOL LEAKAGE = REPAIRED IN V17
WEAK PSEUDO-QUANTITATIVE FORMALISM = REMOVED
EXPERIMENTAL CORE = PRESERVED
ARTIFICIAL LIFE FIT = STRONG CANDIDATE
NEW EXPERIMENT = OPTIONAL / NOT BLOCKING
```

Next gate after this landing:

```text
independent v17 content review
-> check accidental over-deletion
-> check experimental wording against code/results
-> check citation/reference accuracy
-> then decide whether to build journal-formatted PDF/LaTeX and cover letter
```
