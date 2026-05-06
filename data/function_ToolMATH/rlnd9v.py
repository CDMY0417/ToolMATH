def calculate_trips(total_volume: float, unit_volume: float) -> int:
    return int(total_volume // unit_volume) + (total_volume % unit_volume > 0)
