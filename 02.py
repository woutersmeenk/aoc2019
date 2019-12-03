
if __name__ == "__main__":

    text_file = open("02.dat", "r")
    lines = text_file.readlines()
    program = lines[0].split(',')
    program = [int(value) for value in program]
    program[1] = 95
    program[2] = 7
    print(program)
    pc = 0
    while True:
        op = program[pc]
        if op != 99:
            in1_addr = program[pc+1]
            in2_addr = program[pc+2]
            out_addr = program[pc+3]
        if op == 1:
            in1 = program[in1_addr]
            in2 = program[in2_addr]
            program[out_addr] = in1 + in2
            print(
                f"{pc} Add {in1_addr} {in2_addr} : {in1} + {in2} = {program[out_addr]} to {out_addr}")
        elif op == 2:
            in1 = program[in1_addr]
            in2 = program[in2_addr]
            program[out_addr] = in1 * in2
            print(
                f"{pc} Mul {in1_addr} {in2_addr} : {in1} * {in2} = {program[out_addr]} to {out_addr}")
        elif op == 99:
            print(f"{pc} Halt")
            break
        else:
            print("Something has gone wrong!")
            assert False
        pc += 4
        #print(f"{pc} : {program}")

    print(f"{program[0]} diff {program[0] - 19690720}")
