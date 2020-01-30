from intcode_comp import IntcodeComp
from collections import defaultdict

if __name__ == "__main__":
    lines = open("23.dat", "r").readlines()
    prog = list(map(int, lines[0].split(',')))

    comps = {}
    in_queues = defaultdict(list)

    for addr in range(0, 50):
        comp = IntcodeComp(prog)
        out = comp.run_until_input([addr])
        assert len(out) == 0
        comps[addr] = comp

    nat_mem = None
    last_nat_mem_send = None
    done = False
    while not done:
        idle = True
        for addr in range(0, 50):
            in_queue = in_queues[addr]
            if len(in_queue) == 0:
                in_queue.append(-1)
            out = comps[addr].run_until_input(in_queue)
            in_queues[addr] = []
            assert not comps[addr].halted
            for idx in range(0, len(out), 3):
                idle = False
                dest = out[idx]
                x = out[idx + 1]
                y = out[idx + 2]
                #print(f"Packet routed: {addr} -> {dest} data: {x} {y}")
                if dest == 255:
                    if nat_mem is None:
                        print(f"Part 1: {y}")
                    nat_mem = (x, y)

                in_queues[dest].append(x)
                in_queues[dest].append(y)
        #print(f"Idle: {idle}")
        if idle:
            if nat_mem == last_nat_mem_send:
                print(f"Part 2: {y}")
                done = True
            in_queues[0].append(nat_mem[0])
            in_queues[0].append(nat_mem[1])
            last_nat_mem_send = nat_mem
            #print(f"Packet routed: 255 -> 0 data: {nat_mem[0]} {nat_mem[1]}")
