from __future__ import annotations

from typing import Any

import numpy as np
import torch
from torch import nn
from torch.distributions import Categorical


class ActorCritic(nn.Module):
    def __init__(self, grid_channels: int = 7, state_dim: int = 9, action_dim: int = 5) -> None:
        super().__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(grid_channels, 16, kernel_size=3, padding=1),
            nn.Tanh(),
            nn.Conv2d(16, 16, kernel_size=3, padding=1),
            nn.Tanh(),
            nn.Flatten(),
        )
        self.trunk = nn.Sequential(
            nn.Linear(16 * 7 * 7 + state_dim, 128),
            nn.Tanh(),
            nn.Linear(128, 128),
            nn.Tanh(),
        )
        self.actor = nn.Linear(128, action_dim)
        self.critic = nn.Linear(128, 1)

    def forward(self, grid: torch.Tensor, state: torch.Tensor):
        if grid.ndim == 3:
            grid = grid.unsqueeze(0)
        if state.ndim == 1:
            state = state.unsqueeze(0)
        encoded = self.encoder(grid)
        representation = self.trunk(torch.cat([encoded, state], dim=-1))
        return self.actor(representation), self.critic(representation).squeeze(-1), representation

    def distribution(self, grid: torch.Tensor, state: torch.Tensor) -> Categorical:
        logits, _, _ = self.forward(grid, state)
        return Categorical(logits=logits)

    @torch.no_grad()
    def act(self, obs: dict[str, np.ndarray], *, deterministic: bool = False) -> tuple[int, float, float]:
        grid, state = obs_to_tensors(obs, next(self.parameters()).device)
        logits, value, _ = self.forward(grid, state)
        dist = Categorical(logits=logits)
        action = torch.argmax(logits, dim=-1) if deterministic else dist.sample()
        return int(action.item()), float(dist.log_prob(action).item()), float(value.item())


def obs_to_tensors(obs: dict[str, Any], device: torch.device | str) -> tuple[torch.Tensor, torch.Tensor]:
    grid = torch.as_tensor(np.asarray(obs["grid"]), dtype=torch.float32, device=device)
    state = torch.as_tensor(np.asarray(obs["state"]), dtype=torch.float32, device=device)
    return grid, state


def batch_observations(observations: list[dict[str, np.ndarray]]) -> dict[str, np.ndarray]:
    return {
        "grid": np.stack([obs["grid"] for obs in observations]).astype(np.float32),
        "state": np.stack([obs["state"] for obs in observations]).astype(np.float32),
    }


def parameter_vector(model: nn.Module) -> torch.Tensor:
    return torch.cat([parameter.detach().reshape(-1).cpu() for parameter in model.parameters()])
