import pandas as pd

from src.endpoint_matching import select_matched_group


def _config():
    return {
        "matching": {
            "candidate_epoch_min": 2,
            "candidate_epoch_max": 3,
            "adequacy": {"accuracy_min": 0.75, "nll_max": 0.8, "ece_max": 0.15},
            "consecutive_stability": {"accuracy_delta_max": 0.02, "nll_delta_max": 0.08, "ece_delta_max": 0.03},
            "group_tolerance": {"accuracy_range_max": 0.015, "nll_range_max": 0.06, "ece_range_max": 0.03},
        }
    }


def test_endpoint_group_respects_locked_ranges():
    rows = []
    paths = ["standard_full", "head_only", "replay_full", "head_reset_full"]
    for index, path in enumerate(paths):
        for epoch in [1, 2, 3]:
            rows.append(
                {
                    "seed": 1,
                    "path": path,
                    "epoch": epoch,
                    "validation_balanced_accuracy": 0.80 + index * 0.002,
                    "validation_loss": 0.50 + index * 0.005,
                    "validation_ece": 0.05 + index * 0.002,
                    "representation_drift_from_A": index * 0.03,
                    "checkpoint_path": f"/{path}/B{epoch}.pt",
                    "checkpoint_sha256": str(index),
                    "state_dict_sha256": str(index),
                }
            )
    selected = select_matched_group(1, pd.DataFrame(rows), _config())
    assert len(selected) == 4
    assert selected[0]["accuracy_range"] <= 0.015
    assert selected[0]["nll_range"] <= 0.06
    assert selected[0]["ece_range"] <= 0.03
