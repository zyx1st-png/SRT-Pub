"""Generate the distribution-aware v19.1 E1-E4 evidence summary SVG.

This figure is descriptive. It deliberately avoids mean +/- SD for the
floor-dominated E2/E3 distributions. Confirmatory inference remains the
experiment-specific tests reported in the manuscript and committed result
records.
"""
from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results"
FIGURES = HERE / "figures"
OUT = FIGURES / "figure2_evidence_summary_v19_1.svg"


def load(name: str) -> dict:
    return json.loads((RESULTS / name).read_text(encoding="utf-8"))


def esc(value) -> str:
    return str(value).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def text(x, y, value, cls="small", anchor="start") -> str:
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" class="{cls}">{esc(value)}</text>'


def line(x1, y1, x2, y2, cls="axis") -> str:
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="{cls}"/>'


def count_gt(rows: list[dict], key: str, condition_key: str, condition: str, threshold=0.5) -> int:
    return sum(1 for r in rows if r[condition_key] == condition and float(r[key]) > threshold)


def y(value: float, lo: float, hi: float, top=38, bottom=230) -> float:
    value = min(max(float(value), lo), hi)
    return bottom - (value - lo) / (hi - lo) * (bottom - top)


def main() -> None:
    e1 = load("main_results.json")
    e2 = load("recoverability_gradient_results.json")
    e3 = load("consequence_recovery_results.json")
    e4 = load("consequence_scope_results_E4_confirmatory_record.json")

    e1_terminal = float(e1["post_coop"]["real"][0])
    e1_restore = float(e1["post_coop"]["resettable"][0])
    e1_terminal_gt = count_gt(e1["runs"], "post_coop", "regime", "real")

    e2_order = ["tau0", "tau5", "tau15", "tau_inf"]
    e2_labels = ["0", "5", "15", "inf"]
    e2_counts = [int(round(e2["condition_summaries"][c]["fraction_post_coop_gt_0_5"] * 30)) for c in e2_order]

    e3_order = ["k0", "k2", "k5", "k10"]
    e3_counts = [int(round(e3["condition_summaries"][c]["fraction_post_coop_gt_0_5"] * 30)) for c in e3_order]

    primary = e4["primary_scope_test"]
    diff_mean = float(primary["mean_shared_minus_individual_collapsed_over_latency"])
    diff_ci = primary["paired_bootstrap_95_ci"]
    diffs = [float(v) for v in primary["per_seed_collapsed_differences"]]
    diff_median = sorted(diffs)[len(diffs) // 2 - 1:len(diffs) // 2 + 1]
    diff_median = sum(diff_median) / 2.0
    n_positive = sum(v > 0 for v in diffs)

    parts = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1200" height="430" viewBox="0 0 1200 430">',
        '<rect width="1200" height="430" fill="white"/>',
        '<style>text{font-family:Arial,Helvetica,sans-serif;fill:#111}.title{font-size:18px;font-weight:700}.ptitle{font-size:14px;font-weight:700}.small{font-size:10px}.label{font-size:11px}.axis{stroke:#333;stroke-width:1}.grid{stroke:#ddd;stroke-width:.8}.mark{fill:#222}.iqr{stroke:#222;stroke-width:3}.median{stroke:#111;stroke-width:2}.ci{stroke:#111;stroke-width:2}</style>',
        text(600, 28, "E1-E4 evidence: large terminal phenomenon, failed scalar generalizations, modest scope effect", "title", "middle"),
    ]

    # E1
    ox, oy = 35, 65
    parts += [
        f'<g transform="translate({ox},{oy})">',
        '<rect x="0" y="0" width="255" height="275" fill="none" stroke="#333"/>',
        text(127.5, -15, "E1: terminal vs restore", "ptitle", "middle"),
        text(8, 18, "endpoint mean cooperation; scale 0-0.60"),
        line(38, 38, 38, 230), line(38, 230, 235, 230),
        f'<circle cx="95" cy="{y(e1_terminal, 0, .6):.1f}" r="6" class="mark"/>',
        f'<circle cx="180" cy="{y(e1_restore, 0, .6):.1f}" r="6" class="mark"/>',
        text(95, 250, "Terminal", "label", "middle"), text(180, 250, "Restore", "label", "middle"),
        text(95, 270, f"mean {e1_terminal:.3f}; {e1_terminal_gt}/30 > 0.5", "small", "middle"),
        text(180, 270, f"mean {e1_restore:.4f}", "small", "middle"),
        '</g>',
    ]

    # E2 / E3 median + IQR panels
    for ox, title, summaries, order, labels, counts in [
        (330, "E2: impairment duration", e2["condition_summaries"], e2_order, e2_labels, e2_counts),
        (625, "E3: individual recovery latency", e3["condition_summaries"], e3_order, e3_order, e3_counts),
    ]:
        parts += [
            f'<g transform="translate({ox},65)">',
            '<rect x="0" y="0" width="255" height="275" fill="none" stroke="#333"/>',
            text(127.5, -15, title, "ptitle", "middle"),
            text(8, 18, "median + IQR; magnified floor scale 0-0.007"),
            line(38, 38, 38, 230), line(38, 230, 235, 230),
        ]
        for i, (condition, label) in enumerate(zip(order, labels)):
            x = 68 + 44 * i
            s = summaries[condition]
            q1, q3 = map(float, s["iqr"])
            med = float(s["median"])
            parts += [
                line(x, y(q1, 0, .007), x, y(q3, 0, .007), "iqr"),
                line(x - 9, y(med, 0, .007), x + 9, y(med, 0, .007), "median"),
                text(x, 250, label, "label", "middle"),
            ]
        parts += [text(127.5, 270, ">0.5 seeds: " + ", ".join(f"{n}/30" for n in counts), "small", "middle"), '</g>']

    # E4 paired delta panel
    parts += [
        '<g transform="translate(920,65)">',
        '<rect x="0" y="0" width="245" height="275" fill="none" stroke="#333"/>',
        text(122.5, -15, "E4: shared - individual scope", "ptitle", "middle"),
        text(8, 18, "paired delta; DIFFERENT axis -0.06 to +0.30"),
        line(38, 38, 38, 230), line(38, y(0, -.06, .30), 225, y(0, -.06, .30)),
        line(120, y(diff_ci[0], -.06, .30), 120, y(diff_ci[1], -.06, .30), "ci"),
        line(112, y(diff_ci[0], -.06, .30), 128, y(diff_ci[0], -.06, .30), "ci"),
        line(112, y(diff_ci[1], -.06, .30), 128, y(diff_ci[1], -.06, .30), "ci"),
        f'<circle cx="120" cy="{y(diff_mean, -.06, .30):.1f}" r="5" class="mark"/>',
        line(104, y(diff_median, -.06, .30), 136, y(diff_median, -.06, .30), "median"),
        text(120, 250, f"mean {diff_mean:+.3f}", "label", "middle"),
        text(120, 266, f"95% CI [{diff_ci[0]:+.3f},{diff_ci[1]:+.3f}]", "small", "middle"),
        text(120, 282, f"median {diff_median:+.4f}; {n_positive}/30 positive", "small", "middle"),
        '</g>',
    ]

    parts += [
        text(600, 385, "E2/E3 medians and IQRs use magnified floor scales because rare high-cooperation attractors make mean +/- SD misleading.", "label", "middle"),
        text(600, 405, "Panels use explicitly different y-scales; confirmatory inference is experiment-specific and should not be read from visual distances across panels.", "small", "middle"),
        '</svg>',
    ]

    FIGURES.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(parts), encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
