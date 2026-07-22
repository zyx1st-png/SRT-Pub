# 1. Introduction

> Draft of manuscript Section 1. Constraints: single identification question; no
> full SRT / ontology / consciousness / value content; "to our knowledge" on the
> exclusivity claim; no piling of result numbers (numbers live in Sections 5–7).

Two systems can behave identically now and yet not be the same system. One has
merely arrived at a state; the other has been shaped by how it arrived — and the
difference, if it exists, lives entirely in the future: in which outcomes each
system can still reach, how easily, and at what cost when the world changes. The
question this paper addresses is whether that difference can be made
experimentally real in the strictest sense: **after the observable present is
matched — same state, same fast values, same action distribution — can a system's
selection history still hide a different future reachability, carried by nothing
but a slow, history-formed memory?**

The question is easy to blur because several familiar phenomena sit next to it
without answering it. A state that persists after its support is withdrawn may
simply have fallen into a basin that was always there; persistence alone does not
show that anything was written. A transition rule that has changed may have
changed indiscriminately — noise-roughened, globally perturbed — without favoring
what the system actually selected; plasticity alone does not show that the
selection mattered. A system whose future updates are modulated by past surprise
exhibits history dependence of a real but generic kind — any passive observer of
the same event stream would carry the same trace. And a system held in place by an
external controller occupies its state without owning it. Persistence,
generic plasticity, volatility tracking, and clamped occupancy are four ways of
looking historical without being historical in the sense at issue here: none of
them requires that the system's *own selections, through their consequences*,
restructured what it can become.

There is, accordingly, an identification gap rather than a theory gap. Dynamical
systems theory quantifies stability and hysteresis; control theory quantifies the
cost of reaching and holding states; reinforcement learning and metaplasticity
describe how experience reshapes future updates; predictive-processing accounts
describe regulation under changing statistics. Each supplies constructs we use
freely in what follows. Individually, the ingredients are familiar — the
action→outcome information family [Klyubin et al. 2005; Seitzer et al. 2021], its use
as a learning signal [Mohamed and Rezende 2015; Gregor et al. 2016], gated
consolidation [Lindsey and Litwin-Kumar 2024], and future-occupancy representations
[Dayan 1993] — and the intuition that indistinguishable observations can hide
different consequences is the classic problem of perceptual aliasing [Whitehead and
Ballard 1991]. What we assemble from these is a specific identification test: match
the present completely at the level of observables, vary only the history-formed slow
memory, and determine whether — and in which direction — the future behavioral
arrival distribution changes, under yoked and sham controls that differentiate
selection-specific history from generic exposure history. **To our knowledge, no
close protocol-level precedent combining these elements was identified in our
search.**

This paper builds that test and runs it end to end in designed systems. The
battery has three components. *Matched present*: at test time the environment
state, the fast values, and hence the initial action distribution are reset
identically for all agents; the only quantity carried from the past is the slow
memory. *Master-yoked control*: a paired agent receives the identical reward
stream with the action→outcome coupling cut, so that anything driven by exposure
statistics alone appears equally in both arms. *External-action sham*: outcomes
are driven by an observable external action, so that controllable structure is
present in the stream but is not attributable to the agent's own choices. Around
this battery we impose a pre-registration discipline — calibration on dedicated
seeds, frozen parameters and thresholds, fresh-seed holdouts, equivalence bounds
for every claimed null — and an adversarial audit of the finished chain that
separates load-bearing evidence from pipeline validation.

The chain includes a negative result, and we keep it in the main line of the
argument. Our first mechanism — a slow variable accumulating absolute prediction
error, the most natural reading of "history writes itself into the system" —
passed its feasibility gate and then failed the yoked control on a locked holdout:
the yoked agent, with no choice–consequence coupling at all, reproduced the future
effect. That NO-GO is retained frozen, is reported as a primary result, and is
what forced the mechanism revision at the center of the paper: replacing
accumulated surprise with *action-attributable predictive information* — how much
the agent's own chosen action improves outcome prediction over a fixed reference
mixture of the actions it could have taken.

The contributions are four, and all are deliberately limited to designed models.
First, a construct separation: persistence, general rule change, and
selection-specific write-back are shown to be bidirectionally dissociable in a
constructive system, with portable measurement instruments for each. Second, a
negative result: prediction-error accumulation yields history-dependent
metaplasticity that is not selection-specific. Third, a mechanism: action-
attributable predictive information can gate the formation of path-specific
memory, and does so selection-specifically under yoked and sham controls. Fourth,
a behavioral demonstration: with the present matched, a history-formed memory
redirects future arrival distributions directionally — history-aligned advantage
purchased at the price of perseverative cost when the old path is blocked or the
goal is new. What the paper offers, in sum, is not a discovery about any natural
system but an identification framework with a worked, falsifiable instance —
including one genuine failure that the framework itself caught.
