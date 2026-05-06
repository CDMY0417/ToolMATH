def subtract_polynomials_f(poly1: list[float], poly2: list[float]) -> list[float]:
    length = max(len(poly1), len(poly2))
    p1 = poly1 + [0] * (length - len(poly1))
    p2 = poly2 + [0] * (length - len(poly2))
    return [a - b for a, b in zip(p1, p2)]
