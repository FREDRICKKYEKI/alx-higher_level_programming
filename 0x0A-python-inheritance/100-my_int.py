#!/usr/bin/python3
"""

module that contains a class MyInt
that extends the int class

"""


class MyInt(int):
    """
    Class that inherits from class int
    """

    def __eq__(self, other):
        """
        Method that returns == check
        """
        return int.__ne__(self, other)

    def __ne__(self, other):
        """
        Method that returns == check
        """
        return int.__eq__(self, other)
