def triangle_area_shoelace(x1: float, y1: float, x2: float, y2: float, x3: float, y3: float) -> float:
    return 0.5 * abs(x1*y2 + x2*y3 + x3*y1 - y1*x2 - y2*x3 - y3*x1)
