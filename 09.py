from itertools import permutations
debug = True


class ZeroDefaultDict(dict):
    def __getitem__(self, key):
        return dict.get(self, key, 0)


class IntcodeComp(object):
    def __init__(self, prog):
        self._mem = ZeroDefaultDict()
        for i in range(len(prog)):
            self._mem[i] = prog[i]
        self._instrs = {
            1:      (4, "001", "Add", self._add),
            2:      (4, "001", "Mul", self._mul),
            3:      (2, "100", "In", self._input),
            4:      (2, "000", "Out", self._output),
            5:      (3, "000", "JIT", self._jump_true),
            6:      (3, "000", "JIF", self._jump_false),
            7:      (4, "001", "Less", self._less),
            8:      (4, "001", "Eq", self._eq),
            9:      (2, "000", "SetRelBase", self._set_rel_base),
        }
        self._pc = 0
        self._rel_base = 0

    def __str__(self):
        return str(self._mem)

    def _add(self, params):
        self._mem[params[2]] = params[0] + params[1]

    def _mul(self, params):
        self._mem[params[2]] = params[0] * params[1]

    def _input(self, params):
        self._mem[params[0]] = self._input_data.pop(0)

    def _output(self, params):
        self._output_data.append(params[0])

    def _jump_true(self, params):
        return params[1] if params[0] != 0 else None

    def _jump_false(self, params):
        return params[1] if params[0] == 0 else None

    def _less(self, params):
        self._mem[params[2]] = 1 if params[0] < params[1] else 0

    def _eq(self, params):
        self._mem[params[2]] = 1 if params[0] == params[1] else 0

    def _set_rel_base(self, params):
        self._rel_base = params[0]

    def _exec_instr(self):
        if debug:
            print(
                f"B {self._pc}\t{self._input_data}\t{self._output_data}\t{self._rel_base}")

        opcode = self._mem[self._pc]

        opcode_str = str(opcode).zfill(5)
        opcode = int(opcode_str[-2:])
        modes = opcode_str[::-1][2:]

        instr = self._instrs[opcode]
        width = instr[0]
        param_output = instr[1]
        name = instr[2]
        op = instr[3]

        params = []
        params_imm = []
        for i in range(width-1):
            param_imm = self._mem[self._pc + i + 1]
            params_imm.append(param_imm)
            if modes[i] == "0":
                param = self._mem[param_imm]
            elif modes[i] == "1":
                param = param_imm
            elif modes[i] == "2":
                param_imm = self._rel_base + param_imm
                param = self._mem[param_imm]

            if param_output[i] == "1":
                param = param_imm
            params.append(param)

        res = op(params)

        old_pc = self._pc
        if res is not None:
            self._pc = res
        else:
            self._pc += width
        if debug:
            print(
                f"A {self._pc}\t{self._input_data}\t{self._output_data}\t{self._rel_base}\t{name} {modes}\t\t{params_imm}\t{params}")

    def run_until_output(self, input):
        self._input_data = input
        self._output_data = []
        while self._mem[self._pc] != 99 and self._mem[self._pc] != 4:
            self._exec_instr()
        if self._mem[self._pc] == 4:
            self._exec_instr()
            return self._output_data
        else:
            return None

    def run(self, input):
        self._input_data = input
        self._output_data = []
        while self._mem[self._pc] != 99:
            self._exec_instr()
        return self._output_data


if __name__ == "__main__":
    lines = open("09.dat", "r").readlines()
    prog_str = lines[0]
    prog = list(map(int, prog_str.split(',')))
    comp = IntcodeComp(prog)
    print(comp.run([1]))
