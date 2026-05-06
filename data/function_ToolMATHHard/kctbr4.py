import math

def circle_area_pi_coefficient_from_diameter_endpoints(x1: float, y1: float, x2: float, y2: float):
    """Return k where area = k*pi."""
    dx = x2 - x1
    dy = y2 - y1
    diameter = math.hypot(dx, dy)
    r = diameter / 2.0
    return r * r
