from __future__ import annotations

import torch
import torch.nn.functional as F
from torch import nn


class LightCNN(nn.Module):
    def __init__(self) -> None:
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 32, 3, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 32, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.classifier = nn.Linear(64, 10)

    def forward(self, images: torch.Tensor, return_representation: bool = False):
        features = self.features(images)
        representation = F.adaptive_avg_pool2d(features, 1).flatten(1)
        logits = self.classifier(representation)
        if return_representation:
            return logits, representation
        return logits

    def parameter_groups(self) -> dict[str, list[nn.Parameter]]:
        return {
            "trunk": list(self.features.parameters()),
            "head": list(self.classifier.parameters()),
        }


def build_model() -> LightCNN:
    return LightCNN()


def freeze_trunk(model: LightCNN) -> None:
    for parameter in model.features.parameters():
        parameter.requires_grad_(False)
    for parameter in model.classifier.parameters():
        parameter.requires_grad_(True)


def unfreeze_all(model: LightCNN) -> None:
    for parameter in model.parameters():
        parameter.requires_grad_(True)


def reset_head(model: LightCNN, seed: int) -> None:
    devices = [] if not torch.cuda.is_available() else list(range(torch.cuda.device_count()))
    with torch.random.fork_rng(devices=devices):
        torch.manual_seed(seed)
        model.classifier.reset_parameters()
