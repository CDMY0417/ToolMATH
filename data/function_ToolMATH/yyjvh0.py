def cross_x_axis(slope: float, intercept: float) -> float:
    if slope == 0:
        return None
    x = -intercept / slope
    return x
