def intersect_open_intervals(i1, i2):
    """Return [max(low), min(high)] for the intersection of open intervals."""
    low = max(i1[0], i2[0])
    high = min(i1[1], i2[1])
    if low >= high:
        raise ValueError("Empty intersection.")
    return [low, high]
