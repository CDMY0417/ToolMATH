def integer_points_in_interval_a(lower_bound: int, upper_bound: int):
    if lower_bound > upper_bound:
        return 0
    return upper_bound - lower_bound + 1
