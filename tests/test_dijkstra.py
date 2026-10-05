from pathfinder.dijkstra import dijkstra

def test_simple_graph():
    my_graph = {
        "A": {"B": 4, "C": 1},
        "C": {"B": 2},
        "B": {}
    }
    shortest_path = dijkstra(my_graph, "A")
    assert shortest_path == {"A": 0, "C": 1, "B": 3}