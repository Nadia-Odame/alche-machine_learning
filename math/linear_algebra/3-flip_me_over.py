#!/usr/bin/env python3
"""This module contains the matrix_shape function."""
def matrix_shape(matrix):
    """Return the shape of a matrix."""
    if not isinstance(matrix, list):
        return []
    if len(matrix) == 0:
        return [0]
    return [len(matrix)] + matrix_shape(matrix[0])
