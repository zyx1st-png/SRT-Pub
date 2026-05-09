---
patch_id: PATCH-NEURO-CONSC14-PROPOFOL-TRAVELING-WAVE-REORGANIZATION
source_ids:
  - SRC-2026-05-08-NEURO-PROPOFOL-TRAVELING-WAVES-BIORXIV
domain: neuroscience_consciousness
claim_level: bridge
canonical_status: domain_bridge_integrated
status: patch
target_document: "Neuroscience/SRT_Consciousness_Mechanisms.md"
related_claims:
  - traveling_wave_routing
  - wave_ignition_coupling
  - propofol_anesthesia
  - D_align
  - C_wave
  - P_ignite
  - loss_of_responsiveness
tags:
  - propofol
  - traveling_waves
  - anesthesia
  - consciousness
  - spike_wave_coupling
---

# SRT Neuroscience Patch CONSC14: Propofol Traveling-Wave Reorganization v0.1

> Status: consciousness-mechanism bridge patch.  
> Canonical caution: this patch does not define consciousness. It refines an existing traveling-wave routing proxy under propofol loss-of-responsiveness.

## 0. Source anchor

Primary source:

- V. M. Zarr, T. S. Davis, E. H. Smith, B. Greger, Z. W. Davis, and P. A. House. (2026). "Propofol-induced loss of responsiveness reorganizes cortical traveling waves in the human brain." bioRxiv preprint, version 1. DOI: `10.64898/2026.04.30.721975`.

Local processing used official bioRxiv API metadata and abstract. Direct HTML, PDF, and JATS XML access was blocked by Cloudflare, so this patch is intentionally limited to abstract-level claims.

---

## 1. Why this matters for SRT

SRT already models cortical traveling waves as a directional routing field:

```text
R_wave = grad(phi) · n_hier
```

and links wave dynamics to ignition probability:

```text
P_ignite = sigma(alpha C_wave + beta(Phi*d) + gamma D_align - delta)
```

The preprint adds a useful constraint: propofol loss of responsiveness may reorganize traveling waves rather than simply suppress them. A state can therefore fail reportable ignition through misrouting, retuning, or spike-wave decoupling, not only through a monotonic loss of power or coherence.

---

## 2. Main SRT bridge claim

### Claim CONSC14

Under propofol, loss of responsiveness may correspond to a wave-routing reorganization window:

```text
propofol LOR
  -> wave speed / direction / spectrum / spike-wave coupling changes
  -> D_align and C_wave no longer support task-relevant L0 -> L1 routing
  -> P_ignite falls despite preserved or faster traveling-wave propagation
```

This is a bridge hypothesis, not a new primitive. The SRT point is narrow:

```text
faster wave propagation != healthier conscious routing
```

---

## 3. Mapping table

| Source-level result | SRT interpretation | Guardrail |
|---|---|---|
| increased propagation speed under propofol | speed is separable from conscious routing quality | speed is not `P_ignite` |
| shifted propagation directions | `D_align` can fail through route retuning | direction shift is not automatically unconsciousness |
| altered spectral structure | `C_wave` must be frequency-contextual | do not reduce to total power |
| changed firing activity | neuronal participation in the routing field changes | abstract-only; no cell-type claim |
| changed spike-wave relationships | mesoscale waves and neuronal firing must be modeled together | not proof of a unique causal mechanism |

---

## 4. Formal bridge

Existing SRT formula:

```text
P_ignite = sigma(alpha C_wave + beta(Phi*d) + gamma D_align - delta)
```

Patch-level refinement:

```text
C_wave := C_wave(freq, region, state)
D_align := align(direction_wave, route_task, state)
K_spike-wave := coupling(firing_activity, wave_phase, state)

P_ignite^propofol
  = sigma(alpha C_wave + beta(Phi*d) + gamma D_align + zeta K_spike-wave - delta_state)
```

This is not proposed as a new canonical equation. It is an experimental bridge expansion showing which variables should not be collapsed when studying anesthesia.

---

## 5. New claim cluster

1. Propofol loss of responsiveness can be modeled as routing-field reorganization.
2. Traveling-wave speed is not sufficient evidence for preserved conscious routing.
3. Direction and spectral structure should be treated as independent explanatory variables.
4. Spike-wave coupling gives a cross-scale constraint on wave-ignition models.
5. Human intracranial traveling-wave evidence should be kept separate from macaque cross-anesthetic destabilization evidence, but the two can converge on a broader state-transition picture.

---

## 6. Experimental / operational consequences

This patch adds a focused prediction:

```text
H-C14:
In propofol loss-of-responsiveness, wave direction, spectral structure,
and spike-wave coupling should add predictive value over total power
or propagation speed alone when modeling reportability loss and recovery.
```

Minimum falsification handle:

```text
If loss of responsiveness is fully explained by monotonic power/coherence
reduction, and direction/spectrum/spike-wave terms add no predictive value,
then the wave-routing reorganization window should be downgraded.
```

---

## 7. Boundary cautions

- Do not write "consciousness is traveling waves."
- Do not write "propofol increases wave speed, therefore consciousness is preserved."
- Do not treat a bioRxiv preprint as clinical monitoring consensus.
- Do not generalize from two male temporal-lobe recordings to whole-brain anesthesia.
- Do not merge this with all anesthetic mechanisms; propofol, ketamine, dexmedetomidine, sleep, coma, and seizure states need separate state-space handling.

---

## 8. Integration status

Integrated as:

```text
Neuroscience/SRT_Consciousness_Mechanisms.md
  -> 2.8a Propofol Traveling-Wave Reorganization Window
  -> H-C14 Propofol Wave-Routing Reorganization
```

Future synthesis should compress this patch into a state-transition subsection rather than expanding it into a standalone theory of consciousness.

