def days_after_start_day(start_day: str, days_after: int) -> str:
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    start_index = days_of_week.index(start_day)
    end_index = (start_index + days_after) % 7
    return days_of_week[end_index]
