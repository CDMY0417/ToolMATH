def absolute_to_interval(center: int, radius: int):
    lo = center - radius
    hi = center + radius
    return lo, hi
