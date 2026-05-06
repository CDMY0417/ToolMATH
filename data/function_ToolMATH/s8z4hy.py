def days_with_start_interval(start_day: int, interval: int, total_days: int):
    return [day for day in range(start_day, total_days + 1, interval)]
