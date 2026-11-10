#!/usr/bin/env python3
"""Module that concatenates two numpy.ndarrays along an axis."""
import numpy as np


def np_cat(mat1, mat2, axis=0):
    """Concatenate two matrices along a specific axis.

    Args:
        mat1: a numpy.ndarray.
        mat2: a numpy.ndarray.
        axis: the axis to concatenate along.

    Returns:
        A new numpy.ndarray.
    """
    return np.concatenate((mat1, mat2), axis=axis)
