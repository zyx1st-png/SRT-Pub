"""Generate the evidence-led v18 E1/E2/E3 distribution summary figure.

The figure is descriptive. Confirmatory inference remains the preregistered
statistics reported in the manuscript/result records. No values are hard-coded;
all plotted points are read from the committed first-run JSON files.
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
        np.asarray(
            [r[field] for r in payload["runs"] if r[key] == level],
            dtype=float,
        )
        for level in levels
    ]


def draw_panel(ax, groups: list[np.ndarray], labels: list[str], title: str, seed: int):
    positions = np.arange(1, len(groups) + 1)
    bp = ax.boxplot(
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
    _ = bp
    rng = np.random.default_rng(seed)
    for x, group in zip(positions, groups):
        jitter = rng.uniform(-0.12, 0.12, size=len(group))
        ax.scatter(np.full(len(group), x) + jitter, group, s=14, alpha=0.55, linewidths=0)
        ax.scatter([x], [float(np.mean(group))], marker="D", s=28, facecolors="none", edgecolors="black", linewidths=1.0)
    ax.set_xticks(positions)
    ax.set_xticklabels(labels)
    ax.set_ylim(-0.03, 1.03)
    ax.set_title(title, fontsize=10)
    ax.grid(axis="y", alpha=0.2, linewidth=0.6)


def main() -> None:
    e1 = load("main_results.json")
    e2 = load("recoverability_gradient_results.json")
    e3 = load("consequence_recovery_results.json")

    e1_groups = values(e1, "post_coop", "regime", ["real", "resettable"])
    e2_groups = values(e2, "post_coop", "condition", ["tau0", "tau5", "tau15", "tau_inf"])
    e3_groups = values(e3, "post_coop", "condition", ["k0", "k2", "k5", "k10"])

    for group_set in [e1_groups, e2_groups, e3_groups]:
        if any(len(g) != 30 for g in group_set):
            raise RuntimeError("expected exactly 30 paired confirmatory seeds per plotted condition")

    fig, axes = plt.subplots(1, 3, figsize=(11.2, 3.7), sharey=True)
    draw_panel(axes[0], e1_groups, ["Terminal", "Restore"], "E1: depletion transition", 1801)
    draw_panel(axes[1], e2_groups, ["0", "5", "15", "∞"], "E2: impairment duration", 1802)
    draw_panel(axes[2], e3_groups, ["0", "2", "5", "10"], "E3: recovery latency", 1803)

    axes[0].set_ylabel("Post-withdrawal mutual cooperation")
    axes[1].set_xlabel("Subsequent impaired steps")
    axes[2].set_xlabel("Subsequent forced-Rest steps")
    axes[0].text(0.02, 0.98, "strong terminal effect", transform=axes[0].transAxes, va="top", fontsize=8)
    axes[1].text(0.02, 0.98, "preregistered H1: not supported", transform=axes[1].transAxes, va="top", fontsize=8)
    axes[2].text(0.02, 0.98, "preregistered H1: opposite direction", transform=axes[2].transAxes, va="top", fontsize=8)

    fig.suptitle("Failure consequence architectures do not form one empirical severity axis", fontsize=11)
    fig.tight_layout(rect=(0, 0, 1, 0.94))

    FIGURES.mkdir(parents=True, exist_ok=True)
    svg = FIGURES / "figure2_evidence_summary_v18.svg"
    png = FIGURES / "figure2_evidence_summary_v18.png"
    fig.savefig(svg, bbox_inches="tight")
    fig.savefig(png, dpi=220, bbox_inches="tight")
    plt.close(fig)
    print(f"wrote {svg}")
    print(f"wrote {png}")


if __name__ == "__main__":
    main()
