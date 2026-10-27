from app.algorithms.graph import Graph
from app.algorithms.shortest_path import dijkstra


def build_graph() -> Graph:
    graph = Graph()
    graph.add_edge("A", "B", 2)
    graph.add_edge("B", "C", 3)
    graph.add_edge("A", "C", 10)
    return graph


def test_dijkstra() -> None:
    path, distance, visited = dijkstra(build_graph(), "A", "C")
    assert path == ["A", "B", "C"]
    assert distance == 5
    assert visited > 0


def test_bfs_dfs() -> None:
    graph = build_graph()
    assert graph.bfs("A")[0] == "A"
    assert graph.dfs("A")[0] == "A"
