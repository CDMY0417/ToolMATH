import math

def ratio_from_quadratic_relation(k: float):
    """Return |(a+b)/(a-b)| for a^2+b^2 = k*ab."""
    if k <= 2:
        raise ValueError("k must be > 2 for real solutions.")
    return math.sqrt((k + 2) / (k - 2))
