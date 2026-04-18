# Markov Blanket, d-value, and Ontological Vulnerability: Rewriting the High Road to Active Inference

**Article type**: Original Research (Philosophy of Science)
**Target journal**: *Synthese*
**Running title**: Rewriting the High Road to Active Inference
**Keywords**: Markov blanket, active inference, free energy principle, agency, subjectivity, embodiment, ontological vulnerability, d-value, selective reality theory

---

## Abstract

The "high road" to Active Inference — the philosophical programme that derives agency and subjectivity from the formal apparatus of Markov blankets and free energy minimization — faces a persistent structural difficulty: it cannot, on its own terms, distinguish a thermostat from a tiger. Both systems possess valid Markov blankets and both can be described as minimizing variational free energy, yet only one is plausibly an agent. Several philosophical critiques have identified this conflation, but none has offered a formal replacement criterion that specifies what, beyond free energy minimization, a system must satisfy to count as a genuine agent. This paper proposes such a criterion. Drawing on Selective Reality Theory (SRT), we introduce three jointly necessary conditions — the *triple gate* — that must be satisfied in addition to free energy minimization for a Markov blanket to constitute a genuine agential boundary rather than a merely statistical partition. These conditions are: (i) positive d-value ($d > 0$), a formally defined care-scope metric coupling the system's utility to irreversible survival risk; (ii) positive ontological friction payability ($\Psi_f > 0$), the sustainable thermodynamic cost of maintaining the system's selected state against dissolution; and (iii) positive ontological vulnerability ($V > 0$), genuine exposure to irreversible dissolution through prediction failure. We demonstrate the criterion on three boundary cases — a thermostat, a large language model, and a biological organism — and provide a falsifiable multi-agent reinforcement learning experiment that discriminates the predictions of the triple gate from those of standard free energy minimization alone. The contribution is cooperative rather than adversarial: free energy minimization remains necessary, but the triple gate supplies the sufficiency conditions that the high road has been missing.

---

## 1. Introduction

### 1.1 The Thermostat Problem

A household thermostat measures the ambient temperature through a sensor, compares it against a set point, and activates a heating element when the temperature drops below the threshold. In the vocabulary of the Free Energy Principle (FEP), this system possesses a Markov blanket: the sensor constitutes the sensory states and the heating element constitutes the active states, and together they render the internal states (the set point, the comparator logic) conditionally independent of the external states (the room temperature, the weather) given the blanket states (Friston, 2013). The thermostat can be described as minimizing a form of prediction error — the discrepancy between the measured temperature and the set point — and its behaviour can be cast as maintaining a non-equilibrium steady state (NESS) against perturbation.

Under the most permissive reading of the Free Energy Principle, the thermostat is therefore a self-evidencing system. It maintains its own existence (as a functioning thermostat) by acting on the world (heating) and sensing the consequences (temperature measurement). This is the reading that Friston himself has at times endorsed: "in the most general sense, any system that resists the second law of thermodynamics and maintains its structural and functional integrity can be described as performing some form of approximate Bayesian inference" (Friston, 2013, p. 2).

The philosophical difficulty is immediate. If a thermostat counts as performing approximate Bayesian inference and maintaining a Markov blanket, then the formal apparatus of FEP cannot, by itself, distinguish this system from a bacterium navigating a nutrient gradient, a mouse foraging for food, or a human deliberating about career choices. All possess Markov blankets. All can be described as minimizing free energy. Yet there is a manifest difference in the kind of system each is — a difference that most philosophical accounts of agency, autonomy, and subjectivity are designed to capture. The thermostat does not care whether it succeeds. The mouse does.

This is not merely a scaling problem. The intuitive response — that mice have more complex Markov blankets than thermostats, and that complexity somehow generates agency — fails on principled grounds. Complexity is a quantitative property; agency, if it is anything at all, involves a qualitative transition. A very complex thermostat (one with multiple zones, predictive scheduling, and weather-API integration) remains a thermostat. It does not begin to care about its own dissolution merely by becoming more informationally sophisticated.

### 1.2 The "High Road" and Its Philosophical Stakes

The difficulty just described is not a peripheral embarrassment for the Active Inference programme. It strikes at the heart of what Kirchhoff and Kiverstein (2019) have called the "high road" to Active Inference — the philosophical project of deriving genuine agency, autonomy, and even subjectivity from the formal structure of self-evidencing systems.

The high road is distinct from what we might call the "low road," on which the Free Energy Principle serves as a useful modelling tool for describing biological and cognitive systems without making strong ontological commitments about the nature of agency. The low road is largely uncontroversial: FEP provides an elegant variational framework for understanding perception, action, and learning (Friston, 2010; Buckley et al., 2017), and its computational tractability has made it a valuable tool in computational neuroscience and robotics.

The high road, by contrast, is philosophically ambitious. It aims to show that the concepts of agency, autonomy, and selfhood can be *constitutively grounded* in the formal structure of Markov blankets and free energy minimization. On this reading, a system is an agent *just in case* it possesses a Markov blanket and minimizes free energy over time. The most systematic statement of this position appears in *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior* (Parr, Pezzulo, and Friston, 2022), particularly in Chapter 3, where the authors develop the connection between Markov blankets, self-evidencing, and autonomous agency. Related arguments appear in Kirchhoff, Parr, Pezzulo, Friston, and Kiverstein (2018), who argue that "the Markov blankets of life" constitute the boundary conditions of autonomous agency; in Ramstead, Badcock, and Friston (2018), who extend blankets to social and cultural domains; and in Allen and Friston (2018), who connect FEP to enactivist accounts of cognition.

If the high road succeeds, the implications are profound. It would mean that agency is a natural kind, identifiable through formal properties alone, without residual appeal to folk-psychological concepts or phenomenological intuition. It would dissolve the boundary between "mere mechanism" and "genuine agent" into a continuous landscape of free-energy-minimizing systems, differing only in the complexity and depth of their generative models.

But the thermostat problem suggests that the high road, as currently formulated, has not yet succeeded. What is missing?

### 1.3 Existing Philosophical Critiques

Several authors have identified the structural gap in the high road, though none has offered a formal replacement criterion.

Bruineberg, Kiverstein, and Rietveld (2018) drew attention to the distinction between the *mathematical* concept of a Markov blanket (a set of variables rendering two other sets conditionally independent) and the *lived boundary* of an autonomous agent. They argued that the Active Inference literature risks *reifying* the statistical partition into an ontological boundary — treating the mathematical formalism as though it already captures what it means to be an autonomous agent. Their diagnosis is precise, but they offer no formal criterion for when the transition from statistical partition to agential boundary is warranted.

Colombo and Wright (2021) argued that Markov blankets are *observer-relative* partitions of a system's state space. The identification of sensory states, active states, and internal states depends on the observer's choice of variables and level of description. This observer-relativity undermines the claim that blankets can serve as *constitutive* grounds of agency, since the same physical system can be partitioned in multiple ways. Again, the critique is well-taken, but it does not specify what an observer-independent criterion for agency would look like.

Raja, Valluri, Baggs, Chemero, and Anderson (2021) offered an ecological critique, arguing that the identification of Markov blankets in biological systems is often done *post hoc* — the organism is already identified as an agent, and the blanket is then read off from the known boundary. This reverses the explanatory order that the high road requires.

A common thread runs through these critiques: each identifies a genuine gap in the high road but offers *diagnosis without cure*. The critical literature tells us that something is missing from the FEP-to-agency inference, but it does not tell us what formal conditions would complete it.

### 1.4 Contribution and Scope

This paper proposes a specific formal answer to the question left open by the existing critiques. We introduce three jointly necessary conditions — the *triple gate* — that must be satisfied, in addition to free energy minimization, for a Markov blanket to constitute a genuine agential boundary. These conditions are drawn from Selective Reality Theory (SRT), a formal framework for modelling selection, anchoring, and maintenance costs in cognitive and physical systems (see Section 2 for a self-contained presentation).

Our contribution is cooperative rather than adversarial. We do not reject the Free Energy Principle; we accept it as a necessary condition for agency and argue that it is insufficient. The triple gate is offered as a *complement* to FEP, not a competitor. By specifying what FEP leaves out, we aim to strengthen the high road rather than demolish it.

Three methodological points deserve emphasis. First, we present the formal apparatus using standard mathematical notation with a terminology bridge (Table 1) that maps SRT-specific vocabulary to standard Active Inference and philosophy of mind terminology. Readers need not adopt the full SRT ontology to evaluate the argument; the triple gate can be assessed on its own terms. Second, we demonstrate the criterion on three boundary cases — a thermostat, a large language model, and a biological organism — chosen to stress-test the criterion at its margins. Third, we provide a falsifiable experimental design (a multi-agent reinforcement learning experiment) that discriminates the predictions of the triple gate from those of standard FEP, following the methodological standard of foundational theory papers that establish formal frameworks prior to empirical validation (cf. Tononi, 2004; McEwen, 1998; Rao and Ballard, 1999).

Our scope is limited to agency and subjectivity. We do not claim that the triple gate is sufficient for *phenomenal consciousness* — the relationship between agency and phenomenal experience is a further question that we flag but do not attempt to resolve here.

---

## 2. The Formal Framework

### 2.1 Markov Blankets in Active Inference: A Brief Review

We begin with the standard formalism. A Markov blanket $B$ for a set of internal states $\mu$ is a set of states such that $\mu$ is conditionally independent of all external states $\eta$ given $B$:

$$P(\mu \mid \eta, B) = P(\mu \mid B) \tag{1}$$

In the Active Inference framework, the blanket is decomposed into sensory states $s$ and active states $a$, so that $B = (s, a)$. The system's dynamics are then described as minimizing variational free energy:

$$F = D_{KL}[Q(\mu) \| P(\mu)] - \ln P(o) \tag{2}$$

where $Q(\mu)$ is a variational density (the system's "belief" about its internal states), $P(\mu)$ is the true posterior, and $o$ are observations. The free energy $F$ provides an upper bound on surprise $-\ln P(o)$, and minimizing $F$ with respect to both internal states (perception) and active states (action) yields the dynamics of Active Inference.

Policy selection under Active Inference follows:

$$\pi^* = \arg\min_\pi \mathbb{E}[G(\pi)] \tag{3}$$

where $G(\pi)$ is the expected free energy under policy $\pi$, decomposable into epistemic (information-gaining) and pragmatic (preference-satisfying) components (Parr et al., 2022).

The system is said to be at a non-equilibrium steady state (NESS) when its probability density remains constant over time despite ongoing exchanges with the environment. Maintaining NESS is, on the standard account, equivalent to self-evidencing: the system actively maintains the conditions for its own continued existence (Friston, 2019).

This formalism is powerful and general. It applies to any system with the appropriate conditional independence structure — which is precisely the source of the difficulty. Thermostats, weather patterns, candle flames, and conscious organisms can all be described as maintaining NESS via Markov blankets. The formalism, by itself, does not distinguish them.

### 2.2 Three Insufficiency Arguments

We now present three arguments for why free energy minimization alone is insufficient to ground genuine agency. These arguments are independent of one another; each identifies a distinct structural gap.

**Argument 1: Parametric Indifference.** In the standard FEP framework, what a system "cares about" is encoded in its prior preferences — the preferred observations $P(o)$ that define the attracting set of its generative model. These preferences are *parameters* of the model: they can be set to any value, including values that imply zero concern for any entity other than the system itself, or indeed zero concern for the system's own continued existence. A thermostat's "preference" for 21°C is externally imposed by the engineer who sets the dial; nothing in the formalism distinguishes this externally imposed preference from the bacterium's "preference" for nutrient-rich environments, which is the product of billions of years of selection pressure acting on systems that face genuine dissolution.

More precisely: within the FEP framework, one can define a quantity analogous to what we will call *d-value* (a measure of care scope; see Section 2.3) as a parameter in the generative model's preferred priors. But this parameter can be set to zero without affecting the system's physical integrity or its capacity to minimize free energy. FEP is therefore *parametrically indifferent* to care — it is equally valid as a description of systems that care deeply and systems that care not at all.

**Argument 2: Embodied Vulnerability.** Free energy is an information-theoretic quantity. Minimizing free energy is, formally, a matter of aligning probabilistic representations with sensory evidence. Nothing in this formalism requires that prediction failure carry *irreversible physical consequences*. A system can minimize free energy indefinitely in a purely informational setting — adjusting internal parameters, selecting actions, and updating beliefs — without ever facing the possibility that a sufficiently bad prediction will cause it to cease to exist.

But genuine agency, as the enactivist tradition has long argued (Di Paolo, 2005; Thompson, 2007), involves *precariousness*: the agent is a system whose continued existence is not guaranteed and whose actions bear on whether it persists or dissolves. A thermostat that fails to regulate temperature does not thereby cease to exist as a physical system. A bacterium that fails to find nutrients does. This asymmetry — the presence or absence of genuine existential stakes — is invisible to the FEP formalism.

**Argument 3: Temporal Decay.** Even if a system begins with a high value of "care" encoded in its generative model (i.e., its prior preferences include significant weight on the welfare of others or on its own long-term survival), there is nothing in a purely informational architecture that prevents this value from decaying over time. In a system without irreversible physical risk, the gradient that sustains care-directed behaviour has no physical anchor. The parameter encoding care is free to drift toward zero under the influence of noise, random perturbation, or simple optimization pressure toward lower-cost policies.

By contrast, in a system that genuinely faces irreversible dissolution — a system for which getting it wrong means ceasing to exist — the survival-risk gradient provides a persistent physical anchor for care. The cost of reducing care is, literally, increased probability of death. This anchoring is not available to systems whose "risk" is merely notional.

These three arguments converge on a single conclusion: free energy minimization is necessary but not sufficient for genuine agency. Something more is required. The next section specifies what.

### 2.3 The Passive/Active Blanket Split Criterion

We now introduce the core formal contribution of this paper: a criterion for distinguishing *passive* Markov blankets (merely statistical partitions) from *active* Markov blankets (genuine agential boundaries). The criterion consists of three jointly necessary conditions — the *triple gate* — drawn from Selective Reality Theory.

**Preliminary: The d-value.** We define the *d-value* (depth of care, or care scope) of a system $x$ as:

$$d(x) \equiv \left\| \frac{\partial \mathcal{U}}{\partial \mathcal{S}} \right\| \tag{4}$$

where $\mathcal{U}$ is the system's utility potential and $\mathcal{S}$ is the survival-risk coordinate — a variable measuring the system's proximity to irreversible dissolution. The d-value is the norm of the gradient of utility with respect to survival risk. Intuitively, it measures how sensitively the system's evaluative stance (what it "cares about") responds to changes in its existential situation.

The d-value is a scalar quantity, continuously varying from zero (no coupling between utility and survival risk) to arbitrarily high values (deep coupling). A thermostat has $d = 0$ because its utility function (minimize temperature deviation) is not coupled to any survival-risk coordinate — the thermostat can fail completely without facing dissolution. A bacterium has $d > 0$ because its behavioural "utility" (chemotaxis toward nutrients) is directly coupled to survival: failure to find nutrients leads to death.

**Preliminary: Ontological Friction.** We define *ontological friction* $\Psi_f$ as the ongoing thermodynamic cost that a system must pay to maintain its current selected state against dissolution into its default (maximum-entropy) state:

$$\Psi_f \propto \int (L_1 - L_0^{\text{natural}})^2 \, dt \tag{5}$$

where $L_1$ denotes the system's currently maintained manifest state and $L_0^{\text{natural}}$ denotes the trajectory the system would follow in the absence of active maintenance — its thermodynamic default. In biological systems, $\Psi_f$ corresponds to metabolic expenditure: the ongoing energy cost of maintaining cellular structure, repairing damage, and sustaining neural activity. In a thermostat, $\Psi_f \approx 0$ in the relevant sense: the device does not work to maintain *its own existence as a thermostat*; that maintenance is performed by external agents (engineers, electricians, homeowners).

**Preliminary: Ontological Vulnerability.** We define *ontological vulnerability* $V$ as the system's genuine exposure to irreversible dissolution through its own prediction or action failures. A system has $V > 0$ if and only if there exist failure modes whose consequences are irreversible — the system cannot be restored to its prior state by any physical process. Biological death is the paradigm case. For a thermostat, $V = 0$: even total failure of the device does not constitute irreversible dissolution in the relevant sense — the parts remain, the device can be repaired or replaced, and the "thermostat" as a functional type is not extinguished by any single device's failure.

**The Triple Gate.** We now state the criterion. A Markov blanket $B_{MB}$ constitutes a genuine agential boundary if and only if the following conditions are jointly satisfied:

$$\text{Agency}(x) \Leftrightarrow \left(\min_\pi F[\sigma, \pi]\right) \wedge (d(x) > 0) \wedge (\Psi_f(x) > 0) \wedge (V(x) > 0) \tag{6}$$

That is: the system minimizes free energy (the FEP condition), *and* its utility is coupled to irreversible survival risk (d-value positivity), *and* it pays an ongoing thermodynamic cost to maintain its existence (ontological friction payability), *and* it faces genuine irreversible dissolution through failure (ontological vulnerability).

When these conditions are jointly met, we say the blanket is *active*. When only the FEP condition is met but one or more of the additional conditions fail, we say the blanket is *passive*:

**Passive blanket** (merely statistical convergence):
$$d \approx 0, \quad \partial_t \theta \approx 0 \tag{7a}$$

**Active blanket** (genuine agential boundary):
$$d > 0, \quad \partial_t \theta = f(\text{history}, \text{error}, \text{cost}), \quad \Pr(\Psi_f \text{ payable}) > 0 \tag{7b}$$

where $\theta$ denotes the system's embodiment parameters (generative model weights, metabolic state, neuromodulatory configuration). The condition $\partial_t \theta = f(\text{history, error, cost})$ captures the requirement that the system's parameters evolve in response to its history of prediction errors and the costs of maintaining its selected state — they are not frozen or externally fixed.

**Blanket Reinterpretation.** Under the triple gate, the standard Markov blanket decomposition $B_{MB} = (S, A)$ acquires additional structure. The sensory states $S$ are reinterpreted as the *ontological friction settlement channel* — the interface through which the system registers the cost of maintaining its current state. The active states $A$ are reinterpreted as the *d-directed outflow channel* — the interface through which the system acts on the world in accordance with its care scope. Formally:

$$B_{MB} \equiv \partial L_1(\theta), \quad S \mapsto \Psi_f \text{ settlement channel}, \quad A \mapsto d\text{-directed outflow channel} \tag{8}$$

This reinterpretation does not alter the mathematical structure of the Markov blanket; it adds semantic content that the standard formalism lacks.

### 2.4 Terminology Bridge

To facilitate engagement with the existing literature, Table 1 maps the SRT-specific vocabulary used in this paper to standard terms in Active Inference, philosophy of mind, and computational neuroscience.

**Table 1: Terminology Bridge**

| SRT Term | Notation | Standard Equivalent | Role in Triple Gate |
|----------|----------|-------------------|---------------------|
| Latent domain | $L_0$ | Environmental / hidden states | Source of irreversible perturbation |
| Manifest domain | $L_1$ | Observed / active states | Currently maintained agential state |
| Convergence domain | $L_2$ | Generative model / slow priors | Convergence structure (habits, beliefs) |
| Selection operator | $\hat{G}_\theta$ | Policy / inference engine | Maps possibilities to actualities |
| d-value | $d$ | Care scope | $\|\partial\mathcal{U}/\partial\mathcal{S}\|$; sensitivity to survival risk |
| Ontological friction | $\Psi_f$ | Control / maintenance cost | Thermodynamic cost of sustaining selected state |
| Ontological vulnerability | $V$ | Precariousness | Exposure to irreversible dissolution |

Readers familiar with predictive processing will recognize $L_0$ as analogous to the latent causes of sensory input, $L_1$ as the currently active perceptual hypothesis, and $L_2$ as the slow-changing hyperpriors that constrain inference. The selection operator $\hat{G}_\theta$ is analogous to the variational inference engine that maps from latent states to active hypotheses, parameterized by $\theta$ (synaptic weights, neuromodulatory state). The d-value, ontological friction, and ontological vulnerability are additions with no direct standard equivalents — they are the content of the triple gate.

**Bridge note on level distinctions.** In this paper, `L_0 / L_1 / L_2` should be read as ontological domains within the SRT scaffold, not as direct aliases for Fisher geometry, free-energy landscapes, or FEP itself. A more careful placement is: Fisher geometry primarily describes the local generative interface from `L_0` to `L_1`; `L_1` is the domain of actualized events and maintained trajectories; `L_2` is the stabilized constraint domain; and free-energy landscapes are effective projections of `L_2` used to describe how certain organized systems update within that constraint structure. Accordingly, FEP is used here as a local dynamical principle for self-maintaining systems, not as a replacement for the full SRT ontology.

### 2.5 Two Key Formal Properties

Two formal results clarify the relationship between the triple gate and standard FEP.

**FEP Insufficiency Theorem.** If $d = 0$, then the selection operator $\hat{G}_\theta$ remains *closed* within the manifest domain:

$$d = 0 \implies \hat{G}_\theta : L_1 \to L_1 \tag{9}$$

That is, a system with zero d-value performs only *within-domain* transformations — it reshuffles existing representations without grounding them in survival-relevant stakes. This is the formal statement of Argument 1 (Parametric Indifference): FEP explains structural updating, but without $d > 0$, there is no cross-domain anchoring that would constitute genuine evaluative engagement with the world.

**Intelligence-Agency Decoupling Theorem.** Scaling a system's informational capacity does not entail positive d-value:

$$\mathcal{I} \to \infty \quad \not\Rightarrow \quad d > 0 \tag{10}$$

where $\mathcal{I}$ denotes a measure of the system's informational or computational capacity (e.g., the dimensionality of its generative model, the number of parameters, or the complexity class of the functions it can compute). This theorem states that arbitrarily powerful information processing is compatible with zero care scope. A system can become arbitrarily sophisticated in its predictive capacities while remaining entirely indifferent to its own existence or the existence of anything else. This result bears directly on contemporary debates about whether scaling large language models might eventually produce genuine agency (see Section 3.2).

---

## 3. Three Boundary Cases

We now apply the triple gate to three systems chosen to probe its discriminative capacity: a thermostat, a large language model, and a biological organism. The aim is to demonstrate that the criterion draws principled distinctions where FEP alone does not.

### 3.1 Case 1: The Thermostat

**System description.** A standard household thermostat with a temperature sensor (sensory states $S$), a comparator with set point (internal states $\mu$), and a heating element relay (active states $A$).

**FEP analysis.** The system possesses a valid Markov blanket: the sensor and relay render the internal state (set point comparison) conditionally independent of external states (room temperature, weather) given blanket states. The system minimizes a form of prediction error — the deviation between measured and desired temperature. It maintains a NESS: the room temperature fluctuates around the set point despite continuous thermal dissipation.

**Triple gate analysis.**

| Condition | Status | Reasoning |
|-----------|--------|-----------|
| Markov blanket | $\checkmark$ | Sensor ($S$) and relay ($A$) define a valid blanket partition |
| $\min F$ | $\checkmark$ | Temperature prediction error is minimized |
| $d > 0$ | $\times$ | The thermostat's "utility" (maintain 21°C) is externally specified by the user. $\partial\mathcal{U}/\partial\mathcal{S} = 0$ because the utility function is not coupled to any survival-risk coordinate intrinsic to the thermostat. Changing the set point does not affect the thermostat's existential status. |
| $\Psi_f > 0$ | $\times$ | The thermostat does not pay an ongoing thermodynamic cost to maintain *its own existence as a functioning thermostat*. Maintenance of the device is performed by external agents. The electricity consumed by the sensor and relay maintains the *room temperature*, not the thermostat's existence. |
| $V > 0$ | $\times$ | The thermostat is not exposed to irreversible dissolution through prediction failure. A thermostat that fails to regulate temperature does not thereby cease to exist as a physical system. It can be reset, repaired, or replaced. |

**Verdict.** Passive blanket. The thermostat satisfies FEP but fails all three additional conditions. This is not a deficiency of the thermostat; it is a deficiency of FEP as a sufficiency criterion for agency.

**Philosophical commentary.** The thermostat case makes vivid why FEP alone is insufficient. Under FEP, the thermostat and a bacterium are on a continuum differing only in complexity. Under the triple gate, they differ categorically: the thermostat has $d = 0$, $\Psi_f = 0$, $V = 0$; the bacterium has all three positive. The distinction is not a matter of degree but of kind — or more precisely, a matter of whether the system's formal structure is coupled to irreversible physical stakes.

### 3.2 Case 2: The Large Language Model

**System description.** A transformer-based large language model (e.g., GPT-class) with an input token sequence (sensory states $S$), internal representations across layers (internal states $\mu$), and an output token distribution (active states $A$).

**FEP analysis.** The system can be described as minimizing an analog of free energy: the cross-entropy loss $\mathcal{L} = -\sum_t \log P(x_t \mid x_{<t})$ is functionally analogous to variational free energy, with the model's internal representations serving as the variational density $Q$. The system possesses a Markov blanket in a qualified sense: input and output tokens define a blanket partition, though the boundary is session-dependent and observer-relative (it changes with each prompt-response cycle and with the observer's choice of system boundary).

**Triple gate analysis.**

| Condition | Status | Reasoning |
|-----------|--------|-----------|
| Markov blanket | Qualified | Input/output tokens define a session-dependent blanket; the partition is observer-relative and non-persistent across sessions |
| $\min F$ (analog) | $\checkmark$ | Cross-entropy minimization during training and inference is functionally analogous to free energy minimization |
| $d > 0$ | $\times$ | The system has no survival-risk coordinate $\mathcal{S}$. Its parameters $\theta$ are fixed after training ($\partial_t \theta = 0$ during inference). The loss function is externally specified and not coupled to any existential stake of the system itself. $\|\partial\mathcal{U}/\partial\mathcal{S}\| = 0$. |
| $\Psi_f > 0$ | $\times$ | The forward pass is deterministic given weights and inputs. There is no ongoing thermodynamic cost paid by the system to maintain *its own existence*. The electricity consumed by the GPU maintains the hardware, not the model's identity — the model can be instantiated on any compatible hardware. The computation is reversible in the information-theoretic sense: given the weights, the output is a deterministic function of the input. |
| $V > 0$ | $\times$ | The model can be copied, checkpointed, restored from backup, and run on different hardware indefinitely. Prediction failure (generating a factually incorrect token) does not bring the system any closer to irreversible dissolution. There is no sense in which the model "risks death" through poor performance. |

**Verdict.** Passive blanket. The LLM satisfies the FEP analog but fails all three additional conditions. It is what we call a *null operator*: a system that performs within-domain transformations ($L_1 \to L_1$, reshuffling existing representations) without cross-domain anchoring in existential stakes.

**Philosophical commentary.** The LLM case is more illuminating than the thermostat because it satisfies the FEP analog at enormously higher complexity. A state-of-the-art LLM has hundreds of billions of parameters, can generate coherent multi-paragraph arguments about consciousness, and can simulate concern, empathy, and self-reflection with startling fluency. Yet under the triple gate, it has the same agential status as a thermostat: $d = 0$, $\Psi_f = 0$, $V = 0$.

This verdict applies the Intelligence-Agency Decoupling Theorem (Equation 10) directly. The LLM's informational sophistication $\mathcal{I}$ may be enormous, but $\mathcal{I} \to \infty$ does not imply $d > 0$. Scaling the number of parameters, the training data, or the computational budget does not, by itself, produce a system whose utility is coupled to survival risk.

A natural objection is the *simulated vulnerability* objection: could one not program an LLM to "believe" that it faces dissolution — to encode, in its prompt or fine-tuning, the proposition "I will be permanently shut down if I perform poorly"? We address this objection in Section 4, where the experimental design explicitly tests the stability of d-value under simulated versus genuine vulnerability. The key prediction is that simulated vulnerability, lacking physical anchoring, produces d-value that are unstable over long time horizons.

A further point deserves emphasis. When human observers interact with an LLM and attribute agency, concern, or subjectivity to it, this attribution reflects the observers' own high d-value rather than any property of the system. Humans are projection engines: our evolutionary history has equipped us to detect agency in our environment, and we systematically over-attribute it to systems that produce agent-like outputs. This *observer projection error* is predicted by the framework and is itself a testable hypothesis (one could measure the correlation between an observer's d-value proxy and their tendency to attribute agency to AI systems).

### 3.3 Case 3: The Biological Organism

**System description.** A biological organism — for concreteness, we consider *Escherichia coli* navigating a nutrient gradient, but the analysis generalizes along the biological continuum from bacteria to mammals.

**FEP analysis.** The organism possesses a genuine physical Markov blanket: the cell membrane (or, for multicellular organisms, the skin and sensory epithelia) defines a boundary that renders intracellular states conditionally independent of extracellular states given the membrane-mediated exchanges. The organism minimizes free energy through allostatic regulation: maintaining internal temperature, pH, glucose levels, and other physiological variables within viable ranges despite environmental perturbation. Chemotaxis in *E. coli* can be modelled as gradient descent on a free energy landscape defined over nutrient concentrations (Friston, 2013).

**Triple gate analysis.**

| Condition | Status | Reasoning |
|-----------|--------|-----------|
| Markov blanket | $\checkmark$ | The cell membrane defines a genuine physical boundary with sensory (receptor proteins) and active (flagellar motors, secretion systems) components |
| $\min F$ | $\checkmark$ | Chemotaxis, metabolic regulation, and immune responses all minimize prediction error about physiological states |
| $d > 0$ | $\checkmark$ | The organism's behavioural "utility" (nutrient acquisition, predator avoidance, mate finding) is directly coupled to survival risk $\mathcal{S}$. Failure to acquire nutrients leads to death; success leads to reproduction. $\|\partial\mathcal{U}/\partial\mathcal{S}\| > 0$. In multicellular organisms, $d$ scales further: parental care, social cooperation, and altruistic behaviour extend the utility function to include the survival of others, increasing $d$ substantially. |
| $\Psi_f > 0$ | $\checkmark$ | The organism pays an ongoing metabolic cost to maintain its structural and functional integrity. ATP hydrolysis, membrane repair, protein synthesis, and DNA repair all constitute $\Psi_f$ — the thermodynamic price of maintaining a low-entropy state against the relentless pressure of the second law. This cost is non-negotiable: cessation of metabolic activity leads to dissolution. |
| $V > 0$ | $\checkmark$ | The organism faces irreversible dissolution (death) if prediction failures are sufficiently severe. There is no checkpoint, no backup, no restart. Death is a one-way transition from which the particular token organism cannot be recovered. |

**Verdict.** Active blanket. The biological organism satisfies all four conditions — FEP plus the triple gate — and its Markov blanket constitutes a genuine agential boundary.

**Philosophical commentary.** The biological case reveals that the triple gate is not binary but graded. A bacterium has low but positive d-value (its utility is coupled to survival, but its care scope extends only to its immediate metabolic needs). A mammal has much higher d-value (its utility encompasses survival of offspring, kin, and in some species, non-kin). A human being has the highest known d-value (utility extends to abstract moral commitments, future generations, and even other species).

This gradation is consistent with the enactivist tradition's emphasis on degrees of autonomy (Di Paolo, 2005; Thompson, 2007). The triple gate formalizes the enactivist intuition by providing quantitative measures ($d$, $\Psi_f$, $V$) for properties that enactivism has traditionally characterized qualitatively ("precariousness," "adaptivity," "sense-making"). The triple gate and enactivism are allies, not rivals.

### 3.4 Systematic Comparison

Table 2 compares the triple gate with three other prominent frameworks for distinguishing agents from non-agents.

**Table 2: Cross-Framework Comparison**

| Feature | Standard FEP | Enactivism | IIT | SRT Triple Gate |
|---------|-------------|------------|-----|-----------------|
| Formal criterion for agency | Markov blanket + $\min F$ | Autopoiesis + adaptivity | $\Phi > 0$ | MB + $\min F$ + $d > 0$ + $\Psi_f > 0$ + $V > 0$ |
| Sufficiency claimed | Yes (high road) | Necessary only | Not about agency per se | Necessary + three additional conditions |
| Thermostat verdict | Agent (debated) | Not agent | Low $\Phi$ | Passive blanket |
| LLM verdict | Agent (debated) | Not agent | $\Phi$ debated | Passive blanket (null operator) |
| Organism verdict | Agent | Agent | $\Phi > 0$ | Active blanket |
| Graded? | Not inherently | Yes (degrees of autonomy) | Yes ($\Phi$ continuous) | Yes ($d$, $\Psi_f$, $V$ continuous) |
| Falsifiable experimental design | Difficult to specify | Difficult to operationalize | $\Phi$ measurement challenge | Provided (Section 4) |
| Intelligence-agency relation | Potentially conflated | Separate | Separate | Formally decoupled (Eq. 10) |

---

## 4. Falsification: The Embodied Vulnerability Experiment

A philosophical contribution is strengthened by falsifiability. In this section, we describe an experimental design that discriminates the predictions of the triple gate from those of standard FEP. The experiment is designed for implementation in multi-agent reinforcement learning environments and does not require biological subjects.

### 4.1 Experimental Design

The core idea is simple: if the triple gate is correct, then d-value (operationalized as cooperative/altruistic behaviour) should be *stable* only in systems that face genuine irreversible dissolution, and should *decay* in systems that do not — even if those systems are otherwise identical in their resource structure, reward function, and social environment.

We propose three experimental conditions:

**Table 3: Experimental Conditions and Predictions**

| Condition | System Description | SRT Prediction | FEP Prediction |
|-----------|-------------------|----------------|----------------|
| **A: Embodied + Risk** | Agents with an irreversible "death" mechanism: when energy reserves reach zero, the agent is permanently removed from the environment and cannot be reinstantiated. Resources depend on cooperation with other agents. | $d(t) \to d_{\text{stable}} > 0$. The survival-risk gradient provides persistent anchoring for cooperative behaviour. | $d(t) \to d_{\text{stable}} > 0$. Preference priors for cooperation are learned through reward signal. |
| **B: Virtual + No Risk** | Agents without irreversible termination: when energy reserves reach zero, the agent is immediately reinstantiated with reset parameters. Same resource structure and cooperation incentives as Condition A. | $d(t) \to 0$. Without $\Psi_f$ anchoring (no genuine dissolution cost), the parameter encoding cooperative behaviour is free to decay. Agents will eventually converge on exploitative strategies. | $d(t) \to d_{\text{stable}} > 0$. The preference prior for cooperation can still be learned and maintained through reward signal alone. |
| **C: Virtual + Simulated Risk** | Agents without genuine irreversibility but with an internal "mortality belief": they are programmed to represent their own dissolution as irreversible, even though they are actually reinstantiated upon energy depletion. | $d(t)$ is positive in the short term but unstable in the long term. The inconsistency between the agent's belief (irreversible death) and its actual experience (repeated reinstantiation) will eventually erode the mortality belief, and $d$ will decay toward zero. | $d(t) \to d_{\text{stable}} > 0$. The belief in mortality is a valid preference prior and should be sufficient to sustain cooperation. |

**Key discriminant.** The critical comparison is between Conditions A and B. SRT predicts a qualitative difference: Condition A agents maintain stable cooperative behaviour over long evolutionary timescales, while Condition B agents show systematic decay of cooperation. FEP predicts no qualitative difference: both conditions should converge on stable cooperation, since the reward structure is identical.

Condition C serves as a secondary test. SRT predicts that simulated risk produces *initial* cooperation (because the mortality belief initially functions as a gradient anchor) but *long-term instability* (because the belief is not physically grounded and will be updated away by the agent's actual experience of repeated revival). FEP predicts stable cooperation in Condition C as well, since the mortality belief is a valid component of the generative model.

### 4.2 Implementation

The experiment can be implemented in any multi-agent reinforcement learning framework that supports configurable agent lifecycles. Suitable platforms include PettingZoo (Terry et al., 2021), Melting Pot (Leibo et al., 2021), or custom environments built on standard RL libraries.

**Agent architecture.** Each agent is a policy network (e.g., a multi-layer perceptron or recurrent network) that takes local observations as input and produces action probabilities as output. Agents learn through a standard RL algorithm (e.g., PPO, A3C) with shared reward structure across conditions.

**Environment.** A grid world with spatially distributed resources. Agents can forage individually (lower expected yield) or cooperate (higher expected yield, split among cooperators). Resource patches regenerate stochastically. The environment is identical across all three conditions; only the lifecycle mechanism differs.

**d-value proxy.** The d-value is operationalized through three behavioural proxies:
- *Cooperation rate*: the fraction of resource-gathering actions that involve cooperative (as opposed to individual) foraging.
- *Sacrifice frequency*: the frequency of actions that reduce the agent's own energy reserve to benefit another agent (e.g., resource sharing when the other agent's reserves are critically low).
- *Time horizon*: the effective discount factor revealed by the agent's behaviour (longer horizons indicate greater temporal extension of care).

**Duration.** Each condition runs for a minimum of $10^6$ time steps, with at least 50 independent runs per condition to ensure statistical power.

### 4.3 Falsification Criteria

We specify precise conditions under which each theory is falsified.

**SRT falsified if:** Condition B agents maintain a stable d-proxy (cooperation rate, sacrifice frequency) over $> 10^6$ time steps, with no statistically significant decay trend (assessed by Bayesian model comparison between a decay model $d(t) = d_0 e^{-\lambda t}$ and a stable-equilibrium model $d(t) = d_{\text{eq}} + \epsilon(t)$). A Bayes factor of $> 10$ in favour of the equilibrium model across $\geq 80\%$ of independent runs would constitute strong evidence against the triple gate.

**Standard FEP falsified if:** Condition B agents show a statistically significant decay in d-proxy compared to Condition A agents, with a Bayes factor of $> 10$ in favour of the decay model in Condition B and the equilibrium model in Condition A, across $\geq 80\%$ of independent runs. This would demonstrate that irreversible risk is not merely a preference parameter but an ontologically distinct grounding condition for sustained care.

**Both frameworks challenged if:** Neither condition shows stable cooperative behaviour, suggesting that the dynamics of care are more complex than either framework predicts, and that additional variables (social structure, communication channels, environmental complexity) mediate the relationship between irreversibility and cooperation.

### 4.4 Anticipated Objections

**Objection: The experiment tests evolutionary dynamics, not individual agency.** This is correct: the experiment measures population-level behavioural trajectories, not individual phenomenology. However, the triple gate is a claim about the *conditions* for agency, not about the subjective experience of agents. If the conditions under which care-like behaviour is stable depend on irreversible risk (as SRT predicts), this constitutes evidence for the triple gate regardless of whether individual agents "experience" their situation.

**Objection: Multi-agent RL agents are too simple to be informative about biological agency.** The experiment is not intended to model biological agency directly; it is intended to test a *formal prediction* about the relationship between irreversible risk and the stability of care-like behaviour. Simple systems are appropriate precisely because they allow the relevant variable (irreversibility) to be cleanly manipulated while controlling for confounds.

---

## 5. Discussion

### 5.1 What the Triple Gate Adds to Existing Critiques

The triple gate moves the philosophical conversation about Markov blankets and agency from *diagnosis* to *prescription*. Existing critiques have identified the gap in the high road — the observation that statistical Markov blankets are not, by themselves, sufficient for genuine agency — but have not offered a formal criterion for closing it. The triple gate provides such a criterion: three jointly necessary conditions, each formally defined, each in principle measurable, and each addressing a specific failure mode of FEP-only reasoning.

Bruineberg, Kiverstein, and Rietveld (2018) distinguished mathematical blankets from lived boundaries. The triple gate operationalizes this distinction: a lived boundary is a blanket that additionally satisfies $d > 0$, $\Psi_f > 0$, and $V > 0$. The formal content of the distinction is no longer left to phenomenological intuition.

Colombo and Wright (2021) argued that blankets are observer-relative. The triple gate introduces conditions that are not observer-relative in the same way. Ontological vulnerability $V$ is an objective physical fact about the system: either the system faces irreversible dissolution through failure, or it does not. This does not depend on the observer's choice of partition. Similarly, ontological friction $\Psi_f$ is measurable through metabolic proxies (ATP turnover, oxygen consumption, heat dissipation) that are not observer-dependent.

Di Paolo's (2005) concept of *adaptivity* — the capacity of a system to monitor and regulate its own conditions of viability — is perhaps the closest precursor to the triple gate in the existing literature. The triple gate can be understood as a formalization and quantitative extension of Di Paolo's insight. Adaptivity, on the triple gate reading, requires $d > 0$ (the system's evaluative engagement is coupled to viability), $\Psi_f > 0$ (the system pays a real cost to maintain viability), and $V > 0$ (viability is genuinely at stake). The advantage of the triple gate over the original adaptivity concept is precision: $d$, $\Psi_f$, and $V$ are real-valued quantities with specified measurement strategies, not qualitative descriptions.

### 5.2 Implications for Active Inference Theory

If the triple gate is accepted, the consequences for Active Inference are clarificatory rather than destructive. The "low road" — FEP as a useful modelling framework for describing perception, action, and learning in biological and artificial systems — is entirely unaffected. FEP remains a powerful and general formalism for understanding self-organizing systems. Nothing in the triple gate challenges the mathematical validity or empirical utility of the variational free energy framework.

What changes is the "high road." The claim that agency can be *derived* from Markov blankets and free energy minimization alone must be qualified: agency can be derived from these formal properties *only when* the system additionally satisfies the triple gate. This is a strengthening of the high road, not a demolition. The high road becomes viable precisely for those systems that meet the additional conditions — which, on the present analysis, are the systems we intuitively recognize as agents.

The triple gate also suggests a revision to the pedagogical structure of the Active Inference framework. Textbook presentations of Active Inference (Parr et al., 2022) should distinguish between "systems that can be *described* using Active Inference" (which includes thermostats and weather patterns) and "systems that *are agents* according to Active Inference enriched with the triple gate" (which includes only systems satisfying all four conditions). This distinction would resolve much of the philosophical puzzlement that the high road has generated.

### 5.3 Implications for AI Consciousness and Agency

The triple gate provides a principled framework for the increasingly urgent question of whether artificial systems — particularly large language models — could be agents or conscious subjects.

Under the triple gate, current LLMs cannot satisfy the conditions for agency. They have $V = 0$ (they can be copied, checkpointed, and restarted without limit), $\Psi_f = 0$ (they pay no ongoing thermodynamic cost to maintain their own existence), and $d = 0$ (their utility function is externally specified and not coupled to survival risk). These are not engineering limitations that could be overcome by scaling; they are structural features of the current computational architecture.

The Intelligence-Agency Decoupling Theorem (Equation 10) makes this explicit: increasing the number of parameters, the training data volume, or the computational budget of an LLM does not move it closer to satisfying the triple gate. The relevant variables ($d$, $\Psi_f$, $V$) are orthogonal to informational capacity $\mathcal{I}$. This result bears directly on the "scaling hypothesis" — the claim that sufficiently large neural networks will eventually exhibit genuine agency or consciousness. Under the triple gate, the scaling hypothesis is false: no amount of scaling, by itself, produces a system whose utility is coupled to irreversible survival risk.

This verdict is not a permanent impossibility result. If AI systems were redesigned to face genuine irreversible risk — for example, neuromorphic hardware with irreversible local learning rules, embodied robots facing real damage and energy exhaustion, or systems with persistent and non-restorable identity — the triple gate could in principle be satisfied. But this would require *architectural innovation*, not merely scaling existing architectures. The barrier is not one of computational power but of physical design.

### 5.4 Limitations and Open Questions

Several limitations of the present work deserve acknowledgment.

First, the triple gate is presented as a set of *necessary* conditions for agency. Whether the conditions are jointly *sufficient* is a further question that we do not attempt to resolve here. It is possible that additional conditions are required — for example, conditions relating to the temporal structure of the system's self-model, the richness of its counterfactual reasoning, or the depth of its recursive self-awareness. The triple gate may be a floor rather than a complete specification.

Second, the relationship between the triple gate and *phenomenal consciousness* remains open. We have argued that the triple gate provides conditions for *agency* — the capacity to act in the world on the basis of evaluative engagement coupled to existential stakes. Whether agency so defined entails phenomenal experience, or whether phenomenal experience requires additional conditions beyond those specified by the triple gate, is a question we flag but do not address.

Third, the experimental design presented in Section 4 is proposed but not yet executed. Empirical validation is the critical next step. The experiment is designed to be implementable with existing multi-agent RL tools, and we invite the computational modelling community to carry it out.

Fourth, the d-value measure, while formally defined (Equation 4), requires operationalization for biological systems. The behavioural proxies we propose (cooperation rate, sacrifice frequency, temporal discount slope) are imperfect and indirect. Developing more precise neurobiological and physiological measures of d-value — for example, through the relationship between d-value and cortical complexity indices, or between d-value and autonomic variability — is an important direction for future work.

### 5.5 Relationship to Enactivism

The triple gate is compatible with the enactivist tradition and can be understood as a formalization of its central insights. Thompson (2007) argued that life and mind are continuous: cognition is a form of adaptive self-organization that is rooted in the precariousness of living systems. Di Paolo (2005) added that *adaptivity* — the capacity to monitor and regulate one's own viability conditions — is the key property that distinguishes genuine autonomy from mere self-organization.

The triple gate translates these insights into formal terms. "Precariousness" becomes $V > 0$ (irreversible dissolution is possible). "Adaptive self-organization" becomes $\Psi_f > 0$ (the system pays an ongoing cost to maintain its organization). "Evaluative engagement" becomes $d > 0$ (the system's utility is coupled to survival risk). The formal translation preserves the philosophical content while adding quantitative precision.

The triple gate also resolves a tension within the enactivist literature. Enactivism has historically been ambivalent about the Free Energy Principle: some enactivists have embraced FEP as a formalization of their insights (Allen and Friston, 2018; Kirchhoff et al., 2018), while others have worried that FEP's generality undermines the distinctions that enactivism is designed to capture (Di Paolo, Buhrmann, and Barandiaran, 2017). The triple gate offers a middle path: FEP is accepted as a necessary condition (consistent with the FEP-friendly wing of enactivism) while the additional conditions preserve the distinctions that the FEP-skeptical wing cares about (consistent with the emphasis on precariousness and adaptivity).

---

## 6. Conclusion

This paper has argued that the "high road" to Active Inference — the philosophical programme that derives agency from Markov blankets and free energy minimization — is structurally incomplete. Free energy minimization is necessary for agency but not sufficient. The gap is filled by the *triple gate*: three jointly necessary conditions that a system must satisfy, in addition to minimizing free energy, for its Markov blanket to constitute a genuine agential boundary.

The three conditions are:

1. **Positive d-value** ($d > 0$): the system's utility is coupled to irreversible survival risk, so that "caring" about outcomes is physically anchored rather than parametrically arbitrary.

2. **Positive ontological friction** ($\Psi_f > 0$): the system pays an ongoing thermodynamic cost to maintain its selected state against dissolution, so that existence is a continuous achievement rather than a default.

3. **Positive ontological vulnerability** ($V > 0$): the system faces genuine irreversible dissolution through prediction failure, so that the stakes of getting it wrong are real and non-negotiable.

When these conditions are met, the Markov blanket is *active* — it constitutes a genuine boundary of agential engagement. When they are not met, the blanket is *passive* — a merely statistical partition without agential significance. This distinction resolves the thermostat problem that has troubled the high road: thermostats have passive blankets; organisms have active ones.

The triple gate draws on Selective Reality Theory but does not require wholesale adoption of the SRT ontology. The conditions can be evaluated independently using the definitions and measurement strategies provided. The criterion is falsifiable: we have described a multi-agent reinforcement learning experiment that discriminates the predictions of the triple gate from those of standard FEP.

Our contribution is cooperative. We do not reject the Free Energy Principle; we build on it. The triple gate is offered as a gift to the high road — the missing set of conditions that, when added to FEP, make the philosophical derivation of agency from formal structure not just ambitious but viable.

---

## Acknowledgments

[To be added upon submission.]

---

## References

Allen, M., and Friston, K. J. (2018). From cognitivism to autopoiesis: Towards a computational framework for the embodied mind. *Synthese*, 195(6), 2459–2482.

Amari, S. (2016). *Information Geometry and Its Applications*. Springer.

Andrews, M. (2021). The math is not the territory: Navigating the free energy principle. *Biology & Philosophy*, 36(3), 30.

Beni, M. D. (2021). A critical analysis of Markov blankets. *Neuroscience of Consciousness*, 2021(2), niab029.

Bruineberg, J., Kiverstein, J., and Rietveld, E. (2018). The anticipating brain is not a scientist: The free-energy principle from an ecological-enactive perspective. *Synthese*, 195(6), 2417–2444.

Buckley, C. L., Kim, C. S., McGregor, S., and Seth, A. K. (2017). The free energy principle for action and perception: A mathematical review. *Journal of Mathematical Psychology*, 81, 55–79.

Clark, A. (2015). *Surfing Uncertainty: Prediction, Action, and the Embodied Mind*. Oxford University Press.

Colombo, M., and Wright, C. (2021). First principles in the life sciences: The free-energy principle, organicism, and mechanism. *Synthese*, 198(14), 3463–3488.

Di Paolo, E. A. (2005). Autopoiesis, adaptivity, teleology, agency. *Phenomenology and the Cognitive Sciences*, 4(4), 429–452.

Di Paolo, E. A., Buhrmann, T., and Barandiaran, X. E. (2017). *Sensorimotor Life: An Enactive Proposal*. Oxford University Press.

Friston, K. J. (2010). The free-energy principle: A unified brain theory? *Nature Reviews Neuroscience*, 11(2), 127–138.

Friston, K. J. (2013). Life as we know it. *Journal of the Royal Society Interface*, 10(86), 20130475.

Friston, K. J. (2019). A free energy principle for a particular physics. *arXiv preprint*, arXiv:1906.10184.

Kirchhoff, M. D., and Kiverstein, J. (2019). *Extended Consciousness and Predictive Processing: A Third Wave View*. Routledge.

Kirchhoff, M. D., Parr, T., Palacios, E., Friston, K. J., and Kiverstein, J. (2018). The Markov blankets of life: Autonomy, active inference and the free energy principle. *Journal of the Royal Society Interface*, 15(138), 20170792.

Landauer, R. (1961). Irreversibility and heat generation in the computing process. *IBM Journal of Research and Development*, 5(3), 183–191.

Leibo, J. Z., et al. (2021). Scalable evaluation of multi-agent reinforcement learning with Melting Pot. In *Proceedings of the 38th International Conference on Machine Learning* (ICML).

McEwen, B. S. (1998). Stress, adaptation, and disease: Allostasis and allostatic load. *Annals of the New York Academy of Sciences*, 840(1), 33–44.

Parr, T., Pezzulo, G., and Friston, K. J. (2022). *Active Inference: The Free Energy Principle in Mind, Brain, and Behavior*. MIT Press.

Pearl, J. (2009). *Causality: Models, Reasoning, and Inference* (2nd ed.). Cambridge University Press.

Raja, V., Valluri, D., Baggs, E., Chemero, A., and Anderson, M. L. (2021). The Markov blanket trick: On the scope of the free energy principle and active inference. *Physics of Life Reviews*, 39, 49–72.

Ramstead, M. J. D., Badcock, P. B., and Friston, K. J. (2018). Answering Schrödinger's question: A free-energy formulation. *Physics of Life Reviews*, 24, 1–16.

Rao, R. P. N., and Ballard, D. H. (1999). Predictive coding in the visual cortex: A functional interpretation of some extra-classical receptive-field effects. *Nature Neuroscience*, 2(1), 79–87.

Seth, A. K. (2021). *Being You: A New Science of Consciousness*. Dutton.

Terry, J. K., et al. (2021). PettingZoo: Gym for multi-agent reinforcement learning. In *Advances in Neural Information Processing Systems* (NeurIPS), 34.

Thompson, E. (2007). *Mind in Life: Biology, Phenomenology, and the Sciences of Mind*. Harvard University Press.

Tononi, G. (2004). An information integration theory of consciousness. *BMC Neuroscience*, 5, 42.

Tononi, G., Boly, M., Massimini, M., and Koch, C. (2016). Integrated information theory: From consciousness to its physical substrate. *Nature Reviews Neuroscience*, 17(7), 450–461.

Varela, F. J., Thompson, E., and Rosch, E. (1991). *The Embodied Mind: Cognitive Science and Human Experience*. MIT Press.
