def count_perfect_squares_in_interval(start: int, end: int) -> int:
    from math import isqrt
    return isqrt(end) - (isqrt(start - 1) if start > 0 else 0)
