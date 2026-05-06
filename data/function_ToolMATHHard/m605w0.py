import math

def quadratic_real_and_imag_parts(a: float, b: float, c: float):
    """Return (real_part, imag_part) for complex roots."""
    if a == 0:
        raise ValueError("a must be nonzero.")
    disc = b*b - 4.0*a*c
    if disc >= 0:
        raise ValueError("Discriminant is nonnegative.")
    real_part = -b / (2.0*a)
    imag_part = math.sqrt(-disc) / (2.0*a)
    return (real_part, imag_part)
