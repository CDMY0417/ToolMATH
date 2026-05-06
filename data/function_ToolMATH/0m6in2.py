def day_of_week_after_days(start_day: str, days: int) -> str:
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    start_index = days_of_week.index(start_day)
    end_index = (start_index + days) % 7
    return days_of_week[end_index]
