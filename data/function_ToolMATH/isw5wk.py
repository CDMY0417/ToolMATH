def integer_points_in_open_interval(lower_bound: float, upper_bound: float) -> int:
    lo_ceil = int(lower_bound) + 1 if lower_bound % 1 != 0 else int(lower_bound)
    hi_floor = int(upper_bound)
    return max(0, hi_floor - lo_ceil + 1)
