#!/usr/bin/env python3
"""Module that performs element-wise arithmetic on numpy.ndarrays."""


def np_elementwise(mat1, mat2):
    """Add, subtract, multiply and divide two matrices element-wise.

    Args:
        mat1: a numpy.ndarray.
        mat2: a numpy.ndarray or a scalar.

    Returns:
        A tuple with the element-wise sum, difference, product and
        quotient, in that order.
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
