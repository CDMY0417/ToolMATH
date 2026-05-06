def angle_between_clock_hands(hour: int, minute: int) -> float:
    position_hour = (hour % 12) * 30 + (minute / 60) * 30
    position_minute = minute * 6
    angle = abs(position_hour - position_minute)
    return min(angle, 360 - angle)
