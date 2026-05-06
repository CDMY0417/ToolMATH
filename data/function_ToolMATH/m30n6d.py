def law_of_cosines(side_a: float, side_b: float, angle_c_degrees: float) -> float:
    import math
    angle_c_radians = math.radians(angle_c_degrees)
    side_c = math.sqrt(side_a**2 + side_b**2 - 2 * side_a * side_b * math.cos(angle_c_radians))
    return side_c
