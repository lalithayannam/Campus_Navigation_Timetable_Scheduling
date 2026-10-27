# Intelligent Campus Navigation and Scheduling System

A complete educational project for the **Computational Thinking** course.

The system combines:
- campus graph navigation and shortest-path algorithms
- classroom/timetable scheduling
- custom data structures
- Pythonic programming
- object-oriented design and design patterns
- asyncio/threading/multiprocessing examples
- testing, coverage, mypy, Ruff, Black and GitHub Actions
- Docker support
- AI-pair programming documentation

## Main features

1. **Campus Navigation**
   - Dijkstra shortest path
   - A* shortest path
   - BFS and DFS traversal
   - route comparison
   - graph management

2. **Smart Timetable Scheduling**
   - conflict-free scheduling
   - greedy initial assignment
   - backtracking search
   - branch-and-bound optimization
   - room-capacity and teacher-conflict constraints

3. **Pythonic Data Structures**
   - Trie
   - MinHeap wrapper
   - UnionFind
   - SegmentTree
   - Graph
   - Priority Queue

4. **OOP Engineering**
   - dataclasses
   - type hints
   - ABC/protocol
   - Strategy
   - Factory
   - Observer
   - Singleton
   - Adapter
   - Decorator
   - Iterator
   - Command

5. **Concurrency**
   - asyncio
   - threading
   - multiprocessing
   - producer-consumer queue
   - async generators

6. **Quality**
   - pytest
   - Hypothesis
   - coverage
   - mypy strict
   - Ruff
   - Black
   - pre-commit
   - GitHub Actions
   - Docker

## Project structure

```text
intelligent_campus_navigation/
├── app/
│   ├── main.py
│   ├── api.py
│   ├── models.py
│   ├── patterns.py
│   ├── data_structures.py
│   ├── algorithms/
│   │   ├── graph.py
│   │   ├── shortest_path.py
│   │   └── scheduling.py
│   ├── services/
│   │   ├── campus_service.py
│   │   └── scheduling_service.py
│   └── concurrency/
│       └── tasks.py
├── frontend/
│   ├── index.html
│   ├── app.js
│   └── style.css
├── data/
│   └── campus.json
├── tests/
├── docs/
│   ├── architecture.md
│   ├── algorithms.md
│   └── ai_pair_programming.md
├── .github/workflows/ci.yml
├── Dockerfile
├── docker-compose.yml
├── pyproject.toml
└── requirements.txt
```

## Run locally

Python 3.11+ is recommended.

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

### Linux/macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## API examples

```text
GET  /api/campus
GET  /api/route?source=Main Gate&destination=Library&algorithm=dijkstra
GET  /api/route?source=Main Gate&destination=Library&algorithm=astar
POST /api/schedule/generate
GET  /api/schedule/sample
GET  /api/search?q=lib
```

## Test and quality commands

```bash
pytest
pytest --cov=app --cov-report=term-missing
mypy app
ruff check .
black --check .
```

## Docker

```bash
docker compose up --build
```

Then open:

```text
http://localhost:8000
```

## CO mapping

| CO | Implementation |
|---|---|
| CO1 | Dijkstra, A*, BFS, DFS, greedy, DP, backtracking, branch-and-bound, complexity docs |
| CO2 | Trie, heap, union-find, segment tree, comprehensions, generators, decorators, context manager |
| CO3 | dataclasses, generics, ABC/protocol, SOLID, 8 design patterns |
| CO4 | asyncio, threading, multiprocessing, producer-consumer, futures |
| CO5 | pytest, Hypothesis, coverage, mypy, Ruff, Black, CI, Docker |
| CO6 | AI-pair development workflow and post-mortem in `docs/ai_pair_programming.md` |

This is an educational project. Replace the sample campus data with your own college campus for the final submission.
