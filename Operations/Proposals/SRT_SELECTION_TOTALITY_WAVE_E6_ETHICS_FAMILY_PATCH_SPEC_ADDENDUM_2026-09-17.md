---
id: SRT-SELECTION-TOTALITY-WAVE-E6-ETHICS-FAMILY-PATCH-SPEC-ADDENDUM-2026-09-17
type: proposal
status: active
layer: governance
epistemic_layer: proposal
claim_mode: binding_addendum
---

# Wave E6 ethics-family patch-spec binding addendum

This addendum is binding on:

`Operations/Proposals/SRT_SELECTION_TOTALITY_WAVE_E6_ETHICS_FAMILY_PATCH_SPEC_2026-09-17.md`

It adds execution precision only. It does not change the semantic owner set or theory posture.

## 1. Exact split-generator invocation

After the four-owner semantic commit, regenerate `Philosophy/Ethics_Split/*` from the owner with the repository generator using the existing split identity and display title:

```bash
python scripts/create_reading_split.py \
  Philosophy/SRT_Philosophy_Ethics.md \
  Philosophy/Ethics_Split \
  --id SRT-PHIL-ETHICS-SPLIT-INDEX \
  --title "SRT Philosophy Ethics" \
  --force
```

Do not manually preserve the pre-edit four-shard topology. The generator's deterministic post-edit result is authoritative.

Do not manually edit generated shard contents or README metadata after generation.

Run the same command twice from the same semantic owner state and require byte-identical output for the full split directory.

## 2. Frontmatter fail-closed rule

The patch spec permits routing/frontmatter truth-up but does not authorize governance expansion.

For each of the four semantic owners:

```text
canonical must remain false
bridge / governance / applied standing must remain downstream
SRT-GENERATIVE-ONTOLOGY-SPINE must become machine-visible where dependency governance permits
```

If adding a proposed local-owner dependency or normalizing `status` / `version` causes a status/dependency-governance failure:

```text
STOP that optional metadata normalization;
keep the current legal status/version;
do not edit Governance/** or upstream owners;
retain the semantic body truth-up and the minimum legal authority routing.
```

`SRT-GENERATIVE-ONTOLOGY-SPINE` is the minimum intended cross-owner machine route; optional local-owner additions must not be forced by changing governance.

## 3. Commit separation

The semantic commit must contain exactly:

```text
Philosophy/SRT_Philosophy_Ethics.md
Philosophy/SRT_Ethics_PH_SS_Guardrails.md
Philosophy/SRT_Philosophy_Claim_Status.md
Philosophy/SRT_Ethics_Casebook.md
```

The derivative commit must contain exactly the committed output under:

```text
Philosophy/Ethics_Split/*
```

No control-plane audit/proposal/handoff file may be mixed into either commit.

## 4. Main-drift fail-closed rule

Immediately before semantic editing and again before final governance preflight, fetch live `main`.

If main-only movement touches any of:

```text
four E6 semantic owners
Philosophy/Ethics_Split/*
Core_Law/SRT_Generative_Ontology_Spine.md
Core_Law/SRT_Suffering.md
Core_Law/SRT_Occlusion_Dynamics.md
Core_Law/SRT_Irreversibility.md
_SRT_D_VALUE_CANONICAL.md
_SRT_PSI_F_CANONICAL.md
```

STOP and request renewed overlap review. Do not auto-rebase.

## 5. Additional acceptance gates

- **E6-55** exact generator invocation above is used.
- **E6-56** two consecutive generator runs are byte-identical for the complete split directory.
- **E6-57** optional frontmatter normalization fails closed without upstream/governance edits.
- **E6-58** semantic and derivative commits are strictly separated as specified.
- **E6-59** live-main overlap is rechecked both before editing and before final preflight.

## Verdict

```text
ADDENDUM = BINDING
SEMANTIC SCOPE = UNCHANGED
THEORY POSTURE = UNCHANGED
NEXT = INDEPENDENT EXACT-SPEC REVIEW
```
