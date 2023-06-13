#!/usr/bin/python3
"""

Module that contains write_file function
hat writes to a text file

"""


def write_file(filename="", text=""):
    """
    Function that writes to a text file

    Args:
        filename (string): filename
        text (string): text to write

    Raises
        Exception: when the file cannot be opened

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
