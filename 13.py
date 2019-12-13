from intcode_comp import IntcodeComp
from collections import namedtuple, defaultdict
import keyboard
import time
import os


def print_screen(screen, raw_out):
    for point_idx in range(0, len(raw_out), 3):
        p = (raw_out[point_idx], raw_out[point_idx + 1])
        screen[p] = raw_out[point_idx + 2]

    print(f"Score: {screen[(-1,0)]}")
    for y in range(0, 26):
        for x in range(0, 42):
            tile = screen[(x, y)]
            if tile == 0:
                print(" ", end="")
            elif tile == 1:
                print("#", end="")  # wall
            elif tile == 2:
                print("@", end="")  # block
            elif tile == 3:
                print("_", end="")  # paddle
            elif tile == 4:
                print("o", end="")  # ball
        print(" ")


if __name__ == "__main__":
    lines = open("13.dat", "r").readlines()
    prog = list(map(int, lines[0].split(',')))

    seconds_per_frame = 0.5
    frame_start = time.perf_counter()
    screen = defaultdict(lambda: 0)
    comp = IntcodeComp(prog)
    comp.mem[0] = 2

    raw_out = comp.run_until_input([])

    joystick = 0
    while not comp.halted:
        #os.system('cls' if os.name == 'nt' else 'clear')
        print_screen(screen, raw_out)
        frame_end = time.perf_counter()
        frame_time = frame_end - frame_start
        print(f"Frame render time (s): {frame_time}")
        sleep_time = max(0, seconds_per_frame - frame_time)
        time.sleep(sleep_time)
        frame_start = time.perf_counter()
        raw_out = comp.run_until_input([joystick])
        print(f"Joystick: ", end="")
        while True:
            if keyboard.is_pressed('left arrow'):
                joystick = -1
                break
            elif keyboard.is_pressed('right arrow'):
                joystick = 1
                break
            elif keyboard.is_pressed('down arrow'):
                joystick = 0
                break
        print(f"{joystick}")
