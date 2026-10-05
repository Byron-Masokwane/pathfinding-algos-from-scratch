def dijkstra(graph, start):
    costs = {}

    # initialise the starting node shortest path to 0
    # and all other nodes to unknown/infinity
    for node in graph:
        costs[node] = float("inf")
    costs[start] = 0

    visited = set()

    # determine the minimal path (cheapest) unvisited node
    # and mark it as visited
    while True:
        cheapest_unvisited = None
        cheapest_cost = float("inf")
        for node in costs:
            if node not in visited:
                if costs[node] < cheapest_cost:
                    cheapest_unvisited = node
                    cheapest_cost = costs[node]
        if cheapest_unvisited is None:
            break
        visited.add(cheapest_unvisited)

        for neighbour, edge_cost in graph[cheapest_unvisited].items():
            new_cost = costs[cheapest_unvisited] + edge_cost
            if new_cost < costs[neighbour]:
                costs[neighbour] = new_cost

    return start, costs