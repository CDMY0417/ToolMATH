def calculate_time_difference_in_minutes(start_hour: int, start_minute: int, end_hour: int, end_minute: int) -> int:
    start_total_minutes = start_hour * 60 + start_minute
    end_total_minutes = end_hour * 60 + end_minute
    return end_total_minutes - start_total_minutes
