#!/usr/bin/python3
"""
Module that contains save_to_json_file function that writes
an Object to a text file using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Function that writes an object to a text file
    by a JSON representation

    Args:
        my_obj (string): object
        filename (string): textfile name

    Raises:
        Exception: when the object can't be encoded

    """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(my_obj, f)
