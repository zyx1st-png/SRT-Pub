---
id: SRT-NEURO-H3-120-AI-REVIEW-RESEARCHER-AUTHORITY-20261025
type: proposal
status: draft
layer: operations
epistemic_layer: experimental
claim_mode: proposal
canonical: false
ai_do_not_use_for_definition: true
date: 2026-10-25
scope: H3-120-only prospective review-governance decision; not a method, resource, or execution authorization
dependency:
  - Experiments/neuro_sleep_null_calibration/G0_CANONICAL_Q_ORDER_PROSPECTIVE_AMENDMENT_DRAFT_2026-10-23.md
  - Experiments/neuro_sleep_null_calibration/NC0A_RESEARCHER_AUTHORIZED_EXECUTION_AMENDMENT_V1_2026-10-18.md
tags: [Neuroscience, RIKEN, H3, ResearcherAuthority, AIReview, Draft]
---

# H3-120 bounded AI technical review and researcher-accountable decision route — proposal

**DRAFT / NOT EFFECTIVE.** This document proposes **one H3-120-specific prospective change to review evidence and responsibility**. It does not itself settle the current #1128 requirement for a non-author independent methods/resource confirmation, does not activate `CANONICAL_SORTED_EDGE_V1`, and does not authorize a real H3 run. The researcher's separate approval of scientific method and H3 stop limits on 2026-10-25 **must not be interpreted as an approval of this governance change**. An explicit, dated researcher adoption of this route is still needed.

## Problem, precedent and precise exception

- #1128 currently calls for non-author independent confirmation of methods and H3 stop limits. The recorded researcher method and resource decisions are [#1128](https://github.com/zyx1st-png/SRT-Pub/pull/1128#issuecomment-6392797650) and [#1130](https://github.com/zyx1st-png/SRT-Pub/pull/1130#issuecomment-6392797999).
- The existing `NC0A_RESEARCHER_AUTHORIZED_EXECUTION_AMENDMENT_V1_2026-10-18.md` **proposes**, for the *synthetic NC-0a route only*, independent scientific scrutiny with researcher-owned execution responsibility instead of third-party execution cryptographic signatures. That NC-0a document is itself a draft; it is **neither operative H3 authority nor proof a similar route has been accepted**.
- H3-120 is a bounded **real biological-source** graph-reproduction/algorithm-comparability check; unlike NC-0a it accesses private RIKEN source data. No G0 biological null, new population-level inference or T1 is authorized by this proposal.
- The candidate exception, **only if the researcher explicitly adopts this H3-specific governance amendment before activation**, is: a clearly attributed, separately performed AI-model technical review may satisfy the H3 requirement for **independent technical scrutiny**, without pretending that the separate AI run is an external human reviewer or an independently authenticated non-author GitHub signature. The researcher assumes the decision and execution risks personally. Where the existing wording unambiguously requires an actual non-author human approval, this route **replaces that requirement prospectively for this one H3 panel** rather than claiming to have satisfied it retroactively.

## Review evidence and candid provenance

The user supplied a separate-session Claude Opus 5.5 review dated 2026-10-25 of #1128 HEAD `577cfde1000090c1325419417aa5b2c83325a3a2` and #1130 HEAD `fb8d43246e870ded38c22975d8913575d36818fe`. Its reported disposition was **APPROVE — H3-120 technical/resource scope only**, with non-blocking recommendations. The repository owner transcribed qualified records on [#1128](https://github.com/zyx1st-png/SRT-Pub/pull/1128#issuecomment-6398373104) and [#1130](https://github.com/zyx1st-png/SRT-Pub/pull/1130#issuecomment-6398373478).

This is **AI-assisted independent analysis conducted in a separate session, relayed by the researcher**. The GitHub posting account is the author; no other GitHub account submitted a formal review. A relay does not independently authenticate who operated the AI, the unabridged session or its 20 reported synthetic tests, and **does not equal external human peer review**. These limitations must be carried into the effective record. Only a complete, identifiable review report with the stated tested revisions, model, review scope, verdict, concrete blockers and limitations may count as AI technical scrutiny; anonymous approval, the author's self-review and a bare `APPROVE` label cannot.

### Scientific interpretation not waived

- Shared `CANONICAL_SORTED_EDGE_V1` ordering addresses the observed/null **input representation mismatch**; synthetic label/order checks do not prove graph-general unbiasedness, eliminate finite-seed/order sensitivity or make `Qmax_200` a global optimum.
- Historical PS-A remains frozen. For H3, preserve all 120 preselected source/state/N identities, historical replay before canonical replay, two full 200-seed Q vectors, original-neuron identity and graph/seed/runtime hashes. Historical trial absolute tolerance is `1e-10`, Qmax absolute tolerance `1e-6`, and first-max trial index must match exactly.
- Canonical-vs-historical differences are **descriptive**, not a threshold for retuning method, seeds, order, sampling, or stopping conditions after viewing H3 output. Identity or historical-Q failure stops the panel.
- H3 checks source integrity and algorithm compatibility, **not** G0 null inference or scientific support for SRT ontology. The G0/T1 resource decisions, inference thresholds and `MIXING-UNRESOLVED` remain unchanged.

## Stop-loss and independent failure controls remain

The researcher-approved **H3-only** envelope is: **8h elapsed wall time, 8 process-tree CPU-hours, one worker, 4 GiB sampled aggregate RSS (not an OS hard memory cap), 1 GiB run output**. Retain 40 GiB Data/VM launch-floor and 30 GiB reserve checks, sampled host memory pressure, Swap growth, AC power, thermal state, active sleep prevention, host-wide lock, process-group Watchdog stop, verified append-only hash-chain evidence, fail-stop identity/Q rules, no automatic resume and no outcome-directed retry. These are **loss limits, not completion forecasts**. The single-recording 10-graph pilot cannot bound time or RAM for all six source recordings. Source loading materializes the requested frame window across all source neurons before selecting N, so the memory cost need not depend on N alone.

Human-executed approval and actual private-data access remain under the researcher's responsibility. An AI review does not certify privacy clearance, source-use permission, host security, or tamper-proof independent custody. The existing private source/hash controls must remain.

## Steps that would make this prospective route effective

1. **Separate governance choice:** The researcher explicitly approves or rejects **this H3-specific review-standard change**, with a dated record referencing the exact draft commit/content and acknowledging the absence of independently authenticated non-author/human sign-off. The prior method/resource “批准” is not this decision. A rejection leaves #1128's original confirmation requirement in force.
2. **Document source of review:** Preserve the Claude review scope, date, model, complete text and public relay links. Address any material objection before adoption; none may be labeled solved merely by model agreement. If future edits change the science/budget/critical safety behavior, perform new scoped technical review against the changed parts. Mechanical rebases, manifest-status/hash pinning, and tests should be independently checked but need not trigger another full scientific review.
3. **Dated scientific activation:** After the route is adopted and review issues resolved, enter a **distinct effective-dated #1128 method decision** identifying the adopted review route, historical-PS-A boundary and the `Qmax_200` limits; update `status: draft` to exactly `status: active` and remove contradictory draft text. The **method file hash is computed after activation**. Do not preemptively change it.
4. **H3 code/packet synchronization:** Bring #1130 onto the final #1128 base, update the packet's draft method state and fixed hash checks without changing the frozen 120 identities or the 48,000 gross trials. Test on the frozen macOS arm64 / Python 3.14 runtime, rerun relevant synthetic supervisor/authorization tests and pin a clean HEAD, method/packet/source/runtime hashes.
5. **Run-specific authorization remains separate:** After final version pinning, create one new UUID and private path, perform immediately current resource/host preflight for that run and secure the explicit run-specific researcher confirmation bound to UUID, final HEAD, effective method SHA-256, packet SHA-256, source manifest SHA-256 and approved envelope. The real launcher must fail closed on a mismatch. Do not run by merely setting `active` or posting an AI review.

## Exclusions and non-authorizations

- This amendment **does not** modify historic PS-A, the 10-graph pilot, NC-0a's own governance, G0 nulls, T1, or G0/T1 `RESOURCE NO-GO`. G0's 4,900 observed canonical graphs / 980,000 Q trials remain a **separately resourced phase**; neither its execution nor its resource gate is approved here.
- It does not waive future external human review required for publication or other projects, turn GitHub owner relay into a verified independent review signature, or guarantee that an AI review is impartial.
- Until a distinct researcher adoption of this **governance** route exists, status remains `draft`; no execution, formal UUID/commitment, method activation, or packet activation may be inferred from this proposal.
