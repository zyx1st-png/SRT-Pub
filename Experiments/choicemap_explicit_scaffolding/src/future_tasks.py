"""Held-out task templates and exact solvability checks."""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class FutureTask:
    task_id: str
    target_node: int
    required_resource: int | None
    family: str


def task_catalog() -> tuple[FutureTask, ...]:
    return tuple(
        FutureTask(
            task_id=f"future_{i}",
            target_node=8 + i,
            required_resource=(i % 3 if i < 6 else None),
            family=("resource" if i < 6 else "access"),
        )
        for i in range(8)
    )


def is_task_solvable(task: FutureTask, resources: tuple[int, ...], closed_nodes: frozenset[int]) -> bool:
    if task.target_node in closed_nodes:
        return False
    return task.required_resource is None or resources[task.required_resource] > 0

