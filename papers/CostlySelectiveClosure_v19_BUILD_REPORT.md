---
id: CSC-V19-BUILD-REPORT
type: publication_build_report
status: active
canonical: false
---

# CSC v19 Build Report

This report records mechanical publication checks for the v19 candidate. It does not change or upgrade the scientific adjudications.

## 1. Submission builder

The hardened `papers/build_artificial_life_v19_submission.py` was executed against the v19 manuscript after the strongest-neighbor correction and preregistration-provenance revisions. The reviewer-facing build deterministically inserts the E1-E4 architecture schematic (Figure 1) and the E1-E4 evidence summary (Figure 2).

```text
submission builder = PASS
approximate reviewer-facing word count = 7716
Artificial Life 6,000-12,000 Article range = PASS
keywords = 6 / PASS
required v19 hard guards = PASS
superseded v18 / scalar-V wording guards = PASS
Figure 1 insertion = PASS
Figure 2 insertion = PASS
```

The first attempted builder execution exposed one guard-only wording mismatch: the builder required the literal phrase `E5 is not required`, while the manuscript correctly said `does not require an immediate Experiment 5`. The guard was corrected to the actual manuscript wording; no scientific claim or result changed.

## 2. Reference closure

The manuscript contains 15 reference entries. All 15 author forms are cited in the manuscript body, including the multi-word surname `Di Paolo` that a first-pass single-token regex failed to count.

```text
reference entries = 15
reference-body closure = PASS
strongest-neighbor additions = Tampuu et al. (2017); Scott & Pitt (2023)
unused v18 references = removed at current audit depth
```

## 3. Figures

Figure 1 is the E1-E4 failure-transition architecture schematic:

`papers/costly_selective_closure_supplement/figures/figure1_experiment_architectures_v19.svg`

Figure 2 is generated deterministically from the committed result records:

- E1: terminal vs restore post-withdrawal cooperation mean +/- 1 SD;
- E2: damage-duration condition means +/- 1 SD;
- E3: recovery-latency condition means +/- 1 SD;
- E4: all 30 latency-collapsed shared-minus-individual frozen-policy effects plus the preregistered paired 95% CI.

Permanent source:

`papers/costly_selective_closure_supplement/figures/figure2_evidence_summary_v19.svg`

Both figures passed local visual QA with no clipping, overlap, or label collision. Figure 2 retains the negative E4 seed and high positive attractor seeds rather than hiding them behind the mean.

Verified Figure 2 SVG SHA-256:

`59edbe7da69d7b7f7b54a07f21bc758335e306eee586f2bbf4ac5d5ef51bed46`

## 4. Reviewer-facing manuscript packaging

Final local reviewer-facing artifacts were generated from the v19 submission text and the two committed figures.

```text
DOCX generation = PASS
PDF generation = PASS
final PDF pages = 24
all 24 pages visually inspected = PASS
keywords-only blank page = fixed
multi-page integrated-evidence table header/reflow = fixed
clipping / overlap / broken glyphs / black boxes = NONE FOUND
PDF openable = PASS
PDF encrypted = NO
likely scanned = NO
embedded fonts = PASS
PDF preflight warnings = NONE
```

Artifact SHA-256 values:

```text
DOCX = 107bd227250965b1975bb01287041f789b997eba334d4de89c9396cc8ce88e39
PDF  = 57dac17b0321d7b5b7c82700252a3d64cbbbc5fc083514933937b30e1f772fa0
```

## 5. Cover letter

The v19 Artificial Life cover letter was rendered as a compact one-page reviewer/editor-facing document and visually inspected.

```text
cover-letter DOCX = PASS
cover-letter PDF = PASS / 1 page
cover-letter PDF preflight = PASS
cover-letter encrypted = NO
cover-letter likely scanned = NO
cover-letter fonts embedded = PASS
```

## 6. Reviewer evidence package

A static reviewer **evidence/provenance package** was built. It is intentionally not labelled a full standalone reproduction bundle because its packaged JSON files are compact evidence summaries rather than every raw result row and training artifact. The package points to authoritative repository code/result paths and exact preregistration commits.

```text
package role = reviewer evidence/provenance package
full standalone reproduction bundle = NO
package SHA-256 = 222d6203ae269825693afb915c18743f942dc09c5282a5afd8f89d56cf47e99b
```

## 7. Boundary

```text
scientific result changes = NONE
E5 = NOT RUN
E4 = NOT RERUN
parameter retuning = NONE
canonical SRT edits = NONE
reviewer-facing manuscript QA = PASS
reviewer evidence package = PASS / BOUNDED
journal submission = NOT PERFORMED
```
