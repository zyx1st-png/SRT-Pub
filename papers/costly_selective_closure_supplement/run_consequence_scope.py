from __future__ import annotations

import json
from pathlib import Path

from src import csc_consequence_scope as e4


def main():
    cfg = {
        "train_eps": 1000,
        "withdraw_eps": 300,
        "window": 100,
        "lr": 0.04,
        "lr_w": 0.04,
        "gamma": 0.97,
    }
    out = Path(__file__).resolve().parent / "results" / "consequence_scope_results.json"
    payload = e4.run_confirmatory(cfg, e4.CONFIRMATORY_SEEDS, out)
    print(json.dumps({
        "primary_scope_test": payload["primary_scope_test"],
        "latency_level_primary_contrasts": payload["latency_level_primary_contrasts"],
        "secondary_rollout_scope_contrast": payload["secondary_rollout_scope_contrast"],
    }, indent=2))
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
