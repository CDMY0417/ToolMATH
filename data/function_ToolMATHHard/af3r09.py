def recurrence_ratio_periodic(a1: float, a2: float, n: int):
    """Return a_n for recurrence a_n = a_{n-1}/a_{n-2}."""
    if n == 1:
        return a1
    if n == 2:
        return a2
    seq = [None, a1, a2, a2/a1, 1/a1, 1/a2, a1/a2]
    period = 6
    idx = (n - 1) % period + 1
    return seq[idx]
