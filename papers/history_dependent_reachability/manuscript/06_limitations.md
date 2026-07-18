# 10. Limitations

> Draft of manuscript Section 10. Constraints: CLAIM_LEDGER.md (forbidden claims)
> and Experiments/AUDIT.md. No Discussion content here; bridging and outlook live
> in Section 9.

**1. Everything shown is a designed model.** All five systems were constructed to
make the constructs separable and the identification clean. The results are
constructive existence and identification results: they show that persistence,
nonspecific rule change, and selection-specific write-back *can* be dissociated,
that a selection-contingent consolidation mechanism *can* be built and detected
under yoked and sham controls, and that a written path memory *can* redirect
future reachability under a matched present. They do not show that any natural
system — biological, neural, or social — implements this architecture, and no
claim in this paper should be read as empirical evidence about natural systems.

**2. The m → future channel is part of the architecture, not a discovery.** In
the tiny-MDP, the consolidated memory shapes the future through a bounded
retention pull that we defined. What the experiments establish is conditional:
*given* such a channel, action-attributable gating plus consolidated content
produce directional reachability restructuring that survives the identification
battery. The existence of the channel itself is an architectural premise —
demonstrated to be buildable, not discovered in any target system. The same
holds for the double-well system, where the plasticity channel z was likewise
defined into the dynamics.

**3. Phase 2c's pre-registered bootstrap unit overstates its effective sample.**
The frozen Phase 2c holdout pooled seed × volatility cells (80 values from 40 seeds)
rather than resampling seeds. We retain that pre-registered interval as provenance
and additionally report a post-audit seed-clustered bootstrap (average the two
volatility cells per seed, then resample the 40 seeds) as the preferred inferential
summary; the two agree in direction and conclusion (Results 3.3), and the frozen GO
is unchanged. Regardless, Phase 2c is positioned as mechanism feasibility only; the
confirmatory statistics of this paper come exclusively from the tiny-MDP holdout,
whose bootstrap unit is the seed (50 units, 10,000 paired resamples).

**4. The narrow confidence intervals measure model reproducibility, not
construct confidence.** Intervals such as macro-TV [0.374, 0.375] arise because
each per-seed statistic averages N = 400 agents of a frozen deterministic model.
They quantify cross-seed reproducibility of that model and must not be read as
high confidence in the constructs, nor as robustness to architectural,
parametric, or environmental variation. Construct-level uncertainty is not
estimated anywhere in this paper.

**5. The ablation battery is pipeline validation, not causal isolation.**
memory-swap is mechanical (zero by construction), memory-null is
architecture-bound (a residual between two diffuse memories inside the
future = f(m) design), and same-m/different-z is structural (the future task
takes no z argument). They verify the only-m plumbing and nothing more
(Section 8.3). The causal weight of the paper rests on the formation-side
active/yoked/sham comparisons, where the data decide the outcome.

**6. No validation beyond designed systems.** The mechanism has not been tested
in end-to-end trained networks, in biological preparations, or in humans. Our
earlier attempt to run a matched-endpoint history test in an end-to-end
image classifier (Fashion-MNIST) ended in an identification NO-GO: no valid
matched groups existed because history and endpoint live in the same weight
vector. That result is a failure of *that protocol under that architecture* —
it must not be read as evidence that history-dependent reachability is absent
or unidentifiable in end-to-end systems in general. Identifying architectures
in which fast state can be matched while slow history varies remains open
outside designed models.

**7. Scale and scope of the environments.** The systems are deliberately
minimal: one-dimensional dynamics, two- and three-armed bandits, a two-step MDP
with three goals. Role counterbalancing, interior (non-saturated) operating
points, and pre-registered thresholds mitigate — but do not remove — the risk
that the effect sizes are idiosyncratic to small state spaces. The
pre-registered thresholds (Δ_min, equivalence bounds) are themselves
model-relative conventions, not theoretically derived quantities.

**8. Deferred components.** The external-action sham was added only at the
tiny-MDP stage (Phase 2c v1 omitted it rather than duplicate a hidden yoked
control); the latent-inscription condition is established at selection-episode
scale only, and its durable form was obtained only after replacing the
state-tracking slow variable with the two-timescale architecture. The per-class
four-bar arrival distributions and the latent erosion were completed by the
authorized extraction round; the latter is reported only as a **two-point erosion
comparison** (episode-end vs end-of-observation z), because a per-step record is not
extractable without editing frozen code.

**9. What this paper does not claim.** Per the claim ledger fixed before
drafting: no claim that natural systems exhibit historicity write-back; no claim
about the general ontology of possibility spaces; no claim that selection
precedes existence; no claims about value, subjecthood, or consciousness; no
claim of superiority over the free-energy principle, integrated information
theory, or reinforcement-learning accounts of habit — the relation to these
frameworks is complementarity of question, addressed in Section 9; and no
reading of the reported intervals as construct-level confidence.
