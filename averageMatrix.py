#! python3
# averageMatrix.py - Based on 'n' numbers of matrices, create an average matrix of them (image denoise).
# File with data is given in a .txt file.
# First line is the number of rows and columns in matrices (their size) separated by 'x'.
# Following lines are matrices separated by spaces, one line for each matrix.

# To use the script in command line terminal, use 'python averageMatrix.py path/to/file.txt

import argparse


def get_arguments():
    parser = argparse.ArgumentParser(description="Based on 'n' numbers of matrices, create an average matrix of them.")
    parser.add_argument(dest="matrices_file", help="Location of the matrices file")
    arguments = parser.parse_args()

    if arguments.matrices_file is None:
        parser.error("[-] please specify a file with matrices, use --help")

    return arguments


def extract_file_data(file_path):
    with open(file_path, "r") as file:
        file_content = file.read().splitlines()
        dimensions = file_content[0].split(sep="x")
        dimensions = list(map(int, dimensions))
        del file_content[0]

        matrices = []
        for matrix in file_content:
            matrix = matrix.split(sep=" ")
            matrix = list(map(int, matrix))
            matrices.append(matrix)

        return dimensions, matrices


def calculate_average_matrix(dimensions, matrices):
    average_matrix = []
    for i in range(dimensions[0] * dimensions[1]):
        positional_sum = 0
        for matrix in matrices:
            positional_sum += matrix[i]
        positional_average = round(positional_sum / len(matrices))
        average_matrix.append(positional_average)
    return average_matrix


def save_result(file_path, matrix):
    with open(file_path, "a") as file:
        matrix = list(map(str, matrix))
        matrix = " ".join(matrix)
        file.write("\nRESULT:\n" + matrix)


def print_matrix(dimensions, matrix):
    print("Calculations done successfully.")
    print("RESULTING MATRIX:".rjust(20))
    for i in range(len(matrix)):
        if i % dimensions[1] == 0 and i != 0:
            print("")
        print(matrix[i], end=" ")
    print("")


worked_file_path = get_arguments().matrices_file
dims, mx = extract_file_data(worked_file_path)
result = calculate_average_matrix(dims, mx)
save_result(worked_file_path, result)
print_matrix(dims, result)
