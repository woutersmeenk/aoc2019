from intcode_comp import IntcodeComp


def neighbores(loc):
    result = list()
    result.append((loc[0] + 0, loc[1] - 1))  # North
    result.append((loc[0] + 0, loc[1] + 1))  # South
    result.append((loc[0] - 1, loc[1] + 0))  # West
    result.append((loc[0] + 1, loc[1] + 0))  # East
    return result


if __name__ == "__main__":
    lines = open("17.dat", "r").readlines()
    prog = list(map(int, lines[0].split(',')))
    comp = IntcodeComp(prog)
    out = comp.run_until_input([])
    map_str = ''.join(map(chr, out))
    map_lines = map_str.split("\n")
    align_param = 0
    for y in range(1, 45-1):
        for x in range(1, 38-1):
            cross = map_lines[y][x] == '#' and all(map_lines[neig[1]][neig[0]] ==
                                                   '#' for neig in neighbores((x, y)))
            if cross:
                align_param += (x*y)

    print(f"Part 1: {align_param}")
    comp = IntcodeComp(prog)
    comp.mem[0] = 2
    in_data = []
    while not comp.halted:
        out = comp.run_until_input(in_data)
        out_str = ''.join(map(chr, out))
        in_str = input(out_str)
        in_str += '\n'
        in_data = list(map(ord, in_str))
