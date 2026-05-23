---
source_id: SRC-2026-05-20-PHYSICS-RAQM-DISCRETE-HILBERT-PALMER-IAI-PNAS
title: "New theory argues quantum physics must abandon irrational numbers and the continuum"
source_type: public_physics_essay_with_peer_reviewed_primary_paper_anchor
domain: Physics / Quantum foundations / Mathematical foundations / Quantum computing
url: https://iai.tv/articles/new-theory-argues-quantum-physics-must-abandon-irrational-numbers-and-the-continuum-auid-3580?_auid=2020
doi: 10.1073/pnas.2523350123
primary_paper_title: "Rational quantum mechanics: Testing quantum theory with quantum computers"
authors:
  - Tim Palmer
publication: IAI News; primary paper in Proceedings of the National Academy of Sciences
primary_publication: Proceedings of the National Academy of Sciences
primary_date_published_online: 2026-03-16
primary_date_published_print: 2026-03-24
iaI_date_published: 2026-05-20
date_added: 2026-05-22
evidence_level: secondary_public_essay_plus_peer_reviewed_primary_metadata_and_abstract
reliability_level: medium_high_for_source_identity_and_claim_outline; incomplete_for_full_theory_evaluation_without_PNAS_full_text
srt_relevance: finite-accessible-Hilbert-space pressure; counterfactual-definedness guardrail; Bell/nonlocality interpretation caution; quantum-computing discriminator candidate
integration_priority: B_watchlist_high_priority
related_srt_claims:
  - SRT-PHYSICS-CLAIM-STATUS
  - SRT-PHYS-P06-ACCESSIBLE-COUNTERFACTUAL-CLOSURE
  - SRT-OPEN-TENSIONS
  - SRT-SYMBOL-TABLE
tags:
  - rational_quantum_mechanics
  - Hilbert_space
  - continuum
  - rational_numbers
  - Bell
  - counterfactuals
  - quantum_computing
  - PNAS
  - IAI
canonical: false
claim_mode: evidence
---

# SourceCard: Tim Palmer / Rational Quantum Mechanics, discrete Hilbert-space constraints

## 1. One-line summary

Tim Palmer argues, in an IAI public essay anchored to a 2026 PNAS paper, that quantum theory should replace continuum Hilbert space with Rational Quantum Mechanics (RaQM), where rational-number constraints on quantum-state bases make some counterfactual measurement worlds ill-defined and imply a finite qubit information capacity that could cap quantum-computing advantage.

## 2. Core claims of source

- Standard quantum mechanics builds the quantum state as a vector in continuum Hilbert space; Palmer argues this imports irrational-number / continuum structure more strongly than classical physics needs.
- RaQM banishes the continuum from the relevant quantum-state formalism and uses discrete / rational-number constraints on admissible bases.
- In the public IAI essay, Palmer claims this makes quantum interpretation more comprehensible: Born's rule becomes emergent rather than axiomatic; Bell-type nonlocality is reframed by denying well-defined outcomes for some irrational counterfactual worlds rather than by denying experimenter free choice.
- The PNAS abstract states that RaQM does not modify the Schrödinger equation, even during measurement, but constrains the bases in which quantum states are defined.
- The PNAS abstract introduces finite qubit information capacity `N_max`: for sufficiently large `N`, available qubit information grows linearly while continuum quantum degrees of freedom grow exponentially.
- Palmer estimates `N_max` between roughly 200 and 400 for current qubit technologies and never above 1,000; algorithms requiring maximal `N`-qubit superposition/entanglement, such as Shor's algorithm, should saturate before breaking large RSA keys if RaQM is correct.

## 3. Evidence / method

- The user supplied the IAI News essay URL; the official IAI page was accessible and read.
- The IAI essay links to the peer-reviewed PNAS paper: Tim Palmer, "Rational quantum mechanics: Testing quantum theory with quantum computers," *Proceedings of the National Academy of Sciences* 123(12), e2523350123, DOI `10.1073/pnas.2523350123`.
- Crossref metadata and the PNAS abstract were read. Direct PNAS HTML/PDF access returned HTTP 403 in this environment, so this SourceCard does not claim full-paper close reading.
- Evidence status therefore remains: public essay plus peer-reviewed paper metadata/abstract, not full technical adjudication of RaQM.

## 4. Limits

- This source must not be used to claim that SRT proves discreteness, rational quantum mechanics, or a finite Hilbert-space ontology.
- The public essay is explanatory and argumentative; the technical burden sits in the PNAS paper, which was not fully close-read here.
- RaQM's Bell move should not be imported as an SRT claim that Bell experiments are wrong, that locality is restored in a standard sense, or that hidden variables are accepted by SRT.
- The quantum-computing prediction is a high-value discriminator candidate, not current evidence that quantum mechanics has failed.
- `Hilbert space` must remain a candidate physical projection / formal object, not be identified with SRT `L_0` or with `L0_accessible^phys`.

## 5. SRT relevance

Potential B-class interface:

- Finite-accessibility guardrail: SRT physics can use RaQM as a pressure case for distinguishing absolute latent possibility (`L_0`), physical projection `pi_phys(L0)`, and the actually enterable / payable physical possibility domain under current constraints.
- Counterfactual-definedness guardrail: Bell-style discussions should ask whether counterfactual alternatives are physically admissible / well-defined under the relevant projection, rather than assuming every mathematical counterfactual is automatically physically enterable.
- Continuum humility: continuum formalism may be an extraordinarily useful `L_2` mathematical scaffold without being automatically identical to physical ontology.
- Testability interface: the proposed saturation of quantum advantage beyond several hundred to one thousand error-corrected qubits is a rare clean discriminator for a foundations proposal, but it belongs to physics watchlist / lab-hypothesis tracking, not SRT core.

## 6. Suggested patch target

No immediate body patch.

Future possible targets after full PNAS close reading:

- `Physics/patches/SRT_Phys_P06_Accessible_Counterfactual_Closure_v0_1.md` as a cautious addendum or footnote-level comparison under Bell / counterfactual accessibility, if RaQM's technical construction survives close reading.
- `Physics/Extensions/SRT_Phys_E05_Falsifiability_Program.md` as a candidate discriminator example for quantum-computing-scale breakdown of standard quantum theory.
- `Physics/SRT_Physics_Claim_Status.md` as a guardrail note only if the physics domain starts citing RaQM, to prevent finite-Hilbert-space claims from being promoted to SRT primitives.

## 7. Do-not-import list

- Do not write: SRT entails RaQM.
- Do not write: quantum mechanics must abandon irrational numbers as an SRT conclusion.
- Do not write: Bell violations are explained away by SRT.
- Do not write: Shor's algorithm cannot work because SRT says so.
- Do not identify `L_0`, `pi_phys(L0)`, `L0_accessible^phys`, Hilbert space, and RaQM's finite information capacity with each other.
