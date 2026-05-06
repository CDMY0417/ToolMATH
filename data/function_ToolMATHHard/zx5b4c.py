from fractions import Fraction

def reciprocal_exponent(n: int):
    """Return 1/n as a Fraction."""
    if n == 0:
        raise ValueError("n must be nonzero.")
    return Fraction(1, n)
