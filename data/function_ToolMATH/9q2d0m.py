def geometric_series_sum_a(a: float, r: float, n: int) -> float:
    return a * (1 - r**n) / (1 - r)
