---
id: CSC-V19-BUILD-REPORT
type: publication_build_report
status: active
canonical: false
---

# CSC v19 Build Report

This report records mechanical publication checks for the v19 candidate. It does not change or upgrade the scientific adjudications.

## 1. Submission builder

The current `papers/build_artificial_life_v19_submission.py` was executed against the current v19 manuscript after the strongest-neighbor and preregistration-provenance revisions. After the verified E1-E4 Figure 2 link/caption was inserted into the reviewer-facing build, the guarded submission text was re-counted.

```text
submission builder = PASS
approximate guarded word count = 7630
Artificial Life 6,000-12,000 Article range = PASS
keywords = 6 / PASS
required v19 hard guards = PASS
superseded v18 / scalar-V wording guards = PASS
Figure 2 insertion = PASS
```

The first attempted execution exposed one guard-only wording mismatch: the builder required the literal phrase `E5 is not required`, while the manuscript correctly said `does not require an immediate Experiment 5`. The guard was corrected to the actual manuscript wording; no scientific claim or result changed.

## 2. Reference closure

The manuscript contains 15 reference entries. All 15 first authors / author forms are cited in the manuscript body, including the multi-word surname `Di Paolo` that a first-pass single-token regex failed to count.

```text
reference entries = 15
reference-body closure = PASS
strongest-neighbor additions = Tampuu et al. (2017); Scott & Pitt (2023)
unused v18 references = removed at current audit depth
```

## 3. E1-E4 evidence figure

The v19 evidence figure is generated deterministically from the committed result records:

- E1: terminal vs restore post-withdrawal cooperation mean +/- 1 SD;
- E2: damage-duration condition means +/- 1 SD;
- E3: recovery-latency condition means +/- 1 SD;
- E4: all 30 latency-collapsed shared-minus-individual frozen-policy effects plus the preregistered paired 95% CI.

Permanent source:

`papers/costly_selective_closure_supplement/figures/figure2_evidence_summary_v19.svg`

Local visual QA of the generated SVG found no clipping, overlap, or label collision. The E4 negative seed and high positive attractor seeds remain visible rather than being hidden behind the mean.

Verified SVG SHA-256:

`59edbe7da69d7b7f7b54a07f21bc758335e306eee586f2bbf4ac5d5ef51bed46`

## 4. Boundary

```text
scientific result changes = NONE
E5 = NOT RUN
E4 = NOT RERUN
parameter retuning = NONE
canonical SRT edits = NONE
reviewer-safe static reproduction package = NEXT PACKAGING GATE
final DOCX/PDF visual QA = PENDING
```
