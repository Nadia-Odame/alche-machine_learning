#!/usr/bin/env python3
"""A module for calculating the shape of a matrix."""


def matrix_shape(matrix):
    """Calculate the shape of a matrix."""
    if not isinstance(matrix, list):
        return []
    if not matrix:
        return [0]
    return [len(matrix)] + matrix_shape(matrix[0])
