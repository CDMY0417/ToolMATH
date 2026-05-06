def count_perfect_squares_in_range(start: int, end: int) -> int:
    import math
    lower_bound = math.ceil(math.sqrt(start))
    upper_bound = math.floor(math.sqrt(end))
    return max(0, upper_bound - lower_bound + 1)
