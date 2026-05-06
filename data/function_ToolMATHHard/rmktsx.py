import math

def bd_in_isosceles_with_external_point(s: float, base: float, length: float):
    """Return BD for isosceles triangle with C on perpendicular bisector of AB."""
    if s <= 0 or base <= 0 or length <= 0:
        raise ValueError("Inputs must be positive.")
    # Coordinates: A(0,0), B(base,0), C(base/2, h)
    h_sq = s*s - (base/2.0)**2
    if h_sq <= 0:
        raise ValueError("Invalid triangle dimensions.")
    h = math.sqrt(h_sq)
    # D at (base + d, 0), CD=length
    # (base/2 + d)^2 + h^2 = length^2
    d_sq_term = length*length - h*h
    if d_sq_term < 0:
        raise ValueError("No real solution.")
    d1 = math.sqrt(d_sq_term) - base/2.0
    d2 = -math.sqrt(d_sq_term) - base/2.0
    # choose positive d
    d = d1 if d1 > 0 else d2
    if d <= 0:
        raise ValueError("No positive BD found.")
    return d
