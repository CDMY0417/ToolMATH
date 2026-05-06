def integer_points_in_interval_c(lower_bound: float, upper_bound: float):
    int_lo = int(-(-lower_bound // 1))  # Equivalent to math.ceil(lower_bound)
    int_hi = int(upper_bound // 1)      # Equivalent to math.floor(upper_bound)
    if int_lo > int_hi:
        return []
    return list(range(int_lo, int_hi + 1))
