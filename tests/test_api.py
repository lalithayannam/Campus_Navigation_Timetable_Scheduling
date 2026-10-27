from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_home() -> None:
    response = client.get("/")
    assert response.status_code == 200


def test_campus() -> None:
    response = client.get("/api/campus")
    assert response.status_code == 200
    assert "nodes" in response.json()


def test_route() -> None:
    response = client.get(
        "/api/route",
        params={
            "source": "Main Gate",
            "destination": "Library",
            "algorithm": "dijkstra",
        },
    )
    assert response.status_code == 200
    assert response.json()["path"]


def test_schedule() -> None:
    response = client.post(
        "/api/schedule/generate",
        json={"algorithm": "greedy"},
    )
    assert response.status_code == 200
