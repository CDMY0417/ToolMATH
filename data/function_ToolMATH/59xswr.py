def day_of_week_after_days_a(start_day: str, days_ahead: int):
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    start_index = days_of_week.index(start_day)
    return days_of_week[(start_index + days_ahead) % 7]
