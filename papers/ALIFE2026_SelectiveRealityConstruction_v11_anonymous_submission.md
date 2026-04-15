# Costly Selection: A Minimal Criterion for Life-Likeness in Artificial Systems

[Anonymous Submission for Review]

[Author details withheld]

Special Session: Artificial Life as Experimental Philosophy

## Abstract

Artificial life still lacks an operational criterion for life-likeness. Reproduction, metabolism, autopoiesis, adaptive behavior, and predictive closure each capture part of the target, but none distinguishes systems that merely update from those that must sustain organized existence. This paper proposes a minimal criterion drawn from Selective Reality Theory: life-likeness consists in **costly selective closure**. A system is life-like insofar as it selectively stabilizes an actionable world, pays a non-trivial cost to maintain that organization, carries prior selections forward, and faces consequential failure when regulation breaks down. Four coupled dimensions make this claim explicit: selective bandwidth (`d`), maintenance cost (`Psi_f`), hysteretic memory (`eta`), and irreversible vulnerability (`V`). These dimensions distinguish **passive closure** from **active closure**. Applied to Conway's Game of Life, Lenia, autopoietic agents, and resettable reinforcement-learning agents, the framework yields a substrate-flexible gradient of life-likeness. A worked PettingZoo-style example shows how the dimensions can be estimated in practice, and the framework avoids medium chauvinism by requiring token-level irreversibility rather than any privileged substrate. It therefore turns a philosophical dispute into a buildable research program: by varying cost, memory, and vulnerability in artificial systems, ALife can test which forms of organization support durable cooperation, long-horizon commitment, and recovery after perturbation.

**Keywords**: artificial life, life-likeness, autopoiesis, active closure, vulnerability, selective reality theory, artificial agents


## 1. Introduction

Artificial life has always been both a technical program and a philosophical method. Instead of asking only what life is in the abstract, it asks what must be built, varied, and maintained for something life-like to appear. The question is therefore not only classificatory. It is operational: what should count as a success condition for artificial life?

This remains unsettled. Different traditions emphasize different signatures. Self-reproduction captures evolutionary open-endedness but excludes sterile organisms and many familiar living phases. Metabolism captures energetic organization but risks including fire. Autopoiesis captures self-producing organization and organizational closure, but is often difficult to compare across substrates (Moreno and Mossio, 2015). More recent frameworks based on predictive processing or active inference highlight adaptive regulation and boundary maintenance, but by their generality they can blur the difference between organisms, thermostats, and highly capable digital agents. The present proposal also sits alongside work on minimal autonomous systems and enactive artificial intelligence (Ruiz-Mirazo et al., 2004; Froese and Ziemke, 2009). It is also sympathetic to Thompson's life-mind continuity thesis, while departing from it in treating organizational closure as necessary but not by itself sufficient for stronger forms of life-likeness (Thompson, 2007).

For artificial life, this creates a practical problem. Without a shared operational criterion, systems with very different ontological profiles are often discussed in the same vocabulary of "adaptation," "agency," or "self-maintenance." We can describe Conway patterns, Lenia morphologies, soft robots, language models, and bacteria as exhibiting some kind of organization, but not all organization is equally life-like. A criterion is needed that is broad enough to compare unlike systems while still sharp enough to distinguish mere update from consequential self-maintenance.

This paper proposes such a criterion. Drawing on Selective Reality Theory (SRT), treated here in self-contained form, it argues that the minimal signature of life-likeness is **costly selective closure**. A life-like system is not merely one that persists, computes, or reproduces. It is one that:

1. selectively couples to a non-trivial portion of its world,
2. pays a non-zero cost to maintain that coupling,
3. carries the effects of past selections forward in memory and structure, and
4. faces meaningful consequences if its regulation fails.

The point is not to introduce a new essence of life. It is to give artificial life a buildable discrimination rule. On this view, life-likeness is a gradient rather than a binary threshold. Systems can be more or less life-like depending on the degree to which they exhibit selective bandwidth, maintenance cost, hysteresis, and vulnerability.


## 2. Why Existing Criteria Stop Too Early

Classical definitions of life usually succeed by being locally right and globally incomplete. Reproduction identifies one important route by which life persists through time, but not all living systems are reproducing at every moment, and many life-like artifacts may never reproduce at all. Metabolism captures energetic openness and thermodynamic work, but by itself it says too little about selectivity or organization. Autopoiesis comes closer by focusing on self-producing organization, yet its explanatory strength can become a weakness when researchers need tractable comparisons across different media.

The same problem appears in more recent discussions of adaptive systems. A system can maintain a boundary, minimize error, or stabilize a policy without this being enough to make it meaningfully life-like. A thermostat is organized, robust, and responsive. A large language model can exhibit astonishing behavioral complexity. A reinforcement-learning agent can maximize reward under changing conditions. Yet there remains an intuitive and theoretical difference between systems that merely implement a designer's structure and systems whose way of existing is itself under stake.

The missing distinction is between **update** and **consequential self-maintenance**.

Many systems update. Far fewer must continuously pay to remain what they are. In ordinary biological cases, failure has non-trivial consequences: the organism exhausts energy, loses integrity, suffers damage, or dies. Its regulatory activity therefore has existential weight. By contrast, many computational systems operate under extensive buffering. They may be reset, copied, restored, paused, or run again with little cost to their identity. They can display goal-directed behavior without bearing much of the burden that makes biological regulation matter.

Artificial life needs a criterion that can register this difference without collapsing into substrate chauvinism. The criterion should not require carbon chemistry. But neither should every well-regulated or behaviorally rich system be treated as equally life-like. The question is not whether a system behaves as if it had a world. The question is whether it must selectively construct and maintain such a world under real cost and consequence.

This also clarifies the relation to active inference. Active inference provides a powerful account of adaptive regulation under a Markov blanket, but by design it does not distinguish between systems that maintain that blanket at negligible cost to themselves and systems for which boundary-maintenance is existentially burdensome (Friston, 2013; Kirchhoff et al., 2018). The present framework adds that distinction through the vulnerability dimension `V`: two systems may be equally well-described by active inference while differing sharply in life-likeness if one can be freely reset and the other cannot. What `V` adds is therefore not the generic idea that systems resist dispersion. FEP already captures that descriptive insight. The added claim is about token-level irreversibility: whether failure is borne by the individual system whose organization is at issue, or whether loss is cheaply externalized and reversed by the surrounding setup.

A natural objection arises: does `V` simply reintroduce a subtler form of chauvinism by favoring media with irreversible physical loss? The framework's answer is no. It does not privilege carbon, metabolism, or any specific material substrate. What it requires is that the continued organization of the token system be non-trivially at stake. In principle, a digital system could satisfy this condition if its persistence were bound to local irreversible processes rather than to cheap perfect restoration. A simple thought experiment would be an embodied digital agent tied to aging edge hardware with no maintained backup, or an irrevocable smart-contract agent whose local state transitions cannot be rolled back without destroying the token process under evaluation. What is excluded is not digitality as such, but architectures in which losses are systematically externalized and undone by design.


## 3. Costly Selective Closure

### 3.1 Selective Construction

The proposed framework begins with a simple thought: every candidate system faces a space of possible states, perturbations, and interactions. Life-like systems do not passively occupy this space. They selectively stabilize a small and usable region of it.

Using SRT's compact vocabulary, it is helpful to name three layers without importing the full theory. `L0` denotes the open possibility space available to a system, `L1` its currently maintained manifest state, and `L2` the relatively stable structures sedimented by prior successful selection. In this paper these labels function only as a concise map: the key issue is how a system moves from open possibility to maintained organization, and how repeated selections become durable constraints on future behavior.

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
d_{cog} \approx \alpha A(\sigma) + \beta \log V_{concern} + \gamma \tau_{temporal}
$$

where `A(sigma)` is assembly depth, `V_concern` is the spatial or social scope of relevant variables, and `tau_temporal` is the effective planning horizon. The coefficients `alpha`, `beta`, and `gamma` are weighting parameters whose values depend on the comparison context; the decomposition is not a measurement protocol but a heuristic for ensuring that comparisons across substrates attend to the same underlying factors. In particular, assembly depth provides one promising substrate-neutral anchor for the complexity term (Sharma et al., 2023).

**Maintenance cost (`Psi_f`).** A system may display organized behavior while paying little of the cost itself. `Psi_f` denotes the burden of maintaining the selected state against drift, dispersion, or collapse. Crucially, it is not gross energy expenditure measured by an outside observer, but the maintenance burden borne by the system as a condition of preserving its own token organization. A large language model may consume substantial external GPU energy while still ranking low on `Psi_f` in this sense if failure does not threaten the persistence of its own state and checkpoints make restoration cheap.

**Hysteretic memory (`eta`).** Life-like systems do not simply react in the present. Their prior selections sediment into present organization. `eta` measures this historical carry-over. It is not just explicit memory storage; it includes any mechanism by which past regulation becomes embodied as current bias, constraint, or habit.

**Irreversible vulnerability (`V`).** Finally, a system becomes more life-like when failure cannot be costlessly undone. `V > 0` means that bad regulation has non-trivial consequences for the continuation of the system's organization. This need not imply literal death in every artificial case, but it does require more than symbolic risk. In enactive terms, `V` captures a formal analogue of precariousness (Di Paolo, 2005; Egbert and Barandiaran, 2011).

These four dimensions are coupled by a simple viability inequality:

$$
\frac{dq}{dt} \le \alpha P_{sel} - \beta \Psi_f - \gamma N
$$

where `q` is organized order, `P_sel` is selection power, and `N` is noise or perturbation pressure. A life-like system remains viable only when it can generate enough selective power to offset maintenance cost and noise. Existence is therefore not a default state; it is a managed achievement.

### 3.3 Passive and Active Closure

The framework distinguishes two broad regimes.

**Passive closure** describes systems that appear organized but whose organization is heavily buffered by external design, reset, or negligible consequence. They may be elegant, adaptive, and even behaviorally rich, yet they do not bear much of the burden of their own continued organization.

**Active closure** describes systems that must continuously pay to maintain their selected state, carry prior regulation forward, and risk genuine degradation if they fail.

This distinction matters because many debates about artificial life conflate the two. A system may display convincing local closure while remaining weakly life-like overall because its cost, memory, or vulnerability are shallow. The question is not whether closure exists at all, but whether it is passive or active.

### 3.4 Status of the Formalization

The formalism above should be read as a qualitative-to-semi-quantitative comparison framework, not as a closed dynamical theory. The update equation is schematic: it states that current organization depends on present selection and retained history, but it does not assume that `\hat{G}_theta` is linear, deterministic, or defined over a Euclidean state space. When state spaces are non-Euclidean, the weighted update should be understood as shorthand for any compatible local representation or state-update rule that preserves the same conceptual roles.

Likewise, the effective-rank definition of `d` is the principal definition, whereas `d_cog` is an operational proxy intended for comparative work across substrates. The latter does not replace the former; it offers a practical route for approximate estimation when the full operator spectrum is not available. Finally, `q`, `P_sel`, and `N` in the viability inequality should be treated as task-specific observables rather than already-standardized measurements. The present framework is therefore best understood as a disciplined heuristic grammar for comparison and experiment design, not yet as a directly computable model.


## 4. Canonical Cases

Table 1 summarizes the framework's verdict on several familiar cases. The entries should be read as order-of-magnitude heuristic placements rather than measured quantities.

| System | `d` | `Psi_f` | `eta` | `V` | Verdict |
|---|---|---|---|---|---|
| Crystal | 0 | None | None | None | Stable but not life-like |
| Conway's Game of Life pattern | ~0 | None | Very low | None | Organized update, not active closure |
| Lenia morphology | ~1-3 | Low/emergent | Low | Low | Weakly life-like |
| Autopoietic/evolved embodied agent | ~5-20 | Positive | Positive | Positive | Moderately life-like |
| Resettable RL agent | ~10-100 | Often externally buffered | Positive | Weak | Behaviorally rich but ontologically shallow |
| Biological organism | ~10^2-10^4 | Positive | Positive | Strong | Strong active closure |

### 4.1 Conway's Game of Life

Game of Life remains a foundational example because it demonstrates how surprising pattern formation can emerge from simple rules. Yet, under the present framework, it ranks low in life-likeness. Patterns localize and persist, but they do not bear non-trivial cost, retain history in a robust sense, or face consequential failure. Their apparent agency is observer-attributed. The system updates according to fixed rules; it does not actively maintain a selected mode of existence under burden.

### 4.2 Lenia

Lenia is more interesting because it produces morphologies with clear behavioral coherence. Patterns move, stabilize, regenerate, and sometimes appear to "seek" conditions that preserve form. This gives Lenia stronger localization and a weak analogue of maintenance cost: the pattern must continually sustain itself against dispersion. The placement `d ~ 1-3` reflects the fact that Lenia's update kernel and stable morphologies usually organize variation around a small number of dominant spatial modes, such as translation, oscillation, and orientation, rather than a broad set of independently weighted environmental variables. Even so, its hysteresis is limited and its vulnerability is shallow compared with embodied agents. It is therefore best described as weakly life-like.

### 4.3 Autopoietic Agents

Embodied autopoietic or evolved agents in the tradition of Beer and Di Paolo score higher. They regulate sensorimotor coupling, maintain a boundary, and can fail in ways that matter for continued performance. Their current activity is constrained by prior adaptation, which gives them a meaningful `eta`, and their continued organization requires ongoing work, which gives them positive `Psi_f`. Such systems are among the clearest artificial demonstrations of active closure currently available.

### 4.4 Resettable Digital Agents

Many contemporary digital agents complicate the picture. Reinforcement-learning systems can exhibit substantial behavioral flexibility and therefore moderate or high `d`. They may also carry substantial training history and internal state, giving them non-trivial `eta`. But if their organization is extensively buffered by cheap reset, abundant copying, and negligible irreversible loss, then `V` remains weak and `Psi_f` is not borne by the agent in a robust sense. They are therefore best treated as partial life-likeness: high behavioral sophistication under shallow stake conditions. The same point applies, even more strongly, to contemporary large language models.

### 4.5 Worked Example: A Resettable Cooperative RL Agent

Consider a PettingZoo-style two-agent cooperative foraging environment. Each agent observes local resource, partner, obstacle, and threat variables plus a recurrent hidden state; cooperative harvesting yields more reward than solitary harvesting. In the compact SRT map, the observable gridworld state supplies the available possibility structure (`L0`), action selection stabilizes a currently relevant task state (`L1`), and the trained policy plus recurrent hidden state provide the simplest form of sedimented structure (`L2`). Here `d` can be estimated from the effective rank of the Jacobian of action logits with respect to observation features across held-out trajectories. If that rank clusters around 12-18 across runs, the system can be placed at `d ~ 10-20`. `eta` can be operationalized by measuring how strongly hidden-state perturbations continue to influence later actions; slower decay implies higher hysteresis. `Psi_f` is low-to-moderate but externally buffered, because training and inference consume real energy while depletion does not threaten persistence of the token agent. `V` is weak because failed regulation triggers reset rather than irreversible loss; a simple proxy would be `V_proxy = 1 - P(restore | failure)`. The same environment can also be used for the matched-agent comparison in Section 5, which makes the framework's discriminations more explicit:

| Condition | `d` | `Psi_f` | `eta` | `V` | Expected verdict |
|---|---|---|---|---|---|
| Resettable baseline | ~10-20 | Low/moderate, externally buffered | Moderate | Weak | Behaviorally rich, shallow stake |
| Real-stake variant | ~10-20 | Moderate, system-borne | Moderate | Strong | More active closure |
| Simulated-stake variant | ~10-20 | Low/moderate, externally buffered | Moderate | Weak to moderate | Apparent stake without full consequence |

The point is not to claim a completed measurement pipeline, but to show how the four dimensions can be tied to an explicit system description and then carried forward into an experimental comparison.

### 4.6 Biological Organisms

Biological organisms remain the strongest paradigm case because all four dimensions are tightly coupled. Their selective bandwidth is non-trivial, their maintenance cost is ongoing, their history is sedimented into morphology and regulation, and failure can irreversibly damage or destroy the organized whole. The framework therefore preserves the intuition that ordinary living systems are not merely more complex than passive artifacts; they are organized under a more demanding regime of maintenance and consequence.


## 5. Artificial Life as Experimental Philosophy

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

The prediction is not merely that the first class will perform differently. It is that only the first class should stably preserve certain long-horizon properties after reward withdrawal or perturbation: costly cooperation, durable commitment, and meaningful post-shock recovery. Resettable agents may learn these behaviors, but their persistence should be shallower. Simulated-stake agents may initially resemble real-stake agents, yet their commitments should degrade once experience reveals that apparent risk is externally buffered. Persistence can be operationalized as the number of post-perturbation episodes before cooperative behavior falls below a pre-defined baseline, for example 50% of the pre-perturbation cooperation rate.

This also suggests a link to open-ended evolution. On the present view, open-ended evolutionary dynamics can be interpreted as costly selective closure operating across lineage time, where selective commitments are not only maintained within agents but accumulated, revised, and amplified across adaptive transitions (Watson and Szathmáry, 2016).

This does not prove that any given artificial agent is alive. It does something more useful: it converts "what is life-like?" into a buildable discrimination problem. The philosophical claim is therefore experimentally exposed. If cost, memory, and vulnerability can be stripped away without changing the persistence of life-like behavior, then the framework is wrong or incomplete. If they cannot, then costly selective closure marks a real boundary in the design space of artificial life.


## 6. Conclusion

Artificial life needs criteria that are broad enough to compare different substrates and sharp enough to guide construction. This paper has argued that **costly selective closure** provides one such criterion. A system is life-like not simply because it persists, reproduces, predicts, or behaves adaptively, but because it selectively maintains a world under non-trivial cost, historical carry-over, and consequential failure.

The framework does not offer a final essence of life, and it does not claim that there is a single bright line between the living and the non-living. Its aim is practical: it gives artificial life a minimal ontology that can be engineered, varied, and tested. In that sense it is close to Thompson's gradient view of life and mind, while remaining more pluralistic about which organizational forms may count as partial cases of life-likeness beyond standard autopoietic models (Thompson, 2007). The proposal is compatible with threshold-based approaches to minimal cognition, including Unlimited Associative Learning, while remaining focused on life-likeness rather than consciousness per se (Birch et al., 2020). Cross-substrate calibration remains open; assembly depth may provide one useful anchor for the complexity term in `d_cog` (Sharma et al., 2023).

The central lesson is simple: stronger life-likeness requires stronger forms of paid commitment. To build a more life-like system, it is not enough to increase complexity, realism, or behavioral flexibility. Artificial systems must be built so that their organization matters because it must be maintained, carried forward, and can genuinely be lost.


## References

- Beer, R. D. (2004). Autopoiesis and cognition in the Game of Life. *Artificial Life*, 10(3), 309-326.
- Birch, J., Ginsburg, S., and Jablonka, E. (2020). Unlimited Associative Learning and the origins of consciousness: a primer and some predictions. *Biology & Philosophy*, 35, 56.
- Chan, B. W.-C. (2019). Lenia: Biology of artificial life. *Complex Systems*, 28(3), 251-286.
- Di Paolo, E. A. (2005). Autopoiesis, adaptivity, teleology, agency. *Phenomenology and the Cognitive Sciences*, 4(4), 429-452.
- Egbert, M. D., and Barandiaran, X. E. (2011). Quantifying normative behavior and precariousness in adaptive agency. In *Advances in Artificial Life (ECAL 2011)*, 210-217.
- Froese, T., and Ziemke, T. (2009). Enactive artificial intelligence: Investigating the systemic organization of life and mind. *Artificial Intelligence*, 173(3-4), 466-500.
- Friston, K. J. (2013). Life as we know it. *Journal of the Royal Society Interface*, 10(86), 20130475.
- Kirchhoff, M. D., Parr, T., Palacios, E., Friston, K. J., and Kiverstein, J. (2018). The Markov blankets of life: Autonomy, active inference and the free energy principle. *Journal of the Royal Society Interface*, 15(138), 20170792.
- Maturana, H. R., and Varela, F. J. (1980). *Autopoiesis and Cognition: The Realization of the Living*. Reidel.
- Moreno, A., and Mossio, M. (2015). *Biological Autonomy: A Philosophical and Theoretical Enquiry*. Springer.
- Ruiz-Mirazo, K., Peretó, J., and Moreno, A. (2004). A universal definition of life: Autonomy and open-ended evolution. *Origins of Life and Evolution of the Biosphere*, 34(3), 323-346.
- Schrödinger, E. (1944). *What Is Life?* Cambridge University Press.
- Sharma, A., et al. (2023). Assembly Theory explains and quantifies selection and evolution. *Nature*, 622, 321-328.
- Terry, J. K., et al. (2021). PettingZoo: Gym for multi-agent reinforcement learning. *Advances in Neural Information Processing Systems*, 34.
- Thompson, E. (2007). *Mind in Life: Biology, Phenomenology, and the Sciences of Mind*. Harvard University Press.
- von Neumann, J. (1966). *Theory of Self-Reproducing Automata*. University of Illinois Press.
- Watson, R. A., and Szathmáry, E. (2016). How can evolution learn? *Trends in Ecology & Evolution*, 31(2), 147-157.
