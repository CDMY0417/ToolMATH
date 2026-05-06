def law_of_sines(angle_A: float, angle_B: float, side_a: float) -> float:
    import math
    side_b = (side_a * math.sin(math.radians(angle_B))) / math.sin(math.radians(angle_A))
    return side_b
