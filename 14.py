import math
import collections

Reaction = collections.namedtuple("Reaction", ("output_amount", "inputs"))


def parse():
    reactions = {}
    reaction_lines = open("14.dat", "r").readlines()
    for reaction_line in reaction_lines:
        inputs_str, output_str = reaction_line.strip().split('=>')
        output_amount, output_chem = output_str.strip().split(' ')
        inputs = {}
        for input_str in inputs_str.strip().split(','):
            amount, input_chem = input_str.strip().split(' ')
            inputs[input_chem] = int(amount)
        reactions[output_chem] = Reaction(int(output_amount), inputs)

    return reactions


def calc_ore(fuel_needed):

    amounts_needed = {'FUEL': fuel_needed}
    reaction_executed = True
    while reaction_executed:
        # print(f"Needed: {amounts_needed}")

        new_amounts_needed = amounts_needed.copy()
        reaction_executed = False

        # For each chem we need check how to make it
        for needed_chem in amounts_needed.keys():
            if needed_chem == "ORE":
                continue
            amount_needed = new_amounts_needed[needed_chem]
            if amount_needed <= 0:
                continue

            reaction_executed = True
            # Calc how many time we need to do the reaction to get the required amount
            reaction = reactions[needed_chem]
            num_times = math.ceil(amount_needed / reaction.output_amount)
            # remove what we made from the needed chems
            new_amounts_needed[needed_chem] = amount_needed - reaction.output_amount * \
                num_times

            # For each of the input that we needed to make this chem we need to add them to the needed
            # chems
            sub_inputs = reaction.inputs
            for sub_input_chem in sub_inputs.keys():

                current_amount = new_amounts_needed.get(sub_input_chem, 0)
                new_amounts_needed[sub_input_chem] = current_amount + \
                    sub_inputs[sub_input_chem] * num_times

        # print(
        #     f"Create {reaction.output_amount * num_times} {needed_chem} [{num_times}] we need {amount_needed}. {new_amounts_needed}")

        amounts_needed = new_amounts_needed
    return amounts_needed['ORE']


if __name__ == "__main__":
    reactions = parse()

    print(f"Part 1: {calc_ore(1)}")

    l = 1
    h = 10000000
    print(f"{calc_ore(l)} {calc_ore(h)}")
    # if calc_ore(fuel) > 1000000000000:

    #print(f"Part 2: {1000000000000 - calc_ore(fuel)}")
