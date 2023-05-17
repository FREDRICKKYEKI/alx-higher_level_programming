#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary.keys())
    keys.sort()
    for i in range(len(keys)):
        print("{}: {}".format(keys[i], a_dictionary[keys[i]]))
