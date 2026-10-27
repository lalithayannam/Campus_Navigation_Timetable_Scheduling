# Architecture

```text
                         Browser
                            |
                            v
                    FastAPI REST API
                            |
              +-------------+-------------+
              |                           |
              v                           v
      Campus Navigation              Scheduling
              |                           |
              v                           v
       Graph + Trie                Greedy / Backtracking
              |                    / Branch & Bound
              v                           |
        Dijkstra / A*                    v
              |                    Schedule Result
              +-------------+-------------+
                            |
                            v
                       Data Layer
```

## OOP layer

The domain objects are:
- Course
- Room
- TimeSlot
- ScheduledClass
- CampusNode
- Edge

The Strategy pattern isolates navigation algorithms. Factory selects a strategy.
Observer publishes application notifications.

## SOLID

- Single Responsibility: services, algorithms and models have separate responsibilities.
- Open/Closed: new route strategies can be added without changing the route service.
- Liskov Substitution: route strategies share the same abstract interface.
- Interface Segregation: small Observer protocol rather than a large interface.
- Dependency Inversion: services depend on strategy abstractions.

## Deployment

The Docker image runs Uvicorn and exposes port 8000.
