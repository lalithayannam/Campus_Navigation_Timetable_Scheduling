from hypothesis import given, strategies as st

from app.algorithms.graph import Graph
from app.algorithms.shortest_path import dijkstra


@given(st.integers(min_value=0, max_value=100))
def test_self_route_distance_is_zero(value: int) -> None:
    graph = Graph()
    graph.add_node(str(value))
    path, distance, _ = dijkstra(graph, str(value), str(value))
    assert path == [str(value)]
    assert distance == 0
