def cos_and_sec_squared(angle_radians: float) -> float:
    from math import cos
    return (cos(angle_radians) + 1/cos(angle_radians))**2
