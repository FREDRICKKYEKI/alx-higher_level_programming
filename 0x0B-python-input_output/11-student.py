#!/usr/bin/python3
"""
module that defines the class Student
"""


class Student:
    """ Class to create student instances """

    def __init__(self, first_name, last_name, age):
        """
        special method to initialize
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        method that returns directory description
        """
        obj = self.__dict__.copy()
        if type(attrs) is list:

            for item in attrs:
                if type(item) is not str:
                    return obj

            d = {}

            for iattr in range(len(attrs)):
                for sattr in obj:
                    if attrs[iattr] == sattr:
                        d[sattr] = obj[sattr]
            return d

        return obj

    def reload_from_json(self, json):
        """ Replaces all attributes of the Student instance """
        for attr in json:
            self.__dict__[attr] = json[attr]
