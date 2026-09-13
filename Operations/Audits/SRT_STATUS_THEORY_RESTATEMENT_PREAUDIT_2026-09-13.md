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
| 9 | What remains retained | **retained-current compatibility record** — see §3 | a current retention statement is lost |
| 10–11 | What is demoted / retyped; what is retired | **retired-claim historical source** — see §3 | six live ledger citations break |
| 12 | W2 cases E / F current reading | **historical cases + current reading** — see §3 | the current Bearer-classifier boundary is lost |
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

**This is not a routing question.** Whether §7 is pointed, moved or deleted,
`A3` has to stop being presented as a current token first, and the checker should
cover STATUS as it now does for the authority chain.

Note what the Registry's `A1/A2/P/E` is and is not. Spine §6.3 states it as a
chain of non-identities:

```text
Selection affecting later selectability != formed-position anticipation automatically;
formed-position anticipation            != prospective self-indexing P automatically;
P                                       != Bearer without E.
```

Four burdens each paid separately — `A1` / `A2` on the anticipation side,
`P` / `E` in the Bearer gate of §7. It is **not** a four-step ladder, so
"rewrite `A1/A2/A3` as `A1/A2/P/E`" would swap one wrong framing for another.

## 3. §9–§12 is three different things, not one historical block

Only **§10 and §11** are retired-claim history. The citation pattern shows it:
`Operations/Audits/SRT_CANONICAL_RETYPE_LEDGER.md` rows R2C-001…006 cite
`STATUS.md §10` (3×), `§10–11` (1×) and `§11` (2×) as the *source of the retired
claim* — e.g. "pre-#947 Bearer/history route; summarized in `STATUS.md §10–11`",
all `LANDED`. **No ledger row cites §9 or §12.**

```text
§9   = retained-current compatibility record
§10-11 = retired-claim historical source, six live citations
§12  = historical cases carrying a current reading
```

**§9 is not history.** Its heading is "What remains retained" and its lead line
is "Retain from #931/#933 **within scope**" — a present-tense statement of which
pre-#931 content survives the reconstruction (`who causes != who bears`,
`being affected != bearing`, `multiscale standing must be paid independently at
each claimed scale`, …). Archiving it would remove a current compatibility
statement, not an archive entry. Whether each line is already held by an owner is
a line-level question, unexamined here.

**§12 is mixed.** It describes historical W2 cases E / F, but its operative
sentence is present-tense: "neither absence nor presence of that retrospective
relation is **currently** a sufficient Bearer classifier." Archiving the cases
would be one decision; dropping that boundary would be another.

**§10–11 are the archive candidates**, and moving them is not free: six ledger
citations point at those section numbers, which is exactly why
`scripts/check_status_recording_rule.py` already guards those two headings from
renumbering. Any move updates the six rows in the same commit, or leaves a
numbered pointer stub.

## 4. What a contraction would look like

Proposed only; nothing here is applied.

```text
§3-§8, §13, §15   -> one-line pointer + current-delta note per section
§7                -> A3 stops being a current token first; then A or B per §5.2
§9                -> line-level check, then pointer or retained-current summary
§10-§11           -> Operations/Status_History/, with the six ledger citations
                     updated in the same commit
§12               -> archive the cases; the current Bearer-classifier boundary
                     stays wherever its owner is
STATUS keeps      -> checkpoint, programme state, landing constraints, routing,
                     programme verdicts, pointers
```

Expected result: `STATUS.md` around 200 lines, and a Spine landing no longer
requiring a parallel dashboard edit.

## 5. Adjudication questions — author

1. Does §3–§8 become pointer + delta, or does the dashboard keep a short reading
   of the current spine for fresh sessions?
2. §7: `A3` retires as a current token either way. Then — **(A)** STATUS keeps a
   compact `A1` / `A2` anticipation pointer while `P` / `E` route to the Bearer
   owner, or **(B)** STATUS drops the anticipation layering entirely and points
   at Spine §6 + §7?

   Not on the menu: "rewrite `A1/A2/A3` as `A1/A2/P/E`". Spine §6.3 states these
   as a chain of non-identities — `Selection affecting later selectability !=
   formed-position anticipation != prospective self-indexing P`, and
   `P != Bearer without E` — i.e. four burdens each paid separately, with A1/A2
   on the anticipation side and P/E in the Bearer gate. Writing them as one
   four-step ladder would replace a retired framing with a new wrong one.
3. §10–§11: move to `Operations/Status_History/` with the six ledger citations
   updated, or keep on the dashboard as the retype ledger's cited source?
   §9: pointer, or keep as a retained-current compatibility summary?
   §12: archive the cases with a current-reading pointer, or keep the section?
4. §13 and §15: pointer, or keep as landing-relevant guards?
5. Should `check_authority_routing.py` gain a STATUS rule for retired tokens, as
   it already has for the retired authority chain? If so, the rule bans the
   **current framing** (`A3 Bearer research direction`, `A1/A2/A3 anticipation`),
   not the token's existence — `historical A3 = lineage label only` must stay
   sayable. Token presence is not claim identity, the same principle the previous
   two rounds settled.

## 6. Boundaries

- Read-only. No file was edited for this audit.
- No canonical definition, claim level, freeze class or OPEN item touched.
- Category labels are proposals; "restates" is a finding about overlap, not an
  instruction to delete. Line-level confirmation is required before any removal,
  exactly as the OPEN register round required.
- The One Formation owner cycle is not opened by this audit.
