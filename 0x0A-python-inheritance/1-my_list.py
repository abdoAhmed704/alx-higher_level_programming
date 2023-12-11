#!/usr/bin/python3
"""
===========================
Module
===========================
"""


class MyList(list):
    """Class with method print_sorted"""
    pass

    def print_sorted(self):
        """Methot that sorted a list"""

        print(sorted(list(self)))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
