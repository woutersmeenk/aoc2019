from itertools import permutations
from intcode_comp import IntcodeComp


def run_amps(prog, phases):
    amps = []
    phases_supplied = []
    for i in range(5):
        amps.append(IntcodeComp(prog))
        phases_supplied.append(False)
    current_amp = 0
    last_output = [0]
    prev_output = None
    while len(last_output) > 0:
        input_data = []
        if not phases_supplied[current_amp]:
            phases_supplied[current_amp] = True
            input_data.append(phases[current_amp])
        input_data.append(last_output[0])
        prev_output = last_output
        last_output = amps[current_amp].run_until_input(input_data)
        current_amp = (current_amp + 1) % 5
    return prev_output[0]


if __name__ == "__main__":
    lines = open("07.dat", "r").readlines()
    prog_str = lines[0]
    prog = list(map(int, prog_str.split(',')))
    max_signal = 0
    for perm in permutations(range(5, 10)):
        out = run_amps(prog, perm)
        if out > max_signal:
            max_signal = out
    print(max_signal)
