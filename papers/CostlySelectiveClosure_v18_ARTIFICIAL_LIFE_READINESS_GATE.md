# Costly Selective Closure v18 — Artificial Life Readiness Gate

## Scope

This gate applies to the evidence-led v18 manuscript:

**Failure Is Not One-Dimensional: Terminality, Persistent Damage, and Recovery Architecture in Artificial Agents**

It does not alter historical v16/v17 manuscripts, the E2/E3 preregistrations or result artifacts, or canonical SRT files.

## Scientific gate

```text
E1 terminal-vs-restore causal contrast = PASS / bounded to the reported architecture
E1 zero-penalty robustness = PASS
E1 lives-gradient robustness = PASS
E1 payoff-sweep robustness = PASS
E1 common-state frozen-policy probe = PASS
E1 seed heterogeneity disclosure = PASS
E1 historical statistical-method label = PASS
E1 post-hoc matched-seed sensitivity = PASS
E2 preregistered positive generalization = NOT SUPPORTED / RETAINED
E3 preregistered positive generalization = FAILED / OPPOSITE DIRECTION / RETAINED
E4 positive-result hunt = STOP
```

The E1 historical result is explicitly identified as a two-sided two-sample label-permutation analysis. The v18 paired sign-flip analysis is explicitly post-hoc sensitivity analysis on fixed committed outcomes and does not replace or relabel the historical test.

## Conceptual gate

```text
scalar-like V = RETIRED
B / M / H = RETAINED AS DESCRIPTIVE QUESTIONS ONLY
B / M / H universal validation = NOT CLAIMED
consequence architecture = LIVE STRUCTURED DESCRIPTOR
universal life score = NOT CLAIMED
mortality/precariousness priority = NOT CLAIMED
algorithm-general effect = NOT CLAIMED
```

The supported conceptual conclusion is that the tested consequence mechanisms cannot safely be compressed into one ordered vulnerability/recoverability axis. The manuscript does not infer that every form of consequential failure has the same effect or that the observed E3 negative direction is universal.

## Preregistration gate

```text
E1 prospectively preregistered = NO / DISCLOSED
E2 separately repository-preregistered before confirmatory implementation/execution = YES
E3 separately repository-preregistered before confirmatory implementation/execution = YES
full E1/E2/E3 programme prospectively preregistered = NO / DISCLOSED
third-party preregistration service = NO / DISCLOSED
```

## Strongest-neighbor / novelty gate

The manuscript does not claim priority for:

- precariousness or adaptive normativity;
- multidimensional life/life-likeness;
- artificial mortality;
- persistent-vs-reset consequence as a general idea;
- the fact that termination changes reinforcement-learning returns;
- reset costs;
- restricted or stochastic action availability.

The surviving contribution is the evidence-led combination of:

1. explicit organizational unit / boundary / timescale / recovery-regime declaration;
2. structured consequence-architecture decomposition rather than scalar V;
3. the matched E1 terminal-vs-restore intervention plus robustness package;
4. separately preregistered E2 and E3 generalization attempts;
5. transparent retention of null/opposite-direction evidence that forces theoretical narrowing;
6. reproducible seed-level visualization and statistical sensitivity audit.

Verdict: **PASS / NARROW**.

## Artificial Life fit

```text
software artificial-life testbed = YES
life-like organization question = YES
synthetic manipulation tied to theoretical interpretation = YES
clear hypotheses / context / reproducibility / careful analysis = YES
Article-length target (6,000–12,000 words) = PASS
latest guarded submission word count = 6,956
keywords = 6 / PASS
cover letter = PRESENT / v18-specific
AI assistance disclosure = PRESENT
```

## Reproducibility and statistical transparency

Permanent publication assets include:

- `papers/build_artificial_life_v18_submission.py`
- `papers/costly_selective_closure_supplement/audit_e1_paired_sensitivity.py`
- `papers/costly_selective_closure_supplement/generate_v18_evidence_summary.py`
- `papers/costly_selective_closure_supplement/figures/figure2_evidence_summary_v18.svg`

The submission builder hard-fails on superseded v17 framing and on the old incorrect wording that described the historical E1 main test as paired sign-flip inference.

Latest full statistical-transparency artifact check before the final two-sentence scope tightening: Actions run `34969917124` = SUCCESS. The subsequent scope tightening changed two framing sentences only, and the builder passed again at 6,956 words.

## Governance

Publication reconstruction remains stacked on the completed E1/E2/E3 evidence branch. Temporary execution/check workflows and one-time patch scripts are removed after use. Final Governance Preflight must be green on the latest clean head before merge.

## Remaining submission mechanics

The scientific/content gate no longer requires a new experiment. Remaining work is mechanical publication packaging:

- generate the final reviewer-facing PDF from the guarded v18 submission artifact;
- perform visual/typographic QA and final APA-format spot check;
- prepare reviewer-safe supplementary upload/package;
- verify manuscript/cover-letter metadata in the submission system.

These mechanics should not be used to reopen the scientific claim unless they expose a concrete inconsistency.

## Final adjudication

```text
SCIENTIFIC CORE = PASS / BOUNDED
EVIDENCE-LED THEORY REVISION = PASS
PREREGISTRATION TRANSPARENCY = PASS
STATISTICAL TRANSPARENCY = PASS
STRONGEST-NEIGHBOR SURVIVAL = PASS / NARROW
ARTIFICIAL LIFE FIT = STRONG PASS
NEW EXPERIMENT REQUIRED BEFORE SUBMISSION = NO
CONTENT READINESS = READY FOR AUTHOR SUBMISSION PACKAGING
MERGE #981 = HOLD / AUTHOR DECISION
JOURNAL SUBMISSION = NOT PERFORMED
```
