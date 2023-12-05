#!/usr/bin/python3
"""Module for print_square method."""


def print_square(size):
    """Method prints # in square

    Args:
        size: the size of row and colum

    Raises:
        TypeError: If size is not an int.
        ValueError: If size is < 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
