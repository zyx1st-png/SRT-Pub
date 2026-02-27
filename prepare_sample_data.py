import csv
import math
import os
import random
from pathlib import Path


ROOT = Path(__file__).resolve().parent
OUT_DIR = ROOT / "data"
RAW_DIR = OUT_DIR / "raw"
PROC_DIR = OUT_DIR / "processed"
UNIFIED_PATH = OUT_DIR / "unified_srt_mtor.csv"


def ensure_dirs():
    for p in [RAW_DIR / "allen", RAW_DIR / "GSE286175", RAW_DIR / "GSE247367", PROC_DIR]:
        p.mkdir(parents=True, exist_ok=True)


def make_allen_like_rows(n_units=4, T=20.0, dt=0.05, seed=1):
    random.seed(seed)
    rows = []
    n_steps = int(T / dt)

    for u in range(n_units):
        circuit_id = f"unit_{u:03d}"
        base = 4.0 + u * 0.7
        pref = 1 if u % 2 == 0 else 0
        for k in range(n_steps):
            t = k * dt
            stim = 1 if int(t // 2) % 2 == 0 else 0
            u_obs = 1.0 if stim == pref else 0.2

            lam = (base + 8.0 * u_obs)  # Hz
            mean = lam * dt
            # Poisson sample (Knuth)
            L = math.exp(-mean)
            p = 1.0
            c = 0
            while p > L:
                c += 1
                p *= random.random()
            spike_count = c - 1

            rows.append({
                "dataset_id": "allen_vcnp",
                "subject_id": "mouse_demo",
                "session_id": "session_demo_01",
                "circuit_id": circuit_id,
                "t_sec": round(t, 4),
                "dt_sec": dt,
                "spike_count": spike_count,
                "x_mtor_proxy": "",  # unknown at this stage
                "u_observer": round(u_obs, 4),
                "condition": "visual_stim",
                "split": "train" if k < int(0.7 * n_steps) else ("valid" if k < int(0.85 * n_steps) else "test"),
            })
    return rows


def make_omics_like_rows(dataset_id, n_samples=40, seed=7, condition_a="WT", condition_b="variant"):
    random.seed(seed)
    rows = []
    dt = 1.0

    for i in range(n_samples):
        cond = condition_a if i < n_samples // 2 else condition_b
        # mock mTOR proxy: variant shifted higher
        x = random.gauss(0.45, 0.08) if cond == condition_a else random.gauss(0.68, 0.10)
        x = max(0.0, min(1.0, x))

        # derive observer from sample label confidence
        u = 0.3 + 0.8 * (x - 0.5)

        rows.append({
            "dataset_id": dataset_id,
            "subject_id": f"sample_{i:03d}",
            "session_id": f"{dataset_id}_batch_01",
            "circuit_id": "bulk",
            "t_sec": float(i),
            "dt_sec": dt,
            "spike_count": "",
            "x_mtor_proxy": round(x, 4),
            "u_observer": round(u, 4),
            "condition": cond,
            "split": "train" if i < int(0.7 * n_samples) else ("valid" if i < int(0.85 * n_samples) else "test"),
        })
    return rows


def write_unified(rows):
    fields = [
        "dataset_id",
        "subject_id",
        "session_id",
        "circuit_id",
        "t_sec",
        "dt_sec",
        "spike_count",
        "x_mtor_proxy",
        "u_observer",
        "condition",
        "split",
    ]
    with open(UNIFIED_PATH, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def main():
    ensure_dirs()

    rows = []
    rows.extend(make_allen_like_rows())
    rows.extend(make_omics_like_rows("GSE286175", condition_a="control", condition_b="mTOR_perturb"))
    rows.extend(make_omics_like_rows("GSE247367", condition_a="WT", condition_b="TSC2_variant", seed=9))

    write_unified(rows)

    print(f"wrote: {UNIFIED_PATH}")
    print(f"rows: {len(rows)}")
    print("ready for fit_real_pipeline.py ingestion")


if __name__ == "__main__":
    main()
