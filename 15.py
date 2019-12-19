from intcode_comp import IntcodeComp
from graph_tools import *
from collections import defaultdict


def neighbores(loc):
    result = list()
    result.append((loc[0] + 0, loc[1] - 1))  # North
    result.append((loc[0] + 0, loc[1] + 1))  # South
    result.append((loc[0] - 1, loc[1] + 0))  # West
    result.append((loc[0] + 1, loc[1] + 0))  # East
    return result


if __name__ == "__main__":
    lines = open("15.dat", "r").readlines()
    prog = list(map(int, lines[0].split(',')))

    map_graph = defaultdict(set)
    loc = (0, 0)
    for neig in neighbores(loc):
        map_graph[neig].add(loc)
        map_graph[loc].add(neig)
    comp = IntcodeComp(prog)
    direction = 1
    loc_status = defaultdict(lambda: ' ')
    loc_status[loc] = '.'

    while not comp.halted:
        new_loc = neighbores(loc)[direction - 1]
        droid_status = comp.run_until_input([direction])[0]
        if droid_status == 0:
            map_graph[loc].remove(new_loc)
            del map_graph[new_loc]
            loc_status[new_loc] = '#'
        elif droid_status == 1:
            loc_status[new_loc] = '.'
            loc = new_loc
            for neig in neighbores(loc):
                if loc_status[neig] != '#':
                    map_graph[loc].add(neig)
                    map_graph[neig].add(loc)
        elif droid_status == 2:
            break
        dists = dijkstra(map_graph, loc)
        unvisted_dists = {l: dists[l]
                          for l in dists.keys() if loc_status[l] == ' '}
        min_unvisted = min(unvisted_dists, key=unvisted_dists.get)
        next_on_path = min_unvisted
        while dists[next_on_path] > 1:
            neig_dists = {neig: dists[neig]
                          for neig in neighbores(next_on_path) if neig in dists}
            next_on_path = min(neig_dists, key=neig_dists.get)
        loc_neigs = neighbores(loc)
        for d in range(4):
            if loc_neigs[d] == next_on_path:
                direction = d + 1
                break

    print(f"Part 1 {dists[(0,0)]}")
