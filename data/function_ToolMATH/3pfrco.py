def cosine_law_side_length(side_a: float, side_b: float, angle_c: float) -> float:
    from math import cos
    return (side_a**2 + side_b**2 - 2 * side_a * side_b * cos(angle_c))**0.5
