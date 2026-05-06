def integer_points_in_closed_interval(lower_bound: int, upper_bound: int) -> int:
    return max(0, upper_bound - lower_bound + 1)
