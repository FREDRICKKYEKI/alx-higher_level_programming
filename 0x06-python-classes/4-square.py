#!/usr/bin/python3
"""
module which is the continuation of square class
"""


class Square:
    """
    Class that defines a square based on 3-square.py
        Args:
            size (int): size of square
    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates square area
            Args:
                none
            Returns:
                int: the current area of square
        """
        return self.__size**2

    @property
    def size(self):
        """Gets size of the square
            Returns:
                int: size of aquare
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of square
            Args:
                int: value to assign to size of square
            Returns:
                void
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
