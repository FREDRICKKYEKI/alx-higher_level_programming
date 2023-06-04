#!/usr/bin/python3
"""

Module containing maxtrix dividing function

"""


def matrix_divided(matrix, div):
    """Function that divides a matrix by a divider (div)

    Args:
        matrix (list): a list of lists
        div (int): number to divide matrix elements with

    Returns:
        (list): matrix after operation

    """
    if type(matrix) != list:
        raise TypeError("matrix must be a matrix \
                        (list of lists) of integers/floats")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(div) != int and type(div) != float:
        raise TypeError("div must be a number")
    else:
        row_size = len(matrix[0])
        new_mat = []
        row_mat = []
        for row in matrix:
            if len(row) != row_size:
                raise TypeError("Each row of the matrix \
                                 must have the same size")
            else:
                for elem in row:
                    if type(elem) != int and \
                       type(elem) != float:
                        raise TypeError("matrix must be a matrix (list \
                                         of lists) of integers/floats")
                    res = round(float(elem / div), 2)
                    row_mat.append(res)
                new_mat.append(row_mat)
            row_mat = []
    return new_mat
