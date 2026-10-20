---
id: SRT-COG-E2-1-WOJCIK-DRYAD-ADAPTER-CONTRACT-20260927
type: proposal
status: draft
record_stage: pre_download_contract
canonical: false
layer: operations
epistemic_layer: execution_handoff
claim_mode: bounded_adapter_contract
created: 2026-09-27
updated: 2026-09-27
research_mode: U
dependency:
  - Operations/Audits/SRT_COG_E2_1_WOJCIK_EXP2_DOWNLOAD_MANIFEST_2026-09-27.md
  - Operations/Audits/SRT_COG_E2_1_WOJCIK_SESSION_MAPPING_2026-09-27.md
tags: [Cognition, Wójcik, Dryad, Adapter, TargetBlind]
---

# COG-E2-1 — Dryad-to-source-code adapter contract

> Role: define the only permitted data-format bridge before local census.

## 1. Source mismatch

Dryad README describes each session archive as containing:

- neural firing-rate data;
- electrode-location data;
- trial metadata.

The locked analysis code expects:

    <Session>_Spikes_preprocessed.npy
    <Session>_meta.npy
    <Session>_cell_loc.csv

and accesses the location file as:

    pandas.read_csv(...)["Area"]

No conversion script for this Dryad naming/format bridge was found in the locked public analysis repository.

## 2. Adapter may only perform structural translation

Allowed:

- extract archive members;
- map Dryad session ID to locked date-labelled session ID;
- copy / symlink neural data to the expected filename;
- copy / symlink metadata to the expected filename;
- if electrode location is a numeric array, write the same values into one CSV column named `Area`;
- record source and output SHA256 where byte-preserving;
- record value-level equality for format conversion.

Not allowed:

- smoothing / re-smoothing;
- z-scoring;
- trial removal beyond source metadata rules;
- relabeling trial identities;
- remapping area codes;
- dropping neurons;
- changing time axis;
- casting values in a way that changes numeric content;
- using any E2b target to decide conversion.

## 3. Archive-member discovery gate

On the first archive from each animal, record:

    member names
    file types
    array shapes
    dtypes

without running any decoder.

Then verify the same member schema on all remaining archives.

If schemas differ:

    STOP and document before writing a generalized adapter.

## 4. Neural-data contract

Dryad documentation states:

    n_trials × n_neurons × 3500_timepoints

for smoothed firing-rate data.

The analysis source `get_data` loads the expected neural file, then:

    slices timepoints 500:3000
    downsamples by factor 10
    selects trials with nonzero metadata.

Therefore the adapter must not pre-apply those operations.

## 5. Trial-metadata contract

Dryad Experiment-2 trial IDs are 1..16.

Adapter requirement:

    preserve the integer vector exactly.

The source code performs:

    labels = trials[trials != 0]

and matches nonzero trial rows in neural data.

Do not convert IDs to factor labels in the adapter.

## 6. Electrode-location contract

Dryad area codes:

    1 dlPFC dorsal to principal sulcus
    2 dorsal principal sulcus
    3 ventral principal sulcus
    4 vlPFC ventral to principal sulcus
    5 lateral OFC
    6 beyond superior arcuate sulcus
    7 beyond inferior arcuate sulcus

Source analysis uses sampled areas:

    [1,2,3,4]

Adapter requirement:

    preserve integer area code;
    if conversion to CSV is needed, output exactly one required column `Area` plus no inferred ontology.

## 7. Validation

For each adapted session verify:

- neural trial axis compatible with metadata length / nonzero mask;
- neural neuron axis equals electrode-location length;
- time axis = 3500 before source slicing;
- trial IDs subset of expected Experiment-2 coding;
- area codes subset of documented coding;
- no NaN / dtype corruption introduced by adapter.

These checks are target-blind.

## 8. Provenance manifest

Required record per session:

    dryad_archive
    dryad_archive_sha256
    archive_member
    archive_member_sha256 where available
    code_session_id
    adapted_path
    adapted_sha256 or value-equivalence digest
    shape
    dtype
    adapter_action

## 9. Stop rule

STOP before census if:

- archive content cannot be mapped one-to-one to neural/meta/location roles;
- neural arrays are already differently preprocessed from source assumptions;
- metadata alignment is ambiguous;
- location conversion requires interpretation rather than format translation.

## 10. Target firewall

The adapter must not import or call:

    run_decoding_colour_locked
    run_decoding_ler_null_colour_locked
    plot_dec_xgen

or any new code that computes per-session context xgen.

Adapter validation ends at structure/provenance.

Canonical edit = NO.