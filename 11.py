from intcode_comp import IntcodeComp

if __name__ == "__main__":
    lines = open("11.dat", "r").readlines()
    prog = list(map(int, lines[0].split(',')))
    comp = IntcodeComp(prog)
    out = comp.run_until_input([1])
    world = {}
    coords = (0, 0)
    coords_delta = (0, 1)
    d = 0
    while len(out) > 0:
        # print(f"O {coords} {d} {out}")
        world[coords] = out[0]
        if out[1] == 0:
            d = (d - 90) % 360
            if d < 0:
                d = 360 + d
        else:
            d = (d + 90) % 360
        if d == 0:
            coords_delta = (0, 1)
        elif d == 90:
            coords_delta = (1, 0)
        elif d == 180:
            coords_delta = (0, -1)
        elif d == 270:
            coords_delta = (-1, 0)
        else:
            assert False

        coords = (coords[0] + coords_delta[0], coords[1] + coords_delta[1])
        tile_color = world.get(coords, 0)
        # print(f"I {coords} {d} {tile_color}")
        out = comp.run_until_input([tile_color])
    print(len(world))
    for y in range(-10, 10):
        for x in range(-50, 50):
            print("#" if world.get((x, -y), 0) == 1 else ".", end="")
        print(" ")
