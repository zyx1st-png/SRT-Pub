import copy

from src.b_paths import configure_path
from src.models import build_model
from src.utils import set_global_seed, state_dict_sha256


def test_all_paths_start_from_identical_A_tensor_hash():
    set_global_seed(123)
    base = build_model().state_dict()
    expected = state_dict_sha256(base)
    for path in ["standard_full", "head_only", "replay_full", "head_reset_full"]:
        model = build_model()
        model.load_state_dict(copy.deepcopy(base))
        assert state_dict_sha256(model.state_dict()) == expected
        configure_path(model, path, seed=123)
