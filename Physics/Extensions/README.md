---
id: SRT-PHYSICS-EXTENSIONS-INDEX
type: index
tags: [Physics, Extensions, Bridge, Navigation, Quantum Foundations, Information Thermodynamics, Falsifiability]
status: active_v1
layer: meta
epistemic_layer: bridge
claim_mode: navigation
canonical_status: non_canonical
canonical: false
batch: physics_extensions_v0_1
date: 2026-04-30
dependency:
  - SRT-PHYSICS-COMPACT-REGISTRY
  - SRT-PHYS-BRIDGE
  - SRT-PSIF-CANONICAL
  - SRT-D-VALUE-CANONICAL
  - SRT-T-DIR-CANONICAL
  - SRT-SYMBOL-TABLE
  - SRT-CLAIM-LADDER
machine_summary: >
  Index for the v0.1 Physics Extensions batch. Five bridge files give SRT's
  physical primitives (G_hat_theta, theta_boundary, Psi_f, manifest time)
  formal homes in published quantum-foundations / information-thermodynamics
  literature, plus a Lakatos-style falsifiability program. All files are
  bridge layer, non-canonical, and route definitions back to canonical
  anchors.
---

# SRT Physics Extensions v0.1

> **Metadata cleanup note（2026-05）**：frontmatter 的 `claim_mode: navigation` / `canonical: false` 表示本目录只是阅读切片或 interface layer；历史正文中的 axiom/theorem/canonical/physics-law 句式必须回读 `../SRT_Physics_Claim_Status.md`。
> **Status**: bridge / extension batch. Non-canonical. Each file routes back
> to canonical anchors and to the existing `_SRT_Phys_Bridge.md`.

> **Purpose**: tighten the physics section by giving SRT's physical
> primitives mathematical homes in published quantum-foundations and
> non-equilibrium statistical-mechanics literature, and by stating a
> Lakatos-style falsifiability program with hard near-term thresholds.

> **Editing class**: per
> [`../../Governance/SRT_EDIT_PROTOCOL.md`](../../Governance/SRT_EDIT_PROTOCOL.md)
> this batch is treated as **B-class** (compact-core / bridge tightening).
> No file in this batch modifies a canonical anchor or the L0/L1/L2,
> `\hat{G}_\theta`, `\Psi_f`, `d`, or `T_dir` definitions.

---

## 1. Why this batch exists

The current physics section has three structural weaknesses:

1. **Formal thinness of `\hat{G}_\theta`**. Def-Phys-1 names the selection
   operator as a POVM / instrument, but does not anchor it in the
   Gorini-Kossakowski-Lindblad-Sudarshan (GKLS) formalism that physicists
   routinely use for non-unitary evolution.
2. **Underspecification of `\theta`**. The embodiment parameter is split
   into `\theta_{basis}`, `\theta_{boundary}`, `\theta_{H_{int}}`, but
   without a published mathematical formalism this triple risks reading as
   philosophy rather than physics.
3. **Soft falsifiability**. `_SRT_Phys_Bridge.md` §VI lists domain
   pressures, but no consolidated, threshold-based falsification program
   exists.

This batch closes these three gaps with five bridge files. None of them
ascends a hypothesis to a theorem, redefines a primitive, or claims
empirical victory.

---

## 2. File map

| File | Bridge target | Role |
|---|---|---|
| [`SRT_Phys_E01_Quantum_Instrument_Bridge.md`](SRT_Phys_E01_Quantum_Instrument_Bridge.md) | GKLS / Davies–Lewis quantum instruments / Stinespring dilation | Gives `\hat{G}_\theta` a textbook home as a CPTP-instrument family |
| [`SRT_Phys_E02_Quantum_Reference_Frames_Bridge.md`](SRT_Phys_E02_Quantum_Reference_Frames_Bridge.md) | Giacomini–Castro-Ruiz–Brukner quantum reference frames (2019) | Gives `\theta_{boundary}` a QRF-compatible projection |
| [`SRT_Phys_E03_Information_Thermodynamics_Bridge.md`](SRT_Phys_E03_Information_Thermodynamics_Bridge.md) | Landauer / Jarzynski / Crooks / Sagawa–Ueda | Gives `\Psi_f` a scoped `\sigma_f^{phys}` proxy via fluctuation theorems |
| [`SRT_Phys_E04_Relational_Time_Bridge.md`](SRT_Phys_E04_Relational_Time_Bridge.md) | Page–Wootters relational time + recent revivals | Provides a non-discrete relational-time bridge as an alternative read of L1 manifest time |
| [`SRT_Phys_E05_Falsifiability_Program.md`](SRT_Phys_E05_Falsifiability_Program.md) | Lakatos research-programme schema | Hard core / protective belt and five near-term falsification windows |

---

## 3. Recommended reading paths

### Quantum-foundations reader (3 minutes)
1. [`SRT_Phys_E01_Quantum_Instrument_Bridge.md`](SRT_Phys_E01_Quantum_Instrument_Bridge.md)
2. [`SRT_Phys_E02_Quantum_Reference_Frames_Bridge.md`](SRT_Phys_E02_Quantum_Reference_Frames_Bridge.md)
3. [`SRT_Phys_E04_Relational_Time_Bridge.md`](SRT_Phys_E04_Relational_Time_Bridge.md)

### Statistical-physicist reader
1. [`SRT_Phys_E03_Information_Thermodynamics_Bridge.md`](SRT_Phys_E03_Information_Thermodynamics_Bridge.md)
2. [`SRT_Phys_E01_Quantum_Instrument_Bridge.md`](SRT_Phys_E01_Quantum_Instrument_Bridge.md)
3. [`SRT_Phys_E05_Falsifiability_Program.md`](SRT_Phys_E05_Falsifiability_Program.md)

### Pressure-test / falsification reader
1. [`SRT_Phys_E05_Falsifiability_Program.md`](SRT_Phys_E05_Falsifiability_Program.md)
2. [`../_SRT_Phys_Bridge.md`](../_SRT_Phys_Bridge.md) §VI
3. The four bridges above as supporting evidence.

---

## 4. What this batch deliberately does NOT do

1. It does not modify any canonical anchor file. Cross-checked against
   [`../../Governance/SRT_CANONICAL_FREEZE.md`](../../Governance/SRT_CANONICAL_FREEZE.md) §A.
2. It does not promote H-Phys-2 (discrete time) or H-Phys-4 (gravity /
   friction) to theorems. They remain hypothesis / bridge.
3. It does not claim that any of the cited published frameworks (GKLS, QRF,
   Crooks, Page–Wootters) "prove" SRT. The relation is structural: SRT
   inherits formal infrastructure, and pays back with a candidate
   reinterpretation of selection / embodiment / payability.
4. It does not introduce new symbols outside the
   [`../../_SRT_SYMBOL_TABLE.md`](../../_SRT_SYMBOL_TABLE.md) without
   marking them as bridge-local.
5. It does not change the language commitment of
   [`../_SRT_Phys_Bridge.md`](../_SRT_Phys_Bridge.md):
   collapse-family default, MWI translation only as note / appendix.

---

## 5. Promotion path

These files can ascend the claim ladder only by:

1. A canonical-registry update under
   [`../../Governance/SRT_EDIT_PROTOCOL.md`](../../Governance/SRT_EDIT_PROTOCOL.md) §C;
2. Independent empirical anchoring (one or more of the falsification windows
   in `SRT_Phys_E05_Falsifiability_Program.md` returning a positive
   discriminator); and
3. Symbol-table reconciliation in
   [`../../_SRT_SYMBOL_TABLE.md`](../../_SRT_SYMBOL_TABLE.md).

Until then, treat every claim in this directory as **bridge** in the sense
of [`../../Governance/SRT_CLAIM_LADDER.md`](../../Governance/SRT_CLAIM_LADDER.md)
P3 (bridge mapping).

---

## 6. Cross-references back into the repo

| Topic | Existing file | This batch |
|---|---|---|
| Selection operator definition | `_SRT_Phys_Bridge.md` Def-Phys-1 [D1.1.1] | E01 (formal home) |
| Heisenberg cut / `\theta_{boundary}` | `_SRT_Phys_Bridge.md` §I | E02 (QRF formalization) |
| `\Psi_f` payability | `_SRT_PSI_F_CANONICAL.md`, `SRT_Phys_09_Formalism_Ext_CompactCore.md` §4 | E03 (fluctuation-theorem inequality) |
| Time discretization | `_SRT_Phys_Bridge.md` H-Phys-2, `patches/SRT_Phys_P05_*.md` | E04 (relational, non-discrete alternative) |
| Domain pressure / falsifiability | `_SRT_Phys_Bridge.md` §VI | E05 (consolidated program) |
