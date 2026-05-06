def convert_hours_to_days_and_hours(total_hours: int):
    days = total_hours // 24
    remaining_hours = total_hours % 24
    return days, remaining_hours
