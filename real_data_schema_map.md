# Real Data Schema Map (N, U, x)

## Unified schema: `data/unified_srt_mtor_real.csv`

Columns:
- dataset_id
- subject_id
- session_id
- circuit_id
- t_sec
- dt_sec
- spike_count
- x_mtor_proxy
- u_observer
- condition
- split

---

## Mapping A: Allen Neuropixels -> N/U

- dataset_id = `allen_vcnp_real`
- subject_id = specimen/mouse id
- session_id = ecephys session id
- circuit_id = unit_id
- t_sec/dt_sec = binned time
- spike_count = bin count from spike_times
- u_observer = stimulus-conditioned utility (e.g., preferred block=1 else 0.2)
- x_mtor_proxy = empty (temporarily)

---

## Mapping B: GEO -> x

### GSE286175 / GSE247367
- dataset_id = accession
- subject_id = GSM id
- session_id = accession batch
- circuit_id = `bulk`
- t_sec = sample index (placeholder if no time)
- dt_sec = 1.0
- spike_count = empty
- x_mtor_proxy = mTOR gene-set score (z-score)
- u_observer = derived from condition/contrast (low weight)

---

## Prior bridge into model

- `theta ~ N(mu_theta(x_mtor_proxy), sd_theta)`
- `alpha ~ N(mu_alpha(condition contrast), sd_alpha)`

Note: until real time-aligned multimodal data is available, x only informs priors, not per-bin neural latent state.
