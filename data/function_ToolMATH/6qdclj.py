def integer_points_in_closed_interval_b(start: int, end: int) -> int:
    if start > end:
        return 0
    return end - start + 1
