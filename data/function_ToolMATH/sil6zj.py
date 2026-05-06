def midpoint_of_two_points_d(point1: tuple[float, float], point2: tuple[float, float]) -> tuple[float, float]:
    x1, y1 = point1
    x2, y2 = point2
    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2
    return mx, my
