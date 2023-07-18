#!/usr/bin/python3
"""

module that contains the Base class, which
is inherited by the corresponding child classes

"""
import json
import os.path
import csv


class Base:
    """
    Class that is the base class of the
    corresponding child classes (Rectangle and Square
    classes)
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes the Base class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Function that returns the JSON representation
        of a list

        Args:
            list_dictionaries (list): list of dictionaries

        Returns:
            JSON rep. of the list
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class function that writes JSON string rep. of list_objs to
        a file

        Args:
            list_objs (list): list of objects/instances of the
            child classes
        """

        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                list_dic.append(obj.to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w', encoding="utf-8") as f:
            f.write(lists)

    @staticmethod
    def from_json_string(json_string):
        """
        Function that converts JSON string to dictionary
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance
        """
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = "{}.json".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))

        return list_ins

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
        Method that saves a CSV file
        """
        filename = "{}.csv".format(cls.__name__)

        if cls.__name__ == "Rectangle":
            list_dic = [0, 0, 0, 0, 0]
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_dic = ['0', '0', '0', '0']
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        if not list_objs:
            pass
        else:
            for obj in list_objs:
                for kv in range(len(list_keys)):
                    list_dic[kv] = obj.to_dictionary()[list_keys[kv]]
                matrix.append(list_dic[:])

        with open(filename, 'w') as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(matrix)

    @classmethod
    def load_from_file_csv(cls):
        """
        Method that loads a CSV file
        """
        filename = "{}.csv".format(cls.__name__)

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            csv_list = list(reader)

        if cls.__name__ == "Rectangle":
            list_keys = ['id', 'width', 'height', 'x', 'y']
        else:
            list_keys = ['id', 'size', 'x', 'y']

        matrix = []

        for csv_elem in csv_list:
            dict_csv = {}
            for kv in enumerate(csv_elem):
                dict_csv[list_keys[kv[0]]] = int(kv[1])
            matrix.append(dict_csv)

        list_ins = []

        for index in range(len(matrix)):
            list_ins.append(cls.create(**matrix[index]))

        return list_ins

        def draw(list_rectangles, list_squares):
        """
        Function that draws a Rectangle or Square using the Turtle
        module
        Args:
            list_rectangles: a list of rectangles to draw
            list_squares: a list of squares to draw
        """
        draw = turtle.Turtle()
        draw.screen.bgcolor("#50E3E6")
        draw.pensize(4)
        draw.shape("turtle")

        # draw the rectangle
        draw.color("#E55451")
        for item in list_rectangles:
            draw.showturtle()
            draw.up()
            draw.goto(item.x, item.y)
            draw.down()
            for i in range(2):
                draw.forward(item.width)
                draw.left(90)
                draw.forward(item.height)
                draw.left(90)
            draw.hideturtle()

        # draw square
        draw.color("#666362")
        for item in list_squares:
            draw.showturtle()
            draw.up()
            draw.goto(item.x, item.y)
            draw.down()
            for i in range(2):
                draw.forward(item.width)
                draw.left(90)
                draw.forward(item.height)
                draw.left(90)
            draw.hideturtle()

            turtle.exitonclick()
