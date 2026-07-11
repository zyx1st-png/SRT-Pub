from __future__ import annotations

import torch
from torch import nn
import torch.nn.functional as F


class LightCNN(nn.Module):
    def __init__(self, num_classes: int = 10) -> None:
        super().__init__()
        self.features = nn.Sequential(
            nn.Conv2d(1, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(32, 32, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.MaxPool2d(2),
        )
        self.classifier = nn.Linear(64, num_classes)

    def forward(self, x: torch.Tensor, return_representation: bool = False):
        x = self.features(x)
        representation = F.adaptive_avg_pool2d(x, output_size=1).flatten(1)
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
    return LightCNN(num_classes=10)


def count_parameters(model: nn.Module) -> int:
    return sum(parameter.numel() for parameter in model.parameters())
