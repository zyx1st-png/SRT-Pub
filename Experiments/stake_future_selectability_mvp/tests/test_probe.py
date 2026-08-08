from __future__ import annotations

import numpy as np

from src.metrics import observations_from_records, probe_records


def test_counterfactual_probe_changes_only_integrity_input(smoke_config):
    records = probe_records(smoke_config, 42)
    high = observations_from_records(
        smoke_config, records, master_seed=42, condition="S", severity="low", integrity=1.0
    )
    low = observations_from_records(
        smoke_config, records, master_seed=42, condition="S", severity="low", integrity=0.9
    )
    for high_obs, low_obs in zip(high, low):
        np.testing.assert_array_equal(high_obs["grid"], low_obs["grid"])
        difference = np.flatnonzero(high_obs["state"] != low_obs["state"])
        assert difference.tolist() == [1]
