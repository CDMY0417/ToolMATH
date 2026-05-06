def integer_range_for_closest_sqrt(k: int) -> tuple:
    start = k**2 - k + 1
    end = k**2 + k
    return (start, end)
