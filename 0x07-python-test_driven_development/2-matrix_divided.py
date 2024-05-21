#!/usr/bin/python3

"""
This module divides each element of a matrix by a given number
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix
    Args:
        matrix: A list of lists of type integers or floats

        division (integer or float) : divider >= 0
    Raises:
        TypeError: If the matrix contains non-numbers
        TypeError: If the matrix contains rows of different sizes
        TypeError: If division is not an integer or float
        ZeroDivisionError: If division is 0
    """
    new_matrix = []
    error = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or matrix is [[]] or matrix is None:
        raise TypeError(error)
    if type(div) is int or type(div) is float or type(div) is None:
        pass
    else:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix[0]:
        length = len(matrix[0])
    else:
        raise TypeError(error)
    for i in range(len(matrix)):
        if len(matrix[i]) is not length:
            raise TypeError("Each row of the matrix must have the same size")
        new_matrix.append([])
        for n in matrix[i]:
            if type(n) is int or type(n) is float:
                new_matrix[i].append(round(n / div, 2))
            else:
                raise TypeError(error)
    return new_matrix
