"""Generate the v19 E1-E4 evidence summary figure.

The figure is descriptive. Confirmatory inference remains the locked tests and
adjudications reported in the manuscript and result records. E1-E3 show
condition-level cooperation distributions; E4 deliberately uses a separate
scope-effect panel so the four experiments are not visually implied to form
one severity axis.
"""
from __future__ import annotations

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results"
FIGURES = HERE / "figures"


def load(name: str) -> dict:
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


def values(payload: dict, field: str, key: str, levels: list[str]) -> list[np.ndarray]:
    return [
        np.asarray([r[field] for r in payload["runs"] if r[key] == level], dtype=float)
        for level in levels
    ]


def draw_distribution_panel(
    ax,
    groups: list[np.ndarray],
    labels: list[str],
    title: str,
    seed: int,
) -> None:
    positions = np.arange(1, len(groups) + 1)
    ax.boxplot(
        groups,
        positions=positions,
        widths=0.55,
        patch_artist=False,
        showfliers=False,
        medianprops={"linewidth": 1.5},
        whiskerprops={"linewidth": 1.0},
        capprops={"linewidth": 1.0},
        boxprops={"linewidth": 1.0},
    )
    rng = np.random.default_rng(seed)
    for x, group in zip(positions, groups):
        jitter = rng.uniform(-0.12, 0.12, size=len(group))
        ax.scatter(np.full(len(group), x) + jitter, group, s=13, alpha=0.55, linewidths=0)
        ax.scatter(
            [x], [float(np.mean(group))], marker="D", s=26,
            facecolors="none", edgecolors="black", linewidths=1.0,
        )
    ax.set_xticks(positions)
    ax.set_xticklabels(labels)
    ax.set_ylim(-0.03, 1.03)
    ax.set_title(title, fontsize=10)
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
    ax.set_xticklabels(["Shared − individual"])
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

    e1_groups = values(e1, "post_coop", "regime", ["real", "resettable"])
    e2_groups = values(e2, "post_coop", "condition", ["tau0", "tau5", "tau15", "tau_inf"])
    e3_groups = values(e3, "post_coop", "condition", ["k0", "k2", "k5", "k10"])

    for group_set in (e1_groups, e2_groups, e3_groups):
        if any(len(g) != 30 for g in group_set):
            raise RuntimeError("expected exactly 30 confirmatory seeds per E1-E3 condition")

    primary = e4["primary_scope_test"]
    e4_diffs = np.asarray(primary["per_seed_collapsed_differences"], dtype=float)
    if len(e4_diffs) != 30:
        raise RuntimeError("expected exactly 30 collapsed E4 seed effects")
    e4_mean = float(primary["mean_shared_minus_individual_collapsed_over_latency"])
    e4_ci = tuple(float(x) for x in primary["paired_bootstrap_95_ci"])

    fig, axes = plt.subplots(1, 4, figsize=(14.2, 3.8))
    draw_distribution_panel(
        axes[0], e1_groups, ["Terminal", "Restore"], "E1: depletion transition", 1901
    )
    draw_distribution_panel(
        axes[1], e2_groups, ["0", "5", "15", "∞"], "E2: impairment duration", 1902
    )
    draw_distribution_panel(
        axes[2], e3_groups, ["0", "2", "5", "10"], "E3: individual recovery", 1903
    )
    draw_scope_panel(axes[3], e4_diffs, e4_ci, e4_mean)

    axes[0].set_ylabel("Post-withdrawal mutual cooperation")
    axes[1].set_xlabel("Subsequent impaired steps")
    axes[2].set_xlabel("Subsequent forced-Rest steps")

    axes[0].text(
        0.02, 0.98, "strong terminal effect", transform=axes[0].transAxes,
        va="top", fontsize=8,
    )
    axes[1].text(
        0.02, 0.98, "preregistered H1:\nnot supported", transform=axes[1].transAxes,
        va="top", fontsize=8,
    )
    axes[2].text(
        0.02, 0.98, "preregistered H1:\nopposite ordinal direction",
        transform=axes[2].transAxes, va="top", fontsize=8,
    )

    fig.suptitle(
        "E1-E4: distinct failure-transition tests and a bounded consequence-scope effect",
        fontsize=11,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.93))

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
