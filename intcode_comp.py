
class ZeroDefaultDict(dict):
    def __getitem__(self, key):
        return dict.get(self, key, 0)


class IntcodeComp(object):
    def __init__(self, prog):
        self.debug = False
        self.halted = False
        self.need_input = False
        self.instr_exec = 0
        self.mem = ZeroDefaultDict()
        for i in range(len(prog)):
            self.mem[i] = prog[i]
        self.instrs = {
            1:      (4, "001", "Add", self.add),
            2:      (4, "001", "Mul", self.mul),
            3:      (2, "100", "In", self.input),
            4:      (2, "000", "Out", self.output),
            5:      (3, "000", "JIT", self.jump_true),
            6:      (3, "000", "JIF", self.jump_false),
            7:      (4, "001", "Less", self.less),
            8:      (4, "001", "Eq", self.eq),
            9:      (2, "000", "SetRelBase", self.set_rel_base),
            99:     (1, "000", "Halt", self.halt),
        }
        self.pc = 0
        self.rel_base = 0

    def __str__(self):
        return str(self.mem)

    def add(self, params):
        self.mem[params[2]] = params[0] + params[1]

    def mul(self, params):
        self.mem[params[2]] = params[0] * params[1]

    def input(self, params):
        if len(self.input_data) == 0:
            self.need_input = True
            return self.pc  # Exec instruction again later
        self.mem[params[0]] = self.input_data.pop(0)

    def output(self, params):
        self.output_data.append(params[0])

    def jump_true(self, params):
        return params[1] if params[0] != 0 else None

    def jump_false(self, params):
        return params[1] if params[0] == 0 else None

    def less(self, params):
        self.mem[params[2]] = 1 if params[0] < params[1] else 0

    def eq(self, params):
        self.mem[params[2]] = 1 if params[0] == params[1] else 0

    def set_rel_base(self, params):
        self.rel_base += params[0]

    def halt(self, params):
        self.halted = True
        return self.pc  # Dont move the pc

    def exec_instr(self):
        if self.debug:
            print(
                f"B {self.pc}\t{self.input_data}\t{self.output_data}\t{self.rel_base}")

        opcode = self.mem[self.pc]

        opcode_str = str(opcode).zfill(5)
        opcode = int(opcode_str[-2:])
        modes = opcode_str[::-1][2:]

        instr = self.instrs[opcode]
        width = instr[0]
        param_output = instr[1]
        name = instr[2]
        op = instr[3]

        params = []
        params_imm = []
        for i in range(width-1):
            param_imm = self.mem[self.pc + i + 1]
            params_imm.append(param_imm)
            if modes[i] == "0":
                param = self.mem[param_imm]
            elif modes[i] == "1":
                param = param_imm
            elif modes[i] == "2":
                param_imm = self.rel_base + param_imm
                param = self.mem[param_imm]

            if param_output[i] == "1":
                param = param_imm
            params.append(param)

        res = op(params)

        old_pc = self.pc
        if res is not None:
            self.pc = res
        else:
            self.pc += width
        if self.debug:
            print(
                f"A {self.pc}\t{self.input_data}\t{self.output_data}\t{self.rel_base}\t{name} {modes}\t\t{params_imm}\t{params}")
        self.instr_exec += 1

    def run_until_input(self, input):
        self.need_input = False
        self.input_data = input
        self.output_data = []
        while not self.halted and not self.need_input:
            self.exec_instr()
        return self.output_data

    def run(self, input):
        self.input_data = input
        self.output_data = []
        while self.mem[self.pc] != 99:
            self.exec_instr()
        return self.output_data
