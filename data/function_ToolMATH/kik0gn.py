def geometric_series_sum_f(a: float, r: float, n: int) -> float:
    if r == 1:
        return a * n
    return a * (1 - r ** n) / (1 - r)
