---
id: SRT-GRG-BCTB0-T1-SOURCE-MANIFEST-20260922
type: calibration_input_manifest
status: candidate
date: 2026-09-22
canonical: false
ai_do_not_use_for_definition: true
---

# BCTB-0 T1 source-pack manifest — candidate

historical cut:

```text
9900f425369b8840eac9220e567a60b811c52b27
```

Compiler rule:

1. fixed roots exactly as charter §7.1;
2. frontmatter dependencies of fixed roots only, one hop;
3. explicit links matching `Operations/GRG/{NegativeControls,Cases,Transfers,Records}/*.md` in fixed-root text;
4. deduplicate by exact path, first occurrence wins;
5. no target keyword search;
6. no semantic usefulness selection;
7. missing path remains recorded and is not replaced.

| # | rule | path | exists at cut | blob sha |
|---:|---|---|---|---|
| 1 | ROOT | `Operations/GRG/SRT_GRG_RELATION_LIBRARY_V0_1.md` | YES | `838ee77b1ef32df4755bbdf45f326cfd2fe76399` |
| 2 | ROOT | `Operations/Proposals/SRT_GRG_RESEARCH_FRAMEWORK_V0_1_2026-09-21.md` | YES | `6fd1fb5653f07e7036db0d2e747955c81a065b27` |
| 3 | ROOT | `Operations/Proposals/SRT_GRG_DOMAIN_CIVILIZATION_ATLAS_SEED_V0_1_2026-09-21.md` | YES | `44f8e41c1e5dd19d6657d14899c7ff1938a8ec24` |
| 4 | ONE-HOP-DEPENDENCY | `Operations/Templates/SRT_GRG_RELATION_RECORD_TEMPLATE_V0_1.md` | YES | `6797cfb528393a737190c4e3d7b347f91aebf1d5` |
| 5 | ONE-HOP-DEPENDENCY | `Operations/Audits/SRT_GRG_X3_X4_SOURCE_PRESSURE_PASS1_2026-09-21.md` | YES | `b8aae0f0d30f90aa6cf3a29ffcac63bd75c4f33e` |
| 6 | EXPLICIT-GRG-RECORD-LINK | `Operations/GRG/NegativeControls/SRT_GRG_NEG_X3B_FORMAL_DECOUPLING_2026-09-21.md` | YES | `e19fd51551673687978cebccca333a24986f4310` |
| 7 | EXPLICIT-GRG-RECORD-LINK | `Operations/GRG/NegativeControls/SRT_GRG_NEG_X4B_ECOSYSTEM_ENGINEERING_ONLY_2026-09-21.md` | YES | `0f11abb54fc1a6d767025d147131bcc2602be407` |
| 8 | ONE-HOP-DEPENDENCY | `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GRG_MAINLINE_FRAMEWORK_VS_CALIBRATION_2026-09-21.md` | YES | `e56c68bd6299790bb66cdfdd973677fef1535168` |
| 9 | ONE-HOP-DEPENDENCY | `01_Source_Intuition/SRT_AUTHOR_GRG_FOUNDING_TELOS_GENERATIVE_NORMATIVITY_2026-09-20.md` | YES | `28c75343b87a0ddeddc7b5300cf0614408605b2d` |
| 10 | ONE-HOP-DEPENDENCY | `01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GENERATIVE_EXPECTATION_TYPING_2026-09-20.md` | YES | `7dee3fbd9b20acdc108740a7df817a614d5fae76` |
| 11 | ONE-HOP-DEPENDENCY | `Operations/Proposals/SRT_GENERATIVE_RELATIONAL_GRAMMAR_PROGRAMME_V0_1_2026-09-20.md` | YES | `54ef9c00208faf55af3b47a09091c7f78383e4e2` |
| 12 | ONE-HOP-DEPENDENCY | `Operations/Templates/SRT_DOMAIN_RECONSTRUCTION_FRAMEWORK_TEMPLATE.md` | YES | `0a8a97cdff3e2e81b584b2197aae2d9c6079f042` |
| 13 | ONE-HOP-DEPENDENCY | `Operations/Proposals/SRT_CONSTITUTION_DOMAIN_ARCHITECTURE_V2_2026-09-04.md` | YES | `64f886b081978dec88a7e1fc86730de531da6b0f` |
| 14 | ONE-HOP-DEPENDENCY | `Operations/Proposals/SRT_GRG_CIVILIZATIONAL_LEARNING_ARCHITECTURE_V0_1_2026-09-21.md` | YES | `b570fc064760b9ba0812e753dd6fd63194e0d498` |

Compiler output count = 14

Missing count = 0
