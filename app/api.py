from __future__ import annotations

from pathlib import Path

from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel, Field

from app.services.campus_service import CampusService
from app.services.scheduling_service import SchedulingService

router = APIRouter(prefix="/api")
BASE_DIR = Path(__file__).resolve().parent.parent
campus_service = CampusService(BASE_DIR / "data" / "campus.json")
scheduling_service = SchedulingService()


class ScheduleRequest(BaseModel):
    algorithm: str = Field(
        default="branch_and_bound",
        pattern="^(greedy|backtracking|branch_and_bound)$",
    )


@router.get("/campus")
def campus() -> dict[str, object]:
    return campus_service.campus()


@router.get("/search")
def search(q: str = Query(min_length=1, max_length=50)) -> list[str]:
    return campus_service.search(q)


@router.get("/route")
def route(
    source: str,
    destination: str,
    algorithm: str = "dijkstra",
) -> dict[str, object]:
    try:
        result = campus_service.route(source, destination, algorithm)
        return {
            "algorithm": result.algorithm,
            "path": result.path,
            "distance": result.distance,
            "visited": result.visited,
            "complexity": result.complexity,
        }
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@router.get("/schedule/sample")
def sample_schedule() -> dict[str, object]:
    result = scheduling_service.generate("branch_and_bound")
    return _schedule_to_dict(result)


@router.post("/schedule/generate")
def generate_schedule(request: ScheduleRequest) -> dict[str, object]:
    try:
        result = scheduling_service.generate(request.algorithm)
        return _schedule_to_dict(result)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


def _schedule_to_dict(result) -> dict[str, object]:
    return {
        "algorithm": result.algorithm,
        "score": result.score,
        "conflicts": result.conflicts,
        "assignments": [
            {
                "course": a.course.code,
                "course_name": a.course.name,
                "teacher": a.course.teacher,
                "students": a.course.students,
                "room": a.room.name,
                "slot": f"{a.slot.day} - Period {a.slot.period}",
            }
            for a in result.assignments
        ],
    }
