#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""

module that contains the Rectangle class that
extends the BaseGeometry class

"""


class Rectangle(BaseGeometry):
    """
    Class that defines a rectangle from BaseGeometry Class
    """

    def __init__(self, width, height):
        """
        Initializes instance of the class
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
