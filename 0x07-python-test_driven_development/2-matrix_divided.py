#!/usr/bin/python3

"""module for matrix_divided"""


def matrix_divided(matrix, div):
    """
    devide a matrix on number (integer or float)

    Args:
        matrix: the matrix will be divieded
        div: a number (integer or float)

    rasis:
        ZeroDivisionError: if div == 0
        TypeError: nums in matrix and div should be int ,float
        and Each row of the matrix must have the same size
    
    Return:
        a new matrix
    """
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    for i in matrix:
        if not isinstance(i, list) or len(i) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for x in i:
            if not isinstance(x, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(num / div, 2) for num in i] for i in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
