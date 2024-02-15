#!/usr/bin/python3
"""
This module divides all elements of a matrix
"""

def matrix_divided(matrix, div):
    """Function that divides all elements of a matrix."""
    new_matrix = []
    new_row = []

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for row in matrix:
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for col in row:
            if type(col) not in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_row.append(round(col / div, 2))
        new_matrix.append(new_row)
        new_row = []
    return new_matrix
