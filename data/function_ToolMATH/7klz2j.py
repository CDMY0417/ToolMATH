def angle_between_clock_hands_a(hour: int, minute: int) -> float:
    hour_angle = (hour % 12) * 30 + (minute / 60) * 30
    minute_angle = minute * 6
    angle = abs(hour_angle - minute_angle)
    return min(angle, 360 - angle)
