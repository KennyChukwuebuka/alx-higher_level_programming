#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        return

    for row_matrix in matrix:
        for ele_matrix in row_matrix:
            print('{}'.format(ele_matrix), end=' ')
        print()
