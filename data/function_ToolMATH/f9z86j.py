def hour_hand_position_a(hours: int, minutes: int) -> float:
    hour_fraction = hours + (minutes / 60)
    return (hour_fraction / 12) * 360
