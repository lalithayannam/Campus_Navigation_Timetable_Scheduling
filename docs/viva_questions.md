# Viva Preparation

## CO1

**Why use Dijkstra?**
Because campus paths have weighted distances and the weights are non-negative.

**Why A*?**
Because campus locations have coordinates, allowing a geometric heuristic to guide the search.

**Why backtracking for scheduling?**
Because scheduling is a constraint satisfaction problem and choices may need to be undone.

**Why branch and bound?**
To search for the best schedule while pruning branches that cannot improve the current solution.

## CO2

**Why Trie?**
For fast prefix-based building search.

**Why heap?**
For priority queues and efficient minimum selection.

**Why generator?**
It provides lazy evaluation and avoids storing every generated item.

## CO3

**Why Strategy pattern?**
To switch between Dijkstra and A* without changing the service.

**Why Factory?**
To centralize creation of route strategies.

## CO4

**Why asyncio?**
For concurrent I/O-style tasks such as multiple status requests.

**Why multiprocessing?**
For CPU-bound work where multiple processes can bypass the CPython GIL.

## CO5

**Why unit tests?**
They isolate individual functions and make refactoring safer.

**Why property-based testing?**
It explores many generated inputs rather than only hand-written examples.

## CO6

**Was AI allowed to write everything?**
No. AI output was reviewed, tested and modified by the student. The student remains the reviewer of record.
