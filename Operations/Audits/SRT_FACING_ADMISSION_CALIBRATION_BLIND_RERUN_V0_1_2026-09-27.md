---
id: SRT-FACING-ADMISSION-CALIBRATION-BLIND-RERUN-V0-1-20260927
type: audit
status: active
date: 2026-09-27
layer: operations
epistemic_layer: governance
claim_mode: blind_calibration_review
canonical: false
research_mode: U
dependency:
  - Operations/Handoffs/SRT_FACING_ADMISSION_CALIBRATION_BLIND_HANDOFF_2026-09-27.md
  - Operations/Proposals/SRT_FACING_ADMISSION_TEST_V0_1_2026-09-27.md
  - Operations/Templates/SRT_FACING_ADMISSION_RECORD_TEMPLATE_V0_1_2026-09-27.md
  - Core_Law/SRT_Generative_Ontology_Spine.md
  - Core_Law/SRT_One_Formation.md
tags: [Facing, AdmissionTest, BlindCalibration, IndependentReview, PR1079]
---

# Facing Admission Test v0.1 — independent blind calibration rerun (B1–B12)

> **Role**: independent-session execution of `Operations/Handoffs/SRT_FACING_ADMISSION_CALIBRATION_BLIND_HANDOFF_2026-09-27.md`. It serves item 2 of the method's §10 calibration requirement ("at least one independent model/session reruns assignments without seeing seed labels first").
>
> **Boundary**: READ-ONLY with respect to every existing file. There is NO canonical edit, NO Facing v0.3 edit, NO method edit, NO STATUS edit and NO PR merge. This record does not create a new `CURRENT NEXT`. It serves the #1079 pre-merge calibration gate named in the method's §11 and nothing else.
>
> **Merged-handoff disclosure**: the handoff, method, template, seed and ChoiceMap source exist only on the unmerged #1079 head branch `audit/facing-pre0925-coverage-census-20260927`, not on `main`. They are used here as the execution script and objects under test for a read-only calibration, under explicit user instruction. They are not used as a controlling continuation route.

## 0. Provenance and independence

~~~text
#1079 head branch  = audit/facing-pre0925-coverage-census-20260927
#1079 head commit  = 151a25edde2b19b51e0a1cdaa01769a1e6c17b12 (2026-09-27T21:51:53+08:00)
handoff blob       = 47dca1551dcf061b9963b8041dacfc0f6f1466fe
method v0.1 blob   = 5ec3f9b64c27a0bf6ef7b3e0bc9b4d73890a8683
template v0.1 blob = 4dc5c1afeb15f563bdf14b5e0e55db1f8c79eb28
ChoiceMap source   = 67417bc118276948709cbe8778eb4d39114321cc
seed blob (NOT READ before §3 freeze) = 12a3bc2d2dcfd3b6e85f35a9a516d71dce45aff5
~~~

Read before scoring:

- AGENTS.md session start (`SRT_AI_START.md`, retrieval profile §0–§2, `STATUS.md` Fast Status);
- the handoff, the method v0.1 and the template v0.1;
- the primary sources named per case: Spine §§0–6 and §11; One Formation §0 and §§3–5; the 2026-09-25 Gate adjudication §§1–4, §8 and §§12–17; the ChoiceMap reverse-inference source (#1079); Barad Pass 13; Simondon section of Pass 17; FRR focused reading note; FEP comparison §3 and §15; Clin_02 FEP Ax-FEP-1/2 and Ax-REAL-1/2;
- for B11: `Materials/2026/SRC_2026_08_03_Neuro_Asaoka_Habit_Strategy_Execution_Dissociation.md` and grep-level lines from `Materials/2026/SRC_2026_06_11_Philosophy_ActiveInference_FEP_Book_MITPress.md`;
- for B12: `Operations/_SRT_CHOICE_TRACE_LOG.md` header and field definitions.

Deliberately NOT read before the freeze:

- the seed `Operations/Audits/SRT_FACING_ADMISSION_CALIBRATION_SEED_V0_1_2026-09-27.md`;
- every other file added on the #1079 branch (the coverage census, HP-B crosswalk, floor-matched comparator map, the FR-AUTH / FR-ADV / Stage-3 audits, the PR1079 review handoff, and the floor-matched review-position adjudication), plus the PR #1079 description and commit messages;
- earlier machine Facing typings on `main` (the Pass-A audits such as the gate/bridge/objectification pass). They were skipped so that no prior machine facing label anchors the rerun.

Independence limits:

- this session is independent at the session level but may share model-family biases with the producing session;
- the handoff's own trap list (§4) and the method's Q3 clause were visible and may pre-shape attention;
- the B11 repository source is a habit / learning SourceCard, because the repository has no close-read of an active-inference habit-prior (policy-prior) source.

## 1. Conventions used in this rerun

- **Declared-absent is a declaration.** For L0-facing constructs, Step-0 fields such as candidate space or comparison rule are recorded as `DECLARED ABSENT / NOT PRESUPPOSED`. Without this reading every L0 candidate would be forced to UNDETERMINED. See M5.
- **Explanandum over label.** An author or source label (`L1-facing`, `L0视角下的门控`) is treated as source evidence, not as the verdict.
- **Evidential role kept apart.** Where a source uses facing words for what is *evidence* for a reconstruction (e.g. "L2-facing evidence"), that evidential role is noted separately from the construct's ontic burden. See M4.

## 2. Blind case records

### B1 — SRT O0 open / non-preclosed burden

~~~text
construct: O0 — non-maximal indifference / openness (routing label: Oriented Openness)
source: Core_Law/SRT_Generative_Ontology_Spine.md §2, §11 (L0-side)
target cut:
  unit = one finite-position-indexed primitive Selection reality-occurrence
  boundary = finite position index only (not formed locality)
  grain / equivalence / state-candidate space / comparison rule = DECLARED ABSENT
    (Spine: not a prior field, container, option menu, probability distribution,
     endpoint vector, semantic order, moral value or continuation preference)
  timescale = event-level; no before/after relative to S0
  observer / access = not itself manifest; available only through S0-side manifestation and analysis
explanatory burden facing: L0 — non-preclosure relative to determinate manifestation
formal/model realization facing: none admitted; any L_0 possibility-inventory / state-space realization would be an L1-facing model artifact (Q8)
Q1 NO — defined by not being preclosed by a given outcome structure
Q2 PARTLY — names that determinacy is not exhausted or preclosed; does not narrate cut formation alone (co-primitive with S0)
Q3 NO — not the determinate manifest side
Q4 NO
Q5 NO — the relation to S0 is a Q7 co-aspect, not a crossing construct
Q6 YES — survives removal of inventory, coordinates, menu, scale, boundary and output
Q7 YES — O0 / S0 are two co-primitive analytic faces of one Selection reality; no precedence (Spine hard guard)
Q8 no formal latent to upgrade; no formalism downgrade
Q9 PASS — Spine explicitly excludes every listed back-import; "Oriented" is not an endpoint vector
Q10 falsifier: a canonical landing that (a) establishes O0 -> S0 reduction, or (b) makes O0 depend on a given outcome structure / prior field, or (c) under Spine §12 merges O0 because it carries no independently stateable burden
verdict: FACE-L0-CANDIDATE
confidence: HIGH (facing assignment only; O0 truth and the anti-tautology criterion remain OPEN)
~~~

### B2 — SRT S0 actualising Selection

~~~text
construct: S0 — actualising Selection
source: Spine §§2–3, §11 (L1-side)
target cut:
  unit = one actualising Selection event
  boundary = finite position index
  grain = the determinate difference that becomes manifest at the declared level
  equivalence = not pre-given; differentiated in the event
  state / candidate space = NOT PRESUPPOSED (alternatives may themselves be differentiated through Selection)
  comparison rule = none presupposed
  timescale = event
  observer / access = foreground side manifest; background not co-manifest as background
explanatory burden facing: L1 — determinate manifestation / actual differentiation (= relative backgrounding, same event)
formal/model realization facing: G_hat_theta / formal operators model formed organizations, not S0; any realization is L1 and downstream
Q1 NO — no pre-given menu
Q2 YES — a determinate difference becomes manifest / operative
Q3 YES — definitional (Spine §3, §11)
Q4 NO — occurrence != retained efficacy; terminal Selection genuine
Q5 NO — the non-preclosure face is carried by O0 (Q7), not by S0
Q6 PARTLY — not defined by any menu, but its burden is the determinate side
Q7 YES — co-primitive with O0; manifestation / relative backgrounding / event-level verticality are readings of one event
Q8 n/a
Q9 n/a for an L1 verdict; no chooser required
Q10 falsifier: Spine re-routes S0 to itself carry non-preclosure (S0 as O0->manifest transition) -> FACE-L0<->L1-BRIDGE; or O0 merged into S0
verdict: FACE-L1
confidence: HIGH
note: the method's §8 fast tree would route S0 to FACE-L0<->L1-BRIDGE (cut-genesis YES -> constitutive transition YES). The verdict follows §6 criteria + Spine §11 + Q7. See M1.
~~~

### B3 — retained historical efficacy

~~~text
construct: history = prior Selection remaining materially effective in later Selection conditions
source: Spine §4, §11 (L2-side); One Formation §4
target cut:
  unit = a prior Selection-generated retained difference + the later Selection whose conditions it alters
  boundary = the declared later Selection conditions
  grain = the load-bearing retained difference (storage location not criterial)
  equivalence = which later conditions count as altered
  state / candidate space = declared later Selection conditions
  comparison rule = with vs without the retained difference
  timescale = prior -> later interval
  observer / access = efficacy inferred from altered later conditions
explanatory burden facing: L2
formal/model realization facing: scoped formal L_2 / stable-constraint objects — L2; equations owned by formal owners
Q1 YES — presupposes prior Selection and a declared later condition set
Q2 NO
Q3 PARTLY — efficacy shows in present conditions, but the burden is the prior's continued efficacy
Q4 YES — definitional
Q5 NO — the prior->later relation is internal to L2 (Spine §11), not a crossing
Q6 NO
Q7 NO — occurrence and retained efficacy are separable
Q8 n/a  Q9 n/a
Q10 falsifier: owner redefines history as mere retained difference without later efficacy, or the "efficacy" is shown to be current manifestation redescribed without a load-bearing prior difference
verdict: FACE-L2
confidence: HIGH
~~~

### B4 — Selection-position

~~~text
construct: Selection-position_t
source: Spine §6.2; Core_Law/SRT_One_Formation.md §0, §3 (Def-OF-3)
target cut:
  unit = one already formed One at time t
  boundary = operative locality of the formed selective organization
  grain = time-local (developmental lineage excluded per handoff)
  equivalence = role-level, not token identity
  state / candidate space = that of the current Selection; not presupposed as a menu
  comparison rule = n/a
  timescale = t
  observer / access = relational role within the formed organization, not an observer-side perspective
explanatory burden facing: L1 — current operative from-where
formal/model realization facing: sigma_sr family (Individuation) = downstream model variables; L1 at most; non-defining
Q1 YES — requires an already formed One
Q2 NO
Q3 YES — "time-local operative from-where through which that formed organization participates in Selection at time t"
Q4 PARTLY — a formed organization embeds prior conditioning, but the owner assigns the cross-time burden to One (formed-continuation aspect) and time-local operation to position
Q5 NO under the declared cut
Q6 NO
Q7 YES — One and Selection-position_t are distinct aspects of one formed process-unity
Q8 guard respected: not an independently prior selector object
Q9 n/a for L1; no Bearer / subject import required
Q10 falsifier: target widened to formed-continuation aspect or lineage -> FACE-L2 or FACE-L1<->L2-BRIDGE; owner revises position into a pre-One condition -> re-type
verdict: FACE-L1
confidence: HIGH
~~~

### B5 — Gate as currently available stable coarse-graining geometry

~~~text
construct: Gate ~ stable coarse-graining geometry (current role)
source: 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_GATE_GEOMETRY_BEARER_FRICTION_QUALIA_L0_FREEDOM_2026-09-25.md §§2–4, §12, §15
target cut:
  unit = one formed gate geometry relative to a declared position / scale / continuation problem
  boundary = the equivalence / boundary relations it specifies
  grain = the coarse-graining it imposes
  equivalence = SUPPLIED BY the construct
  state / candidate space = differences available before the present object cut (not the object inventory)
  comparison rule = supplied by the construct (neighborhood / transition-reachability)
  timescale = present operation + stability across declared perturbation; gate formation history excluded
  observer / access = gate backgrounded / transparent; reached through object foreground, friction or reflective gate-objectification
explanatory burden facing: L1<->L2 — per author §3.2, coarse-graining (which differences presently count as the same) and stability (that sameness staying operative under disturbance) are "two sides of one burden"
formal/model realization facing: working decomposition equivalence + boundary + neighborhood + reachability + stability — L1 structure with an L2-type robustness component; not a canonical tuple
Q1 PARTLY — does not presuppose the object cut; it IS a determinate formed cut-structure (the Step-0 cut fields map onto gate components)
Q2 PARTLY — explains object foreground / simplicity as successful gate transparency; not its own formation (excluded)
Q3 YES — currently available operative geometry
Q4 YES — "stable" = a prior-achieved equivalence regime remaining operative across later perturbation / Selection; the handoff excludes formation history, not the retention built into stability
Q5 YES — forcing L1 drops stability; forcing L2 drops present coarse-graining
Q6 NO — removing boundary / equivalence / comparison scale removes the gate itself
Q7 PARTLY — gate backgrounding and object foregrounding are readings of one achievement (§4); coarse-graining / stability are co-sides, not successive
Q8 inverse check: "pre-object" wording and A0-Q1 "L0视角下的门控" do not upgrade to L0
Q9 FAIL for L0 — needs formed geometry and retained history (a formed attractor in the addiction case). The author places the L0-facing burden on the *revisability* of gate geometry (§12), not on the gate
Q10 falsifier: source shows "stability" is purely synchronic counterfactual robustness at t with no later-Selection retention -> FACE-L1; gate re-declared as an object-formability burden independent of formed geometry -> reassess FACE-L0<->L1-BRIDGE; author second adjudication of what A0-Q1 "L0视角下的门控" commits the gate to
verdict: FACE-L1<->L2-BRIDGE
confidence: MEDIUM
~~~

### B6 — ChoiceMap latent directional-generative organization

~~~text
construct: L1-facing directional-generative selection process (ChoiceMap reconstruction target)
source: 01_Source_Intuition/SRT_AUTHOR_FACING_CHOICEMAP_REVERSE_INFERENCE_2026-09-27.md §§4–5, §§8–11 (#1079)
target cut:
  unit = one formed subject (formed One / position with historically inherited direction)
  boundary = subject-internal
  grain = process-level (author rejected the stable-latent-preference branch, §5)
  equivalence = not fixed
  state / candidate space = objects, comparison scales and candidate spaces are GENERATED / RECUT, not presupposed
  comparison rule = generated
  timescale = ongoing current generation under changing conditions
  observer / access = not directly observable; reconstructed from recorded traces (author: "L2-facing evidence")
explanatory burden facing: L1 — author-native: dynamic generative selection event currently operative (§4, §5, §8 "two facings of the same ongoing L1 event")
formal/model realization facing: any ChoiceMap-reconstructed latent model = L1 formal latent; hidden != L0 (Q8)
Q1 PARTLY — presupposes formed subject + inherited direction; not the object-level candidate space / comparison scale
Q2 YES at the object-cut level — generates / recuts objects, comparison scale, candidate space
Q3 YES — "continuously operative in current generation"; latent / nonconscious does not block L1 (method Q3 clause)
Q4 PARTLY — direction "historically inherited" = L2 input, not the explanandum
Q5 PARTLY — cut generation resembles pre-object -> determinate bridging, but the author carries the L0 face separately (traces -> L1 process -> L0 primitive Selection as a further reverse inference); alternative generation is S0-type work (Spine §2.1)
Q6 PARTLY — survives removal of object inventory / menu / scale only by keeping formed subject + inherited direction
Q7 YES — felt better/worse readout and next-cut generation = two facings of one L1 event (§8 C); layered phenomenality (§9) = downstream access facing
Q8 inverse check: hidden + generative + pre-object-relative-to-current-cut does not upgrade to L0
Q9 FAIL for L0 — subject, inherited direction (retained history), better/worse polarity (goal / value-adjacent), downstream Bearer / Expectation differentiation
epistemic note: reconstruction from traces is an access route, not the construct's ontic facing (D-G guard)
Q10 falsifier: explanandum narrowed to the pre-object relation by which the next cut becomes determinate, stripped of subject / inherited direction, with the author placing the L0 face inside the construct -> FACE-L0<->L1-BRIDGE; author reverts to the stable-latent-preference branch -> FACE-L1<->L2-BRIDGE or FACE-L2
verdict: FACE-L1
confidence: MEDIUM
~~~

### B7 — Barad agential cut

~~~text
construct: agential cut — constitutive enactment of determinate separability (not the whole theory)
source: Operations/Audits/SRT_PREOBJECT_FOREGROUND_OBSERVABILITY_BARAD_STRONGEST_NEIGHBOR_PASS13_2026-09-10.md §§1–4
target cut:
  unit = one phenomenon (primary ontological unit) with its specific intra-action
  boundary = enacted within the phenomenon (exteriority-within-phenomena), not pre-given
  grain / equivalence = enacted by the cut
  state / candidate space = NO pre-given independent relata
  comparison rule = apparatus-specific
  timescale = intra-action
  observer / access = apparatus / measurement constitutive, not neutral readout
explanatory burden facing: L0<->L1 — constitution of determinate separability out of ontic indeterminacy; both faces are internal to the single construct
formal/model realization facing: apparatus specification + outcomes = L1; a state-space reconstruction = L1 realization (Pass 13 PO-3 still live)
Q1 NO for relata / boundaries; YES for apparatus (itself a phenomenon / material-discursive practice)
Q2 YES — intra-actions enact boundaries and determinate separability
Q3 YES — the enactment yields actual determinate separability
Q4 NO under target (iterative reconfiguration excluded)
Q5 YES — the main role is the indeterminacy -> determinate-separability constitution relation
Q6 PARTLY — survives removal of relata, boundaries, inventory; not removal of apparatus / phenomenon
Q7 YES — enactment and determinacy are one intra-action, not "indeterminate, then determinate"
Q8 n/a
Q9 PARTIAL — no chooser / subject (human agency not required), no menu; but the apparatus is formed content -> L0-only fails; bridge survives
Q10 falsifier: source-native reading shows the cut presupposes determinate relata (mere epistemic boundary-drawing) -> FACE-L1
verdict: FACE-L0<->L1-BRIDGE
confidence: MEDIUM (repository reconstruction, not a direct Barad close-read)
comparison note: SRT S0 (FACE-L1) vs agential cut = INVALID-CROSS-FACING; admissible bridge-level comparator = primitive Selection's O0+S0 pair
~~~

### B8 — Simondon transduction

~~~text
construct: transductive individuation (individual + associated milieu become structured)
source: Operations/Audits/SRT_MANIFESTATION_SELECTION_POSITION_D3_D4_STRONGEST_NEIGHBOR_PASS17_2026-09-10.md §4, §7
target cut:
  unit = one individuation operation within a metastable system
  boundary = individual + associated milieu co-generated, not pre-given
  grain = domain-by-domain propagation of structuration
  equivalence = produced
  state / candidate space = no menu of finished possible individuals
  comparison rule = n/a
  timescale = operation (iterative beyond target)
  observer / access = physical / biological description
explanatory burden facing: L0<->L1 — resolution of metastable preindividual disparation into a structured individual + milieu
formal/model realization facing: energetic / metastability description (supersaturation, crystallization germ) = L1-facing determinate state description (burden vs realization split)
Q1 NO for individuals / milieu; YES for metastable system + structural germ
Q2 YES
Q3 YES for the structured result
Q4 PARTLY — retained preindividual charge + iterative propagation (Pass 17 R4 / R5) are L2-type, outside the declared explanandum
Q5 YES
Q6 PARTLY — survives removal of individuals, boundaries, menu; not removal of the metastable system and germ
Q7 YES — individual and milieu co-differentiated in one operation
Q8 direct check: energetic formalism does not downgrade the burden (preindividual != hidden set of completed objects)
Q9 PARTIAL — germ = formed structure; metastable system determinate at energetic grain -> L0 side is cut-relative, not O0-strength
Q10 falsifier: transduction read strictly as propagation from a formed germ through an already determinate field -> FACE-L1; target widened to retained preindividual charge feeding later individuation -> FACE-MIXED
verdict: FACE-L0<->L1-BRIDGE
confidence: MEDIUM
~~~

### B9 — Whitehead / FRR actualized occasion as later datum

~~~text
construct: actualized occasion in its objective / superjective role
source: 01_Source_Intuition/Conversations/2026-09-23_FRR_SRT_Focused_Reading_Note.md §3, §6
target cut:
  unit = one actualized occasion (objective aspect) + subsequent occasions-in-process
  boundary = the datum relation (internal relatedness)
  grain = occasion-level
  equivalence = compatibility constraints
  state / candidate space = subsequent local Boolean contexts
  comparison rule = context compatibility
  timescale = logical / mereotopological subsequence (temporal = specialization)
  observer / access = datum prehended by subsequent occasions
explanatory burden facing: L2 — actualized fact has causal efficacy for subsequent predication; the augmented totality constrains later local contexts
formal/model realization facing: sheaf-theoretic gluing / added compatibility constraints on later local frames = L2
Q1 YES — presupposes the occasion as actualized
Q2 NO
Q3 NO — the subjective (concrescent) aspect is the L1 side and excluded
Q4 YES
Q5 PARTLY — subjective -> objective transition is a bridge, but the target is the objective role
Q6 NO
Q7 PARTLY — subjective / objective are aspects of one occasion; "subsequent" primarily logical, not temporal (D-F risk)
Q8 n/a  Q9 n/a
Q10 falsifier: FRR logical subsequence shown to carry no later-conditioning ordering -> FACE-L1<->L2-BRIDGE or FACE-UNDETERMINED (the note keeps exact SRT-L2 mapping OPEN)
verdict: FACE-L2
confidence: MEDIUM
~~~

### B10 — active-inference generative model

~~~text
construct: current generative model over declared hidden states, observations and policies
source: Philosophy/SRT_FEP_Comparison.md §3, §15; Neuroscience/SRT_Clin_02_FEP.md Ax-FEP-1/2
target cut:
  unit = one agent's generative model at t
  boundary = given Markov blanket
  grain = declared hidden states / observations / policies
  equivalence = the model's state partition
  state / candidate space = declared policy set
  comparison rule = expected free energy
  timescale = current inference-action cycle
  observer / access = model-internal; observations declared
explanatory burden facing: L1
formal/model realization facing: L1 (POMDP-type declared state space)
Q1 YES — FEP starts from an existing system, boundary and model-update task (FEP comparison §3)
Q2 NO under target (structure learning / model genesis excluded)
Q3 YES
Q4 PARTLY — parameters / priors are learned, but the explanandum is current operation (contrast B11)
Q5 NO  Q6 NO  Q7 NO
Q8 inverse check: hidden / probabilistic / generative does not upgrade to L0. Clin_02 Ax-FEP-2 ("主动推理是 L_0 探索的受限策略") uses the pre-Spine L_0-as-possibility-space reading, which the current symbol guard forbids; policy-set exploration is L1-facing
Q9 n/a
Q10 falsifier: target widened to high-road blanket formation / structure learning -> reassess as a bridge
verdict: FACE-L1
confidence: HIGH
~~~

### B11 — learned prior / habit

~~~text
construct: prior learned organization, only insofar as it continues to constrain later inference / action
source: Materials/2026/SRC_2026_08_03_Neuro_Asaoka_Habit_Strategy_Execution_Dissociation.md §§2, 5–6; Materials/2026/SRC_2026_06_11_Philosophy_ActiveInference_FEP_Book_MITPress.md (priors vocabulary only)
target cut:
  unit = a learned organization (habit strategy / learned prior) + later inference / action episodes
  boundary = declared task / policy domain
  grain = strategy conversion vs execution gain kept separate
  equivalence = same strategy / policy
  state / candidate space = declared action / policy set
  comparison rule = outcome-sensitivity tests; pathway-erasure contrasts
  timescale = training window -> later tests
  observer / access = behavioral + causal manipulation
explanatory burden facing: L2
formal/model realization facing: plasticity / learned parameters constraining later inference = L2 (card §4.7: circuit != canonical L2; facing != identity)
Q1 YES  Q2 NO
Q3 PARTLY — execution gain at t is the L1 side; excluded by "insofar as"
Q4 YES — "historical constraints can control policy selection and output intensity", with selective causal erasure
Q5 NO under restriction (strategy conversion, i.e. historical control replacing outcome-sensitive control, would be the L1<->L2 relation if targeted)
Q6 NO  Q7 NO  Q8 n/a  Q9 n/a
Q10 falsifier: learned organization shown to have no later constraining role (fully overwritten each episode) -> not L2; target re-declared as strategy conversion -> FACE-L1<->L2-BRIDGE
verdict: FACE-L2
confidence: HIGH
note: B10 / B11 are the same architecture with different explanandum; the method's indexing handles this correctly
~~~

### B12 — stored ChoiceMap transcript as archived text

~~~text
construct: ChoiceMap / Choice-trace transcript merely as stored record
source: ChoiceMap reverse-inference source §4 (#1079); Operations/_SRT_CHOICE_TRACE_LOG.md §0–§1
target cut:
  unit = one stored transcript / trace document
  boundary = the document
  grain = recorded fields (seed_fragment, layered_options, chosen, skipped_mode, reason, closure_boundary ...)
  equivalence = same stored content
  state / candidate space = recorded option sets (already determinate)
  comparison rule = field-wise
  timescale = storage interval
  observer / access = reader / analyst retrieval
explanatory burden facing: L1 (thin) — a present determinate artifact; no later-effective role (excluded by target)
formal/model realization facing: none (text record)
Q1 YES — records an already determinate option set and choices
Q2 NO
Q3 YES (weak) — currently actual determinate artifact; not operative in subject generation by stipulation
Q4 NO — archive != L2 without an established later-effective role; the trace log's design intent (future generation / diagnosis may condition on it) is projected conditioning of later LLM generation, not established efficacy on subject generation, and is excluded by target
Q5 NO for the record itself; its use in reverse inference is a method-level evidential bridge, not the record's burden
Q6 NO  Q7 NO  Q8 n/a  Q9 n/a
Q10 falsifier: storage / re-reading shown to materially alter later subject generation (author re-reads traces and recuts) -> FACE-L2 for that role; an evidential-role axis would re-home the author's "L2-facing evidence" label
verdict: FACE-L1
confidence: MEDIUM
alternative considered: FACE-UNDETERMINED — rejected because the cut is declarable and the negative Q4 is decisive; the burden carried is only artifact-level (see M4)
~~~

## 3. BLIND VERDICTS B1–B12 (frozen before seed reading)

| case | construct | verdict | confidence |
|---|---|---|---|
| B1 | SRT O0 open / non-preclosed | FACE-L0-CANDIDATE | HIGH |
| B2 | SRT S0 actualising Selection | FACE-L1 | HIGH |
| B3 | retained historical efficacy | FACE-L2 | HIGH |
| B4 | Selection-position (time-local) | FACE-L1 | HIGH |
| B5 | Gate current stable coarse-graining geometry | FACE-L1<->L2-BRIDGE | MEDIUM |
| B6 | ChoiceMap latent directional-generative process | FACE-L1 | MEDIUM |
| B7 | Barad agential cut | FACE-L0<->L1-BRIDGE | MEDIUM |
| B8 | Simondon transduction | FACE-L0<->L1-BRIDGE | MEDIUM |
| B9 | FRR / Whitehead actualized occasion as datum | FACE-L2 | MEDIUM |
| B10 | active-inference generative model (current) | FACE-L1 | HIGH |
| B11 | learned prior / habit (continued constraint) | FACE-L2 | HIGH |
| B12 | stored ChoiceMap transcript as archive | FACE-L1 | MEDIUM |

Origin-bias self-check against handoff §4: the SRT-internal constructs are not uniformly privileged (B6 = L1, B12 = L1, B5 = no L0), and the traditional constructs are not uniformly downstream (B7 and B8 carry an L0<->L1 bridge).

### 3.1 Pre-seed method observations

These were written before the seed was read, so they are not shaped by the seed:

- **M1 — fast tree lacks an L1 exit in the cut-genesis branch.** The §8 tree routes S0 (the canonical L1 face) and the ChoiceMap process to L0<->L1 BRIDGE. That contradicts the Q3 clause ("dynamic, hidden, latent, generative ... may remain L1-facing") and Spine §2.1 (alternatives can be differentiated through Selection, which is S0-type work). Candidate fix: in the YES branch ask whether the non-preclosure face is carried *inside* this construct or *separately* (by O0, or by a further inference target). If separately, the verdict is L1 with a Q7 aspect note.
- **M2 — the L0 side is ambiguous.** "L0-facing" can mean cut-relative pre-object (relative to a declared object cut; compatible with a formed germ, apparatus or subject) or O0-strength non-preclosure. Q9 enforces O0 strength only for L0-CANDIDATE; the BRIDGE label does not say which strength it means. Candidate fix: bridge records state `L0-side = cut-relative | O0-strength` (B7 and B8 are cut-relative; B1 is O0-strength).
- **M3 — Q3 and Q4 have no tie-break.** Both fire for any currently operative formed organization (B4, B5, B10, B11). Candidate rule: type by what the explanandum needs — present operation at t is L1, a prior formation's continued constraint is L2, and both constitutive of one burden is L1<->L2 BRIDGE. Also record whether "stability" means synchronic robustness or diachronic retention.
- **M4 — evidential facing is not separated from ontic facing.** Author ChoiceMap usage ("L2-facing evidence") labels an evidential / access role, but the method has only burden and realization axes. Candidate fix: a third axis `C. EVIDENTIAL / ACCESS ROLE` to block D-G confusions (B6, B12).
- **M5 — declared-absent cut fields.** Step 0 should say explicitly that `DECLARED ABSENT / NOT PRESUPPOSED` counts as a declaration. Otherwise the rule "if these cannot yet be declared, use FACE-UNDETERMINED" forces every L0 candidate to UNDETERMINED.
- **M6 — nested cuts.** A construct formed at one cut level can constitute cuts at a lower level (gate, ChoiceMap process, Selection-position). Records should name both the construct's own cut and the cut it constitutes.

### 3.2 Comparison-admission implications (method §7)

~~~text
S0 (L1)            vs Barad agential cut (L0<->L1)    = INVALID-CROSS-FACING unless the bridge is the target
O0+S0 pair         vs Barad cut / Simondon transduction = BRIDGE-level comparison (admissible)
B3 history (L2)    vs B9 FRR datum (L2)                = SAME-FACING
B6 ChoiceMap (L1)  vs B10 generative model (L1)       = SAME-FACING
B10 (L1)           vs B11 (L2)                         = not same-facing; the relation (learning -> current model) is an L1<->L2 bridge target
B12 record (L1)    vs B3 history (L2)                  = INVALID-CROSS-FACING (record != efficacy)
~~~

**Freeze statement**: §§0–3 were committed to `claude/srt-blind-calibration-12-oxrhc9` before the seed file was opened. The post-seed comparison follows in §4 and later sections, added in a separate later commit.
