#!/usr/bin/python3
"""

Module that contains is_same_class function

"""


def is_same_class(obj, a_class):
    """
    Function that returns True/False if obj is a type of a_class

    Args:
        obj (class): object
        a_class: class (class) type

    Returns:
        (bool):True if type of obj is a_class
                False, otherwise
    """
    return type(obj) is a_class
