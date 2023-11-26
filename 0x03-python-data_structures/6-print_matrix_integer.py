#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return None
    for small_matrix in matrix:
        if len(small_matrix) == 0:
            print()
        for i in range(len(small_matrix)):
            print("{:d}".format(small_matrix[i]),
                  end="\n" if i == len(small_matrix) - 1 else " ")
