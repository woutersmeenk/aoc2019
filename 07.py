from itertools import permutations
debug = False

class IntcodeComp(object):
    def __init__(self, prog):
        self._mem = prog.copy()
        self._instrs = {
        #   opcode  width   param imm? Name     op
            1:      (4     ,"001"      ,"Add"   ,self._add ),
            2:      (4     ,"001"      ,"Mul"   ,self._mul ),
            3:      (2     ,"111"      ,"In"    ,self._input ),
            4:      (2     ,"011"      ,"Out"   ,self._output ),
            5:      (3     ,"001"      ,"JIT"   ,self._jump_true ),
            6:      (3     ,"001"      ,"JIF"   ,self._jump_false ),
            7:      (4     ,"001"      ,"Less"  ,self._less ),
            8:      (4     ,"001"      ,"Eq"    ,self._eq ),
        }
        self._pc = 0

    def __setitem__(self, key, value):
        self._mem[key] = value
    
    def __getitem__(self, key):
        if key < 0 or key >= len(self._mem):
            return 0
        return self._mem[key]
    
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
    
    def _jump_false(self , params):
        return params[1] if params[0] == 0 else None
    
    def _less(self , params):
        self._mem[params[2]] = 1 if params[0] < params[1] else 0
    
    def _eq(self, params):
        self._mem[params[2]] = 1 if params[0] == params[1] else 0

    def _exec_instr(self):    
        if debug:
            print(f"B {self._pc}\t{self._input_data}\t{self._output_data}")
     
        opcode = self._mem[self._pc]

        opcode_str = str(opcode).zfill(5)
        opcode = int(opcode_str[-2:])
        modes = opcode_str[::-1][2:]

        instr = self._instrs[opcode]
        width = instr[0]
        instr_modes = instr[1]
        name = instr[2]
        op = instr[3]

        params = []
        params_imm = []
        for i in range(width-1):
            param = self._mem[self._pc + i + 1]
            params_imm.append(param)
            if instr_modes[i] == "0" and modes[i] == "0":
                param = self._mem[param]
            params.append(param)
        
        res = op(params)

        old_pc = self._pc
        if res is not None:
            self._pc = res
        else:
            self._pc += width
        if debug:
            print(f"A {self._pc}\t{self._input_data}\t{self._output_data}\t{name} {modes}\t\t{params_imm}\t{params}")

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
        

def run_amps(prog, phases):
    comps = []
    phases_supplied = []
    for i in range(5):
        comps.append(IntcodeComp(prog))
        phases_supplied.append(False)
    current = 0
    out = [0]
    prev_out = None
    while out is not None:
        in_data = []
        if not phases_supplied[current]:
            phases_supplied[current] = True
            in_data.append(phases[current])
        in_data.append(out[0])
        prev_out = out
        out = comps[current].run_until_output(in_data)
        if debug:
            print(f"Run comp {current} out: {out}")
        current = (current + 1) % 5
    return prev_out[0]

if __name__ == "__main__":
    lines = open("07.dat", "r").readlines()
    prog_str = lines[0]
    prog = list(map(int, prog_str.split(',')))
    print(run_amps(prog,[9,7,8,5,6]))
    max_signal = 0
    for perm in permutations(range(5,10)):
        out = run_amps(prog, perm)
        if out > max_signal:
            max_signal = out
        print(f"{perm}: {out}")
    print(max_signal)
