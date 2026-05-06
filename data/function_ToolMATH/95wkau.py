def polynomial_subtraction(poly1: list[float], poly2: list[float]) -> list[float]:
    return [c1 - c2 for c1, c2 in zip(poly1, poly2)]
