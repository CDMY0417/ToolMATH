def angle_between_hands_b(hour_angle: float, minute_angle: float) -> float:
    angle = abs(hour_angle - minute_angle)
    return min(angle, 360 - angle)
