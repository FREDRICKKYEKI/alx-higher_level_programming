#!/usr/bin/python3
"""

module that contains the rectangle class

"""
from models.base import Base


class Rectangle(Base):
    """
    Class that inherits from Base class
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        class instance initializer
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """
        function that is the width getter
        Returns:
            the width of rectangle
        """
        return self.__width

    @width.setter
    def width(self, val):
        """
        Function that is the width setter
        Args:
            val (int): width
        """
        if type(val) != int:
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        self.__width = val

    @property
    def height(self):
        """
        Function that is the height getter
        Returns:
            the height of rectangle
        """
        return self.__height

    @height.setter
    def height(self, val):
        """
        Function that is the height setter
        Args:
            val (int): height
        """
        if type(val) != int:
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        self.__height = val

    @property
    def x(self):
        """
        Function that is the x getter
        Returns:
            the x of rectangle
        """
        return self.__x

    @x.setter
    def x(self, val):
        """
        Function that is the x setter
        Args:
            val (int): x
        """
        if type(val) != int:
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be >= 0")
        self.__x = val

    @property
    def y(self):
        """
        Function that is the y getter
        Returns:
            the y of rectangle
        """
        return self.__y

    @y.setter
    def y(self, val):
        """
        Function that is the y setter
        Args:
            val (int): y
        """
        if type(val) != int:
            raise TypeError("y must be an integer")
        elif val < 0:
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        """
        Function that calculates the area of instance
        rectangle \n
        Returns:
            area (int)
        """
        return self.__width * self.__height

    def display(self):
        """
        Function that prints out the instance Rectangle
        """
        i = 0
        k = 0
        while k < self.y:
            print()
            k += 1
        while i < self.height:
            j = 0
            l = 0
            while l < self.x:
                print(' ', end='')
                l += 1
            while j < self.width:
                print('#', end='')
                j += 1
            print()
            i += 1

    def __str__(self):
        """
        Function that runs when class is passed in
        print function
        """
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    """Needs to be checked"""
    def update(self, *args, **kwargs):
        """
        Function that assigns an argument to each
        attribute

        Args:
            *args (tuple): arguments of variable length passed
            **kwargs (dict): key-word arguments of variable length
                             passed
        """
        length = len(args)
        if length >= 1 and args is not None:
            if length >= 1:
                self.id = args[0]
            if length >= 2:
                self.width = args[1]
            if length >= 3:
                self.height = args[2]
            if length >= 4:
                self.x = args[3]
            if length >= 5:
                self.y = args[4]
        else:
            if kwargs.get('id'):
                self.id = kwargs.get('id')
            if kwargs.get('width'):
                self.width = kwargs.get('width')
            if kwargs.get('height'):
                self.height = kwargs.get('height')
            if kwargs.get('x'):
                self.x = kwargs.get('x')
            if kwargs.get('y'):
                self.y = kwargs.get('y')

    def to_dictionary(self):
        """
        Function that returns the dictionary representation
        of a Rectangle class
        """
        list_attr = ['id', 'width', 'height', 'x', 'y']
        dict_attr = {}

        for key in list_attr:
            dict_attr[key] = getattr(self, key)

        return dict_attr
