def integer_range_sum(start: int, end: int) -> int:
    n = end - start + 1
    return (start + end) * n // 2
