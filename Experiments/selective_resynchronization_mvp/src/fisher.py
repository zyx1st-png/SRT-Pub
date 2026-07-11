from __future__ import annotations

import math

import torch
from torch import nn
from torch.utils.data import DataLoader


@torch.enable_grad()
def diagonal_empirical_fisher_burden(
    model: nn.Module,
    loader: DataLoader,
    previous_parameters: list[torch.Tensor],
    device: torch.device,
    expected_samples: int,
) -> tuple[float, int]:
    was_training = model.training
    model.eval()
    parameters = tuple(model.parameters())
    deltas = [
        parameter.detach() - previous.to(device=device, dtype=parameter.dtype)
        for parameter, previous in zip(parameters, previous_parameters, strict=True)
    ]
    accumulator_dtype = parameters[0].dtype
    total = torch.zeros((), device=device, dtype=accumulator_dtype)
    count = 0
    for images, labels, _ in loader:
        images = images.to(device)
        labels = labels.to(device)
        for offset in range(images.shape[0]):
            logits = model(images[offset : offset + 1])
            log_probability = torch.log_softmax(logits, dim=1)[0, labels[offset]]
            gradients = torch.autograd.grad(log_probability, parameters, retain_graph=False)
            sample_value = torch.zeros((), device=device, dtype=accumulator_dtype)
            for gradient, delta in zip(gradients, deltas, strict=True):
                sample_value = sample_value + torch.sum(
                    gradient.pow(2) * delta.pow(2)
                )
            total = total + sample_value
            count += 1
    if count != expected_samples:
        raise RuntimeError(f"Fisher sample count changed: expected {expected_samples}, got {count}")
    burden = 0.5 * float((total / count).detach().cpu())
    if not math.isfinite(burden):
        raise FloatingPointError("Non-finite empirical-Fisher burden")
    if burden < -1e-10:
        raise AssertionError(f"Empirical-Fisher burden is negative: {burden}")
    if was_training:
        model.train()
    return max(0.0, burden), count
