def distance_between_points_x(point1: tuple[float, float, float], point2: tuple[float, float, float]) -> float:
    x1, y1, z1 = point1
    x2, y2, z2 = point2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
