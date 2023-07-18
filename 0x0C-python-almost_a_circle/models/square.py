#!/usr/bin/python3
"""

module that contains the Square class that
extends the Rectangle class

"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class square that inherits from Base class
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Function that initializes the Square class
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """
        Returns size of square
        """
        return self.width

    @size.setter
    def size(self, val):
        """
        Function that is a size setter

        Args:
            val (int): the size of square
        """
        self.width = self.height = val

    def __str__(self):
        """
        Function that prints the Square class
        """
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                 self.y, self.height)

    def update(self, *args, **kwargs):
        """
        Function that assigns an argument to each
        attribute:

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
                self.size = args[1]
            if length >= 3:
                self.x = args[2]
            if length >= 4:
                self.y = args[3]
        else:
            if kwargs.get('id'):
                self.id = kwargs.get('id')
            if kwargs.get('size'):
                self.size = kwargs.get('size')
            if kwargs.get('x'):
                self.x = kwargs.get('x')
            if kwargs.get('y'):
                self.y = kwargs.get('y')

    def to_dictionary(self):
        """
        Function that returns the dictionary representation of
        the square class
        """
        list_attr = ['id', 'size', 'x', 'y']
        dict_attr = {}

        for key in list_attr:
            dict_attr[key] = getattr(self, key)

        return dict_attr
