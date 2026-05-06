def slope_of_line_b(x1: float, y1: float, x2: float, y2: float) -> float:
    return (y2 - y1) / (x2 - x1) if x1 != x2 else float('inf')
