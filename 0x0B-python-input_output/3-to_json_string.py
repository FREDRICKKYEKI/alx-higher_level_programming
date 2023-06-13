#!/usr/bin/python3
"""
Module that contains to_json_string function that returns the
JSON representation of an object
"""
import json


def to_json_string(my_obj):
    """
    Function that returns the JSON representation of an object

    Args:
        my_obj (dict): object

    Raises:
        Exception: when the object can't be encoded

    """
    return json.dumps(my_obj)
