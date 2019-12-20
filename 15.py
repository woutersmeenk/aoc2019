from intcode_comp import IntcodeComp
from graph_tools import *
from collections import defaultdict
import curses


def neighbores(loc):
    result = list()
    result.append((loc[0] + 0, loc[1] - 1))  # North
    result.append((loc[0] + 0, loc[1] + 1))  # South
    result.append((loc[0] - 1, loc[1] + 0))  # West
    result.append((loc[0] + 1, loc[1] + 0))  # East
    return result


def draw_screen(stdscr, loc_status, loc, dest_loc):
    term_max_y, term_max_x = curses.LINES - 1, curses.COLS - 2
    for y in range(0, term_max_y):
        for x in range(0, term_max_x):
            print_loc = (loc[0]+x-term_max_x//2, loc[1]+y-term_max_y//2)
            if loc == print_loc:
                stdscr.addch(y, x, 'D')
            elif dest_loc == print_loc:
                stdscr.addch(y, x, '@')
            else:
                stdscr.addch(y, x, loc_status[print_loc])
    stdscr.addch(term_max_y, term_max_x, ".")
    stdscr.refresh()


def main(stdscr):
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

    stdscr.clear()
    sys_loc = None
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
            loc_status[new_loc] = 'O'
            loc = new_loc
            sys_loc = loc
            for neig in neighbores(loc):
                if loc_status[neig] != '#':
                    map_graph[loc].add(neig)
                    map_graph[neig].add(loc)
        dists = dijkstra(map_graph, loc)
        unvisted_dists = {l: dists[l]
                          for l in dists.keys() if loc_status[l] == ' '}
        if len(unvisted_dists) == 0:
            break
        dest_loc = min(unvisted_dists, key=unvisted_dists.get)
        next_on_path = dest_loc
        while dists[next_on_path] > 1:
            neig_dists = {neig: dists[neig]
                          for neig in neighbores(next_on_path) if neig in dists}
            next_on_path = min(neig_dists, key=neig_dists.get)
        loc_neigs = neighbores(loc)
        for d in range(4):
            if loc_neigs[d] == next_on_path:
                direction = d + 1
                break
        draw_screen(stdscr, loc_status, loc, dest_loc)

    dists = dijkstra(map_graph, sys_loc)
    stdscr.addstr(0, 0, f"Part 1: {dists[(0,0)]}")
    stdscr.getkey()

    ox_locs = [sys_loc]
    time = 0
    while len(ox_locs) > 0:
        time += 1
        new_ox_locs = []
        for ox_loc in ox_locs:
            for neig in neighbores(ox_loc):
                if loc_status[neig] == '.':
                    new_ox_locs.append(neig)
                    loc_status[neig] = 'O'
        ox_locs = new_ox_locs
        draw_screen(stdscr, loc_status, loc, None)
        stdscr.addstr(0, 0, f"Part 2: {time}")
    stdscr.getkey()


if __name__ == "__main__":
    curses.wrapper(main)
