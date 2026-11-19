#!/usr/bin/env python3
"""Module for calculating the inverse of a matrix."""

determinant = __import__('0-determinant').determinant
adjugate = __import__('3-adjugate').adjugate


def inverse(matrix):
    """Calculate the inverse of a square matrix."""
    adj = adjugate(matrix)
    det = determinant(matrix)

    if det == 0:
        return None

    return [
        [element / det for element in row]
        for row in adj
    ]
