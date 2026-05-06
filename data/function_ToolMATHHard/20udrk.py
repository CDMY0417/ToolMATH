def reciprocal_fraction(n: int):
    """Return [1, n] for nonzero integer n."""
    if n == 0:
        raise ValueError("n must be nonzero.")
    return [1, n]
