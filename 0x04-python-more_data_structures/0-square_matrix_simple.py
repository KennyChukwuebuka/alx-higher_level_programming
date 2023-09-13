#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    #  check if the matrix is empty
    if not matrix:
        return []

    mat_row = len(matrix)
    mat_col = len(matrix[0])

    ret_mat = []

    for i in range(mat_row):
        ret_row = []

        for j in range(mat_col):
            sq_val = matrix[i][j] ** 2
            ret_row.append(sq_val)
        ret_mat.append(ret_row)
    return ret_mat
