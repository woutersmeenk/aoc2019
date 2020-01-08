from intcode_comp import IntcodeComp
from itertools import combinations


def run_inputs(comp, in_strs):
    out_str = None
    for in_str in in_strs:
        in_data = list(map(ord, in_str + "\n"))
        out_data = comp.run_until_input(in_data)
        out_str = ''.join(map(chr, out_data))
    return out_str


if __name__ == "__main__":
    lines = open("25.dat", "r").readlines()
    prog = list(map(int, lines[0].split(',')))
    comp = IntcodeComp(prog)
    in_strs = [
        "east",
        "take antenna",  # Crew
        "west",
        "north",  # Hall
        "take weather machine",
        "north",  # Storage
        "take klein bottle",
        "east",  # Stable
        "take spool of cat6",
        "east",  # Gift
        "south",  # Kitchen
        "take mug",
        "north",
        "north",  # Sick
        "west",  # Hot
        "north",  # Obs
        "take cake",
        "south",
        "east",
        "east",  # Corr
        "south",  # Pass
        "take shell",
        "north",
        "north",  # Holo
        "north",  # Lab
        "take tambourine",
        "south",
        "south",
        "west",
        "south",
        "west",
        "south",
        "south",
        "drop antenna",
        "drop tambourine",
        "drop shell",
        "drop cake",
        "drop mug",
        "drop spool of cat6",
        "drop klein bottle",
        "drop weather machine",  # inv empty
        "east",
    ]

    run_inputs(comp, in_strs)

    items = [
        "antenna",
        "tambourine",
        "shell",
        "cake",
        "mug",
        "spool of cat6",
        "klein bottle",
        "weather machine",
    ]

    for r in range(2, 8):
        for comb in combinations(items, r):
            print(comb)
            in_strs = ["take " + item for item in comb]
            in_strs.append("east")
            out_str = run_inputs(comp, in_strs)

            if "== Security Checkpoint ==" not in out_str:
                break

            in_strs = ["drop " + item for item in comb]
            run_inputs(comp, in_strs)
        if "== Security Checkpoint ==" not in out_str:
            break
    print(out_str)
