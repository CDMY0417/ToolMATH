def ratio_of_two_numbers_b(a: float, b: float):
    """Return a/b."""
    if b == 0:
        raise ValueError("b must be nonzero.")
    return a / b
