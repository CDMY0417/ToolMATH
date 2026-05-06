def hour_hand_position_relative_to_mark(hour: float, minutes: float) -> float:
    return hour * 30 + (minutes / 60) * 30
