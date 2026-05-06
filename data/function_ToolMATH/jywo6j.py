def day_of_week_before_days(start_day: str, days_behind: int) -> str:
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    start_index = days_of_week.index(start_day)
    return days_of_week[(start_index - days_behind) % 7]
