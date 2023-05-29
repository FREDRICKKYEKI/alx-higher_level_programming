#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value), end="")
        print()
    except ValueError as ve:
        sys.stderr.write(str(ve))
        return False
    else:
        return True
