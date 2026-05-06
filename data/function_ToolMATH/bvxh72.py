def cosine_in_standard_position(angle: float) -> float:
    import math
    angle = angle % 360
    if 90 < angle <= 270:
        return -math.cos(math.radians(angle - 180))
    else:
        return math.cos(math.radians(angle))
