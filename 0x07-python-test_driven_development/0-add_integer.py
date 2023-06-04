#!/usr/bin/python3

"""

add module that adds two integers

"""


def add_integer(a, b=98) -> int:
    """This is a simple add function that adds two integers

    Args:
        a (int): first integer
        b (int): second integer initialized to 98

    Returns:
        result (int): a + b

    Raises:
        TypeError: if a or b are not int/float

    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)
