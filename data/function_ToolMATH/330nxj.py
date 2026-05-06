def calculate_reading_time(pages: int, pages_per_set: int, time_per_set: int) -> int:
    sets = pages // pages_per_set
    return sets * time_per_set
