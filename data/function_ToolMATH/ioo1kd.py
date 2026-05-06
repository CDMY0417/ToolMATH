def events_in_period(duration_hours: int, interval_minutes: int) -> int:
    events_per_hour = 60 // interval_minutes
    return events_per_hour * duration_hours
