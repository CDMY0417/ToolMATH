def days_to_weeks_and_days_a(total_days: int, days_in_week: int):
    weeks = total_days // days_in_week
    remaining_days = total_days % days_in_week
    return weeks, remaining_days
