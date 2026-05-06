import math

def law_of_cosines_angle_b(a: float, b: float, c: float) -> float:
    cos_C = (a**2 + b**2 - c**2) / (2 * a * b)
    C_rad = math.acos(cos_C)
    return math.degrees(C_rad)
