from math import acos, degrees

def law_of_cosines_angle_c(a: float, b: float, c: float) -> float:
    cos_angle = (a**2 + b**2 - c**2) / (2 * a * b)
    return degrees(acos(cos_angle))
