---
id: SRT-AUDIT-FIVE-RELATION-PREEXECUTION-SCOPE-RESOURCE-20260914
type: audit
status: active
date: 2026-09-14
layer: meta
epistemic_layer: os
claim_mode: audit
canonical: false
ai_do_not_use_for_definition: true
research_mode: U
dependency:
  - Operations/Experiments/SRT_FIVE_RELATION_CONTROL_ABC_HARDENED_PREREG_2026-09-14.md
  - Experiments/anchoring_tiny_mdp_confirmatory/README.md
  - Experiments/AUDIT.md
tags: [Experiment, PreExecution, FiveRelationTool, Governance, Seeds, Holdout]
---

# Five-relation experiment — pre-execution scope/resource audit

## 0. Verdict

```text
computational implementation = CLEARED
new theory choice = NO
canonical edit = NO
Bearer claim in toy model = FORBIDDEN
old experiment mutation = NO
```

The repository already contains a mature confirmatory-experiment pattern in `Experiments/anchoring_tiny_mdp_confirmatory/`: calibration/holdout separation, fixed seeds, frozen configuration, tests, result JSON and audit provenance.

The five-relation experiment should reuse that governance pattern while using a new model and new directory.

## 1. New experiment boundary

Create a separate directory:

```text
Experiments/five_relation_topology_transfer/
```

Do not modify frozen prior experiments.

Initial implementation scope:

```text
Phase B0: Revision calibration sanity check;
Phase A1: consequence/revision topology under matched aggregate performance;
Phase C0: architecture-transfer classification harness using frozen relation rules.
```

Human-subject data are not required for the first C0 pass. A curated human-AI / organizational scenario corpus may be used only as a transfer-classification target, not as evidence about real human behavior.

## 2. Model terminology guard

Computational units are:

```text
formed positions;
consequence-bearing loci;
adaptive units.
```

Do not call them:

```text
Bearer;
subject;
person;
conscious agent.
```

unless a separate operational gate is later approved.

## 3. Seed and freeze discipline

Use separate seed ranges from prior experiments.

Recommended provisional allocation:

```text
calibration: 51001-51020;
A holdout: 52000-52063;
B calibration/holdout: 53000-53031;
C scenario split seeds / permutation seeds: 54000-54063.
```

No holdout seed may influence thresholds, matching tolerances or scenario rules.

## 4. Matching discipline

Control A must match before perturbation:

```text
aggregate reward;
aggregate cost;
visible option count;
short-horizon stability;
observation bandwidth;
communication bandwidth;
update budget.
```

If the matching gate fails, A is invalid and must not be interpreted.

Control B is calibration only and cannot contribute to a distinctiveness verdict.

## 5. Rival discipline

At minimum implement:

```text
R0 aggregate-only baseline;
R1 state-augmented baseline receiving all raw variables;
R2 typed-collapse baseline that receives identical variables but removes five-relation role separation.
```

The experiment must not hide information from R1/R2.

## 6. C0 transfer corpus

C0 should use a small frozen scenario corpus containing at least:

```text
algorithm shapes options but has no independently established standing;
high-level coordination improves while local consequence burden is externalized;
performance scaffold improves output but weakens endogenous revision;
policy adaptation occurs without generator revision;
collective standing forms without automatic erasure of lower-level consequence channels.
```

The corpus tests relation mapping and deletion errors only. It does not establish social truth or normative correctness.

## 7. Stop rules

Stop before execution and seek author intervention only if implementation requires deciding any of:

```text
new primitive relation;
new Bearer admission rule;
new normative aggregation rule;
new Ground claim;
new canonical metric;
change to CS-1..CS-4 meaning.
```

None is currently required.

## 8. Next action

Implementation is authorized at machine/research-program level:

```text
write model + configs + tests;
validate locally;
freeze calibration protocol;
then run B0 and A1 before C0 interpretation.
```
