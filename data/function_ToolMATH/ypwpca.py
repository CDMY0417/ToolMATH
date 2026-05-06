def distance_point_to_line(x: float, y: float, A: float, B: float, C: float) -> float:
    return abs(A * x + B * y + C) / ((A**2 + B**2)**0.5)
