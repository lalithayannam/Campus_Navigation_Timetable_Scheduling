from __future__ import annotations

import json
import math
from pathlib import Path

from app.algorithms.graph import Graph
from app.algorithms.shortest_path import astar, dijkstra
from app.data_structures import Trie
from app.models import RouteResult


class CampusService:
    def __init__(self, data_path: str | Path) -> None:
        raw = json.loads(Path(data_path).read_text(encoding="utf-8"))
        self.coordinates = {
            item["name"]: (float(item["x"]), float(item["y"])) for item in raw["nodes"]
        }
        self.graph = Graph()
        for item in raw["nodes"]:
            self.graph.add_node(item["name"])
        for source, destination, weight in raw["edges"]:
            self.graph.add_edge(source, destination, float(weight))
        self.trie = Trie()
        for name in self.coordinates:
            self.trie.insert(name)

    def route(self, source: str, destination: str, algorithm: str) -> RouteResult:
        if source not in self.graph.adj or destination not in self.graph.adj:
            raise ValueError("Unknown campus location")

        if algorithm == "dijkstra":
            path, distance, visited = dijkstra(self.graph, source, destination)
            complexity = "O((V + E) log V) with a binary heap"
        elif algorithm == "astar":
            def heuristic(a: str, b: str) -> float:
                ax, ay = self.coordinates[a]
                bx, by = self.coordinates[b]
                return math.hypot(ax - bx, ay - by)

            path, distance, visited = astar(
                self.graph, source, destination, heuristic
            )
            complexity = "O((V + E) log V) worst-case; often fewer explored nodes"
        elif algorithm == "bfs":
            order = self.graph.bfs(source)
            if destination not in order:
                return RouteResult("bfs", [], float("inf"), len(order), "O(V + E)")
            # BFS is unweighted, so this is a hop-minimizing route.
            parent: dict[str, str] = {}
            seen = {source}
            queue = [source]
            for node in queue:
                if node == destination:
                    break
                for neighbor, _ in self.graph.neighbors(node):
                    if neighbor not in seen:
                        seen.add(neighbor)
                        parent[neighbor] = node
                        queue.append(neighbor)
            path = [destination]
            while path[-1] != source:
                path.append(parent[path[-1]])
            path.reverse()
            distance = sum(
                next(w for n, w in self.graph.neighbors(a) if n == b)
                for a, b in zip(path, path[1:])
            )
            visited = len(order)
            complexity = "O(V + E)"
        elif algorithm == "dfs":
            order = self.graph.dfs(source)
            if destination not in order:
                return RouteResult("dfs", [], float("inf"), len(order), "O(V + E)")
            path = [source]
            # DFS order is a traversal, not a guaranteed shortest path.
            previous: dict[str, str] = {}
            stack = [source]
            seen = {source}
            while stack:
                node = stack.pop()
                if node == destination:
                    break
                for neighbor, _ in reversed(list(self.graph.neighbors(node))):
                    if neighbor not in seen:
                        seen.add(neighbor)
                        previous[neighbor] = node
                        stack.append(neighbor)
            if destination not in previous and destination != source:
                return RouteResult("dfs", [], float("inf"), len(order), "O(V + E)")
            while path[-1] != destination:
                path.append(previous[path[-1]])
            distance = sum(
                next(w for n, w in self.graph.neighbors(a) if n == b)
                for a, b in zip(path, path[1:])
            )
            visited = len(order)
            complexity = "O(V + E)"
        else:
            raise ValueError("Unsupported algorithm")

        return RouteResult(algorithm, path, distance, visited, complexity)

    def search(self, query: str) -> list[str]:
        return self.trie.search_prefix(query)

    def campus(self) -> dict[str, object]:
        return {
            "nodes": [
                {"name": name, "x": xy[0], "y": xy[1]}
                for name, xy in self.coordinates.items()
            ],
            "edges": [
                {"source": a, "destination": b, "weight": w}
                for a, neighbors in self.graph.adj.items()
                for b, w in neighbors
                if a < b
            ],
        }
