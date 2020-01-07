from intcode_comp import IntcodeComp


if __name__ == "__main__":
    lines = open("19.dat", "r").readlines()
    prog = list(map(int, lines[0].split(',')))

    affected = 0
    for y in range(0, 50):
        for x in range(0, 50):
            comp = IntcodeComp(prog)
            out = comp.run([x, y])
            print('.' if out[0] == 0 else '#', end="")
            affected += out[0]
        print("")

    print(f"Part 1: {affected}")
