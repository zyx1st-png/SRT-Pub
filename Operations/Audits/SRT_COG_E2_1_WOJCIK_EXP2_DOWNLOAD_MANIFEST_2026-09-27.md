---
id: SRT-COG-E2-1-WOJCIK-EXP2-DOWNLOAD-MANIFEST-20260927
type: audit
status: active
record_stage: download_scope_locked
canonical: false
layer: operations
epistemic_layer: os
claim_mode: source_manifest
created: 2026-09-27
updated: 2026-09-27
research_mode: U
dependency:
  - Operations/Audits/SRT_COG_E2_1_WOJCIK_SESSION_MAPPING_2026-09-27.md
  - Operations/Proposals/SRT_COG_E2_1_WOJCIK_TARGET_BLIND_CENSUS_HANDOFF_2026-09-27.md
tags: [Cognition, Wójcik, Dryad, DownloadManifest, Exp2, Census]
---

# COG-E2-1 — Experiment-2 download manifest

> Purpose: lock the minimal raw-data download scope before target-blind census.

Dryad dataset:

    DOI 10.5061/dryad.c2fqz61kb

Dryad lists the complete dataset as 32.11 GB and each session as one ZIP archive.

Experiment-2 requires only 23 archives.

## 1. Womble / Monkey 1 — Exp2

| Dryad archive | Code session | Size |
|---|---|---:|
| m1_ses18.zip | Wom20201005 | 210.24 MB |
| m1_ses19.zip | Wom20201006 | 302.13 MB |
| m1_ses20.zip | Wom20201007 | 183.74 MB |
| m1_ses21.zip | Wom20201008 | 243.43 MB |
| m1_ses22.zip | Wom20201009 | 267.87 MB |
| m1_ses23.zip | Wom20201012 | 194.84 MB |
| m1_ses24.zip | Wom20201013 | 174.12 MB |
| m1_ses25.zip | Wom20201014 | 242.96 MB |

Subtotal:

    1819.33 MB

## 2. Wilfred / Monkey 2 — Exp2

| Dryad archive | Code session | Size |
|---|---|---:|
| m2_ses11.zip | Wil20201104 | 961.92 MB |
| m2_ses12.zip | Wil20201106 | 930.71 MB |
| m2_ses13.zip | Wil20201109 | 906.51 MB |
| m2_ses14.zip | Wil20201110 | 747.20 MB |
| m2_ses15.zip | Wil20201111 | 786.76 MB |
| m2_ses16.zip | Wil20201112 | 814.73 MB |
| m2_ses17.zip | Wil20201113 | 552.95 MB |
| m2_ses18.zip | Wil20201116 | 522.31 MB |
| m2_ses19.zip | Wil20201117 | 521.92 MB |
| m2_ses20.zip | Wil20201118 | 208.56 MB |
| m2_ses21.zip | Wil20201119 | 296.88 MB |
| m2_ses22.zip | Wil20201120 | 320.44 MB |
| m2_ses23.zip | Wil20201123 | 575.57 MB |
| m2_ses24.zip | Wil20201124 | 492.23 MB |
| m2_ses25.zip | Wil20201125 | 725.30 MB |

Subtotal:

    9363.99 MB

## 3. Total Exp2 scope

    11183.32 MB
    ≈ 11.18 GB decimal
    ≈ 10.92 GiB

This is ~35% of the full 32.11 GB Dryad package.

## 4. Fixed download batches

Dryad currently states that selected-file ZIP download supports up to 11 GB.

Because the full Exp2 scope is slightly above that limit, do not rely on one selected-files bundle.

Use fixed batches:

### Batch A — Womble Exp2

    m1_ses18 ... m1_ses25
    total = 1819.33 MB

### Batch B — Wilfred Exp2 early

    m2_ses11 ... m2_ses18
    total = 6223.09 MB

### Batch C — Wilfred Exp2 late

    m2_ses19 ... m2_ses25
    total = 3140.90 MB

Each batch is independently checksum-locked.

## 5. Archive content expectation

Dryad README states each session ZIP contains session neural data, electrode-location information and trial metadata.

Repository analysis code expects date-labelled equivalents for:

    *_Spikes_preprocessed.npy
    *_meta.npy
    *_cell_loc.csv

Because the Dryad README generically describes three session files while code naming is more specific, the executor must inspect archive member names after download and record the exact adapter.

Do not mutate original archives.

## 6. Target-blind boundary

Download, checksum, archive-member listing and file-shape inspection do not reveal the E2b target and are authorized.

Do not run context cross-set decoding while validating the archives.

## 7. Current disposition

    full 32.11 GB download = NOT REQUIRED
    Exp2-only 11.18 GB scope = LOCKED
    fixed 3-batch plan = LOCKED
    target values = UNINSPECTED