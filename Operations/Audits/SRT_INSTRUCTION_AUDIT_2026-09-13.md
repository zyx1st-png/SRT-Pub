---
id: SRT-INSTRUCTION-AUDIT-2026-09-13
type: audit_report
status: active
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
date: 2026-09-13
---

# Project instruction audit — cross-model, Astra-informed

## Scope and basis

User-requested audit and optimization of repository instructions. GPT-6 Astra's official model guide was one input because it recommends removing conflicting instruction layers, carrying authorized work through, distinguishing skill defaults from user intent, calibrating verification and using delegation where useful. The landing criterion is **not Astra-specific brevity**: the repository must remain reliable across GPT-5.6-class models, GPT-6 Astra and Claude/Claude Code. Critical ordered workflows therefore retain explicit sequence, stop conditions, failure handling and edit boundaries; only duplicate explanation and stale routing are candidates for compression.

Baseline: `0d17abd40eabd224c526dd340bb3d5a54e913d73`. Scope: AGENTS, CLAUDE, AI/retrieval/tool entrypoints, four repository Codex skills, five tracked Claude skills, relevant references, the article workflow and affected context-bundle generation. Personal/global installations and ignored local runtime files were not edited. No model/API/configuration migration or canonical theory edit is part of this instruction audit.

## Findings and disposition

| Finding | Change |
|---|---|
| Competing bootstrap and authority summaries | AGENTS owns bootstrap; CLAUDE becomes a compatibility pointer; Registry §C and generative spine remain the authority route. Conditional source loading replaces repeated general read lists. |
| STATUS theory/history debt leaked into universal bootstrap | Retrieval contract narrows fresh-session STATUS consumption to §0–§2; later STATUS theory/history sections are task-conditional. |
| Old programme files behaved like a second theory bootstrap | Theory Advancement now starts from live STATUS route, latest relevant author adjudication/work package, Registry, Spine and local owner; 2026-09-05 programme layers are conditional when their programme scope is actually in play. |
| Review treated as material writeback | srt-material separates read-only appraisal from explicit Pipeline 1 integration. |
| Read-only pre-audit creates files and advances automatically | srt-structure-extraction keeps read-only requests in review; explicit extraction retains pre-audit/adjudication gates. Routine repairs use edit protocol. |
| Repeated approval despite existing scope | Mechanical edits and accepted decisions reuse authorization; missing substantive decisions still go to the author. |
| Compression risked deleting execution semantics | Cross-model retention rule added to retrieval/Claude routing; `srt-safe-patch` restores explicit locate → unique-anchor → semantic-boundary → preserve → verify → failure-handling steps. |
| Old article prompts applied to all work | Article-specific author convergence remains; direct drafting, language editing and calibration use the user's actual task. Old novelty gate and incorrect P-level shorthand corrected. |
| Retired quick-symbol path and outdated runtime root | Skill routes to AI_START §7 / symbol table; helpers run from the repository root. |
| Blanket bans on adverbs, passives, triples, contrasts and dashes | Contextual style checks preserve logical scope, technical subjects and substantive categories. |
| Examples add data, experience, provenance or completion | Replaced with faithful examples or explicit synthetic supplied context. Removed unsupported statistical thresholds. |
| Bounded example deletes pending sentences | Pending deletions remain in the draft; existing deletion authorization is respected across skill and references. |
| Pipeline loads every reference and enforces bulky output | Sequential purpose remains; references and report detail become conditional. |
| Global and project skill copies can conflict | Prefer the project-local copy unless the user explicitly selects another path. |

Business guards retained: no invented author convergence; author source fidelity; current Registry/spine owners; freeze/edit protocol; U/N-mode and scoped comparison; third-well and broad-synthesis HOLD gates; book status → manifest → active primary before archive; public/submitted manuscript carve-outs; evidence/claim boundaries; no publication or unrelated external mutation implied by an editing skill.

The reduction ratio is descriptive, not a quality target. A shorter entrypoint is accepted only when the deleted material is duplicated, stale, example-only or delegated to an owning reference; ordered gates and stop/failure semantics remain explicit where model inference would be unsafe.

## Cross-model semantic-retention pass

The heavily compressed skill entrypoints were rechecked with three buckets:

```text
A = invariant remains explicit in the skill
B = invariant is explicitly delegated to a mandatory owner/reference
C = invariant disappeared and would have to be reconstructed by model capability
```

Merge criterion: critical execution semantics may be A or B, not C. The second pass identified `srt-safe-patch` as the main C-risk and restored its mechanical contract. `srt-structure-extraction` already retains its three ordered stages plus high-risk adjudication stop; `srt-material` delegates exact gates to Pipeline 1 while retaining read-only/writeback separation; `srt-article` retains author-choice boundaries; `srt-canonical-answer` retains Registry/Spine/claim/Open routing.

`CLAUDE.md` remains intentionally short: Claude-specific reliability comes from the shared retrieval profile and explicit owning skill/workflow contracts, not from duplicating a second governance stack.

## Verification

- Four Codex skills passed skill-creator quick_validate in the original audit pass.
- All nine skill frontmatter/name/description checks passed in the original audit pass. Claude `argument-hint` retained under its platform schema rather than removed to fit the Codex-only validator.
- All 23 relative Markdown links in the skill trees resolved, including the new humanizer patterns reference.
- git diff --check and authority-routing consistency passed before the cross-model follow-up.
- Context bundles were regenerated from changed sources; freshness verified all nine generated package files byte-for-byte in the original pass. Builder regression tests passed.
- Complete governance preflight on a detached, clean baseline passed; after incorporating remote main `2d3d9e47`, clean-worktree governance preflight with `--strict-split-metadata` also passed.
- Existing report-only NODE-BOOK-BACKFLOW warning remains. No warning-baseline expansion or unrelated cleanup was made.
- Independent read-only audit covered 14 original references and five Claude skill entrypoints, and its high-confidence findings were addressed.
- A second independent scenario exercise could not run because the subagent hit an account usage limit. It is not counted as passed.

Manual contract walkthrough: source reading and standalone pre-audit stay read-only; explicit material integration enters Pipeline 1; link fixes and accepted mechanical organization proceed without new substantive adjudication; missing deep-well release remains a real gate; review-only requests do not produce rewritten prose; current bounded owner work routes to live adjudication/owner before older programme context; local patch failure cannot be bypassed with a whole-file rewrite.

## Remaining scope

The instruction optimization is intended to close as a bounded workstream after this PR. Future changes should be maintenance driven by observed routing failures, stale paths or changed programme ownership rather than continued prompt minimization. This report records instruction engineering, not a new SRT theory or author decision.
