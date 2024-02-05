#!/usr/bin/python3
"""base class"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if self.id is None:
            __nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id
