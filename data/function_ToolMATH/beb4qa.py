def law_of_cosines_to_find_angle(a: float, b: float, c: float) -> float:
    from math import acos, degrees
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
    angle_C = degrees(acos(cos_C))
    return angle_C
