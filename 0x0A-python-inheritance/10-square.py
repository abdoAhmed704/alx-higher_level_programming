#!/usr/bin/python3
"""Module for a Derived Class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A Square (drived) class"""
    def __init__(self, size):
        """Constructor"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        return self.__size ** 2

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
