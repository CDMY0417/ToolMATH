def calculate_missing_angle(angle1: int, angle2_plus_difference: int) -> int:
    total = 180
    angle2 = total - (angle1 + angle2_plus_difference)
    return angle2
