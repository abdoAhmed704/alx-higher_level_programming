#!/usr/bin/python3
"""
===========================
Module
===========================
"""


class MyList(list):
    """Class with method print_sorted"""

    def print_sorted(self):
        """Methot that sorted a list"""

        print(sorted(list(self)))
