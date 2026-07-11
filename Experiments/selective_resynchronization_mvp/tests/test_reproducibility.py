import torch

from src.models import build_model
from src.utils import set_global_seed


def test_seeded_initialization_reproducible():
    set_global_seed(1234)
    first = build_model()
    first_state = [parameter.detach().clone() for parameter in first.parameters()]
    set_global_seed(1234)
    second = build_model()
    second_state = [parameter.detach().clone() for parameter in second.parameters()]
    assert all(torch.equal(a, b) for a, b in zip(first_state, second_state, strict=True))
