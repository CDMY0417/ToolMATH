import math

def slope_through_origin_to_point_fraction(x: int, y: int):
    """Return reduced [m,n] for slope y/x."""
    if x == 0:
        raise ValueError("x must be nonzero.")
    g = math.gcd(abs(x), abs(y))
    return [y//g, x//g]
