def solve_for_return_speed(distance: float, speed_to: float, average_speed: float) -> float:
    total_distance = 2 * distance
    time_to = distance / speed_to
    total_time = total_distance / average_speed
    time_from = total_time - time_to
    return distance / time_from
