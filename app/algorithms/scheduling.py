from __future__ import annotations

from dataclasses import dataclass
from typing import Callable

from app.models import Course, Room, ScheduledClass, ScheduleResult, TimeSlot


@dataclass(frozen=True)
class SchedulingInput:
    courses: list[Course]
    rooms: list[Room]
    slots: list[TimeSlot]


def _valid(
    course: Course,
    room: Room,
    slot: TimeSlot,
    assignments: list[ScheduledClass],
) -> bool:
    if room.capacity < course.students:
        return False
    for item in assignments:
        if item.slot == slot and (
            item.room.name == room.name or item.course.teacher == course.teacher
        ):
            return False
    return True


def greedy_schedule(data: SchedulingInput) -> ScheduleResult:
    assignments: list[ScheduledClass] = []
    # Greedy heuristic: schedule larger classes first.
    courses = sorted(data.courses, key=lambda c: c.students, reverse=True)
    for course in courses:
        placed = False
        for slot in data.slots:
            for room in sorted(data.rooms, key=lambda r: r.capacity):
                if _valid(course, room, slot, assignments):
                    assignments.append(ScheduledClass(course, room, slot))
                    placed = True
                    break
            if placed:
                break
    conflicts = [
        f"Could not schedule {course.code}"
        for course in data.courses
        if course.code not in {a.course.code for a in assignments}
    ]
    return ScheduleResult(assignments, conflicts, len(assignments), "greedy")


def backtracking_schedule(data: SchedulingInput) -> ScheduleResult:
    courses = sorted(data.courses, key=lambda c: c.students, reverse=True)
    assignments: list[ScheduledClass] = []

    def search(index: int) -> bool:
        if index == len(courses):
            return True
        course = courses[index]
        for slot in data.slots:
            for room in data.rooms:
                if _valid(course, room, slot, assignments):
                    assignments.append(ScheduledClass(course, room, slot))
                    if search(index + 1):
                        return True
                    assignments.pop()
        return False

    success = search(0)
    conflicts = [] if success else ["No complete conflict-free schedule exists."]
    return ScheduleResult(
        list(assignments), conflicts, float(len(assignments)), "backtracking"
    )


def branch_and_bound_schedule(data: SchedulingInput) -> ScheduleResult:
    courses = sorted(data.courses, key=lambda c: c.students, reverse=True)
    best: list[ScheduledClass] = []
    current: list[ScheduledClass] = []

    def bound(index: int) -> int:
        return len(current) + (len(courses) - index)

    def search(index: int) -> None:
        nonlocal best
        if index == len(courses):
            if len(current) > len(best):
                best = list(current)
            return
        if bound(index) <= len(best):
            return

        course = courses[index]
        for slot in data.slots:
            for room in data.rooms:
                if _valid(course, room, slot, current):
                    current.append(ScheduledClass(course, room, slot))
                    search(index + 1)
                    current.pop()

        # Branch where this course is not scheduled.
        search(index + 1)

    search(0)
    conflicts = [
        f"Could not schedule {course.code}"
        for course in data.courses
        if course.code not in {a.course.code for a in best}
    ]
    return ScheduleResult(
        best, conflicts, float(len(best)), "branch_and_bound"
    )
