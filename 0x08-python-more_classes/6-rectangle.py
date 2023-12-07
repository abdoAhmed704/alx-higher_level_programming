#!/usr/bin/python3
"""
Class for Rectangle
"""


class Rectangle:
    """Class for Rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.height * self.width

    def perimeter(self):
        if self.height == 0 or self.width == 0:
            return 0
        return (self.height + self.width) * 2

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ""
        string = ""
        string = "\n".join("#" * self.width for j in range(self.height))
        return string

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        print("Bye rectangle...")
        number_of_instances -= 1
