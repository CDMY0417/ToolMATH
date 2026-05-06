def calculate_difference_between_angles(angle1: float, angle2: float) -> float:
    difference = abs(angle1 - angle2) % 360
    return min(difference, 360 - difference)
