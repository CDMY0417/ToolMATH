def days_ago(current_day: str, days_ago: int) -> str:
    days_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    current_index = days_of_week.index(current_day)
    new_index = (current_index - days_ago) % 7
    return days_of_week[new_index]
