def hour_hand_position(hour: int, minute: int) -> float:
    return (hour % 12) * (360 / 12) + (minute / 60) * (360 / 12)
