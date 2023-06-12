#!/usr/bin/python3
"""

Module that contains the inherits_from function

"""


def inherits_from(obj, a_class):
    """
    Function that returns True/False if obj is an instance of a_class

    Args:
        obj (class): object
        a_class (class): class type

    Returns:
        (bool): True if obj is an instance of a_class else False
    """
    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
