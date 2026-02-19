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
| Core | `Core/` | `en/Core/` | 12 | P0 | pending |
| Physics | `Physics/` | `en/Physics/` | 9 | P1 | pending |
| Neuroscience | `Neuroscience/` | `en/Neuroscience/` | 13 | P1 | pending |
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

## Per-File Template

Use this front matter in English files:

```yaml
source_path: Core/SRT_Core_00_Intro.md
source_commit: <git-sha>
translation_status: pending|in_progress|done
last_sync: YYYY-MM-DD
```
