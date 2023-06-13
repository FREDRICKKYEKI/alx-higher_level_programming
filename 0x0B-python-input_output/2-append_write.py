#!/usr/bin/python3
"""

Module that contains append_write function
that appends to a text file

"""


def append_write(filename="", text=""):
    """
    Function that appends to a text file

    Args:
        filename (string): filename
        text (string): text to write

    Raises
        Exception: when the file cannot be opened

    """

    with open(filename, 'a', encoding="utf-8") as f:
        return f.write(text)
