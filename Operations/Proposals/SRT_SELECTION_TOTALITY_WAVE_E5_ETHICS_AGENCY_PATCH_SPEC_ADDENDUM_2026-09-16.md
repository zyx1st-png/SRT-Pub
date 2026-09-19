---
id: SRT-SELECTION-TOTALITY-WAVE-E5-ETHICS-AGENCY-PATCH-SPEC-ADDENDUM-2026-09-16
type: proposal
status: active
layer: governance
epistemic_layer: proposal
claim_mode: exact_patch_spec_addendum
---

# Wave E5 exact patch spec addendum — owner frontmatter and machine routing

This addendum is binding together with:

`Operations/Proposals/SRT_SELECTION_TOTALITY_WAVE_E5_ETHICS_AGENCY_PATCH_SPEC_2026-09-16.md`.

It closes one pre-execution gap found during independent exact-spec review: the owner body can be truth-upped while its frontmatter still routes through an older authority graph.

## A1. Owner frontmatter normalization

The E5 semantic commit MAY and SHOULD modify the frontmatter of the **same single semantic owner**:

```text
Philosophy/SRT_Ethics_Agency.md
```

No second semantic owner is created by this frontmatter change.

Normalize:

```yaml
status: active
version: bridge_realign_v2
```

Keep unchanged:

```yaml
canonical: false
claim_level: P2-P4
epistemic_layer: bridge
claim_mode: mixed
```

The purpose is governance normalization, not authority promotion. `status: active` means the bridge is an active routed document; `canonical: false` and `claim_level: P2-P4` continue to block canonical/P1 standing.

## A2. Dependency truth-up

The owner dependency list must make the current cross-owner authority visible to machine routing.

Retain existing historical/support dependencies where still resolvable, and add at minimum:

```text
SRT-GENERATIVE-ONTOLOGY-SPINE
SRT-SUFFERING
SRT-OCCLUSION-DYNAMICS
SRT-IRREVERSIBILITY
```

The result must NOT imply reverse authority. These dependencies mean Ethics/Agency consumes those owners; they do not authorize Ethics/Agency to define or override them.

## A3. Additional acceptance gates

Add to the E5 acceptance matrix:

```text
E5-36 owner status normalized to an allowed active status
E5-37 owner version records bridge_realign_v2
E5-38 canonical:false / claim_level:P2-P4 preserved
E5-39 Generative Ontology Spine is machine-visible in owner dependencies
E5-40 Suffering / Occlusion / Irreversibility current local owners are machine-visible dependencies
E5-41 dependency truth-up introduces no reverse-authority or unresolved hook/dependency error
```

## A4. Scope invariant

The semantic commit remains exactly one semantic owner:

```text
Philosophy/SRT_Ethics_Agency.md
```

All protected upstream/current authority owners remain zero-diff.

If dependency normalization triggers a governance error suggesting an upstream edit, STOP; do not repair that error by broadening E5 scope.
