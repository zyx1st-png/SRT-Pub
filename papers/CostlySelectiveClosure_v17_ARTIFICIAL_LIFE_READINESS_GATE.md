---
id: CSC-V17-ARTIFICIAL-LIFE-READINESS-GATE
type: publication_audit
status: draft
version: v17
target_venue: Artificial Life
canonical: false
---

# Costly Selective Closure v17 — Artificial Life Readiness Gate

Date: 2026-09-15

## 1. Scope

This gate evaluates the post-rejection v17 candidate only for journal readiness. It does not reopen SRT canonical theory, alter experiment code/results, or turn the Adaptive Behavior desk rejection into scientific evidence.

## 2. Current manuscript identity

Primary manuscript:

`papers/CostlySelectiveClosure_v17_ArtificialLife_candidate.md`

Historical submission records remain frozen:

- `papers/CostlySelectiveClosure_v16.md`
- `papers/CostlySelectiveClosure_AdaptiveBehavior_submission.tex`

Submission export is generated from the v17 candidate by:

`papers/build_artificial_life_v17_submission.py`

The builder removes repository-only frontmatter and repository notes, inserts the AI-assistance disclosure required by MIT Press policy, checks for old-symbol/internal residue, verifies six keywords, emits a submission Markdown artifact, and reports an approximate word count.

## 3. Journal-fit gate

**PASS — STRONG.**

Artificial Life explicitly publishes original work on synthesis of life and life-like phenomena in software, hardware and wetware, and work using such synthesis to improve theoretical understanding of life and life-like phenomena. The journal describes regular Articles as typically 6,000–12,000 words and requires a cover letter explaining journal fit.

CSC v17 now presents itself as:

1. a non-scalar profile protocol for cross-system comparison; and
2. a controlled synthetic experiment isolating one recovery-regime contrast.

This is a materially closer fit than the prior Adaptive Behavior positioning.

## 4. Scientific-core gate

**PASS.**

Retained empirical core:

- 30 paired seeds for the principal real-stake versus resettable contrast;
- post-withdrawal cooperation 0.55 versus 0.04;
- paired sign-flip permutation test;
- zero-penalty ablation;
- lives-gradient dose response;
- payoff sweep;
- common-state frozen-policy probe;
- fixed result files and reproducibility package.

No code or numerical result has been modified by the v17 conceptual revision.

## 5. Claim-scope gate

**PASS.**

v17 explicitly separates:

```text
controlled causal result
!= validation of four-dimensional CSC
!= proof of life
!= proof that physical irreversibility is universally necessary
```

The strongest empirical claim is limited to the reported survival-coupled RL architecture: changing depletion from terminate to restore changes the learned policy and strongly suppresses persistence of costly cooperation under cheap restoration.

## 6. Strongest-neighbor gate

**PASS — NARROW CONTRIBUTION ONLY.**

v17 no longer claims novelty for:

- precariousness;
- dimensional approaches to life/life-likeness;
- mortality constraints in artificial agents;
- reset versus persistent consequence as a general idea.

The manuscript directly situates itself against / beside:

- autopoiesis and biological autonomy;
- enactive precariousness, including Beer & Di Paolo (2023);
- Damiano & Stano (2020) on synthetic-cell life-likeness;
- Witkowski & Schwitzgebel (2024) on dimensions of life;
- Korecki et al. (2023) on irreversible artificial-agent death;
- Chen & Chen (2026) on mortality-grounded persistent bodily consequence versus reset;
- active inference / Markov-blanket work.

The remaining candidate contribution is the package:

```text
B / M / H / V maintenance-and-consequence profile
+
unit / boundary / timescale / recovery-regime declaration
+
non-scalar / experimentally decomposable use rule
+
matched terminate-versus-restore experiment
+
lives-gradient + payoff + common-state robustness package
```

This claim is narrower than the v16 positioning and is the version to defend.

## 7. Citation/reference gate

**PASS at current audit depth.**

Every substantive named neighbor introduced in the current v17 body has a corresponding reference entry. Recent reference status checks include:

- Baltieri & Suzuki — 2026, *Philosophical Transactions B*, listed by the author as “to appear”;
- Chen & Chen — arXiv:2608.27843, posted 2026-08-28;
- Witkowski & Schwitzgebel — *Artificial Life* 30(2), 193–215, DOI 10.1162/artl_a_00436;
- Beer & Di Paolo — *BioSystems* 223, 104823;
- Damiano & Stano — *Frontiers in Bioengineering and Biotechnology* 8, 953;
- Korecki et al. — ALIFE 2023, DOI 10.1162/isal_a_00633.

Before actual submission, run one final bibliographic-format pass for strict APA 7 punctuation/capitalization and confirm any “to appear” item has not changed status.

## 8. AI-policy gate

**P0 — RESOLVED IN EXPORT PATH / MUST REMAIN VISIBLE IN SUBMITTED MANUSCRIPT AND COVER LETTER.**

MIT Press policy requires authors who use AI tools to produce text/images or collect data to inform editors and be transparent in the manuscript.

For v17, OpenAI ChatGPT materially assisted manuscript development through literature discovery, structural critique, language revision, and consistency checking. The submission builder therefore inserts an explicit AI Assistance Disclosure, and the cover letter repeats the disclosure.

Do not delete or hide this statement in the submission artifact.

## 9. Supplement/reviewer-anonymity gate

**PASS IF SUPPLEMENT IS UPLOADED DIRECTLY OR PROVIDED THROUGH A NON-IDENTIFYING ACCESS ROUTE.**

Artificial Life allows supplementary material during review either as uploaded material or by URL, but URL access must not facilitate or potentially undermine reviewer anonymity.

Preferred submission route for this manuscript:

- upload the supplement ZIP directly with the initial submission;
- do not require reviewers to request permission;
- avoid access mechanisms that identify individual visitors/reviewers;
- preserve the exact result files and locked-environment metadata.

The historical Adaptive Behavior anonymization note remains provenance only and does not define Artificial Life review policy.

## 10. Format gate

**PASS WITH EXPORT WORK REMAINING.**

Current requirements to preserve in final preparation:

- Article route;
- initial manuscript PDF;
- cover letter explaining scope fit;
- 5–6 keywords (v17 has six);
- APA 7 citations/references;
- later accepted-version route supports LaTeX or Word;
- figures should be supplied in vector/high-resolution formats when required.

The existing supplement already contains vector PDF/SVG outputs for generated figures; the v17 body uses the former Figures 2–4 as Figures 1–3.

## 11. Over-deletion gate

**PASS.**

The v17 reduction removes material that was high-risk and low-evidence rather than removing the experimental argument:

Removed / demoted:

- manuscript-local `d = D_eff` as universal definition;
- `d_cog` weighted proxy;
- `G-hat` update equation;
- bookkeeping viability inequality;
- unsupported numeric cross-substrate rankings;
- claims that mortality/reset or multidimensionality are novel;
- ranking borderline biological cases by unsupported pseudo-precision.

Retained:

- four-part comparative intuition in paper-local terminology;
- level/boundary logic;
- matched experiment;
- all principal robustness analyses;
- common-state probe;
- biological and digital illustrative cases;
- clear falsifiable next experiment.

## 12. Remaining non-blocking issue

The strongest optional scientific upgrade remains a non-terminal irreversible-damage experiment with matched episode length, separating irreversible loss from return truncation. This would materially strengthen V as a broader architectural variable but is **not required** to justify submission of the current result as a narrow Article.

## 13. Final gate

```text
SCIENTIFIC CORE = PASS
ARTIFICIAL LIFE FIT = STRONG PASS
CLAIM SCOPE = PASS
STRONGEST-NEIGHBOR SURVIVAL = PASS / NARROW
CITATION-REFERENCE CLOSURE = PASS AT CURRENT AUDIT DEPTH
AI DISCLOSURE = REQUIRED / EXPORT PATH PREPARED
SUPPLEMENT ROUTE = PASS IF DIRECT-UPLOAD OR REVIEWER-SAFE ACCESS
NEW EXPERIMENT BEFORE SUBMISSION = NOT REQUIRED
MERGE #978 = NO (draft review state retained)
SUBMIT = NO UNTIL EXPORT IS GENERATED AND FINAL PDF/WORD-COUNT/APA CHECK IS RUN
NEXT = RUN SUBMISSION BUILDER + FINAL ARTIFACT REVIEW
```
