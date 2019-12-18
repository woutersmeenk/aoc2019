from intcode_comp import IntcodeComp
from collections import defaultdict


if __name__ == "__main__":
    lines = open("15.dat", "r").readlines()
    prog = list(map(int, lines[0].split(',')))

    seconds_per_frame = 0
    screen = defaultdict(lambda: 0)
    comp = IntcodeComp(prog)
