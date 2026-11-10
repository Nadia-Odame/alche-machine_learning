#!/usr/bin/env python3
"""Module that performs matrix multiplication with numpy."""
import numpy as np


def np_matmul(mat1, mat2):
    """Multiply two numpy.ndarrays as matrices.

    Args:
        mat1: a numpy.ndarray.
        mat2: a numpy.ndarray.

    Returns:
        A new numpy.ndarray holding the matrix product.
    """
    return np.matmul(mat1, mat2)
