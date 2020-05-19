#! python3
"""Based on 'n' numbers of matrices, create an average matrix of them (image denoise).

File with data is given in a .txt file.
First line is the number of rows and columns in matrices (their size) separated by 'x'.
Following lines are matrices separated by spaces, one line for each matrix.
If the calculations succeed, script appends the result at the end of the file.

To use the script, type: `python averageMatrix.py path/to/matrices_file.txt [-w path/to/weight_file.txt]`
"""

import argparse
import math


def get_arguments():
    """Gets location of a file containing matrices to be averaged."""

    parser = argparse.ArgumentParser(description="Based on 'n' numbers of matrices, create an average matrix of them.")
    parser.add_argument(dest="matrices_file", help="Location of the matrices file")
    parser.add_argument("-w", "--weighted", dest="weighted_mode",
                        help="Mode in which the script should be run. Either 'standard' or 'weighted'.")
    arguments = parser.parse_args()

    return arguments


def extract_matrices_file_data(file_path):
    """Reads data from the file and saves it in a way that allows data manipulation. """

    try:
        with open(file_path, "r") as file:
            file_content = file.read().splitlines()

        # If the file has already been operated on, halt the calculations.
        if file_content[-2] == "RESULT:":
            print("[-] Error! The contents of this file have already been calculated.")
            return None

        # Take the dimensions written at the beginning of the file and convert them to integers.
        dimensions = file_content[0].split(sep="x")
        dimensions = list(map(int, dimensions))
        del file_content[0]

        # Save all the lines containing matrices data to the 'matrices' list.
        matrices = []
        for matrix in file_content:
            matrix = matrix.split(sep=" ")
            matrix = list(map(int, matrix))
            matrices.append(matrix)

        # If the dimensions are different than size of matrices in the file, halt the program.
        if dimensions[0] * dimensions[1] != len(matrices[0]):
            raise IndexError

        return dimensions, matrices

    # Catches all the errors possible to happen while working with the file.
    except FileNotFoundError:
        print("[-] Error! Such file doesn't exist.")
    except ValueError:
        print("[-] Error! Data in the file is corrupted and impossible to read.")
    except IndexError:
        print("[-] Error! Incorrect matrix dimensions.")


def extract_weights_file_data(file_path):
    with open(file_path, "r") as file:
        file_content = file.readline().split(sep=" ")
        weights = list(map(float, file_content))
        return weights


def calculate_average_matrix(dimensions, matrices):
    """Does the most important work: takes all the matrices and creates an average of them."""

    average_matrix = []
    size = dimensions[0] * dimensions[1]
    # For all the positions in the matrix, get sum of all the values at the same position
    # from all matrices and calculate their average.
    for i in range(size):
        positional_sum = 0
        for matrix in matrices:
            positional_sum += matrix[i]

        # We round the number since for image denoise, we need integers.
        # It's important to note that rounding uses IEEE 754 standard.
        # Important: the line below is susceptible to change in case of using it for weighted calculations.
        # Change sum(weights) to "size" for non-weighted option.
        positional_average = round(positional_sum / len(matrices))
        average_matrix.append(positional_average)
    return average_matrix


def calculate_average_matrix_weighted(dimensions, matrices, weights):
    """Does the most important work: takes all the matrices and creates an average of them using weights."""

    average_matrix = []
    size = dimensions[0] * dimensions[1]
    # For all the positions in the matrix, get sum of all the values at the same position
    # from all matrices and calculate their average.
    for i in range(size):
        positional_sum = 0
        for index, matrix in enumerate(matrices):
            positional_sum += matrix[i] * weights[index]

        # We round the number since for image denoise, we need integers.
        # It's important to note that rounding uses IEEE 754 standard.
        # Important: the line below is susceptible to change in case of using it for weighted calculations.
        # Change sum(weights) to "size" for non-weighted option.
        positional_average = round(positional_sum / sum(weights))
        average_matrix.append(positional_average)
    return average_matrix


def save_result(file_path, matrix):
    """Appends the calculations' result at the end of the operated file."""

    with open(file_path, "a") as file:
        matrix = list(map(str, matrix))
        matrix = " ".join(matrix)
        file.write("\nRESULT:\n" + matrix)


def print_matrix(dimensions, matrix):
    """Prints the result of the calculations for the user to see in the console."""

    print("[+] Calculations done successfully.")
    print("RESULTING MATRIX:".rjust(20))
    for i in range(len(matrix)):
        if i % dimensions[1] == 0 and i != 0:
            print("")
        print(matrix[i], end=" ")
    print("")


def print_matrices_info(dimensions, matrices):
    """Prints basic info about matrices."""
    for matrix in matrices:
        print(f"STANDARD_DEVIATION: {calculate_standard_deviation(dimensions, matrix)}\n")


# Additional functions for images of different quality (weights applied).
def calculate_standard_deviation(dimensions, matrix):
    """Calculates standard deviation for SINGLE matrix. It is later used to establish weight values for matrices."""
    size = dimensions[0] * dimensions[1]
    average = sum(matrix) / size
    print(f"MATRIX DATA:\n{matrix}")
    print(f"AVERAGE VALUE: {average}")
    standard_deviation = sum([(element - average) ** 2 for element in matrix]) / (size - 1)
    return standard_deviation


def calculate_error(dimensions, resulting_matrix, matrices, weights):
    size = dimensions[0] * dimensions[1]
    for i in range(size):
        pixel_deviation = sum([((matrix[i] - resulting_matrix[i]) ** 2) * weights[j]
                               for j, matrix in enumerate(matrices)]) / (len(matrices) - 1)
        error = round(math.sqrt(pixel_deviation / sum(weights)))
        print(f"Pixel #{i + 1}: {resulting_matrix[i]} ± {error}")


# Get the path of the file from the user's input.
args = get_arguments()
worked_file_path, weighted_mode = args.matrices_file, args.weighted_mode

# Save the matrices data to the list. First object is dimensions list, second is list of matrices.
matrices_data = extract_matrices_file_data(worked_file_path)

# If no errors occurred (meaning there IS some matrices data),
# proceed with the calculations, saving results and printing the matrix.
if matrices_data:
    # Prints all the basic data about matrices.
    print_matrices_info(matrices_data[0], matrices_data[1])

    if weighted_mode:
        print("[+] Script is running in the 'weighted' mode.")
        weights_list = extract_weights_file_data(weighted_mode)
        result = calculate_average_matrix_weighted(matrices_data[0], matrices_data[1], weights_list)
        calculate_error(matrices_data[0], result, matrices_data[1], weights_list)
    else:
        print("[+] Script is running in the 'standard' mode.")
        result = calculate_average_matrix(matrices_data[0], matrices_data[1])

    save_result(worked_file_path, result)
    print_matrix(matrices_data[0], result)
