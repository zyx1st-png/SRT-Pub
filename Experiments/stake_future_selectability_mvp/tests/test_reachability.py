from __future__ import annotations

import pytest

from src.metrics import manipulation_metrics, reach20


def test_x_reach20_uncoupling(smoke_config):
    high = reach20(smoke_config, master_seed=42, condition="X", severity="low", integrity=1.0)
    low = reach20(smoke_config, master_seed=42, condition="X", severity="low", integrity=0.7)
    assert high == low


def test_capability_intervention_changes_t_reach_or_controllability(smoke_config):
    metrics = manipulation_metrics(smoke_config, master_seed=42, condition="T", severity="low")
    changed = abs(metrics["reach20_score_delta_i1_minus_i07"]) > 1e-9 or abs(metrics["emp5_delta_i1_minus_i07"]) > 1e-9
    assert changed
