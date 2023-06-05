#!/usr/bin/python3
"""

module that continues the Rectangle class

"""


class Rectangle:
    """
    Rectangle class - defines a rectangle
    """
    number_of_instances = 0
    print_symbol = '#'

    def __str__(self):
        """
        Instance method that returns an “informal” and nicely printable
        string representation of an instance

        Returns:
            self: str of rectangle

        """
        rtn = ""
        if self.width == 0 or self.height == 0:
            return rtn

        for i in range(self.height):
            for j in range(self.width):
                rtn += str(self.print_symbol)
            rtn += '\n'
        return rtn

    def __repr__(self):
        """
        Method that returns the string represantion of the instance

        Returns:
            string represenation of the object

        """
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """
        Method that prints a message when the instance is deleted

        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def __init__(self, width=0, height=0):
        """ Method that initializes the instance

        Args:
            width: rectangle width
            height: rectangle height

        """
        self.__height = height
        self.__width = width
        type(self).number_of_instances += 1

    @property
    def width(self):
        """ method that returns the value of the width

        Returns:
            rectangle width

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        method that defines the width

        Args:
            value: width

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is less than zero

        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        method that returns the value of the height

        Returns:
            rectangle height

        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        method that defines the height

        Args:
            value: height

        Raises:
            TypeError: if height is not an integer
            ValueError: if height is less than zero

        """

        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Method that calculates the Rectangle area

        Returns:
            rectangle area

        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Method that calculates the Rectangle perimeter

        Returns:
            rectangle perimeter

        """
        return 2 * (self.__width + self.__height)
