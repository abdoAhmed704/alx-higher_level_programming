#!/usr/bin/python3
"""
===================================
module method inherits_from
===================================
"""


def inherits_from(obj, a_class):
    """Method that return True if an object is an instance of a class
    """

    return False if type(obj) is a_class else isinstance(obj, a_class)
