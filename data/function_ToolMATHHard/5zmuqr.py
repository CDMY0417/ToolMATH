import math

def subtract_fractions(a: int, b: int, c: int, d: int):
    """Return [num, den] for (a/b) - (c/d) in lowest terms."""
    if b == 0 or d == 0:
        raise ValueError("Denominator must be nonzero.")
    num = a * d - c * b
    den = b * d
    g = math.gcd(num, den)
    return [num // g, den // g]
