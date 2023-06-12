#!/usr/bin/python3
def lookup(obj):
    """
    Function that returns the list of available attributes
    and methods of an object

    Args:
        obj(class): instance of the class

    Returns:
        (list): list of attributes
    """

    return dir(obj)
