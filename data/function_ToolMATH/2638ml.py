def angle_between_hour_and_minute_hand(hour: int, minute: int) -> float:
    hour_angle = (hour % 12) * 30 + (minute * 0.5)
    minute_angle = minute * 6
    angle = abs(hour_angle - minute_angle)
    return min(angle, 360 - angle)
