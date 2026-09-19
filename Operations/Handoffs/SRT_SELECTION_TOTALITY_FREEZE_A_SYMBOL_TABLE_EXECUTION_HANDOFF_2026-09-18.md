---
id: SRT-SELECTION-TOTALITY-FREEZE-A-SYMBOL-TABLE-EXECUTION-HANDOFF-2026-09-18
type: handoff
status: active
layer: governance
epistemic_layer: operations
claim_mode: execution_handoff
canonical: false
date: 2026-09-18
---

# Freeze-A symbol-table authority-sync — full-worktree execution handoff

## Current gate

```text
E7 = FINAL PASS
FREEZE-A READ-ONLY AUDIT = PASS
FREEZE-A EXACT PATCH SPEC = PASS / BINDING
FREEZE-A FINAL PASS = NOT YET
NEW AUTHOR THEORY ADJUDICATION = NOT REQUIRED
MERGE #976 = NO
MARK READY = NO
```

Branch:

```text
theory/ground-cycle-preobject-differentiation-20260914
```

Current control-plane head before this handoff:

```text
fc0957f41ef6bffb8e25ae4fda20c5b6f4280b37
```

Latest verified live main:

```text
d89b883683e55cb18f1088cd597618ec0438b64b
```

Main has not moved since the E7 execution / closeout sequence. Re-fetch before edit and before final governance.

## Required reading

Read fully:

```text
Operations/Audits/SRT_SELECTION_TOTALITY_WAVE_E7_FINAL_CLOSEOUT_2026-09-18.md
Operations/Audits/SRT_SELECTION_TOTALITY_FREEZE_A_SYMBOL_TABLE_PRELANDING_2026-09-18.md
Operations/Proposals/SRT_SELECTION_TOTALITY_FREEZE_A_SYMBOL_TABLE_PATCH_SPEC_2026-09-18.md
_SRT_SYMBOL_TABLE.md
Core_Law/SRT_Individuation.md
Core_Law/SRT_Generative_Ontology_Spine.md
```

## Exact semantic scope

Exactly one semantic file:

```text
_SRT_SYMBOL_TABLE.md
```

Exactly two semantic rows:

```text
sigma_sr^sub
sigma_sr^self
```

Do not edit any other symbol row unless a purely mechanical syntax correction is strictly required. If an additional semantic row seems necessary, STOP and report.

## Required semantic result

### sigma_sr^sub

Current stronger wording such as:

```text
Subject-Position Entry Threshold
first threshold ... for subject-position entry
```

must become a model-local candidate-transition coordinate.

Required reading:

```text
crossing may count as model-local evidence only
-/> subject-position admission
-/> ISP entry
-/> Bearer
-/> consciousness
-/> natural phase boundary

exact subject-position sufficiency = OPEN
subject-position <-> Bearer = OPEN
```

### sigma_sr^self

Current stronger wording such as:

```text
Self-Consciousness Condensation Threshold
```

must become a candidate second-order / self-consciousness transition coordinate.

Required reading:

```text
subject-position must already be independently established
second-order writeback burden must be separately evidenced
crossing -/> self-consciousness universally proved
crossing -/> phenomenality
crossing -/> moral standing
```

Use the current Individuation sections as source pointers; do not preserve stale section references.

## Explicitly protected from Freeze-A

Do not edit:

```text
sigma_sr base row
sigma_sr^health
sigma_sr^coll
Usage Rule 12
Tier placement
kappa_c1
kappa_c1.5
all other symbol rows
Core/**
Core_Law/**
Philosophy/**
Governance/**
STATUS.md
CANONICAL_REGISTRY.md
all split families
```

The consciousness-family issue around `kappa_c1 / kappa_c1.5` is later whole-tree debt because its source owner itself remains stronger. Do not mask it by changing only the registry row in Freeze-A.

## Commit A — semantic owner

First commit must contain exactly:

```text
_SRT_SYMBOL_TABLE.md
```

Suggested message:

```text
Sync Freeze-A subject-transition symbol semantics
```

## Commit B — generated Context Bundles

Because `_SRT_SYMBOL_TABLE.md` is a SPINE Context Bundle input, run:

```bash
uv run python scripts/build_srt_context_bundles.py --check
```

Expected after semantic edit: NON-NOOP.

Then:

```bash
uv run python scripts/build_srt_context_bundles.py
uv run python scripts/build_srt_context_bundles.py --check
```

Commit only official generator output under:

```text
Operations/Context_Bundles/**
```

Suggested message:

```text
Regenerate context bundles after Freeze-A
```

Do not hand-edit generated bundles.

## Validation

Before semantic edit and before final governance:

```text
fetch latest live main
check main-only overlap with:
  _SRT_SYMBOL_TABLE.md
  Core_Law/SRT_Individuation.md
  Core_Law/SRT_Generative_Ontology_Spine.md
  scripts/build_srt_context_bundles.py
  Operations/Context_Bundles/**
```

If overlap exists:

```text
STOP
NO AUTO-REBASE
```

Otherwise run:

```text
git diff --check
semantic exact-file-set check
generated exact-file-set check
protected-zero-diff
frontmatter validation
baseline monotonicity
hooks / dependencies
registry consistency
authority routing
status rule
material-log consistency
book-split guard where applicable
Context Bundle --check
active-theory-node check
stale phrase / authority search
full Governance Preflight against latest live main
```

Required stale searches include at least:

```text
"Subject-Position Entry Threshold"
"for subject-position entry" in active symbol-table row
"Self-Consciousness Condensation Threshold"
sigma_sr^sub -> ISP entry
sigma_sr^sub -> subject admission
sigma_sr^self -> universal consciousness admission
```

## STOP

After push, report and STOP.

Do not:

```text
declare Freeze-A FINAL PASS
enter whole-tree closure
edit consciousness-family debt
edit SRT_Soc_03_Institutions.md
merge #976
mark ready
```

Independent review closes Freeze-A.
