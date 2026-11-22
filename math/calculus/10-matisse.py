#!/usr/bin/env python3
"""Calculate the derivative of a polynomial."""


def poly_derivative(poly):
    """Return the derivative coefficients."""
    if not isinstance(poly, list) or not poly:
        return None
    if not all(type(x) in (int, float) for x in poly):
        return None
    if len(poly) == 1:
        return [0]
    return [i * poly[i] for i in range(1, len(poly))]
