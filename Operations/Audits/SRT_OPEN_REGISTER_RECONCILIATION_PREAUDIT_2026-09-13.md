---
id: SRT-AUDIT-OPEN-REGISTER-RECONCILIATION-PREAUDIT-20260913
type: audit
status: draft
record_stage: open_register_reconciliation_preaudit
layer: operations
epistemic_layer: os
claim_mode: governance
canonical: false
date: 2026-09-13
research_mode: U
root_question: Which surface owns which OPEN item, given that four surfaces now carry overlapping OPEN registers with no declared owner between them?
comparative_claim: none
named_comparator: null
n_mode_triggered: false
dependency:
  - STATUS.md
  - Core_Law/SRT_Generative_Ontology_Spine.md
  - Core_Law/SRT_One_Formation.md
  - Core/SRT_OPEN_TENSIONS.md
  - Core/SRT_Core_21b_Constitutive_Theorems.md
  - CANONICAL_REGISTRY.md
  - Governance/SRT_EDIT_PROTOCOL.md
tags: [OpenRegister, Reconciliation, PreAudit, Ownership, StatusContraction]
---

# OPEN register reconciliation — pre-audit

> **Role**: read-only inventory before any OPEN item is moved. It assigns no owner and closes nothing. Per `srt-structure-extraction` discipline, extraction without a pre-audit is forbidden; this is that pre-audit, and the adjudication in §5 is the author's.
>
> **Hard rule for the whole exercise**: **no OPEN item may be closed, merged away, or silently reworded during migration.** An item that appears on two surfaces in different words is two records of one question until someone adjudicates that they are the same question.

## 0. Baseline

Measured on `0d17abd4` (post-#962 `main`).

## 1. There are four OPEN surfaces, not two

| Surface | Items | Self-declared role |
|---|---:|---|
| `STATUS.md §OPEN register` | 28 | dashboard; the page states it is "routing / programme state, not definition authority" |
| `Core_Law/SRT_Generative_Ontology_Spine.md §9` | 21 | cross-owner generation order / non-identity / OPEN gates |
| `Core_Law/SRT_One_Formation.md §7` | 17 | local One / Selection-position owner |
| `Core/SRT_OPEN_TENSIONS.md` | ~14 pressure points + per-symbol sections | **`claim_mode: open`; self-described "hardening ledger"** — the repository already has a dedicated OPEN owner |

The fourth one matters most. `SRT_OPEN_TENSIONS.md` is not a stray list: it carries `d`, `Ψ_f`, `T_dir`, Stable-ISP boundary and ε normativity in a three-part form (Current state / Problem point / Future hardening direction) far richer than the one-line versions on the other three surfaces. Any plan that routes owner-local OPEN items "to their owners" has to decide whether that means this ledger or each owner's own §OPEN.

No surface declares itself the owner of the others, and no two lists agree on wording. `CANONICAL_REGISTRY.md §C` owns citation priority but does not assign OPEN ownership.

## 2. Reconciliation table

Every `STATUS.md` OPEN item, with where else the same question is recorded and a **proposed** bucket. Proposed, not applied.

| # | STATUS item | Spine §9 | One §7 | OPEN_TENSIONS | Proposed bucket |
|---|---|---|---|---|---|
| S01 | Oriented Openness ↔ κ₀ / ε / irreversibility exact inheritance | yes (P01) | – | yes | SPINE (L0 owner also states it) |
| S02 | irreversible occurrence → durable / localized / recurrent historical efficacy | yes (§5) | – | – | SPINE (L0 owner also states it) |
| S03 | finite positionality ↔ formation locus / post-One Position / subject-position | yes (§6) | – | – | SPINE |
| S04 | Concern ↔ typed Bearer exact implication / equivalence | yes (P10) | – | – | SPINE — possible overlap with S12; AUTHOR ADJUDICATION REQUIRED |
| S05 | strict numerical identity | yes (P04) | yes | – | SPINE |
| S06 | unique post-branch successor | yes (P04) | yes | – | SPINE |
| S07 | formal necessary-and-sufficient One theorem | yes (P02) | yes | – | SPINE |
| S08 | One-level perspective universal sufficiency | yes (P06) | yes | – | SPINE |
| S09 | formal cross-domain N&S theorem for P+E Bearer | yes (P08) | – | – | SPINE |
| **S10** | **unique empirical / numerical Bearer admission threshold** | – | – | – | **ORPHAN** |
| S11 | Bearer ↔ 承担 | yes (P09) | – | yes (L0 词条) | SPINE |
| S12 | Bearer ↔ 关切 | yes (P10) | – | – | SPINE — possible overlap with S04; AUTHOR ADJUDICATION REQUIRED |
| **S13** | **Bearer ↔ position stability** | – | – | – | **ORPHAN** |
| S14 | Bearer ↔ cognition | partial (P14 is `subject-position → cognition`) | yes | – | SPINE — wording differs, adjudicate |
| S15 | Bearer ↔ subject-position | partial (P13 is a positive gate) | yes | yes | SPINE — wording differs, adjudicate |
| S16 | phenomenality / experiencer transition | yes (P15) | yes | yes | SPINE |
| **S17** | **formal / empirical representation-invariant W1/W2 criteria** | – | – | – | **ORPHAN — and see §3** |
| **S18** | **scale attribution under tightly coupled nested Ones** | – | – | – | **ORPHAN** |
| S19 | whole-architecture non-substitutability | yes (P21) | – | yes | PROGRAMME (STATUS keeps) |
| S20 | scientific distinctiveness | yes (P20) | yes | – | PROGRAMME (STATUS keeps) |
| S21 | Level-2 realization | yes (P19) | yes | – | PROGRAMME (STATUS keeps) |
| S22 | Bearer canonical ownership / sufficiency hardening | – | yes | – | OWNER-ROUTING OPEN — current route = Spine §7; final semantic ownership NOT ADJUDICATED |
| S23 | D4b | – | yes | – | LOCAL — `SRT_One_Formation.md` |
| S24 | D4c | – | yes | – | LOCAL — `SRT_One_Formation.md` |
| S25 | d bearer/domain | yes (P16 `bare-d retyping`) | yes | yes (§1 `d` / `D_eff`) | TENSIONS primary; `_SRT_D_VALUE_CANONICAL.md` is the definition owner |
| S26 | sigma ontology threshold | – | yes | yes | LOCAL / TENSIONS — `Core_21b:177` already says threshold ownership sits with the relevant L1/formal owner |
| S27 | S3 / T_dir relation | – | yes | yes (§3 `T_dir`) | TENSIONS; `_SRT_T_DIR_CANONICAL.md` is the definition owner |
| S28 | collective subject sufficiency | yes (P17) | yes | – | SPINE |

Spine items with **no direct STATUS-register counterpart**: `exact One boundary / unit identification`, `local One-owner lineage wording reconciliation`, `positive E establishment` (echoed in `STATUS §1` prose, not in its register), `Bearer ↔ agency`, `Concern ↔ agency`, `new Level 1`.

「没有对应行」不等于「已单一 owner」。按本文件自己的规则，措辞不同不足以判定是不是同一问题，所以这一组同样未经裁决。已知的具体待核例子：Spine 的 `new Level 1` 与 One Formation §7 的 `new Level assignment` / `Level 2 / HOLD exit` 可能是同一问题的三种写法，也可能不是。单一 owner 的标记只能在四面 cross-check 并经裁决之后给出。

## 3. Orphans — the reason this cannot be a delete

Four STATUS items appear on **no** other canonical surface. Verified by direct search over `Core_Law/`, `Core/`, `Governance/`, `CANONICAL_REGISTRY.md` and the root `_SRT_*` anchors:

```text
S10  unique empirical / numerical Bearer admission threshold
S13  Bearer <-> position stability
S17  formal / empirical representation-invariant W1/W2 criteria
S18  scale attribution under tightly coupled nested Ones
```

Deleting `STATUS.md §OPEN register` without rehoming these four **loses four open questions**.

S17 is worse than an orphan item. The W1 / W2 typology itself has no canonical owner: `STATUS.md §14` is the only live surface that defines `W1 configuration writeback` / `W2 organizational writeback` and states the representation-invariance guard. The Spine does not mention W1/W2 at all. Every other occurrence is a status-history handoff, a proposal, or an author adjudication — none of which is a definition owner.

So the dashboard is currently the de-facto owner of a typology, while its own §20 says it is not a definition authority. **The §3–§15 contraction cannot proceed on W1/W2 until that typology has a home.** This is a finding about ownership, not a proposal to change what W1/W2 mean.

## 4. What the end state would look like

Proposed only; nothing here is applied.

```text
Spine §9        = cross-owner ontology OPEN gates
local owner     = owner-local structural OPEN (D4b / D4c in One Formation, ...)
OPEN_TENSIONS   = symbol- and formalism-level hardening ledger (d / Psi_f / T_dir / sigma / ISP boundary)
STATUS          = programme verdicts only (Level 2 HOLD, new Level 1, scientific
                  distinctiveness, whole-architecture non-substitutability)
                  + pointers to the three above
```

Migration order that keeps the zero-closure rule checkable:

1. rehome the four orphans (§3) — **before** anything is removed from STATUS;
2. give W1/W2 a definition owner, or record explicitly that STATUS keeps it and why;
3. for each remaining item, confirm the receiving surface already states it, then remove the STATUS line in the same commit;
4. never remove and rehome in separate commits — a gap between them is where an OPEN item disappears.

## 5. Adjudication questions — author

1. Does `Core/SRT_OPEN_TENSIONS.md` become the declared owner of owner-local / symbol-level OPEN, or does each owner keep its own §OPEN and the ledger stay a companion?
2. Where do S10, S13 and S18 land — Spine §9 as cross-owner gates, or a local owner?
3. Who owns the W1 / W2 typology? Candidates: Spine §8 (non-stage downstream surfaces), a machine-audit annex, or an explicit decision that STATUS retains it as a machine label set.
4. S04 / S12 and S14 / S15: are the differently-worded pairs one question or two? They must not be merged by an editor's judgement.
5. After migration, does STATUS keep programme verdicts plus pointers, as in §4?

## 6. Boundaries of this pre-audit

- Read-only. No file was edited for it and no OPEN item was closed, merged, reworded or moved.
- It assigns no canonical authority and creates no theory claim.
- Bucket proposals are routing proposals; wording differences are flagged, never resolved.
- It does not touch `STATUS.md §3–§15`, the Spine, One Formation, or the tensions ledger.
