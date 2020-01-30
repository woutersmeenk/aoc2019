from intcode_comp import IntcodeComp

if __name__ == "__main__":
    lines = open("02.dat", "r").readlines()
    prog = list(map(int, lines[0].split(',')))

    comp = IntcodeComp(prog)
    comp.mem[1] = 12
    comp.mem[2] = 2
    comp.run([])
    print(f"Part 1: {comp.mem[0]}")

    target = 19690720
    for noun in range(100):
        for verb in range(100):
            comp = IntcodeComp(prog)
            comp.mem[1] = noun
            comp.mem[2] = verb
            comp.run([])
            if comp.mem[0] == target:
                break
        if comp.mem[0] == target:
            break
    print(f"Part 2: {noun * 100 + verb}")
