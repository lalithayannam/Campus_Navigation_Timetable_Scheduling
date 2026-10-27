from collections import deque
from typing import Iterable


class Graph:
    def __init__(self) -> None:
        self.adj: dict[str, list[tuple[str, float]]] = {}

    def add_node(self, node: str) -> None:
        self.adj.setdefault(node, [])

    def add_edge(self, a: str, b: str, weight: float) -> None:
        self.add_node(a)
        self.add_node(b)
        self.adj[a].append((b, weight))
        self.adj[b].append((a, weight))

    def neighbors(self, node: str) -> Iterable[tuple[str, float]]:
        return self.adj.get(node, [])

    def bfs(self, start: str) -> list[str]:
        if start not in self.adj:
            return []
        seen = {start}
        queue = deque([start])
        order: list[str] = []
        while queue:
            current = queue.popleft()
            order.append(current)
            for neighbor, _ in self.adj[current]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs(self, start: str) -> list[str]:
        if start not in self.adj:
            return []
        seen: set[str] = set()
        order: list[str] = []

        def visit(node: str) -> None:
            seen.add(node)
            order.append(node)
            for neighbor, _ in self.adj[node]:
                if neighbor not in seen:
                    visit(neighbor)

        visit(start)
        return order
