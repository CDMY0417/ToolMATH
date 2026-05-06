def integer_points_in_open_interval_a(lo: int, hi: int) -> int:
    if lo >= hi:
        return 0
    return hi - lo - 1
