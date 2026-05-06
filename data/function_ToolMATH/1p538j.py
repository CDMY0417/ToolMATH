def midpoint_coordinates(point1: tuple[float, float], point2: tuple[float, float]) -> tuple[float, float]:
    x1, y1 = point1
    x2, y2 = point2
    return ((x1 + x2) / 2, (y1 + y2) / 2)
