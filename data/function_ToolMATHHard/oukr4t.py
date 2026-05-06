def line_slope_from_general(A: float, B: float):
    """Return slope -A/B for B!=0."""
    if B == 0:
        raise ValueError("B must be nonzero for finite slope.")
    return -A / B
