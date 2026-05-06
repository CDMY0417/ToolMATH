def calculate_hourly_chimes(hours: int, chime_pattern: list[int]) -> int:
    total_chimes = 0
    for chimes in chime_pattern:
        total_chimes += chimes * hours
    return total_chimes
