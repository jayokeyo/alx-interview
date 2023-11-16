#!/usr/bin/env python3
'''
Given an n x n 2D matrix, rotate it 90 degrees clockwise.

Prototype: def rotate_2d_matrix(matrix):
Do not return anything. The matrix must be edited in-place.
You can assume the matrix will have 2 dimensions and will not be empty.
'''


def rotate_2d_matrix(matrix):
    '''rotates a 2-D matrix by 90 degrees
    '''

    temp = [[] for _ in range(len(matrix))]
    k = 0

    for a in range(len(matrix)):
        for b in range(len(matrix[0])):
            temp[a].append(matrix[a][b])

    for i in range(len(matrix[0])):
        for j in range(-1, -(len(matrix) + 1), -1):
            try:
                matrix[i][k] = temp[j][i]
            except KeyError:
                matrix[i].append(temp[j][i])
            k += 1
        k = 0
