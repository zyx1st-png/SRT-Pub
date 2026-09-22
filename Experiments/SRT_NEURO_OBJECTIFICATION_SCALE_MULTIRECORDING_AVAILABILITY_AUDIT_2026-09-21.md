---
id: SRT-NEURO-OBJECTIFICATION-SCALE-MULTIRECORDING-AVAILABILITY-AUDIT-20260921
type: experiment_audit
status: frozen
version: v0_1
record_stage: availability_audit_completed_before_deltaq
date: 2026-09-22
layer: operations
epistemic_layer: experimental
claim_mode: report
claim_level: P4
canonical: false
ai_do_not_use_for_definition: true
domain: neuroscience
tags: [Neuroscience, MultiRecording, Replication, AvailabilityAudit, ResultBlind]
---

# Multi-recording availability audit

## 1. Audit boundary

This is the result-blind materialization and technical inclusion audit required by the frozen multi-recording preregistration. It was completed before any new correlation, graph, Louvain, `Q`, `DeltaQ`, or state-effect calculation.

The audit inspected HDF5 structure, required signal presence, deterministic signal sanity samples, ROI coordinate finiteness, `frame.used_frame` lengths, state-vector finiteness, and the number of complete source windows. No recording was excluded using a scientific result.

Controlling protocol: `Experiments/SRT_NEURO_OBJECTIFICATION_SCALE_MULTIRECORDING_PREREGISTRATION_2026-09-21.md`.

## 2. Source and version note

- Source: RIKEN CBS Data Sharing Platform API, DOI `10.60178/cbs.20260708-001`.
- Collection folder: `12a35d86-b6e1-4cc0-8e69-ab0cbb6ef010`, “Large-scale two-photon imaging dataset”.
- Processed files were downloaded from the official file IDs listed below using HTTP range requests with resumable per-chunk checkpoints.
- The collection task label referred to this accession as CBS v3.0. The retrieved processed-data README identifies the analysis release as `v2.0` (release 2026-03). This naming discrepancy is preserved; it is not silently relabeled.
- Local raw `.mat` files remain in `.local/phase2_multirecording/` and are not tracked by Git.

## 3. Frozen inclusion result

All 10 candidate recordings are technically eligible under the preregistered result-blind criteria:

- `spike_smoothed` is present and finite in deterministic samples;
- `ROIs/Centroid` is present and finite;
- `frame/used_frame` is present with at least one complete source window in each of the two state segments;
- the state vector is present and finite;
- required HDF5 metadata/groups are readable;
- no result-dependent exclusion was applied.

| recording | condition | animal | neurons | used-frame lengths | complete windows | eligible |
|---|---:|---|---:|---|---|---|
| `mouse01_sleep` | sleep | mouse01 | 7,843 | 2,359 / 5,027 | 1 / 3 | yes |
| `mouse02_sleep` | sleep | mouse02 | 6,574 | 7,000 / 8,375 | 4 / 5 | yes |
| `mouse03_sleep` | sleep | mouse03 | 7,112 | 1,549 / 12,527 | 1 / 8 | yes |
| `mouse04_day1_sleep` | sleep | mouse04 | 9,612 | 2,008 / 11,502 | 1 / 7 | yes |
| `mouse04_day2_sleep` | sleep | mouse04 | 10,197 | 9,235 / 6,557 | 6 / 4 | yes |
| `mouse05_sleep` | sleep | mouse05 | 7,355 | 9,146 / 5,660 | 6 / 3 | yes |
| `mouse03_ane` | anesthesia | mouse03 | 7,350 | 9,500 / 8,263 | 3 / 2 | yes |
| `mouse05_ane` | anesthesia | mouse05 | 6,592 | 15,528 / 2,933 | 5 / 1 | yes |
| `mouse06_ane` | anesthesia | mouse06 | 5,295 | 8,762 / 13,789 | 3 / 4 | yes |
| `mouse07_ane` | anesthesia | mouse07 | 4,337 | 9,500 / 8,500 | 3 / 2 | yes |

Summary: 6 sleep sessions from 5 animals and 4 anesthesia sessions from 4 animals. The two `mouse04` sleep sessions remain separate sessions nested within the same animal.

## 4. Materialization and checksum record

The downloader checkpoint and an independent local `shasum -a 256` pass agreed for every file.

| file | CBS file ID | bytes | SHA-256 |
|---|---|---:|---|
| `mouse01_sleep.mat` | `1f786027-c4b2-4ac9-8449-24c0cfb434db` | 658474258 | `a73526ff842633816a7d03f2578eaeb398fd928c9c2b4a62a2496273dc3c59e6` |
| `mouse02_sleep.mat` | `b266f5ee-cc1d-4a47-9d41-29655a7c3967` | 1093789677 | `e7f283390791c5fbeade9dc2f579d9e89c772a46afcb7f36636d8d081bf99934` |
| `mouse03_sleep.mat` | `3191b169-1d10-4807-9284-edfd96f6c44e` | 1197235306 | `dcac3d396edcb188e88a7e1ff91efe335c904e9defdf2d26c11c36281bcb4277` |
| `mouse04_day1_sleep.mat` | `8d84d7ac-b4c8-4208-9e5c-c3a4605d3e31` | 1625754526 | `3d78be67a6a192c511a41520062f6621b898661d2a2bc127e3f13012fb24ace3` |
| `mouse04_day2_sleep.mat` | `105e2c10-8a9a-4cd2-9c76-411cf673ec28` | 2254368168 | `84c843c06006a283a9df7fc3e081c550500e52909bafc96533b91861130f02c7` |
| `mouse05_sleep.mat` | `ed06e6f2-7485-493e-8d32-d01e0d13aec9` | 1263665343 | `973c27b3e27451d153c108b1ad38e447b749622ac58de2c6c0c0c01ccb380181` |
| `mouse03_ane.mat` | `1616a6b6-edec-4637-bea9-bca9c0a95848` | 1123058079 | `60b1470ddfb0fe2503b8085efb6fad8fd6c0b285f74fd31eb4f4fc3dea492d2b` |
| `mouse05_ane.mat` | `5b5f67db-2bd0-43ae-8b4f-eb50138e6057` | 1079340853 | `1a02c596c87d8b9376c6e7be6476c7d79dd03bff99f4ae80e023cbef3f74b7a9` |
| `mouse06_ane.mat` | `e1dd0560-3486-45e6-a086-e2c1bfb2bb6e` | 563929318 | `2b33bc3d6b3fafafdbdbf377dd3691d2ad6408bf526f6b85de716d85fa3a3cfb` |
| `mouse07_ane.mat` | `ffdc68e6-fbb4-43f5-81e2-a8271a50819a` | 363189208 | `a6eb90c6bd62ef7530bc93320fb906f41584a43a293f4878a01e2ab5bb5e5899` |

Total materialized data bytes: `11222804736`.

## 5. Audit outputs and gate

Machine-readable outputs are retained in `.local/phase2_multirecording/`:

- `dataset_expansion_inventory.json`
- `recording_level_inventory.csv`
- `data_inventory.txt`
- `download_state.json`
- `download.log`

Audit result: `PASS` for data materialization and technical inclusion. `delta_q_computed=false` remains explicit in the machine-readable inventory. This audit authorizes the preregistered multi-recording primary calculation; it does not alter any scientific parameter or authorize later analyses outside the frozen protocol.
