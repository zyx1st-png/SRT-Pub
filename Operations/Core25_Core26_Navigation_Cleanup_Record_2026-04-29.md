---
id: SRT-OPS-CORE25-CORE26-NAV-CLEANUP-2026-04-29
type: cleanup_record
tags: [Operations, Core 25, Core 26, Navigation, Glossary, Public Entry, Cleanup]
status: completed_v1
layer: meta
epistemic_layer: workflow
claim_mode: audit
canonical: false
date: 2026-04-29
dependency:
  - Core/SRT_Core_25_Thermodynamic_Signatures_of_Selection.md
  - Core/SRT_Core_26_MISA_Attractor_Interface.md
  - Core/SRT_Core_25_26_Interface_Index.md
  - _SRT_CONTEXT_ROUTER_CORE25_CORE26_EXTENSION.md
  - Glossary/SRT_Glossary_Core25_Core26_Bridge_Terms.md
  - SRT_Public_Reading_Guide.md
---

# Core 25 / Core 26 Navigation Cleanup Record — 2026-04-29

## 0. Purpose

This record closes the cleanup requested after the recent repository evaluation.

The cleanup addressed three issues:

1. duplicate / conflicting Core 24 numbering;
2. missing routing / glossary anchors for the new thermodynamic and MISA bridge files;
3. lack of a simple public reading guide separate from the engineering / governance entrypoints.

---

## 1. Numbering cleanup

### Problem

Multiple bridge files used the `Core 24` number:

- `Core/SRT_Core_24_Floor_Normativity_Verification.md`
- `Core/SRT_Core_24_Thermodynamic_Signatures_of_Selection.md`
- `Core/SRT_Core_24_MISA_Attractor_Interface.md`

This created ambiguity for citation, indexing, and machine retrieval.

### Action taken

The two newer bridge files were renumbered:

| Old path | New path |
|---|---|
| `Core/SRT_Core_24_Thermodynamic_Signatures_of_Selection.md` | `Core/SRT_Core_25_Thermodynamic_Signatures_of_Selection.md` |
| `Core/SRT_Core_24_MISA_Attractor_Interface.md` | `Core/SRT_Core_26_MISA_Attractor_Interface.md` |

The old duplicate Core 24 files were deleted after the new files were created.

### Boundary

No claim was promoted by renumbering. The new files remain `claim_mode: bridge` and `canonical: false`.

---

## 2. Routing / glossary cleanup

### Problem

The new bridge modules were useful but not yet well-routed.

### Action taken

Created:

- `Core/SRT_Core_25_26_Interface_Index.md`
- `_SRT_CONTEXT_ROUTER_CORE25_CORE26_EXTENSION.md`
- `Glossary/SRT_Glossary_Core25_Core26_Bridge_Terms.md`

These files provide retrieval routes for:

- Thermodynamics of Mind;
- irreversibility;
- entropy production;
- broken detailed balance;
- neural hierarchy;
- MISA attractor;
- mutual inhibition;
- self activation;
- hybrid attractor;
- cell fate;
- L2 hardening.

### Boundary

The extension files are navigation / glossary addenda only. They do not override `_SRT_CONTEXT_ROUTER.md`, `SRT_Glossary.md`, or `_SRT_SYMBOL_TABLE.md`.

---

## 3. Public reading cleanup

### Problem

The repository had strong governance machinery but remained difficult for public readers because the machine / Operations layer is too visible.

### Action taken

Created:

- `SRT_Public_Reading_Guide.md`

This file separates public reading paths from internal governance paths. It gives four routes:

1. general philosophy reader;
2. consciousness / neuroscience reader;
3. AI / agency reader;
4. social / institutional reader.

### Boundary

The public reading guide is navigation only. It does not define theory and does not outrank canonical files.

---

## 4. What was deliberately not done

This cleanup did **not** rewrite the full `_SRT_INDEX.md` or `_SRT_CONTEXT_ROUTER.md` main files.

Reason:

- both files are long and already contain many carefully maintained entries;
- a surgical full rewrite risks accidental deletion of existing routes;
- local extension files provide a safer interim route until the main indexes are next compacted or regenerated.

Recommended next maintenance pass:

```text
merge Core25/Core26 routes into _SRT_INDEX.md and _SRT_CONTEXT_ROUTER.md
then mark the extension files as superseded or keep them as local addenda
```

---

## 5. Final state

After this cleanup:

| Issue | Status |
|---|---|
| Core 24 numbering conflict | resolved |
| Core 25 thermodynamic bridge path | active |
| Core 26 MISA bridge path | active |
| local interface index | added |
| local context-router extension | added |
| local glossary addendum | added |
| public reading guide | added |
| canonical status | unchanged; no promotion |

---

## 6. Stop rule

Do not continue adding new bridge modules until:

1. Core 25 and Core 26 are merged into the main index/router, or
2. a specific new bridge is requested with a clear source interface and boundary note.

The next low-risk work is index consolidation, not theoretical expansion.
