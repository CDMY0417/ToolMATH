def integer_points_in_exclusive_interval(lo: int, hi: int) -> int:
    if lo >= hi:
        return 0
    return sum(range(lo + 1, hi))
