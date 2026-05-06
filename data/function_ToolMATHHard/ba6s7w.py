import math

def radius_from_area_pi_coefficient(A: float):
    """Return radius from area coefficient."""
    if A < 0:
        raise ValueError("A must be nonnegative.")
    return math.sqrt(A)
