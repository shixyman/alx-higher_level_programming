#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    multi_matrix = matrix.copy()

    for i in range(len(matrix)):
        multi_matrix[i] = list(map(lambda x: x**x, matrix[i]))

    return (multi_matrix)
