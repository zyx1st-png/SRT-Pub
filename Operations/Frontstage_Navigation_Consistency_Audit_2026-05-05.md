---
id: SRT-OPS-FRONTSTAGE-NAV-AUDIT-2026-05-05
type: audit
status: draft_v1
layer: operations
claim_mode: audit
canonical: false
---

# Frontstage Navigation Consistency Audit · 2026-05-05

## Scope

This audit checks navigation consistency and claim-status hygiene across the current frontstage entry files, public release files, and external convergence files. It does not modify theory, evaluate whether SRT is correct, accept evidence cards, or alter canonical anchors.

Audited files:

- [`../README.md`](../README.md)
- [`../START_HERE.md`](../START_HERE.md)
- [`../SRT_Quick_Start.md`](../SRT_Quick_Start.md)
- [`../05_Public_Release/SRT_IN_ONE_PAGE.md`](../05_Public_Release/SRT_IN_ONE_PAGE.md)
- [`../05_Public_Release/PUBLIC_INDEX.md`](../05_Public_Release/PUBLIC_INDEX.md)
- [`../04_External_Convergence/README.md`](../04_External_Convergence/README.md)
- [`../04_External_Convergence/EVIDENCE_INDEX.md`](../04_External_Convergence/EVIDENCE_INDEX.md)
- [`../04_External_Convergence/REVIEW_MAP.md`](../04_External_Convergence/REVIEW_MAP.md)
- [`../04_External_Convergence/CONTRADICTION_LEDGER.md`](../04_External_Convergence/CONTRADICTION_LEDGER.md)

## Summary

- Frontstage path is coherent.
- Public entry remains separated from canonical anchors.
- External convergence remains draft / not accepted.
- Governance remains downstream.
- One minor stale-note issue remains in `05_Public_Release/PUBLIC_INDEX.md`: it still says `SRT_Quick_Start.md` may be too governance-heavy and should be rewritten later, even though the quick-start file has already been rewritten.

## Checks

| Check | Result | Notes |
|---|---|---|
| README first screen still starts from founding reversal, not governance. | Pass | `README.md` opens with the founding reversal before formal, governance, or operations links. |
| START_HERE first-time / public reader paths do not route ordinary readers into AGENTS / Governance / Operations. | Pass | First-time and public reader paths route through `README.md`, `SRT_IN_ONE_PAGE.md`, `CORE_REVERSALS.md`, public guardrails, and quick start. Agent / collaborator paths are explicitly separate. |
| SRT_Quick_Start starts from founding reversal and does not present itself as canonical. | Pass | The file opens with the founding reversal and states it is a public-facing map, not a canonical definition source. |
| SRT_IN_ONE_PAGE is public_summary / canonical false and linked from public paths. | Pass | Frontmatter has `type: public_summary`, `claim_mode: public_summary`, and `canonical: false`; it is linked from `README.md`, `START_HERE.md`, and `PUBLIC_INDEX.md`. |
| 05_Public_Release/PUBLIC_INDEX links to SRT_IN_ONE_PAGE. | Pass | The one-page summary is listed under "One-page summaries." |
| EVIDENCE_INDEX marks all cards as draft_v1; not accepted. | Pass | All three listed cards are `E2`, `draft_v1; not accepted`. |
| REVIEW_MAP does not mark cards accepted. | Pass | It repeats `draft_v1; not accepted` and says no card is accepted unless `EVIDENCE_INDEX.md` explicitly marks it accepted. |
| Every evidence card listed in EVIDENCE_INDEX has or is waiting for a pressure link. | Pass | All three current cards have concrete pressure ledger links. No `pending ledger review` entries remain. |
| Existing pressure links resolve to CONTRADICTION_LEDGER anchors. | Pass | `CL-IG-FISHER-GENERIC-DIFFICULTY`, `CL-THERMO-LANDAUER-OVEREXTENSION`, and `CL-AI-FUNCTIONALIST-STAKE-CHALLENGE` exist as ledger headings. |
| No positive "proves / verifies / confirms SRT" language appears in public or external convergence entry files. | Pass | Search found only negated or guardrail contexts, such as "does not claim" or "should not be read as." |
| Governance / Operations remain downstream, not first public entry. | Pass | They appear after reader paths and are framed as maintenance / collaborator layers. |
| No canonical files were modified by this audit. | Pass | This audit PR adds only this operations audit file. |

## Findings

### Must-fix

No must-fix items found.

### Should-fix

- `05_Public_Release/PUBLIC_INDEX.md` still contains a stale note saying `SRT_Quick_Start.md` may be too governance-heavy and should be rewritten in a later pass. Since `SRT_Quick_Start.md` has already been rewritten, a later navigation-cleanup PR should replace that note with a current description.

### Watchlist

- Consider adding [`../04_External_Convergence/REVIEW_MAP.md`](../04_External_Convergence/REVIEW_MAP.md) to the external evidence reader path in `START_HERE.md` after it has settled through one or two more evidence-card cycles.
- Before any evidence card is promoted beyond draft, require a separate acceptance review that checks the pressure ledger, boundary language, source quality, and operational-proxy status.
- Public-facing routes should continue to avoid routing first-time readers into agent, governance, or operations materials.

### No action needed

- The root `README.md` first screen is still theory-first rather than governance-first.
- Public one-page and quick-start materials remain non-canonical.
- External convergence cards remain draft and pressure-linked.
- The review map accurately summarizes draft card status without accepting evidence.

## Link / Claim Status Map

| File | Role | Claim Mode | Canonical? | Notes |
|---|---|---|---|---|
| [`../README.md`](../README.md) | Public-facing repository entry | navigation / public framing | No | Opens with founding reversal; governance and operations are downstream. |
| [`../START_HERE.md`](../START_HERE.md) | Reader navigator | navigation | No | Separates ordinary reader paths from agent / collaborator paths. |
| [`../SRT_Quick_Start.md`](../SRT_Quick_Start.md) | Beginner quick start | public guide | No | States it is not a canonical definition source and points to formal anchors later. |
| [`../05_Public_Release/SRT_IN_ONE_PAGE.md`](../05_Public_Release/SRT_IN_ONE_PAGE.md) | Public one-page summary | public_summary | No | Frontmatter explicitly says `canonical: false`. |
| [`../04_External_Convergence/EVIDENCE_INDEX.md`](../04_External_Convergence/EVIDENCE_INDEX.md) | Evidence-card index | navigation | No | Lists cards as `draft_v1; not accepted` and links pressure entries. |
| [`../04_External_Convergence/REVIEW_MAP.md`](../04_External_Convergence/REVIEW_MAP.md) | Draft-card review map | navigation | No | Summarizes draft cards and next steps; not an acceptance decision. |
| [`../04_External_Convergence/CONTRADICTION_LEDGER.md`](../04_External_Convergence/CONTRADICTION_LEDGER.md) | Pressure / contradiction ledger | ledger | No | Records downgrade pressure and anti-confirmation-bias checks. |

## Recommendations

- Later: run a periodic link check over `README.md`, `START_HERE.md`, public release files, and external convergence files.
- Later: update the stale `SRT_Quick_Start.md` note in `05_Public_Release/PUBLIC_INDEX.md`.
- Later: define an accepted-evidence policy before any card can move beyond draft.
- Later: review quick-start and public one-page tone after the next public-materials pass.
- Later: consider adding `REVIEW_MAP.md` to the external evidence path in `START_HERE.md` once the review-map pattern stabilizes.

## Non-Actions

- No canonical changes.
- No file moves.
- No evidence cards.
- No accepted status changes.
- No `AGENTS.md` changes.
- No `Governance/` changes.
- No edits to public entry files or external convergence entry files.

