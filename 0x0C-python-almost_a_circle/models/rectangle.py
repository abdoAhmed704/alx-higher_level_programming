#!/usr/bin/python3
"""inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """w"""
        return self.__width

    @width.setter
    def width(self, value):
        """w"""    
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        
        self.__width = value

    @property
    def height(self):
        """ww"""
        return self.__height

    @height.setter
    def height(self, value):
        """ww"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ww"""
        return self.__x

    @x.setter
    def x(self, value):
        """ww"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be => 0")
        self.__x = value

    @property
    def y(self):
        """wwww"""
        return self.__y

    @y.setter
    def y(self, value):
        """ww"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be => 0")
        self.__y = value
