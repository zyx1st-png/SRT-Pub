# Translation Status

This file tracks bilingual rollout for SRT documents.

## Policy
- Source of truth: Chinese files in the existing root directories (`Core/`, `Physics/`, etc.).
- English mirror: `en/` with 1:1 path mapping.
- Sync rule: update Chinese first, then sync English.

## Workflow
1. Add/modify Chinese source.
2. Update `source_commit` in corresponding English file header.
3. Update status row in this file.

## Status Legend
- `pending`: not translated yet
- `in_progress`: partial translation available
- `done`: fully translated and synced

## Module Priority

| Module | Source Directory | Target Directory | File Count | Priority | Status |
|:--|:--|:--|--:|:--|:--|
| Core_Law | `Core_Law/` | `en/Core_Law/` | 4 | P0 | done |
| Core | `Core/` | `en/Core/` | 12 | P0 | in_progress |
| Physics | `Physics/` | `en/Physics/` | 9 | P1 | in_progress |
| Neuroscience | `Neuroscience/` | `en/Neuroscience/` | 13 | P1 | in_progress |
| AI | `AI/` | `en/AI/` | 6 | P1 | pending |
| Philosophy | `Philosophy/` | `en/Philosophy/` | 14 | P2 | pending |
| Spirituality | `Spirituality/` | `en/Spirituality/` | 10 | P2 | pending |

## Completed This Round

| Source | English Target | Status |
|:--|:--|:--|
| `Core_Law/SRT_Reference_Axioms.md` | `en/Core_Law/SRT_Reference_Axioms.md` | done |
| `Core_Law/SRT_Reference_Ontology.md` | `en/Core_Law/SRT_Reference_Ontology.md` | done |
| `Core_Law/SRT_Reference_Dynamics.md` | `en/Core_Law/SRT_Reference_Dynamics.md` | done |
| `Core_Law/SRT_Reference_Scaling.md` | `en/Core_Law/SRT_Reference_Scaling.md` | done |
| `Core/SRT_Core_00_Intro.md` | `en/Core/SRT_Core_00_Intro.md` | in_progress |
| `Core/SRT_Core_01_Axioms.md` | `en/Core/SRT_Core_01_Axioms.md` | in_progress |
| `Core/SRT_Core_12a_Ontology_L0L1.md` | `en/Core/SRT_Core_12a_Ontology_L0L1.md` | in_progress |
| `Core/SRT_Core_12b_Ontology_L2.md` | `en/Core/SRT_Core_12b_Ontology_L2.md` | in_progress |
| `Core/SRT_Core_13a_Operator_Basics.md` | `en/Core/SRT_Core_13a_Operator_Basics.md` | in_progress |
| `Core/SRT_Core_13b_Operator_Advanced.md` | `en/Core/SRT_Core_13b_Operator_Advanced.md` | in_progress |
| `Core/SRT_Core_14_Dynamics_Scaling.md` | `en/Core/SRT_Core_14_Dynamics_Scaling.md` | in_progress |
| `Core/_SRT_Core_Bridge.md` | `en/Core/_SRT_Core_Bridge.md` | in_progress |
| `Core/SRT_Core_21_Formal_Axioms.md` | `en/Core/SRT_Core_21_Formal_Axioms.md` | done |
| `Core/SRT_Core_22_Equations.md` | `en/Core/SRT_Core_22_Equations.md` | done |
| `Core/SRT_Experimental_Core.md` | `en/Core/SRT_Experimental_Core.md` | in_progress |
| `Core/SRT_Experimental_Applications.md` | `en/Core/SRT_Experimental_Applications.md` | in_progress |
| `Physics/_SRT_Phys_Bridge.md` | `en/Physics/_SRT_Phys_Bridge.md` | in_progress |
| `Physics/SRT_Quant_00_Intro.md` | `en/Physics/SRT_Quant_00_Intro.md` | in_progress |
| `Physics/SRT_Quant_01_Selection.md` | `en/Physics/SRT_Quant_01_Selection.md` | in_progress |
| `Physics/SRT_Quant_02_Cosmology.md` | `en/Physics/SRT_Quant_02_Cosmology.md` | in_progress |
| `Physics/SRT_Phys_07_Complex_Systems.md` | `en/Physics/SRT_Phys_07_Complex_Systems.md` | in_progress |
| `Physics/SRT_Phys_08_Ontology_Ext.md` | `en/Physics/SRT_Phys_08_Ontology_Ext.md` | in_progress |
| `Physics/SRT_Phys_09_Formalism_Ext.md` | `en/Physics/SRT_Phys_09_Formalism_Ext.md` | in_progress |
| `Physics/SRT_Phys_10_Integration.md` | `en/Physics/SRT_Phys_10_Integration.md` | in_progress |
| `Physics/SRT_Physics_Cosmology.md` | `en/Physics/SRT_Physics_Cosmology.md` | in_progress |
| `Neuroscience/_SRT_Neuro_Axioms.md` | `en/Neuroscience/_SRT_Neuro_Axioms.md` | in_progress |
| `Neuroscience/SRT_Neural_Mechanisms.md` | `en/Neuroscience/SRT_Neural_Mechanisms.md` | in_progress |
| `Neuroscience/SRT_Consciousness_Mechanisms.md` | `en/Neuroscience/SRT_Consciousness_Mechanisms.md` | in_progress |
| `Neuroscience/SRT_Neuro_Experiments.md` | `en/Neuroscience/SRT_Neuro_Experiments.md` | in_progress |
| `Neuroscience/SRT_Clin_00_IIT_PCI.md` | `en/Neuroscience/SRT_Clin_00_IIT_PCI.md` | in_progress |
| `Neuroscience/SRT_Clin_01_Pathology.md` | `en/Neuroscience/SRT_Clin_01_Pathology.md` | in_progress |
| `Neuroscience/SRT_Clin_02_FEP.md` | `en/Neuroscience/SRT_Clin_02_FEP.md` | in_progress |
| `Neuroscience/SRT_Clin_03_DMN_Networks.md` | `en/Neuroscience/SRT_Clin_03_DMN_Networks.md` | in_progress |
| `Neuroscience/SRT_Neuro_06_Field_Effects.md` | `en/Neuroscience/SRT_Neuro_06_Field_Effects.md` | in_progress |
| `Neuroscience/SRT_Neuro_07_Evo_Devo.md` | `en/Neuroscience/SRT_Neuro_07_Evo_Devo.md` | in_progress |
| `Neuroscience/SRT_Neuro_08_Immune_Dist.md` | `en/Neuroscience/SRT_Neuro_08_Immune_Dist.md` | in_progress |
| `Neuroscience/SRT_Neuro_09_Integ_Eq.md` | `en/Neuroscience/SRT_Neuro_09_Integ_Eq.md` | in_progress |
| `Neuroscience/SRT_Neuro_10_Advanced_Models.md` | `en/Neuroscience/SRT_Neuro_10_Advanced_Models.md` | in_progress |

## Per-File Template

Use this front matter in English files:

```yaml
source_path: Core/SRT_Core_00_Intro.md
source_commit: <git-sha>
translation_status: pending|in_progress|done
last_sync: YYYY-MM-DD
```
