def geometric_series_sum(n: int, r: int, a: int):
    if r == 1:
        return n * a
    else:
        return a * (1 - r ** n) // (1 - r)
