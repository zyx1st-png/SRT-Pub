import numpy as np
import torch

from src.models import build_model
from src.representations import linear_cka, subspace_overlap


def test_model_and_representation_metric_shapes():
    model = build_model()
    logits, representation = model(torch.randn(8, 1, 28, 28), return_representation=True)
    assert logits.shape == (8, 10)
    assert representation.shape == (8, 64)
    x = representation.detach().numpy()
    y = x + 0.01 * np.random.default_rng(1).normal(size=x.shape)
    assert 0.0 <= linear_cka(x, y) <= 1.0
    assert 0.0 <= subspace_overlap(x, y, y + 0.01, k=4) <= 1.0
