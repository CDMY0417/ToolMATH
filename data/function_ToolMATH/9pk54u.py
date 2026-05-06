def cosine_of_angle_i(angle: float, in_degrees: bool = False) -> float:
    import math
    if in_degrees:
        angle = math.radians(angle)
    return math.cos(angle)
