---
id: CSC-V19-1-SUBMISSION-READINESS-2026-09-16
type: publication_readiness
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
ai_do_not_use_for_definition: true
---

# CSC v19.1 — Artificial Life submission-readiness closeout

Date: 2026-09-16

Current manuscript:

`papers/CostlySelectiveClosure_v19_1_ArtificialLife_candidate.md`

Title:

**Who Bears Failure? Consequence Scope and Terminality in Survival-Coupled Artificial Agents**

Target venue: *Artificial Life* / Article

## 1. Scientific stop condition

The manuscript's scientific work package is closed at E1–E4 for the current submission candidate.

```text
new confirmatory experiment = NO
E4 second confirmatory run = NO
parameter retuning = NO
E5 required for current manuscript = NO
post-hoc E4 individual-latency cross-check = EXPLORATORY ONLY
external journal submission = NOT PERFORMED
```

The v19.1 manuscript explicitly preserves:

- E1 as discovery / not preregistered;
- E2 and E3 as separately preregistered failed positive generalizations;
- E4 as separately preregistered positive-but-modest scope support below the +0.10 strong-effect threshold;
- E1/E4 numerical non-comparability as a causal decomposition;
- the bundled nature of E4 shared recovery;
- algorithm/testbed generality limits;
- the distinction between confirmatory and post-hoc exploratory analyses.

## 2. Current journal-policy checks

The 2026-09-16 venue check records the current requirements relevant to this package:

- Article length typically `6,000–12,000` words;
- initial manuscript submitted as PDF through the online system;
- cover letter required;
- manuscript substantially unique and not under review elsewhere;
- `5–6` keywords;
- APA 7 citation/bibliography style;
- review-stage supplementary access must not facilitate or potentially undermine reviewer anonymity;
- vector graphics preferred for line art/plots;
- generative-AI use must be transparently disclosed and AI systems may not be authors.

The live submission interface must still be checked immediately before upload for any changed operational instruction.

## 3. Submission-text builder

Submission-text builder:

`papers/build_artificial_life_v19_1_submission.py`

It strips repository-only frontmatter/note, enforces the v19.1 scientific boundaries, enforces 5–6 keywords and the 6,000–12,000 Article word-count range, and patches the reader-facing AI disclosure for submission.

The submission disclosure names:

- OpenAI ChatGPT / OpenAI, including GPT-5.6 Sol, accessed 2026-09-16;
- Anthropic Claude / Anthropic, accessed September 2026, with the exact Claude model version explicitly recorded as not retained rather than invented.

It states that neither system is an author and that confirmatory numerical results come from preserved experiment outputs rather than generative-model output.

## 4. Cover letter

Current cover letter:

`papers/CostlySelectiveClosure_v19_1_ArtificialLife_COVER_LETTER.md`

It presents the manuscript as an E1–E4 experimental decomposition rather than as a new generic claim that shared consequences promote cooperation. It discloses both ChatGPT and Claude use and states that the manuscript is substantially unique and not under review elsewhere.

## 5. Reviewer evidence / reproduction package

Reviewer entry:

`papers/costly_selective_closure_supplement/REVIEWER_README_v19_1.txt`

Whitelist authority:

`papers/CostlySelectiveClosure_v19_1_REVIEWER_PACKAGE_MANIFEST.md`

Deterministic builder:

`papers/build_csc_v19_1_reviewer_package.py`

The builder is whitelist-only. It intentionally excludes the historical supplement root `README.md`, which belongs to an earlier manuscript and contains superseded `double-blind`, scalar-V and four-dimensional CSC framing. It also excludes internal theory/mechanism-development notes not needed to inspect or reproduce the reported results.

## 6. E4 full first-confirmatory artifact preservation

The GitHub Actions copy of the first E4 confirmatory result was scheduled to expire on 2026-09-22. The full result has therefore been persistently preserved in this repository as a lossless XZ payload:

`papers/costly_selective_closure_supplement/artifacts/E4_first_confirmatory_consequence_scope_results_2026-09-15.json.xz`

Provenance / integrity:

```text
workflow run = 34977281851
Actions artifact ID = 10400498866
confirmatory head SHA = 96e9a8bf0a1a45a39c7327533477e1bb76633d89
Actions ZIP SHA-256 = 236c35cb1c7c44b404632438b4e411cc7113dd68ed4780e744af2cdf53dd3d4f
full consequence_scope_results.json SHA-256 = 74b4452a90231dbefdac82fc18373cbecf346df75948092366cb49e6a23406b5
preserved XZ SHA-256 = 283fac7d641d77ea937ccc65f120d750c9b7740bc6b1f29857e84188df639a84
```

The reviewer-package builder decompresses this XZ payload and requires the full JSON hash to match before creating the ZIP.

## 7. Figures

Current manuscript figures:

- `papers/costly_selective_closure_supplement/figures/figure1_experiment_architectures_v19.svg`
- `papers/costly_selective_closure_supplement/figures/figure2_evidence_summary_v19_1.svg`

Figure 2 is distribution-aware and does not use mean ± SD as the main summary for the floor-dominated E2/E3 distributions. E4 uses a separate delta axis and is explicitly not placed on a common severity/effect scale with E1–E3.

## 8. Remaining pre-upload operations

The remaining work is packaging/rendering rather than new scientific inference:

1. run the v19.1 submission-text builder;
2. run the deterministic reviewer-package builder and record its ZIP SHA-256;
3. render the submission text to the final PDF (and editable DOCX/source if desired);
4. visually inspect the rendered PDF for figure/table/page-break/reference problems;
5. render/check the cover letter;
6. check the live *Artificial Life* submission interface one final time;
7. upload only after explicit author authorization.

No item in this list authorizes journal submission by itself.

## 9. Current verdict

```text
scientific content = READY FOR SUBMISSION PACKAGING
claim boundaries = HARDENED
reviewer evidence source set = FIXED BY WHITELIST
full E4 first-confirmatory artifact = PERSISTENTLY PRESERVED
cover letter source = READY
submission builder = READY
reviewer package builder = READY
final rendered PDF/DOCX = TO BE REBUILT FROM v19.1
external submission = NOT PERFORMED / REQUIRES SEPARATE AUTHOR AUTHORIZATION
```
