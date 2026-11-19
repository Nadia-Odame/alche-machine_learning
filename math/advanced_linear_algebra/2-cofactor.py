#!/usr/bin/env python3
"""Module for calculating the cofactor matrix."""

minor = __import__('1-minor').minor


def cofactor(matrix):
    """Calculate the cofactor matrix of a square matrix."""
    minors = minor(matrix)
    n = len(minors)

    return [
        [(-1) ** (i + j) * minors[i][j] for j in range(n)]
        for i in range(n)
    ]
