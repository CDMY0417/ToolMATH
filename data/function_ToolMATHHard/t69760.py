def perpendicular_slope(m: float):
    """Return negative reciprocal of m."""
    if m == 0:
        return float('inf')
    return -1.0 / m
