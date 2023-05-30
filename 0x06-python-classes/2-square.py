#!/usr/bin/python3

class Square:
    """Class that defines a square based on 1-square.py
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