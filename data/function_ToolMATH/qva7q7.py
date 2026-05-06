def sum_alternating_series(n: int) -> int:
    return sum((-1) ** i for i in range(n))
