import pandas as pd

from src.endpoint_matching import select_matched_group
from src.models import build_model, reset_head
from src.utils import state_dict_sha256


def test_head_reset_is_reproducible():
    first = build_model()
    second = build_model()
    reset_head(first, 999)
    reset_head(second, 999)
    assert state_dict_sha256(first.classifier.state_dict()) == state_dict_sha256(second.classifier.state_dict())
