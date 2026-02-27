from pathlib import Path
import csv
import math
from collections import defaultdict


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data" / "unified_srt_mtor_real_stim.csv"
CACHE_MANIFEST = ROOT / "data" / "raw" / "allen" / "ecephys_cache" / "manifest.json"
SESSION_ID = 715093703
DT = 0.05
MAX_T = 600.0
N_UNITS = 5


def bin_spikes(spike_times, T, dt):
    n = int(T / dt)
    counts = [0] * n
    for t in spike_times:
        if 0 <= t < T:
            i = int(t // dt)
            if 0 <= i < n:
                counts[i] += 1
    return counts


def build_bin_stimulus(stim_table, T, dt):
    n = int(T / dt)
    stim = ["unknown"] * n
    st = stim_table[["start_time", "stop_time", "stimulus_name"]].sort_values("start_time")
    rows = list(st.itertuples(index=False, name=None))

    j = 0
    for i in range(n):
        t = i * dt
        while j < len(rows) and rows[j][1] <= t:
            j += 1
        if j < len(rows) and rows[j][0] <= t < rows[j][1]:
            stim[i] = str(rows[j][2])
        else:
            stim[i] = "unknown"
    return stim


def zscore_map(d):
    vals = list(d.values())
    if not vals:
        return {k: 0.0 for k in d}
    m = sum(vals) / len(vals)
    v = sum((x - m) ** 2 for x in vals) / max(1, len(vals) - 1)
    s = math.sqrt(v) if v > 1e-12 else 1.0
    return {k: (x - m) / s for k, x in d.items()}


def main():
    from allensdk.brain_observatory.ecephys.ecephys_project_cache import EcephysProjectCache

    cache = EcephysProjectCache.from_warehouse(manifest=str(CACHE_MANIFEST))
    session = cache.get_session_data(SESSION_ID)
    units = list(session.units.index[:N_UNITS])

    T = min(MAX_T, float(session.get_stimulus_table().stop_time.max()))
    n = int(T / DT)
    stim_by_bin = build_bin_stimulus(session.get_stimulus_table(), T, DT)

    fields = [
        "dataset_id","subject_id","session_id","circuit_id","t_sec","dt_sec",
        "spike_count","x_mtor_proxy","u_observer","condition","split"
    ]

    rows_out = []

    for unit_id in units:
        counts = bin_spikes(session.spike_times[unit_id], T, DT)

        # build per-stimulus utility from TRAIN TIME windows only (first 70% bins)
        cutoff_train = int(0.70 * n)
        agg = defaultdict(list)
        for i in range(cutoff_train):
            agg[stim_by_bin[i]].append(counts[i])
        mean_by_stim = {k: (sum(v) / len(v)) for k, v in agg.items() if len(v) > 0}
        uz_map = zscore_map(mean_by_stim)

        for i, c in enumerate(counts):
            t = i * DT
            stim = stim_by_bin[i]
            u = uz_map.get(stim, 0.0)

            if i < int(0.70 * n):
                split = "train"
            elif i < int(0.85 * n):
                split = "valid"
            else:
                split = "test"

            rows_out.append({
                "dataset_id": "allen_vcnp_real",
                "subject_id": str(session.specimen_name),
                "session_id": str(SESSION_ID),
                "circuit_id": str(unit_id),
                "t_sec": round(t, 4),
                "dt_sec": DT,
                "spike_count": int(c),
                "x_mtor_proxy": "",
                "u_observer": round(float(u), 6),
                "condition": stim,
                "split": split,
            })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows_out)

    print(f"wrote {OUT}")
    print(f"rows={len(rows_out)}")


if __name__ == "__main__":
    main()
