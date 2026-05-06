def slope_of_line_through_points(x1: float, y1: float, x2: float, y2: float) -> float:
    if x2 == x1:
        return float('inf')  # Undefined slope
    return (y2 - y1) / (x2 - x1)
