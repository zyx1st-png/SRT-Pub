import csv
from pathlib import Path

import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
FIG_DIR = ROOT / "figures"
FIG_DIR.mkdir(exist_ok=True)


def read_experiments(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            rows.append({k: float(v) if k not in ("",) else v for k, v in row.items()})
    return rows


def fig_delta_mi(rows):
    # average delta MI by omega
    by_w = {}
    for r in rows:
        w = r["omega"]
        by_w.setdefault(w, []).append(r["delta_mi_vs_omega0"])

    ws = sorted(by_w)
    means = [sum(by_w[w]) / len(by_w[w]) for w in ws]

    plt.figure(figsize=(6, 4))
    plt.plot(ws, means, marker="o")
    plt.axhline(0, linestyle="--", linewidth=1)
    plt.xlabel("omega")
    plt.ylabel("Mean ΔMI (nats)")
    plt.title("SRT signal vs omega")
    plt.tight_layout()
    out = FIG_DIR / "fig_delta_mi_vs_omega.png"
    plt.savefig(out, dpi=160)
    plt.close()
    return out


def fig_rate_vs_omega(rows):
    by_w = {}
    for r in rows:
        w = r["omega"]
        by_w.setdefault(w, []).append(r["mean_rate_hz"])

    ws = sorted(by_w)
    means = [sum(by_w[w]) / len(by_w[w]) for w in ws]

    plt.figure(figsize=(6, 4))
    plt.plot(ws, means, marker="s")
    plt.xlabel("omega")
    plt.ylabel("Mean firing rate (Hz)")
    plt.title("Rate escalation under selective weighting")
    plt.tight_layout()
    out = FIG_DIR / "fig_rate_vs_omega.png"
    plt.savefig(out, dpi=160)
    plt.close()
    return out


def fig_pipeline_bars():
    # hard-coded from current run summaries
    labels = ["v2", "v3", "v4", "v5"]
    valid = [2.306, 8.536, 8.679, 8.056]
    test = [-1.254, 9.765, 9.555, 8.991]

    x = range(len(labels))
    w = 0.36

    plt.figure(figsize=(7, 4))
    plt.bar([i - w / 2 for i in x], valid, width=w, label="valid ΔNLL")
    plt.bar([i + w / 2 for i in x], test, width=w, label="test ΔNLL")
    plt.axhline(0, linestyle="--", linewidth=1)
    plt.xticks(list(x), labels)
    plt.ylabel("ΔNLL (null - model)")
    plt.title("Generalization gain across pipeline versions")
    plt.legend()
    plt.tight_layout()
    out = FIG_DIR / "fig_pipeline_deltanll.png"
    plt.savefig(out, dpi=160)
    plt.close()
    return out


def fig_v6_posterior():
    # approximate normal posterior from v6 summary
    import math

    mu = 0.2921
    lo, hi = 0.2217, 0.3618
    sigma = (hi - lo) / 3.92  # 95% CI approx

    xs = [0.05 + i * 0.002 for i in range(220)]
    ys = [1 / (sigma * (2 * math.pi) ** 0.5) * math.exp(-0.5 * ((x - mu) / sigma) ** 2) for x in xs]

    plt.figure(figsize=(6, 4))
    plt.plot(xs, ys)
    plt.axvline(0, linestyle="--", linewidth=1, label="omega=0")
    plt.axvline(mu, linestyle="-", linewidth=1, label="posterior mean")
    plt.title("v6 posterior of omega")
    plt.xlabel("omega")
    plt.ylabel("density (approx)")
    plt.legend()
    plt.tight_layout()
    out = FIG_DIR / "fig_v6_posterior.png"
    plt.savefig(out, dpi=160)
    plt.close()
    return out


def main():
    exp_csv = ROOT / "experiments_srt_mtor.csv"
    rows = read_experiments(exp_csv)

    outs = [
        fig_delta_mi(rows),
        fig_rate_vs_omega(rows),
        fig_pipeline_bars(),
        fig_v6_posterior(),
    ]

    print("Generated figures:")
    for o in outs:
        print(o)


if __name__ == "__main__":
    main()
