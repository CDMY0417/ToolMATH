def compute_midpoint(point1: tuple[float, float], point2: tuple[float, float]) -> tuple[float, float]:
    mid_x = (point1[0] + point2[0]) / 2
    mid_y = (point1[1] + point2[1]) / 2
    return (mid_x, mid_y)
