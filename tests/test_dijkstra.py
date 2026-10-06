from pathfinder.dijkstra import dijkstra

def test_simple_graph():
    my_graph = {
        "A": {"B": 4, "C": 1},
        "C": {"B": 2},
        "B": {}
    }
    shortest_path = dijkstra(my_graph, "A")
    assert shortest_path == {"A": 0, "C": 1, "B": 3}

def test_unreachable_node():
    my_graph = {
        "A": {"B": 4},
        "B": {},
        "Z": {"A": 1}
    }
    shortest_path = dijkstra(my_graph, "A")
    assert shortest_path == {"A": 0, "Z": float("inf"), "B": 4}