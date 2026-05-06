def angle_subtraction_sin(a: float, b: float) -> float:
    import math
    return math.sin(math.radians(a)) * math.cos(math.radians(b)) - math.cos(math.radians(a)) * math.sin(math.radians(b))
