import math
import collections

Reaction = collections.namedtuple("Reaction", ("output_amount", "inputs"))

if __name__ == "__main__":
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

    inputs = reactions['FUEL'].inputs
    left_overs = {}
    while len(inputs) > 1:
        print(f"Inputs: {inputs}")
        print(f"Left overs: {left_overs}")
        new_inputs = inputs.copy()
        for input_chem in inputs.keys():
            if input_chem == "ORE":
                continue
            input_amount = inputs[input_chem]
            reaction = reactions[input_chem]
            num_times = math.ceil(input_amount / reaction.output_amount)
            left_over_input = input_amount % reaction.output_amount
            sub_inputs = reaction.inputs.copy()
            for sub_input_chem in sub_inputs.keys():
                current_amount = new_inputs.get(sub_input_chem, 0)
                sub_input_left_over = left_overs.get(sub_input_chem, 0)
                new_sub_input = current_amount + \
                    sub_inputs[sub_input_chem] * num_times
                new_sub_input = new_sub_input - sub_input_left_over
                if new_sub_input > 0:
                    new_inputs[sub_input_chem] = new_sub_input
                elif new_sub_input > 0:
                    left_overs[sub_input_chem] = -new_sub_input
                else:
                    del left_overs[sub_input_chem]

            if left_over_input > 0:
                new_inputs[input_chem] = left_over_input
            else:
                del new_inputs[input_chem]
        inputs = new_inputs
    print(inputs)
