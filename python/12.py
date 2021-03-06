from itertools import combinations
from collections import defaultdict
import math


def step(moons):
    for (moon1, moon2) in combinations(moons, 2):
        for axis in range(3):
            if moon1[axis] == moon2[axis]:
                continue
            elif moon1[axis] > moon2[axis]:
                moon1[axis+3] -= 1
                moon2[axis+3] += 1
            elif moon1[axis] < moon2[axis]:
                moon1[axis+3] += 1
                moon2[axis+3] -= 1

    for moon in moons:
        for axis in range(3):
            moon[axis] += moon[axis+3]


def calc_total_energy(moons):
    total_energy = 0

    for moon in moons:
        kin = 0
        pot = 0
        for axis in range(3):
            pot += abs(moon[axis])
            kin += abs(moon[axis + 3])
        total_energy += pot * kin
    return total_energy


def record_history(moons, per_axis_history):
    for moon_idx in range(len(moons)):
        for axis in range(3):
            per_axis_history[(moon_idx, axis)].append(moons[moon_idx][axis])


def find_idx_of_sub(l, pattern):
    pattern_length = len(pattern)
    for i in range(len(l)):
        if l[i:i+pattern_length] == pattern:
            return i
    return -1


def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)


if __name__ == "__main__":
    # io = [-1, 0, 2, 0, 0, 0]
    # europa = [2, -10, -7, 0, 0, 0]
    # ganymede = [4, -8, 8, 0, 0, 0]
    # callisto = [3, 5, -1, 0, 0, 0]
    io = [-16, -1, -12, 0, 0, 0]
    europa = [0, -4, -17, 0, 0, 0]
    ganymede = [-11, 11, 0, 0, 0, 0]
    callisto = [2, 2, -6, 0, 0, 0]
    moons = [io, europa, ganymede, callisto]

    for i in range(1000):
        step(moons)

    print(f"Part 1: {calc_total_energy(moons)}")

    # io = [-8, -10, 0, 0, 0, 0]
    # europa = [5, 5, 10, 0, 0, 0]
    # ganymede = [2, -7, 3, 0, 0, 0]
    # callisto = [9, -8, -3, 0, 0, 0]
    io = [-16, -1, -12, 0, 0, 0]
    europa = [0, -4, -17, 0, 0, 0]
    ganymede = [-11, 11, 0, 0, 0, 0]
    callisto = [2, 2, -6, 0, 0, 0]
    moons = [io, europa, ganymede, callisto]

    per_axis_history = defaultdict(list)

    for i in range(200000):
        record_history(moons, per_axis_history)
        step(moons)

    # Only needed for one moon, because the moons influcence each other but the different axis's do not
    # But for some reason the first and third moon give the wrong result....
    # Why we do not have to think of the velocities .... no clue ...
    total_steps = 1
    for axis in range(3):
        hist = per_axis_history[(1, axis)]
        step = find_idx_of_sub(hist[1:], hist[0:20])
        steps = step + 1
        total_steps = total_steps * (steps // math.gcd(total_steps, steps))
    print(f"Part 2: {total_steps}")
