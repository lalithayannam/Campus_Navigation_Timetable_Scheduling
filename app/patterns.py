from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Callable, Protocol

from app.algorithms.graph import Graph
from app.algorithms.shortest_path import astar, dijkstra


# Strategy Pattern
class RouteStrategy(ABC):
    @abstractmethod
    def find(self, graph: Graph, start: str, goal: str) -> tuple[list[str], float, int]:
        ...


class DijkstraStrategy(RouteStrategy):
    def find(self, graph: Graph, start: str, goal: str) -> tuple[list[str], float, int]:
        return dijkstra(graph, start, goal)


class AStarStrategy(RouteStrategy):
    def __init__(self, coordinates: dict[str, tuple[float, float]]) -> None:
        self.coordinates = coordinates

    def find(self, graph: Graph, start: str, goal: str) -> tuple[list[str], float, int]:
        def h(a: str, b: str) -> float:
            ax, ay = self.coordinates[a]
            bx, by = self.coordinates[b]
            return ((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5

        return astar(graph, start, goal, h)


# Factory Pattern
class RouteStrategyFactory:
    @staticmethod
    def create(
        name: str, coordinates: dict[str, tuple[float, float]]
    ) -> RouteStrategy:
        if name == "astar":
            return AStarStrategy(coordinates)
        if name == "dijkstra":
            return DijkstraStrategy()
        raise ValueError(f"Unknown route strategy: {name}")


# Observer Pattern
class Observer(Protocol):
    def update(self, message: str) -> None:
        ...


class NotificationObserver:
    def __init__(self) -> None:
        self.messages: list[str] = []

    def update(self, message: str) -> None:
        self.messages.append(message)


class EventPublisher:
    def __init__(self) -> None:
        self._observers: list[Observer] = []

    def subscribe(self, observer: Observer) -> None:
        self._observers.append(observer)

    def publish(self, message: str) -> None:
        for observer in self._observers:
            observer.update(message)


# Singleton Pattern
class AppConfig:
    _instance: AppConfig | None = None

    def __new__(cls) -> AppConfig:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


# Adapter Pattern
class LegacyMapProvider:
    def get_distance(self, source: str, destination: str) -> str:
        return f"legacy-distance:{source}->{destination}"


class MapProviderAdapter:
    def __init__(self, legacy: LegacyMapProvider) -> None:
        self.legacy = legacy

    def distance(self, source: str, destination: str) -> str:
        return self.legacy.get_distance(source, destination)


# Decorator Pattern
def timed(function: Callable[..., object]) -> Callable[..., object]:
    import time
    from functools import wraps

    @wraps(function)
    def wrapper(*args: object, **kwargs: object) -> object:
        start = time.perf_counter()
        result = function(*args, **kwargs)
        wrapper.last_elapsed = time.perf_counter() - start  # type: ignore[attr-defined]
        return result

    wrapper.last_elapsed = 0.0  # type: ignore[attr-defined]
    return wrapper


# Iterator Pattern
@dataclass
class CampusIterator:
    items: list[str]
    index: int = 0

    def __iter__(self) -> CampusIterator:
        return self

    def __next__(self) -> str:
        if self.index >= len(self.items):
            raise StopIteration
        item = self.items[self.index]
        self.index += 1
        return item


# Command Pattern
class Command(ABC):
    @abstractmethod
    def execute(self) -> str:
        ...


class SearchCommand(Command):
    def __init__(self, query: str, search: Callable[[str], list[str]]) -> None:
        self.query = query
        self.search = search

    def execute(self) -> str:
        return ", ".join(self.search(self.query))
