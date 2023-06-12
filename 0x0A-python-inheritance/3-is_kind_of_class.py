#!/usr/bin/python3
"""

Module that contains the is_kind_of_class

"""


def is_kind_of_class(obj, a_class):
    """
    Function that returns True/False if obj is an instance of a_class

    Args:
        obj(class): object
        a_class(class): class type

    Returns:
        (bool): True if obj is an instance of a_class else False
    """
    return isinstance(obj, a_class)
