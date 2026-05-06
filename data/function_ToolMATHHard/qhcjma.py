import math

def equilateral_area_from_altitude(h: float):
    """Return area from altitude."""
    side = 2*h/math.sqrt(3)
    return math.sqrt(3)/4 * side*side
