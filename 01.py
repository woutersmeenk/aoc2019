def calc_fuel(mass):
    added_fuel = mass
    total_fuel = 0
    while added_fuel > 0:
        added_fuel = int(added_fuel / 3) - 2
        if added_fuel > 0:
            total_fuel += added_fuel
            #print(" " + str(added_fuel))
    return total_fuel


if __name__ == "__main__":
    print(calc_fuel(1969))
    print(calc_fuel(100756))
    text_file = open("01.dat", "r")
    lines = text_file.readlines()

    sum = 0
    for line in lines:
        mass = int(line)
        sum += calc_fuel(mass)

    print(sum)
