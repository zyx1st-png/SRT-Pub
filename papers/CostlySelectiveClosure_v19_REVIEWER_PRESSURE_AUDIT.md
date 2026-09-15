---
id: CSC-V19-REVIEWER-PRESSURE-AUDIT
type: publication_review_audit
status: active
canonical: false
target_venue: Artificial Life
manuscript: papers/CostlySelectiveClosure_v19_ArtificialLife_candidate.md
---

# Costly Selective Closure v19 — Artificial Life Reviewer-Pressure Audit

Date: 2026-09-15

## 1. Review posture

Question:

> If this manuscript were reviewed as an *Artificial Life* Article, what are the strongest remaining grounds for rejection after E1-E4 and the strongest-neighbor correction?

This audit does not defend CSC as a brand. It evaluates whether the current bounded paper is scientifically coherent and publishable.

## 2. Executive verdict

```text
P0 SCIENTIFIC INVALIDITY = NONE FOUND
P0 HARKING / RESULT SUBSTITUTION = NONE FOUND
P0 FALSE NOVELTY CLAIM = CORRECTED IN CURRENT MANUSCRIPT

P1 ALIFE-FIT / CONTRIBUTION-SCALE RISK = LIVE
P1 E4 MANIPULATION-PURITY RISK = LIVE
P1 E1-vs-E4 MECHANISM-COMPARABILITY RISK = LIVE
P1 ATTRACTOR / EFFECT-SIZE INTERPRETATION RISK = LIVE
P1 REPRODUCTION-PACKAGING RISK = LIVE

NEW EXPERIMENT REQUIRED BEFORE REVIEW = NO
MANUSCRIPT READY WITHOUT FURTHER EDIT = NO
```

The remaining issues are primarily framing, mechanism-boundary, and reviewer-facing reproducibility issues rather than reasons to reopen positive-result experimentation.

## 3. Rejection route A: "This is ordinary MARL reward/interdependence engineering, not Artificial Life"

### Risk

A reviewer may argue that:

- E1 is a standard termination/return effect;
- E3/E4 are action-availability manipulations;
- shared consequences encouraging cooperation are already well known in multi-agent learning;
- the paper therefore belongs in an RL/MARL venue rather than *Artificial Life*.

The strongest-neighbor audit makes this concern more, not less, important. Tampuu et al. (2017) already use a team-scoped punitive event to produce cooperative Pong behavior. Scott and Pitt (2023) already study interdependent cooperative survival in *Artificial Life*.

### Required response

The manuscript must make its ALife contribution architectural rather than algorithmic:

> the paper is not proposing a better cooperation-learning method. It uses controlled learning agents to study how different declared failure/recovery architectures change the organization of future opportunity at different unit scopes.

The Artificial Life relevance rests on:

- organizational level: episode-token vs controller-lineage vs training process;
- recovery architecture and external support;
- failure boundary and consequence bearer;
- sequential falsification of an initially simpler vulnerability interpretation;
- a comparison discipline for claims about artificial mortality/precariousness.

### Gate

```text
ALIFE FIT = DEFENSIBLE, BUT MUST REMAIN EXPLICIT
RL PERFORMANCE CLAIMS = DO NOT CENTER
```

## 4. Rejection route B: "E4 does not isolate abstract consequence scope"

### Risk

E4 is cleaner than E3, but SHARED scope is not a pure abstract flag.

When one agent fails:

- both agents execute the existing Rest transition;
- Rest has reward and energy consequences;
- at long latency, shared Rest can create additional depletion events;
- recovery intervals can refresh;
- at `k=10`, both-forced occupancy is about 0.60 and failure frequency rises substantially.

Therefore a reviewer can correctly say that E4 identifies the effect of **shared forced-recovery dynamics**, not a substrate-independent law of consequence scope.

### Current protection

The manuscript already states this limitation and uses the common-state frozen-policy endpoint so forced occupancy does not mechanically define the measured outcome.

### Required wording discipline

Prefer:

> shared failure-triggered recovery/action-opportunity consequence

or:

> consequence scope under this non-terminal forced-recovery mechanism

Avoid:

> shared fate causes cooperation

> consequence scope is a general causal law

### Gate

```text
E4 INTERNAL VALIDITY FOR ITS IMPLEMENTED CONTRAST = PASS
ABSTRACT / GENERAL SCOPE ISOLATION = NO
```

## 5. Rejection route C: "The +0.03 E4 effect does not explain the +0.51 E1 phenomenon"

### Risk

This is true and should not be argued away.

E4 was designed as a discriminator, not a quantitative decomposition of E1. Its primary scope effect is roughly +0.030, far below E1's terminal-versus-restore difference.

Moreover E1 and E4 do not use identical transition/update structures:

- E1 contains actual variable-length termination;
- E4 has fixed 50-step episodes;
- E1 uses the historical original policy-update path;
- E4 deliberately uses fixed-horizon normalization/scaling to remove the E3-specific confound;
- E4 shared recovery retains Rest rewards/energy dynamics rather than truncating all future token reward.

A reviewer should therefore reject any arithmetic statement such as "scope explains X% of E1."

### Correct interpretation

> E4 shows that scope matters independently. It does not estimate the fraction of E1 caused by scope.

The residual E1 magnitude leaves terminality/return truncation/trajectory structure and interactions among these variables live.

### Gate

```text
E4 AS PARTIAL MECHANISM DISCRIMINATOR = PASS
E4 AS QUANTITATIVE MEDIATION OF E1 = FAIL / DO NOT CLAIM
```

## 6. Rejection route D: "The E1-E4 story is post-hoc narrative construction"

### Risk

The whole four-experiment programme was not prospectively preregistered. E1 was exploratory/discovery. E2 was designed after E1; E3 after E2; E4 after E3 and a mechanism audit.

A skeptical reviewer can describe the sequence as repeated redesign until a new positive effect appeared.

### Protection

The provenance materially distinguishes this sequence from unconstrained positive-result hunting:

- E2 locked a positive prediction before its confirmatory run and retained its no-support result;
- E3 separately locked a positive prediction and retained its opposite-direction result;
- after E3, the mechanism audit explicitly listed H-SCOPE, H-TERM, H-VICTIM, and H-UPDATE as competitors;
- E4 locked six cells, new seeds, one collapsed primary test, an anti-confound update, and a +0.10 strong-effect gate before confirmatory execution;
- E4 is reported as Outcome B rather than promoted to strong support.

### Required wording

Use:

> sequentially preregistered discrimination programme

or:

> discovery followed by prospectively constrained follow-ups

Do not use:

> preregistered four-experiment programme

> prospectively confirmed full theory

### Gate

```text
HARKING RISK = MANAGEABLE IF CHRONOLOGY REMAINS EXPLICIT
```

## 7. Rejection route E: "E2 and E3 are weak evidence because of construct/floor/confound problems"

### E2

The damage manipulation does not directly change immediate reward, normal actions, or reward-bearing time. Its theoretical role must remain narrow:

> internal metabolic impairment alone did not reproduce E1 and excluded the preregistered large +0.10 endpoint effect.

### E3

The regime is floor-dominated and the absolute endpoint difference is modest. The strong negative rho is an ordinal statement, not a large behavioral shift. E3 also contains the later-identified update normalization/scaling confound.

### Why they still matter

Their value is not that they individually establish a general law. They constrain the path from E1 to E4 and document which initially plausible generalizations failed under locked tests.

### Gate

```text
E2/E3 AS STANDALONE MECHANISM PROOFS = NO
E2/E3 AS PREREGISTERED THEORY-NARROWING EVIDENCE = YES
```

## 8. Rejection route F: "The novelty is process rather than scientific substance"

### Risk

After acknowledging Tampuu and Scott-Pitt, a reviewer may say:

> The only novelty is that the authors ran several experiments and honestly reported negative ones.

Transparency alone is not enough for publication.

### Surviving substantive content

The manuscript must therefore distinguish **process value** from **scientific output**.

Process value:

- preregistered follow-ups;
- preserved unfavorable results;
- explicit theory contraction;
- statistical/provenance correction.

Scientific output:

1. a robust terminal-vs-restore policy-regime separation in the declared testbed;
2. evidence that persistent internal impairment and individual recovery latency do not substitute for that terminal intervention;
3. a preregistered positive but modest effect of sharing the same non-terminal action-opportunity loss;
4. a concrete comparative descriptor separating continuity, inheritance, opportunity loss, recovery source, timing, and scope.

The paper is publishable only if these scientific outputs are foregrounded and transparency is treated as evidential credibility, not novelty by itself.

### Gate

```text
NOVELTY = NARROW BUT SUBSTANTIVE IF E1-E4 DECOMPOSITION IS CENTERED
```

## 9. Rejection route G: "The title overstates what was manipulated"

Current title:

> **Who Bears Failure? Consequence Scope and Terminality in Survival-Coupled Artificial Agents**

Verdict:

```text
PASS / BOUNDED
```

"Who Bears Failure?" is a question, not a universal answer. The subtitle specifies the tested artificial-agent context and retains terminality because E4 does not explain it away.

Do not change the subtitle to "Shared Fate" or "Cooperative Survival"; those phrases would imply broader claims and collide more directly with existing literature.

## 10. Rejection route H: reproducibility/provenance package is not yet reviewer-ready

### Current strength

- E2/E3/E4 preregistration commits are identified;
- E4 first/only confirmatory run, artifact ID, and hashes are preserved in adjudication;
- E4 compact result record preserves locked summaries and seed-level collapsed primary/secondary differences;
- experiment code and invariants are in the repository.

### Remaining packaging risk

The unique E4 full Actions artifact was created with finite retention. The compact repository record identifies it by hash but does not itself contain every full cell/episode row.

This is not a scientific-invalidity issue because the deterministic runner and locked seeds can regenerate the analysis, but reviewer-facing archival packaging should not depend on an expiring Actions artifact.

### Required publication action

Before submission:

- create a static reviewer-safe reproduction package containing the full preserved E1-E4 result files and preregistration/adjudication documents;
- archive that package in a stable submission supplement or archival deposit;
- describe any later archive deposit as archival preservation of prior timestamped Git history, not as retroactive third-party preregistration.

### Gate

```text
REPRODUCIBILITY CONTENT = STRONG
REVIEWER-SAFE PERMANENT PACKAGING = NOT YET COMPLETE
```

## 11. Is another experiment required?

Verdict:

```text
NO
```

The remaining mechanism ambiguity is real, especially terminality vs shared non-terminal recovery. But it no longer makes the bounded v19 claim incoherent.

An E5 would be justified only if:

- peer review specifically requires isolation of return-loss scope from action-loss scope; or
- a separately motivated new paper asks that question.

Running E5 now merely because E4 is small would reopen researcher degrees of freedom and weaken the current clean stop rule.

## 12. Required actions before readiness

Priority order:

1. strongest-neighbor citations/novelty correction in manuscript — **DONE at current v19 head**;
2. preregistration commit provenance in Data/Code — **DONE at current v19 head**;
3. remove unused v18 references — **DONE at current v19 head**;
4. generate and insert E1-E4 evidence figure — **GENERATOR WRITTEN / SVG NOT YET GENERATED**;
5. run actual submission-builder word-count and reference-closure check — **PENDING EXECUTION**;
6. prepare permanent reviewer-safe E1-E4 reproduction package — **PENDING**;
7. final PDF visual QA and cover-letter revision — **PENDING**.

## 13. Current publication adjudication

```text
SCIENTIFIC CORE = PASS / BOUNDED
E1-E4 EVIDENCE STORY = COHERENT
E4 H-SCOPE = SUPPORTED / MODEST
E1 RESIDUAL TERMINALITY MECHANISM = OPEN BUT NON-BLOCKING
FALSE GENERIC NOVELTY = CORRECTED
ALIFE FIT = DEFENSIBLE
NEW EXPERIMENT REQUIRED = NO

CONTENT READY FOR FINAL PACKAGING = NOT YET
SUBMISSION BUILDER = MUST PASS AFTER CURRENT HARDENED GUARDS
REVIEWER-SAFE ARCHIVE = PENDING
PDF QA = PENDING

MERGE #984 = HOLD
JOURNAL SUBMISSION = HOLD
```
