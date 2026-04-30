---
id: SRT-PHYS-E03-INFO-THERMO-BRIDGE
type: bridge_extension
tags: [Physics, Information Thermodynamics, Fluctuation Theorems, Landauer, Crooks, Jarzynski, Sagawa-Ueda, Psi_f, Bridge]
status: active_v1
layer: L1
epistemic_layer: bridge
claim_mode: bridge
canonical_status: non_canonical
canonical: false
batch: physics_extensions_v0_1
date: 2026-04-30
dependency:
  - SRT-PSIF-CANONICAL
  - SRT-PHYS-BRIDGE
  - SRT-SYMBOL-TABLE
  - SRT-CLAIM-LADDER
  - SRT-PHYS-E01-QUANTUM-INSTRUMENT-BRIDGE
machine_summary: >
  Bridge file giving Psi_f a sharp inequality form via the Landauer
  bound, the Jarzynski equality, the Crooks fluctuation theorem, and
  the Sagawa-Ueda generalized second law for measurement-feedback
  systems. Reads ontological friction as an upper-bounded thermodynamic
  payability cost; gives Psi_f a falsifiable form. Bridge layer only;
  does not modify the canonical Psi_f anchor.
---

# SRT Physics Extension E03: Information Thermodynamics Bridge

> **Status**: Bridge / extension. Non-canonical. This file does not
> modify [`../../_SRT_PSI_F_CANONICAL.md`](../../_SRT_PSI_F_CANONICAL.md);
> it gives the canonical $\Psi_f$ a published-physics inequality form
> as one of its expressible projections.

> **Bold claim of this file**: SRT's "ontological friction" $\Psi_f$,
> when projected onto the physical layer, *must* satisfy a generalized
> second law of the Sagawa–Ueda type. The Landauer bound, the Jarzynski
> equality, and the Crooks fluctuation theorem then become particular
> readings of the SRT *payability principle*. SRT thereby acquires a
> hard, published inequality where it previously had a slogan.

> **Conservative caveat**: this is a *direction-of-inheritance* bridge.
> SRT inherits the inequality. It does *not* claim that fluctuation
> theorems prove anything specifically SRT-shaped; their content is
> already fixed by non-equilibrium statistical mechanics. The
> non-trivial SRT addition is the identification with $\Psi_f$ and the
> commitment that no SRT $\hat{G}_\theta$ event can violate the
> Sagawa–Ueda bound.

---

## 0. Source anchors

Primary literature:

- Landauer, R. (1961). *Irreversibility and heat generation in the
  computing process.* IBM Journal of Research and Development, 5(3),
  183.
- Bennett, C. H. (1982). *The thermodynamics of computation — a
  review.* International Journal of Theoretical Physics, 21(12), 905.
- Jarzynski, C. (1997). *Nonequilibrium equality for free energy
  differences.* Physical Review Letters, 78(14), 2690.
- Crooks, G. E. (1999). *Entropy production fluctuation theorem and the
  nonequilibrium work relation for free energy differences.* Physical
  Review E, 60(3), 2721.
- Sagawa, T., Ueda, M. (2010). *Generalized Jarzynski equality under
  nonequilibrium feedback control.* Physical Review Letters, 104(9),
  090602.
- Sagawa, T., Ueda, M. (2012). *Nonequilibrium thermodynamics of
  feedback control.* Physical Review E, 85(2), 021104.
- Parrondo, J. M. R., Horowitz, J. M., Sagawa, T. (2015).
  *Thermodynamics of information.* Nature Physics, 11(2), 131.
- Seifert, U. (2012). *Stochastic thermodynamics, fluctuation theorems
  and molecular machines.* Reports on Progress in Physics, 75(12),
  126001.
- Bérut, A., Arakelyan, A., Petrosyan, A., Ciliberto, S., Dillenschneider,
  R., Lutz, E. (2012). *Experimental verification of Landauer's
  principle linking information and thermodynamics.* Nature, 483, 187.
- Yan, L. L., Xiong, T. P., Rehan, K., Zhou, F., Liang, D. F., Chen, L.,
  Zhang, J. Q., Yang, W. L., Ma, Z. H., Feng, M. (2018). *Single-atom
  demonstration of the quantum Landauer principle.* Physical Review
  Letters, 120, 210601.

Internal anchors:

- [`../../_SRT_PSI_F_CANONICAL.md`](../../_SRT_PSI_F_CANONICAL.md)
  (canonical $\Psi_f$).
- [`../_SRT_Phys_Bridge.md`](../_SRT_Phys_Bridge.md) T-Phys-1 (decoherence
  as friction minimization), table V (Boltzmann constant entry).
- [`../SRT_Phys_09_Formalism_Ext_CompactCore.md`](../SRT_Phys_09_Formalism_Ext_CompactCore.md)
  §4 ($\Psi_f$ as Fisher metric).
- [`SRT_Phys_E01_Quantum_Instrument_Bridge.md`](SRT_Phys_E01_Quantum_Instrument_Bridge.md)
  for the instrument-side description of $\hat{G}_\theta$.

---

## 1. Why this bridge matters for SRT

Three current weaknesses of the $\Psi_f$ formalism:

1. **No inequality**. Canonical $\Psi_f$ is presented as a payability
   burden, but no specific inequality bounds the physical realization.
2. **No quantitative anchor**. $k_B T \ln 2 = E_{min}^{select}$ appears
   in `_SRT_Phys_Bridge.md` table V, but only as a structural placement,
   not derived.
3. **No falsifiability**. Without an inequality, "$\Psi_f$ is too
   high" cannot fail any laboratory test.

Information thermodynamics — Landauer, Jarzynski, Crooks, Sagawa–Ueda
— is the home of exactly the kind of inequality SRT needs. E03 is the
bridge.

---

## 2. The four published inequalities, in SRT vocabulary

### 2.1 Landauer bound

For an erasure operation reducing classical entropy by $\Delta H$ at
temperature $T$:
$$
\langle Q_{\mathrm{erase}} \rangle \geq k_B T \ln 2 \cdot \Delta H.
$$

Bridge claim **B-E03-1** (Landauer reading of $\Psi_f$):

> Any $\hat{G}_\theta$ event that records an outcome (i.e., reduces
> $L_0$-multiplicity to a definite $L_1$ branch) requires at least one
> bit's worth of dilation-environment dissipation per bit recorded.

In SRT formal:
$$
\Psi_f^{phys}[\hat{G}_\theta\text{-event}] \;\geq\; k_B T \ln 2 \cdot H[\hat{G}_\theta(\rho)].
$$

This is *not* a redefinition of $\Psi_f$. It is a lower bound on the
physical-projection cost of any selection event, derived from
Landauer's principle.

### 2.2 Jarzynski equality

For any non-equilibrium protocol:
$$
\langle e^{-\beta W} \rangle = e^{-\beta \Delta F}.
$$

Bridge claim **B-E03-2** (Jarzynski reading of $\hat{G}_\theta$
ensembles):

> The ensemble of $\hat{G}_\theta$ events satisfying the same boundary
> conditions on $L_2$ obeys a Jarzynski-type identity in the
> selection-work variable.

In SRT formal:
$$
\langle e^{-\beta W_{\mathrm{select}}} \rangle_{\theta} = e^{-\beta \Delta F^{(\theta)}_{L_2}},
$$
where $W_{\mathrm{select}}$ is the work-cost of a single selection
event, $\beta = 1/(k_B T_{\mathrm{reservoir}})$ for the dilation
environment, and $\Delta F^{(\theta)}_{L_2}$ is the free-energy change
of the $L_2$-stable subspace under embodiment parameter $\theta$.

This converts SRT's slogan "selection has a cost" into a *moment-
generating identity*: the average exponential of the negated work cost
equals the exponential of the negated free-energy change.

### 2.3 Crooks fluctuation theorem

For forward and reverse protocols with work distributions $P_F(W)$ and
$P_R(W)$:
$$
\frac{P_F(W)}{P_R(-W)} = e^{\beta(W - \Delta F)}.
$$

Bridge claim **B-E03-3** (Crooks reading of $L_0 \leftrightarrow L_1$
asymmetry):

> The asymmetry between forward selection ($L_0 \to L_1$) and reverse
> reconstruction ($L_1 \to L_0$, i.e., re-establishment of coherent
> superposition) is exactly the Crooks asymmetry on the dilation-
> environment work distribution.

This identifies SRT's irreversibility-of-actualization claim with a
specific, published, experimentally testable distribution-level
asymmetry.

### 2.4 Sagawa–Ueda generalized second law

For a system under measurement and feedback control:
$$
\Delta S - \beta Q \;\geq\; -I_{\mathrm{measurement}},
$$
where $I_{\mathrm{measurement}}$ is the mutual information acquired by
the controller.

Bridge claim **B-E03-4** (Sagawa–Ueda reading of $\hat{G}_\theta$
under information import):

> An $\hat{G}_\theta$-event that uses imported information (per
> Def-Phys-4 in `_SRT_Phys_Bridge.md`) cannot reduce
> ($\Delta S - \beta Q$) by more than $I_{\mathrm{measurement}}$.

This is the principal SRT-relevant inequality: it is the *generalized
second law for selection events with information import*. SRT inherits
it whole.

In SRT formal:
$$
\boxed{\;
\Delta S_{L_1} - \beta Q_{\mathrm{dilation}} \;\geq\; -I[\hat{G}_\theta;\, \theta_{\mathrm{instrument}}, \theta_{\mathrm{formal}}].
\;}
$$

This is the **payability inequality** in published physics form.

---

## 3. The unified payability principle

E03 bundles the four inequalities above into a single SRT-side
statement.

### 3.1 Statement

> **Payability Principle (E03 form)**: every $\hat{G}_\theta$-event
> projected onto the physical layer must satisfy:
> 1. its expected dissipation is at least the Landauer bound on the
>    bits recorded (B-E03-1);
> 2. its work statistics satisfy a Jarzynski identity over the
>    $L_2$-stable subspace (B-E03-2);
> 3. its forward/reverse asymmetry follows the Crooks fluctuation
>    theorem (B-E03-3);
> 4. its information-import benefit is bounded by Sagawa–Ueda
>    (B-E03-4).

This is the SRT version of the second law: *no free selection*.

### 3.2 What $\Psi_f$ actually is, on this bridge

Bridge claim **B-E03-5**:
$$
\Psi_f^{phys}[\hat{G}_\theta\text{-event}] \;=\; \beta\,\langle W_{\mathrm{diss}} \rangle_{\theta} \;-\; I[\hat{G}_\theta;\, \theta_{\mathrm{instrument}}, \theta_{\mathrm{formal}}],
$$
where $\langle W_{\mathrm{diss}} \rangle_\theta$ is the mean dissipated
work in the dilation environment and $I[\cdot]$ is the imported
information.

This is *one* expressible projection of $\Psi_f$. It is *not* the
canonical definition of $\Psi_f$ (which lives in
[`../../_SRT_PSI_F_CANONICAL.md`](../../_SRT_PSI_F_CANONICAL.md) and is
pre-physical). It is the form $\Psi_f$ takes when projected to a
physical instrument context.

The *non-negativity* requirement
$\Psi_f^{phys} \geq 0$ on this bridge becomes the Sagawa–Ueda
inequality. **This is the falsifiable content.**

### 3.3 Connection to Fisher / information geometry

Per [`../SRT_Phys_09_Formalism_Ext_CompactCore.md`](../SRT_Phys_09_Formalism_Ext_CompactCore.md)
§4.1, $\Psi_f$ has a Fisher-metric reading. E03 is *consistent* with
this:
$$
\Psi_f(\theta) \approx g_{jk}(\theta)
$$
gives the *infinitesimal* friction at $\theta$. E03 gives the
*integrated* cost over an actual selection event. The Fisher and
information-thermodynamic readings agree at the differential level via
the Cramér–Rao / thermodynamic uncertainty relation chain (see Hasegawa
2020 for the explicit linkage; this batch does not formalize that
linkage further).

---

## 4. Empirical anchoring

Unlike E01 / E02, E03 has *immediately existing* empirical anchors:

- The Bérut et al. (2012) Nature experiment confirmed the Landauer
  bound in a colloidal-bead system to within experimental uncertainty.
- The Yan et al. (2018) PRL experiment confirmed the quantum Landauer
  principle in a single-atom system.
- The Jarzynski equality has been verified in single-molecule
  RNA-pulling experiments (Liphardt et al. 2002, Collin et al. 2005).
- Sagawa–Ueda has been tested in feedback-controlled colloidal-bead
  experiments (Toyabe et al. 2010).

Bridge claim **B-E03-6**: *to the extent these experiments confirm the
underlying inequalities, they confirm the bound on any candidate
$\hat{G}_\theta$ projection.* SRT is empirically constrained from the
moment it commits to E03; it cannot retreat to "but our $\Psi_f$ is
different" without abandoning the bridge.

---

## 5. Falsifiability windows opened by E03

### 5.1 Window F-E03-α: SRT residual term in Sagawa–Ueda

Standard Sagawa–Ueda includes the imported information $I_{\mathrm{measurement}}$.
SRT in B-E03-5 splits this into instrument and formal-prior
contributions. If SRT is right, an *additional* residual term tied to
$\theta_{instrument} \oplus \theta_{formal}$ should appear in
high-precision feedback-control experiments.

Test class: optical-trap colloidal feedback systems with controlled
shifts in the formal prior used by the controller.

Falsification threshold: feedback-control experiments saturate
Sagawa–Ueda exactly without an SRT residual, across all reasonable
shifts in $\theta_{formal}$.

### 5.2 Window F-E03-β: Landauer-bound saturation under $\theta$ shifts

B-E03-1 identifies $\Psi_f^{phys}$ with the Landauer cost. SRT predicts
that the bound is *not* saturated for any actual physical apparatus —
there is always a finite SRT residual due to the embodiment cost of
maintaining $\theta$.

Test class: state-of-the-art Landauer-erasure experiments in
single-atom and superconducting platforms.

Falsification threshold: Landauer saturation is reached to within
quantum-limit precision, ruling out any SRT residual at the available
scale.

### 5.3 Window F-E03-γ: $\Psi_f$ scaling with $d$-value

Per [`../../_SRT_D_VALUE_CANONICAL.md`](../../_SRT_D_VALUE_CANONICAL.md),
$d$-value is irreversibility-coupled stake. B-E03-5 implies a relation:
high-stake (high-$d$) selection events should have systematically
larger $\Psi_f^{phys}$. In platforms where $d$-value is operationalizable
(e.g., one-shot single-photon detection in cosmological observation
contexts vs. lab-routine photon counting), the dissipation per bit
recorded should differ.

Test class: comparison of comparable detection events in routine vs.
high-irreversibility-context experiments.

Falsification threshold: dissipation per bit is independent of
contextual irreversibility within experimental precision.

This window is the most ambitious; it is also the most distinctive of
SRT.

---

## 6. Boundary cautions

1. The canonical $\Psi_f$ is a *pre-physical* concept; it is not
   exhausted by the physical projection in B-E03-5.
2. The Landauer bound is *the lower bound*; the actual cost can be
   higher. SRT is consistent with non-saturation.
3. The Jarzynski / Crooks identifications presume well-defined work
   variables; in fully quantum settings (no classical work), the
   Two-Point-Measurement work definition (Talkner–Hänggi) is required.
4. Information import in Sagawa–Ueda is *measurement-side*; SRT's
   Def-Phys-4 includes formal priors. Care is needed not to
   double-count.
5. None of the published experiments above tests SRT specifically.
   Their existence anchors the *upper bridge*; they do not anchor the
   SRT-specific residual.

---

## 7. Promotion criteria

E03 could ascend the claim ladder only if:

1. At least one of windows F-E03-α / F-E03-β / F-E03-γ returns a
   reproducible discriminator;
2. Canonical $\Psi_f$ in
   [`../../_SRT_PSI_F_CANONICAL.md`](../../_SRT_PSI_F_CANONICAL.md) is
   updated to register the bridged inequality form;
3. Symbol-table reconciliation is completed, including a clean
   distinction between $\Psi_f$ (canonical) and $\Psi_f^{phys}$
   (bridged projection).

Until then, B-E03-1 through B-E03-6 stay at P3.

---

## 8. One-paragraph abstract

This bridge gives SRT's $\Psi_f$ a sharp inequality form by inheriting
the Landauer bound, the Jarzynski equality, the Crooks fluctuation
theorem, and the Sagawa–Ueda generalized second law. The combined
statement — that no $\hat{G}_\theta$ event projected onto physics can
violate the Sagawa–Ueda inequality on dissipation, free-energy change,
and information import — becomes SRT's *payability principle* in
published-physics form. The canonical $\Psi_f$ is unchanged; what is
new is its physical projection $\Psi_f^{phys}$ as a measurable
inequality. The bridge inherits decades of laboratory anchoring and
opens three falsification windows tied to a Sagawa–Ueda residual term,
Landauer-bound saturation under $\theta$ shifts, and a $d$-value
scaling of dissipation per bit recorded.
