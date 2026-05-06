def hour_to_degrees(hour: int, fraction: float) -> float:
    return ((hour % 12) + fraction) * (360 / 12)
