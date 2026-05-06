def sum_cubes_from_cubic_coeffs(a: float, b: float, c: float, d: float):
    """Return sum of cubes of roots using Vieta and Newton sums."""
    if a == 0:
        raise ValueError("Leading coefficient must be nonzero.")
    s1 = -b / a
    s2 = c / a
    s3 = -d / a
    return s1**3 - 3*s1*s2 + 3*s3
