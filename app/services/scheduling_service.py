from __future__ import annotations

from app.algorithms.scheduling import (
    SchedulingInput,
    backtracking_schedule,
    branch_and_bound_schedule,
    greedy_schedule,
)
from app.models import Course, Room, TimeSlot, ScheduleResult


class SchedulingService:
    def sample_input(self) -> SchedulingInput:
        courses = [
            Course("CS101", "Python Programming", "Dr. Rao", 55),
            Course("CS202", "Algorithms", "Dr. Mehta", 45),
            Course("CS303", "Database Systems", "Dr. Rao", 35),
            Course("CS404", "Software Engineering", "Dr. Singh", 50),
            Course("CS505", "Artificial Intelligence", "Dr. Kumar", 30),
            Course("CS606", "Computer Networks", "Dr. Singh", 40),
        ]
        rooms = [
            Room("Room A", 60),
            Room("Room B", 50),
            Room("Lab 1", 40),
            Room("Lab 2", 35),
        ]
        slots = [
            TimeSlot("Monday", 1),
            TimeSlot("Monday", 2),
            TimeSlot("Tuesday", 1),
            TimeSlot("Tuesday", 2),
            TimeSlot("Wednesday", 1),
            TimeSlot("Wednesday", 2),
        ]
        return SchedulingInput(courses, rooms, slots)

    def generate(self, algorithm: str = "branch_and_bound") -> ScheduleResult:
        data = self.sample_input()
        if algorithm == "greedy":
            return greedy_schedule(data)
        if algorithm == "backtracking":
            return backtracking_schedule(data)
        if algorithm == "branch_and_bound":
            return branch_and_bound_schedule(data)
        raise ValueError("Unsupported scheduling algorithm")
