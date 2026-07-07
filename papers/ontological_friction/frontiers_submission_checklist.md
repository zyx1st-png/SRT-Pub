# Frontiers Submission Checklist — Revision Round (manuscript 1837760)

Rebuilt from the finalized `executive friction` draft after the first peer-review round.
Build artifacts refreshed (not stale): DOCX/PDF/HTML regenerated with Word equation objects,
figures regenerated, upload files re-numbered.

## Final submission package (what to upload)

| # | Item | File(s) | Status |
|---|---|---|---|
| 1 | **Manuscript** (primary upload) | `paper_ontological_friction_frontiers_submission.docx` | ✅ rebuilt, QA-passed |
| 1b | Manuscript PDF (review preview) | `paper_ontological_friction_frontiers_submission.pdf` | ✅ rebuilt (Word equations; math renders) |
| 1c | Manuscript HTML (optional preview) | `paper_ontological_friction_frontiers_submission.html` | ✅ rebuilt (MathJax) |
| 2 | **Response to reviewers** | `frontiers_response_to_reviewers.md` | ✅ point-by-point, both reviewers |
| 3 | **Figures** (separate high-res upload) | `figures/frontiers_upload/Figure{1..5}.tif` (+ `.jpg`) | ✅ re-numbered 1:1, 300 dpi |
| 3b | Figure zips | `figures/frontiers_upload/frontiers_figures_{tif,jpg}.zip` | ✅ rebuilt |
| 4 | **Supplementary** (at preregistration) | modal dictionaries, tokenization + model-spec + simulation scripts (see §5.6) | ⏳ released at preregistration, not at submission |
| 5 | **Conflict of Interest** | in manuscript (expanded, independent-researcher transparency) | ✅ |
| 6 | **Generative AI disclosure** | in manuscript (single occurrence; author-ownership wording) | ✅ |
| — | Scope / Contribution-to-Field statements | `frontiers_scope_statement.md`, `frontiers_contribution_to_field_statement.md` | ✅ paste into portal form |

## Post-review QA on rebuilt PDF (all verified)

- [x] Title appears once (no duplication).
- [x] Generative AI disclosure appears once (removed the duplicate mention from Acknowledgments).
- [x] No space-gluing artifacts (abstract and body clean).
- [x] `Ψ_f` renders correctly as a subscript everywhere (not `Ψ!` or `(4p)`); figure titles fixed too.
- [x] Figure captions in order 1→5; upload files map 1:1 to source scripts (see `figures/FIGURE_MAP.md`).
- [x] Page and line numbering present (Frontiers requirement).

## Academic figure QA refresh

- [x] Figure scripts' old numbering comments and print messages corrected.
- [x] Figure 2 readability improved.
- [x] Figure 3 causal wording softened.
- [x] Figure 4 marked as schematic predictions, not empirical estimates.
- [x] Figure 5 abbreviations reduced.
- [x] PNG/TIF/JPG regenerated.
- [x] DOCX/PDF/HTML regenerated.
- [x] Figure image-caption binding QA passed: each Figure 1–5 image is followed by its matching caption on the same page.

## Final figure visual QA

- [x] Figure 1 labels and threshold-region spacing refined.
- [x] Figure 2 checked for readability.
- [x] Figure 3 intervention wording softened.
- [x] Figure 4 schematic status retained and labels checked.
- [x] Figure 5 critical-load shading adjusted with vertical padding.
- [x] PNG/TIF/JPG regenerated.
- [x] DOCX/PDF/HTML regenerated.
- [x] Figure image-caption binding verified.

## Author / correspondence

- [x] Corresponding author details: Yuxin Zhang, zyx1st@gmail.com. *(Confirm/replace email in portal if a different address is preferred.)*
- [x] Affiliation: Independent Researcher, Kaili, Guizhou, China.
- [x] ORCID: 0009-0007-6659-8518.

## Still manual in the portal

- [ ] Paste scope statement into the submission form.
- [ ] Confirm all reference metadata (DOI completion where possible) in the portal.
- [ ] Upload the 5 figures as separate files in the correct numbered slots (use `frontiers_upload/Figure{1..5}`).
- [ ] Seek statistical consultation before preregistration/empirical implementation (noted in response letter).

## Reproducing the build

The manuscript now embeds the 5 figures at the end (after Table 5) so the DOCX/PDF are
self-contained for review; the separate `frontiers_upload/Figure{1..5}` files remain the
production-quality upload.

```
# from papers/ontological_friction, with pandoc + pypandoc:
uv run --with pypandoc python render_frontiers_submission_package.py
# figures: see figures/FIGURE_MAP.md
```

**PDF note.** The build script renders the PDF Word-free from the HTML via headless Chrome.
Each final figure is emitted as an indivisible print block on its own page, with the image
immediately followed by its matching caption.

The Chrome preview has figures and rendered math but no Frontiers line numbers (those are a
DOCX feature). The **DOCX is the authoritative upload** (native Word equations + line numbers,
figures embedded and verified pixel-identical to source). If a line-numbered PDF is needed,
convert the DOCX with Word after closing all other open Word documents.
