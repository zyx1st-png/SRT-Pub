import torch
from torch.utils.data import DataLoader, TensorDataset

from src.fisher import diagonal_empirical_fisher_burden
from src.models import build_model
from src.metrics import parameter_snapshot


def test_diagonal_empirical_fisher_is_nonnegative():
    model = build_model()
    previous = parameter_snapshot(model)
    with torch.no_grad():
        next(model.parameters()).add_(0.001)
    images = torch.randn(2, 1, 28, 28)
    labels = torch.tensor([0, 1])
    indices = torch.tensor([10, 11])
    loader = DataLoader(TensorDataset(images, labels, indices), batch_size=2)
    burden, count = diagonal_empirical_fisher_burden(
        model, loader, previous, torch.device("cpu"), expected_samples=2
    )
    assert count == 2
    assert burden >= 0.0
