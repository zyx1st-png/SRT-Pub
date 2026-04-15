# Costly Selection: A Minimal Criterion for Life-Likeness in Artificial Systems

[Author Name(s)]

[Affiliation(s)]

[Contact Email]

Special Session: Artificial Life as Experimental Philosophy

## Abstract

Artificial life still lacks a shared operational criterion for life-likeness. Reproduction, metabolism, autopoiesis, adaptive behavior, and predictive closure each capture part of the target, but none cleanly distinguishes systems that merely update from systems that must sustain an organized mode of existence. This paper proposes a minimal criterion drawn from Selective Reality Theory: life-likeness consists in **costly selective closure**. A system is life-like insofar as it selectively stabilizes an actionable world, pays a non-trivial cost to maintain that organization, carries prior selections forward, and faces consequential failure when regulation breaks down. Four coupled dimensions make this claim explicit: selective bandwidth (`d`), maintenance cost (`Psi_f`), hysteretic memory (`eta`), and irreversible vulnerability (`V`). These dimensions distinguish **passive closure** from **active closure**. Applied to Conway's Game of Life, Lenia, autopoietic agents, and resettable reinforcement-learning agents, the framework yields a substrate-flexible gradient of life-likeness. More importantly, it turns a philosophical dispute into a buildable research program: by varying cost, memory, and vulnerability in artificial systems, ALife can test which forms of organization support durable cooperation, long-horizon commitment, and recovery after perturbation.

**Keywords**: artificial life, life-likeness, autopoiesis, active closure, vulnerability, selective reality theory, artificial agents


## 1. Introduction

Artificial life has always been both a technical program and a philosophical method. Instead of asking only what life is in the abstract, it asks what must be built, varied, and maintained for something life-like to appear. The question is therefore not only classificatory. It is operational: what should count as a success condition for artificial life?

This remains unsettled. Different traditions emphasize different signatures. Self-reproduction captures evolutionary open-endedness but excludes sterile organisms and many familiar living phases. Metabolism captures energetic organization but risks including fire. Autopoiesis captures self-producing organization and organizational closure, but is often difficult to compare across substrates (Moreno and Mossio, 2015). More recent frameworks based on predictive processing or active inference highlight adaptive regulation and boundary maintenance, but by their very generality they can blur the difference between organisms, thermostats, and highly capable digital agents.

For artificial life, this creates a practical problem. Without a shared operational criterion, systems with very different ontological profiles are often discussed in the same vocabulary of "adaptation," "agency," or "self-maintenance." We can describe Conway patterns, Lenia morphologies, soft robots, language models, and bacteria as exhibiting some kind of organization, but not all organization is equally life-like. A criterion is needed that is broad enough to compare unlike systems while still sharp enough to distinguish mere update from consequential self-maintenance.

This paper proposes such a criterion. Drawing on Selective Reality Theory (SRT), it argues that the minimal signature of life-likeness is **costly selective closure**. A life-like system is not merely one that persists, computes, or reproduces. It is one that:

1. selectively couples to a non-trivial portion of its world,
2. pays a non-zero cost to maintain that coupling,
3. carries the effects of past selections forward in memory and structure, and
4. faces meaningful consequences if its regulation fails.

The point is not to introduce a new essence of life. It is to give artificial life a buildable discrimination rule. On this view, life-likeness is a gradient rather than a binary threshold. Systems can be more or less life-like depending on the degree to which they exhibit selective bandwidth, maintenance cost, hysteresis, and vulnerability.

The contribution is threefold. First, the paper offers a compact formal vocabulary for comparing biological and artificial systems without presupposing a single substrate. Second, it applies the framework to canonical cases in artificial life. Third, it shows how the framework turns a philosophical dispute into an experimental program: by manipulating cost, memory, and vulnerability in artificial systems, researchers can test which combinations produce durable life-like organization rather than its simulation.


## 2. Why Existing Criteria Stop Too Early

Classical definitions of life usually succeed by being locally right and globally incomplete. Reproduction identifies one important route by which life persists through time, but not all living systems are reproducing at every moment, and many life-like artifacts may never reproduce at all. Metabolism captures energetic openness and thermodynamic work, but by itself it says too little about selectivity or organization. Autopoiesis comes closer by focusing on self-producing organization, yet its explanatory strength can become a weakness when researchers need tractable comparisons across different media.

The same problem appears in more recent discussions of adaptive systems. A system can maintain a boundary, minimize error, or stabilize a policy without this being enough to make it meaningfully life-like. A thermostat is organized, robust, and responsive. A large language model can exhibit astonishing behavioral complexity. A reinforcement-learning agent can maximize reward under changing conditions. Yet there remains an intuitive and theoretical difference between systems that merely implement a designer's structure and systems whose way of existing is itself under stake.

The missing distinction is between **update** and **consequential self-maintenance**.

Many systems update. Far fewer must continuously pay to remain what they are. In ordinary biological cases, failure has non-trivial consequences: the organism exhausts energy, loses integrity, suffers damage, or dies. Its regulatory activity therefore has existential weight. By contrast, many computational systems operate under extensive buffering. They may be reset, copied, restored, paused, or run again with little cost to their identity. They can display goal-directed behavior without bearing much of the burden that makes biological regulation matter.

Artificial life needs a criterion that can register this difference without collapsing into substrate chauvinism. The criterion should not require carbon chemistry. But neither should every well-regulated or behaviorally rich system be treated as equally life-like. The question is not whether a system behaves as if it had a world. The question is whether it must selectively construct and maintain such a world under real cost and consequence.

This also clarifies the relation to active inference. Active inference provides a powerful account of adaptive regulation under a Markov blanket, but by design it does not distinguish between systems that maintain that blanket at negligible cost to themselves and systems for which boundary-maintenance is existentially burdensome (Friston, 2013; Kirchhoff et al., 2018). The present framework adds that distinction through the vulnerability dimension `V`: two systems may be equally well-described by active inference while differing sharply in life-likeness if one can be freely reset and the other cannot.


## 3. Costly Selective Closure

### 3.1 Selective Construction

The proposed framework begins with a simple thought: every candidate system faces a space of possible states, perturbations, and interactions. Life-like systems do not passively occupy this space. They selectively stabilize a small and usable region of it.

Using SRT's compact vocabulary, it is helpful to name three layers without importing the full theory. `L0` denotes the open possibility space available to a system, `L1` its currently maintained manifest state, and `L2` the relatively stable structures sedimented by prior successful selection. In this paper these labels function only as a concise map: the key issue is how a system moves from open possibility to maintained organization, and how repeated selections become durable constraints on future behavior.

Let `Omega_t` denote the system's currently accessible possibility space and `x_t` its maintained state. We can write the next state schematically as

$$
x_{t+1} = (1 - \eta)\,\hat{G}_{\theta}[\Omega_t] + \eta x_t
$$

where `G_hat_theta` is a selection operator and `eta in [0,1]` is a hysteresis term. The equation is intentionally minimal. It says only that current organization depends partly on present selection and partly on retained structure from the past. When `eta = 0`, the system is purely reactive. When `eta > 0`, previous selections constrain current ones.

This process can be called **selective reality construction**: a system does not encounter all possible states equally. It actively compresses possibilities into an actionable world. In biological organisms this is obvious. What counts as relevant is shaped by metabolism, morphology, history, and need. In artificial systems, the same question can be posed constructively: what dimensions does the system track, what does it ignore, and what does it take to keep that selection stable?

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

**Maintenance cost (`Psi_f`).** A system may display organized behavior while paying little of the cost itself. To count as strongly life-like, its organization must require ongoing expenditure. `Psi_f` denotes the cost of maintaining the selected state against drift, dispersion, or collapse. In biological settings this includes metabolic work; in artificial settings it may include energy, irreversible weight change, structural degradation, or other non-trivial maintenance burdens.

**Hysteretic memory (`eta`).** Life-like systems do not simply react in the present. Their prior selections sediment into present organization. `eta` measures this historical carry-over. It is not just explicit memory storage; it includes any mechanism by which past regulation becomes embodied as current bias, constraint, or habit.

**Irreversible vulnerability (`V`).** Finally, a system becomes more life-like when failure cannot be costlessly undone. `V > 0` means that bad regulation has non-trivial consequences for the continuation of the system's organization. This need not imply literal death in every artificial case, but it does require more than symbolic risk. If the system can be freely reset, cloned, or restored without loss of organization, its vulnerability is weak. In enactive terms, `V` is intended to capture a formal analogue of precariousness: the system's continued organization is not guaranteed, but must be actively preserved (Di Paolo, 2005; Egbert and Barandiaran, 2011).

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


## 4. Canonical Cases

Table 1 summarizes the framework's verdict on several familiar cases.

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

Lenia is more interesting because it produces morphologies with clear behavioral coherence. Patterns move, stabilize, regenerate, and sometimes appear to "seek" conditions that preserve form. This gives Lenia stronger localization and a weak analogue of maintenance cost: the pattern must continually sustain itself against dispersion. Even so, its selective bandwidth is narrow, its hysteresis is limited, and its vulnerability is shallow compared with embodied agents. Lenia is therefore not best described as fully alive or fully non-living. It is better described as weakly life-like.

### 4.3 Autopoietic Agents

Embodied autopoietic or evolved agents in the tradition of Beer and Di Paolo score higher. They regulate sensorimotor coupling, maintain a boundary, and can fail in ways that matter for continued performance. Their current activity is constrained by prior adaptation, which gives them a meaningful `eta`, and their continued organization requires ongoing work, which gives them positive `Psi_f`. Such systems are among the clearest artificial demonstrations of active closure currently available.

### 4.4 Resettable Digital Agents

Many contemporary digital agents complicate the picture. Reinforcement-learning systems can exhibit substantial behavioral flexibility and therefore moderate or high `d`. They may also carry substantial training history and internal state, giving them non-trivial `eta`. But if their organization is extensively buffered by cheap reset, abundant copying, and negligible irreversible loss, then `V` remains weak and `Psi_f` is not borne by the agent in a robust sense. In this framework they are not dismissed as trivial. Rather, they are treated as a specific form of partial life-likeness: high behavioral sophistication under shallow stake conditions.

The same point applies, even more strongly, to contemporary large language models. They can simulate concern and long-horizon planning in discourse, but their vulnerability is typically externalized. This makes them powerful cases of agency simulation without much active closure.

### 4.5 Biological Organisms

Biological organisms remain the strongest paradigm case because all four dimensions are tightly coupled. Their selective bandwidth is non-trivial, their maintenance cost is ongoing, their history is sedimented into morphology and regulation, and failure can irreversibly damage or destroy the organized whole. The framework therefore preserves the intuition that ordinary living systems are not merely more complex than passive artifacts; they are organized under a more demanding regime of maintenance and consequence.


## 5. Artificial Life as Experimental Philosophy

The value of the framework lies not only in classification but in construction. If life-likeness depends on the coupled presence of bandwidth, cost, memory, and vulnerability, then artificial life can manipulate each of these dimensions directly.

This is what philosophy looks like when it has to be built. Instead of arguing verbally about whether a system is alive, researchers can vary one dimension at a time and ask which changes alter the persistence of life-like organization.

Three design lessons follow immediately.

First, **increasing bandwidth alone is not enough**. A system can become better at tracking and exploiting multiple dimensions while remaining weakly life-like if its costs and consequences are buffered. This is one reason why high-capability digital systems can appear agentic without becoming strong candidates for life-likeness.

Second, **cost without bandwidth is not enough**. A system may consume energy or degrade physically while remaining behaviorally trivial. Mere expenditure does not create life-like organization; the expenditure must support selective closure across a non-trivial space.

Third, **memory without vulnerability is not enough**. Rich retained structure can yield impressive persistence and adaptation, but if regulatory failure can always be undone at negligible cost, the system's commitments remain shallow.

The clearest experimental consequence is a matched-agent design with three conditions:

1. **Real-stake agents**: agents face irreversible depletion or removal, and cooperation materially affects continued viability.
2. **Resettable agents**: agents face the same tasks and rewards but can be restored without substantial loss.
3. **Simulated-stake agents**: agents are trained to represent danger or mortality, but the underlying architecture remains resettable.

The prediction is not merely that the first class will perform differently. It is that only the first class should stably preserve certain long-horizon properties after reward withdrawal or perturbation: costly cooperation, durable commitment, and meaningful post-shock recovery. Resettable agents may learn these behaviors, but their persistence should be shallower. Simulated-stake agents may initially resemble real-stake agents, yet their commitments should degrade once experience reveals that apparent risk is externally buffered. Persistence can be operationalized as the number of post-perturbation episodes before cooperative behavior falls below a pre-defined baseline, for example 50% of the pre-perturbation cooperation rate.

This does not prove that any given artificial agent is alive. It does something more useful: it converts "what is life-like?" into a buildable discrimination problem. The philosophical claim is therefore experimentally exposed. If cost, memory, and vulnerability can be stripped away without changing the persistence of life-like behavior, then the framework is wrong or incomplete. If they cannot, then costly selective closure marks a real boundary in the design space of artificial life.


## 6. Conclusion

Artificial life needs criteria that are broad enough to compare different substrates and sharp enough to guide construction. This paper has argued that **costly selective closure** provides one such criterion. A system is life-like not simply because it persists, reproduces, predicts, or behaves adaptively, but because it selectively maintains a world under non-trivial cost, historical carry-over, and consequential failure.

The framework does not offer a final essence of life, and it does not claim that there is a single bright line between the living and the non-living. Its aim is more practical. It gives artificial life a minimal ontology that can be engineered, varied, and tested.

The proposal is compatible with threshold-based approaches to minimal cognition, including Unlimited Associative Learning, while remaining focused on life-likeness rather than consciousness per se (Birch et al., 2020). Cross-substrate calibration remains open; assembly depth may provide one useful anchor for the complexity term in `d_cog` (Sharma et al., 2023).

The central lesson is simple: stronger life-likeness requires stronger forms of paid commitment. To build a more life-like system, it is not enough to increase complexity, realism, or behavioral flexibility. Artificial systems must be built so that their organization matters because it must be maintained, carried forward, and can genuinely be lost.


## References

- Beer, R. D. (2004). Autopoiesis and cognition in the Game of Life. *Artificial Life*, 10(3), 309-326.
- Birch, J., Ginsburg, S., and Jablonka, E. (2020). Unlimited Associative Learning and the origins of consciousness: a primer and some predictions. *Biology & Philosophy*, 35, 56.
- Chan, B. W.-C. (2019). Lenia: Biology of artificial life. *Complex Systems*, 28(3), 251-286.
- Di Paolo, E. A. (2005). Autopoiesis, adaptivity, teleology, agency. *Phenomenology and the Cognitive Sciences*, 4(4), 429-452.
- Egbert, M. D., and Barandiaran, X. E. (2011). Quantifying normative behavior and precariousness in adaptive agency. In *Advances in Artificial Life (ECAL 2011)*, 210-217.
- Friston, K. J. (2013). Life as we know it. *Journal of the Royal Society Interface*, 10(86), 20130475.
- Kirchhoff, M. D., Parr, T., Palacios, E., Friston, K. J., and Kiverstein, J. (2018). The Markov blankets of life: Autonomy, active inference and the free energy principle. *Journal of the Royal Society Interface*, 15(138), 20170792.
- Maturana, H. R., and Varela, F. J. (1980). *Autopoiesis and Cognition: The Realization of the Living*. Reidel.
- Moreno, A., and Mossio, M. (2015). *Biological Autonomy: A Philosophical and Theoretical Enquiry*. Springer.
- Schrödinger, E. (1944). *What Is Life?* Cambridge University Press.
- Sharma, A., et al. (2023). Assembly Theory explains and quantifies selection and evolution. *Nature*, 622, 321-328.
- Terry, J. K., et al. (2021). PettingZoo: Gym for multi-agent reinforcement learning. *Advances in Neural Information Processing Systems*, 34.
- von Neumann, J. (1966). *Theory of Self-Reproducing Automata*. University of Illinois Press.
