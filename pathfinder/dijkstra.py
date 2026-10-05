def dijkstra(graph, start):
    costs = {}
    for node in graph:
        cost = float("inf")
        costs[node] = cost
    costs[start] = 0

    return costs