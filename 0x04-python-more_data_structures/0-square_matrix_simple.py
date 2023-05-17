#!/usr/bin/python3
def square_matrix(matrix=[]):
    len_o = len(matrix)
    len_i = len(matrix[0])
    new_mat = [[] for i in range(len_o)]
    for i in range(len_o):
        for j in range(len_i):
            new_mat[i].append(matrix[i][j] ** 2)
    return (new_mat)
