def ratio_of_two_numbers_a(u: float, v: float):
    """Return v/u."""
    if u == 0:
        raise ValueError("u must be nonzero.")
    return v / u
