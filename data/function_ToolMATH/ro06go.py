def geometric_series_sum_j(a: int, r: int, n: int) -> int:
    return a * (1 - r**n) // (1 - r) if r != 1 else a * n
