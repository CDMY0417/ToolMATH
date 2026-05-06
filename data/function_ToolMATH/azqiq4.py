def count_max_leap_years(years: int, leap_interval: int) -> int:
    full_intervals = years // leap_interval
    extra_years = years % leap_interval
    return full_intervals + (1 if extra_years >= 1 else 0)
