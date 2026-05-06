def elapsed_time_on_clock(hours: int, minutes: int, seconds: int):
    total_hours = (hours % 12)
    return total_hours, minutes, seconds
