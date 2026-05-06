import math

def distance_between_points(x1: float, y1: float, x2: float, y2: float):
    """Return Euclidean distance."""
    return math.hypot(x2 - x1, y2 - y1)
