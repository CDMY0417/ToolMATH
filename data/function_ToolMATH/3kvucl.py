def secant_of_angle(angle_degrees: float) -> float:
    import math
    rad = math.radians(angle_degrees)
    return 1 / math.cos(rad)
