from pathlib import Path
import csv
import math
from collections import defaultdict

SESSION_IDS = [715093703, 719161530, 721123822, 732592105, 737581020]
UNITS_PER_SESSION = 5
DT = 0.05
MAX_T = 600.0

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data" / "unified_srt_mtor_real_multi_condid.csv"
MANIFEST = ROOT / "data" / "raw" / "allen" / "ecephys_cache" / "manifest.json"


def bin_spikes(spike_times, T, dt):
    n = int(T / dt)
    counts = [0] * n
    for t in spike_times:
        if 0 <= t < T:
            i = int(t // dt)
            if 0 <= i < n:
                counts[i] += 1
    return counts


def zscore_map(d):
    vals = list(d.values())
    if not vals:
        return {k: 0.0 for k in d}
    m = sum(vals) / len(vals)
    v = sum((x - m) ** 2 for x in vals) / max(1, len(vals) - 1)
    s = math.sqrt(v) if v > 1e-12 else 1.0
    return {k: (x - m) / s for k, x in d.items()}


def build_bin_condition(stim_table, T, dt):
    n = int(T / dt)
    cond = ["0"] * n
    name = ["unknown"] * n

    st = stim_table[["start_time", "stop_time", "stimulus_condition_id", "stimulus_name"]].sort_values("start_time")
    rows = list(st.itertuples(index=False, name=None))

    j = 0
    for i in range(n):
        t = i * dt
        while j < len(rows) and rows[j][1] <= t:
            j += 1
        if j < len(rows) and rows[j][0] <= t < rows[j][1]:
            cond[i] = str(int(rows[j][2])) if rows[j][2] is not None else "0"
            name[i] = str(rows[j][3])
    return cond, name


def main():
    from allensdk.brain_observatory.ecephys.ecephys_project_cache import EcephysProjectCache

    cache = EcephysProjectCache.from_warehouse(manifest=str(MANIFEST))

    fields = [
        "dataset_id","subject_id","session_id","circuit_id","t_sec","dt_sec",
        "spike_count","x_mtor_proxy","u_observer","condition","split"
    ]

    rows_out = []

    for sidx, sid in enumerate(SESSION_IDS):
        print(f"session {sid} ...")
        session = cache.get_session_data(sid)
        units = list(session.units.index[:UNITS_PER_SESSION])

        T = min(MAX_T, float(session.get_stimulus_table().stop_time.max()))
        n = int(T / DT)
        cond_by_bin, name_by_bin = build_bin_condition(session.get_stimulus_table(), T, DT)

        for unit_id in units:
            counts = bin_spikes(session.spike_times[unit_id], T, DT)
            cutoff = int(0.7 * n)

            # U from train-only mean response per condition-id (finer than stimulus_name)
            agg = defaultdict(list)
            for i in range(cutoff):
                agg[cond_by_bin[i]].append(counts[i])
            mu_cond = {k: (sum(v) / len(v)) for k, v in agg.items() if len(v) > 0}
            uz = zscore_map(mu_cond)

            for i, c in enumerate(counts):
                t = i * DT
                cond = cond_by_bin[i]
                stim_name = name_by_bin[i]
                u = uz.get(cond, 0.0)

                # session-level split (robust leakage control)
                if sidx < int(0.6 * len(SESSION_IDS)):
                    split = "train"
                elif sidx < int(0.8 * len(SESSION_IDS)):
                    split = "valid"
                else:
                    split = "test"

                rows_out.append({
                    "dataset_id": f"allen_vcnp_real_multi|{stim_name}",
                    "subject_id": str(session.specimen_name),
                    "session_id": str(sid),
                    "circuit_id": str(unit_id),
                    "t_sec": round(t, 4),
                    "dt_sec": DT,
                    "spike_count": int(c),
                    "x_mtor_proxy": "",
                    "u_observer": round(float(u), 6),
                    "condition": cond,
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
