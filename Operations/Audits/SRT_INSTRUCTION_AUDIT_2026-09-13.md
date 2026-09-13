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

# Project instruction audit — GPT-6 Astra

## Scope and basis

User-requested audit and optimization of repository instructions, based on the retrieved [GPT-6 Astra official model guide](https://developers.openai.com/api/docs/guides/latest-model?model=gpt-6-astra), accessed 2026-09-13. Its applicable advice is to remove conflicting instruction layers, carry authorized work through, distinguish skill defaults from user intent, calibrate formatting and verification, and use delegation where useful.

Baseline: `0d17abd40eabd224c526dd340bb3d5a54e913d73`. Scope: AGENTS, CLAUDE, AI/retrieval/tool entrypoints, four repository Codex skills, five tracked Claude skills, relevant references, the article workflow and affected context-bundle generation. Personal/global installations and ignored local runtime files were not edited. No model/API/configuration migration, canonical theory edit, commit, push or publication was performed.

## Findings and disposition

| Finding | Change |
|---|---|
| Competing bootstrap and authority summaries | AGENTS owns bootstrap; CLAUDE becomes a pointer; Registry §C and generative spine remain the authority route. Conditional source loading replaces repeated general read lists. |
| Review treated as material writeback | srt-material separates read-only appraisal from explicit Pipeline 1 integration. |
| Read-only pre-audit creates files and advances automatically | srt-structure-extraction keeps read-only requests in review; explicit extraction retains pre-audit/adjudication gates. Routine repairs use edit protocol. |
| Repeated approval despite existing scope | Mechanical edits and accepted decisions reuse authorization; missing substantive decisions still go to the author. |
| Old article prompts applied to all work | Article-specific author convergence remains; direct drafting, language editing and calibration use the user's actual task. Old novelty gate and incorrect P-level shorthand corrected. |
| Retired quick-symbol path and outdated runtime root | Skill routes to AI_START §7 / symbol table; helpers run from the repository root. |
| Blanket bans on adverbs, passives, triples, contrasts and dashes | Contextual style checks preserve logical scope, technical subjects and substantive categories. |
| Examples add data, experience, provenance or completion | Replaced with faithful examples or explicit synthetic supplied context. Removed unsupported statistical thresholds. |
| Bounded example deletes pending sentences | Pending deletions remain in the draft; existing deletion authorization is respected across skill and references. |
| Pipeline loads every reference and enforces bulky output | Sequential three-stage purpose remains; references and report detail become conditional. |
| Global and project skill copies can conflict | Prefer the project-local copy unless the user explicitly selects another path. |

Business guards retained: no invented author convergence; author source fidelity; current Registry/spine owners; freeze/edit protocol; U/N-mode and scoped comparison; third-well and broad-synthesis HOLD gates; book status → manifest → active primary before archive; public/submitted manuscript carve-outs; evidence/claim boundaries; no publication or unrelated external mutation implied by an editing skill.

AGENTS: 235 → 100 lines. Nine skill entrypoints: 36,731 → 13,598 characters (63.0% reduction). Counts concern entrypoints, not all supporting references. Upstream licenses and existing skill invocation metadata remain.

## Verification

- Four Codex skills passed skill-creator quick_validate.
- All nine skill frontmatter/name/description checks passed. Claude `argument-hint` retained under its platform schema rather than removed to fit the Codex-only validator.
- All 23 relative Markdown links in the skill trees resolved, including the new humanizer patterns reference.
- git diff --check and authority-routing consistency passed.
- Context bundles regenerated from changed sources; freshness verified all nine generated package files byte-for-byte. Builder regression tests passed.
- Complete governance preflight on a detached, clean baseline: failures=0.
- Complete governance preflight with the scoped tracked patch and new skill reference applied to that clean worktree: failures=0; frontmatter new warnings=0.
- After incorporating remote main `2d3d9e47`, clean-worktree governance preflight with `--strict-split-metadata` passed (failures=0), as did PR-local frontmatter, baseline monotonicity (added=0), all nine context-package freshness checks and diff whitespace checks.
- Original local worktree preflight: failures=1 in frontmatter. Its new warnings concern pre-existing ignored local files: exports, virtualenv/cache documentation and local runtime overlays. No warning-baseline expansion or unrelated cleanup was made.
- Existing report-only NODE-BOOK-BACKFLOW warning remains. Editing the five tracked .claude skill files also produces nonblocking local-noise warnings; the checker reports errors=0.
- Independent read-only audit covered 14 original references and five Claude skill entrypoints, and its high-confidence findings were addressed.
- A second independent scenario exercise could not run because the subagent hit an account usage limit. It is not counted as passed; no usage reset was consumed.

Manual contract walkthrough (not an independent runtime test): source reading and standalone pre-audit stay read-only; explicit material integration enters Pipeline 1; link fixes and approved option-A organization proceed without new author adjudication; missing deep-well release remains a real gate; authorized empty-sentence removal preserves numbers and “可能”; review-only requests do not produce rewritten prose; calibration requests use the already permitted exception.

## Remaining scope

At audit completion the patch was local and uncommitted on main. The author subsequently requested a PR: the scoped patch is committed on `codex/astra-instruction-audit-20260913`, with remote main through `2d3d9e47` incorporated. Generated context-package conflicts were resolved by regeneration from the merged sources. Local ignored and unrelated untracked artifacts remain intact and outside the PR. PR creation does not authorize merging it. This report records instruction engineering, not a new SRT theory or author decision.
