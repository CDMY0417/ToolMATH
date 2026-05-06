def compute_direction_vector(point1: tuple[float, float], point2: tuple[float, float]) -> tuple[float, float]:
    x1, y1 = point1
    x2, y2 = point2
    return (x2 - x1, y2 - y1)
