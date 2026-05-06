def sum_of_geometric_sequence(a: float, r: float, n: int) -> float:
    return a * (1 - r**n) / (1 - r)
