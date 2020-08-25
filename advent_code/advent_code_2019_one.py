"""
--- Advent of Code 2019 - Day 1: The Tyranny of the Rocket Equation ---
"""

import math


# Calculates fuel
def calculate_fuel(module_mass):
    return math.floor(module_mass / 3) - 2


# Reads input
with open("../resources/day_one.txt", "r") as file:
    modules = file.readlines()

# Part 1.
sum_total_fuel = sum(calculate_fuel(int(fuel)) for fuel in modules)
print(f"Total fuel, part 1: {sum_total_fuel}")

# Part 2.
total_fuel = []
for mass in modules:
    fuel = calculate_fuel(int(mass))
    while fuel > 0:
        total_fuel.append(fuel)
        fuel = calculate_fuel(fuel)

print(f"Total fuel, part 2: {sum(total_fuel)}")

