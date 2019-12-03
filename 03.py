from typing import *


def path(wire):
    result = dict()
    x = y = 0
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

    text_file = open("03.dat", "r")
    lines = text_file.readlines()
    wire1 = lines[0].split(',')
    wire2 = lines[1].split(',')
    wire1_path = path(wire1)
    wire2_path = path(wire2)
    crossings = list(set(wire1_path) & set(wire2_path))
    dists = [wire1_path[(x, y)] + wire2_path[(x, y)] for (x, y) in crossings]

    # print(f"{wire1_path}")
    # print(f"{wire2_path}")
    print(f"{crossings}")
    print(f"{dists}")
    print(f"{min(dists)}")
