def hour_hand_angle(hours: int, minutes: int) -> float:
    return (hours % 12) * 30 + (minutes / 60) * 30
