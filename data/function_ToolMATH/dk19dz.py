def next_geometric_terms(b: int, r: int, count: int) -> list:
    return [b * (r**i) for i in range(count)]
