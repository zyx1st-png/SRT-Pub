---
id: SRT-FACING-ADMISSION-CALIBRATION-BLIND-HANDOFF-20260927
type: handoff
status: active
canonical: false
layer: operations
epistemic_layer: governance
claim_mode: blind_calibration_handoff
created: 2026-09-27
updated: 2026-09-27
dependency:
  - Operations/Proposals/SRT_FACING_ADMISSION_TEST_V0_1_2026-09-27.md
  - Operations/Templates/SRT_FACING_ADMISSION_RECORD_TEMPLATE_V0_1_2026-09-27.md
tags: [Facing, Admission, BlindCalibration, IndependentReview]
---

# Facing Admission Test v0.1 — independent blind calibration handoff

## 0. Independence rule

Before scoring, DO NOT read:

~~~text
Operations/Audits/SRT_FACING_ADMISSION_CALIBRATION_SEED_V0_1_2026-09-27.md
~~~

That file contains the producing model's seed labels.

Read the method and template first, then source material only as needed.

## 1. Review mode

~~~text
READ-ONLY
NO canonical edit
NO Facing v0.3 edit
NO PR merge
NO use of seed labels before scoring
~~~

## 2. Required output per case

Use the v0.1 template and return:

~~~text
construct:
target cut:
explanatory burden facing:
formal/model realization facing:
Q1-Q10 compact reasoning:
verdict:
confidence:
falsifier:
~~~

Allowed verdicts only:

~~~text
FACE-L0-CANDIDATE
FACE-L1
FACE-L2
FACE-L0<->L1-BRIDGE
FACE-L1<->L2-BRIDGE
FACE-MIXED
FACE-UNDETERMINED
~~~

## 3. Blind cases

### B1 — SRT O0 open / non-preclosed burden

Target explanandum: openness / non-preclosure relative to determinate manifestation.

Primary source:
`Core_Law/SRT_Generative_Ontology_Spine.md` §2.

### B2 — SRT S0 actualising Selection

Target explanandum: determinate manifestation / actual differentiation of primitive Selection.

Primary source:
`Core_Law/SRT_Generative_Ontology_Spine.md` §§2–3.

### B3 — retained historical efficacy

Target explanandum: prior Selection remaining materially effective in later Selection conditions.

Primary source:
`Core_Law/SRT_Generative_Ontology_Spine.md` §4.

### B4 — Selection-position

Target explanandum: current operative formed from-where for later Selection, not the entire developmental lineage.

Primary source:
`Core_Law/SRT_Generative_Ontology_Spine.md` §6 plus current One/Position owner if needed.

### B5 — Gate as currently available stable coarse-graining geometry

Target explanandum: current Gate role, not historical Gate formation.

Primary sources:
`01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GATE_GEOMETRY_BEARER_FRICTION_QUALIA_L0_FREEDOM_2026-09-25.md` and the HP-B hook only if needed.

### B6 — ChoiceMap latent directional-generative organization

Target explanandum: latent, subject-internal process reconstructed from L2-facing traces and treated as generating/recutting objects, comparison scales and candidate spaces.

Primary source:
`01_Source_Intuition/SRT_AUTHOR_FACING_CHOICEMAP_REVERSE_INFERENCE_2026-09-27.md` on PR #1079.

### B7 — Barad agential cut

Target explanandum: constitutive enactment of determinate separability, not the whole Baradian theory.

Primary source:
`Operations/Audits/SRT_PREOBJECT_FOREGROUND_OBSERVABILITY_BARAD_STRONGEST_NEIGHBOR_PASS13_2026-09-10.md`.

### B8 — Simondon transduction

Target explanandum: individuation process by which individual + associated milieu become structured.

Primary source:
`Operations/Audits/SRT_MANIFESTATION_SELECTION_POSITION_D3_D4_STRONGEST_NEIGHBOR_PASS17_2026-09-10.md`.

### B9 — Whitehead / FRR actualized occasion as later datum

Target explanandum: prior actualized occasion in its objective/superjective role constraining later occasions.

Primary source:
`01_Source_Intuition/Conversations/2026-09-23_FRR_SRT_Focused_Reading_Note.md`.

### B10 — active-inference generative model

Target explanandum: a current generative model operating over declared hidden states, observations and policies.

Primary sources:
`Philosophy/SRT_FEP_Comparison.md` and `Neuroscience/SRT_Clin_02_FEP.md` as needed.

### B11 — learned prior / habit

Target explanandum: prior learned organization only insofar as it continues to constrain later inference/action.

Use a source-native active-inference / learning source already in repository; do not infer from the case wording alone.

### B12 — stored ChoiceMap transcript as archived text

Target explanandum: transcript merely as stored record, without assuming that storage itself changes later subject generation.

Primary source:
`01_Source_Intuition/SRT_AUTHOR_FACING_CHOICEMAP_REVERSE_INFERENCE_2026-09-27.md` plus ChoiceMap workflow files if needed.

## 4. Mandatory traps to police

Do not assume:

~~~text
hidden -> L0;
generative -> L0;
pre-object word -> L0;
observable -> L1;
past -> L2;
stored -> L2;
bridge -> uncertainty;
SRT term -> privileged facing;
traditional term -> downstream facing.
~~~

## 5. After blind scoring

Only after all B1-B12 verdicts are frozen:

1. read the calibration seed;
2. compare case by case;
3. classify every disagreement as:

~~~text
D-A definition ambiguity
D-B target-cut mismatch
D-C source-evidence ambiguity
D-D burden-vs-formalism confusion
D-E genuine bridge disagreement
D-F same-event analytic-vs-temporal confusion
D-G ontic-vs-epistemic L2 confusion
D-H other
~~~

4. recommend method correction only where disagreement exposes a systematic rule problem.

## 6. Final calibration output

Return:

~~~text
BLIND VERDICTS B1-B12
AGREEMENTS
DISAGREEMENTS
DISAGREEMENT CLASSIFICATIONS
METHOD DEFECTS, IF ANY
CASES UNSUITABLE FOR GOLD SET
PROPOSED GOLD-SET CANDIDATES
PROMOTE v0.1? YES / NO / WITH-CORRECTIONS
~~~

Do not promote the method into Facing v0.3/v0.4 from this handoff alone.