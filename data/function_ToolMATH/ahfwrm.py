def hour_hand_angle_a(hour: int, minutes: int) -> float:
    return (hour % 12 + minutes / 60) * (360 / 12)
