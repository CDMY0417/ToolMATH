def time_difference_adjustment(initial_time: int, hours_to_subtract: int) -> int:
    adjusted_time = (initial_time - hours_to_subtract) % 24
    return adjusted_time
