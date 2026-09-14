---
id: SRT-EXP-FIVE-RELATION-RESULTS-V1-20260914
type: experiment_result
status: active
date: 2026-09-14
layer: meta
epistemic_layer: research_program
claim_mode: result
canonical: false
ai_do_not_use_for_definition: true
---

# Five-relation topology transfer — fresh holdout v1

## 1. Seed hygiene

Fresh ranges used after config freeze:

```text
Control A holdout: 62000-62063
Control B replication: 63000-63031
```

Previously inspected pilot ranges `52000-52063` and `53000-53031` are excluded from confirmatory interpretation.

## 2. Control A — null result on this implementation

Pre-shift matching passed exactly:

```text
max |reward diff| = 0
max |cost diff| = 0
max |alternative-mass diff| = 0
```

Fresh holdout means:

```text
post reward early:
externalized 0.3235970486
returned-revision 0.3235970486
paired difference 0

post reward late:
externalized 0.3239998305
returned-revision 0.3239998305
paired difference 0

post local cost late:
externalized 0.9048958333
returned-revision 0.9048958333
paired difference 0

post alternative scaffold mass late:
externalized 0.1570867826
returned-revision 0.1571023222
mean paired difference 0.0000155397
median paired difference 0
nonzero pairs 24 / 64
```

Interpretation:

> Under this frozen toy implementation, consequence-to-scaffold writeback topology did **not** produce a meaningful aggregate behavioral or burden difference. The tiny scaffold-distribution difference is not sufficient evidence of architecture-level surplus.

No retuning is allowed on the basis of this null.

Current disposition:

```text
Control A support for SRT architecture surplus = NO
Control A falsification of five-relation architecture = NO
Control A result = IMPLEMENTATION-LOCAL NULL
```

The null means this particular topology/model does not operationalize a discriminating effect strongly enough.

## 3. Control B — calibration replicated

Control B is calibration-only and does not count toward distinctiveness.

Fresh replication means:

```text
pre performance:
policy-only 0.9888736290
generator-revision 0.9807486290

post performance early:
policy-only 0.2332237947
generator-revision 0.3865571280
paired difference +0.1533333333

post performance late:
policy-only 0.2607206018
generator-revision 0.9565018518
paired difference +0.69578125
```

Interpretation:

```text
policy adaptation != generator revision
```

is cleanly represented by the calibration model, but mature structure-learning / adaptive-control rivals already pay this distinction.

Therefore:

```text
Control B distinctiveness evidence = NONE
```

## 4. Programme consequence

The preregistered logic already anticipated this outcome.

Because A did not provide discrimination and B is calibration-only, the architecture question now rests primarily on Control C:

```text
Can frozen Generation / Standing / Shaping / Bearing / Revision semantics
transfer across domains,
and does deleting their type separation create stable classification or prediction loss
that strong rivals cannot remove without reintroducing equivalent distinctions?
```

## 5. Status

```text
Control A = NULL ON V1 TOY MODEL
Control B = CALIBRATION PASS
Control C = REQUIRED / NOT YET EXECUTED
parameter retuning after A null = FORBIDDEN
canonical consequence = NONE
scientific distinctiveness = NOT ESTABLISHED
architecture-level non-substitutability = NOT ESTABLISHED
Level 2 = HOLD
```
