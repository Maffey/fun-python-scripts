""" quest-0
t - number of tests
c - number of packages
k - capacity
w - package weight
"""

t = int(input())

for i in range(t):
    task_input = input().split()
    task_input = [float(variable) for variable in task_input]
    c, k, w = task_input[0], task_input[1], task_input[2],
    if c * w <= k:
        print("yes")
    else:
        print("no")
