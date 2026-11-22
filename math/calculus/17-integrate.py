#!/usr/bin/env python3
"""Calculate the integral of a polynomial."""


def poly_integral(poly, C=0):
    """Return the integral coefficients."""
    if not isinstance(poly, list) or not poly:
        return None
    if type(C) is not int:
        return None
    if not all(type(x) in (int, float) for x in poly):
        return None

    result = [C]
    for i, coefficient in enumerate(poly):
        value = coefficient / (i + 1)
        if value.is_integer():
            value = int(value)
        result.append(value)

    while len(result) > 1 and result[-1] == 0:
        result.pop()

    return result
