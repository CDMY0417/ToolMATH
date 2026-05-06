def distance_between_points_a(x1: float, y1: float, x2: float, y2: float) -> float:
    from math import sqrt
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
