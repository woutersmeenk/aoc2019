from graph_tools import *


if __name__ == "__main__":
    text_file = open("06.dat", "r")
    edges = [line.strip().split(')') for line in text_file.readlines()]

    graph = defaultdict(set)
    for (c, o) in edges:
        graph[c].add(o)
        graph[o].add(c)

    depths = dict()
    dfs(graph, 'COM', depths, 0)
    print(f"Part 1: {sum(depths.values())}")

    dists = dijkstra(graph, 'YOU')
    print(f"Part 2: {dists['SAN'] - 2}")
