#!/usr/bin/python3
"""

module with print square function that prints # equivalent to the size

"""


def print_square(size):
    """Function that prints square with '#'

    Args:
        size (int): size of square

    Returns:
        None

    """
    i = 0
    j = 0
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    elif type(size) != int:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    else:
        while i < size:
            j = 0
            while j < size:
                print('#', end='')
                j += 1
            i += 1
            print()
