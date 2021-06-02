#!/bin/python3
"""
Thos problen is solve how many islenad forms are repited
In a matrix 1 means land and 0 is water.
In a matrix
[[1,1,1,0,1,1],
 [ 1,1,0,0,0,1],
 [1,0,0,0,0,0],
 [0,0,1,0,0,1],
 [1,0,0,0,1,1]

Exists 3 different kinds of lands, from 5 lands

Lands looks like graphs and similitude of lands can be
kind of complicated
but what about use a matrix multiplication, for example a land
matrix agains a vector ?
"""


def zero_matrix(i, j):
    base_row = [0 for i in range(i)] 
    zero_matrix = [base_row for j in range(j)]
    return zero_matrix


def matrix_multiplication(matrix_A, matrix_B):
    result = zero_matrix(len(matrix_A), len(matrix_B))
    for i in range(len(matrix_A)):
        for j in range(len(matrix_B)):
            for k in range(len(matrix_A)):
                result[i][j] += matrix_A[i][k] * matrix_B[k][j]
    return result 

matrix_island = [
    [1, 1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 1, 1]
]
matrix_unity = [1, 1, 1, 1, 1]

matrix_mult_result = matrix_multiplication(matrix_island, matrix_island)
print(matrix_mult_result)