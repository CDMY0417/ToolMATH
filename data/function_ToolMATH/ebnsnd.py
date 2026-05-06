def perfect_squares_in_range_c(start: int, end: int) -> int:
    from math import ceil, floor
    lower_bound = ceil(start**0.5)
    upper_bound = floor(end**0.5)
    return max(0, upper_bound - lower_bound + 1)
