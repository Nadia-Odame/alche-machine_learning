#!/usr/bin/env python3
"""Module that returns the transpose of a 2D matrix."""


def matrix_transpose(matrix):
    """Return the transpose of a 2D matrix as a new matrix.

    Args:
        matrix: a non-empty 2D list of numbers.

    Returns:
        A new 2D list with the rows and columns of matrix swapped.
    """
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]
