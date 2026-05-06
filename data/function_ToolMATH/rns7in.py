def revolutions_needed(revolutions: int, distance_from_center_1: float, distance_from_center_2: float) -> int:
    ratio = distance_from_center_1 / distance_from_center_2
    return int(revolutions * ratio)
