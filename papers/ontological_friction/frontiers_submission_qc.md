# Frontiers Submission QC Checklist

Date: 2026-03-24

## 1) Metadata

- [x] Article type: Hypothesis and Theory
- [x] Keywords count: 8 (within 5-8 target)
- [x] First-page metadata uses synchronized journal-facing counts: ~10,000 main-text words; 185 abstract words; 5 figures; 5 tables
- [x] Title shortened for journal-facing readability while preserving the core claim
- [x] Symbol rendering check added for key math tokens (e.g., `\Psi_f`, `\rho_c`) in abstract and contribution sections after export
- [x] Single-author declarations use "The author declares"
- [x] Upload DOCX now matches the journal-facing `executive friction` manuscript rather than the older `ontological friction / SRT / L0-L1-L2` branch
- [x] Author name / affiliation block is present in the synchronized DOCX
- [x] Contribution-to-the-Field text moved to a separate submission-form file
- [x] Manuscript export includes page numbers and line numbers
- [x] Source manuscript for upload is the line-numbered DOCX
- [x] Regenerated DOCX now stores math as Word equations (OMML) rather than raw LaTeX-like `$...$` strings; local spot checks confirm inline and display math tokens such as `\Psi_f`, `\rho_c`, and `\mu_{\text{sem}}` are exported as equation objects
- [x] Local PDF preview refreshed on `2026-03-24` from the synchronized journal-facing DOCX (supporting asset only; authoritative source remains the DOCX or portal-generated review PDF)

## 2) Core-definition consistency

- [x] Single retained Definition 2: Distress Hazard Family (smoothed derivative + appraisal)
- [x] No residual hard-identity claim `Pain(t) = dPsi/dt`
- [x] Single retained Definition 3 label: Selection Budget Inequality (Thermodynamic-Inspired)
- [x] `rho*` locked as primary confirmatory estimator; ratio-based `rho` sensitivity-only

## 3) Tables and figures

- [x] Figure citation order in body is sequential: Figure 1 -> 2 -> 3 -> 4 -> 5
- [x] Strict submission manuscript created with figure callouts in body and figure captions collected after References
- [x] Figure files exist:
  - `figures/fig1_srt_architecture.png`
  - `figures/fig2_proxy_map.png`
  - `figures/fig5_ros_dag.png` (used as Figure 3)
  - `figures/fig3_clinical_radar.png` (used as Figure 4)
  - `figures/fig4_experimental_design.png` (used as Figure 5)
- [x] Table numbering is sequential: Table 1 -> 5
- [x] Table references updated to new numbering (clinical signature table = Table 2)
- [x] Strict submission manuscript moves all editable tables to the end of the manuscript
- [x] Strict submission DOCX contains no embedded `word/media` assets; figures are upload-separate only
- [x] Frontiers upload figure assets exist for Figure 1–5 in both JPG and TIFF bundles
- [x] Local image metadata check confirms Figure 1–5 upload assets are 300 dpi in both JPG and TIFF variants

## 4) Reproducibility and policy sections

- [x] AI usage disclosure included
- [x] Ethics statement included (no human/animal data in this theoretical manuscript)
- [x] Data availability statement includes reproducibility commitment (`mu_sem` dictionary + analysis scripts upon empirical execution)
- [x] Conflict of interest statement included

## 5) Limited mechanism-boundary patch (2026-08)

- [x] Added a narrow limitation that scalar latent-cost estimation does not uniquely identify the generating dynamical organization
- [x] Preserved the Level-0 estimand / Level-1 candidate-mechanism distinction
- [x] Added no formula, figure, table, primary hypothesis, or new mechanism definition
- [x] Added no external reference; source verification for the motivating force-organization preprint remains outside the submission manuscript
- [x] Expected word-count change is small and does not alter the approximate first-page count (`~10,000`)
- [x] No equation, figure, table, section, or bibliography cross-reference changes
- [x] No portal metadata update is required beyond regenerating the final upload artifact from the revised source

## 6) Remaining pre-submission actions (manual)

- [ ] Confirm corresponding-author email and any required correspondence line in manuscript / portal metadata
- [ ] Verify reference style exactly matches Frontiers bib requirements in final submission format
- [x] Ensure submission system "Contribution to the Field" box uses the final approved text
- [x] Upload figure files with final legend-number mapping exactly as in manuscript
- [ ] If required by handling editor, provide preregistration template links when available
- [ ] Open the portal-generated review PDF (preferred final QA target) and verify no upload-stage equation regressions or malformed inline math (especially first appearances of `\Psi_f`, `\rho^*`, `\rho_c`)
