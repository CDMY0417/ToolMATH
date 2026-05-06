def count_perfect_cubes_in_range_a(start: int, end: int) -> int:
    from math import ceil, floor
    lo = ceil(start**(1/3))
    hi = floor(end**(1/3))
    return max(0, hi - lo + 1)
