def clock_angle_between_hands(hour: int, minutes: int) -> float:
    degrees_per_hour = 360 / 12
    minutes_degrees = (minutes / 60) * degrees_per_hour
    hour_position = hour % 12 + minutes / 60
    minute_position = minutes / 5
    angle = abs(minute_position - hour_position) * degrees_per_hour
    return min(angle, 360 - angle)
