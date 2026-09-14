import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CASES = json.loads((ROOT / "c0_transfer_cases.json").read_text(encoding="utf-8"))


def test_c0_has_both_target_domains():
    domains = {case["domain"] for case in CASES}
    assert "human_ai" in domains
    assert "organization" in domains


def test_c0_ids_are_unique():
    ids = [case["id"] for case in CASES]
    assert len(ids) == len(set(ids))


def test_c0_every_case_has_failure_target():
    for case in CASES:
        assert case["facts"]
        assert case["full_expected"]
        assert case["deletion_error"].strip()


def test_c0_covers_preregistered_deletion_families():
    joined = "\n".join(case["deletion_error"] for case in CASES)
    for required in [
        "shaping",
        "aggregate improvement",
        "performance gain",
        "policy adaptation",
        "higher-level standing",
    ]:
        assert required.lower() in joined.lower()
