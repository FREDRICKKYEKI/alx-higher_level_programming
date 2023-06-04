#!/usr/bin/python3
"""

say_my_name module: prints your names

"""


def say_my_name(first_name, last_name=""):
    """Function that prints first and last names
    
    Args:
        first_name (str): first name
        last_name  (str): second name

    Returns:
        None

    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    elif type(last_name) != str:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
