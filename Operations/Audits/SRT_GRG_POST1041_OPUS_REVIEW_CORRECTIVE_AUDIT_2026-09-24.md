---
id: SRT-GRG-POST1041-OPUS-REVIEW-CORRECTIVE-AUDIT-20260924
type: audit
status: draft
date: 2026-09-24
layer: operations
epistemic_layer: os
claim_mode: evidence
canonical: false
research_mode: U
dependency:
  - STATUS.md
  - AGENTS.md
  - Operations/Audits/SRT_GRG_DIALOGUE_TO_REPOSITORY_FIDELITY_AUDIT_2026-09-23.md
  - Operations/Proposals/SRT_GRG_FUSION_CASE_CARD_ITERATION_PLAN_2026-09-23.md
  - Operations/Handoffs/SRT_GRG_DIALOGUE_RECOVERY_CURRENT_NEXT_HANDOFF_2026-09-24.md
tags: [GRG, Audit, Post1041, OpusReview, Continuity, Handoff, StopLoss]
---

# Post-#1041 corrective audit after independent Opus review — 2026-09-24

## 0. Scope

#1041 was merged as commit:

`2a29a5463d8afc0fc181c874fd5f22a403519484`.

The independent review supplied by the author was performed against the earlier #1041 head `a32a7d20`, before the later accepted-machine-analysis retrieval fixes were added.

Therefore this audit separates:

- review findings already addressed by the final #1041 head;
- findings that remained valid after merge;
- corrective actions in this follow-up.

This is a governance / routing / method-cleanup audit.

It does not create GRG v0.4 or a new theory layer.

## 1. Blocking finding B1 — recovery route not reachable from STATUS

Review verdict: VALID after #1041 merge.

Observed state after #1041:

```text
STATUS CURRENT NEXT
= bounded latent-reconstructive-reach reality pressure-test / operationalization

recovery handoff
= separately says first task is #1039 audit
```

That created a practical two-next ambiguity.

Correction:

- keep the STATUS next unchanged;
- define the evolution/popgen recovery audit as the **first bounded instance of the existing CURRENT NEXT**;
- add a merged handoff under `Operations/Handoffs/`;
- no third fusion domain until this bounded instance and §8.1 accounting close.

Current active handoff:

`Operations/Handoffs/SRT_GRG_DIALOGUE_RECOVERY_CURRENT_NEXT_HANDOFF_2026-09-24.md`.

Disposition:

`B1 = FIXED IN FOLLOW-UP`.

## 2. Blocking finding B2 — wrong handoff chronology

Review verdict: VALID.

Verified repository history:

```text
09:17 UTC — 7cd5c00cd
  pre-review handoff names Selection / reach / neutrality /
  retention / higher-order-formation pressure targets.

09:52 UTC
  #1039 created.

10:03 UTC — 652e484ca
  STATUS reconciliation restored;
  stop-loss added;
  evolution terms downgraded to reading hints.

11:04 UTC
  #1037 merged with corrected handoff.
```

Therefore the correct causal statement is:

> #1039 started from stale pre-review prompt text before the reviewed correction landed.

The incorrect statement:

> the handoff that merged with #1037 still preloaded those targets

is withdrawn.

Repository lesson:

> fresh-session execution must derive from merged `main`; chat-copied / unmerged handoff text is provenance only.

Disposition:

`B2 = FIXED IN FOLLOW-UP`.

## 3. Blocking finding B3 — stop-loss was omitted / effectively reset

Review verdict: VALID AS A WARNING; formal two-case trigger NOT YET CLEANLY PAID.

Plan §8.1 requires source-native adequacy to be declared **before** interpreting / scoring the case outcome.

Verified accounting:

### FRR

```text
adequate = declared
result <= M1
target-domain GRG gain = NO
count = adequate case 1
```

### Existing evolution draft

The source note contains:

`ADEQUATE FOR DISCOVERY RECONSTRUCTION`

but this appears after substantial analysis, candidate formation and absorption discussion.

Therefore:

```text
prospective pre-score adequacy declaration
= NOT ESTABLISHED

retroactive adequate-case count
= NOT ALLOWED
```

So evolution cannot be counted after the fact as formal adequate case 2 merely to trigger §8.1.

However its weak / absorbed-leaning result creates a genuine stop-loss warning.

Correction:

> #1041 is classified as a root-question review prompted by that warning, not as a reset of the counter.

No third domain opens until the current-next audit closes.

Disposition:

`B3 = FIXED / FORMAL COUNT PRESERVED`.

## 4. M1 — author authorization vs machine implementation

Review verdict: VALID.

The author directly authorized the recovery direction and instructed execution.

That does not make all implementation wording A1.

Correction:

- author quotations remain A0-Q;
- §§3–§7 of the recovery adjudication are explicitly M-level implementation / reconstruction unless separately supported;
- `probe + explanandum` remains an **M-level operational method rule under the author-approved recovery direction**;
- architecture wording no longer says the recovery “established” that burden as author-level theory.

Disposition:

`M1 = FIXED`.

## 5. M2 — existing content under-credited as missing

Review verdict: VALID.

Corrections:

- GRG as higher-order coarse-graining / self-revising grammar was already explicit in prior Card / v0.3 / #1040 / start surfaces;
- anti-self-sealing / “what would force this equivalence to fail?” was already present;
- the actual missing burden is narrower:
  - route these items reliably;
  - reconstruct relevant GRG cuts **before** new-candidate naming;
  - add existing-owner overlap before new naming.

The fidelity audit now retypes these as `PRESERVED / MISROUTED` where appropriate rather than inventing them as missing.

Disposition:

`M2 = FIXED`.

## 6. M2 / M5 — redundant continuity_role axis

Review verdict: VALID, strengthened by the author's later preference that accepted machine analysis should be load-bearing by default.

Correction:

- remove the new repository-wide `continuity_role` concept from active recovery logic;
- reuse the existing `retrieval value` axis in `_SRT_AGENT_RETRIEVAL_PROFILE.md`;
- author-accepted, non-superseded machine analysis has required retrieval value for continuation by default;
- authority remains independently A0-Q / A0-P / A1 / M.

No new load-bearing tag is required.

Disposition:

`M2/M5 = FIXED`.

## 7. M3 — vocabulary collisions / inconsistent disposition lists

Review verdict: VALID.

Corrections:

### Removed generic disposition uses

- `CALIBRATION`;
- `OPERATIONALIZATION`;
- `SOURCE_REALIZATION`;
- `DECOMPOSITION` as a competing programme result label.

### Unified owner-overlap result vocabulary

```text
INHERIT
REALIZATION
REORGANIZATION
NO_GRG_GAIN
RESIDUAL_CANDIDATE
```

Definitions are carried in the active handoff / protocol / v0.2 record.

### Separate GRG-cut action vocabulary

```text
RETAIN
SPLIT
MERGE
DEMOTE
DELETE
SOURCE_LOCAL
INSUFFICIENT_EVIDENCE
```

### Removed new L1–L4 labels

Writeback surfaces are now named descriptively:

- direct author events;
- visible analytical derivation;
- execution artifact;
- handoff.

Disposition:

`M3 = FIXED`.

## 8. M4 — GRG vocabulary used to describe an operational prompt failure

Review verdict: VALID.

The earlier recovery text described the stale prompt using GRG `proxy / reach / objectification / reconstructibility` language.

That is unnecessary and risks turning an ordinary workflow failure into evidence for GRG vocabulary.

Correction:

Use plain operational language:

```text
stale pre-review prompt
instruction anchoring
review landed after session start
merged-main route not used
```

Generative reconstructibility remains distinct from repository / dialogue recoverability.

Disposition:

`M4 = FIXED`.

## 9. M6 — oversized handoff

Review verdict: VALID.

The archived proposal-side handoff listed roughly twelve body files before target inspection.

Correction:

Active handoff uses:

- two navigation surfaces: AGENTS + STATUS;
- at most six body files in first pass;
- #1039 Card / reconciliation are deferred until the first-pass owner-overlap result requires them.

The old proposal-side handoff is archived and explicitly non-executable.

Disposition:

`M6 = FIXED STATICALLY`.

### Dynamic-probe limitation

No independent fresh-session model run was available inside this repository-editing execution.

Therefore:

```text
static route / budget audit = PASS
independent fresh-session behavioral probe = NOT RUN
```

Do not claim dynamic validation from static inspection.

## 10. External dialogue export identity

The recovery master refers to the author's full conversation export.

Verified external file identity:

```text
filename:
  粘贴的 markdown (1)。md(20260923-150146)

size_bytes:
  571076

sha256:
  551a3bf023691c7d667562c5000cfbb916ce8684e987e2bf85d1fbd1a0b320e9

repository-resident copy:
  NO
```

This is enough to verify the same author-held export later, but not enough to make the repository self-contained.

That limitation remains explicit.

## 11. Template / handoff minor findings

### v0.2 template duplication

v0.1 is now explicitly frozen #1040 provenance.

v0.2 is the resumed-discovery template.

They are not intended as two synchronized active templates.

### GRG lens ordering

The `current GRG lens motivating this inquiry` field was removed from template §0 and moved to the later lens / projection audit after source-native reconstruction.

### Handoff location

Active handoff now lives under:

`Operations/Handoffs/`.

The proposal-side handoff is archived provenance.

## 12. #1039 owner-overlap audit completeness

The active handoff now requires comparison against:

- capacity / availability / accessibility / actualisation;
- active / latent reconstructive reach;
- reach allocation / suppression / recovery / reorganization;
- reach record §R genuine vs supported / subsidized equivalence;
- v0.3 transformation / composition patterns;
- mature canalization / developmental buffering / CGV / Hsp90 capacitance source baseline;
- Rutherford & Lindquist (1998), already present in #1039 source material.

Hsp90 / CGV cannot be reused as held-out confirmation for a candidate they helped generate.

## 13. Current decisions

### Decision 1 — #1039 recovery audit routing

`A`.

It is the first bounded instance of the existing STATUS current-next route.

It is not a second next.

### Decision 2 — stop-loss

Formal §8.1 two-case trigger:

`NOT CLEANLY TRIGGERED`

because the evolution adequacy declaration was not prospectively established before scoring.

Programme response:

`ROOT-QUESTION REVIEW ALREADY WARRANTED BY WARNING / THIRD DOMAIN HOLD`.

### Decision 3 — probe + explanandum

`M-LEVEL OPERATIONAL HARD GATE UNDER AUTHOR-APPROVED RECOVERY DIRECTION`.

Not A1.

Not canonical.

## 14. Final corrective verdict

```text
#1041 diagnosis direction:
  RETAIN

#1041 final merged state:
  REQUIRED FOLLOW-UP

STATUS reachability:
  FIXED

single-next invariant:
  FIXED

handoff chronology:
  FIXED

stop-loss accounting:
  FIXED WITHOUT RETROACTIVE RECLASSIFICATION

accepted machine analysis:
  HIGH RETRIEVAL VALUE BY DEFAULT; AUTHORITY UNCHANGED

continuity_role:
  RETIRED AS A NEW AXIS

probe + explanandum:
  M-LEVEL OPERATIONAL RULE

third fusion domain:
  HOLD

#1039:
  HOLD / CURRENT-NEXT BOUNDED AUDIT TARGET

dynamic fresh-session probe:
  NOT RUN
```
