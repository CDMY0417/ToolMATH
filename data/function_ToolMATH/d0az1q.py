def line_intercept(slope: float, y_intercept: float):
    x_intercept = -y_intercept / slope
    return (x_intercept, 0), (0, y_intercept)
