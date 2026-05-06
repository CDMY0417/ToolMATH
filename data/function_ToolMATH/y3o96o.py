def sum_of_geometric_series_a(a: int, r: int, n: int) -> int:
    return (a * r**n - a) // (r - 1)
