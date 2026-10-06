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

def test_edge_direction():
    my_graph = {
        "A": {"B": 1},
        "B": {},
    }
    shortest_path = dijkstra(my_graph, "B")
    assert shortest_path == {"A": float("inf"), "B": 0}

def test_visit_order():
    my_graph = {
        "A": {"B": 7, "C": 2},
        "B": {"D": 1},
        "C": {"B": 3, "D": 8},
        "D": {}
    }
    shortest_path = dijkstra(my_graph, "A")
    assert shortest_path == {"A": 0, "B": 5, "C": 2, "D": 6}