---
id: CSC-V19-ARTIFICIAL-LIFE-CONSEQUENCE-SCOPE
type: manuscript
status: draft
version: v19
target_venue: Artificial Life
derived_from: papers/CostlySelectiveClosure_v18_ArtificialLife_candidate.md
submission_state: internal_candidate
---

# Who Bears Failure? Consequence Scope and Terminality in Survival-Coupled Artificial Agents

Yuxin Zhang

Independent Researcher

zyx1st@gmail.com

> **Repository note.** This v19 candidate supersedes v18 for publication development but does not overwrite it. It integrates the E1–E4 evidence sequence, including two preregistered failed generalizations and one preregistered consequence-scope discriminator. Historical v16–v18 manuscripts remain unchanged.

## Abstract

Artificial-life systems can be made more consequential in many ways: episodes can terminate, internal state can be persistently impaired, recovery can consume action opportunities, or one agent's failure can also remove opportunities from others. These manipulations are often discussed under broad terms such as mortality, precariousness, vulnerability, or recovery cost, but they need not alter the same part of an agent's future. We study this distinction in a two-agent survival-coupled REINFORCE testbed and ask a narrower question: **who bears the future consequences of failure?**

Experiment 1, which was not preregistered, found a large terminal-versus-restore difference. After withdrawal of a cooperation bonus, mean mutual cooperation was about 0.55 when energy depletion terminated the current episode-token and about 0.04 when depletion triggered restoration, with the difference surviving zero-penalty, lives-budget, payoff, and common-state frozen-policy checks. Two later repository-preregistered follow-ups did not support simple generalizations of that effect. Experiment 2 varied the persistence of non-terminal metabolic impairment while leaving reward-bearing time and normal action availability intact; the preregistered positive gradient was not supported, and the confidence interval excluded the programme's +0.10 strong-effect threshold. Experiment 3 imposed fully reversible individual-scoped recovery latency; its preregistered positive hypothesis also failed, and the observed ordinal association was negative.

A fourth preregistered experiment then held the non-terminal recovery mechanism fixed while changing **consequence scope**: only the failed agent lost normal action opportunity, or both agents did. On a common 2,000-state frozen-policy endpoint, shared scope increased learned mutual-cooperation propensity by about +0.030 on average across latencies (`95% CI [0.012, 0.054]`, paired sign-flip `p = 0.00015`), with 29/30 collapsed seed contrasts positive. The preregistered +0.10 strong-effect gate failed.

The evidence supports a bounded conclusion: **consequence scope is an empirically relevant variable in this testbed, but it is too small to explain the much larger terminality effect by itself**. Artificial-life comparisons should therefore state not only whether failure is costly or recoverable, but which organizational units lose future action, interaction, or return opportunities when failure occurs.

**Keywords**: artificial life, consequence scope, terminality, recovery architecture, reinforcement learning, cooperation

## 1. Introduction

Artificial life is both a constructive and a comparative science. It asks what kinds of organizations can sustain, regulate, reproduce, adapt, or act in ways that resemble living systems, and it asks which architectural differences matter when those capacities are implemented in very different substrates. Those comparisons are difficult because words such as *death*, *damage*, *reset*, *recovery*, *precariousness*, and *self-maintenance* can refer to different organizational levels and different transition structures.

A biological organism that dies, a robot whose controller reboots, a simulated agent whose episode terminates, a learned policy that persists across many terminated episodes, and a copied software process restored from checkpoint may all be described as "failing." Yet the consequences are not equivalent. Failure may destroy the current token while preserving a lineage; it may leave the token intact but impair future resource acquisition; it may temporarily remove actions; it may be repaired externally; or it may cause other agents or higher-level organizations to lose future opportunities as well.

Existing work already supplies richer conceptual vocabularies than a simple alive/dead distinction. Autopoietic and autonomy traditions emphasize self-production, constraint closure, and self-maintenance (Maturana & Varela, 1980; Moreno & Mossio, 2015). Enactive accounts make precariousness and viability central to adaptive agency (Di Paolo, 2005; Egbert & Barandiaran, 2011; Beer & Di Paolo, 2023). Dimensional approaches to life-likeness explicitly resist reducing life to one binary property (Damiano & Stano, 2020; Witkowski & Schwitzgebel, 2024). Artificial-agent work has also directly explored mortality, persistent bodily consequence, reset, and successor learning (Korecki et al., 2023; Chen & Chen, 2026). The present paper does not claim priority for any of those ideas.

The narrower problem studied here emerged from an earlier comparison protocol called **costly selective closure** (CSC). CSC asked how a declared organizational unit maintains selective coupling under ongoing burden, historical constraint, and non-trivial failure. An early version treated "irreversible vulnerability" as if different failures might be located on one ordered dimension. The first experiment in the present programme appeared consistent with that intuition: agents learned much more persistent costly cooperation when depletion terminated the current episode-token than when depletion was cheaply restored.

That first result, however, immediately raised a standard reinforcement-learning objection. Termination changes future discounted return and removes later state-action opportunities. A terminal transition is therefore not merely "more serious" in an intuitive sense; it changes the optimization problem. If the phenomenon reflected a broader failure-consequence principle, some non-terminal ways of making failure costly should reproduce at least part of the effect.

The programme therefore became a sequence of increasingly specific discrimination tests. Experiment 2 asked whether longer-lasting internal metabolic impairment would produce an ordered cooperation gradient when episode length remained fixed. It did not. Experiment 3 asked whether making recovery consume more of the failed agent's future action opportunities would do so. That positive prediction also failed; the observed ordered association was instead negative. Those two outcomes made a simple scalar account untenable, but they did not identify what about terminality mattered.

A subsequent mechanism audit highlighted a distinction that had been hidden inside the original terminal manipulation. In Experiment 1, when either member of the dyad depleted its energy, **the entire episode ended**. The partner therefore lost the remainder of its within-episode future too. In Experiment 3, by contrast, the burden was primarily local: the depleted agent was forced to Rest while the partner remained active. This suggested a more specific variable: **consequence scope**, or which units lose future action or return-bearing opportunity when one unit fails.

Experiment 4 was preregistered specifically to test that mechanism. It reused the non-terminal forced-recovery architecture but compared two scopes. Under **individual scope**, only the failed agent lost normal action choice for a fixed recovery interval. Under **shared scope**, one agent's failure caused both agents to lose normal action choice for the same interval. The experiment also changed the policy-update implementation to remove a decision-count-dependent normalization/scaling confound present in Experiment 3 and used a common frozen-policy state bank as its primary endpoint.

The result was positive but modest. Shared scope increased learned mutual-cooperation propensity relative to individual scope, and the direction was positive in 29 of 30 collapsed seed contrasts. Yet the average effect was only about +0.03, far below the preregistered +0.10 strong-effect threshold and far smaller than the Experiment 1 terminal-versus-restore separation.

The paper therefore makes four bounded contributions.

First, it reports a strong terminal-versus-restore cooperation effect in a survival-coupled multi-agent testbed together with several robustness checks. Second, it reports two preregistered failed generalizations rather than hiding them: persistent internal impairment did not reproduce the effect, and individual-scoped recovery latency moved in the opposite ordinal direction. Third, it reports a preregistered mechanism discriminator showing that **who bears failure-triggered future action-opportunity loss matters independently**, although modestly. Fourth, it proposes a consequence-description discipline for artificial-life comparison: declare the organizational unit, boundary, timescale, recovery regime, and the scope of lost future opportunity instead of collapsing distinct transitions into one generic severity or vulnerability score.

The conclusion is deliberately narrower than a general theory of life or mortality. We do not show that shared fate universally creates cooperation, that terminality has been fully explained, that these agents are alive, or that CSC as a whole has been experimentally validated. We show that one often-hidden architectural choice—**who loses the future when one agent fails**—has measurable policy consequences in this testbed and should be made explicit in cross-system comparison.

## 2. Related Work

### 2.1 Precariousness, autonomy, and life-likeness

Precariousness has long been central to enactive and autonomy-oriented accounts of agency. Di Paolo (2005) links adaptivity to regulation relative to viability conditions, while Egbert and Barandiaran (2011) formalize normative behavior and precariousness in adaptive systems. Beer and Di Paolo (2023) distinguish systemic, processual, and thermodynamic forms of precariousness and argue that fragility is constitutive of living organization rather than an accidental defect. The present work does not redefine precariousness. Its narrower contribution is to show that, in a simple artificial-agent testbed, different ways of operationalizing "failure consequence" are behaviorally non-equivalent.

Synthetic-cell and life-likeness research likewise resists one-dimensional definitions. Damiano and Stano (2020) emphasize organizational rather than merely surface similarity in synthetic cells, while Witkowski and Schwitzgebel (2024) explicitly discuss multiple dimensions relevant to life and moral status. These literatures motivate careful comparison but do not determine which failure transitions should be treated as equivalent in a particular computational model.

### 2.2 Artificial mortality and consequential embodiment

Artificial mortality is not new. Korecki, Carissimo, and Lund (2023) use irreversible artificial death states and successor learning, while Chen and Chen (2026) study a mortality-grounded embodied agent whose persistent bodily history shapes social and linguistic learning. Such work makes broad claims like "mortality matters" non-novel. The present experiments instead focus on matched manipulations within one small system and on what changes when failure consequences are localized or shared.

The level of analysis matters. In our Experiment 1, an episode-token terminates but the controller-lineage survives across episodes and continues learning. The experiment therefore does not implement literal controller destruction. It studies how a repeated-learning process changes when one type of failure removes the remainder of a current interaction token for both agents.

### 2.3 Termination, reset cost, and action availability in reinforcement learning

The reinforcement-learning ingredients are also familiar. Termination changes future return. Reset costs and continuing-task formulations explicitly address how terminal events alter optimization; Hisaki and Ono (2024), for example, introduce adaptive reset cost in an average-reward setting. The fact that termination can matter to a reward-maximizing learner is therefore not our discovery.

Likewise, restricted action availability is a mature decision-process problem. Stochastic-action-set MDPs and reinforcement-learning methods for unavailable actions formalize cases in which an agent cannot always select every action (Boutilier et al., 2018; Chandak et al., 2020). Experiment 3 and Experiment 4 do not claim novelty for action restriction itself. They use temporary action loss as a controlled way of testing hypotheses about failure consequence.

### 2.4 Social dependence and consequence scope

The additional question raised by this programme concerns **scope**. A consequence may be borne only by the unit that crosses a failure threshold, or it may alter the future available to partners, collectives, or higher-level organizations. In social and collective systems, this distinction can change incentives even when immediate reward tables are unchanged. A partner's continued viability can become instrumentally relevant when the partner's failure reduces one's own continuation opportunities.

The present paper does not claim that this general idea is new. Its empirical contribution is more specific: after a large terminal-versus-restore effect and two failed preregistered generalizations, Experiment 4 prospectively manipulates the scope of the *same non-terminal recovery burden* and tests whether learned cooperation changes.

## 3. Conceptual Motivation: Describing Failure Consequences

The experiments were motivated by CSC, but the evidence has progressively reduced the role CSC should play in the paper. The protocol is retained here only as conceptual provenance and as a discipline for declaring what is being compared.

A comparison should specify at least four contextual commitments:

1. **organizational unit** — what exactly is being profiled;
2. **boundary** — which resources and supports count as internal or external;
3. **timescale** — over what interval continuity, maintenance, and failure are evaluated;
4. **recovery regime** — what forms of reset, repair, replacement, copying, or continuation are available.

The E1–E4 sequence suggests that failure itself should then be described structurally rather than with one scalar vulnerability score. At minimum, six questions are useful.

1. **Continuity:** does the same declared unit continue after failure?
2. **State inheritance:** which learned, bodily, or historical structures survive?
3. **Opportunity loss:** which future actions, interactions, rewards, or viability opportunities disappear?
4. **Recovery source:** is recovery performed by the unit, the environment, an external operator, a copy, or a successor?
5. **Recovery timing:** how much environment time and organizational time are consumed before normal regulation resumes?
6. **Consequence scope / bearer:** which units lose future opportunity when one unit fails?

This six-question descriptor is not a validated ontology. The present experiments directly test only a small subset of these distinctions. Experiment 4 provides evidence specifically for item 6 under one non-terminal forced-recovery mechanism.

Three organizational levels should also be kept separate in interpreting the experiments:

- **episode-token** — the currently running interaction episode;
- **controller-lineage** — policy parameters that persist across episodes;
- **training process** — the larger repeated-learning process.

Experiment 1 terminates the episode-token, not the controller-lineage. Experiments 2–4 keep the episode-token running. All experiments preserve learned controller parameters across episodes.

## 4. Experimental Programme

### 4.1 Common survival-coupled testbed

All four experiments use the same basic two-agent environment and policy architecture. Two independent REINFORCE learners (Williams, 1992) receive 12 observation features, pass them through a 16-unit tanh hidden layer, and choose among three actions: `cooperate`, `solo`, or `rest`.

Immediate rewards have a Prisoner's-Dilemma ordering. Unilateral Solo against Cooperate receives `1.4`, mutual cooperation `1.0`, mutual Solo `0.6`, and Cooperate against Solo `0.0`. Rest yields `0.25` to the resting agent. Energy dynamics are distinct from immediate reward. Each step incurs metabolic cost `1.0`; mutual cooperation adds `2.0` energy, mutual Solo adds `0.7`, Solo against Cooperate adds `1.2`, Cooperate against Solo adds `0.0`, and Rest adds `0.5`. Thus cooperation can support energetic maintenance even though unilateral Solo has the larger immediate reward.

Policies are trained for 1,000 episodes with an added mutual-cooperation bonus, followed by 300 online-adaptation episodes after the bonus is withdrawn. Learning continues during withdrawal. The base discount factor is `gamma = 0.97` and learning rate is `0.04`.

The experimental chronology is important. **Experiment 1 was not preregistered.** It established the initial phenomenon. Experiment 2 and Experiment 3 were formulated after Experiment 1 was known and separately locked in timestamped repository preregistrations before their confirmatory implementation/execution on seeds `1..30`. Experiment 4 was formulated after an independent mechanism audit of E1–E3, then separately preregistered before implementation and before confirmatory seeds `101..130` were run. The programme should therefore be read as discovery followed by successive prospectively constrained discrimination tests, not as one prospectively preregistered four-experiment study.

### 4.2 Experiment 1: terminal failure versus restoration

Experiment 1 compares two primary regimes.

1. **Terminal condition.** When either agent depletes its energy, the current episode-token ends for the dyad.
2. **Restore condition.** On depletion, the affected agent is restored to `E0 = 6` and the episode continues.

The same programmed immediate reward function, observation features, base energy dynamics, policy architecture, training schedule, and matched seeds are used. A depletion penalty of `2.0` is applied in the main comparison. Because terminality removes the remainder of the current token's future for both agents, termination changes future return, state occupancy, and realized trajectory length as part of the intervention.

The historical Experiment 1 result files were analysed using a two-sided two-sample label-permutation test with 20,000 resamples. Although matched seeds were used across regimes, that historical test pools outcomes and permutes regime labels rather than exploiting pairing. We therefore retain the historical analysis and separately report a post-hoc paired sign-flip sensitivity analysis on the fixed committed outcomes. No retraining is involved and the historical test is not retroactively relabelled.

Experiment 1 also includes four robustness families: a zero-penalty ablation; a lives-budget gradient from one life toward unbounded restoration; a six-cell payoff sweep; and a common-state frozen-policy probe that evaluates learned policies on identical held-out observation states.

### 4.3 Experiment 2: persistent non-terminal metabolic impairment

Experiment 2 was preregistered to ask whether **damage persistence** could reproduce an ordered version of the Experiment 1 effect without termination.

All conditions remain exactly 50 environment steps. Depletion carries zero explicit failure reward penalty and immediately restores energy to `E0 = 6`. The manipulation multiplies subsequent `ENERGY_GAIN` by `0.75` while damage is active. Damage duration is ordered as immediate recovery, 5 steps, 15 steps, or the remainder of the episode.

A crucial construct boundary is that damaged state does **not** directly change the immediate reward table, remove normal policy actions, or remove reward-bearing environment time. It can affect learning indirectly through energy observations, low-energy indicators, later state occupancy, depletion frequency, and failure-history features. Experiment 2 therefore tests persistent internal metabolic impairment, not every possible form of persistent consequence.

The preregistered primary endpoint is final-100-withdrawal mutual cooperation. A tie-aware Spearman association over ordered damage duration is tested by condition-label permutations blocked within seed. Strong support additionally required the endpoint difference between persistent damage and immediate recovery to be at least `+0.10` with a positive paired bootstrap interval.

### 4.4 Experiment 3: individual-scoped recovery latency

Experiment 3 was separately preregistered after Experiment 2 failed to support the expected gradient. It asked whether a more directly functional but still reversible failure consequence would reproduce the Experiment 1 direction.

All episodes remain exactly 50 environment steps. On depletion, energy is immediately restored to `E0 = 6`, no new explicit failure reward penalty is added, and the failed agent then executes forced Rest for `k = 0,2,5,10` subsequent environment steps. During those steps it does not sample a normal policy action. The partner remains decision-capable unless separately recovering.

Because forced-recovery steps mechanically prevent voluntary mutual cooperation, the primary rollout endpoint counts cooperation only on **eligible decision steps**, where both agents begin the step free to choose normally. The preregistered positive hypothesis uses a blocked-by-seed ordered Spearman test. A common 2,000-state frozen-policy probe was preregistered as a secondary policy-level check.

Experiment 3 has an additional interpretation boundary discovered during later code audit. Its masked policy update standardizes returns over the condition-dependent subset of genuine decision steps and divides gradients by the number of genuine decisions. As recovery latency increases, that normalization population and gradient divisor change. This is not an implementation error relative to the preregistered E3 design, but it is a mechanism-identification confound. The common-state probe shows that learned policies differ, but it cannot remove how those policies were trained.

### 4.5 Experiment 4: individual versus shared consequence scope

Experiment 4 was preregistered after an explicit mechanism audit of E1–E3. Its question was not whether "more consequence" increases cooperation. It asked whether the *scope* of the same failure-triggered action-opportunity loss matters.

The six confirmatory cells cross:

```text
scope = individual, shared
latency k = 2, 5, 10
```

All conditions keep a fixed 50-step environment horizon, the same immediate reward and energy tables, immediate `E0 = 6` rescue after depletion, zero explicit failure reward penalty, the same policy architecture, learning rates, cooperation-bonus schedule, and matched seed within each scope/latency comparison.

Under **individual scope**, only the failed agent is forced to Rest for the next `k` steps. Under **shared scope**, failure of either agent installs the same `k`-step forced-Rest interval for both agents. If an actually depleted agent appears during recovery it is restored to `E0`; shared recovery can therefore generate additional failures through the existing Rest energy dynamics and refresh the shared interval.

Experiment 4 also changes the policy-update rule to remove the specific E3 decision-count scaling confound. Discounted returns are computed over all 50 environment steps, return mean and variance are computed over the complete 50-element return vector, score-function gradients are created only for genuine policy decisions, and the accumulated gradient is divided by the fixed horizon `50` rather than by the number of genuine decisions. A preregistered invariant required `k=0` to match the original policy update numerically when every step is a genuine decision.

Confirmatory seeds were locked to `101..130`, disjoint from earlier confirmatory seeds. The primary endpoint is policy-level: after withdrawal, frozen learned policies are evaluated on the same condition-independent bank of 2,000 paired decision-capable states. For each seed and latency, expected mutual cooperation under shared scope minus individual scope is computed. The three nonzero latencies are then averaged within seed **before** the sole confirmatory paired sign-flip test. The test uses 20,000 sign-flip resamples; the paired bootstrap interval uses 10,000 resamples.

Preregistered support requires a positive mean collapsed scope effect and two-sided `p < 0.05`. Strong manuscript-level support additionally requires a mean scope effect of at least `+0.10` with positive lower confidence bound. Latency-specific effects are secondary and cannot replace the collapsed primary test.

Prespecified mechanism diagnostics record failure-triggering action pairs, first-failure categories, active-partner actions during individual recovery, forced occupancy, eligible-decision fraction, failure frequency, and distributional/attractor summaries.

## 5. Results

### 5.1 Experiment 1: a large terminal-versus-restore difference

After the cooperation bonus is withdrawn, mean mutual cooperation is approximately `0.548` in the terminal condition and `0.0367` in the restore condition across 30 matched seeds. The historical two-sided two-sample label-permutation test gives a mean difference of approximately `+0.511` and reaches the 20,000-resample floor (`p < 0.0001`).

Because the design used matched seeds, a later paired sign-flip sensitivity analysis was applied to the same fixed outcomes. It reaches the same resampling floor: 24 of 30 paired differences are positive, 2 are zero, and 4 are negative. This is a post-hoc sensitivity analysis, not a replacement for the historical Experiment 1 test.

The zero-penalty ablation retains the separation: cooperation is about `0.50` under terminal failure and `0.05` under restoration, with both the historical label-permutation and post-hoc paired sensitivity analyses reaching the same resampling floor. The one-life to unbounded-lives gradient is strongly negative (`rho` approximately `-0.44`, `p < 0.0001`), and terminal/one-life conditions remain above restore/unbounded conditions across all six payoff-sweep cells.

The common-state frozen-policy probe also preserves the difference. At end of withdrawal, terminal policies yield mean expected mutual cooperation `0.485` on 2,292 matched mortality-free observations compared with `0.030` for restore, a paired difference of `+0.454` with 95% CI `[0.346, 0.557]` and `p < 0.0001`. At end of training the corresponding difference is `+0.503` (95% CI `[0.385, 0.612]`). The effect therefore exists in the learned policies and is not solely a consequence of unequal rollout occupancy.

The seed distribution is heterogeneous. Seventeen of 30 terminal seeds end above `0.50` post-withdrawal cooperation, while seven remain below `0.05`. The intervention appears to change the probability of entering or retaining cooperative policy basins rather than applying a uniform increment to every seed.

### 5.2 Experiment 2: persistent internal impairment does not reproduce E1

Experiment 2 clearly changed the internal viability trajectory. Damaged-agent-step fraction rises from zero under immediate recovery to about `0.53` under persistent damage, and depletion frequency also increases.

The preregistered behavioral gradient is nevertheless not supported (`rho = 0.055`, blocked-by-seed two-sided `p = 0.071`). More importantly for the programme's predefined practical threshold, the persistent-damage endpoint differs from immediate recovery by only `+0.006`, with 95% CI approximately `[-0.029, +0.044]`. That interval excludes the preregistered `+0.10` strong-effect threshold.

The correct conclusion is construct-specific. Persistent metabolic impairment that changes energy acquisition and state occupancy, while leaving immediate reward, normal actions, and reward-bearing time intact, does not reproduce the Experiment 1 cooperation effect in this testbed. This result does not establish that every form of persistent non-terminal consequence is behaviorally irrelevant.

### 5.3 Experiment 3: individual recovery latency moves in the opposite ordinal direction

Experiment 3 also passes its manipulation checks. Forced-recovery occupancy increases with latency while episode length remains fixed at 50 steps. The preregistered positive hypothesis fails. The observed ordered association is instead negative (`rho = -0.704`, `p < 0.0001`). The `k10 - k0` endpoint difference is `-0.037`, with 95% CI approximately `[-0.099, -0.003]`.

The statistic is strong in ordinal terms, but the absolute effect is modest and the regime is floor-dominated. Median cooperation is already about `0.003` at `k0` and reaches zero at `k10`. Arithmetic means are not strictly monotonic because `k2` contains several high-cooperation attractor seeds.

The common-state frozen-policy probe shows the same negative direction, so the effect is not merely produced by excluding forced-recovery steps from the cooperation denominator. However, because Experiment 3 also changes the condition-dependent decision-return normalization set and gradient averaging divisor, the negative direction should not be promoted to an architecture-general law about recovery burden.

### 5.4 Experiment 4: shared consequence scope has a small, preregistered positive effect

Experiment 4 passed its preregistered invariant gate before confirmatory execution. The first and only confirmatory run evaluated six scope/latency cells across 30 new matched seeds and the common 2,000-state policy bank.

The preregistered latency-collapsed primary effect was:

```text
mean(shared - individual) = +0.02998
95% paired bootstrap CI   = [+0.01195, +0.05387]
two-sided sign-flip p     = 0.00015
```

The confirmatory support rule therefore passes. The preregistered strong-support threshold of `+0.10` does not. The locked verdict is **positive but modest H-SCOPE support**.

The positive direction is not produced by one extreme seed. Twenty-nine of 30 collapsed seed contrasts are positive, one is negative, and the median collapsed difference is about `+0.0095`. The distribution remains right-skewed, with a few larger attractor shifts contributing substantially to the mean.

Latency-specific values are secondary:

| Recovery latency | Mean shared-individual | Median | 95% paired bootstrap CI | Positive / negative seeds |
|---|---:|---:|---|---:|
| `k=2` | +0.0075 | +0.0015 | [-0.0349, +0.0517] | 22 / 8 |
| `k=5` | +0.0618 | +0.0052 | [+0.0196, +0.1141] | 28 / 2 |
| `k=10` | +0.0206 | +0.0127 | [+0.0139, +0.0279] | 30 / 0 |

There is no monotonic increase of the scope effect with latency, and no such monotonic pattern was preregistered as necessary. A favorable latency-specific result is not substituted for the collapsed primary test.

The secondary eligible-rollout endpoint points in the same direction, with collapsed shared-minus-individual difference about `+0.033` and 95% CI approximately `[+0.012, +0.062]`.

Mechanism diagnostics qualify the interpretation. During individual recovery, the still-active partner chooses Solo roughly 91–96% of the time, while Cooperate falls from about 6% to about 2% as latency increases. This confirms a real unilateral exploitation window when only one agent is recovering. Yet failure triggers themselves are dominated by mutual-Solo states rather than by the predicted `failed Cooperate vs partner Solo` category. The stronger asymmetric-victim explanation is therefore only partially supported.

Shared recovery also changes occupancy strongly. At `k=10`, both agents are forced for about 60% of environment steps and the eligible-decision fraction falls to about 40%; shared Rest dynamics generate additional failure events. The common-state frozen-policy primary endpoint prevents this occupancy difference from mechanically defining the measured cooperation effect, but the learned policy is legitimately shaped by the training dynamics produced by shared recovery.

### 5.5 Integrated E1–E4 evidence

The four experiments now support a more specific decomposition than the v18 claim that failure cannot be placed on one severity axis.

| experiment | failure consequence | who loses normal future opportunity? | main result |
|---|---|---|---|
| E1 | episode termination | both agents lose remaining token future | large terminal > restore effect |
| E2 | persistent internal metabolic impairment | neither directly loses normal action/time | preregistered positive generalization not supported |
| E3 | temporary forced recovery | failed agent primarily | preregistered positive H1 fails; negative ordinal association |
| E4 | same temporary recovery, scope manipulated | failed agent only vs both agents | shared > individual, modest preregistered effect |

Three claims follow.

First, the original E1 phenomenon is not reproduced by simply prolonging internal damage or individual recovery burden. Second, consequence scope has an independent effect under a matched non-terminal recovery mechanism. Third, the modest size of E4 relative to E1 means consequence scope cannot currently replace terminality as the full explanation of the E1 effect.

## 6. Discussion

### 6.1 What Experiment 1 actually establishes

Experiment 1 establishes a large and robust difference between two failure transitions in this specific survival-coupled REINFORCE architecture. The terminal condition changes which policy regimes are learned and retained after cooperation subsidy withdrawal. Zero-penalty, lives-gradient, payoff-sweep, and common-state checks all reinforce that empirical fact.

But terminality is a bundled intervention. When either agent fails, both lose the remainder of the current episode-token. The return stream is truncated, later state occupancy disappears, realized trajectory length changes, and the historical policy-update normalization/averaging is applied to a shorter trajectory. Experiment 1 therefore cannot by itself identify a unique mechanism.

The important ALife question is not whether RL termination changes optimization—it does—but which aspects of a failure transition correspond to organizational dependence, shared viability, or boundary formation in artificial systems.

### 6.2 E2 shows that internal impairment without direct opportunity loss is insufficient here

Experiment 2 is most informative when its construct boundary is respected. It successfully increases damaged-state occupancy and later depletion, but the damage itself does not directly remove reward-bearing time, normal actions, or immediate reward. For a REINFORCE learner, much of the manipulation therefore reaches the objective only indirectly through changed observations and later state trajectories.

Its no-support result should not be used as a sweeping falsification of persistent consequence. What it does show is that making an internal viability variable worse and longer-lasting is not enough, by itself, to reproduce the terminal policy regime in this testbed. The confidence interval additionally excludes the programme's preregistered +0.10 endpoint effect, making the result stronger than a simple failure to cross `p < 0.05`.

### 6.3 Individual recovery burden is not equivalent to terminality

Experiment 3 tests a more functional consequence: the failed agent loses normal action opportunities for a period of environment time. Yet the result moves in the opposite ordinal direction from the preregistered prediction.

Two facts make this result especially useful. First, the frozen-policy probe confirms that learned policies themselves differ, not only rollout denominators. Second, later mechanism audit shows why the sign should not be generalized. Individual recovery changes the social interaction presented to the partner, and the partner has strong immediate incentives to choose Solo against Rest. It also changes the update's decision-conditioned normalization/scaling.

Experiment 3 therefore breaks the simple bridge from "failure is more burdensome to the unit" to "cooperation should become more stable." It does not establish a reverse universal law.

### 6.4 Consequence scope is detectable but modest

Experiment 4 isolates a narrower question by using the same non-terminal recovery mechanism under individual versus shared scope. Its preregistered positive result establishes that **who bears the temporary loss of action opportunity matters** under this architecture.

The effect is statistically clear but practically modest. This distinction matters. A low p-value does not make a +0.03 policy difference equivalent to the much larger Experiment 1 terminal-versus-restore separation. The positive direction across 29 of 30 collapsed seeds shows that the scope effect is broad, while the small median and right-skewed distribution show that its magnitude is limited and attractor-sensitive.

This is precisely why E4 is more useful as a mechanism discriminator than as a new grand result. It weakens the strongest claim that only terminality can matter. It also gives direct empirical content to the question "who bears failure?" But it leaves substantial explanatory burden for terminality, return truncation, trajectory structure, and other interaction effects.

### 6.5 Why terminality remains live

The remaining magnitude gap is scientifically important. Experiment 4 demonstrates a non-terminal scope contribution, but it does not make shared recovery look like Experiment 1 terminality. Several differences remain.

Under terminality, once either agent depletes, neither agent experiences any later state in that token. Under shared recovery, both continue through Rest transitions, accrue rewards and energy changes associated with Rest, can experience further failures, and eventually resume normal decisions. The training process therefore sees a qualitatively different sequence even when future normal action opportunities are shared.

Terminality also changes realized return length and eliminates all later within-token rewards rather than merely replacing normal actions with Rest. These features may account for much of Experiment 1's larger effect. The current evidence supports an additive or interacting role for consequence scope, not a reduction of terminality to scope.

### 6.6 A structured consequence descriptor

The evidence suggests a practical comparison rule. Statements such as "this agent can die," "recovery is costly," or "failure is irreversible" should be unpacked into transition questions.

At minimum:

1. does the declared unit continue?
2. which state/history is inherited?
3. which future actions, interactions, rewards, or viability opportunities are removed?
4. who performs recovery?
5. how much time does recovery consume?
6. **which unit or units bear those losses?**

The sixth question is the only one directly isolated by Experiment 4. The list is therefore a methodological descriptor, not a six-dimensional validated theory. Its purpose is to stop comparisons from treating different interventions as interchangeable before they have been experimentally related.

### 6.7 CSC after the experiments

CSC survives in a smaller role than earlier versions proposed. Its most useful contribution here is the insistence that a comparison declare an organizational unit, boundary, timescale, and recovery regime, and ask whether maintenance or failure costs are borne by the unit being discussed or by external infrastructure.

The experiments do not validate CSC's selective-breadth, maintenance-burden, or historical-retention dimensions. Those ideas should not occupy the evidential center of this article. Instead, CSC is best treated as the conceptual origin of the question that the experiments progressively refined.

The original scalar-like vulnerability term is not retained. E2, E3, and E4 together show that failure consequences must at least distinguish internal impairment, action-opportunity loss, and consequence scope. The result is less elegant than a single axis but more faithful to the evidence.

### 6.8 Relation to precariousness, mortality, and individuality

The consequence-scope result should not be confused with a new definition of precariousness. Enactive precariousness concerns richer organizational dependence than this small RL testbed. What E4 contributes is a controlled demonstration that organizational **scope** of a failure consequence can change learned social policy even when the same recovery mechanism is used.

This makes the result relevant to individuality and collective organization. A failure can be local to one component, or it can change the future available to a larger unit. When the latter occurs, maintaining another agent may become instrumentally relevant to one's own continuation. The present paper demonstrates only a modest version of that logic, but it provides a concrete experimental handle on a question often left implicit in artificial systems.

### 6.9 Limitations

Several limitations substantially bound the conclusions.

First, Experiment 1 was not preregistered. E2, E3, and E4 were each designed after earlier results were known, although each was locked before its own confirmatory implementation/execution. The programme therefore narrows hypotheses sequentially rather than providing one fully prospective four-experiment confirmation.

Second, all experiments use one small REINFORCE architecture. Effects may differ under actor-critic, average-reward, model-based, or population-learning systems. E4 weakens one E3-specific update confound but does not establish algorithm generality.

Third, the environment hand-designs survival coupling. Maintenance actions, energy dynamics, and recovery mechanisms do not emerge endogenously. The experiments study policy adaptation within a designed maintenance architecture, not the evolution or self-production of that architecture.

Fourth, episode-token termination is not controller destruction. Controller parameters persist across episodes. Claims about mortality must therefore remain indexed to organizational level.

Fifth, restoration to `E0 = 6` is itself environmental support. It can function as replenishment and reduce incentives to avoid depletion. This is a real property of E2–E4 rather than a neutral background fact.

Sixth, cooperation is attractor-sensitive. Means and even paired effects can be influenced by rare transitions into high-cooperation basins. We report seed distributions and common-state probes, but do not provide a full dynamical-systems account of attractor formation.

Seventh, E4's shared recovery manipulation changes more than an abstract label of "shared fate." Both agents execute the existing Rest transition during shared recovery, which has its own reward and energy consequences and can trigger additional failures. The safest mechanism label is therefore **shared failure-triggered recovery/action-opportunity consequence**, not universal shared fate.

Finally, E4's effect is small relative to E1. The paper should not present the programme as having found the unique causal owner of terminality's cooperation effect.

### 6.10 Future work and stop rule

The current evidence does not require an immediate Experiment 5. The first mechanism discriminator proposed by the E1–E3 audit has been executed once under preregistration and produced a bounded positive result. Further experimentation should be driven by a specific unresolved question rather than by a desire to increase the effect size or recover a preferred theory.

Useful next directions include direct tests of return-loss scope under fixed action availability, cleaner comparisons of joint versus individual continuation after failure, algorithm replication, evolved or learned repair, and collective systems in which organizational boundaries themselves can change. Such work would extend the present mechanism question rather than rescue a scalar vulnerability construct.

For the current article, the appropriate stopping point is the E1–E4 sequence itself: one strong discovery result, two preregistered failed generalizations, and one preregistered mechanism discriminator that identifies a real but limited scope effect.

## 7. Conclusion

Failure in an artificial agent is not fully described by saying that it is severe, recoverable, irreversible, or costly. A failure transition also has a **scope**: it determines which organizational units lose future action, interaction, return, or viability opportunities.

In the present survival-coupled multi-agent testbed, terminal failure produces a large cooperation separation relative to restoration. Persistent internal metabolic impairment does not reproduce that effect. Individual-scoped recovery latency moves in the opposite ordinal direction from the preregistered positive prediction. When the same non-terminal recovery burden is shared across both agents, cooperation increases relative to localizing the burden to the failed agent, but only modestly.

The strongest conclusion is therefore neither "mortality creates cooperation" nor "failure is multidimensional" in the abstract. It is narrower and more testable: **who bears failure-triggered future opportunity loss is an empirically relevant part of the learning problem, while terminality still contains additional causal structure that remains unresolved.**

Artificial-life comparisons should accordingly ask not only what can fail and how recovery occurs, but **who loses the future when failure happens**.

## Data and Code Availability

The reproduction package preserves the Experiment 1 code and fixed result files; the timestamped repository preregistrations, invariant tests, first confirmatory artifacts, and adjudications for Experiments 2–4; statistical procedures; and figure-generation assets.

Experiment 1 retains its historical two-sample label-permutation analysis. A separate post-hoc paired sign-flip sensitivity audit is reproduced directly from the committed outcomes without retraining or replacing the historical result.

Experiments 2, 3, and 4 use **timestamped repository preregistrations**, not third-party preregistration services. In each case the locked design commit predates confirmatory implementation/execution. Experiment 4's first and only confirmatory run and artifact are additionally identified by run/artifact IDs and SHA-256 hashes in the repository adjudication record.

The historical code uses the regime label `real` for the Experiment 1 terminal condition. The manuscript uses **terminal** to avoid implying that one software condition possesses metaphysically "real" stakes.

A static reviewer reproduction package should be provided through a route that does not require reviewers to reveal identity through repository permissions or authentication logs.

## AI Assistance Disclosure

OpenAI ChatGPT was used during the September 2026 revision process for literature organization, manuscript restructuring, wording assistance, code-review support, experimental-governance checks, and consistency review, including GPT-5.6 Sol during the E1–E4 evidence-led reconstruction. Reported numerical results derive from committed experiment code and preserved result artifacts rather than from generative-model output. The author determined the hypotheses, approved the preregistrations, accepted unfavorable confirmatory outcomes, verified claims against preserved outputs, and takes responsibility for the manuscript.

## References

- Aguilera, M., Millidge, B., Tschantz, A., & Buckley, C. L. (2022). How particular is the physics of the free energy principle? *Physics of Life Reviews, 40*, 24–50.
- Beer, R. D. (1995). A dynamical systems perspective on agent-environment interaction. *Artificial Intelligence, 72*(1–2), 173–215.
- Beer, R. D. (2004). Autopoiesis and cognition in the Game of Life. *Artificial Life, 10*(3), 309–326.
- Beer, R. D., & Di Paolo, E. A. (2023). The theoretical foundations of enaction: Precariousness. *BioSystems, 223*, 104823. https://doi.org/10.1016/j.biosystems.2022.104823
- Boutilier, C., Cohen, A., Daniely, A., Hassidim, A., Mansour, Y., Meshi, O., Mladenov, M., & Schuurmans, D. (2018). Planning and learning with stochastic action sets. In *Proceedings of the Twenty-Seventh International Joint Conference on Artificial Intelligence* (pp. 4674–4682). https://doi.org/10.24963/ijcai.2018/650
- Chan, B. W.-C. (2019). Lenia: Biology of artificial life. *Complex Systems, 28*(3), 251–286.
- Chandak, Y., Theocharous, G., Metevier, B., & Thomas, P. S. (2020). Reinforcement learning when all actions are not always available. *Proceedings of the AAAI Conference on Artificial Intelligence, 34*(04), 3381–3388. https://doi.org/10.1609/aaai.v34i04.5740
- Chen, S., & Chen, T. (2026). Synthetic Linguistic Agency: How an Embodied Mortal Agent Learns Linguistic Affordances through Consequential Social Experience. *arXiv preprint arXiv:2608.27843*.
- Damiano, L., & Stano, P. (2020). On the "life-likeness" of synthetic cells. *Frontiers in Bioengineering and Biotechnology, 8*, 953. https://doi.org/10.3389/fbioe.2020.00953
- Di Paolo, E. A. (2005). Autopoiesis, adaptivity, teleology, agency. *Phenomenology and the Cognitive Sciences, 4*(4), 429–452.
- Egbert, M. D., & Barandiaran, X. E. (2011). Quantifying normative behavior and precariousness in adaptive agency. In *Advances in Artificial Life (ECAL 2011)* (pp. 210–217).
- Friston, K. J. (2013). Life as we know it. *Journal of the Royal Society Interface, 10*(86), 20130475.
- Hisaki, Y., & Ono, I. (2024). RVI-SAC: Average reward off-policy deep reinforcement learning. In *Proceedings of the 41st International Conference on Machine Learning* (PMLR 235, pp. 18352–18373).
- Kirchhoff, M. D., Parr, T., Palacios, E., Friston, K. J., & Kiverstein, J. (2018). The Markov blankets of life: Autonomy, active inference and the free energy principle. *Journal of the Royal Society Interface, 15*(138), 20170792.
- Korecki, M., Carissimo, C., & Lund, T. (2023). aRtificiaL death: learning from stories of failure. *Proceedings of the 2023 Conference on Artificial Life*, 41. https://doi.org/10.1162/isal_a_00633
- Maturana, H. R., & Varela, F. J. (1980). *Autopoiesis and Cognition: The Realization of the Living*. Reidel.
- Moreno, A., & Mossio, M. (2015). *Biological Autonomy: A Philosophical and Theoretical Enquiry*. Springer.
- Raja, V., Valluri, D., Baggs, E., Chemero, A., & Anderson, M. L. (2021). The Markov blanket trick: On the scope of the free energy principle and active inference. *Physics of Life Reviews, 39*, 49–72.
- Williams, R. J. (1992). Simple statistical gradient-following algorithms for connectionist reinforcement learning. *Machine Learning, 8*, 229–256.
- Witkowski, O., & Schwitzgebel, E. (2024). The ethics of life as it could be: Do we have moral obligations to artificial life? *Artificial Life, 30*(2), 193–215. https://doi.org/10.1162/artl_a_00436

## Appendix A. Experiment 1 Details

### A.1 Environment

Two agents share a symmetric survival environment with horizon `T = 50`. Each has initial energy `E0 = 6`, cap `Emax = 10`, and fixed metabolic cost `1.0` per step. The immediate reward / energy-gain matrix is:

| own \\ partner | cooperate | solo | rest |
|---|---|---|---|
| cooperate | 1.0 / +2.0 | 0.0 / +0.0 | 0.2 / +0.4 |
| solo | 1.4 / +1.2 | 0.6 / +0.7 | 0.9 / +1.0 |
| rest | 0.25 / +0.5 | 0.25 / +0.5 | 0.25 / +0.5 |

A metabolic cost of `1.0` is then subtracted. Thus mutual cooperation produces positive net energy while mutual solo gradually depletes both agents.

### A.2 Policy and training

Each policy has 12 input features, 16 tanh hidden units, and three action logits. REINFORCE uses standardized discounted returns, learning rate `0.04`, and `gamma = 0.97`. Training lasts 1,000 episodes with cooperation bonus `1.0`; withdrawal lasts 300 episodes with the bonus removed and learning continuing. Main, zero-penalty, and lives-gradient experiments use 30 paired seeds; payoff-sweep cells use 15 paired seeds.

### A.3 Common-state probe

Held-out policies from bank-generation seeds `1001–1010`, disjoint from evaluation seeds `1–30`, generate mortality-free observation states. States are stratified by energy and time-to-horizon; equal numbers from terminal and restore regimes are drawn within shared-support cells. The final bank contains 2,292 paired observations. Frozen policies are evaluated without learning using expected mutual cooperation `P(CC|s) = P1(C|s1) × P2(C|s2)`.

## Appendix B. Experiment 2 Confirmatory Guard

Experiment 2 preregistered ordered damage-persistence conditions, paired seeds `1–30`, its blocked-by-seed primary test, significance rule, and `+0.10` endpoint threshold before confirmatory execution. Its first confirmatory artifact is preserved. No post-result retuning replaced the no-support outcome.

## Appendix C. Experiment 3 Confirmatory Guard

Experiment 3 was separately preregistered after the Experiment 2 result. Before confirmatory seeds `1–30` were run, latency levels `0/2/5/10`, fixed 50-step horizon, immediate rescue, zero new failure penalty, eligible-step primary endpoint, blocked-by-seed permutation test, common-state secondary probe, and `+0.10` endpoint threshold were locked. The first confirmatory artifact is preserved. The observed negative direction is reported without reversing the preregistered positive hypothesis after seeing the data.

## Appendix D. Experiment 4 Confirmatory Guard

Experiment 4 was preregistered after the E1–E3 mechanism audit and before implementation or confirmatory execution. It locked individual versus shared scope, nonzero latencies `2/5/10`, new seeds `101..130`, fixed 50-step horizon, immediate rescue, zero failure penalty, fixed-horizon return normalization and gradient scaling, a common 2,000-state frozen-policy primary endpoint, latency-collapsed paired sign-flip inference, and the `+0.10` strong-effect threshold. The first and only confirmatory run produced Outcome B: positive but modest scope support. No second confirmatory run or parameter retuning is permitted under that preregistration.
