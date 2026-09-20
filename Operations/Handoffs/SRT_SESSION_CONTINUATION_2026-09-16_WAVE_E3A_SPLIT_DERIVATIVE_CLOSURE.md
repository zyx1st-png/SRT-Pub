---
id: SRT-SESSION-CONTINUATION-2026-09-16-WAVE-E3A-SPLIT-DERIVATIVE-CLOSURE
type: handoff
status: active
layer: governance
epistemic_layer: handoff
claim_mode: execution_authorization
---

# Session continuation — Wave E3-A split derivative closure

## Authorization amendment

Wave E3-A semantic scope is unchanged. Author authorization now additionally allows deterministic regeneration of the registered reading split after the single-owner semantic commit.

Semantic owner remains exactly:

```text
Core_Law/SRT_L1_Formalism.md
```

Generated derivative scope is exactly:

```text
Core_Law/L1_Formalism_Split/README.md
Core_Law/L1_Formalism_Split/00_Part01.md
Core_Law/L1_Formalism_Split/01_Part02.md
```

No other split, Context Bundle, hook, registry, canonical owner, consumer or domain file is authorized.

## Why this amendment exists

The registered split is a non-canonical connector-safe reading copy of the owner. `scripts/create_reading_split.py` regenerates both shards and the README from the source owner. The README records source-owner bytes/SHA and shard digests. After a semantic owner change, refreshing only the README metadata would make the freshness checker pass while leaving stale shard text, so metadata-only repair is not authorized.

`LONGFORM_SPLITS.md` explicitly describes these splits as non-deletive navigation layers that do not create definition authority.

## Required two-commit structure

### Commit 1 — semantic

Exactly one file:

```text
Core_Law/SRT_L1_Formalism.md
```

Must satisfy the existing E3-A exact patch specification and gates E3A-01..E3A-24.

Suggested commit:

```text
Truth-up Wave E3-A L1 formalism after D3-E2
```

### Commit 2 — deterministic split derivatives

After Commit 1, regenerate the registered split with the repository generator, preserving the existing split identity and connector-safe role.

Use the existing generator rather than hand-editing split files. Expected command shape:

```bash
uv run python scripts/create_reading_split.py \
  Core_Law/SRT_L1_Formalism.md \
  Core_Law/L1_Formalism_Split \
  --id SRT-L1-FORMALISM-SPLIT-INDEX \
  --title "SRT L1 Formalism Split Index" \
  --force
```

The exact invocation may follow repository-local established mechanics if equivalent, but it must use `scripts/create_reading_split.py` and must not hand-edit generated content.

Expected generated files are exactly the three registered outputs above. If regeneration creates a third shard, deletes a shard, changes `LONGFORM_SPLITS.md`, changes generator source, or modifies any other path, STOP and report the unexpected derivative topology rather than broadening scope.

Suggested derivative commit:

```text
Regenerate L1 Formalism reading split after Wave E3-A
```

Do not squash the semantic and derivative commits.

## Additional derivative gates

```text
E3A-25 semantic commit contains exactly SRT_L1_Formalism.md
E3A-26 derivative commit contains exactly the three L1_Formalism_Split outputs
E3A-27 split shards are generator-produced reading copies, no hand edits
E3A-28 README source owner bytes/SHA match the semantic owner
E3A-29 shard content reflects the post-E3-A owner, not the stale pre-E3-A text
E3A-30 split freshness check PASS
E3A-31 strict Governance Preflight PASS after both commits
```

`refresh_split_metadata.py` alone is insufficient for this closure because it updates README owner metadata only and does not regenerate shard body text.

## Protected scope

Remain zero diff:

```text
Core_Law/SRT_L1_Hardening_Notes.md
Core_Law/SRT_Suffering.md
Core_Law/SRT_Individuation.md
Core_Law/SRT_Occlusion_Dynamics.md
Core_Law/SRT_Irreversibility.md
Core_Law/SRT_Collective_Selection.md
Core/SRT_Core_21b_Constitutive_Theorems.md
Core/SRT_Core_22_Equations.md
_SRT_T_DIR_CANONICAL.md
_SRT_D_VALUE_CANONICAL.md
_SRT_PSI_F_CANONICAL.md
LONGFORM_SPLITS.md
scripts/create_reading_split.py
scripts/refresh_split_metadata.py
Philosophy/*
AI/*
Spirituality/*
Neuroscience/*
Operations/Context_Bundles/*
STATUS.md
```

If Context Bundle freshness, another split, or a hook is triggered, STOP and report; this amendment authorizes only the L1 Formalism split.

## Control state

```text
Wave E2 = FINAL PASS
Wave E3-A semantic execution = AUTHORIZED
Wave E3-A L1 Formalism split derivative closure = AUTHORIZED
Wave E3-B = HOLD
E4+ = HOLD
MERGE #976 = NO
```

After semantic + derivative commits are pushed and current-head CI is checked, STOP for independent semantic and derivative review.
