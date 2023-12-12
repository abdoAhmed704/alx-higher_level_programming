#!/usr/bin/python3
"""adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add attribute to object if possible.
    Args:
        obj (any): object to add an attribute to.
        att (str): name
        value (any): value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
