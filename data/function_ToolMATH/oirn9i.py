def geometric_series_sum_h(a: int, r: int, n: int) -> int:
    return a * (r**n - 1) // (r - 1)
