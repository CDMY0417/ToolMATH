def interval_intersection(start1: int, end1: int, start2: int, end2: int):
    lo = max(start1, start2)
    hi = min(end1, end2)
    if lo <= hi:
        return (lo, hi)
    else:
        return None
