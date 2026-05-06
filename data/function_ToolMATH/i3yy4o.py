def shift_graph(slope: float, y_intercept: float, x_shift: float, y_shift: float) -> tuple:
    new_y_intercept = y_intercept + y_shift - slope * x_shift
    return slope, new_y_intercept
