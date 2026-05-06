def find_x_intercept(point: tuple, slope: float) -> tuple:
    x, y = point
    x_intercept = x - (y / slope)
    return (x_intercept, 0)
