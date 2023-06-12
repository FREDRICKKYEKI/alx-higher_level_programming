#!/usr/bin/python3
"""

Module that contains class my list

"""


class MyList(list):
    """
    Class that inherits the attributes references of class list
    Args:
        list(list): class list
    """

    def print_sorted(self):
        """ Method that prints the sorted list """
        l_sorted = self.copy()
        l_sorted.sort()
        print(l_sorted)
