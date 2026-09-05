---
id: SRT-OPS-CYCLE1-SHUFFLED-WRITEBACK-MODEL-V2-20260905
type: proposal
status: active
record_stage: executed_verdict_c_generic_credit_assignment
date: 2026-09-05
layer: meta
epistemic_layer: bridge
claim_mode: proposal
canonical: false
ai_do_not_use_for_definition: true
dependency:
  - Operations/Proposals/SRT_AUTHOR_REENTRY_CYCLE1_CLOSURE_2026-09-05.md
  - 01_Source_Intuition/SRT_AUTHOR_REENTRY_CYCLE1_PASS4_2026-09-05.md
  - Operations/Audits/SRT_AUTHOR_REENTRY_CYCLE1_MATURE_NEIGHBOR_PRESSURE_PASS2_HISTORY_CONSTITUTED_ONE_2026-09-05.md
  - Operations/Audits/SRT_AUTHOR_REENTRY_CYCLE1_HISTORY_IN_ONE_ADMISSION_AND_GENESIS_AUDIT_2026-09-05.md
tags: [Cycle1, FormationTime, ShuffledWriteback, Recurrence, CreditAssignment]
---

# Cycle 1 D/O v2 — shuffled writeback and recurrence collapse

## 1. Scope and source consistency

This is an AI-designed, noncanonical falsification probe, explicitly commissioned
by the author on PR #910. It is not a new ontology, owner definition or deep well.
Starting GitHub head: `5a0a7a5f3c7e7bc29360004f545aa57ed1fb1147`, exact branch
`theory/author-reentry-cycle1-one-formation-20260905`, Draft/open; Governance
Preflight successful. The complete branch was checked out before editing.

PASS1–PASS4 were read directly, rather than inferred from the PR body. Core
direction is consistent, with two provenance qualifications to current summaries:

| Source locator | Direct author content | Summary disposition |
|---|---|---|
| PASS1 Q2–Q6 and supplement | Difference-maintenance, cognitive boundary, two One-formations; initial cognitive sedimentation wording | Inherit with PASS2's explicit narrowing; PASS1 Q1 does not choose a multiplicity model |
| PASS2 Q1–Q3 | Minimum non-neutrality; Selection sedimentation; structure as achievement; cognition cannot precede stable bearer; stability is graded | Inherit; no canonical or numerical threshold implied |
| PASS2 Q4 | `类似贝叶斯决策。` | Mechanism analogy only; replace summary wording that suggests established mechanistic equivalence |
| PASS3 B1–B2 | `bearer出现以前选择沉积在多。` / `当历史痕迹沉积在一时，变为Bearer。` | Inherit; “attribution/localization” is AI structural gloss, not an author-defined variable |
| PASS4 original fork and answer | Literal answer `b` selecting the displayed B/S2–S3 option | Portable causal memory insufficient; reconstitution requirement licensed. Equations, routing and readout remain C/AI construction |

Existing assets were inspected and retained: both mature-neighbor audits, both
internal red-teams, owner-reuse audit, history-in-One/genesis audit, domain
discrimination pass, minimal causal model v1, and the code/README/reference
results of `Experiments/cycle1_history_location_toy/`. The v1 crossing is coherent
with its stored results, but is not rerun or promoted into a formation result.
The owner-reuse audit already covers D2, PH-IND02/05/06 and AICONSC01.
`Core_Law/SRT_Individuation.md` §2's own-output trace and its model-local scope
note were checked against genesis-audit §2: circularity is already covered.

The bounded target is whether history helps reconstitute a continuing
selection-position, beyond ordinary stable versus shuffled credit assignment.
“History matters”, recurrence and portable storage alone cannot discharge it.

## 2. Gate 0 before execution

**Engineering topology gate: constructible. Conceptual residual survival: unpaid.**
There is no O-only feedback edge. Both arms contain eight isomorphic loci with
the same two recurrent coordinates per locus, the same update engine and the
same routing crossbar. Only the cross-time source-to-destination association
of incoming history writes differs.

Already before execution, the equations below admit an ordinary recurrent
learner interpretation with no extra SRT assumption. Therefore a positive
O-minus-D effect alone is expected to fall under Verdict C. Running this one
probe measures the absorption; it does not seek a Level-2 win. Passing the
engineering check must never be reported as surviving the full collapse gate.

## 3. Declared model and exact matching

Domain objects are engineered registers, not metaphysical 多 or pre-proven
Bearers. Eight addresses are supplied; no distinguished locus is selected
post hoc. All start with zero history `h` and zero action bias `x`, hence no
learned differentiation. Learning formation is tested, not creation of the
addresses, boundaries or numerical identity themselves.

At each formation epoch `t=1..64`, source `i` emits the evidence token
`y[i,t] = 0.8*s[i] + Uniform(-0.2,0.2)`. The sign vector contains four +1 and
four -1 entries, shuffled once per seed, then fixed. Evidence is exogenous,
independent of the learner's selected action; this is supervised recurrent
prediction, not an on-policy RL experiment. There is no reward budget.

For every destination `j`, simultaneously:

```text
h[j,t] = (1-alpha)*h[j,t-1] + alpha*y[pi_t(j),t]
x[j,t] = rho*x[j,t-1] + (1-rho)*h[j,t]
P(action +1 at j,t) = (1+x[j,t])/2
alpha = 0.125; rho = 0.5
O: pi_t = identity throughout formation
D: pi_t = independent uniform permutation each epoch
```

The learner receives token values, not their source label or the permutation
inverse. The experimental controller retains routing only for verification.
Every source is delivered once and every destination receives once per epoch;
fixed points of a random permutation are allowed. O has stable associations at
all eight loci; D does not concentrate fewer updates at any locus.

| Control | Both arms, and ordinary baseline |
|---|---|
| History/update count | 512 evidence tokens and 512 history writes during formation; 80 updates of each `x`; zero history writes during the 16-step probe |
| Memory/update capacity | 8 durable `h` and 8 fast `x` float64 coordinates; no extra learner log, identity field or trainable parameter |
| Plasticity | Same alpha=0.125, same EMA rule; common probe gate disables evidence writes |
| Exposure | Same exact token multiset per epoch, one delivery per source and destination; no outcome-dependent exposure |
| Environment | Same signs, noise realization, 64-step persistent schedule and 16-step no-evidence probe |
| Recurrence | Same `h -> h` gain .875 during formation, `x -> x` gain .5, `h -> x` gain .5; same node and feedback-edge counts |

The recurrent state-dependency graph is identical. With state order `(h,x)`,
the formation matrix is `[[.875I,0],[.4375I,.5I]]` in BOTH arms. Input matrices
are `[[.125P_t],[.0625P_t]]`: only routing differs. Both use the same physical
all-to-all evidence crossbar with eight selected deliveries per step. This is
not a claim that the labelled, time-unrolled input-routing graphs are identical;
that difference is the intervention. Probe matrices are also identical.

Equal input counts/capacity do NOT imply equal retained task information,
history norm, signal-to-noise ratio or mutual information with source identity.
Shuffling deliberately removes source alignment. Those quantities cannot be
quietly claimed as controlled; this is exactly the ordinary explanation.

## 4. Preregistered primary readout and decision rule

Only candidate A is primary: **history-conditioned action-bias reconstitution**.
At the end of epoch 64, set all `x=0` in every arm; preserve `h`. This is a common
measurement challenge, not a second factorial treatment. For epochs 65..80,
provide no new evidence and freeze `h`; continue the identical `x` recurrence.
Thus measured recovery depends on already formed history, not fresh relearning.

For seed `k`, define
`R_k = mean over all 8 loci and probe steps 1..16 of (1+s[j]*x[j])/2`.
This is the probability of reselecting the source-consistent action, bounded
0..1, neutral value .5. It is an engineered functional proxy for the proposed
selection-position, not a bearer/boundary admission criterion. All loci are
included even if no bias formed. No successful-locus or responder filtering.

Fixed before any run:

```text
seeds = integers 0..63 (64 paired runs; no optional stopping)
comparison = paired mean R_O - R_D
CI = paired-seed percentile bootstrap, 10,000 resamples
bootstrap seed = 20260905, linear 2.5% and 97.5% quantiles
positive toy discrimination iff CI lower bound > 0.05
otherwise = no stable preregistered positive effect (Verdict B)
baseline equality tolerance = 1e-12 maximum absolute state/output difference
```

The .05 threshold is a declared toy effect-size convention, not a natural
boundary. The CI is Monte Carlo uncertainty across the specified toy schedules,
not evidence about populations in nature. A null fails to support the candidate
in this model; it is not a general equivalence theorem. Formation curves and
pre-challenge bias are descriptive only; no secondary metric may rescue a null.

## 5. Ordinary baseline and analytical absorption

Alongside both arms, run an independently written ordinary delta-rule predictor
with leaky recurrent output:

```text
q[j] += alpha*(routed_evidence[j] - q[j])
z[j] += (1-rho)*(q[j] - z[j])
```

The challenge sets `z=0`, preserving `q`, then performs only the second update.
Same initialization, memory, architecture, routing, exposure and schedule.
The baseline does not call the candidate transition function. Compare every
state and primary score, not just the group means. The algebraic map is
`h=q`, `x=z`; this is a substantive equivalence argument, not independent
evidence from another theory. Failure of numerical equivalence is first an
implementation fault, never an SRT residual. No parameter fitting is needed.

By expansion, `h[j,64] = alpha*sum_t (1-alpha)^(64-t)*y[pi_t(j),t]`.
In O its expectation is `.8*s[j]*(1-(1-alpha)^64)`; in D it is zero because
balanced sources are uniformly permuted. In the probe `x[j,u]=(1-rho^u)*h[j,64]`.
Hence the expected O-minus-D readout is analytically
`.4*(1-(1-alpha)^64)*mean_u(1-rho^u)` for `u=1..16`.
Stable assignment preserves each source signal; shuffle mixes opposing signals.
There is no hidden SRT-specific remainder in these equations.

## 6. Verdicts fixed before results

| Verdict | Trigger | Required disposition |
|---|---|---|
| A — DESIGN FAIL | Matched recurrent topology cannot be defined, or O has feedback that D lacks | Level 1 WEAKENED; Level 2 FAIL/HOLD; stop model embellishment |
| B — NO EFFECT | Primary positive rule fails | History-location candidate not supported by this model; no metric switch; reassess Level 1, Level 2 HOLD |
| C — GENERIC RECURRENCE RESULT | Primary positive rule passes but ordinary baseline/credit assignment explains it fully | Toy discrimination positive; SRT distinctiveness NO; Level 1 reassessed rather than automatically retained; Level 2 HOLD/FAIL |
| D — RESIDUAL SURVIVES | All declared matching holds, primary effect passes, and a stated additional discriminator defeats the ordinary stable-assignment account | Gate 0 survival only, never automatic Level 2 PASS |

No additional discriminator exists in this v2 specification. An unexplained
numerical discrepancy cannot retroactively create one. Level verdicts apply to
this tested residual, not whole-SRT identity; author source remains intact.

## 7. Bounded strongest-neighbor supplement

Reuse mature-neighbor pass 2 §§2–5 for Simondon, enactive autonomy and process
identity. Do not redo that scan. The newly exposed strongest **operational**
comparator is ordinary recurrent prediction with stable credit assignment:
learned history and recurrent state are already enough to rebuild output bias.
It is strongest here because it admits an exact state/dynamics mapping, not
merely a verbal resemblance.

Elman's *Finding Structure in Time* (1990) uses recurrent context to make
processing depend on prior internal states and develops task-dependent
representations. This is source-native support for the ordinary recurrence
alternative, not a claim that Elman ran this shuffle experiment or proved the
Bearer argument. [Publisher abstract](https://onlinelibrary.wiley.com/doi/10.1207/s15516709cog1402_1)
and [original paper](https://papers.baulab.info/papers/Elman-1990.pdf).
The exact absorption proof here is our displayed algebra, not a result
attributed to that paper.

The structural comparison tuple is therefore: strongest comparator = ordinary
delta-rule recurrent predictor; native claim = routed evidence updates current
predictive state and that state regenerates action bias; strength = exact
equivalence; proposed SRT change = attribution moved into formation. If that
last change maps completely to source-to-parameter assignment, the operational
partition collapses to the comparator. “Deeper SRT explanation” cannot rescue it.

Uncontrolled stronger alternatives: autonomy and generic self-maintenance need
endogenous resource/constraint production absent here; attractor persistence
beyond this fixed linear relaxation is not isolated; full developmental
organization needs changing boundaries/component organization; biological
individuation needs material, metabolic and lineage mechanisms absent here.
Their subtraction remains unpaid. Recovery of an engineered action bias cannot
stand in for any of these or establish the stronger S2/S3 relation.

## 8. Analytical red-team cases only

- **Copy:** copying complete `(h,x)` with the same future inputs reproduces the
  trajectory; no numerical identity conclusion follows. Portability remains a
  limitation, even though `h` demonstrably regenerates `x` after its erasure.
- **Replacement:** replacing a physical register while retaining all causal
  state leaves this model unchanged. It contains no material lineage variable.
- **Same current state / different history:** with full state, schedule and
  routing matched, futures agree. Do not invent occult history dependence.

The new concrete Individuation pressure is limited: a stable routing address
supplied by the modeller must not become “own history” by definition. `h` and
recovered `x` are downstream learned-state readouts, not a derivation of first
Bearer genesis. Existing theta_trace/theta_ext circularity audit is sufficient;
no canonical owner edit is warranted.

## 9. Execution record

Sections 1–8, runner and config were written to the existing PR head in commit
`8a6748736f254626f421da03bf4bab81b678fe93` BEFORE the first simulation. The remote
head and Draft flag were verified, fetched, and the local index was checked
against that commit before running. The preregistered sections, runner and
config were not tuned after results. No exploratory parameter/seed runs occurred.

Command (repository root):

```bash
uv run python Experiments/cycle1_shuffled_writeback_v2/run_shuffled_writeback.py --output Experiments/cycle1_shuffled_writeback_v2/reference_results.json
```

| Primary result, 64 paired seeds | Value |
|---|---:|
| O mean recovery probability | 0.8758545973 |
| D mean recovery probability | 0.5049263741 |
| O minus D | 0.3709282232 |
| Paired bootstrap 95% CI | [0.3611285070, 0.3805776018] |
| Ordinary baseline O minus D | 0.3709282232 |
| Maximum candidate/baseline state error | 4.4408920985e-16 |
| Analytical expected O minus D | 0.3749275117 |

All matching/control assertions passed. The CI clears the fixed .05 threshold.
The independently implemented baseline reproduces every state to floating-point
precision. The modest finite-sample difference from the expectation is compatible
with the preregistered Monte Carlo interval. No extra metric was promoted.

**Verdict C — GENERIC RECURRENCE RESULT.** O and D differ in formation-dependent
functional recovery under matched recurrence; their difference is completely
explained by stable source-to-parameter assignment versus shuffled assignment.
The engineered recovery readout never isolated the stronger S2/S3 relation.

```text
engineering topology matching: PASS
history-localization residual survives recurrence-collapse Gate 0: NO
toy discrimination: POSITIVE
SRT-specific scientific discriminator in this model: FAIL / NO
Level 0: COLLAPSED (this operational partition is ordinary-learning translation)
Level 1: WEAKENED (the upstream author question remains; its v2 realization
         adds no independent structural partition over the ordinary learner)
Level 2: HOLD (v2 route failed; no earned distinctiveness or next-gate eligibility)
```

These are scoped research verdicts, not a new author adjudication and not a
whole-SRT verdict. Source PASS1–PASS4 and the canonical owners remain unchanged.
The earlier provisional Level-1 pass must no longer be used as an unconditional
current endorsement of this operational residual.

**Only worthwhile next bounded move:** a single analytical discriminator-or-stop
check: can the already author-owned S2/S3 requirement name one observable case
difference that is not identical to source-to-parameter credit assignment or
regeneration from stored causal state? If no such difference can be stated,
retire this residual as a scientific test route; do not build v3 by adding
mechanisms or search new domains merely to preserve it. No new experiment is
licensed by this result.
