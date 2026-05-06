def count_integers_exclusive(lower_bound: int, upper_bound: int) -> int:
    return max(0, upper_bound - lower_bound - 1)
