#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    copy = []

    for row in matrix:
        squared = []
        for num in row:
            squared.append(num ** 2)
        copy.append(squared)
    return copy
