"""
--- Advent of Code 2019 - Day 2: 1202 Program Alarm ---
"""

import copy


def parse_intcode_file(intcode_file):
    intcode_file = intcode_file.split(",")
    return [int(code) for code in intcode_file]


def process_intcode(intcode_instructions):
    for i in range(0, len(intcode_instructions), 4):
        if intcode_instructions[i] == 99:
            break

        if intcode_instructions[i] == 1:
            first_component_index = intcode_instructions[i + 1]
            second_component_index = intcode_instructions[i + 2]
            result_index = intcode_instructions[i + 3]
            intcode_instructions[result_index] = intcode_instructions[first_component_index] + intcode_instructions[
                second_component_index]

        if intcode_instructions[i] == 2:
            first_component_index = intcode_instructions[i + 1]
            second_component_index = intcode_instructions[i + 2]
            result_index = intcode_instructions[i + 3]
            intcode_instructions[result_index] = intcode_instructions[first_component_index] * intcode_instructions[
                second_component_index]

    return intcode_instructions


# Reads input
with open("resources/day_two.txt", "r") as file:
    intcode_input_file = file.read()

# Parsed intcode
gravity_assist_program_intcode = parse_intcode_file(intcode_input_file)

# Ensures the intcode works just like before computer's explosion
gravity_assist_program_intcode[1] = 12
gravity_assist_program_intcode[2] = 2

# Part 1.
print(f"Value at address 0 : {process_intcode(gravity_assist_program_intcode)[0]}")

# Part 2.

# The output we need to achieve
OUTPUT = 19690720

# Parsed intcode
parsed_intcode = parse_intcode_file(intcode_input_file)

for noun in range(99):
    for verb in range(99):
        tested_intcode = copy.copy(parsed_intcode)
        tested_intcode[1] = noun
        tested_intcode[2] = verb
        if process_intcode(tested_intcode)[0] == OUTPUT:
            print(f"Found correct parameters!\n Noun: {noun}, Verb: {verb}")
            print(f"100 * noun + verb = {100 * noun + verb}")
            break
