#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mtrx = []
    for i in matrix:
        tmp = list(map(lambda x: x * x, i))
        mtrx.append(tmp)
    return mtrx
