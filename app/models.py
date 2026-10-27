from dataclasses import dataclass, field
from typing import Literal


@dataclass(frozen=True)
class CampusNode:
    name: str
    x: float
    y: float


@dataclass(frozen=True)
class Edge:
    source: str
    destination: str
    weight: float


@dataclass
class Course:
    code: str
    name: str
    teacher: str
    students: int


@dataclass(frozen=True)
class Room:
    name: str
    capacity: int


@dataclass(frozen=True)
class TimeSlot:
    day: str
    period: int


@dataclass
class ScheduledClass:
    course: Course
    room: Room
    slot: TimeSlot


AlgorithmName = Literal["dijkstra", "astar", "bfs", "dfs"]


@dataclass
class RouteResult:
    algorithm: str
    path: list[str]
    distance: float
    visited: int
    complexity: str


@dataclass
class ScheduleResult:
    assignments: list[ScheduledClass] = field(default_factory=list)
    conflicts: list[str] = field(default_factory=list)
    score: float = 0.0
    algorithm: str = ""
