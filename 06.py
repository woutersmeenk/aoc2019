def dfs(edges, v, depths, depth):
    depths[v] = depth
    for (c, o) in edges:
        if c == v and o not in depths:
            dfs(edges, o, depths, depth + 1)


def calc_dists(edges, s):
    # Borrowed from https://stackoverflow.com/questions/22897209/dijkstras-algorithm-in-python
    nodes = set([v for edge in edges for v in edge])

    unvisited = {node: None for node in nodes}  # using None as +inf
    visited = {}
    current = s
    currentDistance = 0
    unvisited[current] = currentDistance

    while True:
        for (c, o) in edges:
            if c == current:
                neighbour = o
            elif o == current:
                neighbour = c
            else:
                continue
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


if __name__ == "__main__":
    text_file = open("06.dat", "r")
    edges = [line.strip().split(')') for line in text_file.readlines()]

    depths = dict()
    dfs(edges, 'COM', depths, 0)
    print(f"Part 1: {sum(depths.values())}")

    dists = calc_dists(edges, 'YOU')
    print(f"Part 2: {dists['SAN'] - 2}")
