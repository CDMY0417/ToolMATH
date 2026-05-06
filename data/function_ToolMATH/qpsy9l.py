def convert_minutes_to_time(minutes: int) -> str:
    total_minutes = 60 * 12 + minutes  # Start counting from noon
    hours = (total_minutes // 60) % 24
    mins = total_minutes % 60
    return f'{hours:02}:{mins:02}'
