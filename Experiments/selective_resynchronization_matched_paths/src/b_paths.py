from __future__ import annotations

from collections.abc import Iterator

import numpy as np
import torch
import torch.nn.functional as F
from torch import nn
from torch.utils.data import DataLoader

from .models import LightCNN, freeze_trunk, reset_head, unfreeze_all


PATHS = ["standard_full", "head_only", "replay_full", "head_reset_full"]


def configure_path(model: LightCNN, path: str, seed: int) -> None:
    if path not in PATHS:
        raise ValueError(f"Unknown B path: {path}")
    unfreeze_all(model)
    if path == "head_only":
        freeze_trunk(model)
    elif path == "head_reset_full":
        reset_head(model, seed + 700_000)


def build_optimizer(model: nn.Module, settings: dict) -> torch.optim.Optimizer:
    parameters = [parameter for parameter in model.parameters() if parameter.requires_grad]
    return torch.optim.SGD(
        parameters,
        lr=float(settings["lr"]),
        momentum=float(settings.get("momentum", 0.9)),
        weight_decay=float(settings.get("weight_decay", 0.0)),
    )


def _next(iterator: Iterator, loader: DataLoader):
    try:
        return next(iterator), iterator
    except StopIteration:
        iterator = iter(loader)
        return next(iterator), iterator


def train_epoch(
    model: nn.Module,
    loader: DataLoader,
    optimizer: torch.optim.Optimizer,
    device: torch.device,
    replay_loader: DataLoader | None = None,
    replay_fraction: float = 0.0,
) -> dict[str, float]:
    model.train()
    losses = []
    gradient_norms = []
    replay_iterator = iter(replay_loader) if replay_loader is not None else None
    for images, labels, _, _ in loader:
        images = images.to(device)
        labels = labels.to(device)
        if replay_loader is not None and replay_fraction > 0:
            replay_batch, replay_iterator = _next(replay_iterator, replay_loader)
            replay_images, replay_labels, _, _ = replay_batch
            count = max(1, int(round(len(images) * replay_fraction / (1 - replay_fraction))))
            images = torch.cat([images, replay_images[:count].to(device)])
            labels = torch.cat([labels, replay_labels[:count].to(device)])
        optimizer.zero_grad(set_to_none=True)
        loss = F.cross_entropy(model(images), labels)
        if not torch.isfinite(loss):
            raise FloatingPointError("Non-finite training loss")
        loss.backward()
        squared = torch.zeros((), device=device)
        for parameter in model.parameters():
            if parameter.grad is not None:
                squared += torch.sum(parameter.grad.detach() ** 2)
        gradient_norms.append(float(torch.sqrt(squared).cpu()))
        optimizer.step()
        if any(not torch.isfinite(parameter).all() for parameter in model.parameters()):
            raise FloatingPointError("Non-finite model parameter")
        losses.append(float(loss.detach().cpu()))
    return {
        "train_loss": float(np.mean(losses)),
        "train_gradient_norm": float(np.mean(gradient_norms)),
        "learning_rate": float(optimizer.param_groups[0]["lr"]),
        "batches": len(losses),
    }
