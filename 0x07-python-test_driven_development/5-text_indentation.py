#!/usr/bin/python3
"""

Module which contains text_indentation function

"""


def text_indentation(text):
    """ function that prints a text with 2 new lines after each
    of these characters: ., ? and :

    Args:
        text (str): text to be indented

    Return:
        None

    """

    if type(text) != str:
        raise TypeError("text must be a string")
    new_text = ""
    mod_text = text
    mod_text.strip()
    i = 0
    length = len(mod_text)

    while i < length:
        if mod_text[i] in ['.', '?', ':']:
            new_text += mod_text[i]
            try:
                while mod_text[i + 1] and mod_text[i + 1] == ' ':
                    i += 1
            except Exception:
                new_text += '\n'
                break

            new_text += '\n\n'
            i += 1
        else:
            new_text += mod_text[i]
            i += 1
    print(new_text)
