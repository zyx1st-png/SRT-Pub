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
| urgent | 110.6 KiB | `Neuroscience/SRT_Neural_Mechanisms.md` | Neuroscience/Neural_Mechanisms_Split |
| urgent | 109.5 KiB | `Philosophy/SRT_Philosophy_Ethics.md` | Philosophy/Ethics_Split |
| action | 97.2 KiB | `Core/SRT_Core_14_Dynamics_Scaling.md` | Core/Dynamics_Scaling_Split |
| action | 90.6 KiB | `Physics/SRT_Physics_Cosmology.md` | Physics/Cosmology_Split |
| action | 83.4 KiB | `SRT_Glossary.md` | Glossary/README.md |
| action | 82.1 KiB | `Philosophy/SRT_Philosophy_Foundations.md` | Philosophy/Foundations_Split |
| action | 81.6 KiB | `AI/SRT_AI_01_Ontology.md` | AI/Ontology_Split |
| action | 80.0 KiB | `Governance/_SRT_CHANGELOG_2026.md` | Governance/_SRT_CHANGELOG_2026_Split |
| action | 79.5 KiB | `Core/SRT_Core_13a_Operator_Basics.md` | Core/Operator_Basics_Split |
| action | 76.0 KiB | `Core/SRT_Core_12b_Ontology_L2.md` | Core/Ontology_L2_Split |
| action | 74.3 KiB | `AI/SRT_AI_03_Consciousness_Framework.md` | AI/Consciousness_Framework_Split |
| action | 74.2 KiB | `Core/SRT_Core_01_Axioms.md` | Core/Axioms_Split |
| action | 74.0 KiB | `SRT/未命名 1.md` | SRT/未命名 1_Split |
| action | 69.9 KiB | `Philosophy/SRT_Social_Economics.md` | Philosophy/Social_Economics_Split |
| warning | 66.1 KiB | `Core_Law/SRT_Collective_Tower_Hardening_Notes.md` | Core_Law/Collective_Tower_Hardening_Notes_Split |
| warning | 64.8 KiB | `Core/SRT_Core_22_Equations.md` | Core/Equations_Split |
| warning | 60.8 KiB | `Physics/SRT_Phys_09_Formalism_Ext.md` | Physics/Formalism_Ext_Split |
| warning | 59.4 KiB | `Philosophy/SRT_Ethics_Agency.md` | Philosophy/Ethics_Agency_Split |
| warning | 59.1 KiB | `Neuroscience/SRT_Neuro_08_Immune_Dist.md` | Neuroscience/Immune_Dist_Split |
| warning | 57.5 KiB | `Core_Law/SRT_L1_Formalism.md` | Core_Law/L1_Formalism_Split |
| warning | 56.4 KiB | `Philosophy/SRT_Social_Cognition.md` | Philosophy/Social_Cognition_Split |
| warning | 56.0 KiB | `Philosophy/SRT_SocTheory_06_L2_Dynamics.md` | Philosophy/L2_Dynamics_Split |
| warning | 54.0 KiB | `Physics/SRT_Quant_01_Selection.md` | Physics/Selection_Split |
| warning | 53.7 KiB | `Core/SRT_Core_12a_Ontology_L0L1.md` | Core/Ontology_L0L1_Split |
| warning | 51.1 KiB | `Core_Law/SRT_Reference_Dynamics.md` | Core_Law/Reference_Dynamics_Split |
| warning | 50.5 KiB | `AI/Ontology_Annex/00_General_Boundary_Block.md` | AI/Ontology_Annex/General_Boundary_Block_Split |
| warning | 50.4 KiB | `Physics/SRT_Quant_02_Cosmology.md` | Physics/Quant_02_Cosmology_Split |
| warning | 50.3 KiB | `AI/SRT_AI_Architecture.md` | AI/Architecture_Split |
| warning | 49.4 KiB | `Philosophy/SRT_SocTheory_05_Language_Eco.md` | Philosophy/Language_Eco_Split |

## artifact_or_generated

| Risk | Size | File | Split / handling |
|---|---:|---|---|
| urgent | 20554.6 KiB | `papers/ontological_friction/figures/frontiers_upload/Figure5.tif` | artifact/generated; do not use as primary connector read path |
| urgent | 19940.1 KiB | `papers/ontological_friction/figures/frontiers_upload/Figure1.tif` | artifact/generated; do not use as primary connector read path |
| urgent | 15845.8 KiB | `papers/ontological_friction/figures/frontiers_upload/Figure4.tif` | artifact/generated; do not use as primary connector read path |
| urgent | 15488.7 KiB | `papers/ontological_friction/figures/frontiers_upload/Figure2.tif` | artifact/generated; do not use as primary connector read path |
| urgent | 9941.2 KiB | `papers/ontological_friction/figures/frontiers_upload/Figure3.tif` | artifact/generated; do not use as primary connector read path |
| urgent | 8574.4 KiB | `papers/ontological_friction/figures/frontiers_upload/Figure5_v2.tif` | artifact/generated; do not use as primary connector read path |
| urgent | 7627.6 KiB | `papers/ontological_friction/figures/frontiers_upload/Figure1_v2.tif` | artifact/generated; do not use as primary connector read path |
| urgent | 3849.4 KiB | `papers/ontological_friction/paper_ontological_friction_zh.pdf` | artifact/generated; do not use as primary connector read path |
| urgent | 3403.9 KiB | `papers/ontological_friction/paper_ontological_friction.pdf` | artifact/generated; do not use as primary connector read path |
| urgent | 2900.7 KiB | `papers/ontological_friction/paper_ontological_friction_old.pdf` | artifact/generated; do not use as primary connector read path |
| urgent | 2303.9 KiB | `papers/ontological_friction/paper_ontological_friction.docx` | artifact/generated; do not use as primary connector read path |
| urgent | 2300.9 KiB | `papers/ontological_friction/paper_ontological_friction_zh.docx` | artifact/generated; do not use as primary connector read path |
| urgent | 1942.0 KiB | `papers/ontological_friction/figures/frontiers_upload/frontiers_figures_tif.zip` | artifact/generated; do not use as primary connector read path |
| urgent | 1582.9 KiB | `papers/ontological_friction/figures/frontiers_upload/frontiers_figures_jpg.zip` | artifact/generated; do not use as primary connector read path |
| urgent | 1081.4 KiB | `video/out/outro_en.mp4` | artifact/generated; do not use as primary connector read path |
| urgent | 1053.4 KiB | `video/out/outro.mp4` | artifact/generated; do not use as primary connector read path |
| urgent | 868.6 KiB | `video/out/intro.mp4` | artifact/generated; do not use as primary connector read path |
| urgent | 820.7 KiB | `video/out/intro_cn.mp4` | artifact/generated; do not use as primary connector read path |
| urgent | 740.4 KiB | `papers/ontological_friction/figures/fig3_clinical_radar.png` | artifact/generated; do not use as primary connector read path |
| urgent | 556.6 KiB | `papers/ontological_friction/figures/fig5_ros_dag.png` | artifact/generated; do not use as primary connector read path |
| urgent | 554.6 KiB | `papers/ontological_friction/figures/fig4_experimental_design.png` | artifact/generated; do not use as primary connector read path |
| urgent | 549.4 KiB | `papers/ontological_friction/paper_ontological_friction_frontiers_submission.pdf` | artifact/generated; do not use as primary connector read path |
| urgent | 543.4 KiB | `papers/ALIFE2026_submission_anonymous_v14.pdf` | artifact/generated; do not use as primary connector read path |
| urgent | 542.9 KiB | `papers/ALIFE2026_submission_anonymous_v15.pdf` | artifact/generated; do not use as primary connector read path |
| urgent | 526.5 KiB | `papers/ALIFE2026_submission_anonymous_v4.pdf` | artifact/generated; do not use as primary connector read path |
| urgent | 522.2 KiB | `papers/ALIFE2026_submission_anonymous_v3.pdf` | artifact/generated; do not use as primary connector read path |
| urgent | 478.4 KiB | `papers/ALIFE2026_submission_anonymous.pdf` | artifact/generated; do not use as primary connector read path |
| urgent | 477.7 KiB | `papers/ontological_friction/figures/frontiers_upload/Figure5.jpg` | artifact/generated; do not use as primary connector read path |
| urgent | 452.5 KiB | `papers/ontological_friction/figures/frontiers_upload/Figure4.jpg` | artifact/generated; do not use as primary connector read path |
| urgent | 450.4 KiB | `papers/ALIFE2026_submission_anonymous_v2.pdf` | artifact/generated; do not use as primary connector read path |
| urgent | 428.0 KiB | `graphify-out/graph.json` | artifact/generated; do not use as primary connector read path |
| urgent | 378.1 KiB | `graphify-out/root_snapshots/.graphify_extract.json` | artifact/generated; do not use as primary connector read path |
| urgent | 378.1 KiB | `graphify-out/root_snapshots/.graphify_semantic.json` | artifact/generated; do not use as primary connector read path |
| urgent | 377.2 KiB | `graphify-out/root_snapshots/.graphify_semantic_new.json` | artifact/generated; do not use as primary connector read path |
| urgent | 377.1 KiB | `papers/ontological_friction/figures/frontiers_upload/Figure1.jpg` | artifact/generated; do not use as primary connector read path |
| urgent | 363.7 KiB | `graphify-out/graph.html` | artifact/generated; do not use as primary connector read path |
| urgent | 357.9 KiB | `papers/ontological_friction/figures/fig1_srt_architecture.png` | artifact/generated; do not use as primary connector read path |
| urgent | 356.0 KiB | `papers/ontological_friction/figures/frontiers_upload/Figure3.jpg` | artifact/generated; do not use as primary connector read path |
| urgent | 338.9 KiB | `papers/ontological_friction/figures/frontiers_upload/Figure2.jpg` | artifact/generated; do not use as primary connector read path |
| urgent | 291.1 KiB | `papers/ontological_friction/figures/fig2_proxy_map.png` | artifact/generated; do not use as primary connector read path |
| urgent | 277.3 KiB | `Operations/_SRT_DEEP_NAV_COVERAGE_AUDIT_REPORT.json` | artifact/generated; do not use as primary connector read path |
| urgent | 267.5 KiB | `Archive/root_misc/Pasted image 20260306100654.png` | artifact/generated; do not use as primary connector read path |
| urgent | 227.5 KiB | `papers/ontological_friction/figures/frontiers_upload/Figure5_v2.jpg` | artifact/generated; do not use as primary connector read path |
| urgent | 185.0 KiB | `papers/ontological_friction/figures/frontiers_upload/Figure1_v2.jpg` | artifact/generated; do not use as primary connector read path |
| urgent | 118.8 KiB | `papers/ontological_friction/paper_ontological_friction_frontiers_submission.html` | artifact/generated; do not use as primary connector read path |
| urgent | 116.5 KiB | `video/package-lock.json` | artifact/generated; do not use as primary connector read path |
| urgent | 114.0 KiB | `papers/ontological_friction/paper_ontological_friction.html` | artifact/generated; do not use as primary connector read path |
| urgent | 110.9 KiB | `graphify-out/.graphify_chunk_03.json` | artifact/generated; do not use as primary connector read path |
| urgent | 108.0 KiB | `Archive/raw_sessions/SRT_SESSION_RAW_TRANSCRIPT_2026-03-31.md` | artifact/generated; do not use as primary connector read path |
| urgent | 107.2 KiB | `Operations/_SRT_DEEP_NAV_PATH_AUDIT_REPORT.json` | artifact/generated; do not use as primary connector read path |
| urgent | 102.7 KiB | `Archive/root_misc/Selection-Reality Theory (SRT).pdf` | artifact/generated; do not use as primary connector read path |
| action | 95.0 KiB | `papers/ontological_friction/paper_ontological_friction_frontiers_submission.md` | artifact/generated; do not use as primary connector read path |
| action | 91.1 KiB | `papers/ontological_friction/paper_ontological_friction_zh.html` | artifact/generated; do not use as primary connector read path |
| action | 87.9 KiB | `papers/ontological_friction/paper_ontological_friction.md` | artifact/generated; do not use as primary connector read path |
| action | 86.6 KiB | `graphify-out/converted/paper_ontological_friction_frontiers_submission_3a4f7f4b.md` | artifact/generated; do not use as primary connector read path |
| action | 78.7 KiB | `graphify-out/converted/paper_ontological_friction_frontiers_submission.pre_sync_backup_2026-03-24_02815416.md` | artifact/generated; do not use as primary connector read path |
| action | 78.2 KiB | `graphify-out/converted/paper_ontological_friction_ecf0aa83.md` | artifact/generated; do not use as primary connector read path |
| warning | 67.6 KiB | `papers/ontological_friction/paper_ontological_friction_zh.md` | artifact/generated; do not use as primary connector read path |
| warning | 64.1 KiB | `graphify-out/.graphify_chunk_05.json` | artifact/generated; do not use as primary connector read path |
| warning | 64.0 KiB | `papers/SRT_MetaOS_JCS_v2.md` | artifact/generated; do not use as primary connector read path |
| warning | 61.5 KiB | `papers/markov_blanket/paper_markov_blanket_d_value.md` | artifact/generated; do not use as primary connector read path |
| warning | 59.1 KiB | `papers/SRT_MetaOS_JCS_v1.md` | artifact/generated; do not use as primary connector read path |
| warning | 58.9 KiB | `graphify-out/converted/paper_ontological_friction_zh_85046716.md` | artifact/generated; do not use as primary connector read path |
| warning | 57.6 KiB | `papers/ontological_friction/paper_ontological_friction_frontiers_submission.docx` | artifact/generated; do not use as primary connector read path |
| warning | 55.1 KiB | `papers/ontological_friction/paper_ontological_friction_frontiers_submission.pre_sync_backup_2026-03-24.docx` | artifact/generated; do not use as primary connector read path |

## Recommended Queue

- Action-threshold active markdown without split route: `0`

1. Use the split route shown in the table before reading any action-threshold owner file through a connector.
2. Treat `Operations/_SRT_MATERIAL_LOG.md` and `Operations/_SRT_STATUS_HISTORY.md` as split master indexes; read dated parts through `Operations/Material_Log/README.md` and `Operations/Status_History/README.md`.
3. Treat artifact/generated files as non-primary connector read paths; prefer source Markdown, split indexes, or generated summaries.

### Active Markdown Over Action Threshold

| Size | File | Split status |
|---:|---|---|
| 110.6 KiB | `Neuroscience/SRT_Neural_Mechanisms.md` | Neuroscience/Neural_Mechanisms_Split |
| 109.5 KiB | `Philosophy/SRT_Philosophy_Ethics.md` | Philosophy/Ethics_Split |
| 97.2 KiB | `Core/SRT_Core_14_Dynamics_Scaling.md` | Core/Dynamics_Scaling_Split |
| 90.6 KiB | `Physics/SRT_Physics_Cosmology.md` | Physics/Cosmology_Split |
| 83.4 KiB | `SRT_Glossary.md` | Glossary/README.md |
| 82.1 KiB | `Philosophy/SRT_Philosophy_Foundations.md` | Philosophy/Foundations_Split |
| 81.6 KiB | `AI/SRT_AI_01_Ontology.md` | AI/Ontology_Split |
| 80.0 KiB | `Governance/_SRT_CHANGELOG_2026.md` | Governance/_SRT_CHANGELOG_2026_Split |
| 79.5 KiB | `Core/SRT_Core_13a_Operator_Basics.md` | Core/Operator_Basics_Split |
| 76.0 KiB | `Core/SRT_Core_12b_Ontology_L2.md` | Core/Ontology_L2_Split |
| 74.3 KiB | `AI/SRT_AI_03_Consciousness_Framework.md` | AI/Consciousness_Framework_Split |
| 74.2 KiB | `Core/SRT_Core_01_Axioms.md` | Core/Axioms_Split |
| 74.0 KiB | `SRT/未命名 1.md` | SRT/未命名 1_Split |
| 69.9 KiB | `Philosophy/SRT_Social_Economics.md` | Philosophy/Social_Economics_Split |
