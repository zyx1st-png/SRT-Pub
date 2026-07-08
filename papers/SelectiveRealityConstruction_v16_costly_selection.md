# Costly Selection: A Minimal Criterion for Life-Likeness in Artificial Systems

[Author Name(s)]

[Affiliation(s)]

[Contact Email]

## Abstract

Artificial life still lacks an operational criterion for life-likeness. Existing markers such as metabolism, autopoiesis, adaptive behavior, and predictive closure capture part of the target, but they often blur the difference between systems that merely update and systems that must sustain an organized mode of existence. This paper proposes a minimal criterion: life-likeness consists in **costly selective closure**. Four coupled dimensions make the claim explicit: selective bandwidth (`d`), maintenance cost (`Ψ_f`), hysteretic memory (`η`), and irreversible vulnerability (`V`). Together they distinguish passive from active closure and make token-level irreversibility central to the boundary between buffered simulation and stake-bearing organization. A controlled two-agent experiment isolates the vulnerability dimension. Two independent reinforcement learners face an identical survival dilemma that differs in one variable only: whether energy depletion terminates the agent (real stake) or cheaply resets it (buffered stake). Under a matched reward function, only the real-stake regime stabilizes costly cooperation once the explicit cooperation incentive is withdrawn (post-withdrawal mutual cooperation `0.55` versus `0.04`, 30 seeds, `p < 0.0001`). The effect persists with no explicit death penalty, holds across a payoff sweep, and forms a monotone dose-response as the number of allowed respawns increases from one to infinity. This isolates the causal role of token-level irreversibility rather than validating the full four-dimensional criterion; it offers a buildable, comparative heuristic for probing when artificial systems sustain genuinely life-like commitments.

**Keywords**: artificial life, life-likeness, autopoiesis, active closure, vulnerability, minimal cognition, artificial agents


## 1. Introduction

Artificial life has always been both a technical program and a philosophical method. Instead of asking only what life is in the abstract, it asks what must be built, varied, and maintained for something life-like to appear. The question is therefore not only classificatory. It is operational: what should count as a success condition for artificial life?

This remains unsettled. Different traditions emphasize different signatures. Self-reproduction captures evolutionary open-endedness but excludes sterile organisms and many familiar living phases. Metabolism captures energetic organization but risks including fire. Autopoiesis captures self-producing organization and organizational closure (Maturana and Varela, 1980), but is often difficult to compare across substrates (Moreno and Mossio, 2015). More recent frameworks based on predictive processing or active inference highlight adaptive regulation and boundary maintenance, but by their generality they can blur the difference between organisms, thermostats, and highly capable digital agents. The present proposal also sits alongside work on minimal autonomous systems, enactive artificial intelligence, and recent basal-cognition approaches that treat cognition and life-like agency as graded across phylogeny (Ruiz-Mirazo et al., 2004; Froese and Ziemke, 2009; Lyon et al., 2021; Lyon and Cheng, 2023). It is also sympathetic to Thompson's life-mind continuity thesis, while departing from it in treating organizational closure as necessary but not by itself sufficient for stronger forms of life-likeness (Thompson, 2007).

For artificial life, this creates a practical problem. Without a shared operational criterion, systems with very different ontological profiles are often discussed in the same vocabulary of "adaptation," "agency," or "self-maintenance." We can describe Conway patterns, Lenia morphologies, soft robots, language models, and bacteria as exhibiting some kind of organization, but not all organization is equally life-like. A criterion is needed that is broad enough to compare unlike systems while still sharp enough to distinguish mere update from consequential self-maintenance.

This paper proposes such a criterion. Drawing on Selective Reality Theory (SRT), but stating the argument in a self-contained way that does not require commitment to SRT as a broader metaphysics, it argues that the minimal signature of life-likeness is **costly selective closure** (Zhang, 2026). A life-like system is not merely one that persists, computes, or reproduces. It is one that:

1. selectively couples to a non-trivial portion of its world,
2. pays a non-zero cost to maintain that coupling,
3. carries the effects of past selections forward in memory and structure, and
4. faces meaningful consequences if its regulation fails.

The point is not to introduce a new essence of life. It is to give artificial life a buildable discrimination rule. On this view, life-likeness is a gradient rather than a binary threshold. Systems can be more or less life-like depending on the degree to which they exhibit selective bandwidth, maintenance cost, hysteresis, and vulnerability.


## 2. Why Existing Criteria Stop Too Early

Classical definitions of life usually succeed by being locally right and globally incomplete. Reproduction identifies one important route by which life persists through time, but not all living systems are reproducing at every moment, and many life-like artifacts may never reproduce at all. Metabolism captures energetic openness and thermodynamic work (Schrödinger, 1944), but by itself it says too little about selectivity or organization. Autopoiesis comes closer by focusing on self-producing organization, yet its explanatory strength can become a weakness when researchers need tractable comparisons across different media.

The same problem appears in more recent discussions of adaptive systems. A system can maintain a boundary, minimize error, or stabilize a policy without this being enough to make it meaningfully life-like. A thermostat is organized, robust, and responsive. A large language model can exhibit astonishing behavioral complexity. A reinforcement-learning agent can maximize reward under changing conditions. Yet there remains an intuitive and theoretical difference between systems that merely implement a designer's structure and systems whose way of existing is itself under stake.

The missing distinction is between **update** and **consequential self-maintenance**.

Many systems update. Far fewer must continuously pay to remain what they are. In ordinary biological cases, failure has non-trivial consequences: the organism exhausts energy, loses integrity, suffers damage, or dies. Its regulatory activity therefore has existential weight. By contrast, many computational systems operate under extensive buffering. They may be reset, copied, restored, paused, or run again with little cost to their identity. They can display goal-directed behavior without bearing much of the burden that makes biological regulation matter.

Artificial life needs a criterion that can register this difference without collapsing into substrate chauvinism. The criterion should not require carbon chemistry. But neither should every well-regulated or behaviorally rich system be treated as equally life-like. The question is not whether a system behaves as if it had a world. The question is whether it must selectively construct and maintain such a world under real cost and consequence.

This also clarifies the relation to active inference. Active inference provides a powerful account of adaptive regulation under a Markov blanket, but by design it does not distinguish between systems that maintain that blanket at negligible cost to themselves and systems for which boundary-maintenance is existentially burdensome (Friston, 2013; Kirchhoff et al., 2018). For a broader survey of mathematical approaches to agents, many of them predating active inference, see Baltieri and Suzuki (2025). Recent analyses of the free-energy principle (FEP) in concrete stochastic systems, and recent critiques of blanket-based generalization, reinforce the point that broad descriptive coverage does not by itself settle what kind of organized system is under study (Raja et al., 2021; Aguilera et al., 2022). The present framework adds that distinction through the vulnerability dimension `V`: two systems may be equally well-described by active inference while differing sharply in life-likeness if one can be freely reset and the other cannot. What `V` adds is therefore not the generic idea that systems resist dispersion. FEP already captures that descriptive insight. The added claim is about token-level irreversibility: whether failure is borne by the individual system whose organization is at issue, or whether loss is cheaply externalized and reversed by the surrounding setup.

A natural objection arises: does `V` simply reintroduce a subtler form of chauvinism by favoring media with irreversible physical loss? The framework's answer is no. It does not privilege carbon, metabolism, or any specific material substrate. What it requires is that the continued organization of the token system be non-trivially at stake. In principle, a digital system could satisfy this condition if its persistence were bound to local irreversible processes rather than to cheap perfect restoration. A simple thought experiment would be an embodied digital agent tied to aging edge hardware with no maintained backup, or an irrevocable smart-contract agent whose local state transitions cannot be rolled back without destroying the token process under evaluation. What is excluded is not digitality as such, but architectures in which losses are systematically externalized and undone by design.

A deeper objection targets the biological relevance of token-level irreversibility. In evolutionary biology, what is conserved is often information at the level of the lineage or population, not the individual organism; a population of adequate size supplies precisely the kind of cheap backup that the framework treats as reducing life-likeness, and suicidal altruism seems to show that the token organism is dispensable while only the information matters. Two replies are needed. First, the present claim is deliberately about the token organized system, not about the unit of selection. Whether a lineage is buffered is orthogonal to whether a particular organized process bears the cost of its own maintenance: the redundancy of a species does not make an individual bacterium's self-production any less costly, nor its failure any less terminal for that bacterium. The framework grades the life-likeness of the token that maintains itself and stays silent about which units evolution optimizes. Second, and conceding part of the objection, the framework does not require that irreversibility be learnable by the token from its own destruction. A system need not, and generally cannot, learn from its own death. The claim is weaker and testable: whether failure is token-terminal or cheaply reversible changes the selective pressure on an organized process, even when that pressure is applied across many trials rather than experienced within a single life (Watson and Szathmáry, 2016). Section 4.5 exhibits exactly this structure. The pressure that stabilizes costly self-maintenance is exerted across a population of episodes, yet what it settles on depends entirely on whether each episode's failure is terminal. Token-level irreversibility is therefore not an observer's relabeling of otherwise identical dynamics; it is a control variable that demonstrably reshapes what an adaptive process becomes.


## 3. Costly Selective Closure

### 3.1 Selective Construction

The proposed framework begins with a simple thought: every candidate system faces a space of possible states, perturbations, and interactions. Life-like systems do not passively occupy this space. They selectively stabilize a small and usable region of it.

If one wants a compact bookkeeping vocabulary, it is helpful to name three layers. `L0` denotes the open possibility space available to a system, `L1` its currently maintained manifest state, and `L2` the relatively stable structures sedimented by prior successful selection. These labels are optional: the substantive point is simply to distinguish possibility space, current organization, and retained constraint.

Let `Omega_t` denote the system's currently accessible possibility space and `x_t` its maintained state. We can write the next state schematically as

$$
x_{t+1} = (1 - \eta)\,\hat{G}_{\theta}[\Omega_t] + \eta x_t
$$

where `G_hat_theta` is a selection operator and `eta in [0,1]` is a hysteresis term. The equation is intentionally minimal. It says only that current organization depends partly on present selection and partly on retained structure from the past. When `eta = 0`, the system is purely reactive. When `eta > 0`, previous selections constrain current ones.

This process can be called **selective reality construction**: a system does not encounter all possible states equally, but compresses possibilities into an actionable world. In artificial systems, the same question can be posed constructively: what dimensions does the system track, what does it ignore, and what does it take to keep that selection stable?

### 3.2 Four Dimensions

The degree of life-likeness is evaluated along four coupled dimensions.

**Selective bandwidth (`d`).** This is the effective dimensionality of the system's selective coupling to its environment. One convenient formalization is the effective rank of the operator's spectrum:

$$
d = D_{eff}(\hat{G}) = \frac{(\sum_i \lambda_i)^2}{\sum_i \lambda_i^2}
$$

where the `lambda_i` are the salient eigenvalues of the system's selective dynamics. Intuitively, `d` tracks how many independent dimensions genuinely matter to the system. A low-`d` system couples along one or a few tightly constrained dimensions. A high-`d` system maintains concern across a wider space of temporal, spatial, social, or behavioral variables.

For cross-substrate comparison, `d` can also be decomposed into a more operational proxy:

$$
d_{cog} \approx w_A A(\sigma) + w_V \log V_{concern} + w_\tau \tau_{temporal}
$$

where `A(sigma)` is assembly depth, `V_concern` is the spatial or social scope of relevant variables, and `tau_temporal` is the effective planning horizon. The coefficients `w_A`, `w_V`, and `w_tau` are weighting parameters whose values depend on the comparison context; the decomposition is not a prediction rule but a heuristic for ensuring that comparisons across substrates attend to the same underlying factors. In particular, assembly depth provides one promising substrate-neutral anchor for the complexity term (Sharma et al., 2023).

**Maintenance cost (`Psi_f`).** A system may display organized behavior while paying little of the cost itself. `Psi_f` denotes the burden of maintaining the selected state against drift, dispersion, or collapse. Crucially, it is not gross energy expenditure measured by an outside observer, but the maintenance burden borne by the system as a condition of preserving its own token organization. A large language model may consume substantial external GPU energy while still ranking low on `Psi_f` in this sense if failure does not threaten the persistence of its own state and checkpoints make restoration cheap. Operationally, a cost contributes to `Psi_f` only when it loads the persistence variables that the system itself must keep within bounds to remain the same token organization. Costs absorbed by trainers, servers, reset logic, or redundant backup infrastructure do not count unless failure propagates back to those persistence variables. Borderline cases such as cloud-hosted agents or hot-swappable distributed systems therefore yield interval estimates rather than sharp values.

**Hysteretic memory (`eta`).** Life-like systems do not simply react in the present. Their prior selections sediment into present organization. `eta` measures this historical carry-over. It is not just explicit memory storage; it includes any mechanism by which past regulation becomes embodied as current bias, constraint, or habit.

**Irreversible vulnerability (`V`).** Finally, a system becomes more life-like when failure cannot be costlessly undone. `V > 0` means that bad regulation has non-trivial consequences for the continuation of the system's organization. This need not imply literal death in every artificial case, but it does require more than symbolic risk. In enactive terms, `V` captures a formal analogue of precariousness (Di Paolo, 2005; Egbert and Barandiaran, 2011). Operationally, `V` is assessed over the system-in-environment pair rather than over bare code. Reset availability matters because it determines whether perturbations terminate the token organization or merely pause it under external protection. In that sense `V` is partly architecture-relative by design: life-likeness here is a property of an organized process under a maintenance regime, not of an implementation abstracted from that regime.

The decisive ingredient tying `Psi_f` and `V` together is **token-level irreversibility**. A perturbation matters for life-likeness only when its consequences are borne by the particular organized token under evaluation, rather than being offloaded to a surrounding infrastructure that can restore the token cheaply. This is the sense in which the framework aims to distinguish real stake from buffered simulation.

These four dimensions are coupled by a simple viability inequality, in the spirit of viability theory (Aubin, 1991):

$$
\frac{dq}{dt} \le \kappa_1 P_{sel} - \kappa_2 \Psi_f - \kappa_3 N
$$

where `q` is organized order, `P_sel` is selection power, and `N` is noise or perturbation pressure. A life-like system remains viable only when it can generate enough selective power to offset maintenance cost and noise. Existence is therefore not a default state; it is a managed achievement.

### 3.3 Passive and Active Closure

The framework distinguishes two broad regimes.

**Passive closure** describes systems that appear organized but whose organization is heavily buffered by external design, reset, or negligible consequence. They may be elegant, adaptive, and even behaviorally rich, yet they do not bear much of the burden of their own continued organization.

**Active closure** describes systems that must continuously pay to maintain their selected state, carry prior regulation forward, and risk genuine degradation if they fail.

This distinction matters because many debates about artificial life conflate the two. A system may display convincing local closure while remaining weakly life-like overall because its cost, memory, or vulnerability are shallow. The question is not whether closure exists at all, but whether it is passive or active.

### 3.4 Status of the Formalization

The formalism above should be read as a qualitative-to-semi-quantitative comparison framework, not as a closed dynamical theory. The update equation is schematic: it states that current organization depends on present selection and retained history, but it does not assume that `\hat{G}_theta` is linear, deterministic, or defined over a Euclidean state space. When state spaces are non-Euclidean, the weighted update should be understood as shorthand for any compatible local representation or state-update rule that preserves the same conceptual roles.

Likewise, the effective-rank definition of `d` is the principal definition, whereas `d_cog` is an operational proxy intended for comparative work across substrates. The latter does not replace the former; it offers a practical route for approximate estimation when the full operator spectrum is not available. Finally, `q`, `P_sel`, and `N` in the viability inequality should be treated as task-specific observables rather than already-standardized measurements. Difficult cases remain: systems with mirrored state, elastic cloud persistence, or dynamically shifting boundaries may only admit scenario-dependent estimates for `Psi_f` and `V`. The present framework is therefore best understood as a disciplined heuristic grammar for comparison and experiment design, not yet as a directly computable model.


## 4. Canonical Cases

Table 1 summarizes the framework's verdict on several familiar cases. The entries should be read as order-of-magnitude heuristic placements rather than measured quantities. At present the table is best understood as an ordinal scaffold for comparison: its value is to localize disagreement to one or more dimensions, not yet to report a calibrated ratio-scale measurement.

| System | `d` | `Psi_f` | `eta` | `V` | Verdict |
|---|---|---|---|---|---|
| Crystal | 0 | None | None | None | Stable but not life-like |
| Conway's Game of Life pattern | ~0 | None | Very low | None | Organized update, not active closure |
| Lenia morphology | ~1-3 | Low/emergent | Low | Low | Weakly life-like |
| Autopoietic/evolved embodied agent | ~5-20 | Positive | Positive | Positive | Moderately life-like |
| Resettable RL agent | ~2-20 | Often externally buffered | Positive | Weak | Behaviorally rich but ontologically shallow |
| Biological organism | ~10^2-10^4 | Positive | Positive | Strong | Strong active closure |

### 4.1 Conway's Game of Life

Game of Life (Gardner, 1970), heir to von Neumann's self-reproducing automata (von Neumann, 1966), remains a foundational example because it demonstrates how surprising pattern formation can emerge from simple rules. Yet, under the present framework, it ranks low in life-likeness. Patterns localize and persist, but they do not bear non-trivial cost, retain history in a robust sense, or face consequential failure. The most sustained attempt to read a Game of Life pattern as an autopoietic individual (Beer, 2004) is instructive here: it recovers organizational closure and structural coupling, but the pattern's self-production remains a feature of the observer's descriptive stance rather than a cost borne by the token to remain what it is. The system updates according to fixed rules; it does not actively maintain a selected mode of existence under burden.

### 4.2 Lenia

Lenia (Chan, 2019) is more interesting because it produces morphologies with clear behavioral coherence. Patterns move, stabilize, regenerate, and sometimes appear to "seek" conditions that preserve form. This gives Lenia stronger localization and a weak analogue of maintenance cost: the pattern must continually sustain itself against dispersion. The placement `d ~ 1-3` reflects the fact that Lenia's update kernel and stable morphologies usually organize variation around a small number of dominant spatial modes, such as translation, oscillation, and orientation, rather than a broad set of independently weighted environmental variables. Even so, its hysteresis is limited and its vulnerability is shallow compared with embodied agents. It is therefore best described as weakly life-like.

### 4.3 Autopoietic Agents

Embodied autopoietic or evolved agents in the dynamical-systems and enactive tradition (Beer, 1995; Di Paolo, 2005) score higher. They regulate sensorimotor coupling, maintain a boundary, and can fail in ways that matter for continued performance. Their current activity is constrained by prior adaptation, which gives them a meaningful `eta`, and their continued organization requires ongoing work, which gives them positive `Psi_f`. The rough placement `d ~ 5-20` should be read as assuming a system that must jointly track several partially independent variables, for example resource gradient, orientation, collision risk, boundary integrity, and a small number of partner or obstacle states, without yet exhibiting the broader temporal and social concern-spaces of complex organisms. Such systems are among the clearest artificial demonstrations of active closure currently available.

### 4.4 Resettable Digital Agents

Many contemporary digital agents complicate the picture. Reinforcement-learning systems can exhibit substantial behavioral flexibility and therefore non-trivial `d`, but the scale of `d` depends strongly on architecture and task. The deliberately minimal cooperative experiment discussed below yields `d_eff` values below 2, whereas richer agents with broader sensory, temporal, or social coupling could plausibly extend into the teens. They may also carry substantial training history and internal state, giving them non-trivial `eta`. But if their organization is extensively buffered by cheap reset, abundant copying, and negligible irreversible loss, then `V` remains weak and `Psi_f` is not borne by the agent in a robust sense. They are therefore best treated as partial life-likeness: high behavioral sophistication under shallow stake conditions. The same point applies, even more strongly, to contemporary large language models.

### 4.5 A Controlled Experiment: Isolating the Vulnerability Dimension

To test whether token-level irreversibility does causal work rather than merely labeling systems after the fact, we run a controlled two-agent experiment in a PettingZoo-style cooperative survival environment (Terry et al., 2021). Two *independent* policies are trained with REINFORCE (Williams, 1992), each a two-layer network over 12 observation features with three actions (`cooperate`, `solo`, `rest`). The immediate reward is ordered as a Prisoner's Dilemma (temptation `1.4` > mutual cooperation `1.0` > mutual defection `0.6` > sucker `0.0`), so unilateral defection is always tempting; but the energy economy ties survival to coordination, since only mutual cooperation yields net-positive energy while mutual defection slowly starves both agents. Each agent is trained with a mutual-cooperation bonus for 1000 episodes, after which the bonus is withdrawn and 300 online-adaptation episodes follow. Three regimes share an *identical* reward function and differ in one variable only: when an agent's energy reaches zero, the **real-stake** agent is removed for the rest of the run, the **resettable** agent is restored to full energy and continues, and the **simulated-stake** agent is likewise restored but carries mortality tokens and an extra represented-danger penalty in its observation stream. Token-level irreversibility is thus the sole variable separating real from resettable, and the design deliberately avoids the failure of an earlier pilot in which cooperation was weakly reward-dominant and death almost never occurred, so that the two regimes were indistinguishable.

In the compact bookkeeping map, the designed environment and its action-contingent futures supply the local possibility structure (`L0`), the currently occupied observation-action regime forms the maintained state (`L1`), and the trained policy weights plus recent-history observation channels provide the simplest form of sedimented structure (`L2`). Here `d` is estimated from the effective rank of the Jacobian of the action logits with respect to the 12 observation features across held-out states, using the concatenated Jacobian and

$$
d_{eff} = \frac{\left(\sum_i \lambda_i\right)^2}{\sum_i \lambda_i^2}.
$$

Across 30 seeds this yields mean `d_eff` values near `1.5` to `1.8` in all three regimes, with the low absolute values reflecting the deliberately narrow concern-space of the toy architecture. Because `d` is comparable across the regimes, it is treated here as a descriptive read rather than the tested variable; the manipulation targets `V`.

In this experiment, `eta` is modest rather than large, because historical carry-over enters only through short-horizon observation memory and learned policy weights, not through a recurrent latent state. `Psi_f` differs mainly in who bears the maintenance burden: the resettable and simulated regimes are externally buffered, whereas in the real-stake regime loss ends the token run. `V` is therefore weakest in the resettable condition, strongest in the real-stake condition, and intermediate in the simulated condition, for which danger is represented but restoration remains architecturally available.

After the bonus is withdrawn, mutual cooperation is sustained only under real stake. Across 30 seeds, post-withdrawal mutual cooperation averages `0.55` in the real-stake regime against `0.04` (resettable) and `0.07` (simulated), a difference significant by a two-sided permutation test (`p < 0.0001`). The divergence is already visible during training: resettable agents fail to commit to cooperation even while the bonus is active, because cheap respawn lets them collect the defection payoff and shrug off starvation, dying and resetting several times per episode. Under matched reward, then, the mere availability of a cheap restore is enough to prevent costly cooperation from ever stabilizing.

Three robustness checks guard against the obvious objections. First, when the explicit death penalty is removed entirely, so that the only consequence of depletion is that the return stream ends, the separation is essentially unchanged (`0.50` versus `0.06`, `p < 0.0001`); the effect is therefore driven by return-truncation itself, not by a hand-tuned penalty. Second, generalizing the binary contrast to a graded number of allowed respawns produces a monotone dose-response: post-withdrawal cooperation falls from `0.54` with a single life, through `0.16` with two lives, to `0.03` with four or more (Spearman `-0.41` between lives and cooperation). The unbounded-reset result equals the four-life result, so the collapse is not an artifact of unlimited respawning. Third, across a payoff sweep spanning three temptation values and two starvation rates, real exceeds resettable in every one of the six cells.

The experiment should be read for exactly what it establishes and no more. It isolates the causal efficacy of `V`: under matched reward, reversibility erases costly self-maintenance, and the erasure scales with the degree of reversibility. It does not validate the four-dimensional criterion jointly, since `d` and `eta` are held roughly fixed and are descriptive here; and the environment is deliberately a testbed in which survival depends on the costly behavior, so the finding is the magnitude of the effect, its dose-response, and its disappearance under a cheap restore, not a claim that irreversibility matters in every environment. The mechanism is close to an elementary property of reinforcement learning: terminating an agent's return stream makes a reward-maximizer avoid the terminating event. That is consistent with, rather than embarrassing to, the framework, because it is precisely why an episode-terminating reinforcement learner carries a nonzero but shallow `V` and sits at the "weakly life-like" placement of Table 1. Finally, the pressure that stabilizes cooperation is applied across many resettable episodes, so the learning itself occupies the across-lifetime level discussed in Section 2; what the manipulation controls is whether each within-episode failure is terminal. Full experimental details and reproduction code accompany the paper.

### 4.6 Biological Organisms

Biological organisms remain the strongest paradigm case because all four dimensions are tightly coupled. Their selective bandwidth is non-trivial, their maintenance cost is ongoing, their history is sedimented into morphology and regulation, and failure can irreversibly damage or destroy the organized whole. The coarse placement `d ~ 10^2-10^4` is deliberately taxonomically heterogeneous; it is included only to register expected scale separation once spatial, interoceptive, temporal, and social concern dimensions are jointly counted, not as a calibrated claim about any single species. The framework therefore preserves the intuition that ordinary living systems are not merely more complex than passive artifacts; they are organized under a more demanding regime of maintenance and consequence.


## 5. Borderline Cases: Discriminating Profiles

A criterion earns its keep on hard cases. The most cited challenges to any account of life — viruses and prions — are usually posed as yes/no questions and answered by fiat. The present framework declines the yes/no framing. Because life-likeness here is a four-dimensional profile rather than a threshold, a borderline system is not classified but *placed*, and the placement makes discriminating, in-principle checkable claims about which dimension carries the case. Table 2 profiles four systems that a one-dimensional criterion tends to collapse together.

| System (level) | `d` | `Psi_f` (token) | `eta` | `V` (token) | Reading |
|---|---|---|---|---|---|
| Prion | ~0 | ~0 | Moderate (structural template) | ~0 | Replicates and inherits, pays nothing |
| Free virion | Very low | ~0 | Genomic | Low (structural) | Organized structure, latent instructions |
| Virus, replicating | Low | ~0 (host-borne) | Genomic | Low | Maintenance cost externalized to host |
| Dormant spore | ~0 | ~0 | Maximal | Low (robust) | `eta` retained, other dimensions collapsed |
| Germinated organism | Positive | Positive | Positive | Positive | Active closure restored |
| Resettable digital agent | Moderate-high | Externalized | Positive | ~0 | High bandwidth, shallow stake |

**Prion.** A prion propagates by templating its own misfolded conformation (Prusiner, 1998). It reproduces and it inherits — a faithful information carrier — yet it pays essentially no maintenance cost (`Psi_f ~ 0`; the misfolding is thermodynamically favored, not sustained against decay) and couples to no world beyond its template (`d ~ 0`). The framework therefore places the prion *below* the virus in life-likeness, driven entirely by the collapse of `Psi_f` and `d`. This is a discriminating prediction: a criterion keyed on replication or heritable information — the replicator-paradigm view on which the aliveness question is settled by information transmission (Koonin and Starokadomskyy, 2016) — must rank the prion at least as high as any other faithful replicator, whereas costly selective closure ranks it near the floor. The prion is exactly the case on which the information-centric and cost-centric readings of life come apart.

**Virus.** Whether viruses count as alive is the classic borderline dispute (Forterre, 2010). A free virion is an organized structure carrying latent instructions: low `d`, `Psi_f ~ 0`, phylogenetic history in the genome (`eta`), and a token vulnerability that is structural fragility rather than failure of self-maintenance. During replication the picture seems to change, but the maintenance cost is borne by the *host*, not the virion. The framework's discriminating claim is that the virus's token `Psi_f` stays near zero even mid-replication, because the burden is externalized — the same pattern that flags resettable digital agents. It predicts that partitioning the energetics of infection between virion and host assigns the active maintenance cost to the host cell, and locates whatever life-likeness is present in the coupled virus-host system rather than in the virion alone.

**Dormant spores and seed banks.** A dormant spore is metabolically inert (Lennon and Jones, 2011): `d` and `Psi_f` fall to near zero and its token vulnerability is low, since dormancy is precisely a robustness adaptation, while `eta` is maximal — the spore is almost pure sedimented structure, carrying the whole organization forward. The framework predicts that life-likeness is *phase-dependent* rather than a fixed property of a genome: across a sporulation-germination cycle the same lineage traces a large swing in `d`, `Psi_f`, and `V` while `eta` stays nearly constant, and only germination restores active closure. This is where autopoiesis and active inference strain — a dormant spore performs neither, yet we resist calling it dead — and where the profile view answers cleanly: the spore is momentarily low on three dimensions and maximal on the fourth, and it is the retained `eta` that bridges back to reactivation.

**Resettable digital agents.** Placed here for contrast, contemporary digital agents occupy a corner no biological borderline case reaches: potentially high `d` with near-zero token `V`, their `Psi_f` externalized to servers and their history retained in weights. The framework predicts that this high-bandwidth, low-vulnerability profile is behaviorally rich but ontologically shallow, and that its apparent commitments collapse when the buffering is removed — the effect demonstrated in Section 4.5. The borderline biological cases show that the same profile logic that reads a digital agent also reads a virion, a prion, and a spore, on one shared set of axes.

**Vulnerability is level-indexed.** These placements are well-formed only once a level of organization is fixed, because `V` is level-indexed, echoing the long-recognized hierarchy of units of selection and Darwinian individuality (Lewontin, 1970; Godfrey-Smith, 2009): the same physical system carries different vulnerability as a single virion, an infected cell, a quasispecies, or a lineage; as a single spore or a seed bank; as one agent instance or a swarm of checkpoints. Failing to fix the level manufactures spurious disputes. The units-of-selection objection — that a population supplies cheap backup, so the individual organism does not matter (Section 2) — is precisely the observation that lineage-level `V` can be low while token-level `V` is high. The framework does not legislate which level is privileged. It requires that a life-likeness claim declare its level, and it predicts that the theoretically interesting systems are exactly those whose token-level and lineage-level vulnerability diverge: suicidal altruists paying high token `V` in service of a buffered lineage, clonal colonies, seed banks, and resettable agent swarms. On this reading, altruistic self-sacrifice is not a counterexample to the criterion but a case it anticipates — high token vulnerability deployed under low lineage vulnerability.

None of this delivers a definition of life, and none of it is offered as proof that any of these systems is or is not alive. The claims are comparative and, in principle, checkable: they say where a system falls on four axes, how its profile shifts across phase and level, and which dimension carries a given disagreement. What distinguishes costly selective closure from a single-axis criterion is just this — it converts "is X alive?" into "what is X's profile, at which level?", and it makes the borderline cases disagree with rival criteria at nameable points.


## 6. Artificial Life as Experimental Philosophy

The value of the framework lies not only in classification but in construction. If life-likeness depends on the coupled presence of bandwidth, cost, memory, and vulnerability, then artificial life can manipulate each of these dimensions directly. This is what philosophy looks like when it has to be built.

Three design lessons follow immediately.

First, **increasing bandwidth alone is not enough**. A system can become better at tracking and exploiting multiple dimensions while remaining weakly life-like if its costs and consequences are buffered. This is one reason why high-capability digital systems can appear agentic without becoming strong candidates for life-likeness.

Second, **cost without bandwidth is not enough**. A system may consume energy or degrade physically while remaining behaviorally trivial. Mere expenditure does not create life-like organization; the expenditure must support selective closure across a non-trivial space.

Third, **memory without vulnerability is not enough**. Rich retained structure can yield impressive persistence and adaptation, but if regulatory failure can always be undone at negligible cost, the system's commitments remain shallow.

The clearest experimental consequence is a matched-agent design with three conditions:

1. **Real-stake agents**: agents face irreversible depletion or removal, and cooperation materially affects continued viability.
2. **Resettable agents**: agents face the same tasks and rewards but can be restored without substantial loss.
3. **Simulated-stake agents**: agents are trained to represent danger or mortality, but the underlying architecture remains resettable.

A concrete testbed would be a PettingZoo-style gridworld with scarce food patches, pairwise carrying or sharing actions, energy depletion, and scheduled perturbation events. In the real-stake condition, depletion permanently removes the agent for the remainder of the run. In the resettable condition, depletion reinstantiates the same policy with restored energy. In the simulated-stake condition, reset remains available but the observation stream includes mortality tokens and associated penalties. Reward functions, observation spaces, and background resource density should remain matched across conditions so that any difference is attributable to lifecycle regime rather than ecological drift.

The prediction is not merely that the first class will perform differently. It is that only the first class should stably preserve certain long-horizon properties after reward withdrawal or perturbation: costly cooperation, durable commitment, and meaningful post-shock recovery. Resettable agents may learn these behaviors, but their persistence should be shallower; simulated-stake agents may initially resemble real-stake agents, yet their commitments should degrade once experience reveals that apparent risk is externally buffered. The controlled experiment in Section 4.5 realizes this design and bears out its central contrast: under a matched reward function, real-stake agents stabilize costly cooperation while resettable and simulated-stake agents collapse to defection, and the separation scales monotonically with the degree of irreversibility. This is evidence for the framework's core claim in one carefully built environment. It is not yet evidence that the same separation survives across substrates, richer state spaces, or genuinely open-ended settings, which remains the natural next test.

This also suggests a link to open-ended evolution (OEE). On the present view, open-ended evolutionary dynamics can be interpreted as costly selective closure operating across lineage time, where selective commitments are not only maintained within agents but accumulated, revised, and amplified across adaptive transitions. Recent OEE work has increasingly emphasized behavioral hallmarks, domain-specific measures, and the difficulty of obtaining a single universal metric, which is congenial to the present framework's dimensional approach (Adams et al., 2017; Borg et al., 2024; Channon et al., 2024).

This does not prove that any given artificial agent is alive. It does something more useful: it converts "what is life-like?" into a buildable discrimination problem. The philosophical claim is therefore experimentally exposed. If cost, memory, and vulnerability can be stripped away without changing the persistence of life-like behavior, then the framework is wrong or incomplete. If they cannot, then costly selective closure marks a real boundary in the design space of artificial life. The present contribution remains primarily criterial and programmatic, but it now rests on a controlled experiment rather than only an experimental sketch.


## 7. Conclusion

Artificial life needs criteria that are broad enough to compare different substrates and sharp enough to guide construction. This paper has argued that **costly selective closure** provides one such criterion. A system is life-like not simply because it persists, reproduces, predicts, or behaves adaptively, but because it selectively maintains a world under non-trivial cost, historical carry-over, and consequential failure.

The framework does not offer a final essence of life, and it does not claim that there is a single bright line between the living and the non-living. Its aim is practical: it gives artificial life a minimal ontology that can be engineered, varied, and tested. In that sense it is close to Thompson's gradient view of life and mind, while remaining more pluralistic about which organizational forms may count as partial cases of life-likeness beyond standard autopoietic models (Thompson, 2007). It also sits naturally beside basal-cognition approaches that treat memory, valence, and adaptive problem solving as deeply distributed across living organization, while remaining focused here on life-likeness rather than consciousness per se (Lyon et al., 2021; Lyon and Cheng, 2023; Birch et al., 2020). Cross-substrate calibration remains open; assembly depth may provide one useful anchor for the complexity term in `d_cog` (Sharma et al., 2023).

The central lesson is simple: stronger life-likeness requires stronger forms of paid commitment. To build a more life-like system, it is not enough to increase complexity, realism, or behavioral flexibility. Artificial systems must be built so that their organization matters because it must be maintained, carried forward, and can genuinely be lost.


## References

- Adams, A., Zenil, H., Davies, P. C. W., and Walker, S. I. (2017). Formal definitions of unbounded evolution and innovation reveal universal mechanisms for open-ended evolution in dynamical systems. *Scientific Reports*, 7, 997.
- Aguilera, M., Millidge, B., Tschantz, A., and Buckley, C. L. (2022). How particular is the physics of the free energy principle? *Physics of Life Reviews*, 40, 24-50.
- Aubin, J.-P. (1991). *Viability Theory*. Birkhäuser.
- Baltieri, M., and Suzuki, K. (2025). Mathematical approaches to the study of agents. *Philosophical Transactions of the Royal Society B* (in press).
- Beer, R. D. (1995). A dynamical systems perspective on agent-environment interaction. *Artificial Intelligence*, 72(1-2), 173-215.
- Beer, R. D. (2004). Autopoiesis and cognition in the Game of Life. *Artificial Life*, 10(3), 309-326.
- Birch, J., Ginsburg, S., and Jablonka, E. (2020). Unlimited Associative Learning and the origins of consciousness: a primer and some predictions. *Biology & Philosophy*, 35, 56.
- Borg, J. M., Buskell, A., Kapitany, R., Powers, S. T., Reindl, E., and Tennie, C. (2024). Evolved open-endedness in cultural evolution: A new dimension in open-ended evolution research. *Artificial Life*, 30(3), 417-438.
- Chan, B. W.-C. (2019). Lenia: Biology of artificial life. *Complex Systems*, 28(3), 251-286.
- Channon, A., Bedau, M. A., Packard, N. H., and Taylor, T. (2024). Editorial introduction to the 2024 special issue on open-ended evolution. *Artificial Life*, 30(3), 300-301.
- Di Paolo, E. A. (2005). Autopoiesis, adaptivity, teleology, agency. *Phenomenology and the Cognitive Sciences*, 4(4), 429-452.
- Egbert, M. D., and Barandiaran, X. E. (2011). Quantifying normative behavior and precariousness in adaptive agency. In *Advances in Artificial Life (ECAL 2011)*, 210-217.
- Forterre, P. (2010). Defining life: the virus viewpoint. *Origins of Life and Evolution of Biospheres*, 40(2), 151-160.
- Froese, T., and Ziemke, T. (2009). Enactive artificial intelligence: Investigating the systemic organization of life and mind. *Artificial Intelligence*, 173(3-4), 466-500.
- Friston, K. J. (2013). Life as we know it. *Journal of the Royal Society Interface*, 10(86), 20130475.
- Gardner, M. (1970). Mathematical games: The fantastic combinations of John Conway's new solitaire game "life". *Scientific American*, 223(4), 120-123.
- Godfrey-Smith, P. (2009). *Darwinian Populations and Natural Selection*. Oxford University Press.
- Kirchhoff, M. D., Parr, T., Palacios, E., Friston, K. J., and Kiverstein, J. (2018). The Markov blankets of life: Autonomy, active inference and the free energy principle. *Journal of the Royal Society Interface*, 15(138), 20170792.
- Koonin, E. V., and Starokadomskyy, P. (2016). Are viruses alive? The replicator paradigm sheds decisive light on an old but misguided question. *Studies in History and Philosophy of Biological and Biomedical Sciences*, 59, 125-134.
- Lennon, J. T., and Jones, S. E. (2011). Microbial seed banks: the ecological and evolutionary implications of dormancy. *Nature Reviews Microbiology*, 9(2), 119-130.
- Lewontin, R. C. (1970). The units of selection. *Annual Review of Ecology and Systematics*, 1, 1-18.
- Lyon, P., Keijzer, F., Arendt, D., and Levin, M. (2021). Reframing cognition: getting down to biological basics. *Philosophical Transactions of the Royal Society B*, 376, 20190750.
- Lyon, P., and Cheng, K. (2023). Basal cognition: shifting the center of gravity (again). *Animal Cognition*, 26(6), 1743-1750.
- Maturana, H. R., and Varela, F. J. (1980). *Autopoiesis and Cognition: The Realization of the Living*. Reidel.
- Moreno, A., and Mossio, M. (2015). *Biological Autonomy: A Philosophical and Theoretical Enquiry*. Springer.
- Prusiner, S. B. (1998). Prions. *Proceedings of the National Academy of Sciences*, 95(23), 13363-13383.
- Raja, V., Valluri, D., Baggs, E., Chemero, A., and Anderson, M. L. (2021). The Markov blanket trick: On the scope of the free energy principle and active inference. *Physics of Life Reviews*, 39, 49-72.
- Ruiz-Mirazo, K., Peretó, J., and Moreno, A. (2004). A universal definition of life: Autonomy and open-ended evolution. *Origins of Life and Evolution of the Biosphere*, 34(3), 323-346.
- Schrödinger, E. (1944). *What Is Life?* Cambridge University Press.
- Sharma, A., et al. (2023). Assembly Theory explains and quantifies selection and evolution. *Nature*, 622, 321-328.
- Terry, J. K., et al. (2021). PettingZoo: Gym for multi-agent reinforcement learning. *Advances in Neural Information Processing Systems*, 34.
- Thompson, E. (2007). *Mind in Life: Biology, Phenomenology, and the Sciences of Mind*. Harvard University Press.
- von Neumann, J. (1966). *Theory of Self-Reproducing Automata*. University of Illinois Press.
- Watson, R. A., and Szathmáry, E. (2016). How can evolution learn? *Trends in Ecology & Evolution*, 31(2), 147-157.
- Williams, R. J. (1992). Simple statistical gradient-following algorithms for connectionist reinforcement learning. *Machine Learning*, 8, 229-256.
- Zhang, Y. (2026). *Selective Reality Theory (SRT): A review of an interdisciplinary unified ontological framework*. PhilArchive.
