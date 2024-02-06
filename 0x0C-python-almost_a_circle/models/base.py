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

    @staticmethod
    def from_json_string(json_string):
        """from_json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create"""
        if cls.__name__ == "Rectangle":
            new_ins = cls(4, 5)
        if cls.__name__ == "Square":
            new_ins = cls(45)
        new_ins.update(**dictionary)
        return new_ins

    @classmethod
    def load_from_file(cls):
        from os import path
        file_name = "{}.json".format(cls.__name__)
        if not path.isfile(file_name):
            return []
        with open(file_name, "r") as f:
            objs = cls.from_json_string(f.read())
        list_obj = []
        for obj in objs:
            list_obj.append(cls.create(**obj))
        return list_obj
