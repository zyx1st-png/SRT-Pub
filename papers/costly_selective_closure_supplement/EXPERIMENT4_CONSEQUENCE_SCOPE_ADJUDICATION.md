---
id: CSC-EXPERIMENT4-CONSEQUENCE-SCOPE-ADJUDICATION
type: experiment_adjudication
status: complete
canonical: false
claim_mode: confirmatory_result
preregistration: papers/costly_selective_closure_supplement/EXPERIMENT4_CONSEQUENCE_SCOPE_PREREGISTRATION.md
---

# CSC Experiment 4 — Consequence-Scope Confirmatory Adjudication

Date adjudicated: 2026-09-15

## 1. Governance and provenance

Experiment 4 was locked before implementation and before any confirmatory seed was run.

- preregistration first commit: `66cb46c45e99c5535c1f63b9c200ff9dbe911506`
- successful invariant run: `34977044998`
- first and only confirmatory run: `34977281851`
- confirmatory job: `104408120508`
- confirmatory execution head: `96e9a8bf0a1a45a39c7327533477e1bb76633d89`
- unique Actions artifact: `csc-e4-first-confirmatory-result`, artifact ID `10400498866`
- artifact ZIP SHA-256: `236c35cb1c7c44b404632438b4e411cc7113dd68ed4780e744af2cdf53dd3d4f`
- full result JSON SHA-256: `74b4452a90231dbefdac82fc18373cbecf346df75948092366cb49e6a23406b5`
- confirmatory cells: `2 scopes × 3 latencies × 30 seeds = 180`
- confirmatory seeds: exactly `101..130` in every cell
- common-state bank: exactly 2,000 paired states

The workflow's post-run structural check passed before artifact upload. No second confirmatory run was performed.

A repository compact-result record is stored at `results/consequence_scope_results_E4_confirmatory_record.json`. It preserves the locked design, exact adjudicated summaries, all latency-collapsed seed differences for the primary and secondary endpoints, and aggregate diagnostics. The full 10,112,971-byte JSON remains identified by the artifact/run IDs and SHA-256 above.

Governance note: an initial compact-record commit (`58efb3e0...`) contained manual row-transcription errors in a non-adjudicated copy of the cell-level rows. Those rows were not used for scientific interpretation. The record was replaced from the downloaded unique artifact at commit `c15d4695...` before this adjudication. The authoritative numerical source is the unique workflow artifact plus its matching job log.

## 2. Preregistered primary result

The primary endpoint was common-state expected mutual cooperation after withdrawal. For each seed, the preregistered analysis formed `shared - individual` within each latency and then averaged `k = 2, 5, 10` before the sole confirmatory sign-flip test.

Observed collapsed scope effect:

```text
mean(shared - individual) = +0.0299836682
95% paired bootstrap CI   = [+0.0119520663, +0.0538730310]
two-sided sign-flip p     = 0.0001499925
```

The preregistered support rule required `mean > 0` and `p < 0.05`. That rule passes.

The preregistered strong manuscript-level gate additionally required `mean >= +0.10` and a positive 95% CI lower bound. The CI lower bound is positive, but the mean effect is only about `+0.030`, so the `+0.10` practical-effect threshold fails.

Therefore the exact locked-matrix verdict is:

```text
E4 = OUTCOME B — POSITIVE BUT MODEST H-SCOPE SUPPORT
H-SCOPE confirmatory support = YES
H-SCOPE strong-support gate  = NO
```

The allowed interpretation is the preregistered Outcome-B interpretation: consequence scope has a detectable effect under this mechanism, but the effect is too small for a strong explanatory claim about E1 without further discrimination.

## 3. Seed distribution

The latency-collapsed primary effect was positive in 29 of 30 confirmatory seeds and negative in 1 of 30.

```text
mean   = +0.02998
median = +0.00952
IQR    = [+0.00371, +0.02799]
min    = -0.04875
max    = +0.27931
```

The distribution remains attractor-sensitive and right-skewed. The positive direction is nevertheless not carried only by one favorable seed: 29/30 collapsed seed contrasts are positive and the median is positive. This does not override the preregistered practical-effect threshold; it only characterizes the observed distribution.

## 4. Prespecified latency-level reporting

Latency-specific values are secondary descriptions and do not replace the collapsed primary test.

| Recovery latency | Mean shared-individual | Median | 95% paired bootstrap CI | Positive / zero / negative seeds |
| --- | ---: | ---: | --- | ---: |
| `k=2` | +0.00748 | +0.00145 | [-0.03492, +0.05169] | 22 / 0 / 8 |
| `k=5` | +0.06184 | +0.00518 | [+0.01965, +0.11406] | 28 / 0 / 2 |
| `k=10` | +0.02063 | +0.01274 | [+0.01395, +0.02792] | 30 / 0 / 0 |

There is no monotonic increase with latency (`k=5` has the largest mean effect), and no such monotonic pattern was required by the preregistration. No latency-specific result is promoted into a new confirmatory hypothesis.

## 5. Secondary rollout endpoint

Eligible mutual cooperation over the final 100 withdrawal episodes showed the same direction:

```text
collapsed mean(shared - individual) = +0.0331114780
95% paired bootstrap CI             = [+0.0119137860, +0.0621478150]
```

This is secondary. The confirmatory conclusion follows the common-state frozen-policy endpoint, not rollout occupancy.

## 6. Mechanism diagnostics

### 6.1 H-VICTIM: mixed diagnostic support, not a dominant explanation

During INDIVIDUAL recovery, the still-active partner overwhelmingly selected Solo rather than Cooperate:

| Latency | Cooperate | Solo | Rest |
| --- | ---: | ---: | ---: |
| `k=2` | 6.17% | 90.67% | 3.17% |
| `k=5` | 4.60% | 92.50% | 2.90% |
| `k=10` | 1.96% | 95.98% | 2.06% |

Thus the preregistered qualitative diagnostic `P(Solo) > P(Cooperate)` clearly passes: local recovery creates a real post-failure interval in which the active partner usually behaves Solo.

However, failure triggers are not predominantly the predicted `failed C vs partner Solo` pattern. In the INDIVIDUAL cells, `mutual Solo` is by far the largest recorded failure category:

```text
k=2: mutual Solo 8394; failed C vs Solo 1627; involving Rest 753
k=5: mutual Solo 8992; failed C vs Solo 1104; involving Rest 792
k=10: mutual Solo 9783; failed C vs Solo 711; involving Rest 1409
```

The same is true for first failures. Therefore H-VICTIM receives partial diagnostic support for the post-failure exploitation window, but the stronger story that E4 is mainly about asymmetric cooperator victimization is not supported by the trigger structure.

### 6.2 H-UPDATE: the specific E3 scaling confound is weakened

The successful invariant suite established the locked E4 fixed-horizon update: full 50-step return normalization, score-function gradients only on genuine decisions, and fixed `/50` scaling; `k=0` was required to match the original update numerically. Because E4 still yields a positive scope effect under this rule, the detected E4 contrast cannot be assigned to the particular E3 decision-count-dependent normalization/scaling artifact.

This does not eliminate every possible algorithm-specific effect.

### 6.3 H-TERM: weakened in its no-scope version, still live as an E1 explanation

E4 shows that a non-terminal consequence-scope manipulation can measurably change learned cooperation. That weakens the narrow rival claim that only terminality can matter and that shared non-terminal recovery should produce no stable scope effect.

But the effect is modest and E4 does not directly compare a shared non-terminal condition to the original terminal E1 condition within this preregistered test. Terminality / return truncation therefore remains a live explanation for why E1 produced a much larger effect. E4 does not establish that consequence scope fully explains E1.

## 7. Manipulation boundary

The SHARED manipulation is specifically a shared post-failure recovery consequence, not an abstract or substrate-independent notion of "shared fate".

When one agent fails, both agents are forced through the existing Rest transition. Rest itself has reward/energy dynamics, so at longer latency this can generate additional failures and refresh recovery. This becomes particularly visible at `k=10`:

```text
shared k=10 both-forced fraction = 0.60267
shared k=10 eligible fraction    = 0.39733
shared k=10 mean failures        = 5.77233
shared k=10 involving-Rest failure records = 13896
```

The primary common-state policy probe prevents forced-recovery occupancy from mechanically lowering the measured cooperation endpoint, but the learned policy is legitimately shaped by the recovery dynamics experienced during training. Accordingly, the safest mechanism label is **scope of failure-triggered recovery / action-opportunity consequence**, not generic mortality, shared fate, or universal irreversibility.

## 8. Hypothesis adjudication

```text
H-SCOPE  = SUPPORTED, MODEST; STRONG GATE FAILED
H-TERM   = REMAINS LIVE FOR E1; PURE NO-SCOPE VERSION WEAKENED
H-VICTIM = MIXED / PARTIAL DIAGNOSTIC SUPPORT; NOT DOMINANTLY ESTABLISHED
H-UPDATE = SPECIFIC E3 DECISION-COUNT SCALING RIVAL WEAKENED
```

No result here establishes that the agents are alive, that physical irreversibility is universally necessary, that consequence scope is a general ALife law, or that the full CSC profile is validated.

## 9. Publication consequence

The preregistration stated that support for H-SCOPE should move the publication framing toward **who bears failure-triggered future opportunity loss** rather than a generic non-dimensionality claim. E4 does cross the preregistered confirmatory support gate, so that direction is now empirically warranted.

However, because the result is Outcome B rather than Outcome A, any manuscript revision must preserve three restrictions:

1. describe consequence scope as a detectable but modest mechanism effect in this testbed;
2. keep terminality / return truncation live as an explanation for the larger E1 effect;
3. do not present E4 as strong validation of CSC as a whole.

This adjudication does not modify the manuscript or canonical SRT files. The publication candidate remains on scientific hold until an explicit manuscript-revision gate is opened and independently reviewed.

## 10. Closure

```text
E4 invariants = PASS
E4 confirmatory execution = VALID / FIRST AND ONLY RUN
E4 result = OUTCOME B
SECOND CONFIRMATORY RUN = NOT PERMITTED FOR THIS PREREGISTRATION
PARAMETER / ENDPOINT RETUNING = NOT PERMITTED
MANUSCRIPT EDIT = NOT IN THIS PR
CANONICAL EDIT = NONE
```
