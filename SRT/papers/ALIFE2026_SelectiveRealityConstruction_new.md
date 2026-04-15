# What Makes an Artificial System Life-Like? Costly Selection as a Minimal Criterion

## Abstract

Artificial life has long relied on a family resemblance approach to life-likeness. Self-reproduction, metabolism, autopoiesis, adaptive behavior, and predictive closure each capture something important, yet none cleanly separates systems that merely update from systems that must sustain a way of existing. This paper proposes a minimal criterion for life-likeness drawn from Selective Reality Theory: a system is life-like to the extent that it exhibits **costly selective closure**. Such a system does not simply persist or optimize; it selectively constructs and maintains an actionable world under non-trivial cost, memory, and consequence. I formalize this through four coupled dimensions: selective bandwidth (`d`), maintenance cost (`Psi_f`), hysteretic memory (`eta`), and irreversible vulnerability (`V`). Together they distinguish **passive closure** from **active closure**. Passive closure characterizes systems whose apparent agency is fully buffered by external design or reset; active closure characterizes systems whose organization must be continuously paid for and can genuinely fail. The framework is then applied to canonical artificial life cases, including Conway's Game of Life, Lenia, autopoietic agents, and resettable reinforcement-learning agents. The key claim is constructive rather than merely definitional: philosophy becomes experimental when we can vary these dimensions in built systems and observe which combinations produce durable cooperation, long-horizon commitment, and post-perturbation recovery. The result is a substrate-flexible gradient of life-likeness and a practical design agenda for artificial life research: if we want stronger forms of life-likeness, we must build systems that pay to maintain selective commitments rather than merely simulate them.

**Keywords**: artificial life, life-likeness, autopoiesis, active inference, selective reality theory, agency, artificial agents


## 1. Introduction

Artificial life has always been more than a technical program. It is also a way of doing philosophy by construction. Instead of asking only what life is in the abstract, artificial life asks what must be built, varied, and maintained for something life-like to appear. The question is therefore not just classificatory. It is operational: what should count as a success condition for artificial life?

This remains unsettled. Different traditions emphasize different signatures. Self-reproduction captures evolutionary open-endedness but excludes sterile organisms and many familiar living phases. Metabolism captures energetic organization but risks including fire. Autopoiesis captures self-producing organization but is often difficult to compare across substrates. More recent frameworks based on predictive processing or active inference highlight adaptive regulation and boundary maintenance, but by their very generality they can blur the difference between organisms, thermostats, and highly capable digital agents.

For artificial life, this creates a practical problem. Without a shared operational criterion, systems with very different ontological profiles are often discussed in the same vocabulary of "adaptation," "agency," or "self-maintenance." We can describe Conway patterns, Lenia morphologies, soft robots, language models, and bacteria as exhibiting some kind of organization, but not all organization is equally life-like. A criterion is needed that is broad enough to compare unlike systems while still sharp enough to distinguish mere update from consequential self-maintenance.

This paper proposes such a criterion. Drawing on Selective Reality Theory (SRT), I argue that the minimal signature of life-likeness is **costly selective closure**. A life-like system is not merely one that persists, computes, or reproduces. It is one that:

1. selectively couples to a non-trivial portion of its world,
2. pays a non-zero cost to maintain that coupling,
3. carries the effects of past selections forward in memory and structure, and
4. faces meaningful consequences if its regulation fails.

The point is not to introduce a new essence of life. The point is to give artificial life a buildable discrimination rule. On this view, life-likeness is a gradient, not a binary threshold. Systems can be more or less life-like depending on the degree to which they exhibit selective bandwidth, maintenance cost, hysteresis, and vulnerability.

The contribution is threefold. First, I offer a compact formal vocabulary for comparing biological and artificial systems without presupposing a single substrate. Second, I apply the framework to canonical cases in artificial life. Third, I show how the framework turns a philosophical dispute into an experimental program: by manipulating cost, memory, and vulnerability in artificial systems, we can test which combinations produce durable life-like organization rather than its simulation.


## 2. Why Existing Criteria Stop Too Early

Classical definitions of life usually succeed by being locally right and globally incomplete. Reproduction identifies one important route by which life persists through time, but not all living systems are reproducing at every moment, and many life-like artifacts may never reproduce at all. Metabolism captures energetic openness and thermodynamic work, but by itself it says too little about selectivity or organization. Autopoiesis comes closer by focusing on self-producing organization, yet its explanatory strength can become a weakness when researchers need tractable comparisons across different media.

The same problem appears in more recent discussions of adaptive systems. A system can maintain a boundary, minimize error, or stabilize a policy without this being enough to make it meaningfully life-like. A thermostat is organized, robust, and responsive. A large language model can exhibit astonishing behavioral complexity. A reinforcement-learning agent can maximize reward under changing conditions. Yet there remains an intuitive and theoretical difference between systems that merely implement a designer's structure and systems whose way of existing is itself under stake.

The missing distinction is between **update** and **consequential self-maintenance**.

Many systems update. Far fewer must continuously pay to remain what they are. In ordinary biological cases, failure has non-trivial consequences: the organism exhausts energy, loses integrity, suffers damage, or dies. Its regulatory activity therefore has existential weight. By contrast, many computational systems operate under extensive buffering. They may be reset, copied, restored, paused, or run again with little cost to their identity. They can display goal-directed behavior without bearing much of the burden that makes biological regulation matter.

Artificial life needs a criterion that can register this difference without collapsing into substrate chauvinism. We should not require carbon chemistry. But neither should we treat every well-regulated or behaviorally rich system as equally life-like. The question is not whether a system behaves as if it had a world. The question is whether it must selectively construct and maintain such a world under real cost and consequence.


## 3. Costly Selective Closure

### 3.1 Selective Construction

The proposed framework begins with a simple thought: every candidate system faces a space of possible states, perturbations, and interactions. Life-like systems do not passively occupy this space. They selectively stabilize a small and usable region of it.

Let `Omega_t` denote the system's currently accessible possibility space and `x_t` its maintained state. We can write the next state schematically as

$$
x_{t+1} = (1 - \eta)\,\hat{G}_{\theta}[\Omega_t] + \eta x_t
$$

where `G_hat_theta` is a selection operator and `eta in [0,1]` is a hysteresis term. The equation is intentionally minimal. It says only that current organization depends partly on present selection and partly on retained structure from the past. When `eta = 0`, the system is purely reactive. When `eta > 0`, previous selections constrain current ones.

This is what I call **selective reality construction**: a system does not encounter all possible states equally. It actively compresses possibilities into an actionable world. In biological organisms this is obvious. What counts as relevant is shaped by metabolism, morphology, history, and need. In artificial systems, the same question can be posed constructively: what dimensions does the system track, what does it ignore, and what does it take to keep that selection stable?

### 3.2 Four Dimensions

The degree of life-likeness is evaluated along four coupled dimensions.

**Selective bandwidth (`d`).** This is the effective dimensionality of the system's selective coupling to its environment. One convenient formalization is the effective rank of the operator's spectrum:

$$
d = D_{eff}(\hat{G}) = \frac{(\sum_i \lambda_i)^2}{\sum_i \lambda_i^2}
$$

where the `lambda_i` are the salient eigenvalues of the system's selective dynamics. Intuitively, `d` tracks how many independent dimensions genuinely matter to the system. A low-`d` system couples along one or a few tightly constrained dimensions. A high-`d` system maintains concern across a wider space of temporal, spatial, social, or behavioral variables.

**Maintenance cost (`Psi_f`).** A system may display organized behavior while paying little of the cost itself. To count as strongly life-like, its organization must require ongoing expenditure. `Psi_f` denotes the cost of maintaining the selected state against drift, dispersion, or collapse. In biological settings this includes metabolic work; in artificial settings it may include energy, irreversible weight change, structural degradation, or other non-trivial maintenance burdens.

**Hysteretic memory (`eta`).** Life-like systems do not simply react in the present. Their prior selections sediment into present organization. `eta` measures this historical carry-over. It is not just explicit memory storage; it includes any mechanism by which past regulation becomes embodied as current bias, constraint, or habit.

**Irreversible vulnerability (`V`).** Finally, a system becomes more life-like when failure cannot be costlessly undone. `V > 0` means that bad regulation has non-trivial consequences for the continuation of the system's organization. This need not imply literal death in every artificial case, but it does require more than symbolic risk. If the system can be freely reset, cloned, or restored without loss of organization, its vulnerability is weak.

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
| Crystal | None | None | None | None | Stable but not life-like |
| Conway's Game of Life pattern | Very low | None | Very low | None | Organized update, not active closure |
| Lenia morphology | Low | Low/emergent | Low | Low | Weakly life-like |
| Autopoietic/evolved embodied agent | Moderate | Positive | Positive | Positive | Moderately life-like |
| Resettable RL agent | Moderate to high | Often externally buffered | Positive | Weak | Behaviorally rich but ontologically shallow |
| Biological organism | High | Positive | Positive | Strong | Strong active closure |

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

The value of the framework lies not only in classification but in construction. If life-likeness depends on the coupled presence of bandwidth, cost, memory, and vulnerability, then artificial life can treat each of these as an experimental variable.

This is what philosophy looks like when we have to build it. Instead of arguing verbally about whether a system is alive, we can vary one dimension at a time and observe what changes.

Three design lessons follow immediately.

First, **increasing bandwidth alone is not enough**. A system can become better at tracking and exploiting multiple dimensions while remaining weakly life-like if its costs and consequences are buffered. This is one reason why high-capability digital systems can appear agentic without becoming strong candidates for life-likeness.

Second, **cost without bandwidth is not enough**. A system may consume energy or degrade physically while remaining behaviorally trivial. Mere expenditure does not create life-like organization; the expenditure must support selective closure across a non-trivial space.

Third, **memory without vulnerability is not enough**. Rich retained structure can yield impressive persistence and adaptation, but if regulatory failure can always be undone at negligible cost, the system's commitments remain shallow.

The clearest experimental consequence is a matched-agent design with three conditions:

1. **Real-stake agents**: agents face irreversible depletion or removal, and cooperation materially affects continued viability.
2. **Resettable agents**: agents face the same tasks and rewards but can be restored without substantial loss.
3. **Simulated-stake agents**: agents are trained to represent danger or mortality, but the underlying architecture remains resettable.

The prediction is not merely that the first class will perform differently. It is that only the first class should stably preserve certain long-horizon properties after reward withdrawal or perturbation: costly cooperation, durable commitment, and meaningful post-shock recovery. Resettable agents may learn such behaviors, but their persistence should be shallower. Simulated-stake agents may initially resemble real-stake agents, yet their commitments should degrade once experience reveals that apparent risk is externally buffered.

This does not prove that any given artificial agent is alive. It does something more useful: it converts "what is life-like?" into a buildable discrimination problem. The philosophical claim is therefore experimentally exposed. If cost, memory, and vulnerability can be stripped away without changing the persistence of life-like behavior, then the framework is wrong or incomplete. If they cannot, then costly selective closure marks a real boundary in the design space of artificial life.


## 6. Conclusion

Artificial life needs criteria that are broad enough to compare different substrates and sharp enough to guide construction. I have argued that **costly selective closure** provides such a criterion. A system is life-like not simply because it persists, reproduces, predicts, or behaves adaptively, but because it selectively maintains a world under non-trivial cost, historical carry-over, and consequential failure.

The framework does not offer a final essence of life, and it does not claim that there is a single bright line between the living and the non-living. Its aim is more practical. It gives artificial life a minimal ontology that can be engineered, varied, and tested.

On this view, the deepest lesson is simple: stronger life-likeness requires stronger forms of paid commitment. To build a more life-like system, we must do more than increase complexity or realism. We must build systems whose organization matters to them because it must be maintained, carried forward, and can genuinely be lost.


## References

- Beer, R. D. (2004). Autopoiesis and cognition in the Game of Life. *Artificial Life*, 10(3), 309-326.
- Chan, B. W.-C. (2019). Lenia: Biology of artificial life. *Complex Systems*, 28(3), 251-286.
- Di Paolo, E. A. (2005). Autopoiesis, adaptivity, teleology, agency. *Phenomenology and the Cognitive Sciences*, 4(4), 429-452.
- Friston, K. J. (2013). Life as we know it. *Journal of the Royal Society Interface*, 10(86), 20130475.
- Kirchhoff, M. D., Parr, T., Palacios, E., Friston, K. J., and Kiverstein, J. (2018). The Markov blankets of life: Autonomy, active inference and the free energy principle. *Journal of the Royal Society Interface*, 15(138), 20170792.
- Maturana, H. R., and Varela, F. J. (1980). *Autopoiesis and Cognition: The Realization of the Living*. Reidel.
- Schrödinger, E. (1944). *What Is Life?* Cambridge University Press.
- Terry, J. K., et al. (2021). PettingZoo: Gym for multi-agent reinforcement learning. *Advances in Neural Information Processing Systems*, 34.
- von Neumann, J. (1966). *Theory of Self-Reproducing Automata*. University of Illinois Press.
