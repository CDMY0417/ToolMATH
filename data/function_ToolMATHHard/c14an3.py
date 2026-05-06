def sum_squares_from_cubic_coeffs(a: float, b: float, c: float, d: float):
    """Return sum of squares of roots using Vieta."""
    if a == 0:
        raise ValueError("Leading coefficient must be nonzero.")
    s1 = -b / a
    s2 = c / a
    return s1*s1 - 2*s2
