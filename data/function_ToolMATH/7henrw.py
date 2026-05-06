def add_days_to_date(start_day_index: int, days_to_add: int) -> int:
    return (start_day_index + days_to_add) % 7
