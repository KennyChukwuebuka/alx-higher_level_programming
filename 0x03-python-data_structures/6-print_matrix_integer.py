#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row_matrix in matrix:
        for ele_matrix in row_matrix:
            print('{:d}'.format(ele_matrix), end=' ')
        print()
