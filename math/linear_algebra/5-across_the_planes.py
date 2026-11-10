#!/usr/bin/env python3
"""Module that adds two 2D matrices element-wise."""


def add_matrices2D(mat1, mat2):
    """Add two 2D matrices element-wise and return a new matrix.

    Args:
        mat1: a 2D list of ints/floats.
        mat2: a 2D list of ints/floats.

    Returns:
        A new 2D list with the sums, or None if the shapes differ.
    """
    if len(mat1) != len(mat2):
        return None
    if len(mat1[0]) != len(mat2[0]):
        return None
    return [[a + b for a, b in zip(row1, row2)]
            for row1, row2 in zip(mat1, mat2)]
