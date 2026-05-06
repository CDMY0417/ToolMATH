def add_minutes_to_time_a(hours: int, minutes: int, additional_minutes: int) -> str:
    total_minutes = hours * 60 + minutes + additional_minutes
    new_hours = (total_minutes // 60) % 24
    new_minutes = total_minutes % 60
    return f"{new_hours:02}:{new_minutes:02}"
