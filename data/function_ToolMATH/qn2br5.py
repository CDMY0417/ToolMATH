from datetime import datetime, timedelta

def days_after_date(start_date: str, days_to_add: int) -> str:
    date_format = '%Y-%m-%d'
    start = datetime.strptime(start_date, date_format)
    end_date = start + timedelta(days=days_to_add)
    return end_date.strftime(date_format)
