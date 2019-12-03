

if __name__ == "__main__":
    instr_size = dict()
    instr_size[99] = 1
    instr_size[1] = 4
    instr_size[2] = 4
    instr_size[3] = 2
    instr_size[4] = 2
    instr_size[5] = 3
    instr_size[6] = 3
    instr_size[7] = 4
    instr_size[8] = 4

    text_file = open("05.dat", "r")
    lines = text_file.readlines()
    memory = lines[0].split(',')
    memory = [int(value) for value in memory]
    memory.append(0)
    memory.append(0)
    memory.append(0)
    memory.append(0)
    pc = 0
    while True:
        old_pc = pc
        op = memory[pc] % 100
        p1_mode = int(memory[pc] / 100) % 10
        p2_mode = int(memory[pc] / 1000) % 10
        p3_mode = int(memory[pc] / 10000) % 10
        p1_val = memory[pc+1]
        p2_val = memory[pc+2]
        p3_val = memory[pc+3]
        jumped = False
        if instr_size[op] > 1:
            p1 = p1_val if p1_mode == 1 else memory[p1_val]
        if instr_size[op] > 2:
            p2 = p2_val if p2_mode == 1 else memory[p2_val]
        if instr_size[op] > 3:
            p3 = p3_val if p3_mode == 1 else memory[p3_val]
        if op == 1:
            memory[p3_val] = p1 + p2
            print(
                f"{pc} Add[{p1_mode} {p2_mode}] {p1_val} {p2_val} : {p1} + {p2} = {memory[p3_val]} to {p3_val}")
        elif op == 2:
            memory[p3_val] = p1 * p2
            print(
                f"{pc} Mul[{p1_mode} {p2_mode}] {p1_val} {p2_val} : {p1} * {p2} = {memory[p3_val]} to {p3_val}")
        elif op == 3:
            memory[p1_val] = input = int(input("Input: "))
            print(f"{pc} In [{p1_mode}] {p1_val}: {memory[p1_val]}")
        elif op == 4:
            print(f"{pc} Out [{p1_mode}] {p1_val}: {p1}")
        elif op == 5:
            if p1 != 0:
                pc = p2
                jumped = True
            print(
                f"{old_pc} JNZ [{p1_mode} {p2_mode}] {p1_val} {p2_val} : {p1} {p2} jump to: {pc}")
        elif op == 6:
            if p1 == 0:
                pc = p2
                jumped = True
            print(
                f"{old_pc} JZ  [{p1_mode} {p2_mode}] {p1_val} {p2_val} : {p1} {p2} jump to: {pc}")
        elif op == 7:
            memory[p3_val] = 1 if p1 < p2 else 0
            print(
                f"{pc} <  [{p1_mode} {p2_mode}] {p1_val} {p2_val} : {p1} < {p2} = {memory[p3_val]} to {p3_val}")
        elif op == 8:
            memory[p3_val] = 1 if p1 == p2 else 0
            print(
                f"{pc} == [{p1_mode} {p2_mode}] {p1_val} {p2_val} : {p1} == {p2} = {memory[p3_val]} to {p3_val}")
        elif op == 99:
            print(f"{pc} Halt")
            break
        else:
            print("Something has gone wrong!")
            assert False
        if not jumped:
            pc += instr_size[op]
        #print(f"{pc} : {program}")
