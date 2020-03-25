# CalcSequenceEasy.py - calculate n-th element of sequence based on first and second element.


def calc_nth_element_arth(a1, r, n):
    return a1 + (n - 1) * r


def calc_nth_element_geo(a1, q, n):
    return a1 * q**(n-1)


while True:
    type_of_sequence = str(input("Please enter type of sequence. ('geo' or 'arth' or 'quit'): "))
    if type_of_sequence == 'quit':
        break
    first_element = float(input("Please provide the first element: "))
    second_element = float(input("Please provide the second element: "))

    if type_of_sequence == "arth":
        difference = second_element - first_element
        print(f"Standard formula: An = {first_element} + (n-1)*{difference}")
        nth = int(input("Which element of the sequence do you want to calculate: "))
        print("Here you go!\n" + str(calc_nth_element_arth(first_element, difference, nth)))
    else:
        difference = second_element / first_element
        print(f"Standard formula: An = {first_element} * {difference}^(n-1)")
        nth = int(input("Which element of the sequence do you want to calculate?"))
        print("Here you go!\n" + str(calc_nth_element_geo(first_element, difference, nth)))
