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
        return self.width

    @size.setter
    def size(self, val):
        """setting the size"""
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        if args is not None and len(args) != 0:
            lista = ["id", "size", "x", "y"]
            for a, v in zip(lista, args):
                setattr(self, a, v)
        else:
            for k, v in kwargs.items():
                if hasattr(self, k):
                    setattr(self, str(k), v)
