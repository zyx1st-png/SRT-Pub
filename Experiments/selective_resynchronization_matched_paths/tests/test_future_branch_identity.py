import pytest

from src.future_tasks import verify_future_branch_identity


def _records():
    return [
        {
            "seed": 1,
            "path": path,
            "future_task": "rotation20",
            "data_order_hash": "same-order",
            "budget_updates": 100,
            "branch_start_state_dict_sha256": f"state-{path}",
            "matched_B_state_dict_sha256": f"state-{path}",
        }
        for path in ["standard_full", "head_only", "replay_full", "head_reset_full"]
    ]


def test_future_paths_share_order_and_budget_and_exact_B_state():
    verify_future_branch_identity(_records())


def test_future_identity_rejects_path_specific_order():
    records = _records()
    records[0]["data_order_hash"] = "different"
    with pytest.raises(RuntimeError):
        verify_future_branch_identity(records)
