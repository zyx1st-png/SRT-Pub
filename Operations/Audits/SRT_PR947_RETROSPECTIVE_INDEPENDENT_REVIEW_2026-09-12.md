---
id: SRT-PR947-RETROSPECTIVE-INDEPENDENT-REVIEW-20260912
type: audit
status: active
record_stage: retrospective_independent_review
date: 2026-09-12
layer: operations
epistemic_layer: os
claim_mode: audit
canonical: false
ai_do_not_use_for_definition: true
research_mode: U
root_question: Does the canonical generative ontology spine landed by PR #947 actually hold as a cross-owner routing standard when re-derived independently from the repository, and what did landing it before old-canonical cleanup leave unpaid?
n_mode_triggered: false
dependency:
  - Core_Law/SRT_Generative_Ontology_Spine.md
  - CANONICAL_REGISTRY.md
  - Governance/SRT_CANONICAL_FREEZE.md
  - Operations/Audits/SRT_GENERATIVE_ONTOLOGY_SPINE_CANONICAL_LANDING_SCOPE_2026-09-11.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GENERATIVE_SPINE_FIRST_CANONICAL_CLEANUP_2026-09-11.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_R1_BEARER_PROSPECTIVE_EXPOSURE_2026-09-11.md
  - Core_Law/SRT_One_Formation.md
  - Core/SRT_Core_21b_Constitutive_Theorems.md
  - SRT_AI_START.md
tags: [PR947, RetrospectiveReview, GenerativeSpine, CanonicalAuthority, Routing, CleanupDebt, Governance]
---

# PR #947 — retrospective independent review

> **Scope:** independent post-merge review of PR #947 (`Land canonical generative ontology spine before old-canonical cleanup`, merged 2026-09-11, 15 files, +1453/-121). The review re-derives what #947 claimed from the repository itself rather than from the PR description, and asks what landing the spine **before** cleanup left unpaid.
>
> **This record is not:** an author adjudication, a canonical file, a Level assignment, or authorization to close any OPEN gate. It proposes dispositions; it does not apply them. No canonical, routing or governance file was edited by this review — the findings below touch C-risk authority surfaces and belong to author adjudication, not to the reviewer.

---

## 1. Method

Independent re-derivation, not description-following:

1. read `Core_Law/SRT_Generative_Ontology_Spine.md` in full and checked its internal consistency before reading the PR rationale;
2. checked every claim in the PR body against `git diff f7676c4..a6dc96e`;
3. re-derived the Bearer gate from its author provenance (`SRT_AUTHOR_ADJUDICATION_R1_BEARER_PROSPECTIVE_EXPOSURE_2026-09-11.md`) rather than from the spine's own summary;
4. searched the repository for every surface that references the new spine, and for every competing authority chain that does not;
5. ran the repository's own checks: `scripts/check_frontmatter.py`, `scripts/build_srt_context_bundles.py --check`, and read `scripts/governance_preflight.py` to establish what is and is not machine-verifiable here;
6. sampled the legacy conflict surface (`Stable ISP`, `σ_sr^sub` / T-IND-2, `bearer`, `d > 0`) to size the cleanup debt the PR deferred.

---

## 2. Verification of the PR's own claims

Every claim in the PR body was checked against the diff and the merged tree. All hold.

| PR claim | Independent result |
|---|---|
| Adds `Core_Law/SRT_Generative_Ontology_Spine.md` as cross-owner canonical spine | CONFIRMED — 492 lines, `canonical: true`, `claim_mode: canonical` |
| Registers it at the top of registry definitions routing | CONFIRMED — new `§A.0`, plus `dependency:` header update |
| Changes canonical citation priority so the spine is checked before local owners | CONFIRMED — registry `§C` now 10 steps, spine at position 2 |
| Adds the spine to `Governance/SRT_CANONICAL_FREEZE.md` | CONFIRMED — freeze list A, plus a new cross-owner routing rule |
| Updates `scripts/build_srt_context_bundles.py` so the SPINE bundle includes the new owner | CONFIRMED — added to both `SPINE` and `SPINE_BUCKETS` |
| Regenerates bundles with clean provenance and budget validation | CONFIRMED — `--check` reports 9 files byte-identical; `source_dirty: false` |
| Does not rewrite old canonical bodies | CONFIRMED — no L0 / Core_21* / d / Ψ_f / T_dir body was touched |
| No new Level 1; Level 2 remains HOLD | CONFIRMED — no Level file changed; spine `§10` keeps both OPEN |

Machine checks on the merged tree: `check_frontmatter.py` → `errors=0` (the 1423 warnings are the pre-existing BOOK-archive baseline; the spine raises none). `build_srt_context_bundles.py --check` → pass. `governance-preflight` → success on the merged head. No temporary file leaked into `main`: `.github/workflows/` holds only the two permanent workflows and `scripts/` holds no `tmp_*`.

Theory-side fidelity, re-derived rather than trusted:

- the P + E gate reproduces author option **B** faithfully, including both asymmetries (`P without E`, `E without P`);
- the Stable-ISP guard does **not** contradict its owner — `P1-T06` was already repaired in #938/#940 and now states the same formation/standing boundary;
- `Core_Law/SRT_Individuation.md` already carries an R1 owner-boundary note (line 36) subordinating `σ_sr^sub` / T-IND-2, so the sharpest legacy conflict was pre-guarded before #947;
- sampled Philosophy / AI downstream files carry explicit `canonical caution` blocks; they disclaim the blocked inference shapes rather than asserting them.

**Assessment:** the landing is honest. Nothing was overstated in the PR description, and the mechanical work is clean and reproducible. The findings below are about what the landing does not yet cover.

---

## 3. Findings

Severity is relative to the spine's own purpose: preventing older canonical material from silently controlling current routing.

### F1 — A competing authority chain still ships in bootstrap read #1 (HIGH)

`SRT_AI_START.md §6` still publishes:

```text
When exact current registered meanings are required, still follow the existing authority chain:
1. CANONICAL_REGISTRY.md
2. Governance/SRT_CLAIM_LADDER.md
3. Governance/SRT_CLAIM_MODE_AUDIT.md
4. Core_Law/SRT_L0_Metaphysics.md
...
```

The spine is absent, and the section explicitly claims to "record present repository authority". `SRT_AI_START.md` is bootstrap read #1 under `AGENTS.md §Session Start`, and it is also the **first file inside the SPINE context bundle** — so the bundle assembled to carry the new routing opens with a chain that omits it.

This is exactly the shape the spine's own `§9` cleanup test #6 names (*authority duplication — does a reader / bridge / FAQ / alignment file redefine an object owned elsewhere?*). It is the highest-leverage single fix.

**Proposed disposition:** RETYPE `§6` to defer to `CANONICAL_REGISTRY.md §C` instead of restating a parallel chain. (Owner-level edit — author adjudication required.)

### F2 — `Bearer` became a canonical typed term over ~480 files of legacy usage (HIGH)

#947 canonicalizes `Bearer` as a specific gate (`One + P + E`) and simultaneously states `Bearer != 承担 / concern / subject / experiencer by definition`. But:

- 482 markdown files use the word `bearer` in the pre-spine sense (`same-bearer stake`, `bearer consequence return`, `已建立的 bearer`);
- `SRT_Glossary.md` has **no** `Bearer` entry at all (last touched 2026-08-18, #830);
- `_SRT_SYMBOL_TABLE.md` has no row for it;
- no legacy-reading rule was published.

So after #947 the token is a live homonym with no disambiguation rule, in the one area the spine most wants precision. Note the failure mode is not that downstream files overclaim — the sampled ones are heavily guarded — it is that their guards are written against the *older* sense and now read ambiguously.

**Proposed disposition:** add a Bearer disambiguation entry (spine `§7` note or `SRT_Glossary.md`) fixing how pre-#947 `bearer` occurrences are to be read until retyped.

### F3 — Supersession was declared without a conflict inventory (MEDIUM-HIGH)

Spine `§0`: conflicting older cross-layer inference "becomes cleanup / retyping debt". `§9` supplies the disposition vocabulary (`KEEP | RETYPE | DEMOTE | RETIRE | MERGE | SIMPLIFY | OPEN`). The landing scope `§5` lists nine target *areas* in prose. What does not exist anywhere is a **per-claim register**: which specific older statements are in conflict, and what disposition each receives.

Consequence: the supersession rule is currently invocable but not auditable. Any agent can retire an older canonical claim by asserting spine conflict, and no record shows whether that conflict was ever adjudicated. Sizing: `Stable ISP` alone appears in ~110 non-Operations files; `σ_sr^sub` is narrow (7 Core_Law + 1 Core + symbol table + registry).

**Proposed disposition:** open a retyping ledger keyed by claim, using the `§9` vocabulary, before the reverse audit starts — it is the artifact the reverse audit will otherwise have to invent mid-flight.

### F4 — Registry `§A.0` cites a token the canonical file does not define (MEDIUM)

`CANONICAL_REGISTRY.md §A.0` says `typed layering：One-level endogenous perspective、A1/A2/A3 anticipation 分层须保留`. The spine defines `A1`, `A2`, `P`, `E` — `A3` appears nowhere in it. The mapping `A3 = P` exists only in the noncanonical landing scope `§4`, and `A3` itself is defined only in `Operations/Audits/SRT_R1_BEARER_PROSPECTIVE_EXPOSURE_AUTHOR_GATE_2026-09-11.md`. A routing surface therefore points at a label its canonical target does not carry, and the resolution lives in a file marked `ai_do_not_use_for_definition: true`.

**Proposed disposition:** either add `P (= A3 in the R1 gate lineage)` to the spine `§6.4`, or drop `A3` from the registry entry. The first preserves provenance traceability.

### F5 — The E criterion is a coherence test, not an applicable criterion (MEDIUM)

Spine `§7`:

```text
If a consequence burden can be completely reassigned to another unit while the claimed
Bearer relation is said to remain unchanged, E has not been established for the original One.
```

`E` is stated in terms of "the claimed Bearer relation" — so it tests an already-asserted Bearer attribution for coherence; it cannot decide Bearer for a One where no claim is yet on the table. The modality is also unbound (reassignable by whom, under which counterfactual, at which scale). This is inherited verbatim from the author adjudication, so it is not a drafting error introduced by #947; but the spine presents it as the `E semantic test` inside a section whose role is gating.

`§10` currently registers only *formal cross-domain N&S theorem for P + E Bearer* as OPEN, which is a weaker and different gap.

**Proposed disposition:** relabel as a consistency test, and register `independently applicable E criterion` in `§10`.

### F6 — Two canonical formation-order blocks with different granularity (MEDIUM)

`Core_Law/SRT_One_Formation.md §0` opens `The canonical order is:` with a 4-node trunk (subjectless Selection → event-level active verticalization → recurrent localized vertical organization → One / Selection-position). The spine `§1.1` publishes a 6-node trunk (`G0`–`G5`), adding minimum non-neutrality upstream and separating manifestation/backgrounding.

They are compatible — the spine's `G2` is folded into `Def-OF-1`, `G0` sits in L0 — but two canonical files now each publish "the canonical order" for the exact object the spine claims to own. An agent asking for the formation order gets two differently segmented answers depending on which file it reached first.

**Proposed disposition:** RETYPE `One_Formation §0` to cite the spine trunk and keep only its local `Def-OF-*` elaboration.

### F7 — The frozen spine delegates detail to an unfrozen draft (MEDIUM)

The spine is in freeze list A. Its named local owner for One formation, `Core_Law/SRT_One_Formation.md`, is `status: draft`, `claim_level: P1-candidate`, and appears in **neither** freeze list A nor B — so the file the frozen routing spine points at for "detailed definitions" is freely rewritable. `Core_Law/SRT_Individuation.md` (`status: draft_v0`, `claim_mode: hybrid`) is likewise unlisted.

**Proposed disposition:** decide the freeze status of the local owners the spine delegates to; at minimum add `One_Formation` to list B.

### F8 — A quotable shortcut inside the anti-shortcut file (LOW-MEDIUM)

Spine `§1.2` ends with the bare line `P + E -> Bearer`. `§7` states the actual gate as `already admitted One / Selection-position + P + E -> Bearer`. In context `§1.2` sits under "After G5", so it is not wrong — but it is the one line in the file most likely to be extracted into a bundle summary, a domain patch or a downstream citation, and it drops the precondition. A file whose purpose is blocking shortcut inference should not ship a quotable shortcut.

**Proposed disposition:** restate `§1.2` as `formed One + P + E -> Bearer`.

### F9 — Claim-strength ratchet between the adjudication and the spine (LOW-MEDIUM)

Author adjudication: P + E yields a "**Bearer standing candidate** accepted at the reconstruction level". Spine `§7` heading: "Bearer — P + E at **current canonical semantic strength**", described as a "canonical semantic / architectural gate".

The spine does guard this (`§7` strength guard; frontmatter `claim_level: mixed_P0_P1_candidate_open`; registry: `不是形式化或实证 N&S theorem`). The residual risk is downstream: a citer picks up "canonical gate" and drops "candidate", because the candidacy lives in frontmatter and a guard paragraph rather than in the statement itself.

**Proposed disposition:** one explicit citation rule in `§11` — cite the gate as canonical *routing*, never as an established theorem.

### F10 — Routing surfaces not updated, partially compensated (LOW)

Not updated by #947 and still stale: `CLAUDE.md §权威层级` (registry 1, L0 2, …), `_SRT_MANIFEST.yaml canonical_anchors`, `_SRT_AGENT_RETRIEVAL_PROFILE.md §2.2 Theory Advancement`, `AGENTS.md §Canonical Runtime Paths`.

Compensations that genuinely reduce this: registry is step 1 of every chain and now carries `§A.0` + the reordered `§C`; `STATUS.md` (via #948) names the spine first for ontology/cleanup work; the SPINE bundle carries the spine text in the right position.

Explicitly **not** a #947 regression: absence from `_SRT_INDEX.md` and from the symbol table matches existing practice — `Core_Law/SRT_One_Formation.md` is absent from both as well. That is pre-existing routing debt, not something this PR introduced.

**Proposed disposition:** fold into the same pass as F1; these are the same edit class.

### F11 — None of F1/F4/F10 is machine-detectable (LOW, process)

`governance_preflight.py` covers large files, split freshness, registry-split consistency, material log, frontmatter (baselined), integration-hook closure, and bundle byte-freshness. Nothing checks that the repository's several authority chains agree with each other. That is why #947 could reorder registry `§C` while `SRT_AI_START.md §6` kept the old order, with every check green.

**Proposed disposition:** add a check that each priority chain (`CLAUDE.md §权威层级`, `SRT_AI_START.md §6`, `_SRT_MANIFEST.yaml canonical_anchors`) is a consistent projection of registry `§C`. This is the one finding that is cheap, mechanical, and prevents the whole class from recurring.

### F12 — Merge posture (process, informational)

Opened 2026-09-11T16:06:23Z, merged 16:12:47Z — **6m24s**, self-merged, **0 reviews**, on an edit the PR itself classifies as C-risk authority change. Of its 26 commits, 8 are add/remove pairs of ephemeral `.github/workflows/tmp-*.yml` and `scripts/tmp_*.py`: the canonical landing was performed by transient CI runners that were deleted within the same branch.

Net effect on `main` is clean and preflight passed on the final head, so this is not a defect. It is a reviewability note: the final diff shows the result, and the mechanism that produced it is reachable only through branch history. It is also the direct reason this retrospective review exists.

---

## 4. Overall judgment

```text
mechanical execution      = SOUND (reproducible, no leakage, all PR claims verified)
theory-side fidelity      = SOUND (P+E faithful to author option B; no live contradiction
                            found at P1-T06, One_Formation or the guarded Individuation note)
authority landing         = INCOMPLETE (one competing chain still ships in bootstrap read #1)
supersession mechanism    = DECLARED BUT UNTRACKED (no per-claim conflict register)
term hygiene              = UNPAID (Bearer homonym across ~480 files, no reading rule)
```

The spine-first order was the right call and the file itself is well built — it is thin, it types its layers, and it keeps OPEN open rather than filling gaps with older theorems. What it has not yet earned is the authority it declares: it says "cite this file first", and the repository's own first-read file still says otherwise. Until F1 and F2 are paid, the spine is canonical by registration but not yet canonical in practice.

## 5. Recommended order

Ahead of the reverse audit queued in `STATUS.md`, because each one changes what that audit finds:

1. **F1** — remove the competing chain in `SRT_AI_START.md §6` (highest leverage, smallest edit).
2. **F11** — add the authority-chain consistency check, so F1/F4/F10 cannot silently recur.
3. **F2** — publish the `Bearer` legacy-reading rule before the reverse audit touches ~480 files carrying the old sense.
4. **F3** — open the per-claim retyping ledger; it is the reverse audit's working surface.
5. **F4, F5, F8, F9** — one small spine/registry correction pass (all are wording-level).
6. **F6, F7, F10** — local-owner retyping and freeze-status decisions.
7. only then continue the old-canonical reverse audit from the spine, in the order `STATUS.md` already records.

## 6. Re-audit closed by this review

These were checked and found sound; a later audit need not repeat them:

- PR body vs. actual diff (all eight claims);
- bundle reproducibility, provenance cleanliness, and `SPINE_BUCKETS` registration;
- COMPACTCORE / domain bundles correctly carry **no** definition source and list the spine under `§0.4 未收录` — no silent authority mismatch there;
- frontmatter legality of the new files;
- absence of temporary-file leakage into `main`;
- P + E fidelity to the author adjudication;
- spine-vs-`P1-T06` consistency;
- the `σ_sr^sub` / T-IND-2 conflict, already guarded by the R1 owner-boundary note.
