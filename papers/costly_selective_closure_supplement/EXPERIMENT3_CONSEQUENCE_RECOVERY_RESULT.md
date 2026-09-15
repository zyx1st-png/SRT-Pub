# CSC Experiment 3 — Confirmatory Result

Date: 2026-09-15

Status: **FIRST PREREGISTERED CONFIRMATORY RUN — OUTCOME C / H1 NOT SUPPORTED**

## 1. Provenance

Preregistration-only commit:

`0c599c14ea24196c6e2d411ecd0e4e17124f18f1`

At that commit:

- Experiment 3 implementation did not yet exist;
- confirmatory seeds `1..30` had not been run;
- no Experiment 3 result existed.

Invariant-only validation used non-confirmatory seed `31` plus deterministic transition checks and explicitly confirmed that no seed in `1..30` had been executed.

Confirmatory execution commit:

`82a468857bbfa5475d349e5ad7295ee134c70fd0`

First confirmatory GitHub Actions run:

`34963586328` — **SUCCESS**

Immutable first-run artifact:

- artifact ID: `10395001598`
- artifact SHA-256: `54d567306ac87deaf36be553aea15a02ce2f20347a8a1e49be62d74a132e9630`
- exact result JSON imported into `results/consequence_recovery_results.json`
- no rerun was used to replace or select the first result.

Runtime recorded by the first run:

- Python `3.12.14`
- NumPy `2.5.3`
- checked-out scientific head `82a468857bbfa5475d349e5ad7295ee134c70fd0`.

## 2. Locked design actually executed

All four conditions were non-terminal and exactly 50 environment steps long.

On depletion every condition received:

- immediate rescue to `E0 = 6`;
- zero new explicit failure penalty;
- unchanged existing reward table;
- unchanged existing energy-gain table.

Only the number of subsequent forced-recovery steps differed:

```text
k0  = 0
k2  = 2
k5  = 5
k10 = 10
```

During a recovery step the failed agent did not sample a policy action and instead executed the already-existing `Rest` action. The step remained in environment time and in the preceding decisions' discounted return stream.

The primary endpoint was final-100-withdrawal mutual cooperation restricted to **eligible decision steps**, defined before execution as steps beginning with both agents outside recovery and able to choose normally.

## 3. Primary confirmatory result

Preregistered H1 required:

```text
rho > 0
AND
blocked-by-seed two-sided p < 0.05
```

Observed:

```text
tie-aware Spearman rho = -0.7037203560
blocked-by-seed two-sided p = 0.0000499975
PRIMARY H1 = NOT SUPPORTED
```

The association is statistically strong but in the **opposite direction** from the preregistered hypothesis.

This does not become a positive confirmatory finding by reversing the hypothesis after observing the data. Under the preregistered rule the result is Outcome C.

## 4. Locked endpoint contrast

Preregistered strong support additionally required:

```text
mean(k10 - k0) >= +0.10
AND
paired 95% CI excludes 0
```

Observed:

```text
mean(k10 - k0) = -0.0373433866
paired bootstrap 95% CI = [-0.0989698089, -0.0027866667]
practical +0.10 threshold = NOT MET
STRONG MANUSCRIPT SUPPORT = FALSE
```

In the first-run data, the `k10` primary endpoint is below the paired `k0` endpoint for all 30 confirmatory seeds. This is a strong endpoint regularity, but it is opposite to the preregistered positive prediction.

## 5. Condition summaries

| condition | mean post eligible-coop | median | fraction > 0.50 |
|---|---:|---:|---:|
| `k0` | 0.05477 | 0.00280 | 2/30 |
| `k2` | 0.10270 | 0.00103 | 3/30 |
| `k5` | 0.04885 | 0.00028 | 1/30 |
| `k10` | 0.01743 | 0.00000 | 1/30 |

The arithmetic means are attractor-sensitive. In particular `k2` contains several high-cooperation seeds and therefore has a larger mean than `k0`, even though its median is lower.

Accordingly, the data should **not** be described as a clean monotonic decline in condition means. The preregistered rank statistic nevertheless shows a strong overall negative ordinal association across paired seed-condition observations, and the `k10-k0` endpoint contrast is uniformly negative across seeds.

## 6. Manipulation and occupancy checks

| condition | mean episode length | mean depletion count | forced-recovery agent-step fraction | eligible-step fraction |
|---|---:|---:|---:|---:|
| `k0` | 50.0 | 3.710 | 0.000 | 1.000 |
| `k2` | 50.0 | 3.272 | 0.064 | 0.879 |
| `k5` | 50.0 | 3.549 | 0.160 | 0.724 |
| `k10` | 50.0 | 4.619 | 0.350 | 0.546 |

The manipulation therefore worked: longer recovery latency produced substantial temporary loss of normal action availability while the environment horizon remained exactly fixed.

The primary endpoint excluded forced-recovery steps by construction, so the negative primary association is not the trivial arithmetic consequence of counting a forced `Rest` step as voluntary non-cooperation.

## 7. Secondary common-state policy probe

A common bank of 2,000 decision-capable paired states was generated independently of confirmatory seeds `1..30`. Frozen end-of-withdrawal policies from every condition were evaluated on the same bank without applying recovery forcing.

Observed descriptive ordered association:

```text
secondary common-state rho = -0.8004443519
```

Condition means of expected mutual cooperation on the common bank:

| condition | mean expected mutual cooperation |
|---|---:|
| `k0` | 0.04139 |
| `k2` | 0.08355 |
| `k5` | 0.03393 |
| `k10` | 0.01240 |

For the paired `k10-k0` comparison, every confirmatory seed also has lower expected mutual cooperation under `k10` than under `k0` on this identical non-recovery state bank.

Thus the main negative direction is not explained solely by reduced eligible-step occupancy. Learned policies themselves differ in the same direction on common decision-capable states.

The secondary probe was preregistered as interpretive support only and cannot rescue the failed positive primary H1.

## 8. Confirmatory adjudication

The preregistered outcome is:

```text
OUTCOME C — NO CONFIRMATORY SUPPORT FOR THE POSITIVE RECOVERY-LATENCY HYPOTHESIS
```

More specifically:

> In this architecture, increasing a fully reversible, failure-triggered period of forced `Rest` does not reproduce the positive cooperation effect seen under terminal failure. The association is instead strongly negative: longer temporary loss of normal action opportunity is associated with lower learned costly cooperation.

This directly blocks the proposed inference:

```text
more unit-borne recovery burden
=> more cooperation / stronger CSC-like selective closure
```

That implication is not supported by Experiment 3 and should not be restored by post-result parameter tuning.

## 9. What the result does and does not establish

### Established by this experiment

- the locked latency manipulation was active and substantial;
- the episode remained non-terminal and exactly 50 steps;
- a longer forced-recovery interval did not create the predicted positive cooperation gradient;
- the endpoint `k10` condition was lower than `k0` for every paired seed;
- the common-state frozen-policy probe points in the same negative direction.

### Not established

Experiment 3 does **not** establish a universal law that recovery cost reduces cooperation.

The forced-`Rest` implementation simultaneously changes:

- temporary action availability;
- the interaction faced by the partner during recovery;
- the number and timing of genuine policy decisions;
- the discounted return sequence following a failure;
- the distribution of states visited during learning.

The observed negative effect is therefore architecture- and intervention-specific unless independently replicated under a different consequence mechanism.

Likewise, the result does not show that terminality, death, irreversibility, or return truncation is universally necessary for life-like organization.

## 10. Consequence for the CSC vulnerability dimension

The combined evidence is now:

```text
Experiment 1:
terminate versus cheap restore
= strong positive cooperation effect

Experiment 2:
persistent non-terminal metabolic impairment
= preregistered no-support result

Experiment 3:
fully reversible temporary action-opportunity loss
= preregistered positive H1 failed;
  strong opposite-direction association observed
```

This means the post-E2 proposal to make generic **consequence-bearing recovery burden** the empirical owner of `V` is also too broad.

Current evidence does not justify any of the following equivalences:

```text
V = damage persistence
V = generic recovery cost
V = temporary action loss
V = irreversibility as such
```

The only strong causal effect currently established by this experimental programme remains the narrower Experiment 1 transition:

> **terminal depletion versus cheap restoration changes learned policy strongly in the reported survival-coupled RL architecture.**

The larger cross-substrate interpretation must remain explicitly open.

## 11. Publication-path implication

The negative E2 followed by opposite-direction E3 changes the publication strategy materially.

The v17 paper should **not** present its four-dimensional profile as if the `V` dimension has now received broad experimental confirmation.

The defensible publication core is instead:

1. a carefully declared unit/boundary/timescale/recovery-regime profiling protocol;
2. a strong controlled terminal-versus-restore Experiment 1;
3. explicit acknowledgement that two preregistered non-terminal follow-ups failed to generalize the expected direction;
4. use of those failures to narrow the interpretation rather than conceal them.

No Experiment 4 should be launched merely to search for a positive non-terminal result. A further experiment would require a new independent theoretical reason that is not selected because Experiments 2 and 3 were unfavorable.

## 12. Current gate

```text
E3 PREREGISTRATION PROVENANCE = PASS
E3 INVARIANT CHECKS = PASS
FIRST CONFIRMATORY RUN = PASS / EXECUTED ONCE
RESULT PRESERVATION = PASS
PRIMARY POSITIVE H1 = FAIL / OPPOSITE DIRECTION
ENDPOINT PRACTICAL GATE = FAIL / OPPOSITE DIRECTION
SECONDARY COMMON-STATE DIRECTION = NEGATIVE
STRONG MANUSCRIPT SUPPORT = FALSE
POST-HOC RETUNING = FORBIDDEN
E4 POSITIVE-RESULT HUNT = STOP
#980 MERGE = HOLD FOR CONTENT REVIEW
#979 MERGE = HOLD
#978 MERGE = HOLD
V17 SUBMISSION = HOLD
NEXT = RECONSTRUCT PUBLICATION CLAIMS AROUND THE FULL E1/E2/E3 EVIDENCE
```
