from intcode_comp import IntcodeComp
from collections import namedtuple, defaultdict
import time
import os


def print_screen(screen, raw_out):
    for point_idx in range(0, len(raw_out), 3):
        p = (raw_out[point_idx], raw_out[point_idx + 1])
        screen[p] = raw_out[point_idx + 2]

    ball_x = 0
    paddle_x = 0
    print(f"Score: {screen[(-1,0)]}")
    for y in range(0, 26):
        for x in range(0, 42):
            tile = screen[(x, y)]
            if tile == 0:
                #print(" ", end="")
                pass
            elif tile == 1:
                # print("#", end="")  # wall
                pass
            elif tile == 2:
                # print("@", end="")  # block
                pass
            elif tile == 3:
                # print("_", end="")  # paddle
                paddle_x = x
            elif tile == 4:
                # print("o", end="")  # ball
                ball_x = x
        #print(" ")
    return (ball_x, paddle_x)


if __name__ == "__main__":
    lines = open("13.dat", "r").readlines()
    prog = list(map(int, lines[0].split(',')))

    seconds_per_frame = 0
    frame_start = time.perf_counter()
    screen = defaultdict(lambda: 0)
    comp = IntcodeComp(prog)
    comp.mem[0] = 2

    raw_out = comp.run_until_input([])

    while not comp.halted:
        #os.system('cls' if os.name == 'nt' else 'clear')
        ball_x, paddle_x = print_screen(screen, raw_out)
        if ball_x < paddle_x:
            joystick = -1
        elif ball_x > paddle_x:
            joystick = 1
        else:
            joystick = 0
        frame_end = time.perf_counter()
        frame_time = frame_end - frame_start
        #print(f"Frame render time (s): {frame_time}")
        sleep_time = max(0, seconds_per_frame - frame_time)
        time.sleep(sleep_time)
        frame_start = time.perf_counter()
        raw_out = comp.run_until_input([joystick])

    print_screen(screen, raw_out)
