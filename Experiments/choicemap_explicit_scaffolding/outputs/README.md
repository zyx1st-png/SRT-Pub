---
id: SRT-EXP-CHOICEMAP-EXPLICIT-SCAFFOLDING-OUTPUTS-README
type: experiment_output_readme
status: active_locked
layer: lab
epistemic_layer: p4
claim_mode: evidence
canonical: false
---

# Output layout

`confirmatory/` is the authoritative locked run. The `raw` and `processed` entry paths
point to that run. Smoke and pilot outputs are diagnostic only and are not used as
confirmatory evidence.

Raw CSV streams are reproducible intermediates and are intentionally not repository
deliverables; the lossless compressed Parquet files are the committed raw logs.
