from collections import defaultdict


def dfs(graph, v, depths, depth):
    depths[v] = depth
    for o in graph[v]:
        if o not in depths:
            dfs(graph, o, depths, depth + 1)


def dijkstra(graph, source):
    # Borrowed from https://stackoverflow.com/questions/22897209/dijkstras-algorithm-in-python

    unvisited = {node: None for node in graph.keys()}
    visited = {}
    current = source
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for neighbour in graph[current]:
            if neighbour not in unvisited:
                continue
            newDistance = currentDistance + 1
            if unvisited[neighbour] is None or unvisited[neighbour] > newDistance:
                unvisited[neighbour] = newDistance
        visited[current] = currentDistance
        del unvisited[current]
        if not unvisited:
            break
        candidates = [node for node in unvisited.items() if node[1]]
        current, currentDistance = sorted(candidates, key=lambda x: x[1])[0]

    return visited
