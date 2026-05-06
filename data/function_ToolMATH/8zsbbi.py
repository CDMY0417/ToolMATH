def count_perfect_squares_d(lo: int, hi: int) -> int:
    import math
    lower_bound = math.ceil(math.sqrt(lo))
    upper_bound = math.floor(math.sqrt(hi))
    return max(0, upper_bound - lower_bound + 1)
