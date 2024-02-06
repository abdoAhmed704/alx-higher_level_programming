#!/usr/bin/python3
"""base class"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string"""
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file"""
        file_name = "{}.json".format(cls.__name__)
        lista = []
        if list_objs is None:
            pass
        else:
            for i in list_objs:
                lista.append(i.to_dictionary())
        with open(file_name, "w") as file:
            file.write(cls.to_json_string(lista))
