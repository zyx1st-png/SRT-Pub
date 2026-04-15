<!-- converted from paper_ontological_friction.docx -->

# Ontological Friction: A Testable Cross-Modal Cost Model for Executive Breakdown
Article type: Hypothesis and Theory
Target journal: Frontiers in Neuroscience
Running title: Ontological Friction in Executive Breakdown
Word count: 10,069 words (main text, excluding abstract, figures, tables, captions, and references)
Abstract: 223 words
Figures/Tables: 5 figures; 5 tables
Keywords: ontological friction, executive dysfunction, task-switching, predictive processing, psychophysiology, clinical neuroscience, linguistic biomarker, hypothesis-driven modeling

## Abstract
The dissociation between knowing and doing, where an agent can represent an appropriate action but fails to execute it, is common across neurological and psychiatric disorders and remains insufficiently formalized. We propose a latent cross-modal control-cost factor (termed ontological friction, ) for this gap, where “ontological” is used as an explanatory label for maintenance costs spanning representation and action layers. Within Selective Reality Theory,  is specified at two levels: an empirical latent variable and a mechanistic control-cost model (integrated control effort and information-geometric deviation under baseline drift). Subjective distress is modeled as a hazard-family function of smoothed friction change under appraisal constraints, and executive collapse is formulated as a bandwidth saturation event when friction and noise costs exceed available selection power. To maximize falsifiability, the primary validation chain is low-cost and replicable: behavioral control tasks, adjusted linguistic modal-ratio scoring, and autonomic physiology (HRV/SCR). Neural and biochemical markers (e.g., PCI, Fisher geometry, theta-gamma coupling, ROS) are positioned as optional later-phase adjudication tests. Major depressive disorder, obsessive-compulsive disorder, and Parkinson’s disease are used as boundary use cases for parameter stress-testing rather than as claims of full nosological replacement. We formulate five pre-registration-ready hypotheses with explicit falsification thresholds, including estimation of a critical load parameter for the knowing-doing transition. No new data are presented. The manuscript provides a theory-to-experiment framework for direct empirical adjudication.

## 1. Introduction
### 1.1 The Knowing–Doing Gap
Consider three clinical scenarios. A patient with Parkinson’s disease can describe, in precise detail, the sequence of movements required to stand from a chair — yet remains seated, unable to initiate the motor program. A patient with obsessive-compulsive disorder recognizes that her hand-washing compulsion is irrational and disproportionate — yet cannot resist executing it. A patient with major depressive disorder articulates what steps would improve his situation — exercise, social contact, medication adherence — yet lies immobile, unable to translate knowledge into action.
These scenarios share a striking structural similarity: the agent’s representational model of the world and of appropriate action remains intact, while the capacity to implement that knowledge is compromised. This dissociation between knowing and doing — what we term the knowing–doing gap — is among the most clinically significant yet theoretically underspecified phenomena in cognitive neuroscience. While executive function research has catalogued the behavioral signatures of this gap extensively (Miyake et al., 2000; Diamond, 2013), and neuroimaging studies have identified associated neural substrates (Stuss and Alexander, 2007; Miller and Cohen, 2001), no existing framework provides a unified quantitative account that explains why knowledge and action can decouple, predicts when they will, and specifies how to measure the decoupling across behavioral, physiological, neural, and linguistic domains.
### 1.2 Limitations of Current Frameworks
Several theoretical frameworks address aspects of the knowing–doing gap, but each captures only a partial picture.
Cognitive load theory (Sweller, 1988; Sweller et al., 2019) quantifies the demands placed on working memory during learning and task execution. While influential in educational psychology, it remains a purely behavioral construct without physiological or neural grounding, and it does not address the maintenance cost of sustaining a selected state over time against competing defaults.
The Free Energy Principle (FEP; Friston, 2010) provides an elegant variational framework in which organisms minimize prediction error. The complexity term in variational free energy () captures some of what we mean by “friction” — the cost of maintaining a model that deviates from priors. However, FEP treats this cost as something to be minimized, and does not provide a framework for situations in which sustained high deviation cost is adaptive (e.g., creative problem-solving, ethical resistance to default heuristics) or for the failure mode in which deviation cost overwhelms the system’s capacity.
Integrated Information Theory (IIT; Tononi et al., 2016) offers a scalar measure of consciousness () based on the irreducibility of cause-effect structures. While  captures integration, it does not address the dynamic cost of maintaining integrated states or the transition costs between states. It provides a snapshot measure, not a cost function.
Allostatic load (McEwen, 1998; McEwen and Stellar, 1993) captures the cumulative physiological cost of chronic stress adaptation, but operates at too coarse a temporal grain to explain moment-to-moment executive breakdowns, and lacks a formal connection to information-theoretic quantities.
Classical ego depletion models conceptualize self-control as a limited resource (Baumeister et al., 1998), but glucose-specific substrate interpretations have received substantial methodological criticism, weak meta-analytic support, and replication concerns (Hagger et al., 2016; Vadillo et al., 2016). This motivates treating metabolic readouts as testable correlates rather than fixed assumptions.
These frameworks are not interchangeable with the present proposal. The  framework makes three specific predictions that are jointly stronger than prior accounts: a nonlinear critical-load transition (), context-sensitive modal-language shifts (), and convergence of behavioral-linguistic-physiological indicators onto a single latent factor.
The critical gap is this: none of these frameworks provides a single formally defined quantity that (a) is grounded in both information-theoretic and thermodynamic principles, (b) generates measurable predictions across behavioral, physiological, neural, and linguistic domains simultaneously, (c) explains the knowing–doing gap as a specific failure mode, and (d) produces disorder-specific clinical predictions.
### 1.3 Contribution and Scope
In this paper, we introduce ontological friction (), formalized within Selective Reality Theory (SRT), as a candidate unifying quantity. We define  as a measurable control-cost construct and operationalize it through a staged strategy: core low-cost validation first (behavioral + linguistic + autonomic physiology), then high-cost expansion modalities (neural and biochemical). The clinical examples (MDD, OCD, and PD) are treated as boundary use cases for parameter drift and gating stress tests, not as attempts to fully replace existing disease-specific pathophysiology. The main text uses a compact three-level notation (); a mapping to standard control/predictive-processing terminology is provided in Appendix A for readers who prefer established vocabulary.
This is a theoretical and computational contribution. We report no empirical data. We follow the tradition of foundational theoretical papers in consciousness science (Tononi, 2004), allostatic regulation (McEwen, 1998), and predictive processing (Rao and Ballard, 1999) that established formal frameworks prior to systematic empirical validation. Our aim is to provide the theoretical architecture and measurement protocols that enable such validation.

## 2. Theoretical Framework: Selective Reality Theory and Ontological Friction
### 2.0 Standard Terminology Bridge (Used Throughout Main Text)
To reduce interpretation burden, the main text uses a compact notation with direct computational-neuroscience meanings:
: estimable control/execution cost (latent cross-modal factor). The term “ontological” is naming-level shorthand for cross-layer maintenance/switching cost, not a required metaphysical commitment.
: available control budget (selection capacity proxy).
: candidate policy space, currently executed state, and slow prior/hyperprior constraints.
: resource-bounded selection operator from candidate policies to active execution.
Appendix A retains the full SRT-to-standard mapping for readers who want one-to-one terminology correspondence.
### 2.1 A Minimal Selective Reality Theory Primer
Selective Reality Theory (SRT) is used here as a modeling architecture for selection and control costs. In this manuscript, the three-domain decomposition is treated as a pragmatic level-of-description choice rather than a mandatory metaphysical claim. Readers do not need to adopt a new global ontology to evaluate : the same equations can be read as compatible with working-memory gating accounts and active-inference/predictive-coding control loops.
(candidate space / policy-relevant hypothesis space).  denotes the candidate state or strategy set available to the agent at a given time. Operationally, this is the policy-relevant hypothesis space from which selections are made.
(currently executed percept-action state).  denotes the active state being implemented now (perceptual interpretation plus action policy in force).
(slow variables).  denotes slower constraints that shape future selections, including habits, model priors, and hyperpriors. In this paper,  is the level connected to parameter drift, switching viscosity, and trait-like control limits.
The three layers are linked by the selection operator , which maps candidates into executed states:

where  denotes finite embodiment parameters (e.g., network weights, neuromodulatory state, and metabolic constraints). The subscript  emphasizes resource-bounded selection.
The convergence domain updates through stabilization:

Within this architecture, the key claim is that maintaining or switching  relative to a baseline policy trajectory incurs a measurable control cost, termed ontological friction (), that constrains executive function.
### 2.2 Ontological Friction: Formal Definition
We define ontological friction through a two-level specification designed for direct estimation and mechanistic testing.
Definition 1A (Level-0 empirical latent variable). At the measurement level,  is a latent factor jointly loaded by behavioral, linguistic, and physiological indicators (with neural and biochemical indicators used as expansion modalities):

where  are standardized observed indicators,  are factor loadings, and  are residuals. This is the estimand used in SEM/CFA analyses.
Definition 1B (Level-1 mechanistic control cost). At the mechanism level, let state dynamics be

where  is control input and  is the no-control (baseline drift) trajectory. Ontological friction is instantiated as integrated control effort:

with an information-geometric comparator model:

where  denotes the baseline-policy distribution. Under regularity conditions (e.g., locally smooth trajectories and second-order KL expansion in exponential-family neighborhoods), the KL form admits a Fisher-metric approximation:

(Amari, 2016). In this paper,  denotes the Level-0 latent construct, while Equations (3c), (3d), and (3d’) are treated as competing/related mechanism models to be compared empirically rather than universally equivalent identities.
Mechanism-model comparison plan. Equation (3c) is treated as a control-energy model best matched to trial-level demand manipulations (e.g., switch/inhibition load), whereas Equations (3d)/(3d’) are treated as distributional-deviation models for belief-drift or habit-override regimes. In empirical programs, matched hierarchical models will be fit to the same outcomes and compared with out-of-sample criteria (LOO/WAIC, with Bayes factors where model regularity allows). Pre-registered interpretation is: if the 3c-family wins, friction is operationally summarized as control effort; if 3d/3d’ wins, friction is better summarized as information-geometric deviation; if no mechanism family dominates, Equation (3a) remains the estimand and mechanism equations are treated as context-specific modules.
Definition 2 (Distress Hazard Family). Subjective distress is modeled as a hazard-family function of smoothed friction change and appraisal state:

where  is a smoothed friction trajectory (window ),  is a monotone link (e.g., logistic), and Appraisal captures contextual evaluation (Gaab et al., 2005). In the local linear limit with approximately constant appraisal, Equation (4) reduces to the familiar approximation . This preserves the core intuition that rapidly increasing friction is destabilizing while avoiding the stronger and less defensible claim that all pain is solely driven by raw derivatives.
For pre-registration,  is treated as a sensitivity parameter (default grid: 10 s, 30 s, 60 s, or trial-window analogs), and Appraisal is measured block-wise on a 0-100 challenge/threat scale immediately after each block to reduce retrospective distortion.
Definition 3 (Selection Budget Inequality; Thermodynamic-Inspired). The rate of change of macroscopic order  — operationalizable as mutual information density, topological invariants, or compression ratio — is bounded by:

where  is the selection power (the net energy available for maintaining and extending the current ),  is the friction cost,  is the environmental noise entropy, and  are coupling constants.
This inequality is the master budget constraint of SRT. It states that an agent’s capacity to maintain or increase order in its manifest domain is bounded by available selection power minus friction and noise costs. In early-phase experiments,  is treated as a boundary variable rather than a mandatory primary endpoint; optional operationalizations include compression ratio, entropy-rate surrogates, or task-state stability metrics. When , the system enters order collapse (), manifesting as cognitive disorganization or executive failure.
Definition 4 (Parameter Dynamics). The embodiment parameters  evolve according to:

where ,  is the learning signal (error-driven adaptation),  is the gradient of the friction potential (driving parameters toward lower-friction configurations), and the third term captures homeostatic pressure to return to baseline. This equation governs the slow dynamics of habit formation, belief revision, and therapeutic change.
### 2.3 The Knowing–Doing Gap as Bandwidth Saturation
The knowing–doing gap emerges naturally from the selection-budget inequality (Equation 5). Consider an agent whose  model (crystallized knowledge) correctly specifies the appropriate action — the patient who knows she should exercise, the surgeon who knows the next step of the procedure. The knowledge is encoded in  and is intact.
Throughout this manuscript, selection power () is the primary term; “bandwidth” is used only as an informal synonym for residual selection capacity.
However, implementing this knowledge requires converting it into an  action state via the selection operator . This conversion consumes selection power  and incurs ontological friction . When the agent is already operating under high baseline friction — due to chronic stress, neurodegeneration, or pathological parameter configurations — the remaining selection power may be insufficient to execute the known action.
Formally, the agent enters the knowing–doing gap when:

where  is the friction cost of maintaining the current state, and  is the additional friction cost of initiating the target action. The agent’s  model is intact (she “knows”), but  lacks the residual bandwidth to execute (she “can’t do”).
This formulation makes a specific prediction: the knowing–doing gap should be nonlinearly related to baseline friction load. At low , adding task demands produces proportional increases in task-switching cost (linear regime). As  approaches , small additional demands produce steep performance collapse (saturation regime).
To parameterize this as a fit-ready critical phenomenon, define normalized control load:

and model switch cost with a changepoint:

where  is the estimated critical point. The model predicts a stable linear region for  and accelerated cost growth for , with  expected in a high-load band near resource saturation. Empirically,  can be estimated via segmented regression, threshold mixed models, or Bayesian changepoint inference.
### 2.4 Relationship to Predictive Processing and Free Energy Minimization
bears a formal relationship to the complexity term in variational free energy. In the FEP framework, the variational free energy  decomposes as:

The complexity term  penalizes posteriors that deviate from priors — formally analogous to the information-geometric friction form in Equation (3d). In this reading,  generalizes complexity cost by (a) accumulating over time, (b) applying to executed percept-action control rather than beliefs alone, and (c) linking to energetic budgets through Equation (5).
The critical distinction between SRT and standard FEP is in the normative implication. FEP implies that systems should minimize free energy and, by extension, minimize the complexity cost. SRT acknowledges that some states require sustained high  — creative insight that resists premature closure, ethical choices that resist default heuristics, grief that maintains connection to the departed. In these cases, high  is not pathological but constitutive of the valued state. Pathology arises not from high  per se, but from unsustainable  — when the cost chronically exceeds the agent’s selection power budget.
This distinction has immediate clinical relevance: the therapeutic goal is not to eliminate  (which would eliminate agency) but to restore the balance between  and , either by reducing unnecessary friction or by expanding selection power capacity.
### 2.5 Dimensionalization and Identifiability (Empirical Budget Form)
Equation (5) is used in this manuscript as an empirically identifiable statistical budget model, not as a closed-form physical law with fixed SI units. For phase-1/2 inference, we estimate all terms in standardized space:

where tildes denote z-scored quantities, and  are regression weights to be estimated from data (not universal physical constants). In this form,  is a dimensionless state-stability/order index, and all predictors are unitless standardized indicators. Minimal proxy anchoring follows Table 1:  from HRV/SCR recovery indicators,  from latent-factor estimation over behavioral-linguistic-physiological indicators, and  from task conflict/entropy manipulations.
For confirmatory phase-1 analyses, we operationalize  with a minimal observable index:

where  is windowed response-error entropy and  is windowed reaction-time coefficient of variation. Higher  indicates greater local task-state stability.
Interpretively,  captures a minimal “order/stability” surrogate: stable control states should show lower local error unpredictability and lower RT dispersion. To separate this from generic arousal/fatigue accounts, phase-1 models include baseline arousal and block-order covariates; if  variance is explained by arousal/fatigue alone while budget terms contribute no directional signal, the Eq. (5) interpretation is weakened. The confirmatory phase-1 test for Eq. (5) is directional and statistical: whether , , and  jointly predict  with expected signs, rather than whether Eq. (5) is a literal thermodynamic identity.
For changepoint testing, we retain the theoretical ratio in Equation (7a) and additionally define a phase-1 robust approximation:

which avoids instability of ratio estimators in low-denominator regions. Inference targets are therefore statistical critical points ( or ) rather than claims of a universal thermodynamic constant.
Figure 1. Selective Reality Theory architecture and selection power budget. (A) Three-domain structure: latent domain (, possibility space), manifest domain (, selected reality), and convergence domain (, stabilized constraints), linked by the selection operator . Dashed feedback arrow indicates ’s constraint on future selection. (B) Selection-budget diagram illustrating how the “knowing–doing gap” emerges when the red bar () plus orange bar () exceeds the green bar (), progressing from healthy function through stressed operation to clinical breakdown. Final artwork should keep these exact symbol labels for one-to-one correspondence with Equation (5).

Figure 1

## 3. Operationalization: Four Proxy Classes for
A theoretical construct is scientifically useful only to the extent that it can be measured. We now derive four classes of proxy measures for , each grounded in established measurement paradigms but unified under a common latent variable interpretation. The central claim of this section is that  is not reducible to any single proxy but manifests as a correlated pattern across behavioral, physiological, neural, and linguistic indicators.
### 3.0 Validation-First Prioritization
To maximize empirical tractability, this manuscript adopts a staged validation strategy. The core validation chain uses low-cost modalities that can be replicated broadly: behavioral control-cost tasks, the linguistic modal-ratio probe (), and low-cost physiology (HRV and SCR; cortisol optional). High-cost markers (ROS assays, PCI, Fisher-geometry readouts, and theta-gamma coupling) are treated as expansion layers for later-phase adjudication rather than prerequisites for first-pass falsification. Failure of expansion markers to add value does not invalidate the core-chain model.
For transparency, we explicitly map model terms to measurable proxies:
Table 1. Equation-to-proxy mapping for core and expansion layers.
### 3.1 Behavioral Proxies
Task-switching cost. When an agent must reconfigure its selection operator to serve a new task rule, the reconfiguration incurs ontological friction proportional to the distance between the current and target  configurations. The classical task-switching cost — the increase in reaction time and error rate on switch trials relative to repeat trials (Monsell, 2003; Kiesel et al., 2010) — directly indexes this reconfiguration friction. Computational accounts further decompose this cost into reconfiguration and interference-control components (Yeung and Monsell, 2003; Brown et al., 2007), supporting model-based estimation of behavioral friction. We predict that task-switching cost scales with  across individuals and within individuals across conditions.
Perseverative errors. In the Wisconsin Card Sorting Test (WCST; Berg, 1948) and related paradigms, perseverative errors reflect the agent’s failure to abandon a high-friction configuration — the previous sorting rule has become deeply anchored (high ) and the system cannot pay the switching cost. The number of perseverative errors indexes the viscosity  of the parameter space: .
Stroop interference. The Stroop effect (Stroop, 1935) measures the friction cost of suppressing a default selection (word reading) in favor of a non-default selection (color naming). The Stroop interference ratio (incongruent RT / congruent RT) provides a normalized behavioral index of the friction differential between default and non-default selections.
Temporal discounting. Steep temporal discounting — the preference for smaller-sooner over larger-later rewards — reflects the high friction cost of maintaining a non-default, future-oriented  state (Bickel et al., 2012). The temporal discounting rate  in the hyperbolic model () can be interpreted as a proxy for the friction cost of temporal extension of the selection horizon. This interpretation is consistent with effort-based decision frameworks that treat control allocation as a cost-benefit computation (Westbrook and Braver, 2015).
Composite score. We propose a composite behavioral  score computed as the average of standardized (Z-scored) values across: (a) mean task-switching cost, (b) WCST perseverative error proportion, (c) Stroop interference ratio, and (d) temporal discounting rate.
### 3.2 Physiological Proxies (Core and Expansion)
Heart rate variability (HRV) recovery. Vagal-mediated HRV reflects the capacity of the autonomic nervous system to regulate arousal — a physiological substrate of selection power . The neurovisceral integration model (Thayer and Lane, 2009) establishes that high resting HRV indexes flexible autonomic control, while reduced HRV indexes rigidity. We predict that HRV recovery slope — the rate at which HRV returns to baseline following a stressor — indexes the system’s capacity to dissipate . Slow recovery indicates sustained high friction; rapid recovery indicates efficient friction resolution.
Cortisol circadian rhythm. The diurnal cortisol curve (cortisol awakening response and diurnal slope) reflects the integrity of the hypothalamic-pituitary-adrenal axis. Chronic high  is predicted to flatten the cortisol curve — reducing the morning peak and elevating the evening nadir — reflecting exhaustion of the neuroendocrine substrate that supports selection power (Adam et al., 2017). We propose the cortisol awakening response (CAR) magnitude and the diurnal cortisol slope (DCS) as complementary physiological proxies.
Skin conductance response (SCR). Phasic SCR amplitude during decision-making tasks reflects momentary spikes in autonomic arousal associated with conflict and uncertainty — acute increases in . SCR peak amplitude during high-conflict choices (e.g., the Iowa Gambling Task; Bechara et al., 1994) provides a real-time physiological index of the hazard function (Equation 4).
Reactive oxygen species (ROS) as a biochemical signature (expansion layer). We propose a link between  and oxidative stress for later-phase testing. The sustained energetic expenditure required to maintain high-friction states should produce elevated mitochondrial activity and, consequently, elevated ROS production. We formalize this as:

where  is the friction-to-oxidative-load coupling coefficient and  represents antioxidant clearance capacity. Measurable ROS biomarkers include GSH/GSSG, malondialdehyde (MDA), 8-OHdG, and superoxide dismutase (SOD) activity. This is deliberately positioned as a phase-3 extension after core low-cost validation succeeds.
Falsification condition for ROS coupling. If experimentally induced high- tasks (e.g., sustained task-switching under time pressure) do not produce elevated ROS relative to low- control tasks, or if antioxidant supplementation (increasing ) does not modulate behavioral  proxies, the ROS-friction coupling model is rejected.
### 3.3 Neural Proxies
Neural proxies provide mechanistic depth but are not required for phase-1 falsification. They are treated as expansion modalities to test whether control-cost signatures generalize from low-cost measures to circuit-level dynamics.
Perturbational Complexity Index (PCI). PCI quantifies the complexity of the cortical response to transcranial magnetic stimulation perturbation, capturing the system’s capacity for differentiated, integrated processing (Casali et al., 2013). We interpret PCI as indexing the available selection capacity of : high PCI reflects high residual , while low PCI reflects depleted capacity. PCI should decrease under high  load and correlate negatively with behavioral  proxies.
Fisher information metric. The Fisher information matrix  captures the curvature of the neural state-space manifold — how sharply the system’s responses change as parameters vary. We propose that the empirical Fisher condition number , the Fisher volume term , and the maximum eigenvalue drift  serve as neural proxies for  during state transitions (Amari, 2016). Specifically, transitions between cognitive states (e.g., task switches) should produce Fisher metric peaks preceding behavioral performance degradation — a “structural reconfiguration signal” that indexes friction before it manifests behaviorally.
Theta-gamma coupling in prefrontal cortex. Theta-phase/gamma-amplitude coupling (TGC) in prefrontal regions implements a multiplexing mechanism that constrains working memory capacity to approximately 5–7 items (Lisman and Idiart, 1995; Lundqvist et al., 2011). We interpret TGC integrity as an index of selection capacity: degraded TGC under high  should predict working memory failures and executive breakdowns. Specifically, the phase-amplitude coupling modulation index (Tort et al., 2010) should decrease as behavioral  composite scores increase.
Thalamo–basal ganglia gating integrity. The thalamus–basal ganglia circuit functions as a selection gate () that determines which candidate action trajectories are projected to manifest execution. Gate integrity can be indexed through reinforcement-learning model parameters (learning rate, exploration–exploitation balance) derived from probabilistic reversal-learning tasks (Frank et al., 2004). Degraded gating — as in Parkinson’s disease — should produce specifically elevated  for action initiation while leaving cognitive  relatively preserved.
### 3.4 Linguistic Proxy: The Modal Mechanics Probe
We introduce a novel, non-invasive proxy for  based on the distribution of modal verbs in natural language production. We term this the modal mechanics probe (hypothesis H72 in the SRT framework).
Theoretical rationale. Modal verbs encode speakers’ orientation toward necessity, obligation, possibility, and desire (Palmer, 2001; van der Auwera and Plungian, 1998). We hypothesize that the balance between constraint-oriented modals (must, should, have to, cannot) and possibility-oriented modals (can, might, could, want to) reflects the speaker’s experienced level of ontological friction. High  — experienced as constraint, obligation, and restriction — should bias language production toward constraint modals. Low  — experienced as agency, possibility, and flow — should bias toward possibility modals.
This directionality is consistent with broader evidence that clinically relevant affective-control states leave measurable signatures in language production (Rude et al., 2004), including large-scale clinical NLP evidence that natural language markers can prospectively index depression risk (Eichstaedt et al., 2018), motivating modal usage as a targeted, mechanistically interpretable subchannel.
Neurobiological plausibility. We do not treat  as a purely stylistic marker. Under cognitive-control and embodied language accounts, lexical selection under conflict depends on frontally mediated control allocation and policy constraints (Miller and Cohen, 2001; Diamond, 2013). On this view, constraint-heavy modal output is interpretable as a semantic spillover of high control demand, i.e., a downstream linguistic footprint of constrained control budgets rather than a detached linguistic artifact.
Operational definition. The semantic modal ratio  is defined as:

where  are domain-specific weights (initially set to 1.0 for equal weighting) and Freq denotes frequency per 1000 words in a transcribed speech sample. Constraint modals include: must, have to, need to, should, ought to, cannot, must not. Possibility modals include: can, could, may, might, want to, would like to, choose to.
Reproducible scoring protocol and confound control. To make  scale-like rather than anecdotal, we use a residualized score:

This controls for major non-theoretical variance sources: education level, interview context, prompt wording, interviewer style, global affective-word prevalence, and lexical diversity. Recommended reliability checks are split-half agreement, inter-rater agreement for modal tagging (if manual annotation is used), and longitudinal ICC in repeated sessions. To reduce floor/ceiling instability, analyses should exclude samples with fewer than 10 total modal tokens.
Cross-language mapping protocol (Mandarin example). Cross-linguistic adaptation should preserve semantic role classes (constraint vs possibility), not literal word matching. For Mandarin Chinese, an initial inventory can be instantiated as:
Constraint-oriented modals (Mandarin pinyin): bixu, dei, yao, yinggai, buneng, bude
Possibility-oriented modals (Mandarin pinyin): keyi, neng, keneng, huoxu, xiang, yuanyi
Each language version should report (1) dictionary construction rules, (2) tokenization/segmentation pipeline, (3) ambiguity resolution rules (e.g., deontic vs epistemic usage), and (4) measurement-invariance checks before pooling cross-language samples. The minimum pre-registered sequence is configural then metric invariance (scalar optional); if metric invariance fails, confirmatory analyses remain language-specific and pooled estimates are treated as exploratory only.
Methodological advantages.  is non-invasive, low-cost, and scalable to large corpora, including interview archives and longitudinal recordings. It is therefore suitable as a phase-1 marker in the core validation chain.
### 3.5 Convergent Validity Architecture
The central operationalization claim is that the four proxy classes converge on a single latent variable —  — rather than measuring four independent constructs. This claim is testable through structural equation modeling (SEM).
Proposed model. A single-factor confirmatory factor analysis with four indicator classes:
Behavioral composite   (expected loading: )
Physiological composite (HRV recovery slope, inverse-coded)   ()
Neural composite (PCI, inverse-coded; Fisher condition number)   ()
Linguistic index ()   ()
For staged validation, we use a nested modeling strategy. Core model (phase 1/2): behavioral + linguistic + low-cost physiology. Expansion model (phase 3): add neural and ROS blocks and test whether they improve fit and prediction beyond the core model.
Expected correlation structure. Within-domain correlations should be moderate to strong (–); between-domain correlations should be moderate (–). If between-domain correlations fall below  uniformly, the unitary latent variable interpretation is rejected in favor of independent constructs.
Minimum survivable model if single-factor fails. The fallback is pre-registered rather than post hoc: (a) a two-factor model separating control-performance (behavioral + physiology) from semantic-constraint (linguistic, plus optional neural/expansion indicators), and (b) a bifactor model with one general factor plus modality-specific factors. The framework is retained only if the general factor shows stable loadings and predicts critical-load outcomes beyond modality factors; otherwise, the theory is downgraded to a family of modality-indexed frictions () rather than one unitary latent variable.
Discriminant validity.  should be empirically distinguishable from general cognitive ability (IQ), general psychopathology (-factor), and trait neuroticism. We predict that  shows incremental validity over these constructs in predicting task-switching cost and clinical executive dysfunction.
Figure 2. Cross-modal operationalization map for ontological friction (). Central latent construct with four proxy classes. Core validation chain: behavioral, linguistic, and low-cost physiology (HRV/SCR/cortisol). Expansion chain: ROS biomarkers and neural proxies (PCI, Fisher information, theta-gamma coupling, basal ganglia gating). Arrows indicate predicted direction of association; “(inv)” denotes inverse coding.

Figure 2

## 4. Clinical Mapping:  Across Disorders
The  framework generates disorder-specific predictions that go beyond the generic claim that “executive function is impaired.” Each clinical condition is modeled as a distinct perturbation of the  dynamics, producing a characteristic friction signature across the four proxy classes.
### 4.1 Major Depressive Disorder: Sustained Friction with Oxidative Coupling
In the  framework, major depressive disorder (MDD) is modeled as a state of chronic friction elevation in which  remains positive over extended periods, leading to progressive exhaustion of selection power and oxidative stress accumulation.
Mechanism. The depressed agent’s  model may be accurate or even hyperaccurate (“depressive realism”; Alloy and Abramson, 1979) — the agent correctly identifies what actions would be beneficial. However, the friction cost of initiating state transitions () chronically exceeds the available residual selection power (). The agent enters a stable low-energy attractor in which inaction minimizes acute distress () at the cost of chronic friction accumulation.
The ROS coupling equation (Equation 9) generates a specific pathophysiological chain: sustained  elevated metabolic demand  increased mitochondrial ROS production  oxidative damage  inflammatory signaling  further reduction of  through immune-mediated neuromodulatory changes. This positive feedback loop is consistent with the inflammatory hypothesis of depression (Maes et al., 2011; Miller and Raison, 2016) and provides a mechanistic link between the cognitive and immunological dimensions of MDD. In this manuscript, this chain is treated as a phase-3 mechanistic adjudication target; cross-sectional data can establish compatibility but not causal direction.
Predicted friction signature. Core chain prediction for depression is: (a) elevated behavioral  composite, particularly temporal discounting and task-switching cost; (b) reduced HRV recovery slope and altered SCR/cortisol profile; and (c) elevated  with predominance of obligation/constraint modals. Expansion prediction is reduced PCI/degraded theta-gamma coupling plus elevated ROS biomarkers (reduced GSH/GSSG ratio, elevated MDA).
Figure 3. ROS– coupling mechanism: from ontological friction to clinical expression. Directed acyclic graph showing the pathophysiological chain from sustained high  through elevated metabolic demand, increased ROS production, oxidative damage, inflammatory signaling, reduced selection power (), and deepened knowing–doing gap, forming a positive feedback loop (dashed red arrow). Dashed boxes at bottom indicate three intervention targets: pharmacological (), behavioral (), and antioxidant ( clearance).

Figure 3
### 4.2 Obsessive-Compulsive Disorder: Switching Viscosity
OCD is modeled as a pathological elevation of switching viscosity  — the resistance of the parameter space to state transitions. The compulsive behavior occupies a local minimum in the friction landscape with extremely steep walls, making it energetically prohibitive to transition to alternative states.
Mechanism. We model OCD switching viscosity using a network-modulated gradient flow:

where  is the friction potential,  is the network degree (or weighted centrality) of node , and  is noise. High-centrality nodes update more slowly because effective step size is reduced by . Local trapping strength is quantified by curvature:

so compulsive states correspond to deep, high-curvature local wells that raise transition cost.
Predicted friction signature. OCD is characterized by: (a) dramatically elevated task-switching cost specifically for uncertainty- and contamination-related stimuli; (b) elevated SCR during obsession-related cues (acute  spikes); and (c) the highest  values, dominated by “must/have to” constructions. Expansion prediction is relatively preserved PCI (system not globally bandwidth-depleted but dynamically stuck). The discriminator from depression is elevated switching friction with comparatively preserved maintenance capacity.
### 4.3 Parkinson’s Disease: Selection Gate Degradation
Parkinson’s disease (PD) is modeled as a degradation of the selection gate operator  — the thalamo-basal ganglia circuit that converts motor plans ( representations) into initiated actions ( states).
Mechanism. The dopaminergic signal-to-noise ratio in the striatum serves as a gain parameter for the gate. As dopaminergic neurons in the substantia nigra degenerate, the gate’s capacity to distinguish candidate actions diminishes, and initiation friction rises (Frank et al., 2004; Redgrave et al., 2010). We use a dimensionless embodied anchoring index:

where  and  are participant-specific normalization constants (e.g., baseline grip force and baseline initiation friction estimate). As dopaminergic availability decreases, : the agent can generate a motor plan but fails to anchor execution in embodied output.
Predicted friction signature. PD is characterized by: (a) elevated task-switching cost for motor tasks with relatively preserved cognitive switching (early stages); (b) elevated SCR during motor initiation attempts with less pronounced endocrine flattening; and (c)  elevation concentrated in motor-action expressions. Expansion prediction is region-specific PCI reduction in motor cortex with relative prefrontal preservation.
For empirical PD cohorts, a minimal adjustment set should include dopaminergic medication state (ON/OFF and levodopa-equivalent daily dose), disease duration, motor severity (e.g., UPDRS), sleep status, and major psychiatric comorbidity.
### 4.4 Differential Prediction Table
The clinical utility of  depends on its capacity to generate disorder-specific predictions, not merely generic “executive dysfunction” claims. Table 2 summarizes the predicted friction signatures across conditions.
Table 2. Predicted  proxy signatures across clinical conditions.
Core-chain inference in this manuscript is based primarily on behavioral + linguistic + low-cost physiological rows. ROS and neural rows are treated as expansion targets for later-phase adjudication.
To sharpen falsifiability, we propose quantitative priors for two discriminator patterns. Pattern A (OCD dissociation): OCD should show higher  than controls (–) and than MDD (–), while PCI remains near control range (). Pattern B (PD motor selectivity): PD should show large motor-switch impairment () with smaller cognitive-switch impairment () in early-stage cohorts. In contrast, single-resource formulations (including standard single-task EVC fits or undifferentiated global-deficit accounts) typically predict more monotonic cross-domain impairment and weaker dissociation in these paired contrasts.
These predictions are falsifiable: if, for example, OCD patients do not show the highest  values, or if PD patients show generalized rather than motor-specific switching cost elevation, the disorder-specific  models require revision.
Figure 4. Predicted  proxy signatures across clinical conditions. Radar chart showing disorder-specific friction profiles for healthy controls (green), major depressive disorder (red), obsessive-compulsive disorder (purple), and Parkinson’s disease (orange) across ten proxy measures. Higher values indicate greater impairment or higher ontological friction. These predictions constitute falsifiable claims derived from the  framework.

Figure 4
### 4.5 Competing Explanations and Decisive Phase-2 Tests
To reduce over-interpretation risk, each disorder signature is paired with a concrete competing explanation and a decisive phase-2 contrast:
MDD: versus generic symptom-severity accounts. Decisive test: whether high  profile predicts a specific combination (high temporal discounting + slow HRV recovery + elevated ) rather than uniform global impairment alone.
OCD: versus generalized anxiety/rumination accounts. Decisive test: domain-specific switching viscosity plus highest  under preserved global PCI-range indices in expansion cohorts.
PD: versus global psychomotor slowing. Decisive test: motor-selective switch impairment with comparatively preserved cognitive switching in early-stage cohorts, plus initiation-specific autonomic spikes.
If these contrasts fail, the clinical mapping should be downgraded to transdiagnostic severity effects rather than disorder-specific signatures.

## 5. Falsifiable Hypotheses and Proposed Experimental Protocols
We now present five pre-registration-ready hypotheses derived from the  framework. Each hypothesis specifies the prediction, the falsification criterion, the required sample size, and the core measurement protocol. We emphasize that these hypotheses are designed to be individually falsifiable — rejection of any single hypothesis does not invalidate the entire framework but constrains its scope.
### 5.1 Hypothesis H72: Modal Verb Patterns Reflect Ontological Friction
Prediction. Within-subject adjusted modal ratio  (Equation 10a) is higher in self-decision narratives than in neutral factual retell prompts, and the context contrast  correlates positively with behavioral  composite (task-switch cost + Stroop interference + perseverative errors) with , and negatively with HRV recovery slope with . We further predict incremental validity after adding symptom controls (PHQ-9, GAD-7, or equivalent), affective-word ratio, and block-wise appraisal ratings.
Protocol.  healthy adults, tested in three sessions over six weeks. Each session includes: (1) two fixed prompt blocks (neutral factual retell and self-decision narrative; total 15 minutes), recorded and transcribed; (2) behavioral battery (task switching, Stroop, WCST); and (3) HRV + SCR recording (cortisol optional for the core chain). Prompt administration is standardized: factual block uses a fixed non-evaluative script (e.g., “describe yesterday’s routine chronologically”), decision block uses a fixed self-choice script (e.g., “describe an unresolved decision and candidate actions”), each with fixed speaking duration and counterbalanced order across sessions. After each block, participants provide a 0-100 challenge/threat appraisal score used in Equation (4)-linked analyses.  is extracted with a pre-registered modal dictionary and residualized using Equation (10a). Interviewer identity is modeled as a random effect (random intercept plus context slope when estimable). Samples with fewer than 10 modal tokens are excluded a priori.
Statistical analysis. Multilevel models with random intercepts and slopes are used for within-subject association tests. Primary fixed effects are context (decision vs factual), , block-wise appraisal, and their links to behavioral/HRV outcomes. Incremental validity is tested via  after adding PHQ-9 and GAD-7 (Kroenke et al., 2001; Spitzer et al., 2006) or equivalent symptom scales, plus affective-word ratio. If multilingual cohorts are used, configural/metric invariance is tested before pooled confirmatory inference. Test-retest reliability is assessed via ICC for both raw  and adjusted .
Falsification criterion. If (a) no decision-vs-factual context effect is observed for , and (b) adjusted  provides no incremental variance beyond symptom and affect controls (), H72 is rejected and the linguistic proxy class is removed from the core model.
Power analysis. With , three time points, and an expected ICC of 0.50, the design has 90% power to detect a within-subject correlation of  at .
### 5.2 Hypothesis H-NEURO-EXEC-01: Nonlinear Executive Cost Under High
Prediction. Task-switching cost increases nonlinearly as a function of concurrent normalized load. The confirmatory estimator is  (Equation 7c), with ratio-based  (Equation 7a) as sensitivity analysis. Specifically, a changepoint model (Equation 7b) should outperform a linear model by  and yield an identifiable critical point  (and concordant  in sensitivity checks).
Protocol.  healthy adults in a within-subject design.  load is manipulated at four levels: (1) single-task switching, (2) low concurrent load, (3) high concurrent load, and (4) social-evaluative stress. Task-switching cost is measured at each level; HRV and SCR are recorded to estimate concurrent load. For phase-1 estimation, baseline friction is operationalized as a latent composite from , resting HRV (inverse-coded), and baseline switch cost;  is proxied by normalized HRV/SCR recovery. Primary confirmatory analyses use  (Eq. 7c); ratio-based  (Eq. 7a) is pre-specified sensitivity analysis.
Falsification criterion. If a linear model provides equal or better fit in the primary  analysis (), or if no positive  is identifiable, the bandwidth-saturation account is rejected in favor of additive resource models. Ratio-based  results are reported as sensitivity checks.
### 5.3 Hypothesis H-MET-01: Free Choice Metabolic Premium
Prediction. Decisions that require overriding default or habitual responses — operationalized as choosing the counter-habitual option in a trained stimulus-response compatibility task — produce higher autonomic control cost (primary endpoint: SCR amplitude) than decisions aligned with trained responses, and this cost differential is predicted by the individual’s behavioral  composite score. Blood glucose change is treated as a secondary exploratory endpoint because the glucose-specific ego-depletion mechanism remains contested (Baumeister et al., 1998; Hagger et al., 2016; Vadillo et al., 2016).
Protocol.  healthy adults. Phase 1 (training): participants learn a stimulus-response mapping over 200 trials. Phase 2 (test): on 50% of trials, participants are instructed to execute the opposite of their trained response. SCR is recorded continuously as the primary physiological endpoint; capillary blood glucose (pre/post Phase 2) is collected as a secondary exploratory endpoint. Behavioral  composite is measured in a separate session.
Falsification criterion. If SCR amplitude does not differ between habitual and counter-habitual responses, or if the SCR difference is not predicted by the  composite (), the primary metabolic-premium hypothesis is rejected. A null glucose effect alone does not falsify H-MET-01 but constrains substrate-level interpretations.
### 5.4 Hypothesis H-CLIN-DEP-01: ROS– Coupling in Depression
Prediction. In a sample of MDD patients () and matched healthy controls (), the behavioral  composite score predicts ROS biomarker levels (GSH/GSSG ratio) with  in the MDD group. HRV mediation is tested as a compatibility model in cross-sectional data and is not interpreted as causal directionality.
Protocol. Cross-sectional comparison. Each participant completes the full behavioral task battery (§3.1), provides salivary cortisol and blood samples for ROS assays, and undergoes HRV recording. MDD diagnosis is confirmed via structured clinical interview (SCID-5). Predefined exclusion/covariate set includes acute inflammatory disease, systemic steroid or high-dose antioxidant use, unstable medical illness, substance dependence, antidepressant class/dose (e.g., SSRI/SNRI), illness duration, episode severity, anxiety comorbidity, and sleep-quality index.
Falsification criterion. If the  composite–GSH/GSSG correlation is  in the MDD group, or if the mediation by HRV is non-significant, the ROS-friction coupling model is rejected for depression.
### 5.5 Hypothesis H-CLIN-OCD-01: Maximal  in OCD
Prediction. In a three-group comparison (OCD, ; MDD, ; healthy controls, ), the OCD group shows significantly higher  than both MDD and control groups (, medium effect size), driven specifically by elevated frequency of constraint modals.
Protocol. Each participant completes a 20-minute semi-structured clinical interview (using the Yale-Brown Obsessive Compulsive Scale for OCD group, Hamilton Depression Rating Scale for MDD group) plus a standardized free-narrative prompt (“Describe your daily routine and the challenges you face”). Transcripts are analyzed for . Minimal adjustment set includes SSRI/antipsychotic augmentation status, benzodiazepine use, illness duration, anxiety and sleep comorbidity indices, and interviewer random effects.
Falsification criterion. If OCD  does not significantly exceed healthy control  (, one-tailed), the disorder-specific linguistic signature model is rejected.
### 5.6 Proposed Validation Roadmap
We propose a three-phase validation program:
Phase 1 (core low-cost mechanism test). Execute H72 and H-NEURO-EXEC-01 using behavioral tasks, , HRV, and SCR. Objective: identify whether a stable latent  factor and a measurable critical point  exists in healthy cohorts (with ratio-based  as sensitivity check). . Estimated timeline: 12 months.
Phase 2 (core clinical generalization). Execute H-CLIN-OCD-01 and H-MET-01 with the same low-cost core chain, extending to clinical and quasi-clinical groups while preserving protocol simplicity. . Estimated timeline: 18 months.
Phase 3 (high-cost optional adjudication). Execute H-CLIN-DEP-01 with ROS assays and neural expansion markers (e.g., PCI, theta-gamma coupling, Fisher-geometry metrics) to test whether costly modalities add explanatory value beyond the core chain. These modalities are explicitly optional adjudicators, not prerequisites for validating the core model. . Estimated timeline: 24 months.
At pre-registration release, the public repository will include: modal dictionaries by language, preprocessing/tokenization scripts, model-specification files (core and fallback), and simulation scripts used to justify decision thresholds.
Table 3. Falsification criteria summary.
Primary-endpoint decision rules: directional primary tests are one-sided (); secondary tests use Benjamini-Hochberg FDR control (). Predefined primary endpoints are: H72 (context effect and ), H-NEURO-EXEC-01 ( identification), H-MET-01 (SCR contrast), H-CLIN-OCD-01 (group contrast on ), and H-CLIN-DEP-01 (-ROS association). Ratio-based  inference is explicitly sensitivity-only.
The one-sided choice is justified by preregistered directional monotonic predictions implied by Equations (4), (5), and (7); all primary effects are also reported with two-sided sensitivity analyses. Thresholds (e.g., , , pruning rule at ) are design anchors linked to planned simulation-based power checks under expected reliability ranges, rather than universal constants.
Figure 5. Core-chain protocol and critical-load prediction. (A) Low-cost protocol for H72 and H-NEURO-EXEC-01, integrating two prompt contexts (neutral factual retell vs self-decision narrative), behavioral battery, HRV/SCR recording, appraisal ratings, and NLP extraction for latent-factor estimation. Baseline load is estimated as  (Eq. 7c) in primary analyses; ratio-based  is sensitivity-only. (B) Predicted task-switch cost as a function of normalized load : the saturation model (solid red) includes a critical point  and nonlinear escalation into a “know but can’t do” zone, while the additive model (dashed gray) predicts linear increase.

Figure 5

## 6. Discussion
### 6.1 Theoretical Implications
The  framework addresses a persistent gap in cognitive neuroscience: the absence of a cross-modal cost quantity that unifies behavioral, physiological, neural, and linguistic signatures of executive breakdown under a formal selection-budget constraint. By deriving the knowing–doing gap as bandwidth saturation (Equation 7) rather than as a domain-specific failure, the framework generates testable predictions that current models — cognitive load theory, FEP, IIT, allostatic load — do not individually produce.
The key theoretical advance is the decoupling of knowledge from capacity. In existing frameworks, executive failure is typically attributed to degraded representations (the agent doesn’t know), degraded attention (the agent can’t focus), or degraded motivation (the agent doesn’t want to). The  framework introduces a fourth possibility: the agent knows, can focus, and wants to act, but the cost of converting knowledge into action exceeds available resources. This bandwidth saturation account explains why patients often report the phenomenology of “knowing exactly what to do but being unable to do it” — a subjective experience that is puzzling under representational, attentional, or motivational accounts.
### 6.2 Comparison with Existing Frameworks
Table 4 compares  with five existing frameworks across seven evaluation criteria.
Table 4. Framework comparison.
This comparison is not intended to argue that  replaces existing frameworks. Rather,  can be understood as a generalization that subsumes aspects of each: it includes cognitive load as a behavioral special case, allostatic load as a physiological special case, and variational complexity as an information-theoretic special case, while adding explicit cross-modal latent modeling and dissociation predictions.
Relative to the Expected Value of Control (EVC) framework (Shenhav et al., 2013; Shenhav et al., 2017),  is closest to a transmodal control-cost extension: both treat control as a cost-constrained process, but  explicitly predicts disorder-specific cross-domain dissociations (e.g., high  with near-normal PCI in OCD) that are not native outputs of single-task EVC fits. This positioning is consistent with computational psychiatry goals of mechanistic yet clinically testable bridges (Huys et al., 2016).
### 6.3 Limitations and Boundary Conditions
Several important limitations must be acknowledged.
First,  is a latent construct inferred from multiple indicators. No single measure is sufficient, and the convergent validity of the four proxy classes is an empirical claim that remains to be tested. If the structural equation model (§3.5) fails to support a single-factor solution, the framework requires fundamental revision.
Second, the modal verb probe () may be language-specific. The inventory of modal verbs and their semantic valence varies across languages (Palmer, 2001), and the constraint/possibility distinction may not partition cleanly in all linguistic systems. Cross-linguistic validation with Mandarin Chinese, German, and Arabic modal systems is a necessary follow-up.
Third, distress and pain are not assumed to be generated solely by control cost. Equation (4) is a conditional hazard model; nociceptive injury, social threat, affective dysregulation, and appraisal shifts can all elevate distress even when  is modest. This is why we model a hazard family with smoothing and appraisal terms rather than a one-to-one derivative identity.
Fourth, the ROS coupling hypothesis (Equation 9) requires longitudinal data to establish temporal precedence. A cross-sectional correlation between  and ROS markers, while consistent with the model, does not establish directionality. Prospective designs and intervention studies (manipulating  and measuring ROS change) are essential.
Fifth, the equations presented (Equations 3a-6) use simplified functional forms. In particular, the control-cost quadratic form in Equation (3c), the KL form in Equation (3d), and its local Fisher approximation in Equation (3d’) are modeling choices, not identifiability guarantees. The precise friction-cost shape (quadratic, piecewise, exponential, or sigmoidal) remains an empirical question.
Sixth, the framework is silent on the hard problem of consciousness in the Chalmersian sense (Chalmers, 1995).  provides a measurable correlate of the cost of maintaining conscious states, but it does not explain why subjective experience accompanies high-friction processing. We view this as an appropriate scope limitation rather than a deficiency.
Seventh, this paper reports no empirical data. While we have specified protocols with sufficient detail for pre-registration and replication, the entire framework remains at the stage of theoretical proposal until the validation program (§5.6) is executed.
### 6.4 Alternative Models and Decisive Tests
The framework is designed to be partially rejectable rather than all-or-none. Key adjudication rules are:
If linear models consistently outperform changepoint models, reject the saturation component (Eq. 7b) while retaining additive control-cost formulations.
If cross-modal convergence fails (between-domain correlations uniformly ), reject the single latent-factor claim and move to domain-specific modules.
If  lacks context sensitivity or incremental validity, remove the linguistic probe from the core chain and retain behavioral-physiological modeling.
If optional expansion markers (ROS/PCI/Fisher) do not add predictive value, retain the core chain and demote expansion markers to exploratory status.
These outcomes define explicit model-pruning pathways and prevent post hoc theory protection.
Table 5. Alternative-model adjudication matrix (pre-registered decision rules).
### 6.5 Translational Potential
If empirically validated, the  framework offers several translational applications.
Transdiagnostic biomarker. The friction signature profiles (Table 2) could enable a biologically grounded, transdiagnostic classification of executive dysfunction that cuts across traditional categorical diagnoses.
Passive linguistic monitoring.  can be extracted from clinical interview transcripts, therapy session recordings, or — with appropriate consent and ethical oversight — naturalistic text data. This enables longitudinal  tracking without additional testing burden.
Treatment response prediction. Therapeutic interventions can be modeled as either reducing  (pharmacological approaches targeting the friction cost) or increasing  (behavioral approaches expanding selection power capacity). The  trajectory over treatment could serve as an early indicator of therapeutic response, potentially outperforming symptom-based monitoring.
Intervention design. The distinction between  reduction and  expansion suggests that combination therapies — pairing pharmacological  reduction with behavioral  training — should show synergistic effects quantifiable as:

where a positive synergy metric indicates genuine cross-domain recovery rather than compensation.

### 6.6 Conclusion
We have introduced ontological friction () as a formally defined, cross-modally operationalizable construct that transforms an abstract philosophical quantity — the cost of maintaining a selected reality against latent defaults — into a testable framework for cognitive and clinical dynamics. The construct is grounded in four core equations that specify friction accumulation, the hazard function for subjective distress, the selection-budget inequality, and the dynamics of parameter evolution. We have operationalized  through four convergent proxy classes — behavioral, physiological, neural, and linguistic — and demonstrated how the knowing–doing gap emerges as bandwidth saturation when friction cost exceeds available selection power.
The clinical mapping onto major depressive disorder, obsessive-compulsive disorder, and Parkinson’s disease generates disorder-specific, falsifiable predictions (Table 2) that distinguish the  account from generic executive dysfunction descriptions. Five pre-registration-ready hypotheses with explicit falsification criteria and a three-phase validation roadmap provide the experimental architecture for systematic testing.
The knowing–doing gap is not merely a clinical curiosity but a window into the fundamental cost structure of agency. Every act of will — from suppressing a craving to overriding a prejudice to initiating a motor sequence — incurs ontological friction. Understanding this cost, measuring it, and learning to modulate it may prove to be among the most consequential challenges at the intersection of cognitive neuroscience, clinical science, and the philosophy of mind.

## Appendix A. SRT-to-Standard Terminology Mapping
The core model can be read entirely in standard control/predictive-processing language:
(SRT latent domain) -> candidate state/policy space.
(SRT manifest domain) -> currently executed active state.
(SRT convergence domain) -> prior/hyperprior-like slow constraints.
-> resource-bounded selection operator/policy realization map.
-> control cost (latent, cross-modally estimated).
-> available control budget (residual selection capacity).
-> exogenous/environmental uncertainty load.
This appendix is intended to keep the main text maximally accessible to readers who prefer established computational-neuroscience terminology.

## Conflict of Interest Statement
The author declares that the research was conducted in the absence of any commercial or financial relationships that could be construed as a potential conflict of interest.
## Author Contributions
The author conceived the theoretical framework, developed the formal model, designed the proposed experimental program, prepared the figures and tables, and wrote the manuscript.
## Funding
This work received no external funding.
## Acknowledgments
The author thanks colleagues in the SRT research workflow for critical discussion and manuscript feedback. The author used multiple generative AI systems (including Anthropic Claude and OpenAI GPT-5 via Codex) for language refinement and structural editing. All AI-assisted content was critically reviewed, revised, and verified by the author, who retains full responsibility for the manuscript.
## Generative AI Statement
The author declares that generative AI was used only for drafting and language-structure optimization during manuscript preparation (including Anthropic Claude and OpenAI GPT-5 via Codex). Generative AI was not used for data generation, statistical analysis, or unverified citation insertion. Final factual accuracy, citation integrity, and scientific claims were checked by the author.
## Data Availability Statement
No empirical datasets were generated or analyzed for this theoretical manuscript. All equations, hypotheses, and analysis plans are fully reported in the main text. Upon empirical execution, the author will release the  dictionary specification, analysis code, and pre-registered scripts to support reproducibility.
## Ethics Statement
No human or animal participants were involved in this theoretical work; ethics approval and informed consent were therefore not required.
## Abbreviations
SRT, Selective Reality Theory; FEP, Free Energy Principle; IIT, Integrated Information Theory; MDD, major depressive disorder; OCD, obsessive-compulsive disorder; PD, Parkinson’s disease; HRV, heart rate variability; SCR, skin conductance response; ROS, reactive oxygen species; PCI, perturbational complexity index; WCST, Wisconsin Card Sorting Test; SEM, structural equation modeling; CFA, confirmatory factor analysis.

## References
Adam, E. K., Quinn, M. E., Tavernier, R., McQuillan, M. T., Dahlke, K. A., and Gilbert, K. E. (2017). Diurnal cortisol slopes and mental and physical health outcomes: A systematic review and meta-analysis. Psychoneuroendocrinology, 83, 25–41.
Alloy, L. B., and Abramson, L. Y. (1979). Judgment of contingency in depressed and nondepressed students: Sadder but wiser? Journal of Experimental Psychology: General, 108(4), 441–485.
Amari, S. (2016). Information Geometry and Its Applications. Springer.
Baumeister, R. F., Bratslavsky, E., Muraven, M., and Tice, D. M. (1998). Ego depletion: Is the active self a limited resource? Journal of Personality and Social Psychology, 74(5), 1252–1265.
Bechara, A., Damasio, A. R., Damasio, H., and Anderson, S. W. (1994). Insensitivity to future consequences following damage to human prefrontal cortex. Cognition, 50(1-3), 7–15.
Berg, E. A. (1948). A simple objective technique for measuring flexibility in thinking. Journal of General Psychology, 39(1), 15–22.
Bickel, W. K., Jarmolowicz, D. P., Mueller, E. T., Koffarnus, M. N., and Gatchalian, K. M. (2012). Excessive discounting of delayed reinforcers as a trans-disease process contributing to addiction and other disease-related vulnerabilities: Emerging evidence. Pharmacology & Therapeutics, 134(3), 287–297.
Brown, J. W., Reynolds, J. R., and Braver, T. S. (2007). A computational model of fractionated conflict-control mechanisms in task-switching. Cognitive Psychology, 55(1), 37–85.
Casali, A. G., Gosseries, O., Rosanova, M., Boly, M., Sarasso, S., Casarotto, S., et al. (2013). A theoretically based index of consciousness independent of sensory processing and behavior. Science Translational Medicine, 5(198), 198ra105.
Chalmers, D. J. (1995). Facing up to the problem of consciousness. Journal of Consciousness Studies, 2(3), 200–219.
Diamond, A. (2013). Executive functions. Annual Review of Psychology, 64, 135–168.
Eichstaedt, J. C., Smith, R. J., Merchant, R. M., Ungar, L. H., Crutchley, P., Preotiuc-Pietro, D., et al. (2018). Facebook language predicts depression in medical records. Proceedings of the National Academy of Sciences, 115(44), 11203–11208.
Frank, M. J., Seeberger, L. C., and O’Reilly, R. C. (2004). By carrot or by stick: Cognitive reinforcement learning in parkinsonism. Science, 306(5703), 1940–1943.
Friston, K. (2010). The free-energy principle: A unified brain theory? Nature Reviews Neuroscience, 11(2), 127–138.
Gaab, J., Rohleder, N., Nater, U. M., and Ehlert, U. (2005). Psychological determinants of the cortisol stress response: The role of anticipatory cognitive appraisal. Psychoneuroendocrinology, 30(6), 599–610.
Hagger, M. S., Chatzisarantis, N. L. D., Alberts, H., Anggono, C. O., Batailler, C., Birt, A. R., et al. (2016). A multilab preregistered replication of the ego-depletion effect. Perspectives on Psychological Science, 11(4), 546–573.
Huys, Q. J. M., Maia, T. V., and Frank, M. J. (2016). Computational psychiatry as a bridge from neuroscience to clinical applications. Nature Neuroscience, 19(3), 404–413.
Kiesel, A., Steinhauser, M., Wendt, M., Falkenstein, M., Jost, K., Philipp, A. M., et al. (2010). Control and interference in task switching — A review. Psychological Bulletin, 136(5), 849–874.
Kroenke, K., Spitzer, R. L., and Williams, J. B. W. (2001). The PHQ-9: Validity of a brief depression severity measure. Journal of General Internal Medicine, 16(9), 606–613.
Lisman, J. E., and Idiart, M. A. P. (1995). Storage of 7 ± 2 short-term memories in oscillatory subcycles. Science, 267(5203), 1512–1515.
Lundqvist, M., Herman, P., and Lansner, A. (2011). Theta and gamma power increases and alpha/beta power decreases with memory load in an attractor network model. Journal of Cognitive Neuroscience, 23(10), 3008–3020.
Maes, M., Galecki, P., Chang, Y. S., and Berk, M. (2011). A review on the oxidative and nitrosative stress (O&NS) pathways in major depression and their possible contribution to the (neuro)degenerative processes in that illness. Progress in Neuro-Psychopharmacology and Biological Psychiatry, 35(3), 676–692.
McEwen, B. S. (1998). Stress, adaptation, and disease: Allostasis and allostatic load. Annals of the New York Academy of Sciences, 840(1), 33–44.
McEwen, B. S., and Stellar, E. (1993). Stress and the individual: Mechanisms leading to disease. Archives of Internal Medicine, 153(18), 2093–2101.
Miller, A. H., and Raison, C. L. (2016). The role of inflammation in depression: From evolutionary imperative to modern treatment target. Nature Reviews Immunology, 16(1), 22–34.
Miller, E. K., and Cohen, J. D. (2001). An integrative theory of prefrontal cortex function. Annual Review of Neuroscience, 24(1), 167–202.
Miyake, A., Friedman, N. P., Emerson, M. J., Witzki, A. H., Howerter, A., and Wager, T. D. (2000). The unity and diversity of executive functions and their contributions to complex “frontal lobe” tasks: A latent variable analysis. Cognitive Psychology, 41(1), 49–100.
Monsell, S. (2003). Task switching. Trends in Cognitive Sciences, 7(3), 134–140.
Palmer, F. R. (2001). Mood and Modality (2nd ed.). Cambridge University Press.
Rao, R. P. N., and Ballard, D. H. (1999). Predictive coding in the visual cortex: A functional interpretation of some extra-classical receptive-field effects. Nature Neuroscience, 2(1), 79–87.
Rude, S., Gortner, E.-M., and Pennebaker, J. (2004). Language use of depressed and depression-vulnerable college students. Cognition and Emotion, 18(8), 1121–1133.
Redgrave, P., Rodriguez, M., Smith, Y., Rodriguez-Oroz, M. C., Lehericy, S., Bergman, H., et al. (2010). Goal-directed and habitual control in the basal ganglia: Implications for Parkinson’s disease. Nature Reviews Neuroscience, 11(11), 760–772.
Shenhav, A., Botvinick, M. M., and Cohen, J. D. (2013). The expected value of control: An integrative theory of anterior cingulate cortex function. Neuron, 79(2), 217–240.
Shenhav, A., Musslick, S., Lieder, F., Kool, W., Griffiths, T. L., Cohen, J. D., and Botvinick, M. M. (2017). Toward a rational and mechanistic account of mental effort. Annual Review of Neuroscience, 40, 99–124.
Spitzer, R. L., Kroenke, K., Williams, J. B. W., and Loewe, B. (2006). A brief measure for assessing generalized anxiety disorder: The GAD-7. Archives of Internal Medicine, 166(10), 1092–1097.
Stroop, J. R. (1935). Studies of interference in serial verbal reactions. Journal of Experimental Psychology, 18(6), 643–662.
Stuss, D. T., and Alexander, M. P. (2007). Is there a dysexecutive syndrome? Philosophical Transactions of the Royal Society B, 362(1481), 901–915.
Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. Cognitive Science, 12(2), 257–285.
Sweller, J., van Merriënboer, J. J. G., and Paas, F. (2019). Cognitive architecture and instructional design: 20 years later. Educational Psychology Review, 31(2), 261–292.
Thayer, J. F., and Lane, R. D. (2009). Claude Bernard and the heart–brain connection: Further elaboration of a model of neurovisceral integration. Neuroscience & Biobehavioral Reviews, 33(2), 81–88.
Tononi, G. (2004). An information integration theory of consciousness. BMC Neuroscience, 5, 42.
Tononi, G., Boly, M., Massimini, M., and Koch, C. (2016). Integrated information theory: An updated account. Archives Italiennes de Biologie, 154(2-3), 56–67.
Tort, A. B. L., Komorowski, R., Eichenbaum, H., and Kopell, N. (2010). Measuring phase-amplitude coupling between neuronal oscillations of different frequencies. Journal of Neurophysiology, 104(2), 1195–1210.
Vadillo, M. A., Gold, N., and Osman, M. (2016). The bitter truth about sugar and willpower: The limited evidential value of the glucose model of ego depletion. Psychological Science, 27(9), 1207–1214.
van der Auwera, J., and Plungian, V. A. (1998). Modality’s semantic map. Linguistic Typology, 2(1), 79–124.
Westbrook, A., and Braver, T. S. (2015). Cognitive effort: A neuroeconomic approach. Cognitive, Affective, & Behavioral Neuroscience, 15(2), 395–415.
Yeung, N., and Monsell, S. (2003). Switching between tasks of unequal familiarity: The role of stimulus-attribute and response-set selection. Journal of Experimental Psychology: Human Perception and Performance, 29(2), 455–469.
| Model term | Functional interpretation | Core measurement mapping | Expansion mapping |
| --- | --- | --- | --- |
| in Eq. (5) | Available control budget | HRV recovery slope, SCR recovery profile, diurnal cortisol slope | PCI and network-level complexity indices |
| in Eqs. (3a), (5), (7) | Latent control cost | Task-switch cost, Stroop interference, perseverative errors, | ROS markers, Fisher-geometry metrics |
| in Eq. (5) | Environmental/task uncertainty load | Conflict level manipulations, distractor entropy, prompt variability controls | Ecological noise paradigms |
| in Eq. (5) | Task-state order/stability | from error entropy and RT variability (Eq. 5q) | Compression-ratio or sequence-complexity alternatives |
| Appraisal in Eq. (4) | Contextual threat/challenge evaluation | Trial/block-wise self-report rating (0-100 challenge/threat scale) | Multi-item stress appraisal inventories |
| in Eq. (3c) | Momentary control input effort | Trial-wise inhibitory/control demand (e.g., incongruent Stroop, switch trials, rule override trials) | Neural control-energy surrogates from EEG/TMS paradigms |
| and  in Eqs. (7a, 7c) | Normalized friction load | Primary:  (score-based); sensitivity: ratio-based | Cross-modal validation with neural/biochemical layers |
| Proxy | Healthy Controls | MDD | OCD | PD |
| --- | --- | --- | --- | --- |
| Task-switch cost (RT) | Low | Moderate–High | High (domain-specific) | High (motor-specific) |
| Perseverative errors | Low | Moderate | High | Low–Moderate |
| Temporal discounting | Moderate | High | Moderate | Low–Moderate |
| HRV recovery slope | Fast | Slow | Moderate | Moderate |
| Cortisol curve | Normal | Flattened | Normal | Normal |
| SCR during conflict | Moderate | Low (blunted) | High (cue-specific) | High (initiation-specific) |
| ROS biomarkers | Normal | Elevated | Normal–Mild | Moderate |
| PCI | High | Reduced | Preserved | Reduced (motor cortex) |
| Theta-gamma coupling | Intact | Degraded | Intact | Intact (cognitive) |
|  | Low | Moderate–High | Highest | Moderate (motor verbs) |
| Hypothesis | Tier | Core Prediction | Falsification Criterion | Required | Key Measures |
| --- | --- | --- | --- | --- | --- |
| H72 | Core | Context-sensitive  + incremental validity | No context effect and | 120 | Adjusted modal ratio, RT, HRV/SCR, symptom scales |
| H-NEURO-EXEC-01 | Core | Nonlinear cost increase with identifiable  (primary) | Linear fit dominates or no | 80 | Task-switch  load, HRV/SCR, baseline latent score |
| H-MET-01 | Core-extension bridge | Counter-habitual choice increases SCR (glucose exploratory) | No SCR difference or SCR- link | 60 | SCR (primary), glucose (secondary), compatibility task |
| H-CLIN-OCD-01 | Core clinical | Highest  in OCD | OCD  = controls | 90 (30$$3) | Modal ratio, clinical interview |
| H-CLIN-DEP-01 | Expansion | ROS predicted by  in MDD |  | 80 (40+40) | GSH/GSSG, task battery, HRV |
| Feature | Cognitive Load Theory | Allostatic Load | Free Energy Principle | EVC | IIT () | SRT () |
| --- | --- | --- | --- | --- | --- | --- |
| Cross-modal operationalization | No (behavioral only) | Partial (physiological) | Partial (neural + computational) | Partial (behavioral + computational) | No (neural only) | Yes (4 proxy classes) |
| Formal equations | Minimal | No | Yes | Yes | Yes | Yes |
| Dynamic cost function | No (static) | Yes (cumulative) | Yes (instantaneous) | Yes (cost-benefit allocation) | No (snapshot) | Yes (accumulated + derivative) |
| Clinical disorder specificity | No | Partial | Partial | Partial (task-level, non-nosological) | No | Yes (Table 2) |
| Linguistic probe | No | No | No | No | No | Yes () |
| Bandwidth saturation model | No | No | Implicit | Not explicit | No | Yes (Equation 7) |
| Explains knowing–doing gap | Partially | No | Partially | Partially | No | Yes |
| Competing account | Core competing prediction | prediction | Decisive test | Predefined decision rule |
| --- | --- | --- | --- | --- |
| Additive resource model | Switch cost rises approximately linearly with load | Changepoint/nonlinear acceleration near | Compare linear vs changepoint models in H-NEURO-EXEC-01 | If linear fit  changepoint in primary  analysis, reject saturation component |
| Generic symptom-severity model | Clinical groups differ mainly by global severity | Disorder-specific dissociations (Table 2) | Phase-2 contrasts in §4.5 | If dissociation contrasts fail, downgrade to transdiagnostic severity interpretation |
| Language-style/trait model | mostly stable stylistic variance | Context-sensitive shifts + incremental validity | H72 context contrast +  over PHQ-9/GAD-7/affect controls | If no context effect and , remove linguistic probe from core model |
| Global-deficit account | Expansion markers add little structure beyond symptoms | Optional expansion markers may add mechanistic precision | Compare core vs expansion model fit in phase-3 | If no incremental value, retain core chain and demote expansion markers to exploratory |