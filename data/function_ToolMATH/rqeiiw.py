def area_of_triangle_m(a: float, b: float, angle_degrees: float) -> float:
    import math
    return 0.5 * a * b * math.sin(math.radians(angle_degrees))
