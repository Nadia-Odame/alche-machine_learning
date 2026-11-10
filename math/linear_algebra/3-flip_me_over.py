#!/usr/bin/env python3
"""Defines a function that calculates the shape of a matrix."""


def matrix_shape(matrix):
    """Return the shape of a matrix."""
    if isinstance(matrix, list):
        return [len(matrix)] + matrix_shape(matrix[0]) if matrix else [0]
    return []
