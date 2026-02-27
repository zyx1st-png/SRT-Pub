import csv
import math
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data" / "unified_srt_mtor_v2.csv"


def poisson_sample(mean):
    if mean <= 0:
        return 0
    L = math.exp(-mean)
    p, k = 1.0, 0
    while p > L:
        p *= random.random()
        k += 1
    return k - 1


def main():
    random.seed(123)

    fields = [
        "dataset_id","subject_id","session_id","circuit_id","t_sec","dt_sec",
        "spike_count","x_mtor_proxy","u_observer","condition","split"
    ]

    rows = []
    dt = 0.05
    T = 30.0
    n_steps = int(T / dt)

    # generate Allen-like rows with explicit friction dynamics coupling
    for u in range(4):
        cid = f"unit_{u:03d}"
        base = 8.0 + 0.8 * u
        omega_true = 0.22
        alpha_true = 0.5
        theta_true = 0.6
        c_fric_true = 0.7

        prev_e = 0.0
        for k in range(n_steps):
            t = k * dt
            block = int(t // 5)
            l2_rig = 0.7 if block % 2 == 0 else -0.4
            u_obs = 0.9 * math.sin(2 * math.pi * 0.3 * t + 0.2 * u) + (0.2 if block % 3 == 0 else -0.1)
            x_hat = 1 / (1 + math.exp(-0.8 * u_obs))
            gate = 1 / (1 + math.exp(-4.0 * (x_hat - theta_true)))

            e = u_obs - l2_rig
            psi_f = abs(e - prev_e)
            prev_e = e

            lam = base * math.exp(omega_true * u_obs) * math.exp(alpha_true * (gate - 0.5)) * math.exp(-c_fric_true * psi_f)
            y = poisson_sample(lam * dt)

            split = "train" if u < 2 else ("valid" if u == 2 else "test")
            rows.append({
                "dataset_id": "allen_vcnp_v2",
                "subject_id": "mouse_demo",
                "session_id": "session_demo_02",
                "circuit_id": cid,
                "t_sec": round(t, 4),
                "dt_sec": dt,
                "spike_count": y,
                "x_mtor_proxy": "",
                "u_observer": round(u_obs, 6),
                "condition": "visual_stim",
                "split": split,
            })

    # add omics mock rows
    for ds, condA, condB, seed in [("GSE286175", "control", "mTOR_perturb", 7), ("GSE247367", "WT", "TSC2_variant", 9)]:
        random.seed(seed)
        for i in range(40):
            cond = condA if i < 20 else condB
            x = random.gauss(0.45, 0.08) if i < 20 else random.gauss(0.7, 0.1)
            x = max(0.0, min(1.0, x))
            rows.append({
                "dataset_id": ds,
                "subject_id": f"sample_{i:03d}",
                "session_id": f"{ds}_batch_01",
                "circuit_id": "bulk",
                "t_sec": float(i),
                "dt_sec": 1.0,
                "spike_count": "",
                "x_mtor_proxy": round(x, 6),
                "u_observer": round(0.3 + 0.8 * (x - 0.5), 6),
                "condition": cond,
                "split": "train" if i < 28 else ("valid" if i < 34 else "test"),
            })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    print(f"wrote {OUT}")
    print(f"rows={len(rows)}")


if __name__ == "__main__":
    main()
