"""Generate the v19 E1-E4 evidence summary figure.

The figure is descriptive. Confirmatory inference remains the locked tests and
adjudications reported in the manuscript and result records. E1-E3 use
condition summaries already stored in committed result JSON. E4 uses the 30
latency-collapsed per-seed scope effects plus the preregistered paired CI.

The panels deliberately do not imply that E1-E4 lie on one severity axis.
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["svg.fonttype"] = "none"

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results"
FIGURES = HERE / "figures"


def load(name: str) -> dict:
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


def draw_summary_panel(ax, labels, means, spreads, title, xlabel=None):
    x = np.arange(1, len(labels) + 1)
    ax.errorbar(x, means, yerr=spreads, fmt="o", capsize=3, linewidth=1.0)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylim(-0.05, 1.05)
    ax.set_title(title, fontsize=10)
    if xlabel:
        ax.set_xlabel(xlabel)
    ax.grid(axis="y", alpha=0.2, linewidth=0.6)


def draw_scope_panel(ax, diffs: np.ndarray, ci: tuple[float, float], mean: float) -> None:
    rng = np.random.default_rng(1904)
    jitter = rng.uniform(-0.13, 0.13, size=len(diffs))
    ax.axhline(0.0, linewidth=0.9)
    ax.scatter(np.ones(len(diffs)) + jitter, diffs, s=15, alpha=0.6, linewidths=0)
    ax.errorbar(
        [1.0], [mean],
        yerr=[[mean - ci[0]], [ci[1] - mean]],
        fmt="D", markersize=5, capsize=4,
    )
    ax.set_xlim(0.55, 1.45)
    ax.set_xticks([1.0])
    ax.set_xticklabels(["Shared - individual"])
    ax.set_ylabel("Expected mutual-cooperation difference")
    ax.set_title("E4: consequence scope", fontsize=10)
    ax.grid(axis="y", alpha=0.2, linewidth=0.6)
    ax.text(
        0.03, 0.97,
        "preregistered support\nmodest; +0.10 gate failed",
        transform=ax.transAxes, va="top", fontsize=8,
    )


def main() -> None:
    e1 = load("main_results.json")
    e2 = load("recoverability_gradient_results.json")
    e3 = load("consequence_recovery_results.json")
    e4 = load("consequence_scope_results_E4_confirmatory_record.json")

    e1_labels = ["Terminal", "Restore"]
    e1_means = [float(e1["post_coop"]["real"][0]), float(e1["post_coop"]["resettable"][0])]
    e1_sd = [float(e1["post_coop"]["real"][1]), float(e1["post_coop"]["resettable"][1])]

    e2_order = ["tau0", "tau5", "tau15", "tau_inf"]
    e2_labels = ["0", "5", "15", "inf"]
    e2_means = [float(e2["condition_summaries"][k]["mean"]) for k in e2_order]
    e2_sd = [float(e2["condition_summaries"][k]["std"]) for k in e2_order]

    e3_order = ["k0", "k2", "k5", "k10"]
    e3_labels = ["0", "2", "5", "10"]
    e3_means = [float(e3["condition_summaries"][k]["mean"]) for k in e3_order]
    e3_sd = [float(e3["condition_summaries"][k]["std"]) for k in e3_order]

    primary = e4["primary_scope_test"]
    e4_diffs = np.asarray(primary["per_seed_collapsed_differences"], dtype=float)
    if len(e4_diffs) != 30:
        raise RuntimeError("expected exactly 30 collapsed E4 seed effects")
    e4_mean = float(primary["mean_shared_minus_individual_collapsed_over_latency"])
    e4_ci = tuple(float(x) for x in primary["paired_bootstrap_95_ci"])

    fig, axes = plt.subplots(1, 4, figsize=(14.2, 3.8))
    draw_summary_panel(axes[0], e1_labels, e1_means, e1_sd, "E1: depletion transition")
    draw_summary_panel(
        axes[1], e2_labels, e2_means, e2_sd,
        "E2: impairment duration", "Subsequent impaired steps",
    )
    draw_summary_panel(
        axes[2], e3_labels, e3_means, e3_sd,
        "E3: individual recovery", "Subsequent forced-Rest steps",
    )
    draw_scope_panel(axes[3], e4_diffs, e4_ci, e4_mean)

    axes[0].set_ylabel("Post-withdrawal mutual cooperation")
    axes[0].text(0.02, 0.98, "strong terminal effect", transform=axes[0].transAxes, va="top", fontsize=8)
    axes[1].text(0.02, 0.98, "preregistered H1:\nnot supported", transform=axes[1].transAxes, va="top", fontsize=8)
    axes[2].text(0.02, 0.98, "preregistered H1:\nopposite ordinal direction", transform=axes[2].transAxes, va="top", fontsize=8)

    fig.suptitle(
        "E1-E4: distinct failure-transition tests and a bounded consequence-scope effect",
        fontsize=11,
    )
    fig.text(
        0.5, 0.005,
        "E1-E3 points show condition means with +/- 1 SD; E4 shows 30 collapsed seed effects and the paired 95% CI.",
        ha="center", fontsize=8,
    )
    fig.tight_layout(rect=(0, 0.035, 1, 0.93))

    FIGURES.mkdir(parents=True, exist_ok=True)
    svg = FIGURES / "figure2_evidence_summary_v19.svg"
    png = FIGURES / "figure2_evidence_summary_v19.png"
    fig.savefig(svg, bbox_inches="tight")
    fig.savefig(png, dpi=220, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {svg}")
    print(f"wrote {png}")


if __name__ == "__main__":
    main()
