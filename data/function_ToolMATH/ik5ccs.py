def geometric_series_sum_v(a: float, r: float, n: int):
    return a * (1 - r**n) / (1 - r)
