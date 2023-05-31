#!/usr/bin/python3
import math


"""
module that contains decompiled magic class code
"""


class MagicClass:

    """
    Class that stores the properties
    of a circumference
    """
    def __init__(self, radius=0):
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """
        Method that calculates the area of the circumference
        """
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """
        Method that calculates the perimeter of a circumference
        """
        return (2 * math.pi * self.__radius)
