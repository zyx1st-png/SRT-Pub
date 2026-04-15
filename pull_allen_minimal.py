from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data" / "unified_srt_mtor_real.csv"
CACHE = ROOT / "data" / "raw" / "allen" / "ecephys_cache"


def append_rows(rows):
    fields = [
        "dataset_id","subject_id","session_id","circuit_id","t_sec","dt_sec",
        "spike_count","x_mtor_proxy","u_observer","condition","split"
    ]
    with open(OUT, "a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        for r in rows:
            w.writerow(r)


def bin_spikes(spike_times, T, dt):
    n = int(T / dt)
    counts = [0] * n
    for t in spike_times:
        if 0 <= t < T:
            idx = int(t // dt)
            if 0 <= idx < n:
                counts[idx] += 1
    return counts


def main():
    try:
        from allensdk.brain_observatory.ecephys.ecephys_project_cache import EcephysProjectCache
    except Exception as e:
        print(f"import allensdk failed: {e}")
        return

    CACHE.mkdir(parents=True, exist_ok=True)
    manifest = CACHE / "manifest.json"

    print("loading Allen cache...")
    cache = EcephysProjectCache.from_warehouse(manifest=str(manifest))
    sessions = cache.get_session_table()
    if sessions is None or len(sessions) == 0:
        print("no sessions found")
        return

    # choose first available session for minimal run
    session_id = int(sessions.index[0])
    print(f"selected session: {session_id}")

    session = cache.get_session_data(session_id)

    units = session.units
    if units is None or len(units) == 0:
        print("no units")
        return

    # take first 5 units to limit volume
    unit_ids = list(units.index[:5])
    print(f"units used: {len(unit_ids)}")

    # choose analysis window from available duration
    T = min(600.0, float(session.get_stimulus_table().stop_time.max()))  # up to 10 min
    dt = 0.05

    rows = []
    for ui, unit_id in enumerate(unit_ids):
        spk = session.spike_times[unit_id]
        counts = bin_spikes(spk, T=T, dt=dt)
        for k, c in enumerate(counts):
            t = k * dt
            # minimal observer utility from temporal block (placeholder until stimulus-specific mapping)
            u_obs = 1.0 if int(t // 2) % 2 == 0 else 0.2
            if ui < 3:
                split = "train"
            elif ui == 3:
                split = "valid"
            else:
                split = "test"

            rows.append({
                "dataset_id": "allen_vcnp_real",
                "subject_id": str(session.specimen_name),
                "session_id": str(session_id),
                "circuit_id": str(unit_id),
                "t_sec": round(t, 4),
                "dt_sec": dt,
                "spike_count": c,
                "x_mtor_proxy": "",
                "u_observer": u_obs,
                "condition": "allen_minimal",
                "split": split,
            })

    append_rows(rows)
    print(f"appended rows: {len(rows)}")
    print(f"output: {OUT}")


if __name__ == "__main__":
    main()
