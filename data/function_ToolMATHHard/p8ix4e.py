import math

def inscribed_circle_radius_three_tangent(a: float, b: float, c: float):
    """Return r from the given formula."""
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("a,b,c must be positive.")
    term = 1.0/a + 1.0/b + 1.0/c + 2.0*math.sqrt(1.0/(a*b) + 1.0/(a*c) + 1.0/(b*c))
    return 1.0 / term
