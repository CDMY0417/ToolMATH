def perfect_squares_in_range_d(lo: int, hi: int) -> int:
    from math import ceil, floor
    smallest_square = ceil(lo ** 0.5)
    largest_square = floor(hi ** 0.5)
    return max(0, largest_square - smallest_square + 1)
