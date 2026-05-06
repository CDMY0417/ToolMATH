def point_slope_to_slope_intercept(m: float, x1: float, y1: float) -> tuple:
    b = y1 - m * x1
    return m, b
