def point_slope_to_slope_intercept_c(x1: float, y1: float, slope: float) -> str:
    y_intercept = y1 - slope * x1
    return f'y = {slope}x + {y_intercept}'
