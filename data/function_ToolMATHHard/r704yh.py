def sum_abs_less_than_interval(a: float, b: float, L: float):
    """Return open interval [low, high] for |x-a|+|x-b| < L."""
    if L <= abs(a - b):
        raise ValueError("No solution interval.")
    low = (a + b - L) / 2.0
    high = (a + b + L) / 2.0
    return [low, high]
