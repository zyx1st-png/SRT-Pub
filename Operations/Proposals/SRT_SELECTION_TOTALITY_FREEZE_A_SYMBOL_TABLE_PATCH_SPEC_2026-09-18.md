---
id: SRT-SELECTION-TOTALITY-FREEZE-A-SYMBOL-TABLE-PATCH-SPEC-2026-09-18
type: proposal
status: active
layer: governance
epistemic_layer: proposal
claim_mode: exact_patch_spec
canonical: false
date: 2026-09-18
---

# Freeze-A — exact symbol-table authority-sync patch specification

## Exact semantic file set

```text
_SRT_SYMBOL_TABLE.md
```

Exactly one semantic file.

## FA-01 — sigma_sr^sub row

Replace the current role:

```text
Subject-Position Entry Threshold
```

with a candidate-transition role such as:

```text
Subject-Position Candidate Transition Coordinate
```

Required atomic meaning:

```text
first model-coordinate threshold in the declared individuation parameterization
used to track a candidate subject-position transition;
crossing may count as model-local evidence only;
crossing does not establish subject-position, ISP entry, Bearer, consciousness,
or a representation-independent natural phase boundary.
```

Required scope note:

```text
P3/P4 model coordinate
conventional / replaceable
upstream formed One / Selection-position must be independently established
any stronger continuity / perspective / history / stake burden used by the claim
must be independently paid
exact subject-position sufficiency = OPEN
subject-position <-> Bearer = OPEN
T-IND-2 != ISP entry
```

Use the current source pointer:

```text
Core_Law/SRT_Individuation.md §4.2, §4.3, §八
```

## FA-02 — sigma_sr^self row

Replace the current role:

```text
Self-Consciousness Condensation Threshold
```

with a candidate-transition role such as:

```text
Second-Order / Self-Consciousness Candidate Transition Coordinate
```

Required atomic meaning:

```text
second model-coordinate threshold in the declared sigma_sr parameterization
used to track candidate second-order writeback condensation;
it may be interpreted as a self-consciousness candidate only when
subject-position is independently established and the stronger second-order
conditions are separately evidenced.
```

Required negative guards:

```text
crossing sigma_sr^self -/> self-consciousness universally proved
sigma_sr^self != universal natural consciousness boundary
sigma_sr^self -/> phenomenality
sigma_sr^self -/> moral standing
```

Use the current source pointer:

```text
Core_Law/SRT_Individuation.md §4.4, §4.5, §八
```

## FA-03 — no collateral theory edits

Do not change:

```text
sigma_sr base row
sigma_sr^health
sigma_sr^coll
Usage Rule 12
Tier placement
kappa_c1 / kappa_c1.5
other symbols
```

unless a mechanical syntax correction is strictly necessary. If an additional semantic row appears necessary, STOP and report instead of widening scope.

## FA-04 — protected surfaces

Zero semantic diff:

```text
Core/**
Core_Law/**
Philosophy/**
Governance/**
STATUS.md
CANONICAL_REGISTRY.md
_SRT_D_VALUE_CANONICAL.md
_SRT_PSI_F_CANONICAL.md
_SRT_T_DIR_CANONICAL.md
all split families
```

## FA-05 — semantic commit separation

First commit must contain exactly:

```text
_SRT_SYMBOL_TABLE.md
```

Suggested message:

```text
Sync Freeze-A subject-transition symbol semantics
```

## FA-06 — Context Bundle derivative

After the semantic commit:

```bash
uv run python scripts/build_srt_context_bundles.py --check
```

Expected result: NON-NOOP because Symbol Table is a SPINE input.

Then run:

```bash
uv run python scripts/build_srt_context_bundles.py
uv run python scripts/build_srt_context_bundles.py --check
```

Commit only official generated files under:

```text
Operations/Context_Bundles/**
```

Suggested message:

```text
Regenerate context bundles after Freeze-A
```

Do not hand-edit generated bundle text.

## FA-07 — validation

Before edit and before final governance, fetch latest main.

If main-only movement touches:

```text
_SRT_SYMBOL_TABLE.md
Core_Law/SRT_Individuation.md
Core_Law/SRT_Generative_Ontology_Spine.md
Context Bundle generator / generated outputs
```

STOP and do not auto-rebase.

Run at least:

```text
git diff --check
semantic exact-file-set check
generated exact-file-set check
protected-zero-diff
frontmatter / baseline / hooks / dependency / registry / authority routing
Context Bundle --check
active-theory-node check
stale phrase search:
  "Subject-Position Entry Threshold"
  "subject-position entry" in active symbol-table semantics
  "Self-Consciousness Condensation Threshold"
full Governance Preflight against latest live main
```

## FA-08 — stop rule

After push:

```text
STOP
DO NOT declare Freeze-A FINAL PASS
DO NOT enter whole-tree closure
DO NOT edit consciousness-family debt
DO NOT merge #976
DO NOT mark ready
```

Independent review closes Freeze-A.
