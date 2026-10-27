from app.algorithms.scheduling import (
    SchedulingInput,
    backtracking_schedule,
    branch_and_bound_schedule,
    greedy_schedule,
)
from app.models import Course, Room, TimeSlot


def data() -> SchedulingInput:
    return SchedulingInput(
        [
            Course("A", "Algorithms", "T1", 20),
            Course("B", "Python", "T2", 15),
            Course("C", "Networks", "T1", 10),
        ],
        [Room("R1", 30), Room("R2", 20)],
        [TimeSlot("Mon", 1), TimeSlot("Mon", 2)],
    )


def test_greedy() -> None:
    result = greedy_schedule(data())
    assert len(result.assignments) == 3


def test_backtracking() -> None:
    result = backtracking_schedule(data())
    assert len(result.assignments) == 3


def test_branch_bound() -> None:
    result = branch_and_bound_schedule(data())
    assert len(result.assignments) == 3
