def count_integers_in_interval_b(lower_bound: int, upper_bound: int) -> int:
    return max(0, upper_bound - lower_bound - 1)
