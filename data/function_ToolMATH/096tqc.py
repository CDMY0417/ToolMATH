def integer_points_in_square_interval(lo: int, hi: int) -> int:
    start = int(lo**0.5) + 1
    end = int(hi**0.5)
    positive_count = max(0, end - start + 1)
    total_count = positive_count * 2
    return total_count
