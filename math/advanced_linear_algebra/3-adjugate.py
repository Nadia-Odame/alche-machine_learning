#!/usr/bin/env python3
"""Module for calculating the adjugate matrix."""

cofactor = __import__('2-cofactor').cofactor


def adjugate(matrix):
    """Calculate the adjugate matrix of a square matrix."""
    cofactors = cofactor(matrix)
    n = len(cofactors)

    return [
        [cofactors[j][i] for j in range(n)]
        for i in range(n)
    ]
