def days_in_month(month: str, year: int) -> int:
    import calendar
    month_number = list(calendar.month_name).index(month)
    return calendar.monthrange(year, month_number)[1]
