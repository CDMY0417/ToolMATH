def invert_ratio(value: float):
    """Return 1/value."""
    if value == 0:
        raise ValueError("value must be nonzero.")
    return 1.0 / value
