def angle_between_clock_hands_b(hours: int, minutes: int):
    hour_hand_angle = (hours % 12) * 30 + (minutes / 60) * 30
    minute_hand_angle = (minutes / 60) * 360
    angle = abs(hour_hand_angle - minute_hand_angle)
    return min(angle, 360 - angle)
