def law_of_sines_side_length(side_length: float, angle_opposite_side: float, given_angle: float) -> float:
    import math
    return side_length * math.sin(math.radians(given_angle)) / math.sin(math.radians(angle_opposite_side))
