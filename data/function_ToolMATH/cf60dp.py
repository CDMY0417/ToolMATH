def intersection_with_line_y_eq_x(slope: float, y_intercept: float):
    x = y_intercept / (1 - slope)
    return (x, x)
