#!/usr/bin/env python3
"""Module that adds two arrays element-wise."""


def add_arrays(arr1, arr2):
    """Add two arrays element-wise and return the result as a new list.

    Args:
        arr1: a list of ints/floats.
        arr2: a list of ints/floats.

    Returns:
        A new list with the sums, or None if the arrays differ in length.
    """
    if len(arr1) != len(arr2):
        return None
    return [a + b for a, b in zip(arr1, arr2)]
