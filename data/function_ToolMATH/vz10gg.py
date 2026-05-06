def law_of_cosines_b(a: float, b: float, angle_c: float) -> float:
    from math import cos, radians
    return (a**2 + b**2 - 2 * a * b * cos(radians(angle_c)))**0.5
