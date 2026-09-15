"""Generate the compact v19 E1-E4 evidence summary SVG.

The figure is descriptive. Confirmatory inference remains the locked tests and
adjudications reported in the manuscript and result records. E1-E3 use
committed condition summaries. E4 uses all 30 latency-collapsed seed effects
plus the preregistered paired confidence interval.
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results"
FIGURES = HERE / "figures"
W, H = 1200, 360
PANEL_W, PANEL_H = 260, 210
TOP = 78
LEFTS = [60, 350, 640, 930]


def load(name: str) -> dict:
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


def esc(value) -> str:
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def line(x1, y1, x2, y2, stroke="#555", sw=1) -> str:
    return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" stroke-width="{sw}" />'


def text(x, y, value, size=12, anchor="middle", weight="normal") -> str:
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="Arial,Helvetica,sans-serif" '
        f'font-size="{size}" text-anchor="{anchor}" font-weight="{weight}">{esc(value)}</text>'
    )


def circle(x, y, r=4, fill="#222") -> str:
    return f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" />'


def y_map(value, top=TOP, height=PANEL_H, lo=0.0, hi=1.0) -> float:
    value = max(lo, min(hi, float(value)))
    return top + height - (value - lo) / (hi - lo) * height


def summary_panel(parts, left, title, labels, means, spreads, subtitle="") -> None:
    parts.append(f'<rect x="{left}" y="{TOP}" width="{PANEL_W}" height="{PANEL_H}" fill="none" stroke="#333" />')
    parts.append(text(left + PANEL_W / 2, TOP - 18, title, 14, weight="bold"))
    if subtitle:
        parts.append(text(left + 8, TOP + 18, subtitle, 11, anchor="start"))
    for tick in [0, 0.2, 0.4, 0.6, 0.8, 1.0]:
        y = y_map(tick)
        parts.append(line(left, y, left + PANEL_W, y, "#ddd", 0.8))
        parts.append(text(left - 8, y + 4, f"{tick:.1f}", 10, anchor="end"))
    n = len(labels)
    for i, (label, mean, spread) in enumerate(zip(labels, means, spreads)):
        x = left + (i + 1) * PANEL_W / (n + 1)
        y_low = y_map(max(0, mean - spread))
        y_high = y_map(min(1, mean + spread))
        y_mean = y_map(mean)
        parts.extend([
            line(x, y_low, x, y_high, "#555", 1.5),
            line(x - 5, y_low, x + 5, y_low, "#555", 1.5),
            line(x - 5, y_high, x + 5, y_high, "#555", 1.5),
            circle(x, y_mean, 4, "#111"),
            text(x, TOP + PANEL_H + 20, label, 11),
        ])


def scope_panel(parts, left, diffs, mean, ci) -> None:
    lo, hi = -0.06, 0.30
    parts.append(f'<rect x="{left}" y="{TOP}" width="{PANEL_W}" height="{PANEL_H}" fill="none" stroke="#333" />')
    parts.append(text(left + PANEL_W / 2, TOP - 18, "E4: consequence scope", 14, weight="bold"))
    parts.append(text(left + 8, TOP + 18, "preregistered support; modest", 11, anchor="start"))

    def ym(value):
        return y_map(value, lo=lo, hi=hi)

    for tick in [0, 0.1, 0.2, 0.3]:
        y = ym(tick)
        parts.append(line(left, y, left + PANEL_W, y, "#ddd", 0.8))
        parts.append(text(left - 8, y + 4, f"{tick:.1f}", 10, anchor="end"))
    parts.append(line(left, ym(0), left + PANEL_W, ym(0), "#555", 1.0))

    center = left + PANEL_W / 2
    offsets = [((i % 7) - 3) * 6 + ((i // 7) % 2) * 2 for i in range(len(diffs))]
    for offset, value in zip(offsets, diffs):
        parts.append(circle(center + offset, ym(value), 3, "#777"))

    y_low, y_high, y_mean = ym(ci[0]), ym(ci[1]), ym(mean)
    parts.extend([
        line(center, y_low, center, y_high, "#111", 2),
        line(center - 7, y_low, center + 7, y_low, "#111", 2),
        line(center - 7, y_high, center + 7, y_high, "#111", 2),
        f'<polygon points="{center},{y_mean - 5} {center + 5},{y_mean} {center},{y_mean + 5} {center - 5},{y_mean}" fill="#111" />',
        text(center, TOP + PANEL_H + 20, "Shared - individual", 11),
        text(left + PANEL_W / 2, TOP + PANEL_H + 39, "mean +0.030; 95% CI [+0.012, +0.054]", 10),
    ])


def main() -> None:
    e1 = load("main_results.json")
    e2 = load("recoverability_gradient_results.json")
    e3 = load("consequence_recovery_results.json")
    e4 = load("consequence_scope_results_E4_confirmatory_record.json")

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">',
        '<rect width="100%" height="100%" fill="white"/>',
        text(W / 2, 28, "E1-E4: distinct failure-transition tests and a bounded consequence-scope effect", 17, weight="bold"),
    ]

    summary_panel(
        parts, LEFTS[0], "E1: depletion transition", ["Terminal", "Restore"],
        [e1["post_coop"]["real"][0], e1["post_coop"]["resettable"][0]],
        [e1["post_coop"]["real"][1], e1["post_coop"]["resettable"][1]],
        "strong terminal effect",
    )

    e2_order = ["tau0", "tau5", "tau15", "tau_inf"]
    summary_panel(
        parts, LEFTS[1], "E2: impairment duration", ["0", "5", "15", "inf"],
        [e2["condition_summaries"][key]["mean"] for key in e2_order],
        [e2["condition_summaries"][key]["std"] for key in e2_order],
        "preregistered H1: not supported",
    )

    e3_order = ["k0", "k2", "k5", "k10"]
    summary_panel(
        parts, LEFTS[2], "E3: individual recovery", ["0", "2", "5", "10"],
        [e3["condition_summaries"][key]["mean"] for key in e3_order],
        [e3["condition_summaries"][key]["std"] for key in e3_order],
        "preregistered H1: opposite direction",
    )

    primary = e4["primary_scope_test"]
    scope_panel(
        parts, LEFTS[3], primary["per_seed_collapsed_differences"],
        primary["mean_shared_minus_individual_collapsed_over_latency"],
        primary["paired_bootstrap_95_ci"],
    )

    parts.append(text(600, 347, "E1-E3 show condition mean +/- 1 SD. E4 shows 30 collapsed seed effects and the paired 95% CI.", 10))
    parts.append("</svg>")

    FIGURES.mkdir(parents=True, exist_ok=True)
    out = FIGURES / "figure2_evidence_summary_v19.svg"
    out.write_text("\n".join(parts), encoding="utf-8")
    print(f"wrote {out}")


if __name__ == "__main__":
    main()
