#!/usr/bin/python3
"""

module that contains the pascal_triangle function

"""


def pascal_triangle(n):
    """
    function that returns the pascal triangle

    Args:
        n (int): number of lines

    Returns:
        matrix: a matrix with the pascal triangle

    """

    matrix = []
    prev = []

    for i in range(n):
        res_list = []
        a1 = -1
        a2 = 0
        for j in range(len(prev) + 1):
            if a1 == -1 or a2 == len(prev):
                res_list += [1]
            else:
                res_list += [prev[a1] + prev[a2]]
            a1 += 1
            a2 += 1
        matrix.append(res_list)
        prev = res_list[:]

    return matrix
