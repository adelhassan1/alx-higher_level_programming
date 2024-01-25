#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    total_matrics = []
    new_row = []
    for row in matrix:
        for col in row:            
            new_row.append(col ** 2)
        total_matrics.append(new_row)
        new_row = []
    return total_matrics

