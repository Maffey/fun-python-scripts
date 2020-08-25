""" quest-2
t - number of tasks
a - evaluated number
"""


def sort_and_cut(number):
    number = "".join(sorted(str(number)))
    result = int(number[::-1]) - int(number)
    if result < 1000:
        result = int(str(result) + "0")
    return result


number_of_iterations = 0

t = int(input())
for i in range(t):
    iterations = 0
    input_number = int(input())
    while input_number != 6174:
        iterations += 1
        input_number = sort_and_cut(input_number)
        if input_number < 1000 or input_number > 9999:
            iterations = -1
            break
    print(iterations)
