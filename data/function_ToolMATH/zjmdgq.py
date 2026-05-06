def linear_equation_from_points(point1: tuple[float, float], point2: tuple[float, float]) -> tuple[float, float]:
    x1, y1 = point1
    x2, y2 = point2
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1
    return m, b
