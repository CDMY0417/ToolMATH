def first_multiple_above(n: int, lower_bound: int) -> int:
    m = (lower_bound // n + 1) * n
    return m
