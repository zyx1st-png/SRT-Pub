from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable

import numpy as np
import torch
import torch.nn.functional as F
from torch import nn
from torch.utils.data import DataLoader


@dataclass
class Evaluation:
    loss: float
    accuracy: float
    balanced_accuracy: float
    ece: float
    predictive_entropy: float
    representation_coherence: float
    effective_rank: float
    inactive_unit_ratio: float
    labels: np.ndarray
    probabilities: np.ndarray
    representations: np.ndarray


def balanced_accuracy(labels: np.ndarray, predictions: np.ndarray, classes: Iterable[int] | None = None) -> float:
    class_values = sorted(np.unique(labels)) if classes is None else list(classes)
    recalls = []
    for value in class_values:
        mask = labels == value
        if np.any(mask):
            recalls.append(float(np.mean(predictions[mask] == labels[mask])))
    return float(np.mean(recalls)) if recalls else float("nan")


def expected_calibration_error(
    probabilities: np.ndarray,
    labels: np.ndarray,
    bins: int = 15,
    weights: np.ndarray | None = None,
) -> float:
    confidence = probabilities.max(axis=1)
    predictions = probabilities.argmax(axis=1)
    correct = (predictions == labels).astype(float)
    sample_weights = np.ones(len(labels), dtype=float) if weights is None else np.asarray(weights, dtype=float)
    edges = np.linspace(0.0, 1.0, bins + 1)
    total_weight = sample_weights.sum()
    value = 0.0
    for index in range(bins):
        lower, upper = edges[index], edges[index + 1]
        mask = (confidence > lower if index else confidence >= lower) & (confidence <= upper)
        if np.any(mask):
            weight = sample_weights[mask]
            bin_weight = weight.sum()
            accuracy = float(np.average(correct[mask], weights=weight))
            mean_confidence = float(np.average(confidence[mask], weights=weight))
            value += bin_weight / total_weight * abs(accuracy - mean_confidence)
    return float(value)


def linear_cka(x: np.ndarray, y: np.ndarray, eps: float = 1e-12) -> float:
    x = np.asarray(x, dtype=np.float64) - np.mean(x, axis=0, keepdims=True)
    y = np.asarray(y, dtype=np.float64) - np.mean(y, axis=0, keepdims=True)
    numerator = float(np.sum((x.T @ y) ** 2))
    denominator = math.sqrt(float(np.sum((x.T @ x) ** 2)) * float(np.sum((y.T @ y) ** 2)))
    return float(np.clip(numerator / (denominator + eps), 0.0, 1.0))


def representation_coherence(representations: np.ndarray, labels: np.ndarray) -> float:
    values = np.asarray(representations, dtype=np.float64)
    total = float(np.sum((values - values.mean(axis=0, keepdims=True)) ** 2))
    within = 0.0
    for label in np.unique(labels):
        subset = values[labels == label]
        within += float(np.sum((subset - subset.mean(axis=0, keepdims=True)) ** 2))
    return float(np.clip(1.0 - within / (total + 1e-12), 0.0, 1.0))


def effective_rank(representations: np.ndarray) -> float:
    centered = np.asarray(representations, dtype=np.float64)
    centered -= centered.mean(axis=0, keepdims=True)
    singular = np.linalg.svd(centered, compute_uv=False)
    eigenvalues = singular**2
    probabilities = eigenvalues / (eigenvalues.sum() + 1e-12)
    entropy = -np.sum(probabilities * np.log(probabilities + 1e-12))
    return float(np.exp(entropy))


@torch.no_grad()
def evaluate(model: nn.Module, loader: DataLoader, device: torch.device) -> Evaluation:
    was_training = model.training
    model.eval()
    losses, labels_all, probabilities_all, reps_all, weights_all = [], [], [], [], []
    for images, labels, _, weights in loader:
        images = images.to(device)
        labels_device = labels.to(device)
        logits, representations = model(images, return_representation=True)
        probabilities = torch.softmax(logits, dim=1)
        per_sample = F.cross_entropy(logits, labels_device, reduction="none")
        losses.extend(per_sample.detach().cpu().tolist())
        labels_all.append(labels.numpy())
        probabilities_all.append(probabilities.detach().cpu().numpy())
        reps_all.append(representations.detach().cpu().numpy())
        weights_all.append(weights.numpy())
    labels_np = np.concatenate(labels_all)
    probabilities_np = np.concatenate(probabilities_all)
    representations_np = np.concatenate(reps_all)
    weights_np = np.concatenate(weights_all).astype(float)
    predictions = probabilities_np.argmax(axis=1)
    entropy = -np.sum(probabilities_np * np.log(probabilities_np + 1e-12), axis=1)
    inactive = np.mean(np.mean(np.abs(representations_np), axis=0) < 1e-4)
    result = Evaluation(
        loss=float(np.average(np.asarray(losses), weights=weights_np)),
        accuracy=float(np.average(predictions == labels_np, weights=weights_np)),
        balanced_accuracy=balanced_accuracy(labels_np, predictions),
        ece=expected_calibration_error(probabilities_np, labels_np, weights=weights_np),
        predictive_entropy=float(np.average(entropy, weights=weights_np)),
        representation_coherence=representation_coherence(representations_np, labels_np),
        effective_rank=effective_rank(representations_np),
        inactive_unit_ratio=float(inactive),
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
    return math.sqrt(
        sum(
            float(torch.sum((a.to(torch.float64) - b.to(torch.float64)) ** 2))
            for a, b in zip(current, reference, strict=True)
        )
    )


def group_parameter_distance(
    model: nn.Module,
    current: list[torch.Tensor],
    reference: list[torch.Tensor],
) -> tuple[float, float]:
    trunk = 0.0
    head = 0.0
    for (name, _), a, b in zip(model.named_parameters(), current, reference, strict=True):
        value = float(torch.sum((a.to(torch.float64) - b.to(torch.float64)) ** 2))
        if name.startswith("classifier"):
            head += value
        else:
            trunk += value
    return math.sqrt(trunk), math.sqrt(head)


def flat_gradient(model: nn.Module, images: torch.Tensor, labels: torch.Tensor) -> torch.Tensor:
    model.zero_grad(set_to_none=True)
    loss = F.cross_entropy(model(images), labels)
    gradients = torch.autograd.grad(loss, tuple(parameter for parameter in model.parameters() if parameter.requires_grad))
    return torch.cat([gradient.detach().flatten() for gradient in gradients])


def gradient_disagreement(
    model: nn.Module,
    loader: DataLoader,
    device: torch.device,
    groups: int = 4,
) -> tuple[float, float]:
    was_training = model.training
    model.eval()
    gradients = []
    for images, labels, _, _ in loader:
        gradients.append(flat_gradient(model, images.to(device), labels.to(device)))
        if len(gradients) == groups:
            break
    if len(gradients) < 2:
        raise RuntimeError("Gradient disagreement requires at least two batches")
    norms = [float(torch.linalg.vector_norm(value).cpu()) for value in gradients]
    similarities = []
    for left in range(len(gradients)):
        for right in range(left + 1, len(gradients)):
            denominator = torch.linalg.vector_norm(gradients[left]) * torch.linalg.vector_norm(gradients[right]) + 1e-12
            similarities.append(float((torch.dot(gradients[left], gradients[right]) / denominator).cpu()))
    if was_training:
        model.train()
    return float(1.0 - np.mean(similarities)), float(np.mean(norms))


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
    total = torch.zeros((), device=device, dtype=parameters[0].dtype)
    count = 0
    for images, labels, _, _ in loader:
        images = images.to(device)
        labels = labels.to(device)
        for offset in range(len(images)):
            log_probability = torch.log_softmax(model(images[offset : offset + 1]), dim=1)[0, labels[offset]]
            gradients = torch.autograd.grad(log_probability, parameters)
            total += sum(torch.sum(gradient.pow(2) * delta.pow(2)) for gradient, delta in zip(gradients, deltas, strict=True))
            count += 1
    if count != expected_samples:
        raise RuntimeError(f"Fisher count mismatch: {count} != {expected_samples}")
    burden = 0.5 * float((total / count).detach().cpu())
    if not math.isfinite(burden) or burden < -1e-10:
        raise FloatingPointError(f"Invalid empirical-Fisher burden: {burden}")
    if was_training:
        model.train()
    return max(0.0, burden), count
