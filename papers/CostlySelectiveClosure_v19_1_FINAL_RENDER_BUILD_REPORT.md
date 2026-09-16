---
id: CSC-V19-1-FINAL-RENDER-BUILD-REPORT-2026-09-16
type: publication_build_report
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
ai_do_not_use_for_definition: true
---

# CSC v19.1 — Final render build report

Date: 2026-09-16

This report records the final rendered submission artifacts produced from the validated v19.1 submission package. It changes no scientific result or interpretation.

## 1. Source / repository baseline

```text
main after submission-package landing = f15715a5429d9f68d8449864d6064fd4cdd2849c
PR #988 = MERGED
scientific content = E1-E4 CLOSED FOR CURRENT SUBMISSION
E5 = NOT RUN
E4 second confirmatory run = NO
parameter retuning = NONE
journal submission = NOT PERFORMED
```

The source submission builder had already passed with an approximate reader-facing word count of 8,739 words.

## 2. Final manuscript artifacts

Rendered manuscript title:

**Who Bears Failure? Consequence Scope and Terminality in Survival-Coupled Artificial Agents**

Artifacts produced for author delivery:

```text
Who_Bears_Failure_v19_1_Artificial_Life_Submission.docx
SHA-256 = 344b3a55e7d12ac05bcf2a9c55a1ce8f269d45e659c87e125675f00a12bd69ab

Who_Bears_Failure_v19_1_Artificial_Life_Submission.pdf
SHA-256 = 1fbec1757df6343a11aaced68a204e25c86523e8f35f63d14637eb88f00e2a7b
pages = 17
```

The final DOCX was rendered with the repository's two current figures, three manuscript tables, references and Appendices A-E intact.

## 3. Manuscript visual QA

The DOCX was rendered through the standard container-safe LibreOffice DOCX renderer to 17 page PNGs and PDF. Every page was visually inspected.

Checked conditions:

```text
clipped text = NONE FOUND
overlap = NONE FOUND
broken / missing glyphs = NONE FOUND
broken tables = NONE FOUND
figure clipping = NONE FOUND
figure-caption separation = PASS
page-number/footer placement = PASS
reference continuation = PASS
appendix continuation = PASS
```

After the cover-letter-only style adjustment, the manuscript DOCX was regenerated once more. Its 17 new rendered page images were then compared pixel-for-pixel against the already inspected render:

```text
page 1..17 = PIXEL IDENTICAL
```

The latest manuscript PDF was therefore regenerated from the latest DOCX and retained as the final PDF above.

## 4. Manuscript PDF preflight

```text
pages = 17
encrypted = NO
openable with PyMuPDF = YES
likely scanned = NO
XFA = NO
```

No PDF preflight blocking condition was detected.

## 5. Final cover-letter artifacts

Artifacts produced for author delivery:

```text
Who_Bears_Failure_v19_1_Cover_Letter.docx
SHA-256 = 706a80cc3e6ebec9bb3d2326d021b5ce60983986d4106b1fc2167f8cbdb34989

Who_Bears_Failure_v19_1_Cover_Letter.pdf
SHA-256 = cac7bde5e214ba575ffde7861286705485dcdbc2586e175f98f38682d09aabf8
pages = 1
```

The first cover-letter render placed only the signature block on a second page. That layout was rejected. Margins / paragraph spacing / type size were tightened without changing the letter's substantive content, and the final letter was regenerated as one clean page. The final page was visually inspected.

Cover-letter PDF preflight:

```text
pages = 1
encrypted = NO
openable with PyMuPDF = YES
likely scanned = NO
XFA = NO
```

## 6. Reviewer evidence package

The independently validated reviewer evidence package delivered with these artifacts is:

```text
CostlySelectiveClosure_v19_1_REVIEWER_EVIDENCE_PACKAGE.zip
SHA-256 = 5241e8d4f6e42ebaf5cc308f82b714cfc84bd674d2d94edd8c28d66b69a8f517
```

Its internal SHA-256 manifest had previously been independently recomputed with 39/39 entries matching. The full original E4 first-confirmatory JSON inside the package recomputed to:

`74b4452a90231dbefdac82fc18373cbecf346df75948092366cb49e6a23406b5`

The historical root supplement README and internal mechanism-development audits are not present in the reviewer ZIP.

## 7. Final boundary

```text
scientific manuscript = COMPLETE FOR CURRENT SUBMISSION CANDIDATE
submission source package = PASS
reviewer evidence package = PASS
final manuscript DOCX = PASS / VISUALLY VERIFIED
final manuscript PDF = PASS / VISUALLY VERIFIED / PREFLIGHT PASS
final cover-letter DOCX = PASS / VISUALLY VERIFIED
final cover-letter PDF = PASS / VISUALLY VERIFIED / PREFLIGHT PASS
external journal submission = NOT PERFORMED
```

Actual upload to *Artificial Life* remains a separate author-authorized external action.
