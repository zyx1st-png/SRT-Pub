import csv
import math
from collections import defaultdict
from pathlib import Path

INP = Path("data/unified_srt_mtor_real_multi_featureu.csv")
OUT = Path("data/unified_srt_mtor_real_multi_featureu_calib.csv")


def main():
    rows = []
    with open(INP, "r", encoding="utf-8") as f:
        r = csv.DictReader(f)
        fields = r.fieldnames
        for row in r:
            rows.append(row)

    # use TRAIN split global stats for calibration per condition key
    by_cond = defaultdict(list)
    for row in rows:
        if row["split"] == "train" and row["spike_count"] != "":
            by_cond[row["condition"]].append(float(row["u_observer"]))

    cond_stats = {}
    for k, v in by_cond.items():
        m = sum(v) / len(v)
        var = sum((x - m) ** 2 for x in v) / max(1, len(v) - 1)
        s = math.sqrt(var) if var > 1e-12 else 1.0
        cond_stats[k] = (m, s)

    # calibrate all splits using train-derived condition stats
    for row in rows:
        u = float(row["u_observer"])
        m, s = cond_stats.get(row["condition"], (0.0, 1.0))
        row["u_observer"] = f"{(u - m)/s:.6f}"

    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    print(f"wrote {OUT} rows={len(rows)}")


if __name__ == "__main__":
    main()
