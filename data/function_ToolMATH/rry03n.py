def days_to_weeks_and_days(days: int) -> tuple:
    weeks = days // 7
    remaining_days = days % 7
    return weeks, remaining_days
