# AGENTS.md - SRT Local Workspace

This project keeps its own OpenClaw/ClawX entrypoints.

Use this file as the canonical runtime overlay when the current work is inside this repository, even if sibling projects exist in the same parent workspace.

`CLAUDE.md` is only a compatibility wrapper.
`SRT_AI_START.md` is the AI minimal-theory entry.
`README.md` is the public-facing repo entry.

## Session Start

`AGENTS.md` is the **single authority for fresh-session read order**. Other entry files should point here rather than maintaining competing bootstrap lists.

For a fresh AI session inside this repo, read in this order (3 files):

1. `SRT_AI_START.md` — minimal theory/runtime guard; not a definition authority.
2. `_SRT_AGENT_RETRIEVAL_PROFILE.md` — classify the task before choosing context depth.
3. `STATUS.md §Fast Status` — compact current status; note that the 2026-09-05 author-reentry amendment below supersedes stale bearer-totalizing / direct-to-increment programme wording.

### Current programme expansion — Author Re-entry + Constitution + Domain Reconstruction

For **theory advancement, source-intuition recovery, Constitution work, Core/Core_Law role questions, or a new/revised domain deep-dive**, after the 3-file bootstrap above read:

4. `01_Source_Intuition/SRT_AUTHOR_REENTRY_CORRECTION_2026-09-05.md` — latest explicit author correction on pace, author role and bearer scope.
5. `Governance/SRT_GOV_AUTHOR_REENTRY_ONTOLOGY_RECONSTRUCTION_AMENDMENT_2026-09-05.md` — current sequencing/interpretation authority, including the 2026-09-08 SRT-led collaboration update (§0.3 / §4.2).
6. `Operations/Proposals/SRT_CONSTITUTION_DOMAIN_ARCHITECTURE_V2_2026-09-04.md` — retained post-Constitution architecture, read under the 2026-09-05 amendment.
7. `Operations/Proposals/SRT_CONSTITUTION_DOMAIN_RECONSTRUCTION_BLUEPRINT_2026-08-29.md` — compact historical/identity blueprint.
8. `Operations/Proposals/SRT_CONSTITUTION_DOMAIN_EXECUTION_PLAN_2026-08-29.md` — execution plan as amended by Architecture v2 and the 2026-09-05 governance correction.
9. `Operations/Templates/SRT_DOMAIN_RECONSTRUCTION_FRAMEWORK_TEMPLATE.md` for new/backfilled/revised domain work.
10. `Governance/SRT_GOV_CONSTITUTION_DOMAIN_RECONSTRUCTION_2026-08-29.md`.
11. `Operations/Proposals/SRT_CONSTITUTION_SOURCE_RECOVERY_MAP_2026-08-29.md` when recovering existing SRT intuition rather than answering a narrow factual question.

Current identity guard:

```text
SRT reconstruction
= author-guided reconstruction of an open ontological problem field

SRT Constitution v1
= active reader-interface / perspective-operation prototype
  that opens questions without claiming to exhaust SRT ontology

Bearer / position / participation
= one important SRT ontology/method problem family,
  not the whole ontology

Domain Reconstruction Framework
= author/ontology status × domain starting picture × mature-neighbor adaptation
  × common-problem extraction × Constitution interface × inherited assets/materials
  -> provisional problem-space / candidate SRT response / eventual deep-well queue

Domain Theory / Hypothesis / Model
= mechanisms / formalisms / proxies / candidate explanations

Deep Well / Evidence
= later bounded discrimination / strongest baseline / Case A-B-C / data / proof / archive
  after a bounded author-owned SRT response actually exists
```

Do not restart the older `unified ontology -> local formalization -> D2` sequence as the active programme merely because older proposal files contain it. Also do **not** treat the more recent `bearer-involved perspective framework` shorthand as an exhaustive ontology identity. No replacement final identity is authorized yet.

Until the 2026-09-05 author-reentry hold is explicitly lifted, do not open a third main deep well or infer whole-SRT identity from the two early pilots.

Then load conditionally:

8. `_SRT_INDEX.md` when file routing, domain entrypoints, registry relations, or edit landing zones matter.
9. `_SRT_SYMBOL_TABLE.md` when exact symbol definitions, notation conflicts, or canonical term precision matters.
10. `_SRT_CONTEXT_ROUTER.md` for non-simple conceptual, cross-domain, or deep theory questions.
11. `_SRT_DEEP_THEORY_MAP.md` for cross-domain theory synthesis.
12. `_SRT_PARKED_INDEX.md` when a task touches parked seeds, B-verdict materials, or unmerged proposal work.
13. `Operations/Status_History/` when historical status detail matters.

Read `README.md` when public-facing framing or external onboarding context is useful.

For theory advancement, book writing, domain deep-dives, material fusion, public release, governance work, or any non-trivial SRT answer, classify the task with `_SRT_AGENT_RETRIEVAL_PROFILE.md` before deciding how much context to load. `canonical: false` means "not a definition authority"; it does not mean "do not retrieve."

`Manifesto/SRT_MANIFESTO.md` is a human-first worldview entry (`claim_mode: manifesto`). It is not part of AI session bootstrap; read it only when the task involves user-facing framing or source recovery.

Before doing substantial pipeline / governance / theory work:

- check current `STATUS.md` routing rather than assuming an older pass is still the active entry;
- respect explicit `forward routing`, `supersedes`, `record_stage`, author adjudication and scope over date-only ordering;
- when `STATUS.md` names a conditional handoff/current-priority surface, load it **after** the canonical 3-file bootstrap; that handoff does not become a competing fresh-session read-order authority.

## Research mode discipline

The following runtime mode fields are a **required audit discipline for active bounded theory/audit work packages that actually perform Constitution/ontology/cross-domain synthesis or comparative pressure**. Passive source-intuition records, frozen author gates, status handoffs and simple routing records do not each need to duplicate the five-field block.

For an active bounded work package, record in the existing work package (not a new ledger):

```text
research_mode = U | N
root_question = ...
comparative_claim = none | <bounded claim>
named_comparator = none | <named rival / mapping cases>
n_mode_triggered = false | true
```

Default to `U`. If `research_mode = N`, a bounded comparative claim and named comparator must be present; `neighbor-paid` by itself is not an N-mode trigger.

This is presently a **procedural/audit requirement, not a repository-wide frontmatter schema or CI gate**. The bounded work package and its closure/review are responsible for making compliance inspectable. Do not claim automated enforcement unless a checker is later added.

### Neighbor-paid default route

When a mature neighbor already explains a local mechanism / role and no bounded comparative claim remains active, route:

```text
NEIGHBOR-PAID
-> INHERIT / REALIZATION / REORGANIZATION
-> root question
```

Ask what can be inherited, what relation is reorganized, what cross-domain invariant or new question appears, and what reverse constraint follows. Do not automatically continue residual hunting.

### Residual-hunt circuit breaker

If two consecutive strongest-neighbor/substitution passes on the same root question produce no new gain except:

```text
neighbor-paid -> narrower residual
```

stop automatic narrowing and perform a ChoiceMap/root-return. Continue N-mode only if an explicit bounded comparative claim still requires it; otherwise restore U-mode.

This breaker is auditable from the recorded runtime fields and pass sequence. Until a mechanical checker exists, a closure/review must not describe the breaker as CI-enforced.

## Author Re-entry / ontology dialogue hard rules

- Two models agreeing is corroboration, not proof and not author convergence.
- AI may recover historical SRT, but must not treat the smoothest synthesis of old files as the author's current ontology.
- **When mature-domain overlap, neighbor comparison, or cross-domain mapping is in play, use cross-domain ontological unification (U-mode) rather than domain-local novelty maximization.** Switch to novelty/increment subtraction (N-mode) only when a bounded author-owned SRT response exists and the active task explicitly requires discrimination.
- Do not use novelty/prior-art as a permission gate before the author knows what they mean.
- **Light / bounded Neighbor Awareness** before provisional convergence exists to reduce rediscovery and sharpen the author's problem; it is not a keep/drop gate.
- **Fuller Neighbor Adaptation** after provisional convergence must be allowed to change, narrow or defeat SRT wording. Use `resonance / contrast / pressure / translation / realization` as appropriate.

## Current identity / authority discipline

Use K/A/B/C/D explicitly in high-risk theory work:

```text
K = current canonical constraint
A = current explicit author intuition / adjudication
B = historical / recovered SRT source
C = AI reconstruction / synthesis
D = open pressure / unresolved question
```

A current ontology axis may contain both K and D. Do not silently downgrade K to D because the wider problem field is open.

The current identity-level workflow is:

```text
current author question / intuition
-> canonical/source audit
-> K/A/B/C/D
-> AI divergence
-> bounded mature-neighbor awareness
-> author provisional convergence
-> internal red-team
-> fuller mature-neighbor adaptation / strongest objections
-> common-problem extraction / SRT-led absorption / relational reorganization
-> non-substitutability / structural consequence where a comparative claim exists
-> author second adjudication
-> only then ontology/interface write or conditional domain discrimination
```

AI-generated alternatives are not author decisions. A one-letter author response is adjudication only relative to the complete option set that was actually presented; preserve that option set or a lossless provenance pointer when freezing the gate.

No theory write before author convergence merely because a machine synthesis appears smooth. Same-day status records need explicit control/supersedes/routing and scope; date alone never determines authority.

## Canonical / deep-well guard

Current canonical owners, claim ladder, Pipeline 1 source-fidelity rules and manuscript carve-outs remain binding until separately changed through their own governance path.

No current manifestation/pre-object reconstruction result authorizes:

```text
canonical L0 rewrite by implication;
absolute no-third-person-formalization theorem;
Level-2 claim without a prospective domain-native discriminator;
HOLD exit without the named review conditions;
new deep well solely to protect a positive theory result.
```

For exact registered meanings, continue to follow `CANONICAL_REGISTRY.md`, `Governance/SRT_CLAIM_LADDER.md`, and the relevant `Core_Law/Core` owners.
