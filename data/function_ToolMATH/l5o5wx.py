def days_from_weekday(start_day: str, days_ahead: int) -> str:
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    start_index = days_of_week.index(start_day)
    end_index = (start_index + days_ahead) % 7
    return days_of_week[end_index]
