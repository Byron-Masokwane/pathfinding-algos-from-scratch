# Visualise Dijkstra's shortest paths on a random weighted graph.

# Runs my from-scratch implementation, checks every distance against
# NetworkX's built-in Dijkstra, and saves a figure of the shortest-path
# tree to images/dijkstra_result.png.

import os
import random

import matplotlib.pyplot as plt
import networkx as nx

from pathfinder.dijkstra import dijkstra

SEED = 7
START = 0


def random_graph(n_nodes=8, edge_prob=0.25, seed=SEED):
    """A random directed graph with integer weights, as {node: {neighbour: weight}}."""
    rng = random.Random(seed)
    graph = {node: {} for node in range(n_nodes)}
    for u in range(n_nodes):
        for v in range(n_nodes):
            if u != v and rng.random() < edge_prob:
                graph[u][v] = rng.randint(1, 9)
    return graph


def shortest_path_tree(graph, costs):
    """Recover one predecessor per node: an edge u -> v lies on a shortest
    path if costs[u] + weight(u, v) == costs[v]."""
    tree = []
    for v in graph:
        if v == START or costs[v] == float("inf"):
            continue
        for u in graph:
            if v in graph[u] and costs[u] + graph[u][v] == costs[v]:
                tree.append((u, v))
                break
    return tree


def main():
    graph = random_graph()
    costs = dijkstra(graph, START)

    # Check against NetworkX
    G = nx.DiGraph()
    G.add_nodes_from(graph)
    for u, nbrs in graph.items():
        for v, w in nbrs.items():
            G.add_edge(u, v, weight=w)
    expected = nx.single_source_dijkstra_path_length(G, START)
    for node in graph:
        assert costs[node] == expected.get(node, float("inf")), node
    print(f"All {len(graph)} distances match NetworkX.")

    # Graph plot
    tree = shortest_path_tree(graph, costs)
    pos = nx.kamada_kawai_layout(G)
    fig, ax = plt.subplots(figsize=(10, 8))

    other_edges = [e for e in G.edges if e not in tree]
    nx.draw_networkx_edges(G, pos, edgelist=other_edges, edge_color="lightgrey",
                           arrows=True, arrowsize=12, ax=ax, connectionstyle="arc3,rad=0.08")
    nx.draw_networkx_edges(G, pos, edgelist=tree, edge_color="crimson", width=2.5,
                           arrows=True, arrowsize=18, ax=ax, connectionstyle="arc3,rad=0.08")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, "weight"),
                                 font_size=8, ax=ax, connectionstyle="arc3,rad=0.08")

    colours = ["gold" if n == START else
               ("lightgrey" if costs[n] == float("inf") else "skyblue") for n in G.nodes]
    nx.draw_networkx_nodes(G, pos, node_color=colours, node_size=900, edgecolors="black", ax=ax)
    labels = {n: f"{n}\nd={'∞' if costs[n] == float('inf') else costs[n]}" for n in G.nodes}
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=9, ax=ax)

    ax.set_title(f"Dijkstra from node {START}: shortest-path tree in red, "
                 f"d = shortest distance", fontsize=12)
    ax.axis("off")

    os.makedirs("images", exist_ok=True)
    plt.savefig("images/dijkstra_result.png", dpi=150, bbox_inches="tight")
    print("Saved images/dijkstra_result.png")


if __name__ == "__main__":
    main()