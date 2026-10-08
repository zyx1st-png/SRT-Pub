---
id: SRT-ONE-GATE-MINIMAL-FORMALIZATION-PROOF-COUNTERMODEL-AUDIT-20261008
type: audit
status: draft
canonical: false
layer: operations
epistemic_layer: machine_analysis
claim_mode: formalization_audit
created: 2026-10-08
updated: 2026-10-08
research_mode: U
root_question: What does a bounded One and typed Gate formalization actually establish at current owner strength, and which admission burdens remain independently OPEN?
comparative_claim: none
named_comparator: null
n_mode_triggered: false
dependency:
  - STATUS.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_PRIMITIVE_SELECTION_ANTI_TAUTOLOGY_STOP_AND_NEXT_ROUTING_2026-09-27.md
  - Core/SRT_Core_21_Minimal_Axioms.md
  - Core/SRT_Core_21b_Constitutive_Theorems.md
  - Core_Law/SRT_Generative_Ontology_Spine.md
  - Core_Law/SRT_One_Formation.md
  - Operations/Audits/SRT_GATE_TYPED_OPERATOR_MINIMAL_FORMALIZATION_2026-09-26.md
  - Operations/Proposals/SRT_PREOBJECT_GENERATIVE_ORIENTATION_COGNITION_RESEARCH_PROGRAM_2026-09-26.md
  - 01_Source_Intuition/SRT_AUTHOR_ADJUDICATION_BEARER_GATE_VERTICALITY_MEMBRANE_GATING_2026-10-07.md
tags: [Formalization, OneFormation, Gate, Countermodel, RefinementTypes, ProofScope, AntiOverclaim]
---

# Bounded One / Gate formalization — model limits and admission obligations (revised)

> **Verdict:** at the **current local owners' strength**, event- and edge-signature examples yield only **trivial syntactic non-entailments**. The first substantive unresolved One-formation obstacle is the positive, independently applicable **relative continuation separability** criterion in Def-OF-2 / §2. Candidate classifiers based on an observed cycle, generic path dependence or one deletion effect may over-admit. Form / Close / Compose require **evidence-carrying admission steps**, not automatic candidate promotion. Neither a new One theorem nor a universal Gate algebra is claimed.
>
> **Status:** noncanonical U-mode feasibility/review record. No Lean/Lake verification, empirical result, independent full-domain theorem, new canonical definition, current-next change, or approval to execute an experiment. Prior first draft was challenged by an author-forwarded Claude review; this revision accepts its principal mathematical and typing corrections. Reviewer agreement is not proof.

## 0. Authorization, source of interpretation, and scope (A1)

- **Operational authorization:** in the 2026-10-08 GitHub-connected dialogue, the author said 「继续，如有必要可写入仓库」 in direct continuation of a bounded One/Gate formalization-feasibility analysis, and then supplied a critical review of the resulting Draft PR #1104. That permits **scoped noncanonical analysis/revision**, not elevation of each machine-suggested F-item to author theory, not a new ongoing research programme, and not blanket permission to change frozen canonical owners. This is a dialogue-scope note, not an invented A1 theoretical adjudication.
- **Owner authority:** the active cross-owner Generative Ontology Spine and Def-OF-1..3 / §7 of Core_Law/SRT_One_Formation.md remain controlling; Gate typing comes from the 2026-09-26 noncanonical typed audit. The 2026-10-07 Bearer/Gate source has already landed in merged PR #1103, but the **post-Bearer maintenance/revision interpretation inside that source** remains pending a second author adjudication.
- **Programme boundary:** STATUS CURRENT NEXT = neutral cognition E2/E3/E4 discriminator first. No anti-tautology STOP reopening, no author-owned new formal domain claim, no toy execution, no third deep well, no independent branch/merge-identity inquiry beyond noting its **HOLD**. No modifications to canonical, STATUS, CURRENT NEXT, HP-B, symbol table or cognitive owner.
- **Constitution boundary:** a formal model chooses unit, boundary, grain, equivalence and normalization; those choices do not become SRT constitutional authority. All symbols in this file are audit-only.
- **2026-10-07 source's 'no formal model is opened' guard:** the finite toy cases below are retrospective **tests of whether an attempted classifier over-admits** within this bounded machine audit, not an independently launched formal model, research lane, preregistered experiment, formal domain reconstruction or canonical construction. No newly active model or project is claimed.

## 1. Owner facts to preserve (not outputs of the proposed math)

1. **Primitive Selection** is genuine actualised non-neutral differentiation; not an ordinary choice among a pre-given option menu and not identified with a formal operator. A **modelled state-transition edge is not thereby an established ontic Selection**; this does **not** demote genuine real changes to a special admissible subclass. The 2026-09-27 author ruling explicitly disallows narrowing primitive Selection to a special subclass of real changes. The precise anti-tautology discriminator remains OPEN. Neither "admitted model event" nor graph edge independently pays for ontic Selection.
2. **One / Def-OF-2** requires *Selection-mediated vertical reconstitution* that yields relatively separable formed process-unity. Ordinary path dependence, causal recurrence, similarity, cyclicity and mere persistence are not sufficient. The exact necessary-and-sufficient formal classifier remains OPEN.
3. **Type order:** Selection-mediated formation path -> One where independently admitted -> lineage/identity attribution where warranted. A model event is not automatically the unit whose **strict identity** is at issue.
4. **Branch/merge numerical identity:** **OPEN as a One §7 ontology question**; **HOLD as a research/execution route under STATUS §Immediate routing**. These are different axes, distinct from graph-path branching.
5. **Downstream guards:** One != Stable ISP != Bearer, and none automatically entails agency, subject-position, consciousness or phenomenality. P and positive E must be separately paid for Bearer.
6. **Gate owner:** Formation, Closure and Composition are different typed transformations. Their formed outputs may acquire a gating role only if that role is separately admitted. SC-1..SC-6 is a candidate shared stabilization contract; U1..U5 are proposed cross-type invariants, **not** already-proved invariants.
7. **Author source scope:** formed Gate can precede Bearer; Bearer is not a universal source of Gate. Post-Bearer gate maintenance/revision remains pending, and membrane examples do not establish a universal GK-1a unification.

## 2. F-01 / F-02 — signature-level checks only

### 2.1 Explicit sorts and predicates

For a deliberately **weak, syntactic toy signature**, declare:

~~~text
Event : Type
FormationSupport : Type      -- locally considered finite event subgraph
                             -- (a finite set of event records plus an edge relation);
                             -- not necessarily a linear sequence or unique successor
AdmEvent : Event -> Prop      -- only a declared *model* event role
MarkedVertical : Event -> Prop -- a model label, not primitive Selection
Edge : Event -> Event -> Prop -- descriptive / candidate transition
Member : Event -> FormationSupport -> Prop
AdmissionOn : FormationSupport -> Prop
                             -- hypothetical claim that a support carries an
                             -- independently admitted formed process-unity
FormedOne : Type             -- abstract post-admission type, no token assumed
Carries : FormationSupport -> FormedOne -> Prop
                             -- optional *post-admission* carrier relation;
                             -- no existence or uniqueness axiom is supplied
~~~

A `FormationSupport` may be a **finite, branching subgraph**; it is not a list, linear timeline, pre-given One identity or N&S One admission criterion. `AdmissionOn(s)` says that an independently qualified formed process-unity is carried by `s`, **not** that `s` or an event **is** a One. `Carries` is a possible post-admission description and does not provide any formation theorem. Both remain deliberately unconstrained in this weak signature.

### F-01 — isolated-event witness: trivial non-entailment only

Choose Event = {e0} and a support s0 consisting of that node and no edge; AdmEvent(e0), MarkedVertical(e0) true and AdmissionOn(s0) false. The minimal positive event statement is true while independently qualified formed One admission is absent. This is **not** a model of primitive Selection, and s0 is not automatically an ontic path.

**Accurate status:** merely the familiar signature-level observation that if AdmittedOne is unconstrained by event axioms then its existence does not follow. **Do not** add "One not forced by occurrence" as a model axiom: if formulated as a negated implication it would already assert the intended outcome, and if treated metatheoretically it is the very claim being checked. The witness adds **no nontrivial information** about Def-OF-2 and does not exercise the owner's "generic recurrence != One" boundary.

### F-02 — nonfunctional edge relation: trivial branching only

Take Event = {a,b,c,d,e} and Edge = {(a,b),(a,c),(b,d),(c,e)} in a finite candidate support. There are two graph walks [a,b,d] and [a,c,e]; neither walk is a designated One carrier, and nothing admits a formed One.

**Accurate status:** a relation not constrained to be a function can branch. This is not an ontological identity discovery and was already allowed by the chosen toy signature. Distinguish strictly:

~~~text
event graph branching      = two paths in a declared graph
formed-One strict identity = status of an already formed One;
                             additional admission + identity rules required
                             One §7: OPEN (ontology); STATUS: HOLD (execution)
~~~

**No branch/merge identity result is inferred or proposed for promotion.**

## 3. F-03 — the load-bearing unresolved separability burden

### 3.1 Two over-admission counterexamples to *candidate shortcuts*

**C1: SCC / cycle shortcut over-admits (intervention-qualified).** Suppose an exogenous clock U alternates 0 and 1 while the recorded local observable is x_t := U_t, with U_(t+1) := 1 - U_t. The **observed graph** contains 0 -> 1 and 1 -> 0, so is strongly connected. Observationally, x_(t+1) = 1 - x_t predicts perfectly; lagged predictive / Granger-style tests alone could find the relationship. **But** under a permitted intervention do(x_t := a) that leaves the exogenous clock mechanism unchanged, x_(t+1) := U_(t+1) is unaffected. Thus an *observed SCC / predictive recurrence* cannot alone establish local intervention-mediated reconstitution, much less relative continuation separability. This rejects a **naive observed-SCC sufficiency classifier**; it neither rules out all possible model structures nor establishes that no One exists in the full system.

**C2: one-step deletion-effect shortcut over-admits (memoryless relay).** Fix a structural causal model across declared times:
   
~~~text
U_t   := exogenous input at time t
X_t   := U_t                  -- memoryless relay; no X_(t-1) dependence
Y_t   := X_t                  -- measured downstream output
X_(t+1) := U_(t+1)           -- no X_t -> X_(t+1) reconstitution arrow
~~~

With U_t=1, do(X_t := 0) changes Y_t from 1 to 0. The one-step criterion "removing / altering X changes a declared probe" therefore accepts X as *causally relevant*. However, in this **fixed** model, X_(t+1) is not affected by do(X_t), and there is **no prior X-produced organization re-entering later X-formation conditions**. The one-step effect is therefore unable to discriminate a memoryless relay from the stronger **Selection-mediated vertical reconstitution** target. This is **a false positive for that insufficient classifier**, not proof that no real One exists in the surrounding system. In particular, a passive memorylessness observation cannot be elevated to an independent criterion for primitive Selection or for excluding every form of One.

**Replacement guard / correction of the earlier owner misquote:** One §2 actually says **'the relevant reconstitution dependence is not wholly or freely replaceable by arbitrary surrounding-field history while preserving the same claimed formation path'**, **NOT** 'actual surrounding-field history'. The word **arbitrary** is an owner-level semantic burden and currently has **no independently adjudicated operational quantifier**. Testing only the one realized history supplies no counterfactual; admitting every mathematically imaginable/unbounded control can falsely classify genuinely environment-supported processes as freely replaceable. A domain-model audit may predeclare an intervention envelope and grain, but **must not identify that chosen envelope with the canonical One criterion** or promote its result to ontic One admission. Rewiring Y := U into a new system is not evidence that the tested original path was replaced. The fixed-relay C2 only establishes absence of recurrence conditioning in its declared toy model; it does not settle One presence or absence.

These examples distinguish a **descriptive transition graph** and an observed **causal effect** from the owner's stronger path-specific, Selection-mediated formation burden. Neither may silently be relabelled as a demonstrated ontic Selection process.

### 3.2 What a real positive F-03 candidate would need

The positive target is *Selection-mediated vertical reconstitution with independently evidenced relative continuation separability*, **not** "true path dependence." Ordinary path dependence and an externally replaceable common input belong among controls / rejection cases.

A later **bounded and independently approved** domain proposal would have to specify:

- a candidate vertical-reconstitution dependency beyond recorded correlation, passive persistence and clocked common input;
- bounded perturbations and declared model-level backgrounds and histories, while **explicitly recording that no owner-grounded range for 'arbitrary surrounding-field history' is yet available**; one actual history is not a counterfactual, an unbounded imaginary-control range can over-exclude, and a predeclared empirical envelope is only an **exploratory domain proxy**, never the canonical One criterion;
- comparable controls (ordinary history dependence; observer re-identification; externally replaceable driver; passive recurrence), and a declared failure case;
- how the same claimed formation-path effect remains or fails when candidate organization and background supports are separately manipulated;
- what would count merely as a model realization / proxy, *without* claiming that any positive proxy proves primitive Selection or One's metaphysical N&S theorem.

**Verdict:** F-03 remains **OPEN**. The counterexamples reject naive classifier sufficiency only. No positive objective and no author-established natural boundary has yet been solved.

## 4. F-04 — time-indexed, recursive, evidence-bearing typed Gate sketch

This is **not** a one-directional total pipeline or a newly adopted formal model. The 2026-09-26 typed Gate audit §8 makes the **recursion** load-bearing: formed organizations change later sampling / selectability, which changes what will be formed next. A type sketch that stops at Compose and omits the prospective feedback would misstate FK4 and MK5.

### 4.1 Audit-only typed staging (candidate != admitted)

~~~text
History_t, EncounterSequence_t, RelevanceDirectionConditions_t : local inputs

Form_t : (History_t, EncounterSequence_t, RelevanceDirectionConditions_t)
         -> BridgeCandidate_t
FK_t : BridgeCandidate_t -> EvidenceObligation
       -- F-K1..F-K5, including F-K4 prospective reuse and F-K5 revision

AdmittedBridge_(t+1)
  := Σ (b : BridgeCandidate_t), IndependentlyAssessedEvidence(FK_t(b))

Close_t : (ThinIndex_t, Family(AdmittedBridge_t), History_t)
          -> ClosureCandidate_t
CK_t : ClosureCandidate_t -> EvidenceObligation
       -- C-K1..C-K6, including prospective downstream efficacy

AdmittedClosure_(t+1)
  := Σ (c : ClosureCandidate_t), IndependentlyAssessedEvidence(CK_t(c))

Compose_t : (Family(AdmittedClosure_t), ContextBodyGoalConditions_t)
            -> FieldCandidate_t
MK_t : FieldCandidate_t -> EvidenceObligation
       -- M-K1..M-K5, including M-K5 future bridge sampling/revision

AdmittedField_(t+1)
  := Σ (phi : FieldCandidate_t), IndependentlyAssessedEvidence(MK_t(phi))

Update_t : (AdmittedField_t, Consequence_t) -> History_(t+1)
           -- where no previously admitted Field_t exists, a declared
           -- empty/partial baseline must be separately handled

Field_t / formed organization -> changes A_(t+1) over bounded Q_(t+1)
                              -> affects next encounter / sampling
                              -> Form_(t+1) (possibly revised bridge)
                              -> Close / Compose in subsequent rounds
                              -> later admitted Field where warranted
~~~

The `Σ` notation means **candidate + independently supplied evidence**, not a magic constructor. `History_t` belongs only to this scoped history-bearing realization, **not** the ontic definition of every primitive Selection occurrence. The schema does not imply that the typed families or their evidence are populated at every t.

### 4.2 The missing prospective proof obligations

- **F-K4:** evaluate at a **later declared probing opportunity** (e.g. t+1), before the outcome of that continuation is known. Compare bounded future-selectability `A_(t+1)` across matched *candidate bridge present / counterfactual bridge absent* trajectories at declared `Q_(t+1)`, controlling for the admitted background field / Compose context. "Bridge changes A" may **not** be read off the candidate's label or its parent Form call. Observed change also does not alone settle causality unless the comparison design warrants it.
- **C-K6:** a closure candidate's added future efficacy relative to independently handled admitted bridges is likewise a separately measured / model-justified prospective contrast; it is not entailed by the Close type signature.
- **M-K5:** compare a trial organization's effect on the **later bridge sampling / retention / revision process** (t+1 or a declared subsequent interval) with a matched condition in which the candidate field organization is absent. Merely computing `Compose_t` does not prove recursive feedback.
- **Other FK/CK/MK obligations** may require multiple perturbations, repeated trials or later windows; "t+1" here marks **strict prospective dependence on later evidence**, **not** a universally sufficient one-step observation or evidence threshold.

**Non-circular staging:** any `AdmittedField_t` used to govern `Update_t` must have been admitted from evidence available **before** that call. A candidate `FieldCandidate_t` can be placed in **explicitly tagged counterfactual/trial trajectories** to test MK5, but cannot bootstrap its own `AdmittedField_t` witness. Candidate admissions produced from those prospective trials are at t+1 **only after** evidence has been independently checked. Analogously F-K4's candidate bridge is a *trial candidate*, never silently promoted to `AdmittedBridge_t` by inclusion in a trial field. No within-time evidence dependency is allowed to loop back onto itself. A prior admissible baseline (possibly empty) is needed to start induction.

Time indexing **makes acyclic staging possible**; it does not by itself prove that the evidentiary criteria, intervention definitions or ontology are well founded, or that this programme has a total recursive semantics. If any FK/CK/MK assessment calls the same stage's unproved admission as a premise, the sketch fails closed.

### 4.3 Separate Gate-role criterion and refusal conditions

~~~text
GateRole : FormedOrganization -> Prop
-- distinct independently warranted organization-level function;
-- no implicit FK/CK/MK -> GateRole coercion
~~~

1. No unguarded Candidate -> Admitted conversion; no FK -> CK -> MK or MK -> GateRole inference.
2. No claim that relevance/direction arguments are primitive Selection direction or ethical direction.
3. No universal Bearer / Concern / Psi_f / consciousness input requirement.
4. No identification of Form, Close and Compose with a single Gate equation; SC-1..6 remain a distinct contract.
5. No inference that a field's feedback `Update_t` proves One / Bearer / primitive Selection.

**Status:** typed **provisional recursive interface**, not a nontrivial ontic theorem or completed proof. The outstanding content is independently justified evidence for FK/CK/MK and robust time-indexed counterfactuals.

## 5. F-05 — remove rank lemma from this One / Gate result set

The first draft placed an ordinary matrix-rank bound inside One/Gate formalization even though its target is E2 predictive geometry. This was a scope error. **No F-05 proof, SRT formal milestone, or E2 owner edit is retained in this audit.**

For exact disposition / avoiding future reuse without its assumptions:

- Standard fact: if ΔY = BΔZ with fixed B in R^(m x r) and ΔZ in R^(r x n), then rank(ΔY) <= r. **It is a conditional linear-algebra identity, not an SRT claim.**
- **Independent fixed r and r < min(m,n)** are necessary for the rank bound to be a nonvacuous exclusion test. With no independently fixed r, choose r >= min(m,n) and every m-by-n matrix can be factored.
- If B is allowed to change freely across conditions, **every** matrix is realizable with r=1 by setting B_j equal to its j-th column and z_j=1. For the draft's incompatible 3-by-2 example, the correct columns are [1,0,1]^T and [0,1,1]^T, not the previously claimed 2-vectors.
- ΔY requires a **declared measurement baseline**. A common intercept cancels under subtraction for a fixed affine readout, but a drifting condition-dependent baseline does not. Nonlinear readouts require explicit local linearization and only local scope; empirical noise requires a declared uncertainty/effective-rank rule.
- **Main non-discriminator:** low rank cannot distinguish an SRT-labelled shared Gate from ordinary H2 latent-state/representation models, which already generate shared low-dimensional response geometry. H1 and H2 remain competent same-target baselines, not straw rivals. Successful low rank is at best an implementation-class description, never evidence of distinctive SRT ontology.
- Any future E2 note or test belongs under the *existing* cognition programme's review and preregistration gates. **No E2 work is authorized by this PR.**

## 6. F-06 — keep U1..U5 distinct from SC-1..SC-6

The **existing typed audit §14** enumerates U1..U5 as candidate cross-type invariants, **not** proven universal results:

| Candidate | Target in the typed audit | Blocking question |
|---|---|---|
| U1 selective compression | selectively retain load-bearing differences | is this more than generic information compression? |
| U2 robustness envelope | perturbation tolerance and failure boundaries | does it really depend on formed organization rather than an imposed filter? |
| U3 counterfactual future efficacy | change the bounded local A_t for declared probes | is the effect only a replaceable common driver? |
| U4 recursive writeback | later formation responds to consequences | does the proposed type support actual revisability? |
| U5 composition without microdetail | a higher organization constrains lower selectability | could standard task-set / control graphs already provide it? |

**SC-1..SC-6** in typed audit §6 are a distinct *candidate selective-stabilization contract*, including SC-2 active/history-dependent stabilization and SC-6 revisability. Passing an SC test does not prove any U invariant across Form, Close and Compose, and does not make the three operations identical. Do not mix One admission language into a Gate-invariant test.

**Status:** prospective review questions only; no new algebra, no empirical confirmation, no canonical promotion. Preserve the typed audit's W1..W6 withdrawal conditions.

## 7. Next bounded work and stop condition

A meaningful subsequent formalization cannot simply restate F-01/F-02 or prove that a pair of datatypes is unequal.

The following are **possible, not queued** audit checks. They require an explicit author choice before execution and do **not** create a second CURRENT NEXT under AGENTS §Session Start:

1. Verify that positive evidence for the **same path's** Selection-mediated vertical reconstitution and relative nonreplaceability can be specified without defining One by its own output. Otherwise record **OPEN**, not a theorem.
2. For the **historical negative guard only**, retain controls for common input, ordinary path dependence, observer-driven segmentation and the unresolved replacement-scope ambiguity. Do **not** assert that a historically available replacement under a chosen perturbation envelope tests canonical 'arbitrary surrounding-field history'; no arbitrary rewiring or One-absence inference.
3. If a bounded Gate realization is separately selected, check whether FK/CK/MK evidence can actually be supplied rather than assumed, and whether any proposed U invariant survives type change and external ordinary control baselines.
4. Keep E2 algebra and experimental design with the currently active neutral cognition owner, not this One/Gate feasibility file. Do not initiate a new experiment, preregistration or formal domain claim from this review.

**Stop:** if no independently applicable separability admission condition emerges, end with **no nontrivial One theorem at current owner strength**, rather than manufacture one by adopting cycle/SCC, simple deletion effect, or a pre-given identity as a definition.

**Machine verification:** NOT RUN. F-01/F-02 are deliberately trivial toy-signature observations, F-03 rejects candidate shortcuts with model cases, F-04 is a proposed time-indexed recursive typed contract with missing independent evidentiary premises, and F-05 has been routed out of scope. Neither Lean build nor full repository preflight is claimed by this revision.

## 8. Review disposition / external-comparison three items

### Claude review disposition (author forwarded; no independent PASS claimed)

- **A1 operational source:** the bounded 2026-10-08 author GitHub continuation permits this noncanonical audit/revision; it does not authorize theoretical convergence or canonical hardening. No new research programme.
- **M1 / M2:** ACCEPT — F-01/F-02 downgraded to trivial syntactic results; One admission now typed over candidate paths; branch/merge-identity HOLD explicit.
- **M3:** ACCEPT — full input arguments restored; Bridge/Closure/Field candidate-to-admitted steps made evidence-dependent.
- **M4:** ACCEPT — removed rank lemma from core result set and documented dimensional, r, baseline, time-varying and H2 non-discrimination limitations as E2-only disposition.
- **R1 / R2 (follow-up review):** ACCEPT — C2 now uses a fixed memoryless-relay model instead of arbitrary rewiring; F-04 now includes prospective t+1 evidence, trial-only candidate use, Update_t feedback and explicit prohibition on self-evidencing admission.
- **Minor corrections:** ACCEPT — U1..U5 vs SC-1..SC-6 fixed; positive F-03 target corrected; C1 intervention dependence, real-change source guard, OPEN vs HOLD typing, branching formation supports, unqueued checks, and merged #1103 with still-pending internal post-Bearer adjudication clarified.

### 外部对照三项 (AGENTS §Constitution / Ontology Dialogue Hard Guard)

1. **事实冲突：** 无（本轮已核范围内未发现）。本审计不输入新的作者经验性陈述或经验数据。
2. **内部矛盾：** 无（本轮已核范围内未发现）。这次修复的是机器草稿与既有owner边界之间的问题，而不是互相矛盾的两项作者陈述。
3. **已有说法：**
   - F-01/F-02：模型论中用反模型判断逻辑蕴含/独立性的标准做法（Chang & Keisler, *Model Theory*, 3rd ed., 1990）；**完全相同**，没有新的One结果。
   - F-03（图论）：有向图强连通分量是标准图论对象（Tarjan, "Depth-First Search and Linear Graph Algorithms", 1972）；作为图算法**完全相同**，但将其等同One形成没有依据。
   - F-03（干预不等于构成）：Craver, *Explaining the Brain* (2007), ch. 4 §8.3 "Constitutive Relevance as Mutual Manipulability" (https://doi.org/10.1093/acprof:oso/9780199299317.003.0004)，以及 Woodward, *Making Things Happen* (2003/2004) (https://doi.org/10.1093/0195155270.001.0001)：**部分重合**；干预因果效应本身不等于One形成的充分性证据。两位作者均未提出SRT One准入。
   - F-03（相对可分离性邻居）：Moreno & Mossio, *Biological Autonomy* (2015), ch. 1 "Constraints and Organisational Closure" (https://doi.org/10.1007/978-94-017-9837-2)：**部分重合**。One owner已明确 relative separability != organizational closure，不能当作同义词。
   - F-04：证据携带的依赖对是标准依赖类型技术（Martin-Löf, *Intuitionistic Type Theory*, 1984），按时间分层的递归定义属于标准形式方法；**完全相同**的形式工具，尚无SRT机制新增。
   - F-05：乘积矩阵的秩上界为标准矩阵论（Horn & Johnson, *Matrix Analysis*, 2nd ed., 2013）；**完全相同**。E2低维实现与常见潜变量/系统辨识方法**部分重合**，且无SRT独有判别力。

**Final machine verdict:** at current One-owner strength, **only trivial syntactic non-entailments are available from the deliberately weak signature**. A substantive One result is blocked by independent positive *relative continuation separability* admission (F-03, OPEN); the revised Gate typed contract makes its own FK/CK/MK evidence obligations explicit but does not solve them. Leave Draft PR #1104 open for fresh review; do not merge solely on mechanical green checks.
