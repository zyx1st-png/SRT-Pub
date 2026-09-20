---
id: SRT-SELECTION-TOTALITY-WAVE-E7-SOCIAL-POLITICAL-PATCH-SPEC-ADDENDUM-2026-09-17
type: proposal
status: active
layer: governance
epistemic_layer: proposal
claim_mode: binding_addendum
canonical: false
date: 2026-09-17
---

# Wave E7 social / political patch-spec binding addendum

This addendum is binding on:

`Operations/Proposals/SRT_SELECTION_TOTALITY_WAVE_E7_SOCIAL_POLITICAL_PATCH_SPEC_2026-09-17.md`

It resolves the derivative-tooling ambiguity in E7-J. It does not change the nine-owner semantic scope or the theory posture.

## 1. Tooling audit result

The repository contains the current generic deterministic reading-shard generator:

```text
scripts/create_reading_split.py
```

Its output topology is generic:

```text
00_Part01.md
01_Part02.md
...
README.md
```

The two E7 legacy split families do not currently use that topology.

### Social Economics legacy topology

```text
Philosophy/Social_Economics_Split/
  00_Formal_Core.md
  01_Foundations_and_Mechanisms.md
  02_HumanReadable_Framework.md
  03_Classics_and_Summary.md
  README.md
```

These files are legacy topical copies / slices of the source owner.

### Political Philosophy legacy topology

```text
Philosophy/Political_Philosophy_Split/
  00_Political_Ontology.md
  01_Legitimacy_Freedom_Rights.md
  02_Justice_Institutions_Democracy.md
  03_Emergency_and_Pathology.md
  04_Comparative_Positioning_and_Minimum_Program.md
  README.md
```

These files are legacy curated navigation summaries rather than current `create_reading_split.py` output.

The repository also contains:

```text
scripts/refresh_split_metadata.py
```

but that script updates only source-owner bytes / SHA metadata in registered split README files. It does not rewrite stale shard semantics.

Therefore neither of the following is acceptable for E7:

```text
run create_reading_split.py blindly
  -> would replace legacy named topology and discard curated navigation structure

run refresh_split_metadata.py only
  -> would update README owner hash while leaving stale strong claims inside legacy shards
```

## 2. Binding derivative strategy

For E7 only, preserve both existing legacy split topologies.

After the nine semantic owners are truth-upped, review every existing shard in both E7 split families and apply a bounded derivative truth-up wherever the shard repeats a claim that changed in its source owner.

Derivative rule:

```text
owner = authority
legacy shard / summary = navigation derivative
shard may mirror / compress owner
shard may not remain semantically stronger than owner
shard may not introduce a new theory claim
```

This is an explicitly authorized legacy-derivative maintenance operation, not a new semantic owner wave.

## 3. Exact derivative review set

Review exactly:

```text
Philosophy/Social_Economics_Split/00_Formal_Core.md
Philosophy/Social_Economics_Split/01_Foundations_and_Mechanisms.md
Philosophy/Social_Economics_Split/02_HumanReadable_Framework.md
Philosophy/Social_Economics_Split/03_Classics_and_Summary.md
Philosophy/Social_Economics_Split/README.md

Philosophy/Political_Philosophy_Split/00_Political_Ontology.md
Philosophy/Political_Philosophy_Split/01_Legitimacy_Freedom_Rights.md
Philosophy/Political_Philosophy_Split/02_Justice_Institutions_Democracy.md
Philosophy/Political_Philosophy_Split/03_Emergency_and_Pathology.md
Philosophy/Political_Philosophy_Split/04_Comparative_Positioning_and_Minimum_Program.md
Philosophy/Political_Philosophy_Split/README.md
```

No other split family may be modified by this derivative step.

A reviewed shard may remain byte-identical if it contains no E7-stale claim. The execution matrix must say so explicitly.

## 4. Derivative semantic limits

Derivative edits may only:

```text
add / strengthen navigation-only authority guards;
replace stale universal / definitional wording with the owner's new historical / candidate / framework-relative standing;
repair automatic Psi_f / high-d / legitimacy / rights / pathology inference;
preserve headings, examples, comparisons and navigation structure where possible.
```

Derivative edits may not:

```text
create a new political theory claim;
change the nine-owner semantic decision;
add a stronger criterion than the source owner;
endorse / oppose a political ideology, institution or electoral choice;
turn navigation summaries into independent authority.
```

## 5. Source-owner metadata refresh

After owner and derivative content are final, run first:

```bash
python scripts/refresh_split_metadata.py --check
```

Expected E7-relevant stale metadata includes the two README files whose source owners changed.

Before running write mode, inspect the complete `would_change` set.

If the dry run contains files outside the E7 authorized split families because of unrelated branch debt:

```text
DO NOT accept those unrelated changes into E7.
```

The executor may run the tool and restore all non-E7 outputs before commit, or use an equivalent deterministic owner-bytes / SHA update for the two authorized README files, but must report the exact procedure and verify the resulting values against the source files.

Then require:

```bash
python scripts/check_split_freshness.py --strict-metadata
```

PASS.

## 6. Commit separation

Required commit classes:

```text
Commit A — primary semantic truth-up
  only the 9 E7 semantic owners

Commit B — legacy split derivative truth-up
  only files under:
    Philosophy/Social_Economics_Split/**
    Philosophy/Political_Philosophy_Split/**

Commit C — Context Bundle generated output, only if official check is NON-NOOP
  only official Operations/Context_Bundles generated outputs
```

Control-plane files must not be mixed into these execution commits.

## 7. Additional acceptance gates

Add to the E7 matrix:

```text
E7-48 legacy split topology preserved
E7-49 all 11 legacy split files reviewed for stale E7 claims
E7-50 derivative navigation files are not stronger than source owners
E7-51 source-owner bytes / SHA metadata refreshed deterministically
E7-52 strict split metadata / freshness passes
E7-53 generic create_reading_split.py is NOT used to destroy the legacy E7 topology in this wave
```

## 8. Main-drift rule includes derivative files

Fresh-main overlap checks must include all 11 exact derivative review files above.

If main changes any of them after the prelanding checkpoint:

```text
STOP FOR RENEWED OVERLAP REVIEW
NO AUTO-REBASE
```

## Verdict

```text
ADDENDUM = BINDING
E7 SEMANTIC OWNER SET = UNCHANGED
LEGACY SPLIT TOPOLOGY = PRESERVE
DERIVATIVE TRUTH-UP = AUTHORIZED AFTER OWNER EDIT
CONTEXT BUNDLE CONDITIONAL REGEN = UNCHANGED
NEXT = INDEPENDENT EXACT-SPEC REVIEW
E7 SEMANTIC EXECUTION = NOT YET AUTHORIZED
MERGE #976 = NO
```
