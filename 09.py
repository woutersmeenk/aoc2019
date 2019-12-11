from intcode_comp import IntcodeComp

if __name__ == "__main__":
    lines = open("09.dat", "r").readlines()
    prog = list(map(int, lines[0].split(',')))

    comp = IntcodeComp(prog)
    out = comp.run([1])
    print(f"Part 1: {out}")

    comp = IntcodeComp(prog)
    out = comp.run([2])
    print(f"Part 2: {out}")
