def days_ago_to_weekday(current_day: str, days_ago: int):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    current_index = days_of_week.index(current_day)
    past_index = (current_index - days_ago) % 7
    return days_of_week[past_index]
