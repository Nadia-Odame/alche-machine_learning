#!/usr/bin/env python3
"""Module that performs matrix multiplication."""


def mat_mul(mat1, mat2):
    """Multiply two 2D matrices.

    Args:
        mat1: a 2D list of ints/floats.
        mat2: a 2D list of ints/floats.

    Returns:
        A new matrix holding the product, or None if the matrices
        cannot be multiplied.
    """
    if len(mat1[0]) != len(mat2):
        return None
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*mat2)]
            for row in mat1]
