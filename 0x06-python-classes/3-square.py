#!/usr/bin/python3
"""
Module which continues the definitions of square class
"""


class Square:
    def __init__(self, size=0):
        """
        Class that defines a square based on 2-square.py
        Args:
            size (int): size of square
        """

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
