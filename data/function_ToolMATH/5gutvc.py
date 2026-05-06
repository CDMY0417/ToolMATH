def law_of_sines_a(side_a: float, angle_a: float, angle_b: float) -> float:
    import math
    side_b = side_a * math.sin(math.radians(angle_b)) / math.sin(math.radians(angle_a))
    return side_b
