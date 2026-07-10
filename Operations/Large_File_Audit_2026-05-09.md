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
| urgent | 829.9 KiB | `Output/从存在到秩序_完整版_2026-06-23.md` | missing_or_not_needed |
| urgent | 326.1 KiB | `Output/从存在到秩序_哲学读者试读版_2026-06-23.md` | missing_or_not_needed |
| urgent | 218.2 KiB | `01_Source_Intuition/BOOK/BOOK_CHAPTER_CARDS_2026-05-22.md` | missing_or_not_needed |
| urgent | 131.9 KiB | `01_Source_Intuition/BOOK/External_Theory_Notes/BARAD_SRT_ALIGNMENT_AND_INSERTION_MAP_2026-06-10.md` | missing_or_not_needed |
| urgent | 125.9 KiB | `01_Source_Intuition/BOOK/BOOK_PROBLEM_CHAIN_REWRITE_2026-05-21.md` | missing_or_not_needed |
| urgent | 111.0 KiB | `Neuroscience/SRT_Neural_Mechanisms.md` | Neuroscience/Neural_Mechanisms_Split |
| urgent | 110.3 KiB | `Philosophy/SRT_Philosophy_Ethics.md` | Philosophy/Ethics_Split |
| action | 97.2 KiB | `Core/SRT_Core_14_Dynamics_Scaling.md` | Core/Dynamics_Scaling_Split |
| action | 92.2 KiB | `01_Source_Intuition/BOOK/BOOK_VERSION_LOG.md` | missing_or_not_needed |
| action | 90.9 KiB | `Physics/SRT_Physics_Cosmology.md` | Physics/Cosmology_Split |
| action | 88.7 KiB | `SRT_Glossary.md` | Glossary/README.md |
| action | 82.5 KiB | `Philosophy/SRT_Philosophy_Foundations.md` | Philosophy/Foundations_Split |
| action | 82.2 KiB | `AI/SRT_AI_01_Ontology.md` | AI/Ontology_Split |
| action | 80.1 KiB | `Governance/_SRT_CHANGELOG_2026.md` | Governance/_SRT_CHANGELOG_2026_Split |
| action | 79.5 KiB | `Core/SRT_Core_13a_Operator_Basics.md` | Core/Operator_Basics_Split |
| action | 76.0 KiB | `Core/SRT_Core_12b_Ontology_L2.md` | Core/Ontology_L2_Split |
| action | 74.8 KiB | `AI/SRT_AI_03_Consciousness_Framework.md` | AI/Consciousness_Framework_Split |
| action | 74.2 KiB | `Core/SRT_Core_01_Axioms.md` | Core/Axioms_Split |
| action | 74.0 KiB | `SRT/未命名 1.md` | SRT/未命名 1_Split |
| action | 72.8 KiB | `Philosophy/Papers/Before_Objects_Selection_Realism.md` | missing_or_not_needed |
| action | 70.2 KiB | `Philosophy/SRT_Social_Economics.md` | Philosophy/Social_Economics_Split |
| warning | 66.1 KiB | `Core_Law/SRT_Collective_Tower_Hardening_Notes.md` | Core_Law/Collective_Tower_Hardening_Notes_Split |
| warning | 65.2 KiB | `Core/SRT_Core_22_Equations.md` | Core/Equations_Split |
| warning | 64.5 KiB | `Physics/SRT_Phys_09_Formalism_Ext.md` | Physics/Formalism_Ext_Split |
| warning | 62.8 KiB | `Philosophy/SRT_Ethics_Agency.md` | Philosophy/Ethics_Agency_Split |
| warning | 62.4 KiB | `Philosophy/Papers/Biomarkers_Before_Treatments_NT1_Decoupled_TCI.md` | missing_or_not_needed |
| warning | 59.5 KiB | `Neuroscience/SRT_Neuro_08_Immune_Dist.md` | Neuroscience/Immune_Dist_Split |
| warning | 57.5 KiB | `Core_Law/SRT_L1_Formalism.md` | Core_Law/L1_Formalism_Split |
| warning | 57.0 KiB | `Philosophy/Papers/Before_Objects_Selection_Realism_Submission_EN.md` | missing_or_not_needed |
| warning | 56.9 KiB | `Philosophy/SRT_Social_Cognition.md` | Philosophy/Social_Cognition_Split |
| warning | 56.4 KiB | `Philosophy/SRT_SocTheory_06_L2_Dynamics.md` | Philosophy/L2_Dynamics_Split |
| warning | 54.3 KiB | `Physics/SRT_Quant_01_Selection.md` | Physics/Selection_Split |
| warning | 53.7 KiB | `Core/SRT_Core_12a_Ontology_L0L1.md` | Core/Ontology_L0L1_Split |
| warning | 52.6 KiB | `Core_Law/SRT_Reference_Dynamics.md` | Core_Law/Reference_Dynamics_Split |
| warning | 50.8 KiB | `AI/Ontology_Annex/00_General_Boundary_Block.md` | AI/Ontology_Annex/General_Boundary_Block_Split |
| warning | 50.7 KiB | `Physics/SRT_Quant_02_Cosmology.md` | Physics/Quant_02_Cosmology_Split |
| warning | 50.6 KiB | `AI/SRT_AI_Architecture.md` | AI/Architecture_Split |
| warning | 50.0 KiB | `01_Source_Intuition/SRT_CHOICEMAP_RANDOM_RESYNCHRONIZATION_TRACE_2026-07-09.md` | missing_or_not_needed |
| warning | 49.9 KiB | `Philosophy/SRT_SocTheory_05_Language_Eco.md` | Philosophy/Language_Eco_Split |

## artifact_or_generated

| Risk | Size | File | Split / handling |
|---|---:|---|---|
| urgent | 277.3 KiB | `Operations/_SRT_DEEP_NAV_COVERAGE_AUDIT_REPORT.json` | artifact/generated; do not use as primary connector read path |
| urgent | 267.5 KiB | `Archive/root_misc/Pasted image 20260306100654.png` | artifact/generated; do not use as primary connector read path |
| urgent | 137.3 KiB | `papers/ontological_friction/paper_ontological_friction_frontiers_submission.html` | artifact/generated; do not use as primary connector read path |
| urgent | 116.5 KiB | `video/package-lock.json` | artifact/generated; do not use as primary connector read path |
| urgent | 114.0 KiB | `papers/ontological_friction/paper_ontological_friction.html` | artifact/generated; do not use as primary connector read path |
| urgent | 111.3 KiB | `papers/ontological_friction/paper_ontological_friction_frontiers_submission.md` | artifact/generated; do not use as primary connector read path |
| urgent | 108.0 KiB | `Archive/raw_sessions/SRT_SESSION_RAW_TRANSCRIPT_2026-03-31.md` | artifact/generated; do not use as primary connector read path |
| urgent | 107.2 KiB | `Operations/_SRT_DEEP_NAV_PATH_AUDIT_REPORT.json` | artifact/generated; do not use as primary connector read path |
| urgent | 102.7 KiB | `Archive/root_misc/Selection-Reality Theory (SRT).pdf` | artifact/generated; do not use as primary connector read path |
| action | 91.1 KiB | `papers/ontological_friction/paper_ontological_friction_zh.html` | artifact/generated; do not use as primary connector read path |
| action | 87.9 KiB | `papers/ontological_friction/paper_ontological_friction.md` | artifact/generated; do not use as primary connector read path |
| warning | 67.6 KiB | `papers/ontological_friction/paper_ontological_friction_zh.md` | artifact/generated; do not use as primary connector read path |
| warning | 64.0 KiB | `papers/SRT_MetaOS_JCS_v2.md` | artifact/generated; do not use as primary connector read path |
| warning | 61.5 KiB | `papers/markov_blanket/paper_markov_blanket_d_value.md` | artifact/generated; do not use as primary connector read path |
| warning | 59.1 KiB | `papers/SRT_MetaOS_JCS_v1.md` | artifact/generated; do not use as primary connector read path |
| warning | 54.8 KiB | `papers/alife2026_pilot_results/v2_costly_selection/results_nopenalty.json` | artifact/generated; do not use as primary connector read path |
| warning | 51.5 KiB | `papers/alife2026_pilot_results/v2_costly_selection/results_full.json` | artifact/generated; do not use as primary connector read path |
| warning | 49.4 KiB | `papers/CostlySelectiveClosure_v16.md` | artifact/generated; do not use as primary connector read path |

## Recommended Queue

- Action-threshold active markdown without split route: `7`

1. Use the split route shown in the table before reading any action-threshold owner file through a connector.
2. Treat `Operations/_SRT_MATERIAL_LOG.md` and `Operations/_SRT_STATUS_HISTORY.md` as split master indexes; read dated parts through `Operations/Material_Log/README.md` and `Operations/Status_History/README.md`.
3. Treat artifact/generated files as non-primary connector read paths; prefer source Markdown, split indexes, or generated summaries.

### Active Markdown Over Action Threshold

| Size | File | Split status |
|---:|---|---|
| 829.9 KiB | `Output/从存在到秩序_完整版_2026-06-23.md` | missing_or_not_needed |
| 326.1 KiB | `Output/从存在到秩序_哲学读者试读版_2026-06-23.md` | missing_or_not_needed |
| 218.2 KiB | `01_Source_Intuition/BOOK/BOOK_CHAPTER_CARDS_2026-05-22.md` | missing_or_not_needed |
| 131.9 KiB | `01_Source_Intuition/BOOK/External_Theory_Notes/BARAD_SRT_ALIGNMENT_AND_INSERTION_MAP_2026-06-10.md` | missing_or_not_needed |
| 125.9 KiB | `01_Source_Intuition/BOOK/BOOK_PROBLEM_CHAIN_REWRITE_2026-05-21.md` | missing_or_not_needed |
| 111.0 KiB | `Neuroscience/SRT_Neural_Mechanisms.md` | Neuroscience/Neural_Mechanisms_Split |
| 110.3 KiB | `Philosophy/SRT_Philosophy_Ethics.md` | Philosophy/Ethics_Split |
| 97.2 KiB | `Core/SRT_Core_14_Dynamics_Scaling.md` | Core/Dynamics_Scaling_Split |
| 92.2 KiB | `01_Source_Intuition/BOOK/BOOK_VERSION_LOG.md` | missing_or_not_needed |
| 90.9 KiB | `Physics/SRT_Physics_Cosmology.md` | Physics/Cosmology_Split |
| 88.7 KiB | `SRT_Glossary.md` | Glossary/README.md |
| 82.5 KiB | `Philosophy/SRT_Philosophy_Foundations.md` | Philosophy/Foundations_Split |
| 82.2 KiB | `AI/SRT_AI_01_Ontology.md` | AI/Ontology_Split |
| 80.1 KiB | `Governance/_SRT_CHANGELOG_2026.md` | Governance/_SRT_CHANGELOG_2026_Split |
| 79.5 KiB | `Core/SRT_Core_13a_Operator_Basics.md` | Core/Operator_Basics_Split |
| 76.0 KiB | `Core/SRT_Core_12b_Ontology_L2.md` | Core/Ontology_L2_Split |
| 74.8 KiB | `AI/SRT_AI_03_Consciousness_Framework.md` | AI/Consciousness_Framework_Split |
| 74.2 KiB | `Core/SRT_Core_01_Axioms.md` | Core/Axioms_Split |
| 74.0 KiB | `SRT/未命名 1.md` | SRT/未命名 1_Split |
| 72.8 KiB | `Philosophy/Papers/Before_Objects_Selection_Realism.md` | missing_or_not_needed |
| 70.2 KiB | `Philosophy/SRT_Social_Economics.md` | Philosophy/Social_Economics_Split |
