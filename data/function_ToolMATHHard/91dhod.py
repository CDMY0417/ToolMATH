import math

def max_C_for_quadratic_inequality(d: float):
    """Return C_max = sqrt(2d)."""
    if d < 0:
        raise ValueError("d must be nonnegative.")
    return math.sqrt(2.0 * d)
