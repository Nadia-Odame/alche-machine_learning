#!/usr/bin/env python3
"""Defines a function that transposes a matrix."""
def matrix_transpose(matrix):
    """Return the transpose of a 2D matrix."""
    return [
        [matrix[row][col] for row in range(len(matrix))]
        for col in range(len(matrix[0]))
    ]
