def average_speed_b(distance: float, speed_to: float, speed_from: float) -> float:
    total_distance = 2 * distance
    time_to = distance / speed_to
    time_from = distance / speed_from
    total_time = time_to + time_from
    return total_distance / total_time
