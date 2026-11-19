#!/usr/bin/env python3
"""Module for calculating the minor matrix."""

determinant = __import__('0-determinant').determinant


def minor(matrix):
    """Calculate the minor matrix of a square matrix."""
    if not isinstance(matrix, list) or not matrix:
        raise TypeError("matrix must be a list of lists")

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    n = len(matrix)

    if any(len(row) != n for row in matrix):
        raise ValueError("matrix must be a non-empty square matrix")

    if n == 1:
        return [[1]]

    result = []

    for i in range(n):
        row_minors = []

        for j in range(n):
            submatrix = [
                row[:j] + row[j + 1:]
                for k, row in enumerate(matrix) if k != i
            ]

            row_minors.append(determinant(submatrix))

        result.append(row_minors)

    return result
