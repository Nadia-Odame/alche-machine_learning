#!/usr/bin/env python3
def matrix_shape(matrix):
    if isinstance(matrix, list):
        return [len(matrix)] + matrix_shape(matrix[0]) if matrix else [0]
    return []
