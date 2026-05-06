def angle_bisector_theorem(total_length: float, ratio_a: float, ratio_b: float) -> tuple:
    length_a = total_length * ratio_a / (ratio_a + ratio_b)
    length_b = total_length * ratio_b / (ratio_a + ratio_b)
    return length_a, length_b
