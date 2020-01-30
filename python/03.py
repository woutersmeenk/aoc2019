def calc_path_locations(wire):
    result = dict()
    x = 0
    y = 0
    steps = 0
    for instr in wire:
        direction = instr[0]
        x_dir = 0
        y_dir = 0
        if 'R' == direction:
            x_dir = 1
        elif 'L' == direction:
            x_dir = -1
        elif 'U' == direction:
            y_dir = 1
        elif 'D' == direction:
            y_dir = -1
        length = int(instr[1:])
        for i in range(length):
            steps += 1
            x += x_dir
            y += y_dir
            if (x, y) not in result:
                result[(x, y)] = steps
    return result


if __name__ == "__main__":
    wires = open("03.dat", "r").readlines()
    wire1_instrs = wires[0].split(',')
    wire2_instrs = wires[1].split(',')
    wire1_path = calc_path_locations(wire1_instrs)
    wire2_path = calc_path_locations(wire2_instrs)
    crossings = list(set(wire1_path) & set(wire2_path))

    def manhatten_dist(point):
        return abs(point[0]) + abs(point[1])

    print(f"Part 1: {min(map(manhatten_dist, crossings))}")

    def combined_steps(point):
        return wire1_path[point] + wire2_path[point]

    print(f"Part 2: {min(map(combined_steps, crossings))}")
