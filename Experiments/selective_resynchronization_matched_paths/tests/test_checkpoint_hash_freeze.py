import pandas as pd
import pytest

from src.endpoint_matching import freeze_matching_outputs, verify_matching_freeze


def test_matching_freeze_detects_mutation(tmp_path):
    matched = pd.DataFrame([{"seed": 1, "path": "standard_full", "uses_future_data": False}])
    balance = pd.DataFrame([{"seed": 1, "matched": True}])
    freeze_matching_outputs(tmp_path, "test", matched, balance)
    assert verify_matching_freeze(tmp_path / "outputs" / "test")["matched_groups"] == 1
    path = tmp_path / "outputs" / "test" / "matched_B_checkpoints.parquet"
    path.chmod(0o644)
    changed = pd.read_parquet(path)
    changed.loc[0, "path"] = "mutated"
    changed.to_parquet(path, index=False)
    with pytest.raises(RuntimeError):
        verify_matching_freeze(tmp_path / "outputs" / "test")
