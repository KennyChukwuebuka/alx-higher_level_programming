#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row_matrix in matrix:
        for ele_matrix in row_matrix:
            if row_matrix.index(ele_matrix) != len(row_matrix) - 1:
                endspace = ' '
            else:
                endspace = ''
            print('{:d}'.format(ele_matrix), end=endspace)
        print()
