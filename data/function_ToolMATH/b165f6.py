def law_of_cosines_angle_d(side_a: float, side_b: float, side_c: float) -> float:
    import math
    cos_angle = (side_a**2 + side_b**2 - side_c**2) / (2 * side_a * side_b)
    return math.acos(cos_angle) * (180 / math.pi)
