def angle_from_linear_relation(offset: float, multiple: float, k_range: list[int]):
    angles = [(multiple * k + offset) % 360 for k in k_range]
    return [angle for angle in angles if 0 < angle < 90]
