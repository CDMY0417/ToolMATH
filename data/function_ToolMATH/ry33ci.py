def compare_polynomials(poly1: list[float], poly2: list[float]) -> bool:
    return len(poly1) == len(poly2) and all(c1 == c2 for c1, c2 in zip(poly1, poly2))
