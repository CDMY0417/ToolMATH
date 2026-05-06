def compute_tours_per_day(start_hour: int, end_hour: int, interval_minutes: int):
    total_hours = end_hour - start_hour
    tours_per_hour = 60 // interval_minutes
    total_tours = total_hours * tours_per_hour + 1
    return total_tours
