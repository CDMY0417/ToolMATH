def time_to_travel_miles(miles: int, speed_mph: int) -> int:
    hours = miles / speed_mph
    return int(hours * 60)
