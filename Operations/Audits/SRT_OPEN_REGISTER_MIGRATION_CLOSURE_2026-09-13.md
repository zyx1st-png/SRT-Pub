---
id: SRT-AUDIT-OPEN-REGISTER-MIGRATION-CLOSURE-20260913
type: audit
status: active
record_stage: open_register_migration_closure
layer: operations
epistemic_layer: os
claim_mode: governance
canonical: false
date: 2026-09-13
research_mode: U
root_question: Did every OPEN item leaving STATUS.md arrive somewhere, unchanged and unclosed?
comparative_claim: none
named_comparator: null
n_mode_triggered: false
dependency:
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_OPEN_REGISTER_OWNERSHIP_2026-09-13.md
  - Operations/Audits/SRT_OPEN_REGISTER_RECONCILIATION_PREAUDIT_2026-09-13.md
  - Operations/Audits/SRT_OPEN_REGISTER_OWNERSHIP_ADJUDICATION_2026-09-13.md
  - STATUS.md
  - Core_Law/SRT_Generative_Ontology_Spine.md
  - Core_Law/SRT_One_Formation.md
  - Core_Law/SRT_Collective_Selection.md
  - Core/SRT_OPEN_TENSIONS.md
  - Operations/SRT_W1_W2_WRITEBACK_AUDIT_LABELS.md
tags: [OpenRegister, Migration, Closure, StatusContraction]
---

# OPEN register migration — extraction record and closure

Third stage of pre-audit → adjudication → extraction. Executes
`SRT_OPEN_REGISTER_OWNERSHIP_ADJUDICATION_2026-09-13.md` and reports whether the
zero-closure rule held.

## 1. Closure check — 28 / 28

Every item that stood in `STATUS.md §OPEN register` was searched for in the
receiving surfaces after the move. All 28 are accounted for; **none was closed,
and none was reworded except where the adjudication required it**.

| # | item | now held by |
|---|---|---|
| S01 | Oriented Openness ↔ κ₀ / ε / irreversibility inheritance | Spine §9 |
| S02 | irreversible occurrence → durable / localized / recurrent efficacy | Spine §5 (verbatim "does not settle…") |
| S03 | finite positionality ↔ formation locus / post-One Position / subject-position | Spine §9 **(added)** |
| S04 + S12 | Concern ↔ typed Bearer / Bearer ↔ 关切 | Spine §9 `Bearer <-> Concern / 关切` — **one record** |
| S05 | strict numerical identity | Spine §9, One §7 |
| S06 | unique post-branch successor | Spine §9, One §7 |
| S07 | formal N&S One theorem | Spine §9, One §7 |
| S08 | One-level perspective universal sufficiency | Spine §9, One §7 |
| S09 | formal cross-domain P+E Bearer theorem | Spine §9 |
| S10 | unique empirical / numerical Bearer admission threshold | Spine §9 **(added, PROVISIONAL)** |
| S11 | Bearer ↔ 承担 | Spine §9 |
| S13 | Bearer ↔ position stability | Spine §9 **(added, PROVISIONAL)** |
| S14 | Bearer ↔ cognition | Spine §9 **(added)** |
| S15 | Bearer ↔ subject-position | Spine §9 **(added)** |
| S16 | phenomenality / experiencer transition | Spine §9, One §7 |
| S17 | representation-invariant W1/W2 criteria | `Operations/SRT_W1_W2_WRITEBACK_AUDIT_LABELS.md` **(new owner)** |
| S18 | scale attribution under tightly coupled nested Ones | **split**: Spine §9 (gate) / One §7 (local formation-unit) / Collective §9.8 (higher-order realization) |
| S19 | whole-architecture non-substitutability | STATUS (programme verdict) |
| S20 | scientific distinctiveness | STATUS (programme verdict) |
| S21 | Level-2 realization | STATUS (programme verdict) |
| S22 | Bearer canonical ownership / sufficiency hardening | Spine §9 **(added, owner-routing OPEN)** |
| S23 / S24 | D4b / D4c | One §7 |
| S25 | d bearer/domain | One §7, OPEN_TENSIONS §1 |
| S26 | sigma ontology threshold | One §7, OPEN_TENSIONS |
| S27 | `S3` / `T_dir` relation | OPEN_TENSIONS §3 **(added, `S3 /` prefix preserved)** |
| S28 | collective subject sufficiency | Spine §9, One §7 |

## 2. Items that needed adding, and why deleting them would have lost them

Eight rows above are marked **(added)**. Six of those are the reason this
migration could not be a delete:

- **S03** — Spine §6 carries the *non-identity guards* (`finite positionality !=
  formed One / Selection-position / perspective / Bearer / subjecthood`) but did
  not state the exact relation as open. Guards are not an OPEN record.
- **S14 / S15** — the nearest Spine items were `subject-position -> cognition`
  (P14) and `positive subject-position gate` (P13). Neither is a *Bearer*
  relation. The pre-audit had marked both "partial"; treating partial as covered
  would have dropped two questions.
- **S10 / S13 / S22** — orphans, present on no other canonical surface.
- **S27** — `Core_Law/SRT_One_Formation.md §7` carries `T_dir relation` without
  the `S3 /` prefix. Differently worded is two records until adjudicated, and
  S27 was never put to the author, so the full wording was preserved.

## 3. Qualifications carried into the receiving surfaces

```text
S10, S13 = PROVISIONAL ROUTING in Spine §9
```

Recorded in the Spine with the reason stated there: `Bearer canonical ownership`
(S22) is itself open, so this routing is where they are held until that is
settled — not a finding that the spine owns Bearer. Without the marker the
routing would close S22 with itself.

```text
S04 + S12 = merged records, question still OPEN
```

Stated in both the Spine and `STATUS.md`, because a reader of either alone would
otherwise see one item where the dashboard had two and could read the merge as a
closure.

```text
S18 = split three ways, not moved whole
```

Forced by the receiving file's own text: `SRT_Collective_Selection.md` declares
it does not define `One / Selection-position` and carries the R1 One-formation
boundary. Its new §9.8 says so explicitly and forbids inferring One formation or
unit division from the item.

## 4. The 一进一出 for the new owner

`Operations/SRT_W1_W2_WRITEBACK_AUDIT_LABELS.md` is the 一进.
The 一出 is `STATUS.md §14`'s de-facto ownership of the W1/W2 typology: that
section now points at the new owner and no longer defines the labels. The new
file records this in its own "Why this file exists" section, so the trade is
visible from the file that caused it. `claim_mode: machine`, `canonical: false` —
the labels were not promoted on the way out.

## 5. What did not happen

```text
no OPEN item closed;
no canonical definition changed;
no claim level or freeze class changed;
no P-level assigned or moved;
S22 Bearer canonical ownership = STILL OPEN;
One Formation owner cycle = NOT OPENED.
```

Edits to `Core_Law/SRT_Generative_Ontology_Spine.md`, `SRT_One_Formation.md` and
`SRT_Collective_Selection.md` are confined to their OPEN registers and the notes
attached to them. No definition, theorem, guard or ordering in those files was
touched.

## 6. Verification run

- 28 / 28 items located in a receiving surface by direct search after the move
- `governance_preflight.py --strict-split-metadata` → `preflight: failures=0`
- `check_status_recording_rule.py` → PASS
- `check_authority_routing.py` → PASS
- `check_frontmatter.py --fail-on-new-warnings` → `errors=0 warnings=0`
- context bundles regenerated from a clean tree (the Spine is a bundle body file)
