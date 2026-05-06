def linear_fraction_excluded_value(a: float, b: float, c: float, d: float):
    """Return a/c, the excluded range value for a proper linear fractional map."""
    if c == 0:
        raise ValueError("c must be nonzero.")
    return a / c
