def calculate_perp_b_value(x1: float, y1: float, slope: float) -> float:
    perp_slope = -1 / slope
    b = y1 - perp_slope * x1
    return b
