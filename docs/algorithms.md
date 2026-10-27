# Algorithm Selection and Complexity

## Navigation

### BFS
Use when edges are effectively unweighted and minimum number of edges is required.

Complexity: **O(V + E)**.

### DFS
Useful for traversal, connectivity and exploration.

Complexity: **O(V + E)**.

### Dijkstra
Use for weighted graphs with non-negative edge weights.

With a binary heap: **O((V + E) log V)**.

### A*
Use when coordinates or a useful heuristic are available.

Worst-case is similar to Dijkstra, while a good admissible heuristic can reduce explored nodes.

## Scheduling

### Greedy
Quick initial solution. It schedules larger classes first and chooses the first feasible room/time.

Typical complexity depends on C courses, R rooms and T slots: approximately **O(C × T × R × C)** due to conflict checking.

### Backtracking
Explores feasible assignments and stops after finding a complete schedule.

Worst case is exponential: roughly **O((T × R)^C)**.

### Branch and Bound
Searches the solution tree while pruning branches that cannot beat the current best solution.

Worst case remains exponential, but pruning can substantially reduce practical search.

## Other computational-thinking patterns

- Divide and conquer: merge-sort style sorting can be used for ranking/search preprocessing.
- Dynamic programming: can be added for weighted room/resource allocation or interval scheduling.
- Greedy: implemented in the scheduler.
- Backtracking: implemented in scheduler.
- Branch and bound: implemented in scheduler.

## Why not force every pattern into every feature?

An engineering project should use a pattern where it is appropriate. The documentation and viva should explain the decision rather than using an algorithm artificially.
