def add_minutes_to_time(start_hour: int, start_minute: int, minutes_to_add: int) -> (int, int):
    total_minutes = start_hour * 60 + start_minute + minutes_to_add
    new_hour = (total_minutes // 60) % 24
    new_minute = total_minutes % 60
    return new_hour, new_minute
