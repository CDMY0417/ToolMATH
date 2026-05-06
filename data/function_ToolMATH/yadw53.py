def angle_difference_a(angle1: int, angle2: int) -> int:
    diff = abs(angle1 - angle2) % 360
    return min(diff, 360 - diff)
