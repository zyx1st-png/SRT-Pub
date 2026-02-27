import csv
import math
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATASETS = [
    ROOT / "data" / "unified_srt_mtor_real_multi_condid.csv",
    ROOT / "data" / "unified_srt_mtor_real_multi_featureu.csv",
]


def corr(xs, ys):
    n = len(xs)
    if n < 3:
        return float("nan")
    mx = sum(xs) / n
    my = sum(ys) / n
    vx = sum((x - mx) ** 2 for x in xs)
    vy = sum((y - my) ** 2 for y in ys)
    if vx <= 1e-12 or vy <= 1e-12:
        return float("nan")
    c = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    return c / math.sqrt(vx * vy)


def summarize(path: Path):
    by_split = defaultdict(lambda: [[], []])
    by_ss = defaultdict(lambda: [[], []])

    with open(path, "r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        for row in r:
            if row["spike_count"] == "":
                continue
            u = float(row["u_observer"])
            y = float(row["spike_count"])
            sp = row["split"]
            sid = row["session_id"]

            by_split[sp][0].append(u)
            by_split[sp][1].append(y)
            by_ss[(sid, sp)][0].append(u)
            by_ss[(sid, sp)][1].append(y)

    lines = [f"# Audit: {path.name}", "", "## Split-level corr(u, spike_count)"]
    for sp in ["train", "valid", "test"]:
        xs, ys = by_split[sp]
        lines.append(f"- {sp}: n={len(xs)}, corr={corr(xs, ys):.6f}, mean_u={sum(xs)/len(xs):.6f}, mean_y={sum(ys)/len(ys):.6f}")

    lines += ["", "## Session x Split corr(u, spike_count)"]
    keys = sorted(by_ss.keys(), key=lambda z: (int(z[0]), z[1]))
    for sid, sp in keys:
        xs, ys = by_ss[(sid, sp)]
        lines.append(f"- sid={sid} split={sp}: n={len(xs)}, corr={corr(xs, ys):.6f}")

    return "\n".join(lines)


def main():
    out = []
    for p in DATASETS:
        if p.exists():
            out.append(summarize(p))
            out.append("\n---\n")

    target = ROOT / "observer_shift_audit.md"
    target.write_text("\n".join(out), encoding="utf-8")
    print(f"wrote {target}")


if __name__ == "__main__":
    main()
