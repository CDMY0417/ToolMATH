def cosecant_of_angle(angle: float) -> float:
    from math import sin, radians
    sin_value = sin(radians(angle))
    return 1 / sin_value if sin_value != 0 else float('inf')
