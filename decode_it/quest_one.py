""" quest-1
r - number of columns
s - number of beads
"""

from functools import reduce


def calculate_beads_combinations(list_of_beads):
    combinations_in_each_column = [(column_beads + 1) * 2 for column_beads in list_of_beads]
    return reduce(lambda x, y: x * y, combinations_in_each_column)


r, s = input().split()
r, s = int(r), int(s)
beads_list = [0] * r
beads_per_column = s // r
remainder = s % r
beads_list = [column + beads_per_column for column in beads_list]
for i in range(len(beads_list)):
    if remainder == 0:
        break
    beads_list[i] += 1
    remainder -= 1
print(calculate_beads_combinations(beads_list))
