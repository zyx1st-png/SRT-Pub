from __future__ import annotations

import math
from collections.abc import Iterator

import numpy as np
import torch
import torch.nn.functional as F
from torch import nn
from torch.utils.data import DataLoader


class ScientificFailure(RuntimeError):
    pass


def build_optimizer(model: nn.Module, settings: dict) -> torch.optim.Optimizer:
    return torch.optim.SGD(
        model.parameters(),
        lr=float(settings["lr"]),
        momentum=float(settings.get("momentum", 0.9)),
        weight_decay=float(settings.get("weight_decay", 0.0)),
    )


def _next_replay(iterator: Iterator, loader: DataLoader):
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
    losses: list[float] = []
    gradient_norms: list[float] = []
    replay_iterator = iter(replay_loader) if replay_loader is not None else None
    for images, labels, _ in loader:
        images = images.to(device)
        labels = labels.to(device)
        if replay_loader is not None and replay_fraction > 0:
            replay_batch, replay_iterator = _next_replay(replay_iterator, replay_loader)
            replay_images, replay_labels, _ = replay_batch
            replay_count = max(1, int(round(images.shape[0] * replay_fraction / (1.0 - replay_fraction))))
            images = torch.cat([images, replay_images[:replay_count].to(device)], dim=0)
            labels = torch.cat([labels, replay_labels[:replay_count].to(device)], dim=0)
        optimizer.zero_grad(set_to_none=True)
        logits = model(images)
        loss = F.cross_entropy(logits, labels)
        if not torch.isfinite(loss):
            raise ScientificFailure("Non-finite training loss")
        loss.backward()
        squared = torch.zeros((), device=device)
        for parameter in model.parameters():
            if parameter.grad is not None:
                squared = squared + torch.sum(parameter.grad.detach() ** 2)
        gradient_norm = float(torch.sqrt(squared).detach().cpu())
        optimizer.step()
        if any(not torch.isfinite(parameter).all() for parameter in model.parameters()):
            raise ScientificFailure("Non-finite model parameter")
        losses.append(float(loss.detach().cpu()))
        gradient_norms.append(gradient_norm)
    return {
        "train_loss": float(np.mean(losses)),
        "train_gradient_norm": float(np.mean(gradient_norms)),
        "learning_rate": float(optimizer.param_groups[0]["lr"]),
        "batches": float(len(losses)),
    }
