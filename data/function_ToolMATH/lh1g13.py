def sum_of_geometric_series(a0: float, r: float, n: int) -> float:
    return a0 * (1 - r**n) / (1 - r)
