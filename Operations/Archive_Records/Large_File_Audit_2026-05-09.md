---
id: SRT-LARGE-FILE-AUDIT-2026-05-09
type: audit_report
tags: [LargeFiles, ConnectorSafety, DocumentationEngineering]
status: active_v1
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
---

# Large File Audit 2026-05-09

> Purpose: identify files that may be truncated by GitHub-style connectors and route them into split, archive, or artifact policies.

- Generated: 2026-05-09
- Warning threshold: `48.8 KiB`
- Action threshold: `68.4 KiB`
- Urgent threshold: `97.7 KiB`
- Excluded scan roots: `.git/`, `.claude/`

## active_text

| Risk | Size | File | Split / handling |
|---|---:|---|---|
| urgent | 1288.1 KiB | `Experiments/choicemap_explicit_scaffolding/outputs/confirmatory/processed/compute_budget_audit.csv` | - |
| urgent | 895.3 KiB | `Output/pdf/从存在到秩序_完整稿_2026-07-04.md` | missing_or_not_needed |
| urgent | 829.9 KiB | `Output/从存在到秩序_完整版_2026-06-23.md` | missing_or_not_needed |
| urgent | 453.7 KiB | `Output/pdf/从存在到秩序_哲学读者试读版_2026-07-04.md` | missing_or_not_needed |
| urgent | 326.1 KiB | `Output/从存在到秩序_哲学读者试读版_2026-06-23.md` | missing_or_not_needed |
| urgent | 218.2 KiB | `01_Source_Intuition/BOOK/BOOK_CHAPTER_CARDS_2026-05-22.md` | missing_or_not_needed |
| urgent | 202.5 KiB | `Governance/Frontmatter_Warning_Baseline.txt` | missing_or_not_needed |
| urgent | 180.3 KiB | `Experiments/stake_future_selectability_mvp/manifests/probe_state_bank.json` | - |
| urgent | 131.9 KiB | `01_Source_Intuition/BOOK/External_Theory_Notes/BARAD_SRT_ALIGNMENT_AND_INSERTION_MAP_2026-06-10.md` | missing_or_not_needed |
| urgent | 125.9 KiB | `01_Source_Intuition/BOOK/BOOK_PROBLEM_CHAIN_REWRITE_2026-05-21.md` | missing_or_not_needed |
| urgent | 117.8 KiB | `Experiments/choicemap_explicit_scaffolding/outputs/confirmatory/processed/seed_level_metrics.csv` | - |
| urgent | 112.7 KiB | `Neuroscience/SRT_Neural_Mechanisms.md` | Neuroscience/Neural_Mechanisms_Split |
| urgent | 110.3 KiB | `Philosophy/SRT_Philosophy_Ethics.md` | Philosophy/Ethics_Split |
| action | 97.2 KiB | `Core/SRT_Core_14_Dynamics_Scaling.md` | Core/Dynamics_Scaling_Split |
| action | 96.0 KiB | `01_Source_Intuition/BOOK/BOOK_VERSION_LOG.md` | missing_or_not_needed |
| action | 94.2 KiB | `Experiments/stake_future_selectability_mvp/outputs/formal/processed/preC_features.json` | - |
| action | 90.9 KiB | `Physics/SRT_Physics_Cosmology.md` | Physics/Cosmology_Split |
| action | 88.7 KiB | `SRT_Glossary.md` | Glossary/README.md |
| action | 82.5 KiB | `Philosophy/SRT_Philosophy_Foundations.md` | Philosophy/Foundations_Split |
| action | 82.3 KiB | `AI/SRT_AI_01_Ontology.md` | AI/Ontology_Split |
| action | 80.9 KiB | `Governance/_SRT_CHANGELOG_2026.md` | Governance/_SRT_CHANGELOG_2026_Split |
| action | 79.5 KiB | `Core/SRT_Core_13a_Operator_Basics.md` | Core/Operator_Basics_Split |
| action | 76.0 KiB | `Core/SRT_Core_12b_Ontology_L2.md` | Core/Ontology_L2_Split |
| action | 75.6 KiB | `Core/SRT_Core_01_Axioms.md` | Core/Axioms_Split |
| action | 74.9 KiB | `AI/SRT_AI_03_Consciousness_Framework.md` | AI/Consciousness_Framework_Split |
| action | 74.0 KiB | `SRT/未命名 1.md` | SRT/未命名 1_Split |
| action | 72.8 KiB | `Philosophy/Papers/Before_Objects_Selection_Realism.md` | missing_or_not_needed |
| action | 70.2 KiB | `Philosophy/SRT_Social_Economics.md` | Philosophy/Social_Economics_Split |
| warning | 66.9 KiB | `Philosophy/Papers/Forcing_CH_Research_Regime_Staged_Draft_EN.md` | missing_or_not_needed |
| warning | 66.6 KiB | `Core_Law/SRT_Collective_Tower_Hardening_Notes.md` | Core_Law/Collective_Tower_Hardening_Notes_Split |
| warning | 65.2 KiB | `Core/SRT_Core_22_Equations.md` | Core/Equations_Split |
| warning | 64.5 KiB | `Physics/SRT_Phys_09_Formalism_Ext.md` | Physics/Formalism_Ext_Split |
| warning | 63.5 KiB | `Core/SRT_OPEN_TENSIONS.md` | missing_or_not_needed |
| warning | 62.8 KiB | `Philosophy/SRT_Ethics_Agency.md` | Philosophy/Ethics_Agency_Split |
| warning | 62.7 KiB | `Philosophy/Papers/Forcing_CH_Evidence/D05_C5op_Goedel_to_Cohen_Audit.md` | missing_or_not_needed |
| warning | 62.6 KiB | `01_Source_Intuition/Conversations/2026-07-12_SRT_Theory_Discussion_Transcript_CN.md` | missing_or_not_needed |
| warning | 62.4 KiB | `Philosophy/Papers/Biomarkers_Before_Treatments_NT1_Decoupled_TCI.md` | missing_or_not_needed |
| warning | 62.2 KiB | `01_Source_Intuition/Conversations/2026-07-12_SRT_本体论_意识_AI_交流原始转录.md` | missing_or_not_needed |
| warning | 59.7 KiB | `Philosophy/Papers/Forcing_CH_Evidence/D05b_Forcing_Representation_and_Method_Family_Audit.md` | missing_or_not_needed |
| warning | 59.5 KiB | `Neuroscience/SRT_Neuro_08_Immune_Dist.md` | Neuroscience/Immune_Dist_Split |
| warning | 57.7 KiB | `Core_Law/SRT_L1_Formalism.md` | Core_Law/L1_Formalism_Split |
| warning | 57.2 KiB | `Experiments/stake_future_selectability_mvp/outputs/formal/processed/C_outcomes.json` | - |
| warning | 57.0 KiB | `Philosophy/Papers/Before_Objects_Selection_Realism_Submission_EN.md` | missing_or_not_needed |
| warning | 56.9 KiB | `Philosophy/SRT_Social_Cognition.md` | Philosophy/Social_Cognition_Split |
| warning | 56.4 KiB | `Philosophy/SRT_SocTheory_06_L2_Dynamics.md` | Philosophy/L2_Dynamics_Split |
| warning | 54.6 KiB | `Experiments/selective_resynchronization_mvp/outputs/processed/phase_summary.csv` | - |
| warning | 54.3 KiB | `Physics/SRT_Quant_01_Selection.md` | Physics/Selection_Split |
| warning | 53.7 KiB | `Core/SRT_Core_12a_Ontology_L0L1.md` | Core/Ontology_L0L1_Split |
| warning | 52.6 KiB | `Core_Law/SRT_Reference_Dynamics.md` | Core_Law/Reference_Dynamics_Split |
| warning | 50.8 KiB | `AI/Ontology_Annex/00_General_Boundary_Block.md` | AI/Ontology_Annex/General_Boundary_Block_Split |
| warning | 50.7 KiB | `Physics/SRT_Quant_02_Cosmology.md` | Physics/Quant_02_Cosmology_Split |
| warning | 50.6 KiB | `AI/SRT_AI_Architecture.md` | AI/Architecture_Split |
| warning | 50.0 KiB | `01_Source_Intuition/SRT_CHOICEMAP_RANDOM_RESYNCHRONIZATION_TRACE_2026-07-09.md` | missing_or_not_needed |
| warning | 49.9 KiB | `Philosophy/SRT_SocTheory_05_Language_Eco.md` | Philosophy/Language_Eco_Split |
| warning | 49.3 KiB | `Neuroscience/SRT_Consciousness_Mechanisms.md` | missing_or_not_needed |

## artifact_or_generated

| Risk | Size | File | Split / handling |
|---|---:|---|---|
| urgent | 3127.9 KiB | `papers/ontological_friction/paper_ontological_friction_frontiers_submission.pdf` | artifact/generated; do not use as primary connector read path |
| urgent | 2460.1 KiB | `papers/ontological_friction/paper_ontological_friction_frontiers_submission.docx` | artifact/generated; do not use as primary connector read path |
| urgent | 1070.7 KiB | `papers/CostlySelectiveClosure_AdaptiveBehavior_submission.docx` | artifact/generated; do not use as primary connector read path |
| urgent | 462.4 KiB | `Operations/Context_Bundles/SRT_CONTEXT_BUNDLE_SPINE.md` | artifact/generated; do not use as primary connector read path |
| urgent | 363.1 KiB | `papers/costly_selective_closure_supplement/figures/figure4_common_state_probe.png` | artifact/generated; do not use as primary connector read path |
| urgent | 336.4 KiB | `papers/costly_selective_closure_supplement/figures/figure3_results.png` | artifact/generated; do not use as primary connector read path |
| urgent | 277.3 KiB | `Operations/_SRT_DEEP_NAV_COVERAGE_AUDIT_REPORT.json` | artifact/generated; do not use as primary connector read path |
| urgent | 267.5 KiB | `Archive/root_misc/Pasted image 20260306100654.png` | artifact/generated; do not use as primary connector read path |
| urgent | 207.8 KiB | `Operations/Context_Bundles/SRT_CONTEXT_BUNDLE_COMPACTCORE.md` | artifact/generated; do not use as primary connector read path |
| urgent | 181.2 KiB | `papers/costly_selective_closure_supplement/figures/figure1_framework.png` | artifact/generated; do not use as primary connector read path |
| urgent | 142.4 KiB | `papers/costly_selective_closure_supplement/figures/figure2_design.png` | artifact/generated; do not use as primary connector read path |
| urgent | 137.4 KiB | `papers/ontological_friction/paper_ontological_friction_frontiers_submission.html` | artifact/generated; do not use as primary connector read path |
| urgent | 121.8 KiB | `papers/costly_selective_closure_supplement/figures/figure1_framework.pdf` | artifact/generated; do not use as primary connector read path |
| urgent | 116.5 KiB | `video/package-lock.json` | artifact/generated; do not use as primary connector read path |
| urgent | 114.0 KiB | `papers/ontological_friction/paper_ontological_friction.html` | artifact/generated; do not use as primary connector read path |
| urgent | 111.4 KiB | `papers/ontological_friction/paper_ontological_friction_frontiers_submission.md` | artifact/generated; do not use as primary connector read path |
| urgent | 108.2 KiB | `Archive/raw_sessions/SRT_SESSION_RAW_TRANSCRIPT_2026-03-31.md` | artifact/generated; do not use as primary connector read path |
| urgent | 107.2 KiB | `Operations/_SRT_DEEP_NAV_PATH_AUDIT_REPORT.json` | artifact/generated; do not use as primary connector read path |
| urgent | 106.2 KiB | `Operations/Context_Bundles/SRT_CONTEXT_BUNDLE_DOMAIN_PHILOSOPHY.md` | artifact/generated; do not use as primary connector read path |
| urgent | 102.7 KiB | `Archive/root_misc/Selection-Reality Theory (SRT).pdf` | artifact/generated; do not use as primary connector read path |
| action | 97.6 KiB | `Operations/Context_Bundles/SRT_CONTEXT_BUNDLE_DOMAIN_PHYSICS.md` | artifact/generated; do not use as primary connector read path |
| action | 91.1 KiB | `papers/ontological_friction/paper_ontological_friction_zh.html` | artifact/generated; do not use as primary connector read path |
| action | 87.9 KiB | `papers/ontological_friction/paper_ontological_friction.md` | artifact/generated; do not use as primary connector read path |
| action | 87.9 KiB | `papers/ontological_friction/paper_ontological_friction_preprint.md` | artifact/generated; do not use as primary connector read path |
| action | 83.1 KiB | `papers/costly_selective_closure_supplement/figures/figure3_results.pdf` | artifact/generated; do not use as primary connector read path |
| action | 82.5 KiB | `Operations/Context_Bundles/SRT_CONTEXT_BUNDLE_DOMAIN_AI.md` | artifact/generated; do not use as primary connector read path |
| action | 81.7 KiB | `papers/costly_selective_closure_supplement/figures/figure3_results.svg` | artifact/generated; do not use as primary connector read path |
| action | 80.4 KiB | `papers/costly_selective_closure_supplement/figures/figure4_common_state_probe.pdf` | artifact/generated; do not use as primary connector read path |
| action | 75.1 KiB | `papers/CostlySelectiveClosure_AdaptiveBehavior_submission.tex` | artifact/generated; do not use as primary connector read path |
| action | 74.0 KiB | `Operations/Context_Bundles/SRT_CONTEXT_BUNDLE_DOMAIN_NEUROSCIENCE.md` | artifact/generated; do not use as primary connector read path |
| action | 69.2 KiB | `papers/history_dependent_reachability/manuscript/MANUSCRIPT.md` | artifact/generated; do not use as primary connector read path |
| action | 69.0 KiB | `papers/costly_selective_closure_supplement/figures/figure4_common_state_probe.svg` | artifact/generated; do not use as primary connector read path |
| warning | 67.6 KiB | `papers/ontological_friction/paper_ontological_friction_zh.md` | artifact/generated; do not use as primary connector read path |
| warning | 65.9 KiB | `papers/CostlySelectiveClosure_v16.md` | artifact/generated; do not use as primary connector read path |
| warning | 64.0 KiB | `papers/SRT_MetaOS_JCS_v2.md` | artifact/generated; do not use as primary connector read path |
| warning | 61.5 KiB | `papers/markov_blanket/paper_markov_blanket_d_value.md` | artifact/generated; do not use as primary connector read path |
| warning | 59.1 KiB | `papers/SRT_MetaOS_JCS_v1.md` | artifact/generated; do not use as primary connector read path |
| warning | 56.4 KiB | `papers/costly_selective_closure_supplement/results/common_state_probe.json` | artifact/generated; do not use as primary connector read path |
| warning | 54.8 KiB | `papers/alife2026_pilot_results/v2_costly_selection/results_nopenalty.json` | artifact/generated; do not use as primary connector read path |
| warning | 54.8 KiB | `papers/costly_selective_closure_supplement/results/zero_penalty_results.json` | artifact/generated; do not use as primary connector read path |
| warning | 51.5 KiB | `papers/alife2026_pilot_results/v2_costly_selection/results_full.json` | artifact/generated; do not use as primary connector read path |
| warning | 51.5 KiB | `papers/costly_selective_closure_supplement/results/main_results.json` | artifact/generated; do not use as primary connector read path |

## binary_or_media

| Risk | Size | File | Split / handling |
|---|---:|---|---|
| urgent | 11553.0 KiB | `Output/pdf/从存在到秩序_完整稿_2026-07-04.pdf` | binary/media artifact |
| urgent | 6252.5 KiB | `Output/pdf/从存在到秩序_试读版_2026-07-04.pdf` | binary/media artifact |
| urgent | 4383.1 KiB | `Experiments/choicemap_explicit_scaffolding/outputs/confirmatory/raw/candidate_logs.parquet` | binary/media artifact |
| urgent | 2082.1 KiB | `Experiments/choicemap_explicit_scaffolding/outputs/confirmatory/raw/episode_logs.parquet` | binary/media artifact |
| urgent | 324.2 KiB | `tmp/pdfs/srt_book_watermark_p80.png` | binary/media artifact |
| urgent | 316.7 KiB | `tmp/pdfs/srt_book_watermark_p20.png` | binary/media artifact |
| urgent | 255.6 KiB | `tmp/pdfs/srt_book_watermark_p333.png` | binary/media artifact |
| urgent | 255.3 KiB | `tmp/pdfs/srt_book_watermark_p333_fixed.png` | binary/media artifact |
| urgent | 227.1 KiB | `tmp/pdfs/srt_spine_copyable_p90.png` | binary/media artifact |
| urgent | 197.4 KiB | `Experiments/selective_resynchronization_mvp/outputs/figures/abc_full_learning_curves.png` | binary/media artifact |
| urgent | 173.5 KiB | `Experiments/selective_resynchronization_mvp/outputs/processed/step_metrics.parquet` | binary/media artifact |
| urgent | 168.2 KiB | `tmp/pdfs/srt_spine_copyable_p178.png` | binary/media artifact |
| urgent | 155.8 KiB | `Experiments/selective_resynchronization_mvp/outputs/figures/abc_learning_curves.png` | binary/media artifact |
| urgent | 152.8 KiB | `Experiments/selective_resynchronization_mvp/outputs/figures/metric_correlation_matrix.png` | binary/media artifact |
| urgent | 140.2 KiB | `Experiments/choicemap_explicit_scaffolding/outputs/confirmatory/raw/commitment_logs.parquet` | binary/media artifact |
| action | 86.1 KiB | `Experiments/selective_resynchronization_mvp/outputs/figures/sr_prec_vs_qc.png` | binary/media artifact |
| action | 79.9 KiB | `Experiments/selective_resynchronization_mvp/outputs/figures/partial_sr_prec_qc.png` | binary/media artifact |
| action | 74.8 KiB | `Experiments/choicemap_explicit_scaffolding/outputs/confirmatory/figures/heldout_future_task_performance.png` | binary/media artifact |
| action | 72.5 KiB | `Experiments/selective_resynchronization_mvp/outputs/figures/model_comparison.png` | binary/media artifact |
| action | 69.4 KiB | `Experiments/selective_resynchronization_mvp/outputs/figures/fisher_vs_simple_baselines.png` | binary/media artifact |
| warning | 65.7 KiB | `Experiments/selective_resynchronization_matched_paths/outputs/diagnostic/v1_diagnostic_frame.parquet` | binary/media artifact |
| warning | 63.6 KiB | `Experiments/choicemap_explicit_scaffolding/outputs/confirmatory/figures/compute_performance.png` | binary/media artifact |
| warning | 62.1 KiB | `Experiments/choicemap_explicit_scaffolding/outputs/confirmatory/figures/effect_by_seed.png` | binary/media artifact |
| warning | 59.5 KiB | `scripts/build_srt_context_bundles.py` | binary/media artifact |
| warning | 57.0 KiB | `Experiments/stake_future_selectability_mvp/outputs/formal/processed/locked_analysis_frame.parquet` | binary/media artifact |
| warning | 57.0 KiB | `tmp/pdfs/srt_spine_copyable_fixed_p178.png` | binary/media artifact |
| warning | 56.9 KiB | `Experiments/choicemap_explicit_scaffolding/outputs/confirmatory/figures/current_success.png` | binary/media artifact |
| warning | 56.6 KiB | `Experiments/choicemap_explicit_scaffolding/outputs/confirmatory/figures/rfs_auc.png` | binary/media artifact |
| warning | 56.0 KiB | `Experiments/choicemap_explicit_scaffolding/outputs/confirmatory/figures/irreversible_failure.png` | binary/media artifact |
| warning | 55.7 KiB | `Experiments/choicemap_explicit_scaffolding/outputs/confirmatory/figures/future_by_environment.png` | binary/media artifact |
| warning | 50.0 KiB | `Experiments/choicemap_explicit_scaffolding/outputs/confirmatory/figures/probe_count.png` | binary/media artifact |

## Recommended Queue

- Action-threshold active markdown without split route: `10`

1. Use the split route shown in the table before reading any action-threshold owner file through a connector.
2. Treat `Operations/_SRT_MATERIAL_LOG.md` and `Operations/_SRT_STATUS_HISTORY.md` as split master indexes; read dated parts through `Operations/Material_Log/README.md` and `Operations/Status_History/README.md`.
3. Treat artifact/generated files as non-primary connector read paths; prefer source Markdown, split indexes, or generated summaries.

### Active Markdown Over Action Threshold

| Size | File | Split status |
|---:|---|---|
| 895.3 KiB | `Output/pdf/从存在到秩序_完整稿_2026-07-04.md` | missing_or_not_needed |
| 829.9 KiB | `Output/从存在到秩序_完整版_2026-06-23.md` | missing_or_not_needed |
| 453.7 KiB | `Output/pdf/从存在到秩序_哲学读者试读版_2026-07-04.md` | missing_or_not_needed |
| 326.1 KiB | `Output/从存在到秩序_哲学读者试读版_2026-06-23.md` | missing_or_not_needed |
| 218.2 KiB | `01_Source_Intuition/BOOK/BOOK_CHAPTER_CARDS_2026-05-22.md` | missing_or_not_needed |
| 202.5 KiB | `Governance/Frontmatter_Warning_Baseline.txt` | missing_or_not_needed |
| 131.9 KiB | `01_Source_Intuition/BOOK/External_Theory_Notes/BARAD_SRT_ALIGNMENT_AND_INSERTION_MAP_2026-06-10.md` | missing_or_not_needed |
| 125.9 KiB | `01_Source_Intuition/BOOK/BOOK_PROBLEM_CHAIN_REWRITE_2026-05-21.md` | missing_or_not_needed |
| 112.7 KiB | `Neuroscience/SRT_Neural_Mechanisms.md` | Neuroscience/Neural_Mechanisms_Split |
| 110.3 KiB | `Philosophy/SRT_Philosophy_Ethics.md` | Philosophy/Ethics_Split |
| 97.2 KiB | `Core/SRT_Core_14_Dynamics_Scaling.md` | Core/Dynamics_Scaling_Split |
| 96.0 KiB | `01_Source_Intuition/BOOK/BOOK_VERSION_LOG.md` | missing_or_not_needed |
| 90.9 KiB | `Physics/SRT_Physics_Cosmology.md` | Physics/Cosmology_Split |
| 88.7 KiB | `SRT_Glossary.md` | Glossary/README.md |
| 82.5 KiB | `Philosophy/SRT_Philosophy_Foundations.md` | Philosophy/Foundations_Split |
| 82.3 KiB | `AI/SRT_AI_01_Ontology.md` | AI/Ontology_Split |
| 80.9 KiB | `Governance/_SRT_CHANGELOG_2026.md` | Governance/_SRT_CHANGELOG_2026_Split |
| 79.5 KiB | `Core/SRT_Core_13a_Operator_Basics.md` | Core/Operator_Basics_Split |
| 76.0 KiB | `Core/SRT_Core_12b_Ontology_L2.md` | Core/Ontology_L2_Split |
| 75.6 KiB | `Core/SRT_Core_01_Axioms.md` | Core/Axioms_Split |
| 74.9 KiB | `AI/SRT_AI_03_Consciousness_Framework.md` | AI/Consciousness_Framework_Split |
| 74.0 KiB | `SRT/未命名 1.md` | SRT/未命名 1_Split |
| 72.8 KiB | `Philosophy/Papers/Before_Objects_Selection_Realism.md` | missing_or_not_needed |
| 70.2 KiB | `Philosophy/SRT_Social_Economics.md` | Philosophy/Social_Economics_Split |
