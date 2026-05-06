def geometric_series_sum_l(a: int, r: int, n: int) -> int:
    return a * (1 - r**n) // (1 - r)
