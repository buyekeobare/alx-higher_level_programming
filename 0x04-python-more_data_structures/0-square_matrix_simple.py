#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = matrix.copy()

    for p in range(len(matrix)):
        new_matrix[p] = list(map(lambda x: x**2, matrix[p]))

    return (new_matrix)
