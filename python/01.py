def calc_fuel_needed_part1(mass):
    return int(mass / 3) - 2


def calc_fuel_needed_part2(mass):
    added_mass = mass
    total_fuel = 0
    while added_mass > 0:
        added_mass = int(added_mass / 3) - 2
        if added_mass > 0:
            total_fuel += added_mass
    return total_fuel


if __name__ == "__main__":
    text_file = open("01.dat", "r")
    modules_mass = list(map(int, text_file.readlines()))

    total_fuel_needed = sum(map(calc_fuel_needed_part1, modules_mass))
    print(f"Part 1: {total_fuel_needed}")

    total_fuel_needed = sum(map(calc_fuel_needed_part2, modules_mass))
    print(f"Part 2: {total_fuel_needed}")
