#!/usr/bin/env python3
"""Module for determining the definiteness of a matrix."""

import numpy as np


def definiteness(matrix):
    """Calculate the definiteness of a matrix."""
    if not isinstance(matrix, np.ndarray):
        raise TypeError("matrix must be a numpy.ndarray")

    if matrix.ndim != 2 or matrix.size == 0:
        return None

    if matrix.shape[0] != matrix.shape[1]:
        return None

    if not np.array_equal(matrix, matrix.T):
        return None

    eigenvalues = np.linalg.eigvalsh(matrix)

    tolerance = (np.finfo(float).eps * len(eigenvalues)
                 * np.max(np.abs(eigenvalues)))

    eigenvalues[np.abs(eigenvalues) <= tolerance] = 0

    if np.all(eigenvalues > 0):
        return "Positive definite"

    if np.all(eigenvalues < 0):
        return "Negative definite"

    if np.all(eigenvalues >= 0):
        return "Positive semi-definite"

    if np.all(eigenvalues <= 0):
        return "Negative semi-definite"

    if np.any(eigenvalues > 0) and np.any(eigenvalues < 0):
        return "Indefinite"

    return None
