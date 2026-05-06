def calculate_slope_l(point1: tuple[float, float], point2: tuple[float, float]) -> float:
    x1, y1 = point1
    x2, y2 = point2
    if x1 == x2:
        return float('inf')
    return (y2 - y1) / (x2 - x1)
