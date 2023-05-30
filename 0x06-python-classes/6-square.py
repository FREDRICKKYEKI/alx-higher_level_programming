#!/usr/bin/python3
"""
module which continues the defination of square class
"""


class Square:
    """
    Class that defines a square based on 4-square.py
        Args:
            size (int): size of square
    """
    def __init__(self, size=0, position=(0, 0)):

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) != tuple or type(position[0]) != int \
                or type(position[1]) != int or len(position) > 2\
                or position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

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

    def my_print(self):
        """Prints the square with '#'"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(" ", end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
    
    @property
    def position(self):
        """Returns the position of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position attribute of the square"""
        if type(value) != tuple or type(value[0]) != int \
                or type(value[1]) != int or len(value) > 2\
                or value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

       

