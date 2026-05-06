def law_of_cosines_angle(a: float, b: float, c: float) -> float:
    import math
    cos_angle = (a**2 + b**2 - c**2) / (2 * a * b)
    angle_rad = math.acos(cos_angle)
    angle_deg = math.degrees(angle_rad)
    return angle_deg
