# Response to Reviewers

**Manuscript ID:** 1837760
**Title:** A Translational Cross-Modal Control-Cost Framework for Executive Breakdown
**Article type:** Hypothesis and Theory — *Frontiers in Neuroscience* (Translational Neuroscience)

We thank both reviewers for their careful and constructive reading. The comments have substantially improved the manuscript's clarity and its grounding in the literature. Below we respond to each point individually. Reviewer comments are in *italics*; our response and the location of the change follow. All line/section references are to the revised manuscript.

## Summary of major changes

1. **Accessibility.** The Abstract and the Introduction (especially §1.3) were rewritten to lead with plain-language explanation before any formal terminology. Specialized phrases flagged by the reviewers ("latent cross-modal control-cost factor," "information-geometric deviation," "hazard-family function," "bandwidth-saturation event") were removed from the Abstract or replaced with accessible wording.
2. **Situating the contribution.** §1.1 now places the knowing–doing gap within the existing literature (the intention–behavior gap and implementation intentions; transdiagnostic executive-dysfunction work) and states explicitly what is, and is not, novel here. Six recent references were added.
3. **Exposition of the formal model.** Each Definition now opens with a plain-language conceptual introduction and closes with an intuition summary. The Definition 1A vs. 1B distinction is made explicit, all variables (including the noise term) are defined, and the two mechanistic interpretations are explained *as they are introduced*.
4. **Clinical section.** The newly introduced variables (switching viscosity, anchoring index) are now tied back to previously defined quantities, and the overlap between disorders (e.g., switching deficits in both OCD and MDD) is discussed openly and added to the Limitations.
5. **Prose quality and AI-assistance concerns.** The manuscript was reflowed to reduce fragmentation and markedly reduce em-dash usage (from 40 spaced em-dashes to a handful, all in citations or table cells). The Conflict-of-Interest and Generative-AI statements were expanded for transparency.
6. **Figures.** Figure source was corrected: numbering, accessible titles, larger fonts, black (not grey) text, removal of a disconnected equation, and removal of legacy labels. See the Figures section below.
7. **Statistical review.** Because both reviewers indicated that a statistician may be needed, the statistical modeling plan and sensitivity analyses have been clarified, and statistical consultation will be sought before preregistration and empirical implementation.

---

## Reviewer 1

**1. General — density/clarity.** *The writing is often dense and difficult to follow, which sometimes obscured the core conceptual contributions.*
Response: We restructured for accessibility throughout, most heavily in the Abstract, §1.3, and Section 2, following the specific suggestions below.

**2. Abstract — too many specialized terms.**
Response: The Abstract was rewritten to be readable outside the field. It now opens "Across neurological and neuropsychiatric conditions, patients often know what they should do yet cannot bring themselves to do it," and states the collapse condition in the reviewer's own accessible form ("executive collapse as the point at which control demands outstrip available capacity"). "Hazard-family function," "information-geometric deviation," and "bandwidth-saturation event" no longer appear in the Abstract.

**3. Introduction — situate the knowing–doing gap in the literature; add references (e.g., Wieber et al., 2015); note if underrepresented.**
Response: A new paragraph in §1.1 situates the phenomenon in the intention–behavior gap and implementation-intention literatures (Gollwitzer, 1999; Wieber et al., 2015) and in transdiagnostic clinical work (Gillan et al., 2016; Snyder et al., 2015; McTeague et al., 2017). It states explicitly that "the gap itself is not a new observation" and that what is underrepresented is "a single, formally defined, measurable *quantity*" tying the descriptions together.

**4. Introduction — executive-function references are dated.**
Response: Recent references added, including Friedman and Robbins (2022), Snyder et al. (2015), McTeague et al. (2017), and Gillan et al. (2016).

**5. Introduction — clarify which aspects of the gap existing frameworks address and how the proposal relates.**
Response: §1.2 now opens by stating that each framework "names a real piece" of the gap but lacks a cross-modal cost quantity, and reviews each "noting… what it captures and what it leaves out." The revised paragraph now states that the framework connects selected cost-related aspects of these accounts rather than competing with or replacing them, forward-referencing §6.2.

**6. Contribution and Scope (§1.3) — rewrite; introduce intuition before terminology.**
Response: §1.3 now opens with a plain-language paragraph closely following the reviewer's suggested framing ("this work proposes… that turning knowledge into action has a cost, which we call executive friction, and that when this cost grows too high, three things follow…"), before the formal paragraph.

**7. Section 2 — Definition 1A vs. 1B distinction unclear.**
Response: §2.2 now states the distinction up front: "Definition 1A specifies how Ψ_f is estimated from observable data… Definition 1B offers candidate mechanistic interpretations… none of them is required in order to estimate Ψ_f." Each definition header repeats its role.

**8. Section 2 — underexplained variables (e.g., the noise term).**
Response: All symbols in Eq. (3b) are now defined, including ξ(t) ("a zero-mean stochastic noise term representing intrinsic neural and measurement variability, e.g., a Wiener increment"), along with x(t), f_θ, B_θ, and the baseline-drift trajectory.

**9. Section 2 — explain the two mechanistic interpretations (3c ≈ accumulated effort; 3d ≈ deviation from default) while introducing them.**
Response: The intuitions are now given at the point of introduction: (3c) "reads friction as accumulated control effort… how hard the controller has to push," and (3d) "reads friction… as departure from the habitual default policy." A closing sentence contrasts them: "(3c) charges for how much force the controller applies, whereas (3d) charges for how far the chosen policy strays from habit."

**10. Section 2 — add conceptual intros to each Definition and plain-language summaries after equations.**
Response: Definition 2 now opens "Definitions 1A and 1B specify executive friction itself. We now turn to the *distress* that accompanies it, which is a separate quantity," and explains the hazard function in words. Definition 3 opens with an accounting intuition ("an agent has a finite control budget, friction and noise draw on it…"). Existing plain-language summaries after Eqs. (4) and (5) were retained.

**11. §2.4 — clarify the relevance of relating to the Free Energy Principle.**
Response: §2.4 now opens by answering "Why relate the proposal to the Free Energy Principle at all?" with two explicit reasons (demonstrating Ψ_f is a recognizable generalization of an established cost, and sharpening exactly where the clinically load-bearing departure lies).

**12. §2.5 — operational definition of response-error entropy; explain critical points.**
Response: Response-error entropy is now defined operationally (sliding window of w trials → outcome-category probabilities → Shannon entropy H = −Σ p log p), with interpretation. The critical point is now explained as the value of "how close friction has come to exhausting control capacity" at which behavior changes character, with both the ratio (Eq. 7a) and difference (Eq. 7c) forms explained in words.

**13. Minor — SEM/CFA and LOO/WAIC spelled out at first use.**
Response: Done (§2.2 and the mechanism-comparison paragraph). A comprehensive Abbreviations list was also added.

**14. Minor — missing equation labels (e.g., 3c).**
Response: Equation labels were checked throughout; (3c), (3d), (3d'), and the Eq. (9)/§3.2 label are present and consistent.

**15. §3 minor — spell out GSH/GSSG, ICC, CFI, RMSEA at first use.**
Response: Done: reduced-to-oxidized glutathione ratio (GSH/GSSG), intraclass correlation coefficient (ICC), comparative fit index (CFI), root mean square error of approximation (RMSEA); also MDA and 8-OHdG.

**16. §4 — new variables (viscosity, anchoring index) not tied to prior definitions.**
Response: §4.2 now states that switching viscosity η "is not a new parameter but the same viscosity introduced behaviorally in Section 3.1," where η ∝ ∂Ψ_f/∂θ. §4.3 now states that the anchoring index's denominator "is simply the action-initiation friction Ψ_f^action from the knowing–doing inequality (Eq. 7) applied to the motor domain."

**17. §4 — OCD vs. MDD overlap on switching; discuss in Limitations.**
Response: §4.2 now explicitly acknowledges that "depression also impairs task-switching, so the two conditions overlap on any single switching measure," and clarifies that the differentiating claim rests on the multivariate profile. A dedicated Limitation (§6.3, "Eighth") discusses this boundary ambiguity as "a real risk to the account."

**18. §5.5 — distinguish OCD > controls from OCD > MDD.**
Response: The prediction now separates the two inequalities explicitly: OCD > controls is "the weaker, more general claim that friction leaves a constraint-modal signature at all," whereas OCD > MDD is "the stronger and genuinely disorder-differentiating claim." The falsification criterion now rejects at two levels accordingly (weak-form failure vs. loss of the disorder-specific claim, retaining μ_sem as a transdiagnostic index).

**19. §5 minor — spell out SCID-5 and SSRI/SNRI at first use.**
Response: Done in §5.4.

**20. §6 Limitations — discuss the indirect nature of the proxies and implications for construct validity.**
Response: A dedicated Limitation (§6.3, "Seventh") now states that "every proxy proposed here is indirect… construct validity cannot be settled by any single indicator and rests entirely on convergence," and frames demonstrating convergence as "the central empirical burden of the program rather than a settled premise."

**21. Figures — numbering error (ROS shown as Fig 1 should be Fig 3; proxy signatures Fig 3 → Fig 4; architecture Fig 4 → Fig 1).**
Response: Confirmed and corrected. The mismatch arose because the uploaded figure image files were bound in the wrong order relative to the manuscript. Numbering is now: **Figure 1** hierarchical control architecture, **Figure 2** cross-modal operationalization map, **Figure 3** ROS–Ψ_f coupling, **Figure 4** predicted proxy signatures, **Figure 5** core-chain protocol. Figure files are re-exported to match.

**22. Figure (ROS coupling) — too many technical terms; more accessible title; larger fonts; clearer feedback loop; remove disconnected bottom equation.**
Response: Title changed to "Proposed Oxidative Feedback Loop: How Sustained Executive Friction May Drive Clinical Decline." Legacy symbols removed. Fonts enlarged and text set to black. The disconnected bottom equation was removed (Eq. 9 remains in the text). The positive-feedback arrow is retained as the salient dashed loop.

**23. Minor figure notes — architecture-figure equation overlaps the second legend; Figure 5 study-design box too small / too many abbreviations.**
Response: The study-design box font was enlarged; the architecture panel layout was adjusted so the budget equation does not overlap the legend; abbreviation density in the protocol figure was reduced (e.g., cortisol marked optional to match the text).

---

## Reviewer 2

**1. Generative-AI concerns; em-dash overuse; style inconsistent with author guidelines.**
Response: The manuscript was thoroughly reflowed. Em-dash usage was cut from 40 spaced em-dashes to a small number confined to citation titles and "not applicable" table cells; short fragmented passages were merged into connected paragraphs with topic sentences and transitions. We have re-checked formatting against the *Frontiers* author guidelines. We note that AI assistance was limited to language editing of author-specified content and is disclosed transparently (see below); the intellectual content, model, hypotheses, and every claim are the author's own and were independently verified.

**2. Affiliation / conflict of interest — author is "independent researcher" with no further information, preventing COI assessment.**
Response: The author information was completed to support this assessment. The affiliation now reads "Independent Researcher, Kaili, Guizhou, China," with a correspondence email and an ORCID identifier (0009-0007-6659-8518). The Conflict-of-Interest statement was expanded to make the independent status transparent and assessable: it states that the author has no employment, consultancy, patent, equity, grant, or other financial relationship with any organization that could benefit from the framework, and clarifies that the single self-citation (Appendix A) is non-commercial, confers no financial interest, and is not required for any claim in the paper.

**3. Writing — short paragraphs, poor flow, reads like disorganized bullet points; needs substantial rewriting.**
Response: Addressed as part of the reflow described above and the section-level rewrites requested by Reviewer 1 (Abstract, §1.3, all of Section 2). Run-in emphasis and choppy passages were consolidated into flowing prose.

**4. Rewrite absent of AI use.**
Response: We have revised the manuscript ourselves and take full responsibility for it. Per journal policy and in the interest of transparency, we retain an honest disclosure of AI-assisted language editing rather than removing it. The disclosure now states that AI assistance was limited to language editing and structural clarity, and that the author developed and verified the framework, equations, hypotheses, references, and final content. The strengthened prose (in particular the corrected em-dash usage and paragraph structure) reflects author revision throughout.

**5. Figures — grey text in color-box charts should be black.**
Response: Done. Text in the box/flow figures was changed from grey to near-black across the figure sources.


---

## Reviewer 1 — Follow-up Minor Comments

**1. Reviewer comment:** *In Table 2, please indicate in the caption what the bold font with a cross denotes.*
Response: Thank you for pointing this out. The caption of Table 2 now clarifies that bold entries marked with the dagger symbol (†) denote the primary disorder-discriminating predictions used in the paired dissociation tests.

**2. Reviewer comment:** *In Table 3, please correct "30$3" (it should be "30³", i.e., 30 raised to the power of 3).*
Response: Thank you for identifying this rendering error. The intended notation referred to three groups of 30 participants, for a total sample size of 90, rather than a mathematical exponent. To eliminate ambiguity and prevent further rendering problems, Table 3 now states “90 (three groups of 30 participants).”

---

We believe these revisions address the reviewers' concerns and materially strengthen the manuscript, and we thank the reviewers again for their time.
