# Simple ackermann implementation to check how well Python deals with it.

iterations = 0


def ackermann(m, n):
    global iterations
    iterations += 1
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))


# Due to default Python recursion limit (=1000), we cannot go beyond values: m=3, n=4
for current_m in range(4):
    for current_n in range(5):
        print(f"Input: m={current_m}, n={current_n}\t"
              f"Result: {ackermann(current_m, current_n)}\t"
              f"Iterations: {iterations}")
