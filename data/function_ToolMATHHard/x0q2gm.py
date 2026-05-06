import math

def telescoping_product_one_minus_reciprocal(N: int):
    """Return [1, N] for N>=2."""
    if N < 2:
        raise ValueError("N must be >= 2.")
    return [1, N]
