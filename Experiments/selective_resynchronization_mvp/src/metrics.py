from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable

import numpy as np
import torch
import torch.nn.functional as F
from torch import nn
from torch.utils.data import DataLoader

from .representations import representation_coherence


CHANGED_CLASSES = (0, 2, 4, 6)
UNCHANGED_CLASSES = (1, 3, 5, 7, 8, 9)


@dataclass
class Evaluation:
    loss: float
    accuracy: float
    balanced_accuracy: float
    changed_balanced_accuracy: float
    unchanged_balanced_accuracy: float
    predictive_entropy: float
    coherence: float
    labels: np.ndarray
    probabilities: np.ndarray
    representations: np.ndarray


def _balanced_accuracy(labels: np.ndarray, predictions: np.ndarray, classes: Iterable[int]) -> float:
    recalls = []
    for cls in classes:
        mask = labels == cls
        if np.any(mask):
            recalls.append(float(np.mean(predictions[mask] == labels[mask])))
    return float(np.mean(recalls)) if recalls else float("nan")


@torch.no_grad()
def evaluate(model: nn.Module, loader: DataLoader, device: torch.device) -> Evaluation:
    was_training = model.training
    model.eval()
    losses: list[float] = []
    all_labels: list[np.ndarray] = []
    all_probabilities: list[np.ndarray] = []
    all_representations: list[np.ndarray] = []
    for images, labels, _ in loader:
        images = images.to(device)
        labels = labels.to(device)
        logits, representations = model(images, return_representation=True)
        loss = F.cross_entropy(logits, labels, reduction="none")
        probabilities = torch.softmax(logits, dim=1)
        losses.extend(loss.detach().cpu().tolist())
        all_labels.append(labels.detach().cpu().numpy())
        all_probabilities.append(probabilities.detach().cpu().numpy())
        all_representations.append(representations.detach().cpu().numpy())
    labels_np = np.concatenate(all_labels)
    probabilities_np = np.concatenate(all_probabilities)
    representations_np = np.concatenate(all_representations)
    predictions = probabilities_np.argmax(axis=1)
    entropy = -np.sum(probabilities_np * np.log(probabilities_np + 1e-12), axis=1)
    result = Evaluation(
        loss=float(np.mean(losses)),
        accuracy=float(np.mean(predictions == labels_np)),
        balanced_accuracy=_balanced_accuracy(labels_np, predictions, range(10)),
        changed_balanced_accuracy=_balanced_accuracy(labels_np, predictions, CHANGED_CLASSES),
        unchanged_balanced_accuracy=_balanced_accuracy(labels_np, predictions, UNCHANGED_CLASSES),
        predictive_entropy=float(np.mean(entropy)),
        coherence=representation_coherence(representations_np, labels_np),
        labels=labels_np,
        probabilities=probabilities_np,
        representations=representations_np,
    )
    if was_training:
        model.train()
    return result


def parameter_snapshot(model: nn.Module) -> list[torch.Tensor]:
    return [parameter.detach().cpu().clone() for parameter in model.parameters()]


def parameter_distance(current: list[torch.Tensor], reference: list[torch.Tensor]) -> float:
    total = 0.0
    for a, b in zip(current, reference, strict=True):
        total += float(torch.sum((a.to(torch.float64) - b.to(torch.float64)) ** 2))
    return math.sqrt(total)


def group_parameter_distance(
    model: nn.Module,
    current: list[torch.Tensor],
    reference: list[torch.Tensor],
) -> tuple[float, float]:
    names = [name for name, _ in model.named_parameters()]
    trunk = 0.0
    head = 0.0
    for name, a, b in zip(names, current, reference, strict=True):
        value = float(torch.sum((a.to(torch.float64) - b.to(torch.float64)) ** 2))
        if name.startswith("classifier"):
            head += value
        else:
            trunk += value
    return math.sqrt(trunk), math.sqrt(head)


def predictive_kl(previous: np.ndarray, current: np.ndarray) -> float:
    p = np.clip(np.asarray(previous, dtype=np.float64), 1e-12, 1.0)
    q = np.clip(np.asarray(current, dtype=np.float64), 1e-12, 1.0)
    return float(np.mean(np.sum(p * (np.log(p) - np.log(q)), axis=1)))


def flat_gradient(model: nn.Module, images: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    model.zero_grad(set_to_none=True)
    logits = model(images)
    loss = F.cross_entropy(logits, labels)
    grads = torch.autograd.grad(loss, tuple(model.parameters()), retain_graph=False)
    return torch.cat([gradient.detach().flatten() for gradient in grads])


def gradient_disagreement(
    model: nn.Module,
    loader: DataLoader,
    device: torch.device,
    groups: int = 4,
) -> tuple[float, float]:
    was_training = model.training
    model.eval()
    gradients: list[torch.Tensor] = []
    for images, labels, _ in loader:
        images = images.to(device)
        labels = labels.to(device)
        gradients.append(flat_gradient(model, images, labels))
        if len(gradients) >= groups:
            break
    if len(gradients) < 2:
        raise RuntimeError("Gradient disagreement requires at least two fixed probe batches")
    cosines = []
    norms = []
    for gradient in gradients:
        norms.append(float(torch.linalg.vector_norm(gradient).detach().cpu()))
    for i in range(len(gradients)):
        for j in range(i + 1, len(gradients)):
            denom = torch.linalg.vector_norm(gradients[i]) * torch.linalg.vector_norm(gradients[j]) + 1e-12
            cosines.append(float((torch.dot(gradients[i], gradients[j]) / denom).detach().cpu()))
    if was_training:
        model.train()
    return float(1.0 - np.mean(cosines)), float(np.mean(norms))
