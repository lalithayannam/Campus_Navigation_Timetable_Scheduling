from __future__ import annotations

import heapq
import math
from typing import Callable

from .graph import Graph


def _reconstruct(previous: dict[str, str], start: str, goal: str) -> list[str]:
    if start == goal:
        return [start]
    if goal not in previous:
        return []
    path = [goal]
    while path[-1] != start:
        path.append(previous[path[-1]])
    path.reverse()
    return path


def dijkstra(graph: Graph, start: str, goal: str) -> tuple[list[str], float, int]:
    distances = {node: math.inf for node in graph.adj}
    distances[start] = 0.0
    previous: dict[str, str] = {}
    heap: list[tuple[float, str]] = [(0.0, start)]
    visited = 0

    while heap:
        distance, current = heapq.heappop(heap)
        if distance != distances[current]:
            continue
        visited += 1
        if current == goal:
            break
        for neighbor, weight in graph.neighbors(current):
            candidate = distance + weight
            if candidate < distances[neighbor]:
                distances[neighbor] = candidate
                previous[neighbor] = current
                heapq.heappush(heap, (candidate, neighbor))

    path = _reconstruct(previous, start, goal)
    return path, distances.get(goal, math.inf), visited


def astar(
    graph: Graph,
    start: str,
    goal: str,
    heuristic: Callable[[str, str], float],
) -> tuple[list[str], float, int]:
    g_score = {node: math.inf for node in graph.adj}
    g_score[start] = 0.0
    previous: dict[str, str] = {}
    heap: list[tuple[float, str]] = [(heuristic(start, goal), start)]
    visited = 0

    while heap:
        _, current = heapq.heappop(heap)
        visited += 1
        if current == goal:
            break
        for neighbor, weight in graph.neighbors(current):
            candidate = g_score[current] + weight
            if candidate < g_score[neighbor]:
                g_score[neighbor] = candidate
                previous[neighbor] = current
                score = candidate + heuristic(neighbor, goal)
                heapq.heappush(heap, (score, neighbor))

    return _reconstruct(previous, start, goal), g_score.get(goal, math.inf), visited
