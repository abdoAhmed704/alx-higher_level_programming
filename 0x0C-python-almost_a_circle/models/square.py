#!/usr/bin/python3
"""Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        x = f"[Square] ({self.id}) {self.x}/{self.y} - {self.height}"
        return x

    @property
    def size(self):
        """return the size"""
        return self.height

    @size.setter
    def size(self, val):
        self.height = val
        self.width = val
