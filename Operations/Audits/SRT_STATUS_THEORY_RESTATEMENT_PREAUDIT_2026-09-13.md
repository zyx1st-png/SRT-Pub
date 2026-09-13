---
id: SRT-AUDIT-STATUS-THEORY-RESTATEMENT-PREAUDIT-20260913
type: audit
status: draft
record_stage: status_theory_restatement_preaudit
layer: operations
epistemic_layer: os
claim_mode: governance
canonical: false
date: 2026-09-13
research_mode: U
root_question: Which of STATUS §3-§15 restates an owner, which is historical record, and which is genuinely the dashboard's own — and what breaks if each is removed?
comparative_claim: none
named_comparator: null
n_mode_triggered: false
dependency:
  - STATUS.md
  - Core_Law/SRT_Generative_Ontology_Spine.md
  - Core_Law/SRT_One_Formation.md
  - CANONICAL_REGISTRY.md
  - Core/SRT_Core_21b_Constitutive_Theorems.md
  - Operations/Audits/SRT_CANONICAL_RETYPE_LEDGER.md
  - Operations/Audits/SRT_OPEN_REGISTER_MIGRATION_CLOSURE_2026-09-13.md
  - Governance/SRT_EDIT_PROTOCOL.md
tags: [Status, TheoryRestatement, PreAudit, Ownership, Contraction]
---

# STATUS §3–§15 theory restatement — pre-audit

> **Role**: read-only inventory. It moves nothing, removes nothing, and decides
> no ownership. Same discipline as the OPEN register round: pre-audit first, then
> author adjudication, then extraction.
>
> **Baseline**: `d327bf20` (post-#965 `main`), `STATUS.md` at 567 lines.

## 0. Why this section exists at all

`STATUS.md §20` states the page is routing / programme state, **not a definition
authority**. §3–§15 is roughly 280 of its 567 lines and reads as a second
statement of the current theory. The OPEN register round removed one such
overlap; this is the remaining one, and it is the largest.

The cost is not only duplication. Every bounded owner landing currently requires
a **parallel STATUS edit**, and the two surfaces drift in wording while doing it
(§1 below is a live example).

## 1. Section-by-section

| § | content | category | if removed outright |
|---|---|---|---|
| 3 | Primary ontology-generation spine | **restates Spine §1** | nothing lost — near-verbatim |
| 4 | History / verticality typed separation | **restates Spine §5** | nothing lost |
| 5 | Positionality and Selection-position | **restates Spine §6.1 / §6.2** | nothing lost |
| 6 | Perspective layering | **restates Spine §6.3** | needs line-level check |
| 7 | Anticipation layering A1 / A2 / **A3** | **carries a retired token — see §2** | must be corrected, not merely moved |
| 8 | One / Selection-position / Bearer layering | **restates Spine §4 + §7** | nothing lost — the P+E route is stated twice in the Spine already |
| 9–12 | Supersession ledger for #931 / #933 | **historical record** — see §3 | six live citations break |
| 13 | Stable ISP and B13 | **restates P1-T06 / 21C B13 routing** | needs line-level check |
| 14 | W1 / W2 | already a pointer (#965) | — |
| 15 | d / sigma / T_dir guards | mostly owner-held; d/q/o already a pointer | needs line-level check |

"Nothing lost" above means the same claim is already stated by the named owner.
It does **not** authorize deletion: the OPEN register round found four items that
looked covered and were not, so every line still needs the same one-by-one
confirmation before removal.

## 2. Hard finding — §7 uses a token the Registry has retired

`CANONICAL_REGISTRY.md:42`:

> typed layering：One-level endogenous perspective、**A1/A2/P/E 分层**须保留；
> `all Ones automatically perspective-bearing` 仍未建立。
> **历史 `A3` 仅作为 R1 gate lineage 标签，不作为当前 canonical token。**

`scripts/check_authority_routing.py:48` additionally **forbids** the string
`A1/A2/A3 anticipation` from appearing in `CANONICAL_REGISTRY.md`.

`STATUS.md §7` still presents **A1 / A2 / A3** as the current anticipation
layering, with `A3` given as "Bearer research direction".

So the fresh-session dashboard states as current a token the Registry demoted to
a lineage label, and the repository's own checker guards the Registry against
that framing while leaving STATUS uncovered — the same shape as the §20 authority
chain and the W1/W2 ownership found in the previous two rounds.

**This is not a routing question.** Whether §7 is pointed, moved or deleted, the
`A3` framing has to be corrected against `A1/A2/P/E` first, and the checker
should cover STATUS as it now does for the authority chain.

## 3. §9–§12 are historical record, and they are cited

`Operations/Audits/SRT_CANONICAL_RETYPE_LEDGER.md` rows **R2C-001 … R2C-006**
cite `STATUS.md §10` / `§11` as the *source of the retired claim* — e.g.
"pre-#947 Bearer/history route; summarized in `STATUS.md §10–11`". All six rows
are `LANDED`.

So these sections are not live claims; they are the record of what #931/#933
retired. `Governance/SRT_EDIT_PROTOCOL.md` assigns `historical status` to
`Operations/Status_History/`.

Moving them is therefore plausible but **not free**: six ledger citations point
at those section numbers, and `scripts/check_status_recording_rule.py` currently
guards exactly those two headings from renumbering for that reason. Any move must
update the six rows in the same commit, or leave a numbered pointer stub.

## 4. What a contraction would look like

Proposed only; nothing here is applied.

```text
§3-§8, §13, §15   -> one-line pointer + current-delta note per section
§7                -> correct A3 against Registry A1/A2/P/E first, then as above
§9-§12            -> Operations/Status_History/, with the six ledger citations
                     updated in the same commit
STATUS keeps      -> checkpoint, programme state, landing constraints, routing,
                     programme verdicts, pointers
```

Expected result: `STATUS.md` around 200 lines, and a Spine landing no longer
requiring a parallel dashboard edit.

## 5. Adjudication questions — author

1. Does §3–§8 become pointer + delta, or does the dashboard keep a short reading
   of the current spine for fresh sessions?
2. §7: correct `A3` to the Registry's `A1/A2/P/E` in place, or drop the
   anticipation layering from STATUS entirely and point at the owner?
3. §9–§12: move to `Operations/Status_History/` with the six ledger citations
   updated, or keep on the dashboard as the retype ledger's cited source?
4. §13 and §15: pointer, or keep as landing-relevant guards?
5. Should `check_authority_routing.py` gain a STATUS rule for retired tokens, as
   it already has for the retired authority chain?

## 6. Boundaries

- Read-only. No file was edited for this audit.
- No canonical definition, claim level, freeze class or OPEN item touched.
- Category labels are proposals; "restates" is a finding about overlap, not an
  instruction to delete. Line-level confirmation is required before any removal,
  exactly as the OPEN register round required.
- The One Formation owner cycle is not opened by this audit.
