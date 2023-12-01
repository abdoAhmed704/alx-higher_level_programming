#!/usr/bin/python3
"""Square module."""


class Square:
    """defines a square."""
    def __init__(self, size=0):

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        if self.__size is 0:
            print()
        for i in range(1, self.__size * self.__size + 1):
            print("#", end="\n" if i % self.__size == 0 else "")
