from __future__ import annotations

import numpy as np


def _center_features(x: np.ndarray) -> np.ndarray:
    x = np.asarray(x, dtype=np.float64)
    return x - x.mean(axis=0, keepdims=True)


def linear_cka(x: np.ndarray, y: np.ndarray, eps: float = 1e-12) -> float:
    x_c = _center_features(x)
    y_c = _center_features(y)
    cross = x_c.T @ y_c
    numerator = float(np.sum(cross * cross))
    x_norm = float(np.sqrt(np.sum((x_c.T @ x_c) ** 2)))
    y_norm = float(np.sqrt(np.sum((y_c.T @ y_c) ** 2)))
    value = numerator / (x_norm * y_norm + eps)
    return float(np.clip(value, 0.0, 1.0))


def representation_coherence(representations: np.ndarray, labels: np.ndarray, eps: float = 1e-12) -> float:
    x = np.asarray(representations, dtype=np.float64)
    y = np.asarray(labels, dtype=np.int64)
    global_mean = x.mean(axis=0, keepdims=True)
    total = float(np.sum((x - global_mean) ** 2))
    within = 0.0
    for cls in np.unique(y):
        subset = x[y == cls]
        if len(subset):
            within += float(np.sum((subset - subset.mean(axis=0, keepdims=True)) ** 2))
    return float(np.clip(1.0 - within / (total + eps), 0.0, 1.0))


def subspace_overlap(
    z_a: np.ndarray,
    z_open: np.ndarray,
    z_stable: np.ndarray,
    k: int = 8,
) -> float:
    delta_open = _center_features(np.asarray(z_open) - np.asarray(z_a))
    delta_stable = _center_features(np.asarray(z_stable) - np.asarray(z_a))
    _, _, vt_open = np.linalg.svd(delta_open, full_matrices=False)
    _, _, vt_stable = np.linalg.svd(delta_stable, full_matrices=False)
    k_eff = max(1, min(k, vt_open.shape[0], vt_stable.shape[0]))
    u_open = vt_open[:k_eff].T
    u_stable = vt_stable[:k_eff].T
    overlap = np.linalg.norm(u_open.T @ u_stable, ord="fro") ** 2 / k_eff
    return float(np.clip(overlap, 0.0, 1.0))


def temporal_permutation_overlaps(
    z_a: np.ndarray,
    z_open: np.ndarray,
    z_stable: np.ndarray,
    k: int,
    permutations: int,
    seed: int,
) -> np.ndarray:
    rng = np.random.default_rng(seed)
    values = []
    for _ in range(permutations):
        permuted = np.asarray(z_stable)[rng.permutation(len(z_stable))]
        values.append(subspace_overlap(z_a, z_open, permuted, k=k))
    return np.asarray(values, dtype=np.float64)
