from __future__ import annotations

TIMING_HOLD_PROFILES: dict[str, dict[int, int]] = {
    "agi": {
        83: 1848,
        88: 2485,
        94: 2265,
    },
    "insight": {
        45: 2200,
        47: 2400,
        83: 1800,
        88: 2000,
        94: 1800,
        101: 1400,
        112: 2200,
        118: 3000,
        126: 1200,
        127: 4000,
        128: 1400,
    },
}


def get_timing_holds(profile: str) -> dict[int, int]:
    if not profile or profile == "none":
        return {}
    return dict(TIMING_HOLD_PROFILES.get(profile, {}))
