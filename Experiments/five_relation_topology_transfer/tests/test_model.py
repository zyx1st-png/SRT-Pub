from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from model import load_config, run_control_a, run_control_b


def config():
    return load_config(ROOT / "config_frozen_v1.json")


def test_control_a_pre_shift_is_exactly_matched():
    c = config()
    # Engineering/pilot seeds only; confirmatory 62000+ seeds stay untouched by tests.
    for seed in [51001, 51007, 52000, 52031]:
        ext = run_control_a(seed, "externalized", c)
        ret = run_control_a(seed, "returned_revision", c)
        assert ext["pre_reward"] == ret["pre_reward"]
        assert ext["pre_cost"] == ret["pre_cost"]
        assert ext["pre_alt_mass"] == ret["pre_alt_mass"]


def test_control_a_topology_only_changes_after_shift():
    c = config()
    ext = run_control_a(52000, "externalized", c)
    ret = run_control_a(52000, "returned_revision", c)
    assert ext["post_alt_mass_late"] != ret["post_alt_mass_late"]


def test_control_b_generator_revision_changes_generator():
    c = config()
    bp = run_control_b(53000, "policy_only", c)
    bg = run_control_b(53000, "generator_revision", c)
    assert bp["final_generator"] != bg["final_generator"]


def test_toy_model_makes_no_bearer_claim():
    text = (ROOT / "model.py").read_text(encoding="utf-8")
    assert "not SRT Bearers" in text
    assert "run_bearer" not in text
